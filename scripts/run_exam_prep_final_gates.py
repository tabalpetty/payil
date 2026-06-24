#!/usr/bin/env python3
"""Run final exam-prep gates for a reviewed question bank."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PILOT = ROOT / "docs/Pilot1/aip-c01"
EXAM_PREP = PILOT / "exam-prep"
OBJECTIVES_JSON = PILOT / "source-material/ai-professional-01.objectives.json"
TRACEABILITY_MATRIX = PILOT / "curriculum-model/source-to-topic-traceability-matrix.md"


def day_slug(day: int) -> str:
    return f"day-{day:02d}"


def reviewed_dir(day: int) -> Path:
    return EXAM_PREP / f"reviewed/{day_slug(day)}"


def reviewed_bank_path(day: int) -> Path:
    return reviewed_dir(day) / f"{day_slug(day)}-reviewed-question-bank.md"


def cull_log_path(day: int) -> Path:
    return reviewed_dir(day) / f"{day_slug(day)}-cull-log.md"


def review_checks_path(day: int) -> Path:
    return reviewed_dir(day) / f"{day_slug(day)}-review-output-checks.json"


def report_path(day: int) -> Path:
    return reviewed_dir(day) / f"{day_slug(day)}-final-gate-report.md"


def report_json_path(day: int) -> Path:
    return reviewed_dir(day) / f"{day_slug(day)}-final-gates.json"


def logs_dir(day: int) -> Path:
    return EXAM_PREP / f"logs/{day_slug(day)}"


def topic_brief_dir(day: int) -> Path:
    return EXAM_PREP / f"topic-briefs/{day_slug(day)}"


REJECTED_OUTPUT_PATTERNS = [
    "as of early 2024",
    "no current support",
    "does not currently",
    "does not yet",
    "currently does not",
    "sagemaker studio classic",
    "what is the most suitable service",
    "which aws service",
]


def parse_items(text: str) -> list[str]:
    reviewed_section = section(text, "Reviewed Items", [])
    blocks = re.split(r"(?m)^### ", reviewed_section)
    return ["### " + block.strip() + "\n" for block in blocks[1:] if block.strip()]


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


def load_objectives() -> tuple[set[str], set[str], set[str]]:
    data = json.loads(OBJECTIVES_JSON.read_text(encoding="utf-8"))
    domains: set[str] = set()
    tasks: set[str] = set()
    skills: set[str] = set()
    for domain in data.get("domains", []):
        domains.add(domain["domain"])
        for task in domain.get("tasks", []):
            tasks.add(task["task"])
            for skill in task.get("skills", []):
                skills.add(skill["skill"])
    return domains, tasks, skills


def path_exists(value: str) -> bool:
    stripped = value.strip().strip("`")
    if not stripped.startswith("docs/"):
        return False
    return (ROOT / stripped).exists()


def remediation_paths(item: str) -> list[str]:
    block = extract_block(item, "Remediation target:", ["### "])
    paths = re.findall(r"docs/[^\s`]+", block)
    return [path.rstrip(".,);") for path in paths]


def source_trace(item: str) -> str:
    return extract_block(item, "Source trace:", ["Remediation target:", "### "])


def normalized_answer(value: str) -> str:
    value = re.sub(r"^\s*(?:option\s*)?\d+[.):\-]\s*", "", value, flags=re.IGNORECASE)
    value = re.sub(r"\s+", " ", value).strip().rstrip(".")
    return value.casefold()


def correct_answer_index(item: str, question_format: str) -> str:
    options_block = extract_block(item, "Options:", ["Correct answer:"])
    correct = extract_block(item, "Correct answer:", ["Rationale:"])
    if not correct:
        return "missing"
    if question_format == "multiple-response":
        return "multiple-response"
    options = []
    for line in options_block.splitlines():
        match = re.match(r"(\d+)\.\s+(.*)", line.strip())
        if match:
            options.append((int(match.group(1)), match.group(2).strip()))
    for index, option in options:
        if normalized_answer(option) == normalized_answer(correct):
            return str(index)
    return "not-matched"


def raw_response_records(day: int) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    raw_directory = EXAM_PREP / f"raw/{day_slug(day)}"
    for path in sorted(raw_directory.glob("*-openai-*.md")):
        text = path.read_text(encoding="utf-8")
        metadata_match = re.search(r"## Metadata\s+```json\s+(.*?)\s+```", text, re.DOTALL)
        response_match = re.search(r"## Raw Response JSON\s+```json\s+(.*?)\s+```", text, re.DOTALL)
        if not metadata_match or not response_match:
            continue
        try:
            metadata = json.loads(metadata_match.group(1))
            response = json.loads(response_match.group(1))
        except json.JSONDecodeError:
            continue
        usage = response.get("usage", {})
        output_text = section(text, "Raw Response Text", ["Raw Response JSON"])
        records.append(
            {
                "raw_source": path.name,
                "run_id": metadata.get("run_id"),
                "candidate_count": len(re.findall(r'"stem"\s*:', output_text)),
                "input_tokens": usage.get("input_tokens") or 0,
                "output_tokens": usage.get("output_tokens") or 0,
                "total_tokens": usage.get("total_tokens") or 0,
            }
        )
    return records


def cost_summary(day: int, fields: list[dict[str, str]]) -> dict[str, Any]:
    calls = raw_response_records(day)
    totals = Counter()
    for call in calls:
        for key in ["input_tokens", "output_tokens", "total_tokens", "candidate_count"]:
            totals[key] += int(call[key] or 0)
    used_external_sources = {
        field.get("raw_source", "").split(" item ", 1)[0]
        for field in fields
        if field.get("raw_provider") == "openai"
    }
    metered_sources = {call["raw_source"] for call in calls}
    missing_telemetry = sorted(source for source in used_external_sources if source not in metered_sources)
    return {
        "api_calls": len(calls),
        "token_totals": dict(totals),
        "calls": calls,
        "used_external_raw_sources": len(used_external_sources),
        "missing_telemetry": missing_telemetry,
        "telemetry_complete": not missing_telemetry,
    }


def mapped_skills_by_topic(day: int) -> dict[str, set[str]]:
    result: dict[str, set[str]] = defaultdict(set)
    if not TRACEABILITY_MATRIX.exists():
        return result
    for line in TRACEABILITY_MATRIX.read_text(encoding="utf-8").splitlines():
        order_match = re.search(rf"\|\s*(Day{day:02d}-order\d{{3}})\s*\|", line)
        skill_match = re.search(r"\|\s*(\d+\.\d+\.\d+)\s*\|", line)
        if order_match and skill_match:
            result[order_match.group(1)].add(skill_match.group(1))
    return result


def topic_counts_by_skill() -> Counter[str]:
    counts: Counter[str] = Counter()
    if not TRACEABILITY_MATRIX.exists():
        return counts
    for line in TRACEABILITY_MATRIX.read_text(encoding="utf-8").splitlines():
        skill_match = re.search(r"\|\s*(\d+\.\d+\.\d+)\s*\|", line)
        order_match = re.search(r"\|\s*(Day\d{2}-order\d{3})\s*\|", line)
        if skill_match and order_match:
            counts[skill_match.group(1)] += 1
    return counts


def skill_id(value: str) -> str:
    match = re.search(r"\bSkill\s+(\d+\.\d+\.\d+)\b", value)
    return match.group(1) if match else ""


def iteration_summary(day: int) -> dict[str, Any]:
    observed = 0
    configured_limits: list[int] = []
    blocked = False
    for path in sorted(logs_dir(day).glob("*-topup-loop.jsonl")):
        for line in path.read_text(encoding="utf-8").splitlines():
            try:
                record = json.loads(line)
            except json.JSONDecodeError:
                continue
            if record.get("event") == "loop-start":
                configured_limits.append(int(record.get("max_iterations", 0)))
            if record.get("event") == "iteration-start":
                observed = max(observed, int(record.get("iteration", 0)))
            if record.get("event") == "loop-blocked":
                blocked = True
    configured = max(configured_limits, default=3)
    return {
        "observed_iterations": observed,
        "configured_max_iterations": configured,
        "blocked": blocked,
        "within_limit": not blocked and observed <= configured,
    }


def teaching_substrate_check(day: int) -> tuple[bool, list[str]]:
    missing: list[str] = []
    directory = topic_brief_dir(day)
    if not directory.exists():
        return False, [str(directory.relative_to(ROOT))]
    briefs = sorted(directory.glob(f"day{day:02d}-order*-topic-brief.md"))
    if not briefs:
        return False, [str(directory.relative_to(ROOT))]
    for brief in briefs:
        text = brief.read_text(encoding="utf-8")
        for label in ["Study guide", "Focused artifact", "Answer guidance"]:
            match = re.search(rf"^- {re.escape(label)}: `(?P<path>.+?)`$", text, re.MULTILINE)
            if not match or not (ROOT / match.group("path")).exists():
                missing.append(f"{brief.name}: {label}")
    return not missing, missing


def approved_output_regressions(items: list[str]) -> list[str]:
    regressions: list[str] = []
    for index, item in enumerate(items, 1):
        fields = parse_fields(item)
        item_id = fields.get("item_id", f"item-{index}")
        body_parts = [
            extract_block(item, "Stem:", ["Options:"]),
            extract_block(item, "Options:", ["Correct answer:"]),
            extract_block(item, "Correct answer:", ["Rationale:"]),
            extract_block(item, "Rationale:", ["Distractors:"]),
            extract_block(item, "Distractors:", ["Misconception tags:"]),
        ]
        body = " ".join(body_parts).lower()
        for pattern in REJECTED_OUTPUT_PATTERNS:
            if pattern in body:
                regressions.append(f"{item_id}: {pattern}")
    return regressions


def run_gates(day: int, target: int) -> dict[str, Any]:
    bank = reviewed_bank_path(day)
    checks = review_checks_path(day)
    culls = cull_log_path(day)
    if not bank.exists():
        raise SystemExit(f"Missing reviewed bank: {bank}")
    if not checks.exists():
        raise SystemExit(f"Missing Step 12 checks: {checks}")
    if not culls.exists():
        raise SystemExit(f"Missing cull log: {culls}")

    bank_text = bank.read_text(encoding="utf-8")
    items = parse_items(bank_text)
    fields = [parse_fields(item) for item in items]
    domains, tasks, skills = load_objectives()
    step12 = json.loads(checks.read_text(encoding="utf-8"))

    per_topic = Counter(field.get("learning_unit", "MISSING") for field in fields)
    difficulty = Counter(field.get("difficulty", "MISSING") for field in fields)
    format_counts = Counter(field.get("question_format", "MISSING") for field in fields)
    cognitive = Counter(field.get("cognitive_demand", "MISSING") for field in fields)
    source_status = Counter(field.get("source_trace_status", "MISSING") for field in fields)
    answer_positions = Counter(
        correct_answer_index(item, field.get("question_format", ""))
        for item, field in zip(items, fields)
    )
    teaching_ok, teaching_missing = teaching_substrate_check(day)
    approved_regressions = approved_output_regressions(items)

    objective_mismatches = []
    remediation_missing = []
    source_trace_missing = []
    topic_skill_mismatches = []
    skills_tested_by_topic: dict[str, set[str]] = defaultdict(set)
    mapped_skills = mapped_skills_by_topic(day)
    global_skill_topic_counts = topic_counts_by_skill()
    for index, (item, field) in enumerate(zip(items, fields), 1):
        item_id = field.get("item_id", f"item-{index}")
        if field.get("exam_domain") not in domains:
            objective_mismatches.append(f"{item_id}: exam_domain")
        if field.get("exam_task") not in tasks:
            objective_mismatches.append(f"{item_id}: exam_task")
        if field.get("exam_skill") not in skills:
            objective_mismatches.append(f"{item_id}: exam_skill")
        item_skill = skill_id(field.get("exam_skill", ""))
        topic = field.get("learning_unit", "")
        if item_skill:
            skills_tested_by_topic[topic].add(item_skill)
        if topic in mapped_skills and item_skill not in mapped_skills[topic]:
            topic_skill_mismatches.append(
                f"{item_id}: {topic} does not map to Skill {item_skill}"
            )

        paths = remediation_paths(item)
        if not paths or any(not path_exists(path) for path in paths):
            remediation_missing.append(item_id)
        trace = source_trace(item)
        if not trace or trace == "MISSING":
            source_trace_missing.append(item_id)

    short_topics = {topic: count for topic, count in sorted(per_topic.items()) if count < target}
    missing_mapped_skills = {
        topic: sorted(expected - skills_tested_by_topic.get(topic, set()))
        for topic, expected in sorted(mapped_skills.items())
        if expected - skills_tested_by_topic.get(topic, set())
    }
    must_not_drift_skills = sorted(
        {
            skill
            for expected in mapped_skills.values()
            for skill in expected
            if global_skill_topic_counts[skill] == 1
        }
    )
    final_source_pending = any(status != "source-verified" for status in source_status)
    cost = cost_summary(day, fields)
    iteration = iteration_summary(day)
    single_answer_positions = {
        position: count
        for position, count in answer_positions.items()
        if position in {"1", "2", "3", "4", "5"}
    }
    single_answer_total = sum(single_answer_positions.values())
    max_position_share = (
        max(single_answer_positions.values(), default=0) / single_answer_total
        if single_answer_total
        else 1.0
    )
    position_ok = (
        answer_positions.get("not-matched", 0) == 0
        and answer_positions.get("missing", 0) == 0
        and len(single_answer_positions) >= 3
        and max_position_share <= 0.50
    )

    gates = {
        "teaching_substrate_gate": "pass" if teaching_ok else "fail",
        "source_objective_gate": "pass" if OBJECTIVES_JSON.exists() and not objective_mismatches else "fail",
        "raw_provenance_gate": "pass" if all(field.get("raw_provider") and field.get("raw_model") for field in fields) else "fail",
        "schema_gate": "pass" if step12["checks"]["required_fields_present"] else "fail",
        "traceability_gate": "pass" if not objective_mismatches and not remediation_missing and not source_trace_missing and not topic_skill_mismatches else "fail",
        "factual_verification_gate": "pending" if final_source_pending else "pass",
        "review_evidence_gate": "pass" if step12["checks"]["cull_evidence_present"] else "fail",
        "coverage_gate": "pass" if not short_topics and not missing_mapped_skills else "fail",
        "distribution_gate": "pass" if len(difficulty) >= 2 and len(cognitive) >= 4 and "multiple-response" in format_counts and position_ok else "fail",
        "approved_output_gate": "pass" if not approved_regressions else "fail",
        "cost_gate": "pass" if cost["telemetry_complete"] else "fail",
        "iteration_gate": "pass" if iteration["within_limit"] else "fail",
        "human_resolution_gate": "pending" if final_source_pending else "pass",
    }

    blockers = [
        gate for gate, status in gates.items() if status == "fail"
    ]
    pending = [
        gate for gate, status in gates.items() if status in {"pending", "review", "not-run-by-final-gate-script"}
    ]

    return {
        "day": day,
        "generated": date.today().isoformat(),
        "target_per_topic": target,
        "reviewed_item_count": len(items),
        "gate_status": gates,
        "blockers": blockers,
        "pending_items": pending,
        "per_topic_counts": dict(sorted(per_topic.items())),
        "difficulty_counts": dict(difficulty),
        "question_format_counts": dict(format_counts),
        "cognitive_demand_counts": dict(cognitive),
        "answer_position_counts": dict(answer_positions),
        "answer_position_max_share": round(max_position_share, 4),
        "source_trace_status_counts": dict(source_status),
        "objective_mismatches": objective_mismatches,
        "topic_skill_mismatches": topic_skill_mismatches,
        "missing_mapped_skills": missing_mapped_skills,
        "must_not_drift_skills": must_not_drift_skills,
        "remediation_missing": remediation_missing,
        "source_trace_missing": source_trace_missing,
        "teaching_substrate_missing": teaching_missing,
        "approved_output_regressions": approved_regressions,
        "cost_summary": cost,
        "iteration_summary": iteration,
        "completion_status": "blocked" if blockers else ("pending-final-source-verification" if pending else "complete"),
    }


def render_report(result: dict[str, Any]) -> str:
    gates = result["gate_status"]
    lines = [
        f"# Day {result['day']} Final Gate Report",
        "",
        f"Generated: {result['generated']}",
        "",
        f"Completion status: `{result['completion_status']}`",
        "",
        "## Gate Summary",
        "",
        "| Gate | Status |",
        "|---|---|",
    ]
    for gate, status in gates.items():
        lines.append(f"| {gate} | {status} |")

    lines.extend(
        [
            "",
            "## Coverage",
            "",
            "| Curriculum order | Reviewed count | Target | Status |",
            "|---|---:|---:|---|",
        ]
    )
    for topic, count in result["per_topic_counts"].items():
        lines.append(f"| {topic} | {count} | {result['target_per_topic']} | {'pass' if count >= result['target_per_topic'] else 'fail'} |")

    lines.extend(
        [
            "",
            "## Distribution",
            "",
            f"- Difficulty: `{result['difficulty_counts']}`",
            f"- Question format: `{result['question_format_counts']}`",
            f"- Cognitive demand: `{result['cognitive_demand_counts']}`",
            f"- Answer positions: `{result['answer_position_counts']}`",
            f"- Maximum single-answer position share: `{result['answer_position_max_share']}`",
            "",
            "## Traceability",
            "",
            f"- Objective mismatches: `{result['objective_mismatches'] or 'none'}`",
            f"- Missing remediation targets: `{result['remediation_missing'] or 'none'}`",
            f"- Missing source traces: `{result['source_trace_missing'] or 'none'}`",
            f"- Topic/skill mismatches: `{result['topic_skill_mismatches'] or 'none'}`",
            f"- Missing mapped skills: `{result['missing_mapped_skills'] or 'none'}`",
            f"- Source trace status: `{result['source_trace_status_counts']}`",
            f"- Teaching substrate missing: `{result['teaching_substrate_missing'] or 'none'}`",
            f"- Approved-output regressions: `{result['approved_output_regressions'] or 'none'}`",
            "",
            "## Cost Summary",
            "",
            f"- API calls recorded: `{result['cost_summary']['api_calls']}`",
            f"- Token totals: `{result['cost_summary']['token_totals']}`",
            f"- Missing cost telemetry: `{result['cost_summary']['missing_telemetry'] or 'none'}`",
            f"- Iteration summary: `{result['iteration_summary']}`",
            "",
            "Dollar cost is not estimated here because no versioned model-price table",
            "is configured in the repository. Token usage is recorded for budget",
            "reconciliation.",
            "",
            "## Remaining Work",
            "",
        ]
    )
    if result["blockers"]:
        lines.append(f"- Blockers: `{result['blockers']}`")
    if result["pending_items"]:
        lines.append(f"- Pending gates: `{result['pending_items']}`")
    if not result["blockers"] and not result["pending_items"]:
        lines.append("- No remaining final-gate work.")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--day", type=int, required=True, choices=range(1, 8))
    parser.add_argument("--target", type=int, default=10)
    args = parser.parse_args()

    result = run_gates(args.day, args.target)
    report_path(args.day).write_text(render_report(result), encoding="utf-8")
    report_json_path(args.day).write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(f"final_gate_report={report_path(args.day).relative_to(ROOT)}")
    print(f"final_gates_json={report_json_path(args.day).relative_to(ROOT)}")
    print(f"completion_status={result['completion_status']}")
    return 0 if not result["blockers"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
