# Day02-order005: Document Chunking And Segmentation

## Traceability

| Field | Value |
|---|---|
| Curriculum order | Day02-order005 |
| Section | Layer 1 - Data and RAG foundations |
| Topic | Document chunking and segmentation |
| Knowledge category | Knowledge; Skill |
| Knowledge type | Conceptual; Procedural; Causal; Conditional |
| Artifact family | Lab worksheet or runbook; decision table; cause-effect worksheet |

## Purpose

Choose a chunking strategy that preserves meaning while supporting precise,
secure, and efficient retrieval.

## Artifact A: Chunking Decision Table

| Approach | Strength | Weakness | Use or reject for the policy assistant? |
|---|---|---|---|
| Fixed-size chunking |  |  |  |
| Section-based chunking |  |  |  |
| Hierarchical chunking |  |  |  |
| Semantic chunking |  |  |  |
| Table-aware chunking |  |  |  |

## Artifact B: Cause-Effect Worksheet

| Chunking change | Predicted effect | Risk to test |
|---|---|---|
| Make chunks smaller |  |  |
| Make chunks larger |  |  |
| Preserve headings |  |  |
| Add overlap |  |  |
| Split tables from headers |  |  |

## Artifact C: Chunking Runbook

| Step | Action | Evidence |
|---:|---|---|
| 1 | Inspect document structure. |  |
| 2 | Choose chunking approach. |  |
| 3 | Preserve source, section, page, and heading metadata. |  |
| 4 | Test retrieval on representative questions. |  |
| 5 | Adjust chunk size or boundaries based on failures. |  |

## Self-Check

| Question | My answer |
|---|---|
| What does "too small" look like in retrieval results? |  |
| What does "too large" look like in prompt context? |  |
| Which scenario would make you reject fixed-size chunking? |  |
