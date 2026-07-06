# Day03-order007: Conversation Context, History, Intent, And State Management

## Traceability

| Field | Value |
|---|---|
| Curriculum order | Day03-order007 |
| Section | Layer 2 - Prompt systems and application interaction |
| Topic | Conversation context, history, intent, and state management |
| Knowledge category | Knowledge; Skill |
| Knowledge type | Conceptual; Procedural; Conditional |
| Artifact family | Lab worksheet or runbook; decision table; concept map |

## Purpose

Decide what conversational state belongs in the prompt, what belongs in
application state, and what should be discarded or summarized.

## Artifact A: State Map

| State element | Store where? | Include in prompt? | Why |
|---|---|---|---|
| User profile |  |  |  |
| Current task intent |  |  |  |
| Prior turns |  |  |  |
| Retrieved facts |  |  |  |
| Tool results |  |  |  |
| Sensitive data |  |  |  |

## Artifact B: Context Policy

```text
Keep full conversation history when...

Summarize history when...

Drop history when...

Never include...
```

## Artifact C: Decision Table

| Scenario | State strategy | Risk | Mitigation |
|---|---|---|---|
| Short support chat |  |  |  |
| Long research assistant session |  |  |  |
| Regulated financial workflow |  |  |  |
| Multi-step tool task |  |  |  |

## Self-Check

| Question | My answer |
|---|---|
| Why is conversation history not automatically useful context? |  |
| How do token limits affect state management? |  |
| What should happen when user intent changes mid-conversation? |  |

## Mastery Evidence

You can decide what state belongs in storage, what belongs in the prompt, what
should be summarized, and what should be excluded for safety or relevance.

## Remediation

If your policy keeps all history by default, redo Artifact A with a strict token
budget and a sensitive-data example. Mark each state element as keep, summarize,
retrieve again, or drop.
