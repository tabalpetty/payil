# Day03-order015: Token Limits, Request Validation, And Response Handling

## Traceability

| Field | Value |
|---|---|
| Curriculum order | Day03-order015 |
| Section | Layer 2 - Prompt systems and application interaction |
| Topic | Token limits, request validation, and response handling |
| Knowledge category | Knowledge; Skill |
| Knowledge type | Declarative; Procedural; Causal |
| Artifact family | Lab runbook; cause-effect worksheet; retrieval cards |

## Purpose

Prevent token-limit failures, malformed requests, unexpected output shapes, and
unsafe response handling before they reach the user.

## Artifact A: Validation Checklist

| Check | Rule | Failure response |
|---|---|---|
| Input length |  |  |
| Required fields |  |  |
| Allowed file types |  |  |
| Prompt/context budget |  |  |
| Output schema |  |  |
| Sensitive data handling |  |  |

## Artifact B: Token Budget

| Component | Estimated tokens | Keep, summarize, or drop? |
|---|---:|---|
| System instructions |  |  |
| Developer/application instructions |  |  |
| User request |  |  |
| Conversation history |  |  |
| Retrieved context |  |  |
| Output allowance |  |  |

## Artifact C: Cause-Effect Notes

| Failure | Likely cause | Prevention |
|---|---|---|
| Context overflow |  |  |
| Truncated answer |  |  |
| Invalid JSON |  |  |
| Missing citation |  |  |
| User-provided injection attempt |  |  |

## Self-Check

| Question | My answer |
|---|---|
| Why should token budgeting happen before invocation? |  |
| What is the difference between request validation and response validation? |  |
| What should happen when the output schema is invalid? |  |

## Mastery Evidence

You can budget prompt and output tokens, reject invalid requests before
invocation, validate response shape, and define safe behavior for malformed or
truncated output.

## Remediation

If your validation only checks whether the model returns text, add input length,
required fields, context budget, output schema, truncation handling, and
sensitive-data handling to the checklist.
