# Day03-order003: Query Expansion, Decomposition, And Transformation

## Traceability

| Field | Value |
|---|---|
| Curriculum order | Day03-order003 |
| Section | Layer 1 - Data and RAG foundations |
| Topic | Query expansion, decomposition, and transformation |
| Knowledge category | Knowledge; Skill |
| Knowledge type | Conceptual; Procedural; Causal |
| Artifact family | Lab worksheet or runbook; cause-effect worksheet; concept map |

## Purpose

Improve retrieval by rewriting the user request into a better retrieval query,
without changing the user’s intent or introducing unsupported assumptions.

## Concept Map

```text
user question
  -> intent detection
  -> expansion OR decomposition OR transformation
  -> retrieval query or subqueries
  -> retrieved evidence
  -> answer synthesis
```

Add your notes:

```text

```

## Artifact A: Query Rewrite Table

| User question | Technique | Rewritten retrieval query or subqueries | Risk |
|---|---|---|---|
| "Why is upload broken after the new release?" |  |  |  |
| "Compare policy A and policy B for contractors." |  |  |  |
| "What does E1027 mean?" |  |  |  |
| "Summarize the last three incidents for billing." |  |  |  |

## Artifact B: Cause-Effect Notes

| Rewrite choice | Expected benefit | Possible harm | Guardrail |
|---|---|---|---|
| Expansion |  |  |  |
| Decomposition |  |  |  |
| Transformation |  |  |  |

## Self-Check

| Question | My answer |
|---|---|
| How is query expansion different from decomposition? |  |
| What would count as an unsafe query transformation? |  |
| How would you prove the rewrite helped retrieval? |  |

## Mastery Evidence

You can choose the correct rewrite technique for a user question, preserve user
intent, and identify how the rewrite could improve or damage retrieval.

## Remediation

If your rewrites add facts the user did not provide, redo the table and label
each added term as either supported synonym, inferred intent, or unsafe
assumption. Remove unsafe assumptions before retesting.
