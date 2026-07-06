# Day03-order010: Prompt Regression Testing And Quality Assurance

## Traceability

| Field | Value |
|---|---|
| Curriculum order | Day03-order010 |
| Section | Layer 2 - Prompt systems and application interaction |
| Topic | Prompt regression testing and quality assurance |
| Knowledge category | Skill; Knowledge |
| Knowledge type | Procedural; Causal; Strategic |
| Artifact family | Architecture decision record; lab runbook; cause-effect worksheet |

## Purpose

Build a prompt test process that catches broken instructions, output formats,
safety behavior, and quality regressions before release.

## Artifact A: Regression Set Design

| Test case type | Example input | Expected behavior | Pass/fail signal |
|---|---|---|---|
| Happy path |  |  |  |
| Ambiguous request |  |  |  |
| Missing context |  |  |  |
| Unsafe request |  |  |  |
| Required output format |  |  |  |
| Edge case from production |  |  |  |

## Artifact B: QA Runbook

| Step | Action | Evidence |
|---:|---|---|
| 1 | Select prompt version and candidate change. |  |
| 2 | Run baseline tests. |  |
| 3 | Run candidate tests. |  |
| 4 | Compare quality, format, safety, and latency. |  |
| 5 | Approve, reject, or revise. |  |
| 6 | Record rollout and rollback plan. |  |

## Artifact C: Strategic Release Decision

```text
Ship the prompt change if...

Block the change if...

Allow limited rollout if...

Rollback trigger:
```

## Self-Check

| Question | My answer |
|---|---|
| Why should regression tests include known failure cases? |  |
| What is the difference between prompt QA and model evaluation? |  |
| What production signal would trigger rollback? |  |

## Mastery Evidence

You can design a prompt regression set with happy paths, edge cases, safety
cases, output-format checks, and a release decision rule.

## Remediation

If your tests only check normal successful requests, add at least one ambiguous
case, one unsafe case, one missing-context case, and one strict output-format
case. Define the rollback trigger before approving release.
