#!/usr/bin/env python3
"""Review normalized exam-prep draft items and cull weak candidates."""

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
    "estimated_time_seconds",
    "last_reviewed",
    "source_trace_status",
    "raw_source",
]

WEAK_STEM_PATTERNS = [
    "which of the following best describes",
    "what is a key benefit",
    "what is the primary purpose",
    "what is the role of",
    "which aws service",
    "what is the most suitable service",
]

STALE_OR_RISKY_PATTERNS = [
    "as of early 2024",
    "no current support",
    "does not currently",
    "does not yet",
    "currently does not",
    "sagemaker studio classic",
]

REVIEWER_META_PATTERNS = [
    "reviewer should",
    "reviewer must",
    "reviewer needs to",
    "confirm against current",
    "verify against current",
]

PROMPT_ADJUSTMENTS = {
    "duplicate-pattern": "Provide approved and rejected stem excerpts in the next top-up prompt and require a different scenario, constraint, and misconception.",
    "keyword-trivia stem": "Ban glossary-style or service-name stems; require a professional scenario with a constraint-driven decision.",
    "recall-only item": "Ask for diagnosis, configuration, tradeoff, or first action instead of a definition or service lookup.",
    "not scenario-based": "Require actor, workload, goal, constraint, and failure signal in every stem.",
    "stale or risky technical claim": "Avoid dated or capability-boundary claims unless the exact current AWS source is provided.",
    "reviewer meta-text": "Return learner-visible question content only. Put review instructions in generation notes, never in stems, options, rationales, or source traces.",
    "schema defect": "Regenerate with the required schema and validate before returning items.",
}

STOP_WORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "best",
    "by",
    "for",
    "from",
    "in",
    "is",
    "it",
    "most",
    "of",
    "on",
    "or",
    "should",
    "that",
    "the",
    "their",
    "to",
    "what",
    "which",
    "with",
    "you",
    "your",
}


@dataclass
class Candidate:
    fields: dict[str, str]
    stem: str
    options: list[str]
    correct_answer: str
    rationale: str
    distractors: str
    misconception_tags: str
    source_trace: str
    remediation_target: str
    generation_notes: str
    normalization_warnings: str


@dataclass
class CullRecord:
    candidate: Candidate
    reasons: list[str]
    evidence: list[str]


@dataclass
class ApprovedStem:
    item_id: str
    stem: str
    key: str
    terms: set[str]


def normalized_bank_path(day: int) -> Path:
    return EXAM_PREP / f"reviewed/day-{day:02d}/day-{day:02d}-normalized-draft-question-bank.md"


def reviewed_path(day: int) -> Path:
    return EXAM_PREP / f"reviewed/day-{day:02d}/day-{day:02d}-reviewed-candidate-bank.md"


def feedback_path(day: int) -> Path:
    return EXAM_PREP / f"reviewed/day-{day:02d}/day-{day:02d}-review-feedback.json"


def extract_until(block: str, heading: str, stop_headings: list[str]) -> str:
    start = block.find(heading)
    if start == -1:
        return ""
    start += len(heading)
    remainder = block[start:]
    stops = [remainder.find(stop) for stop in stop_headings if remainder.find(stop) != -1]
    end = min(stops) if stops else len(remainder)
    return remainder[:end].strip()


def parse_table_fields(block: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    table_match = re.search(r"\| Field \| Value \|\n\|---\|---\|\n(?P<body>(?:\|.*\|\n)+)", block)
    if not table_match:
        return fields
    for line in table_match.group("body").splitlines():
        match = re.match(r"\| `([^`]+)` \| (.*) \|", line)
        if match:
            fields[match.group(1)] = match.group(2).strip()
    return fields


def parse_options(text: str) -> list[str]:
    options: list[str] = []
    for line in text.splitlines():
        match = re.match(r"\d+\.\s+(.*)", line.strip())
        if match:
            options.append(match.group(1).strip())
    return options


def parse_candidates(path: Path) -> list[Candidate]:
    text = path.read_text(encoding="utf-8")
    blocks = re.split(r"(?m)^### ", text)
    candidates: list[Candidate] = []
    for raw_block in blocks[1:]:
        block = "### " + raw_block
        fields = parse_table_fields(block)
        stem = extract_until(block, "Stem:", ["Options:"])
        options_text = extract_until(block, "Options:", ["Correct answer:"])
        correct_answer = extract_until(block, "Correct answer:", ["Rationale:"])
        rationale = extract_until(block, "Rationale:", ["Distractors:"])
        distractors = extract_until(block, "Distractors:", ["Misconception tags:"])
        misconception_tags = extract_until(block, "Misconception tags:", ["Source trace:"])
        source_trace = extract_until(block, "Source trace:", ["Remediation target:"])
        remediation_target = extract_until(block, "Remediation target:", ["Generation notes:", "Normalization warnings:", "### "])
        generation_notes = extract_until(block, "Generation notes:", ["Normalization warnings:", "### "])
        normalization_warnings = extract_until(block, "Normalization warnings:", ["### "])
        candidates.append(
            Candidate(
                fields=fields,
                stem=stem,
                options=parse_options(options_text),
                correct_answer=correct_answer,
                rationale=rationale,
                distractors=distractors,
                misconception_tags=misconception_tags,
                source_trace=source_trace,
                remediation_target=remediation_target,
                generation_notes=generation_notes,
                normalization_warnings=normalization_warnings,
            )
        )
    return candidates


def normalize_stem_key(stem: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9]+", " ", stem.lower())).strip()


def stem_terms(stem: str) -> set[str]:
    return {
        token
        for token in re.findall(r"[a-z0-9]+", stem.lower())
        if len(token) > 2 and token not in STOP_WORDS
    }


def duplicate_match(stem: str, approved: list[ApprovedStem]) -> tuple[str, ApprovedStem, float] | None:
    key = normalize_stem_key(stem)
    terms = stem_terms(stem)
    for prior in approved:
        if key and key == prior.key:
            return ("exact", prior, 1.0)
    if len(terms) < 8:
        return None
    for prior in approved:
        union = terms | prior.terms
        similarity = len(terms & prior.terms) / len(union) if union else 0
        if similarity >= 0.72:
            return ("near", prior, similarity)
    return None


def is_scenario_based(stem: str) -> bool:
    lowered = stem.lower()
    signals = [
        "a team",
        "a company",
        "an enterprise",
        "a data",
        "a developer",
        "a customer",
        "an engineer",
        "an ml",
        "a global",
        "a healthcare",
        "a legal",
        "a vector store",
        "your team",
        "you are",
        "you need",
        "after ",
        "during ",
        "when ",
        "while ",
    ]
    return any(signal in lowered for signal in signals)


def review_candidate(candidate: Candidate) -> tuple[bool, list[str], list[str]]:
    reasons: list[str] = []
    evidence: list[str] = []

    def reject(reason: str, detail: str) -> None:
        if reason not in reasons:
            reasons.append(reason)
        evidence.append(f"{reason}: {detail}")

    missing = [field for field in REQUIRED_FIELDS if not candidate.fields.get(field)]
    if missing:
        reject("schema defect", f"missing required field(s): {', '.join(missing)}")
    if candidate.fields.get("official_exam_code") != "AIP-C01":
        reject("schema defect", f"official_exam_code={candidate.fields.get('official_exam_code')!r}")
    if candidate.fields.get("status") != "draft":
        reject("schema defect", f"expected normalized draft status; found {candidate.fields.get('status')!r}")
    if candidate.fields.get("question_format") not in {"multiple-choice", "multiple-response"}:
        reject("schema defect", f"question_format={candidate.fields.get('question_format')!r}")
    if len(candidate.options) < 4:
        reject("schema defect", f"expected at least 4 options; found {len(candidate.options)}")
    if not candidate.correct_answer:
        reject("schema defect", "correct_answer is empty")
    if not candidate.rationale or not candidate.distractors:
        reject("schema defect", "rationale_correct or rationale_distractors is empty")
    if candidate.normalization_warnings:
        reject("schema defect", f"normalization warnings present: {candidate.normalization_warnings}")

    difficulty = candidate.fields.get("difficulty", "").lower()
    demand = candidate.fields.get("cognitive_demand", "").lower()
    if difficulty == "easy":
        reject("recall-only item", "difficulty is easy")
    if demand == "recall":
        reject("recall-only item", "cognitive_demand is recall")
    if not is_scenario_based(candidate.stem) and demand in {"recall", "explain", ""}:
        reject("not scenario-based", "stem lacks a clear actor/workload/constraint scenario")

    lowered_stem = candidate.stem.lower()
    weak_matches = [pattern for pattern in WEAK_STEM_PATTERNS if pattern in lowered_stem]
    if weak_matches:
        reject(
            "keyword-trivia stem",
            f"matched weak stem pattern(s): {', '.join(weak_matches)}; "
            f"stem=\"{truncate(candidate.stem, 260)}\"",
        )

    searchable = " ".join(
        [
            candidate.stem,
            " ".join(candidate.options),
            candidate.correct_answer,
            candidate.rationale,
            candidate.distractors,
            candidate.source_trace,
            candidate.generation_notes,
        ]
    ).lower()
    stale_matches = [pattern for pattern in STALE_OR_RISKY_PATTERNS if pattern in searchable]
    if stale_matches:
        reject(
            "stale or risky technical claim",
            "; ".join(
                f"pattern={pattern}; excerpt=\"{context_excerpt(searchable, pattern)}\""
                for pattern in stale_matches
            ),
        )

    learner_visible = " ".join(
        [
            candidate.stem,
            " ".join(candidate.options),
            candidate.correct_answer,
            candidate.rationale,
            candidate.distractors,
            candidate.source_trace,
        ]
    ).lower()
    meta_matches = [pattern for pattern in REVIEWER_META_PATTERNS if pattern in learner_visible]
    if meta_matches:
        reject(
            "reviewer meta-text",
            "; ".join(
                f"pattern={pattern}; excerpt=\"{context_excerpt(searchable, pattern)}\""
                for pattern in meta_matches
            ),
        )

    if not candidate.source_trace or candidate.source_trace == "MISSING":
        reject("schema defect", "source_trace is missing")
    if not candidate.remediation_target or candidate.remediation_target == "MISSING":
        reject("schema defect", "remediation_target is missing")

    return not reasons, reasons, evidence


def table_cell(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", "<br>")


def truncate(value: str, limit: int) -> str:
    compact = " ".join(value.split())
    return compact if len(compact) <= limit else compact[: limit - 3] + "..."


def context_excerpt(text: str, pattern: str, radius: int = 130) -> str:
    index = text.find(pattern)
    if index == -1:
        return ""
    start = max(0, index - radius)
    end = min(len(text), index + len(pattern) + radius)
    return truncate(text[start:end], 280)


def render_field_table(candidate: Candidate, item_id: str) -> list[str]:
    fields = dict(candidate.fields)
    fields["item_id"] = item_id
    fields["status"] = "reviewed"
    fields["last_reviewed"] = date.today().isoformat()
    fields["source_trace_status"] = "needs-final-source-check"
    ordered = [
        "item_id",
        "status",
        "official_exam_code",
        "exam_domain",
        "exam_task",
        "exam_skill",
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
    lines = ["| Field | Value |", "|---|---|"]
    for field in ordered:
        if field in fields:
            lines.append(f"| `{field}` | {fields[field]} |")
    return lines


def render_candidate(candidate: Candidate, item_id: str) -> str:
    lines = [f"### {item_id}", ""]
    lines.extend(render_field_table(candidate, item_id))
    lines.extend(["", "Stem:", "", candidate.stem, "", "Options:", ""])
    for index, option in enumerate(candidate.options, 1):
        lines.append(f"{index}. {option}")
    lines.extend(
        [
            "",
            f"Correct answer: {candidate.correct_answer}",
            "",
            f"Rationale: {candidate.rationale}",
            "",
            f"Distractors: {candidate.distractors}",
            "",
            f"Misconception tags: {candidate.misconception_tags}",
            "",
            "Source trace:",
            "",
            candidate.source_trace,
            "",
            "Remediation target:",
            "",
            candidate.remediation_target,
            "",
        ]
    )
    return "\n".join(lines)


def render_review(day: int) -> tuple[str, dict[str, Any]]:
    candidates = parse_candidates(normalized_bank_path(day))
    approved: list[Candidate] = []
    culled: list[CullRecord] = []
    approved_stems: dict[str, list[ApprovedStem]] = defaultdict(list)

    for candidate in candidates:
        ok, reasons, evidence = review_candidate(candidate)
        order = candidate.fields.get("learning_unit", "unknown")
        match = duplicate_match(candidate.stem, approved_stems[order]) if ok else None
        if match:
            match_type, prior, similarity = match
            ok = False
            reasons.append("duplicate-pattern")
            evidence.append(
                "duplicate-pattern: "
                f"match_type={match_type}; similarity={similarity:.2f}; "
                f"candidate_stem=\"{truncate(candidate.stem, 320)}\"; "
                f"matched_approved_item={prior.item_id}; "
                f"matched_approved_stem=\"{truncate(prior.stem, 320)}\""
            )

        if ok:
            approved.append(candidate)
            synthetic_id = f"P1-AIP-D{day}-{len(approved):03d}"
            approved_stems[order].append(
                ApprovedStem(
                    item_id=synthetic_id,
                    stem=candidate.stem,
                    key=normalize_stem_key(candidate.stem),
                    terms=stem_terms(candidate.stem),
                )
            )
        else:
            culled.append(CullRecord(candidate=candidate, reasons=reasons, evidence=evidence))

    raw_counts = Counter(candidate.fields.get("learning_unit", "unknown") for candidate in candidates)
    approved_counts = Counter(candidate.fields.get("learning_unit", "unknown") for candidate in approved)
    culled_counts = Counter(record.candidate.fields.get("learning_unit", "unknown") for record in culled)
    reason_counts = Counter(reason for record in culled for reason in record.reasons)

    feedback: dict[str, Any] = {
        "day": day,
        "generated": date.today().isoformat(),
        "minimum_reviewed_candidates_per_topic": 10,
        "summary_by_topic": {},
        "prompt_improvement_signals": [],
        "top_up_guidance": {},
        "reviewed_stems_by_topic": defaultdict(list),
        "culled_items": [],
    }

    lines = [
        f"# Day {day} Reviewed Candidate Bank",
        "",
        "## Review Status",
        "",
        "This file is a review/cull pass over normalized draft candidates.",
        "Items marked `reviewed` passed automated schema, scenario, duplicate,",
        "and stale/risky-claim checks, but still require the final source and",
        "coverage gates before being treated as approved question-bank content.",
        "",
        f"Review date: {date.today().isoformat()}",
        f"Input: `{normalized_bank_path(day).relative_to(ROOT)}`",
        f"Machine-readable feedback: `{feedback_path(day).relative_to(ROOT)}`",
        "",
        "## Review Summary",
        "",
        "| Curriculum order | Raw normalized | Reviewed candidates | Culled | Completion target | Status |",
        "|---|---:|---:|---:|---:|---|",
    ]
    for order in sorted(raw_counts):
        status = "candidate-complete" if approved_counts[order] >= 10 else "short"
        feedback["summary_by_topic"][order] = {
            "raw_normalized": raw_counts[order],
            "reviewed_candidates": approved_counts[order],
            "culled": culled_counts[order],
            "completion_target": 10,
            "status": status,
        }
        lines.append(
            f"| {order} | {raw_counts[order]} | {approved_counts[order]} | {culled_counts[order]} | 10 | {status} |"
        )

    lines.extend(
        [
            "",
            "## Prompt Improvement Signals",
            "",
            "| Failure reason | Count | Prompt adjustment |",
            "|---|---:|---|",
        ]
    )
    if reason_counts:
        for reason, count in reason_counts.most_common():
            adjustment = PROMPT_ADJUSTMENTS.get(reason, "Add a prompt guardrail for this observed failure mode.")
            feedback["prompt_improvement_signals"].append(
                {
                    "failure_reason": reason,
                    "count": count,
                    "prompt_adjustment": adjustment,
                }
            )
            lines.append(f"| {reason} | {count} | {adjustment} |")
    else:
        feedback["prompt_improvement_signals"].append(
            {
                "failure_reason": "None",
                "count": 0,
                "prompt_adjustment": "No prompt adjustment from this pass.",
            }
        )
        lines.append("| None | 0 | No prompt adjustment from this pass. |")

    lines.extend(
        [
            "",
            "## Top-Up Guidance",
            "",
            "| Curriculum order | Reviewed candidates | Deficit to 10 | Recommended raw top-up |",
            "|---|---:|---:|---:|",
        ]
    )
    for order in sorted(raw_counts):
        deficit = max(0, 10 - approved_counts[order])
        top_up = 0 if deficit == 0 else max(deficit + 2, round(deficit * 1.5))
        feedback["top_up_guidance"][order] = {
            "reviewed_candidates": approved_counts[order],
            "deficit_to_10": deficit,
            "recommended_raw_top_up": top_up,
        }
        lines.append(f"| {order} | {approved_counts[order]} | {deficit} | {top_up} |")

    lines.extend(
        [
            "",
            "## Review Rules Applied",
            "",
            "- Required schema fields must be present after normalization.",
            "- Stems must be scenario-based and avoid keyword-trivia patterns.",
            "- `easy` and `recall` items are culled.",
            "- Exact and near-duplicate stems are culled within the same curriculum-order topic.",
            "- Duplicate culls include both the rejected stem and matched reviewed stem.",
            "- Dated, stale, or high-risk unsupported service-capability claims are culled.",
            "- Source traces and remediation targets must be present; final source verification remains a later gate.",
            "",
            "## Reviewed Candidates",
            "",
        ]
    )

    for idx, candidate in enumerate(approved, 1):
        item_id = f"P1-AIP-D{day}-{idx:03d}"
        lines.append(render_candidate(candidate, item_id))
        feedback["reviewed_stems_by_topic"][candidate.fields.get("learning_unit", "unknown")].append(
            {
                "item_id": item_id,
                "stem": candidate.stem,
                "raw_source": candidate.fields.get("raw_source", "unknown"),
            }
        )

    lines.extend(
        [
            "## Culled Items",
            "",
            "| Raw source | Curriculum order | Stem excerpt | Reasons | Evidence |",
            "|---|---|---|---|---|",
        ]
    )
    for record in culled:
        candidate = record.candidate
        raw_source = candidate.fields.get("raw_source", "unknown")
        order = candidate.fields.get("learning_unit", "unknown")
        evidence = "<br>".join(table_cell(item) for item in record.evidence)
        feedback["culled_items"].append(
            {
                "raw_source": raw_source,
                "curriculum_order": order,
                "stem": candidate.stem,
                "reasons": record.reasons,
                "evidence": record.evidence,
            }
        )
        lines.append(
            f"| `{raw_source}` | {order} | {table_cell(truncate(candidate.stem, 140))} | {', '.join(record.reasons)} | {evidence} |"
        )

    feedback["reviewed_stems_by_topic"] = dict(feedback["reviewed_stems_by_topic"])
    return "\n".join(lines).rstrip() + "\n", feedback


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--day", type=int, required=True)
    args = parser.parse_args()

    text, feedback = render_review(args.day)
    out = reviewed_path(args.day)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    feedback_out = feedback_path(args.day)
    feedback_out.write_text(json.dumps(feedback, indent=2), encoding="utf-8")
    reviewed_count = sum(item["reviewed_candidates"] for item in feedback["summary_by_topic"].values())
    culled_count = sum(item["culled"] for item in feedback["summary_by_topic"].values())
    print(
        f"reviewed_candidates={reviewed_count} culled={culled_count} "
        f"output={out.relative_to(ROOT)} feedback={feedback_out.relative_to(ROOT)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
