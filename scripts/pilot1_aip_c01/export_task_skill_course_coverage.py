#!/usr/bin/env python3
"""Export official task and skill course coverage to a two-column XLSX file."""

from __future__ import annotations

import json
import re
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile
from xml.etree import ElementTree as ET
from xml.sax.saxutils import escape


ROOT = Path(__file__).resolve().parents[2]
PILOT = ROOT / "docs/Pilot1/aip-c01"
OBJECTIVES = PILOT / "source-material/ai-professional-01.objectives.json"
MATRIX = PILOT / "source-material/AIP-C01_Curriculum_Dependency_and_Mastery_Matrix.xlsx"
TOPIC_MAP = PILOT / "curriculum-model/aip-c01-topic-knowledge-category-map.md"
STUDENT_PATH = PILOT / "student-kit/accelerated-7-day"
OUTPUT = PILOT / "curriculum-model/aip-c01-task-skill-course-coverage.xlsx"

MAIN_NS = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"


def skill_topic_indices() -> dict[str, set[int]]:
    namespace = {"m": MAIN_NS}
    with ZipFile(MATRIX) as workbook:
        sheet = ET.fromstring(workbook.read("xl/worksheets/sheet6.xml"))

    mappings: dict[str, set[int]] = {}
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
            mappings.setdefault(skill_id, set()).add(int(topic_index))
    return mappings


def completed_topic_indices() -> set[int]:
    curriculum_orders: list[str] = []
    for line in TOPIC_MAP.read_text(encoding="utf-8").splitlines():
        match = re.match(r"\|\s*(Day\d{2}-order\d{3})\s*\|", line)
        if match:
            curriculum_orders.append(match.group(1))

    completed: set[int] = set()
    for topic_index, curriculum_order in enumerate(curriculum_orders, start=1):
        match = re.fullmatch(r"Day(\d{2})-order(\d{3})", curriculum_order)
        if not match:
            continue
        day, order = match.groups()
        artifact_directory = STUDENT_PATH / f"day-{day}-artifacts"
        topic_artifact = list(artifact_directory.glob(f"day{day}-order{order}-*.md"))
        answer_guidance = artifact_directory / f"day-{day}-answer-guidance.md"
        study_guides = list((STUDENT_PATH / "study-guides").glob(f"day-{day}-*.md"))
        if topic_artifact and answer_guidance.exists() and study_guides:
            completed.add(topic_index)
    return completed


def objective_text(value: str) -> str:
    return value.split(": ", 1)[1] if ": " in value else value


def coverage_rows() -> list[tuple[str, str, str, str]]:
    objectives = json.loads(OBJECTIVES.read_text(encoding="utf-8"))
    mappings = skill_topic_indices()
    completed_topics = completed_topic_indices()
    covered_skills = {
        skill_id
        for skill_id, topic_indices in mappings.items()
        if topic_indices.intersection(completed_topics)
    }
    rows: list[tuple[str, str, str, str]] = []

    for domain in objectives["domains"]:
        for task in domain["tasks"]:
            skills = task["skills"]
            task_covered = all(skill["skill_id"] in covered_skills for skill in skills)
            rows.append(
                (
                    "Task",
                    task["task_id"],
                    objective_text(task["task"]),
                    "covered" if task_covered else "not covered",
                )
            )
            for skill in skills:
                status = "covered" if skill["skill_id"] in covered_skills else "not covered"
                rows.append(
                    (
                        "Skill",
                        skill["skill_id"],
                        objective_text(skill["skill"]),
                        status,
                    )
                )
    return rows


def inline_cell(reference: str, value: str, style: int = 0) -> str:
    return (
        f'<c r="{reference}" t="inlineStr" s="{style}">'
        f"<is><t>{escape(value)}</t></is></c>"
    )


def worksheet_xml(rows: list[tuple[str, str, str, str]]) -> str:
    sheet_rows = [
        '<row r="1" ht="24" customHeight="1">'
        + inline_cell("A1", "Task or Skill", 1)
        + inline_cell("B1", "Index", 1)
        + inline_cell("C1", "Skill / Task", 1)
        + inline_cell("D1", "Covered or Not Covered in Our Course", 1)
        + "</row>"
    ]
    for row_number, (objective_type, index, objective, status) in enumerate(rows, start=2):
        status_style = 2 if status == "covered" else 3
        sheet_rows.append(
            f'<row r="{row_number}">'
            + inline_cell(f"A{row_number}", objective_type)
            + inline_cell(f"B{row_number}", index)
            + inline_cell(f"C{row_number}", objective)
            + inline_cell(f"D{row_number}", status, status_style)
            + "</row>"
        )

    last_row = len(rows) + 1
    return (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        f'<worksheet xmlns="{MAIN_NS}">'
        '<sheetViews><sheetView workbookViewId="0">'
        '<pane ySplit="1" topLeftCell="A2" activePane="bottomLeft" state="frozen"/>'
        "</sheetView></sheetViews>"
        '<cols><col min="1" max="1" width="16" customWidth="1"/>'
        '<col min="2" max="2" width="14" customWidth="1"/>'
        '<col min="3" max="3" width="110" customWidth="1"/>'
        '<col min="4" max="4" width="38" customWidth="1"/></cols>'
        f'<sheetData>{"".join(sheet_rows)}</sheetData>'
        f'<autoFilter ref="A1:D{last_row}"/>'
        "</worksheet>"
    )


def write_workbook(rows: list[tuple[str, str, str, str]]) -> None:
    content_types = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>
  <Override PartName="/xl/worksheets/sheet1.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>
  <Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/>
</Types>"""
    root_relationships = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/>
</Relationships>"""
    workbook = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"
 xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">
  <sheets><sheet name="Course Coverage" sheetId="1" r:id="rId1"/></sheets>
</workbook>"""
    workbook_relationships = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet1.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
</Relationships>"""
    styles = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<styleSheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">
  <fonts count="2">
    <font><sz val="11"/><name val="Calibri"/></font>
    <font><b/><color rgb="FFFFFFFF"/><sz val="11"/><name val="Calibri"/></font>
  </fonts>
  <fills count="4">
    <fill><patternFill patternType="none"/></fill>
    <fill><patternFill patternType="gray125"/></fill>
    <fill><patternFill patternType="solid"><fgColor rgb="FF1F4E78"/><bgColor indexed="64"/></patternFill></fill>
    <fill><patternFill patternType="solid"><fgColor rgb="FFE2F0D9"/><bgColor indexed="64"/></patternFill></fill>
  </fills>
  <borders count="1"><border><left/><right/><top/><bottom/><diagonal/></border></borders>
  <cellStyleXfs count="1"><xf numFmtId="0" fontId="0" fillId="0" borderId="0"/></cellStyleXfs>
  <cellXfs count="4">
    <xf numFmtId="0" fontId="0" fillId="0" borderId="0" xfId="0" applyAlignment="1"><alignment vertical="top" wrapText="1"/></xf>
    <xf numFmtId="0" fontId="1" fillId="2" borderId="0" xfId="0" applyFont="1" applyFill="1"/>
    <xf numFmtId="0" fontId="0" fillId="3" borderId="0" xfId="0" applyFill="1" applyAlignment="1"><alignment horizontal="center"/></xf>
    <xf numFmtId="0" fontId="0" fillId="0" borderId="0" xfId="0" applyAlignment="1"><alignment horizontal="center"/></xf>
  </cellXfs>
  <cellStyles count="1"><cellStyle name="Normal" xfId="0" builtinId="0"/></cellStyles>
</styleSheet>"""

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(OUTPUT, "w", ZIP_DEFLATED) as target:
        target.writestr("[Content_Types].xml", content_types)
        target.writestr("_rels/.rels", root_relationships)
        target.writestr("xl/workbook.xml", workbook)
        target.writestr("xl/_rels/workbook.xml.rels", workbook_relationships)
        target.writestr("xl/styles.xml", styles)
        target.writestr("xl/worksheets/sheet1.xml", worksheet_xml(rows))


def main() -> None:
    rows = coverage_rows()
    write_workbook(rows)
    covered = sum(status == "covered" for _, _, _, status in rows)
    print(f"wrote={OUTPUT.relative_to(ROOT)}")
    print(f"rows={len(rows)}")
    print(f"covered={covered}")
    print(f"not_covered={len(rows) - covered}")


if __name__ == "__main__":
    main()
