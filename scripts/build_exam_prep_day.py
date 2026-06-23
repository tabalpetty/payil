#!/usr/bin/env python3
"""Build exam-prep agent planning artifacts for a curriculum day.

The first implementation slice is Step 4 of the agent build: convert existing
curriculum-map rows into exam-prep topic briefs. This is deterministic and does
not call an LLM or approve question-bank items.
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PILOT = ROOT / "docs/Pilot1/aip-c01"
MAP_PATH = PILOT / "curriculum-model/aip-c01-topic-knowledge-category-map.md"
EXAM_PREP = PILOT / "exam-prep"
STUDENT_KIT = PILOT / "student-kit/accelerated-7-day"
SOURCE_PDF = PILOT / "source-material/ai-professional-01.pdf"
SOURCE_TRANSCRIPT = PILOT / "source-material/ai-professional-01.extracted.md"
SOURCE_OBJECTIVES = PILOT / "source-material/ai-professional-01.objectives.json"

DAY_STUDY_GUIDES = {
    1: STUDENT_KIT / "study-guides/day-01-foundations-system-map-invocation-prompt.md",
    2: STUDENT_KIT / "study-guides/day-02-data-embeddings-vector-stores-rag.md",
    3: STUDENT_KIT / "study-guides/day-03-advanced-retrieval-prompt-governance-api-resilience.md",
    4: STUDENT_KIT / "study-guides/day-04-deployment-model-routing-enterprise-agents.md",
    5: STUDENT_KIT / "study-guides/day-05-safety-security-privacy-governance.md",
    6: STUDENT_KIT / "study-guides/day-06-optimization-monitoring-evaluation-troubleshooting.md",
    7: STUDENT_KIT / "study-guides/day-07-integration-exam-readiness.md",
}


@dataclass(frozen=True)
class TopicRow:
    order: str
    section: str
    topic: str
    category: str
    knowledge_type: str
    artifact_to_create: str


@dataclass(frozen=True)
class TopicBrief:
    row: TopicRow
    study_guide: Path
    artifact: Path | None
    answer_guidance: Path | None
    output_path: Path


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def day_label(day: int) -> str:
    return f"Day{day:02d}"


def day_slug(day: int) -> str:
    return f"day-{day:02d}"


def parse_table_row(line: str) -> list[str] | None:
    stripped = line.strip()
    if not stripped.startswith("|") or not stripped.endswith("|"):
        return None
    cells = [cell.strip() for cell in stripped.strip("|").split("|")]
    if len(cells) != 6:
        return None
    if cells[0] in {"Curriculum Order", "---"} or set(cells[0]) <= {"-", ":"}:
        return None
    return cells


def load_map_rows() -> list[TopicRow]:
    if not MAP_PATH.exists():
        raise SystemExit(f"Missing curriculum map: {MAP_PATH}")

    rows: list[TopicRow] = []
    for line in MAP_PATH.read_text(encoding="utf-8").splitlines():
        cells = parse_table_row(line)
        if not cells:
            continue
        rows.append(TopicRow(*cells))
    return rows


def rows_for_day(day: int) -> list[TopicRow]:
    prefix = f"{day_label(day)}-"
    rows = [row for row in load_map_rows() if row.order.startswith(prefix)]
    if not rows:
        raise SystemExit(f"No curriculum-map rows found for {day_label(day)}")
    return rows


def artifact_dir(day: int) -> Path:
    return STUDENT_KIT / f"{day_slug(day)}-artifacts"


def find_artifact(day: int, order: str) -> Path | None:
    candidates = sorted(artifact_dir(day).glob(f"{order.lower()}-*.md"))
    return candidates[0] if candidates else None


def answer_guidance(day: int) -> Path | None:
    path = artifact_dir(day) / f"{day_slug(day)}-answer-guidance.md"
    return path if path.exists() else None


def output_dir(day: int) -> Path:
    return EXAM_PREP / f"topic-briefs/{day_slug(day)}"


def brief_path(day: int, order: str) -> Path:
    return output_dir(day) / f"{order.lower()}-topic-brief.md"


def question_focus_for_types(knowledge_type: str) -> list[str]:
    lowered = knowledge_type.lower()
    focus: list[str] = []
    if "declarative" in lowered:
        focus.append("Test necessary recall only inside a scenario; avoid glossary-only stems.")
    if "conceptual" in lowered:
        focus.append("Ask the learner to explain relationships, boundaries, or system roles.")
    if "procedural" in lowered:
        focus.append("Ask for next step, runbook step, configuration choice, or failure-handling action.")
    if "conditional" in lowered:
        focus.append("Ask when to choose or reject an approach based on scenario constraints.")
    if "causal" in lowered:
        focus.append("Ask the learner to predict effects or diagnose cause from symptoms.")
    if "strategic" in lowered:
        focus.append("Ask for tradeoff, architecture decision, or defended plan.")
    if "embedded" in lowered:
        focus.append("Include platform/tool/API/configuration evidence where relevant.")
    if "normative" in lowered:
        focus.append("Ask for control placement, policy/risk judgment, or responsible practice.")
    if not focus:
        focus.append("Create scenario-based items that match the mapped knowledge type.")
    return focus


def misconception_prompts(row: TopicRow) -> list[str]:
    topic = row.topic.lower()
    prompts = [
        "Confusing a tool or service with the full architecture.",
        "Selecting a plausible option without checking the scenario constraint.",
    ]
    if "rag" in topic or "retrieval" in topic:
        prompts.append("Assuming RAG means the model searches documents by itself.")
    if "metadata" in topic:
        prompts.append("Treating metadata as decoration instead of a filtering/security control.")
    if "chunk" in topic:
        prompts.append("Assuming one chunk size works for every source document.")
    if "embedding" in topic or "vector" in topic:
        prompts.append("Assuming embeddings enforce authorization, freshness, or source authority.")
    if "data-quality" in topic or "preprocessing" in topic:
        prompts.append("Blaming the model before inspecting data quality or extraction.")
    return prompts


def render_brief(brief: TopicBrief, day: int) -> str:
    row = brief.row
    study = rel(brief.study_guide)
    artifact = rel(brief.artifact) if brief.artifact else "MISSING"
    guidance = rel(brief.answer_guidance) if brief.answer_guidance else "MISSING"
    source_pdf = rel(SOURCE_PDF) if SOURCE_PDF.exists() else "MISSING"
    source_transcript = rel(SOURCE_TRANSCRIPT) if SOURCE_TRANSCRIPT.exists() else "MISSING"
    source_objectives = rel(SOURCE_OBJECTIVES) if SOURCE_OBJECTIVES.exists() else "MISSING"
    generated = date.today().isoformat()
    focus = "\n".join(f"- {item}" for item in question_focus_for_types(row.knowledge_type))
    misconceptions = "\n".join(f"- {item}" for item in misconception_prompts(row))

    return "\n".join(
        [
            f"# Topic Brief: {row.order}",
            "",
            "## Metadata",
            "",
            "| Field | Value |",
            "|---|---|",
            f"| Curriculum order | {row.order} |",
            f"| Accelerated day | Day {day} |",
            f"| Section | {row.section} |",
            f"| Topic | {row.topic} |",
            f"| Knowledge category | {row.category} |",
            f"| Knowledge type | {row.knowledge_type} |",
            f"| Artifact to create | {row.artifact_to_create} |",
            f"| Generated | {generated} |",
            "",
            "## Teaching And Remediation Sources",
            "",
            f"- Study guide: `{study}`",
            f"- Focused artifact: `{artifact}`",
            f"- Answer guidance: `{guidance}`",
            f"- Official objectives JSON: `{source_objectives}`",
            f"- Official exam guide transcript: `{source_transcript}`",
            f"- Official exam guide PDF: `{source_pdf}`",
            "",
            "## Official Objective Mapping",
            "",
            "- Status: `needs-objective-mapping`",
            "- Required before generation: official `exam_domain`, `exam_task`, and `exam_skill` from the AIP-C01 objectives JSON.",
            "- Rule: do not invent official objective tags in candidate items.",
            "",
            "## Question Focus",
            "",
            focus,
            "",
            "## Misconceptions And Traps To Test",
            "",
            misconceptions,
            "",
            "## Raw Candidate Guidance",
            "",
            "- Generate scenario-based, professional-level draft items.",
            "- Include a concrete actor, workload, constraint, and tradeoff.",
            "- Include plausible distractors with rationales.",
            "- Mark source-sensitive technical claims for verification.",
            "- Route misses to the study guide, focused artifact, or answer guidance listed above.",
            "",
            "## Readiness Notes",
            "",
            "- This brief is ready for prompt planning after official objective mapping is filled.",
            "- If any teaching/remediation source above is `MISSING`, generation must stop for this topic.",
            "",
        ]
    )


def build_briefs(day: int, write: bool, force: bool = False) -> tuple[list[TopicBrief], int, int]:
    rows = rows_for_day(day)
    study = DAY_STUDY_GUIDES.get(day)
    if study is None:
        raise SystemExit(f"No study-guide path configured for Day {day}")

    guidance = answer_guidance(day)
    briefs: list[TopicBrief] = []
    for row in rows:
        briefs.append(
            TopicBrief(
                row=row,
                study_guide=study,
                artifact=find_artifact(day, row.order),
                answer_guidance=guidance,
                output_path=brief_path(day, row.order),
            )
        )

    written = 0
    skipped = 0

    if write:
        out_dir = output_dir(day)
        out_dir.mkdir(parents=True, exist_ok=True)
        for brief in briefs:
            if brief.output_path.exists() and not force:
                existing = brief.output_path.read_text(encoding="utf-8")
                if "- Status: `mapped`" in existing:
                    skipped += 1
                    continue
            brief.output_path.write_text(render_brief(brief, day), encoding="utf-8")
            written += 1
        readme = out_dir / "README.md"
        if force or not readme.exists():
            readme.write_text(render_readme(briefs, day), encoding="utf-8")

    return briefs, written, skipped


def status(value: bool) -> str:
    return "OK" if value else "MISSING"


def render_readme(briefs: list[TopicBrief], day: int) -> str:
    rows = [
        "# Day {day} Exam-Prep Topic Briefs".format(day=day),
        "",
        "## Purpose",
        "",
        "These briefs convert the curriculum map into exam-prep planning inputs.",
        "They do not approve question-bank items and they do not call an LLM.",
        "",
        "## Brief Index",
        "",
        "| Curriculum order | Topic | Brief | Artifact |",
        "|---|---|---|---|",
    ]
    for brief in briefs:
        artifact = rel(brief.artifact) if brief.artifact else "MISSING"
        rows.append(
            f"| {brief.row.order} | {brief.row.topic} | "
            f"[{brief.output_path.name}]({brief.output_path.name}) | `{artifact}` |"
        )
    rows.extend(
        [
            "",
            "## Readiness Summary",
            "",
            "| Check | Status |",
            "|---|---|",
            f"| Study guide exists | {status(briefs[0].study_guide.exists())} |",
            f"| Answer guidance exists | {status(bool(briefs[0].answer_guidance and briefs[0].answer_guidance.exists()))} |",
            f"| Focused artifacts exist | {status(all(brief.artifact and brief.artifact.exists() for brief in briefs))} |",
            f"| Official objectives JSON exists | {status(SOURCE_OBJECTIVES.exists())} |",
            f"| Official exam guide transcript exists | {status(SOURCE_TRANSCRIPT.exists())} |",
            f"| Official exam guide PDF exists | {status(SOURCE_PDF.exists())} |",
            "| Official objective mapping filled | NEEDS WORK |",
            "",
            "## Next Required Work",
            "",
            "Fill official `exam_domain`, `exam_task`, and `exam_skill` mappings from the objectives JSON before using these briefs for candidate generation.",
            "",
        ]
    )
    return "\n".join(rows)


def print_plan(briefs: list[TopicBrief], day: int) -> None:
    print(f"Day {day} topic briefs: {len(briefs)}")
    print(f"Output directory: {rel(output_dir(day))}")
    print()
    print("| Curriculum order | Topic | Study guide | Artifact | Answer guidance | Brief |")
    print("|---|---|---|---|---|---|")
    for brief in briefs:
        print(
            "| {order} | {topic} | {study} | {artifact} | {guidance} | {out} |".format(
                order=brief.row.order,
                topic=brief.row.topic,
                study=status(brief.study_guide.exists()),
                artifact=status(bool(brief.artifact and brief.artifact.exists())),
                guidance=status(bool(brief.answer_guidance and brief.answer_guidance.exists())),
                out=rel(brief.output_path),
            )
        )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--day", type=int, required=True, choices=range(1, 8), help="Accelerated day number.")
    parser.add_argument(
        "--plan",
        action="store_true",
        help="Write topic briefs and print the readiness plan.",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Print the readiness plan without writing files.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing mapped briefs. Use only when regenerating official mappings intentionally.",
    )
    args = parser.parse_args()

    write = args.plan
    if not args.plan and not args.check:
        parser.error("Use --plan to write briefs or --check to inspect readiness.")

    briefs, written, skipped = build_briefs(args.day, write=write, force=args.force)
    print_plan(briefs, args.day)
    if write:
        print()
        print(f"Wrote {written} briefs; skipped {skipped} already-mapped briefs.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
