# Day03-order013: Asynchronous FM Processing

## Traceability

| Field | Value |
|---|---|
| Curriculum order | Day03-order013 |
| Section | Layer 2 - Prompt systems and application interaction |
| Topic | Asynchronous FM processing |
| Knowledge category | Knowledge; Skill; Representation / Location |
| Knowledge type | Conceptual; Procedural; Conditional; Embedded |
| Artifact family | Lab runbook; configuration inspection worksheet; decision table |

## Purpose

Design a job-based FM processing path for workloads that should not block a
user request while the model or workflow completes.

## Artifact A: Async Workflow

```text
request
  -> validate and authorize
  -> create job
  -> enqueue work
  -> process with retries
  -> store result
  -> notify or expose status
```

My workflow:

```text

```

## Artifact B: Job Contract

| Field | Design |
|---|---|
| Job ID |  |
| Idempotency key |  |
| Input location |  |
| Status states |  |
| Retry policy |  |
| Result location |  |
| Notification method |  |
| Failure record |  |

## Artifact C: Decision Table

| Workload | Async fit? | Why | User experience |
|---|---|---|---|
| Bulk document summarization |  |  |  |
| Interactive chat turn |  |  |  |
| Compliance report generation |  |  |  |
| Image batch labeling |  |  |  |

## Artifact D: Embedded Inspection Record

Inspect a real or simulated async processing configuration.

| Config surface | Observable fact to record | My notes |
|---|---|---|
| Queue or job store | queue/topic/table name, retention, visibility/status model |  |
| Job schema | job ID, idempotency key, input location, tenant |  |
| Worker settings | concurrency, timeout, retry limit, dead-letter behavior |  |
| Result store | output location, status update, expiration |  |
| Notification | polling endpoint, event, email, webhook, or callback |  |
| Failure evidence | error class, attempts, failed step, redrive path |  |
| Trace linkage | request ID connected to job ID and worker logs |  |

## Self-Check

| Question | My answer |
|---|---|
| Why does async processing need status tracking? |  |
| What does idempotency protect against? |  |
| When is async worse than synchronous? |  |

## Mastery Evidence

You can design an async FM job with job ID, idempotency, status states, retry
policy, result storage, notification, and failure evidence.

## Remediation

If your async design is just "send it to a queue," add the full job contract:
status lifecycle, idempotency key, retry limits, result location, failure
record, and user notification path.
