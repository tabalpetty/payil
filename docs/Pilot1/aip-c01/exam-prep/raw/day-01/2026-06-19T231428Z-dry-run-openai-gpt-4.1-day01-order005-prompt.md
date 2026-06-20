# Dry Run Prompt

- run_id: `order005`
- model: `gpt-4.1`
- created_utc: `2026-06-19T231428Z`

```text
        You are generating raw draft practice-question candidates for a curriculum repository.

        Follow the complete Day 1 prompt pack below, especially the output schema,
        global guardrails, and question quality requirements. Then execute the
        selected batch prompt.

        IMPORTANT:
        - Return only the generated draft questions and any compact batch metadata.
        - Do not say you cannot source-review the items; instead mark source_trace_needed.
        - Do not mark anything as approved.
        - Do not include copied official exam questions or third-party question-bank content.

        ===== DAY 1 PROMPT PACK =====
        # Day 1 Question Generation Prompts

## Purpose

Use this prompt pack to generate **draft** AIP-C01 Day 1 practice questions.

Generated questions are not approved question-bank items. Store raw responses
first, then review them against:

- the official AIP-C01 exam guide;
- relevant official AWS documentation;
- the Day 1 study guide and focused artifacts;
- [question-bank-specification.md](question-bank-specification.md).

## Day 1 Scope

Day 1 covers foundational GenAI and AWS system orientation:

| Curriculum order | Topic |
|---|---|
| Day01-order001 | Foundation models and GenAI fundamentals |
| Day01-order002 | Tokens, context windows, inference, temperature, top-k, and top-p |
| Day01-order003 | AWS GenAI service landscape |
| Day01-order004 | API, event-driven, serverless, container, and workflow fundamentals |
| Day01-order005 | IAM, trust boundaries, least privilege, networking, and data protection |
| Day01-order006 | GenAI requirements analysis and basic solution architecture |
| Day01-order007 | Foundation-model capabilities, limitations, and basic model selection |
| Day01-order008 | Basic Amazon Bedrock model invocation |
| Day01-order009 | Prompt fundamentals, instructions, templates, and structured outputs |
| Day01-order010 | Basic GenAI evaluation concepts and golden datasets |

## Output Schema Required From The LLM

Ask the LLM to return JSON or Markdown with these fields for each item:

| Field | Requirement |
|---|---|
| `status` | Always `draft`. |
| `official_exam_code` | `AIP-C01`. |
| `accelerated_day` | `Day 1`. |
| `curriculum_order` | One of `Day01-order001` through `Day01-order010`. |
| `topic` | Exact topic name. |
| `knowledge_category` | Knowledge, Skill, Representation / Location, etc. |
| `knowledge_type` | Declarative, Conceptual, Procedural, Conditional, Causal, Strategic, Normative, Embedded, etc. |
| `question_format` | `multiple-choice` or `multiple-response`. |
| `difficulty` | `easy`, `medium`, `hard`, or `exam-plus`. |
| `cognitive_demand` | Recall, explain, configure, select, compare, judge, or diagnose. |
| `stem` | Scenario-based question stem. |
| `options` | Four options for multiple choice; five or more for multiple response if needed. |
| `correct_answer` | Correct option or options. |
| `rationale_correct` | Why the correct answer is best. |
| `rationale_distractors` | Why each distractor is wrong or less appropriate. |
| `misconception_tags` | Trap or misconception tested. |
| `source_trace_needed` | AWS docs or exam-guide claim that must be checked during review. |
| `remediation_target` | Day 1 study guide, slide, artifact, or focused artifact file. |

## Global Guardrails

Include this block in every prompt:

```text
Create original practice questions only. Do not copy official AWS practice
questions, exam dumps, proprietary question banks, or third-party copyrighted
questions. The questions are draft learning items and must be source-reviewed
before approval.

Use the official exam name: AWS Certified Generative AI Developer -
Professional (AIP-C01).

Make questions scenario-based when possible. Avoid trivia unless the knowledge
type is explicitly declarative. Include plausible distractors that test real
misconceptions. Prefer professional judgment over keyword matching.
```

## Question Quality Requirements

Include this block in every prompt:

```text
Question quality requirements:

- Generate tough, tricky, professional-level questions suitable for serious
  AIP-C01 preparation.
- At least 80% of questions must be scenario-based.
- Include realistic distractors that are technically plausible but wrong
  because of a constraint, priority, AWS service boundary, operational risk,
  security issue, or misunderstanding.
- Avoid obvious answers, toy scenarios, and questions that can be answered by
  keyword matching.
- Include a mix of:
  - direct best-answer selection;
  - choose the best architecture or control;
  - identify the most likely failure/risk;
  - choose what to do first;
  - multiple-response questions where more than one option is correct.
- Mark each question with difficulty: `medium`, `hard`, or `exam-plus`.
  Do not generate easy questions unless explicitly requested.
- For every distractor, explain why it is tempting and why it is wrong or less
  suitable.
- Include misconception tags, such as `model-vs-application-confusion`,
  `bigger-context-is-always-better`, `service-role-confusion`,
  `security-afterthought`, `prompt-as-one-off`, or `evaluation-after-deployment`.
```

## Prompt 1: Day 1 Balanced Mini-Batch

Use this prompt when you want the full Day 1 draft pool.

```text
Act as an expert AWS Certified Generative AI Developer - Professional
(AIP-C01) instructor and exam-item writer.

Generate 100 original draft practice questions for Day 1 of an accelerated
AIP-C01 curriculum.

Create exactly 10 questions for each curriculum order:

1. Day01-order001 - Foundation models and GenAI fundamentals
2. Day01-order002 - Tokens, context windows, inference, temperature, top-k, and top-p
3. Day01-order003 - AWS GenAI service landscape
4. Day01-order004 - API, event-driven, serverless, container, and workflow fundamentals
5. Day01-order005 - IAM, trust boundaries, least privilege, networking, and data protection
6. Day01-order006 - GenAI requirements analysis and basic solution architecture
7. Day01-order007 - Foundation-model capabilities, limitations, and basic model selection
8. Day01-order008 - Basic Amazon Bedrock model invocation
9. Day01-order009 - Prompt fundamentals, instructions, templates, and structured outputs
10. Day01-order010 - Basic GenAI evaluation concepts and golden datasets

Use a mix of multiple-choice and multiple-response questions. At least 80 of
the 100 questions must be scenario-based. Make the questions tricky and
professional-level, with plausible distractors and detailed explanations.

Use the output schema specified above.

[PASTE GLOBAL GUARDRAILS]
[PASTE QUESTION QUALITY REQUIREMENTS]
```

## Prompt 2: Day 1 Foundation Concepts

Use this prompt for Day01-order001 and Day01-order002.

```text
Act as an expert AIP-C01 instructor and exam-item writer.

Generate 20 original draft practice questions for Day 1 foundation concepts:

- Day01-order001 - Foundation models and GenAI fundamentals
- Day01-order002 - Tokens, context windows, inference, temperature, top-k, and top-p

Create exactly 10 questions per curriculum order.

Test declarative, conceptual, and causal understanding. Include scenarios
where the learner must reason about model behavior, context limits,
determinism, output variability, latency, cost, and truncation risk.

Make the questions tricky and professional-level. Use the required output
schema, global guardrails, and question quality requirements from this file.
```

## Prompt 3: Day 1 AWS System Map And Architecture

Use this prompt for Day01-order003 through Day01-order006.

```text
Act as an expert AIP-C01 instructor and exam-item writer.

Generate 40 original draft practice questions for Day 1 AWS GenAI system
orientation:

- Day01-order003 - AWS GenAI service landscape
- Day01-order004 - API, event-driven, serverless, container, and workflow fundamentals
- Day01-order005 - IAM, trust boundaries, least privilege, networking, and data protection
- Day01-order006 - GenAI requirements analysis and basic solution architecture

Create exactly 10 questions per curriculum order.

Test conceptual, conditional, strategic, normative, and embedded knowledge.
Use scenarios where the learner must place services in the correct role,
choose integration patterns, identify trust boundaries, and select a basic
architecture based on requirements.

Make the questions tricky and professional-level. Use the required output
schema, global guardrails, and question quality requirements from this file.
```

## Prompt 4: Day 1 Model Selection, Bedrock Invocation, Prompting, Evaluation

Use this prompt for Day01-order007 through Day01-order010.

```text
Act as an expert AIP-C01 instructor and exam-item writer.

Generate 40 original draft practice questions for Day 1 applied foundations:

- Day01-order007 - Foundation-model capabilities, limitations, and basic model selection
- Day01-order008 - Basic Amazon Bedrock model invocation
- Day01-order009 - Prompt fundamentals, instructions, templates, and structured outputs
- Day01-order010 - Basic GenAI evaluation concepts and golden datasets

Create exactly 10 questions per curriculum order.

Test procedural, embedded, conditional, strategic, conceptual, and causal
understanding. Include scenarios involving model selection tradeoffs, basic
Bedrock invocation shape, prompt templates, structured output, and evaluation
with small golden datasets.

Make the questions tricky and professional-level. Use the required output
schema, global guardrails, and question quality requirements from this file.
```


## Topic-Level Prompts

Use these prompts when you want maximum quality and cleanest traceability: one
API call per Day 1 topic, exactly 10 questions per call.

### Topic Prompt: Day01-order001 Foundation Models And GenAI Fundamentals

```text
Act as an expert AWS Certified Generative AI Developer - Professional
(AIP-C01) instructor and exam-item writer.

Generate exactly 10 original draft practice questions for:

- curriculum_order: Day01-order001
- topic: Foundation models and GenAI fundamentals
- knowledge_category: Knowledge
- knowledge_type: Declarative; Conceptual

Test whether the learner can distinguish foundation models, generative AI,
inference, prompts, outputs, modalities, customization, and evaluation. Include
questions that expose model-vs-application confusion and shallow memorization.

Use the required output schema, global guardrails, and question quality
requirements from this file.
```

### Topic Prompt: Day01-order002 Tokens Context Inference Parameters

```text
Act as an expert AWS Certified Generative AI Developer - Professional
(AIP-C01) instructor and exam-item writer.

Generate exactly 10 original draft practice questions for:

- curriculum_order: Day01-order002
- topic: Tokens, context windows, inference, temperature, top-k, and top-p
- knowledge_category: Knowledge
- knowledge_type: Declarative; Conceptual; Causal

Test causal understanding of how tokens, context windows, inference parameters,
max output length, determinism, variability, latency, cost, truncation, and
output quality interact. Include tricky scenarios where bigger context or higher
creativity is a tempting but wrong answer.

Use the required output schema, global guardrails, and question quality
requirements from this file.
```

### Topic Prompt: Day01-order003 AWS GenAI Service Landscape

```text
Act as an expert AWS Certified Generative AI Developer - Professional
(AIP-C01) instructor and exam-item writer.

Generate exactly 10 original draft practice questions for:

- curriculum_order: Day01-order003
- topic: AWS GenAI service landscape
- knowledge_category: Knowledge; Representation / Location
- knowledge_type: Declarative; Conceptual; Embedded

Test whether the learner can classify AWS services by role in a GenAI system:
model access, model hosting/customization, application compute, API boundary,
orchestration, eventing, storage, retrieval/vector search, observability,
security, and governance/audit. Include plausible service-role distractors.

Use the required output schema, global guardrails, and question quality
requirements from this file.
```

### Topic Prompt: Day01-order004 Application Integration Patterns

```text
Act as an expert AWS Certified Generative AI Developer - Professional
(AIP-C01) instructor and exam-item writer.

Generate exactly 10 original draft practice questions for:

- curriculum_order: Day01-order004
- topic: API, event-driven, serverless, container, and workflow fundamentals
- knowledge_category: Knowledge
- knowledge_type: Conceptual; Conditional

Test when to choose synchronous APIs, asynchronous jobs, streaming responses,
event-driven workflows, serverless functions, containers, and multi-step
workflow orchestration for GenAI workloads. Make distractors hinge on latency,
user experience, task duration, failure handling, and workflow complexity.

Use the required output schema, global guardrails, and question quality
requirements from this file.
```

### Topic Prompt: Day01-order005 Trust Boundaries IAM Data Protection

```text
Act as an expert AWS Certified Generative AI Developer - Professional
(AIP-C01) instructor and exam-item writer.

Generate exactly 10 original draft practice questions for:

- curriculum_order: Day01-order005
- topic: IAM, trust boundaries, least privilege, networking, and data-protection fundamentals
- knowledge_category: Knowledge
- knowledge_type: Conceptual; Conditional; Normative

Test security boundary reasoning for GenAI systems: identity, authorization,
least privilege, network isolation, sensitive data exposure, logging privacy,
unauthorized retrieval, and risk tradeoffs. Include questions where security as
an afterthought is the tempting wrong answer.

Use the required output schema, global guardrails, and question quality
requirements from this file.
```

### Topic Prompt: Day01-order006 Requirements Basic Solution Architecture

```text
Act as an expert AWS Certified Generative AI Developer - Professional
(AIP-C01) instructor and exam-item writer.

Generate exactly 10 original draft practice questions for:

- curriculum_order: Day01-order006
- topic: GenAI requirements analysis and basic solution architecture
- knowledge_category: Knowledge; Skill
- knowledge_type: Conceptual; Conditional; Strategic

Test whether the learner can translate requirements into a basic GenAI solution
architecture. Include scenarios with competing requirements around business
goal, users, data, output quality, latency, cost, security, governance, and
audit. Require choosing and rejecting architecture options.

Use the required output schema, global guardrails, and question quality
requirements from this file.
```

### Topic Prompt: Day01-order007 Model Capabilities Limitations Selection

```text
Act as an expert AWS Certified Generative AI Developer - Professional
(AIP-C01) instructor and exam-item writer.

Generate exactly 10 original draft practice questions for:

- curriculum_order: Day01-order007
- topic: Foundation-model capabilities, limitations, and basic model selection
- knowledge_category: Knowledge; Skill
- knowledge_type: Declarative; Conditional; Strategic

Test model selection tradeoffs: quality, latency, cost, context window,
modality, structured output, safety behavior, regional availability, and fit to
use case. Include tricky scenarios where the largest or cheapest model is not
the best answer.

Use the required output schema, global guardrails, and question quality
requirements from this file.
```

### Topic Prompt: Day01-order008 Basic Bedrock Model Invocation

```text
Act as an expert AWS Certified Generative AI Developer - Professional
(AIP-C01) instructor and exam-item writer.

Generate exactly 10 original draft practice questions for:

- curriculum_order: Day01-order008
- topic: Basic Amazon Bedrock model invocation
- knowledge_category: Skill; Representation / Location
- knowledge_type: Procedural; Embedded

Test the basic shape of Amazon Bedrock model invocation: choosing a model,
confirming permissions, preparing request body, setting inference parameters,
invoking the runtime API, parsing responses, validating output, and handling
permission, request-shape, throttling, timeout, and malformed-output failures.

Use the required output schema, global guardrails, and question quality
requirements from this file.
```

### Topic Prompt: Day01-order009 Prompt Fundamentals Structured Output

```text
Act as an expert AWS Certified Generative AI Developer - Professional
(AIP-C01) instructor and exam-item writer.

Generate exactly 10 original draft practice questions for:

- curriculum_order: Day01-order009
- topic: Prompt fundamentals, instructions, templates, and structured outputs
- knowledge_category: Knowledge; Skill
- knowledge_type: Conceptual; Procedural; Causal

Test prompt anatomy and output control: role/system instruction, task, input
boundaries, output format, examples, safety/refusal rule, quality criteria,
structured JSON/YAML output, validation, and prompt-change effects. Include
questions where low temperature alone is a tempting but incomplete answer.

Use the required output schema, global guardrails, and question quality
requirements from this file.
```

### Topic Prompt: Day01-order010 Basic Evaluation Golden Datasets

```text
Act as an expert AWS Certified Generative AI Developer - Professional
(AIP-C01) instructor and exam-item writer.

Generate exactly 10 original draft practice questions for:

- curriculum_order: Day01-order010
- topic: Basic GenAI evaluation concepts and golden datasets
- knowledge_category: Knowledge; Skill
- knowledge_type: Conceptual; Procedural

Test evaluation concepts: golden datasets, expected output properties,
pass/fail notes, regression testing, dataset diversity, representativeness,
label ambiguity, systematic error analysis, and why one good answer is not proof
that the system works.

Use the required output schema, global guardrails, and question quality
requirements from this file.
```

## Batch Generation Advice

The full Day 1 pool is 100 draft questions. If the LLM struggles with length,
generate by topic or by prompt group:

- 20 questions for Prompt 2;
- 40 questions for Prompt 3;
- 40 questions for Prompt 4.

Do not accept low-quality volume. If a batch contains shallow questions,
obvious answers, weak distractors, or hallucinated AWS claims, discard or
regenerate it before review.

## Storage Workflow

1. Save unmodified LLM responses under:

   [raw/day-01/](raw/day-01/)

2. Normalize reviewed items under:

   [reviewed/day-01/](reviewed/day-01/)

3. Approve only after source review and schema validation.

## Repo Script

The repo includes a helper script that sends these prompts to the OpenAI API
and saves the raw response:

```bash
python3 scripts/generate_day01_questions.py --batch balanced
```

Set `OPENAI_API_KEY` before running. Use `--dry-run` to inspect the prompt
without calling the API.


        ===== SELECTED BATCH TO EXECUTE =====
        ```text
Act as an expert AWS Certified Generative AI Developer - Professional
(AIP-C01) instructor and exam-item writer.

Generate exactly 10 original draft practice questions for:

- curriculum_order: Day01-order005
- topic: IAM, trust boundaries, least privilege, networking, and data-protection fundamentals
- knowledge_category: Knowledge
- knowledge_type: Conceptual; Conditional; Normative

Test security boundary reasoning for GenAI systems: identity, authorization,
least privilege, network isolation, sensitive data exposure, logging privacy,
unauthorized retrieval, and risk tradeoffs. Include questions where security as
an afterthought is the tempting wrong answer.

Use the required output schema, global guardrails, and question quality
requirements from this file.
```

```
