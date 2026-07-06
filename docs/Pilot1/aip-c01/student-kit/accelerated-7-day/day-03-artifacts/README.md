# Day 3 Focused Artifacts

Day 3 moves from a basic RAG design into production-style integration:
advanced retrieval, prompt lifecycle, FM API patterns, and resilience.

Use these files after reading:

- `../study-guides/day-03-advanced-retrieval-prompt-governance-api-resilience.md`
- `../presentations/day-03-slides.md`
- `../day-03-integration-decision-record.md`

## How To Work Through Day 3

Day 3 has more focused topics than Days 1 and 2. Complete them in order, but
use the tiering below as pacing guidance. It is not permission to skip quality.
All topics remain in scope for learning; the tiers only describe how to spend
the limited in-day attention.

| Tier | Topics | Required action |
|---|---|---|
| Core in-session | 001, 002, 004, 006, 009, 010, 012, 013, 016, 017, 018 | Fill the worksheet enough to support review. |
| Guided inspection | 005, 011, 014, 015 | Fill the configuration/interface inspection section and self-check. |
| Compressed but assessed | 003, 007, 008 | Read, answer the self-check, and pull one idea into the capstone decision record. |

The order matters because later API and resilience decisions depend on earlier
retrieval and prompt-governance choices.

If a compressed topic is weak after self-check, do not mark it complete. Extend
Day 3 toward the seven-to-eight-hour range or carry the topic into named
remediation. The accelerated path may move faster; it should not pretend that
unmastered topics were mastered.

| Order | Artifact |
|---|---|
| Day03-order001 | Hybrid search and custom scoring |
| Day03-order002 | Reranking |
| Day03-order003 | Query expansion, decomposition, and transformation |
| Day03-order004 | Vector-store ingestion, synchronization, refresh, and maintenance |
| Day03-order005 | Retrieval APIs, function interfaces, and MCP access |
| Day03-order006 | RAG quality evaluation and retrieval troubleshooting |
| Day03-order007 | Conversation context, history, intent, and state management |
| Day03-order008 | Advanced prompt engineering and iterative refinement |
| Day03-order009 | Prompt versioning, repositories, approvals, and governance |
| Day03-order010 | Prompt regression testing and quality assurance |
| Day03-order011 | Prompt chaining, branching, and Bedrock Prompt Flows |
| Day03-order012 | Synchronous FM API integration |
| Day03-order013 | Asynchronous FM processing |
| Day03-order014 | Streaming responses, WebSockets, and server-sent events |
| Day03-order015 | Token limits, request validation, and response handling |
| Day03-order016 | Retries, exponential backoff, rate limiting, and timeouts |
| Day03-order017 | Fallbacks, circuit breakers, and graceful degradation |
| Day03-order018 | Distributed tracing and FM API observability |

## Pilot Instructions

As the learner, fill each artifact honestly. As the teacher, mark whether the
prompt gave enough support to produce the evidence. As the examiner, decide
whether the completed artifact proves usable knowledge, not just exposure.

For every file, record:

- what you decided;
- why you rejected alternatives;
- what evidence would convince another reviewer;
- what you would remediate if the answer is weak.

Use `day-03-answer-guidance.md` after your first attempt, not before.

## Review-Ready Gate

An artifact is review-ready when it contains enough evidence for another person
to decide whether the learner can use the topic under scenario pressure.

For each topic file, check:

- the traceability table matches the curriculum map;
- the learner made at least one scenario-specific decision;
- the learner explained why the decision fits the constraints;
- the learner named at least one risk, failure mode, or rejected alternative;
- the learner identified evidence that would prove the design works;
- the learner completed the self-check;
- the learner wrote a remediation action for any weak answer.

Do not mark a Day 3 artifact complete only because the tables are filled. The
answers must show usable retrieval, prompt, API, resilience, or observability
judgment.
