#!/usr/bin/env python3
"""Bucket unresolved exam-prep source-review items by next action."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from datetime import date
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
EXAM_PREP = ROOT / "docs/Pilot1/aip-c01/exam-prep"


BUCKETS = {
    "A": {
        "name": "AWS URL with fetched evidence",
        "action": "Run grounded judge; likely highest auto-clear yield.",
    },
    "B": {
        "name": "Local teaching source with fetched evidence",
        "action": "Run grounded judge, but prefer AWS reassignment for AWS factual claims.",
    },
    "C": {
        "name": "source_trace_needed placeholder",
        "action": "Retrieve/propose a real source, then fetch and judge.",
    },
    "D": {
        "name": "AWS URL without fetched evidence",
        "action": "Retry fetch or reject/reassign dead URLs before human review.",
    },
    "E": {
        "name": "NONE source marker",
        "action": "Apply policy: judgment item, rewrite, or cull.",
    },
    "F": {
        "name": "Other unsupported source condition",
        "action": "Inspect source token and normalize to an accepted source type.",
    },
}


def day_slug(day: int) -> str:
    return f"day-{day:02d}"


def reviewed_dir(day: int) -> Path:
    return EXAM_PREP / f"reviewed/{day_slug(day)}"


def claim_report_path(day: int) -> Path:
    return reviewed_dir(day) / f"{day_slug(day)}-claim-source-verification.json"


def output_json_path(day: int) -> Path:
    return reviewed_dir(day) / f"{day_slug(day)}-source-review-triage.json"


def output_md_path(day: int) -> Path:
    return reviewed_dir(day) / f"{day_slug(day)}-source-review-triage-report.md"


def classify(source: str, evidence: str) -> str:
    normalized = (source or "").strip()
    lowered = normalized.lower()
    if lowered == "source_trace_needed":
        return "C"
    if lowered == "none" or not normalized:
        return "E"
    if normalized.startswith("https://docs.aws.amazon.com/"):
        return "A" if evidence.strip() else "D"
    if normalized.startswith("docs/"):
        return "B" if evidence.strip() else "F"
    return "F"


def triage_items(day: int) -> list[dict[str, Any]]:
    path = claim_report_path(day)
    if not path.exists():
        raise SystemExit(f"Missing claim verification report: {path}")
    data = json.loads(path.read_text(encoding="utf-8"))
    records: list[dict[str, Any]] = []
    for item in data.get("items", []):
        if item.get("verdict") != "unresolved":
            continue
        claims = item.get("claims", [])
        claim = claims[0] if claims else {}
        source = str(claim.get("source", "") or "")
        evidence = str(claim.get("evidence", "") or "")
        bucket = classify(source, evidence)
        records.append(
            {
                "item_id": item.get("item_id"),
                "learning_unit": item.get("learning_unit"),
                "bucket": bucket,
                "bucket_name": BUCKETS[bucket]["name"],
                "recommended_action": BUCKETS[bucket]["action"],
                "source": source,
                "has_evidence": bool(evidence.strip()),
                "evidence_length": len(evidence),
                "verification_note": claim.get("verification_note", ""),
                "term_coverage": claim.get("term_coverage"),
                "matched_terms": claim.get("matched_terms", []),
                "claim_excerpt": str(claim.get("claim", ""))[:500],
            }
        )
    return records


def render_markdown(day: int, records: list[dict[str, Any]]) -> str:
    counts = Counter(record["bucket"] for record in records)
    lines = [
        f"# Day {day} Source Review Triage",
        "",
        f"Generated: {date.today().isoformat()}",
        "",
        "This report breaks unresolved source-review items into next-action buckets.",
        "It is not an approval report; it is a work queue for reducing",
        "`needs-human-source-review`.",
        "",
        "## Summary",
        "",
        "| Bucket | Count | Meaning | Next action |",
        "|---|---:|---|---|",
    ]
    for bucket in sorted(BUCKETS):
        lines.append(
            f"| {bucket} | {counts[bucket]} | {BUCKETS[bucket]['name']} | {BUCKETS[bucket]['action']} |"
        )
    lines.extend(
        [
            "",
            "## Items",
            "",
            "| Bucket | Item | Unit | Evidence | Coverage | Source | Note |",
            "|---|---|---|---:|---:|---|---|",
        ]
    )
    for record in records:
        source = record["source"].replace("|", "\\|")
        note = str(record["verification_note"]).replace("|", "\\|")
        lines.append(
            "| {bucket} | {item_id} | {unit} | {evidence_length} | {coverage} | {source} | {note} |".format(
                bucket=record["bucket"],
                item_id=record["item_id"],
                unit=record["learning_unit"],
                evidence_length=record["evidence_length"],
                coverage=record["term_coverage"],
                source=source,
                note=note,
            )
        )
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--day", type=int, required=True, choices=range(1, 8))
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()

    records = triage_items(args.day)
    counts = Counter(record["bucket"] for record in records)
    result = {
        "day": args.day,
        "generated": date.today().isoformat(),
        "bucket_counts": {bucket: counts[bucket] for bucket in sorted(BUCKETS)},
        "buckets": BUCKETS,
        "items": records,
    }
    if args.write:
        output_json_path(args.day).write_text(json.dumps(result, indent=2), encoding="utf-8")
        output_md_path(args.day).write_text(render_markdown(args.day, records), encoding="utf-8")
    print(" ".join(f"{bucket}={counts[bucket]}" for bucket in sorted(BUCKETS)))
    if args.write:
        print(f"report={output_md_path(args.day).relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
