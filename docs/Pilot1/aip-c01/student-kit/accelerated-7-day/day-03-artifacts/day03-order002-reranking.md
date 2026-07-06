# Day03-order002: Reranking

## Traceability

| Field | Value |
|---|---|
| Curriculum order | Day03-order002 |
| Section | Layer 1 - Data and RAG foundations |
| Topic | Reranking |
| Knowledge category | Skill; Knowledge |
| Knowledge type | Procedural; Causal; Conditional |
| Artifact family | Lab worksheet or runbook; decision table; cause-effect worksheet |

## Purpose

Use reranking to improve the final context sent to the model, while recognizing
the cost, latency, and operational risk added by another ranking step.

## Scenario

The retriever returns ten chunks. The correct chunk is often present, but it is
ranked sixth or lower, so the final prompt misses it when only the top three
chunks are included.

## Artifact A: Reranking Runbook

| Step | Action | Evidence |
|---:|---|---|
| 1 | Capture baseline top-k retrieval results. |  |
| 2 | Label which chunks actually answer the query. |  |
| 3 | Apply reranker to candidate set. |  |
| 4 | Compare before/after rank of relevant chunks. |  |
| 5 | Check latency and cost impact. |  |
| 6 | Decide whether to ship, tune, or reject reranking. |  |

## Artifact B: Before And After Review

| Query | Baseline top result | Correct chunk rank before | Correct chunk rank after | Ship? |
|---|---|---:|---:|---|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

## Artifact C: Conditional Decision

```text
Use reranking when...

Do not use reranking when...

This decision changes if...
```

## Self-Check

| Question | My answer |
|---|---|
| What problem does reranking solve that embedding search may not solve? |  |
| Why should reranking be tested against latency and cost? |  |
| How can reranking harm the system? |  |

## Mastery Evidence

You can explain when reranking is useful, show before/after rank evidence, and
decide whether the gain justifies added latency and cost.

## Remediation

If your answer treats reranking as automatically better, create three failed
retrieval examples: one where reranking helps, one where it does nothing, and
one where it makes the result worse. Update the conditional decision after that
comparison.
