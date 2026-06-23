# Day02-order007: Vector-Store Technologies And Architecture

## Traceability

| Field | Value |
|---|---|
| Curriculum order | Day02-order007 |
| Section | Layer 1 - Data and RAG foundations |
| Topic | Vector-store technologies and architecture |
| Knowledge category | Knowledge; Skill; Representation / Location |
| Knowledge type | Conceptual; Conditional; Strategic; Embedded |
| Artifact family | Architecture decision record or tradeoff matrix; console/API configuration record or inspection worksheet; decision table |

## Purpose

Choose and defend a vector-store architecture from requirements, controls, and
operational tradeoffs.

## Artifact A: Architecture Decision Matrix

| Requirement | Architecture implication | Candidate choice | Rejected alternative |
|---|---|---|---|
| Managed RAG integration |  |  |  |
| Metadata filtering |  |  |  |
| Hybrid keyword + vector retrieval |  |  |  |
| Strict access control |  |  |  |
| Rebuild/recovery path |  |  |  |
| Operational observability |  |  |  |

## Artifact B: Embedded Inspection Record

Inspect documentation or examples for a candidate vector-store or managed RAG
path. Verify current service support before using named service features in a
live design.

| Inspection target | Capability observed | Architecture implication |
|---|---|---|
| Managed RAG path |  |  |
| Vector store or search service |  |  |
| Metadata filtering support |  |  |
| Security/network/access control surface |  |  |

## Artifact C: Mini ADR

| Field | Response |
|---|---|
| Decision |  |
| Context |  |
| Chosen option |  |
| Rejected option |  |
| Tradeoff |  |
| Risk |  |
| Evidence needed before production |  |

## Self-Check

| Question | My answer |
|---|---|
| What does the vector store need to do besides store vectors? |  |
| Which requirement most strongly drives the architecture? |  |
| What would make you choose a more custom retrieval architecture? |  |
