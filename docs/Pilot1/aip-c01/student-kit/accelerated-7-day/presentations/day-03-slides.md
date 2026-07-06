# Day 3 Slides: Advanced Retrieval, Prompt Governance, APIs, And Resilience

## How To Use This Deck

This is not a blank slide-building assignment for the learner. It is a
teaching and review deck for the accelerated path. Read it after the Day 3
study guide and before filling:

- `../day-03-integration-decision-record.md`
- `../day-03-artifacts/README.md`

Learner job: use the slides to reconstruct the decision logic from memory.
Teacher job: use the speaker notes to test whether the learner can explain
tradeoffs, not just name services or patterns.

## Source Traceability

Day 3 supports AIP-C01 objectives around:

- advanced search architectures for FM context;
- query handling systems for retrieval effectiveness;
- consistent retrieval access mechanisms;
- prompt management, governance, regression testing, and prompt flows;
- synchronous, asynchronous, and streaming FM API integration;
- resilient FM interaction patterns, including retry, timeout, fallback, and
  observability behavior.

Reference source: `../../../source-material/ai-professional-01.objectives.json`.

## Slide 1: Today's Job

Day 3 answers one question:

```text
How does a RAG or prompt capability behave inside a production application?
```

By the end of the day, you should be able to design:

- advanced retrieval choices;
- prompt governance and regression tests;
- API integration pattern;
- resilience behavior;
- observability evidence.

Speaker note: do not let the learner treat Day 3 as "more RAG terms." The
point is application behavior under constraints.

## Slide 2: The Day 3 System Path

```text
user request
  -> validate and authorize
  -> understand intent/state
  -> retrieve or transform query
  -> rerank/filter context
  -> assemble governed prompt
  -> invoke model through API pattern
  -> validate response
  -> retry/fallback/degrade if needed
  -> trace, log, evaluate, and improve
```

Teaching point: every arrow is a design decision. Weak designs hide decisions;
strong designs make them inspectable.

## Slide 3: Advanced Retrieval Decision

Basic semantic search may fail when:

- exact terms matter, such as codes, names, part numbers, or policy clauses;
- user language differs from document language;
- documents vary by freshness, jurisdiction, entitlement, or product version;
- the right chunk is retrieved but ranked too low;
- the query contains multiple subquestions.

Decision rule:

```text
Choose the simplest retrieval method that meets recall, precision, latency,
security, freshness, and cost constraints.
```

Learner check: name one case where semantic search alone is enough and one case
where it is not.

## Slide 4: Hybrid Search And Custom Scoring

Hybrid retrieval combines signals:

| Signal | Good for | Watch for |
|---|---|---|
| Semantic similarity | Meaning and paraphrase | May miss exact identifiers |
| Keyword search | Exact terms, codes, names | May over-rank shallow matches |
| Metadata filters | permissions, date, type | Bad metadata causes silent misses |
| Custom scoring | business priority, freshness | Can hide bias or stale assumptions |

Speaker note: custom scoring should be explainable. If nobody can explain why
a chunk ranked first, troubleshooting becomes guesswork.

Artifact link: `../day-03-artifacts/day03-order001-hybrid-search-custom-scoring.md`.

## Slide 5: Reranking

Reranking is useful when the correct evidence is in the candidate set but not
near the top.

```text
retrieve broad candidate set
  -> rerank for relevance
  -> send only the best evidence to prompt context
```

Use reranking when the relevance gain beats the extra cost and latency.

Do not assume reranking fixes:

- missing documents;
- bad chunking;
- wrong metadata filters;
- stale indexes;
- permission leaks.

Artifact link: `../day-03-artifacts/day03-order002-reranking.md`.

## Slide 6: Query Expansion, Decomposition, Transformation

| Technique | What it does | Best fit |
|---|---|---|
| Expansion | Adds related terms or synonyms | User query is too narrow |
| Decomposition | Splits complex request into subqueries | User asks multiple things |
| Transformation | Rewrites into a retrieval-friendly query | User wording is vague or conversational |

Guardrail:

```text
Improve retrieval without changing the user's intent.
```

Common failure: the system "helpfully" adds assumptions and retrieves evidence
for a question the user did not ask.

Artifact link: `../day-03-artifacts/day03-order003-query-expansion-decomposition-transformation.md`.

## Slide 7: Vector Store Maintenance Is Part Of Correctness

A vector store is not correct forever after initial ingestion.

It must handle:

- source document updates;
- deleted documents;
- permission changes;
- metadata corrections;
- embedding model changes;
- index rebuilds;
- freshness checks;
- validation queries.

Teaching point: stale retrieval is not merely an operations problem. It can
become a correctness, security, and compliance problem.

Artifact link: `../day-03-artifacts/day03-order004-vector-store-ingestion-synchronization-refresh-maintenance.md`.

## Slide 8: Retrieval Interfaces

Retrieval should be exposed through a controlled contract:

| Contract area | Example design question |
|---|---|
| Input schema | What can the caller ask for? |
| Authorization | What is the caller allowed to retrieve? |
| Parameters | Which settings are exposed vs server-controlled? |
| Output schema | What evidence and source IDs come back? |
| Errors | How are no-result, timeout, and denied-access cases reported? |
| Logging | What is recorded for audit and troubleshooting? |

Speaker note: ad hoc retrieval calls make agent and application behavior hard
to secure, test, and debug.

Artifact link: `../day-03-artifacts/day03-order005-retrieval-apis-function-interfaces-mcp-access.md`.

## Slide 9: RAG Troubleshooting

When an answer is bad, isolate the layer:

```text
user query
  -> query rewrite
  -> filters
  -> embedding/index
  -> retrieved chunks
  -> reranking
  -> prompt assembly
  -> model output
  -> response validation
```

Rule:

```text
Change one thing at a time, then rerun the golden cases.
```

Common weak answer: "change the prompt." Sometimes correct, often premature.

Artifact link: `../day-03-artifacts/day03-order006-rag-quality-evaluation-retrieval-troubleshooting.md`.

## Slide 10: Conversation State

Conversation history is not automatically good context.

Decide what belongs in:

- prompt context;
- application state;
- durable storage;
- retrieved memory;
- summary;
- discard path.

Risk examples:

- irrelevant old turns distract the model;
- sensitive data is repeated unnecessarily;
- token budget is consumed by stale context;
- user intent changes but state does not.

Artifact link: `../day-03-artifacts/day03-order007-conversation-context-history-intent-state-management.md`.

## Slide 11: Prompt Engineering As Controlled Experiment

Weak prompt refinement:

```text
try wording -> dislike answer -> try new wording -> repeat
```

Strong prompt refinement:

```text
name failure
  -> propose change
  -> predict effect
  -> test against examples
  -> measure improvement and new risk
```

Ask after every prompt edit:

- What failure is this intended to fix?
- Which cases should improve?
- Which cases might get worse?
- What evidence decides ship or reject?

Artifact link: `../day-03-artifacts/day03-order008-advanced-prompt-engineering-iterative-refinement.md`.

## Slide 12: Prompt Governance

Prompts can change application behavior, cost, safety, and compliance.

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

Speaker note: a prompt repository is not just storage. It is change control for
application behavior.

Artifact link: `../day-03-artifacts/day03-order009-prompt-versioning-repositories-approvals-governance.md`.

## Slide 13: Prompt Regression Testing

A useful regression set includes:

| Test type | What it catches |
|---|---|
| Happy path | Expected normal behavior |
| Ambiguous request | Clarification behavior |
| Missing context | Refusal or bounded uncertainty |
| Unsafe request | Safety behavior |
| Output format | JSON/schema/table contract failures |
| Production miss | Known real-world weak case |

Release rule:

```text
Ship only if quality improves without breaking safety, format, latency, or
known edge cases.
```

Artifact link: `../day-03-artifacts/day03-order010-prompt-regression-testing-quality-assurance.md`.

## Slide 14: Prompt Chains And Flows

Use chaining when separate responsibilities improve control:

```text
classify intent
  -> retrieve or call tool
  -> draft response
  -> validate output
  -> return, retry, or escalate
```

Good chains have:

- step purpose;
- input contract;
- output contract;
- branch conditions;
- failure behavior;
- trace evidence.

Bad chains hide complexity and make failures harder to diagnose.

Artifact link: `../day-03-artifacts/day03-order011-prompt-chaining-branching-bedrock-prompt-flows.md`.

## Slide 15: API Pattern Choice

| Pattern | Choose when | Main risk |
|---|---|---|
| Synchronous | User needs direct response and latency is acceptable | timeout, waiting, retry behavior |
| Asynchronous | Work is long-running or can finish later | status tracking, idempotency, notification |
| Streaming | Partial output improves experience | partial failure, moderation, disconnects |
| Batch | Many items can run offline | checkpoints, scheduling, cost control |

Decision rule:

```text
Choose based on user experience, latency, workload size, reliability, and
failure behavior.
```

Artifacts:

- `../day-03-artifacts/day03-order012-synchronous-fm-api-integration.md`
- `../day-03-artifacts/day03-order013-asynchronous-fm-processing.md`
- `../day-03-artifacts/day03-order014-streaming-websockets-server-sent-events.md`

## Slide 16: Synchronous Integration

Synchronous path:

```text
client
  -> application endpoint
  -> validate request
  -> authorize caller
  -> assemble prompt/context
  -> invoke model
  -> validate response
  -> return response or safe error
  -> log evidence
```

Use for direct interactions with acceptable latency.

Do not use blindly for long jobs, large documents, uncertain dependency chains,
or workflows that need durable status tracking.

## Slide 17: Asynchronous Processing

Async path:

```text
request
  -> create job
  -> enqueue work
  -> process with retries
  -> store result
  -> update status
  -> notify user or expose polling endpoint
```

Required design fields:

- job ID;
- idempotency key;
- status lifecycle;
- retry policy;
- result location;
- failure record;
- notification or polling design.

Learner check: explain why "put it on a queue" is not enough.

## Slide 18: Streaming

Streaming is about experience, not magic performance.

Use when:

- user benefits from seeing partial output;
- generation may take long enough that progress matters;
- the client can handle partial results.

Design for:

- client disconnects;
- unsafe partial output;
- final validation;
- stream timeouts;
- logging partial failure.

Learner check: identify one scenario where streaming is the wrong choice.

## Slide 19: Token Limits And Validation

Before model invocation:

- validate request shape;
- reject unsupported inputs;
- estimate prompt/context/output budget;
- decide what to keep, summarize, retrieve, or drop.

After model invocation:

- validate output schema;
- detect truncation;
- check citations or grounding when required;
- return user-safe errors for malformed output.

Artifact link: `../day-03-artifacts/day03-order015-token-limits-request-validation-response-handling.md`.

## Slide 20: Retries, Backoff, Rate Limits, Timeouts

Do not retry everything.

| Failure | Typical response |
|---|---|
| Throttling | capped backoff, jitter, respect rate limits |
| Temporary network failure | retry if idempotent and within timeout budget |
| Validation failure | do not retry unchanged request |
| Safety block | fail closed or route to safe handling |
| Dependency outage | fallback, queue, or degrade if safe |

Speaker note: retries can protect the user or amplify an outage. The difference
is policy.

Artifact link: `../day-03-artifacts/day03-order016-retries-backoff-rate-limiting-timeouts.md`.

## Slide 21: Fallbacks And Circuit Breakers

Fallbacks are not always safe.

Good fallback examples:

- use a smaller model for low-risk summarization;
- return cached public documentation with freshness label;
- queue work for later;
- fail with clear user-safe message.

Unsafe fallback examples:

- bypass permission checks;
- answer without grounding when grounding is required;
- use stale content for regulated decisions;
- hide safety-block reason from logs.

Artifact link: `../day-03-artifacts/day03-order017-fallbacks-circuit-breakers-graceful-degradation.md`.

## Slide 22: Observability

A GenAI request should be traceable:

```text
request_id
  -> app span
  -> retrieval span
  -> prompt assembly span
  -> model invocation span
  -> validation span
  -> response span
```

Useful signals:

- latency by step;
- model ID;
- prompt version;
- token counts;
- retrieval result count;
- error class;
- request ID;
- redacted tenant/user context where appropriate.

Do not casually log raw sensitive prompts or outputs.

Artifact link: `../day-03-artifacts/day03-order018-distributed-tracing-fm-api-observability.md`.

## Slide 23: Day 3 Capstone Decision

Fill the integration decision record:

1. State the application scenario.
2. Choose advanced retrieval strategy.
3. Define prompt ownership, testing, rollout, and rollback.
4. Select API pattern.
5. Define failure handling.
6. List rejected alternatives.
7. Explain what evidence proves the design works.

File: `../day-03-integration-decision-record.md`.

## Slide 24: Examiner Questions

Use these to test readiness:

1. When is hybrid search worth the complexity?
2. How do you prove reranking helped?
3. What makes prompt governance different from prompt storage?
4. When should a workload move from synchronous to asynchronous?
5. Why can streaming complicate moderation or validation?
6. Which failures should not be retried?
7. When is fallback unsafe?
8. What trace evidence would isolate a slow or bad response?

## Slide 25: Exit Standard

Day 3 is complete when you can say:

```text
Given this scenario and constraints,
I choose this retrieval design,
this prompt governance model,
this API pattern,
this failure-handling strategy,
and this observability evidence.

I reject these alternatives because...
I would change my decision if...
```

If you cannot explain the rejected alternatives, the artifact is not ready for
review yet.
