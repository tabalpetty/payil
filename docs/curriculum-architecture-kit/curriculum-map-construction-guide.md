# Curriculum Map Construction Guide

## Purpose

This guide explains how to build an explainable curriculum map: a table that
connects learning order, topic, knowledge category, knowledge type, and learner
artifact.

The map helps teachers, learners, examiners, and curriculum designers see the
logic of the course instead of treating the curriculum as a black box.

## When To Create It

Create the map after:

1. source objectives have been inventoried;
2. topics or capabilities have been decomposed;
3. prerequisite and dependency order has been established;
4. supported pacing tracks have been defined;
5. knowledge categories and types have been assigned.

Create it before:

- generating full lessons;
- creating slide decks;
- writing labs;
- building practice exams;
- producing teacher and student kits at scale.

## Required Columns

| Column | Meaning |
|---|---|
| Curriculum Order | Position in the selected route, such as `Day01-order001`, `Week02-order004`, or `Module03-order002`. |
| Section | Domain section, dependency layer, or curriculum layer. |
| Topic | Learnable capability or topic. |
| Knowledge Category | Broad category: knowledge, skill, representation/location, social/organizational, or embodied skill. |
| Knowledge Type | Specific type: declarative, conceptual, procedural, diagnostic, embedded, institutional, etc. |
| Artifact To Create | Learner work product aligned to the category/type mix. |

Optional columns may include source objective, prerequisite IDs, proficiency
level, teaching method, assessment method, remediation route, and exam weight.

## Construction Process

### Step 1: Preserve The Dependency Order

Start from the prerequisite-oriented sequence, not from the source document's
order unless the source order already reflects learning dependencies.

The sequence should generally move from:

1. foundations;
2. concepts that depend on foundations;
3. procedures that use the concepts;
4. conditional decisions among procedures;
5. causal and diagnostic reasoning;
6. strategic or institutional integration;
7. final transfer and synthesis.

### Step 2: Apply The Pacing Track

Map ordered topics into the selected route.

Examples:

- `Day01-order001` for an accelerated daily route;
- `Week03-order007` for a weekly route;
- `Module05-order002` for a modular route.

The route can compress or distribute topics, but it should not break the
dependency logic. If compression forces a risky jump, record the risk.

### Step 3: Classify Category And Type

Use separate axes.

| Category | Example types |
|---|---|
| Knowledge | Declarative, conceptual, conditional, causal, normative. |
| Skill | Procedural, diagnostic, strategic, metacognitive. |
| Representation / Location | Explicit, tacit, implicit, embedded, institutional, collective. |
| Social / Organizational | Social, relational. |
| Embodied Skill | Embodied. |

Do not flatten everything into "knowledge type." A procedural topic may be a
skill. Embedded or institutional knowledge describes where knowledge lives.

### Step 4: Derive The Artifact

Choose artifacts from the category/type mix.

| Type | Artifact family |
|---|---|
| Declarative | Retrieval cards, glossary recall sheet, closed-book quiz record. |
| Conceptual | Concept map, architecture diagram, comparison table. |
| Conditional | Decision table, contrasting scenario worksheet. |
| Causal | Cause-effect worksheet, predict-observe-explain log. |
| Normative | Policy/risk review, responsible-practice checklist. |
| Procedural | Lab worksheet, runbook, worked example. |
| Diagnostic | Troubleshooting worksheet, incident reconstruction, postmortem. |
| Strategic | Architecture decision record, tradeoff matrix. |
| Metacognitive | Error log, confidence-calibration note. |
| Embedded | Console/API configuration record, tool inspection worksheet. |
| Tacit | Expert critique notes, weak-vs-strong case comparison. |
| Institutional / Collective | RACI chart, policy-to-control evidence map, ownership register. |

When a topic has multiple types, combine only the artifact families needed to
produce useful evidence. More artifact names do not automatically mean better
learning.

### Step 5: Add The Explainability Notes

Above the table, include:

- source used;
- route and ordering rule;
- category mapping;
- artifact selection rule;
- any compression assumptions.

These notes are part of the design. They let a teacher or student understand
why the table exists and how to challenge it.

## Template

```markdown
| Curriculum Order | Section | Topic | Knowledge Category | Knowledge Type | Artifact To Create |
|---|---|---|---|---|---|
| Day01-order001 | Foundation layer | Example topic | Knowledge | Declarative; Conceptual | concept map; retrieval cards |
```

## Quality Checks

Before using the map, check:

- Does the order follow prerequisite logic?
- Are foundations placed before dependent topics?
- Are categories and types separated cleanly?
- Does each artifact match the kind of evidence needed?
- Are high-risk topics producing stronger evidence than recall alone?
- Can a teacher explain why a topic is placed where it is?
- Can a learner understand what they are expected to produce?
- Can an examiner use the artifact to judge readiness?

## Pilot1 Reference Example

Pilot1 AIP-C01 applies this guide in:

`docs/Pilot1/aip-c01/curriculum-model/aip-c01-topic-knowledge-category-map.md`

That map uses `DayNN-orderNNN` identifiers for the accelerated 7-day route and
derives artifact families from the knowledge category/type mix.
