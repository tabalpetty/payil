# Dry Run Day 2 Prompt

## Metadata

```json
{
  "provider": "openai",
  "model": "gpt-4.1",
  "run_id": "order001",
  "created_utc": "2026-06-23T053203Z",
  "status": "dry-run-prompt",
  "accelerated_day": "Day 2",
  "prompt_pack": "docs/Pilot1/aip-c01/exam-prep/day-02-question-generation-prompts.md",
  "provenance": "prompt only; no LLM call"
}
```

## Prompt That Would Be Sent

```text
You are generating raw draft practice-question candidates for a curriculum repository.

Follow the complete Day 2 prompt pack below, especially the output schema,
global guardrails, question quality requirements, official objective
traceability, and remediation-target constraints. Then execute the
selected prompt.

IMPORTANT:
- Return only the generated draft questions and any compact batch metadata.
- Do not say you cannot source-review the items; instead mark source_trace_needed.
- Do not mark anything as approved.
- Do not include copied official exam questions or third-party question-bank content.
- Preserve exact official objective values from the selected prompt.

===== DAY 2 PROMPT PACK =====
# Day 2 Question Generation Prompts

## Purpose

Use this prompt pack to generate **draft** AIP-C01 Day 2 practice questions.

Generated questions are not approved question-bank items. Store raw responses first, then review them against:

- `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`;
- relevant official AWS documentation;
- the Day 2 study guide, focused artifacts, and answer guidance;
- [question-bank-specification.md](question-bank-specification.md).

Default raw-generation target: `12` candidates per topic. A complete reviewed bank still requires at least `10` approved items per curriculum-order topic after review.

## Day 2 Scope

| Curriculum order | Topic | Official task | Primary skill |
|---|---|---|---|
| Day02-order001 | Data-quality validation and monitoring | Task 1.3: Implement data validation and processing pipelines for FM consumption. | Skill 1.3.1 |
| Day02-order002 | Text, image, audio, and tabular-data preprocessing | Task 1.3: Implement data validation and processing pipelines for FM consumption. | Skill 1.3.2 |
| Day02-order003 | Model-specific input formatting and data normalization | Task 1.3: Implement data validation and processing pipelines for FM consumption. | Skill 1.3.3 |
| Day02-order004 | Embeddings and vector-similarity fundamentals | Task 1.5: Design retrieval mechanisms for FM augmentation. | Skill 1.5.2 |
| Day02-order005 | Document chunking and segmentation | Task 1.5: Design retrieval mechanisms for FM augmentation. | Skill 1.5.1 |
| Day02-order006 | Metadata design and filtering | Task 1.4: Design and implement vector store solutions. | Skill 1.4.2 |
| Day02-order007 | Vector-store technologies and architecture | Task 1.4: Design and implement vector store solutions. | Skill 1.4.1 |
| Day02-order008 | Vector indexing, sharding, scaling, and performance | Task 1.4: Design and implement vector store solutions. | Skill 1.4.3 |
| Day02-order009 | Basic semantic retrieval | Task 1.5: Design retrieval mechanisms for FM augmentation. | Skill 1.5.3 |
| Day02-order010 | Basic Retrieval-Augmented Generation | Task 1.5: Design retrieval mechanisms for FM augmentation. | Skill 1.5.6 |

## Output Schema Required From The LLM

Return a single JSON array. Each object must contain these fields:

| Field | Requirement |
|---|---|
| `status` | Always `draft`. |
| `official_exam_code` | Always `AIP-C01`. |
| `accelerated_day` | Always `Day 2`. |
| `curriculum_order` | Exact curriculum-order value from the prompt. |
| `topic` | Exact topic name from the prompt. |
| `exam_domain` | Preserve the exact official value from the topic brief. |
| `exam_task` | Preserve the exact official value from the topic brief. |
| `exam_skill` | Preserve the exact official value from the topic brief. |
| `secondary_exam_skills` | Preserve the exact value from the topic brief. |
| `knowledge_category` | Exact knowledge category from the topic brief. |
| `knowledge_type` | Exact knowledge type from the topic brief. |
| `question_format` | `multiple-choice` or `multiple-response`. |
| `difficulty` | `medium`, `hard`, or `exam-plus`; do not generate `easy`. |
| `cognitive_demand` | Recall, explain, implement, integrate, configure, select, diagnose, optimize, compare, or judge. |
| `stem` | Scenario-based question stem. |
| `options` | Four options for multiple choice; five or more for multiple response. |
| `correct_answer` | Correct option or options. |
| `rationale_correct` | Why the correct answer is best. |
| `rationale_distractors` | Why each distractor is tempting but wrong or less appropriate. |
| `misconception_tags` | Trap, misconception, or tradeoff tested. |
| `source_trace_needed` | Specific AWS doc, objective, or project source that review must verify. |
| `remediation_target` | Existing study guide, focused artifact, or answer-guidance path from the topic brief. |
| `generation_notes` | Short note naming the scenario constraint and the quality risk the reviewer should inspect. |

## Global Guardrails

Include this block in every prompt:

```text
Create original practice questions only. Do not copy official AWS practice
questions, exam dumps, proprietary question banks, or third-party copyrighted
questions. The questions are draft learning items and must be source-reviewed
before approval.

Use the official exam name: AWS Certified Generative AI Developer -
Professional (AIP-C01).

Use `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
as the canonical source for official objective values. Preserve `exam_domain`,
`exam_task`, and `exam_skill` exactly as given in the topic brief.

Make questions scenario-based. Avoid trivia unless the topic brief's knowledge
type is explicitly declarative and the item still tests the fact inside a
professional scenario. Include plausible distractors that test real
misconceptions. Prefer professional judgment over keyword matching.

Generated items are raw Day 2 candidates, not approved bank items.
```

## Question Quality Requirements

Include this block in every prompt:

```text
Question quality requirements:

- Generate tough, tricky, professional-level questions suitable for serious
  AIP-C01 preparation.
- At least 90% of generated items must be scenario-based.
- Include realistic distractors that are technically plausible but wrong
  because of a constraint, priority, AWS service boundary, operational risk,
  security issue, data-quality issue, retrieval failure, or misunderstanding.
- Avoid obvious answers, toy scenarios, and questions that can be answered by
  keyword matching.
- Include a mix of direct best-answer selection, best architecture/control,
  most likely failure/risk, first action, and multiple-response formats.
- Mark each question with difficulty: `medium`, `hard`, or `exam-plus`.
- For every distractor, explain why it is tempting and why it is wrong or less
  suitable.
- Do not use stale date-bound service claims such as "as of early 2024",
  "currently does not support", or "does not yet support".
- If an item depends on a fast-changing AWS service capability, write the item
  around the decision process and put the exact AWS documentation needed in
  `source_trace_needed`.
- Route misses to existing Day 2 remediation files only.
```

## Review Feedback Incorporated

These prompts intentionally incorporate the Day 1 lessons:

- prompt more raw candidates than the approved target because review will cull
  weak, duplicate, or unverifiable items;
- preserve official objective fields from the canonical objectives JSON;
- require source-sensitive claims to be marked for review;
- demand scenario constraints and distractor rationales;
- avoid recall-only, keyword-trivia, and stale service-capability claims;
- keep remediation targets tied to actual study guide, artifact, or answer
  guidance files.

## Prompt 1: Day 2 Balanced Full-Pool Draft

Use this prompt when you want the full Day 2 raw draft pool.

```text
Act as an expert AWS Certified Generative AI Developer - Professional
(AIP-C01) instructor and exam-item writer.

Generate 120 original draft practice questions for Day 2 of an
accelerated AIP-C01 curriculum.

Create exactly 12 questions for each curriculum order:

1. Day02-order001 - Data-quality validation and monitoring
2. Day02-order002 - Text, image, audio, and tabular-data preprocessing
3. Day02-order003 - Model-specific input formatting and data normalization
4. Day02-order004 - Embeddings and vector-similarity fundamentals
5. Day02-order005 - Document chunking and segmentation
6. Day02-order006 - Metadata design and filtering
7. Day02-order007 - Vector-store technologies and architecture
8. Day02-order008 - Vector indexing, sharding, scaling, and performance
9. Day02-order009 - Basic semantic retrieval
10. Day02-order010 - Basic Retrieval-Augmented Generation

Use approximately 90 multiple-choice and 30 multiple-response questions across the whole
batch. At least 108 of the 120 questions must be
scenario-based. Make the questions tricky and professional-level, with
plausible distractors and detailed explanations.

Use the output schema specified above. Preserve all official objective fields
exactly from the topic briefs below.

Do not mark anything as approved.
```

## Topic-Level Prompts

## Topic Prompt: Day02-order001 Data-quality validation and monitoring

Use this prompt for focused generation or top-up generation for `Day02-order001`.

```text
Act as an expert AWS Certified Generative AI Developer - Professional
(AIP-C01) instructor and exam-item writer.

Generate exactly 12 original draft practice questions for:

- curriculum_order: Day02-order001
- topic: Data-quality validation and monitoring
- accelerated_day: Day 2
- knowledge_category: Skill; Knowledge; Representation / Location
- knowledge_type: Procedural; Causal; Embedded
- exam_domain: Content Domain 1: Foundation Model Integration, Data Management, and Compliance
- exam_task: Task 1.3: Implement data validation and processing pipelines for FM consumption.
- exam_skill: Skill 1.3.1: Create comprehensive data validation workflows to ensure data meets quality standards for FM consumption (for example, by using AWS Glue Data Quality, SageMaker Data Wrangler, custom Lambda functions, Amazon CloudWatch metrics).
- secondary_exam_skills: None.

Question focus:
- Ask for next step, runbook step, configuration choice, or failure-handling action.
- Ask the learner to predict effects or diagnose cause from symptoms.
- Include platform/tool/API/configuration evidence where relevant.

Misconceptions and traps to test:
- Confusing a tool or service with the full architecture.
- Selecting a plausible option without checking the scenario constraint.
- Blaming the model before inspecting data quality or extraction.

Required remediation targets. Use only these existing files:

- study_guide: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-02-data-embeddings-vector-stores-rag.md
- focused_artifact: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order001-data-quality-validation-monitoring.md
- answer_guidance: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day-02-answer-guidance.md

Generate approximately 9 multiple-choice and 3 multiple-response items for this topic.
Every item must be scenario-based unless the item is testing a necessary
declarative fact inside a realistic work situation.

Preserve the official objective fields exactly. Do not invent, paraphrase, or
rename the official domain, task, or skill.

Return only a JSON array of draft items using the required schema.
```

## Topic Prompt: Day02-order002 Text, image, audio, and tabular-data preprocessing

Use this prompt for focused generation or top-up generation for `Day02-order002`.

```text
Act as an expert AWS Certified Generative AI Developer - Professional
(AIP-C01) instructor and exam-item writer.

Generate exactly 12 original draft practice questions for:

- curriculum_order: Day02-order002
- topic: Text, image, audio, and tabular-data preprocessing
- accelerated_day: Day 2
- knowledge_category: Knowledge; Skill
- knowledge_type: Conceptual; Procedural; Conditional
- exam_domain: Content Domain 1: Foundation Model Integration, Data Management, and Compliance
- exam_task: Task 1.3: Implement data validation and processing pipelines for FM consumption.
- exam_skill: Skill 1.3.2: Create data processing workflows to handle complex data types including text, image, audio, and tabular data with specialized processing requirements for FM consumption (for example, by using Amazon Bedrock multimodal models, SageMaker Processing, AWS Transcribe, advanced multimodal pipeline architectures).
- secondary_exam_skills: None.

Question focus:
- Ask the learner to explain relationships, boundaries, or system roles.
- Ask for next step, runbook step, configuration choice, or failure-handling action.
- Ask when to choose or reject an approach based on scenario constraints.

Misconceptions and traps to test:
- Confusing a tool or service with the full architecture.
- Selecting a plausible option without checking the scenario constraint.
- Blaming the model before inspecting data quality or extraction.

Required remediation targets. Use only these existing files:

- study_guide: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-02-data-embeddings-vector-stores-rag.md
- focused_artifact: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order002-multimodal-data-preprocessing.md
- answer_guidance: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day-02-answer-guidance.md

Generate approximately 9 multiple-choice and 3 multiple-response items for this topic.
Every item must be scenario-based unless the item is testing a necessary
declarative fact inside a realistic work situation.

Preserve the official objective fields exactly. Do not invent, paraphrase, or
rename the official domain, task, or skill.

Return only a JSON array of draft items using the required schema.
```

## Topic Prompt: Day02-order003 Model-specific input formatting and data normalization

Use this prompt for focused generation or top-up generation for `Day02-order003`.

```text
Act as an expert AWS Certified Generative AI Developer - Professional
(AIP-C01) instructor and exam-item writer.

Generate exactly 12 original draft practice questions for:

- curriculum_order: Day02-order003
- topic: Model-specific input formatting and data normalization
- accelerated_day: Day 2
- knowledge_category: Knowledge; Skill; Representation / Location
- knowledge_type: Declarative; Procedural; Embedded
- exam_domain: Content Domain 1: Foundation Model Integration, Data Management, and Compliance
- exam_task: Task 1.3: Implement data validation and processing pipelines for FM consumption.
- exam_skill: Skill 1.3.3: Format input data for FM inference according to model-specific requirements (for example, by using JSON formatting for Amazon Bedrock API requests, structured data preparation for SageMaker AI endpoints, conversation formatting for dialog-based applications).
- secondary_exam_skills: Skill 1.3.4: Enhance input data quality to improve FM response quality and consistency (for example, by using Amazon Bedrock to reformat text, Amazon Comprehend to extract entities, Lambda functions to normalize data).

Question focus:
- Test necessary recall only inside a scenario; avoid glossary-only stems.
- Ask for next step, runbook step, configuration choice, or failure-handling action.
- Include platform/tool/API/configuration evidence where relevant.

Misconceptions and traps to test:
- Confusing a tool or service with the full architecture.
- Selecting a plausible option without checking the scenario constraint.

Required remediation targets. Use only these existing files:

- study_guide: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-02-data-embeddings-vector-stores-rag.md
- focused_artifact: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order003-input-formatting-normalization.md
- answer_guidance: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day-02-answer-guidance.md

Generate approximately 9 multiple-choice and 3 multiple-response items for this topic.
Every item must be scenario-based unless the item is testing a necessary
declarative fact inside a realistic work situation.

Preserve the official objective fields exactly. Do not invent, paraphrase, or
rename the official domain, task, or skill.

Return only a JSON array of draft items using the required schema.
```

## Topic Prompt: Day02-order004 Embeddings and vector-similarity fundamentals

Use this prompt for focused generation or top-up generation for `Day02-order004`.

```text
Act as an expert AWS Certified Generative AI Developer - Professional
(AIP-C01) instructor and exam-item writer.

Generate exactly 12 original draft practice questions for:

- curriculum_order: Day02-order004
- topic: Embeddings and vector-similarity fundamentals
- accelerated_day: Day 2
- knowledge_category: Knowledge
- knowledge_type: Declarative; Conceptual
- exam_domain: Content Domain 1: Foundation Model Integration, Data Management, and Compliance
- exam_task: Task 1.5: Design retrieval mechanisms for FM augmentation.
- exam_skill: Skill 1.5.2: Select and configure optimal embedding solutions to create efficient vector representations for semantic search (for example, by using Amazon Titan embeddings based on dimensionality and domain fit, by evaluating performance characteristics of Amazon Bedrock embedding models, by using Lambda functions to batch generate embeddings).
- secondary_exam_skills: None.

Question focus:
- Test necessary recall only inside a scenario; avoid glossary-only stems.
- Ask the learner to explain relationships, boundaries, or system roles.

Misconceptions and traps to test:
- Confusing a tool or service with the full architecture.
- Selecting a plausible option without checking the scenario constraint.
- Assuming embeddings enforce authorization, freshness, or source authority.

Required remediation targets. Use only these existing files:

- study_guide: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-02-data-embeddings-vector-stores-rag.md
- focused_artifact: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order004-embeddings-vector-similarity.md
- answer_guidance: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day-02-answer-guidance.md

Generate approximately 9 multiple-choice and 3 multiple-response items for this topic.
Every item must be scenario-based unless the item is testing a necessary
declarative fact inside a realistic work situation.

Preserve the official objective fields exactly. Do not invent, paraphrase, or
rename the official domain, task, or skill.

Return only a JSON array of draft items using the required schema.
```

## Topic Prompt: Day02-order005 Document chunking and segmentation

Use this prompt for focused generation or top-up generation for `Day02-order005`.

```text
Act as an expert AWS Certified Generative AI Developer - Professional
(AIP-C01) instructor and exam-item writer.

Generate exactly 12 original draft practice questions for:

- curriculum_order: Day02-order005
- topic: Document chunking and segmentation
- accelerated_day: Day 2
- knowledge_category: Knowledge; Skill
- knowledge_type: Conceptual; Procedural; Causal; Conditional
- exam_domain: Content Domain 1: Foundation Model Integration, Data Management, and Compliance
- exam_task: Task 1.5: Design retrieval mechanisms for FM augmentation.
- exam_skill: Skill 1.5.1: Develop effective document segmentation approaches to optimize retrieval performance for FM context augmentation (for example, by using Amazon Bedrock chunking capabilities, Lambda functions to implement fixed-size chunking, custom processing for hierarchical chunking based on content structure).
- secondary_exam_skills: None.

Question focus:
- Ask the learner to explain relationships, boundaries, or system roles.
- Ask for next step, runbook step, configuration choice, or failure-handling action.
- Ask when to choose or reject an approach based on scenario constraints.
- Ask the learner to predict effects or diagnose cause from symptoms.

Misconceptions and traps to test:
- Confusing a tool or service with the full architecture.
- Selecting a plausible option without checking the scenario constraint.
- Assuming one chunk size works for every source document.

Required remediation targets. Use only these existing files:

- study_guide: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-02-data-embeddings-vector-stores-rag.md
- focused_artifact: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order005-document-chunking-segmentation.md
- answer_guidance: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day-02-answer-guidance.md

Generate approximately 9 multiple-choice and 3 multiple-response items for this topic.
Every item must be scenario-based unless the item is testing a necessary
declarative fact inside a realistic work situation.

Preserve the official objective fields exactly. Do not invent, paraphrase, or
rename the official domain, task, or skill.

Return only a JSON array of draft items using the required schema.
```

## Topic Prompt: Day02-order006 Metadata design and filtering

Use this prompt for focused generation or top-up generation for `Day02-order006`.

```text
Act as an expert AWS Certified Generative AI Developer - Professional
(AIP-C01) instructor and exam-item writer.

Generate exactly 12 original draft practice questions for:

- curriculum_order: Day02-order006
- topic: Metadata design and filtering
- accelerated_day: Day 2
- knowledge_category: Knowledge; Skill
- knowledge_type: Conceptual; Procedural; Conditional
- exam_domain: Content Domain 1: Foundation Model Integration, Data Management, and Compliance
- exam_task: Task 1.4: Design and implement vector store solutions.
- exam_skill: Skill 1.4.2: Develop comprehensive metadata frameworks to improve search precision and context awareness for FM interactions (for example, by using S3 object metadata for document timestamps, custom attributes for authorship information, tagging systems for domain classification).
- secondary_exam_skills: None.

Question focus:
- Ask the learner to explain relationships, boundaries, or system roles.
- Ask for next step, runbook step, configuration choice, or failure-handling action.
- Ask when to choose or reject an approach based on scenario constraints.

Misconceptions and traps to test:
- Confusing a tool or service with the full architecture.
- Selecting a plausible option without checking the scenario constraint.
- Treating metadata as decoration instead of a filtering/security control.

Required remediation targets. Use only these existing files:

- study_guide: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-02-data-embeddings-vector-stores-rag.md
- focused_artifact: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order006-metadata-design-filtering.md
- answer_guidance: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day-02-answer-guidance.md

Generate approximately 9 multiple-choice and 3 multiple-response items for this topic.
Every item must be scenario-based unless the item is testing a necessary
declarative fact inside a realistic work situation.

Preserve the official objective fields exactly. Do not invent, paraphrase, or
rename the official domain, task, or skill.

Return only a JSON array of draft items using the required schema.
```

## Topic Prompt: Day02-order007 Vector-store technologies and architecture

Use this prompt for focused generation or top-up generation for `Day02-order007`.

```text
Act as an expert AWS Certified Generative AI Developer - Professional
(AIP-C01) instructor and exam-item writer.

Generate exactly 12 original draft practice questions for:

- curriculum_order: Day02-order007
- topic: Vector-store technologies and architecture
- accelerated_day: Day 2
- knowledge_category: Knowledge; Skill; Representation / Location
- knowledge_type: Conceptual; Conditional; Strategic; Embedded
- exam_domain: Content Domain 1: Foundation Model Integration, Data Management, and Compliance
- exam_task: Task 1.4: Design and implement vector store solutions.
- exam_skill: Skill 1.4.1: Create advanced vector database architectures specifically for FM augmentation to enable efficient semantic retrieval beyond traditional search capabilities (for example, by using Amazon Bedrock Knowledge Bases for hierarchical organization, Amazon OpenSearch Service with the Neural plugin for Amazon Bedrock integration for topic-based segmentation, Amazon RDS with Amazon S3 document repositories, Amazon DynamoDB with vector databases for metadata and embeddings).
- secondary_exam_skills: Skill 1.5.3: Deploy and configure vector search solutions to enable semantic search capabilities for FM augmentation (for example, by using OpenSearch Service with vector search capabilities, Amazon Aurora with the pgvector extension, Amazon Bedrock Knowledge Bases with managed vector store functionality).

Question focus:
- Ask the learner to explain relationships, boundaries, or system roles.
- Ask when to choose or reject an approach based on scenario constraints.
- Ask for tradeoff, architecture decision, or defended plan.
- Include platform/tool/API/configuration evidence where relevant.

Misconceptions and traps to test:
- Confusing a tool or service with the full architecture.
- Selecting a plausible option without checking the scenario constraint.
- Assuming embeddings enforce authorization, freshness, or source authority.

Required remediation targets. Use only these existing files:

- study_guide: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-02-data-embeddings-vector-stores-rag.md
- focused_artifact: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order007-vector-store-architecture.md
- answer_guidance: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day-02-answer-guidance.md

Generate approximately 9 multiple-choice and 3 multiple-response items for this topic.
Every item must be scenario-based unless the item is testing a necessary
declarative fact inside a realistic work situation.

Preserve the official objective fields exactly. Do not invent, paraphrase, or
rename the official domain, task, or skill.

Return only a JSON array of draft items using the required schema.
```

## Topic Prompt: Day02-order008 Vector indexing, sharding, scaling, and performance

Use this prompt for focused generation or top-up generation for `Day02-order008`.

```text
Act as an expert AWS Certified Generative AI Developer - Professional
(AIP-C01) instructor and exam-item writer.

Generate exactly 12 original draft practice questions for:

- curriculum_order: Day02-order008
- topic: Vector indexing, sharding, scaling, and performance
- accelerated_day: Day 2
- knowledge_category: Knowledge; Skill; Representation / Location
- knowledge_type: Conceptual; Procedural; Causal; Embedded
- exam_domain: Content Domain 1: Foundation Model Integration, Data Management, and Compliance
- exam_task: Task 1.4: Design and implement vector store solutions.
- exam_skill: Skill 1.4.3: Implement high-performance vector database architectures to optimize semantic search performance at scale for FM retrieval (for example, by using OpenSearch sharding strategies, multi-index approaches for specialized domains, hierarchical indexing techniques).
- secondary_exam_skills: Skill 1.4.5: Design and deploy data maintenance systems to ensure that vector stores contain current and accurate information for FM augmentation (for example, by using incremental update mechanisms, real-time change detection systems, automated synchronization workflows, scheduled refresh pipelines).

Question focus:
- Ask the learner to explain relationships, boundaries, or system roles.
- Ask for next step, runbook step, configuration choice, or failure-handling action.
- Ask the learner to predict effects or diagnose cause from symptoms.
- Include platform/tool/API/configuration evidence where relevant.

Misconceptions and traps to test:
- Confusing a tool or service with the full architecture.
- Selecting a plausible option without checking the scenario constraint.
- Assuming embeddings enforce authorization, freshness, or source authority.

Required remediation targets. Use only these existing files:

- study_guide: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-02-data-embeddings-vector-stores-rag.md
- focused_artifact: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order008-vector-indexing-scaling-performance.md
- answer_guidance: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day-02-answer-guidance.md

Generate approximately 9 multiple-choice and 3 multiple-response items for this topic.
Every item must be scenario-based unless the item is testing a necessary
declarative fact inside a realistic work situation.

Preserve the official objective fields exactly. Do not invent, paraphrase, or
rename the official domain, task, or skill.

Return only a JSON array of draft items using the required schema.
```

## Topic Prompt: Day02-order009 Basic semantic retrieval

Use this prompt for focused generation or top-up generation for `Day02-order009`.

```text
Act as an expert AWS Certified Generative AI Developer - Professional
(AIP-C01) instructor and exam-item writer.

Generate exactly 12 original draft practice questions for:

- curriculum_order: Day02-order009
- topic: Basic semantic retrieval
- accelerated_day: Day 2
- knowledge_category: Knowledge; Skill
- knowledge_type: Conceptual; Procedural
- exam_domain: Content Domain 1: Foundation Model Integration, Data Management, and Compliance
- exam_task: Task 1.5: Design retrieval mechanisms for FM augmentation.
- exam_skill: Skill 1.5.3: Deploy and configure vector search solutions to enable semantic search capabilities for FM augmentation (for example, by using OpenSearch Service with vector search capabilities, Amazon Aurora with the pgvector extension, Amazon Bedrock Knowledge Bases with managed vector store functionality).
- secondary_exam_skills: Skill 1.5.4: Create advanced search architectures to improve the relevance and accuracy of retrieved information for FM context (for example, by using OpenSearch for semantic search, hybrid search that combines keywords and vectors, Amazon Bedrock reranker models).

Question focus:
- Ask the learner to explain relationships, boundaries, or system roles.
- Ask for next step, runbook step, configuration choice, or failure-handling action.

Misconceptions and traps to test:
- Confusing a tool or service with the full architecture.
- Selecting a plausible option without checking the scenario constraint.
- Assuming RAG means the model searches documents by itself.

Required remediation targets. Use only these existing files:

- study_guide: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-02-data-embeddings-vector-stores-rag.md
- focused_artifact: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order009-basic-semantic-retrieval.md
- answer_guidance: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day-02-answer-guidance.md

Generate approximately 9 multiple-choice and 3 multiple-response items for this topic.
Every item must be scenario-based unless the item is testing a necessary
declarative fact inside a realistic work situation.

Preserve the official objective fields exactly. Do not invent, paraphrase, or
rename the official domain, task, or skill.

Return only a JSON array of draft items using the required schema.
```

## Topic Prompt: Day02-order010 Basic Retrieval-Augmented Generation

Use this prompt for focused generation or top-up generation for `Day02-order010`.

```text
Act as an expert AWS Certified Generative AI Developer - Professional
(AIP-C01) instructor and exam-item writer.

Generate exactly 12 original draft practice questions for:

- curriculum_order: Day02-order010
- topic: Basic Retrieval-Augmented Generation
- accelerated_day: Day 2
- knowledge_category: Knowledge; Skill
- knowledge_type: Conceptual; Procedural; Strategic
- exam_domain: Content Domain 1: Foundation Model Integration, Data Management, and Compliance
- exam_task: Task 1.5: Design retrieval mechanisms for FM augmentation.
- exam_skill: Skill 1.5.6: Create consistent access mechanisms to enable seamless integration with FMs (for example, by using function calling interfaces for vector search, Model Context Protocol [MCP] clients for vector queries, standardized API patterns for retrieval augmentation).
- secondary_exam_skills: Skill 1.1.1: Create comprehensive architectural designs that align with specific business needs and technical constraints (for example, by using appropriate FMs, integration patterns, deployment strategies).

Question focus:
- Ask the learner to explain relationships, boundaries, or system roles.
- Ask for next step, runbook step, configuration choice, or failure-handling action.
- Ask for tradeoff, architecture decision, or defended plan.

Misconceptions and traps to test:
- Confusing a tool or service with the full architecture.
- Selecting a plausible option without checking the scenario constraint.
- Assuming RAG means the model searches documents by itself.

Required remediation targets. Use only these existing files:

- study_guide: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-02-data-embeddings-vector-stores-rag.md
- focused_artifact: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order010-basic-rag-design.md
- answer_guidance: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day-02-answer-guidance.md

Generate approximately 9 multiple-choice and 3 multiple-response items for this topic.
Every item must be scenario-based unless the item is testing a necessary
declarative fact inside a realistic work situation.

Preserve the official objective fields exactly. Do not invent, paraphrase, or
rename the official domain, task, or skill.

Return only a JSON array of draft items using the required schema.
```


===== SELECTED PROMPT TO EXECUTE =====
Use this prompt for focused generation or top-up generation for `Day02-order001`.

```text
Act as an expert AWS Certified Generative AI Developer - Professional
(AIP-C01) instructor and exam-item writer.

Generate exactly 12 original draft practice questions for:

- curriculum_order: Day02-order001
- topic: Data-quality validation and monitoring
- accelerated_day: Day 2
- knowledge_category: Skill; Knowledge; Representation / Location
- knowledge_type: Procedural; Causal; Embedded
- exam_domain: Content Domain 1: Foundation Model Integration, Data Management, and Compliance
- exam_task: Task 1.3: Implement data validation and processing pipelines for FM consumption.
- exam_skill: Skill 1.3.1: Create comprehensive data validation workflows to ensure data meets quality standards for FM consumption (for example, by using AWS Glue Data Quality, SageMaker Data Wrangler, custom Lambda functions, Amazon CloudWatch metrics).
- secondary_exam_skills: None.

Question focus:
- Ask for next step, runbook step, configuration choice, or failure-handling action.
- Ask the learner to predict effects or diagnose cause from symptoms.
- Include platform/tool/API/configuration evidence where relevant.

Misconceptions and traps to test:
- Confusing a tool or service with the full architecture.
- Selecting a plausible option without checking the scenario constraint.
- Blaming the model before inspecting data quality or extraction.

Required remediation targets. Use only these existing files:

- study_guide: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-02-data-embeddings-vector-stores-rag.md
- focused_artifact: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order001-data-quality-validation-monitoring.md
- answer_guidance: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day-02-answer-guidance.md

Generate approximately 9 multiple-choice and 3 multiple-response items for this topic.
Every item must be scenario-based unless the item is testing a necessary
declarative fact inside a realistic work situation.

Preserve the official objective fields exactly. Do not invent, paraphrase, or
rename the official domain, task, or skill.

Return only a JSON array of draft items using the required schema.
```

```
