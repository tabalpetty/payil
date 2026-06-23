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


ROOT = Path(__file__).resolve().parents[1]
EXAM_PREP = ROOT / "docs/Pilot1/aip-c01/exam-prep"
SPEC_PATH = EXAM_PREP / "question-bank-specification.md"

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


def normalize_options(value: Any) -> list[str]:
    if isinstance(value, list):
        return [str(option).strip() for option in value if str(option).strip()]
    if isinstance(value, dict):
        return [f"{key}. {val}" for key, val in value.items()]
    if isinstance(value, str) and value.strip():
        return [value.strip()]
    return []


def normalize_item(
    raw_item: dict[str, Any],
    *,
    day: int,
    sequence: int,
    raw_source: str,
    raw_index: int,
    metadata: dict[str, Any],
    brief: dict[str, str] | None,
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
    item["question_format"] = str(raw_item.get("question_format") or "MISSING").strip()
    item["difficulty"] = str(raw_item.get("difficulty") or "MISSING").strip()
    item["cognitive_demand"] = str(raw_item.get("cognitive_demand") or "MISSING").strip()
    item["stem"] = str(raw_item.get("stem") or "MISSING").strip()
    item["options"] = normalize_options(raw_item.get("options"))
    item["correct_answer"] = raw_item.get("correct_answer", "MISSING")
    item["rationale_correct"] = str(raw_item.get("rationale_correct") or "MISSING").strip()
    item["rationale_distractors"] = raw_item.get("rationale_distractors", "MISSING")
    item["misconception_tags"] = raw_item.get("misconception_tags", [])
    item["source_trace"] = normalize_source_trace(raw_item)
    item["source_trace_status"] = "needs-source-check"
    item["remediation_target"] = normalize_remediation_target(raw_item.get("remediation_target"))
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
                f"# Reviewed Day {day}",
                "",
                "This folder currently contains the draft-normalized input for the review pass.",
                "",
                f"- `day-{day:02d}-normalized-draft-question-bank.md`: schema-shaped draft candidates; not approved.",
                f"- `day-{day:02d}-normalization-report.md`: counts, parse status, and normalization warnings.",
                "",
                "The approved bank should be written separately after source-checking, duplicate review, and quality culling.",
            ]
        )
        + "\n",
        encoding="utf-8",
    )


def normalize_day(day: int) -> tuple[int, int]:
    briefs = topic_briefs_for_day(day)
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
            if order.startswith("order"):
                order = f"Day{day:02d}-{order}"
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
