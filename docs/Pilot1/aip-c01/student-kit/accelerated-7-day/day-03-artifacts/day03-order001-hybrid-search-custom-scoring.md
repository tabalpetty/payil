# Day03-order001: Hybrid Search And Custom Scoring

## Traceability

| Field | Value |
|---|---|
| Curriculum order | Day03-order001 |
| Section | Layer 1 - Data and RAG foundations |
| Topic | Hybrid search and custom scoring |
| Knowledge category | Skill; Knowledge |
| Knowledge type | Procedural; Causal; Conditional |
| Artifact family | Lab worksheet or runbook; decision table; cause-effect worksheet |

## Purpose

Decide when semantic retrieval alone is insufficient and design a hybrid
retrieval approach that combines semantic, keyword, metadata, and business
signals without making retrieval slower or less explainable than necessary.

## Scenario

A support assistant answers questions from product manuals, release notes, and
known-issue tickets. Users often search by exact error code, product nickname,
or vague symptom.

## Artifact A: Search Signal Plan

| Signal | What it captures | When it helps | Risk if overweighted |
|---|---|---|---|
| Semantic similarity |  |  |  |
| Keyword or lexical match |  |  |  |
| Metadata filter |  |  |  |
| Freshness or recency |  |  |  |
| Business priority |  |  |  |

## Artifact B: Custom Scoring Rule

Write a plain-English scoring rule. Keep it inspectable.

```text
For this scenario, rank results by...

Boost when...

Penalize when...

Never allow scoring to override...
```

## Artifact C: Decision Table

| Query type | Retrieval method | Why | Evidence to collect |
|---|---|---|---|
| Exact error code |  |  |  |
| Vague symptom |  |  |  |
| Recent release issue |  |  |  |
| Permission-restricted document |  |  |  |

## Self-Check

| Question | My answer |
|---|---|
| When is hybrid search worth the added complexity? |  |
| What failure happens if keyword score dominates semantic relevance? |  |
| What metric or review would prove the scoring rule improved retrieval? |  |

## Mastery Evidence

You can defend one hybrid strategy, name one rejected simpler strategy, and
show how retrieval quality would be measured before and after the change.

## Remediation

If your answer only says "use hybrid search," redo Artifact C with four
different query types and force yourself to reject hybrid search for at least
one of them. Then add one measurable retrieval-quality signal.
