# Decision 0003: Exam Preparation Layer

## Status

Accepted on June 18, 2026.

## Decision

Add a distinct exam preparation layer for the AWS Certified Generative AI
Developer - Professional (AIP-C01) reference implementation.

The exam preparation layer must include:

- an official exam-format summary;
- a tagged question-bank specification;
- topic and domain quizzes;
- full-length simulated exams;
- scoring and readiness gates that are slightly stricter than the official
  passing standard;
- review workflows that link missed questions back to learning units,
  remediation, and reassessment.

Exam preparation does not replace the Teacher Kit, Student Kit, or unit-level
mastery evidence. It verifies that learners who have studied the material can
perform under exam-like constraints.

## Rationale

The project has two related goals:

1. teach the subject well enough for durable understanding and usable
   capability;
2. prepare learners to pass the certification exam.

Those goals overlap, but they are not identical. A learner may understand or
implement a capability but still struggle with timed exam wording,
multiple-choice items, multiple-response items, distractors, pacing, or domain
coverage. A learner may also memorize question-bank answers without mastering
the underlying capability.

Keeping exam preparation separate protects teaching quality while giving
learners deliberate practice with the actual certification format.

## Consequences

- The Pilot1 AIP-C01 implementation will include
  `docs/Pilot1/aip-c01/exam-prep/`.
- Question-bank items must be tagged by exam domain, task statement, learning
  unit, knowledge type, format, difficulty, misconception, and remediation
  target.
- Practice tests should approximate the official exam structure, including
  timing and question formats.
- Readiness criteria should be stricter than the official pass/fail threshold.
- Missed exam-prep items must route learners back to specific teaching or
  remediation materials rather than only showing the correct answer.
- Official AWS exam-guide claims must be checked against current official AWS
  sources before exam-prep materials are updated.
