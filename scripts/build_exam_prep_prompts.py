#!/usr/bin/env python3
"""Build day-specific exam-prep raw question-generation prompt packs.

This implements Step 6 of the exam-prep agent build. It reads mapped topic
briefs and writes a prompt pack. It does not call an LLM and does not approve
question-bank content.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PILOT = ROOT / "docs/Pilot1/aip-c01"
EXAM_PREP = PILOT / "exam-prep"
OBJECTIVES_JSON = PILOT / "source-material/ai-professional-01.objectives.json"
QUESTION_SPEC = EXAM_PREP / "question-bank-specification.md"


@dataclass(frozen=True)
class Brief:
    order: str
    day_number: int
    topic: str
    knowledge_category: str
    knowledge_type: str
    study_guide: str
    artifact: str
    answer_guidance: str
    exam_domain: str
    exam_task: str
    exam_skill: str
    secondary_exam_skills: str
    question_focus: list[str]
    misconceptions: list[str]
    path: Path


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def day_slug(day: int) -> str:
    return f"day-{day:02d}"


def topic_brief_dir(day: int) -> Path:
    return EXAM_PREP / f"topic-briefs/{day_slug(day)}"


def output_path(day: int) -> Path:
    return EXAM_PREP / f"{day_slug(day)}-question-generation-prompts.md"


def read_required(path: Path) -> str:
    if not path.exists():
        raise SystemExit(f"Missing required file: {path}")
    return path.read_text(encoding="utf-8")


def field(text: str, label: str) -> str:
    pattern = re.compile(rf"^\| {re.escape(label)} \| (?P<value>.*?) \|$", re.MULTILINE)
    match = pattern.search(text)
    if not match:
        raise SystemExit(f"Missing metadata field {label!r}")
    return match.group("value")


def bullet_value(text: str, label: str) -> str:
    pattern = re.compile(rf"^- `{re.escape(label)}`: (?P<value>.+)$", re.MULTILINE)
    match = pattern.search(text)
    if not match:
        raise SystemExit(f"Missing objective field {label!r}")
    return match.group("value")


def source_value(text: str, label: str) -> str:
    pattern = re.compile(rf"^- {re.escape(label)}: `(?P<value>.+?)`$", re.MULTILINE)
    match = pattern.search(text)
    if not match:
        raise SystemExit(f"Missing source field {label!r}")
    return match.group("value")


def section_bullets(text: str, heading: str) -> list[str]:
    pattern = re.compile(rf"^## {re.escape(heading)}\n\n(?P<body>.*?)(?=^## |\Z)", re.MULTILINE | re.DOTALL)
    match = pattern.search(text)
    if not match:
        raise SystemExit(f"Missing section {heading!r}")
    bullets = []
    for line in match.group("body").splitlines():
        if line.startswith("- "):
            bullets.append(line[2:].strip())
    return bullets


def parse_brief(path: Path) -> Brief:
    text = read_required(path)
    if "- Status: `mapped`" not in text:
        raise SystemExit(f"Brief is not mapped; cannot build prompts: {path}")

    order = field(text, "Curriculum order")
    day_field = field(text, "Accelerated day")
    day_match = re.search(r"Day (\d+)", day_field)
    if not day_match:
        raise SystemExit(f"Could not parse day number in {path}")

    return Brief(
        order=order,
        day_number=int(day_match.group(1)),
        topic=field(text, "Topic"),
        knowledge_category=field(text, "Knowledge category"),
        knowledge_type=field(text, "Knowledge type"),
        study_guide=source_value(text, "Study guide"),
        artifact=source_value(text, "Focused artifact"),
        answer_guidance=source_value(text, "Answer guidance"),
        exam_domain=bullet_value(text, "exam_domain"),
        exam_task=bullet_value(text, "exam_task"),
        exam_skill=bullet_value(text, "exam_skill"),
        secondary_exam_skills=bullet_value(text, "secondary_exam_skills"),
        question_focus=section_bullets(text, "Question Focus"),
        misconceptions=section_bullets(text, "Misconceptions And Traps To Test"),
        path=path,
    )


def load_briefs(day: int) -> list[Brief]:
    directory = topic_brief_dir(day)
    if not directory.exists():
        raise SystemExit(f"Missing topic-brief directory: {directory}")
    paths = sorted(directory.glob(f"day{day:02d}-order*-topic-brief.md"))
    if not paths:
        raise SystemExit(f"No topic briefs found in {directory}")
    briefs = [parse_brief(path) for path in paths]
    if any(brief.day_number != day for brief in briefs):
        raise SystemExit(f"One or more briefs do not match Day {day}")
    return briefs


def count_format_target(total: int) -> str:
    multiple_response = max(2, total // 4)
    multiple_choice = total - multiple_response
    return f"{multiple_choice} multiple-choice and {multiple_response} multiple-response"


def render_schema(day: int) -> str:
    return f"""## Output Schema Required From The LLM

Return a single JSON array. Each object must contain these fields:

| Field | Requirement |
|---|---|
| `status` | Always `draft`. |
| `official_exam_code` | Always `AIP-C01`. |
| `accelerated_day` | Always `Day {day}`. |
| `curriculum_order` | Exact curriculum-order value from the prompt. |
| `topic` | Exact topic name from the prompt. |
| `exam_domain` | Preserve the exact official value from the topic brief. |
| `exam_task` | Preserve the exact official value from the topic brief. |
| `exam_skill` | Preserve the exact official value from the topic brief. |
| `secondary_exam_skills` | Preserve the exact value from the topic brief. |
| `knowledge_category` | Exact knowledge category from the topic brief. |
| `knowledge_type` | Exact knowledge type from the topic brief. |
| `question_format` | `multiple-choice` or `multiple-response`. |
| `difficulty` | `medium`, `hard`, or `exam-plus`; do not generate `easy`. |
| `cognitive_demand` | Recall, explain, implement, integrate, configure, select, diagnose, optimize, compare, or judge. |
| `stem` | Scenario-based question stem. |
| `options` | Four options for multiple choice; five or more for multiple response. |
| `correct_answer` | Correct option or options. |
| `rationale_correct` | Why the correct answer is best. |
| `rationale_distractors` | Why each distractor is tempting but wrong or less appropriate. |
| `misconception_tags` | Trap, misconception, or tradeoff tested. |
| `source_trace_needed` | Specific AWS doc, objective, or project source that review must verify. |
| `remediation_target` | Existing study guide, focused artifact, or answer-guidance path from the topic brief. |
| `generation_notes` | Short note naming the scenario constraint and the quality risk the reviewer should inspect. |
"""


def render_guardrails(day: int) -> str:
    return f"""## Global Guardrails

Include this block in every prompt:

```text
Create original practice questions only. Do not copy official AWS practice
questions, exam dumps, proprietary question banks, or third-party copyrighted
questions. The questions are draft learning items and must be source-reviewed
before approval.

Use the official exam name: AWS Certified Generative AI Developer -
Professional (AIP-C01).

Use `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
as the canonical source for official objective values. Preserve `exam_domain`,
`exam_task`, and `exam_skill` exactly as given in the topic brief.

Make questions scenario-based. Avoid trivia unless the topic brief's knowledge
type is explicitly declarative and the item still tests the fact inside a
professional scenario. Include plausible distractors that test real
misconceptions. Prefer professional judgment over keyword matching.

Generated items are raw Day {day} candidates, not approved bank items.
```

## Question Quality Requirements

Include this block in every prompt:

```text
Question quality requirements:

- Generate tough, tricky, professional-level questions suitable for serious
  AIP-C01 preparation.
- At least 90% of generated items must be scenario-based.
- Include realistic distractors that are technically plausible but wrong
  because of a constraint, priority, AWS service boundary, operational risk,
  security issue, data-quality issue, retrieval failure, or misunderstanding.
- Avoid obvious answers, toy scenarios, and questions that can be answered by
  keyword matching.
- Include a mix of direct best-answer selection, best architecture/control,
  most likely failure/risk, first action, and multiple-response formats.
- Mark each question with difficulty: `medium`, `hard`, or `exam-plus`.
- For every distractor, explain why it is tempting and why it is wrong or less
  suitable.
- Do not use stale date-bound service claims such as "as of early 2024",
  "currently does not support", or "does not yet support".
- If an item depends on a fast-changing AWS service capability, write the item
  around the decision process and put the exact AWS documentation needed in
  `source_trace_needed`.
- Route misses to existing Day {day} remediation files only.
```

## Review Feedback Incorporated

These prompts intentionally incorporate the Day 1 lessons:

- prompt more raw candidates than the approved target because review will cull
  weak, duplicate, or unverifiable items;
- preserve official objective fields from the canonical objectives JSON;
- require source-sensitive claims to be marked for review;
- demand scenario constraints and distractor rationales;
- avoid recall-only, keyword-trivia, and stale service-capability claims;
- keep remediation targets tied to actual study guide, artifact, or answer
  guidance files.
"""


def render_scope(briefs: list[Brief], day: int) -> str:
    rows = "\n".join(f"| {brief.order} | {brief.topic} | {brief.exam_task} | {brief.exam_skill.split(':', 1)[0]} |" for brief in briefs)
    return f"""## Day {day} Scope

| Curriculum order | Topic | Official task | Primary skill |
|---|---|---|---|
{rows}
"""


def render_balanced_prompt(briefs: list[Brief], day: int, per_topic: int) -> str:
    total = len(briefs) * per_topic
    topic_list = "\n".join(f"{index}. {brief.order} - {brief.topic}" for index, brief in enumerate(briefs, start=1))
    return f"""## Prompt 1: Day {day} Balanced Full-Pool Draft

Use this prompt when you want the full Day {day} raw draft pool.

```text
Act as an expert AWS Certified Generative AI Developer - Professional
(AIP-C01) instructor and exam-item writer.

Generate {total} original draft practice questions for Day {day} of an
accelerated AIP-C01 curriculum.

Create exactly {per_topic} questions for each curriculum order:

{topic_list}

Use approximately {count_format_target(total)} questions across the whole
batch. At least {round(total * 0.9)} of the {total} questions must be
scenario-based. Make the questions tricky and professional-level, with
plausible distractors and detailed explanations.

Use the output schema specified above. Preserve all official objective fields
exactly from the topic briefs below.

Do not mark anything as approved.
```
"""


def render_topic_prompt(brief: Brief, per_topic: int) -> str:
    focus = "\n".join(f"- {item}" for item in brief.question_focus)
    misconceptions = "\n".join(f"- {item}" for item in brief.misconceptions)
    secondary = brief.secondary_exam_skills
    return f"""## Topic Prompt: {brief.order} {brief.topic}

Use this prompt for focused generation or top-up generation for `{brief.order}`.

```text
Act as an expert AWS Certified Generative AI Developer - Professional
(AIP-C01) instructor and exam-item writer.

Generate exactly {per_topic} original draft practice questions for:

- curriculum_order: {brief.order}
- topic: {brief.topic}
- accelerated_day: Day {brief.day_number}
- knowledge_category: {brief.knowledge_category}
- knowledge_type: {brief.knowledge_type}
- exam_domain: {brief.exam_domain}
- exam_task: {brief.exam_task}
- exam_skill: {brief.exam_skill}
- secondary_exam_skills: {secondary}

Question focus:
{focus}

Misconceptions and traps to test:
{misconceptions}

Required remediation targets. Use only these existing files:

- study_guide: {brief.study_guide}
- focused_artifact: {brief.artifact}
- answer_guidance: {brief.answer_guidance}

Generate approximately {count_format_target(per_topic)} items for this topic.
Every item must be scenario-based unless the item is testing a necessary
declarative fact inside a realistic work situation.

Preserve the official objective fields exactly. Do not invent, paraphrase, or
rename the official domain, task, or skill.

Return only a JSON array of draft items using the required schema.
```
"""


def render_prompt_pack(briefs: list[Brief], day: int, per_topic: int) -> str:
    title = f"# Day {day} Question Generation Prompts"
    sections = [
        title,
        "",
        "## Purpose",
        "",
        f"Use this prompt pack to generate **draft** AIP-C01 Day {day} practice questions.",
        "",
        "Generated questions are not approved question-bank items. Store raw responses first, then review them against:",
        "",
        "- `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`;",
        "- relevant official AWS documentation;",
        f"- the Day {day} study guide, focused artifacts, and answer guidance;",
        "- [question-bank-specification.md](question-bank-specification.md).",
        "",
        f"Default raw-generation target: `{per_topic}` candidates per topic. A complete reviewed bank still requires at least `10` approved items per curriculum-order topic after review.",
        "",
        render_scope(briefs, day),
        render_schema(day),
        render_guardrails(day),
        render_balanced_prompt(briefs, day, per_topic),
        "## Topic-Level Prompts",
        "",
    ]
    sections.extend(render_topic_prompt(brief, per_topic) for brief in briefs)
    return "\n".join(sections).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--day", type=int, required=True, choices=range(1, 8), help="Accelerated day number.")
    parser.add_argument("--per-topic", type=int, default=12, help="Raw candidates to request per topic.")
    parser.add_argument("--check", action="store_true", help="Validate inputs and print the output path without writing.")
    args = parser.parse_args()

    if not OBJECTIVES_JSON.exists():
        raise SystemExit(f"Missing canonical objectives JSON: {OBJECTIVES_JSON}")
    if not QUESTION_SPEC.exists():
        raise SystemExit(f"Missing question-bank specification: {QUESTION_SPEC}")

    briefs = load_briefs(args.day)
    output = output_path(args.day)
    prompt_pack = render_prompt_pack(briefs, args.day, args.per_topic)

    if args.check:
        print(f"Day {args.day} prompt pack would use {len(briefs)} mapped topic briefs.")
        print(f"Output path: {rel(output)}")
        print(f"Raw candidate target: {len(briefs) * args.per_topic}")
        return 0

    output.write_text(prompt_pack, encoding="utf-8")
    print(f"Wrote {rel(output)}")
    print(f"Prompt pack uses {len(briefs)} mapped topic briefs.")
    print(f"Raw candidate target: {len(briefs) * args.per_topic}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
