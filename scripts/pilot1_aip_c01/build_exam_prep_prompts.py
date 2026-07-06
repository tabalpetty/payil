#!/usr/bin/env python3
"""Build day-specific exam-prep raw question-generation prompt packs.

This implements Step 6 of the exam-prep agent build. It reads mapped topic
briefs and writes a prompt pack. It does not call an LLM and does not approve
question-bank content.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PILOT = ROOT / "docs/Pilot1/aip-c01"
EXAM_PREP = PILOT / "exam-prep"
OBJECTIVES_JSON = PILOT / "source-material/ai-professional-01.objectives.json"
QUESTION_SPEC = EXAM_PREP / "question-bank-specification.md"
TRACEABILITY_MATRIX = PILOT / "curriculum-model/source-to-topic-traceability-matrix.md"
SOURCE_CATALOG = EXAM_PREP / "source-catalog.json"


@dataclass(frozen=True)
class ObjectiveMapping:
    domain: str
    task: str
    skill: str


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
    objective_mappings: tuple[ObjectiveMapping, ...]
    allowed_sources: tuple[dict[str, str], ...]
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
        objective_mappings=(),
        allowed_sources=(),
        path=path,
    )


def load_source_catalog(day: int) -> dict[str, tuple[dict[str, str], ...]]:
    path = SOURCE_CATALOG
    if not path.exists():
        raise SystemExit(
            f"Missing course source catalog: {path}\n"
            "Create or update the course-level source catalog before building generation prompts."
        )
    data = json.loads(read_required(path))
    if data.get("contract_version") != "source-grounded-v1":
        raise SystemExit(f"Unsupported source catalog contract in {path}")
    topic_mappings = data.get("topic_mappings", {})
    source_registry = data.get("sources", {})
    result: dict[str, tuple[dict[str, str], ...]] = {}
    day_prefix = f"Day{day:02d}-"
    for order, payload in topic_mappings.items():
        if not order.startswith(day_prefix):
            continue
        source_ids = payload.get("allowed_source_ids", [])
        if not source_ids:
            raise SystemExit(f"Source catalog has no allowed_source_ids for {order}")
        normalized = []
        for source_id in source_ids:
            source = source_registry.get(source_id)
            if not source:
                raise SystemExit(f"Source catalog topic {order} references unknown source id: {source_id}")
            source_type = source.get("source_type")
            source_value = source.get("source")
            if not source_type or not source_value:
                raise SystemExit(f"Incomplete source catalog entry for {order}/{source_id}: {source}")
            if source_type == "local_teaching" and not (ROOT / source_value).exists():
                raise SystemExit(f"Local catalog source does not exist for {order}: {source_value}")
            if source_type == "aws_doc" and not source_value.startswith("https://docs.aws.amazon.com/"):
                raise SystemExit(f"AWS catalog source is not an AWS docs URL for {order}: {source_value}")
            normalized.append(
                {
                    "id": str(source_id),
                    "source_type": str(source_type),
                    "source": str(source_value),
                    "use_for": str(source.get("use_for", "")),
                }
            )
        result[order] = tuple(normalized)
    return result


def traceability_mappings() -> dict[str, tuple[ObjectiveMapping, ...]]:
    objectives = json.loads(read_required(OBJECTIVES_JSON))
    official_by_skill: dict[str, ObjectiveMapping] = {}
    for domain in objectives.get("domains", []):
        for task in domain.get("tasks", []):
            for skill in task.get("skills", []):
                official_by_skill[skill["skill_id"]] = ObjectiveMapping(
                    domain=domain["domain"],
                    task=task["task"],
                    skill=skill["skill"],
                )

    mappings: dict[str, list[ObjectiveMapping]] = {}
    for line in read_required(TRACEABILITY_MATRIX).splitlines():
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
        mappings.setdefault(order, []).append(official_by_skill[skill_id])
    return {
        order: tuple(dict.fromkeys(values))
        for order, values in mappings.items()
    }


def load_briefs(day: int) -> list[Brief]:
    directory = topic_brief_dir(day)
    if not directory.exists():
        raise SystemExit(f"Missing topic-brief directory: {directory}")
    paths = sorted(directory.glob(f"day{day:02d}-order*-topic-brief.md"))
    if not paths:
        raise SystemExit(f"No topic briefs found in {directory}")
    matrix = traceability_mappings()
    source_allowlist = load_source_catalog(day)
    briefs = []
    for path in paths:
        brief = parse_brief(path)
        mappings = matrix.get(brief.order, ())
        if not mappings:
            raise SystemExit(f"No official skill mapping for {brief.order} in {TRACEABILITY_MATRIX}")
        allowed_sources = source_allowlist.get(brief.order)
        if not allowed_sources:
            raise SystemExit(f"No source catalog mapping for {brief.order} in {SOURCE_CATALOG}")
        briefs.append(
            Brief(
                **{
                    **brief.__dict__,
                    "objective_mappings": mappings,
                    "allowed_sources": allowed_sources,
                }
            )
        )
    if any(brief.day_number != day for brief in briefs):
        raise SystemExit(f"One or more briefs do not match Day {day}")
    return briefs


def count_format_target(total: int) -> str:
    multiple_response = max(2, total // 4)
    multiple_choice = total - multiple_response
    return f"{multiple_choice} multiple-choice and {multiple_response} multiple-response"


def render_schema(day: int) -> str:
    return f"""## Lean Output Required From The LLM

Return a single JSON array. Each object must contain only the intellectually
important exam-item fields below. The repository normalizer will fill
mechanical curriculum metadata, IDs, remediation targets, status fields, and
source-contract fields after generation.

| Field | Requirement |
|---|---|
| `stem` | Scenario-based question stem. |
| `options` | Four options for multiple choice; five or more for multiple response. |
| `correct_answer` | Exact correct option text, or an array of exact option texts for multiple-response. Do not use numeric indexes. |
| `rationale_correct` | Why the correct answer is best for the scenario constraints. |
| `rationale_distractors` | Why each distractor is tempting but wrong or less appropriate. |
| `misconception_tags` | Trap, misconception, or tradeoff tested. |
| `source_trace` | Exact source URL/path from the allowed source list. Do not use source IDs or prose titles. |
| `evidence_span` | Short phrase or sentence from the selected source that supports the keyed answer and rationale. |
| `defensible_correct_answer` | One or two sentences proving why the keyed answer is defensible from the evidence span and source. |
| `defensibility_check` | `pass` only when the answer can be defended from the selected source; otherwise discard the item before returning it. |
| `defensibility_risk` | `low`, `medium`, or `high`. Return only `low` or `medium` risk items. |
| `question_format` | Optional. `multiple-choice` or `multiple-response`; the normalizer can infer this if omitted. |
| `difficulty` | Optional. `medium`, `hard`, or `exam-plus`; omit rather than weakening the question to classify it. |
| `cognitive_demand` | Optional. diagnose, select, configure, optimize, compare, judge, integrate, or implement. |
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
- For multiple-choice items, distribute the correct answer across option
  positions 1, 2, 3, and 4. Counts per position must differ by at most one.
  Do not place every correct answer first and do not move weak distractors merely
  to satisfy the quota.
- Mark each question with difficulty: `medium`, `hard`, or `exam-plus`.
- For every distractor, explain why it is tempting and why it is wrong or less
  suitable.
- Do not use stale date-bound service claims such as "as of early 2024",
  "currently does not support", or "does not yet support".
- If an item depends on a fast-changing AWS service capability, write the item
  around the decision process and put the exact AWS documentation in
  `source_trace`.
- Source traces must be audit-resolvable. Use an official
  `https://docs.aws.amazon.com/...` URL, a real local `docs/...` path, the
  canonical objectives JSON path, or `NONE`. Do not write prose citation names
  such as "AWS Lambda streaming documentation" or "Amazon Bedrock API docs".
- Use only the topic's allowed sources. If no allowed source can support the
  keyed answer and rationale, discard or rewrite the item before returning it.
- Do not optimize for easy source matching. First create a tough, realistic
  exam-quality item; then ensure the keyed answer is defensible from the allowed
  source. Never turn the item into a documentation lookup just to pass review.
- Return only items whose `defensibility_check` is `pass`.
```

## Review Feedback Incorporated

These prompts intentionally incorporate the Day 1 lessons:

- prompt more raw candidates than the approved target because review will cull
  weak, duplicate, or unverifiable items;
- preserve official objective fields from the canonical objectives JSON;
- require source-sensitive claims to be marked for review;
- require citations to be resolvable URLs/local paths or explicit `NONE`;
- require source-backed atomic claims at generation time;
- keep the first-pass LLM output lean so question quality, answer reasoning,
  source trace, and evidence defense are the model's main cognitive load;
- demand scenario constraints and distractor rationales;
- avoid recall-only, keyword-trivia, and stale service-capability claims;
- keep remediation targets tied to actual study guide, artifact, or answer
  guidance files.
"""


def render_scope(briefs: list[Brief], day: int) -> str:
    rows = "\n".join(
        f"| {brief.order} | {brief.topic} | "
        f"{'<br>'.join(dict.fromkeys(mapping.task for mapping in brief.objective_mappings))} | "
        f"{', '.join(mapping.skill.split(':', 1)[0] for mapping in brief.objective_mappings)} |"
        for brief in briefs
    )
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

Use the lean output schema specified above. Use the topic briefs below to stay
inside the correct official objective scope, but do not copy mechanical
objective metadata into the JSON output.

Do not mark anything as approved.
```
"""


def render_topic_prompt(brief: Brief, per_topic: int) -> str:
    focus = "\n".join(f"- {item}" for item in brief.question_focus)
    misconceptions = "\n".join(f"- {item}" for item in brief.misconceptions)
    objective_rows = "\n".join(
        f"- {mapping.domain} | {mapping.task} | {mapping.skill}"
        for mapping in brief.objective_mappings
    )
    skill_count = len(brief.objective_mappings)
    minimum_per_skill = max(1, per_topic // skill_count)
    source_rows = "\n".join(
        "- source_value: `{source}`; source_type: {source_type}; use_for: {use_for}".format(
            **source
        )
        for source in brief.allowed_sources
    )
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

Official objective context for this topic. Use this to understand the skill
being tested. You do not need to copy these fields into the JSON output:
{objective_rows}

Use only these mappings as the skill boundary. Generate at least
{minimum_per_skill} item(s) that test each mapped skill before using the
remaining item budget.

Question focus:
{focus}

Misconceptions and traps to test:
{misconceptions}

Existing remediation targets. The normalizer will attach these later; do not
copy them into the JSON output:

- study_guide: {brief.study_guide}
- focused_artifact: {brief.artifact}
- answer_guidance: {brief.answer_guidance}

Allowed sources. Use only one exact `source_value` below for `source_trace`:

{source_rows}

Generate approximately {count_format_target(per_topic)} items for this topic.
Every item must be scenario-based unless the item is testing a necessary
declarative fact inside a realistic work situation.

For every generated item:

- create a tough, tricky, scenario-rich exam-prep question first;
- choose a correct answer that is defensible from one allowed source;
- set `source_trace` to the exact allowed source URL/path, not the ID;
- set `evidence_span` to a short phrase or sentence from that source;
- set `defensible_correct_answer` to a concise proof of the keyed answer;
- set `defensibility_check` to `pass`;
- set `defensibility_risk` to `low` or `medium`;
- discard or rewrite the item if you cannot defend the correct answer from the
  selected source.

For multiple-choice items, distribute correct answers across positions 1, 2,
3, and 4 with counts differing by at most one. Use exact option text in
`correct_answer`; do not use numeric indexes such as `0`, `1`, or `A`.

Return only a JSON array of lean draft items using the lean output schema.
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
    if not TRACEABILITY_MATRIX.exists():
        raise SystemExit(f"Missing source-to-topic traceability matrix: {TRACEABILITY_MATRIX}")

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
