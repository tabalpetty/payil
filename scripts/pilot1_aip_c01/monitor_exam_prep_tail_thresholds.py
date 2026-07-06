#!/usr/bin/env python3
"""Monitor exam-prep automation tail thresholds.

The exam-prep pipeline should keep source-verification repair work small.
If the LLM repair tail or human-review tail grows large, generation has not
met the automation-quality contract even if item counts are complete.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from datetime import date
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
EXAM_PREP = ROOT / "docs/Pilot1/aip-c01/exam-prep"

DEFAULT_LLM_REPAIR_TAIL_THRESHOLD = 0.15
DEFAULT_HUMAN_REVIEW_TAIL_THRESHOLD = 0.05


def day_slug(day: int) -> str:
    return f"day-{day:02d}"


def reviewed_dir(day: int) -> Path:
    return EXAM_PREP / f"reviewed/{day_slug(day)}"


def final_gates_path(day: int) -> Path:
    return reviewed_dir(day) / f"{day_slug(day)}-final-gates.json"


def claim_report_path(day: int) -> Path:
    return reviewed_dir(day) / f"{day_slug(day)}-claim-source-verification.json"


def output_json_path(day: int) -> Path:
    return reviewed_dir(day) / f"{day_slug(day)}-tail-threshold-monitor.json"


def output_md_path(day: int) -> Path:
    return reviewed_dir(day) / f"{day_slug(day)}-tail-threshold-monitor.md"


def ratio(numerator: int, denominator: int) -> float:
    return numerator / denominator if denominator else 1.0


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise SystemExit(f"Missing required file: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def monitor(
    day: int,
    *,
    llm_repair_threshold: float,
    human_review_threshold: float,
) -> dict[str, Any]:
    final_gates = load_json(final_gates_path(day))
    reviewed_count = int(final_gates.get("reviewed_item_count", 0))
    source_counts = Counter(final_gates.get("source_trace_status_counts", {}))
    human_review_count = int(source_counts.get("needs-human-source-review", 0))

    claim_report = load_json(claim_report_path(day))
    claim_items = claim_report.get("items", [])
    claim_counts = Counter(item.get("verdict", "missing") for item in claim_items)
    claim_total = len(claim_items) or reviewed_count
    llm_repair_count = int(claim_counts.get("unresolved", 0))

    human_review_ratio = ratio(human_review_count, reviewed_count)
    llm_repair_ratio = ratio(llm_repair_count, claim_total)
    breaches = []
    if llm_repair_ratio > llm_repair_threshold:
        breaches.append(
            {
                "threshold": "llm_repair_tail",
                "count": llm_repair_count,
                "total": claim_total,
                "ratio": round(llm_repair_ratio, 4),
                "limit": llm_repair_threshold,
                "meaning": "Too many items require LLM repair/judgment after deterministic verification.",
            }
        )
    if human_review_ratio > human_review_threshold:
        breaches.append(
            {
                "threshold": "human_review_tail",
                "count": human_review_count,
                "total": reviewed_count,
                "ratio": round(human_review_ratio, 4),
                "limit": human_review_threshold,
                "meaning": "Too many reviewed items still require human source review.",
            }
        )

    return {
        "day": day,
        "generated": date.today().isoformat(),
        "reviewed_item_count": reviewed_count,
        "thresholds": {
            "llm_repair_tail_max_ratio": llm_repair_threshold,
            "human_review_tail_max_ratio": human_review_threshold,
        },
        "counts": {
            "claim_verification": dict(claim_counts),
            "source_trace_status": dict(source_counts),
            "llm_repair_tail": llm_repair_count,
            "human_review_tail": human_review_count,
        },
        "ratios": {
            "llm_repair_tail": round(llm_repair_ratio, 4),
            "human_review_tail": round(human_review_ratio, 4),
        },
        "breaches": breaches,
        "status": "breach" if breaches else "pass",
    }


def render_markdown(result: dict[str, Any]) -> str:
    lines = [
        f"# Day {result['day']} Tail Threshold Monitor",
        "",
        f"Generated: {result['generated']}",
        "",
        f"Status: `{result['status']}`",
        "",
        "## Thresholds",
        "",
        "| Tail | Limit | Actual | Count | Status |",
        "|---|---:|---:|---:|---|",
    ]
    reviewed = result["reviewed_item_count"]
    thresholds = result["thresholds"]
    ratios = result["ratios"]
    counts = result["counts"]
    rows = [
        (
            "LLM repair/judge tail",
            thresholds["llm_repair_tail_max_ratio"],
            ratios["llm_repair_tail"],
            counts["llm_repair_tail"],
        ),
        (
            "Human source-review tail",
            thresholds["human_review_tail_max_ratio"],
            ratios["human_review_tail"],
            counts["human_review_tail"],
        ),
    ]
    for label, limit, actual, count in rows:
        status = "pass" if actual <= limit else "breach"
        lines.append(f"| {label} | {limit:.0%} | {actual:.1%} | {count}/{reviewed} | {status} |")

    lines.extend(["", "## Breaches", ""])
    if result["breaches"]:
        for breach in result["breaches"]:
            lines.append(
                "- {threshold}: {count}/{total} ({ratio:.1%}) exceeds {limit:.0%}. {meaning}".format(
                    **breach
                )
            )
    else:
        lines.append("- none")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--day", type=int, required=True, choices=range(1, 8))
    parser.add_argument("--llm-repair-threshold", type=float, default=DEFAULT_LLM_REPAIR_TAIL_THRESHOLD)
    parser.add_argument("--human-review-threshold", type=float, default=DEFAULT_HUMAN_REVIEW_TAIL_THRESHOLD)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()

    result = monitor(
        args.day,
        llm_repair_threshold=args.llm_repair_threshold,
        human_review_threshold=args.human_review_threshold,
    )
    if args.write:
        output_json_path(args.day).write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        output_md_path(args.day).write_text(render_markdown(result), encoding="utf-8")
    print(
        "status={status} llm_repair_tail={llm:.1%} human_review_tail={human:.1%}".format(
            status=result["status"],
            llm=result["ratios"]["llm_repair_tail"],
            human=result["ratios"]["human_review_tail"],
        )
    )
    if result["breaches"]:
        for breach in result["breaches"]:
            print(
                "BREACH {threshold}: {count}/{total} ({ratio:.1%}) > {limit:.0%}".format(
                    **breach
                )
            )
    if args.write:
        print(f"report={output_md_path(args.day).relative_to(ROOT)}")
    return 0 if result["status"] == "pass" else 2


if __name__ == "__main__":
    raise SystemExit(main())
