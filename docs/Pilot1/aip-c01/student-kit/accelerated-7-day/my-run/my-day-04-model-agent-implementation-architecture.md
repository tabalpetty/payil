# Day 4 Artifact: Model And Agent Implementation Architecture

## Purpose

Design the implementation-heavy core: deployment, model routing, enterprise
integration, and agent/tool behavior.

## Scenario

| Field | Response |
|---|---|
| Business goal |  |
| User groups |  |
| Data sources |  |
| Tools/actions required |  |
| Latency, cost, and quality priorities |  |
| Security and compliance constraints |  |
| Deployment constraints |  |

## Part A: Model Selection And Routing

| Candidate model or endpoint | Strength | Weakness | Use case fit |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

Routing policy:

| Condition | Route to | Reason |
|---|---|---|
| Simple low-risk request |  |  |
| Complex reasoning request |  |  |
| High-sensitivity request |  |  |
| High-volume request |  |  |
| Primary model unavailable |  |  |

## Part B: Deployment Choice

| Option | Use? | Rationale | Operational implication |
|---|---|---|---|
| Bedrock on-demand |  |  |  |
| Bedrock provisioned throughput |  |  |  |
| Cross-Region inference |  |  |  |
| SageMaker endpoint |  |  |  |
| Hybrid or on-premises integration |  |  |  |

## Part C: Enterprise Integration

| Concern | Design choice | Owner/evidence |
|---|---|---|
| Identity federation |  |  |
| RBAC or attribute-based access |  |  |
| Network boundary |  |  |
| GenAI gateway or proxy |  |  |
| CI/CD |  |  |
| IaC |  |  |
| Deployment gates |  |  |
| Rollback |  |  |

## Part D: Agent And Tool Design

| Tool/action | Input schema | Authorization boundary | Failure handling |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

Agent behavior:

| Design point | Decision |
|---|---|
| Planning style |  |
| Memory use |  |
| Tool-call limits |  |
| Stopping conditions |  |
| Human escalation trigger |  |
| Unsafe action prevention |  |
| Audit trail |  |

## Part E: Changed-Constraint Defense

How would your design change?

| New constraint | Change | Why |
|---|---|---|
| Cost must drop by 40%. |  |  |
| Latency must be cut in half. |  |  |
| Data cannot leave a specific jurisdiction. |  |  |
| Tool actions require human approval. |  |  |
| Model quality drops after deployment. |  |  |

## Exit Check

| Check | Evidence |
|---|---|
| I can defend deployment and agent choices under changed requirements. |  |
| I can identify tool-use failures and boundary violations. |  |
| I completed timed Day 4 practice. |  |
| I logged misses and remediation. |  |

