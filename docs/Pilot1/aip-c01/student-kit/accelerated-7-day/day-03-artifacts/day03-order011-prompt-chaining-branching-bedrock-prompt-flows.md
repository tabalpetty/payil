# Day03-order011: Prompt Chaining, Branching, And Bedrock Prompt Flows

## Traceability

| Field | Value |
|---|---|
| Curriculum order | Day03-order011 |
| Section | Layer 2 - Prompt systems and application interaction |
| Topic | Prompt chaining, branching, and Bedrock Prompt Flows |
| Knowledge category | Knowledge; Skill; Representation / Location |
| Knowledge type | Conceptual; Procedural; Strategic; Embedded |
| Artifact family | Architecture decision record; lab runbook; configuration inspection worksheet |

## Purpose

Design multi-step prompt workflows where each step has a clear responsibility,
input contract, output contract, and failure behavior.

## Artifact A: Flow Sketch

```text
input
  -> classify intent
  -> retrieve or call tool
  -> draft response
  -> validate response
  -> return or escalate
```

My flow:

```text

```

## Artifact B: Step Contract

| Flow step | Input | Output | Failure handling |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

## Artifact C: Branching Decision

| Condition | Branch | Why | Evidence logged |
|---|---|---|---|
| Low confidence |  |  |  |
| Missing context |  |  |  |
| Unsafe request |  |  |  |
| Tool failure |  |  |  |

## Artifact D: Mini Architecture Decision Record

| ADR field | Response |
|---|---|
| Decision |  |
| Context and constraints |  |
| Chosen flow pattern |  |
| Rejected alternative |  |
| Main risk |  |
| Evidence that would prove it works |  |
| Rollback or simplification path |  |

## Artifact E: Embedded Inspection Record

Inspect a real or simulated prompt-flow configuration. For Bedrock Prompt Flows
or an equivalent workflow, focus on the embedded workflow shape.

| Config surface | Observable fact to record | My notes |
|---|---|---|
| Flow inputs | required fields and validation |  |
| Nodes | prompt, model, condition, tool, retrieval, validation |  |
| Connections | execution order and branch paths |  |
| Prompt versions | version or identifier used by each prompt node |  |
| Branch conditions | confidence, missing context, unsafe request, tool failure |  |
| Failure path | retry, fallback, human review, safe stop |  |
| Trace evidence | flow run ID, node status, latency, error class |  |

## Self-Check

| Question | My answer |
|---|---|
| When is chaining better than one large prompt? |  |
| What makes a prompt flow maintainable? |  |
| Where should validation happen in the flow? |  |

## Mastery Evidence

You can split a multi-step prompt workflow into clear steps, define input and
output contracts, add branches, and describe failure handling for each step.

## Remediation

If your flow is a single large prompt with no contracts, split it into classify,
retrieve/tool, draft, validate, and respond steps. Add one branch for missing
context and one branch for unsafe requests.
