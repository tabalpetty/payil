#!/usr/bin/env python3
"""Populate exam-prep claim ledgers with conservative source evidence."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from datetime import date
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
PILOT = ROOT / "docs/Pilot1/aip-c01"
EXAM_PREP = PILOT / "exam-prep"

STOP_WORDS = {
    "about", "across", "after", "again", "against", "allows", "answer", "because",
    "before", "being", "between", "claim", "claims", "correct", "could", "each",
    "enables", "ensure", "from", "have", "into", "item", "more", "most", "must",
    "only", "option", "question", "rationale", "should", "source", "than", "that",
    "their", "then", "these", "this", "through", "when", "where", "which", "while",
    "with", "without", "would", "your",
}
PLACEHOLDER_SOURCES = {"source_trace_needed", "none", "NONE", ""}


def day_slug(day: int) -> str:
    return f"day-{day:02d}"


def reviewed_dir(day: int) -> Path:
    return EXAM_PREP / f"reviewed/{day_slug(day)}"


def ledger_path(day: int) -> Path:
    return reviewed_dir(day) / f"{day_slug(day)}-claim-verification-ledger.json"


def url_report_path(day: int) -> Path:
    return reviewed_dir(day) / f"{day_slug(day)}-source-url-verification.json"


def report_json_path(day: int) -> Path:
    return reviewed_dir(day) / f"{day_slug(day)}-claim-source-verification.json"


def report_md_path(day: int) -> Path:
    return reviewed_dir(day) / f"{day_slug(day)}-claim-source-verification-report.md"


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def claim_terms(claim: str) -> list[str]:
    cleaned = re.sub(r"(?i)^keyed answer and rationale:\s*", "", claim)
    words = re.findall(r"[A-Za-z][A-Za-z0-9-]{3,}", cleaned.lower())
    result = []
    for word in words:
        word = word.strip("-")
        if word not in STOP_WORDS and word not in result:
            result.append(word)
    return result


def split_sentences(text: str) -> list[str]:
    text = normalize(text)
    return [part.strip() for part in re.split(r"(?<=[.!?])\s+", text) if part.strip()]


def best_evidence(claim: str, source_text: str) -> tuple[str, float, list[str]]:
    terms = claim_terms(claim)
    if not terms or not source_text.strip():
        return "", 0.0, terms
    lowered_source = source_text.lower()
    present = [term for term in terms if term in lowered_source]
    coverage = len(present) / max(len(terms), 1)

    best_sentence = ""
    best_score = 0
    for sentence in split_sentences(source_text):
        lowered = sentence.lower()
        score = sum(1 for term in terms if term in lowered)
        if score > best_score:
            best_score = score
            best_sentence = sentence
    if not best_sentence and present:
        first = lowered_source.find(present[0])
        start = max(0, first - 180)
        end = min(len(source_text), first + 320)
        best_sentence = normalize(source_text[start:end])
    if len(best_sentence) > 600:
        best_sentence = best_sentence[:597].rstrip() + "..."
    return best_sentence, coverage, present


def load_url_sources(day: int) -> dict[str, str]:
    path = url_report_path(day)
    if not path.exists():
        return {}
    report = json.loads(path.read_text(encoding="utf-8"))
    sources: dict[str, str] = {}
    for result in report.get("results", []):
        if result.get("status") != "reachable" or not result.get("cache_path"):
            continue
        cache_path = ROOT / result["cache_path"]
        if cache_path.exists():
            text = cache_path.read_text(encoding="utf-8", errors="replace")
            sources[result["url"]] = text
            sources[result.get("url_without_fragment", result["url"])] = text
    return sources


def load_source_text(source: str, url_sources: dict[str, str]) -> tuple[str, str]:
    if source in PLACEHOLDER_SOURCES or source.lower() in PLACEHOLDER_SOURCES:
        return "", "placeholder source"
    if source.startswith("https://docs.aws.amazon.com/"):
        text = url_sources.get(source)
        if text:
            return text, ""
        no_fragment = source.split("#", 1)[0]
        text = url_sources.get(no_fragment, "")
        return text, "" if text else "AWS URL was not fetched/reachable"
    if source.startswith("docs/"):
        path = ROOT / source
        if path.exists():
            return path.read_text(encoding="utf-8", errors="replace"), ""
        return "", "local source path does not exist"
    return "", "unsupported source type"


def verify_claim(claim: dict[str, Any], url_sources: dict[str, str], *, min_coverage: float) -> dict[str, Any]:
    text, source_error = load_source_text(str(claim.get("source", "")), url_sources)
    evidence, coverage, present = best_evidence(str(claim.get("claim", "")), text)
    updated = dict(claim)
    updated["verification_method"] = "deterministic lexical source match"
    updated["term_coverage"] = round(coverage, 3)
    updated["matched_terms"] = present[:30]
    if source_error:
        updated["evidence"] = ""
        updated["verdict"] = "unresolved"
        updated["verification_note"] = source_error
    elif evidence and coverage >= min_coverage and len(present) >= 4:
        updated["evidence"] = evidence
        updated["verdict"] = "supported"
        updated["verification_note"] = "source text contains sufficient claim terms; audit still recommended for high-risk claims"
    else:
        updated["evidence"] = evidence
        updated["verdict"] = "unresolved"
        updated["verification_note"] = "insufficient lexical support for conservative auto-approval"
    return updated


def render_report(day: int, items: list[dict[str, Any]]) -> str:
    item_counts = Counter(item.get("verdict", "missing") for item in items)
    claim_counts = Counter()
    for item in items:
        for claim in item.get("claims", []):
            claim_counts[claim.get("verdict", "missing")] += 1
    lines = [
        f"# Day {day} Claim Source Verification Report",
        "",
        f"Generated: {date.today().isoformat()}",
        "",
        f"- Items verified: {item_counts['verified']}",
        f"- Items unresolved: {item_counts['unresolved']}",
        f"- Supported claims: {claim_counts['supported']}",
        f"- Unresolved claims: {claim_counts['unresolved']}",
        "",
        "| Item | Unit | Verdict | Claim Verdicts | Notes |",
        "|---|---|---|---|---|",
    ]
    for item in items:
        claim_verdicts = Counter(claim.get("verdict", "missing") for claim in item.get("claims", []))
        notes = "; ".join(
            sorted(
                {
                    claim.get("verification_note", "")
                    for claim in item.get("claims", [])
                    if claim.get("verification_note") and claim.get("verdict") != "supported"
                }
            )
        )
        lines.append(
            f"| {item.get('item_id')} | {item.get('learning_unit')} | {item.get('verdict')} | {dict(claim_verdicts)} | {notes.replace('|', '\\|')} |"
        )
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--day", type=int, required=True, choices=range(1, 8))
    parser.add_argument("--write", action="store_true", help="Update claim ledger and write reports.")
    parser.add_argument("--min-coverage", type=float, default=0.35)
    args = parser.parse_args()

    path = ledger_path(args.day)
    if not path.exists():
        raise SystemExit(f"Missing claim ledger: {path}")
    ledger = json.loads(path.read_text(encoding="utf-8"))
    url_sources = load_url_sources(args.day)

    updated_items = []
    for item in ledger.get("items", []):
        updated = dict(item)
        updated_claims = [
            verify_claim(claim, url_sources, min_coverage=args.min_coverage)
            for claim in item.get("claims", [])
        ]
        updated["claims"] = updated_claims
        updated["verdict"] = "verified" if updated_claims and all(claim.get("verdict") == "supported" for claim in updated_claims) else "unresolved"
        updated_items.append(updated)

    ledger["items"] = updated_items
    ledger["status"] = "verified" if updated_items and all(item.get("verdict") == "verified" for item in updated_items) else "in-progress"
    ledger["last_claim_source_verification"] = date.today().isoformat()

    if args.write:
        path.write_text(json.dumps(ledger, indent=2), encoding="utf-8")
        report_json_path(args.day).write_text(
            json.dumps({"day": args.day, "items": updated_items}, indent=2),
            encoding="utf-8",
        )
        report_md_path(args.day).write_text(render_report(args.day, updated_items), encoding="utf-8")

    item_counts = Counter(item.get("verdict", "missing") for item in updated_items)
    claim_counts = Counter()
    for item in updated_items:
        for claim in item.get("claims", []):
            claim_counts[claim.get("verdict", "missing")] += 1
    print(f"items_verified={item_counts['verified']} items_unresolved={item_counts['unresolved']}")
    print(f"claims_supported={claim_counts['supported']} claims_unresolved={claim_counts['unresolved']}")
    if args.write:
        print(f"report={report_md_path(args.day).relative_to(ROOT)}")
    return 0 if item_counts["unresolved"] == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
