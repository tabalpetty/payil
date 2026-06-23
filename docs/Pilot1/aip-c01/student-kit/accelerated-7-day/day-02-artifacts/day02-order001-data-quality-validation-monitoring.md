# Day02-order001: Data-Quality Validation And Monitoring

## Traceability

| Field | Value |
|---|---|
| Curriculum order | Day02-order001 |
| Section | Layer 1 - Data and RAG foundations |
| Topic | Data-quality validation and monitoring |
| Knowledge category | Skill; Knowledge; Representation / Location |
| Knowledge type | Procedural; Causal; Embedded |
| Artifact family | Lab worksheet or runbook; console/API configuration record or inspection worksheet; cause-effect worksheet |

## Purpose

Create evidence that you can detect, repair, and monitor data-quality problems
before they become retrieval or answer-quality failures.

## Artifact A: Validation Runbook

| Step | Action | Evidence to record |
|---:|---|---|
| 1 | Inventory source data. |  |
| 2 | Check duplicates and versions. |  |
| 3 | Check required metadata. |  |
| 4 | Check format and extraction quality. |  |
| 5 | Check sensitive data and access labels. |  |
| 6 | Quarantine or repair failed records. |  |
| 7 | Record owner, threshold, and monitoring action. |  |

## Artifact B: Cause-Effect Table

| Data issue | Likely retrieval or answer effect | Repair or control |
|---|---|---|
| Duplicate documents |  |  |
| Stale policy version |  |  |
| Missing access label |  |  |
| Broken PDF extraction |  |  |
| Conflicting source documents |  |  |
| Sensitive content in source |  |  |

## Artifact C: Embedded Inspection Record

Inspect a source repository, ingestion log, document metadata view, storage
object, or documentation example.

| Inspection target | Observable fact | What it tells me |
|---|---|---|
| Source inventory |  |  |
| Metadata record |  |  |
| Failed or quarantined record |  |  |
| Monitoring signal |  |  |

## Self-Check

| Question | My answer |
|---|---|
| Which data-quality issue would most damage retrieval quality? |  |
| Which issue would create the largest security or audit risk? |  |
| What signal would tell me the ingestion process is becoming unhealthy? |  |
