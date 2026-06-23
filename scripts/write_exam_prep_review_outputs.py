#!/usr/bin/env python3
"""Write final review-output files from a reviewed candidate bank."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from datetime import date
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
EXAM_PREP = ROOT / "docs/Pilot1/aip-c01/exam-prep"


def day_slug(day: int) -> str:
    return f"day-{day:02d}"


def reviewed_dir(day: int) -> Path:
    return EXAM_PREP / f"reviewed/{day_slug(day)}"


def candidate_bank_path(day: int) -> Path:
    return reviewed_dir(day) / f"{day_slug(day)}-reviewed-candidate-bank.md"


def final_bank_path(day: int) -> Path:
    return reviewed_dir(day) / f"{day_slug(day)}-reviewed-question-bank.md"


def cull_log_path(day: int) -> Path:
    return reviewed_dir(day) / f"{day_slug(day)}-cull-log.md"


def checks_path(day: int) -> Path:
    return reviewed_dir(day) / f"{day_slug(day)}-review-output-checks.md"


def checks_json_path(day: int) -> Path:
    return reviewed_dir(day) / f"{day_slug(day)}-review-output-checks.json"


def section(text: str, heading: str, next_headings: list[str]) -> str:
    marker = f"## {heading}"
    start = text.find(marker)
    if start == -1:
        return ""
    start += len(marker)
    remainder = text[start:]
    stops = [remainder.find(f"## {next_heading}") for next_heading in next_headings]
    stops = [stop for stop in stops if stop != -1]
    end = min(stops) if stops else len(remainder)
    return remainder[:end].strip()


def parse_review_summary(text: str) -> list[dict[str, Any]]:
    summary = section(text, "Review Summary", ["Prompt Improvement Signals"])
    rows: list[dict[str, Any]] = []
    for line in summary.splitlines():
        if not line.startswith("| Day"):
            continue
        parts = [part.strip() for part in line.strip("|").split("|")]
        if len(parts) != 6:
            continue
        rows.append(
            {
                "curriculum_order": parts[0],
                "raw_normalized": int(parts[1]),
                "reviewed_candidates": int(parts[2]),
                "culled": int(parts[3]),
                "completion_target": int(parts[4]),
                "status": parts[5],
            }
        )
    return rows


def parse_items(reviewed_candidates: str) -> list[str]:
    blocks = re.split(r"(?m)^### ", reviewed_candidates)
    return ["### " + block.strip() + "\n" for block in blocks[1:] if block.strip()]


def parse_item_fields(item: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    for line in item.splitlines():
        match = re.match(r"\| `([^`]+)` \| (.*) \|", line)
        if match:
            fields[match.group(1)] = match.group(2).strip()
    return fields


def parse_cull_rows(culled_items: str) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for line in culled_items.splitlines():
        if not line.startswith("| `"):
            continue
        parts = [part.strip() for part in line.strip("|").split("|")]
        if len(parts) != 5:
            continue
        rows.append(
            {
                "raw_source": parts[0],
                "curriculum_order": parts[1],
                "stem_excerpt": parts[2],
                "reasons": parts[3],
                "evidence": parts[4],
            }
        )
    return rows


def render_final_bank(day: int, source_text: str, items: list[str], summary_rows: list[dict[str, Any]]) -> str:
    prompt_signals = section(source_text, "Prompt Improvement Signals", ["Top-Up Guidance"])
    top_up = section(source_text, "Top-Up Guidance", ["Review Rules Applied"])
    rules = section(source_text, "Review Rules Applied", ["Reviewed Candidates"])

    lines = [
        f"# Day {day} Reviewed Question Bank",
        "",
        "## Review Status",
        "",
        "This file contains reviewed Day "
        f"{day} question-bank candidates that passed schema, scenario, duplicate,",
        "and stale/risky-claim checks. Items are not final approved exam-prep",
        "content until Step 13 completes traceability, source, distribution, and",
        "cost gates.",
        "",
        f"Review-output date: {date.today().isoformat()}",
        f"Input candidate bank: `{candidate_bank_path(day).relative_to(ROOT)}`",
        f"Cull log: `{cull_log_path(day).relative_to(ROOT)}`",
        f"Checks: `{checks_path(day).relative_to(ROOT)}`",
        "",
        "## Review Summary",
        "",
        "| Curriculum order | Raw normalized | Reviewed candidates | Culled | Completion target | Status |",
        "|---|---:|---:|---:|---:|---|",
    ]
    for row in summary_rows:
        lines.append(
            f"| {row['curriculum_order']} | {row['raw_normalized']} | {row['reviewed_candidates']} | "
            f"{row['culled']} | {row['completion_target']} | {row['status']} |"
        )

    lines.extend(
        [
            "",
            "## Prompt Improvement Signals",
            "",
            prompt_signals,
            "",
            "## Top-Up Guidance",
            "",
            top_up,
            "",
            "## Review Rules Applied",
            "",
            rules,
            "",
            "## Reviewed Items",
            "",
        ]
    )
    lines.extend(item.rstrip() + "\n" for item in items)
    return "\n".join(lines).rstrip() + "\n"


def render_cull_log(day: int, source_text: str) -> str:
    prompt_signals = section(source_text, "Prompt Improvement Signals", ["Top-Up Guidance"])
    culled = section(source_text, "Culled Items", [])
    lines = [
        f"# Day {day} Cull Log",
        "",
        f"Generated: {date.today().isoformat()}",
        "",
        "This file records candidates rejected by the Step 9 review/cull pass.",
        "Each cull must include observable evidence so prompt improvements and",
        "review decisions remain auditable.",
        "",
        "## Prompt Improvement Signals",
        "",
        prompt_signals,
        "",
        "## Culled Items",
        "",
        culled,
        "",
    ]
    return "\n".join(lines).rstrip() + "\n"


def build_checks(day: int, source_text: str, target: int) -> tuple[str, dict[str, Any]]:
    reviewed = section(source_text, "Reviewed Candidates", ["Culled Items"])
    culled = section(source_text, "Culled Items", [])
    items = parse_items(reviewed)
    cull_rows = parse_cull_rows(culled)
    summary_rows = parse_review_summary(source_text)
    field_rows = [parse_item_fields(item) for item in items]

    status_counts = Counter(fields.get("status", "MISSING") for fields in field_rows)
    source_status_counts = Counter(fields.get("source_trace_status", "MISSING") for fields in field_rows)
    per_topic_counts = Counter(fields.get("learning_unit", "MISSING") for fields in field_rows)

    missing_required: list[str] = []
    required = [
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
    for index, fields in enumerate(field_rows, 1):
        for key in required:
            if not fields.get(key):
                missing_required.append(f"item {index}: {key}")

    short_topics = {
        topic: count for topic, count in sorted(per_topic_counts.items()) if count < target
    }
    culls_missing_evidence = [
        row["raw_source"] for row in cull_rows if not row.get("evidence") or row["evidence"] == ""
    ]

    checks = {
        "day": day,
        "generated": date.today().isoformat(),
        "target_per_topic": target,
        "reviewed_item_count": len(items),
        "cull_count": len(cull_rows),
        "summary_rows": summary_rows,
        "status_counts": dict(status_counts),
        "source_trace_status_counts": dict(source_status_counts),
        "per_topic_counts": dict(sorted(per_topic_counts.items())),
        "short_topics": short_topics,
        "missing_required_fields": missing_required,
        "culls_missing_evidence": culls_missing_evidence,
        "checks": {
            "reviewed_items_present": len(items) > 0,
            "all_items_reviewed_status": set(status_counts) == {"reviewed"},
            "per_topic_target_met": not short_topics,
            "required_fields_present": not missing_required,
            "cull_evidence_present": not culls_missing_evidence,
            "final_source_verification_pending": bool(source_status_counts),
        },
    }

    lines = [
        f"# Day {day} Review Output Checks",
        "",
        f"Generated: {date.today().isoformat()}",
        "",
        "| Check | Status | Detail |",
        "|---|---|---|",
        f"| Reviewed items present | {'pass' if checks['checks']['reviewed_items_present'] else 'fail'} | {len(items)} reviewed items |",
        f"| All items have reviewed status | {'pass' if checks['checks']['all_items_reviewed_status'] else 'fail'} | {dict(status_counts)} |",
        f"| Per-topic target met | {'pass' if checks['checks']['per_topic_target_met'] else 'fail'} | target={target}; short_topics={short_topics or 'none'} |",
        f"| Required fields present | {'pass' if checks['checks']['required_fields_present'] else 'fail'} | missing={len(missing_required)} |",
        f"| Cull evidence present | {'pass' if checks['checks']['cull_evidence_present'] else 'fail'} | missing_evidence={len(culls_missing_evidence)} |",
        f"| Final source verification | pending | source_trace_status_counts={dict(source_status_counts)} |",
        "",
        "## Per-Topic Reviewed Counts",
        "",
        "| Curriculum order | Reviewed count | Target | Status |",
        "|---|---:|---:|---|",
    ]
    for topic, count in sorted(per_topic_counts.items()):
        lines.append(f"| {topic} | {count} | {target} | {'pass' if count >= target else 'fail'} |")

    lines.extend(
        [
            "",
            "## Outputs",
            "",
            f"- Reviewed bank: `{final_bank_path(day).relative_to(ROOT)}`",
            f"- Cull log: `{cull_log_path(day).relative_to(ROOT)}`",
            f"- Machine-readable checks: `{checks_json_path(day).relative_to(ROOT)}`",
            "",
        ]
    )
    return "\n".join(lines), checks


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--day", type=int, required=True, choices=range(1, 8))
    parser.add_argument("--target", type=int, default=10)
    args = parser.parse_args()

    source = candidate_bank_path(args.day)
    if not source.exists():
        raise SystemExit(f"Missing reviewed candidate bank: {source}")

    text = source.read_text(encoding="utf-8")
    reviewed = section(text, "Reviewed Candidates", ["Culled Items"])
    items = parse_items(reviewed)
    summary_rows = parse_review_summary(text)

    final_bank_path(args.day).write_text(
        render_final_bank(args.day, text, items, summary_rows),
        encoding="utf-8",
    )
    cull_log_path(args.day).write_text(render_cull_log(args.day, text), encoding="utf-8")
    checks_md, checks = build_checks(args.day, text, args.target)
    checks_path(args.day).write_text(checks_md, encoding="utf-8")
    checks_json_path(args.day).write_text(json.dumps(checks, indent=2), encoding="utf-8")

    print(f"reviewed_bank={final_bank_path(args.day).relative_to(ROOT)}")
    print(f"cull_log={cull_log_path(args.day).relative_to(ROOT)}")
    print(f"checks={checks_path(args.day).relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
