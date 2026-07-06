# Day03-order006: RAG Quality Evaluation And Retrieval Troubleshooting

## Traceability

| Field | Value |
|---|---|
| Curriculum order | Day03-order006 |
| Section | Layer 1 - Data and RAG foundations |
| Topic | RAG quality evaluation and retrieval troubleshooting |
| Knowledge category | Skill; Knowledge; Representation / Location |
| Knowledge type | Diagnostic; Causal; Procedural; Tacit |
| Artifact family | Troubleshooting worksheet; lab runbook; cause-effect worksheet |

## Purpose

Diagnose whether poor RAG answers come from retrieval, context assembly, model
behavior, output validation, or stale/incorrect source material.

## Artifact A: Symptom-To-Layer Table

| Symptom | Likely layer | Evidence to inspect | First fix to try |
|---|---|---|---|
| Correct source never retrieved |  |  |  |
| Correct source retrieved but ranked low |  |  |  |
| Correct source in prompt but answer wrong |  |  |  |
| Answer lacks citation |  |  |  |
| Answer cites stale document |  |  |  |
| User sees unauthorized content |  |  |  |

## Artifact B: Troubleshooting Runbook

| Step | Action | Evidence |
|---:|---|---|
| 1 | Reproduce the failing query. |  |
| 2 | Inspect rewritten query and filters. |  |
| 3 | Inspect retrieved chunks and ranks. |  |
| 4 | Inspect assembled prompt context. |  |
| 5 | Inspect model output and validation. |  |
| 6 | Apply one fix at a time. |  |
| 7 | Rerun golden query set. |  |

## Artifact C: Incident Note

```text
Failure:

Root cause:

Evidence:

Fix:

Regression test added:
```

## Self-Check

| Question | My answer |
|---|---|
| Why should you avoid changing chunking, prompt, and model at the same time? |  |
| What is the difference between retrieval failure and generation failure? |  |
| What golden test would prevent recurrence? |  |

## Mastery Evidence

You can isolate a RAG failure to the likely layer, name the evidence that proves
the diagnosis, apply one fix at a time, and add a regression test.

## Remediation

If your diagnosis jumps straight to "change the prompt," rerun the failure
through the symptom-to-layer table. Inspect query, filters, retrieved chunks,
rank, prompt context, and model output before choosing a fix.
