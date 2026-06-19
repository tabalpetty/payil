# Day 5 Study Guide: Safety, Security, Privacy, Governance, And Responsible AI

## What You Are Learning Today

Day 5 turns safety and governance into operational design. The goal is not to
say "use guardrails" and move on. The goal is to know where controls belong,
who owns them, what evidence proves they work, and what residual risk remains.

## Control Layers

Think in layers:

```text
User and identity
  -> application validation
  -> data access and retrieval controls
  -> prompt and context controls
  -> model safety controls
  -> output validation
  -> logging, monitoring, audit
  -> human review and governance
```

No single layer is enough.

## Threats And Controls

| Threat | What it means | Control ideas |
|---|---|---|
| Prompt injection | User input tries to override instructions or extract hidden context. | Input filtering, instruction hierarchy, retrieval isolation, output checks. |
| Jailbreak | User tries to bypass safety behavior. | Safety policies, moderation, refusal rules, adversarial tests. |
| Data exposure | Sensitive data appears in output or logs. | Access control, masking, redaction, logging controls. |
| Unauthorized retrieval | User retrieves documents they should not access. | Permission-aware retrieval and metadata filtering. |
| Hallucination | Model produces unsupported or false content. | Grounding, citations, factual checks, evaluation datasets. |
| Unsafe tool use | Agent performs risky or unauthorized action. | Tool authorization, validation, human approval, audit trail. |

## Security Design

Security decisions include:

- who can call the application;
- what data they can retrieve;
- what tools they can invoke;
- how credentials are stored;
- whether traffic uses private network paths;
- what is encrypted;
- what is logged;
- how sensitive content is redacted or masked.

Do not forget logging privacy. Logs are evidence, but they can also leak data.

## Governance Design

Governance makes accountability visible.

For each major control, define:

- owner;
- approving role;
- evidence retained;
- review cadence;
- escalation path;
- residual risk;
- risk acceptance authority.

If you cannot name the owner or evidence, the control is not operational yet.

## Responsible AI

Responsible AI concerns include:

- fairness;
- transparency;
- explainability;
- human oversight;
- traceability;
- misuse prevention;
- monitoring after deployment.

For exam scenarios, connect the responsible AI value to a concrete mechanism.
For example, transparency may require citations, user notices, model cards, or
reviewable decision records depending on the case.

## Teach-Back

Close the guide and explain:

1. Why guardrails are not the entire safety architecture.
2. How prompt injection can be blocked, detected, logged, and remediated.
3. What evidence an auditor would ask for.
4. Who owns residual risk.

Then fill the Day 5 control pack.

