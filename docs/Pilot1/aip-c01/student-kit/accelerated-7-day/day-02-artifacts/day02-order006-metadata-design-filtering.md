# Day02-order006: Metadata Design And Filtering

## Traceability

| Field | Value |
|---|---|
| Curriculum order | Day02-order006 |
| Section | Layer 1 - Data and RAG foundations |
| Topic | Metadata design and filtering |
| Knowledge category | Knowledge; Skill |
| Knowledge type | Conceptual; Procedural; Conditional |
| Artifact family | Lab worksheet or runbook; decision table; concept map |

## Purpose

Design metadata that supports retrieval quality, access control, freshness,
audit, and operations.

## Artifact A: Metadata Concept Map

Map the relationship among:

```text
source document -> metadata -> filters -> retrieved context -> citation/audit
```

My concept map:

```text

```

## Artifact B: Metadata Schema

| Metadata field | Type | Required? | Used for filtering, ranking, security, or audit? |
|---|---|---|---|
| `source_id` |  |  |  |
| `source_type` |  |  |  |
| `owner` |  |  |  |
| `effective_date` |  |  |  |
| `version` |  |  |  |
| `access_group` |  |  |  |
| `jurisdiction` |  |  |  |
| `topic` |  |  |  |
| `source_url` or page |  |  |  |

## Artifact C: Filter Decision Table

| Scenario | Filter needed | Why | Risk if missing |
|---|---|---|---|
| User is in a restricted employee group |  |  |  |
| Policy has been superseded |  |  |  |
| Question applies to one jurisdiction |  |  |  |
| Source owner requires audit evidence |  |  |  |

## Self-Check

| Question | My answer |
|---|---|
| Which metadata field protects against unauthorized retrieval? |  |
| Which field protects against stale answers? |  |
| Which field supports citation or audit? |  |
