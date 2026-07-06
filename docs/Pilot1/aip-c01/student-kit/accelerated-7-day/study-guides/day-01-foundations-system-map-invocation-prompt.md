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

Acceleration note: Day 1 is not a service-name skim. It is the foundation for
the whole system. If you cannot reconstruct the system path, classify service
roles, and explain where controls and evaluation belong, spend the extra time
now. A weak Day 1 makes Days 2-7 feel artificially harder.

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
| Generative AI | AI that creates new content such as text, images, code, audio, or structured data from inputs and learned patterns. | GenAI systems must control both what is generated and how the output is used. |
| Foundation model | A large pretrained model used as a base for language, image, or other generative tasks. | Model choice affects quality, latency, cost, safety, and supported modalities. |
| Inference | Running the model to produce an output from an input. | Most application integration work is inference integration. |
| Token | A unit of text processed by the model. | Token count drives context limits, cost, latency, and truncation risk. |
| Context window | The maximum input/output context the model can consider. | Too much context can truncate inputs or degrade answer quality. |
| Modality | The kind of input or output a model handles, such as text, image, audio, video, or embeddings. | A model that fits a text task may not fit a multimodal or embedding task. |
| Temperature | A control that influences randomness. | Lower values usually support consistency; higher values support variety. |
| Top-p | Nucleus sampling: limits choices to the smallest set of likely next tokens whose cumulative probability reaches the threshold. | Lower values usually narrow the output; higher values allow more variety. |
| Top-k | Limits choices to the `k` most likely next tokens. | Smaller `k` narrows choices; larger `k` allows more alternatives. |
| Max output length | The maximum number of output tokens the model may generate. | If too low, the response may stop early, omit required fields, or truncate before completion. |
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

## Service Landscape: What Each Component Is For

Day 1 does not require expert depth in every service. It does require a
reliable first classification: when a scenario names a service, decide whether
it is providing model access, application logic, orchestration, storage,
retrieval, security, observability, or governance evidence.

Use this first-pass map:

| Scenario need | First service family to consider | Reason |
|---|---|---|
| Call a managed foundation model | Amazon Bedrock | Bedrock provides managed access to foundation models and model-inference APIs. |
| Customize a Bedrock-supported foundation model or invoke an imported custom model through Bedrock | Amazon Bedrock | Bedrock supports managed FM customization paths and custom model import for supported model architectures. |
| Build, train, host, or operate ML models with deeper workflow and infrastructure control | SageMaker AI | SageMaker AI is the managed ML platform path when the scenario needs broader training, deployment, or custom ML operations beyond Bedrock-managed inference. |
| Run lightweight request logic | AWS Lambda | Lambda fits event-driven glue code, validation, prompt assembly, and simple API handlers. |
| Expose an authenticated API boundary | Amazon API Gateway plus IAM or authorizer controls | The API boundary should authenticate callers before application logic invokes model or data resources. |
| Coordinate multi-step work | AWS Step Functions | A workflow is clearer than tangled application code when steps include retries, approvals, branches, or long-running tasks. |
| Decouple producers and consumers | Amazon SQS or Amazon EventBridge | Queues and events protect the system from spikes and let downstream work happen asynchronously. |
| Store source documents or outputs | Amazon S3 | Object storage is a common source, sink, and evidence location, but access and encryption still matter. |
| Store app state or request metadata | Amazon DynamoDB | Low-latency key-value or document-style state is often separate from unstructured source documents. |
| Retrieve relevant text for RAG | OpenSearch, vector stores, or Bedrock Knowledge Bases | Retrieval components bring selected context to the prompt rather than relying only on model memory. |
| Observe behavior and incidents | CloudWatch, X-Ray, CloudTrail | Logs, metrics, traces, and API audit history answer different operational questions. |
| Restrict what can happen | IAM, encryption, VPC endpoints, resource policies | Security controls belong before, during, and after the model call. |

The exam trap is service-role confusion. A storage service is not a retrieval
strategy by itself. A model-access service is not an application architecture.
An observability service records evidence; it does not replace authentication
or least privilege.

For the Day01-order003 embedded inspection artifact, you do not need expert
depth in every service. You do need one observable fact per role family. Use
the table above to record what each service is for:

| Role family | Example inspection target | What to notice |
|---|---|---|
| Model access | Bedrock runtime API or model catalog | Model invocation needs a model ID, region/account availability, permissions, request shape, and response handling. |
| Model hosting/customization | Bedrock customization/import docs or SageMaker AI overview | Bedrock covers managed FM customization/import paths; SageMaker AI covers broader ML build/train/deploy workflows. |
| Application compute | Lambda docs, handler example, or console view | Application logic validates requests, builds prompts, invokes services, and handles errors. |
| API boundary | API Gateway route/auth example | The API boundary authenticates and shapes user/system requests before application logic runs. |
| Orchestration/workflow | Step Functions state machine example | Workflows make branches, retries, approvals, and audit checkpoints explicit. |
| Eventing/queueing | SQS queue or EventBridge rule example | Queues/events decouple producers from downstream model or workflow processing. |
| Storage | S3 bucket/object example | Source documents, outputs, and evidence need access control, encryption, and lifecycle choices. |
| App state | DynamoDB table example | Request metadata or app state is usually stored separately from source documents. |
| Retrieval/vector search | OpenSearch or Bedrock Knowledge Bases docs | Retrieval selects relevant context instead of sending every document to the model. |
| Observability | CloudWatch, X-Ray, or CloudTrail docs | Logs, traces, metrics, and API history answer different operational questions. |
| Security | IAM policy, VPC endpoint, encryption, or resource policy docs | Security controls define who can call, read, write, route privately, and decrypt. |

## Integration Patterns

Choose the integration pattern from the timing, reliability, and human-control
requirements.

| Pattern | Use when | Avoid when |
|---|---|---|
| Synchronous API call | The user is waiting, the request is small enough, and a fast answer is expected. | The job can exceed request timeouts, needs human approval, or should survive spikes. |
| Event-driven flow | The request can be accepted now and processed later. | The caller needs an immediate final answer. |
| Queue-backed worker | Demand is bursty or downstream model/API capacity must be protected. | Every request must be completed inline. |
| Workflow orchestration | The process has multiple steps, branches, retries, approvals, or audit checkpoints. | A single function can do the work clearly and safely. |
| Streaming response | The user benefits from seeing partial output as it is generated, such as a chat answer appearing token by token. | The workflow needs a single final validated answer before showing anything to the user. |
| Container service | The application needs longer-running services, dependencies, or runtime control. | The logic is simple event glue that fits serverless constraints. |

For GenAI systems, the model call is usually only one step. The surrounding
pattern decides where authentication, prompt assembly, retrieval, validation,
human review, retries, and logging belong.

## Trust Boundaries And Control Placement

A trust boundary is a point where the system should stop assuming that the
previous actor or component can be trusted without checks. In a GenAI
application, trust boundaries usually appear at:

- user to API;
- API to application logic;
- application logic to data source;
- application logic to model;
- model output to downstream system or user;
- application to logging, evaluation, and audit stores.

Controls should be placed where they prevent or detect the failure they are
meant to handle.

| Concern | Control placement rule |
|---|---|
| Authentication | Check at the API or application boundary before model or data access. |
| Authorization | Scope IAM roles and resource policies to the caller, function, data source, and model action required. |
| Data exposure | Minimize prompt context, encrypt stored data, avoid logging sensitive prompts or responses, and redact when needed. |
| Network path | Use private connectivity or VPC controls when the scenario requires restricted network exposure. |
| Model output risk | Validate, filter, or route to human review before output reaches users or business systems. |
| Auditability | Preserve CloudTrail, application logs, evaluation records, and approval evidence without exposing sensitive content. |

Least privilege means more than "use IAM." It means the caller can perform
only the required actions, on the required resources, in the required context.
For Bedrock invocation, that includes permission for model invocation actions
and any data, prompt, logging, or retrieval resources used around the call.

## Requirements And Basic Architecture

Start architecture work by extracting constraints before choosing services.

| Requirement signal | Architecture implication |
|---|---|
| User waits for a response | Prefer synchronous request path if latency and timeout constraints fit. |
| Large batch or long-running work | Prefer asynchronous queue or workflow pattern. |
| Sensitive internal data | Add explicit data boundary, least privilege, encryption, and logging privacy. |
| Must cite or ground answers | Add retrieval and source-trace behavior before the model call. |
| Must approve before publish | Add workflow and human review before final delivery. |
| Must produce machine-readable output | Add structured output contract and validation. |
| Must improve over time | Add evaluation dataset, regression checks, and error analysis. |

A strong Day 1 architecture answer names the path of the request, the main AWS
roles, the controls, the evidence captured, and one tradeoff. A weak answer
only lists services.

## Model Selection Basics

Model selection is a tradeoff, not a contest for the biggest model.

| Selection factor | What to ask |
|---|---|
| Task fit | Is the task generation, summarization, classification, extraction, embedding, image, or multimodal? |
| Quality | Does the model produce acceptable answers on representative examples? |
| Latency | Can it meet the user or workflow timing requirement? |
| Cost | Is the quality improvement worth the token and throughput cost? |
| Context | Can the useful input fit without flooding the model? |
| Safety | Does the model behavior require extra filtering, review, or refusal handling? |
| Integration | Does the API, message format, region, and operational model fit the application? |

The first model-selection artifact should include the rejected alternatives.
That is how you prove conditional and strategic knowledge: "I chose this
because the scenario values X, and I rejected that because it fails Y."

On Day 1, you may compare generic model candidates rather than naming a
specific live Bedrock model. Later days add more service-specific benchmarking.
For now, make the tradeoff visible:

| Candidate | Strength | Limitation | Best fit | Reject when |
|---|---|---|---|---|
| Larger general text model | Strong reasoning and summarization quality | Higher latency and cost | Complex policy answers where quality matters most | The workflow has strict latency or cost limits. |
| Smaller/faster text model | Lower latency and cost | May miss nuance on complex answers | High-volume simple classification or routing | The answer must handle ambiguous policy reasoning. |
| Embedding model plus retrieval | Finds relevant source context | Does not generate the final answer by itself | Grounding answers in approved documents | The task is pure generation with no source corpus. |
| Multimodal model | Handles image or mixed text/image inputs | Unnecessary for text-only workflows | Inputs include screenshots, diagrams, or images | The application only processes text. |

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

Amazon Bedrock exposes model invocation through runtime APIs. `InvokeModel`
runs inference for a specified model using the prompt and inference parameters
in a JSON request body. `Converse` provides a consistent message-oriented
interface for supported models. In both cases, the caller still needs
permissions, a valid model identifier, the expected request shape, response
handling, and error handling.

Minimal Bedrock Converse-style request shape:

```json
{
  "modelId": "us.anthropic.claude-3-5-sonnet-20240620-v1:0",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "text": "Summarize the ticket in three bullet points."
        }
      ]
    }
  ],
  "inferenceConfig": {
    "maxTokens": 300,
    "temperature": 0.2,
    "topP": 0.9
  }
}
```

Minimal InvokeModel-style body for a model with an Anthropic messages shape:

```json
{
  "anthropic_version": "bedrock-2023-05-31",
  "max_tokens": 300,
  "temperature": 0.2,
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Return JSON with keys: summary, risk, next_action."
        }
      ]
    }
  ]
}
```

The exact request body is model-specific. The stable procedural habit is to
verify the model ID, content type, request body schema, parameters, and response
shape before treating a call as production-ready.

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

Prompt changes have effects you can predict and test. Compare the weak and
strong versions below.

Weak prompt:

```text
Answer the employee's policy question.
```

Why it is weak:

- no source boundary;
- no output contract;
- no instruction for missing context;
- no safety or escalation behavior;
- hard to regression-test.

Stronger prompt baseline:

```text
System: You answer employee support-policy questions using only the provided
policy snippets.

Task: Answer the question in one paragraph and cite source_ids.

Input boundary: Use only text inside <policy_context>. If the context is
missing or insufficient, say "insufficient policy source" and set
escalation_needed to true.

Output format: Return JSON with keys answer, source_ids, confidence, and
escalation_needed.

Safety: Do not reveal confidential text outside the caller's entitlement.
```

Structured-output validation checks whether the response can be parsed and
whether required keys exist. A response can be fluent and still fail if it is
not valid JSON, omits `source_ids`, invents a source, or ignores the
insufficient-context rule.

Use this cause-effect rule of thumb:

| Prompt change | Expected effect | Risk to test |
|---|---|---|
| Add a strict JSON output contract | Easier parsing and downstream validation | Model may return prose around the JSON or omit required keys. |
| Add examples | More consistent format and tone | Bad examples can anchor wrong behavior. |
| Remove source/context boundaries | More fluent answers from general knowledge | Higher hallucination or policy-leak risk. |
| Add refusal or escalation condition | Safer behavior when context is missing or unsafe | Over-refusal if the rule is too broad. |

## Evaluation And Golden Datasets

Evaluation is how you prevent "it worked once" from becoming a false
readiness signal. A golden dataset is a small, reviewed set of inputs with
expected properties that represent important normal cases, edge cases, risky
cases, and regression cases.

For Day 1, expected properties are usually better than one exact expected
answer. A summarization output might need to be faithful, under a length limit,
free of unsupported facts, and in valid JSON. A classifier might need an exact
label plus a confidence threshold. A customer-facing answer might need source
grounding and a refusal when the input asks for restricted content.

| Dataset item type | Example purpose |
|---|---|
| Happy path | Confirms the prompt handles the normal request. |
| Boundary case | Checks context size, ambiguity, missing fields, or unusual wording. |
| Safety/security case | Checks refusal, redaction, or escalation behavior. |
| Structured-output case | Checks valid JSON or schema compliance. |
| Regression case | Preserves behavior that was fixed after a previous failure. |

Evaluation supports governance because it creates evidence: what was tested,
what passed, what failed, what changed, and whether the change improved or
damaged behavior.

## Common Misconceptions

| Misconception | Better view |
|---|---|
| The model is the application. | The model is one component inside an application system. |
| Bigger context always solves the problem. | Better retrieval, summarization, chunking, or prompt design may be better. |
| Prompt engineering is only wording. | It includes structure, versioning, testing, output contracts, and governance. |
| If the answer is good once, the prompt is good. | Prompts need regression examples across expected and risky cases. |
| Security starts after the model responds. | Security starts at identity, data access, prompt construction, tool access, and logging. |
| A service list is an architecture. | Architecture explains request flow, boundaries, controls, and tradeoffs. |
| The largest model is automatically the best choice. | Model fit depends on quality, latency, cost, context, modality, safety, and operations. |
| Evaluation is only an exam-prep activity. | Evaluation is part of production prompt and model governance. |

## Source Notes

Current official AWS documentation checked for this guide:

- Amazon Bedrock `InvokeModel` API Reference:
  <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModel.html>
- Amazon Bedrock `Converse` API Reference:
  <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html>
- Amazon Bedrock Guardrails User Guide:
  <https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html>
- Amazon Bedrock model customization:
  <https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html>
- Amazon Bedrock custom model import:
  <https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html>
- Amazon SageMaker AI overview:
  <https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html>

## Teach-Back

Close this guide and explain:

1. What happens between a user request and a model response?
2. Where do identity, retrieval, safety, and logging fit?
3. Why is a prompt template an application asset?
4. What can go wrong if token usage is ignored?

Then open the Day 1 artifact and fill it.
