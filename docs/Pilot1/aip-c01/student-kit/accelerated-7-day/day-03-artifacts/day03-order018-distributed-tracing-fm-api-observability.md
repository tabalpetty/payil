# Day03-order018: Distributed Tracing And FM API Observability

## Traceability

| Field | Value |
|---|---|
| Curriculum order | Day03-order018 |
| Section | Layer 2 - Prompt systems and application interaction |
| Topic | Distributed tracing and FM API observability |
| Knowledge category | Skill; Knowledge; Representation / Location |
| Knowledge type | Procedural; Diagnostic; Causal; Embedded |
| Artifact family | Troubleshooting worksheet; lab runbook; configuration inspection worksheet |

## Purpose

Make a GenAI request path inspectable from user request through retrieval,
prompt assembly, model invocation, validation, and response.

## Artifact A: Trace Map

```text
request_id
  -> app span
  -> retrieval span
  -> prompt assembly span
  -> model invocation span
  -> validation span
  -> response span
```

My trace fields:

```text

```

## Artifact B: Observability Checklist

| Signal | Capture? | Why | Redaction needed? |
|---|---|---|---|
| Request ID |  |  |  |
| User or tenant ID |  |  |  |
| Model ID |  |  |  |
| Token counts |  |  |  |
| Latency by step |  |  |  |
| Retrieval result count |  |  |  |
| Error class |  |  |  |
| Prompt/version ID |  |  |  |

## Artifact C: Embedded Inspection Record

Inspect a real or simulated tracing/logging configuration.

| Config surface | Observable fact to record | My notes |
|---|---|---|
| Trace propagation | request ID carried across app, retrieval, model, validation |  |
| Span names | app, retrieval, prompt assembly, model call, validation |  |
| Metrics | latency, token counts, result count, retry count, cost proxy |  |
| Error taxonomy | throttle, timeout, validation, safety block, dependency failure |  |
| Sensitive fields | prompt/output redaction or sampling policy |  |
| Dashboard | p95 latency, error rate, model failures, retrieval failures |  |
| Alert rule | threshold, owner, escalation path |  |

## Artifact D: Diagnostic Scenario

```text
Symptom:

Trace evidence:

Likely cause:

Next diagnostic step:

Fix:
```

## Self-Check

| Question | My answer |
|---|---|
| Why is a single request ID important? |  |
| Which observability fields could expose sensitive data if logged poorly? |  |
| How does tracing support troubleshooting and governance? |  |

## Mastery Evidence

You can sketch the trace path, choose useful signals, protect sensitive log
data, and use the trace to isolate a performance or quality problem.

## Remediation

If your observability plan logs raw prompts, raw outputs, or sensitive user
data without controls, revise the checklist with redaction rules. Then add one
diagnostic scenario that uses request ID, latency, model ID, retrieval count,
and error class to isolate the issue.
