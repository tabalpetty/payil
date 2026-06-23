# Day02-order010: Basic Retrieval-Augmented Generation

## Traceability

| Field | Value |
|---|---|
| Curriculum order | Day02-order010 |
| Section | Layer 1 - Data and RAG foundations |
| Topic | Basic Retrieval-Augmented Generation |
| Knowledge category | Knowledge; Skill |
| Knowledge type | Conceptual; Procedural; Strategic |
| Artifact family | Architecture decision record or tradeoff matrix; lab worksheet or runbook; concept map |

## Purpose

Design a basic RAG request path that connects data preparation, retrieval,
prompt assembly, answer validation, and evaluation.

## Artifact A: RAG Architecture Sketch

```text
authenticated user
  -> application
  -> retrieval query
  -> filters
  -> retrieved chunks
  -> prompt context
  -> model answer
  -> citation/validation
  -> logs/evaluation
```

My architecture sketch:

```text

```

## Artifact B: RAG Runbook

| Step | Action | Evidence |
|---:|---|---|
| 1 | Authenticate and authorize caller. |  |
| 2 | Build retrieval query. |  |
| 3 | Apply entitlement and freshness filters. |  |
| 4 | Retrieve and rank chunks. |  |
| 5 | Assemble prompt context with source IDs. |  |
| 6 | Invoke model. |  |
| 7 | Validate answer grounding and output shape. |  |
| 8 | Record sanitized logs and evaluation evidence. |  |

## Artifact C: Strategic Tradeoff Matrix

| Decision | Option A | Option B | Chosen option and why |
|---|---|---|---|
| Chunk size | Smaller chunks | Larger chunks |  |
| Filtering | Strict filters | Broad filters |  |
| RAG path | Managed RAG service | Custom retrieval architecture |  |
| Evaluation | Manual review only | Golden retrieval and answer set |  |

## Self-Check

| Question | My answer |
|---|---|
| Why is RAG more than a vector-store decision? |  |
| Where do access control and freshness belong in the request path? |  |
| Which tradeoff would you revisit after seeing retrieval failures? |  |
