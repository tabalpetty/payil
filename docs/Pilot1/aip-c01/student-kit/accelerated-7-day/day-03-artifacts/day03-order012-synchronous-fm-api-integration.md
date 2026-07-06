# Day03-order012: Synchronous FM API Integration

## Traceability

| Field | Value |
|---|---|
| Curriculum order | Day03-order012 |
| Section | Layer 2 - Prompt systems and application interaction |
| Topic | Synchronous FM API integration |
| Knowledge category | Skill; Representation / Location |
| Knowledge type | Procedural; Embedded |
| Artifact family | Lab runbook; configuration inspection worksheet |

## Purpose

Design a direct request-response model invocation path for user-facing actions
where latency, validation, and timeout behavior are acceptable.

## Artifact A: Request Path

```text
client
  -> application endpoint
  -> validate request
  -> authorize user
  -> assemble prompt
  -> invoke model
  -> validate response
  -> return response
  -> log evidence
```

My request path notes:

```text

```

## Artifact B: Integration Checklist

| Concern | Design choice | Evidence |
|---|---|---|
| Authentication |  |  |
| Authorization |  |  |
| Request validation |  |  |
| Prompt assembly |  |  |
| Timeout budget |  |  |
| Response validation |  |  |
| Error response |  |  |
| Logging |  |  |

## Artifact C: Fit Test

| Scenario | Synchronous fit? | Why |
|---|---|---|
| Chat answer under five seconds |  |  |
| Overnight document processing |  |  |
| User-visible draft generation |  |  |
| Long multi-tool workflow |  |  |

## Artifact D: Embedded Inspection Record

Inspect a real or simulated synchronous FM request shape.

| Config surface | Observable fact to record | My notes |
|---|---|---|
| Endpoint or operation | model invocation operation and route |  |
| Auth context | caller identity and permissions |  |
| Request body | prompt/messages, model ID, parameters, max output |  |
| Validation | input schema, length, allowed content types |  |
| Timeout | client timeout and server timeout budget |  |
| Response handling | output schema, citation/grounding checks, malformed output |  |
| Logs/traces | request ID, model ID, latency, token counts, error class |  |

## Self-Check

| Question | My answer |
|---|---|
| What makes a workload suitable for synchronous FM integration? |  |
| Where do validation and authorization happen? |  |
| What should the user see when the model call times out? |  |

## Mastery Evidence

You can design a synchronous FM request path with validation, authorization,
prompt assembly, timeout behavior, response validation, and logging.

## Remediation

If your path starts at model invocation, add the missing application steps
before and after the model call. Include request validation, authz, timeout,
response validation, and user-safe error handling.
