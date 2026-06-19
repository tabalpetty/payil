# Day 3 Study Guide: Advanced Retrieval, Prompt Governance, APIs, And Resilience

## What You Are Learning Today

Day 3 connects retrieval and prompts to real application integration. The
central question is: how does this GenAI capability behave as part of a
production application?

You will make decisions about advanced retrieval, prompt lifecycle, API
patterns, and failure handling.

## Advanced Retrieval

Basic semantic retrieval may not be enough. Professional systems often add:

| Technique | Purpose |
|---|---|
| Hybrid search | Combine semantic and keyword signals. |
| Reranking | Reorder retrieved results using a stronger relevance step. |
| Query expansion | Add related terms to improve recall. |
| Query decomposition | Split complex queries into smaller subqueries. |
| Query transformation | Rewrite vague user input into a better retrieval query. |
| Metadata filtering | Restrict retrieval by user, topic, date, jurisdiction, or permission. |

The tradeoff is usually quality versus cost, latency, complexity, and
operational risk.

## Prompt Governance

Prompts change application behavior. Treat them as governed assets.

Prompt governance includes:

- owner;
- version history;
- review/approval process;
- regression test set;
- rollout plan;
- rollback plan;
- safety review;
- monitoring after release.

If a prompt update changes answer quality, safety, or output format, you need a
way to detect and reverse that change.

## API Pattern Selection

| Pattern | Use when | Watch for |
|---|---|---|
| Synchronous | User needs a direct response and latency is acceptable. | Timeout, user wait time, retry behavior. |
| Asynchronous | Work may take longer or can be processed later. | Status tracking, retries, idempotency, notification. |
| Streaming | User benefits from partial output as it is generated. | Partial failures, client disconnects, output moderation. |
| Batch | Large sets can be processed offline. | Throughput, cost, scheduling, retry and checkpointing. |

Choose based on user experience, latency, workload size, reliability, and
failure behavior.

## Resilience

A GenAI app must handle ordinary distributed-system failures plus model-specific
failures.

Plan for:

- throttling;
- timeouts;
- malformed output;
- safety filter blocks;
- retrieval failures;
- unavailable model or region;
- context length overflow;
- cost or latency spikes.

For each failure, define:

1. how it is detected;
2. whether it is retried;
3. whether fallback is used;
4. what the user sees;
5. what is logged;
6. what alert or review happens.

## Scenario Decision Pattern

When selecting an API or resilience pattern:

```text
Given these constraints...
I choose...
I reject...
The main risk is...
I detect it by...
I mitigate it by...
This decision changes if...
```

## Teach-Back

Close the guide and explain:

1. When hybrid retrieval is worth the extra complexity.
2. Why prompt changes need regression tests.
3. When streaming is better than synchronous response.
4. How you would handle throttling or malformed output.

Then fill the Day 3 integration decision record.

