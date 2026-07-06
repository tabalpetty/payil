#!/usr/bin/env python3
"""Map exam-prep topic briefs to official objectives from traceability matrix."""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PILOT = ROOT / "docs/Pilot1/aip-c01"
EXAM_PREP = PILOT / "exam-prep"
OBJECTIVES_JSON = PILOT / "source-material/ai-professional-01.objectives.json"
TRACEABILITY_MATRIX = PILOT / "curriculum-model/source-to-topic-traceability-matrix.md"


@dataclass(frozen=True)
class ObjectiveMapping:
    domain: str
    task: str
    skill: str


def day_slug(day: int) -> str:
    return f"day-{day:02d}"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def load_official_by_skill() -> dict[str, ObjectiveMapping]:
    objectives = json.loads(OBJECTIVES_JSON.read_text(encoding="utf-8"))
    result: dict[str, ObjectiveMapping] = {}
    for domain in objectives.get("domains", []):
        for task in domain.get("tasks", []):
            for skill in task.get("skills", []):
                result[skill["skill_id"]] = ObjectiveMapping(
                    domain=domain["domain"],
                    task=task["task"],
                    skill=skill["skill"],
                )
    return result


def load_traceability() -> dict[str, list[ObjectiveMapping]]:
    official_by_skill = load_official_by_skill()
    mappings: dict[str, list[ObjectiveMapping]] = {}
    for line in TRACEABILITY_MATRIX.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| Domain "):
            continue
        cells = [cell.strip().replace(r"\|", "|") for cell in line.strip("|").split("|")]
        if len(cells) != 7:
            continue
        _, _, _, skill_id, _, order, _ = cells
        if skill_id == "Skill index":
            continue
        if skill_id not in official_by_skill:
            raise SystemExit(f"Traceability matrix references unknown Skill {skill_id}")
        mappings.setdefault(order, [])
        if official_by_skill[skill_id] not in mappings[order]:
            mappings[order].append(official_by_skill[skill_id])
    return mappings


def replacement_section(mappings: list[ObjectiveMapping]) -> str:
    primary = mappings[0]
    secondaries = mappings[1:]
    secondary_text = "None." if not secondaries else "; ".join(mapping.skill for mapping in secondaries)
    return "\n".join(
        [
            "## Official Objective Mapping",
            "",
            "- Status: `mapped`",
            f"- `exam_domain`: {primary.domain}",
            f"- `exam_task`: {primary.task}",
            f"- `exam_skill`: {primary.skill}",
            f"- `secondary_exam_skills`: {secondary_text}",
        ]
    )


def map_brief(path: Path, mappings_by_order: dict[str, list[ObjectiveMapping]], force: bool) -> str:
    text = path.read_text(encoding="utf-8")
    order_match = re.search(r"^\| Curriculum order \| (?P<order>Day\d{2}-order\d{3}) \|$", text, re.MULTILINE)
    if not order_match:
        raise SystemExit(f"Could not find curriculum order in {path}")
    order = order_match.group("order")
    mappings = mappings_by_order.get(order)
    if not mappings:
        raise SystemExit(f"No traceability mapping found for {order}")
    if "- Status: `mapped`" in text and not force:
        return "skipped"

    new_section = replacement_section(mappings)
    pattern = re.compile(r"^## Official Objective Mapping\n\n.*?(?=^## )", re.MULTILINE | re.DOTALL)
    if not pattern.search(text):
        raise SystemExit(f"Could not find objective-mapping section in {path}")
    updated = pattern.sub(new_section + "\n\n", text, count=1)
    updated = updated.replace(
        "- This brief is ready for prompt planning after official objective mapping is filled.",
        "- This brief is ready for prompt planning.",
    )
    path.write_text(updated, encoding="utf-8")
    return "mapped"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--day", type=int, required=True, choices=range(1, 8))
    parser.add_argument("--check", action="store_true", help="Report mapping availability without writing.")
    parser.add_argument("--force", action="store_true", help="Remap briefs that are already mapped.")
    args = parser.parse_args()

    if not OBJECTIVES_JSON.exists():
        raise SystemExit(f"Missing objectives JSON: {OBJECTIVES_JSON}")
    if not TRACEABILITY_MATRIX.exists():
        raise SystemExit(f"Missing traceability matrix: {TRACEABILITY_MATRIX}")

    directory = EXAM_PREP / f"topic-briefs/{day_slug(args.day)}"
    paths = sorted(directory.glob(f"day{args.day:02d}-order*-topic-brief.md"))
    if not paths:
        raise SystemExit(f"No topic briefs found in {directory}")

    mappings_by_order = load_traceability()
    missing = []
    for path in paths:
        text = path.read_text(encoding="utf-8")
        match = re.search(r"^\| Curriculum order \| (?P<order>Day\d{2}-order\d{3}) \|$", text, re.MULTILINE)
        if not match or match.group("order") not in mappings_by_order:
            missing.append(rel(path))
    if missing:
        raise SystemExit("Missing traceability mappings for:\n" + "\n".join(missing))

    if args.check:
        print(f"Day {args.day} briefs ready for objective mapping: {len(paths)}")
        print(f"Directory: {rel(directory)}")
        return 0

    counts = {"mapped": 0, "skipped": 0}
    for path in paths:
        result = map_brief(path, mappings_by_order, args.force)
        counts[result] += 1
    print(f"Day {args.day} objective mapping complete: mapped={counts['mapped']} skipped={counts['skipped']}")
    print(f"Directory: {rel(directory)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
