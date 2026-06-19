# Day 1 Study Guide: Foundations, System Map, Invocation, And Prompt Baseline

## What You Are Learning Today

Day 1 gives you the vocabulary and system map for the rest of the week. The
goal is not to memorize every AWS service. The goal is to see where each part
of a GenAI application belongs and how a request moves from user intent to
model output, controls, logging, and evaluation.

By the end of today, you should be able to explain the difference among:

- the application;
- the prompt;
- the foundation model;
- retrieval/data context;
- orchestration;
- safety and security controls;
- monitoring and evaluation.

## The Core Mental Model

A GenAI application is not just a model call.

Think of it as a chain:

```text
User request
  -> application/API layer
  -> identity and authorization checks
  -> prompt construction
  -> optional retrieval or tool selection
  -> model invocation
  -> output validation and safety checks
  -> response to user
  -> logs, metrics, traces, evaluation, audit evidence
```

The model is important, but the professional work is in the system around it:
data, controls, routing, failure handling, observability, and governance.

## Foundation Model Concepts

| Concept | Plain meaning | Why it matters |
|---|---|---|
| Foundation model | A large pretrained model used as a base for language, image, or other generative tasks. | Model choice affects quality, latency, cost, safety, and supported modalities. |
| Inference | Running the model to produce an output from an input. | Most application integration work is inference integration. |
| Token | A unit of text processed by the model. | Token count drives context limits, cost, latency, and truncation risk. |
| Context window | The maximum input/output context the model can consider. | Too much context can truncate inputs or degrade answer quality. |
| Temperature | A control that influences randomness. | Lower values usually support consistency; higher values support variety. |
| Top-p / top-k | Controls that limit candidate token choices. | They shape output diversity and determinism. |
| Prompt template | A reusable prompt structure. | Templates support consistency, versioning, testing, and governance. |
| Structured output | Output constrained into a format such as JSON. | Needed when downstream systems parse the response. |

## AWS System Roles To Recognize

In AIP-C01 scenarios, classify services and capabilities by the job they do.

| Role | What it does | Examples of services/capabilities to recognize |
|---|---|---|
| Model access | Provides access to foundation models. | Amazon Bedrock, SageMaker AI endpoints. |
| Retrieval/data | Stores and retrieves context for RAG. | Amazon S3, Amazon OpenSearch Service, vector stores, Bedrock Knowledge Bases. |
| Application compute | Runs application logic. | AWS Lambda, containers, application services. |
| Orchestration | Coordinates multi-step workflows. | AWS Step Functions, agent workflows. |
| API boundary | Exposes the app to users or systems. | Amazon API Gateway, application APIs. |
| Security | Controls identity, permissions, secrets, network access. | IAM, VPC endpoints, encryption, access policies. |
| Observability | Captures metrics, logs, traces, and alarms. | Amazon CloudWatch, AWS X-Ray, CloudTrail. |
| Governance | Captures ownership, approval, evidence, policy mapping. | Audit logs, model cards, approval workflows, review records. |

Do not memorize this as a flat list. Ask: what job does this component do in
the GenAI system?

## Minimal Invocation Flow

At the simplest level, model invocation requires:

1. a caller with permission;
2. a selected model or endpoint;
3. input in the shape expected by that model/API;
4. inference parameters;
5. response handling;
6. logging and error handling.

Professional scenarios add:

- retries and timeouts;
- throttling behavior;
- validation of output format;
- safety filtering;
- request and response logging that avoids exposing sensitive data;
- cost and token tracking;
- fallback or graceful degradation.

## Prompt Baseline

Good prompts are not magic sentences. They are controllable application assets.

A useful prompt baseline has:

- a role or system instruction;
- a task;
- input data boundaries;
- output format;
- examples when useful;
- safety or refusal conditions;
- evaluation expectations.

For production-style systems, prompts should be versioned, tested, reviewed,
and rolled back like other behavior-changing assets.

## Common Misconceptions

| Misconception | Better view |
|---|---|
| The model is the application. | The model is one component inside an application system. |
| Bigger context always solves the problem. | Better retrieval, summarization, chunking, or prompt design may be better. |
| Prompt engineering is only wording. | It includes structure, versioning, testing, output contracts, and governance. |
| If the answer is good once, the prompt is good. | Prompts need regression examples across expected and risky cases. |
| Security starts after the model responds. | Security starts at identity, data access, prompt construction, tool access, and logging. |

## Teach-Back

Close this guide and explain:

1. What happens between a user request and a model response?
2. Where do identity, retrieval, safety, and logging fit?
3. Why is a prompt template an application asset?
4. What can go wrong if token usage is ignored?

Then open the Day 1 artifact and fill it.

