#!/usr/bin/env python3
"""Normalize raw exam-prep LLM outputs into schema-shaped draft bank files."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
EXAM_PREP = ROOT / "docs/Pilot1/aip-c01/exam-prep"
SPEC_PATH = EXAM_PREP / "question-bank-specification.md"
SOURCE_CATALOG = EXAM_PREP / "source-catalog.json"

REQUIRED_FIELDS = [
    "item_id",
    "status",
    "official_exam_code",
    "exam_domain",
    "exam_task",
    "exam_skill",
    "learning_unit",
    "accelerated_day",
    "knowledge_type",
    "question_format",
    "difficulty",
    "cognitive_demand",
    "stem",
    "options",
    "correct_answer",
    "rationale_correct",
    "rationale_distractors",
    "misconception_tags",
    "source_trace",
    "remediation_target",
    "estimated_time_seconds",
    "last_reviewed",
]


@dataclass
class NormalizedItem:
    item: dict[str, Any]
    raw_source: str
    raw_index: int
    warnings: list[str]


def read_fenced_json_after_marker(text: str, marker: str) -> Any | None:
    start = text.find(marker)
    if start == -1:
        return None

    fenced = re.search(r"```json\n(.*?)\n```", text[start:], re.DOTALL)
    if not fenced:
        return None

    return json.loads(fenced.group(1))


def extract_output_text(raw_file_text: str) -> str:
    raw_json = read_fenced_json_after_marker(raw_file_text, "## Raw Response JSON")
    if isinstance(raw_json, dict):
        chunks: list[str] = []
        for output in raw_json.get("output", []):
            for content in output.get("content", []):
                if content.get("type") == "output_text":
                    chunks.append(content.get("text", ""))
        if chunks:
            return "\n".join(chunks)

    text_marker = raw_file_text.find("## Raw Response Text")
    if text_marker != -1:
        fenced = re.search(r"```(?:json|text)?\n(.*?)\n```", raw_file_text[text_marker:], re.DOTALL)
        if fenced:
            return fenced.group(1)

    raise ValueError("could not find LLM output text")


def parse_first_json_array(text: str) -> list[dict[str, Any]]:
    cleaned = text.strip()
    if cleaned.startswith("```"):
        cleaned = re.sub(r"^```(?:json|text)?\s*", "", cleaned)
        cleaned = re.sub(r"\s*```$", "", cleaned)

    decoder = json.JSONDecoder()
    for match in re.finditer(r"\[", cleaned):
        try:
            value, _ = decoder.raw_decode(cleaned[match.start() :])
        except json.JSONDecodeError:
            continue

        if isinstance(value, list):
            if not all(isinstance(item, dict) for item in value):
                raise ValueError("decoded JSON array contains non-object entries")
            return value

    raise ValueError("could not decode first JSON array")


def parse_metadata(raw_file_text: str) -> dict[str, Any]:
    metadata = read_fenced_json_after_marker(raw_file_text, "## Metadata")
    if isinstance(metadata, dict):
        return metadata
    return {}


def parse_topic_brief(brief_path: Path) -> dict[str, str]:
    text = brief_path.read_text(encoding="utf-8")
    values: dict[str, str] = {}

    table_map = {
        "Curriculum order": "curriculum_order",
        "Accelerated day": "accelerated_day",
        "Topic": "topic",
        "Knowledge category": "knowledge_category",
        "Knowledge type": "knowledge_type",
    }
    for label, key in table_map.items():
        match = re.search(rf"\| {re.escape(label)} \| (.*?) \|", text)
        if match:
            values[key] = match.group(1).strip()

    for key in ["exam_domain", "exam_task", "exam_skill", "secondary_exam_skills"]:
        match = re.search(rf"- `{key}`: (.*)", text)
        if match:
            values[key] = match.group(1).strip()

    source_labels = {
        "Study guide": "study_guide",
        "Focused artifact": "focused_artifact",
        "Answer guidance": "answer_guidance",
    }
    for label, key in source_labels.items():
        match = re.search(rf"^- {re.escape(label)}: `(?P<path>.+?)`$", text, re.MULTILINE)
        if match:
            values[key] = match.group("path").strip()

    sources: list[str] = []
    in_sources = False
    for line in text.splitlines():
        if line.startswith("## Teaching And Remediation Sources"):
            in_sources = True
            continue
        if in_sources and line.startswith("## "):
            break
        if in_sources and line.startswith("- "):
            sources.append(line[2:].strip())
    values["teaching_sources"] = "\n".join(sources)
    return values


def raw_files_for_day(day: int) -> list[Path]:
    raw_dir = EXAM_PREP / f"raw/day-{day:02d}"
    pattern = f"*openai-*-day-{day:02d}-order*.md"
    return sorted(
        path
        for path in raw_dir.glob(pattern)
        if "dry-run" not in path.name and "balanced" not in path.name
    )


def topic_briefs_for_day(day: int) -> dict[str, dict[str, str]]:
    briefs_dir = EXAM_PREP / f"topic-briefs/day-{day:02d}"
    briefs: dict[str, dict[str, str]] = {}
    for brief_path in sorted(briefs_dir.glob(f"day{day:02d}-order*-topic-brief.md")):
        values = parse_topic_brief(brief_path)
        order = values.get("curriculum_order")
        if order:
            briefs[order] = values
    return briefs


def normalize_remediation_target(value: Any) -> str:
    if isinstance(value, list):
        value = "; ".join(str(part) for part in value)
    if not isinstance(value, str):
        return "MISSING"

    stripped = value.strip()
    prefix_match = re.match(r"^(study_guide|focused_artifact|answer_guidance|source):\s*(.*)$", stripped)
    if prefix_match:
        stripped = prefix_match.group(2).strip()
    return stripped or "MISSING"


def normalize_source_trace(raw: dict[str, Any]) -> str:
    value = raw.get("source_trace") or raw.get("source_trace_needed")
    if isinstance(value, list):
        return "\n".join(f"- {entry}" for entry in value)
    if isinstance(value, str) and value.strip():
        return value.strip()
    return "MISSING"


def infer_question_format(raw_item: dict[str, Any], options: list[str]) -> str:
    value = str(raw_item.get("question_format") or "").strip()
    if value:
        return value
    correct = raw_item.get("correct_answer")
    if isinstance(correct, list) and len(correct) > 1:
        return "multiple-response"
    if isinstance(correct, str) and ";" in correct:
        return "multiple-response"
    if len(options) > 4:
        return "multiple-response"
    return "multiple-choice"


def infer_cognitive_demand(stem: str, raw_item: dict[str, Any]) -> str:
    value = str(raw_item.get("cognitive_demand") or "").strip()
    if value:
        return value
    lowered = stem.lower()
    if "troubleshoot" in lowered or "root cause" in lowered or "most likely" in lowered:
        return "diagnose"
    if "optimiz" in lowered or "latency" in lowered or "cost" in lowered:
        return "optimize"
    if "configure" in lowered or "implement" in lowered:
        return "configure"
    if "compare" in lowered or "tradeoff" in lowered:
        return "compare"
    return "judge"


def normalize_difficulty(raw_item: dict[str, Any]) -> str:
    value = str(raw_item.get("difficulty") or "").strip().lower()
    if value in {"medium", "hard", "exam-plus"}:
        return value
    risk = str(raw_item.get("defensibility_risk") or "").strip().lower()
    return "exam-plus" if risk == "medium" else "hard"


def load_source_catalog_index(day: int) -> dict[str, dict[str, str]]:
    if not SOURCE_CATALOG.exists():
        return {}
    data = json.loads(SOURCE_CATALOG.read_text(encoding="utf-8"))
    sources = data.get("sources", {})
    result: dict[str, dict[str, str]] = {}
    for order, mapping in data.get("topic_mappings", {}).items():
        if not order.startswith(f"Day{day:02d}-"):
            continue
        for source_id in mapping.get("allowed_source_ids", []):
            source = sources.get(source_id, {})
            source_value = str(source.get("source", ""))
            if source_value:
                result[f"{order}\n{source_value}"] = {
                    "allowed_source_id": str(source_id),
                    "source": source_value,
                    "source_type": str(source.get("source_type", "")),
                }
    return result


def source_catalog_entry(
    source_index: dict[str, dict[str, str]],
    order: str,
    source_trace: str,
) -> dict[str, str] | None:
    return source_index.get(f"{order}\n{source_trace}")


def normalize_curriculum_order(value: str, day: int) -> str:
    order = value.strip()
    if order.startswith("order"):
        order = f"Day{day:02d}-{order}"
    match = re.match(rf"^(Day{day:02d}-order\d{{3}})(?:-top-up-\d+)?$", order)
    if match:
        return match.group(1)
    return order


def lean_atomic_claim(raw_item: dict[str, Any], source_trace: str) -> list[dict[str, str]]:
    existing = normalize_atomic_claims(raw_item.get("atomic_claims"))
    if existing:
        return existing
    evidence_span = str(raw_item.get("evidence_span") or "").strip()
    if not evidence_span:
        return []
    claim = str(
        raw_item.get("defensible_correct_answer")
        or raw_item.get("rationale_correct")
        or raw_item.get("correct_answer")
        or ""
    ).strip()
    return [
        {
            "claim": claim,
            "source": source_trace,
            "evidence_span": evidence_span,
        }
    ]


def normalize_options(value: Any) -> list[str]:
    if isinstance(value, list):
        return [str(option).strip() for option in value if str(option).strip()]
    if isinstance(value, dict):
        return [f"{key}. {val}" for key, val in value.items()]
    if isinstance(value, str) and value.strip():
        return [value.strip()]
    return []


def normalize_atomic_claims(value: Any) -> list[dict[str, str]]:
    if not isinstance(value, list):
        return []
    claims: list[dict[str, str]] = []
    for claim in value:
        if not isinstance(claim, dict):
            continue
        claims.append(
            {
                "claim": str(claim.get("claim", "")).strip(),
                "source": str(claim.get("source", "")).strip(),
                "evidence_span": str(claim.get("evidence_span", "")).strip(),
            }
        )
    return claims


def normalize_item(
    raw_item: dict[str, Any],
    *,
    day: int,
    sequence: int,
    raw_source: str,
    raw_index: int,
    metadata: dict[str, Any],
    brief: dict[str, str] | None,
    source_index: dict[str, dict[str, str]],
) -> NormalizedItem:
    warnings: list[str] = []
    item: dict[str, Any] = {}
    canonical = brief or {}

    def raw_or_canonical(key: str, default: str = "MISSING") -> str:
        value = raw_item.get(key)
        if isinstance(value, str) and value.strip():
            if canonical.get(key) and value.strip() != canonical[key]:
                warnings.append(f"{key} differs from topic brief")
            return value.strip()
        if canonical.get(key):
            warnings.append(f"{key} filled from topic brief")
            return canonical[key]
        warnings.append(f"{key} missing")
        return default

    item["item_id"] = f"P1-AIP-D{day}-N{sequence:03d}"
    item["status"] = "draft"
    item["official_exam_code"] = raw_item.get("official_exam_code") or "AIP-C01"
    item["exam_domain"] = raw_or_canonical("exam_domain")
    item["exam_task"] = raw_or_canonical("exam_task")
    item["exam_skill"] = raw_or_canonical("exam_skill")

    local_focus = raw_item.get("exam_skill_local")
    if isinstance(local_focus, str) and local_focus.strip():
        item["exam_skill_local"] = local_focus.strip()

    item["secondary_exam_skills"] = raw_or_canonical("secondary_exam_skills", "None.")
    item["learning_unit"] = raw_item.get("learning_unit") or raw_or_canonical("curriculum_order")
    item["accelerated_day"] = raw_item.get("accelerated_day") or f"Day {day}"
    item["topic"] = raw_or_canonical("topic")
    item["knowledge_category"] = raw_or_canonical("knowledge_category")
    item["knowledge_type"] = raw_or_canonical("knowledge_type")
    item["stem"] = str(raw_item.get("stem") or "MISSING").strip()
    item["options"] = normalize_options(raw_item.get("options"))
    item["question_format"] = infer_question_format(raw_item, item["options"])
    item["difficulty"] = normalize_difficulty(raw_item)
    item["cognitive_demand"] = infer_cognitive_demand(item["stem"], raw_item)
    item["correct_answer"] = raw_item.get("correct_answer", "MISSING")
    item["rationale_correct"] = str(
        raw_item.get("rationale_correct")
        or raw_item.get("defensible_correct_answer")
        or "MISSING"
    ).strip()
    item["rationale_distractors"] = raw_item.get("rationale_distractors", "MISSING")
    item["misconception_tags"] = raw_item.get("misconception_tags", [])
    item["source_trace"] = normalize_source_trace(raw_item)
    item["source_trace_status"] = "needs-source-check"
    catalog_entry = source_catalog_entry(source_index, item["learning_unit"], item["source_trace"])
    item["source_contract_version"] = str(raw_item.get("source_contract_version") or "").strip()
    if not item["source_contract_version"] and catalog_entry:
        item["source_contract_version"] = "source-grounded-v1"
        warnings.append("source_contract_version filled from source catalog")
    item["allowed_source_id"] = str(raw_item.get("allowed_source_id") or "").strip()
    if not item["allowed_source_id"] and catalog_entry:
        item["allowed_source_id"] = catalog_entry["allowed_source_id"]
        warnings.append("allowed_source_id filled from source catalog")
    item["atomic_claims"] = lean_atomic_claim(raw_item, item["source_trace"])
    if item["source_contract_version"] == "source-grounded-v1":
        if not item["allowed_source_id"]:
            warnings.append("allowed_source_id missing for source-grounded-v1")
        if not item["atomic_claims"]:
            warnings.append("atomic_claims missing for source-grounded-v1")
        for index, claim in enumerate(item["atomic_claims"], start=1):
            if not claim["claim"] or not claim["source"] or not claim["evidence_span"]:
                warnings.append(f"atomic_claims[{index}] missing claim/source/evidence_span")
    remediation_value = raw_item.get("remediation_target")
    if not remediation_value and canonical.get("answer_guidance"):
        remediation_value = canonical["answer_guidance"]
        warnings.append("remediation_target filled from topic brief")
    item["remediation_target"] = normalize_remediation_target(remediation_value)
    for target in re.split(r";\s*", item["remediation_target"]):
        if target.startswith("docs/") and not (ROOT / target).exists():
            warnings.append(f"remediation target not found: {target}")
    item["estimated_time_seconds"] = raw_item.get("estimated_time_seconds") or estimate_time(item)
    item["last_reviewed"] = "not-reviewed"
    item["raw_source"] = f"{raw_source} item {raw_index}"
    item["raw_provider"] = metadata.get("provider", "unknown")
    item["raw_model"] = metadata.get("model", "unknown")
    item["raw_created_utc"] = metadata.get("created_utc", "unknown")
    item["raw_run_id"] = metadata.get("run_id", "unknown")
    item["generation_notes"] = raw_item.get("generation_notes", "")
    if raw_item.get("defensibility_check") != "pass":
        warnings.append("defensibility_check missing or not pass")
    if raw_item.get("evidence_span") and not item["atomic_claims"]:
        warnings.append("evidence_span present but atomic claim derivation failed")

    for field in REQUIRED_FIELDS:
        if field not in item or item[field] in ("", [], "MISSING"):
            warnings.append(f"{field} missing or empty")

    return NormalizedItem(item=item, raw_source=raw_source, raw_index=raw_index, warnings=warnings)


def estimate_time(item: dict[str, Any]) -> int:
    difficulty = str(item.get("difficulty", "")).lower()
    if difficulty == "exam-plus":
        return 180
    if difficulty == "hard":
        return 150
    return 120


def markdown_value(value: Any) -> str:
    if isinstance(value, list):
        return "; ".join(str(part) for part in value)
    if isinstance(value, dict):
        return "; ".join(f"{key}: {val}" for key, val in value.items())
    return str(value)


def render_item(normalized: NormalizedItem) -> str:
    item = normalized.item
    lines = [f"### {item['item_id']}", ""]
    table_fields = [
        "item_id",
        "status",
        "official_exam_code",
        "exam_domain",
        "exam_task",
        "exam_skill",
        "exam_skill_local",
        "secondary_exam_skills",
        "learning_unit",
        "accelerated_day",
        "topic",
        "knowledge_category",
        "knowledge_type",
        "question_format",
        "difficulty",
        "cognitive_demand",
        "estimated_time_seconds",
        "last_reviewed",
        "source_trace_status",
        "source_contract_version",
        "allowed_source_id",
        "raw_source",
        "raw_provider",
        "raw_model",
        "raw_created_utc",
        "raw_run_id",
    ]
    lines.extend(["| Field | Value |", "|---|---|"])
    for field in table_fields:
        if field in item and item[field] not in ("", None):
            lines.append(f"| `{field}` | {markdown_value(item[field])} |")
    lines.append("")

    lines.extend(["Stem:", "", item["stem"], "", "Options:", ""])
    for index, option in enumerate(item["options"], start=1):
        lines.append(f"{index}. {option}")
    lines.append("")

    lines.extend(
        [
            f"Correct answer: {markdown_value(item['correct_answer'])}",
            "",
            f"Rationale: {item['rationale_correct']}",
            "",
            f"Distractors: {markdown_value(item['rationale_distractors'])}",
            "",
            f"Misconception tags: {markdown_value(item['misconception_tags'])}",
            "",
            "Source trace:",
            "",
            item["source_trace"],
            "",
            "Remediation target:",
            "",
            item["remediation_target"],
        ]
    )
    if item.get("atomic_claims"):
        lines.extend(["", "Atomic claims:", ""])
        for index, claim in enumerate(item["atomic_claims"], start=1):
            lines.extend(
                [
                    f"{index}. Claim: {claim['claim']}",
                    f"   Source: {claim['source']}",
                    f"   Evidence span: {claim['evidence_span']}",
                ]
            )
    if item.get("generation_notes"):
        lines.extend(["", f"Generation notes: {item['generation_notes']}"])
    if normalized.warnings:
        lines.extend(["", f"Normalization warnings: {'; '.join(sorted(set(normalized.warnings)))}"])
    lines.append("")
    return "\n".join(lines)


def write_outputs(day: int, normalized_items: list[NormalizedItem], errors: list[str]) -> None:
    reviewed_dir = EXAM_PREP / f"reviewed/day-{day:02d}"
    reviewed_dir.mkdir(parents=True, exist_ok=True)

    draft_path = reviewed_dir / f"day-{day:02d}-normalized-draft-question-bank.md"
    report_path = reviewed_dir / f"day-{day:02d}-normalization-report.md"
    readme_path = reviewed_dir / "README.md"

    topic_counts = Counter(item.item["learning_unit"] for item in normalized_items)
    warning_counts = Counter(
        warning for item in normalized_items for warning in sorted(set(item.warnings))
    )
    format_counts = Counter(item.item["question_format"] for item in normalized_items)
    difficulty_counts = Counter(item.item["difficulty"] for item in normalized_items)
    by_source = Counter(item.raw_source for item in normalized_items)

    header = [
        f"# Day {day} Normalized Draft Question Bank",
        "",
        f"Generated: {date.today().isoformat()}",
        "",
        "Status: draft-normalized; not reviewed and not approved.",
        "",
        "This file normalizes raw LLM outputs into the question-bank schema so the review pass can source-check, cull, deduplicate, and assign final approved status.",
        "",
        f"Spec: `{SPEC_PATH.relative_to(ROOT)}`",
        "",
        "## Summary",
        "",
        f"- Normalized candidate count: {len(normalized_items)}",
        f"- Raw parse errors: {len(errors)}",
        f"- Topics represented: {len(topic_counts)}",
        "",
        "## Topic Counts",
        "",
        "| Learning unit | Candidate count |",
        "|---|---:|",
    ]
    for topic, count in sorted(topic_counts.items()):
        header.append(f"| {topic} | {count} |")
    header.extend(["", "## Draft Items", ""])
    draft_path.write_text(
        "\n".join(header) + "\n".join(render_item(item) for item in normalized_items),
        encoding="utf-8",
    )

    report_lines = [
        f"# Day {day} Normalization Report",
        "",
        f"Generated: {date.today().isoformat()}",
        "",
        "## Counts",
        "",
        f"- Normalized candidates: {len(normalized_items)}",
        f"- Raw parse errors: {len(errors)}",
        "",
        "## Candidate Count By Topic",
        "",
        "| Learning unit | Candidate count | Meets >=10 raw target? |",
        "|---|---:|---|",
    ]
    for topic, count in sorted(topic_counts.items()):
        report_lines.append(f"| {topic} | {count} | {'yes' if count >= 10 else 'no'} |")

    report_lines.extend(["", "## Format Counts", "", "| Format | Count |", "|---|---:|"])
    for fmt, count in sorted(format_counts.items()):
        report_lines.append(f"| {fmt} | {count} |")

    report_lines.extend(["", "## Difficulty Counts", "", "| Difficulty | Count |", "|---|---:|"])
    for difficulty, count in sorted(difficulty_counts.items()):
        report_lines.append(f"| {difficulty} | {count} |")

    report_lines.extend(["", "## Raw Source Counts", "", "| Raw source | Candidate count |", "|---|---:|"])
    for raw_source, count in sorted(by_source.items()):
        report_lines.append(f"| `{raw_source}` | {count} |")

    report_lines.extend(["", "## Normalization Warnings", ""])
    if warning_counts:
        report_lines.extend(["| Warning | Count |", "|---|---:|"])
        for warning, count in sorted(warning_counts.items()):
            report_lines.append(f"| {warning} | {count} |")
    else:
        report_lines.append("No normalization warnings.")

    report_lines.extend(["", "## Parse Errors", ""])
    if errors:
        for error in errors:
            report_lines.append(f"- {error}")
    else:
        report_lines.append("No parse errors.")

    report_path.write_text("\n".join(report_lines) + "\n", encoding="utf-8")

    readme_path.write_text(
        "\n".join(
            [
                f"# Day {day} Exam-Prep Review Outputs",
                "",
                "This folder contains generated review artifacts for the day. Early in",
                "the pipeline it contains normalized draft candidates; after the review",
                "and source gates run it also contains reviewed candidate banks, cull",
                "logs, source-verification reports, and gate status files.",
                "",
                f"- `day-{day:02d}-normalized-draft-question-bank.md`: schema-shaped draft candidates; not approved.",
                f"- `day-{day:02d}-normalization-report.md`: counts, parse status, and normalization warnings.",
                f"- `day-{day:02d}-reviewed-question-bank.md`: reviewed candidates when present; not learner-release approved until final gates pass.",
                f"- `day-{day:02d}-review-output-checks.md`: deterministic review-output checks when present.",
                f"- `day-{day:02d}-answer-position-report.md`: answer-position distribution after rebalancing when present.",
                f"- `day-{day:02d}-source-verification-report.md`: human source-review status when present.",
                f"- `day-{day:02d}-claim-verification-ledger.json`: item-level claim verification worklist when present.",
                "",
                "Do not publish reviewed candidates to learners until source verification",
                "and final gates have passed.",
            ]
        )
        + "\n",
        encoding="utf-8",
    )


def normalize_day(day: int) -> tuple[int, int]:
    briefs = topic_briefs_for_day(day)
    source_index = load_source_catalog_index(day)
    normalized_items: list[NormalizedItem] = []
    errors: list[str] = []
    sequence = 1

    by_order: dict[str, int] = defaultdict(int)
    for raw_path in raw_files_for_day(day):
        raw_text = raw_path.read_text(encoding="utf-8")
        metadata = parse_metadata(raw_text)
        try:
            output_text = extract_output_text(raw_text)
            raw_items = parse_first_json_array(output_text)
        except Exception as exc:  # noqa: BLE001 - report all raw parse failures.
            errors.append(f"`{raw_path.name}`: {exc}")
            continue

        for raw_index, raw_item in enumerate(raw_items, start=1):
            order = str(raw_item.get("curriculum_order") or metadata.get("run_id") or "")
            order = normalize_curriculum_order(order, day)
            brief = briefs.get(order)
            if not brief:
                # Fall back to the item itself. The warning will make the review gap visible.
                brief = None
            normalized = normalize_item(
                raw_item,
                day=day,
                sequence=sequence,
                raw_source=raw_path.name,
                raw_index=raw_index,
                metadata=metadata,
                brief=brief,
                source_index=source_index,
            )
            if not brief:
                normalized.warnings.append(f"no topic brief found for {order or 'unknown order'}")
            normalized_items.append(normalized)
            by_order[order] += 1
            sequence += 1

    write_outputs(day, normalized_items, errors)
    return len(normalized_items), len(errors)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--day", type=int, required=True)
    args = parser.parse_args()

    count, errors = normalize_day(args.day)
    print(f"normalized={count} parse_errors={errors}")


if __name__ == "__main__":
    main()
