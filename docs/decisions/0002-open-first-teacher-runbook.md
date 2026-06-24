# Decision 0002: Open-First Teacher Runbook

## Status

Accepted on June 15, 2026.

## Decision

Every AIP-C01 Teacher Kit unit will contain an `OPEN-FIRST.md` file as its
authoritative instructor entry point.

The runbook must tell the teacher:

- what to understand and prepare before the lesson;
- which supporting files and materials are required;
- what to say, draw, demonstrate, and ask in sequence;
- what learner responses and diagnostic signals to expect;
- how to administer the mastery assessment;
- how to select remediation and reassessment;
- what evidence to record before progression.

The lesson plan remains a compact planning view. The teaching guide remains a
deeper subject-matter and explanation reference.

## Rationale

A complete collection of teaching assets is still difficult to use if the
teacher must infer their order and relationships. A single executable runbook
makes the intended teaching experience explicit while preserving focused
supporting documents.

## Consequences

- Teacher Kit indexes link to `OPEN-FIRST.md`, not an arbitrary supporting
  file.
- Supporting documents should avoid duplicating the full runbook.
- A unit is not ready for delivery until its runbook covers preparation,
  instruction, evidence, assessment, remediation, and recording.

## Implementation Note (2026-06-23)

In Pilot1's accelerated 7-day track, the realized instructor entry point is the
teacher-kit `facilitator-guide.md`, and the learner-facing entry point is
`student-kit/accelerated-7-day/OPEN_FIRST.md` (underscore, not the hyphenated
`OPEN-FIRST.md` named above). The decision's intent — a single authoritative
"open first" runbook per unit — holds; the realized filename and kit placement
differ from the original wording.

