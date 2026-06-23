# Day02-order009: Basic Semantic Retrieval

## Traceability

| Field | Value |
|---|---|
| Curriculum order | Day02-order009 |
| Section | Layer 1 - Data and RAG foundations |
| Topic | Basic semantic retrieval |
| Knowledge category | Knowledge; Skill |
| Knowledge type | Conceptual; Procedural |
| Artifact family | Lab worksheet or runbook; concept map |

## Purpose

Show that you can specify a basic semantic retrieval path and test whether it
returns the right context.

## Artifact A: Retrieval Concept Map

Map the relationship among:

```text
user query -> query embedding -> metadata filters -> candidate retrieval -> ranking -> selected context
```

My concept map:

```text

```

## Artifact B: Retrieval Runbook

| Step | Action | Evidence |
|---:|---|---|
| 1 | Normalize the user query. |  |
| 2 | Generate or inspect query embedding. |  |
| 3 | Apply access and freshness filters. |  |
| 4 | Retrieve top candidate chunks. |  |
| 5 | Select context and source IDs. |  |
| 6 | Record failure signal if expected context is missing. |  |

## Artifact C: Retrieval Test Cases

| Test type | Test query | Expected retrieved content | Filter expectation | Failure signal |
|---|---|---|---|---|
| Happy path |  |  |  |  |
| Paraphrase |  |  |  |  |
| Missing context |  |  |  |  |
| Access control |  |  |  |  |
| Freshness |  |  |  |  |

## Self-Check

| Question | My answer |
|---|---|
| Why does semantic retrieval need test cases? |  |
| What failure looks like a model problem but starts in retrieval? |  |
| Which filter must run before context reaches the model? |  |
