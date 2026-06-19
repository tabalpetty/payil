# Project Instructions

## Mission

Create a subject-agnostic Curriculum Architecture Kit for designing rich,
multi-method teaching systems. Validate and refine it through Pilot1, an
AIP-C01 reference implementation consisting of a curriculum model, Teacher Kit,
Student Kit, and exam-preparation layer.

## Governing Principles

1. Domain structure, dependencies, and prerequisites determine learning order.
2. Knowledge type determines the primary teaching method.
3. A learning unit may contain multiple knowledge types. Use secondary types to
   select supporting methods.
4. Teach and assess knowledge in the form in which it must be used.
5. Mastery evidence, not content exposure, determines progression.
6. Teaching quality is the primary goal. Process, gates, workbooks, and
   evaluation tools exist to support teaching.
7. Do not reduce learning to reading followed by multiple-choice questions.
8. Avoid replacing one uniform method with another. Use a justified blend of
   methods when the unit requires it.
9. Preserve traceability from source objective to learning unit, activity,
   artifact, assessment, and remediation.
10. Prefer a complete pilot unit over prematurely generating the entire course.

## Deliverable Boundaries

- `docs/curriculum-architecture-kit/` is subject-agnostic. It may contain
  generic templates, examples, and lessons learned from implementations.
- `docs/Pilot1/aip-c01/teacher-kit/` contains Pilot1 AIP-C01-specific
  instructor materials.
- `docs/Pilot1/aip-c01/student-kit/` contains Pilot1 AIP-C01-specific learner
  materials.
- `docs/Pilot1/aip-c01/curriculum-model/` contains the application of the
  generic architecture method to the AIP-C01 domain.
- `docs/Pilot1/aip-c01/exam-prep/` contains Pilot1 AIP-C01 exam-preparation
  materials.
- `docs/Pilot1/aip-c01/source-material/` contains Pilot1 AIP-C01 source
  syllabi, research, prior planning views, and trusted reference inputs.
- `docs/decisions/` records important decisions, assumptions, and changes.

## Content Standards

- Distinguish classification axes instead of flattening them into one taxonomy:
  cognitive function, representation or locus, subject domain, and proficiency.
- State the dominant and secondary knowledge types for each learning unit.
- Include actual teaching material, not only instructions to teach.
- Define the learner artifact or observable performance that demonstrates
  mastery.
- Pair every assessment with gap-specific remediation and a reassessment path.
- Use current official AWS sources for AIP-C01 technical claims and preserve
  source traceability.
- Keep generic methodology free of unnecessary AWS-specific assumptions.

## Working Practice

- Read the project charter and relevant decision records before substantial
  changes.
- Make narrowly scoped changes and update decision records when architecture or
  terminology changes.
- Keep `docs/curriculum-architecture-kit/lessons-learned.md` current when an
  implementation reveals an error, design improvement, efficiency, or
  remediation pattern that should inform future projects.
- Treat generated spreadsheets and documents as views of the source material,
  not as the sole source of truth.
