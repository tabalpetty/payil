# Day03-order004: Vector-Store Ingestion, Synchronization, Refresh, And Maintenance

## Traceability

| Field | Value |
|---|---|
| Curriculum order | Day03-order004 |
| Section | Layer 1 - Data and RAG foundations |
| Topic | Vector-store ingestion, synchronization, refresh, and maintenance |
| Knowledge category | Skill; Knowledge; Representation / Location |
| Knowledge type | Procedural; Causal; Strategic; Embedded |
| Artifact family | Architecture decision record; lab runbook; configuration inspection worksheet |

## Purpose

Design the operational path that keeps a vector store accurate, current,
permission-aware, and recoverable.

## Artifact A: Ingestion Pipeline Sketch

```text
source system
  -> extract
  -> normalize
  -> chunk
  -> enrich metadata
  -> embed
  -> index
  -> validate
  -> monitor drift/freshness
```

My pipeline notes:

```text

```

## Artifact B: Maintenance Runbook

| Operation | Trigger | Steps | Evidence retained |
|---|---|---|---|
| Initial ingestion |  |  |  |
| Incremental refresh |  |  |  |
| Document deletion |  |  |  |
| Permission change |  |  |  |
| Embedding model change |  |  |  |
| Index rebuild |  |  |  |

## Artifact C: Strategic Decision

| Decision | Option A | Option B | Chosen option and why |
|---|---|---|---|
| Refresh style | Scheduled batch | Event-driven update |  |
| Deletion handling | Soft delete | Hard delete and reindex |  |
| Rebuild approach | Blue/green index | In-place update |  |
| Validation | Sample review | Automated canary queries |  |

## Artifact D: Embedded Inspection Record

Inspect a real or simulated vector-store maintenance configuration. Use AWS
service names only when you can verify them from your source or console; the
learning goal is the inspection habit, not memorizing a single vendor screen.

| Config surface | Observable fact to record | My notes |
|---|---|---|
| Ingestion job status | last success, failure count, skipped documents |  |
| Source connector | source location, sync schedule or event trigger |  |
| Metadata mapping | fields used for filtering, freshness, ownership |  |
| Vector index settings | dimensions, distance metric, index name/version |  |
| Delete propagation | tombstone, hard delete, or reindex behavior |  |
| Permission propagation | how source access changes affect retrieval |  |
| Validation evidence | canary queries, sample reviewed docs, freshness check |  |

## Self-Check

| Question | My answer |
|---|---|
| What breaks if source permissions change but embeddings are not refreshed? |  |
| Why is deletion handling part of RAG correctness? |  |
| What evidence proves an index refresh succeeded? |  |

## Mastery Evidence

You can describe the full ingestion and refresh lifecycle, including deletes,
permission changes, validation, rollback, and evidence retained after a refresh.

## Remediation

If your plan only covers initial ingestion, add rows for document deletion,
permission changes, source updates, and embedding-model changes. Then define
one validation query that would catch stale or unauthorized retrieval.
