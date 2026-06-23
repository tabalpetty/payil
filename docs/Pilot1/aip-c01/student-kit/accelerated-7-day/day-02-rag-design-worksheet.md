# Day 2 Artifact: RAG Design Worksheet

## Purpose

Design the data preparation, embedding, vector-store, metadata, chunking, and
basic retrieval foundation for a RAG system.

This is the roll-up workbook for Day 2. For topic-by-topic practice and answer
guidance, use the focused artifacts:

[day-02-artifacts/README.md](day-02-artifacts/README.md)

## Scenario

| Field | Response |
|---|---|
| Use case |  |
| Users |  |
| Source documents/data |  |
| Sensitivity level |  |
| Freshness requirement |  |
| Expected answer style |  |
| Compliance or audit constraints |  |

## Part A: Data Quality And Preparation

| Data issue | How it appears | Repair or control |
|---|---|---|
| Duplicates |  |  |
| Stale content |  |  |
| Missing metadata |  |  |
| Inconsistent formatting |  |  |
| PII or sensitive content |  |  |
| Tables, images, audio, or non-text content |  |  |
| Conflicting source documents |  |  |

## Part B: Chunking Decision

| Option | Strength | Weakness | Use or reject? |
|---|---|---|---|
| Fixed-size chunking |  |  |  |
| Hierarchical chunking |  |  |  |
| Semantic chunking |  |  |  |
| Document-section chunking |  |  |  |

Chosen chunking approach:

```text

```

Why this choice fits the scenario:

```text

```

## Part C: Metadata Schema

| Metadata field | Type | Required? | Used for filtering, ranking, security, or audit? |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

## Part D: Embedding And Vector Store Design

| Decision | Choice | Rationale |
|---|---|---|
| Embedding model |  |  |
| Vector store |  |  |
| Similarity/search approach |  |  |
| Index refresh strategy |  |  |
| Access-control strategy |  |  |
| Backup or recovery expectation |  |  |

## Part E: Retrieval Test Cases

| Test query | Expected retrieved content | Metadata/filter expectation | Failure signal |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

## Part F: Failure Diagnosis

| Symptom | Likely cause | Evidence to inspect | Fix |
|---|---|---|---|
| Relevant document is not retrieved |  |  |  |
| Irrelevant document is ranked highly |  |  |  |
| User sees unauthorized information |  |  |  |
| New document is missing from answers |  |  |  |
| Answer is grounded in stale content |  |  |  |

## Exit Check

| Check | Evidence |
|---|---|
| I can defend the chunking, embedding, vector-store, and metadata design. |  |
| I can identify where data quality, sync, or retrieval failures appear. |  |
| I completed timed Day 2 practice. |  |
| I logged misses and remediation. |  |
