# Polymethod Teaching System

This project develops a subject-agnostic method for designing education around
the way knowledge actually exists and is used.

The core principle is:

> Domain structure determines learning order. Knowledge type determines
> teaching method. Mastery evidence determines progression.

Pilot1, the AWS Certified Generative AI Developer - Professional (AIP-C01)
implementation, is the first reference implementation.

> **Reviewing this repository?** Start with [FOR-REVIEW.md](FOR-REVIEW.md) — it
> maps where to begin, how to read the materials, and the current status
> (including what is deliberately left `blocked`) honestly.

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
is available. The
[Curriculum Map Construction Guide](docs/curriculum-architecture-kit/curriculum-map-construction-guide.md)
captures how to make topic ordering, knowledge classification, and artifact
selection explainable. The
[Curriculum Production Agent Architecture](docs/curriculum-architecture-kit/curriculum-production-agent-architecture.md)
defines the orchestrated author-review-verify-release workflow for producing
complete teaching and assessment packages. Lessons learned from pilots are tracked in
[lessons-learned.md](docs/curriculum-architecture-kit/lessons-learned.md).

Pilot1 lives at `docs/Pilot1/aip-c01/`. As of 2026-06-23:

- **Curriculum model — complete.** 133 dependency-ordered topics, two-axis
  knowledge classification, mapped to a 7-day accelerated track with hard
  readiness gates (82% overall, 72% per domain, ≤170 minutes). The Layer 0
  source-to-decomposition audit passes: all 98 official AIP-C01 skills are
  mapped across 226 relationships, with every topic accounted for.
- **Student Kit — Days 1 and 2 built** and passing content-quality review.
  Days 3–7 have study guides, slides, and learner worksheets, but not yet the
  full per-topic artifact + answer-guidance treatment.
- **Exam Prep — Day 1 reviewed bank is approved** (100 items, 10 per topic).
  Day 2 is the first full run of the orchestrated exam-prep production agent
  (118 reviewed items); its final gate result is currently **`blocked`** —
  the traceability and coverage gates fail and factual verification is pending,
  so the Day 2 bank is not yet released. Live status is tracked in
  [exam-prep-agent-open-items.md](docs/Pilot1/aip-c01/exam-prep/exam-prep-agent-open-items.md).
- **Teacher Kit —** accelerated 7-day facilitator guide is in place.

The pilot has not yet been run with live learners.

Start with [the project charter](docs/project-charter.md) and
[the conversation handoff](docs/decisions/conversation-handoff.md).
