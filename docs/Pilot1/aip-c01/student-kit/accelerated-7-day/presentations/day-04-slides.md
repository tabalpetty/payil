# Day 4 Slides: Deployment, Routing, Enterprise Integration, Agents

## Slide 1: Today's Job

- Decide how models are selected, deployed, routed, and connected to tools.

## Slide 2: Model Tradeoffs

- Quality
- Latency
- Cost
- Context window
- Modality
- Safety
- Region
- Throughput
- Customization

## Slide 3: Routing Policy

```text
request type + risk + cost + latency + quality need -> model/endpoint
```

## Slide 4: Deployment Choices

- Bedrock on-demand
- Provisioned throughput
- Cross-Region inference
- SageMaker endpoint
- Hybrid integration

## Slide 5: Enterprise Integration

- Identity federation
- Access control
- Network boundary
- CI/CD
- IaC
- Approval gates
- Rollback
- Audit evidence

## Slide 6: Agent Boundaries

- Tool schema
- Authorization
- Validation
- Tool-call limit
- Stopping condition
- Human escalation
- Audit trail

## Slide 7: Artifact Prompt

Fill the model-and-agent implementation architecture with routing, deployment,
enterprise integration, and tool boundaries.

