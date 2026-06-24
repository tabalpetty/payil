# Conversation Handoff

## Recovered Context

The project began by examining different types of knowledge and the learning,
teaching, and assessment methods best suited to each. AIP-C01 was selected as a
complex practical example for applying that analysis.

Initial work classified the exam syllabus at domain and skill level, designed
learning layers and mastery gates, and produced workbook-style planning
artifacts. A critical realization followed: the project had become stronger at
process, evaluation, and progression than at teaching itself.

The mission was then clarified. The goal is not primarily to create another
AIP-C01 exam course. It is to develop and test a polymethod teaching system in
which:

> Domain structure determines learning order. Knowledge type determines
> teaching method. Mastery evidence determines progression.

## Decisions Made

1. Maintain three distinct deliverables:
   - a generic Curriculum Architecture Kit;
   - an AIP-C01 Teacher Kit;
   - an AIP-C01 Student Kit.
2. Treat AIP-C01 as the first reference implementation and source of lessons
   for the generic kit.
3. Do not flatten different classification axes into one list.
4. Add embedded knowledge and collective or institutional knowledge to the
   representation and locus axis.
5. Treat subject domain as an overlay, not a cognitive knowledge type.
6. Treat expertise as proficiency, not a knowledge type.
7. Allow units to contain multiple knowledge types. Use the dominant type for
   the primary teaching method and secondary types for supporting methods.
8. Make teaching quality the primary design concern. Workbooks, assessments,
   gates, and tracking mechanisms support that concern.
9. Build one complete pilot unit before generating materials for the entire
   syllabus.

## Teaching Methods Identified

- Declarative: retrieval practice, spaced repetition, concise references.
- Conceptual: diagrams, analogy, comparison, reconstruction, teach-back.
- Procedural: demonstration, guided lab, fading support, varied independent
  practice.
- Conditional and strategic: contrasting cases, decision scenarios, rejection
  of alternatives, architecture review.
- Causal and diagnostic: prediction, experiment, failure injection, trace
  analysis, root-cause work.
- Normative and institutional: policy cases, stakeholder roles, control
  mapping, RACI exercises, mock audits.
- Tacit and pattern recognition: repeated cases, expert critique, think-alouds,
  apprenticeship, weak-versus-strong comparisons.
- Metacognitive: confidence calibration, evidence-based reflection, and
  strategy adjustment.

## Important Warning

A template that says "use a conceptual teaching method" is not yet teaching
material. A complete unit must provide the explanation, diagram, comparison,
questions, activity, feedback, artifact, assessment, and remediation needed to
create the intended learning experience.

## Prior Artifacts

Earlier conversation references include:

- a detailed AIP-C01 syllabus classification;
- research comparing alternative knowledge taxonomies;
- an AIP-C01 knowledge architecture matrix;
- a topic knowledge-type and method map;
- a curriculum architecture and mastery framework;
- a Layer 0 Foundations Mastery Kit spreadsheet.

Several prior artifacts are now present under
`docs/Pilot1/aip-c01/source-material/`:

- `AIP-C01_Teaching_Strategy.md`;
- `AIP-C01_Curriculum_Dependency_and_Mastery_Matrix.xlsx`;
- `AIP-C01_Topics_Learning_Order_With_Knowledge_Type.xlsx`;
- `AIP-C01_Assessment_and_Progression_Kit.xlsx`;
- `AIP-C01_Layer_0_Foundations_Mastery_Kit_FIXED.xlsx`.

See `docs/Pilot1/aip-c01/source-material/README.md` for the intake inventory.
The detailed syllabus
classification and research documents named in the earlier conversation are
not separately present under those names.

## Current Next Step

The first version of the subject-agnostic Teaching System Specification now
exists at
`docs/curriculum-architecture-kit/teaching-system-specification.md`. It includes:

- the multidimensional knowledge taxonomy;
- the teaching-method library;
- rules for blended-method units;
- standard learning-unit, teacher-package, and student-package schemas;
- artifact and mastery-evidence rules;
- adaptation and remediation rules;
- validation criteria for the first AIP-C01 pilot.

Status update as of 2026-06-23: the AIP-C01 implementation has since been
rebuilt under `docs/Pilot1/aip-c01/`. The curriculum model is complete (133
topics, 98 official skills mapped across 226 relationships, 7-day accelerated
track); Day 1 and Day 2 Student Kits are built; Day 1 exam-prep has an approved
100-item bank; and the Day 2 exam-prep production agent has had its first full
run (118 items, final gate result `blocked`).

This handoff predates the numbered decision records. The authoritative
decisions are now `docs/decisions/0001`–`0009`, and live implementation status
is tracked in
`docs/Pilot1/aip-c01/exam-prep/exam-prep-agent-open-items.md` and
`docs/Pilot1/aip-c01/exam-prep/agent_creation_progress.md`.
