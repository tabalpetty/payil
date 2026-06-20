# Day01-order004: Application Integration Patterns

## Traceability

| Field | Value |
|---|---|
| Curriculum order | Day01-order004 |
| Section | Layer 0 - GenAI and AWS foundations |
| Topic | API, event-driven, serverless, container, and workflow fundamentals |
| Knowledge category | Knowledge |
| Knowledge type | Conceptual; Conditional |
| Artifact family | Decision table with contrasting scenarios; concept map |

## Purpose

Know when basic application integration patterns fit GenAI workloads.

## Artifact A: Pattern Comparison

| Pattern | Best fit | Poor fit | GenAI-specific concern |
|---|---|---|---|
| Synchronous API |  |  |  |
| Asynchronous job |  |  |  |
| Streaming response |  |  |  |
| Event-driven workflow |  |  |  |
| Serverless function |  |  |  |
| Containerized service |  |  |  |
| Multi-step workflow |  |  |  |

## Artifact B: Choose And Reject

| Scenario | Chosen pattern | Rejected pattern | Why |
|---|---|---|---|
| User needs an immediate short answer. |  |  |  |
| Document processing may take minutes. |  |  |  |
| User benefits from seeing tokens as generated. |  |  |  |
| Workflow requires approval before final action. |  |  |  |

## Self-Check

| Question | My answer |
|---|---|
| What makes synchronous integration risky for long GenAI tasks? |  |
| What changes if the workload is batch-oriented? |  |
| Which pattern would I choose under strict latency pressure? |  |
