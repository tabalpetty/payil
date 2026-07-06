#!/usr/bin/env python3
"""Audit focused student artifacts for knowledge-type method fit."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PILOT = ROOT / "docs/Pilot1/aip-c01"
TOPIC_MAP = PILOT / "curriculum-model/aip-c01-topic-knowledge-category-map.md"
STUDENT_KIT = PILOT / "student-kit/accelerated-7-day"


@dataclass(frozen=True)
class TopicRow:
    order: str
    topic: str
    knowledge_type: str
    artifact_to_create: str


def day_slug(day: int) -> str:
    return f"day-{day:02d}"


def order_prefix(day: int) -> str:
    return f"Day{day:02d}-order"


def focused_artifact_dir(day: int) -> Path:
    return STUDENT_KIT / f"{day_slug(day)}-artifacts"


def load_topic_rows(day: int) -> list[TopicRow]:
    rows: list[TopicRow] = []
    for line in TOPIC_MAP.read_text(encoding="utf-8").splitlines():
        if not line.startswith(f"| {order_prefix(day)}"):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) != 6:
            continue
        rows.append(
            TopicRow(
                order=cells[0],
                topic=cells[2],
                knowledge_type=cells[4],
                artifact_to_create=cells[5],
            )
        )
    return rows


def artifact_for_order(day: int, order: str) -> Path | None:
    order_number = order.split("-order", 1)[1]
    matches = sorted(focused_artifact_dir(day).glob(f"day{day:02d}-order{order_number}-*.md"))
    return matches[0] if matches else None


def audit_day(day: int) -> tuple[list[str], list[str]]:
    rows = load_topic_rows(day)
    if not rows:
        return [], [f"No topic-map rows found for Day {day}."]

    failures: list[str] = []
    notes: list[str] = []

    embedded_rows = [row for row in rows if "Embedded" in row.knowledge_type]
    notes.append(f"Day {day}: {len(rows)} topic rows; {len(embedded_rows)} Embedded topic(s).")

    directory = focused_artifact_dir(day)
    if embedded_rows and not directory.exists():
        failures.append(f"Missing focused artifact directory for Day {day}: {directory.relative_to(ROOT)}")
        return notes, failures

    for row in embedded_rows:
        path = artifact_for_order(day, row.order)
        if not path:
            failures.append(f"{row.order}: missing focused artifact file in {directory.relative_to(ROOT)}")
            continue
        text = path.read_text(encoding="utf-8")
        if "Embedded Inspection Record" not in text:
            failures.append(f"{row.order}: missing 'Embedded Inspection Record' section in {path.relative_to(ROOT)}")
        if not re.search(r"Observable fact|What to inspect|Inspect a real|Inspect a simulated", text, re.IGNORECASE):
            failures.append(f"{row.order}: inspection section lacks observable inspection prompt in {path.relative_to(ROOT)}")

    return notes, failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--day", type=int, required=True, choices=range(1, 8))
    args = parser.parse_args()

    notes, failures = audit_day(args.day)
    for note in notes:
        print(note)
    if failures:
        print("FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
