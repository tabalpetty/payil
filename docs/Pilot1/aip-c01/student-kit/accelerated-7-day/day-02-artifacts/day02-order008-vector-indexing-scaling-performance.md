# Day02-order008: Vector Indexing, Sharding, Scaling, And Performance

## Traceability

| Field | Value |
|---|---|
| Curriculum order | Day02-order008 |
| Section | Layer 1 - Data and RAG foundations |
| Topic | Vector indexing, sharding, scaling, and performance |
| Knowledge category | Knowledge; Skill; Representation / Location |
| Knowledge type | Conceptual; Procedural; Causal; Embedded |
| Artifact family | Lab worksheet or runbook; console/API configuration record or inspection worksheet; cause-effect worksheet |

## Purpose

Identify the operational signals that show whether a vector index is fresh,
healthy, scalable, and recoverable.

## Artifact A: Index Operations Runbook

| Step | Action | Evidence |
|---:|---|---|
| 1 | Confirm source-to-index pipeline status. |  |
| 2 | Check failed ingestion or embedding jobs. |  |
| 3 | Check index freshness and changed-document counts. |  |
| 4 | Check query latency and timeout rate. |  |
| 5 | Check retrieval quality on a golden set. |  |
| 6 | Check filter behavior and result counts. |  |
| 7 | Confirm rebuild or recovery path. |  |

## Artifact B: Cause-Effect Worksheet

| Operational condition | Likely effect | Evidence to inspect |
|---|---|---|
| Index is stale |  |  |
| Filter is too narrow |  |  |
| Filter is too broad |  |  |
| Query latency rises |  |  |
| Rebuild path is untested |  |  |

## Artifact C: Embedded Inspection Record

| Signal or config surface | What I inspected | What it taught me |
|---|---|---|
| Index freshness |  |  |
| Query latency |  |  |
| Failed ingestion jobs |  |  |
| Capacity or partition health |  |  |

## Self-Check

| Question | My answer |
|---|---|
| Which signal shows a freshness problem? |  |
| Which signal shows a scaling or performance problem? |  |
| Why is rebuild evidence part of production readiness? |  |
