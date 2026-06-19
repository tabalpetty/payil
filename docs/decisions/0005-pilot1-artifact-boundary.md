# Decision 0005: Pilot1 Artifact Boundary

## Status

Accepted on June 18, 2026.

## Decision

Store all regenerated AIP-C01 implementation artifacts under:

`docs/Pilot1/aip-c01/`

The Pilot1 directory contains the reference implementation. The generic
Curriculum Architecture Kit remains in:

`docs/curriculum-architecture-kit/`

Pilot1 AIP-C01 subdirectories are:

- `curriculum-model/`
- `teacher-kit/`
- `student-kit/`
- `exam-prep/`

## Rationale

The project needs a clean separation between durable methodology and pilot
implementation artifacts. The Curriculum Architecture Kit should accumulate
reusable lessons and design rules, while Pilot1 can be regenerated, revised, or
discarded without destabilizing the generic kit.

## Consequences

- Do not create regenerated AIP-C01 artifacts directly under `docs/aip-c01/`.
- Keep AIP-C01-specific teacher, student, curriculum, and exam-prep materials
  under `docs/Pilot1/aip-c01/`.
- Keep reusable methodology, templates, and lessons learned under
  `docs/curriculum-architecture-kit/`.
- Update `docs/curriculum-architecture-kit/lessons-learned.md` when Pilot1
  reveals reusable mistakes, remediation patterns, efficiencies, or design
  improvements.
