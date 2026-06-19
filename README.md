# Polymethod Teaching System

This project develops a subject-agnostic method for designing education around
the way knowledge actually exists and is used.

The core principle is:

> Domain structure determines learning order. Knowledge type determines
> teaching method. Mastery evidence determines progression.

Pilot1, the AWS Certified Generative AI Developer - Professional (AIP-C01)
implementation, is the first reference implementation.

## Deliverables

1. **Curriculum Architecture Kit** - reusable methodology for designing a
   teaching system for any subject.
2. **Pilot1 AIP-C01 Teacher Kit** - instructor materials, tools, facilitation
   guides, rubrics, and remediation guidance.
3. **Pilot1 AIP-C01 Student Kit** - explanations, diagrams, retrieval
   materials, labs, scenarios, practice, and assessments.
4. **Pilot1 AIP-C01 Exam Prep** - tagged question banks, timed practice, and
   readiness checks.

## Current Status

The first reusable
[Teaching System Specification](docs/curriculum-architecture-kit/teaching-system-specification.md)
is available. Lessons learned from pilots are tracked in
[lessons-learned.md](docs/curriculum-architecture-kit/lessons-learned.md).

Pilot1 has a clean artifact home at `docs/Pilot1/aip-c01/`. The next
implementation pass should regenerate the curriculum model, Teacher Kit,
Student Kit, and exam-prep materials there from the official AWS Certified
Generative AI Developer - Professional (AIP-C01) exam guide.

Start with [the project charter](docs/project-charter.md) and
[the conversation handoff](docs/decisions/conversation-handoff.md).
