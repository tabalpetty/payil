# Day 1 Reviewed Question Bank

## Review Status

This file is a normalized reviewed bank generated from preserved raw Day 1
question-candidate responses. It approves only candidates that pass
schema, scenario, traceability, and quality checks. It remains partial
until each Day 1 curriculum-order topic has at least 10 approved items.

Review date: 2026-06-20

## Source Raw Files

- `docs/Pilot1/aip-c01/exam-prep/raw/day-01/2026-06-19T230500Z-openai-gpt-4.1-day01-foundations.md`
- `docs/Pilot1/aip-c01/exam-prep/raw/day-01/2026-06-19T230854Z-openai-gpt-4.1-day01-system-map.md`
- `docs/Pilot1/aip-c01/exam-prep/raw/day-01/2026-06-19T231108Z-openai-gpt-4.1-day01-applied-foundations.md`
- `docs/Pilot1/aip-c01/exam-prep/raw/day-01/2026-06-21T020500Z-manual-codex-authored-day01-quality-top-up.md`

## Raw Source Provenance

| Raw file | Provider | Model | Run ID |
|---|---|---|---|
| `2026-06-19T230500Z-openai-gpt-4.1-day01-foundations.md` | openai | gpt-4.1 | unknown |
| `2026-06-19T230854Z-openai-gpt-4.1-day01-system-map.md` | openai | gpt-4.1 | unknown |
| `2026-06-19T231108Z-openai-gpt-4.1-day01-applied-foundations.md` | openai | gpt-4.1 | unknown |
| `2026-06-21T020500Z-manual-codex-authored-day01-quality-top-up.md` | manual | codex-authored | quality-top-up |

## Coverage Notes

Primary Day 1 official coverage:

- Task 1.1: Analyze requirements and design GenAI solutions.
- Task 1.2: Select and configure FMs.
- Task 1.6: Implement prompt engineering strategies and governance for FM interactions.
- Task 2.4: Implement FM API integrations.
- Task 2.5: Implement application integration patterns and development tools.

Seeded cross-domain foundations:

- Task 3.2: Implement data security and privacy controls.
- Task 5.1: Implement evaluation systems for GenAI.

The `exam_task` and `exam_skill` fields use official statements extracted
from `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`. The `exam_skill_local` field is an editorial
description of the narrower reviewed focus tested by the item.

## Review Summary

| Curriculum order | Raw parsed | Approved | Culled | Completion target | Status |
|---|---:|---:|---:|---:|---|
| Day01-order001 | 14 | 10 | 4 | 10 | complete |
| Day01-order002 | 14 | 10 | 4 | 10 | complete |
| Day01-order003 | 13 | 10 | 3 | 10 | complete |
| Day01-order004 | 11 | 10 | 1 | 10 | complete |
| Day01-order005 | 11 | 10 | 1 | 10 | complete |
| Day01-order006 | 11 | 10 | 1 | 10 | complete |
| Day01-order007 | 11 | 10 | 1 | 10 | complete |
| Day01-order008 | 11 | 10 | 1 | 10 | complete |
| Day01-order009 | 12 | 10 | 2 | 10 | complete |
| Day01-order010 | 11 | 10 | 1 | 10 | complete |

## Prompt Improvement Signals

Review culls are treated as prompt-improvement data before the next
generation or top-up pass. The next prompt should explicitly address
the highest-frequency failure reasons below instead of only asking for
more questions.

| Failure reason | Count | Prompt adjustment |
|---|---:|---|
| not scenario-based | 12 | Require a concrete actor, workload, goal, constraint, and tradeoff in the stem. |
| recall-only item | 8 | Ask the learner to select, diagnose, configure, judge, or choose a first action instead of defining a term. |
| keyword-trivia stem | 6 | Ban glossary-style stem openers and require distractors that fail because of a constraint. |
| outdated or unverified technical claim | 4 | Avoid time-bound service-capability claims unless the exact official AWS source is named. |

## Top-Up Guidance

The completion target is 10 approved items per curriculum-order topic.
Generate a surplus over the exact deficit because the review pass is
expected to cull weak, duplicate, or unverifiable candidates.

| Curriculum order | Approved | Deficit | Recommended raw top-up |
|---|---:|---:|---:|
| Day01-order001 | 10 | 0 | 0 |
| Day01-order002 | 10 | 0 | 0 |
| Day01-order003 | 10 | 0 | 0 |
| Day01-order004 | 10 | 0 | 0 |
| Day01-order005 | 10 | 0 | 0 |
| Day01-order006 | 10 | 0 | 0 |
| Day01-order007 | 10 | 0 | 0 |
| Day01-order008 | 10 | 0 | 0 |
| Day01-order009 | 10 | 0 | 0 |
| Day01-order010 | 10 | 0 | 0 |

## Review Rules Applied

- Approved items must use the required schema fields or a repairable equivalent.
- Approved items must be scenario-based rather than keyword-trivia recall.
- Approved items must not duplicate or closely mirror an already approved item for the same topic.
- Every cull must include audit evidence explaining the failed rule.
- Duplicate culls must show the rejected stem and the matched approved stem as audit evidence.
- Approved items must have plausible options, correct answers, and distractor rationales.
- Items with stale claims such as `as of early 2024` or unsupported service-limit claims are culled.
- Remediation targets are mapped to existing Day 1 artifact files and answer guidance.
- Source traces are normalized to the official exam guide, AWS documentation, and Day 1 learning materials.

## Approved Items

### P1-AIP-D1-001

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-001 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.1: Analyze requirements and design GenAI solutions. |
| `exam_skill` | Skill 1.1.1: Create comprehensive architectural designs that align with specific business needs and technical constraints (for example, by using appropriate FMs, integration patterns, deployment strategies). |
| `exam_skill_local` | Distinguish model behavior from application responsibilities |
| `learning_unit` | Day01-order001 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Declarative; Conceptual |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | explain |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T230500Z-openai-gpt-4.1-day01-foundations.md` item 1 |

Stem:

A company is considering training its own large language model from scratch to support its text analytics application. What is the primary risk compared to using a proven foundation model via an AWS managed service?

Options:

A. Significantly higher costs and longer time-to-market due to data, compute, and tuning requirements.

B. Increased control over fine-grained model behaviors for niche domains.

C. Much less risk of model hallucinations.

D. Reduced need to monitor model drift and bias.

Correct answer: Significantly higher costs and longer time-to-market due to data, compute, and tuning requirements.

Rationale: Training a foundation model from scratch is resource-intensive in terms of data, compute, and expertise, causing much higher direct and opportunity costs compared to reusing a managed model.

Distractors: Increased control over fine-grained model behaviors for niche domains.: While self-training can increase control, it does not offset the risk—rather, it can increase cost and complexity. Control is not the primary risk. Much less risk of model hallucinations.: Model hallucinations occur in both custom and managed models, and training from scratch without massive high-quality data might increase hallucination risk. Reduced need to monitor model drift and bias.: Any model, trained or managed, still requires active monitoring for drift and bias. Starting from scratch doesn’t remove this duty.

Misconception tags: `start-from-scratch-equals-better`, `monitoring-only-for-managed-models`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`
- `docs/Pilot1/aip-c01/curriculum-model/aip-c01-topic-knowledge-category-map.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order001-foundation-models-genai-fundamentals.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-002

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-002 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.1: Analyze requirements and design GenAI solutions. |
| `exam_skill` | Skill 1.1.1: Create comprehensive architectural designs that align with specific business needs and technical constraints (for example, by using appropriate FMs, integration patterns, deployment strategies). |
| `exam_skill_local` | Distinguish model behavior from application responsibilities |
| `learning_unit` | Day01-order001 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Declarative; Conceptual |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | explain |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T230500Z-openai-gpt-4.1-day01-foundations.md` item 3 |

Stem:

An enterprise uses a foundation model on AWS to automate summarization of legal documents. Suddenly, the summaries contain subtle legal inaccuracies. What is the most likely cause?

Options:

A. The distribution of new legal documents significantly differs from the model's pretraining data.

B. The model's underlying architecture has suddenly changed.

C. The cost threshold for API calls has been lowered.

D. The organization is using the wrong AWS region.

Correct answer: The distribution of new legal documents significantly differs from the model's pretraining data.

Rationale: When input data strays from the training data distribution, especially for complex domains, foundation models can produce unreliable outputs.

Distractors: The model's underlying architecture has suddenly changed.: Vendors rarely change architectures without notice; this is unlikely and would typically trigger service notifications. The cost threshold for API calls has been lowered.: API cost thresholds don’t change model outputs. The organization is using the wrong AWS region.: While region selection matters for latency and compliance, it does not induce legal inaccuracies in text outputs.

Misconception tags: `model-guarantees-domain-expertise`, `architecture-blame`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`
- `docs/Pilot1/aip-c01/curriculum-model/aip-c01-topic-knowledge-category-map.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order001-foundation-models-genai-fundamentals.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-003

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-003 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.1: Analyze requirements and design GenAI solutions. |
| `exam_skill` | Skill 1.1.1: Create comprehensive architectural designs that align with specific business needs and technical constraints (for example, by using appropriate FMs, integration patterns, deployment strategies). |
| `exam_skill_local` | Distinguish model behavior from application responsibilities |
| `learning_unit` | Day01-order001 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Declarative; Conceptual |
| `question_format` | multiple-response |
| `difficulty` | medium |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T230500Z-openai-gpt-4.1-day01-foundations.md` item 4 |

Stem:

Which two of the following actions are commonly required to adapt a foundation model for a specialized enterprise use case? (Select TWO.)

Options:

A. Fine-tuning the model with domain-specific data.

B. Prompt engineering to guide the model’s outputs.

C. Lowering the model’s token context window.

D. Switching to a lighter model without retraining.

E. Ignoring prompt structure since the model is pre-trained.

Correct answer: Fine-tuning the model with domain-specific data., Prompt engineering to guide the model’s outputs.

Rationale: Fine-tuning and prompt engineering are the two standard ways to adapt foundation models to specialized domains.

Distractors: Lowering the model’s token context window.: Reducing context window typically limits performance rather than adapting the model. Switching to a lighter model without retraining.: Switching models does not constitute adaptation; it risks losing needed capabilities. Ignoring prompt structure since the model is pre-trained.: Prompt structure is always important, even for pre-trained models.

Misconception tags: `prompt-irrelevance`, `context-window-overemphasis`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`
- `docs/Pilot1/aip-c01/curriculum-model/aip-c01-topic-knowledge-category-map.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order001-foundation-models-genai-fundamentals.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-004

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-004 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.1: Analyze requirements and design GenAI solutions. |
| `exam_skill` | Skill 1.1.1: Create comprehensive architectural designs that align with specific business needs and technical constraints (for example, by using appropriate FMs, integration patterns, deployment strategies). |
| `exam_skill_local` | Distinguish model behavior from application responsibilities |
| `learning_unit` | Day01-order001 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Declarative; Conceptual |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | compare |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T230500Z-openai-gpt-4.1-day01-foundations.md` item 5 |

Stem:

A team is weighing two approaches: (A) fine-tuning a foundation model versus (B) training a model from scratch. Which is the main advantage of approach A?

Options:

A. It requires significantly fewer computational resources and less training data.

B. It enables full control over every parameter and weight.

C. It eliminates the need for domain-specific expertise.

D. It produces smaller model sizes suitable for edge deployment.

Correct answer: It requires significantly fewer computational resources and less training data.

Rationale: Fine-tuning a foundation model leverages prior training and only requires adaptation data, cutting down cost and effort.

Distractors: It enables full control over every parameter and weight.: Full control is more relevant in from-scratch training. It eliminates the need for domain-specific expertise.: Domain knowledge is still vital for quality fine-tuning. It produces smaller model sizes suitable for edge deployment.: Fine-tuned models typically have similar size unless quantized or further compressed.

Misconception tags: `tuning-vs-control`, `domain-knowledge-overlooked`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`
- `docs/Pilot1/aip-c01/curriculum-model/aip-c01-topic-knowledge-category-map.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order001-foundation-models-genai-fundamentals.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-005

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-005 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.1: Analyze requirements and design GenAI solutions. |
| `exam_skill` | Skill 1.1.1: Create comprehensive architectural designs that align with specific business needs and technical constraints (for example, by using appropriate FMs, integration patterns, deployment strategies). |
| `exam_skill_local` | Distinguish model behavior from application responsibilities |
| `learning_unit` | Day01-order001 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Declarative; Conceptual |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T230500Z-openai-gpt-4.1-day01-foundations.md` item 7 |

Stem:

A developer observes that outputs from a foundation model demonstrate unexpected biases toward recent internet slang. What is the likely explanation?

Options:

A. The model has been primarily pre-trained on recent public web data.

B. The developer is using an outdated client library.

C. Output bias can only be caused by explicit adversarial attacks.

D. The number of generated tokens per request is too high.

Correct answer: The model has been primarily pre-trained on recent public web data.

Rationale: Foundation models reflect patterns in recent, high-volume data sources if they dominate the training set.

Distractors: The developer is using an outdated client library.: This affects deployment compatibility, not output content generation. Output bias can only be caused by explicit adversarial attacks.: Bias is often emergent from training data, not just attacks. The number of generated tokens per request is too high.: Token count affects output length, not bias.

Misconception tags: `bias-causal-confusion`, `deployment-vs-training-data`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`
- `docs/Pilot1/aip-c01/curriculum-model/aip-c01-topic-knowledge-category-map.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order001-foundation-models-genai-fundamentals.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-006

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-006 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.1: Analyze requirements and design GenAI solutions. |
| `exam_skill` | Skill 1.1.1: Create comprehensive architectural designs that align with specific business needs and technical constraints (for example, by using appropriate FMs, integration patterns, deployment strategies). |
| `exam_skill_local` | Distinguish model behavior from application responsibilities |
| `learning_unit` | Day01-order001 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Declarative; Conceptual |
| `question_format` | multiple-response |
| `difficulty` | hard |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T230500Z-openai-gpt-4.1-day01-foundations.md` item 9 |

Stem:

Which THREE factors must be considered when assessing if a foundation model is ‘safe’ to use in a regulated healthcare application? (Select THREE.)

Options:

A. Evidence of training dataset coverage and documentation.

B. Demonstrated ability to handle sensitive information securely.

C. Regularly audited output monitoring and risk management processes.

D. Whether the model can generate images from text.

E. If the model’s developer won a major AI competition.

Correct answer: Evidence of training dataset coverage and documentation., Demonstrated ability to handle sensitive information securely., Regularly audited output monitoring and risk management processes.

Rationale: Coverage, data handling, and output/risk procedures are all required for safe use in regulated settings.

Distractors: Whether the model can generate images from text.: Capability is not equivalent to safety or compliance. If the model’s developer won a major AI competition.: Reputation does not guarantee compliance or safety practices.

Misconception tags: `capability-equals-safety`, `developer-reputation-overreliance`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`
- `docs/Pilot1/aip-c01/curriculum-model/aip-c01-topic-knowledge-category-map.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order001-foundation-models-genai-fundamentals.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-007

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-007 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.1: Analyze requirements and design GenAI solutions. |
| `exam_skill` | Skill 1.1.1: Create comprehensive architectural designs that align with specific business needs and technical constraints (for example, by using appropriate FMs, integration patterns, deployment strategies). |
| `exam_skill_local` | Distinguish model behavior from application responsibilities |
| `learning_unit` | Day01-order001 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Declarative; Conceptual |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | judge |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-21T020500Z-manual-codex-authored-day01-quality-top-up.md` item 1 |

Stem:

A product team wants a GenAI assistant to draft support replies, but leadership expects the model itself to enforce refund policy, check customer entitlements, and open tickets. Which design decision best separates foundation-model capability from application responsibility?

Options:

A. Use the foundation model for language generation while the application retrieves policy, verifies entitlements, and performs ticket actions through controlled services.

B. Fine-tune the model on refund policies so the model can become the system of record for entitlement decisions.

C. Increase the model context window so all policies fit into the prompt and no application controls are needed.

D. Move ticket creation into the prompt instructions so the model can decide when operational actions are valid.

Correct answer: A

Rationale: The model can generate and reason over text, but application code and trusted services should enforce policy, authorization, state changes, and workflow actions.

Distractors: B: Fine-tuning may improve task behavior but does not make the model a trusted authority for entitlement or policy enforcement. C: A larger context window does not replace deterministic application controls. D: Prompt instructions cannot safely perform or authorize operational side effects by themselves.

Misconception tags: `model-vs-application-confusion`, `prompt-as-control-plane`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`
- `docs/Pilot1/aip-c01/curriculum-model/aip-c01-topic-knowledge-category-map.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order001-foundation-models-genai-fundamentals.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-008

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-008 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.1: Analyze requirements and design GenAI solutions. |
| `exam_skill` | Skill 1.1.1: Create comprehensive architectural designs that align with specific business needs and technical constraints (for example, by using appropriate FMs, integration patterns, deployment strategies). |
| `exam_skill_local` | Distinguish model behavior from application responsibilities |
| `learning_unit` | Day01-order001 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Declarative; Conceptual |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-21T020500Z-manual-codex-authored-day01-quality-top-up.md` item 2 |

Stem:

A company deploys a summarization feature using a foundation model. Users report fluent summaries that occasionally introduce claims not present in the source documents. What is the best initial interpretation of this failure?

Options:

A. The system is seeing a generative behavior risk and needs grounding, evaluation, and output controls around the model.

B. The model endpoint is unavailable and the application is falling back to cached summaries.

C. The model has been trained from scratch incorrectly and must be rebuilt before any mitigation is possible.

D. The token limit is always the root cause whenever a summary contains unsupported claims.

Correct answer: A

Rationale: Fluent unsupported claims are a known GenAI output risk; the application should add grounding, checks, and evaluation rather than assuming infrastructure outage or retraining from scratch.

Distractors: B: Endpoint failure would usually present as invocation errors or fallback behavior, not necessarily fluent new claims. C: Most teams use existing foundation models; rebuilding from scratch is not the first response. D: Truncation can cause omissions, but unsupported claims are broader than token limits alone.

Misconception tags: `hallucination-as-infrastructure-failure`, `training-from-scratch-default`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`
- `docs/Pilot1/aip-c01/curriculum-model/aip-c01-topic-knowledge-category-map.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order001-foundation-models-genai-fundamentals.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-009

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-009 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.1: Analyze requirements and design GenAI solutions. |
| `exam_skill` | Skill 1.1.1: Create comprehensive architectural designs that align with specific business needs and technical constraints (for example, by using appropriate FMs, integration patterns, deployment strategies). |
| `exam_skill_local` | Distinguish model behavior from application responsibilities |
| `learning_unit` | Day01-order001 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Declarative; Conceptual |
| `question_format` | multiple-response |
| `difficulty` | exam-plus |
| `cognitive_demand` | compare |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-21T020500Z-manual-codex-authored-day01-quality-top-up.md` item 3 |

Stem:

A team is deciding whether a planned feature should be treated as a GenAI use case or a conventional rules-and-search workflow. Which two signals most strongly indicate that a foundation model is appropriate? (Select TWO.)

Options:

A. The output must be synthesized in natural language from variable user input and contextual evidence.

B. The workflow requires deterministic arithmetic on a fixed schema with no language ambiguity.

C. The feature needs flexible interpretation of messy text, intent, or semantic similarity.

D. The main requirement is to copy an exact stored value from one database field to another.

E. The business wants to remove all validation and authorization code from the application.

Correct answer: A, C

Rationale: Foundation models are well suited when the task requires language synthesis, semantic interpretation, or flexible handling of unstructured input.

Distractors: B: Deterministic arithmetic over fixed schemas is usually better handled with conventional code. D: Exact data movement is not a GenAI capability need. E: Using a model does not remove the need for validation or authorization.

Misconception tags: `genai-for-everything`, `model-vs-application-confusion`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`
- `docs/Pilot1/aip-c01/curriculum-model/aip-c01-topic-knowledge-category-map.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order001-foundation-models-genai-fundamentals.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-010

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-010 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.1: Analyze requirements and design GenAI solutions. |
| `exam_skill` | Skill 1.1.1: Create comprehensive architectural designs that align with specific business needs and technical constraints (for example, by using appropriate FMs, integration patterns, deployment strategies). |
| `exam_skill_local` | Distinguish model behavior from application responsibilities |
| `learning_unit` | Day01-order001 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Declarative; Conceptual |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-21T020500Z-manual-codex-authored-day01-quality-top-up.md` item 4 |

Stem:

An enterprise architecture review finds that a proposed GenAI service sends user prompts directly to a model and returns the raw response to the user. Which addition most directly turns the model call into a governed application workflow?

Options:

A. Add retrieval, input validation, authorization checks, output validation, logging, and human escalation paths around the model invocation.

B. Raise temperature so responses cover a wider range of user intents.

C. Store prompts in a larger object store before sending them to the model.

D. Replace all application code with a longer system prompt that describes company policy.

Correct answer: A

Rationale: A governed GenAI application wraps model inference with controls, context, validation, observability, and operational handling.

Distractors: B: Temperature affects output variability, not governance. C: Storage alone does not create controls or workflow. D: Prompts help steer behavior but do not replace application controls.

Misconception tags: `raw-model-call-as-application`, `security-afterthought`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`
- `docs/Pilot1/aip-c01/curriculum-model/aip-c01-topic-knowledge-category-map.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order001-foundation-models-genai-fundamentals.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-011

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-011 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.5: Enhance FM performance to refine prompts iteratively and improve response quality beyond basic prompting techniques (for example, by using structured input components, output format specifications, chain-of-thought instruction patterns, feedback loops). |
| `exam_skill_local` | Predict effects of token and inference-parameter choices |
| `learning_unit` | Day01-order002 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Declarative; Conceptual; Causal |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T230500Z-openai-gpt-4.1-day01-foundations.md` item 11 |

Stem:

A developer increases the input length for a summarization task and notices that the model starts omitting key points from the end of the input. What is the most likely explanation?

Options:

A. The model’s context window is being exceeded, causing truncation.

B. The temperature parameter is too low, making outputs more deterministic.

C. The top-p parameter is set to 1, making sampling too diverse.

D. The model is overfitting on recent inputs.

Correct answer: The model’s context window is being exceeded, causing truncation.

Rationale: Exceeding the context window means tokens at the end of the input are dropped or ignored.

Distractors: The temperature parameter is too low, making outputs more deterministic.: Temperature affects randomness, not token truncation. The top-p parameter is set to 1, making sampling too diverse.: Setting top-p to 1 does not cause input truncation. The model is overfitting on recent inputs.: Overfitting is a training issue, irrelevant to single inference context.

Misconception tags: `context-window-vs-temperature`, `sampling-vs-context-window`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order002-tokens-context-inference-parameters.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-012

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-012 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.5: Enhance FM performance to refine prompts iteratively and improve response quality beyond basic prompting techniques (for example, by using structured input components, output format specifications, chain-of-thought instruction patterns, feedback loops). |
| `exam_skill_local` | Predict effects of token and inference-parameter choices |
| `learning_unit` | Day01-order002 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Declarative; Conceptual; Causal |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T230500Z-openai-gpt-4.1-day01-foundations.md` item 13 |

Stem:

A product discovery chatbot produces repetitive answers even though the knowledge base is large. What inference parameter adjustment is most likely to resolve this?

Options:

A. Increase the temperature parameter to introduce more variability.

B. Decrease the context window size.

C. Lower the top-p parameter to restrict sampling.

D. Add more tokens to the user prompt.

Correct answer: Increase the temperature parameter to introduce more variability.

Rationale: Higher temperature increases randomness, making repeated outputs less likely.

Distractors: Decrease the context window size.: Reducing the context window will likely make the model less informed, not more varied. Lower the top-p parameter to restrict sampling.: Restricting top-p makes outputs even more repetitive. Add more tokens to the user prompt.: This may add context, but does not directly influence output diversity.

Misconception tags: `context-vs-temperature`, `diversity-via-context`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order002-tokens-context-inference-parameters.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-013

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-013 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.5: Enhance FM performance to refine prompts iteratively and improve response quality beyond basic prompting techniques (for example, by using structured input components, output format specifications, chain-of-thought instruction patterns, feedback loops). |
| `exam_skill_local` | Predict effects of token and inference-parameter choices |
| `learning_unit` | Day01-order002 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Declarative; Conceptual; Causal |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | explain |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T230500Z-openai-gpt-4.1-day01-foundations.md` item 14 |

Stem:

What is the main tradeoff when you lower the top-k value during generative text sampling?

Options:

A. The output will be more deterministic, but may lose diversity.

B. The model will process inputs faster.

C. The output will become more random and verbose.

D. The model will consume more memory during inference.

Correct answer: The output will be more deterministic, but may lose diversity.

Rationale: Lowering top-k restricts the choices to a smaller set, making outputs more focused but less diverse.

Distractors: The model will process inputs faster.: Top-k does not impact processing time in a meaningful way. The output will become more random and verbose.: Limiting top-k does the opposite—less randomness. The model will consume more memory during inference.: Memory usage is mostly unaffected.

Misconception tags: `sampling-vs-performance`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order002-tokens-context-inference-parameters.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-014

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-014 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.5: Enhance FM performance to refine prompts iteratively and improve response quality beyond basic prompting techniques (for example, by using structured input components, output format specifications, chain-of-thought instruction patterns, feedback loops). |
| `exam_skill_local` | Predict effects of token and inference-parameter choices |
| `learning_unit` | Day01-order002 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Declarative; Conceptual; Causal |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | explain |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T230500Z-openai-gpt-4.1-day01-foundations.md` item 15 |

Stem:

An application team is surprised by highly variable model output lengths for similar prompts, even with the same input token counts. Which parameter is most likely responsible for this variability?

Options:

A. Temperature

B. Context window size

C. Model version

D. Input encoding format

Correct answer: Temperature

Rationale: Temperature controls randomness; higher temperature leads to more varied outputs, including lengths.

Distractors: Context window size.: This is a hard limit, not a parameter producing variability per request. Model version.: This affects model capabilities, not direct per-call variability given same version. Input encoding format.: This determines token parsing, not output length.

Misconception tags: `context-vs-temperature`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order002-tokens-context-inference-parameters.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-015

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-015 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.5: Enhance FM performance to refine prompts iteratively and improve response quality beyond basic prompting techniques (for example, by using structured input components, output format specifications, chain-of-thought instruction patterns, feedback loops). |
| `exam_skill_local` | Predict effects of token and inference-parameter choices |
| `learning_unit` | Day01-order002 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Declarative; Conceptual; Causal |
| `question_format` | multiple-response |
| `difficulty` | medium |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T230500Z-openai-gpt-4.1-day01-foundations.md` item 16 |

Stem:

A data scientist must ensure outputs are both relevant to the prompt and diverse when generating creative marketing slogans. Which TWO parameter settings best support this? (Select TWO.)

Options:

A. Increase the temperature moderately.

B. Set top-k to a value greater than 1.

C. Reduce the input context window.

D. Decrease the temperature to near zero.

E. Set top-p to a high value, such as 0.95.

Correct answer: Increase the temperature moderately., Set top-p to a high value, such as 0.95.

Rationale: Higher temperature encourages creativity; high top-p samples from a wider probability distribution for more diverse outputs.

Distractors: Set top-k to a value greater than 1.: Increasing top-k (if used) is possible, but top-p is more commonly supported and interpretable. Reduce the input context window.: This would lower prompt quality, not encourage diversity. Decrease the temperature to near zero.: This enforces deterministic, less creative outputs.

Misconception tags: `context-window-diversity`, `low-temp-diversity`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order002-tokens-context-inference-parameters.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-016

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-016 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.5: Enhance FM performance to refine prompts iteratively and improve response quality beyond basic prompting techniques (for example, by using structured input components, output format specifications, chain-of-thought instruction patterns, feedback loops). |
| `exam_skill_local` | Predict effects of token and inference-parameter choices |
| `learning_unit` | Day01-order002 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Declarative; Conceptual; Causal |
| `question_format` | multiple-response |
| `difficulty` | medium |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T230500Z-openai-gpt-4.1-day01-foundations.md` item 19 |

Stem:

You are troubleshooting an inference pipeline for a customer service chatbot that suddenly returns truncated or incomplete responses. Which TWO actions are most likely to resolve this? (Select TWO.)

Options:

A. Reduce the length of the user prompt and system context.

B. Increase the model’s maximum output tokens setting.

C. Decrease the temperature parameter to minimize random cutoffs.

D. Switch the sampling method from top-k to top-p.

E. Limit the number of concurrent active inference calls.

Correct answer: Reduce the length of the user prompt and system context., Increase the model’s maximum output tokens setting.

Rationale: Shorter prompts leave more room for output, and adjusting max output tokens combats truncation.

Distractors: Decrease the temperature parameter to minimize random cutoffs.: Temperature changes output randomness, not cutoffs. Switch the sampling method from top-k to top-p.: This swaps sampling style, not output budget. Limit the number of concurrent active inference calls.: Concurrency affects scaling, not output truncation.

Misconception tags: `sampling-vs-budget`, `temperature-vs-truncation`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order002-tokens-context-inference-parameters.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-017

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-017 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.5: Enhance FM performance to refine prompts iteratively and improve response quality beyond basic prompting techniques (for example, by using structured input components, output format specifications, chain-of-thought instruction patterns, feedback loops). |
| `exam_skill_local` | Predict effects of token and inference-parameter choices |
| `learning_unit` | Day01-order002 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Declarative; Conceptual; Causal |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-21T020500Z-manual-codex-authored-day01-quality-top-up.md` item 5 |

Stem:

A team adds long policy documents to every prompt for a chatbot. Latency and cost rise sharply, and some late-document rules appear to be ignored. Which explanation best connects the symptoms?

Options:

A. The prompt is consuming more tokens, increasing inference work and risking context-window truncation or reduced attention to later content.

B. The model has switched from inference mode to training mode because the prompt contains policy documents.

C. Lowering top-p will automatically reduce token usage while preserving all policy context.

D. The application must raise temperature because long prompts always make outputs deterministic.

Correct answer: A

Rationale: Longer prompts consume more tokens, increase processing cost and latency, and can stress context-window limits.

Distractors: B: Including documents in a prompt does not train the model. C: Top-p affects sampling, not how many input tokens are sent. D: Temperature controls randomness, not whether long prompts are fully represented.

Misconception tags: `bigger-context-is-always-better`, `prompt-is-training`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order002-tokens-context-inference-parameters.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-018

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-018 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.5: Enhance FM performance to refine prompts iteratively and improve response quality beyond basic prompting techniques (for example, by using structured input components, output format specifications, chain-of-thought instruction patterns, feedback loops). |
| `exam_skill_local` | Predict effects of token and inference-parameter choices |
| `learning_unit` | Day01-order002 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Declarative; Conceptual; Causal |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-21T020500Z-manual-codex-authored-day01-quality-top-up.md` item 6 |

Stem:

A customer-support assistant must answer policy questions consistently and avoid creative wording in regulated responses. Which inference-parameter strategy is the best starting point?

Options:

A. Use a lower temperature and constrain sampling so the model favors more predictable completions.

B. Use a higher temperature so the model explores more unusual response paths.

C. Maximize top-k so every possible token is equally likely.

D. Increase the context window and leave sampling unconstrained because consistency comes only from more context.

Correct answer: A

Rationale: Lower-temperature and constrained sampling settings are a reasonable starting point when consistency matters more than creative variation.

Distractors: B: Higher temperature tends to increase variation. C: Broad sampling does not improve consistency. D: More context can help grounding but does not by itself control output variability.

Misconception tags: `temperature-means-quality`, `context-window-as-control`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order002-tokens-context-inference-parameters.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-019

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-019 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.5: Enhance FM performance to refine prompts iteratively and improve response quality beyond basic prompting techniques (for example, by using structured input components, output format specifications, chain-of-thought instruction patterns, feedback loops). |
| `exam_skill_local` | Predict effects of token and inference-parameter choices |
| `learning_unit` | Day01-order002 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Declarative; Conceptual; Causal |
| `question_format` | multiple-response |
| `difficulty` | exam-plus |
| `cognitive_demand` | judge |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-21T020500Z-manual-codex-authored-day01-quality-top-up.md` item 7 |

Stem:

A team is tuning a model-backed code-review assistant. They want concise comments, stable formatting, and enough room for a pull-request diff. Which two changes address different parts of the problem? (Select TWO.)

Options:

A. Set explicit output-length and formatting instructions in the prompt.

B. Choose a context window large enough for the diff and required review instructions.

C. Raise temperature to make the assistant less likely to vary its formatting.

D. Assume top-k controls how many input files can be included in the request.

E. Remove all examples from the prompt because examples always waste context.

Correct answer: A, B

Rationale: Formatting and output length are prompt-design concerns; fitting the diff and instructions is a context-window/token-budget concern.

Distractors: C: Higher temperature generally increases variation. D: Top-k affects sampling over output tokens, not the number of input files. E: Examples can be valuable when used deliberately within the token budget.

Misconception tags: `sampling-vs-context-confusion`, `examples-are-always-bad`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order002-tokens-context-inference-parameters.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-020

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-020 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.5: Enhance FM performance to refine prompts iteratively and improve response quality beyond basic prompting techniques (for example, by using structured input components, output format specifications, chain-of-thought instruction patterns, feedback loops). |
| `exam_skill_local` | Predict effects of token and inference-parameter choices |
| `learning_unit` | Day01-order002 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Declarative; Conceptual; Causal |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-21T020500Z-manual-codex-authored-day01-quality-top-up.md` item 8 |

Stem:

An application passes a retrieved contract excerpt plus a user question to a model. The response omits a clause that appears near the end of the excerpt. Which first investigation is most appropriate?

Options:

A. Check token counts, truncation behavior, prompt ordering, and whether the relevant clause is within the effective context sent to the model.

B. Assume the model permanently learned an incorrect version of the contract and fine-tune immediately.

C. Increase temperature so the model is more likely to mention unusual clauses.

D. Remove retrieval and ask the model to rely on pretraining for contract terms.

Correct answer: A

Rationale: The symptom may come from token budget, truncation, prompt structure, or retrieval packaging, so those should be checked first.

Distractors: B: Prompted context is not permanent training data, and fine-tuning is not the first diagnostic step. C: Temperature does not guarantee attention to omitted context. D: Pretraining is not reliable for specific contract clauses.

Misconception tags: `prompt-is-training`, `temperature-fixes-grounding`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order002-tokens-context-inference-parameters.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-021

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-021 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.1: Analyze requirements and design GenAI solutions. |
| `exam_skill` | Skill 1.1.1: Create comprehensive architectural designs that align with specific business needs and technical constraints (for example, by using appropriate FMs, integration patterns, deployment strategies). |
| `exam_skill_local` | Classify AWS services by role in a GenAI application |
| `learning_unit` | Day01-order003 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Declarative; Conceptual; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T230854Z-openai-gpt-4.1-day01-system-map.md` item 1 |

Stem:

A team plans to build a GenAI application on AWS that requires custom model training pipelines, hosting of proprietary model artifacts, endpoint management, and integration with text-embedding workflows. Which AWS managed service best fits this custom model platform requirement?

Options:

A. Amazon Bedrock

B. Amazon SageMaker

C. Amazon Lex

D. AWS Lambda

Correct answer: Amazon SageMaker

Rationale: Amazon SageMaker provides managed ML infrastructure for custom training pipelines, proprietary model hosting, endpoint management, and integration with embedding workflows.

Distractors: Amazon Bedrock: Amazon Bedrock provides managed access to supported foundation models and customization options, but it is not the best fit when the requirement is a custom model training and hosting platform for proprietary model artifacts. Amazon Lex: Amazon Lex is focused on conversational chatbots and does not expose direct foundation model fine-tuning or embedding features. AWS Lambda: AWS Lambda is a compute service but does not provide native GenAI models or model management.

Misconception tags: `service-scope-confusion`, `bedrock-does-everything`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- AWS Bedrock User Guide: <https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html>
- AWS Lambda Developer Guide: <https://docs.aws.amazon.com/lambda/latest/dg/welcome.html>
- Amazon CloudWatch User Guide: <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html>
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order003-aws-genai-service-landscape.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-022

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-022 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.1: Analyze requirements and design GenAI solutions. |
| `exam_skill` | Skill 1.1.1: Create comprehensive architectural designs that align with specific business needs and technical constraints (for example, by using appropriate FMs, integration patterns, deployment strategies). |
| `exam_skill_local` | Classify AWS services by role in a GenAI application |
| `learning_unit` | Day01-order003 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Declarative; Conceptual; Embedded |
| `question_format` | multiple-response |
| `difficulty` | medium |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T230854Z-openai-gpt-4.1-day01-system-map.md` item 2 |

Stem:

Which of the following AWS services can directly host large language models for real-time inference? (Select TWO.)

Options:

A. Amazon SageMaker

B. Amazon Bedrock

C. Amazon Polly

D. AWS Batch

E. Amazon Rekognition

Correct answer: Amazon SageMaker, Amazon Bedrock

Rationale: SageMaker and Bedrock can both host large language models for inference workflows. Bedrock provides API-based foundation model inference, and SageMaker offers custom LLM hosting.

Distractors: Amazon Polly: Polly converts text to speech and does not host LLMs. AWS Batch: Batch is for batch compute and does not natively host LLMs. Amazon Rekognition: Rekognition is for image and video analysis, not text LLM hosting.

Misconception tags: `service-matchup-confusion`, `llm-terminology-confusion`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- AWS Bedrock User Guide: <https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html>
- AWS Lambda Developer Guide: <https://docs.aws.amazon.com/lambda/latest/dg/welcome.html>
- Amazon CloudWatch User Guide: <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html>
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order003-aws-genai-service-landscape.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-023

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-023 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.1: Analyze requirements and design GenAI solutions. |
| `exam_skill` | Skill 1.1.1: Create comprehensive architectural designs that align with specific business needs and technical constraints (for example, by using appropriate FMs, integration patterns, deployment strategies). |
| `exam_skill_local` | Classify AWS services by role in a GenAI application |
| `learning_unit` | Day01-order003 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Declarative; Conceptual; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T230854Z-openai-gpt-4.1-day01-system-map.md` item 4 |

Stem:

A regulated company needs to ensure all GenAI data remains in a dedicated VPC and never leaves their specified AWS Region. Which service is best suited to enforce these strict network and data residency controls for custom model hosting?

Options:

A. Amazon SageMaker

B. Amazon Bedrock

C. Amazon Translate

D. AWS Chatbot

Correct answer: Amazon SageMaker

Rationale: SageMaker provides fine-grained control over networking, including VPC endpoints and regional controls for custom model deployments. Bedrock is managed and abstracts some of these controls.

Distractors: Amazon Bedrock: Amazon Bedrock is a managed foundation-model service for invoking supported FMs. It is not the best fit when the requirement is custom model hosting with fine-grained control over the model-serving environment. Amazon Translate: Translate is a managed service, not suitable for custom model hosting. AWS Chatbot: AWS Chatbot integrates chat tools with AWS, not used for GenAI model hosting or compliance.

Misconception tags: `bedrock-vs-sagemaker-compliance`, `misunderstood-data-isolation`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- AWS Bedrock User Guide: <https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html>
- AWS Lambda Developer Guide: <https://docs.aws.amazon.com/lambda/latest/dg/welcome.html>
- Amazon CloudWatch User Guide: <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html>
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order003-aws-genai-service-landscape.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-024

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-024 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.1: Analyze requirements and design GenAI solutions. |
| `exam_skill` | Skill 1.1.1: Create comprehensive architectural designs that align with specific business needs and technical constraints (for example, by using appropriate FMs, integration patterns, deployment strategies). |
| `exam_skill_local` | Classify AWS services by role in a GenAI application |
| `learning_unit` | Day01-order003 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Declarative; Conceptual; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T230854Z-openai-gpt-4.1-day01-system-map.md` item 7 |

Stem:

A startup wants to integrate an externally hosted LLM via API into their AWS application, while keeping the option to swap to AWS-native FMs in the future. Which architectural choice best supports this flexibility?

Options:

A. Design a thin wrapper interface in their application between the API and downstream logic

B. Hardcode API calls throughout the application code

C. Use AWS Lambda to invoke external HTTP APIs directly

D. Directly proxy all API calls via an AWS API Gateway

Correct answer: Design a thin wrapper interface in their application between the API and downstream logic

Rationale: A wrapper interface abstracts model-specific API differences, allowing an easy switch to AWS-native FMs with minimal refactoring.

Distractors: Hardcode API calls throughout the application code: Hardcoding leads to inflexible code that is difficult and risky to swap out. Use AWS Lambda to invoke external HTTP APIs directly: Lambda invocation could help, but without an interface, model-specific logic leaks into the Lambda. Directly proxy all API calls via an AWS API Gateway: While API Gateway simplifies endpoint exposure, it doesn't abstract protocol or payload details, nor help portability.

Misconception tags: `api-vs-abstraction-confusion`, `cloud-native-only-mindset`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- AWS Bedrock User Guide: <https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html>
- AWS Lambda Developer Guide: <https://docs.aws.amazon.com/lambda/latest/dg/welcome.html>
- Amazon CloudWatch User Guide: <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html>
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order003-aws-genai-service-landscape.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-025

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-025 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.1: Analyze requirements and design GenAI solutions. |
| `exam_skill` | Skill 1.1.1: Create comprehensive architectural designs that align with specific business needs and technical constraints (for example, by using appropriate FMs, integration patterns, deployment strategies). |
| `exam_skill_local` | Classify AWS services by role in a GenAI application |
| `learning_unit` | Day01-order003 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Declarative; Conceptual; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | compare |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T230854Z-openai-gpt-4.1-day01-system-map.md` item 8 |

Stem:

Which AWS service enables retrieval-augmented generation (RAG) by providing vector search over embeddings to supplement GenAI model responses?

Options:

A. Amazon OpenSearch Serverless

B. AWS Lambda

C. Amazon EC2

D. AWS Batch

Correct answer: Amazon OpenSearch Serverless

Rationale: Amazon OpenSearch supports vector search and is used for RAG workloads in AWS.

Distractors: AWS Lambda: Lambda is a serverless compute engine, not a search/indexing service. Amazon EC2: EC2 is basic compute; you must build, operate, and maintain the entire solution. AWS Batch: Batch is for running compute workloads, not indexing or vector search.

Misconception tags: `vector-search-implementation-confusion`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- AWS Bedrock User Guide: <https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html>
- AWS Lambda Developer Guide: <https://docs.aws.amazon.com/lambda/latest/dg/welcome.html>
- Amazon CloudWatch User Guide: <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html>
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order003-aws-genai-service-landscape.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-026

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-026 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.1: Analyze requirements and design GenAI solutions. |
| `exam_skill` | Skill 1.1.1: Create comprehensive architectural designs that align with specific business needs and technical constraints (for example, by using appropriate FMs, integration patterns, deployment strategies). |
| `exam_skill_local` | Classify AWS services by role in a GenAI application |
| `learning_unit` | Day01-order003 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Declarative; Conceptual; Embedded |
| `question_format` | multiple-response |
| `difficulty` | medium |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T230854Z-openai-gpt-4.1-day01-system-map.md` item 9 |

Stem:

You want to offer an intelligent chatbot in your web application using AWS-native services. Which services could you combine to implement a GenAI-based conversational agent with voice input and output? (Select TWO.)

Options:

A. Amazon Lex

B. Amazon Polly

C. AWS Identity Center

D. AWS Glue

E. Amazon CloudWatch

Correct answer: Amazon Lex, Amazon Polly

Rationale: Lex is AWS's native conversational AI (bot) service, and Polly can generate speech from text, enabling voice output.

Distractors: AWS Identity Center: Identity management, unrelated to conversational flows. AWS Glue: Data integration/ETL, not chatbots. Amazon CloudWatch: Monitoring service, not chatbot NLU or TTS.

Misconception tags: `chatbot-vs-NLU-vs-TTS`, `misapplied-service-use`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- AWS Bedrock User Guide: <https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html>
- AWS Lambda Developer Guide: <https://docs.aws.amazon.com/lambda/latest/dg/welcome.html>
- Amazon CloudWatch User Guide: <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html>
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order003-aws-genai-service-landscape.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-027

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-027 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.1: Analyze requirements and design GenAI solutions. |
| `exam_skill` | Skill 1.1.1: Create comprehensive architectural designs that align with specific business needs and technical constraints (for example, by using appropriate FMs, integration patterns, deployment strategies). |
| `exam_skill_local` | Classify AWS services by role in a GenAI application |
| `learning_unit` | Day01-order003 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Declarative; Conceptual; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T230854Z-openai-gpt-4.1-day01-system-map.md` item 10 |

Stem:

A production workload needs a fully managed, scalable API for real-time inference from multiple foundation models with pay-per-use pricing on AWS. What should you select?

Options:

A. Amazon Bedrock

B. Amazon SageMaker

C. Amazon EC2

D. Amazon S3

Correct answer: Amazon Bedrock

Rationale: Bedrock provides a unified, managed API for multiple foundation models, with no infra to manage and consumption-based billing.

Distractors: Amazon SageMaker: SageMaker requires more config and management and does not offer the same unified API experience for multi-vendor FM APIs as Bedrock. Amazon EC2: EC2 is base compute, not a GenAI inference service. Amazon S3: S3 is object storage, not an inference API.

Misconception tags: `sagemaker-vs-bedrock-confusion`, `compute-vs-api-misunderstanding`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- AWS Bedrock User Guide: <https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html>
- AWS Lambda Developer Guide: <https://docs.aws.amazon.com/lambda/latest/dg/welcome.html>
- Amazon CloudWatch User Guide: <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html>
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order003-aws-genai-service-landscape.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-028

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-028 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.1: Analyze requirements and design GenAI solutions. |
| `exam_skill` | Skill 1.1.1: Create comprehensive architectural designs that align with specific business needs and technical constraints (for example, by using appropriate FMs, integration patterns, deployment strategies). |
| `exam_skill_local` | Classify AWS services by role in a GenAI application |
| `learning_unit` | Day01-order003 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Declarative; Conceptual; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-21T020500Z-manual-codex-authored-day01-quality-top-up.md` item 9 |

Stem:

A team needs managed access to multiple foundation models, embeddings, and guardrail features without operating model-serving infrastructure. Which service role should they place at the model-access layer of their architecture?

Options:

A. Amazon Bedrock for managed foundation-model access and related GenAI capabilities.

B. Amazon CloudWatch as the primary model runtime because it stores operational metrics.

C. AWS CloudFormation as the runtime inference endpoint because it provisions stacks.

D. Amazon S3 as the model reasoning layer because it stores prompt and document files.

Correct answer: A

Rationale: Amazon Bedrock belongs at the managed foundation-model access layer for invoking models and related GenAI capabilities.

Distractors: B: CloudWatch observes systems but is not the model runtime. C: CloudFormation provisions infrastructure but does not perform inference. D: S3 stores data but does not provide model reasoning.

Misconception tags: `service-role-confusion`, `storage-as-runtime`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- AWS Bedrock User Guide: <https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html>
- AWS Lambda Developer Guide: <https://docs.aws.amazon.com/lambda/latest/dg/welcome.html>
- Amazon CloudWatch User Guide: <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html>
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order003-aws-genai-service-landscape.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-029

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-029 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.1: Analyze requirements and design GenAI solutions. |
| `exam_skill` | Skill 1.1.1: Create comprehensive architectural designs that align with specific business needs and technical constraints (for example, by using appropriate FMs, integration patterns, deployment strategies). |
| `exam_skill_local` | Classify AWS services by role in a GenAI application |
| `learning_unit` | Day01-order003 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Declarative; Conceptual; Embedded |
| `question_format` | multiple-response |
| `difficulty` | hard |
| `cognitive_demand` | compare |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-21T020500Z-manual-codex-authored-day01-quality-top-up.md` item 10 |

Stem:

A company is drawing a Day 1 GenAI system map for a retrieval-augmented assistant. Which two components are correctly placed outside the foundation model itself? (Select TWO.)

Options:

A. A vector or document retrieval layer that selects grounding context.

B. An IAM role that grants the application permission to call required AWS APIs.

C. The model's learned parameters inside the managed model provider.

D. The model's token sampling process during generation.

E. The pretraining corpus originally used to build the foundation model.

Correct answer: A, B

Rationale: Retrieval and IAM permissions are application/platform components around the model, not the model internals.

Distractors: C: Model parameters are part of the model. D: Sampling is part of inference behavior. E: The pretraining corpus is not an application component the team places in the runtime architecture.

Misconception tags: `model-vs-application-confusion`, `service-role-confusion`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- AWS Bedrock User Guide: <https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html>
- AWS Lambda Developer Guide: <https://docs.aws.amazon.com/lambda/latest/dg/welcome.html>
- Amazon CloudWatch User Guide: <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html>
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order003-aws-genai-service-landscape.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-030

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-030 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.1: Analyze requirements and design GenAI solutions. |
| `exam_skill` | Skill 1.1.1: Create comprehensive architectural designs that align with specific business needs and technical constraints (for example, by using appropriate FMs, integration patterns, deployment strategies). |
| `exam_skill_local` | Classify AWS services by role in a GenAI application |
| `learning_unit` | Day01-order003 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Declarative; Conceptual; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-21T020500Z-manual-codex-authored-day01-quality-top-up.md` item 11 |

Stem:

An application team says their GenAI workload needs monitoring, but their diagram sends CloudWatch logs into the prompt as the primary control for model safety. What correction best clarifies the service role?

Options:

A. Use observability data to monitor and investigate the application, while safety controls and prompt/context design remain explicit application and Bedrock-layer concerns.

B. Use CloudWatch metrics as the only grounding source because metrics are more reliable than documents.

C. Remove application logging because model outputs are enough to reconstruct every failure.

D. Put IAM policies inside the model prompt so CloudWatch can enforce data access.

Correct answer: A

Rationale: CloudWatch supports observability and investigation; it does not replace safety controls, grounding design, or IAM enforcement.

Distractors: B: Metrics are not a general grounding source for user answers. C: Logging is necessary for operations and auditability. D: IAM policies are enforced by AWS, not by prompt text.

Misconception tags: `observability-as-safety-control`, `iam-in-prompt`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- AWS Bedrock User Guide: <https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html>
- AWS Lambda Developer Guide: <https://docs.aws.amazon.com/lambda/latest/dg/welcome.html>
- Amazon CloudWatch User Guide: <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html>
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order003-aws-genai-service-landscape.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-031

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-031 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 2: Implementation and Integration |
| `exam_task` | Task 2.5: Implement application integration patterns and development tools. |
| `exam_skill` | Skill 2.5.1: Create FM API interfaces to address the specific requirements of GenAI workloads (for example, by using API Gateway to handle streaming responses, token limit management, retry strategies to handle model timeouts). |
| `exam_skill_local` | Select synchronous, asynchronous, event-driven, or workflow patterns |
| `learning_unit` | Day01-order004 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Conceptual; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T230854Z-openai-gpt-4.1-day01-system-map.md` item 11 |

Stem:

An application exposes a serverless API that triggers GenAI model inference via Amazon Bedrock. Users report latency spikes and occasional function timeouts. Which architectural improvement best addresses both issues?

Options:

A. Move API processing to asynchronous workflow using AWS Step Functions

B. Increase Lambda memory allocation only

C. Switch from Bedrock to Amazon Lex

D. Increase API Gateway throttle limits

Correct answer: Move API processing to asynchronous workflow using AWS Step Functions

Rationale: Workflow orchestration reduces user-perceived latency spikes by decoupling triggering and inference, and shields API clients from model timeouts.

Distractors: Increase Lambda memory allocation only: While this may help compute-bound Lambda tasks, it won’t address Bedrock inference latency or timeout risks. Switch from Bedrock to Amazon Lex: Lex does not expose foundation models for general inference and would not address latency or API scope. Increase API Gateway throttle limits: Raising limits does not solve backend processing or inference latency bottlenecks.

Misconception tags: `serverless-latency-confusion`, `api-gateway-bottleneck-misunderstanding`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- AWS Step Functions Developer Guide: <https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html>
- Amazon SQS Developer Guide: <https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html>
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order004-application-integration-patterns.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-032

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-032 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 2: Implementation and Integration |
| `exam_task` | Task 2.5: Implement application integration patterns and development tools. |
| `exam_skill` | Skill 2.5.1: Create FM API interfaces to address the specific requirements of GenAI workloads (for example, by using API Gateway to handle streaming responses, token limit management, retry strategies to handle model timeouts). |
| `exam_skill_local` | Select synchronous, asynchronous, event-driven, or workflow patterns |
| `learning_unit` | Day01-order004 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Conceptual; Conditional |
| `question_format` | multiple-response |
| `difficulty` | medium |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T230854Z-openai-gpt-4.1-day01-system-map.md` item 12 |

Stem:

Which AWS services allow you to implement event-driven architectures for processing image uploads with GenAI capabilities? (Select TWO.)

Options:

A. Amazon S3

B. Amazon EventBridge

C. Amazon EC2

D. AWS IAM

E. AWS CodeBuild

Correct answer: Amazon S3, Amazon EventBridge

Rationale: S3 events can trigger Lambda or EventBridge, enabling event-driven flows for GenAI processing on image uploads.

Distractors: Amazon EC2: EC2 can host workloads but does not provide native event-driven triggers. AWS IAM: IAM is used for permissions, not eventing. AWS CodeBuild: CodeBuild is for CI/CD, not for event-based image processing workflows.

Misconception tags: `event-driven-vs-batch-confusion`, `iam-vs-event-source-confusion`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- AWS Step Functions Developer Guide: <https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html>
- Amazon SQS Developer Guide: <https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html>
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order004-application-integration-patterns.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-033

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-033 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 2: Implementation and Integration |
| `exam_task` | Task 2.5: Implement application integration patterns and development tools. |
| `exam_skill` | Skill 2.5.1: Create FM API interfaces to address the specific requirements of GenAI workloads (for example, by using API Gateway to handle streaming responses, token limit management, retry strategies to handle model timeouts). |
| `exam_skill_local` | Select synchronous, asynchronous, event-driven, or workflow patterns |
| `learning_unit` | Day01-order004 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Conceptual; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T230854Z-openai-gpt-4.1-day01-system-map.md` item 14 |

Stem:

You deploy a containerized GenAI inference app on Amazon ECS Fargate. At peak usage, some inference requests fail with 502 errors and no inference logs are written. What is the most likely issue?

Options:

A. Container tasks are being killed due to running out of memory

B. Bedrock API authentication failure

C. IAM role permissions are missing for log write

D. API Gateway integration is misconfigured

Correct answer: Container tasks are being killed due to running out of memory

Rationale: 502 errors with no logs indicate container crashes, commonly because the process is killed by OOM killer before it can log errors.

Distractors: Bedrock API authentication failure: Would result in 4xx errors returned from Bedrock, not container-level 502s. IAM role permissions are missing for log write: Missing log permissions would not crash the container, logs would not be written but inference would still run. API Gateway integration is misconfigured: Misconfiguration could lead to 4xx/5xx errors, but problem specifically points to no logs and process failure.

Misconception tags: `infrastructure-vs-api-issue`, `misunderstood-502-cause`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- AWS Step Functions Developer Guide: <https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html>
- Amazon SQS Developer Guide: <https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html>
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order004-application-integration-patterns.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-034

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-034 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 2: Implementation and Integration |
| `exam_task` | Task 2.5: Implement application integration patterns and development tools. |
| `exam_skill` | Skill 2.5.1: Create FM API interfaces to address the specific requirements of GenAI workloads (for example, by using API Gateway to handle streaming responses, token limit management, retry strategies to handle model timeouts). |
| `exam_skill_local` | Select synchronous, asynchronous, event-driven, or workflow patterns |
| `learning_unit` | Day01-order004 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Conceptual; Conditional |
| `question_format` | multiple-response |
| `difficulty` | medium |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T230854Z-openai-gpt-4.1-day01-system-map.md` item 15 |

Stem:

A GenAI workflow must run ad hoc, stateless inference jobs triggered by user requests. Which AWS service patterns can implement such serverless scale-out efficiently? (Select TWO.)

Options:

A. Amazon Lambda functions

B. Amazon ECS Fargate

C. Amazon Redshift

D. AWS Glue

E. AWS Direct Connect

Correct answer: Amazon Lambda functions, Amazon ECS Fargate

Rationale: Lambda and ECS Fargate both support serverless compute for stateless, on-demand workloads.

Distractors: Amazon Redshift: Redshift is a data warehouse, not for general compute or GenAI inference. AWS Glue: Glue is for ETL workloads, not ad hoc inference. AWS Direct Connect: Direct Connect is for network connectivity, not compute.

Misconception tags: `serverless-definition-confusion`, `compute-vs-data-service-confusion`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- AWS Step Functions Developer Guide: <https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html>
- Amazon SQS Developer Guide: <https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html>
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order004-application-integration-patterns.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-035

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-035 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 2: Implementation and Integration |
| `exam_task` | Task 2.5: Implement application integration patterns and development tools. |
| `exam_skill` | Skill 2.5.1: Create FM API interfaces to address the specific requirements of GenAI workloads (for example, by using API Gateway to handle streaming responses, token limit management, retry strategies to handle model timeouts). |
| `exam_skill_local` | Select synchronous, asynchronous, event-driven, or workflow patterns |
| `learning_unit` | Day01-order004 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Conceptual; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | compare |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T230854Z-openai-gpt-4.1-day01-system-map.md` item 16 |

Stem:

Which AWS service provides web-based APIs to expose serverless functions and can natively handle authentication and throttling?

Options:

A. Amazon API Gateway

B. Amazon AppFlow

C. Amazon Step Functions

D. Amazon S3

Correct answer: Amazon API Gateway

Rationale: API Gateway exposes REST and HTTP APIs, integrates with Lambda, and supports auth/throttling mechanisms.

Distractors: Amazon AppFlow: AppFlow is for ETL/data transfer workflows, not API presentation. Amazon Step Functions: Step Functions orchestrate workflows, but do not directly expose web APIs. Amazon S3: S3 does not provide web APIs over Lambda functions.

Misconception tags: `api-gateway-vs-orchestrator-confusion`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- AWS Step Functions Developer Guide: <https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html>
- Amazon SQS Developer Guide: <https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html>
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order004-application-integration-patterns.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-036

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-036 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 2: Implementation and Integration |
| `exam_task` | Task 2.5: Implement application integration patterns and development tools. |
| `exam_skill` | Skill 2.5.1: Create FM API interfaces to address the specific requirements of GenAI workloads (for example, by using API Gateway to handle streaming responses, token limit management, retry strategies to handle model timeouts). |
| `exam_skill_local` | Select synchronous, asynchronous, event-driven, or workflow patterns |
| `learning_unit` | Day01-order004 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Conceptual; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T230854Z-openai-gpt-4.1-day01-system-map.md` item 17 |

Stem:

Your GenAI job must run a sequence of data preprocessing, model inference, and postprocessing steps across different AWS services. Which pattern minimizes code complexity and operational overhead?

Options:

A. Model each step as a Lambda function and orchestrate with Step Functions

B. Develop a monolithic application in Amazon ECS

C. Write glue code to chain S3 event triggers only

D. Deploy all logic in a single, large Lambda function

Correct answer: Model each step as a Lambda function and orchestrate with Step Functions

Rationale: This pattern decomposes complexity, supports stepwise error handling and retries, and enables observability.

Distractors: Develop a monolithic application in Amazon ECS: Monoliths increase coupling and operational risk. Write glue code to chain S3 event triggers only: S3 events offer simple triggers but not robust sequencing or error handling. Deploy all logic in a single, large Lambda function: Large functions risk timeouts, difficulty debugging, and poor error visibility.

Misconception tags: `serverless-pitfalls`, `event-glue-vs-orchestration-confusion`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- AWS Step Functions Developer Guide: <https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html>
- Amazon SQS Developer Guide: <https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html>
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order004-application-integration-patterns.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-037

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-037 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 2: Implementation and Integration |
| `exam_task` | Task 2.5: Implement application integration patterns and development tools. |
| `exam_skill` | Skill 2.5.1: Create FM API interfaces to address the specific requirements of GenAI workloads (for example, by using API Gateway to handle streaming responses, token limit management, retry strategies to handle model timeouts). |
| `exam_skill_local` | Select synchronous, asynchronous, event-driven, or workflow patterns |
| `learning_unit` | Day01-order004 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Conceptual; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T230854Z-openai-gpt-4.1-day01-system-map.md` item 18 |

Stem:

A GenAI container app processes NLP requests in real-time and must scale to thousands of concurrent users. Which AWS pattern best supports seamless scaling and minimizes idle cost?

Options:

A. Deploy containers using Amazon ECS on AWS Fargate with auto-scaling policies

B. Run a cluster of large EC2 instances with custom autoscaling scripts

C. Use AWS Lambda directly for all NLP workloads

D. Schedule jobs via AWS Batch

Correct answer: Deploy containers using Amazon ECS on AWS Fargate with auto-scaling policies

Rationale: ECS Fargate allows serverless, scalable container deployment with auto-scaling, minimizing idle cost.

Distractors: Run a cluster of large EC2 instances with custom autoscaling scripts: More operationally complex and may incur higher idle cost. Use AWS Lambda directly for all NLP workloads: Lambdas have limitations for large model packaging and concurrency. Schedule jobs via AWS Batch: Batch is optimized for asynchronous, not real-time, workloads.

Misconception tags: `container-vs-serverless-confusion`, `batch-vs-realtime-error`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- AWS Step Functions Developer Guide: <https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html>
- Amazon SQS Developer Guide: <https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html>
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order004-application-integration-patterns.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-038

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-038 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 2: Implementation and Integration |
| `exam_task` | Task 2.5: Implement application integration patterns and development tools. |
| `exam_skill` | Skill 2.5.1: Create FM API interfaces to address the specific requirements of GenAI workloads (for example, by using API Gateway to handle streaming responses, token limit management, retry strategies to handle model timeouts). |
| `exam_skill_local` | Select synchronous, asynchronous, event-driven, or workflow patterns |
| `learning_unit` | Day01-order004 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Conceptual; Conditional |
| `question_format` | multiple-response |
| `difficulty` | medium |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T230854Z-openai-gpt-4.1-day01-system-map.md` item 19 |

Stem:

You need to expose an API endpoint for GenAI model inference, supporting both synchronous and long-running asynchronous jobs. Which AWS service patterns could support both? (Select TWO.)

Options:

A. Amazon API Gateway integrated with Step Functions

B. Amazon API Gateway with direct Lambda integration

C. Amazon CloudFront distribution with S3 backend

D. AWS Glue job triggers

E. AWS IAM policies

Correct answer: Amazon API Gateway integrated with Step Functions, Amazon API Gateway with direct Lambda integration

Rationale: API Gateway + Lambda supports synchronous, and API Gateway + Step Functions supports asynchronous jobs (client polls or is notified on completion).

Distractors: Amazon CloudFront distribution with S3 backend: CloudFront and S3 are for static content, not dynamic API or async orchestration. AWS Glue job triggers: Glue jobs are for ETL, not API-exposed GenAI inference. AWS IAM policies: IAM controls permissions but does not expose APIs or manage jobs.

Misconception tags: `api-gateway-pattern-confusion`, `iam-vs-api-endpoint`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- AWS Step Functions Developer Guide: <https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html>
- Amazon SQS Developer Guide: <https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html>
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order004-application-integration-patterns.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-039

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-039 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 2: Implementation and Integration |
| `exam_task` | Task 2.5: Implement application integration patterns and development tools. |
| `exam_skill` | Skill 2.5.1: Create FM API interfaces to address the specific requirements of GenAI workloads (for example, by using API Gateway to handle streaming responses, token limit management, retry strategies to handle model timeouts). |
| `exam_skill_local` | Select synchronous, asynchronous, event-driven, or workflow patterns |
| `learning_unit` | Day01-order004 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Conceptual; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T230854Z-openai-gpt-4.1-day01-system-map.md` item 20 |

Stem:

An organization wants to minimize operational toil, allow developers to focus on code, and enable fast scaling for bursty GenAI inference workloads. Which AWS architecture best fulfills these goals?

Options:

A. Build microservices using AWS Lambda and Amazon API Gateway

B. Host all logic in a managed Kubernetes cluster (EKS)

C. Run inference workloads on reserved EC2 instances

D. Set up workflow orchestration in Amazon ECS with custom scripts

Correct answer: Build microservices using AWS Lambda and Amazon API Gateway

Rationale: Lambda and API Gateway minimize operations, automatically scale to demand, and reduce waste by billing for actual usage.

Distractors: Host all logic in a managed Kubernetes cluster (EKS): Kubernetes offers flexibility but requires significant operational expertise and overhead. Run inference workloads on reserved EC2 instances: Reserved EC2 instances can waste resources during idle periods. Set up workflow orchestration in Amazon ECS with custom scripts: This pattern may introduce unnecessary complexity for bursty workloads.

Misconception tags: `kubernetes-vs-serverless`, `ec2-always-optimal`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- AWS Step Functions Developer Guide: <https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html>
- Amazon SQS Developer Guide: <https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html>
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order004-application-integration-patterns.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-040

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-040 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 2: Implementation and Integration |
| `exam_task` | Task 2.5: Implement application integration patterns and development tools. |
| `exam_skill` | Skill 2.5.1: Create FM API interfaces to address the specific requirements of GenAI workloads (for example, by using API Gateway to handle streaming responses, token limit management, retry strategies to handle model timeouts). |
| `exam_skill_local` | Select synchronous, asynchronous, event-driven, or workflow patterns |
| `learning_unit` | Day01-order004 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Conceptual; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-21T020500Z-manual-codex-authored-day01-quality-top-up.md` item 12 |

Stem:

A team is building a GenAI document-analysis feature where a user uploads a file, the system extracts text, invokes a model, stores results, and notifies the user minutes later. Which integration pattern best fits the end-to-end workflow?

Options:

A. Asynchronous event-driven processing with a queue or workflow orchestrator coordinating the long-running steps.

B. A single synchronous browser request that blocks until every document page has been analyzed.

C. A static website call directly to the model endpoint using the user's browser credentials.

D. A scheduled batch job that ignores the upload event and scans the bucket once per month.

Correct answer: A

Rationale: Long-running multi-step processing after an upload fits asynchronous event-driven or workflow orchestration patterns.

Distractors: B: Blocking a browser request is brittle for long-running work. C: Direct browser-to-model calls create credential and control problems. D: Monthly scanning fails the user-triggered workflow requirement.

Misconception tags: `sync-for-everything`, `client-direct-model-call`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- AWS Step Functions Developer Guide: <https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html>
- Amazon SQS Developer Guide: <https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html>
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order004-application-integration-patterns.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-041

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-041 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 3: AI Safety, Security, and Governance |
| `exam_task` | Task 3.2: Implement data security and privacy controls. |
| `exam_skill` | Skill 3.2.1: Develop protected AI environments to ensure comprehensive security for FM deployments (for example, by using VPC endpoints to isolate networks, IAM policies to enforce secure data access patterns, AWS Lake Formation to provide granular data access, CloudWatch to monitor data access). |
| `exam_skill_local` | Place IAM, data-protection, logging, and retrieval controls |
| `learning_unit` | Day01-order005 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Conceptual; Conditional; Normative |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | judge |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T230854Z-openai-gpt-4.1-day01-system-map.md` item 21 |

Stem:

You are designing a GenAI workflow where an API Gateway triggers a Lambda function, which in turn invokes Amazon Bedrock. What is the most secure way to grant the Lambda function access to Bedrock APIs?

Options:

A. Attach a minimal IAM role to the Lambda granting only required Bedrock permissions

B. Add Bedrock permissions to the API Gateway execution role

C. Attach 'AmazonBedrockFullAccess' to all developers

D. Use root credentials in the Lambda function's environment variables

Correct answer: Attach a minimal IAM role to the Lambda granting only required Bedrock permissions

Rationale: Least privilege principle dictates scoping permissions tightly and to the execution context (Lambda's role), not to users or unrelated principals.

Distractors: Add Bedrock permissions to the API Gateway execution role: API Gateway does not invoke Bedrock directly. Attach 'AmazonBedrockFullAccess' to all developers: Gives excessive privilege and violates least privilege. Use root credentials in the Lambda function's environment variables: Root credentials should never be used in applications.

Misconception tags: `least-privilege-violation`, `role-assignment-error`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- AWS IAM User Guide: <https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html>
- AWS Bedrock Guardrails documentation: <https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html>
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order005-trust-boundaries-iam-data-protection.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-042

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-042 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 3: AI Safety, Security, and Governance |
| `exam_task` | Task 3.2: Implement data security and privacy controls. |
| `exam_skill` | Skill 3.2.1: Develop protected AI environments to ensure comprehensive security for FM deployments (for example, by using VPC endpoints to isolate networks, IAM policies to enforce secure data access patterns, AWS Lake Formation to provide granular data access, CloudWatch to monitor data access). |
| `exam_skill_local` | Place IAM, data-protection, logging, and retrieval controls |
| `learning_unit` | Day01-order005 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Conceptual; Conditional; Normative |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T230854Z-openai-gpt-4.1-day01-system-map.md` item 22 |

Stem:

A GenAI batch inference job running in Amazon SageMaker needs access to training data stored in an encrypted S3 bucket. Data owners require strict access controls and auditability. What configuration maximizes security and compliance?

Options:

A. Grant SageMaker execution role least privilege access via a resource policy and enable S3 access logging

B. Use public bucket ACLs for S3, but encrypt objects

C. Provide SageMaker with administrator access

D. Store unencrypted data in a private bucket

Correct answer: Grant SageMaker execution role least privilege access via a resource policy and enable S3 access logging

Rationale: Least privilege, resource policies, and audit logging combine to control and trace access to sensitive data.

Distractors: Use public bucket ACLs for S3, but encrypt objects: Public access violates security best practice, even if data is encrypted. Provide SageMaker with administrator access: Admin access is excessive and does not support compliance. Store unencrypted data in a private bucket: Data must be encrypted to meet security and compliance needs.

Misconception tags: `public-vs-private-access`, `encryption-alone-is-enough`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- AWS IAM User Guide: <https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html>
- AWS Bedrock Guardrails documentation: <https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html>
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order005-trust-boundaries-iam-data-protection.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-043

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-043 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 3: AI Safety, Security, and Governance |
| `exam_task` | Task 3.2: Implement data security and privacy controls. |
| `exam_skill` | Skill 3.2.1: Develop protected AI environments to ensure comprehensive security for FM deployments (for example, by using VPC endpoints to isolate networks, IAM policies to enforce secure data access patterns, AWS Lake Formation to provide granular data access, CloudWatch to monitor data access). |
| `exam_skill_local` | Place IAM, data-protection, logging, and retrieval controls |
| `learning_unit` | Day01-order005 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Conceptual; Conditional; Normative |
| `question_format` | multiple-response |
| `difficulty` | medium |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T230854Z-openai-gpt-4.1-day01-system-map.md` item 23 |

Stem:

A GenAI API hosted on AWS must restrict access to only approved internal IP ranges. Which mechanisms can enforce this? (Select TWO.)

Options:

A. API Gateway resource policies with IP whitelisting

B. VPC endpoint policies

C. S3 bucket lifecycle policies

D. IAM user access keys

E. Enable public access on the API

Correct answer: API Gateway resource policies with IP whitelisting, VPC endpoint policies

Rationale: API Gateway policies and VPC endpoint policies are designed to enforce network-layer access controls.

Distractors: S3 bucket lifecycle policies: Lifecycle rules control object expiry, not access. IAM user access keys: Keys enable IAM-user auth but do not limit by source IP. Enable public access on the API: This contradicts the restriction intent.

Misconception tags: `policy-vs-access-key-confusion`, `network-vs-identity-controls`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- AWS IAM User Guide: <https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html>
- AWS Bedrock Guardrails documentation: <https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html>
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order005-trust-boundaries-iam-data-protection.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-044

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-044 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 3: AI Safety, Security, and Governance |
| `exam_task` | Task 3.2: Implement data security and privacy controls. |
| `exam_skill` | Skill 3.2.1: Develop protected AI environments to ensure comprehensive security for FM deployments (for example, by using VPC endpoints to isolate networks, IAM policies to enforce secure data access patterns, AWS Lake Formation to provide granular data access, CloudWatch to monitor data access). |
| `exam_skill_local` | Place IAM, data-protection, logging, and retrieval controls |
| `learning_unit` | Day01-order005 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Conceptual; Conditional; Normative |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | judge |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T230854Z-openai-gpt-4.1-day01-system-map.md` item 24 |

Stem:

A developer accidentally grants full S3 access to an IAM role used by a GenAI application. What is the recommended best practice?

Options:

A. Restrict the IAM role to least privilege required for only the relevant S3 resources

B. Do nothing if no production data is affected

C. Use CloudTrail to hide the permission grant from audit logs

D. Share the IAM role with other teams for reuse

Correct answer: Restrict the IAM role to least privilege required for only the relevant S3 resources

Rationale: Best practice is the principle of least privilege: remove excess permissions and scope only to resources needed.

Distractors: Do nothing if no production data is affected: Leaving excessive permissions risks future misuse or breach. Use CloudTrail to hide the permission grant from audit logs: CloudTrail audit logs must not be tampered with. Share the IAM role with other teams for reuse: Roles should not be shared indiscriminately; this risks privilege escalation.

Misconception tags: `least-privilege-violation`, `audit-misuse`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- AWS IAM User Guide: <https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html>
- AWS Bedrock Guardrails documentation: <https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html>
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order005-trust-boundaries-iam-data-protection.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-045

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-045 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 3: AI Safety, Security, and Governance |
| `exam_task` | Task 3.2: Implement data security and privacy controls. |
| `exam_skill` | Skill 3.2.1: Develop protected AI environments to ensure comprehensive security for FM deployments (for example, by using VPC endpoints to isolate networks, IAM policies to enforce secure data access patterns, AWS Lake Formation to provide granular data access, CloudWatch to monitor data access). |
| `exam_skill_local` | Place IAM, data-protection, logging, and retrieval controls |
| `learning_unit` | Day01-order005 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Conceptual; Conditional; Normative |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | judge |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T230854Z-openai-gpt-4.1-day01-system-map.md` item 25 |

Stem:

A GenAI pipeline stores user-uploaded documents in an S3 bucket for model ingestion. To minimize risk of data exfiltration, which configuration change offers the strongest control?

Options:

A. Restrict bucket access to VPC endpoints and enforce encryption in transit and at rest

B. Use public-read ACL on the bucket

C. Allow all AWS principals read-only access

D. Disable S3 bucket versioning

Correct answer: Restrict bucket access to VPC endpoints and enforce encryption in transit and at rest

Rationale: Limiting access to the VPC, and enforcing encryption, minimizes attack surface and exfiltration risk.

Distractors: Use public-read ACL on the bucket: Public access is the opposite of secure. Allow all AWS principals read-only access: This still allows many entities unnecessary access. Disable S3 bucket versioning: Versioning is unrelated to access controls or exfiltration risk.

Misconception tags: `public-vs-private-acls`, `bucket-versioning-confusion`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- AWS IAM User Guide: <https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html>
- AWS Bedrock Guardrails documentation: <https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html>
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order005-trust-boundaries-iam-data-protection.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-046

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-046 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 3: AI Safety, Security, and Governance |
| `exam_task` | Task 3.2: Implement data security and privacy controls. |
| `exam_skill` | Skill 3.2.1: Develop protected AI environments to ensure comprehensive security for FM deployments (for example, by using VPC endpoints to isolate networks, IAM policies to enforce secure data access patterns, AWS Lake Formation to provide granular data access, CloudWatch to monitor data access). |
| `exam_skill_local` | Place IAM, data-protection, logging, and retrieval controls |
| `learning_unit` | Day01-order005 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Conceptual; Conditional; Normative |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | judge |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T230854Z-openai-gpt-4.1-day01-system-map.md` item 27 |

Stem:

What is a key reason to separate IAM roles for GenAI inference services from roles for data ingestion or preprocessing?

Options:

A. Each role should have only the minimum needed permissions for its purpose, reducing blast radius

B. It reduces CloudWatch logging charges

C. Shared roles increase authentication speed

D. Separation is only important for billing

Correct answer: Each role should have only the minimum needed permissions for its purpose, reducing blast radius

Rationale: Separation of roles is fundamental to enforcing least privilege and minimizing compromise scope.

Distractors: It reduces CloudWatch logging charges: Role separation doesn't impact logging costs. Shared roles increase authentication speed: Sharing roles could increase risk, not improve speed. Separation is only important for billing: It's primarily important for security, not billing.

Misconception tags: `least-privilege-importance`, `role-sharing-misconception`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- AWS IAM User Guide: <https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html>
- AWS Bedrock Guardrails documentation: <https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html>
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order005-trust-boundaries-iam-data-protection.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-047

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-047 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 3: AI Safety, Security, and Governance |
| `exam_task` | Task 3.2: Implement data security and privacy controls. |
| `exam_skill` | Skill 3.2.1: Develop protected AI environments to ensure comprehensive security for FM deployments (for example, by using VPC endpoints to isolate networks, IAM policies to enforce secure data access patterns, AWS Lake Formation to provide granular data access, CloudWatch to monitor data access). |
| `exam_skill_local` | Place IAM, data-protection, logging, and retrieval controls |
| `learning_unit` | Day01-order005 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Conceptual; Conditional; Normative |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T230854Z-openai-gpt-4.1-day01-system-map.md` item 28 |

Stem:

A vendor-supplied GenAI service must ingest sensitive data from your AWS environment. What is a secure pattern to establish a trust boundary?

Options:

A. Expose only the necessary APIs to the vendor and use explicit allow-list IAM resource policies

B. Give the vendor access to all S3 buckets via cross-account IAM trust

C. Provide public API endpoints with no authentication

D. Allow vendor’s root user to access the AWS account directly

Correct answer: Expose only the necessary APIs to the vendor and use explicit allow-list IAM resource policies

Rationale: Minimal exposure and explicit allow-listing reduces risk; cross-account trust must also be precisely scoped.

Distractors: Give the vendor access to all S3 buckets via cross-account IAM trust: Too broad and unsafe. Provide public API endpoints with no authentication: This is highly insecure. Allow vendor’s root user to access the AWS account directly: Never provide root access to anyone external.

Misconception tags: `cross-account-risk`, `unrestricted-interface-misconception`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- AWS IAM User Guide: <https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html>
- AWS Bedrock Guardrails documentation: <https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html>
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order005-trust-boundaries-iam-data-protection.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-048

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-048 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 3: AI Safety, Security, and Governance |
| `exam_task` | Task 3.2: Implement data security and privacy controls. |
| `exam_skill` | Skill 3.2.1: Develop protected AI environments to ensure comprehensive security for FM deployments (for example, by using VPC endpoints to isolate networks, IAM policies to enforce secure data access patterns, AWS Lake Formation to provide granular data access, CloudWatch to monitor data access). |
| `exam_skill_local` | Place IAM, data-protection, logging, and retrieval controls |
| `learning_unit` | Day01-order005 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Conceptual; Conditional; Normative |
| `question_format` | multiple-response |
| `difficulty` | medium |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T230854Z-openai-gpt-4.1-day01-system-map.md` item 29 |

Stem:

Which AWS features help trace data flow for a GenAI application to support incident response and auditing? (Select TWO.)

Options:

A. AWS CloudTrail data event logging

B. Amazon S3 access logs

C. Amazon Polly speech rate controls

D. IAM instance profiles

E. Amazon Forecast job tuning

Correct answer: AWS CloudTrail data event logging, Amazon S3 access logs

Rationale: CloudTrail and S3 access logging give visibility into API/data access for investigation and audit.

Distractors: Amazon Polly speech rate controls: Polly feature not relevant to auditing. IAM instance profiles: Provide credentials, not audit/logging. Amazon Forecast job tuning: Forecast is unrelated to audit trails.

Misconception tags: `audit-vs-access-control`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- AWS IAM User Guide: <https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html>
- AWS Bedrock Guardrails documentation: <https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html>
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order005-trust-boundaries-iam-data-protection.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-049

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-049 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 3: AI Safety, Security, and Governance |
| `exam_task` | Task 3.2: Implement data security and privacy controls. |
| `exam_skill` | Skill 3.2.1: Develop protected AI environments to ensure comprehensive security for FM deployments (for example, by using VPC endpoints to isolate networks, IAM policies to enforce secure data access patterns, AWS Lake Formation to provide granular data access, CloudWatch to monitor data access). |
| `exam_skill_local` | Place IAM, data-protection, logging, and retrieval controls |
| `learning_unit` | Day01-order005 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Conceptual; Conditional; Normative |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | judge |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-21T020500Z-manual-codex-authored-day01-quality-top-up.md` item 13 |

Stem:

A regulated team is designing a GenAI assistant that retrieves internal HR documents. The first design gives the model invocation role broad read access to every HR bucket because the prompt promises to ignore restricted records. What is the best review finding?

Options:

A. The design violates least privilege because access controls must be enforced by IAM and retrieval filtering, not only by prompt instructions.

B. The design is acceptable because the model can decide which records the user should see.

C. The design only needs a higher temperature so restricted documents are less likely to be repeated.

D. The design should remove logging to reduce the chance of sensitive data appearing in audit trails.

Correct answer: A

Rationale: Least privilege and retrieval authorization must be enforced outside the prompt using IAM, data access controls, and filtering.

Distractors: B: The model should not be trusted as the authorization boundary. C: Sampling settings do not enforce data access. D: Logging needs careful handling, not removal as a security strategy.

Misconception tags: `prompt-as-access-control`, `security-afterthought`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- AWS IAM User Guide: <https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html>
- AWS Bedrock Guardrails documentation: <https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html>
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order005-trust-boundaries-iam-data-protection.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-050

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-050 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 3: AI Safety, Security, and Governance |
| `exam_task` | Task 3.2: Implement data security and privacy controls. |
| `exam_skill` | Skill 3.2.1: Develop protected AI environments to ensure comprehensive security for FM deployments (for example, by using VPC endpoints to isolate networks, IAM policies to enforce secure data access patterns, AWS Lake Formation to provide granular data access, CloudWatch to monitor data access). |
| `exam_skill_local` | Place IAM, data-protection, logging, and retrieval controls |
| `learning_unit` | Day01-order005 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Conceptual; Conditional; Normative |
| `question_format` | multiple-response |
| `difficulty` | exam-plus |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-21T020500Z-manual-codex-authored-day01-quality-top-up.md` item 14 |

Stem:

A company is preparing a baseline security review for a new Bedrock-backed application that handles confidential customer text. Which two controls belong in the initial trust-boundary design? (Select TWO.)

Options:

A. Grant the application role only the model invocation and data access permissions needed for its workflow.

B. Log model requests and responses according to the organization's sensitive-data handling policy.

C. Let users pass arbitrary AWS role ARNs in prompts so the model can choose its own permissions.

D. Use one shared administrator role for development, test, and production model access.

E. Disable all output checks because IAM already controls every model response.

Correct answer: A, B

Rationale: Least-privilege roles and policy-aligned observability are basic trust-boundary controls for a confidential GenAI workload.

Distractors: C: Prompts must not select AWS permissions. D: Shared administrator roles violate least privilege and environment separation. E: IAM does not validate model-output content.

Misconception tags: `iam-in-prompt`, `iam-solves-output-safety`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- AWS IAM User Guide: <https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html>
- AWS Bedrock Guardrails documentation: <https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html>
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order005-trust-boundaries-iam-data-protection.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-051

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-051 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.1: Analyze requirements and design GenAI solutions. |
| `exam_skill` | Skill 1.1.1: Create comprehensive architectural designs that align with specific business needs and technical constraints (for example, by using appropriate FMs, integration patterns, deployment strategies). |
| `exam_skill_local` | Convert requirements into a basic GenAI architecture |
| `learning_unit` | Day01-order006 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Conceptual; Conditional; Strategic |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T230854Z-openai-gpt-4.1-day01-system-map.md` item 30 |

Stem:

Your business stakeholder requests a GenAI document summarization tool with high accuracy and the ability for human review before results are published. Which architectural pattern best meets this requirement?

Options:

A. Integrate Amazon Bedrock for summarization with a Step Functions workflow and Amazon Simple Queue Service (SQS) for human review loop

B. Call Bedrock inference directly in a synchronous REST API

C. Batch process with AWS Glue and deliver results to S3 only

D. Use Amazon Kendra to automatically summarize and publish results

Correct answer: Integrate Amazon Bedrock for summarization with a Step Functions workflow and Amazon Simple Queue Service (SQS) for human review loop

Rationale: This pattern enables GenAI inference followed by a human-in-the-loop review and approval step before publishing.

Distractors: Call Bedrock inference directly in a synchronous REST API: No human review possible in a synchronous-only flow. Batch process with AWS Glue and deliver results to S3 only: Glue is for ETL, not GenAI summarization or human review. Use Amazon Kendra to automatically summarize and publish results: Kendra is enterprise search, not summarization, and cannot implement human review.

Misconception tags: `human-in-the-loop-lack`, `etl-vs-ai-confusion`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- AWS Well-Architected Framework: <https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html>
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order006-requirements-basic-solution-architecture.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-052

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-052 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.1: Analyze requirements and design GenAI solutions. |
| `exam_skill` | Skill 1.1.1: Create comprehensive architectural designs that align with specific business needs and technical constraints (for example, by using appropriate FMs, integration patterns, deployment strategies). |
| `exam_skill_local` | Convert requirements into a basic GenAI architecture |
| `learning_unit` | Day01-order006 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Conceptual; Conditional; Strategic |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | judge |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T230854Z-openai-gpt-4.1-day01-system-map.md` item 32 |

Stem:

A customer asks for a GenAI application that answers questions about internal documentation. The dataset is highly sensitive and must remain in their VPC. What high-level AWS architecture should you suggest?

Options:

A. Private S3 bucket, foundation model hosting in SageMaker inside a VPC, and vector search using Amazon OpenSearch with VPC endpoints

B. Amazon Bedrock with public endpoints and data sync from S3

C. OpenAI API with direct VPN integration

D. Publicly accessible S3 with Bedrock managed inference

Correct answer: Private S3 bucket, foundation model hosting in SageMaker inside a VPC, and vector search using Amazon OpenSearch with VPC endpoints

Rationale: This design avoids public endpoint exposure and keeps all data flows within the customer's VPC.

Distractors: Amazon Bedrock with public endpoints and data sync from S3: Bedrock public endpoints may not meet strict VPC/data residency requirements. OpenAI API with direct VPN integration: Third-party API increases data movement risk. Publicly accessible S3 with Bedrock managed inference: Public S3 buckets expose sensitive internal data.

Misconception tags: `vpc-vs-public-access-confusion`, `bedrock-vpc-capability-assumption`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- AWS Well-Architected Framework: <https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html>
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order006-requirements-basic-solution-architecture.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-053

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-053 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.1: Analyze requirements and design GenAI solutions. |
| `exam_skill` | Skill 1.1.1: Create comprehensive architectural designs that align with specific business needs and technical constraints (for example, by using appropriate FMs, integration patterns, deployment strategies). |
| `exam_skill_local` | Convert requirements into a basic GenAI architecture |
| `learning_unit` | Day01-order006 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Conceptual; Conditional; Strategic |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | judge |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T230854Z-openai-gpt-4.1-day01-system-map.md` item 33 |

Stem:

Which GenAI solution pattern minimizes cost for low-frequency, unpredictable inference requests via API?

Options:

A. Serverless approach using API Gateway and Lambda to trigger on-demand inference

B. Always-on EC2 cluster with pre-provisioned models

C. Multi-AZ ECS deployment with reserved capacity

D. Daily scheduled SageMaker batch endpoints

Correct answer: Serverless approach using API Gateway and Lambda to trigger on-demand inference

Rationale: Serverless patterns bill only for usage, reducing idle cost for low-frequency workloads.

Distractors: Always-on EC2 cluster with pre-provisioned models: Incurs high idle/standby cost. Multi-AZ ECS deployment with reserved capacity: Reserved capacity is cost-inefficient for unpredictable workloads. Daily scheduled SageMaker batch endpoints: Batch endpoints are for large, scheduled batches, not ad hoc API calls.

Misconception tags: `always-on-vs-serverless`, `batch-vs-event-driven-confusion`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- AWS Well-Architected Framework: <https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html>
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order006-requirements-basic-solution-architecture.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-054

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-054 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.1: Analyze requirements and design GenAI solutions. |
| `exam_skill` | Skill 1.1.1: Create comprehensive architectural designs that align with specific business needs and technical constraints (for example, by using appropriate FMs, integration patterns, deployment strategies). |
| `exam_skill_local` | Convert requirements into a basic GenAI architecture |
| `learning_unit` | Day01-order006 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Conceptual; Conditional; Strategic |
| `question_format` | multiple-response |
| `difficulty` | medium |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T230854Z-openai-gpt-4.1-day01-system-map.md` item 34 |

Stem:

Which are best practices for architecting GenAI APIs for production use on AWS? (Select TWO.)

Options:

A. Implement authentication and authorization for all API endpoints

B. Enforce usage quotas and rate limits

C. Use public S3 buckets for model outputs

D. Deploy all logic in a single, monolithic EC2 instance

E. Log all prompts and responses to a world-readable SNS topic

Correct answer: Implement authentication and authorization for all API endpoints, Enforce usage quotas and rate limits

Rationale: Access controls and rate limiting protect APIs from abuse, and these are standard GenAI API best practices.

Distractors: Use public S3 buckets for model outputs: Exposes sensitive data to the public. Deploy all logic in a single, monolithic EC2 instance: Monoliths are less resilient/scalable/maintainable. Log all prompts and responses to a world-readable SNS topic: Violates data privacy.

Misconception tags: `public-data-misuse`, `monolith-preference`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- AWS Well-Architected Framework: <https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html>
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order006-requirements-basic-solution-architecture.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-055

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-055 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.1: Analyze requirements and design GenAI solutions. |
| `exam_skill` | Skill 1.1.1: Create comprehensive architectural designs that align with specific business needs and technical constraints (for example, by using appropriate FMs, integration patterns, deployment strategies). |
| `exam_skill_local` | Convert requirements into a basic GenAI architecture |
| `learning_unit` | Day01-order006 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Conceptual; Conditional; Strategic |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T230854Z-openai-gpt-4.1-day01-system-map.md` item 35 |

Stem:

Which architectural choice best reduces the blast radius of a misconfigured GenAI model that produces harmful or offensive content in a multi-tenant application?

Options:

A. Implement output validation and content moderation before delivering results to end-users

B. Expose model inference output directly to clients

C. Allow all tenants to invoke the same model endpoint

D. Disable logging of model outputs

Correct answer: Implement output validation and content moderation before delivering results to end-users

Rationale: Moderation and validation prevent propagation of problematic outputs to the wider user base.

Distractors: Expose model inference output directly to clients: Risks harmful content reaching users. Allow all tenants to invoke the same model endpoint: Multi-tenant shared endpoints may increase risk. Disable logging of model outputs: Disables observability and audit.

Misconception tags: `moderation-importance`, `output-pass-through-error`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- AWS Well-Architected Framework: <https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html>
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order006-requirements-basic-solution-architecture.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-056

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-056 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.1: Analyze requirements and design GenAI solutions. |
| `exam_skill` | Skill 1.1.1: Create comprehensive architectural designs that align with specific business needs and technical constraints (for example, by using appropriate FMs, integration patterns, deployment strategies). |
| `exam_skill_local` | Convert requirements into a basic GenAI architecture |
| `learning_unit` | Day01-order006 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Conceptual; Conditional; Strategic |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T230854Z-openai-gpt-4.1-day01-system-map.md` item 36 |

Stem:

A GenAI-powered FAQ assistant is experiencing inaccurate and hallucinated responses shortly after launch on real user data. No retraining is possible due to time constraints. What solution pattern most directly addresses this risk?

Options:

A. Implement retrieval-augmented generation using a custom document index via OpenSearch

B. Switch to a more powerful foundation model immediately

C. Increase the API rate limits for users

D. Enable S3 object versioning on the FAQ data

Correct answer: Implement retrieval-augmented generation using a custom document index via OpenSearch

Rationale: RAG enables the model to reference accurate context from up-to-date data, reducing hallucinations.

Distractors: Switch to a more powerful foundation model immediately: Model size doesn't guarantee up-to-date or more accurate knowledge. Increase the API rate limits for users: Does not affect accuracy. Enable S3 object versioning on the FAQ data: Versioning assists rollback, not model accuracy.

Misconception tags: `model-size-fixation`, `rag-vs-training-confusion`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- AWS Well-Architected Framework: <https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html>
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order006-requirements-basic-solution-architecture.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-057

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-057 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.1: Analyze requirements and design GenAI solutions. |
| `exam_skill` | Skill 1.1.1: Create comprehensive architectural designs that align with specific business needs and technical constraints (for example, by using appropriate FMs, integration patterns, deployment strategies). |
| `exam_skill_local` | Convert requirements into a basic GenAI architecture |
| `learning_unit` | Day01-order006 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Conceptual; Conditional; Strategic |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T230854Z-openai-gpt-4.1-day01-system-map.md` item 37 |

Stem:

You are tasked with creating a GenAI transcription service for multilingual documents, requiring on-demand scaling and support for secure, auditable access to results. Which AWS services and architectural pattern best meet these needs?

Options:

A. Serverless pipeline using S3 triggers, Lambda, and Step Functions, with IAM-based access and CloudTrail auditing

B. Batch processing on large EC2 instances, with access logs written to local disk

C. Self-hosted LLM inferencing on a Kubernetes cluster

D. Direct access from client apps to Bedrock with S3 public buckets for result storage

Correct answer: Serverless pipeline using S3 triggers, Lambda, and Step Functions, with IAM-based access and CloudTrail auditing

Rationale: This serverless architecture supports on-demand scaling, and IAM plus CloudTrail provides security and audit.

Distractors: Batch processing on large EC2 instances, with access logs written to local disk: Not scalable or auditable by default. Self-hosted LLM inferencing on a Kubernetes cluster: Higher operational burden. Direct access from client apps to Bedrock with S3 public buckets for result storage: Public buckets expose sensitive data.

Misconception tags: `serverless-benefits`, `auditability-neglect`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- AWS Well-Architected Framework: <https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html>
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order006-requirements-basic-solution-architecture.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-058

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-058 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.1: Analyze requirements and design GenAI solutions. |
| `exam_skill` | Skill 1.1.1: Create comprehensive architectural designs that align with specific business needs and technical constraints (for example, by using appropriate FMs, integration patterns, deployment strategies). |
| `exam_skill_local` | Convert requirements into a basic GenAI architecture |
| `learning_unit` | Day01-order006 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Conceptual; Conditional; Strategic |
| `question_format` | multiple-response |
| `difficulty` | medium |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T230854Z-openai-gpt-4.1-day01-system-map.md` item 38 |

Stem:

In AWS GenAI solutions, which practices should be followed to maintain clear trust boundaries between system components? (Select TWO.)

Options:

A. Implement IAM roles scoped to individual services/functions

B. Use network segmentation and private VPC endpoints

C. Hardcode IAM credentials into application code

D. Allow all AWS services full cross-account access

E. Deploy all components in a single, public subnet

Correct answer: Implement IAM roles scoped to individual services/functions, Use network segmentation and private VPC endpoints

Rationale: Service-scoped IAM and network segmentation both help maintain and enforce trust boundaries.

Distractors: Hardcode IAM credentials into application code: Never secure; violates trust boundary. Allow all AWS services full cross-account access: Too permissive; breaks boundaries. Deploy all components in a single, public subnet: Removes network isolation.

Misconception tags: `trust-boundary-importance`, `credential-handling`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- AWS Well-Architected Framework: <https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html>
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order006-requirements-basic-solution-architecture.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-059

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-059 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.1: Analyze requirements and design GenAI solutions. |
| `exam_skill` | Skill 1.1.1: Create comprehensive architectural designs that align with specific business needs and technical constraints (for example, by using appropriate FMs, integration patterns, deployment strategies). |
| `exam_skill_local` | Convert requirements into a basic GenAI architecture |
| `learning_unit` | Day01-order006 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Conceptual; Conditional; Strategic |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-21T020500Z-manual-codex-authored-day01-quality-top-up.md` item 15 |

Stem:

A business sponsor asks for a GenAI assistant for field technicians. Requirements include offline capture, later synchronization, retrieval from repair manuals, and human approval before warranty decisions. Which architecture decision best reflects those requirements?

Options:

A. Separate capture/sync, retrieval grounding, model assistance, and human approval into distinct components with explicit control points.

B. Send technician notes directly to a model and automatically approve warranty claims from the response.

C. Train a new foundation model so offline capture and approval workflow are unnecessary.

D. Use only a prompt template because retrieval and workflow controls are implementation details that can wait.

Correct answer: A

Rationale: The architecture should translate requirements into components and controls: data capture, retrieval, inference, and approval workflow.

Distractors: B: Automatic approval violates the human-approval requirement. C: Training a model does not remove application workflow needs. D: Retrieval and workflow controls are core requirements, not optional details.

Misconception tags: `requirements-to-architecture-gap`, `model-replaces-workflow`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- AWS Well-Architected Framework: <https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html>
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order006-requirements-basic-solution-architecture.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-060

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-060 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.1: Analyze requirements and design GenAI solutions. |
| `exam_skill` | Skill 1.1.1: Create comprehensive architectural designs that align with specific business needs and technical constraints (for example, by using appropriate FMs, integration patterns, deployment strategies). |
| `exam_skill_local` | Convert requirements into a basic GenAI architecture |
| `learning_unit` | Day01-order006 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Conceptual; Conditional; Strategic |
| `question_format` | multiple-response |
| `difficulty` | exam-plus |
| `cognitive_demand` | judge |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-21T020500Z-manual-codex-authored-day01-quality-top-up.md` item 16 |

Stem:

A team is reviewing requirements for a GenAI claims triage system. Which two requirements most directly affect the first architecture sketch rather than only the final prompt wording? (Select TWO.)

Options:

A. Claims with low confidence must route to a human reviewer before customer notification.

B. The system must retrieve policy and claim history from approved internal sources before model invocation.

C. The assistant should use a friendly tone in its customer-facing explanation.

D. The response should avoid contractions when writing status summaries.

E. The prompt should call the model a claims expert.

Correct answer: A, B

Rationale: Human routing and retrieval from approved systems define components, data flows, and control placement in the architecture.

Distractors: C: Tone matters, but it is primarily prompt/output guidance. D: Style constraints are prompt-level details. E: Role framing is a prompt tactic, not a system architecture requirement.

Misconception tags: `prompt-vs-architecture`, `human-review-omitted`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- AWS Well-Architected Framework: <https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html>
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order006-requirements-basic-solution-architecture.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-061

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-061 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.2: Select and configure FMs. |
| `exam_skill` | Skill 1.2.1: Assess and choose FMs to ensure optimal alignment with specific business use cases and technical requirements (for example, by using performance benchmarks, capability analysis, limitation evaluation). |
| `exam_skill_local` | Select a model based on task, quality, latency, cost, context, and safety |
| `learning_unit` | Day01-order007 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Declarative; Conditional; Strategic |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T231108Z-openai-gpt-4.1-day01-applied-foundations.md` item 1 |

Stem:

A startup needs to generate product descriptions for a catalog. They want fluency, minimal hallucination, and the ability to fine-tune on their proprietary data. Which foundation model type should they prioritize?

Options:

A. A large language model (LLM) supporting supervised fine-tuning

B. A retrieval-augmented generation (RAG) model only

C. A text embedding model

D. A vision-language model

Correct answer: A large language model (LLM) supporting supervised fine-tuning

Rationale: LLMs designed for text generation and supporting supervised fine-tuning can be tailored to generate fluent descriptions and minimize hallucinations using proprietary data.

Distractors: A retrieval-augmented generation (RAG) model only: RAG models integrate retrieval but do not directly allow supervised fine-tuning; also, for generation quality, LLMs are more appropriate. A text embedding model: Text embedding models are suited for similarity search, not text generation tasks like product descriptions. A vision-language model: Vision-language models are used for multimodal inputs (e.g., image+text), not solely text generation.

Misconception tags: `model-vs-application-confusion`, `bigger-context-is-always-better`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- Amazon Bedrock model evaluation docs: <https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html>
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order007-model-capabilities-limitations-selection.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-062

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-062 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.2: Select and configure FMs. |
| `exam_skill` | Skill 1.2.1: Assess and choose FMs to ensure optimal alignment with specific business use cases and technical requirements (for example, by using performance benchmarks, capability analysis, limitation evaluation). |
| `exam_skill_local` | Select a model based on task, quality, latency, cost, context, and safety |
| `learning_unit` | Day01-order007 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Declarative; Conditional; Strategic |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | compare |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T231108Z-openai-gpt-4.1-day01-applied-foundations.md` item 2 |

Stem:

Your team must process documents with specialized scientific terminology. Which model limitation is MOST likely to impact accuracy?

Options:

A. Training data domain coverage

B. Inference latency

C. Model parameter count

D. API throughput limits

Correct answer: Training data domain coverage

Rationale: If a model wasn’t trained on enough scientific domain data, it will lack the ability to handle these terms accurately.

Distractors: Inference latency: Latency affects user experience, not the linguistic accuracy of the model. Model parameter count: While more parameters sometimes improve generality, domain knowledge depends more on data than size alone. API throughput limits: Throughput is an operational constraint, not a knowledge limitation.

Misconception tags: `bigger-context-is-always-better`, `parameter-count-equals-capability`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- Amazon Bedrock model evaluation docs: <https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html>
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order007-model-capabilities-limitations-selection.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-063

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-063 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.2: Select and configure FMs. |
| `exam_skill` | Skill 1.2.1: Assess and choose FMs to ensure optimal alignment with specific business use cases and technical requirements (for example, by using performance benchmarks, capability analysis, limitation evaluation). |
| `exam_skill_local` | Select a model based on task, quality, latency, cost, context, and safety |
| `learning_unit` | Day01-order007 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Declarative; Conditional; Strategic |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T231108Z-openai-gpt-4.1-day01-applied-foundations.md` item 3 |

Stem:

After integrating a new foundation model for chatbots, your team notices that model answers often contain fabricated references. Which primary capability is lacking in your current setup?

Options:

A. Ability to ground outputs in a trusted knowledge base

B. Increased model parameter size

C. Expanded context window

D. Response output formatting

Correct answer: Ability to ground outputs in a trusted knowledge base

Rationale: Grounding outputs minimizes hallucination by anchoring generation to verified data sources.

Distractors: Increased model parameter size: Bigger models can memorize more, but hallucinations stem from lack of grounding, not just size. Expanded context window: A larger context helps input more data, but does not prevent hallucination if facts are missing. Response output formatting: Formatting affects structure, not factual reliability.

Misconception tags: `bigger-context-is-always-better`, `model-vs-application-confusion`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- Amazon Bedrock model evaluation docs: <https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html>
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order007-model-capabilities-limitations-selection.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-064

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-064 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.2: Select and configure FMs. |
| `exam_skill` | Skill 1.2.1: Assess and choose FMs to ensure optimal alignment with specific business use cases and technical requirements (for example, by using performance benchmarks, capability analysis, limitation evaluation). |
| `exam_skill_local` | Select a model based on task, quality, latency, cost, context, and safety |
| `learning_unit` | Day01-order007 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Declarative; Conditional; Strategic |
| `question_format` | multiple-response |
| `difficulty` | medium |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T231108Z-openai-gpt-4.1-day01-applied-foundations.md` item 4 |

Stem:

Which TWO attributes should you consider most when choosing a foundation model for summarizing sensitive corporate documents?

Options:

A. Data privacy features

B. Model input length limits

C. Output temperature default

D. Organization’s AWS region

E. API authentication method

Correct answer: Data privacy features, Model input length limits

Rationale: Data privacy is critical with sensitive documents; input length limits impact whether documents fit in one inference call.

Distractors: Output temperature default: Defaults can be adjusted but are less critical than fundamental privacy and input constraints. Organization’s AWS region: Although region can matter, model selection primarily hinges on need and capabilities before locality. API authentication method: Authentication does not affect model suitability for summarization.

Misconception tags: `security-afterthought`, `prompt-as-one-off`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- Amazon Bedrock model evaluation docs: <https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html>
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order007-model-capabilities-limitations-selection.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-065

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-065 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.2: Select and configure FMs. |
| `exam_skill` | Skill 1.2.1: Assess and choose FMs to ensure optimal alignment with specific business use cases and technical requirements (for example, by using performance benchmarks, capability analysis, limitation evaluation). |
| `exam_skill_local` | Select a model based on task, quality, latency, cost, context, and safety |
| `learning_unit` | Day01-order007 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Declarative; Conditional; Strategic |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | judge |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T231108Z-openai-gpt-4.1-day01-applied-foundations.md` item 5 |

Stem:

A team is evaluating two foundation models: one excels in code generation, the other in natural conversational tasks. The application is a code assistant that also answers coding questions in plain English. Which model should they select?

Options:

A. Use an ensemble, invoking the appropriate model based on user question intent.

B. Use only the natural conversation model for all tasks.

C. Use only the code generation model for all tasks.

D. Select based on which model has lower cost per token.

Correct answer: Use an ensemble, invoking the appropriate model based on user question intent.

Rationale: An ensemble allows using each model’s strengths, ensuring both coding and conversational needs are handled optimally.

Distractors: Use only the natural conversation model for all tasks.: This model may underperform in technical, code-centric responses. Use only the code generation model for all tasks.: Such models typically aren’t optimized for open-ended, conversational queries. Select based on which model has lower cost per token.: Cost is important, but functional requirements should determine model choice first.

Misconception tags: `model-vs-application-confusion`, `cost-vs-requirements`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- Amazon Bedrock model evaluation docs: <https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html>
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order007-model-capabilities-limitations-selection.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-066

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-066 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.2: Select and configure FMs. |
| `exam_skill` | Skill 1.2.1: Assess and choose FMs to ensure optimal alignment with specific business use cases and technical requirements (for example, by using performance benchmarks, capability analysis, limitation evaluation). |
| `exam_skill_local` | Select a model based on task, quality, latency, cost, context, and safety |
| `learning_unit` | Day01-order007 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Declarative; Conditional; Strategic |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T231108Z-openai-gpt-4.1-day01-applied-foundations.md` item 6 |

Stem:

Your medical domain solution requires answers based strictly on curated documentation and no hallucinations. What’s the best model integration pattern?

Options:

A. Combine an LLM with retrieval-augmented grounding to your docs

B. Increase the model’s temperature

C. Choose a larger context window

D. Use a conversational agent without external structured data

Correct answer: Combine an LLM with retrieval-augmented grounding to your docs

Rationale: RAG reduces hallucination by ensuring the model uses trusted content as answer sources.

Distractors: Increase the model’s temperature: Higher temperature yields more creative (not controlled) answers; this increases risk of hallucination. Choose a larger context window: Larger context helps with more data, but does not ground outputs. Use a conversational agent without external structured data: Without grounding, hallucinations are more likely.

Misconception tags: `bigger-context-is-always-better`, `creativity-vs-control`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- Amazon Bedrock model evaluation docs: <https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html>
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order007-model-capabilities-limitations-selection.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-067

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-067 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.2: Select and configure FMs. |
| `exam_skill` | Skill 1.2.1: Assess and choose FMs to ensure optimal alignment with specific business use cases and technical requirements (for example, by using performance benchmarks, capability analysis, limitation evaluation). |
| `exam_skill_local` | Select a model based on task, quality, latency, cost, context, and safety |
| `learning_unit` | Day01-order007 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Declarative; Conditional; Strategic |
| `question_format` | multiple-response |
| `difficulty` | hard |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T231108Z-openai-gpt-4.1-day01-applied-foundations.md` item 7 |

Stem:

Which of the following are valid reasons for preferring a smaller foundation model? (Select TWO.)

Options:

A. Lower inference cost

B. Faster response latency

C. Better handling of rare domain-specific terminology

D. Easier to train from scratch

E. Improved accuracy for complex reasoning tasks

Correct answer: Lower inference cost, Faster response latency

Rationale: Smaller models are typically faster and cost less to run, but may not match large models’ accuracy or reasoning capabilities.

Distractors: Better handling of rare domain-specific terminology: Smaller models are likely to have less domain knowledge. Easier to train from scratch: Training from scratch is resource-intensive regardless of size; usually fine-tuning is used. Improved accuracy for complex reasoning tasks: Larger models generally outperform small ones on complex reasoning.

Misconception tags: `parameter-count-equals-capability`, `cost-vs-requirements`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- Amazon Bedrock model evaluation docs: <https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html>
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order007-model-capabilities-limitations-selection.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-068

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-068 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.2: Select and configure FMs. |
| `exam_skill` | Skill 1.2.1: Assess and choose FMs to ensure optimal alignment with specific business use cases and technical requirements (for example, by using performance benchmarks, capability analysis, limitation evaluation). |
| `exam_skill_local` | Select a model based on task, quality, latency, cost, context, and safety |
| `learning_unit` | Day01-order007 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Declarative; Conditional; Strategic |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | judge |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T231108Z-openai-gpt-4.1-day01-applied-foundations.md` item 9 |

Stem:

You need to process large legal contracts, some exceeding the maximum context window of your chosen model. What’s the best solution for extracting key clauses?

Options:

A. Chunk documents and process each chunk separately, then merge results

B. Increase the model temperature significantly

C. Switch to a model with more parameters, regardless of its context size

D. Only process the first part of each document

Correct answer: Chunk documents and process each chunk separately, then merge results

Rationale: By splitting documents, you work within model limits and can aggregate results intelligently.

Distractors: Increase the model temperature significantly: Higher temperature results in less stable outputs and does not address input length limits. Switch to a model with more parameters, regardless of its context size: Parameter count does not necessarily mean a larger context window. Only process the first part of each document: This would miss key clauses further down the document.

Misconception tags: `bigger-context-is-always-better`, `parameter-count-equals-capability`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- Amazon Bedrock model evaluation docs: <https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html>
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order007-model-capabilities-limitations-selection.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-069

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-069 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.2: Select and configure FMs. |
| `exam_skill` | Skill 1.2.1: Assess and choose FMs to ensure optimal alignment with specific business use cases and technical requirements (for example, by using performance benchmarks, capability analysis, limitation evaluation). |
| `exam_skill_local` | Select a model based on task, quality, latency, cost, context, and safety |
| `learning_unit` | Day01-order007 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Declarative; Conditional; Strategic |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T231108Z-openai-gpt-4.1-day01-applied-foundations.md` item 10 |

Stem:

A customer wants to use a vision-language model to analyze scanned invoices for itemized charges and payment due dates. Which limitation is most likely to cause problems?

Options:

A. OCR errors from poor image quality

B. Model’s context window size

C. Lack of API authentication

D. Large model parameter count

Correct answer: OCR errors from poor image quality

Rationale: The initial extraction of text from images relies on OCR; poor quality images lead to errors before the model sees any data.

Distractors: Model’s context window size: Most invoices are well within reasonable input limits. Lack of API authentication: This could cause security issues, but not output errors due to model limitations. Large model parameter count: Parameter count is not directly relevant to extracting structured data from invoices.

Misconception tags: `model-vs-application-confusion`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- Amazon Bedrock model evaluation docs: <https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html>
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order007-model-capabilities-limitations-selection.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-070

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-070 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.2: Select and configure FMs. |
| `exam_skill` | Skill 1.2.1: Assess and choose FMs to ensure optimal alignment with specific business use cases and technical requirements (for example, by using performance benchmarks, capability analysis, limitation evaluation). |
| `exam_skill_local` | Select a model based on task, quality, latency, cost, context, and safety |
| `learning_unit` | Day01-order007 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Declarative; Conditional; Strategic |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-21T020500Z-manual-codex-authored-day01-quality-top-up.md` item 17 |

Stem:

A team must choose a model for a customer chat feature that needs low latency, strong instruction following, moderate reasoning, and predictable cost at high request volume. What is the best selection approach?

Options:

A. Compare candidate models against task-specific quality, latency, context, safety, and cost criteria before selecting.

B. Select the largest available model because model size always dominates latency and cost concerns.

C. Select the cheapest model without evaluation because chat quality can be fixed entirely with prompts.

D. Select a model based only on whether it supports the longest context window.

Correct answer: A

Rationale: Model selection should weigh the actual use case across quality, latency, context, safety, and cost constraints.

Distractors: B: Larger models may increase latency and cost and are not always necessary. C: Prompts cannot compensate for every model capability gap. D: Context length is only one selection dimension.

Misconception tags: `largest-model-is-best`, `prompt-fixes-all-model-gaps`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- Amazon Bedrock model evaluation docs: <https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html>
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order007-model-capabilities-limitations-selection.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-071

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-071 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 2: Implementation and Integration |
| `exam_task` | Task 2.4: Implement FM API integrations. |
| `exam_skill` | Skill 2.4.1: Create flexible model interaction systems (for example, by using Amazon Bedrock APIs to manage synchronous requests from various compute environments, language-specific AWS SDKs and Amazon SQS for asynchronous processing, API Gateway to provide custom API clients with request validation). |
| `exam_skill_local` | Inspect basic Amazon Bedrock invocation requirements |
| `learning_unit` | Day01-order008 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Procedural; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T231108Z-openai-gpt-4.1-day01-applied-foundations.md` item 11 |

Stem:

You want to invoke a Jurassic-2 language model in Amazon Bedrock using the AWS Command Line Interface (CLI). Which AWS CLI subcommand should you use to invoke the model?

Options:

A. bedrock-runtime invoke-model

B. sagemaker invoke-endpoint

C. bedrock admin create-model

D. lambda invoke

Correct answer: bedrock-runtime invoke-model

Rationale: Amazon Bedrock's runtime API for LLMs is invoked with the bedrock-runtime invoke-model CLI subcommand.

Distractors: sagemaker invoke-endpoint: SageMaker inference endpoints are a different service; Bedrock has its own runtime interface. bedrock admin create-model: This is an admin operation, not an invocation. lambda invoke: AWS Lambda is for functions, not direct LLM invocation.

Misconception tags: `service-role-confusion`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- AWS Bedrock `InvokeModel` API Reference: <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModel.html>
- AWS Bedrock `Converse` API Reference: <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html>

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order008-basic-bedrock-model-invocation.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-072

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-072 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 2: Implementation and Integration |
| `exam_task` | Task 2.4: Implement FM API integrations. |
| `exam_skill` | Skill 2.4.1: Create flexible model interaction systems (for example, by using Amazon Bedrock APIs to manage synchronous requests from various compute environments, language-specific AWS SDKs and Amazon SQS for asynchronous processing, API Gateway to provide custom API clients with request validation). |
| `exam_skill_local` | Inspect basic Amazon Bedrock invocation requirements |
| `learning_unit` | Day01-order008 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Procedural; Embedded |
| `question_format` | multiple-response |
| `difficulty` | medium |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T231108Z-openai-gpt-4.1-day01-applied-foundations.md` item 12 |

Stem:

You are preparing a Bedrock InvokeModel API request for a text-generation model. Which TWO fields are REQUIRED in the request payload?

Options:

A. input

B. modelId

C. maxTokens

D. temperature

E. metadata

Correct answer: input, modelId

Rationale: 'input' defines what the model processes; 'modelId' identifies which Bedrock-hosted model to use.

Distractors: maxTokens: Useful for controlling output, but often defaults or is optional. temperature: Improves variation, but not strictly required. metadata: Not mandatory for a basic inference request.

Misconception tags: `prompt-as-one-off`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- AWS Bedrock `InvokeModel` API Reference: <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModel.html>
- AWS Bedrock `Converse` API Reference: <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html>

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order008-basic-bedrock-model-invocation.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-073

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-073 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 2: Implementation and Integration |
| `exam_task` | Task 2.4: Implement FM API integrations. |
| `exam_skill` | Skill 2.4.1: Create flexible model interaction systems (for example, by using Amazon Bedrock APIs to manage synchronous requests from various compute environments, language-specific AWS SDKs and Amazon SQS for asynchronous processing, API Gateway to provide custom API clients with request validation). |
| `exam_skill_local` | Inspect basic Amazon Bedrock invocation requirements |
| `learning_unit` | Day01-order008 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Procedural; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T231108Z-openai-gpt-4.1-day01-applied-foundations.md` item 13 |

Stem:

You invoke a Bedrock Titan model through the console, but receive an 'AccessDeniedException'. What should you troubleshoot FIRST?

Options:

A. The IAM role or user permissions for Bedrock model invocation

B. The context window size requested

C. The VPC endpoint for Bedrock

D. The current language selected in your console

Correct answer: The IAM role or user permissions for Bedrock model invocation

Rationale: An access error stems from IAM permissions, not model parameters or UI settings.

Distractors: The context window size requested: This affects model truncation, not IAM errors. The VPC endpoint for Bedrock: A VPC error would result in endpoint connectivity issues, not access denied. The current language selected in your console: Console language doesn’t affect authorization.

Misconception tags: `service-role-confusion`, `security-afterthought`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- AWS Bedrock `InvokeModel` API Reference: <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModel.html>
- AWS Bedrock `Converse` API Reference: <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html>

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order008-basic-bedrock-model-invocation.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-074

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-074 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 2: Implementation and Integration |
| `exam_task` | Task 2.4: Implement FM API integrations. |
| `exam_skill` | Skill 2.4.1: Create flexible model interaction systems (for example, by using Amazon Bedrock APIs to manage synchronous requests from various compute environments, language-specific AWS SDKs and Amazon SQS for asynchronous processing, API Gateway to provide custom API clients with request validation). |
| `exam_skill_local` | Inspect basic Amazon Bedrock invocation requirements |
| `learning_unit` | Day01-order008 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Procedural; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T231108Z-openai-gpt-4.1-day01-applied-foundations.md` item 14 |

Stem:

Your Bedrock text generation output is being truncated mid-sentence, even with short input prompts. What is the MOST likely cause?

Options:

A. The 'maxTokens' parameter is set too low in your request

B. Model permissions are insufficient for this input

C. Bedrock only supports short outputs by design

D. A VPC endpoint limit has been reached

Correct answer: The 'maxTokens' parameter is set too low in your request

Rationale: The output is cut off when the allowed output token count is too small.

Distractors: Model permissions are insufficient for this input: Permissions issues cause errors, not output truncation. Bedrock only supports short outputs by design: Bedrock supports long outputs if configured properly. A VPC endpoint limit has been reached: This would block all requests, not truncate outputs.

Misconception tags: `prompt-as-one-off`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- AWS Bedrock `InvokeModel` API Reference: <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModel.html>
- AWS Bedrock `Converse` API Reference: <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html>

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order008-basic-bedrock-model-invocation.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-075

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-075 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 2: Implementation and Integration |
| `exam_task` | Task 2.4: Implement FM API integrations. |
| `exam_skill` | Skill 2.4.1: Create flexible model interaction systems (for example, by using Amazon Bedrock APIs to manage synchronous requests from various compute environments, language-specific AWS SDKs and Amazon SQS for asynchronous processing, API Gateway to provide custom API clients with request validation). |
| `exam_skill_local` | Inspect basic Amazon Bedrock invocation requirements |
| `learning_unit` | Day01-order008 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Procedural; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T231108Z-openai-gpt-4.1-day01-applied-foundations.md` item 15 |

Stem:

When invoking a Bedrock model for inference from a Lambda function running in a VPC, what networking consideration is MOST important?

Options:

A. Configuring a VPC endpoint for Bedrock Runtime

B. Using EFS for prompt storage

C. Granting Lambda internet access

D. Adding Amazon S3 VPC endpoint

Correct answer: Configuring a VPC endpoint for Bedrock Runtime

Rationale: Without a VPC endpoint, the Lambda cannot securely access Bedrock from within the VPC.

Distractors: Using EFS for prompt storage: Prompt storage is not needed for basic invocation. Granting Lambda internet access: Direct internet access isn’t required when using VPC endpoints. Adding Amazon S3 VPC endpoint: S3 endpoints matter for storage, not for invoking Bedrock.

Misconception tags: `networking-misunderstanding`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- AWS Bedrock `InvokeModel` API Reference: <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModel.html>
- AWS Bedrock `Converse` API Reference: <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html>

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order008-basic-bedrock-model-invocation.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-076

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-076 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 2: Implementation and Integration |
| `exam_task` | Task 2.4: Implement FM API integrations. |
| `exam_skill` | Skill 2.4.1: Create flexible model interaction systems (for example, by using Amazon Bedrock APIs to manage synchronous requests from various compute environments, language-specific AWS SDKs and Amazon SQS for asynchronous processing, API Gateway to provide custom API clients with request validation). |
| `exam_skill_local` | Inspect basic Amazon Bedrock invocation requirements |
| `learning_unit` | Day01-order008 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Procedural; Embedded |
| `question_format` | multiple-response |
| `difficulty` | medium |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T231108Z-openai-gpt-4.1-day01-applied-foundations.md` item 16 |

Stem:

Which of the following can you configure per request when invoking LLMs via Bedrock? (Select TWO.)

Options:

A. Temperature

B. Session persistence duration

C. Maximum output tokens

D. Region of the underlying model

E. Billing metric interval

Correct answer: Temperature, Maximum output tokens

Rationale: Temperature and max output tokens are core configurable model inference parameters.

Distractors: Session persistence duration: Bedrock does not allow session management by default. Region of the underlying model: In-region model invocation is determined by deployment, not configuration. Billing metric interval: Billing granularity cannot be set by the API caller.

Misconception tags: `prompt-as-one-off`, `request-config-misunderstanding`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- AWS Bedrock `InvokeModel` API Reference: <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModel.html>
- AWS Bedrock `Converse` API Reference: <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html>

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order008-basic-bedrock-model-invocation.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-077

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-077 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 2: Implementation and Integration |
| `exam_task` | Task 2.4: Implement FM API integrations. |
| `exam_skill` | Skill 2.4.1: Create flexible model interaction systems (for example, by using Amazon Bedrock APIs to manage synchronous requests from various compute environments, language-specific AWS SDKs and Amazon SQS for asynchronous processing, API Gateway to provide custom API clients with request validation). |
| `exam_skill_local` | Inspect basic Amazon Bedrock invocation requirements |
| `learning_unit` | Day01-order008 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Procedural; Embedded |
| `question_format` | multiple-response |
| `difficulty` | hard |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T231108Z-openai-gpt-4.1-day01-applied-foundations.md` item 17 |

Stem:

Which actions are considered best practices for production Bedrock model invocation at scale? (Select TWO.)

Options:

A. Implement retry logic for transient errors

B. Store prompt history client-side

C. Hard-code all hyperparameters in your application

D. Monitor response latency and error rates

E. Use public model IDs regardless of version

Correct answer: Implement retry logic for transient errors, Monitor response latency and error rates

Rationale: Retries and monitoring are critical for resilience and operational oversight.

Distractors: Store prompt history client-side: May be useful in some scenarios, but not a Bedrock best practice. Hard-code all hyperparameters in your application: Hard-coding impedes tuning and flexibility. Use public model IDs regardless of version: Ignoring model versioning can break production.

Misconception tags: `production-misunderstanding`, `prompt-as-one-off`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- AWS Bedrock `InvokeModel` API Reference: <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModel.html>
- AWS Bedrock `Converse` API Reference: <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html>

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order008-basic-bedrock-model-invocation.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-078

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-078 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 2: Implementation and Integration |
| `exam_task` | Task 2.4: Implement FM API integrations. |
| `exam_skill` | Skill 2.4.1: Create flexible model interaction systems (for example, by using Amazon Bedrock APIs to manage synchronous requests from various compute environments, language-specific AWS SDKs and Amazon SQS for asynchronous processing, API Gateway to provide custom API clients with request validation). |
| `exam_skill_local` | Inspect basic Amazon Bedrock invocation requirements |
| `learning_unit` | Day01-order008 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Procedural; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T231108Z-openai-gpt-4.1-day01-applied-foundations.md` item 18 |

Stem:

Your application architecture must call Bedrock in a way that never exposes AWS credentials to the client. Which pattern is MOST appropriate?

Options:

A. Invoke Bedrock from a backend service using an IAM role

B. Embed AWS credentials in the client code

C. Add Bedrock invocation inside mobile app logic

D. Use client-side API Gateway with pass-through

Correct answer: Invoke Bedrock from a backend service using an IAM role

Rationale: Backend invocation avoids credential exposure, increasing security.

Distractors: Embed AWS credentials in the client code: Credentials in client code expose security risk. Add Bedrock invocation inside mobile app logic: Mobile clients should not have direct AWS permissions. Use client-side API Gateway with pass-through: API Gateway should be integrated from a backend, not directly from clients.

Misconception tags: `security-afterthought`, `service-role-confusion`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- AWS Bedrock `InvokeModel` API Reference: <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModel.html>
- AWS Bedrock `Converse` API Reference: <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html>

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order008-basic-bedrock-model-invocation.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-079

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-079 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 2: Implementation and Integration |
| `exam_task` | Task 2.4: Implement FM API integrations. |
| `exam_skill` | Skill 2.4.1: Create flexible model interaction systems (for example, by using Amazon Bedrock APIs to manage synchronous requests from various compute environments, language-specific AWS SDKs and Amazon SQS for asynchronous processing, API Gateway to provide custom API clients with request validation). |
| `exam_skill_local` | Inspect basic Amazon Bedrock invocation requirements |
| `learning_unit` | Day01-order008 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Procedural; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-21T020500Z-manual-codex-authored-day01-quality-top-up.md` item 18 |

Stem:

A developer invokes a Bedrock model from a Lambda function and receives an authorization error before any model response is returned. Which first check best matches the invocation path?

Options:

A. Verify the Lambda execution role has permission for the Bedrock runtime action and the selected model resource or allowed model scope.

B. Increase model temperature because authorization errors often occur when outputs are too deterministic.

C. Add more examples to the prompt so the model can infer the missing AWS permission.

D. Reduce max output tokens because Bedrock rejects all long requests as authorization failures.

Correct answer: A

Rationale: Authorization errors occur before model generation and should be investigated through IAM permissions for the runtime invocation path.

Distractors: B: Temperature has no bearing on AWS authorization. C: Prompt examples cannot grant IAM permissions. D: Token limits and authorization failures are different classes of errors.

Misconception tags: `iam-in-prompt`, `sampling-fixes-api-error`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- AWS Bedrock `InvokeModel` API Reference: <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModel.html>
- AWS Bedrock `Converse` API Reference: <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html>

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order008-basic-bedrock-model-invocation.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-080

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-080 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 2: Implementation and Integration |
| `exam_task` | Task 2.4: Implement FM API integrations. |
| `exam_skill` | Skill 2.4.1: Create flexible model interaction systems (for example, by using Amazon Bedrock APIs to manage synchronous requests from various compute environments, language-specific AWS SDKs and Amazon SQS for asynchronous processing, API Gateway to provide custom API clients with request validation). |
| `exam_skill_local` | Inspect basic Amazon Bedrock invocation requirements |
| `learning_unit` | Day01-order008 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Procedural; Embedded |
| `question_format` | multiple-response |
| `difficulty` | hard |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-21T020500Z-manual-codex-authored-day01-quality-top-up.md` item 19 |

Stem:

A team is writing a minimal Bedrock invocation runbook for a new service. Which two details must the runbook capture so another developer can reproduce the call shape? (Select TWO.)

Options:

A. The runtime API or SDK method being used and the model identifier selected for the request.

B. The request body structure, including messages or prompt fields and inference parameters required by that model/API.

C. The exact model weights used during provider pretraining.

D. A promise that the model will never produce unexpected content.

E. A user password embedded in the prompt so the model can authenticate itself.

Correct answer: A, B

Rationale: A reproducible invocation needs the API/method, model identifier, and request payload shape including relevant inference parameters.

Distractors: C: Pretraining weights are not part of a basic invocation runbook. D: A runbook cannot guarantee all model behavior. E: Credentials must not be embedded in prompts.

Misconception tags: `missing-request-shape`, `credentials-in-prompt`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- AWS Bedrock `InvokeModel` API Reference: <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModel.html>
- AWS Bedrock `Converse` API Reference: <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html>

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order008-basic-bedrock-model-invocation.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-081

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-081 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.1: Create effective model instruction frameworks to control FM behavior and outputs (for example, by using Amazon Bedrock Prompt Management to enforce role definitions, Amazon Bedrock Guardrails to enforce responsible AI guidelines, template configurations to format responses). |
| `exam_skill_local` | Design a prompt baseline with boundaries and structured output |
| `learning_unit` | Day01-order009 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Conceptual; Procedural; Causal |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T231108Z-openai-gpt-4.1-day01-applied-foundations.md` item 20 |

Stem:

You want consistent model outputs for downstream processing. What is the MOST effective prompt technique?

Options:

A. Provide a detailed output format or schema in the prompt

B. Set the temperature parameter to the lowest value possible

C. Increase the number of prompt examples

D. Use ambiguous language to encourage creativity

Correct answer: Provide a detailed output format or schema in the prompt

Rationale: Detailed structure yields predictable, machine-readable outputs.

Distractors: Set the temperature parameter to the lowest value possible: This reduces randomness but does not guarantee structured format. Increase the number of prompt examples: This improves few-shot learning, not output structure per se. Use ambiguous language to encourage creativity: Ambiguity reduces, not increases, consistency.

Misconception tags: `prompt-as-one-off`, `creativity-vs-control`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- Amazon Bedrock Prompt Management User Guide: <https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html>
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order009-prompt-fundamentals-structured-output.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-082

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-082 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.1: Create effective model instruction frameworks to control FM behavior and outputs (for example, by using Amazon Bedrock Prompt Management to enforce role definitions, Amazon Bedrock Guardrails to enforce responsible AI guidelines, template configurations to format responses). |
| `exam_skill_local` | Design a prompt baseline with boundaries and structured output |
| `learning_unit` | Day01-order009 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Conceptual; Procedural; Causal |
| `question_format` | multiple-response |
| `difficulty` | medium |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T231108Z-openai-gpt-4.1-day01-applied-foundations.md` item 21 |

Stem:

Which prompt engineering practices can help minimize hallucination? (Select TWO.)

Options:

A. Explicitly instructing the model to respond with 'I don't know' when unsure

B. Providing highly specific instructions limiting scope

C. Using extremely high temperature values

D. Requesting creative or speculative outputs

E. Offering ambiguous or open-ended prompts

Correct answer: Explicitly instructing the model to respond with 'I don't know' when unsure, Providing highly specific instructions limiting scope

Rationale: Both increase focus and self-constraint, reducing hallucination.

Distractors: Using extremely high temperature values: High temperature increases randomness and hallucination. Requesting creative or speculative outputs: Encourages less factual output. Offering ambiguous or open-ended prompts: Ambiguity increases hallucination risk.

Misconception tags: `prompt-as-one-off`, `creativity-vs-control`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- Amazon Bedrock Prompt Management User Guide: <https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html>
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order009-prompt-fundamentals-structured-output.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-083

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-083 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.1: Create effective model instruction frameworks to control FM behavior and outputs (for example, by using Amazon Bedrock Prompt Management to enforce role definitions, Amazon Bedrock Guardrails to enforce responsible AI guidelines, template configurations to format responses). |
| `exam_skill_local` | Design a prompt baseline with boundaries and structured output |
| `learning_unit` | Day01-order009 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Conceptual; Procedural; Causal |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T231108Z-openai-gpt-4.1-day01-applied-foundations.md` item 22 |

Stem:

A downstream process fails to extract data from Bedrock LLM output because the answer is sometimes a string, and sometimes a JSON object. What prompt change is most likely to fix this?

Options:

A. Instruct the model to always respond in a specific JSON schema

B. Decrease temperature to zero

C. Increase the maximum number of tokens allowed

D. Ask for more creative answers

Correct answer: Instruct the model to always respond in a specific JSON schema

Rationale: Direct output formatting instructions produce reliably structured, machine-parsable output.

Distractors: Decrease temperature to zero: Low temperature reduces randomness, but does not ensure format. Increase the maximum number of tokens allowed: Token budget does not fix inconsistent output types. Ask for more creative answers: Creativity likely increases variability.

Misconception tags: `prompt-as-one-off`, `creativity-vs-control`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- Amazon Bedrock Prompt Management User Guide: <https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html>
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order009-prompt-fundamentals-structured-output.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-084

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-084 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.1: Create effective model instruction frameworks to control FM behavior and outputs (for example, by using Amazon Bedrock Prompt Management to enforce role definitions, Amazon Bedrock Guardrails to enforce responsible AI guidelines, template configurations to format responses). |
| `exam_skill_local` | Design a prompt baseline with boundaries and structured output |
| `learning_unit` | Day01-order009 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Conceptual; Procedural; Causal |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T231108Z-openai-gpt-4.1-day01-applied-foundations.md` item 23 |

Stem:

In a prompt template for extracting entities from support tickets, which instruction will MOST likely improve extraction completeness?

Options:

A. List all required entities to extract and provide canonical labels upfront

B. Increase the model's temperature parameter

C. Provide shorter prompts for performance

D. Omit entity definitions to allow creativity

Correct answer: List all required entities to extract and provide canonical labels upfront

Rationale: Clear expectations and labels set up the model for structured, complete outputs.

Distractors: Increase the model's temperature parameter: This can add diversity, not completeness or reliability. Provide shorter prompts for performance: Short prompts may be faster but less exact. Omit entity definitions to allow creativity: Lack of instruction leads to inconsistency.

Misconception tags: `prompt-as-one-off`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- Amazon Bedrock Prompt Management User Guide: <https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html>
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order009-prompt-fundamentals-structured-output.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-085

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-085 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.1: Create effective model instruction frameworks to control FM behavior and outputs (for example, by using Amazon Bedrock Prompt Management to enforce role definitions, Amazon Bedrock Guardrails to enforce responsible AI guidelines, template configurations to format responses). |
| `exam_skill_local` | Design a prompt baseline with boundaries and structured output |
| `learning_unit` | Day01-order009 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Conceptual; Procedural; Causal |
| `question_format` | multiple-response |
| `difficulty` | medium |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T231108Z-openai-gpt-4.1-day01-applied-foundations.md` item 25 |

Stem:

Which prompt characteristics help generate reliable structured outputs for downstream processing? (Select TWO.)

Options:

A. Including an explicit output schema or example in the prompt

B. Requesting outputs in plain natural language

C. Being concise but vague in instructions

D. Adding temperature = 2 for maximum randomness

E. Providing few-shot examples for structure

Correct answer: Including an explicit output schema or example in the prompt, Providing few-shot examples for structure

Rationale: Schema and in-context examples anchor the model in consistent formatting.

Distractors: Requesting outputs in plain natural language: Natural language lacks structure and increases parsing challenges. Being concise but vague in instructions: Vagueness causes inconsistency. Adding temperature = 2 for maximum randomness: High temperature reduces structure.

Misconception tags: `prompt-as-one-off`, `creativity-vs-control`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- Amazon Bedrock Prompt Management User Guide: <https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html>
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order009-prompt-fundamentals-structured-output.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-086

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-086 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.1: Create effective model instruction frameworks to control FM behavior and outputs (for example, by using Amazon Bedrock Prompt Management to enforce role definitions, Amazon Bedrock Guardrails to enforce responsible AI guidelines, template configurations to format responses). |
| `exam_skill_local` | Design a prompt baseline with boundaries and structured output |
| `learning_unit` | Day01-order009 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Conceptual; Procedural; Causal |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T231108Z-openai-gpt-4.1-day01-applied-foundations.md` item 26 |

Stem:

An LLM returns plausible but incorrect answers when given vague prompts. What prompt adjustment is MOST likely to improve factual accuracy?

Options:

A. Add explicit relevant facts and context into the prompt

B. Increase top-k sampling parameter

C. Reduce output token length to focus responses

D. Increase the number of creative prompt variations

Correct answer: Add explicit relevant facts and context into the prompt

Rationale: Supplying facts and precise context increases probability of accurate, grounded answers.

Distractors: Increase top-k sampling parameter: High top-k increases diversity, not accuracy. Reduce output token length to focus responses: Shorter outputs might be factual or not, depending on input. Increase the number of creative prompt variations: Creative variation likely reduces factuality.

Misconception tags: `creativity-vs-control`, `prompt-as-one-off`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- Amazon Bedrock Prompt Management User Guide: <https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html>
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order009-prompt-fundamentals-structured-output.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-087

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-087 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.1: Create effective model instruction frameworks to control FM behavior and outputs (for example, by using Amazon Bedrock Prompt Management to enforce role definitions, Amazon Bedrock Guardrails to enforce responsible AI guidelines, template configurations to format responses). |
| `exam_skill_local` | Design a prompt baseline with boundaries and structured output |
| `learning_unit` | Day01-order009 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Conceptual; Procedural; Causal |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T231108Z-openai-gpt-4.1-day01-applied-foundations.md` item 27 |

Stem:

When prompting an LLM for a business report summary in YAML, what structure should the prompt include?

Options:

A. Explicit YAML block examples and required fields

B. Instructions for creative wording

C. A larger model context window

D. Low temperature configuration

Correct answer: Explicit YAML block examples and required fields

Rationale: Providing explicit structure aligns output to machine-readable YAML.

Distractors: Instructions for creative wording: Creativity may cause structural violations. A larger model context window: Context size does not enforce format. Low temperature configuration: Low temperature reduces randomness but does not enforce schema.

Misconception tags: `prompt-as-one-off`, `creativity-vs-control`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- Amazon Bedrock Prompt Management User Guide: <https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html>
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order009-prompt-fundamentals-structured-output.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-088

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-088 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.1: Create effective model instruction frameworks to control FM behavior and outputs (for example, by using Amazon Bedrock Prompt Management to enforce role definitions, Amazon Bedrock Guardrails to enforce responsible AI guidelines, template configurations to format responses). |
| `exam_skill_local` | Design a prompt baseline with boundaries and structured output |
| `learning_unit` | Day01-order009 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Conceptual; Procedural; Causal |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-21T020500Z-manual-codex-authored-day01-quality-top-up.md` item 20 |

Stem:

A team wants a model to return incident summaries that downstream code can parse reliably. The current prompt asks for a helpful summary, and parsing fails when headings vary. Which prompt change best targets the failure?

Options:

A. Specify a strict output schema with required fields, formatting constraints, and examples of valid output.

B. Raise temperature so the model explores more heading styles and one may match the parser.

C. Remove all role and task instructions so the model is not constrained.

D. Ask the model to decide the best structure for each incident because flexibility improves parsing.

Correct answer: A

Rationale: Structured-output requirements and examples reduce variation and align the response with downstream parsing needs.

Distractors: B: More variation worsens parser reliability. C: Removing instructions makes the output less predictable. D: Flexible structure conflicts with reliable parsing.

Misconception tags: `structured-output-afterthought`, `temperature-fixes-format`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- Amazon Bedrock Prompt Management User Guide: <https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html>
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order009-prompt-fundamentals-structured-output.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-089

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-089 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.1: Create effective model instruction frameworks to control FM behavior and outputs (for example, by using Amazon Bedrock Prompt Management to enforce role definitions, Amazon Bedrock Guardrails to enforce responsible AI guidelines, template configurations to format responses). |
| `exam_skill_local` | Design a prompt baseline with boundaries and structured output |
| `learning_unit` | Day01-order009 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Conceptual; Procedural; Causal |
| `question_format` | multiple-response |
| `difficulty` | hard |
| `cognitive_demand` | judge |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-21T020500Z-manual-codex-authored-day01-quality-top-up.md` item 21 |

Stem:

A company is creating a reusable prompt template for customer-email classification. Which two prompt elements most directly reduce ambiguity for the model? (Select TWO.)

Options:

A. A clear task instruction with the allowed classification labels.

B. Definitions or examples that distinguish similar labels.

C. A note that the model should use any label it finds creative.

D. A hidden assumption that downstream code will infer missing fields.

E. An instruction to ignore all customer text if it is difficult.

Correct answer: A, B

Rationale: Explicit task framing, label set, definitions, and examples reduce ambiguity and make outputs easier to evaluate.

Distractors: C: Invented labels break classification consistency. D: Downstream code should not guess missing output structure. E: Ignoring difficult inputs is not a valid classification strategy.

Misconception tags: `ambiguous-labels`, `downstream-parser-will-fix-it`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- Amazon Bedrock Prompt Management User Guide: <https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html>
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order009-prompt-fundamentals-structured-output.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-090

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-090 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.1: Create effective model instruction frameworks to control FM behavior and outputs (for example, by using Amazon Bedrock Prompt Management to enforce role definitions, Amazon Bedrock Guardrails to enforce responsible AI guidelines, template configurations to format responses). |
| `exam_skill_local` | Design a prompt baseline with boundaries and structured output |
| `learning_unit` | Day01-order009 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Conceptual; Procedural; Causal |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-21T020500Z-manual-codex-authored-day01-quality-top-up.md` item 22 |

Stem:

An application uses the same prompt template for refund, fraud, and shipping questions. The model often answers outside the intended domain and mixes policies. Which prompt-design issue should be addressed first?

Options:

A. The prompt lacks domain boundaries, task-specific instructions, and routing or context rules for different request types.

B. The prompt is too structured; removing constraints will make the model infer the correct policy domain.

C. The model needs a higher top-p value because policy mixing is caused only by narrow sampling.

D. The application should stop using templates because every prompt must be handwritten by an operator.

Correct answer: A

Rationale: Domain boundaries, routing/context rules, and task-specific instructions are needed when one application handles different policy areas.

Distractors: B: Fewer constraints would likely increase mixing. C: Sampling settings do not define policy routing. D: Reusable templates are useful when designed with the right variables and constraints.

Misconception tags: `one-prompt-for-all-domains`, `sampling-fixes-policy-routing`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- Amazon Bedrock Prompt Management User Guide: <https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html>
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order009-prompt-fundamentals-structured-output.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-091

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-091 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 5: Testing, Validation, and Troubleshooting |
| `exam_task` | Task 5.1: Implement evaluation systems for GenAI. |
| `exam_skill` | Skill 5.1.1: Develop comprehensive assessment frameworks to evaluate the quality and effectiveness of FM outputs beyond traditional ML evaluation approaches (for example, by using metrics for relevance, factual accuracy, consistency, and fluency). |
| `exam_skill_local` | Build a golden dataset that tests expected behavior and failure modes |
| `learning_unit` | Day01-order010 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Conceptual; Procedural |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T231108Z-openai-gpt-4.1-day01-applied-foundations.md` item 29 |

Stem:

You design a golden dataset to evaluate a Bedrock LLM’s FAQ-answering ability but observe high pass rates with vague questions. What’s the most likely issue?

Options:

A. The golden dataset questions lack specificity or challenge

B. Model is overfitting to training distribution

C. API rate limits are too restrictive

D. The golden dataset is too large

Correct answer: The golden dataset questions lack specificity or challenge

Rationale: Overly vague or generic test cases can be passed by models via pattern-matching; hard, specific cases are needed for proper evaluation.

Distractors: Model is overfitting to training distribution: FAQ-style models often generalize poorly, but this scenario points to easy questions, not overfitting. API rate limits are too restrictive: This would result in throttling, not high pass/fail discrepancies. The golden dataset is too large: Dataset size is not the root cause of low challenge.

Misconception tags: `evaluation-after-deployment`, `prompt-as-one-off`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- Amazon Bedrock Model Evaluation User Guide: <https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html>
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order010-basic-evaluation-golden-datasets.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-092

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-092 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 5: Testing, Validation, and Troubleshooting |
| `exam_task` | Task 5.1: Implement evaluation systems for GenAI. |
| `exam_skill` | Skill 5.1.1: Develop comprehensive assessment frameworks to evaluate the quality and effectiveness of FM outputs beyond traditional ML evaluation approaches (for example, by using metrics for relevance, factual accuracy, consistency, and fluency). |
| `exam_skill_local` | Build a golden dataset that tests expected behavior and failure modes |
| `learning_unit` | Day01-order010 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Conceptual; Procedural |
| `question_format` | multiple-response |
| `difficulty` | medium |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T231108Z-openai-gpt-4.1-day01-applied-foundations.md` item 30 |

Stem:

Which criteria should you apply when selecting examples for a golden dataset? (Select TWO.)

Options:

A. Diversity of topics/problems

B. Representativeness of real-world use cases

C. Likelihood of producing high-confidence outputs

D. Shortest possible inputs and outputs

E. Easy questions only

Correct answer: Diversity of topics/problems, Representativeness of real-world use cases

Rationale: A robust evaluation requires varied and realistic problems, not just easy or short ones.

Distractors: Likelihood of producing high-confidence outputs: Tests should include both easy and hard questions. Shortest possible inputs and outputs: Short items reduce realism. Easy questions only: Hard cases matter most for true model performance.

Misconception tags: `evaluation-after-deployment`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- Amazon Bedrock Model Evaluation User Guide: <https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html>
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order010-basic-evaluation-golden-datasets.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-093

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-093 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 5: Testing, Validation, and Troubleshooting |
| `exam_task` | Task 5.1: Implement evaluation systems for GenAI. |
| `exam_skill` | Skill 5.1.1: Develop comprehensive assessment frameworks to evaluate the quality and effectiveness of FM outputs beyond traditional ML evaluation approaches (for example, by using metrics for relevance, factual accuracy, consistency, and fluency). |
| `exam_skill_local` | Build a golden dataset that tests expected behavior and failure modes |
| `learning_unit` | Day01-order010 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Conceptual; Procedural |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T231108Z-openai-gpt-4.1-day01-applied-foundations.md` item 31 |

Stem:

After replacing a foundation model in production, user complaint rates rise, but basic accuracy measures on the golden dataset don’t change. What is the most plausible explanation?

Options:

A. The golden dataset lacks coverage for specific user scenarios

B. All users are submitting adversarial prompts

C. The old model was always less accurate

D. Inference token cost has increased

Correct answer: The golden dataset lacks coverage for specific user scenarios

Rationale: Metrics using incomplete datasets miss off-distribution user prompts that matter in production.

Distractors: All users are submitting adversarial prompts: Unlikely to suddenly change for all users. The old model was always less accurate: Contradicted by user satisfaction dropping after the change. Inference token cost has increased: Does not explain accuracy perceptions.

Misconception tags: `evaluation-after-deployment`, `prompt-as-one-off`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- Amazon Bedrock Model Evaluation User Guide: <https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html>
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order010-basic-evaluation-golden-datasets.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-094

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-094 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 5: Testing, Validation, and Troubleshooting |
| `exam_task` | Task 5.1: Implement evaluation systems for GenAI. |
| `exam_skill` | Skill 5.1.1: Develop comprehensive assessment frameworks to evaluate the quality and effectiveness of FM outputs beyond traditional ML evaluation approaches (for example, by using metrics for relevance, factual accuracy, consistency, and fluency). |
| `exam_skill_local` | Build a golden dataset that tests expected behavior and failure modes |
| `learning_unit` | Day01-order010 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Conceptual; Procedural |
| `question_format` | multiple-response |
| `difficulty` | medium |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T231108Z-openai-gpt-4.1-day01-applied-foundations.md` item 32 |

Stem:

Which TWO evaluation tasks are essential before deploying a new foundation-model-powered feature?

Options:

A. Run the feature against a golden dataset

B. Perform security review of data handling

C. Increase inference temperature for creative tests

D. Collect real user feedback before any release

E. Disable prompt logging

Correct answer: Run the feature against a golden dataset, Perform security review of data handling

Rationale: Evaluation and security are both critical pre-deployment tasks.

Distractors: Increase inference temperature for creative tests: Creativity tests are secondary to correctness and security. Collect real user feedback before any release: Feedback comes after, not before, initial deployment in most workflows. Disable prompt logging: Logging is useful for troubleshooting and safety.

Misconception tags: `security-afterthought`, `evaluation-after-deployment`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- Amazon Bedrock Model Evaluation User Guide: <https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html>
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order010-basic-evaluation-golden-datasets.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-095

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-095 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 5: Testing, Validation, and Troubleshooting |
| `exam_task` | Task 5.1: Implement evaluation systems for GenAI. |
| `exam_skill` | Skill 5.1.1: Develop comprehensive assessment frameworks to evaluate the quality and effectiveness of FM outputs beyond traditional ML evaluation approaches (for example, by using metrics for relevance, factual accuracy, consistency, and fluency). |
| `exam_skill_local` | Build a golden dataset that tests expected behavior and failure modes |
| `learning_unit` | Day01-order010 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Conceptual; Procedural |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T231108Z-openai-gpt-4.1-day01-applied-foundations.md` item 33 |

Stem:

A foundation model produces correct answers on golden dataset cases but fails with slightly rephrased user queries. What does this indicate MOST likely?

Options:

A. The test set is too narrow and lacks variation

B. Output temperature is set too low

C. Inference cost is too high

D. Model context window is too small

Correct answer: The test set is too narrow and lacks variation

Rationale: Lack of query diversity in the test set fails to capture real-world question variability.

Distractors: Output temperature is set too low: Low temperature increases consistency, not coverage. Inference cost is too high: Cost is an operational concern, not a cause of accuracy blind spots. Model context window is too small: Context is critical for long queries, but here question phrasing is the driver.

Misconception tags: `evaluation-after-deployment`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- Amazon Bedrock Model Evaluation User Guide: <https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html>
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order010-basic-evaluation-golden-datasets.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-096

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-096 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 5: Testing, Validation, and Troubleshooting |
| `exam_task` | Task 5.1: Implement evaluation systems for GenAI. |
| `exam_skill` | Skill 5.1.1: Develop comprehensive assessment frameworks to evaluate the quality and effectiveness of FM outputs beyond traditional ML evaluation approaches (for example, by using metrics for relevance, factual accuracy, consistency, and fluency). |
| `exam_skill_local` | Build a golden dataset that tests expected behavior and failure modes |
| `learning_unit` | Day01-order010 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Conceptual; Procedural |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T231108Z-openai-gpt-4.1-day01-applied-foundations.md` item 34 |

Stem:

You are evaluating LLM outputs using a manually labeled golden dataset. What should you do if labelers disagree on a significant fraction of cases?

Options:

A. Investigate ambiguity in dataset examples or labeling criteria

B. Remove all disputed examples from the dataset

C. Settle disputes by random label assignment

D. Increase output temperature to see if disagreement lessens

Correct answer: Investigate ambiguity in dataset examples or labeling criteria

Rationale: High annotator disagreement suggests unclear standards or ambiguous items.

Distractors: Remove all disputed examples from the dataset: This may bias the dataset and loses useful data. Settle disputes by random label assignment: Randomness damages dataset integrity. Increase output temperature to see if disagreement lessens: Temperature is irrelevant to human label quality.

Misconception tags: `evaluation-after-deployment`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- Amazon Bedrock Model Evaluation User Guide: <https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html>
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order010-basic-evaluation-golden-datasets.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-097

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-097 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 5: Testing, Validation, and Troubleshooting |
| `exam_task` | Task 5.1: Implement evaluation systems for GenAI. |
| `exam_skill` | Skill 5.1.1: Develop comprehensive assessment frameworks to evaluate the quality and effectiveness of FM outputs beyond traditional ML evaluation approaches (for example, by using metrics for relevance, factual accuracy, consistency, and fluency). |
| `exam_skill_local` | Build a golden dataset that tests expected behavior and failure modes |
| `learning_unit` | Day01-order010 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Conceptual; Procedural |
| `question_format` | multiple-response |
| `difficulty` | hard |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T231108Z-openai-gpt-4.1-day01-applied-foundations.md` item 35 |

Stem:

Which are valid use cases for a golden dataset? (Select TWO.)

Options:

A. Regression testing for model updates

B. Systematic error analysis of model predictions

C. Loading as model training data

D. Short-term logging through an API Gateway

E. Mainly reducing token cost during inference

Correct answer: Regression testing for model updates, Systematic error analysis of model predictions

Rationale: Golden datasets are evaluation sets for tracking changes and finding root causes of failures.

Distractors: Loading as model training data: Golden datasets should not bias model training. Short-term logging through an API Gateway: Logging is not a test set function. Mainly reducing token cost during inference: Token cost is a deployment/inference issue.

Misconception tags: `evaluation-after-deployment`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- Amazon Bedrock Model Evaluation User Guide: <https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html>
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order010-basic-evaluation-golden-datasets.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-098

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-098 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 5: Testing, Validation, and Troubleshooting |
| `exam_task` | Task 5.1: Implement evaluation systems for GenAI. |
| `exam_skill` | Skill 5.1.1: Develop comprehensive assessment frameworks to evaluate the quality and effectiveness of FM outputs beyond traditional ML evaluation approaches (for example, by using metrics for relevance, factual accuracy, consistency, and fluency). |
| `exam_skill_local` | Build a golden dataset that tests expected behavior and failure modes |
| `learning_unit` | Day01-order010 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Conceptual; Procedural |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-19T231108Z-openai-gpt-4.1-day01-applied-foundations.md` item 36 |

Stem:

When is it most important to use a golden dataset for foundation model evaluation?

Options:

A. When rolling out new models or changes that can affect critical user-facing behavior

B. Every time a single inference is run

C. To minimize cloud infrastructure cost

D. Only in training or pre-production environments

Correct answer: When rolling out new models or changes that can affect critical user-facing behavior

Rationale: Golden datasets support controlled testing during high-stakes changes.

Distractors: Every time a single inference is run: That is operationally impractical. To minimize cloud infrastructure cost: Evaluation relates to quality, not cost. Only in training or pre-production environments: Should be used both in pre-production and on release gates.

Misconception tags: `evaluation-after-deployment`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- Amazon Bedrock Model Evaluation User Guide: <https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html>
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order010-basic-evaluation-golden-datasets.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-099

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-099 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 5: Testing, Validation, and Troubleshooting |
| `exam_task` | Task 5.1: Implement evaluation systems for GenAI. |
| `exam_skill` | Skill 5.1.1: Develop comprehensive assessment frameworks to evaluate the quality and effectiveness of FM outputs beyond traditional ML evaluation approaches (for example, by using metrics for relevance, factual accuracy, consistency, and fluency). |
| `exam_skill_local` | Build a golden dataset that tests expected behavior and failure modes |
| `learning_unit` | Day01-order010 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Conceptual; Procedural |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-21T020500Z-manual-codex-authored-day01-quality-top-up.md` item 23 |

Stem:

A team wants to evaluate a GenAI assistant before changing its prompt template. They have only three examples that all represent happy-path customer questions. What is the best next step for the golden dataset?

Options:

A. Add representative edge cases, failure modes, ambiguous inputs, and expected evaluation notes before using it as a regression signal.

B. Use the three examples because a golden dataset should be as small as possible.

C. Replace the examples with one long prompt that asks the model whether it is accurate.

D. Evaluate only average response length because shorter answers are always better.

Correct answer: A

Rationale: A useful golden dataset should cover representative success cases, edge cases, and known failure modes with expected behavior.

Distractors: B: A tiny happy-path set is not enough for regression confidence. C: Self-judgment is not a substitute for defined test cases. D: Response length alone is not a quality metric.

Misconception tags: `happy-path-only-evaluation`, `self-evaluation-as-proof`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- Amazon Bedrock Model Evaluation User Guide: <https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html>
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order010-basic-evaluation-golden-datasets.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

### P1-AIP-D1-100

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D1-100 |
| `status` | approved |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Domain 5: Testing, Validation, and Troubleshooting |
| `exam_task` | Task 5.1: Implement evaluation systems for GenAI. |
| `exam_skill` | Skill 5.1.1: Develop comprehensive assessment frameworks to evaluate the quality and effectiveness of FM outputs beyond traditional ML evaluation approaches (for example, by using metrics for relevance, factual accuracy, consistency, and fluency). |
| `exam_skill_local` | Build a golden dataset that tests expected behavior and failure modes |
| `learning_unit` | Day01-order010 |
| `accelerated_day` | Day 1 |
| `knowledge_type` | Conceptual; Procedural |
| `question_format` | multiple-response |
| `difficulty` | exam-plus |
| `cognitive_demand` | judge |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-20 |
| `raw_source` | `2026-06-21T020500Z-manual-codex-authored-day01-quality-top-up.md` item 24 |

Stem:

After a prompt update, a GenAI assistant scores the same on broad human preference ratings but fails more often on refund-policy questions. Which two evaluation changes would make this regression easier to detect next time? (Select TWO.)

Options:

A. Tag golden-dataset cases by policy area or capability so regressions can be segmented.

B. Include expected-answer criteria for refund-policy cases rather than only general preference scores.

C. Remove domain tags because aggregate scores are easier to read.

D. Use only one evaluator comment for the entire dataset to keep review fast.

E. Increase temperature during evaluation so the model has more chances to answer correctly.

Correct answer: A, B

Rationale: Segmentation and explicit expected criteria help reveal focused regressions that aggregate preference ratings can hide.

Distractors: C: Removing tags makes localized regressions harder to find. D: One broad comment is not enough diagnostic evidence. E: Changing sampling during evaluation can obscure comparison rather than isolate regression.

Misconception tags: `aggregate-score-hides-regression`, `evaluation-after-deployment`

Source trace:

- Official AIP-C01 objectives JSON: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- Amazon Bedrock Model Evaluation User Guide: <https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html>
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md`

Remediation target:

- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order010-basic-evaluation-golden-datasets.md`
- `docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md`

## Culled Items

| Raw source | Curriculum order | Stem excerpt | Reasons | Evidence |
|---|---|---|---|---|
| `2026-06-19T230500Z-openai-gpt-4.1-day01-foundations.md` item 2 | Day01-order001 | Which of the following best describes a 'foundation model' in the generative AI landscape? | recall-only item, not scenario-based, keyword-trivia stem | recall-only item: cognitive_demand='recall'<br>not scenario-based: stem lacks scenario signals such as actor, workload, constraint, or event; cognitive_demand='recall'<br>keyword-trivia stem: matched weak stem pattern(s): which of the following best describes |
| `2026-06-19T230500Z-openai-gpt-4.1-day01-foundations.md` item 6 | Day01-order001 | What is a key benefit of using a foundation model via Amazon Bedrock versus running an open-source model on custom in... | not scenario-based, keyword-trivia stem | not scenario-based: stem lacks scenario signals such as actor, workload, constraint, or event; cognitive_demand='explain'<br>keyword-trivia stem: matched weak stem pattern(s): what is a key benefit |
| `2026-06-19T230500Z-openai-gpt-4.1-day01-foundations.md` item 8 | Day01-order001 | Which of the following tasks is typically outside the intended scope of a foundation model? | recall-only item, not scenario-based | recall-only item: cognitive_demand='recall'<br>not scenario-based: stem lacks scenario signals such as actor, workload, constraint, or event; cognitive_demand='recall' |
| `2026-06-19T230500Z-openai-gpt-4.1-day01-foundations.md` item 10 | Day01-order001 | Where in an AWS solution is the foundation model typically located when using Amazon Bedrock? | recall-only item, keyword-trivia stem | recall-only item: cognitive_demand='recall'<br>keyword-trivia stem: matched weak stem pattern(s): where in an aws solution |
| `2026-06-19T230500Z-openai-gpt-4.1-day01-foundations.md` item 12 | Day01-order002 | What does increasing the temperature parameter in a generative language model typically cause? | recall-only item, not scenario-based, keyword-trivia stem | recall-only item: cognitive_demand='recall'<br>not scenario-based: stem lacks scenario signals such as actor, workload, constraint, or event; cognitive_demand='recall'<br>keyword-trivia stem: matched weak stem pattern(s): what does increasing the temperature |
| `2026-06-19T230500Z-openai-gpt-4.1-day01-foundations.md` item 17 | Day01-order002 | What is a likely outcome if a model’s input prompt almost fills the maximum allowed context window? | not scenario-based | not scenario-based: stem lacks scenario signals such as actor, workload, constraint, or event; cognitive_demand='explain' |
| `2026-06-19T230500Z-openai-gpt-4.1-day01-foundations.md` item 18 | Day01-order002 | In the context of foundation models, what is a 'token'? | recall-only item, not scenario-based | recall-only item: cognitive_demand='recall'<br>not scenario-based: stem lacks scenario signals such as actor, workload, constraint, or event; cognitive_demand='recall' |
| `2026-06-19T230500Z-openai-gpt-4.1-day01-foundations.md` item 20 | Day01-order002 | Why does increasing the model’s context window typically lead to higher costs in AWS-hosted foundation model inference? | not scenario-based | not scenario-based: stem lacks scenario signals such as actor, workload, constraint, or event; cognitive_demand='explain' |
| `2026-06-19T230854Z-openai-gpt-4.1-day01-system-map.md` item 3 | Day01-order003 | A customer wants to use a fully managed API to access and query several popular foundation models without managing in... | recall-only item | recall-only item: cognitive_demand='recall' |
| `2026-06-19T230854Z-openai-gpt-4.1-day01-system-map.md` item 5 | Day01-order003 | A customer needs to automate content moderation using GenAI in images and videos and wants minimal setup. Which AWS s... | keyword-trivia stem | keyword-trivia stem: matched weak stem pattern(s): which aws service should they use directly |
| `2026-06-19T230854Z-openai-gpt-4.1-day01-system-map.md` item 6 | Day01-order003 | Which AWS services provide managed APIs to access foundation models for NLP tasks? (Select TWO.) | keyword-trivia stem, outdated or unverified technical claim | keyword-trivia stem: matched weak stem pattern(s): which aws services provide managed apis<br>outdated or unverified technical claim: matched stale/unverified claim pattern(s): sagemaker jumpstart |
| `2026-06-19T230854Z-openai-gpt-4.1-day01-system-map.md` item 13 | Day01-order004 | Which AWS service is designed to coordinate microservices and serverless functions into complex workflow executions w... | recall-only item, not scenario-based | recall-only item: cognitive_demand='recall'<br>not scenario-based: stem lacks scenario signals such as actor, workload, constraint, or event; cognitive_demand='recall' |
| `2026-06-19T230854Z-openai-gpt-4.1-day01-system-map.md` item 26 | Day01-order005 | A GenAI system deployed in a private VPC cannot connect to Amazon Bedrock endpoints. What is the most likely cause? | outdated or unverified technical claim | outdated or unverified technical claim: matched stale/unverified claim pattern(s): as of early 2024, bedrock does not yet |
| `2026-06-19T230854Z-openai-gpt-4.1-day01-system-map.md` item 31 | Day01-order006 | A customer needs GenAI model inference with the ability to restrict data residency to a specific AWS region and fine-... | outdated or unverified technical claim | outdated or unverified technical claim: matched stale/unverified claim pattern(s): as of early 2024, bedrock currently does not, bedrock does not yet |
| `2026-06-19T231108Z-openai-gpt-4.1-day01-applied-foundations.md` item 8 | Day01-order007 | Which of the following is LEAST likely to be improved by increasing foundation model parameter count? | recall-only item, not scenario-based | recall-only item: cognitive_demand='recall'<br>not scenario-based: stem lacks scenario signals such as actor, workload, constraint, or event; cognitive_demand='recall' |
| `2026-06-19T231108Z-openai-gpt-4.1-day01-applied-foundations.md` item 19 | Day01-order008 | A team wants to invoke a Bedrock model from within an AWS Glue ETL job. What should they ensure FIRST? | outdated or unverified technical claim | outdated or unverified technical claim: matched stale/unverified claim pattern(s): bedrock + glue |
| `2026-06-19T231108Z-openai-gpt-4.1-day01-applied-foundations.md` item 24 | Day01-order009 | Why is it important to clarify instructions in a prompt for multi-step tasks? | not scenario-based | not scenario-based: stem lacks scenario signals such as actor, workload, constraint, or event; cognitive_demand='explain' |
| `2026-06-19T231108Z-openai-gpt-4.1-day01-applied-foundations.md` item 28 | Day01-order009 | What prompt template technique best supports multi-lingual responses? | not scenario-based | not scenario-based: stem lacks scenario signals such as actor, workload, constraint, or event; cognitive_demand='explain' |
| `2026-06-19T231108Z-openai-gpt-4.1-day01-applied-foundations.md` item 37 | Day01-order010 | Why is systematic error analysis of LLM predictions using a golden dataset valuable? | not scenario-based | not scenario-based: stem lacks scenario signals such as actor, workload, constraint, or event; cognitive_demand='explain' |
