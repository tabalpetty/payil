# Day03-order017: Fallbacks, Circuit Breakers, And Graceful Degradation

## Traceability

| Field | Value |
|---|---|
| Curriculum order | Day03-order017 |
| Section | Layer 2 - Prompt systems and application interaction |
| Topic | Fallbacks, circuit breakers, and graceful degradation |
| Knowledge category | Knowledge; Skill |
| Knowledge type | Conceptual; Procedural; Causal; Strategic |
| Artifact family | Architecture decision record; lab runbook; cause-effect worksheet |

## Purpose

Design what the application does when the preferred model, region, retrieval
service, or prompt workflow cannot safely complete.

## Artifact A: Degradation Strategy

| Failure mode | Primary path | Fallback or degraded path | User experience |
|---|---|---|---|
| Model unavailable |  |  |  |
| Region unavailable |  |  |  |
| Retrieval unavailable |  |  |  |
| Safety block |  |  |  |
| High latency |  |  |  |
| Cost threshold exceeded |  |  |  |

## Artifact B: Circuit Breaker Rule

```text
Open circuit when...

While open, route traffic to...

Half-open test is...

Close circuit when...
```

## Artifact C: Strategic Tradeoff

| Option | Benefit | Risk | Choose when |
|---|---|---|---|
| Return cached answer |  |  |  |
| Use smaller/faster model |  |  |  |
| Queue for later processing |  |  |  |
| Return partial response |  |  |  |
| Fail closed |  |  |  |

## Self-Check

| Question | My answer |
|---|---|
| What is graceful degradation in a GenAI app? |  |
| When is fallback dangerous? |  |
| What evidence shows a circuit breaker is working? |  |

## Mastery Evidence

You can define fallback and degradation behavior for major failure modes,
explain when fallback is unsafe, and specify circuit-breaker open, half-open,
and close conditions.

## Remediation

If your fallback always returns a lower-quality answer, add fail-closed cases
where safety, permission, or grounding risk makes fallback unacceptable. Then
define what the user sees in each degraded state.
