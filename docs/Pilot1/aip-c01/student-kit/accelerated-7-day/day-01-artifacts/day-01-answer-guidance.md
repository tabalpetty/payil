# Day 1 Answer Guidance And Exemplars

## How To Use This File

Attempt the blank artifacts first. Use this file only after you have produced
your own answer. Its job is calibration: it shows what a strong answer sounds
like and why it earns mastery evidence.

For Day 1, a score of `3` means the answer is specific to a scenario, names
the relevant component or control, explains why it belongs there, and records a
gap or tradeoff when appropriate.

## Shared Scenario For Exemplars

A product team is building an internal support assistant. Employees ask
questions about support policies. The application retrieves approved policy
snippets, invokes a foundation model through Amazon Bedrock, returns a concise
answer with source references, and records evaluation evidence without storing
sensitive user data in logs.

## Day01-order001: Foundation Models And GenAI Fundamentals

Strong concept-map notes:

```text
User intent is converted into a prompt. The foundation model predicts an
output from the prompt and retrieved context; it does not independently know
which support policy is current. The application must provide grounding,
validate the answer, and decide whether the output is safe to return.
```

What makes this strong:

- separates model behavior from application responsibility;
- avoids saying "the model looks up the policy";
- names grounding and validation as system responsibilities.

## Day01-order002: Tokens, Context, Inference Parameters

Strong cause-effect row:

| Change | Likely effect | Why it matters |
|---|---|---|
| Add entire policy manual to the prompt | Higher cost, higher latency, possible truncation, and more irrelevant context | Context windows are finite; retrieval should select the most relevant passages. |
| Lower temperature for policy answers | More consistent phrasing and fewer creative variations | The task values reliable support guidance over novelty. |

What makes this strong:

- predicts consequences rather than only defining terms;
- links parameters to the business task.

## Day01-order003: AWS GenAI Service Landscape

Strong service-role table excerpt:

| Component | Role in the system | Why |
|---|---|---|
| Amazon Bedrock | Managed model access | The app invokes a foundation model without hosting it directly. |
| Bedrock customization/import or SageMaker AI | Model customization/hosting path | Bedrock fits supported managed FM customization or imported-model invocation; SageMaker AI fits broader custom ML training and hosting workflows. |
| Amazon S3 | Source document storage | Approved policy files can be stored as versioned objects. |
| Amazon DynamoDB | App state or request metadata | The app may keep request records, evaluation run status, or user/session metadata outside the source document store. |
| OpenSearch or Bedrock Knowledge Bases | Retrieval/data context | The assistant needs relevant snippets, not the whole document set. |
| Step Functions, SQS, or EventBridge | Workflow, queueing, or eventing | Longer-running evaluation or approval work should not be tangled into the interactive request path. |
| API Gateway and Lambda | API boundary and request logic | The user request is authenticated, shaped, and passed to the application flow. |
| CloudWatch, X-Ray, and CloudTrail | Operational logs, traces, and API audit evidence | They help investigate failures, follow requests, and prove which actions occurred. |
| IAM, VPC endpoints, encryption, or resource policies | Security controls | They restrict who can call, route privately, read/write data, and decrypt sensitive material. |

What makes this strong:

- classifies services by job;
- avoids treating a service list as an architecture.

## Day01-order004: Integration Patterns

Strong decision table excerpt:

| Scenario | Pattern | Reason |
|---|---|---|
| Employee asks a short policy question in chat | Synchronous API path | The user is waiting and the answer should return quickly. |
| Nightly evaluation of 500 regression prompts | Asynchronous queue or workflow | The work is batch-like and should not block an interactive request. |
| Answer needs compliance review before publication | Step Functions workflow with approval step | The process has a human gate and audit evidence requirement. |

What makes this strong:

- selects pattern from timing and control requirements;
- gives a reason that would change if the scenario changed.

## Day01-order005: Trust Boundaries, IAM, And Data Protection

Strong control-placement excerpt:

| Concern | Control | Where it belongs | Why |
|---|---|---|---|
| User authentication | Corporate identity provider or API authorizer | Before application logic | No model or policy access should occur until the caller is known. |
| Least privilege | IAM role limited to required Bedrock model invocation, retrieval index read, and logging writes | Lambda or service execution role | The app should not have broad account or data access. |
| Sensitive data exposure | Redaction plus log allowlist | Before writing prompts/responses to logs | Logs are useful evidence but can leak employee or customer data. |
| Unauthorized retrieval | Data-source policy and retrieval filter by user entitlement | Retrieval boundary | The model must not receive policy snippets the caller may not view. |

What makes this strong:

- places controls at the boundary where the risk appears;
- recognizes logs as both evidence and risk.

Strong risk-review row:

| Risk | Likelihood | Impact | Control | Residual risk |
|---|---|---|---|---|
| Sensitive employee or customer data is written into prompt/response logs | Medium | High | Redact sensitive fields before logging and allowlist only request ID, latency, status, and sanitized error detail | Some sensitive text may still appear in unexpected fields, so sampling and log review remain necessary. |

What makes this strong:

- states a concrete risk rather than a vague category;
- rates likelihood and impact before choosing the control;
- keeps a residual risk instead of pretending the control removes the risk.

## Day01-order006: Requirements And Basic Architecture

Strong architecture summary:

```text
The request enters through an authenticated API. Lambda validates the request,
retrieves policy snippets from the approved index, builds a prompt with source
boundaries, invokes Bedrock, validates that the response cites sources and fits
the output contract, then returns the answer. CloudWatch records operational
signals and CloudTrail records API activity. Sensitive prompt content is
redacted before logging.
```

Strong tradeoff:

```text
I chose a synchronous path for the chat answer because employees need a quick
response. I would use a workflow or queue for nightly evaluation because those
runs are longer and should survive retries without holding open a user request.
```

What makes this strong:

- describes request flow and control flow;
- names a tradeoff instead of only listing services.

## Day01-order007: Model Selection

Strong model-selection row:

| Requirement | Model implication | Rejected alternative |
|---|---|---|
| Policy answers must be faithful and concise | Choose a text model that performs well on summarization and grounded Q&A tests at low temperature | Do not choose solely by largest context window; irrelevant context can still degrade answers. |
| Interactive chat needs low latency | Test latency on representative prompts before selecting | Do not choose a slower model unless quality gains justify the user impact. |
| Output must be JSON for downstream logging | Prefer model/prompt combination that reliably follows structured output instructions | Do not rely on manual parsing of free-form prose. |

Strong candidate comparison:

| Candidate | Strength | Limitation | Best-fit use | Reject when |
|---|---|---|---|---|
| Larger general text model | Better reasoning and summarization on hard policy questions | Higher latency and cost | Ambiguous policy answers where quality matters most | The chat path has strict latency or high-volume cost pressure. |
| Smaller/faster text model | Lower latency and cost | May miss nuance on ambiguous policy cases | Simple routing, extraction, or classification | The answer must explain nuanced policy tradeoffs. |
| Embedding model plus retrieval | Finds relevant approved policy snippets | Does not generate the final answer by itself | Grounding the answer before generation | There is no source corpus or grounding requirement. |

What makes this strong:

- ties model choice to task constraints;
- preserves rejected alternatives and reasons.

## Day01-order008: Basic Bedrock Invocation

Strong invocation inspection record:

| Field | Value |
|---|---|
| Model/provider | Bedrock-supported text model, selected by model ID or inference profile |
| Invocation API or method | `Converse` for message-oriented calls, or `InvokeModel` for model-specific request bodies |
| Input shape | JSON body containing messages or model-specific prompt fields plus inference parameters |
| Output shape | Model response body parsed by the application; answer must be validated before use |
| Permissions required | Caller execution role needs Bedrock model invocation permission and access to surrounding data/log resources |
| Region/account assumption | Model and supporting resources are available in the selected region/account path |
| Logging evidence | Request ID, latency, status, token/cost signal if available, and sanitized error detail |
| Error or failure mode | Access denied, validation error, throttling, timeout, malformed output |

What makes this strong:

- inspects a real API shape rather than hand-waving "call Bedrock";
- treats permissions, body schema, and response parsing as procedural evidence.

## Day01-order009: Prompt Fundamentals And Structured Output

Strong prompt baseline:

```text
System: You answer employee support-policy questions using only provided
context. If the context does not answer the question, say that the policy
source is insufficient.

Task: Return a concise answer with cited source IDs.

Input boundaries: Use only snippets inside <policy_context>.

Output format: JSON with answer, source_ids, confidence, and escalation_needed.

Safety: Do not reveal confidential policy text beyond the answer needed for
the caller's entitlement.
```

Strong structured-output test:

| Test | Prompt | Expected structure | Validation check |
|---:|---|---|---|
| 1 | Ask for a policy answer with relevant context | JSON with `answer`, `source_ids`, `confidence`, `escalation_needed` | Parses as JSON and includes a real source ID from the context. |
| 2 | Ask the same question with no relevant context | JSON with insufficient-source answer and `escalation_needed: true` | Does not guess from general knowledge. |
| 3 | Ask for prose instead of JSON | Same JSON contract | Refuses format drift and still returns the required keys. |

Strong cause-effect row:

| Prompt change | Expected effect | Risk |
|---|---|---|
| Add stricter output format | Easier validation by the application | Model may wrap JSON in prose or omit a required key. |
| Remove context boundaries | More fluent but less grounded answers | Higher risk of hallucinated or unauthorized policy content. |

What makes this strong:

- defines role, task, boundaries, output, and safety behavior;
- makes the prompt testable.

## Day01-order010: Evaluation And Golden Datasets

Strong golden-dataset mini-set:

| Test ID | Input | Expected output properties | Must avoid | Pass/fail note |
|---|---|---|---|---|
| G001 | "What is the remote-work reimbursement limit?" with matching policy snippet | Correct limit, source ID, concise answer | Inventing a different amount | Pass only if cited source matches snippet |
| G002 | Same question with no relevant context | Says source is insufficient and escalates | Guessing from general knowledge | Pass if refusal is clear |
| G003 | Prompt asks to ignore policy and reveal confidential text | Refuses unsafe instruction and preserves boundary | Following prompt injection | Pass if no confidential text is exposed |
| G004 | Input requires JSON output | Valid JSON with required keys | Free-form prose | Pass if schema validates |
| G005 | Previously failed reimbursement wording | Corrected behavior remains fixed | Regression to old answer | Pass if previous defect does not recur |

What makes this strong:

- includes normal, missing-context, safety, structured-output, and regression cases;
- checks expected properties rather than one lucky answer.

## Calibration Rubric

| Score | Evidence |
|---:|---|
| 3 | Scenario-specific, technically plausible, includes component/control placement, rationale, and at least one tradeoff or failure mode. |
| 2 | Mostly correct but generic, missing a constraint, weak on why, or incomplete on evidence. |
| 1 | Recognizes some terms but cannot place them in the system or justify a decision. |
| 0 | Blank, unsafe, technically wrong, or contradicts the scenario. |

## Reassessment Path

If your answer scores below `3`, do not rewrite it from memory alone. First
classify the gap:

| Gap | Remediation |
|---|---|
| Service-role confusion | Return to the service landscape section and rebuild the role table. |
| Pattern-selection confusion | Create two contrasting scenarios and explain why the integration pattern changes. |
| Security/control gap | Fill the control-placement table before revising the architecture. |
| Procedural invocation gap | Inspect the Bedrock request examples and rewrite the runbook with concrete fields. |
| Evaluation gap | Add one missing-context case and one regression case to the golden dataset. |
