# Day02-order002: Text, Image, Audio, And Tabular-Data Preprocessing

## Traceability

| Field | Value |
|---|---|
| Curriculum order | Day02-order002 |
| Section | Layer 1 - Data and RAG foundations |
| Topic | Text, image, audio, and tabular-data preprocessing |
| Knowledge category | Knowledge; Skill |
| Knowledge type | Conceptual; Procedural; Conditional |
| Artifact family | Lab worksheet or runbook; decision table with contrasting scenarios; concept map |

## Purpose

Choose preprocessing steps that preserve meaning, source traceability, and
retrieval usefulness across different data types.

## Artifact A: Preprocessing Concept Map

Map the relationship among:

```text
source modality -> extraction -> normalization -> metadata -> quality check -> retrievable record
```

My concept map:

```text

```

## Artifact B: Modality Decision Table

| Source type | Preprocessing needed | Why | Reject or avoid |
|---|---|---|---|
| HTML or plain text |  |  |  |
| PDF |  |  |  |
| Image or screenshot |  |  |  |
| Audio or video |  |  |  |
| Table or spreadsheet |  |  |  |
| Tabular records |  |  |  |

## Artifact C: Preprocessing Runbook

| Step | Action | Notes/evidence |
|---:|---|---|
| 1 | Identify source modality. |  |
| 2 | Extract usable text or structured fields. |  |
| 3 | Preserve source references. |  |
| 4 | Normalize fields, dates, units, and encoding. |  |
| 5 | Apply redaction or access labels. |  |
| 6 | Validate output before ingestion. |  |

## Self-Check

| Question | My answer |
|---|---|
| What gets lost if tables are flattened without headers? |  |
| When should a source be quarantined instead of ingested? |  |
| Which preprocessing decision is conditional on the source modality? |  |
