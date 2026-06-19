# Day 4 Study Guide: Deployment, Model Routing, Enterprise Integration, And Agents

## What You Are Learning Today

Day 4 is implementation-heavy. You will decide how models are selected,
deployed, routed, integrated into enterprise systems, and connected to tools or
agent workflows.

The exam pattern is rarely "which service exists?" It is more often "which
implementation choice fits these constraints?"

## Model Selection And Routing

Model choice is a tradeoff among:

- quality;
- latency;
- cost;
- modality;
- context window;
- safety behavior;
- regional availability;
- throughput needs;
- customization needs;
- operational control.

Model routing means different requests may go to different models or endpoints.

Examples:

- simple classification goes to a cheaper/faster model;
- high-value reasoning goes to a stronger model;
- sensitive requests go through stricter controls;
- overflow traffic uses a fallback route;
- unavailable models trigger alternate routing.

## Deployment Choices

Recognize the shape of deployment choices:

| Choice | Good fit | Watch for |
|---|---|---|
| Bedrock on-demand | Managed model access and variable usage. | Quotas, latency, model availability, cost. |
| Provisioned throughput | Predictable high-volume or latency-sensitive workloads. | Commitment, capacity planning, utilization. |
| Cross-Region inference | Resilience or capacity across Regions. | Data residency, latency, compliance. |
| SageMaker endpoint | Custom model hosting or more control. | Operational ownership and deployment complexity. |
| Hybrid integration | Existing enterprise or edge constraints. | Network, identity, governance, and synchronization complexity. |

## Enterprise Integration

A professional GenAI system must fit the enterprise boundary.

Design for:

- identity federation;
- role-based or attribute-based access;
- network boundaries;
- secrets and credential handling;
- deployment pipelines;
- infrastructure as code;
- approval gates;
- rollback;
- audit evidence.

If the system can take action, the integration boundary matters even more.

## Agents And Tool Use

Agents combine model reasoning with tools, memory, planning, and sometimes
human escalation.

Key design questions:

- What tools can the agent call?
- What inputs are allowed?
- What permissions does each tool call require?
- What stops the agent from looping?
- When must a human approve?
- What is logged for audit?
- What happens when a tool fails?

Tool schemas should be explicit. Authorization should be narrow. Dangerous
actions should require stronger controls.

## Common Failure Modes

| Failure | Prevention |
|---|---|
| Agent calls wrong tool. | Clear tool descriptions, validation, and routing constraints. |
| Agent loops. | Tool-call limits, stopping conditions, state checks. |
| Agent exceeds authority. | Least privilege and action-specific authorization. |
| Model route is too expensive. | Cost-aware routing and monitoring. |
| Deployment cannot roll back. | Versioned deployment and rollback plan. |

## Teach-Back

Close the guide and explain:

1. How model routing balances cost, latency, quality, and risk.
2. When provisioned throughput might be justified.
3. What makes an agent tool boundary safe.
4. What changes if human approval is required.

Then fill the Day 4 implementation architecture.

