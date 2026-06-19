# Question Generation Prompt Intake

## Source

Prompt file supplied for Pilot1:

`docs/Pilot1/aip-c01/source-material/question-generation-prompts.txt`

## Intended Use

Use these prompts to gather candidate AIP-C01 practice questions from LLMs or
other external sources. The raw responses are not approved question-bank items
until reviewed against official AWS sources and the project question-bank
schema.

## Prompt Topics

| Prompt topic | Main accelerated-path day |
|---|---|
| Data Preparation | Day 2 |
| Retrieval Augmented Generation (RAG) | Day 2 and Day 3 |
| Compliance & Data Governance | Day 5 |
| Agentic AI & Tool Use | Day 4 |
| Prompt Engineering & Management | Day 1 and Day 3 |
| App Integration | Day 3 and Day 4 |
| Safety & Moderation | Day 5 |
| Access Control | Day 4 and Day 5 |
| Inference Optimization | Day 6 |
| Monitoring & Observability | Day 6 |
| Model Evaluation | Day 6 |
| Troubleshooting | Day 6 and Day 7 |

## Required Prompt Revisions Before Use

Before sending these prompts to a model, revise them to require:

- official exam name: AWS Certified Generative AI Developer - Professional
  (AIP-C01);
- official domain, task, and skill tags;
- both official question formats: multiple choice and multiple response;
- source traceability to the official exam guide and relevant AWS docs;
- misconception or distractor tags;
- difficulty level;
- remediation target;
- original questions only, with no copied official practice questions,
  proprietary exam dumps, or third-party copyrighted question banks.

## Batch-Size Guardrail

The supplied prompts ask for at least 20 questions each. For first-pass
collection, use smaller batches:

- `5-8` full-schema questions per prompt;
- `8-12` simpler multiple-choice questions only when the target is narrow;
- one official task or skill cluster per prompt.

This is a quality guardrail. Smaller batches reduce repetition, weak
distractors, shallow explanations, and hallucinated AWS claims.
