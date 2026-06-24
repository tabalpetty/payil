#!/usr/bin/env python3
"""Export the AIP-C01 official-skill-to-curriculum-topic audit matrix."""

from __future__ import annotations

import json
import re
from pathlib import Path
from zipfile import ZipFile
from xml.etree import ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
PILOT = ROOT / "docs/Pilot1/aip-c01"
OBJECTIVES = PILOT / "source-material/ai-professional-01.objectives.json"
SOURCE_MATRIX = PILOT / "source-material/AIP-C01_Curriculum_Dependency_and_Mastery_Matrix.xlsx"
TOPIC_MAP = PILOT / "curriculum-model/aip-c01-topic-knowledge-category-map.md"
OUTPUT = PILOT / "curriculum-model/source-to-topic-traceability-matrix.md"

MAIN_NS = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"


def parse_topics() -> list[dict[str, str]]:
    topics: list[dict[str, str]] = []
    headers: list[str] | None = None
    for line in TOPIC_MAP.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped.startswith("|") or not stripped.endswith("|"):
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if cells and set(cells[0]) <= {"-", ":"}:
            continue
        if cells and cells[0] == "Curriculum Order":
            headers = cells
            continue
        if headers and len(cells) == len(headers) and cells[0].startswith("Day"):
            topics.append(dict(zip(headers, cells, strict=True)))
    return topics


def parse_skill_topic_relationships() -> list[tuple[str, int]]:
    namespace = {"m": MAIN_NS}
    with ZipFile(SOURCE_MATRIX) as workbook:
        sheet = ET.fromstring(workbook.read("xl/worksheets/sheet6.xml"))

    relationships: list[tuple[str, int]] = []
    for row in sheet.findall(".//m:sheetData/m:row", namespace):
        values: dict[str, str] = {}
        for cell in row.findall("m:c", namespace):
            column = re.match(r"[A-Z]+", cell.attrib["r"])
            value = cell.find("m:v", namespace)
            if column and value is not None and value.text:
                values[column.group()] = value.text
        skill_id = values.get("A", "")
        topic_index = values.get("B", "")
        if re.fullmatch(r"\d+\.\d+\.\d+", skill_id) and topic_index.isdigit():
            relationships.append((skill_id, int(topic_index)))
    return relationships


def official_lookup() -> dict[str, dict[str, str]]:
    data = json.loads(OBJECTIVES.read_text(encoding="utf-8"))
    lookup: dict[str, dict[str, str]] = {}
    for domain in data["domains"]:
        for task in domain["tasks"]:
            for skill in task["skills"]:
                lookup[skill["skill_id"]] = {
                    "domain_id": domain["domain_id"],
                    "task_id": task["task_id"],
                    "task": task["task"].split(": ", 1)[-1],
                    "skill": skill["skill"].split(": ", 1)[-1],
                }
    return lookup


def escape_cell(value: str) -> str:
    return value.replace("|", r"\|").replace("\n", " ")


def render() -> str:
    topics = parse_topics()
    relationships = parse_skill_topic_relationships()
    objectives = official_lookup()
    mapped_topic_indices = {topic_index for _, topic_index in relationships}
    represented_skills = {skill_id for skill_id, _ in relationships}

    lines = [
        "# AIP-C01 Source-To-Topic Traceability Matrix",
        "",
        "## Purpose",
        "",
        "This is the canonical audit view connecting official AIP-C01 skills to the",
        "dependency-ordered curriculum topics. It preserves the relationships that",
        "were previously visible only in the planning workbook.",
        "",
        "Coverage in this matrix means **mapped into the curriculum design**. It does",
        "not mean that learner-ready teaching material has already been delivered.",
        "",
        "## Audit Summary",
        "",
        f"- Official skills represented: `{len(represented_skills)}` of `{len(objectives)}`",
        f"- Official skill-to-topic relationships: `{len(relationships)}`",
        f"- Curriculum topics represented: `{len(topics)}` of `{len(topics)}`",
        f"- Officially mapped topics: `{len(mapped_topic_indices)}`",
        f"- Foundation or integration topics: `{len(topics) - len(mapped_topic_indices)}`",
        "",
        "## Official Skill Relationships",
        "",
        "| Domain | Task index | Official task | Skill index | Official skill | Curriculum order | Curriculum topic |",
        "|---|---|---|---|---|---|---|",
    ]

    for skill_id, topic_index in sorted(
        relationships,
        key=lambda item: (item[1], tuple(int(part) for part in item[0].split("."))),
    ):
        objective = objectives[skill_id]
        topic = topics[topic_index - 1]
        values = [
            f"Domain {objective['domain_id']}",
            objective["task_id"],
            objective["task"],
            skill_id,
            objective["skill"],
            topic["Curriculum Order"],
            topic["Topic"],
        ]
        lines.append("| " + " | ".join(escape_cell(value) for value in values) + " |")

    lines.extend(
        [
            "",
            "## Foundation And Integration Topics",
            "",
            "These topics are intentional curriculum additions rather than direct",
            "decompositions of one official Skill X.Y.Z statement.",
            "",
            "| Curriculum order | Curriculum topic | Trace classification | Source scope |",
            "|---|---|---|---|",
        ]
    )
    classifications = {
        1: (
            "Cross-domain foundation",
            "Assumed foundation supporting all official domains",
        ),
        3: (
            "Cross-domain foundation",
            "Official in-scope AWS services and cross-domain architecture vocabulary",
        ),
        133: (
            "Cross-objective integration",
            "Mixed-domain synthesis and exam-scenario application across all official objectives",
        ),
    }
    for topic_index, topic in enumerate(topics, start=1):
        if topic_index in mapped_topic_indices:
            continue
        classification, source_scope = classifications.get(
            topic_index,
            ("Curriculum foundation", "Supporting prerequisite or integration capability"),
        )
        values = [
            topic["Curriculum Order"],
            topic["Topic"],
            classification,
            source_scope,
        ]
        lines.append("| " + " | ".join(escape_cell(value) for value in values) + " |")

    lines.extend(
        [
            "",
            "## Audit Rules",
            "",
            "The decomposition passes source traceability only when:",
            "",
            "1. every official skill appears in at least one official relationship row;",
            "2. every referenced curriculum order exists in the curriculum topic map;",
            "3. every curriculum topic appears either in an official relationship row or",
            "   in the foundation and integration table;",
            "4. task and domain identifiers match the official objective hierarchy;",
            "5. mapped coverage and delivered teaching coverage are reported separately.",
            "",
            "Generated from:",
            "",
            f"- `{OBJECTIVES.relative_to(ROOT)}`",
            f"- `{SOURCE_MATRIX.relative_to(ROOT)}`",
            f"- `{TOPIC_MAP.relative_to(ROOT)}`",
            "",
            "Regenerate with:",
            "",
            "```bash",
            "python3 scripts/export_source_topic_traceability_matrix.py",
            "```",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    OUTPUT.write_text(render(), encoding="utf-8")
    print(f"wrote={OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
