# Day03-order016: Retries, Exponential Backoff, Rate Limiting, And Timeouts

## Traceability

| Field | Value |
|---|---|
| Curriculum order | Day03-order016 |
| Section | Layer 2 - Prompt systems and application interaction |
| Topic | Retries, exponential backoff, rate limiting, and timeouts |
| Knowledge category | Skill; Knowledge |
| Knowledge type | Procedural; Causal; Conditional |
| Artifact family | Lab runbook; decision table; cause-effect worksheet |

## Purpose

Handle transient failures without amplifying load, duplicating work, or leaving
users waiting indefinitely.

## Artifact A: Resilience Policy

| Failure | Retry? | Backoff | Timeout | User response |
|---|---|---|---|---|
| Throttling |  |  |  |  |
| Network timeout |  |  |  |  |
| Validation failure |  |  |  |  |
| Safety block |  |  |  |  |
| Downstream dependency unavailable |  |  |  |  |

## Artifact B: Retry Runbook

| Step | Action | Evidence |
|---:|---|---|
| 1 | Classify error as retryable or non-retryable. |  |
| 2 | Check request idempotency. |  |
| 3 | Apply capped exponential backoff and jitter. |  |
| 4 | Stop at timeout budget or max attempts. |  |
| 5 | Return clear user-safe failure. |  |
| 6 | Log error class, attempts, and latency. |  |

## Artifact C: Cause-Effect Reflection

```text
Unbounded retries cause...

Too-short timeouts cause...

Too-long timeouts cause...

Rate limiting protects...
```

## Self-Check

| Question | My answer |
|---|---|
| Why should not every error be retried? |  |
| What is jitter and why does it matter? |  |
| How do retries interact with user experience? |  |

## Mastery Evidence

You can distinguish retryable from non-retryable failures, apply capped backoff
with jitter, respect timeout budgets, and return user-safe failures.

## Remediation

If your policy retries every failure, classify each row as retryable,
non-retryable, or fail-closed. Add max attempts, timeout budget, idempotency,
and logging before review.
