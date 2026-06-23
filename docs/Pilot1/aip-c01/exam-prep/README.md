# Pilot1 AIP-C01 Exam Prep

## Purpose

This directory will contain exam-readiness materials for **AWS Certified
Generative AI Developer - Professional (AIP-C01)**.

Exam prep supports the curriculum. It does not replace teaching, labs,
artifacts, remediation, or mastery gates.

## Provenance Rule

Raw question candidates must be labeled by true origin before review:
external LLM generation, manual authoring, Codex-assisted authoring,
reviewer-authored top-up, imported source, or transformed item. Review approval
does not erase provenance; the reviewed bank must preserve the raw source used
for each approved item.

## Source Extraction Rule

For official AIP-C01 domain, task, skill, and weighting references, use
`source-material/ai-professional-01.objectives.json` as the canonical project
input. Use `source-material/ai-professional-01.extracted.md` for human wording
checks and `source-material/ai-professional-01.pdf` only as the source of
record for audit or regeneration.

Before generating or reviewing objective-tagged items, verify that the
objective JSON exists and contains the official domain, task, and Skill X.Y.Z
statements used by the question-bank schema. If a field is local editorial
focus, label it separately from the official objective field.

## Bank Completion Rule

A day's bank is complete only after review approves at least `10` items per
curriculum-order topic for that day. Smaller reviewed sets are usable as
minimum viable approved slices, but they are not complete banks.

## Continuous Improvement Rule

Every review pass must preserve cull reasons and feed them into the next
generation prompt. Top-up generation should address the highest-frequency
failure patterns and produce a surplus over the exact deficit because weak,
duplicate, or unverifiable items will be rejected.

Top-up prompts should include existing approved stems and rejected stem
excerpts for the same topic. The review pass is still responsible for rejecting
exact or near-duplicate stems; prompt instructions are a prevention aid, not
the quality gate.

## Source Verification Rule

Final gates must not pass while any item has unresolved source markers, stale
claim patterns, or unsupported high-risk service claims. The source-verifier
report must explain each unresolved item; factual culls discovered at this
stage must be added to the cull log with observable evidence.

## Official Baseline

| Property | Value |
|---|---|
| Exam code | AIP-C01 |
| Duration | 180 minutes |
| Total questions | 75 |
| Scored questions | 65 |
| Unscored questions | 10 |
| Question formats | Multiple choice and multiple response |
| Minimum passing score | 750 |

## Internal Accelerated-Route Readiness Gate

The 7-day accelerated path uses a stricter operational readiness gate:

- `82%` or higher overall on a full-length simulated exam;
- `72%` or higher in every official domain;
- completed in `170` minutes or less;
- no severe unresolved gap in safety, security, governance, RAG, integration,
  operations, or troubleshooting;
- written error analysis for missed, guessed, and low-confidence correct
  questions.

## Files

- [question-bank-specification.md](question-bank-specification.md)
- [question-generation-prompt-intake.md](question-generation-prompt-intake.md)
- [agent_creation_progress.md](agent_creation_progress.md)
- [exam-prep-agent-architecture.md](exam-prep-agent-architecture.md)
- [exam-prep-agent-architecture.drawio](exam-prep-agent-architecture.drawio)
- [exam-prep-agent-design-lessons.md](exam-prep-agent-design-lessons.md)
- [topic-briefs/day-02/README.md](topic-briefs/day-02/README.md)
- [day-02-question-generation-prompts.md](day-02-question-generation-prompts.md)
- [reviewed/day-02/day-02-reviewed-question-bank.md](reviewed/day-02/day-02-reviewed-question-bank.md)
- [day-01-question-generation-prompts.md](day-01-question-generation-prompts.md)
- [reviewed/day-01/day-01-reviewed-question-bank.md](reviewed/day-01/day-01-reviewed-question-bank.md)
