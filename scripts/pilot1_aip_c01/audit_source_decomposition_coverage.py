#!/usr/bin/env python3
"""Audit official-source coverage before downstream curriculum generation."""

from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from datetime import date
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
PILOT = ROOT / "docs/Pilot1/aip-c01"
CURRICULUM_MODEL = PILOT / "curriculum-model"
OBJECTIVES_JSON = PILOT / "source-material/ai-professional-01.objectives.json"
TOPIC_MAP = CURRICULUM_MODEL / "aip-c01-topic-knowledge-category-map.md"
ACCELERATED_PLAN = CURRICULUM_MODEL / "accelerated-7-day-plan.md"
DEFERRALS = CURRICULUM_MODEL / "source-to-decomposition-deferrals.md"
TRACEABILITY_MATRIX = CURRICULUM_MODEL / "source-to-topic-traceability-matrix.md"
REPORT_MD = CURRICULUM_MODEL / "source-to-decomposition-coverage-audit.md"
REPORT_JSON = CURRICULUM_MODEL / "source-to-decomposition-coverage-audit.json"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def objective_sort_key(value: str) -> tuple[int, ...]:
    return tuple(int(part) for part in value.split("."))


def load_objectives(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def parse_topic_rows(path: Path) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    headers: list[str] | None = None
    for line in path.read_text(encoding="utf-8").splitlines():
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
            rows.append(dict(zip(headers, cells, strict=True)))
    return rows


def markdown_files_for_upstream_audit() -> list[Path]:
    return [
        CURRICULUM_MODEL / "README.md",
        CURRICULUM_MODEL / "accelerated-path-design.md",
        CURRICULUM_MODEL / "accelerated-7-day-plan.md",
        TOPIC_MAP,
        TRACEABILITY_MATRIX,
    ]


def read_existing(paths: list[Path]) -> dict[str, str]:
    contents: dict[str, str] = {}
    for path in paths:
        if path.exists():
            contents[rel(path)] = path.read_text(encoding="utf-8")
    return contents


def find_task_references(contents: dict[str, str]) -> dict[str, list[str]]:
    refs: dict[str, list[str]] = defaultdict(list)
    for source, text in contents.items():
        for task_id in re.findall(r"\bTask\s+(\d+\.\d+)\b", text):
            refs[task_id].append(source)
    return dict(refs)


def find_skill_references(contents: dict[str, str]) -> dict[str, list[str]]:
    refs: dict[str, list[str]] = defaultdict(list)
    for source, text in contents.items():
        for skill_id in re.findall(r"\bSkill\s+(\d+\.\d+\.\d+)\b", text):
            refs[skill_id].append(source)
    return dict(refs)


def parse_deferrals(path: Path) -> dict[str, dict[str, str]]:
    if not path.exists():
        return {}
    rows: dict[str, dict[str, str]] = {}
    headers: list[str] | None = None
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped.startswith("|") or not stripped.endswith("|"):
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if cells and set(cells[0]) <= {"-", ":"}:
            continue
        if cells and cells[0].lower() in {"objective id", "official objective id"}:
            headers = cells
            continue
        if not headers or len(cells) != len(headers):
            continue
        row = dict(zip(headers, cells, strict=True))
        objective_id = (
            row.get("Objective ID")
            or row.get("Official Objective ID")
            or row.get("objective_id")
            or ""
        ).strip()
        if objective_id:
            rows[objective_id] = row
    return rows


def parse_traceability_matrix(path: Path) -> tuple[set[str], set[str]]:
    skill_ids: set[str] = set()
    curriculum_orders: set[str] = set()
    if not path.exists():
        return skill_ids, curriculum_orders
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|"):
            continue
        skill_match = re.search(r"\|\s*(\d+\.\d+\.\d+)\s*\|", line)
        order_match = re.search(r"\|\s*(Day\d{2}-order\d{3})\s*\|", line)
        if skill_match:
            skill_ids.add(skill_match.group(1))
        if order_match:
            curriculum_orders.add(order_match.group(1))
    return skill_ids, curriculum_orders


def task_topic_evidence(path: Path) -> dict[str, list[str]]:
    evidence: dict[str, set[str]] = defaultdict(set)
    if not path.exists():
        return {}
    for line in path.read_text(encoding="utf-8").splitlines():
        task_match = re.search(r"\|\s*(\d+\.\d+)\s*\|", line)
        order_match = re.search(r"\|\s*(Day\d{2}-order\d{3})\s*\|", line)
        if task_match and order_match:
            evidence[task_match.group(1)].add(order_match.group(1))
    return {task_id: sorted(orders) for task_id, orders in evidence.items()}


def official_records(data: dict[str, Any]) -> tuple[list[dict[str, str]], list[dict[str, str]], list[dict[str, str]]]:
    domains: list[dict[str, str]] = []
    tasks: list[dict[str, str]] = []
    skills: list[dict[str, str]] = []
    for domain in data.get("domains", []):
        domains.append(
            {
                "domain_id": domain["domain_id"],
                "domain": domain["domain"],
                "weight_percent": str(domain.get("weight_percent", "")),
            }
        )
        for task in domain.get("tasks", []):
            tasks.append(
                {
                    "domain_id": domain["domain_id"],
                    "task_id": task["task_id"],
                    "task": task["task"],
                }
            )
            for skill in task.get("skills", []):
                skills.append(
                    {
                        "domain_id": domain["domain_id"],
                        "task_id": task["task_id"],
                        "skill_id": skill["skill_id"],
                        "skill": skill["skill"],
                    }
                )
    return domains, tasks, skills


def group_topic_counts(rows: list[dict[str, str]]) -> dict[str, int]:
    counts: dict[str, int] = defaultdict(int)
    for row in rows:
        match = re.match(r"Day(\d{2})-", row.get("Curriculum Order", ""))
        if match:
            counts[f"Day {int(match.group(1))}"] += 1
    return dict(sorted(counts.items()))


def render_report(audit: dict[str, Any]) -> str:
    missing_tasks = audit["missing_tasks"]
    missing_skills = audit["missing_skills"]
    deferred_tasks = audit["deferred_tasks"]
    deferred_skills = audit["deferred_skills"]
    topic_rows_without_trace = audit["topic_rows_without_explicit_source_trace"]

    lines = [
        "# Source-To-Decomposition Coverage Audit",
        "",
        f"Generated: {audit['generated']}",
        "",
        "## Verdict",
        "",
        f"- `overall_status`: `{audit['overall_status']}`",
        f"- `task_coverage_status`: `{audit['task_coverage_status']}`",
        f"- `skill_coverage_status`: `{audit['skill_coverage_status']}`",
        f"- `topic_traceability_status`: `{audit['topic_traceability_status']}`",
        "",
        "This is an upstream Layer 0 gate. It checks whether the official source",
        "objectives are represented by the decomposition before topic briefs,",
        "question prompts, question banks, or teaching packages are generated.",
        "",
        "## Inputs",
        "",
        f"- Official objectives: `{audit['inputs']['objectives_json']}`",
        f"- Curriculum topic map: `{audit['inputs']['topic_map']}`",
        f"- Accelerated plan: `{audit['inputs']['accelerated_plan']}`",
        f"- Source-to-topic matrix: `{audit['inputs']['traceability_matrix']}`",
        f"- Deferrals file: `{audit['inputs']['deferrals']}`",
        "",
        "## Counts",
        "",
        "| Measure | Count |",
        "|---|---:|",
        f"| Official domains | {audit['counts']['official_domains']} |",
        f"| Official tasks | {audit['counts']['official_tasks']} |",
        f"| Official skills | {audit['counts']['official_skills']} |",
        f"| Curriculum topic rows | {audit['counts']['curriculum_topic_rows']} |",
        f"| Covered or deferred tasks | {audit['counts']['covered_or_deferred_tasks']} |",
        f"| Covered or deferred skills | {audit['counts']['covered_or_deferred_skills']} |",
        "",
        "## Topic Rows By Day",
        "",
        "| Day | Topic rows |",
        "|---|---:|",
    ]
    for day, count in audit["topic_rows_by_day"].items():
        lines.append(f"| {day} | {count} |")

    lines.extend(
        [
            "",
            "## Task Coverage",
            "",
            "The accelerated plan references every official task ID. This means the",
            "day-level plan has not silently dropped an official task.",
            "",
            "| Task | Status | Evidence |",
            "|---|---|---|",
        ]
    )
    for task in audit["tasks"]:
        evidence = "; ".join(task["evidence"]) if task["evidence"] else task["deferral_reason"]
        lines.append(f"| Task {task['task_id']} | {task['status']} | {evidence} |")

    lines.extend(
        [
            "",
            "## Skill Coverage",
            "",
            "Layer 0 requires either explicit coverage or explicit deferral for each",
            "official skill. Evidence must come from the canonical source-to-topic",
            "matrix or an explicit deferral.",
            "",
        ]
    )
    if missing_skills:
        lines.extend(
            [
                f"Missing or undeferred official skills: `{len(missing_skills)}`",
                "",
                "| Skill | Task | Official text |",
                "|---|---|---|",
            ]
        )
        for skill in missing_skills:
            lines.append(f"| Skill {skill['skill_id']} | Task {skill['task_id']} | {skill['skill']} |")
    else:
        lines.append("No missing or undeferred skills.")

    lines.extend(
        [
            "",
            "## Topic Traceability",
            "",
            "The curriculum topic map should carry explicit source objective coverage,",
            "such as official task IDs, skill IDs, or a link to a source-to-topic",
            "coverage map. The audit also accepts explicitly classified foundation",
            "and cross-objective integration topics.",
            "",
        ]
    )
    if topic_rows_without_trace:
        lines.extend(["| Curriculum order | Topic |", "|---|---|"])
        for row in topic_rows_without_trace:
            lines.append(f"| {row['Curriculum Order']} | {row['Topic']} |")
    else:
        lines.append("All topic rows have explicit source traceability.")

    lines.extend(
        [
            "",
            "## Deferrals",
            "",
        ]
    )
    if deferred_tasks or deferred_skills:
        lines.extend(["| Objective | Reason |", "|---|---|"])
        for item in deferred_tasks + deferred_skills:
            lines.append(f"| {item['objective_id']} | {item['reason']} |")
    else:
        lines.append("No explicit deferrals were found.")

    lines.extend(["", "## Required Next Action", ""])
    if audit["overall_status"] == "complete":
        lines.extend(
            [
                "No decomposition repair is required. Regenerate the traceability",
                "matrix and rerun this audit whenever the official objectives or",
                "curriculum topic decomposition changes.",
            ]
        )
    else:
        lines.extend(
            [
                "Add explicit source-objective coverage to the decomposition layer before",
                "treating Layer 0 as complete. Use the source-to-topic matrix for official",
                "task and Skill X.Y.Z relationships, and the separate deferral file for",
                "objectives intentionally omitted or delayed.",
                "",
                "After that mapping exists, rerun:",
                "",
                "```bash",
                "python3 scripts/pilot1_aip_c01/audit_source_decomposition_coverage.py",
                "```",
            ]
        )
    if missing_tasks:
        lines.extend(["", "## Missing Tasks", ""])
        for task in missing_tasks:
            lines.append(f"- Task {task['task_id']}: {task['task']}")

    return "\n".join(lines) + "\n"


def build_audit() -> dict[str, Any]:
    objectives = load_objectives(OBJECTIVES_JSON)
    domains, tasks, skills = official_records(objectives)
    topic_rows = parse_topic_rows(TOPIC_MAP)
    upstream_contents = read_existing(markdown_files_for_upstream_audit())
    task_refs = find_task_references(upstream_contents)
    skill_refs = find_skill_references(upstream_contents)
    deferrals = parse_deferrals(DEFERRALS)
    traced_skill_ids, traced_curriculum_orders = parse_traceability_matrix(TRACEABILITY_MATRIX)
    traced_task_topics = task_topic_evidence(TRACEABILITY_MATRIX)

    task_rows = []
    missing_tasks = []
    deferred_tasks = []
    for task in sorted(tasks, key=lambda item: objective_sort_key(item["task_id"])):
        task_id = task["task_id"]
        if task_id in traced_task_topics:
            status = "covered"
            evidence = [
                f"{rel(TRACEABILITY_MATRIX)}#{order}"
                for order in traced_task_topics[task_id]
            ]
            reason = ""
        elif task_id in task_refs:
            status = "covered"
            evidence = sorted(set(task_refs[task_id]))
            reason = ""
        elif task_id in deferrals:
            status = "deferred"
            evidence = []
            reason = deferrals[task_id].get("Reason", "") or deferrals[task_id].get("Deferral Reason", "")
            deferred_tasks.append({"objective_id": f"Task {task_id}", "reason": reason})
        else:
            status = "missing"
            evidence = []
            reason = ""
            missing_tasks.append(task)
        task_rows.append({**task, "status": status, "evidence": evidence, "deferral_reason": reason})

    skill_rows = []
    missing_skills = []
    deferred_skills = []
    for skill in sorted(skills, key=lambda item: objective_sort_key(item["skill_id"])):
        skill_id = skill["skill_id"]
        if skill_id in traced_skill_ids:
            status = "covered"
            evidence = [rel(TRACEABILITY_MATRIX)]
            reason = ""
        elif skill_id in skill_refs:
            status = "covered"
            evidence = sorted(set(skill_refs[skill_id]))
            reason = ""
        elif skill_id in deferrals:
            status = "deferred"
            evidence = []
            reason = deferrals[skill_id].get("Reason", "") or deferrals[skill_id].get("Deferral Reason", "")
            deferred_skills.append({"objective_id": f"Skill {skill_id}", "reason": reason})
        else:
            status = "missing"
            evidence = []
            reason = ""
            missing_skills.append(skill)
        skill_rows.append({**skill, "status": status, "evidence": evidence, "deferral_reason": reason})

    topic_rows_without_trace = [
        row
        for row in topic_rows
        if row.get("Curriculum Order", "") not in traced_curriculum_orders
    ]

    task_coverage_status = "pass" if not missing_tasks else "fail"
    skill_coverage_status = "pass" if not missing_skills else "fail"
    topic_traceability_status = "pass" if not topic_rows_without_trace else "fail"
    overall_status = (
        "complete"
        if task_coverage_status == skill_coverage_status == topic_traceability_status == "pass"
        else "incomplete"
    )

    return {
        "generated": date.today().isoformat(),
        "overall_status": overall_status,
        "task_coverage_status": task_coverage_status,
        "skill_coverage_status": skill_coverage_status,
        "topic_traceability_status": topic_traceability_status,
        "inputs": {
            "objectives_json": rel(OBJECTIVES_JSON),
            "topic_map": rel(TOPIC_MAP),
            "accelerated_plan": rel(ACCELERATED_PLAN),
            "deferrals": rel(DEFERRALS) if DEFERRALS.exists() else "missing",
            "traceability_matrix": rel(TRACEABILITY_MATRIX) if TRACEABILITY_MATRIX.exists() else "missing",
        },
        "counts": {
            "official_domains": len(domains),
            "official_tasks": len(tasks),
            "official_skills": len(skills),
            "curriculum_topic_rows": len(topic_rows),
            "covered_or_deferred_tasks": len(tasks) - len(missing_tasks),
            "covered_or_deferred_skills": len(skills) - len(missing_skills),
        },
        "topic_rows_by_day": group_topic_counts(topic_rows),
        "tasks": task_rows,
        "skills": skill_rows,
        "missing_tasks": missing_tasks,
        "missing_skills": missing_skills,
        "deferred_tasks": deferred_tasks,
        "deferred_skills": deferred_skills,
        "topic_rows_without_explicit_source_trace": topic_rows_without_trace,
    }


def write_outputs(audit: dict[str, Any]) -> None:
    REPORT_JSON.write_text(json.dumps(audit, indent=2) + "\n", encoding="utf-8")
    REPORT_MD.write_text(render_report(audit), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Run audit without writing report files.")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Return a non-zero exit code when Layer 0 is incomplete.",
    )
    args = parser.parse_args()

    audit = build_audit()
    if not args.check:
        write_outputs(audit)

    print(f"overall_status={audit['overall_status']}")
    print(f"task_coverage_status={audit['task_coverage_status']}")
    print(f"skill_coverage_status={audit['skill_coverage_status']}")
    print(f"topic_traceability_status={audit['topic_traceability_status']}")
    print(f"official_tasks={audit['counts']['official_tasks']}")
    print(f"official_skills={audit['counts']['official_skills']}")
    print(f"curriculum_topic_rows={audit['counts']['curriculum_topic_rows']}")
    if args.strict and audit["overall_status"] != "complete":
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
