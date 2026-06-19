# Day 3 Slides: Retrieval, Prompt Governance, APIs, Resilience

## Slide 1: Today's Job

- Connect RAG and prompts to production application behavior.
- Choose API patterns and resilience controls.

## Slide 2: Advanced Retrieval

- Hybrid search
- Reranking
- Query expansion
- Query decomposition
- Query transformation
- Metadata filtering

## Slide 3: Prompt Governance

- Owner
- Version
- Approval
- Regression tests
- Rollout
- Rollback
- Monitoring

## Slide 4: API Pattern Choice

- Synchronous: direct response.
- Asynchronous: longer-running work.
- Streaming: partial output improves experience.
- Batch: offline throughput.

## Slide 5: Resilience Questions

- How detected?
- Retry or not?
- Fallback or not?
- What does user see?
- What is logged?
- Who is alerted?

## Slide 6: Failure Modes

- Throttling
- Timeout
- Malformed response
- Retrieval outage
- Model/Region unavailable
- Safety block

## Slide 7: Artifact Prompt

Fill the integration decision record with chosen patterns, rejected
alternatives, and failure handling.

