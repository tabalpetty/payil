# Day02-order003: Model-Specific Input Formatting And Data Normalization

## Traceability

| Field | Value |
|---|---|
| Curriculum order | Day02-order003 |
| Section | Layer 1 - Data and RAG foundations |
| Topic | Model-specific input formatting and data normalization |
| Knowledge category | Knowledge; Skill; Representation / Location |
| Knowledge type | Declarative; Procedural; Embedded |
| Artifact family | Lab worksheet or runbook; console/API configuration record or inspection worksheet; retrieval cards |

## Purpose

Create a normalized record shape that can be embedded, retrieved, cited, and
audited without losing source meaning or access controls.

## Artifact A: Retrieval Cards

| Term | My definition | Example |
|---|---|---|
| Normalized record |  |  |
| Source ID |  |  |
| Chunk ID |  |  |
| Modality |  |  |
| Access label |  |  |
| Effective date |  |  |
| Input limit |  | Maximum size, format, or token/file boundary accepted by the selected model or ingestion step. |

## Artifact B: Normalized Record Template

Fill a sample record for one source document.

| Field | Value | Why it is needed |
|---|---|---|
| `source_id` |  |  |
| `chunk_id` |  |  |
| `title` |  |  |
| `section` |  |  |
| `effective_date` |  |  |
| `version` |  |  |
| `owner` |  |  |
| `access_group` |  |  |
| `modality` |  |  |
| normalized text |  |  |

## Artifact C: Embedded Formatting Inspection

Inspect a model/API example, embedding job example, or normalized source
record. Record what shape the model or pipeline expects.

| Inspection target | Required input shape | Validation check |
|---|---|---|
| Embedding input |  |  |
| Generation prompt context |  |  |
| Metadata payload |  |  |

## Self-Check

| Question | My answer |
|---|---|
| Why is raw source text not enough? |  |
| Which normalized fields support citation and audit? |  |
| Which fields support access control and freshness? |  |
