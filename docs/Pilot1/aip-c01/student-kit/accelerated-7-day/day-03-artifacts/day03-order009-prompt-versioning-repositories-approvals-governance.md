# Day03-order009: Prompt Versioning, Repositories, Approvals, And Governance

## Traceability

| Field | Value |
|---|---|
| Curriculum order | Day03-order009 |
| Section | Layer 2 - Prompt systems and application interaction |
| Topic | Prompt versioning, repositories, approvals, and governance |
| Knowledge category | Skill; Knowledge; Representation / Location |
| Knowledge type | Procedural; Normative; Institutional; Embedded |
| Artifact family | Lab runbook; configuration record; RACI and policy-to-control evidence map |

## Purpose

Treat prompts as governed application assets whose changes can affect quality,
safety, cost, compliance, and user trust.

## Artifact A: Prompt Repository Record

| Field | Value |
|---|---|
| Prompt name |  |
| Owner |  |
| Current version |  |
| Approved use case |  |
| Test set link or ID |  |
| Rollback version |  |
| Approval requirement |  |
| Monitoring owner |  |

## Artifact B: RACI

| Activity | Responsible | Accountable | Consulted | Informed |
|---|---|---|---|---|
| Draft prompt |  |  |  |  |
| Review safety risk |  |  |  |  |
| Approve release |  |  |  |  |
| Monitor production |  |  |  |  |
| Roll back prompt |  |  |  |  |

## Artifact C: Governance Control Map

| Risk | Control | Evidence |
|---|---|---|
| Unreviewed behavior change |  |  |
| Output format regression |  |  |
| Unsafe instruction introduced |  |  |
| No rollback path |  |  |
| Owner unknown |  |  |

## Artifact D: Embedded Inspection Record

Inspect a real or simulated prompt-management record. The goal is to prove that
the prompt is a governed asset, not an informal text snippet.

| Config surface | Observable fact to record | My notes |
|---|---|---|
| Prompt identifier | name, version, environment, approved use case |  |
| Template variables | required variables, defaults, validation rules |  |
| Model binding | selected model, inference parameters, fallback model |  |
| Approval state | draft, approved, rejected, retired |  |
| Test evidence | regression set, latest result, reviewer |  |
| Rollout control | deployment target, staged rollout, rollback version |  |
| Audit trail | who changed what, when, and why |  |

## Self-Check

| Question | My answer |
|---|---|
| Why is a prompt repository more than a folder of text files? |  |
| Which prompt changes need approval? |  |
| What evidence would satisfy an audit of prompt change control? |  |

## Mastery Evidence

You can define prompt ownership, versioning, approval, rollback, monitoring,
and audit evidence for a prompt that affects application behavior.

## Remediation

If your repository record has no owner, approval rule, test set, or rollback
version, fill those fields before review. Then map one prompt-change risk to a
specific governance control.
