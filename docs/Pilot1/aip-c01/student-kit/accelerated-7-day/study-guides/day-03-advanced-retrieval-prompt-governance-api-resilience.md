# Day 3 Study Guide: Advanced Retrieval, Prompt Governance, APIs, And Resilience

## What You Are Learning Today

Day 3 connects retrieval and prompts to real application integration. The
central question is:

```text
How does this GenAI capability behave as part of a production application?
```

By the end of Day 3, you should be able to make and defend decisions about:

- advanced retrieval strategy;
- vector-store freshness and maintenance;
- retrieval API boundaries;
- prompt lifecycle and governance;
- prompt regression testing;
- synchronous, asynchronous, and streaming FM API patterns;
- retries, timeouts, fallbacks, degradation, and observability.

This is a heavy day. Do not try to memorize every pattern. Learn the decision
logic: when to use a pattern, what can go wrong, what evidence proves it works,
and what you would inspect when it fails.

Acceleration does not mean shallow learning. If Day 3 takes closer to eight
hours, that is acceptable for the accelerated route. If a topic still does not
fit, keep the material and mark the gap honestly as remediation or self-paced
continuation.

## Day 3 Workload Tiers

The Day 3 map contains 18 focused topics. In the accelerated route, complete
them with this priority. The priority is about time management, not mastery
standards.

| Tier | Topics | Required action |
|---|---|---|
| Core in-session | 001, 002, 004, 006, 009, 010, 012, 013, 016, 017, 018 | Fill the worksheet enough to support review. |
| Guided inspection | 005, 011, 014, 015 | Fill the configuration or interface inspection section and self-check. |
| Compressed but assessed | 003, 007, 008 | Read, answer the self-check, and pull one idea into the capstone decision record. |

The capstone file, `../day-03-integration-decision-record.md`, remains
required. It is the evidence that the pieces connect.

## The Day 3 System Path

```text
user request
  -> validate and authorize
  -> understand intent and state
  -> transform query if needed
  -> retrieve and filter
  -> rerank or rescore
  -> assemble governed prompt
  -> invoke model through an API pattern
  -> validate response
  -> retry, fallback, or degrade if needed
  -> trace, log, evaluate, and improve
```

Every arrow is a design decision. Weak designs hide these decisions. Strong
designs make them inspectable.

## Advanced Retrieval

Basic semantic retrieval is often a good starting point, but it may not be
enough when exact identifiers, product names, recent documents, permissions,
or multi-part questions matter.

| Technique | Purpose | Use when | Watch for |
|---|---|---|---|
| Hybrid search | Combine semantic and keyword signals. | Exact terms and meaning both matter. | Keyword matches can over-rank shallow results. |
| Custom scoring | Add freshness, priority, or domain-specific boosts. | Ranking must reflect business or operational rules. | Scoring can hide bias or stale assumptions. |
| Reranking | Reorder retrieved candidates with a stronger relevance step. | The right chunk is retrieved but ranked too low. | Extra latency and cost. |
| Query expansion | Add synonyms or related terms. | The user query is too narrow. | Added terms can drift from user intent. |
| Query decomposition | Split one complex question into subqueries. | The user asks multiple things at once. | Subanswers may be combined incorrectly. |
| Query transformation | Rewrite user wording into retrieval-friendly form. | User language is vague or conversational. | The rewrite may add unsupported assumptions. |

Decision rule:

```text
Choose the simplest retrieval method that meets recall, precision, latency,
security, freshness, and cost constraints.
```

Day 2 promised that Day 3 would go deeper on hybrid retrieval. The depth is
this: hybrid search is not "semantic plus keyword because more is better." It
is a scoring design. You decide which signals matter, when to boost them, when
to filter before ranking, and how to measure whether the new ranking improved
retrieval.

## Reranking Mechanics

Think of retrieval in two stages:

```text
candidate generation -> reranking -> prompt context selection
```

The first stage retrieves a broader candidate set. The reranker then compares
the query and candidates more carefully and reorders them. This is useful when
the relevant chunk exists in the candidate set but does not land near the top.

Reranking does not fix:

- missing documents;
- bad chunking;
- stale indexes;
- wrong filters;
- permission mistakes;
- a prompt that ignores good evidence.

Evidence to collect:

- relevant chunk rank before and after reranking;
- answer quality before and after;
- latency added;
- cost added;
- failures where reranking made results worse.

## Vector-Store Maintenance

A vector store is not correct forever after initial ingestion. It must stay
aligned with source truth.

Maintenance events include:

- new source document;
- changed source document;
- deleted source document;
- permission or entitlement change;
- metadata correction;
- embedding model change;
- index rebuild;
- scheduled freshness validation.

For embedded/config knowledge, inspect a real or simulated configuration
surface. Examples:

- ingestion job status and last successful sync time;
- failed document count;
- metadata fields available for filtering;
- vector index dimensions and distance metric;
- index rebuild plan or blue/green index identifier;
- deletion propagation evidence;
- access-control or entitlement filter source.

If a learner cannot say what they would inspect, they do not yet own the
embedded part of the knowledge.

## Retrieval APIs, Function Interfaces, And MCP Access

Retrieval should be exposed through a controlled interface rather than ad hoc
queries scattered through application code.

An interface contract should specify:

- caller identity;
- input schema;
- authorization check;
- exposed retrieval parameters;
- server-controlled retrieval parameters;
- output schema;
- citation/source fields;
- error responses;
- timeout behavior;
- audit/log fields.

For agent or MCP-style access, the key question is not "can the model call a
tool?" The key question is whether the tool boundary is safe, typed,
permission-aware, observable, and limited enough to prevent accidental or
unauthorized retrieval.

## RAG Troubleshooting

When a RAG answer is poor, isolate the layer:

```text
user query
  -> query rewrite
  -> filters
  -> embedding/index
  -> retrieved chunks
  -> reranking
  -> prompt assembly
  -> model output
  -> validation/citation
```

Use a one-change-at-a-time rule. If you change chunking, prompt wording, model,
and filters together, you may improve the answer but learn nothing.

Common symptoms:

| Symptom | Likely place to inspect |
|---|---|
| Correct source never appears | indexing, metadata filters, query rewrite, permissions |
| Correct source appears too low | reranking, scoring, chunking |
| Correct source appears in prompt but answer is wrong | prompt instructions, model behavior, response validation |
| Answer cites stale source | refresh pipeline, source timestamps, index maintenance |
| Unauthorized content appears | entitlement filter, caller identity, retrieval API contract |

## Conversation Context And State

Conversation history is not automatically useful context.

Decide where each state element belongs:

| State element | Typical location |
|---|---|
| Current user request | prompt |
| Current task intent | prompt or application state |
| Long history | summary or durable store |
| Retrieved facts | prompt with source IDs |
| Tool results | prompt if needed, log for trace |
| Sensitive data | minimize, redact, or exclude |

State failures are subtle. Old turns can distract the model, stale summaries
can preserve wrong assumptions, and sensitive data can be repeated beyond need.

## Prompt Engineering As Controlled Experiment

Weak prompt iteration:

```text
try wording -> dislike answer -> try new wording -> repeat
```

Strong prompt iteration:

```text
name failure
  -> propose change
  -> predict effect
  -> test against cases
  -> measure improvement and new risk
```

Every prompt change should have:

- hypothesis;
- affected examples;
- expected behavior;
- regression risk;
- release decision.

## Prompt Governance And RACI

Prompts can change application behavior. Treat them as governed assets.

A governed prompt has:

- owner;
- approved use case;
- version history;
- review and approval rule;
- regression test set;
- rollout plan;
- rollback plan;
- monitoring owner;
- audit evidence.

RACI is a simple way to make ownership inspectable:

| Role | Meaning |
|---|---|
| Responsible | Does the work. |
| Accountable | Owns the outcome. |
| Consulted | Gives required input. |
| Informed | Must know about the change. |

Prompt governance fails when everyone can edit a prompt but nobody owns the
behavior, test result, rollout, rollback, or incident response.

## Prompt Regression Testing

A regression set should include:

| Test type | What it catches |
|---|---|
| Happy path | Normal intended behavior |
| Ambiguous request | Clarification behavior |
| Missing context | Refusal or bounded uncertainty |
| Unsafe request | Safety handling |
| Output format | JSON/schema/table failures |
| Production miss | Known real-world weak case |

Regression testing is not the same as model evaluation. Model evaluation asks
whether a model is suitable. Prompt regression asks whether a prompt change
broke behavior you depend on.

## Prompt Chaining And Bedrock Prompt Flows

Use a multi-step prompt flow when separating responsibilities improves control:

```text
classify intent
  -> retrieve or call tool
  -> draft response
  -> validate response
  -> return, retry, or escalate
```

Each step needs:

- purpose;
- input contract;
- output contract;
- branch conditions;
- failure behavior;
- trace evidence.

A Prompt Flow-style design should be inspectable as configuration: nodes,
connections, input/output bindings, branch conditions, model or prompt version,
and failure path. If those are missing, the learner has only drawn a diagram,
not inspected embedded workflow knowledge.

## API Pattern Selection

| Pattern | Use when | Watch for |
|---|---|---|
| Synchronous | User needs a direct response and latency is acceptable. | Timeout, user wait time, retry behavior. |
| Asynchronous | Work may take longer or can finish later. | Status tracking, idempotency, notification. |
| Streaming | User benefits from partial output. | Partial failures, client disconnects, output moderation. |
| Batch | Large sets can run offline. | Throughput, cost, scheduling, retry and checkpointing. |

Decision rule:

```text
Choose based on user experience, latency, workload size, reliability, and
failure behavior.
```

Synchronous integration still needs validation, authorization, prompt assembly,
timeout handling, response validation, and logging. Asynchronous integration
adds job ID, idempotency, status lifecycle, result storage, and notification.
Streaming adds partial-output handling, disconnect behavior, and final
validation.

## Token Limits And Response Handling

Before invocation:

- validate request shape;
- reject unsupported inputs;
- estimate token budget;
- decide what to keep, summarize, retrieve, or drop.

After invocation:

- validate output schema;
- detect truncation;
- check citation or grounding requirements;
- return user-safe errors for malformed output.

Token management is not just cost control. It changes answer quality and
failure behavior.

## Resilience

A GenAI app must handle ordinary distributed-system failures plus
model-specific failures.

Plan for:

- throttling;
- timeouts;
- malformed output;
- safety blocks;
- retrieval failures;
- unavailable model or Region;
- context overflow;
- cost or latency spikes.

For each failure, define:

1. how it is detected;
2. whether it is retried;
3. whether fallback is safe;
4. what the user sees;
5. what is logged;
6. what alert or review happens.

Retries need limits: max attempts, timeout budget, capped exponential backoff,
jitter, idempotency, and clear stop conditions.

Fallbacks are not always safe. Do not fall back to an ungrounded answer when
grounding is required. Do not bypass permissions to preserve availability.

## Distributed Tracing And Observability

A useful trace connects the whole request:

```text
request_id
  -> application span
  -> retrieval span
  -> prompt assembly span
  -> model invocation span
  -> validation span
  -> response span
```

Useful fields:

- request ID;
- tenant or user context, redacted where needed;
- prompt version;
- model ID;
- token counts;
- retrieval result count;
- latency by step;
- error class;
- retry count;
- fallback path.

Do not casually log raw prompts, raw outputs, or sensitive data. Observability
must support troubleshooting and governance without creating a privacy problem.

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
2. How reranking differs from query rewriting.
3. What configuration evidence proves a vector store is fresh.
4. Why prompt changes need ownership and regression tests.
5. What RACI adds to prompt governance.
6. When streaming is better than synchronous response.
7. Why some failures should not be retried.
8. What trace fields would isolate a slow or bad response.

Then fill the Day 3 integration decision record.
