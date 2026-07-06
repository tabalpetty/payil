# Day03-order014: Streaming Responses, WebSockets, And Server-Sent Events

## Traceability

| Field | Value |
|---|---|
| Curriculum order | Day03-order014 |
| Section | Layer 2 - Prompt systems and application interaction |
| Topic | Streaming responses, WebSockets, and server-sent events |
| Knowledge category | Skill; Knowledge; Representation / Location |
| Knowledge type | Procedural; Causal; Embedded |
| Artifact family | Lab runbook; configuration inspection worksheet; cause-effect worksheet |

## Purpose

Design response streaming when partial output improves user experience, while
handling moderation, disconnects, partial failures, and final validation.

## Artifact A: Streaming Path

```text
client opens stream
  -> app validates request
  -> model produces chunks
  -> app buffers or filters chunks
  -> client receives partial output
  -> final response validated and logged
```

## Artifact B: Streaming Risk Table

| Risk | Cause | Mitigation | Evidence |
|---|---|---|---|
| Client disconnect |  |  |  |
| Unsafe partial output |  |  |  |
| Final answer incomplete |  |  |  |
| Backpressure |  |  |  |
| Stream timeout |  |  |  |

## Artifact C: Protocol Choice

| Scenario | WebSocket, SSE, or non-streaming? | Why |
|---|---|---|
| One-way text generation |  |  |
| Bidirectional interactive session |  |  |
| Background batch job |  |  |
| Browser-based assistant |  |  |

## Artifact D: Embedded Inspection Record

Inspect a real or simulated streaming integration.

| Config surface | Observable fact to record | My notes |
|---|---|---|
| Protocol | WebSocket, server-sent events, or non-streaming HTTP |  |
| Chunk handling | buffering, token/chunk forwarding, final marker |  |
| Moderation point | before stream, during stream, after stream, or combined |  |
| Disconnect behavior | cancellation, background completion, cleanup |  |
| Timeout/backpressure | idle timeout, max stream duration, client flow control |  |
| Final validation | schema, citation, truncation, safety review |  |
| Logging | request ID, partial failure, emitted length, final status |  |

## Self-Check

| Question | My answer |
|---|---|
| What user problem does streaming solve? |  |
| Why can streaming complicate safety checks? |  |
| What should be logged if a stream fails halfway? |  |

## Mastery Evidence

You can choose streaming only when partial output improves the experience, pick
an appropriate protocol pattern, and handle disconnects, moderation, timeout,
and final validation.

## Remediation

If your answer says streaming is always better, redo Artifact C and choose
non-streaming for at least one scenario. Then add how unsafe partial output and
half-finished streams are handled.
