#!/usr/bin/env python3
"""Reorder reviewed multiple-choice options to balance correct-answer positions."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
EXAM_PREP = ROOT / "docs/Pilot1/aip-c01/exam-prep"


def bank_path(day: int) -> Path:
    return EXAM_PREP / f"reviewed/day-{day:02d}/day-{day:02d}-reviewed-question-bank.md"


def report_path(day: int) -> Path:
    return EXAM_PREP / f"reviewed/day-{day:02d}/day-{day:02d}-answer-position-report.md"


def report_json_path(day: int) -> Path:
    return EXAM_PREP / f"reviewed/day-{day:02d}/day-{day:02d}-answer-position-report.json"


def split_items(text: str) -> tuple[str, list[str]]:
    marker = "## Reviewed Items"
    start = text.find(marker)
    if start == -1:
        raise SystemExit("Reviewed Items section not found")
    prefix = text[:start] + marker + "\n\n"
    blocks = re.split(r"(?m)^### ", text[start + len(marker):])
    return prefix, ["### " + block.strip() + "\n" for block in blocks if block.strip()]


def field(item: str, name: str) -> str:
    match = re.search(rf"^\| `{re.escape(name)}` \| (.*?) \|$", item, re.MULTILINE)
    return match.group(1).strip() if match else ""


def block(item: str, heading: str, stop: str) -> str:
    match = re.search(
        rf"{re.escape(heading)}\s*\n\n(?P<body>.*?)(?=\n\n{re.escape(stop)})",
        item,
        re.DOTALL,
    )
    return match.group("body").strip() if match else ""


def normalize(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip().rstrip(".").casefold()


def rebalance_item(item: str, target_position: int) -> tuple[str, int]:
    if field(item, "question_format") != "multiple-choice":
        return item, 0
    options_text = block(item, "Options:", "Correct answer:")
    correct_match = re.search(r"^Correct answer:\s*(.*?)$", item, re.MULTILINE)
    correct = correct_match.group(1).strip() if correct_match else ""
    options = []
    for line in options_text.splitlines():
        match = re.match(r"\d+\.\s+(.*)", line.strip())
        if match:
            options.append(match.group(1).strip())
    if len(options) != 4:
        raise SystemExit(f"Expected four options in {field(item, 'item_id')}")
    if correct == "0":
        correct_option = options[0]
    elif correct in {"1", "2", "3", "4"}:
        correct_option = options[int(correct) - 1]
    else:
        correct_matches = [option for option in options if normalize(option) == normalize(correct)]
        if len(correct_matches) != 1:
            raise SystemExit(f"Could not uniquely match correct answer in {field(item, 'item_id')}")
        correct_option = correct_matches[0]
    distractors = [option for option in options if option != correct_option]
    reordered = list(distractors)
    reordered.insert(target_position - 1, correct_option)
    replacement = "\n".join(f"{index}. {option}" for index, option in enumerate(reordered, 1))
    updated = re.sub(
        r"Options:\s*\n\n.*?(?=\n\nCorrect answer:)",
        "Options:\n\n" + replacement,
        item,
        count=1,
        flags=re.DOTALL,
    )
    updated = re.sub(
        r"^Correct answer:\s*.*?$",
        f"Correct answer: {correct_option}",
        updated,
        count=1,
        flags=re.MULTILINE,
    )
    return updated, target_position


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--day", type=int, required=True, choices=range(1, 8))
    parser.add_argument("--check", action="store_true", help="Report the planned distribution without writing.")
    args = parser.parse_args()

    path = bank_path(args.day)
    original = path.read_text(encoding="utf-8")
    prefix, items = split_items(original)
    positions = Counter()
    updated_items = []
    multiple_choice_index = 0
    for item in items:
        if field(item, "question_format") == "multiple-choice":
            target = multiple_choice_index % 4 + 1
            multiple_choice_index += 1
        else:
            target = 0
        updated, position = rebalance_item(item, target)
        updated_items.append(updated)
        if position:
            positions[str(position)] += 1

    print(f"multiple_choice_items={multiple_choice_index}")
    print(f"planned_positions={dict(positions)}")
    if not args.check:
        path.write_text(prefix + "\n".join(item.rstrip() for item in updated_items) + "\n", encoding="utf-8")
        print(f"wrote={path.relative_to(ROOT)}")
        report = {
            "day": args.day,
            "generated": date.today().isoformat(),
            "multiple_choice_items": multiple_choice_index,
            "answer_position_counts": dict(positions),
            "balanced": max(positions.values(), default=0) - min(positions.values(), default=0) <= 1,
        }
        report_json_path(args.day).write_text(json.dumps(report, indent=2), encoding="utf-8")
        lines = [
            f"# Day {args.day} Answer Position Report",
            "",
            f"Generated: {date.today().isoformat()}",
            "",
            f"- Multiple-choice items: {multiple_choice_index}",
            f"- Balanced: {'yes' if report['balanced'] else 'no'}",
            "",
            "| Correct-answer position | Count |",
            "|---:|---:|",
        ]
        for position in ("1", "2", "3", "4"):
            lines.append(f"| {position} | {positions.get(position, 0)} |")
        report_path(args.day).write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"report={report_path(args.day).relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
