# Day 3 Answer Guidance

This guide gives review criteria, not one perfect answer. Day 3 topics require
tradeoff judgment, so strong answers explain constraints, rejected alternatives,
failure behavior, and evidence.

## What Strong Day 3 Evidence Looks Like

| Evidence type | Strong evidence | Weak evidence |
|---|---|---|
| Retrieval decision | Connects search method to query type, corpus shape, latency, and evaluation result. | Says "use hybrid" or "use vector search" without conditions. |
| Prompt decision | Shows ownership, versioning, tests, rollout, rollback, and quality risk. | Treats prompts as text snippets edited informally. |
| API pattern | Matches synchronous, asynchronous, streaming, or batch behavior to user experience and failure mode. | Picks a pattern because it is familiar. |
| Resilience | Names detection, retry or fallback behavior, user experience, and logging. | Lists generic retries without limits or observability. |
| Troubleshooting | Starts from symptoms, isolates likely causes, gathers evidence, and verifies the fix. | Changes many things at once or relies on guesses. |

## Review Questions For Every Artifact

1. Did the learner name the scenario and constraints?
2. Did the learner make a decision rather than only list options?
3. Did the learner explain why the chosen option fits the constraints?
4. Did the learner reject at least one tempting alternative?
5. Did the learner identify failure modes and evidence?
6. Did the learner state what would change their decision?

## Common Remediation Patterns

| Gap | Remediation |
|---|---|
| Confuses retrieval quality with answer quality | Rebuild the retrieval path and label retrieval recall, ranking quality, context assembly, model response, and answer validation separately. |
| Chooses every advanced retrieval technique | Force a cost-latency-complexity budget and require one rejected technique with rationale. |
| Treats prompt engineering as trial and error | Add a regression set, expected output contract, prompt owner, version, and rollback step. |
| Picks synchronous APIs for long jobs | Compare user wait time, timeout risk, status tracking, retry behavior, and notification needs. |
| Adds retries without control | Add max attempts, backoff, jitter, idempotency, rate-limit behavior, timeout budget, and alert threshold. |
| Cannot troubleshoot RAG | Use a symptom-to-layer table: query, filters, embedding, index, retrieval, reranking, prompt assembly, model output, validation, logging. |

## Worked Exemplar 1: Retrieval Strategy

This is one strong answer, not the only strong answer.

**Scenario:** A support assistant answers product questions from manuals,
release notes, and incident tickets. Users often search by exact error code or
vague symptom.

| Decision area | Strong sample answer |
|---|---|
| Retrieval choice | Use hybrid search: semantic search for vague symptoms, keyword boost for exact error codes, metadata filters for product version and entitlement, and recency boost for release notes. |
| Rejected alternative | Reject semantic-only retrieval because exact error codes and product-version constraints are too important. |
| Main risk | Keyword boost may over-rank documents that mention an error code without solving the issue. |
| Evidence | Compare top-5 retrieval before/after on a golden set with exact-code, symptom, and recent-release queries. Track relevant chunk rank, unauthorized-result count, and latency. |
| Inspection surface | Check metadata fields, index version, last ingestion time, and scoring/boost rules. |

Why this is strong: it connects the method to query types, states a rejected
alternative, names a failure mode, and defines review evidence.

Weak version:

```text
Use hybrid search because it is better than vector search.
```

Why weak: no condition, no tradeoff, no scoring rule, no evidence, and no
inspection target.

## Worked Exemplar 2: API And Resilience Pattern

This example calibrates the Day 3 capstone decision record.

**Scenario:** A compliance team uploads 200 documents and wants a summarized
risk report. The report can arrive later, but the user needs status and a clear
failure record.

| Decision area | Strong sample answer |
|---|---|
| API pattern | Use asynchronous processing. Create a job ID, store input location, enqueue work, process with bounded retries, store result, and expose status polling. |
| Rejected alternative | Reject synchronous invocation because document volume and processing time make request timeout likely. |
| Validation | Validate file type, size, tenant, and required metadata before job creation. Validate output schema before marking the job complete. |
| Retry policy | Retry transient model/API failures with capped exponential backoff and jitter. Do not retry validation failures or safety blocks unchanged. |
| Fallback/degradation | If model service is unavailable, keep job in retryable state or pause queue. Do not produce an ungrounded risk report as fallback. |
| Observability | Link request ID, job ID, worker logs, model ID, token counts, attempts, failed step, and final status. |

Why this is strong: it fits user experience, explains why synchronous is wrong,
distinguishes retryable and non-retryable failures, and preserves audit
evidence.

Weak version:

```text
Use a queue and retry failures.
```

Why weak: no status lifecycle, no idempotency, no retry limits, no validation,
no user experience, and no trace evidence.

## Exit Standard

Day 3 is ready when the learner can design and defend a GenAI application path
that includes retrieval, prompt governance, API integration, failure handling,
and observability. The learner should be able to explain the design under a
scenario change without rebuilding it from memory prompts.
