#!/usr/bin/env python3
"""Verify reviewed exam-prep item source traces against trusted local sources."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from datetime import date
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PILOT = ROOT / "docs/Pilot1/aip-c01"
EXAM_PREP = PILOT / "exam-prep"
OBJECTIVES_JSON = PILOT / "source-material/ai-professional-01.objectives.json"

TRUSTED_EXTERNAL_MARKERS = [
    "docs.aws.amazon.com",
    "AWS ",
    "Amazon ",
    "Glue Data Quality",
    "SageMaker Data Wrangler",
    "Bedrock",
    "OpenSearch",
    "Titan",
]

UNVERIFIABLE_TRACE_MARKERS = [
    "source_trace_needed",
    "source: requirement",
    "documentation needed",
]

REJECTED_FACT_PATTERNS = [
    "as of early 2024",
    "no current support",
    "does not currently",
    "does not yet",
    "currently does not",
    "sagemaker studio classic",
]

KNOWN_BAD_CLAIM_PATTERNS = [
    {
        "name": "open-files-increase-shards",
        "required_fragments": [
            "too many open files",
            "increase the shard count",
        ],
        "reason": (
            "unsupported OpenSearch operational claim: adding shards is not a safe "
            "remediation for file-handle exhaustion and can increase shard/segment overhead"
        ),
    },
]

SERVICE_TERMS = [
    "AWS Glue Data Quality",
    "SageMaker Data Wrangler",
    "Amazon CloudWatch",
    "AWS Lambda",
    "Amazon S3",
    "AWS Transcribe",
    "Amazon Transcribe",
    "Amazon Textract",
    "Amazon Rekognition",
    "SageMaker Processing",
    "Amazon Bedrock",
    "Bedrock Knowledge Bases",
    "Amazon OpenSearch Service",
    "OpenSearch",
    "Amazon Aurora",
    "pgvector",
    "Amazon Titan",
]


def day_slug(day: int) -> str:
    return f"day-{day:02d}"


def reviewed_dir(day: int) -> Path:
    return EXAM_PREP / f"reviewed/{day_slug(day)}"


def bank_path(day: int) -> Path:
    return reviewed_dir(day) / f"{day_slug(day)}-reviewed-question-bank.md"


def report_path(day: int) -> Path:
    return reviewed_dir(day) / f"{day_slug(day)}-source-verification-report.md"


def report_json_path(day: int) -> Path:
    return reviewed_dir(day) / f"{day_slug(day)}-source-verification.json"


def claim_ledger_path(day: int) -> Path:
    return reviewed_dir(day) / f"{day_slug(day)}-claim-verification-ledger.json"


def topic_brief_dir(day: int) -> Path:
    return EXAM_PREP / f"topic-briefs/{day_slug(day)}"


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


def split_items(text: str) -> list[str]:
    reviewed = section(text, "Reviewed Items", [])
    blocks = re.split(r"(?m)^### ", reviewed)
    return ["### " + block.strip() + "\n" for block in blocks[1:] if block.strip()]


def parse_fields(item: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    for line in item.splitlines():
        match = re.match(r"\| `([^`]+)` \| (.*) \|", line)
        if match:
            fields[match.group(1)] = match.group(2).strip()
    return fields


def extract_block(item: str, heading: str, stops: list[str]) -> str:
    start = item.find(heading)
    if start == -1:
        return ""
    start += len(heading)
    remainder = item[start:]
    stop_indexes = [remainder.find(stop) for stop in stops if remainder.find(stop) != -1]
    end = min(stop_indexes) if stop_indexes else len(remainder)
    return remainder[:end].strip()


def source_trace(item: str) -> str:
    return extract_block(item, "Source trace:", ["Remediation target:", "### "])


def remediation_paths(item: str) -> list[str]:
    block = extract_block(item, "Remediation target:", ["### "])
    return [path.rstrip(".,);") for path in re.findall(r"docs/[^\s`]+", block)]


def item_claim_text(item: str) -> str:
    parts = [
        extract_block(item, "Stem:", ["Options:"]),
        extract_block(item, "Options:", ["Correct answer:"]),
        extract_block(item, "Correct answer:", ["Rationale:"]),
        extract_block(item, "Rationale:", ["Distractors:"]),
        extract_block(item, "Distractors:", ["Misconception tags:"]),
    ]
    return " ".join(parts)


def topic_sources(day: int) -> dict[str, list[Path]]:
    result: dict[str, list[Path]] = {}
    for brief in sorted(topic_brief_dir(day).glob(f"day{day:02d}-order*-topic-brief.md")):
        text = brief.read_text(encoding="utf-8")
        order_match = re.search(r"\| Curriculum order \| (.*?) \|", text)
        if not order_match:
            continue
        paths: list[Path] = []
        for match in re.finditer(r"`(docs/[^`]+)`", text):
            path = ROOT / match.group(1)
            if path.exists():
                paths.append(path)
        result[order_match.group(1)] = paths
    return result


def load_objective_text() -> str:
    return OBJECTIVES_JSON.read_text(encoding="utf-8") if OBJECTIVES_JSON.exists() else ""


def read_sources(paths: list[Path]) -> str:
    chunks: list[str] = []
    for path in dict.fromkeys(paths):
        try:
            chunks.append(path.read_text(encoding="utf-8", errors="replace"))
        except OSError:
            continue
    return "\n".join(chunks)


def local_paths_from_trace(trace: str) -> list[Path]:
    paths = []
    for match in re.finditer(r"docs/[^\s`]+", trace):
        path = ROOT / match.group(0).rstrip(".,);")
        if path.exists():
            paths.append(path)
    return paths


def terms_in_text(text: str, terms: list[str]) -> list[str]:
    lowered = text.lower()
    return [term for term in terms if term.lower() in lowered]


def load_claim_ledger(day: int) -> dict[str, dict[str, Any]]:
    path = claim_ledger_path(day)
    if not path.exists():
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    return {
        record["item_id"]: record
        for record in data.get("items", [])
        if record.get("item_id")
    }


def verify_item(
    item: str,
    *,
    topic_source_paths: dict[str, list[Path]],
    objective_text: str,
    claim_ledger: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    fields = parse_fields(item)
    item_id = fields.get("item_id", "unknown")
    order = fields.get("learning_unit", "unknown")
    trace = source_trace(item)
    claim_text = item_claim_text(item)
    reasons: list[str] = []

    if not trace or trace == "MISSING":
        reasons.append("missing source_trace")
    lowered_trace = trace.lower()
    for marker in UNVERIFIABLE_TRACE_MARKERS:
        if marker in lowered_trace:
            reasons.append(f"unresolved source-trace marker: {marker}")
    lowered_claim = claim_text.lower()
    for pattern in REJECTED_FACT_PATTERNS:
        if pattern in lowered_claim:
            reasons.append(f"rejected stale/risky fact pattern: {pattern}")
    for pattern in KNOWN_BAD_CLAIM_PATTERNS:
        if all(fragment in lowered_claim for fragment in pattern["required_fragments"]):
            reasons.append(pattern["reason"])

    source_paths = []
    source_paths.extend(topic_source_paths.get(order, []))
    source_paths.extend(local_paths_from_trace(trace))
    source_paths.extend(ROOT / path for path in remediation_paths(item) if (ROOT / path).exists())
    local_corpus = (objective_text + "\n" + read_sources(source_paths)).lower()

    item_services = terms_in_text(claim_text, SERVICE_TERMS)
    unsupported_services = [
        term for term in item_services if term.lower() not in local_corpus and term.lower() not in lowered_trace
    ]
    if unsupported_services:
        reasons.append(f"service terms not found in trusted local/source trace text: {', '.join(unsupported_services)}")

    if not source_paths and not any(marker.lower() in lowered_trace for marker in TRUSTED_EXTERNAL_MARKERS):
        reasons.append("no trusted local source path or recognizable official-source marker")

    ledger_record = claim_ledger.get(item_id)
    claim_checks = ledger_record.get("claims", []) if ledger_record else []
    if not ledger_record:
        reasons.append("missing item-level claim verification ledger record")
    elif ledger_record.get("verdict") != "verified":
        reasons.append(f"claim verification verdict is {ledger_record.get('verdict', 'missing')}")
    elif not claim_checks:
        reasons.append("claim verification record has no atomic claims")
    else:
        for claim in claim_checks:
            if claim.get("verdict") != "supported":
                reasons.append(
                    f"atomic claim is not supported: {claim.get('claim', 'unnamed claim')}"
                )
            if not claim.get("evidence") or not claim.get("source"):
                reasons.append(
                    f"atomic claim lacks source/evidence: {claim.get('claim', 'unnamed claim')}"
                )

    status = "source-verified" if not reasons else "needs-human-source-review"
    return {
        "item_id": item_id,
        "learning_unit": order,
        "status": status,
        "reasons": reasons,
        "source_trace": trace,
        "service_terms": item_services,
        "local_sources": [str(path.relative_to(ROOT)) for path in dict.fromkeys(source_paths)],
        "claim_verification_record": bool(ledger_record),
        "atomic_claim_count": len(claim_checks),
    }


def replace_status(item: str, status: str) -> str:
    if "| `source_trace_status` |" not in item:
        return item
    return re.sub(r"\| `source_trace_status` \| .*? \|", f"| `source_trace_status` | {status} |", item, count=1)


def initialize_claim_ledger(day: int, items: list[str]) -> None:
    existing = load_claim_ledger(day)
    records = []
    for item in items:
        fields = parse_fields(item)
        item_id = fields.get("item_id", "unknown")
        if item_id in existing:
            records.append(existing[item_id])
            continue
        correct = extract_block(item, "Correct answer:", ["Rationale:"])
        rationale = extract_block(item, "Rationale:", ["Distractors:"])
        records.append(
            {
                "item_id": item_id,
                "verdict": "unresolved",
                "claims": [
                    {
                        "claim": f"Keyed answer and rationale: {correct} - {rationale}",
                        "source": source_trace(item),
                        "evidence": "",
                        "verdict": "unresolved"
                    }
                ]
            }
        )
    claim_ledger_path(day).write_text(
        json.dumps(
            {
                "day": day,
                "status": "in-progress",
                "instructions": [
                    "Split compound claim candidates into atomic claims before verification.",
                    "Use exact official or trusted sources.",
                    "Record concise evidence or a faithful paraphrase.",
                    "Set the item verdict to verified only when every material claim is supported."
                ],
                "items": records
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )


def rebuild_bank(original: str, items: list[str]) -> str:
    reviewed = section(original, "Reviewed Items", [])
    if not reviewed:
        return original
    before = original[: original.find("## Reviewed Items")]
    return before.rstrip() + "\n\n## Reviewed Items\n\n" + "\n".join(item.rstrip() for item in items) + "\n"


def render_report(day: int, results: list[dict[str, Any]]) -> str:
    counts = Counter(result["status"] for result in results)
    lines = [
        f"# Day {day} Source Verification Report",
        "",
        f"Generated: {date.today().isoformat()}",
        "",
        "This report records deterministic source verification against trusted local",
        "teaching/remediation sources, official objective extraction, source-trace",
        "markers, and an item-level atomic-claim ledger. Source presence alone never",
        "produces a verified verdict. Items without claim evidence remain",
        "`needs-human-source-review`.",
        "",
        "## Summary",
        "",
        f"- Source verified: {counts['source-verified']}",
        f"- Needs human source review: {counts['needs-human-source-review']}",
        "",
        "| Item | Unit | Status | Reasons |",
        "|---|---|---|---|",
    ]
    for result in results:
        reasons = "; ".join(result["reasons"]) if result["reasons"] else "none"
        lines.append(f"| {result['item_id']} | {result['learning_unit']} | {result['status']} | {reasons} |")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--day", type=int, required=True, choices=range(1, 8))
    parser.add_argument("--write", action="store_true", help="Update source_trace_status fields in the reviewed bank.")
    parser.add_argument(
        "--initialize-ledger",
        action="store_true",
        help="Create unresolved item-level claim records without overwriting existing records.",
    )
    args = parser.parse_args()

    bank = bank_path(args.day)
    if not bank.exists():
        raise SystemExit(f"Missing reviewed bank: {bank}")

    original = bank.read_text(encoding="utf-8")
    items = split_items(original)
    if args.initialize_ledger:
        initialize_claim_ledger(args.day, items)
    topic_source_paths = topic_sources(args.day)
    objective_text = load_objective_text()
    claim_ledger = load_claim_ledger(args.day)
    results = [
        verify_item(
            item,
            topic_source_paths=topic_source_paths,
            objective_text=objective_text,
            claim_ledger=claim_ledger,
        )
        for item in items
    ]

    if args.write:
        updated_items = [replace_status(item, result["status"]) for item, result in zip(items, results)]
        bank.write_text(rebuild_bank(original, updated_items), encoding="utf-8")

    report_path(args.day).write_text(render_report(args.day, results), encoding="utf-8")
    report_json_path(args.day).write_text(json.dumps({"day": args.day, "results": results}, indent=2), encoding="utf-8")
    counts = Counter(result["status"] for result in results)
    print(f"source_verified={counts['source-verified']} needs_human_source_review={counts['needs-human-source-review']}")
    print(f"report={report_path(args.day).relative_to(ROOT)}")
    return 0 if counts["needs-human-source-review"] == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
