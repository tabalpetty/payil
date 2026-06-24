# Decision 0009: Curriculum Production Multi-Agent Architecture

## Status

Accepted on June 23, 2026.

## Decision

Use one deterministic Curriculum Production Orchestrator to coordinate
specialized authoring, review, verification, assessment, packaging, and
continuous-improvement workers.

Treat LLM providers as configurable adapters. The initial intended deployment
uses Codex for authoring and revision and Claude Code for independent semantic
review. Deterministic scripts and explicit human control points retain final
authority over gates and release status.

The existing Exam Prep Production Agent remains a subsystem responsible for
assessment-question production. It does not become the owner of study guides,
learner artifacts, answer guidance, teacher material, or curriculum
decomposition.

## Rationale

Day 1 and Day 2 showed that high-quality curriculum production is an ordered
system rather than one generation prompt:

- teaching must precede dependent activities;
- artifacts must match knowledge type;
- exemplars and answer guidance are required for self-study;
- independent review exposes depth, traceability, and correctness gaps;
- fact checking and reverse testing are separate learner-protection gates;
- review findings must feed authoring prompts, tests, and kit lessons;
- no semantic worker should certify its own output.

A single conversational mega-agent would hide state, blur authority, and make
partial completion difficult to audit. A deterministic orchestrator with
bounded workers preserves separation of concerns and permits different models,
tools, or humans to fill each role.

## Consequences

- Add a subject-agnostic project architecture under the Curriculum
  Architecture Kit.
- Build production briefs and manifests before automating Days 3-7.
- Preserve prompts, raw output, review output, revisions, verification, and
  gate evidence.
- Keep author and reviewer roles independent where practical.
- Use deterministic status and release gates.
- Treat Day 1 and Day 2 as quality exemplars and regression fixtures. (The Day
  2 *exam-prep* bank is still gate-`blocked` and not yet released; see
  `docs/Pilot1/aip-c01/exam-prep/exam-prep-agent-open-items.md`. The Day 2
  *student kit* has passed content review.)
- Record provider choice in configuration rather than embedding it into
  workflow semantics.
