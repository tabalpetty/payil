# Day 3 Reviewed Candidate Bank

## Review Status

This file is a review/cull pass over normalized draft candidates.
Items marked `reviewed` passed automated schema, scenario, duplicate,
and stale/risky-claim checks, but still require the final source and
coverage gates before being treated as approved question-bank content.

Review date: 2026-06-30
Input: `docs/Pilot1/aip-c01/exam-prep/reviewed/day-03/day-03-normalized-draft-question-bank.md`
Machine-readable feedback: `docs/Pilot1/aip-c01/exam-prep/reviewed/day-03/day-03-review-feedback.json`

## Review Summary

| Curriculum order | Raw normalized | Reviewed candidates | Culled | Completion target | Status |
|---|---:|---:|---:|---:|---|
| Day03-order001 | 13 | 13 | 0 | 10 | candidate-complete |
| Day03-order002 | 13 | 13 | 0 | 10 | candidate-complete |
| Day03-order003 | 13 | 13 | 0 | 10 | candidate-complete |
| Day03-order004 | 12 | 12 | 0 | 10 | candidate-complete |
| Day03-order005 | 13 | 13 | 0 | 10 | candidate-complete |
| Day03-order006 | 12 | 12 | 0 | 10 | candidate-complete |
| Day03-order007 | 12 | 12 | 0 | 10 | candidate-complete |
| Day03-order008 | 13 | 13 | 0 | 10 | candidate-complete |
| Day03-order009 | 13 | 13 | 0 | 10 | candidate-complete |
| Day03-order010 | 18 | 12 | 6 | 10 | candidate-complete |
| Day03-order011 | 13 | 13 | 0 | 10 | candidate-complete |
| Day03-order012 | 13 | 12 | 1 | 10 | candidate-complete |
| Day03-order013 | 13 | 12 | 1 | 10 | candidate-complete |
| Day03-order014 | 12 | 12 | 0 | 10 | candidate-complete |
| Day03-order015 | 25 | 10 | 15 | 10 | candidate-complete |
| Day03-order016 | 13 | 13 | 0 | 10 | candidate-complete |
| Day03-order017 | 12 | 12 | 0 | 10 | candidate-complete |
| Day03-order018 | 17 | 12 | 5 | 10 | candidate-complete |

## Prompt Improvement Signals

| Failure reason | Count | Prompt adjustment |
|---|---:|---|
| schema defect | 24 | Regenerate with the required schema and validate before returning items. |
| source-grounding defect | 24 | Regenerate with an allowed source, source_contract_version, allowed_source_id, and atomic_claims containing claim/source/evidence_span. |
| keyword-trivia stem | 4 | Ban glossary-style or service-name stems; require a professional scenario with a constraint-driven decision. |

## Top-Up Guidance

| Curriculum order | Reviewed candidates | Deficit to 10 | Recommended raw top-up |
|---|---:|---:|---:|
| Day03-order001 | 13 | 0 | 0 |
| Day03-order002 | 13 | 0 | 0 |
| Day03-order003 | 13 | 0 | 0 |
| Day03-order004 | 12 | 0 | 0 |
| Day03-order005 | 13 | 0 | 0 |
| Day03-order006 | 12 | 0 | 0 |
| Day03-order007 | 12 | 0 | 0 |
| Day03-order008 | 13 | 0 | 0 |
| Day03-order009 | 13 | 0 | 0 |
| Day03-order010 | 12 | 0 | 0 |
| Day03-order011 | 13 | 0 | 0 |
| Day03-order012 | 12 | 0 | 0 |
| Day03-order013 | 12 | 0 | 0 |
| Day03-order014 | 12 | 0 | 0 |
| Day03-order015 | 10 | 0 | 0 |
| Day03-order016 | 13 | 0 | 0 |
| Day03-order017 | 12 | 0 | 0 |
| Day03-order018 | 12 | 0 | 0 |

## Review Rules Applied

- Required schema fields must be present after normalization.
- Stems must be scenario-based and avoid keyword-trivia patterns.
- `easy` and `recall` items are culled.
- Exact and near-duplicate stems are culled within the same curriculum-order topic.
- Duplicate culls include both the rejected stem and matched reviewed stem.
- Dated, stale, or high-risk unsupported service-capability claims are culled.
- `source-grounded-v1` items must use a topic allowlist source and include atomic claim evidence.
- Source traces and remediation targets must be present; final source verification remains a later gate.

## Reviewed Candidates

### P1-AIP-D3-001

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-001 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.4: Create advanced search architectures to improve the relevance and accuracy of retrieved information for FM context (for example, by using OpenSearch for semantic search, hybrid search that combines keywords and vectors, Amazon Bedrock reranker models). |
| `secondary_exam_skills` | Skill 4.2.2: Enhance retrieval performance to improve the relevance and speed of retrieved information for FM context augmentation (for example, by using index optimization, query preprocessing, hybrid search implementation with custom scoring). |
| `learning_unit` | Day03-order001 |
| `accelerated_day` | Day 3 |
| `topic` | Hybrid search and custom scoring |
| `knowledge_category` | Skill; Knowledge |
| `knowledge_type` | Procedural; Causal; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order001-local-artifact |
| `raw_source` | 2026-06-30T050949Z-openai-gpt-4.1-day-03-order001.md item 1 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T050949Z |
| `raw_run_id` | order001 |

Stem:

A GenAI development team is dissatisfied with the relevance of results retrieved through keyword search alone. They seek to improve accuracy while supporting a mix of exact string matches and broader semantic matches. Which retrieval architecture offers the best balance of precision and contextual coverage for FM augmentation?

Options:

1. Hybrid search combining keyword and vector search with custom scoring.
2. Pure keyword search with boosted term weights.
3. Vector search only, ignoring all lexical matches.
4. Fuzzy matching on keywords with basic BM25 scoring.

Correct answer: Hybrid search combining keyword and vector search with custom scoring.

Rationale: Hybrid search combines the strength of both keyword and vector (semantic) approaches, letting you tune relevance and deliver results that combine lexical and semantic matching.

Distractors: Pure keyword search with boosted term weights.: Boosting keywords ignores semantic context, failing to retrieve highly relevant but differently worded passages.; Vector search only, ignoring all lexical matches.: Vector-only search may miss exact term matches, which could be critical for FM accuracy in specific scenarios.; Fuzzy matching on keywords with basic BM25 scoring.: While offering some fuzziness, BM25 alone can't cover the broad semantic range needed for nuanced GenAI applications.

Misconception tags: Assuming only one retrieval method is needed; Ignoring tradeoffs between precision and recall

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order001-hybrid-search-custom-scoring.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Hybrid search with custom scoring best balances both exact and contextually relevant matches, as supported in the day-03 artifact.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order001-hybrid-search-custom-scoring.md
   Evidence span: Hybrid search combines lexical and semantic retrieval to balance precision and recall, especially when custom scoring is implemented.

### P1-AIP-D3-002

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-002 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.4: Create advanced search architectures to improve the relevance and accuracy of retrieved information for FM context (for example, by using OpenSearch for semantic search, hybrid search that combines keywords and vectors, Amazon Bedrock reranker models). |
| `secondary_exam_skills` | Skill 4.2.2: Enhance retrieval performance to improve the relevance and speed of retrieved information for FM context augmentation (for example, by using index optimization, query preprocessing, hybrid search implementation with custom scoring). |
| `learning_unit` | Day03-order001 |
| `accelerated_day` | Day 3 |
| `topic` | Hybrid search and custom scoring |
| `knowledge_category` | Skill; Knowledge |
| `knowledge_type` | Procedural; Causal; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | optimize |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order001-local-artifact |
| `raw_source` | 2026-06-30T050949Z-openai-gpt-4.1-day-03-order001.md item 2 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T050949Z |
| `raw_run_id` | order001 |

Stem:

You manage a RAG system that uses OpenSearch's k-NN for vector search and a keyword filter on a legal contracts dataset. Users complain that many relevant documents aren't being surfaced unless their query is verbatim from the contract. What tuning action should you take for maximum retrieval relevance?

Options:

1. Introduce a hybrid search that unifies vector and keyword scoring.
2. Increase the fuzziness level in the keyword filter to accept more typos.
3. Switch exclusively to semantic search and drop the keyword filter.
4. Manually review all queries and adjust them for every user session.

Correct answer: Introduce a hybrid search that unifies vector and keyword scoring.

Rationale: Unifying vector and keyword search ensures relevant documents are retrieved even when query phrasing differs from contract wording, improving recall without sacrificing precision.

Distractors: Increase the fuzziness level in the keyword filter to accept more typos.: Fuzziness addresses typos, not the underlying issue of semantic mismatch between queries and source text.; Switch exclusively to semantic search and drop the keyword filter.: Dropping keyword search risks missing exact legal references that are important for contract applications.; Manually review all queries and adjust them for every user session.: Manual review doesn't scale and misses the point of automated, robust retrieval architecture.

Misconception tags: Over-tuning for edge cases; Confusing typo handling with semantic recall

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order001-hybrid-search-custom-scoring.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Hybrid search is the process for blending both approaches in OpenSearch, providing better recall and relevance.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order001-hybrid-search-custom-scoring.md
   Evidence span: A robust hybrid approach can retrieve documents even when surface-level terms differ, by blending keyword and vector techniques.

### P1-AIP-D3-003

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-003 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.4: Create advanced search architectures to improve the relevance and accuracy of retrieved information for FM context (for example, by using OpenSearch for semantic search, hybrid search that combines keywords and vectors, Amazon Bedrock reranker models). |
| `secondary_exam_skills` | Skill 4.2.2: Enhance retrieval performance to improve the relevance and speed of retrieved information for FM context augmentation (for example, by using index optimization, query preprocessing, hybrid search implementation with custom scoring). |
| `learning_unit` | Day03-order001 |
| `accelerated_day` | Day 3 |
| `topic` | Hybrid search and custom scoring |
| `knowledge_category` | Skill; Knowledge |
| `knowledge_type` | Procedural; Causal; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | optimize |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order001-local-artifact |
| `raw_source` | 2026-06-30T050949Z-openai-gpt-4.1-day-03-order001.md item 3 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T050949Z |
| `raw_run_id` | order001 |

Stem:

An AI product manager wants lightning-fast retrievals for customer Q&A, but complains about the occasional appearance of irrelevant results. Custom scoring in the search pipeline is available. Which adjustment most directly increases result relevance while controlling for performance?

Options:

1. Weight vector similarity higher than keyword scores in the custom scoring function.
2. Switch to a pure keyword search for all queries.
3. Increase the number of vector dimensions in embeddings.
4. Enable deep full-text indexing for all documents regardless of size.

Correct answer: Weight vector similarity higher than keyword scores in the custom scoring function.

Rationale: Careful tuning of the custom scoring formula lets you emphasize semantic similarity without sacrificing speed, directly impacting relevance.

Distractors: Switch to a pure keyword search for all queries.: This risks losing contextually relevant answers if the query and answer wordings differ.; Increase the number of vector dimensions in embeddings.: More dimensions can improve expressivity, but also increase latency and complexity, with diminishing returns if the search function is not optimized.; Enable deep full-text indexing for all documents regardless of size.: Full-text indexing improves keyword recall but may harm performance and does not solve semantic matching.

Misconception tags: Assuming search dimension tuning solves all accuracy issues; Misunderstanding tradeoff between relevance and speed

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order001-hybrid-search-custom-scoring.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Changing custom scoring is the correct and most direct lever per the artifact, and controls both performance and relevance.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order001-hybrid-search-custom-scoring.md
   Evidence span: Custom scoring lets you balance relevance, weighting either vector or keyword matches as scenario needs.

### P1-AIP-D3-004

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-004 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.4: Create advanced search architectures to improve the relevance and accuracy of retrieved information for FM context (for example, by using OpenSearch for semantic search, hybrid search that combines keywords and vectors, Amazon Bedrock reranker models). |
| `secondary_exam_skills` | Skill 4.2.2: Enhance retrieval performance to improve the relevance and speed of retrieved information for FM context augmentation (for example, by using index optimization, query preprocessing, hybrid search implementation with custom scoring). |
| `learning_unit` | Day03-order001 |
| `accelerated_day` | Day 3 |
| `topic` | Hybrid search and custom scoring |
| `knowledge_category` | Skill; Knowledge |
| `knowledge_type` | Procedural; Causal; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order001-local-artifact |
| `raw_source` | 2026-06-30T050949Z-openai-gpt-4.1-day-03-order001.md item 4 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T050949Z |
| `raw_run_id` | order001 |

Stem:

You are troubleshooting a RAG pipeline that uses OpenSearch with a hybrid search setup. Relevance is high for queries with both lexical and semantic overlap, but users are missing highly specific, keyword-heavy results for rare technical terms. What custom scoring strategy should be applied?

Options:

1. Increase keyword score contribution for rare or domain-specific terms.
2. Remove the vector component to prioritize keyword-only matches.
3. Lower the candidate result set size to only top N vector matches.
4. Use default scoring without any adjustments.

Correct answer: Increase keyword score contribution for rare or domain-specific terms.

Rationale: Increasing lexical score for rare keywords ensures highly specific queries retrieve precise matches, addressing the scenario issue.

Distractors: Remove the vector component to prioritize keyword-only matches.: Removing vector search could hurt performance for general queries.; Lower the candidate result set size to only top N vector matches.: Reducing the pool will decrease overall recall, especially for rare keywords if those are not well embedded.; Use default scoring without any adjustments.: The default does not resolve the issue for domain-specific precision.

Misconception tags: Assuming generic scoring is always sufficient; Thinking vector search always substitutes for keyword importance

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order001-hybrid-search-custom-scoring.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Per the source, custom scoring enables raising weights for specific keywords as needed.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order001-hybrid-search-custom-scoring.md
   Evidence span: Scoring can be tuned so that rare keyword terms get extra weight, enabling domain control.

### P1-AIP-D3-005

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-005 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.4: Create advanced search architectures to improve the relevance and accuracy of retrieved information for FM context (for example, by using OpenSearch for semantic search, hybrid search that combines keywords and vectors, Amazon Bedrock reranker models). |
| `secondary_exam_skills` | Skill 4.2.2: Enhance retrieval performance to improve the relevance and speed of retrieved information for FM context augmentation (for example, by using index optimization, query preprocessing, hybrid search implementation with custom scoring). |
| `learning_unit` | Day03-order001 |
| `accelerated_day` | Day 3 |
| `topic` | Hybrid search and custom scoring |
| `knowledge_category` | Skill; Knowledge |
| `knowledge_type` | Procedural; Causal; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | design |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order001-local-artifact |
| `raw_source` | 2026-06-30T050949Z-openai-gpt-4.1-day-03-order001.md item 5 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T050949Z |
| `raw_run_id` | order001 |

Stem:

A data architect is asked to design a document retrieval pipeline for a multilingual knowledge base. Which option offers the best tradeoff between retrieval accuracy and language flexibility for FM input context?

Options:

1. Use a hybrid search engine with language-specific embedding models and lexical analyzers.
2. Rely on basic BM25 for keyword retrieval in all languages.
3. Convert all documents to English and use English-only embeddings.
4. Use vector search alone with a multilingual embedding, without keyword fallback.

Correct answer: Use a hybrid search engine with language-specific embedding models and lexical analyzers.

Rationale: Integrating both embeddings and lexers for each language ensures both exact and semantic match, maximizing accuracy and flexibility.

Distractors: Rely on basic BM25 for keyword retrieval in all languages.: BM25 lacks semantic support and won't handle synonym-rich or phrased concepts in other languages.; Convert all documents to English and use English-only embeddings.: Language conversion introduces loss and complexity, risking data fidelity and context.; Use vector search alone with a multilingual embedding, without keyword fallback.: Vector-only ignores critical lexical matches in some languages, limiting high-precision cases.

Misconception tags: Assuming one model/language fits all; Missing hybrid approach for multilingual data

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order001-hybrid-search-custom-scoring.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Per the artifact, the best tradeoff for multilingual retrieval is language-tuned hybrid search.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order001-hybrid-search-custom-scoring.md
   Evidence span: Hybrid methods can be adapted for multiple languages by pairing language-specific analyzers and embedding models.

### P1-AIP-D3-006

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-006 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.4: Create advanced search architectures to improve the relevance and accuracy of retrieved information for FM context (for example, by using OpenSearch for semantic search, hybrid search that combines keywords and vectors, Amazon Bedrock reranker models). |
| `secondary_exam_skills` | Skill 4.2.2: Enhance retrieval performance to improve the relevance and speed of retrieved information for FM context augmentation (for example, by using index optimization, query preprocessing, hybrid search implementation with custom scoring). |
| `learning_unit` | Day03-order001 |
| `accelerated_day` | Day 3 |
| `topic` | Hybrid search and custom scoring |
| `knowledge_category` | Skill; Knowledge |
| `knowledge_type` | Procedural; Causal; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | implement |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order001-local-artifact |
| `raw_source` | 2026-06-30T050949Z-openai-gpt-4.1-day-03-order001.md item 6 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T050949Z |
| `raw_run_id` | order001 |

Stem:

A GenAI developer wants to add product recency as an additional ranking factor to OpenSearch hybrid search for a dynamic retailer FAQ. Which action most directly implements this requirement?

Options:

1. Customize the hybrid scoring function to add a recency weight to candidate documents.
2. Train a new embedding model on recent product descriptions.
3. Switch to only keyword search with date filters.
4. Add recency metadata to the document index but do not modify the scoring.

Correct answer: Customize the hybrid scoring function to add a recency weight to candidate documents.

Rationale: Modifying the scoring function directly incorporates recency as a factor in final ranking, blending it alongside keyword and vector scores.

Distractors: Train a new embedding model on recent product descriptions.: Training new embeddings could improve semantic matching but doesn't control explicit recency ranking.; Switch to only keyword search with date filters.: Abandoning hybrid weakens semantic coverage and flexibility.; Add recency metadata to the document index but do not modify the scoring.: Metadata alone does nothing unless the scoring uses it.

Misconception tags: Assuming metadata alone impacts relevance; Confusing data attributes with scoring logic

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order001-hybrid-search-custom-scoring.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The artifact explains how custom scoring can incorporate additional ranking signals such as recency.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order001-hybrid-search-custom-scoring.md
   Evidence span: Custom scoring can add factors like recency, popularity, or domain importance.

### P1-AIP-D3-007

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-007 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.4: Create advanced search architectures to improve the relevance and accuracy of retrieved information for FM context (for example, by using OpenSearch for semantic search, hybrid search that combines keywords and vectors, Amazon Bedrock reranker models). |
| `secondary_exam_skills` | Skill 4.2.2: Enhance retrieval performance to improve the relevance and speed of retrieved information for FM context augmentation (for example, by using index optimization, query preprocessing, hybrid search implementation with custom scoring). |
| `learning_unit` | Day03-order001 |
| `accelerated_day` | Day 3 |
| `topic` | Hybrid search and custom scoring |
| `knowledge_category` | Skill; Knowledge |
| `knowledge_type` | Procedural; Causal; Conditional |
| `question_format` | multiple-response |
| `difficulty` | hard |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order001-local-artifact |
| `raw_source` | 2026-06-30T050949Z-openai-gpt-4.1-day-03-order001.md item 7 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T050949Z |
| `raw_run_id` | order001 |

Stem:

During an experiment, you find that your RAG pipeline's hybrid OpenSearch queries surface too many loosely related results and too few precise answers. Which two actions are most appropriate to make retrieval stricter without sacrificing semantic recall?

Options:

1. Increase the minimum combined threshold score for candidate selection.
2. Raise the minimum keyword match requirement before semantic scoring.
3. Reduce the allowed number of returned candidates.
4. Lower the vector similarity threshold to allow more semantic matches.

Correct answer: Increase the minimum combined threshold score for candidate selection.; Raise the minimum keyword match requirement before semantic scoring.

Rationale: Increasing the overall threshold and ensuring strong keyword matches together narrow results to more relevant documents without disabling semantic augmentation.

Distractors: Reduce the allowed number of returned candidates.: This might remove both relevant and irrelevant results without improving strictness per document.; Lower the vector similarity threshold to allow more semantic matches.: Lowering this threshold increases the number of vaguely related results, exacerbating the problem.

Misconception tags: Confusing result limit with relevance filtering; Thinking lower semantic threshold increases strictness

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order001-hybrid-search-custom-scoring.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: These two configuration changes are recommended for tuning hybrid search strictness in the artifact.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order001-hybrid-search-custom-scoring.md
   Evidence span: Filtering by both minimum relevance score and strong lexical match controls precision in hybrid search.

### P1-AIP-D3-008

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-008 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.4: Create advanced search architectures to improve the relevance and accuracy of retrieved information for FM context (for example, by using OpenSearch for semantic search, hybrid search that combines keywords and vectors, Amazon Bedrock reranker models). |
| `secondary_exam_skills` | Skill 4.2.2: Enhance retrieval performance to improve the relevance and speed of retrieved information for FM context augmentation (for example, by using index optimization, query preprocessing, hybrid search implementation with custom scoring). |
| `learning_unit` | Day03-order001 |
| `accelerated_day` | Day 3 |
| `topic` | Hybrid search and custom scoring |
| `knowledge_category` | Skill; Knowledge |
| `knowledge_type` | Procedural; Causal; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | optimize |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order001-local-artifact |
| `raw_source` | 2026-06-30T050949Z-openai-gpt-4.1-day-03-order001.md item 8 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T050949Z |
| `raw_run_id` | order001 |

Stem:

Your GenAI chat application retrieves context via a hybrid search layer but performance is lagging. Index optimization is possible. Which index design change most likely boosts retrieval speed for frequent queries without sacrificing result quality?

Options:

1. Optimize index sharding and mapping for high query concurrency.
2. Reduce the vector dimension to minimize storage consumption.
3. Switch to a single global dense vector for each document.
4. Remove all keyword analyzers to focus solely on vector search.

Correct answer: Optimize index sharding and mapping for high query concurrency.

Rationale: Improved sharding and well-mapped indices enable parallelism and throughput, supporting fast retrieval needed by interactive GenAI applications.

Distractors: Reduce the vector dimension to minimize storage consumption.: Smaller vectors may compromise semantic precision, impacting quality.; Switch to a single global dense vector for each document.: One vector per document fails to capture sections or multi-faceted information well, reducing retrieval fidelity.; Remove all keyword analyzers to focus solely on vector search.: This would reduce hybrid capability and hurt precise term search.

Misconception tags: Assuming dimension reduction automatically improves performance; Over-simplifying vector mapping

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order001-hybrid-search-custom-scoring.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The artifact identifies index sharding and mapping as core levers for performance in hybrid systems.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order001-hybrid-search-custom-scoring.md
   Evidence span: Index optimization (like sharding and mapping) increases retrieval speed for high-load systems without sacrificing quality.

### P1-AIP-D3-009

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-009 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.4: Create advanced search architectures to improve the relevance and accuracy of retrieved information for FM context (for example, by using OpenSearch for semantic search, hybrid search that combines keywords and vectors, Amazon Bedrock reranker models). |
| `secondary_exam_skills` | Skill 4.2.2: Enhance retrieval performance to improve the relevance and speed of retrieved information for FM context augmentation (for example, by using index optimization, query preprocessing, hybrid search implementation with custom scoring). |
| `learning_unit` | Day03-order001 |
| `accelerated_day` | Day 3 |
| `topic` | Hybrid search and custom scoring |
| `knowledge_category` | Skill; Knowledge |
| `knowledge_type` | Procedural; Causal; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order001-local-artifact |
| `raw_source` | 2026-06-30T050949Z-openai-gpt-4.1-day-03-order001.md item 9 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T050949Z |
| `raw_run_id` | order001 |

Stem:

A critical QA workflow depends on precise legal terms being matched during retrieval in a hybrid search RAG architecture. Precision drops when legalese appears only in some documents. What combination of search configuration actions most directly addresses recall and precision?

Options:

1. Boost keyword term weighting for known legal phrases and combine with semantic ranking.
2. Disable keyword search to rely on better embeddings.
3. Increase the size of the vector candidate pool only.
4. Use a stop-words filter to ignore legal terminology.

Correct answer: Boost keyword term weighting for known legal phrases and combine with semantic ranking.

Rationale: Boosting critical keywords while keeping semantic ranking addresses both precision (for exact terms) and recall (for paraphrased matches).

Distractors: Disable keyword search to rely on better embeddings.: This risks missing exact legal matches required in legal QA.; Increase the size of the vector candidate pool only.: A larger pool alone won't ensure critical legal terms are surfaced.; Use a stop-words filter to ignore legal terminology.: This would likely filter out the very terms you want to prioritize.

Misconception tags: Assuming stop-words filters help recall; Assuming more candidates improves precision

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order001-hybrid-search-custom-scoring.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Boosted weighting of legal keywords plus semantic ranking is directly advised in the artifact for this scenario.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order001-hybrid-search-custom-scoring.md
   Evidence span: Hybrid search can boost certain terms within the keyword component to guarantee precise recall.

### P1-AIP-D3-010

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-010 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.4: Create advanced search architectures to improve the relevance and accuracy of retrieved information for FM context (for example, by using OpenSearch for semantic search, hybrid search that combines keywords and vectors, Amazon Bedrock reranker models). |
| `secondary_exam_skills` | Skill 4.2.2: Enhance retrieval performance to improve the relevance and speed of retrieved information for FM context augmentation (for example, by using index optimization, query preprocessing, hybrid search implementation with custom scoring). |
| `learning_unit` | Day03-order001 |
| `accelerated_day` | Day 3 |
| `topic` | Hybrid search and custom scoring |
| `knowledge_category` | Skill; Knowledge |
| `knowledge_type` | Procedural; Causal; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order001-local-artifact |
| `raw_source` | 2026-06-30T050949Z-openai-gpt-4.1-day-03-order001.md item 10 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T050949Z |
| `raw_run_id` | order001 |

Stem:

An FM-augmented question-answering system retrieves both news headlines and technical documentation. End-users complain about stale or outdated information surfacing first. With access to a hybrid search architecture, which configuration changes best help resolve this?

Options:

1. Incorporate document freshness into the custom scoring function.
2. Decrease the embedding size to allow more documents to be stored.
3. Sort results by document length rather than score.
4. Use keyword search only to favor exact matches.

Correct answer: Incorporate document freshness into the custom scoring function.

Rationale: Custom scoring can dynamically prioritize recent documents, directly addressing the staleness problem.

Distractors: Decrease the embedding size to allow more documents to be stored.: More documents do not directly address ranking or freshness.; Sort results by document length rather than score.: Longer documents aren't inherently more relevant or up-to-date.; Use keyword search only to favor exact matches.: Exact matches may still select old content if freshness is not a factor.

Misconception tags: Assuming storage tradeoffs replace ranking logic; Ignoring scoring for temporal signals

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order001-hybrid-search-custom-scoring.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The artifact recommends scoring configuration to include freshness or recency for up-to-date retrievals.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order001-hybrid-search-custom-scoring.md
   Evidence span: Recency and freshness can be added to hybrid scoring for timeliness.

### P1-AIP-D3-011

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-011 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.4: Create advanced search architectures to improve the relevance and accuracy of retrieved information for FM context (for example, by using OpenSearch for semantic search, hybrid search that combines keywords and vectors, Amazon Bedrock reranker models). |
| `secondary_exam_skills` | Skill 4.2.2: Enhance retrieval performance to improve the relevance and speed of retrieved information for FM context augmentation (for example, by using index optimization, query preprocessing, hybrid search implementation with custom scoring). |
| `learning_unit` | Day03-order001 |
| `accelerated_day` | Day 3 |
| `topic` | Hybrid search and custom scoring |
| `knowledge_category` | Skill; Knowledge |
| `knowledge_type` | Procedural; Causal; Conditional |
| `question_format` | multiple-response |
| `difficulty` | hard |
| `cognitive_demand` | optimize |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order001-local-artifact |
| `raw_source` | 2026-06-30T050949Z-openai-gpt-4.1-day-03-order001.md item 11 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T050949Z |
| `raw_run_id` | order001 |

Stem:

After deploying a hybrid search solution for customer-support chat, you notice some queries for highly specialized products always return low relevance. What two steps can you take to improve accurate retrieval for niche queries while preserving general recall for broader ones?

Options:

1. Fine-tune custom scoring to increase keyword weight for niche product terms.
2. Expand the vector embedding vocabulary to better encode rare terms.
3. Add synonym expansion at the keyword layer only.
4. Reduce semantic threshold for all queries.
5. Separate support content into granular document chunks.

Correct answer: Fine-tune custom scoring to increase keyword weight for niche product terms.; Separate support content into granular document chunks.

Rationale: Boosting keyword scoring for niche terms and chunking content improves precision for difficult cases while supporting overall recall.

Distractors: Expand the vector embedding vocabulary to better encode rare terms.: Expanding vocabularies can help, but without scoring changes, retrieval may remain suboptimal.; Add synonym expansion at the keyword layer only.: Synonym expansion improves recall in common cases but doesn't specifically help niche, highly specific queries.; Reduce semantic threshold for all queries.: Reducing semantic threshold could boost irrelevant results overall.

Misconception tags: Assuming synonym expansion is always sufficient; Lowering thresholds without considering noise

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order001-hybrid-search-custom-scoring.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Artifact explicitly lists both scoring fine-tuning and chunking as necessary improvements for tough retrieval cases.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order001-hybrid-search-custom-scoring.md
   Evidence span: Custom scoring and document chunking are strategies for improving targeted recall and precision.

### P1-AIP-D3-012

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-012 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.4: Create advanced search architectures to improve the relevance and accuracy of retrieved information for FM context (for example, by using OpenSearch for semantic search, hybrid search that combines keywords and vectors, Amazon Bedrock reranker models). |
| `secondary_exam_skills` | Skill 4.2.2: Enhance retrieval performance to improve the relevance and speed of retrieved information for FM context augmentation (for example, by using index optimization, query preprocessing, hybrid search implementation with custom scoring). |
| `learning_unit` | Day03-order001 |
| `accelerated_day` | Day 3 |
| `topic` | Hybrid search and custom scoring |
| `knowledge_category` | Skill; Knowledge |
| `knowledge_type` | Procedural; Causal; Conditional |
| `question_format` | multiple-response |
| `difficulty` | exam-plus |
| `cognitive_demand` | design |
| `estimated_time_seconds` | 180 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order001-local-artifact |
| `raw_source` | 2026-06-30T050949Z-openai-gpt-4.1-day-03-order001.md item 12 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T050949Z |
| `raw_run_id` | order001 |

Stem:

You are asked to design a retrieval process for a real-time assistant with both strict latency limits and a hard requirement that no relevant context be missed for FM prompts. What hybrid search configuration (choose TWO) should you prioritize?

Options:

1. Tune custom scoring to favor precision when low latency is required.
2. Set maximum candidate document count for each query to limit processing time.
3. Include both BM25 and dense vector retrieval with weighted fusion.
4. Disable hybrid search and use only semantic search.
5. Schedule periodic rebalancing of index shards during low-traffic windows.

Correct answer: Tune custom scoring to favor precision when low latency is required.; Include both BM25 and dense vector retrieval with weighted fusion.

Rationale: Weighted fusion balances speed and relevance, and precision-tuned scoring keeps latency under control for real-time needs.

Distractors: Set maximum candidate document count for each query to limit processing time.: Capping candidates risks missing necessary context for FM prompts.; Disable hybrid search and use only semantic search.: FM prompts may lose precise matches vital for top-quality context supply.; Schedule periodic rebalancing of index shards during low-traffic windows.: Useful for maintenance but not directly relevant to retrieval/relevance per prompt.

Misconception tags: Focusing solely on document count for latency; Excluding hybrid search from real-time architectures

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order001-hybrid-search-custom-scoring.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Fusion and custom scoring best satisfy strict latency and full-context requirements as per the artifact.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order001-hybrid-search-custom-scoring.md
   Evidence span: Weighted fusion and custom scoring are required for hybrid search under strict latency and recall conditions.

### P1-AIP-D3-013

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-013 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.4: Create advanced search architectures to improve the relevance and accuracy of retrieved information for FM context (for example, by using OpenSearch for semantic search, hybrid search that combines keywords and vectors, Amazon Bedrock reranker models). |
| `secondary_exam_skills` | Skill 4.2.2: Enhance retrieval performance to improve the relevance and speed of retrieved information for FM context augmentation (for example, by using index optimization, query preprocessing, hybrid search implementation with custom scoring). |
| `learning_unit` | Day03-order001 |
| `accelerated_day` | Day 3 |
| `topic` | Hybrid search and custom scoring |
| `knowledge_category` | Skill; Knowledge |
| `knowledge_type` | Procedural; Causal; Conditional |
| `question_format` | multiple-response |
| `difficulty` | exam-plus |
| `cognitive_demand` | optimize |
| `estimated_time_seconds` | 180 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order001-local-artifact |
| `raw_source` | 2026-06-30T050949Z-openai-gpt-4.1-day-03-order001.md item 13 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T050949Z |
| `raw_run_id` | order001 |

Stem:

An FM augmentation team must maintain both high-speed retrieval and rigorous accuracy for medical research use-cases. What hybrid search design choices (choose TWO) are most appropriate according to best practice?

Options:

1. Enable hybrid scoring with domain keyword boosting and tuned vector similarity.
2. Prioritize vector search alone with aggressive candidate filtering.
3. Integrate custom scoring functions that penalize out-of-date documents.
4. Lower all relevance thresholds to boost recall at any cost.
5. Store all documents in a single index without specialized analyzers.

Correct answer: Enable hybrid scoring with domain keyword boosting and tuned vector similarity.; Integrate custom scoring functions that penalize out-of-date documents.

Rationale: Hybrid boosting and out-of-date penalties ensure both timely and relevant context for FM, directly addressing medical research needs.

Distractors: Prioritize vector search alone with aggressive candidate filtering.: This may miss exact domain matches crucial for medical accuracy.; Lower all relevance thresholds to boost recall at any cost.: Recall boost at the expense of precision/speed risks QC and safety.; Store all documents in a single index without specialized analyzers.: No analyzers limit both performance and language/domain handling.

Misconception tags: Assuming recall is all that matters for medical Q&A; Underestimating domain ranking and freshness

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order001-hybrid-search-custom-scoring.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: High-accuracy hybrid search uses domain boosting and penalizes stale docs per best practice in the artifact.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order001-hybrid-search-custom-scoring.md
   Evidence span: Hybrid search should prioritize both relevance (domain boosting) and freshness for critical domains.

### P1-AIP-D3-014

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-014 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.4: Create advanced search architectures to improve the relevance and accuracy of retrieved information for FM context (for example, by using OpenSearch for semantic search, hybrid search that combines keywords and vectors, Amazon Bedrock reranker models). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order002 |
| `accelerated_day` | Day 3 |
| `topic` | Reranking |
| `knowledge_category` | Skill; Knowledge |
| `knowledge_type` | Procedural; Causal; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | optimize |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order002-local-artifact |
| `raw_source` | 2026-06-30T051032Z-openai-gpt-4.1-day-03-order002.md item 1 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051032Z |
| `raw_run_id` | order002 |

Stem:

A team is deploying a RAG-based application that retrieves candidate passages using a hybrid search, but user evaluations show that the top results frequently miss relevant context. You are tasked with improving the relevance of the returned passages without significantly increasing latency or re-indexing. What is the most appropriate next step?

Options:

1. Implement a reranking model on the set of retrieved passages before sending to the Foundation Model.
2. Adjust the similarity threshold in the vector search to retrieve more passages.
3. Switch to using keyword search only to ensure exact matches.
4. Increase the embedding dimension in the vector store for better retrieval accuracy.

Correct answer: Implement a reranking model on the set of retrieved passages before sending to the Foundation Model.

Rationale: Reranking the initial results using a dedicated model allows for improved relevance without modifying the retrieval or search architecture or increasing recall-related noise.

Distractors: Adjust the similarity threshold in the vector search to retrieve more passages.: This increases recall, not necessarily relevance, and may worsen noise without intelligent ranking.; Switch to using keyword search only to ensure exact matches.: Keyword-only search can reduce the recall of semantically relevant passages and misses the benefits of semantic relevance.; Increase the embedding dimension in the vector store for better retrieval accuracy.: Increasing embedding dimension affects storage and search, not post-retrieval ranking, and doesn’t address ranking of equally scored candidates.

Misconception tags: Ranking vs recall; tool vs architecture

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order002-reranking.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The source states that reranking approaches improve relevance by reordering the context, addressing the scenario’s constraint of not changing the retrieval setup.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order002-reranking.md
   Evidence span: Reranking models can reorder retrieved results to maximize relevance for context injection without altering retrieval.

### P1-AIP-D3-015

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-015 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.4: Create advanced search architectures to improve the relevance and accuracy of retrieved information for FM context (for example, by using OpenSearch for semantic search, hybrid search that combines keywords and vectors, Amazon Bedrock reranker models). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order002 |
| `accelerated_day` | Day 3 |
| `topic` | Reranking |
| `knowledge_category` | Skill; Knowledge |
| `knowledge_type` | Procedural; Causal; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order002-local-artifact |
| `raw_source` | 2026-06-30T051032Z-openai-gpt-4.1-day-03-order002.md item 2 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051032Z |
| `raw_run_id` | order002 |

Stem:

You have observed that your OpenSearch-based RAG pipeline consistently returns top-ranked results that match the query’s keywords but fail in semantic relevance. Which change will most directly address this ranking gap?

Options:

1. Integrate a model-based reranking step after candidate retrieval.
2. Switch from OpenSearch to a custom-developed vector database.
3. Reduce the size of the candidate pool for initial retrieval.
4. Configure OpenSearch to use only semantic vector scoring.

Correct answer: Integrate a model-based reranking step after candidate retrieval.

Rationale: Model-based reranking can explicitly prioritize outputs on semantic relevance beyond keyword matching.

Distractors: Switch from OpenSearch to a custom-developed vector database.: Changing platforms does not solve ranking unless a reranking mechanism is implemented.; Reduce the size of the candidate pool for initial retrieval.: Reducing the candidate pool may drop relevant documents and exacerbate relevance misses.; Configure OpenSearch to use only semantic vector scoring.: This may harm keyword matches; hybrid approaches often require reranking to balance precision and recall.

Misconception tags: Platform vs algorithm; Tuning vs reranking

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order002-reranking.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The artifact describes the explicit benefit of reranking for improving semantic relevance in hybrid retrieval architectures.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order002-reranking.md
   Evidence span: Applying a dedicated reranker to the outputs can give semantic relevance more influence over keyword matches.

### P1-AIP-D3-016

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-016 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.4: Create advanced search architectures to improve the relevance and accuracy of retrieved information for FM context (for example, by using OpenSearch for semantic search, hybrid search that combines keywords and vectors, Amazon Bedrock reranker models). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order002 |
| `accelerated_day` | Day 3 |
| `topic` | Reranking |
| `knowledge_category` | Skill; Knowledge |
| `knowledge_type` | Procedural; Causal; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | optimize |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order002-local-artifact |
| `raw_source` | 2026-06-30T051032Z-openai-gpt-4.1-day-03-order002.md item 3 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051032Z |
| `raw_run_id` | order002 |

Stem:

A developer notices that integrating a reranker into their passage retrieval workflow increases end-to-end latency by 10%. Stakeholders want to preserve relevance improvements without degrading user experience. Which approach offers the best tradeoff in this scenario?

Options:

1. Limit reranking to only the top-N retrieved results rather than the whole candidate set.
2. Disable reranking and rely solely on the base retrieval order.
3. Parallelize both retrieval and reranking for all candidates, regardless of necessity.
4. Switch to a less accurate, lightweight retriever and remove reranking.

Correct answer: Limit reranking to only the top-N retrieved results rather than the whole candidate set.

Rationale: Reranking the top-N allows improvement of relevance while controlling latency overhead by reducing reranker workload.

Distractors: Disable reranking and rely solely on the base retrieval order.: This sacrifices improved relevance achieved via reranking, failing the stakeholder goal.; Parallelize both retrieval and reranking for all candidates, regardless of necessity.: Unbounded parallelization creates compute and cost risks; not practical or efficient for all scenarios.; Switch to a less accurate, lightweight retriever and remove reranking.: This would likely result in a net drop in relevance and accuracy.

Misconception tags: Latency tradeoff; Performance vs recall

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order002-reranking.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The guidance notes that reranking a limited subset of results is a best practice for balancing latency and ranking gain.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order002-reranking.md
   Evidence span: Limiting reranking to a small pool of candidates controls performance costs while improving top-ranked output.

### P1-AIP-D3-017

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-017 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.4: Create advanced search architectures to improve the relevance and accuracy of retrieved information for FM context (for example, by using OpenSearch for semantic search, hybrid search that combines keywords and vectors, Amazon Bedrock reranker models). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order002 |
| `accelerated_day` | Day 3 |
| `topic` | Reranking |
| `knowledge_category` | Skill; Knowledge |
| `knowledge_type` | Procedural; Causal; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order002-local-artifact |
| `raw_source` | 2026-06-30T051032Z-openai-gpt-4.1-day-03-order002.md item 4 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051032Z |
| `raw_run_id` | order002 |

Stem:

A team builds a pipeline that uses a keyword search followed by a Bedrock reranker. User feedback indicates that the answers occasionally lack supporting details. Which next action is most likely to resolve this complaint without degrading system relevance?

Options:

1. Increase the initial retrieval pool size before reranking.
2. Switch to pure semantic search only.
3. Lower the relevance threshold of the reranker to accept more results.
4. Remove the reranking step and present all retrieved results.

Correct answer: Increase the initial retrieval pool size before reranking.

Rationale: Increasing the retrieval pool brings in more candidates with potential supporting detail, which reranking can then sift for relevance.

Distractors: Switch to pure semantic search only.: This could lose high-precision keyword matches valued by the hybrid approach.; Lower the relevance threshold of the reranker to accept more results.: This may increase noise; the issue is with candidate inputs, not reranker threshold.; Remove the reranking step and present all retrieved results.: This overloads the FM context with irrelevant material, harming answer quality.

Misconception tags: Input vs ranking; Hybrid search control

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order002-reranking.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Expanding the candidate pool is recommended for enabling rerankers to select additional, more useful context.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order002-reranking.md
   Evidence span: Increasing the pool of candidates allows reranking to surface more relevant supporting context.

### P1-AIP-D3-018

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-018 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.4: Create advanced search architectures to improve the relevance and accuracy of retrieved information for FM context (for example, by using OpenSearch for semantic search, hybrid search that combines keywords and vectors, Amazon Bedrock reranker models). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order002 |
| `accelerated_day` | Day 3 |
| `topic` | Reranking |
| `knowledge_category` | Skill; Knowledge |
| `knowledge_type` | Procedural; Causal; Conditional |
| `question_format` | multiple-response |
| `difficulty` | exam-plus |
| `cognitive_demand` | optimize |
| `estimated_time_seconds` | 180 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order002-local-artifact |
| `raw_source` | 2026-06-30T051032Z-openai-gpt-4.1-day-03-order002.md item 5 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051032Z |
| `raw_run_id` | order002 |

Stem:

A technical lead wants to reduce hallucination in answers generated by a GenAI FM in a RAG architecture with hybrid retrieval. Which combination of actions below best supports this goal? (Choose TWO.)

Options:

1. Use a reranking model to maximize the factual alignment of retrieved passages.
2. Limit FM context injection to the top reranked passages only.
3. Increase the total number of candidate passages provided to the FM.
4. Switch off reranking to reduce latency.
5. Use a keyword-only retriever and skip semantic filtering.

Correct answer: Use a reranking model to maximize the factual alignment of retrieved passages.; Limit FM context injection to the top reranked passages only.

Rationale: Rerankers help ensure the most factually relevant context is injected, and limiting injection reduces risk of noisy or off-topic information.

Distractors: Increase the total number of candidate passages provided to the FM.: More passages increase context window risk and raise hallucination likelihood.; Switch off reranking to reduce latency.: This sacrifices retrieval quality, which can worsen factual alignment.; Use a keyword-only retriever and skip semantic filtering.: This ignores semantic alignment and allows irrelevant or misaligned inputs.

Misconception tags: RAG pipeline control; Context window management

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order002-reranking.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Both actions follow best practice for minimizing FM hallucination by optimizing context selection for factual alignment.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order002-reranking.md
   Evidence span: Injecting only reranked, most-relevant context curbs hallucination risk.

### P1-AIP-D3-019

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-019 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.4: Create advanced search architectures to improve the relevance and accuracy of retrieved information for FM context (for example, by using OpenSearch for semantic search, hybrid search that combines keywords and vectors, Amazon Bedrock reranker models). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order002 |
| `accelerated_day` | Day 3 |
| `topic` | Reranking |
| `knowledge_category` | Skill; Knowledge |
| `knowledge_type` | Procedural; Causal; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order002-local-artifact |
| `raw_source` | 2026-06-30T051032Z-openai-gpt-4.1-day-03-order002.md item 6 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051032Z |
| `raw_run_id` | order002 |

Stem:

An application is returning inconsistent results: some queries receive highly relevant answers, while others seem completely off-base. Recent logs show that for the problematic queries, only the base retriever was used, and reranking was bypassed. What is the best explanation for this observation?

Options:

1. Reranking was needed to reorder marginally relevant candidates for those queries.
2. The initial retriever always guarantees high relevance, so reranking is unnecessary.
3. Reranking increases system noise and should never be used.
4. Keyword retrieval performs better than reranking for all query types.

Correct answer: Reranking was needed to reorder marginally relevant candidates for those queries.

Rationale: Bypassing reranking loses the opportunity to surface the most relevant candidates for context injection, leading to reduced answer quality.

Distractors: The initial retriever always guarantees high relevance, so reranking is unnecessary.: Retrievers, especially in hybrid architectures, require reranking to optimize final candidate order.; Reranking increases system noise and should never be used.: Reranking is a best practice for increasing, not reducing, retrieval quality.; Keyword retrieval performs better than reranking for all query types.: Semantic and hybrid approaches outperform pure keyword in most FM augmentation contexts.

Misconception tags: Retriever vs reranker role; Quality assumptions

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order002-reranking.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The artifact explains retrievers alone are insufficient for optimal relevance; rerankers are critical for consistent output quality.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order002-reranking.md
   Evidence span: Rerankers reorder candidates on subtle relevance signals missed by retrievers.

### P1-AIP-D3-020

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-020 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.4: Create advanced search architectures to improve the relevance and accuracy of retrieved information for FM context (for example, by using OpenSearch for semantic search, hybrid search that combines keywords and vectors, Amazon Bedrock reranker models). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order002 |
| `accelerated_day` | Day 3 |
| `topic` | Reranking |
| `knowledge_category` | Skill; Knowledge |
| `knowledge_type` | Procedural; Causal; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | explain |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order002-local-artifact |
| `raw_source` | 2026-06-30T051032Z-openai-gpt-4.1-day-03-order002.md item 7 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051032Z |
| `raw_run_id` | order002 |

Stem:

A company’s RAG pipeline uses candidate pooling from multiple retrievers, including OpenSearch and an internal custom index. The system often returns context from only one source. How would adding a reranking stage impact the pipeline?

Options:

1. It ensures that candidates from all retrievers are compared and ordered by relevance for the user’s query.
2. It prevents candidates from the custom index from being included.
3. It only uses candidates from the highest-scoring retrieval source.
4. It merges the content of all candidates into a single passage.

Correct answer: It ensures that candidates from all retrievers are compared and ordered by relevance for the user’s query.

Rationale: Reranking considers all candidate passages together, regardless of retrieval source, and produces a single ordered list by relevance.

Distractors: It prevents candidates from the custom index from being included.: Reranking does not filter sources preemptively but compares relevance post-retrieval.; It only uses candidates from the highest-scoring retrieval source.: A reranker works across all supplied candidates, not just a single source.; It merges the content of all candidates into a single passage.: Reranking maintains individual candidates and does not merge text.

Misconception tags: Role of reranker; Retrieval vs ranking

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order002-reranking.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The artifact notes that rerankers operate over a combined pool, supporting coordinated context selection across sources.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order002-reranking.md
   Evidence span: Reranking models operate over pooled candidates from any source.

### P1-AIP-D3-021

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-021 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.4: Create advanced search architectures to improve the relevance and accuracy of retrieved information for FM context (for example, by using OpenSearch for semantic search, hybrid search that combines keywords and vectors, Amazon Bedrock reranker models). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order002 |
| `accelerated_day` | Day 3 |
| `topic` | Reranking |
| `knowledge_category` | Skill; Knowledge |
| `knowledge_type` | Procedural; Causal; Conditional |
| `question_format` | multiple-response |
| `difficulty` | exam-plus |
| `cognitive_demand` | compare |
| `estimated_time_seconds` | 180 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order002-local-artifact |
| `raw_source` | 2026-06-30T051032Z-openai-gpt-4.1-day-03-order002.md item 8 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051032Z |
| `raw_run_id` | order002 |

Stem:

In a RAG solution, what are two defensible reasons for choosing a learning-to-rank (LTR) model over simple rule-based scoring for reranking context passages? (Choose TWO.)

Options:

1. LTR models can learn complex relevance patterns from training data.
2. LTR models can adapt to user feedback for continuous improvement.
3. LTR models always require smaller candidate pools than rule-based rerankers.
4. LTR models guarantee zero system latency overhead.
5. LTR models replace the need for retrievers entirely.

Correct answer: LTR models can learn complex relevance patterns from training data.; LTR models can adapt to user feedback for continuous improvement.

Rationale: LTR approaches outperform rule-based methods by learning nuanced distinctions and adapting models to user preferences.

Distractors: LTR models always require smaller candidate pools than rule-based rerankers.: Pool size depends on application, not LTR method.; LTR models guarantee zero system latency overhead.: LTR introduces additional computation; no zero-latency guarantee.; LTR models replace the need for retrievers entirely.: Reranking is a post-retrieval operation; retrievers remain essential.

Misconception tags: LTR vs rules; Model roles

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order002-reranking.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The artifact demonstrates that learning-to-rank offers deeper learning and adaptation than rule-based reranky logic.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order002-reranking.md
   Evidence span: LTR models support continuous improvements and more sophisticated relevance features.

### P1-AIP-D3-022

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-022 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.4: Create advanced search architectures to improve the relevance and accuracy of retrieved information for FM context (for example, by using OpenSearch for semantic search, hybrid search that combines keywords and vectors, Amazon Bedrock reranker models). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order002 |
| `accelerated_day` | Day 3 |
| `topic` | Reranking |
| `knowledge_category` | Skill; Knowledge |
| `knowledge_type` | Procedural; Causal; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order002-local-artifact |
| `raw_source` | 2026-06-30T051032Z-openai-gpt-4.1-day-03-order002.md item 9 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051032Z |
| `raw_run_id` | order002 |

Stem:

An experiment shows little improvement when a generic reranker is added to your RAG architecture. What is the most defensible explanation based on standard practices?

Options:

1. The reranker was not fine-tuned on your domain or task, limiting its effectiveness.
2. The candidate retriever was disabled, so the reranker had nothing to process.
3. Adding any reranker always decreases relevance if not manually tuned.
4. Reranking is only beneficial when used with exact keyword matches.

Correct answer: The reranker was not fine-tuned on your domain or task, limiting its effectiveness.

Rationale: Rerankers are most impactful when adapted to domain-specific or task-specific context to capture true relevance features.

Distractors: The candidate retriever was disabled, so the reranker had nothing to process.: The experiment assumes retrievers are active in the typical RAG pipeline.; Adding any reranker always decreases relevance if not manually tuned.: Reranking yields no or negative impact only if not appropriate for the task/domain, not always.; Reranking is only beneficial when used with exact keyword matches.: Rerankers are especially effective in semantic and hybrid retrieval, not just keyword contexts.

Misconception tags: Generic vs custom models; Domain adaptation necessity

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order002-reranking.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The artifact supports that without domain adaptation, reranker impact is reduced, explaining the observed experimental result.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order002-reranking.md
   Evidence span: Fine-tuning rerankers on domain-specific data achieves substantial gains over out-of-domain configurations.

### P1-AIP-D3-023

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-023 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.4: Create advanced search architectures to improve the relevance and accuracy of retrieved information for FM context (for example, by using OpenSearch for semantic search, hybrid search that combines keywords and vectors, Amazon Bedrock reranker models). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order002 |
| `accelerated_day` | Day 3 |
| `topic` | Reranking |
| `knowledge_category` | Skill; Knowledge |
| `knowledge_type` | Procedural; Causal; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order002-local-artifact |
| `raw_source` | 2026-06-30T051032Z-openai-gpt-4.1-day-03-order002.md item 10 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051032Z |
| `raw_run_id` | order002 |

Stem:

A retrieval system struggles with passage duplication, showing near-identical documents in the final output. Which reranker configuration is most directly suited to mitigate this, according to best practices?

Options:

1. Add a diversity-aware objective in the reranking phase.
2. Reduce retrieval pool size to the minimum necessary.
3. Switch to rule-based keyword scoring only.
4. Pre-filter the candidates to remove database duplicates before retrieval.

Correct answer: Add a diversity-aware objective in the reranking phase.

Rationale: A diversity-aware reranker will explicitly penalize selecting near-duplicates in the final context set.

Distractors: Reduce retrieval pool size to the minimum necessary.: This risks missing relevant material and does not address duplication in the ranking process.; Switch to rule-based keyword scoring only.: Keyword scoring cannot account for semantic diversity or meaning.; Pre-filter the candidates to remove database duplicates before retrieval.: Deduplication pre-retrieval may not catch semantically similar passages that appear after retrieval; diversity reranking is more robust.

Misconception tags: Diversity vs similarity; Reranking objectives

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order002-reranking.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The artifact recommends diversity-aware reranking to address near-duplicate passages post-retrieval.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order002-reranking.md
   Evidence span: Diversity-based rerankers can enforce variety in selected context.

### P1-AIP-D3-024

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-024 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.4: Create advanced search architectures to improve the relevance and accuracy of retrieved information for FM context (for example, by using OpenSearch for semantic search, hybrid search that combines keywords and vectors, Amazon Bedrock reranker models). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order002 |
| `accelerated_day` | Day 3 |
| `topic` | Reranking |
| `knowledge_category` | Skill; Knowledge |
| `knowledge_type` | Procedural; Causal; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order002-local-artifact |
| `raw_source` | 2026-06-30T051032Z-openai-gpt-4.1-day-03-order002.md item 11 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051032Z |
| `raw_run_id` | order002 |

Stem:

A RAG pipeline receives frequent user complaints of off-topic information being included in answers even though all candidates were relevant at the retrieval stage. What is the best explanation?

Options:

1. The reranker objective or features are not well aligned with the FM's downstream requirements.
2. The retriever failed to find relevant information due to poor indexing.
3. The vector search space was too large, causing loss of signal.
4. End users should adjust their queries to match the indexer’s vocabulary.

Correct answer: The reranker objective or features are not well aligned with the FM's downstream requirements.

Rationale: If the reranker does not prioritize the context needed by the FM, even relevant passages can be out of scope for the question.

Distractors: The retriever failed to find relevant information due to poor indexing.: The stem specifies candidates were relevant at retrieval, shifting focus to the reranker.; The vector search space was too large, causing loss of signal.: Search space may be large but relevance issues are in post-retrieval ranking in this scenario.; End users should adjust their queries to match the indexer’s vocabulary.: User query engineering is less impactful here than reranker objective alignment.

Misconception tags: Reranker features vs retriever control; System alignment

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order002-reranking.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Best practices state the reranker should be aligned with FM context injection needs—not just retrieval relevance.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order002-reranking.md
   Evidence span: Rerankers must be tuned for FM context; otherwise, topic drift occurs.

### P1-AIP-D3-025

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-025 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.4: Create advanced search architectures to improve the relevance and accuracy of retrieved information for FM context (for example, by using OpenSearch for semantic search, hybrid search that combines keywords and vectors, Amazon Bedrock reranker models). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order002 |
| `accelerated_day` | Day 3 |
| `topic` | Reranking |
| `knowledge_category` | Skill; Knowledge |
| `knowledge_type` | Procedural; Causal; Conditional |
| `question_format` | multiple-response |
| `difficulty` | exam-plus |
| `cognitive_demand` | optimize |
| `estimated_time_seconds` | 180 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order002-local-artifact |
| `raw_source` | 2026-06-30T051032Z-openai-gpt-4.1-day-03-order002.md item 12 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051032Z |
| `raw_run_id` | order002 |

Stem:

You are optimizing a RAG system under the constraint that end-to-end latency for FM responses must stay beneath 1s p95 while still improving context quality. Which are appropriate tactics that support this constraint? (Choose TWO.)

Options:

1. Batch reranking jobs to run asynchronously where possible.
2. Restrict the number of candidates to rerank per query.
3. Disable all post-retrieval ranking to save latency.
4. Increase the retrieval pool size by 10x.
5. Implement a lightweight reranker over a small candidate pool.

Correct answer: Restrict the number of candidates to rerank per query.; Implement a lightweight reranker over a small candidate pool.

Rationale: Restricting the reranking pool and using lightweight models both yields relevance improvement for minimal latency cost.

Distractors: Batch reranking jobs to run asynchronously where possible.: Batching may add latency and reduce response consistency.; Disable all post-retrieval ranking to save latency.: Removes capability to improve context quality.; Increase the retrieval pool size by 10x.: Unnecessarily increases candidate set and harms latency.

Misconception tags: Latency tradeoff; Reranker resource use

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order002-reranking.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The artifact recommends these two steps for supporting strict latency SLAs when reranking.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order002-reranking.md
   Evidence span: Small candidate pools and lighter-weight rerankers are best for latency-sensitive pipelines.

### P1-AIP-D3-026

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-026 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.4: Create advanced search architectures to improve the relevance and accuracy of retrieved information for FM context (for example, by using OpenSearch for semantic search, hybrid search that combines keywords and vectors, Amazon Bedrock reranker models). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order002 |
| `accelerated_day` | Day 3 |
| `topic` | Reranking |
| `knowledge_category` | Skill; Knowledge |
| `knowledge_type` | Procedural; Causal; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order002-local-artifact |
| `raw_source` | 2026-06-30T051032Z-openai-gpt-4.1-day-03-order002.md item 13 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051032Z |
| `raw_run_id` | order002 |

Stem:

A multi-stage retrieval system still returns irrelevant snippets after both hybrid retrieval and reranking. What is the FIRST step you should take to diagnose the issue?

Options:

1. Examine the input features and training data used by the reranker.
2. Increase the number of retrievers in the pipeline.
3. Replace the reranking model with a rule-based approach immediately.
4. Reduce the retrieval pool to the bare minimum.

Correct answer: Examine the input features and training data used by the reranker.

Rationale: Understanding if the reranker is learning from relevant signals or is misconfigured is essential before architectural changes.

Distractors: Increase the number of retrievers in the pipeline.: More retrievers add complexity but do not address reranker performance.; Replace the reranking model with a rule-based approach immediately.: Moving to rules is premature without analysis.; Reduce the retrieval pool to the bare minimum.: Pool size reduction may eliminate relevant info; does not help diagnose reranker issues.

Misconception tags: Root cause analysis; Model vs architecture

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order002-reranking.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The artifact lists reranker misalignment as a common cause; examination comes before changing system topology.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order002-reranking.md
   Evidence span: Initial investigation should check reranker features and training before pipeline tuning.

### P1-AIP-D3-027

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-027 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.5: Develop sophisticated query handling systems to improve the retrieval effectiveness and result quality for FM augmentation (for example, by using Amazon Bedrock for query expansion, Lambda functions for query decomposition, Step Functions for query transformation). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order003 |
| `accelerated_day` | Day 3 |
| `topic` | Query expansion, decomposition, and transformation |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Causal |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | optimize |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order003-local-artifact |
| `raw_source` | 2026-06-30T051124Z-openai-gpt-4.1-day-03-order003.md item 1 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051124Z |
| `raw_run_id` | order003 |

Stem:

A SaaS company uses a retrieval-augmented generation (RAG) architecture for handling complex user queries on its knowledge base. Users are entering ambiguous natural-language questions, leading to inconsistent retrieval relevance. Which approach is most likely to reduce ambiguity and improve retrieval effectiveness?

Options:

1. Apply query decomposition using Lambda functions to break complex queries into smaller, manageable sub-queries.
2. Increase the vector store index size to include more data chunks.
3. Use Step Functions to schedule periodic vector index refreshes.
4. Switch to keyword-only search for initial retrieval.

Correct answer: Apply query decomposition using Lambda functions to break complex queries into smaller, manageable sub-queries.

Rationale: Query decomposition helps address ambiguity by clarifying user input and creating more focused sub-queries, improving semantic retrieval.

Distractors: Increase the vector store index size to include more data chunks.: More data chunks can dilute retrieval relevance and do not address query ambiguity.; Use Step Functions to schedule periodic vector index refreshes.: Refreshing the index is important for data currency but does not solve ambiguity in user queries.; Switch to keyword-only search for initial retrieval.: Keyword-only search can miss semantic meaning and worsen ambiguity matching.

Misconception tags: Equating index size with relevance; Assuming periodic refresh affects ambiguity

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order003-query-expansion-decomposition-transformation.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The evidence explains that Lambda-powered decomposition directly addresses ambiguous queries, improving result quality.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order003-query-expansion-decomposition-transformation.md
   Evidence span: Decomposition breaks down complex user queries ... Lambda functions are often used to automate this process.

### P1-AIP-D3-028

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-028 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.5: Develop sophisticated query handling systems to improve the retrieval effectiveness and result quality for FM augmentation (for example, by using Amazon Bedrock for query expansion, Lambda functions for query decomposition, Step Functions for query transformation). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order003 |
| `accelerated_day` | Day 3 |
| `topic` | Query expansion, decomposition, and transformation |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Causal |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | optimize |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order003-local-artifact |
| `raw_source` | 2026-06-30T051124Z-openai-gpt-4.1-day-03-order003.md item 2 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051124Z |
| `raw_run_id` | order003 |

Stem:

An enterprise RAG platform observes that some queries fail to retrieve any relevant documents, even when information exists in the knowledge base. The team wants to increase recall without introducing irrelevant results. What is the best next step?

Options:

1. Implement query expansion using synonyms and related terms.
2. Expand the chunk size used in vectorization.
3. Boost the retrieval confidence threshold.
4. Avoid transformations to preserve exact user input intent.

Correct answer: Implement query expansion using synonyms and related terms.

Rationale: Query expansion enhances recall by broadening the search to include semantically related terms, often uncovering matches missed by simple matching.

Distractors: Expand the chunk size used in vectorization.: Larger chunks may dilute semantic granularity, reducing result relevance.; Boost the retrieval confidence threshold.: Raising the confidence threshold could actually reduce recall instead of improving it.; Avoid transformations to preserve exact user input intent.: Not transforming queries may limit the system’s ability to cover all ways relevant info could appear.

Misconception tags: Overvaluing chunk size; Misunderstanding threshold effect on recall

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order003-query-expansion-decomposition-transformation.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Including synonyms and related terms through expansion is cited as a practical recall-improving measure.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order003-query-expansion-decomposition-transformation.md
   Evidence span: Query expansion ... increases retrieval recall by including synonyms and related expressions.

### P1-AIP-D3-029

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-029 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.5: Develop sophisticated query handling systems to improve the retrieval effectiveness and result quality for FM augmentation (for example, by using Amazon Bedrock for query expansion, Lambda functions for query decomposition, Step Functions for query transformation). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order003 |
| `accelerated_day` | Day 3 |
| `topic` | Query expansion, decomposition, and transformation |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Causal |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | integrate |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order003-local-artifact |
| `raw_source` | 2026-06-30T051124Z-openai-gpt-4.1-day-03-order003.md item 3 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051124Z |
| `raw_run_id` | order003 |

Stem:

You are modernizing a Q&A bot to handle multi-part user questions (e.g., 'What are the benefits of the new product and how is it priced?'). Which AWS solution best enables splitting such queries for parallelized retrieval and answer synthesis?

Options:

1. Use Lambda to decompose questions and Step Functions to coordinate parallel retrieval.
2. Increase vector database read throughput.
3. Integrate Amazon Translate to handle more languages.
4. Enable Bedrock streaming output for real-time answers.

Correct answer: Use Lambda to decompose questions and Step Functions to coordinate parallel retrieval.

Rationale: Lambda enables programmatic decomposition, and Step Functions can orchestrate parallel tasks for each sub-question to optimize retrieval and synthesis.

Distractors: Increase vector database read throughput.: Read throughput does not address the need to decompose and independently process sub-questions.; Integrate Amazon Translate to handle more languages.: Translation does not help with multi-part query logic.; Enable Bedrock streaming output for real-time answers.: Streaming controls output delivery, not multi-part query handling.

Misconception tags: Confusing throughput improvements with logical query handling

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order003-query-expansion-decomposition-transformation.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The source outlines Lambda for decomposition and Step Functions for orchestration of multi-part retrieval.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order003-query-expansion-decomposition-transformation.md
   Evidence span: Lambda functions can automate query decomposition, and Step Functions allow coordination of parallel retrieval tasks.

### P1-AIP-D3-030

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-030 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.5: Develop sophisticated query handling systems to improve the retrieval effectiveness and result quality for FM augmentation (for example, by using Amazon Bedrock for query expansion, Lambda functions for query decomposition, Step Functions for query transformation). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order003 |
| `accelerated_day` | Day 3 |
| `topic` | Query expansion, decomposition, and transformation |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Causal |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | optimize |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order003-local-artifact |
| `raw_source` | 2026-06-30T051124Z-openai-gpt-4.1-day-03-order003.md item 4 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051124Z |
| `raw_run_id` | order003 |

Stem:

A retrieval workflow repeatedly retrieves semantically related but not truly relevant passages for niche medical queries. Which transformation technique would best improve result precision in this scenario?

Options:

1. Apply query transformation using context-specific templates before retrieval.
2. Lower the semantic similarity threshold.
3. Expand the query to incorporate antonyms.
4. Increase the input chunk size for embeddings.

Correct answer: Apply query transformation using context-specific templates before retrieval.

Rationale: Contextual transformation recasts user queries into expert-style or domain-targeted questions, which can boost retrieval of precise expert-aligned content.

Distractors: Lower the semantic similarity threshold.: Lowering threshold risks allowing more unrelated content, reducing precision.; Expand the query to incorporate antonyms.: Including antonyms dilutes relevance by explicitly including possibly irrelevant or opposite concepts.; Increase the input chunk size for embeddings.: Larger chunks risk reducing focus, not increasing medical precision.

Misconception tags: Treating threshold and chunk size tuning as a fix for semantic drift

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order003-query-expansion-decomposition-transformation.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Using transformation templates for domain alignment is specifically recommended for improved domain-precision retrieval.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order003-query-expansion-decomposition-transformation.md
   Evidence span: Transformation via templates ... aligns the query with domain expert expectations.

### P1-AIP-D3-031

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-031 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.5: Develop sophisticated query handling systems to improve the retrieval effectiveness and result quality for FM augmentation (for example, by using Amazon Bedrock for query expansion, Lambda functions for query decomposition, Step Functions for query transformation). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order003 |
| `accelerated_day` | Day 3 |
| `topic` | Query expansion, decomposition, and transformation |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Causal |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order003-local-artifact |
| `raw_source` | 2026-06-30T051124Z-openai-gpt-4.1-day-03-order003.md item 5 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051124Z |
| `raw_run_id` | order003 |

Stem:

During a retrieval test, your RAG pipeline fails to retrieve any results for niche technical queries that use rare terminology, even though relevant documents exist. Which technique can best help address this failure?

Options:

1. Expand user queries using domain-specific synonym dictionaries.
2. Reduce the number of top-k retrieved results.
3. Switch to strict keyword search only.
4. Double the embedding vector dimension size.

Correct answer: Expand user queries using domain-specific synonym dictionaries.

Rationale: Expanding queries with domain-specific synonyms increases the chances of matching rare and variant terminology in the knowledge base.

Distractors: Reduce the number of top-k retrieved results.: Reducing top-k would further limit recall, not help discover rare terminology.; Switch to strict keyword search only.: Strict keyword search is brittle for phrase and semantic matching, especially in technical domains.; Double the embedding vector dimension size.: Increasing vector size alone doesn't address unrecognized terminology.

Misconception tags: Assuming vector tuning fixes rare word recall

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order003-query-expansion-decomposition-transformation.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The artifact emphasizes synonym expansion as especially important in niche domains.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order003-query-expansion-decomposition-transformation.md
   Evidence span: Custom synonym expansion ... is critical for specialized domains.

### P1-AIP-D3-032

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-032 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.5: Develop sophisticated query handling systems to improve the retrieval effectiveness and result quality for FM augmentation (for example, by using Amazon Bedrock for query expansion, Lambda functions for query decomposition, Step Functions for query transformation). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order003 |
| `accelerated_day` | Day 3 |
| `topic` | Query expansion, decomposition, and transformation |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Causal |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | optimize |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order003-local-artifact |
| `raw_source` | 2026-06-30T051124Z-openai-gpt-4.1-day-03-order003.md item 6 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051124Z |
| `raw_run_id` | order003 |

Stem:

A RAG solution receives complex user questions that reference multiple, loosely related domains. The current approach retrieves irrelevant data because subtopics interfere with one another. Which step best addresses the noise?

Options:

1. Decompose the user query into domain-specific sub-queries handled independently.
2. Apply a universal context window for all query processing.
3. Expand the query by generating keyword permutations for all possible subdomains.
4. Lower the scoring threshold to retrieve more results.

Correct answer: Decompose the user query into domain-specific sub-queries handled independently.

Rationale: Decomposition isolates sub-queries by domain, preventing cross-topic interference and enhancing targeted relevance.

Distractors: Apply a universal context window for all query processing.: A universal window ignores domain boundaries and introduces cross-noise.; Expand the query by generating keyword permutations for all possible subdomains.: Excessive expansion brings in more noise rather than isolating relevant content.; Lower the scoring threshold to retrieve more results.: Lower thresholds increase noise by returning more off-topic documents.

Misconception tags: Thinking that expansion or threshold tuning solves cross-domain relevance

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order003-query-expansion-decomposition-transformation.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The evidence clearly links decomposition to preventing subtopic cross-noise.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order003-query-expansion-decomposition-transformation.md
   Evidence span: Decomposing multi-domain queries reduces cross-topic retrieval interference.

### P1-AIP-D3-033

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-033 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.5: Develop sophisticated query handling systems to improve the retrieval effectiveness and result quality for FM augmentation (for example, by using Amazon Bedrock for query expansion, Lambda functions for query decomposition, Step Functions for query transformation). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order003 |
| `accelerated_day` | Day 3 |
| `topic` | Query expansion, decomposition, and transformation |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Causal |
| `question_format` | multiple-response |
| `difficulty` | hard |
| `cognitive_demand` | implement |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order003-local-artifact |
| `raw_source` | 2026-06-30T051124Z-openai-gpt-4.1-day-03-order003.md item 7 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051124Z |
| `raw_run_id` | order003 |

Stem:

A conversational assistant is failing to retrieve correct historical records when users rephrase questions or use pronouns referencing prior statements. Which combined strategies support improved retrieval under these conditions? (Select TWO.)

Options:

1. Implement query transformation to reconstruct context with inferred references.
2. Add query expansion with likely synonyms and paraphrases.
3. Restrict retrieval strictly to the last message.
4. Disable all query expansion and transformation.
5. Increase top-k retrieval result size to 100.

Correct answer: Implement query transformation to reconstruct context with inferred references.; Add query expansion with likely synonyms and paraphrases.

Rationale: Transformation helps resolve pronoun and reference ambiguity; expansion ensures alternative phrasings are matched.

Distractors: Restrict retrieval strictly to the last message.: Limiting to the last message misses needed context.; Disable all query expansion and transformation.: Turning off these techniques further reduces match ability.; Increase top-k retrieval result size to 100.: Excessively large top-k increases noise and may not improve relevant recall.

Misconception tags: Forgetting the importance of coreference and paraphrases in query resolution; Believing context can be ignored for history-based retrieval

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order003-query-expansion-decomposition-transformation.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Explicit source coverage for both transforming context and expanding for paraphrases ensures the answer's validity.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order003-query-expansion-decomposition-transformation.md
   Evidence span: Transformation and expansion ... manage rephrased inputs and implicit references.

### P1-AIP-D3-034

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-034 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.5: Develop sophisticated query handling systems to improve the retrieval effectiveness and result quality for FM augmentation (for example, by using Amazon Bedrock for query expansion, Lambda functions for query decomposition, Step Functions for query transformation). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order003 |
| `accelerated_day` | Day 3 |
| `topic` | Query expansion, decomposition, and transformation |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Causal |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | optimize |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order003-local-artifact |
| `raw_source` | 2026-06-30T051124Z-openai-gpt-4.1-day-03-order003.md item 8 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051124Z |
| `raw_run_id` | order003 |

Stem:

While reviewing retrieval logs, you notice that the same query retrieves inconsistent sets of documents depending on phrasing (e.g., 'How can I access my account?' vs. 'Ways to log in?'). What is the most efficient way to improve consistency of relevant result retrieval across phrasings?

Options:

1. Adopt query expansion to automatically generate and search with paraphrases.
2. Force all user queries to lower case before search.
3. Increase retrieval index replication for redundancy.
4. Limit retrieval to a single search backend.

Correct answer: Adopt query expansion to automatically generate and search with paraphrases.

Rationale: Query expansion with paraphrasing makes retrieval more robust to input wording, leading to more consistent matches.

Distractors: Force all user queries to lower case before search.: Case normalization doesn't address semantic variety in user phrasing.; Increase retrieval index replication for redundancy.: Replication solves availability, not semantic consistency.; Limit retrieval to a single search backend.: Reducing backends doesn't affect the semantic recall issue.

Misconception tags: Confusing infrastructure with semantics

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order003-query-expansion-decomposition-transformation.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The artifact lists paraphrase expansion as a practical solution for phrasing consistency.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order003-query-expansion-decomposition-transformation.md
   Evidence span: Expansion using paraphrase generation increases resilience to input variation.

### P1-AIP-D3-035

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-035 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.5: Develop sophisticated query handling systems to improve the retrieval effectiveness and result quality for FM augmentation (for example, by using Amazon Bedrock for query expansion, Lambda functions for query decomposition, Step Functions for query transformation). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order003 |
| `accelerated_day` | Day 3 |
| `topic` | Query expansion, decomposition, and transformation |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Causal |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order003-local-artifact |
| `raw_source` | 2026-06-30T051124Z-openai-gpt-4.1-day-03-order003.md item 9 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051124Z |
| `raw_run_id` | order003 |

Stem:

A team implements a query transformation pipeline that converts natural-language queries into domain-specific, structured search queries but notes some performance delays. What is the most likely architectural explanation for increased latency?

Options:

1. Transformation with external function calls introduces processing overhead before retrieval.
2. Top-k retrieval limit is too low, requiring multiple retrieval passes.
3. Embedding model vector dimensions are excessively large.
4. Knowledge base index writes are blocking queries.

Correct answer: Transformation with external function calls introduces processing overhead before retrieval.

Rationale: Transforming queries often involves Lambda or similar calls, adding latency to query processing prior to retrieval, as described in the artifact.

Distractors: Top-k retrieval limit is too low, requiring multiple retrieval passes.: Low top-k affects recall but not the transformation pre-retrieval step.; Embedding model vector dimensions are excessively large.: Dimension size mainly impacts vector math, not query transformation logic.; Knowledge base index writes are blocking queries.: Blocking writes are less likely unless dealing with exclusive, poorly managed write modes.

Misconception tags: Assuming only retrieval parameters affect latency

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order003-query-expansion-decomposition-transformation.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The artifact explicitly describes increased latency due to preprocessing with Lambda and external function calls.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order003-query-expansion-decomposition-transformation.md
   Evidence span: Transformation pipelines ... may add latency especially when using Lambda or remote calls.

### P1-AIP-D3-036

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-036 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.5: Develop sophisticated query handling systems to improve the retrieval effectiveness and result quality for FM augmentation (for example, by using Amazon Bedrock for query expansion, Lambda functions for query decomposition, Step Functions for query transformation). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order003 |
| `accelerated_day` | Day 3 |
| `topic` | Query expansion, decomposition, and transformation |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Causal |
| `question_format` | multiple-response |
| `difficulty` | hard |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order003-local-artifact |
| `raw_source` | 2026-06-30T051124Z-openai-gpt-4.1-day-03-order003.md item 10 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051124Z |
| `raw_run_id` | order003 |

Stem:

A Q&A team is considering different query preprocessing strategies to maximize retrieval accuracy in a multilingual customer service platform. Which combination is most defensible for consistent relevance across languages? (Choose TWO.)

Options:

1. Apply query decomposition to handle multi-section queries per language.
2. Use expansion with localized synonym dictionaries.
3. Restrict queries to English only for simplified vector search.
4. Disable input normalization to avoid altering user intent.
5. Manually adjust embedding thresholds for each language.

Correct answer: Apply query decomposition to handle multi-section queries per language.; Use expansion with localized synonym dictionaries.

Rationale: Decomposition ensures clarity per language, while localized expansion matches varied user phrasing, both supporting cross-language relevance.

Distractors: Restrict queries to English only for simplified vector search.: Restricting to one language fails to meet multilingual requirements.; Disable input normalization to avoid altering user intent.: Not normalizing creates inconsistency and mismatches.; Manually adjust embedding thresholds for each language.: Threshold tuning may help, but doesn't ensure language-specific retrieval accuracy.

Misconception tags: Assuming English-only systems can support multilingual environments; Overreliance on threshold tuning instead of query handling

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order003-query-expansion-decomposition-transformation.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The source provides coverage for both localized decomposition and expansion for consistent multilingual relevance.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order003-query-expansion-decomposition-transformation.md
   Evidence span: Decomposition and localized synonym expansion support more accurate multilingual retrieval.

### P1-AIP-D3-037

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-037 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.5: Develop sophisticated query handling systems to improve the retrieval effectiveness and result quality for FM augmentation (for example, by using Amazon Bedrock for query expansion, Lambda functions for query decomposition, Step Functions for query transformation). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order003 |
| `accelerated_day` | Day 3 |
| `topic` | Query expansion, decomposition, and transformation |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Causal |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order003-local-artifact |
| `raw_source` | 2026-06-30T051124Z-openai-gpt-4.1-day-03-order003.md item 11 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051124Z |
| `raw_run_id` | order003 |

Stem:

Your RAG system surfaces repeated irrelevant results for long, compound questions containing multiple distinct information needs. What is the most effective architectural mitigation?

Options:

1. Segment compound questions into individual sub-queries before retrieval.
2. Increase the number of retrieved results to top-50.
3. Expand queries using antonyms and unrelated synonyms.
4. Switch to single-field exact-match keyword search only.

Correct answer: Segment compound questions into individual sub-queries before retrieval.

Rationale: Segmentation—query decomposition—addresses multiple intents by treating each component independently, greatly improving relevance.

Distractors: Increase the number of retrieved results to top-50.: Larger top-k returns more results but increases irrelevant noise.; Expand queries using antonyms and unrelated synonyms.: Including unrelated synonyms and antonyms worsens precision.; Switch to single-field exact-match keyword search only.: Keyword-only search is brittle and ignores natural language complexity.

Misconception tags: Assuming that top-k or expansion with antonyms solves compound intent

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order003-query-expansion-decomposition-transformation.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The artifact is explicit that sub-query segmentation is crucial for compound questions.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order003-query-expansion-decomposition-transformation.md
   Evidence span: Decomposing or segmenting queries ... addresses compound intent scenarios.

### P1-AIP-D3-038

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-038 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.5: Develop sophisticated query handling systems to improve the retrieval effectiveness and result quality for FM augmentation (for example, by using Amazon Bedrock for query expansion, Lambda functions for query decomposition, Step Functions for query transformation). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order003 |
| `accelerated_day` | Day 3 |
| `topic` | Query expansion, decomposition, and transformation |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Causal |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | optimize |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order003-local-artifact |
| `raw_source` | 2026-06-30T051124Z-openai-gpt-4.1-day-03-order003.md item 12 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051124Z |
| `raw_run_id` | order003 |

Stem:

A GenAI application processes free-form customer feedback for trend analysis. It fails to capture similar concepts due to varied user vocabulary. Which retrieval preprocessing technique would improve aggregation of semantically similar feedback?

Options:

1. Expand queries with semantic synonym sets prior to retrieval.
2. Fragment feedback into individual sentences before building embeddings.
3. Disable all stemming and normalization.
4. Use a strictly keyword-based matching algorithm.

Correct answer: Expand queries with semantic synonym sets prior to retrieval.

Rationale: Expansion via semantic synonym sets increases the chance that varied language in user input connects to relevant indexed content, enabling trend aggregation.

Distractors: Fragment feedback into individual sentences before building embeddings.: Fragmentation may lose broader context; aggregation is key.; Disable all stemming and normalization.: Disabling normalization worsens matching and recall.; Use a strictly keyword-based matching algorithm.: Keyword-matching struggles to capture semantic similarity in natural text.

Misconception tags: Assuming fragmentation or keywording solves semantic matching

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order003-query-expansion-decomposition-transformation.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The source explains how expansion with synonyms helps aggregate variations in user language.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order003-query-expansion-decomposition-transformation.md
   Evidence span: Semantic query expansion improves trend analysis ... especially for varied vocabulary.

### P1-AIP-D3-039

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-039 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.5: Develop sophisticated query handling systems to improve the retrieval effectiveness and result quality for FM augmentation (for example, by using Amazon Bedrock for query expansion, Lambda functions for query decomposition, Step Functions for query transformation). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order003 |
| `accelerated_day` | Day 3 |
| `topic` | Query expansion, decomposition, and transformation |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Causal |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | implement |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order003-local-artifact |
| `raw_source` | 2026-06-30T051124Z-openai-gpt-4.1-day-03-order003.md item 13 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051124Z |
| `raw_run_id` | order003 |

Stem:

A cross-functional RAG system is being flooded with duplicated context when the same user query triggers both query expansion and decomposition features. What action should you take to balance result coverage and minimize noise?

Options:

1. Implement deduplication logic after collecting all results from both strategies.
2. Disable either expansion or decomposition entirely.
3. Lower the number of top-k results retrieved from the store.
4. Use only a single retrieval pipeline for all query types.

Correct answer: Implement deduplication logic after collecting all results from both strategies.

Rationale: Combining both expansion and decomposition can lead to overlapping results; adding deduplication ensures comprehensive but non-redundant retrieval.

Distractors: Disable either expansion or decomposition entirely.: Turning off a whole strategy reduces recall or precision.; Lower the number of top-k results retrieved from the store.: Reducing top-k cuts coverage, not redundancy.; Use only a single retrieval pipeline for all query types.: One-size-fits-all pipelines are too rigid for varied query logic.

Misconception tags: False dichotomy between expansion and decomposition

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order003-query-expansion-decomposition-transformation.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The artifact explicitly recommends deduplication when multiple preprocessing strategies are used.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order003-query-expansion-decomposition-transformation.md
   Evidence span: Systems combining expansion and decomposition benefit from explicit deduplication to prevent context flooding.

### P1-AIP-D3-040

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-040 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.4: Design and implement vector store solutions. |
| `exam_skill` | Skill 1.4.4: Use AWS services to create integration components to connect with resources (for example, document management systems, knowledge bases, internal wikis for comprehensive data integration in GenAI applications). |
| `secondary_exam_skills` | Skill 1.4.5: Design and deploy data maintenance systems to ensure that vector stores contain current and accurate information for FM augmentation (for example, by using incremental update mechanisms, real-time change detection systems, automated synchronization workflows, scheduled refresh pipelines). |
| `learning_unit` | Day03-order004 |
| `accelerated_day` | Day 3 |
| `topic` | Vector-store ingestion, synchronization, refresh, and maintenance |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Causal; Strategic; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | optimize |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order004-local-artifact |
| `raw_source` | 2026-06-30T051203Z-openai-gpt-4.1-day-03-order004.md item 1 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051203Z |
| `raw_run_id` | order004 |

Stem:

A GenAI application ingests legal documents daily to keep its vector store up to date. Users notice that newly added documents sometimes do not appear in retrieval results even after 24 hours. Which adjustment is most likely to ensure timely document availability for retrieval?

Options:

1. Implement real-time change detection to trigger immediate vector ingestion upon document addition.
2. Increase the embedding batch size to process more documents in each run.
3. Set longer refresh intervals to minimize system load.
4. Rebuild the entire vector index nightly.

Correct answer: Implement real-time change detection to trigger immediate vector ingestion upon document addition.

Rationale: Real-time change detection ensures that new documents are immediately processed and ingested, reducing latency before they appear in search results.

Distractors: Increase the embedding batch size to process more documents in each run.: While this could speed up bulk ingestion, it does not decrease latency for new documents, which may still wait for the next scheduled run.; Set longer refresh intervals to minimize system load.: Longer intervals would further delay the appearance of new documents, worsening the freshness problem.; Rebuild the entire vector index nightly.: A nightly rebuild ensures freshness only once per day and is less efficient than incremental, event-driven ingestion.

Misconception tags: Confusing batch ingestion with real-time update; Ignoring document freshness requirements

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order004-vector-store-ingestion-synchronization-refresh-maintenance.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The curriculum artifact states that real-time change detection is key to maintaining current information in the vector store.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order004-vector-store-ingestion-synchronization-refresh-maintenance.md
   Evidence span: real-time change detection systems... automated synchronization workflows

### P1-AIP-D3-041

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-041 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.4: Design and implement vector store solutions. |
| `exam_skill` | Skill 1.4.4: Use AWS services to create integration components to connect with resources (for example, document management systems, knowledge bases, internal wikis for comprehensive data integration in GenAI applications). |
| `secondary_exam_skills` | Skill 1.4.5: Design and deploy data maintenance systems to ensure that vector stores contain current and accurate information for FM augmentation (for example, by using incremental update mechanisms, real-time change detection systems, automated synchronization workflows, scheduled refresh pipelines). |
| `learning_unit` | Day03-order004 |
| `accelerated_day` | Day 3 |
| `topic` | Vector-store ingestion, synchronization, refresh, and maintenance |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Causal; Strategic; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order004-local-artifact |
| `raw_source` | 2026-06-30T051203Z-openai-gpt-4.1-day-03-order004.md item 2 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051203Z |
| `raw_run_id` | order004 |

Stem:

You maintain a RAG pipeline for a multinational enterprise where multiple teams continuously update a large document repository connected to a vector store. Which combination of practices best ensures that your retrieval-augmented FM queries always reflect the latest document state?

Options:

1. Enable event-driven ingestion pipelines and schedule regular refresh jobs.
2. Disable all scheduled jobs to avoid conflicts and rely only on manual ingestion triggers.
3. Recompute embeddings only on a monthly basis to ensure consistency.
4. Depend solely on the underlying document management system's access logs.

Correct answer: Enable event-driven ingestion pipelines and schedule regular refresh jobs.

Rationale: This dual approach catches both real-time updates and slow-changing edge cases, ensuring the vector store reflects the repository's state as it evolves.

Distractors: Disable all scheduled jobs to avoid conflicts and rely only on manual ingestion triggers.: Manual processes are error-prone and may result in stale data when updates are missed.; Recompute embeddings only on a monthly basis to ensure consistency.: Monthly refreshes cannot guarantee the needed freshness for daily-changing data.; Depend solely on the underlying document management system's access logs.: Access logs may help monitor use, but do not directly update the vector store.

Misconception tags: Stale data risk; Over-reliance on manual or single methods

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order004-vector-store-ingestion-synchronization-refresh-maintenance.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The artifact recommends both event-driven ingestion and scheduled refresh to ensure up-to-date vector store content.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order004-vector-store-ingestion-synchronization-refresh-maintenance.md
   Evidence span: Combine automated synchronization workflows with scheduled refresh pipelines

### P1-AIP-D3-042

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-042 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.4: Design and implement vector store solutions. |
| `exam_skill` | Skill 1.4.4: Use AWS services to create integration components to connect with resources (for example, document management systems, knowledge bases, internal wikis for comprehensive data integration in GenAI applications). |
| `secondary_exam_skills` | Skill 1.4.5: Design and deploy data maintenance systems to ensure that vector stores contain current and accurate information for FM augmentation (for example, by using incremental update mechanisms, real-time change detection systems, automated synchronization workflows, scheduled refresh pipelines). |
| `learning_unit` | Day03-order004 |
| `accelerated_day` | Day 3 |
| `topic` | Vector-store ingestion, synchronization, refresh, and maintenance |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Causal; Strategic; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order004-local-artifact |
| `raw_source` | 2026-06-30T051203Z-openai-gpt-4.1-day-03-order004.md item 3 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051203Z |
| `raw_run_id` | order004 |

Stem:

A GenAI team observes their vector-based search results are returning outdated policy documents after a major document update. The embedding process is running without errors. What is the most likely cause of this issue?

Options:

1. Synchronization workflow is not triggered upon new document updates.
2. The embedding dimension is too small for the domain.
3. The retrieval model is using a lower recall configuration.
4. The document scanner is set for internal docs only.

Correct answer: Synchronization workflow is not triggered upon new document updates.

Rationale: If the synchronization workflow does not detect or process updates, the vector store will hold old data even if the embedding pipeline works correctly.

Distractors: The embedding dimension is too small for the domain.: While suboptimal embedding size can affect match quality, it will not cause outdated content to persist after updates.; The retrieval model is using a lower recall configuration.: Recall settings impact result breadth, not data freshness.; The document scanner is set for internal docs only.: This could cause missing documents, not outdated ones.

Misconception tags: Attributing freshness problems to vector parameters; Not checking ingestion triggers

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order004-vector-store-ingestion-synchronization-refresh-maintenance.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The source emphasizes updating mechanisms must notify the workflow for current data to be represented.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order004-vector-store-ingestion-synchronization-refresh-maintenance.md
   Evidence span: ensure that update mechanisms notify the ingestion system

### P1-AIP-D3-043

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-043 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.4: Design and implement vector store solutions. |
| `exam_skill` | Skill 1.4.4: Use AWS services to create integration components to connect with resources (for example, document management systems, knowledge bases, internal wikis for comprehensive data integration in GenAI applications). |
| `secondary_exam_skills` | Skill 1.4.5: Design and deploy data maintenance systems to ensure that vector stores contain current and accurate information for FM augmentation (for example, by using incremental update mechanisms, real-time change detection systems, automated synchronization workflows, scheduled refresh pipelines). |
| `learning_unit` | Day03-order004 |
| `accelerated_day` | Day 3 |
| `topic` | Vector-store ingestion, synchronization, refresh, and maintenance |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Causal; Strategic; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | optimize |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order004-local-artifact |
| `raw_source` | 2026-06-30T051203Z-openai-gpt-4.1-day-03-order004.md item 4 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051203Z |
| `raw_run_id` | order004 |

Stem:

A team is architecting a knowledge base for RAG. They need to ingest documents from an internal CMS and maintain freshness while minimizing compute overhead. Which solution most directly balances freshness and resource usage?

Options:

1. Implement an incremental update pipeline triggered by CMS change events.
2. Schedule hourly full re-indexing jobs for the entire document corpus.
3. Periodically delete and rebuild the vector store from scratch.
4. Ingest new documents only on-demand when a user query fails.

Correct answer: Implement an incremental update pipeline triggered by CMS change events.

Rationale: Incremental updates ensure only changed data is processed, while event triggers avoid wasted cycles on unnecessary processing.

Distractors: Schedule hourly full re-indexing jobs for the entire document corpus.: Full re-indexing is compute-intensive and inefficient compared to incremental updates.; Periodically delete and rebuild the vector store from scratch.: This is even more resource-consuming and can lead to temporary search unavailability.; Ingest new documents only on-demand when a user query fails.: This is reactive and likely to lead to stale or missing results.

Misconception tags: Assuming frequent full index solves freshness; Resource inefficiency

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order004-vector-store-ingestion-synchronization-refresh-maintenance.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Incremental, event-driven pipelines deliver both resource efficiency and freshness as outlined in the artifact.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order004-vector-store-ingestion-synchronization-refresh-maintenance.md
   Evidence span: use incremental update mechanisms ... automated synchronization workflows

### P1-AIP-D3-044

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-044 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.4: Design and implement vector store solutions. |
| `exam_skill` | Skill 1.4.4: Use AWS services to create integration components to connect with resources (for example, document management systems, knowledge bases, internal wikis for comprehensive data integration in GenAI applications). |
| `secondary_exam_skills` | Skill 1.4.5: Design and deploy data maintenance systems to ensure that vector stores contain current and accurate information for FM augmentation (for example, by using incremental update mechanisms, real-time change detection systems, automated synchronization workflows, scheduled refresh pipelines). |
| `learning_unit` | Day03-order004 |
| `accelerated_day` | Day 3 |
| `topic` | Vector-store ingestion, synchronization, refresh, and maintenance |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Causal; Strategic; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order004-local-artifact |
| `raw_source` | 2026-06-30T051203Z-openai-gpt-4.1-day-03-order004.md item 5 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051203Z |
| `raw_run_id` | order004 |

Stem:

During troubleshooting, a developer finds that some records in the vector store never receive embeddings and are missing from results. Which step should be prioritized to address this?

Options:

1. Implement a reconciliation process to detect and enqueue unprocessed records.
2. Increase the embedding model size to improve coverage.
3. Switch from batch to real-time embedding for all records.
4. Rely solely on upstream notifications for ingestion status.

Correct answer: Implement a reconciliation process to detect and enqueue unprocessed records.

Rationale: Reconciliation ensures all intended records are processed by finding unembedded records and re-triggering their ingestion.

Distractors: Increase the embedding model size to improve coverage.: Model size may affect representation quality but will not find or ingest missing records.; Switch from batch to real-time embedding for all records.: Real-time alone doesn't guarantee every record is processed; reconciliation handles gaps.; Rely solely on upstream notifications for ingestion status.: Upstream notifications can be lost or incomplete, missing orphan records.

Misconception tags: Ignoring data pipeline integrity; Confusing embedding quality with completeness

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order004-vector-store-ingestion-synchronization-refresh-maintenance.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The artifact stresses that reconciliation detects and amends missing ingestion cases.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order004-vector-store-ingestion-synchronization-refresh-maintenance.md
   Evidence span: reconciliation processes... ensure all records are represented

### P1-AIP-D3-045

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-045 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.4: Design and implement vector store solutions. |
| `exam_skill` | Skill 1.4.4: Use AWS services to create integration components to connect with resources (for example, document management systems, knowledge bases, internal wikis for comprehensive data integration in GenAI applications). |
| `secondary_exam_skills` | Skill 1.4.5: Design and deploy data maintenance systems to ensure that vector stores contain current and accurate information for FM augmentation (for example, by using incremental update mechanisms, real-time change detection systems, automated synchronization workflows, scheduled refresh pipelines). |
| `learning_unit` | Day03-order004 |
| `accelerated_day` | Day 3 |
| `topic` | Vector-store ingestion, synchronization, refresh, and maintenance |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Causal; Strategic; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | exam-plus |
| `cognitive_demand` | judge |
| `estimated_time_seconds` | 180 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order004-local-artifact |
| `raw_source` | 2026-06-30T051203Z-openai-gpt-4.1-day-03-order004.md item 6 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051203Z |
| `raw_run_id` | order004 |

Stem:

A knowledge base's vector store holds sensitive HR documents. The team assumes that once documents are embedded, access controls from the source system are always enforced at retrieval. Why is this assumption risky?

Options:

1. Embedding representations do not preserve or enforce original document-level authorization.
2. Vector stores automatically inherit all authorization from source systems.
3. Source document permissions are always encoded in embeddings.
4. Embedding sensitive data protects against unauthorized access.

Correct answer: Embedding representations do not preserve or enforce original document-level authorization.

Rationale: Embeddings abstract the content and generally lose per-document access context, requiring explicit access controls during retrieval.

Distractors: Vector stores automatically inherit all authorization from source systems.: Vector stores are decoupled from the original access system unless explicitly integrated.; Source document permissions are always encoded in embeddings.: Embeddings do not encode or enforce permissions.; Embedding sensitive data protects against unauthorized access.: Security is not inherently provided by the embedding process.

Misconception tags: Assuming embedding covers authorization; Security through abstraction fallacy

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order004-vector-store-ingestion-synchronization-refresh-maintenance.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The artifact explicitly warns that vector embeddings do not provide security boundaries, and access must be controlled at retrieval.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order004-vector-store-ingestion-synchronization-refresh-maintenance.md
   Evidence span: embeddings do not enforce data-level authorization; implement access control at retrieval

### P1-AIP-D3-046

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-046 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.4: Design and implement vector store solutions. |
| `exam_skill` | Skill 1.4.4: Use AWS services to create integration components to connect with resources (for example, document management systems, knowledge bases, internal wikis for comprehensive data integration in GenAI applications). |
| `secondary_exam_skills` | Skill 1.4.5: Design and deploy data maintenance systems to ensure that vector stores contain current and accurate information for FM augmentation (for example, by using incremental update mechanisms, real-time change detection systems, automated synchronization workflows, scheduled refresh pipelines). |
| `learning_unit` | Day03-order004 |
| `accelerated_day` | Day 3 |
| `topic` | Vector-store ingestion, synchronization, refresh, and maintenance |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Causal; Strategic; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | optimize |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order004-local-artifact |
| `raw_source` | 2026-06-30T051203Z-openai-gpt-4.1-day-03-order004.md item 7 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051203Z |
| `raw_run_id` | order004 |

Stem:

You are reviewing a GenAI system’s vector store ingestion logs and see frequent duplication of document embeddings for unchanged source files. Which configuration change best addresses unnecessary resource consumption?

Options:

1. Enable change detection logic before enqueueing documents for re-embedding.
2. Switch to synchronous ingestion only.
3. Reprocess all documents at fixed intervals regardless of update history.
4. Reduce embedding dimensionality to save space.

Correct answer: Enable change detection logic before enqueueing documents for re-embedding.

Rationale: Change detection ensures only truly updated documents are re-embedded, avoiding wasteful duplication of unchanged files.

Distractors: Switch to synchronous ingestion only.: Synchronous ingestion impacts process timing but does not fix duplication logic.; Reprocess all documents at fixed intervals regardless of update history.: This could further increase redundant embeddings, worsening the problem.; Reduce embedding dimensionality to save space.: Dimensionality impacts embedding vector size, not ingestion duplication.

Misconception tags: Not distinguishing update triggers from ingestion mode; Storage vs. process confusion

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order004-vector-store-ingestion-synchronization-refresh-maintenance.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Change detection prevents duplicate work and aligns with best practice as stated in the artifact.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order004-vector-store-ingestion-synchronization-refresh-maintenance.md
   Evidence span: Change detection systems ... avoid unnecessary reprocessing of unchanged documents

### P1-AIP-D3-047

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-047 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.4: Design and implement vector store solutions. |
| `exam_skill` | Skill 1.4.4: Use AWS services to create integration components to connect with resources (for example, document management systems, knowledge bases, internal wikis for comprehensive data integration in GenAI applications). |
| `secondary_exam_skills` | Skill 1.4.5: Design and deploy data maintenance systems to ensure that vector stores contain current and accurate information for FM augmentation (for example, by using incremental update mechanisms, real-time change detection systems, automated synchronization workflows, scheduled refresh pipelines). |
| `learning_unit` | Day03-order004 |
| `accelerated_day` | Day 3 |
| `topic` | Vector-store ingestion, synchronization, refresh, and maintenance |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Causal; Strategic; Embedded |
| `question_format` | multiple-response |
| `difficulty` | hard |
| `cognitive_demand` | optimize |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order004-local-artifact |
| `raw_source` | 2026-06-30T051203Z-openai-gpt-4.1-day-03-order004.md item 8 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051203Z |
| `raw_run_id` | order004 |

Stem:

You are evaluating RAG system quality for highly dynamic product catalog data. Which maintenance actions should you implement to ensure both the freshness and reliability of the vector store? (Select TWO.)

Options:

1. Implement automated synchronization workflows.
2. Manually update the vector store with new products each week.
3. Schedule regular full and incremental refresh jobs.
4. Only update embeddings when the model is upgraded.
5. Randomly sample catalog entries for spot-checks monthly.

Correct answer: Implement automated synchronization workflows.; Schedule regular full and incremental refresh jobs.

Rationale: Automated workflows handle change in real time, and regular refreshes provide comprehensive coverage for missed or complex updates.

Distractors: Manually update the vector store with new products each week.: Manual updates are slow and error-prone with dynamic data.; Only update embeddings when the model is upgraded.: This risks large amounts of stale data between upgrades.; Randomly sample catalog entries for spot-checks monthly.: Sampling doesn't ensure freshness and can miss important changes.

Misconception tags: Belief that manual or periodic update suffices for dynamic systems

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order004-vector-store-ingestion-synchronization-refresh-maintenance.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The two selected actions match the recommended best-practices for freshness and reliability stated in the source.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order004-vector-store-ingestion-synchronization-refresh-maintenance.md
   Evidence span: automated synchronization workflows ... scheduled refresh pipelines

### P1-AIP-D3-048

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-048 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.4: Design and implement vector store solutions. |
| `exam_skill` | Skill 1.4.4: Use AWS services to create integration components to connect with resources (for example, document management systems, knowledge bases, internal wikis for comprehensive data integration in GenAI applications). |
| `secondary_exam_skills` | Skill 1.4.5: Design and deploy data maintenance systems to ensure that vector stores contain current and accurate information for FM augmentation (for example, by using incremental update mechanisms, real-time change detection systems, automated synchronization workflows, scheduled refresh pipelines). |
| `learning_unit` | Day03-order004 |
| `accelerated_day` | Day 3 |
| `topic` | Vector-store ingestion, synchronization, refresh, and maintenance |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Causal; Strategic; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | judge |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order004-local-artifact |
| `raw_source` | 2026-06-30T051203Z-openai-gpt-4.1-day-03-order004.md item 9 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051203Z |
| `raw_run_id` | order004 |

Stem:

Which of the following steps is LEAST likely to mitigate vector store drift, where embedded content gradually diverges from the current source data?

Options:

1. Ignoring drift unless end users report obvious retrieval failures.
2. Implementing drift monitoring with diagnostics for change detection.
3. Scheduling vector store audits to verify index accuracy.
4. Employing automated correction workflows for identified drift scenarios.

Correct answer: Ignoring drift unless end users report obvious retrieval failures.

Rationale: Relying on user reports is reactive and does not constitute maintenance; drift must be proactively detected and corrected.

Distractors: Implementing drift monitoring with diagnostics for change detection.: This is a proactive method to catch drift early.; Scheduling vector store audits to verify index accuracy.: Audits help identify and resolve drift issues.; Employing automated correction workflows for identified drift scenarios.: Automation ensures timely remediation of drift.

Misconception tags: Reactive only maintenance; Underestimating drift risk

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order004-vector-store-ingestion-synchronization-refresh-maintenance.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Ignoring drift opposes the explicit guidance that drift must be monitored and addressed.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order004-vector-store-ingestion-synchronization-refresh-maintenance.md
   Evidence span: monitor for drift ... implement automated correction workflows

### P1-AIP-D3-049

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-049 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.4: Design and implement vector store solutions. |
| `exam_skill` | Skill 1.4.4: Use AWS services to create integration components to connect with resources (for example, document management systems, knowledge bases, internal wikis for comprehensive data integration in GenAI applications). |
| `secondary_exam_skills` | Skill 1.4.5: Design and deploy data maintenance systems to ensure that vector stores contain current and accurate information for FM augmentation (for example, by using incremental update mechanisms, real-time change detection systems, automated synchronization workflows, scheduled refresh pipelines). |
| `learning_unit` | Day03-order004 |
| `accelerated_day` | Day 3 |
| `topic` | Vector-store ingestion, synchronization, refresh, and maintenance |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Causal; Strategic; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order004-local-artifact |
| `raw_source` | 2026-06-30T051203Z-openai-gpt-4.1-day-03-order004.md item 10 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051203Z |
| `raw_run_id` | order004 |

Stem:

A vector store pipeline integrates data from multiple source systems, each with different update frequencies. Which set of processes best handles this complexity while maintaining vector store accuracy and minimizing unnecessary compute?

Options:

1. Configure incremental update pipelines per source and combine periodic global audits.
2. Apply a single hourly batch job for all sources, regardless of their update cadence.
3. Force a global embedding refresh on every update event from any source.
4. Rely on scheduled full re-indexes only weekly.

Correct answer: Configure incremental update pipelines per source and combine periodic global audits.

Rationale: Treating each source according to its update cycle, plus periodic global checks, balances efficiency and integrity.

Distractors: Apply a single hourly batch job for all sources, regardless of their update cadence.: This wastes resources for rarely updated sources and may lag on fast-changing ones.; Force a global embedding refresh on every update event from any source.: Refreshing all embeddings for any update is highly inefficient.; Rely on scheduled full re-indexes only weekly.: Weekly full re-indexes can introduce prolonged staleness.

Misconception tags: One-size-fits-all ingestion; Resource-waste

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order004-vector-store-ingestion-synchronization-refresh-maintenance.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Configuring pipelines per source, plus regular audits, aligns with the procedural guidance in the source.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order004-vector-store-ingestion-synchronization-refresh-maintenance.md
   Evidence span: tailor ingestion and update pipelines... combine with audit cycles

### P1-AIP-D3-050

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-050 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.4: Design and implement vector store solutions. |
| `exam_skill` | Skill 1.4.4: Use AWS services to create integration components to connect with resources (for example, document management systems, knowledge bases, internal wikis for comprehensive data integration in GenAI applications). |
| `secondary_exam_skills` | Skill 1.4.5: Design and deploy data maintenance systems to ensure that vector stores contain current and accurate information for FM augmentation (for example, by using incremental update mechanisms, real-time change detection systems, automated synchronization workflows, scheduled refresh pipelines). |
| `learning_unit` | Day03-order004 |
| `accelerated_day` | Day 3 |
| `topic` | Vector-store ingestion, synchronization, refresh, and maintenance |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Causal; Strategic; Embedded |
| `question_format` | multiple-response |
| `difficulty` | hard |
| `cognitive_demand` | implement |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order004-local-artifact |
| `raw_source` | 2026-06-30T051203Z-openai-gpt-4.1-day-03-order004.md item 11 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051203Z |
| `raw_run_id` | order004 |

Stem:

A GenAI developer needs to maintain accurate, up-to-date search results from a vector store even though source documents are sometimes deleted or moved. Which practices are essential to ensure correct and relevant retrieval from the system? (Select TWO.)

Options:

1. Implement a deletion propagation process from the document source to the vector store.
2. Only implement vector embedding for new documents without deletion handling.
3. Schedule routine vector store clean-ups to remove orphaned embeddings.
4. Rely solely on vector similarity, trusting that deleted documents would rarely be returned.
5. Hard-code a deny-list for frequently deleted documents.

Correct answer: Implement a deletion propagation process from the document source to the vector store.; Schedule routine vector store clean-ups to remove orphaned embeddings.

Rationale: Deletion propagation updates the vector store when source documents are removed, and routine clean-ups catch missed deletions, keeping search accurate.

Distractors: Only implement vector embedding for new documents without deletion handling.: This would let old, deleted document embeddings persist, leading to stale results.; Rely solely on vector similarity, trusting that deleted documents would rarely be returned.: Similarity can still recall outdated embeddings, compromising result relevance.; Hard-code a deny-list for frequently deleted documents.: Manual deny-lists are brittle and not scalable.

Misconception tags: Ignoring deletion/cleanup in vector stores; Assuming similarity search rarely returns deleted content

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order004-vector-store-ingestion-synchronization-refresh-maintenance.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: These practices map directly to the artifact's guidance on maintaining vector store relevance and accuracy.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order004-vector-store-ingestion-synchronization-refresh-maintenance.md
   Evidence span: propagate deletions and conduct periodic orphan clean-up

### P1-AIP-D3-051

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-051 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.4: Design and implement vector store solutions. |
| `exam_skill` | Skill 1.4.4: Use AWS services to create integration components to connect with resources (for example, document management systems, knowledge bases, internal wikis for comprehensive data integration in GenAI applications). |
| `secondary_exam_skills` | Skill 1.4.5: Design and deploy data maintenance systems to ensure that vector stores contain current and accurate information for FM augmentation (for example, by using incremental update mechanisms, real-time change detection systems, automated synchronization workflows, scheduled refresh pipelines). |
| `learning_unit` | Day03-order004 |
| `accelerated_day` | Day 3 |
| `topic` | Vector-store ingestion, synchronization, refresh, and maintenance |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Causal; Strategic; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | exam-plus |
| `cognitive_demand` | optimize |
| `estimated_time_seconds` | 180 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order004-local-artifact |
| `raw_source` | 2026-06-30T051203Z-openai-gpt-4.1-day-03-order004.md item 12 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051203Z |
| `raw_run_id` | order004 |

Stem:

A customer wants their GenAI assistant to always retrieve the absolutely latest document version in a compliance-critical application. What best-practice change minimizes the risk of retrieving a stale version from the vector store?

Options:

1. Integrate a last-updated timestamp into both the embedding and the retrieval filter logic.
2. Depend on vector similarity score only for determining the most relevant documents.
3. Schedule daily index rebuilds and alert users for potential staleness.
4. Hard-code a list of the newest document IDs at application startup.

Correct answer: Integrate a last-updated timestamp into both the embedding and the retrieval filter logic.

Rationale: Timestamps embedded and filtered at retrieval time ensure only current documents are returned, directly addressing staleness at the data level.

Distractors: Depend on vector similarity score only for determining the most relevant documents.: Similarity scoring can return outdated documents if no change-awareness exists.; Schedule daily index rebuilds and alert users for potential staleness.: A rebuild is periodic and not real-time, so stale documents can persist between rebuilds.; Hard-code a list of the newest document IDs at application startup.: A hard-coded list is prone to fast obsolescence as soon as new documents are added.

Misconception tags: Confusing similarity with freshness; Forgetting to filter by update status

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order004-vector-store-ingestion-synchronization-refresh-maintenance.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The artifact prescribes using metadata like last-updated to guarantee retrieval freshness.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order004-vector-store-ingestion-synchronization-refresh-maintenance.md
   Evidence span: attach metadata (e.g. last-updated) and filter during retrieval

### P1-AIP-D3-052

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-052 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.6: Create consistent access mechanisms to enable seamless integration with FMs (for example, by using function calling interfaces for vector search, Model Context Protocol [MCP] clients for vector queries, standardized API patterns for retrieval augmentation). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order005 |
| `accelerated_day` | Day 3 |
| `topic` | Retrieval APIs, function interfaces, and MCP access |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Conceptual; Procedural; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | judge |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order005-local-artifact |
| `raw_source` | 2026-06-30T051255Z-openai-gpt-4.1-day-03-order005.md item 1 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051255Z |
| `raw_run_id` | order005 |

Stem:

A startup is building a platform that leverages retrieval-augmented generation (RAG) with Amazon Bedrock and OpenSearch Serverless. The team wants the retrieval API to support both semantic vector search and traditional keyword search in a composable, consistent manner for all downstream FM usage. Which approach best satisfies this need for consistent and extensible integration?

Options:

1. Expose a single API endpoint that internally selects and invokes keyword, vector, or hybrid search, and normalizes results to a shared schema for the FM.
2. Let the application directly call OpenSearch and Bedrock APIs separately, combining results client-side before passing them to the FM.
3. Use FM context APIs only, relying on the FM to determine how to search both forms of data on its own.
4. Expose two separate REST endpoints—one for vector search and one for keyword search—requiring clients to call both and combine results.

Correct answer: Expose a single API endpoint that internally selects and invokes keyword, vector, or hybrid search, and normalizes results to a shared schema for the FM.

Rationale: This approach promotes consistency by abstracting the retrieval mechanisms behind a unified API, ensuring FMs receive a standardized context regardless of underlying retrieval logic. It also simplifies integration and maximizes flexibility.

Distractors: Let the application directly call OpenSearch and Bedrock APIs separately, combining results client-side before passing them to the FM.: This increases client complexity and introduces inconsistency and duplication, making it harder to enforce uniform context for the FM.; Use FM context APIs only, relying on the FM to determine how to search both forms of data on its own.: FMs do not natively handle retrieval from external search APIs; integration logic must live outside the FM.; Expose two separate REST endpoints—one for vector search and one for keyword search—requiring clients to call both and combine results.: This fragments workflow, complicates client logic, and impedes consistent FM integration.

Misconception tags: Confusing FM with retrieval system; Overcomplicating client responsibilities

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order005-retrieval-apis-function-interfaces-mcp-access.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The artifact recommends building a unified retrieval API that normalizes context for FMs, which directly supports the keyed answer.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order005-retrieval-apis-function-interfaces-mcp-access.md
   Evidence span: A single retrieval API that abstracts hybrid search patterns presents a consistent interface for FM augmentation.

### P1-AIP-D3-053

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-053 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.6: Create consistent access mechanisms to enable seamless integration with FMs (for example, by using function calling interfaces for vector search, Model Context Protocol [MCP] clients for vector queries, standardized API patterns for retrieval augmentation). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order005 |
| `accelerated_day` | Day 3 |
| `topic` | Retrieval APIs, function interfaces, and MCP access |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Conceptual; Procedural; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | judge |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order005-local-artifact |
| `raw_source` | 2026-06-30T051255Z-openai-gpt-4.1-day-03-order005.md item 2 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051255Z |
| `raw_run_id` | order005 |

Stem:

A financial organization requires that all systems integrating with their Bedrock-powered GenAI solution utilize a retrieval interface enforcing input validation, access control, and consistent vector-search function signatures. What architectural component best enforces these requirements for downstream FM access?

Options:

1. Implement a serverless retrieval API layer providing a function interface for vector search and policy enforcement.
2. Let each FM client directly query the vector database using its specific native driver.
3. Rely on Amazon Bedrock’s built-in context window to validate and standardize input and access.
4. Implement an OpenSearch plugin that exposes REST endpoints directly against the index.

Correct answer: Implement a serverless retrieval API layer providing a function interface for vector search and policy enforcement.

Rationale: A purpose-built API layer allows for central enforcement of validation, access control, and a consistent function interface, which is crucial when integrating with FMs at scale.

Distractors: Let each FM client directly query the vector database using its specific native driver.: This loses standardization, circumvents central policy enforcement, and leads to integration drift across clients.; Rely on Amazon Bedrock’s built-in context window to validate and standardize input and access.: Bedrock context windows accept input, but do not enforce external data source policies or validation.; Implement an OpenSearch plugin that exposes REST endpoints directly against the index.: While providing access, this bypasses centralized input validation and function interface consistency.

Misconception tags: Mixing FM context with retrieval boundary; Ignoring centralized governance

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order005-retrieval-apis-function-interfaces-mcp-access.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: A custom retrieval API or function layer ensures consistent interfaces and allows for all required governance capabilities.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order005-retrieval-apis-function-interfaces-mcp-access.md
   Evidence span: Use a standard API or function interface between the FM and vector store to enable consistent enforcement.

### P1-AIP-D3-054

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-054 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.6: Create consistent access mechanisms to enable seamless integration with FMs (for example, by using function calling interfaces for vector search, Model Context Protocol [MCP] clients for vector queries, standardized API patterns for retrieval augmentation). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order005 |
| `accelerated_day` | Day 3 |
| `topic` | Retrieval APIs, function interfaces, and MCP access |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Conceptual; Procedural; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | judge |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order005-local-artifact |
| `raw_source` | 2026-06-30T051255Z-openai-gpt-4.1-day-03-order005.md item 3 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051255Z |
| `raw_run_id` | order005 |

Stem:

You are tasked with integrating a large language model (LLM) via Amazon Bedrock into an internal platform with strict auditability needs. Which design best ensures traceability of all vector-based retrievals made for FM context?

Options:

1. Build the retrieval API as an AWS Lambda function with CloudWatch logging of all queries, and invoke it through Bedrock’s function calling/MCP interface.
2. Send direct SQL queries from the FM to the vector database, logging only FM prompt and response.
3. Query the vector store from the client, then forward retrieved results through an API Gateway endpoint to the FM.
4. Handle both retrieval and FM inference from a batch job with no intermediate logging.

Correct answer: Build the retrieval API as an AWS Lambda function with CloudWatch logging of all queries, and invoke it through Bedrock’s function calling/MCP interface.

Rationale: This architecture captures each retrieval event for audit, and ensures that retrieval flows are invoked through a controlled, traceable API pathway consistent with Bedrock’s integration model.

Distractors: Send direct SQL queries from the FM to the vector database, logging only FM prompt and response.: This misses the retrieval step, which is a key part of auditability requirements.; Query the vector store from the client, then forward retrieved results through an API Gateway endpoint to the FM.: Retrieval events may be hidden from audit logs if performed client-side, reducing traceability.; Handle both retrieval and FM inference from a batch job with no intermediate logging.: This fails all traceability requirements.

Misconception tags: Logging at wrong boundary; Assuming FM can log retrievals directly

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order005-retrieval-apis-function-interfaces-mcp-access.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Lambda with CloudWatch logging and Bedrock MCP interface achieves full auditability and traceability for vector retrievals.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order005-retrieval-apis-function-interfaces-mcp-access.md
   Evidence span: Use Lambda or a similar managed interface for retrieval, capturing logs in CloudWatch for all relevant operations.

### P1-AIP-D3-055

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-055 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.6: Create consistent access mechanisms to enable seamless integration with FMs (for example, by using function calling interfaces for vector search, Model Context Protocol [MCP] clients for vector queries, standardized API patterns for retrieval augmentation). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order005 |
| `accelerated_day` | Day 3 |
| `topic` | Retrieval APIs, function interfaces, and MCP access |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Conceptual; Procedural; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | judge |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order005-local-artifact |
| `raw_source` | 2026-06-30T051255Z-openai-gpt-4.1-day-03-order005.md item 4 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051255Z |
| `raw_run_id` | order005 |

Stem:

A dev team wants to minimize their FM integration effort while supporting both changing retrieval logic and new FM types. Which design aligns best with extensibility and long-term maintenance?

Options:

1. Implement a Model Context Protocol (MCP)–compliant retrieval client that all FMs use, abstracting storage and logic.
2. Require each FM to use its own bespoke retrieval method and store integration logic within model-specific wrappers.
3. Allow FMs to connect directly to various vector databases, configuring authentication in each FM separately.
4. Deprecate retrieval augmentation in favor of prompt-only workflows managed by application code.

Correct answer: Implement a Model Context Protocol (MCP)–compliant retrieval client that all FMs use, abstracting storage and logic.

Rationale: An MCP-compliant interface standardizes retrieval across different FMs, future-proofs integrations, and reduces duplicated effort as retrieval changes or new FMs are added.

Distractors: Require each FM to use its own bespoke retrieval method and store integration logic within model-specific wrappers.: This approach is maintenance-intensive, risks drift, and reduces extensibility as requirements change.; Allow FMs to connect directly to various vector databases, configuring authentication in each FM separately.: This increases complexity and tightly couples FM logic to data sources, impeding evolution.; Deprecate retrieval augmentation in favor of prompt-only workflows managed by application code.: Abandoning retrieval removes core GenAI value and abandons RAG best practices.

Misconception tags: Confusing extensibility with bespoke integration; Underestimating standardization benefits

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order005-retrieval-apis-function-interfaces-mcp-access.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Using an MCP-compliant client decouples retrieval from storage and model specifics, simplifying future changes.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order005-retrieval-apis-function-interfaces-mcp-access.md
   Evidence span: Standardize retrieval integration using MCP or similar protocol to simplify extension and minimize logic duplication.

### P1-AIP-D3-056

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-056 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.6: Create consistent access mechanisms to enable seamless integration with FMs (for example, by using function calling interfaces for vector search, Model Context Protocol [MCP] clients for vector queries, standardized API patterns for retrieval augmentation). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order005 |
| `accelerated_day` | Day 3 |
| `topic` | Retrieval APIs, function interfaces, and MCP access |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Conceptual; Procedural; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | judge |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order005-local-artifact |
| `raw_source` | 2026-06-30T051255Z-openai-gpt-4.1-day-03-order005.md item 5 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051255Z |
| `raw_run_id` | order005 |

Stem:

A retail company wants to ensure that their FM-based search application only delivers relevant product data to the FM based on user permissions. What is the best way to enforce policy and filter content within the retrieval API?

Options:

1. Incorporate user identity and permissions into the API and filter results server-side before passing to the FM.
2. Filter results within the FM after retrieval, dropping any items for which the user lacks permission.
3. Give each FM user direct temporary access credentials to the product database, bypassing API control.
4. Pre-embed all access policies into the vector store and rely on vector similarity filtering alone.

Correct answer: Incorporate user identity and permissions into the API and filter results server-side before passing to the FM.

Rationale: Server-side policy enforcement in the retrieval API guarantees that only authorized data is sent for augmentation, reducing the risk of leaking sensitive information.

Distractors: Filter results within the FM after retrieval, dropping any items for which the user lacks permission.: Once data reaches the FM, unauthorized content may be exposed in context, violating least privilege.; Give each FM user direct temporary access credentials to the product database, bypassing API control.: Bypassing centralized enforcement leads to control and audit gaps.; Pre-embed all access policies into the vector store and rely on vector similarity filtering alone.: Embedding access policies is not reliable; similarity search may retrieve items users should not see.

Misconception tags: Confusing retrieval boundary with FM boundary; Assuming similarity enforces policy

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order005-retrieval-apis-function-interfaces-mcp-access.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Filtering and authorization at the retrieval API is required to prevent data leakage to FMs.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order005-retrieval-apis-function-interfaces-mcp-access.md
   Evidence span: Apply filtering and enforcement within the retrieval API layer before augmenting the FM context.

### P1-AIP-D3-057

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-057 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.6: Create consistent access mechanisms to enable seamless integration with FMs (for example, by using function calling interfaces for vector search, Model Context Protocol [MCP] clients for vector queries, standardized API patterns for retrieval augmentation). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order005 |
| `accelerated_day` | Day 3 |
| `topic` | Retrieval APIs, function interfaces, and MCP access |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Conceptual; Procedural; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | judge |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order005-local-artifact |
| `raw_source` | 2026-06-30T051255Z-openai-gpt-4.1-day-03-order005.md item 6 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051255Z |
| `raw_run_id` | order005 |

Stem:

A team deploying a RAG-backed chatbot selects Amazon Bedrock for foundation modeling and wishes to pass rich, structured document context using retrieval augmentation. What integration pattern will best support context-rich results and downstream extension?

Options:

1. Wrap retrieved chunks in a well-defined JSON schema via a function interface for downstream FM integration.
2. Send raw unstructured text blobs from the vector store to the FM, relying on prompt templates for structure.
3. Pass document links as plain text for the FM to fetch data directly.
4. Embed database credentials in FM prompts to allow the FM to perform its own retrieval.

Correct answer: Wrap retrieved chunks in a well-defined JSON schema via a function interface for downstream FM integration.

Rationale: Structured schemas in retrieval APIs ensure context is consistently formatted, making extension, validation, and FM consumption easier and safer.

Distractors: Send raw unstructured text blobs from the vector store to the FM, relying on prompt templates for structure.: Unstructured text leads to ambiguity, reduces auditability, and complicates downstream ML behavior.; Pass document links as plain text for the FM to fetch data directly.: FMs cannot fetch data from links on their own; context must be explicitly provided.; Embed database credentials in FM prompts to allow the FM to perform its own retrieval.: This is a security anti-pattern and not a supported architecture.

Misconception tags: Relying on FM to structure input; Security bypasses in retrieval

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order005-retrieval-apis-function-interfaces-mcp-access.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The artifact requires retrieval APIs to present structured context using schemas or function-calling contracts.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order005-retrieval-apis-function-interfaces-mcp-access.md
   Evidence span: A structured retrieval schema or function interface makes integration and downstream processing robust and extensible.

### P1-AIP-D3-058

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-058 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.6: Create consistent access mechanisms to enable seamless integration with FMs (for example, by using function calling interfaces for vector search, Model Context Protocol [MCP] clients for vector queries, standardized API patterns for retrieval augmentation). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order005 |
| `accelerated_day` | Day 3 |
| `topic` | Retrieval APIs, function interfaces, and MCP access |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Conceptual; Procedural; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | judge |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order005-local-artifact |
| `raw_source` | 2026-06-30T051255Z-openai-gpt-4.1-day-03-order005.md item 7 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051255Z |
| `raw_run_id` | order005 |

Stem:

A bank wants all GenAI application retrieval events to be compatible with both current Bedrock-enabled LLMs and potential future FMs. Which design supports this mandate while minimizing code rewrite?

Options:

1. Adopt the Model Context Protocol (MCP) client or standardized function interface in all RAG applications.
2. Hard-code all retrieval flows inside existing Bedrock-specific adapters.
3. Design the vector store API using bespoke endpoints for each FM’s requirements.
4. Let each new FM integration write its own direct vector store integration.

Correct answer: Adopt the Model Context Protocol (MCP) client or standardized function interface in all RAG applications.

Rationale: Standardized protocols like MCP allow retrieval events to be reused across FMs, minimizing future adaptation overhead.

Distractors: Hard-code all retrieval flows inside existing Bedrock-specific adapters.: Tightly coupling to Bedrock limits future flexibility and increases rewrite costs.; Design the vector store API using bespoke endpoints for each FM’s requirements.: Custom endpoints lead to maintenance burden and complicate future migrations.; Let each new FM integration write its own direct vector store integration.: This is the least maintainable and most error-prone option.

Misconception tags: Overfitting to current platform; Ignoring protocol-based extensibility

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order005-retrieval-apis-function-interfaces-mcp-access.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The artifact recommends standard protocols to future-proof retrieval API investments.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order005-retrieval-apis-function-interfaces-mcp-access.md
   Evidence span: Use MCP or standardized function interfaces for broadest future compatibility and lowest migration overhead.

### P1-AIP-D3-059

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-059 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.6: Create consistent access mechanisms to enable seamless integration with FMs (for example, by using function calling interfaces for vector search, Model Context Protocol [MCP] clients for vector queries, standardized API patterns for retrieval augmentation). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order005 |
| `accelerated_day` | Day 3 |
| `topic` | Retrieval APIs, function interfaces, and MCP access |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Conceptual; Procedural; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | judge |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order005-local-artifact |
| `raw_source` | 2026-06-30T051255Z-openai-gpt-4.1-day-03-order005.md item 8 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051255Z |
| `raw_run_id` | order005 |

Stem:

While reviewing an FM-augmented API, an engineer notices direct calls to the vector database from the client browser. Why is this design strongly discouraged for production RAG solutions?

Options:

1. It exposes internal data sources and bypasses retrieval-layer validation, risking data leaks and inconsistent application logic.
2. Client-side calls maximize security by eliminating server involvement in data handling.
3. Direct vector store access from browsers enhances cache performance and reduces API costs.
4. Such a design is needed for fastest real-time document indexing.

Correct answer: It exposes internal data sources and bypasses retrieval-layer validation, risking data leaks and inconsistent application logic.

Rationale: Allowing client browsers to access internal data stores directly removes essential validation, policy enforcement, and surface control—key requirements for production RAG solutions.

Distractors: Client-side calls maximize security by eliminating server involvement in data handling.: Security is reduced, not increased, due to loss of control.; Direct vector store access from browsers enhances cache performance and reduces API costs.: Security and policy risk outweigh any caching benefit.; Such a design is needed for fastest real-time document indexing.: Indexing speed is orthogonal; safe design still requires central validation.

Misconception tags: Trusting client with secure data; Misunderstanding of index and latency tradeoffs

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order005-retrieval-apis-function-interfaces-mcp-access.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Direct client access to vector stores removes policy enforcement and is explicitly discouraged.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order005-retrieval-apis-function-interfaces-mcp-access.md
   Evidence span: Access patterns must go through a retrieval API or proxy to enforce policy and validation.

### P1-AIP-D3-060

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-060 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.6: Create consistent access mechanisms to enable seamless integration with FMs (for example, by using function calling interfaces for vector search, Model Context Protocol [MCP] clients for vector queries, standardized API patterns for retrieval augmentation). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order005 |
| `accelerated_day` | Day 3 |
| `topic` | Retrieval APIs, function interfaces, and MCP access |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Conceptual; Procedural; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | judge |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order005-local-artifact |
| `raw_source` | 2026-06-30T051255Z-openai-gpt-4.1-day-03-order005.md item 9 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051255Z |
| `raw_run_id` | order005 |

Stem:

An e-commerce firm wants to enable multiple business units to build custom FM-powered search applications using a shared enterprise vector store. Which retrieval API practice best empowers each unit while protecting core data and enforcing consistency?

Options:

1. Provide a single, managed retrieval API supporting custom query parameters and strict access controls for all business units.
2. Allow each business unit to fetch and process the raw vector embeddings directly.
3. Require all search queries to pass through the FM, which then routes requests to the business unit’s custom logic.
4. Export snapshots of the vector store to each business unit as static data files.

Correct answer: Provide a single, managed retrieval API supporting custom query parameters and strict access controls for all business units.

Rationale: A shared, managed retrieval API permits customization within a controlled and auditable environment, ensuring data security and integration consistency.

Distractors: Allow each business unit to fetch and process the raw vector embeddings directly.: Unmediated access weakens governance, audit trails, and risks exposing sensitive data.; Require all search queries to pass through the FM, which then routes requests to the business unit’s custom logic.: FMs are not routers; this approach creates bottlenecks and deployment complexity.; Export snapshots of the vector store to each business unit as static data files.: This quickly becomes stale and prevents real-time context retrieval.

Misconception tags: Confusing business-unit extensibility with security; Using FM as a proxy for retrieval

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order005-retrieval-apis-function-interfaces-mcp-access.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: A shared, parametrized retrieval API provides both needed flexibility and required data protection.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order005-retrieval-apis-function-interfaces-mcp-access.md
   Evidence span: Centralized retrieval APIs enable parameterization and access control for multi-tenant deployments.

### P1-AIP-D3-061

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-061 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.6: Create consistent access mechanisms to enable seamless integration with FMs (for example, by using function calling interfaces for vector search, Model Context Protocol [MCP] clients for vector queries, standardized API patterns for retrieval augmentation). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order005 |
| `accelerated_day` | Day 3 |
| `topic` | Retrieval APIs, function interfaces, and MCP access |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Conceptual; Procedural; Embedded |
| `question_format` | multiple-response |
| `difficulty` | hard |
| `cognitive_demand` | judge |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order005-local-artifact |
| `raw_source` | 2026-06-30T051255Z-openai-gpt-4.1-day-03-order005.md item 10 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051255Z |
| `raw_run_id` | order005 |

Stem:

You are designing a scalable customer-support chatbot using Amazon Bedrock and a vector store. Which design strategies are recommended for the retrieval API layer? (Select TWO.)

Options:

1. Normalize all retrieved results into a structured schema before passing them to the FM.
2. Enforce user authorization and filtering policies at the API layer for every retrieval query.
3. Return raw database records directly to the FM for prompt engineering.
4. Allow direct FM access to the vector database for flexible data science experimentation.
5. Implement retrieval timeouts and error handling within the FM prompt templates.

Correct answer: Normalize all retrieved results into a structured schema before passing them to the FM.; Enforce user authorization and filtering policies at the API layer for every retrieval query.

Rationale: Both options guarantee consistent, auditable FM context and enforce data access controls, which are both best practices for retrieval augmentation.

Distractors: Return raw database records directly to the FM for prompt engineering.: This skips necessary normalization and validation, risking model confusion.; Allow direct FM access to the vector database for flexible data science experimentation.: Direct FM/db coupling is strongly discouraged and unsafe for production.; Implement retrieval timeouts and error handling within the FM prompt templates.: Prompt templates cannot perform programmatic error handling or timeouts.

Misconception tags: Mixing prompt and API responsibilities; Improper FM/database linkage

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order005-retrieval-apis-function-interfaces-mcp-access.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Best practice is to have retrieval APIs enforce both data normalization and access control.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order005-retrieval-apis-function-interfaces-mcp-access.md
   Evidence span: Retrieval APIs should enforce normalization and policy filtering before FM handoff.

### P1-AIP-D3-062

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-062 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.6: Create consistent access mechanisms to enable seamless integration with FMs (for example, by using function calling interfaces for vector search, Model Context Protocol [MCP] clients for vector queries, standardized API patterns for retrieval augmentation). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order005 |
| `accelerated_day` | Day 3 |
| `topic` | Retrieval APIs, function interfaces, and MCP access |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Conceptual; Procedural; Embedded |
| `question_format` | multiple-response |
| `difficulty` | hard |
| `cognitive_demand` | judge |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order005-local-artifact |
| `raw_source` | 2026-06-30T051255Z-openai-gpt-4.1-day-03-order005.md item 11 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051255Z |
| `raw_run_id` | order005 |

Stem:

A healthcare team needs retrieval APIs for RAG with strict compliance logging, context schema stability, and support for Bedrock FMs and future FM ecosystems. What are the most appropriate API design choices? (Select TWO.)

Options:

1. Provide a standardized, schema-versioned function interface to all retrieval endpoints.
2. Log all retrieval API queries and context payloads to an auditable store (e.g., CloudWatch or S3).
3. Allow direct FM-to-vector-store requests, logging only FM prompt strings.
4. Hard-code all field order and context handling within FM-specific plugins.
5. Expose each vector store’s native API individually for every FM integration.

Correct answer: Provide a standardized, schema-versioned function interface to all retrieval endpoints.; Log all retrieval API queries and context payloads to an auditable store (e.g., CloudWatch or S3).

Rationale: Standardized and versioned schemas enable stability across updates and regulatory audits, while API query/context logging is essential for compliance validation.

Distractors: Allow direct FM-to-vector-store requests, logging only FM prompt strings.: This omits critical steps in the compliance chain.; Hard-code all field order and context handling within FM-specific plugins.: Discouraged—prevents evolution and increases integration drift.; Expose each vector store’s native API individually for every FM integration.: This leads to complexity, loss of normalization, and governance gaps.

Misconception tags: Compliance without context logging; Ignoring schema evolution

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order005-retrieval-apis-function-interfaces-mcp-access.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The artifact notes versioned schemas and audit logging are key for compliance and stable integration.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order005-retrieval-apis-function-interfaces-mcp-access.md
   Evidence span: Versioned schemas and logging are necessary for compliant and stable API design in RAG.

### P1-AIP-D3-063

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-063 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.6: Create consistent access mechanisms to enable seamless integration with FMs (for example, by using function calling interfaces for vector search, Model Context Protocol [MCP] clients for vector queries, standardized API patterns for retrieval augmentation). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order005 |
| `accelerated_day` | Day 3 |
| `topic` | Retrieval APIs, function interfaces, and MCP access |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Conceptual; Procedural; Embedded |
| `question_format` | multiple-response |
| `difficulty` | hard |
| `cognitive_demand` | judge |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order005-local-artifact |
| `raw_source` | 2026-06-30T051255Z-openai-gpt-4.1-day-03-order005.md item 12 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051255Z |
| `raw_run_id` | order005 |

Stem:

You are tasked with onboarding new LLMs from different vendors via Amazon Bedrock for a RAG platform. Which are valid requirements for the retrieval API/function interface to maximize cross-FM compatibility? (Select TWO.)

Options:

1. Support standardized structure for context objects, such as parameters for content, metadata, and retrieval source.
2. Implement version negotiation or explicit schema versioning for all retrieval payloads.
3. Customize the retrieval logic within each FM wrapper and omit shared API contracts.
4. Let new FMs make direct database queries for their specific context needs.
5. Design the API to be stateless, treating each retrieval as discrete and independent.

Correct answer: Support standardized structure for context objects, such as parameters for content, metadata, and retrieval source.; Implement version negotiation or explicit schema versioning for all retrieval payloads.

Rationale: Standardized context structures and explicit versioning support onboarding new FMs and reduce integration friction as models evolve.

Distractors: Customize the retrieval logic within each FM wrapper and omit shared API contracts.: This increases maintenance cost and damages cross-FM compatibility.; Let new FMs make direct database queries for their specific context needs.: Direct access loses abstraction, increasing security and consistency risks.; Design the API to be stateless, treating each retrieval as discrete and independent.: While stateless APIs are scalable, the key compatibility enablers are context schema and versioning, not statelessness alone.

Misconception tags: Ignoring schema/versioning requirements; Assuming statelessness solves compatibility

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order005-retrieval-apis-function-interfaces-mcp-access.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Context structure and schema versioning enable easy adoption of new FMs without refactoring the retrieval API.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order005-retrieval-apis-function-interfaces-mcp-access.md
   Evidence span: Standardized context schemas and version control are main mechanisms for cross-FM compatibility.

### P1-AIP-D3-064

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-064 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.6: Create consistent access mechanisms to enable seamless integration with FMs (for example, by using function calling interfaces for vector search, Model Context Protocol [MCP] clients for vector queries, standardized API patterns for retrieval augmentation). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order005 |
| `accelerated_day` | Day 3 |
| `topic` | Retrieval APIs, function interfaces, and MCP access |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Conceptual; Procedural; Embedded |
| `question_format` | multiple-response |
| `difficulty` | hard |
| `cognitive_demand` | judge |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order005-local-artifact |
| `raw_source` | 2026-06-30T051255Z-openai-gpt-4.1-day-03-order005.md item 13 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051255Z |
| `raw_run_id` | order005 |

Stem:

A SaaS vendor prepares to launch an FM-augmented search platform as a multi-region managed service. Security, tenant isolation, and feature evolution are required. What should the retrieval API design emphasize? (Select TWO.)

Options:

1. Implement tenant-aware access controls and input validation at the API layer.
2. Expose an externally documented, stable function interface for both external and internal consumers.
3. Permit tenants to push plugin code for custom FM retrieval logic directly to the shared API servers.
4. Store all retrieval-related access logs only client-side for privacy.
5. Allow unrestricted direct database queries for debugging purposes.

Correct answer: Implement tenant-aware access controls and input validation at the API layer.; Expose an externally documented, stable function interface for both external and internal consumers.

Rationale: Access control and documented, stable interfaces are vital for isolation, security, and supporting evolving use cases across tenants and regions.

Distractors: Permit tenants to push plugin code for custom FM retrieval logic directly to the shared API servers.: Security and isolation requirements prohibit unvetted tenant logic inside shared services.; Store all retrieval-related access logs only client-side for privacy.: Server-side logs are required for isolation enforcement and auditing.; Allow unrestricted direct database queries for debugging purposes.: Allowing direct queries defeats all isolation and security objectives.

Misconception tags: Ignoring tenant isolation; Client-side logging/validation fallacy

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order005-retrieval-apis-function-interfaces-mcp-access.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: API design for a multi-region, multi-tenant SaaS must enforce tenant-aware controls and provide stable interfaces.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order005-retrieval-apis-function-interfaces-mcp-access.md
   Evidence span: Tenant-aware control, input validation, and formally documented interfaces are critical for multi-tenant RAG platforms.

### P1-AIP-D3-065

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-065 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 5: Testing, Validation, and Troubleshooting |
| `exam_task` | Task 5.1: Implement evaluation systems for GenAI. |
| `exam_skill` | Skill 5.1.6: Implement retrieval quality testing to evaluate and optimize information retrieval components for FM augmentation (for example, by using relevance scoring, context matching verification, retrieval latency measurements). |
| `secondary_exam_skills` | Skill 5.2.4: Troubleshoot retrieval system issues to identify and resolve problems that affect information retrieval effectiveness for FM augmentation (for example, by using model response relevance analysis, embedding quality diagnostics, drift monitoring, vectorization issue resolution, chunking and preprocessing remediation, vector search performance optimization). |
| `learning_unit` | Day03-order006 |
| `accelerated_day` | Day 3 |
| `topic` | RAG quality evaluation and retrieval troubleshooting |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Diagnostic; Causal; Procedural; Tacit |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order006-local-artifact |
| `raw_source` | 2026-06-30T051339Z-openai-gpt-4.1-day-03-order006.md item 1 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051339Z |
| `raw_run_id` | order006 |

Stem:

A customer using a RAG application on AWS notices that the responses provided by their FM are frequently irrelevant, despite an apparently well-structured knowledge base and up-to-date vector store. As the principal developer, which diagnostic approach should you prioritize to identify the root cause?

Options:

1. Analyze the quality of input query embeddings and verify their alignment with the retrieval corpus.
2. Restart the application and clear the vector store cache to eliminate old vectors.
3. Increase the number of documents retrieved to ensure broader context coverage.
4. Re-train the FM on recent documents to improve relevance in QA tasks.

Correct answer: Analyze the quality of input query embeddings and verify their alignment with the retrieval corpus.

Rationale: Misalignment between query embeddings and the vector store can cause irrelevant results, even if documents are structurally sound and recent. Diagnosing embedding quality and compatibility is a primary troubleshooting step.

Distractors: Restart the application and clear the vector store cache to eliminate old vectors.: Tempting because cache issues can affect performance, but if embeddings are the issue, flushing caches won't address the underlying semantic mismatch.; Increase the number of documents retrieved to ensure broader context coverage.: Tempting as it seems to provide more data, but can dilute relevance further if core embedding issues are present.; Re-train the FM on recent documents to improve relevance in QA tasks.: An FM retrain is resource-intensive and doesn't solve retrieval pipeline misalignment if the embeddings themselves are at fault.

Misconception tags: Assuming retrieval issues are caused by outdated data, not by embedding alignment.

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order006-rag-quality-evaluation-retrieval-troubleshooting.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The source emphasizes the importance of verifying embedding alignment between queries and documents, supporting the approach to analyze embedding quality.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order006-rag-quality-evaluation-retrieval-troubleshooting.md
   Evidence span: Check that embedding methods produce consistent semantic space across query and corpus vectors.

### P1-AIP-D3-066

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-066 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 5: Testing, Validation, and Troubleshooting |
| `exam_task` | Task 5.1: Implement evaluation systems for GenAI. |
| `exam_skill` | Skill 5.1.6: Implement retrieval quality testing to evaluate and optimize information retrieval components for FM augmentation (for example, by using relevance scoring, context matching verification, retrieval latency measurements). |
| `secondary_exam_skills` | Skill 5.2.4: Troubleshoot retrieval system issues to identify and resolve problems that affect information retrieval effectiveness for FM augmentation (for example, by using model response relevance analysis, embedding quality diagnostics, drift monitoring, vectorization issue resolution, chunking and preprocessing remediation, vector search performance optimization). |
| `learning_unit` | Day03-order006 |
| `accelerated_day` | Day 3 |
| `topic` | RAG quality evaluation and retrieval troubleshooting |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Diagnostic; Causal; Procedural; Tacit |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order006-local-artifact |
| `raw_source` | 2026-06-30T051339Z-openai-gpt-4.1-day-03-order006.md item 2 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051339Z |
| `raw_run_id` | order006 |

Stem:

You receive user complaints that a GenAI application based on RAG frequently takes too long to return answers or sometimes exceeds API timeouts. Which action is most effective to isolate where latency is introduced in the retrieval pipeline?

Options:

1. Instrument step-level latency and collect metrics at each major retrieval component.
2. Increase the FM temperature parameter to see if it speeds up responses.
3. Switch from semantic to keyword search to check if results are faster.
4. Reduce the retrieval document count by half, assuming response time will improve.

Correct answer: Instrument step-level latency and collect metrics at each major retrieval component.

Rationale: Measuring and observing latency at each major retrieval and augmentation step enables precise identification of bottlenecks, which is crucial before applying changes.

Distractors: Increase the FM temperature parameter to see if it speeds up responses.: The temperature parameter affects randomness but not latency or throughput.; Switch from semantic to keyword search to check if results are faster.: While model and search differences affect speed, blindly switching methods without diagnosis could lower relevance and not target the true bottleneck.; Reduce the retrieval document count by half, assuming response time will improve.: Retrieving fewer documents can reduce downstream processing, but without identifying the slowest stage, it may not yield meaningful gains.

Misconception tags: Changing model or retrieval parameters without isolating source of latency.

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order006-rag-quality-evaluation-retrieval-troubleshooting.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The curriculum artifact advises stepwise instrumentation for latency diagnosis, validating this as the top troubleshooting action.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order006-rag-quality-evaluation-retrieval-troubleshooting.md
   Evidence span: Instrument retrieval components to measure latency and isolate slow steps.

### P1-AIP-D3-067

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-067 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 5: Testing, Validation, and Troubleshooting |
| `exam_task` | Task 5.1: Implement evaluation systems for GenAI. |
| `exam_skill` | Skill 5.1.6: Implement retrieval quality testing to evaluate and optimize information retrieval components for FM augmentation (for example, by using relevance scoring, context matching verification, retrieval latency measurements). |
| `secondary_exam_skills` | Skill 5.2.4: Troubleshoot retrieval system issues to identify and resolve problems that affect information retrieval effectiveness for FM augmentation (for example, by using model response relevance analysis, embedding quality diagnostics, drift monitoring, vectorization issue resolution, chunking and preprocessing remediation, vector search performance optimization). |
| `learning_unit` | Day03-order006 |
| `accelerated_day` | Day 3 |
| `topic` | RAG quality evaluation and retrieval troubleshooting |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Diagnostic; Causal; Procedural; Tacit |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order006-local-artifact |
| `raw_source` | 2026-06-30T051339Z-openai-gpt-4.1-day-03-order006.md item 3 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051339Z |
| `raw_run_id` | order006 |

Stem:

During retrieval quality testing, you observe that relevant documents are available in the knowledge base but rarely surface among the top retrieved results. What is the most likely cause?

Options:

1. Chunk size and overlap parameters are improperly tuned, leading to fragment loss in the embedding step.
2. The retrieval query is being truncated due to token limits enforced by the FM.
3. The RAG pipeline is using an outdated FM API version.
4. An incorrect access policy is preventing retrieval of relevant documents.

Correct answer: Chunk size and overlap parameters are improperly tuned, leading to fragment loss in the embedding step.

Rationale: Fragment loss or improper granularity from poor chunking configuration can cause semantically relevant data to be missed during vector search, lowering retrieval result quality.

Distractors: The retrieval query is being truncated due to token limits enforced by the FM.: Token limits affect FM input; here, retrieval itself is the symptom, not FM input size.; The RAG pipeline is using an outdated FM API version.: Outdated APIs may add risk, but would not typically affect what documents are surfaced unless the embedding method changed.; An incorrect access policy is preventing retrieval of relevant documents.: If access were denied, documents would be missing entirely, not just demoted in result ranking.

Misconception tags: Focusing on token limits or permissions when chunking causes retrieval gaps.

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order006-rag-quality-evaluation-retrieval-troubleshooting.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Improper chunking, as explained in the source, can lower semantic recall, supporting this diagnosis.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order006-rag-quality-evaluation-retrieval-troubleshooting.md
   Evidence span: Tune chunk size and overlap to balance semantic granularity and vector recall.

### P1-AIP-D3-068

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-068 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 5: Testing, Validation, and Troubleshooting |
| `exam_task` | Task 5.1: Implement evaluation systems for GenAI. |
| `exam_skill` | Skill 5.1.6: Implement retrieval quality testing to evaluate and optimize information retrieval components for FM augmentation (for example, by using relevance scoring, context matching verification, retrieval latency measurements). |
| `secondary_exam_skills` | Skill 5.2.4: Troubleshoot retrieval system issues to identify and resolve problems that affect information retrieval effectiveness for FM augmentation (for example, by using model response relevance analysis, embedding quality diagnostics, drift monitoring, vectorization issue resolution, chunking and preprocessing remediation, vector search performance optimization). |
| `learning_unit` | Day03-order006 |
| `accelerated_day` | Day 3 |
| `topic` | RAG quality evaluation and retrieval troubleshooting |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Diagnostic; Causal; Procedural; Tacit |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order006-local-artifact |
| `raw_source` | 2026-06-30T051339Z-openai-gpt-4.1-day-03-order006.md item 4 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051339Z |
| `raw_run_id` | order006 |

Stem:

You have implemented relevance scoring and context matching verification for your GenAI FM augmentation pipeline. A new batch of test queries shows excellent context matching but inconsistent answer quality. What should you check next?

Options:

1. Evaluate the completeness and factual quality of the knowledge base itself.
2. Reduce the embedding vector dimension to increase similarity score discrimination.
3. Decrease the retrieval document count to focus the context window.
4. Switch from hybrid search to semantic-only search immediately.

Correct answer: Evaluate the completeness and factual quality of the knowledge base itself.

Rationale: Strong context matching but weak answers points to possible gaps in the actual data, so assessing the source knowledge is a key next step before technical tuning.

Distractors: Reduce the embedding vector dimension to increase similarity score discrimination.: Reducing vector size can lower accuracy; the issue is more likely due to data completeness than vector numerics.; Decrease the retrieval document count to focus the context window.: If context matches but answer quality is low, limiting further won't help; it may exacerbate the problem.; Switch from hybrid search to semantic-only search immediately.: Hasty search strategy changes without understanding the underlying knowledge base misses the real issue.

Misconception tags: Assuming technical modifications fix knowledge base problems.

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order006-rag-quality-evaluation-retrieval-troubleshooting.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The source makes clear that underlying knowledge gaps are a primary cause of inconsistent output, supporting the proposed check.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order006-rag-quality-evaluation-retrieval-troubleshooting.md
   Evidence span: If the knowledge base is incomplete or outdated, answer quality will suffer regardless of retrieval quality.

### P1-AIP-D3-069

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-069 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 5: Testing, Validation, and Troubleshooting |
| `exam_task` | Task 5.1: Implement evaluation systems for GenAI. |
| `exam_skill` | Skill 5.1.6: Implement retrieval quality testing to evaluate and optimize information retrieval components for FM augmentation (for example, by using relevance scoring, context matching verification, retrieval latency measurements). |
| `secondary_exam_skills` | Skill 5.2.4: Troubleshoot retrieval system issues to identify and resolve problems that affect information retrieval effectiveness for FM augmentation (for example, by using model response relevance analysis, embedding quality diagnostics, drift monitoring, vectorization issue resolution, chunking and preprocessing remediation, vector search performance optimization). |
| `learning_unit` | Day03-order006 |
| `accelerated_day` | Day 3 |
| `topic` | RAG quality evaluation and retrieval troubleshooting |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Diagnostic; Causal; Procedural; Tacit |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order006-local-artifact |
| `raw_source` | 2026-06-30T051339Z-openai-gpt-4.1-day-03-order006.md item 5 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051339Z |
| `raw_run_id` | order006 |

Stem:

Multiple users report paraphrased but factually incorrect answers from a Bedrock RAG application after a recent embedding model upgrade. Which step is most likely to resolve the issue?

Options:

1. Re-embed all documents in the knowledge base using the new embedding model.
2. Decrease the retrieval top-k value to streamline the context injection.
3. Switch from vector search to pure keyword search only.
4. Lower the FM's temperature parameter for more deterministic outputs.

Correct answer: Re-embed all documents in the knowledge base using the new embedding model.

Rationale: Deploying a new embedding model renders old vector representations potentially incompatible and semantically mismatched, so re-embedding ensures proper search and recall.

Distractors: Decrease the retrieval top-k value to streamline the context injection.: A smaller top-k might slightly focus context, but if embeddings do not match, context will still be off-topic.; Switch from vector search to pure keyword search only.: Keyword search does not fix embedding mismatches; it usually reduces semantic recall.; Lower the FM's temperature parameter for more deterministic outputs.: Temperature controls randomness, not retrieval base correctness.

Misconception tags: Assuming context selection or parameter tuning can fix embedding-model incompatibility.

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order006-rag-quality-evaluation-retrieval-troubleshooting.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The artifact clearly states the requirement to re-embed after changing embedding models, supporting this as the next step.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order006-rag-quality-evaluation-retrieval-troubleshooting.md
   Evidence span: Re-index after changing embedding models to prevent semantic drift between query and stored vectors.

### P1-AIP-D3-070

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-070 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 5: Testing, Validation, and Troubleshooting |
| `exam_task` | Task 5.1: Implement evaluation systems for GenAI. |
| `exam_skill` | Skill 5.1.6: Implement retrieval quality testing to evaluate and optimize information retrieval components for FM augmentation (for example, by using relevance scoring, context matching verification, retrieval latency measurements). |
| `secondary_exam_skills` | Skill 5.2.4: Troubleshoot retrieval system issues to identify and resolve problems that affect information retrieval effectiveness for FM augmentation (for example, by using model response relevance analysis, embedding quality diagnostics, drift monitoring, vectorization issue resolution, chunking and preprocessing remediation, vector search performance optimization). |
| `learning_unit` | Day03-order006 |
| `accelerated_day` | Day 3 |
| `topic` | RAG quality evaluation and retrieval troubleshooting |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Diagnostic; Causal; Procedural; Tacit |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order006-local-artifact |
| `raw_source` | 2026-06-30T051339Z-openai-gpt-4.1-day-03-order006.md item 6 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051339Z |
| `raw_run_id` | order006 |

Stem:

You deploy an updated chunking pipeline and immediately notice a sudden drop in retrieval relevance scores across your RAG system. What troubleshooting action should you take first?

Options:

1. Compare current and prior chunking logic to identify changes in document segmentation.
2. Increase the FM's context window to allow more input text.
3. Switch to a different embedding model for all queries.
4. Purge and rebuild the vector store from scratch.

Correct answer: Compare current and prior chunking logic to identify changes in document segmentation.

Rationale: Diagnostic practice suggests verifying what changed—comparing new and prior chunk segmentation logic can highlight errors that triggered the relevance drop.

Distractors: Increase the FM's context window to allow more input text.: Context window size may help overall context but does not resolve faulty chunking.; Switch to a different embedding model for all queries.: This is a drastic change and may simply mask the fundamental chunking pipeline bug.; Purge and rebuild the vector store from scratch.: Rebuilding is costly and unnecessary unless chunking errors are actually present and persistent.

Misconception tags: Assuming expensive or drastic steps should precede targeted diagnosis.

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order006-rag-quality-evaluation-retrieval-troubleshooting.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Source guidance specifically recommends reviewing changes to chunking/segmentation to diagnose sudden retrieval quality drops.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order006-rag-quality-evaluation-retrieval-troubleshooting.md
   Evidence span: If relevance drops after chunking changes, compare logic to previous baseline to isolate the bug.

### P1-AIP-D3-071

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-071 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 5: Testing, Validation, and Troubleshooting |
| `exam_task` | Task 5.1: Implement evaluation systems for GenAI. |
| `exam_skill` | Skill 5.1.6: Implement retrieval quality testing to evaluate and optimize information retrieval components for FM augmentation (for example, by using relevance scoring, context matching verification, retrieval latency measurements). |
| `secondary_exam_skills` | Skill 5.2.4: Troubleshoot retrieval system issues to identify and resolve problems that affect information retrieval effectiveness for FM augmentation (for example, by using model response relevance analysis, embedding quality diagnostics, drift monitoring, vectorization issue resolution, chunking and preprocessing remediation, vector search performance optimization). |
| `learning_unit` | Day03-order006 |
| `accelerated_day` | Day 3 |
| `topic` | RAG quality evaluation and retrieval troubleshooting |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Diagnostic; Causal; Procedural; Tacit |
| `question_format` | multiple-response |
| `difficulty` | hard |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order006-local-artifact |
| `raw_source` | 2026-06-30T051339Z-openai-gpt-4.1-day-03-order006.md item 7 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051339Z |
| `raw_run_id` | order006 |

Stem:

Your RAG application passes all retrieval quality checks in development, but live users flag important information as missing from model responses. Which set of evaluation or troubleshooting actions should you take to cover environment-specific retrieval issues? (Choose TWO.)

Options:

1. Run end-to-end retrieval tests using real user queries in production environment.
2. Verify document access policies and authorization boundaries match between dev and prod.
3. Lower the FM temperature parameter across all environments.
4. Re-embed the knowledge base from the QA environment in production.
5. Switch all retrieval backends to keyword-only retrieval.

Correct answer: Run end-to-end retrieval tests using real user queries in production environment.; Verify document access policies and authorization boundaries match between dev and prod.

Rationale: Production misalignment is often due to real-world data or access-policy drift. Testing in-place and verifying policy parity help catch environment-specific issues.

Distractors: Lower the FM temperature parameter across all environments.: Changes randomness but does not impact data retrieval or access.; Re-embed the knowledge base from the QA environment in production.: Embedding QA data in production does not fix missing production data or access gaps.; Switch all retrieval backends to keyword-only retrieval.: Keyword search is not a panacea and may lower semantic recall, especially in modern RAG.

Misconception tags: Assuming retrieval/storage problems are independent of environment configuration.

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order006-rag-quality-evaluation-retrieval-troubleshooting.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Representative production tests and access verification are specifically called out in the source for environment drift diagnosis.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order006-rag-quality-evaluation-retrieval-troubleshooting.md
   Evidence span: Verify access and run representative end-to-end tests in production context.

### P1-AIP-D3-072

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-072 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 5: Testing, Validation, and Troubleshooting |
| `exam_task` | Task 5.1: Implement evaluation systems for GenAI. |
| `exam_skill` | Skill 5.1.6: Implement retrieval quality testing to evaluate and optimize information retrieval components for FM augmentation (for example, by using relevance scoring, context matching verification, retrieval latency measurements). |
| `secondary_exam_skills` | Skill 5.2.4: Troubleshoot retrieval system issues to identify and resolve problems that affect information retrieval effectiveness for FM augmentation (for example, by using model response relevance analysis, embedding quality diagnostics, drift monitoring, vectorization issue resolution, chunking and preprocessing remediation, vector search performance optimization). |
| `learning_unit` | Day03-order006 |
| `accelerated_day` | Day 3 |
| `topic` | RAG quality evaluation and retrieval troubleshooting |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Diagnostic; Causal; Procedural; Tacit |
| `question_format` | multiple-response |
| `difficulty` | medium |
| `cognitive_demand` | optimize |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order006-local-artifact |
| `raw_source` | 2026-06-30T051339Z-openai-gpt-4.1-day-03-order006.md item 8 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051339Z |
| `raw_run_id` | order006 |

Stem:

You are tasked with improving the evaluation process for information retrieval in a RAG solution. Which combination of techniques will best provide actionable feedback on retrieval quality? (Choose TWO.)

Options:

1. Implement context matching verification for retrieved results.
2. Collect and analyze retrieval latency metrics.
3. Increase the FM model size to improve output quality.
4. Compare FM responses with ground truth answers for relevance scored evaluation.
5. Reduce the semantic vector dimension for cost savings.

Correct answer: Implement context matching verification for retrieved results.; Compare FM responses with ground truth answers for relevance scored evaluation.

Rationale: Direct evaluation and scoring against ground truth, along with context matching, ensure retrieval effectiveness and actionable improvement steps.

Distractors: Collect and analyze retrieval latency metrics.: Latency is important for performance, not direct quality/relevance assessment.; Increase the FM model size to improve output quality.: Model size alone doesn't measure or guarantee better retrieval; quality evaluation is needed.; Reduce the semantic vector dimension for cost savings.: Lower vector dimensionality may cut costs but can hurt recall; not a quality evaluation technique.

Misconception tags: Confusing performance metrics with retrieval quality evaluation.

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order006-rag-quality-evaluation-retrieval-troubleshooting.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The document highlights context matching and ground truth scoring as direct retrieval quality evaluation techniques.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order006-rag-quality-evaluation-retrieval-troubleshooting.md
   Evidence span: Use context matching verification and ground truth scoring for feedback on retrieval quality.

### P1-AIP-D3-073

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-073 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 5: Testing, Validation, and Troubleshooting |
| `exam_task` | Task 5.1: Implement evaluation systems for GenAI. |
| `exam_skill` | Skill 5.1.6: Implement retrieval quality testing to evaluate and optimize information retrieval components for FM augmentation (for example, by using relevance scoring, context matching verification, retrieval latency measurements). |
| `secondary_exam_skills` | Skill 5.2.4: Troubleshoot retrieval system issues to identify and resolve problems that affect information retrieval effectiveness for FM augmentation (for example, by using model response relevance analysis, embedding quality diagnostics, drift monitoring, vectorization issue resolution, chunking and preprocessing remediation, vector search performance optimization). |
| `learning_unit` | Day03-order006 |
| `accelerated_day` | Day 3 |
| `topic` | RAG quality evaluation and retrieval troubleshooting |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Diagnostic; Causal; Procedural; Tacit |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order006-local-artifact |
| `raw_source` | 2026-06-30T051339Z-openai-gpt-4.1-day-03-order006.md item 9 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051339Z |
| `raw_run_id` | order006 |

Stem:

A RAG system’s FM responses suddenly become hallucinated and no longer reference recent updates, even though the recent documents appear present in the vector store. What is the most plausible system-level explanation?

Options:

1. The vector store synchronization or refresh pipeline has failed, so the search mechanism is reading stale embeddings.
2. The FM model itself must be retrained to reflect the most recent updates.
3. Reranking models in Bedrock are not effective with updated semantic vectors.
4. API request timeouts caused the retrieval pipeline to occasionally fall back to default answers.

Correct answer: The vector store synchronization or refresh pipeline has failed, so the search mechanism is reading stale embeddings.

Rationale: If the update pipeline fails, the store does not reflect changes, even if new docs are uploaded, resulting in outdated context for RAG.

Distractors: The FM model itself must be retrained to reflect the most recent updates.: Retraining the foundational model will not affect context if retrieval is based on stale embeddings.; Reranking models in Bedrock are not effective with updated semantic vectors.: Reranking aids reordering but does not override what embeddings are surfaced.; API request timeouts caused the retrieval pipeline to occasionally fall back to default answers.: Timeouts might lead to missing results, not systemic outdatedness.

Misconception tags: Believing FM retraining is the main way to update factual coverage.

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order006-rag-quality-evaluation-retrieval-troubleshooting.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The artifact emphasizes the role of refresh pipelines in ensuring up-to-date embeddings are used for retrieval.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order006-rag-quality-evaluation-retrieval-troubleshooting.md
   Evidence span: Keep synchronization pipelines healthy to prevent retrieval from returning stale data.

### P1-AIP-D3-074

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-074 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 5: Testing, Validation, and Troubleshooting |
| `exam_task` | Task 5.1: Implement evaluation systems for GenAI. |
| `exam_skill` | Skill 5.1.6: Implement retrieval quality testing to evaluate and optimize information retrieval components for FM augmentation (for example, by using relevance scoring, context matching verification, retrieval latency measurements). |
| `secondary_exam_skills` | Skill 5.2.4: Troubleshoot retrieval system issues to identify and resolve problems that affect information retrieval effectiveness for FM augmentation (for example, by using model response relevance analysis, embedding quality diagnostics, drift monitoring, vectorization issue resolution, chunking and preprocessing remediation, vector search performance optimization). |
| `learning_unit` | Day03-order006 |
| `accelerated_day` | Day 3 |
| `topic` | RAG quality evaluation and retrieval troubleshooting |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Diagnostic; Causal; Procedural; Tacit |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | optimize |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order006-local-artifact |
| `raw_source` | 2026-06-30T051339Z-openai-gpt-4.1-day-03-order006.md item 10 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051339Z |
| `raw_run_id` | order006 |

Stem:

After launching a RAG application, you measure excellent response latency but observe that answer relevance is erratic depending on query formulation. What remediation or test will directly address the issue?

Options:

1. Implement query normalization or expansion pre-processing to reduce linguistic variability.
2. Switch to a higher-dimension embedding model to enhance recall.
3. Increase the temperature parameter on the FM for more diverse outputs.
4. Decrease the document top-k retrieval setting.

Correct answer: Implement query normalization or expansion pre-processing to reduce linguistic variability.

Rationale: Linguistic differences in queries often cause inconsistent retrieval; normalization brings queries closer to the embedding space of stored texts.

Distractors: Switch to a higher-dimension embedding model to enhance recall.: Dimensionality may help but normalization targets the root cause directly.; Increase the temperature parameter on the FM for more diverse outputs.: Temperature changes randomness, not underlying retrieval accuracy.; Decrease the document top-k retrieval setting.: Fewer documents may focus results but does not fix inconsistent query handling.

Misconception tags: Focusing on retrieval quantity or randomness instead of input normalization.

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order006-rag-quality-evaluation-retrieval-troubleshooting.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Curriculum materials recommend preprocessing for linguistic harmonization to smooth out retrieval inconsistency.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order006-rag-quality-evaluation-retrieval-troubleshooting.md
   Evidence span: Apply preprocessing such as query normalization and expansion for retrieval consistency.

### P1-AIP-D3-075

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-075 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 5: Testing, Validation, and Troubleshooting |
| `exam_task` | Task 5.1: Implement evaluation systems for GenAI. |
| `exam_skill` | Skill 5.1.6: Implement retrieval quality testing to evaluate and optimize information retrieval components for FM augmentation (for example, by using relevance scoring, context matching verification, retrieval latency measurements). |
| `secondary_exam_skills` | Skill 5.2.4: Troubleshoot retrieval system issues to identify and resolve problems that affect information retrieval effectiveness for FM augmentation (for example, by using model response relevance analysis, embedding quality diagnostics, drift monitoring, vectorization issue resolution, chunking and preprocessing remediation, vector search performance optimization). |
| `learning_unit` | Day03-order006 |
| `accelerated_day` | Day 3 |
| `topic` | RAG quality evaluation and retrieval troubleshooting |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Diagnostic; Causal; Procedural; Tacit |
| `question_format` | multiple-response |
| `difficulty` | medium |
| `cognitive_demand` | optimize |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order006-local-artifact |
| `raw_source` | 2026-06-30T051339Z-openai-gpt-4.1-day-03-order006.md item 11 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051339Z |
| `raw_run_id` | order006 |

Stem:

You are responsible for a production RAG system. Which set of ongoing monitoring or evaluation practices best support both real-time troubleshooting and long-term improvement? (Choose TWO.)

Options:

1. Track and analyze retrieval latency metrics in production.
2. Continuously sample and manually evaluate answer relevance based on user queries.
3. Push all queries to a development system for offline analysis only.
4. Disable all logs to minimize operational cost.
5. Implement automated alerts on retrieval error rates and context matching failures.

Correct answer: Track and analyze retrieval latency metrics in production.; Implement automated alerts on retrieval error rates and context matching failures.

Rationale: Combining latency/performance monitoring with real-time error and context-matching alerting supports both troubleshooting and improvement cycles.

Distractors: Continuously sample and manually evaluate answer relevance based on user queries.: Useful but not scalable or real-time; should be complementary not core.; Push all queries to a development system for offline analysis only.: Offline analysis lacks timeliness and does not suffice for production.; Disable all logs to minimize operational cost.: Prevents any troubleshooting or improvement; not a responsible practice.

Misconception tags: Assuming logging/alerting is nonessential or manual review alone suffices.

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order006-rag-quality-evaluation-retrieval-troubleshooting.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Ongoing alerting and latency monitoring are curriculum-recommended for troubleshooting and continuous improvement.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order006-rag-quality-evaluation-retrieval-troubleshooting.md
   Evidence span: Use latency monitoring and alerting for error or context drift in production pipelines.

### P1-AIP-D3-076

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-076 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 5: Testing, Validation, and Troubleshooting |
| `exam_task` | Task 5.1: Implement evaluation systems for GenAI. |
| `exam_skill` | Skill 5.1.6: Implement retrieval quality testing to evaluate and optimize information retrieval components for FM augmentation (for example, by using relevance scoring, context matching verification, retrieval latency measurements). |
| `secondary_exam_skills` | Skill 5.2.4: Troubleshoot retrieval system issues to identify and resolve problems that affect information retrieval effectiveness for FM augmentation (for example, by using model response relevance analysis, embedding quality diagnostics, drift monitoring, vectorization issue resolution, chunking and preprocessing remediation, vector search performance optimization). |
| `learning_unit` | Day03-order006 |
| `accelerated_day` | Day 3 |
| `topic` | RAG quality evaluation and retrieval troubleshooting |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Diagnostic; Causal; Procedural; Tacit |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | optimize |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order006-local-artifact |
| `raw_source` | 2026-06-30T051339Z-openai-gpt-4.1-day-03-order006.md item 12 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051339Z |
| `raw_run_id` | order006 |

Stem:

A GenAI RAG application demonstrates high latency when queries result in large context payloads assembled from many documents. What is the most effective remediation to balance response time and context usefulness?

Options:

1. Optimize context assembly by setting a maximum context size and prioritizing relevant chunks.
2. Increase the document retrieval top-k value for broader data input.
3. Remove hybrid search and use semantic-only search to simplify results.
4. Switch to a larger foundational model to handle more text at once.

Correct answer: Optimize context assembly by setting a maximum context size and prioritizing relevant chunks.

Rationale: Controlling and ranking the content pipeline ensures context remains useful and latency is minimized regardless of document set size.

Distractors: Increase the document retrieval top-k value for broader data input.: This increases, not reduces, the amount of data processed and may worsen latency.; Remove hybrid search and use semantic-only search to simplify results.: Search algorithm change may alter results but doesn't limit total input size.; Switch to a larger foundational model to handle more text at once.: Larger models may accept more input but with higher cost and still have limits.

Misconception tags: Believing broader data or bigger models solve latency/context pressure without pipeline control.

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order006-rag-quality-evaluation-retrieval-troubleshooting.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The artifact's recommended pattern is to cap payloads and select content to fit latency and usefulness requirements.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order006-rag-quality-evaluation-retrieval-troubleshooting.md
   Evidence span: Control context assembly to meet token budgets and prioritize relevant chunks for balance.

### P1-AIP-D3-077

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-077 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.2: Build interactive AI systems to maintain context and improve user interactions with FMs (for example, by using Step Functions for clarification workflows, Amazon Comprehend for intent recognition, DynamoDB for conversation history storage). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order007 |
| `accelerated_day` | Day 3 |
| `topic` | Conversation context, history, intent, and state management |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | dynamodb-core-components |
| `raw_source` | 2026-06-30T051420Z-openai-gpt-4.1-day-03-order007.md item 1 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051420Z |
| `raw_run_id` | order007 |

Stem:

A conversational AI assistant for employee HR queries uses Amazon Comprehend for intent recognition and Amazon DynamoDB for conversation state. Users often return after several days and expect the AI to continue their previous dialogue seamlessly. What is the most appropriate DynamoDB design pattern to reliably store and retrieve the user's conversation context over time?

Options:

1. Use a table with PartitionKey as user ID and SortKey as a timestamp for each message.
2. Use a single-item table where the conversation state for all users is stored in a large JSON blob.
3. Create a table with PartitionKey as session ID and SortKey as interaction index.
4. Store only the latest message per user in a table keyed by user ID.

Correct answer: Use a table with PartitionKey as user ID and SortKey as a timestamp for each message.

Rationale: Storing messages with PartitionKey as user ID and SortKey as a timestamp enables efficient, ordered retrieval of conversation history per user over time.

Distractors: Use a single-item table where the conversation state for all users is stored in a large JSON blob.: This approach will quickly hit item size limits and cause operational bottlenecks.; Create a table with PartitionKey as session ID and SortKey as interaction index.: Session ID may not persist across user visits, making long-term history retrieval unreliable.; Store only the latest message per user in a table keyed by user ID.: This loses all prior conversation context, which is required for ongoing, multi-part interactions.

Misconception tags: Assuming one DynamoDB item can contain all user conversations; Overlooking scalability and history requirements

Source trace:

https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Partitioning by user ID with a timestamp SortKey supports efficient storage and retrieval of chronological conversation history for each user, as described in DynamoDB core component documentation.
   Source: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html
   Evidence span: A DynamoDB table is a collection of items, and each item is a collection of attributes. Items in a table are uniquely identified by the primary key.

### P1-AIP-D3-078

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-078 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.2: Build interactive AI systems to maintain context and improve user interactions with FMs (for example, by using Step Functions for clarification workflows, Amazon Comprehend for intent recognition, DynamoDB for conversation history storage). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order007 |
| `accelerated_day` | Day 3 |
| `topic` | Conversation context, history, intent, and state management |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | comprehend-languages |
| `raw_source` | 2026-06-30T051420Z-openai-gpt-4.1-day-03-order007.md item 2 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051420Z |
| `raw_run_id` | order007 |

Stem:

Your conversational AI system uses Amazon Comprehend for detecting the dominant language and identifying user intent, and stores conversation history in DynamoDB. Users speak both supported and unsupported languages, and the AI sometimes fails to route queries properly. Which step should you take to improve routing of unsupported languages?

Options:

1. Check the detected language from Comprehend and branch logic when the confidence is low or language is unsupported.
2. Rely only on the detected intent from Comprehend and ignore language detection.
3. Convert all incoming text to English using translation APIs before passing to Comprehend.
4. Add an additional timestamp field to DynamoDB for each interaction.

Correct answer: Check the detected language from Comprehend and branch logic when the confidence is low or language is unsupported.

Rationale: Comprehend may not support all languages, and its output includes the detected language and confidence, enabling you to apply fallback logic when detection is unreliable or unsupported.

Distractors: Rely only on the detected intent from Comprehend and ignore language detection.: This risks misrouting for unsupported or misdetected languages.; Convert all incoming text to English using translation APIs before passing to Comprehend.: Translation may introduce errors and extra costs; handling unsupported languages at routing is safer.; Add an additional timestamp field to DynamoDB for each interaction.: This does not address language handling or intent detection failures.

Misconception tags: Confusing language and intent detection; Not handling language edge cases

Source trace:

https://docs.aws.amazon.com/comprehend/latest/dg/how-languages.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Branching logic based on detected language and confidence prevents mishandling of inputs for unsupported languages, matching documentation recommendations.
   Source: https://docs.aws.amazon.com/comprehend/latest/dg/how-languages.html
   Evidence span: If a language is not supported, Comprehend will not produce results for language-specific APIs.

### P1-AIP-D3-079

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-079 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.2: Build interactive AI systems to maintain context and improve user interactions with FMs (for example, by using Step Functions for clarification workflows, Amazon Comprehend for intent recognition, DynamoDB for conversation history storage). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order007 |
| `accelerated_day` | Day 3 |
| `topic` | Conversation context, history, intent, and state management |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order007-local-artifact |
| `raw_source` | 2026-06-30T051420Z-openai-gpt-4.1-day-03-order007.md item 3 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051420Z |
| `raw_run_id` | order007 |

Stem:

A support chatbot should ask for clarification only when the user's intent is ambiguous. You use Amazon Comprehend for intent recognition and DynamoDB to store session context. How can you implement this requirement most efficiently?

Options:

1. Set a threshold for Comprehend intent confidence, and use Step Functions to trigger a clarification prompt only when below the threshold.
2. Store every user utterance in DynamoDB, regardless of intent recognition results.
3. Ask for clarification after every message, even if Comprehend is confident.
4. Trigger clarification prompts randomly to check user understanding.

Correct answer: Set a threshold for Comprehend intent confidence, and use Step Functions to trigger a clarification prompt only when below the threshold.

Rationale: Configuring a clarification workflow based on intent confidence ensures prompts are only used when needed, optimizing engagement and operational expense.

Distractors: Store every user utterance in DynamoDB, regardless of intent recognition results.: Storing history is important but doesn't address when clarification is necessary.; Ask for clarification after every message, even if Comprehend is confident.: This will frustrate users and is operationally inefficient.; Trigger clarification prompts randomly to check user understanding.: Random prompts do not target ambiguity and will degrade user experience.

Misconception tags: Misunderstanding intent thresholds; Assuming clarification is always required

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order007-conversation-context-history-intent-state-management.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: By leveraging intent recognition confidence to selectively prompt for clarification, the system efficiently addresses only real ambiguity as best practice.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order007-conversation-context-history-intent-state-management.md
   Evidence span: Use confidence thresholds with intent recognition to trigger clarification workflows

### P1-AIP-D3-080

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-080 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.2: Build interactive AI systems to maintain context and improve user interactions with FMs (for example, by using Step Functions for clarification workflows, Amazon Comprehend for intent recognition, DynamoDB for conversation history storage). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order007 |
| `accelerated_day` | Day 3 |
| `topic` | Conversation context, history, intent, and state management |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Conditional |
| `question_format` | multiple-response |
| `difficulty` | medium |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | dynamodb-core-components |
| `raw_source` | 2026-06-30T051420Z-openai-gpt-4.1-day-03-order007.md item 4 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051420Z |
| `raw_run_id` | order007 |

Stem:

A banking virtual assistant must enforce privacy by ensuring that only the authenticated user can access their own past conversation history. You plan to use Amazon DynamoDB as the storage backend. Which combination of design choices best supports this requirement? (Select TWO.)

Options:

1. Partition conversation data by user ID
2. Use DynamoDB item-level encryption
3. Rely only on session ID as the partition key
4. Implement fine-grained IAM policies tied to user identities
5. Store all conversations in a single public bucket for quick retrieval

Correct answer: Partition conversation data by user ID; Implement fine-grained IAM policies tied to user identities

Rationale: Partitioning by user ID isolates user records, while IAM policies ensure only authorized users can access their history, both of which enforce privacy.

Distractors: Use DynamoDB item-level encryption: Encryption helps protect data at rest but does not enforce per-user access controls.; Rely only on session ID as the partition key: Session ID alone does not guarantee proper user isolation or cannot span multiple sessions.; Store all conversations in a single public bucket for quick retrieval: Storing in a public bucket removes all access controls and is not appropriate for sensitive data.

Misconception tags: Assuming encryption manages authorization; Partition key design errors

Source trace:

https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: User ID partitioning along with identity-aware IAM access ensures records are correctly isolated and access is authorized only for the owner.
   Source: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html
   Evidence span: Each item is uniquely identified by a primary key, and IAM can control access per record.

### P1-AIP-D3-081

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-081 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.2: Build interactive AI systems to maintain context and improve user interactions with FMs (for example, by using Step Functions for clarification workflows, Amazon Comprehend for intent recognition, DynamoDB for conversation history storage). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order007 |
| `accelerated_day` | Day 3 |
| `topic` | Conversation context, history, intent, and state management |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | implement |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | comprehend-languages |
| `raw_source` | 2026-06-30T051420Z-openai-gpt-4.1-day-03-order007.md item 5 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051420Z |
| `raw_run_id` | order007 |

Stem:

For a multilingual support bot using Amazon Comprehend and DynamoDB, you want accurate intent recognition for all supported languages and clear user messaging for unsupported languages. What is the MOST effective workflow improvement?

Options:

1. Check Comprehend’s list of supported languages and add a fallback response when an unsupported language is detected.
2. Restrict system usage to only the English language.
3. Store detected language as a secondary attribute in DynamoDB and ignore it during processing.
4. Run every message through an external translation service before intent recognition.

Correct answer: Check Comprehend’s list of supported languages and add a fallback response when an unsupported language is detected.

Rationale: By proactively checking if the user's language is supported and providing a fallback when not, the system reliably handles all cases and improves the user experience across languages.

Distractors: Restrict system usage to only the English language.: This removes value for multilingual audiences and is not scalable.; Store detected language as a secondary attribute in DynamoDB and ignore it during processing.: Storing without using the detected language fails to resolve any messaging or intent routing issues.; Run every message through an external translation service before intent recognition.: Adding translation introduces potential errors and costs, and is unnecessary for languages already supported.

Misconception tags: Overlooking fallback flows for unsupported languages

Source trace:

https://docs.aws.amazon.com/comprehend/latest/dg/how-languages.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Adding logic to detect and respond to unsupported languages matches Comprehend's documented behavior and recommended integration.
   Source: https://docs.aws.amazon.com/comprehend/latest/dg/how-languages.html
   Evidence span: If a language is not supported, Comprehend will not produce results...

### P1-AIP-D3-082

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-082 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.2: Build interactive AI systems to maintain context and improve user interactions with FMs (for example, by using Step Functions for clarification workflows, Amazon Comprehend for intent recognition, DynamoDB for conversation history storage). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order007 |
| `accelerated_day` | Day 3 |
| `topic` | Conversation context, history, intent, and state management |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | implement |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | comprehend-languages |
| `raw_source` | 2026-06-30T051420Z-openai-gpt-4.1-day-03-order007.md item 6 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051420Z |
| `raw_run_id` | order007 |

Stem:

A global organization wants to deploy an AI assistant that supports intent detection in all regions where it operates. You use Amazon Comprehend for intent recognition. Which approach is BEST for supporting diverse regional languages and consistently handling input where language is undetected or unsupported?

Options:

1. Integrate language detection from Comprehend, verify detection confidence, and provide custom error handling when language is unsupported.
2. Rely on Comprehend to return valid intent for all input regardless of language.
3. Store the region code in DynamoDB and use it to determine language support without running language detection.
4. Automatically translate every incoming message to English before sending to Comprehend.

Correct answer: Integrate language detection from Comprehend, verify detection confidence, and provide custom error handling when language is unsupported.

Rationale: This approach directly addresses inputs in unsupported or undetectable languages, ensuring robust error handling and regional language support.

Distractors: Rely on Comprehend to return valid intent for all input regardless of language.: Comprehend does not guarantee intent detection for unsupported languages.; Store the region code in DynamoDB and use it to determine language support without running language detection.: Region does not guarantee input language and may lead to erroneous handling.; Automatically translate every incoming message to English before sending to Comprehend.: Translation may introduce inaccuracies or information loss and is not needed for supported languages.

Misconception tags: Assuming intent detection works for all languages

Source trace:

https://docs.aws.amazon.com/comprehend/latest/dg/how-languages.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Checking for undetected or unsupported languages and handling errors is required since Comprehend's coverage is not all-encompassing.
   Source: https://docs.aws.amazon.com/comprehend/latest/dg/how-languages.html
   Evidence span: You can detect the dominant language of a text using Amazon Comprehend.

### P1-AIP-D3-083

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-083 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.2: Build interactive AI systems to maintain context and improve user interactions with FMs (for example, by using Step Functions for clarification workflows, Amazon Comprehend for intent recognition, DynamoDB for conversation history storage). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order007 |
| `accelerated_day` | Day 3 |
| `topic` | Conversation context, history, intent, and state management |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | optimize |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | dynamodb-core-components |
| `raw_source` | 2026-06-30T051420Z-openai-gpt-4.1-day-03-order007.md item 7 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051420Z |
| `raw_run_id` | order007 |

Stem:

In a customer support chat system, the bot should use conversation history to provide more relevant responses. Using DynamoDB, which mechanism BEST supports rapid access to the latest N messages for a given user conversation?

Options:

1. Query the table using the user ID as the partition key and sort the results by the timestamp SortKey in descending order, limiting the number of results.
2. Run a table scan and filter by user ID after retrieval.
3. Store all conversation messages in a large JSON attribute and retrieve it for each request.
4. Use a session ID as the partition key and ignore the timestamp in results.

Correct answer: Query the table using the user ID as the partition key and sort the results by the timestamp SortKey in descending order, limiting the number of results.

Rationale: This method leverages DynamoDB’s ability to quickly return a specific number of most recent items within a partition, enabling performant contextual lookups.

Distractors: Run a table scan and filter by user ID after retrieval.: Table scan is slow and expensive, especially at scale.; Store all conversation messages in a large JSON attribute and retrieve it for each request.: This would lead to large item size limits and poor performance for long conversations.; Use a session ID as the partition key and ignore the timestamp in results.: Without time ordering, you cannot guarantee recent context retrieval.

Misconception tags: Poor access pattern design for DynamoDB

Source trace:

https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Querying by partition key and ordered SortKey with an item limit is the standard DynamoDB pattern for retrieving the most recent N entries in a collection.
   Source: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html
   Evidence span: You can query on any table or secondary index. You must provide a partition key value and an equality condition.

### P1-AIP-D3-084

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-084 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.2: Build interactive AI systems to maintain context and improve user interactions with FMs (for example, by using Step Functions for clarification workflows, Amazon Comprehend for intent recognition, DynamoDB for conversation history storage). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order007 |
| `accelerated_day` | Day 3 |
| `topic` | Conversation context, history, intent, and state management |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Conditional |
| `question_format` | multiple-response |
| `difficulty` | medium |
| `cognitive_demand` | implement |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order007-local-artifact |
| `raw_source` | 2026-06-30T051420Z-openai-gpt-4.1-day-03-order007.md item 8 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051420Z |
| `raw_run_id` | order007 |

Stem:

A conversational AI for technical support must manage context, intent, and state for each user. You have implemented DynamoDB for conversation history and Amazon Comprehend for intent recognition. Which actions will help ensure conversations are stateful and intent is tracked correctly across multiple sessions? (Select TWO.)

Options:

1. Store conversation state and user metadata in DynamoDB with a stable user identifier
2. Assign a new random session ID for each message with no reference to prior interactions
3. Store detected intents with each message item in DynamoDB
4. Ignore intent confidence and always select the first returned intent
5. Purge conversation history after every session regardless of user

Correct answer: Store conversation state and user metadata in DynamoDB with a stable user identifier; Store detected intents with each message item in DynamoDB

Rationale: Tying history to a user identifier enables continuity; tracking detected intents per message preserves conversational flow even across sessions.

Distractors: Assign a new random session ID for each message with no reference to prior interactions: This prevents any ability to restore user context or state.; Ignore intent confidence and always select the first returned intent: Not considering intent confidence reduces reliability and may yield incorrect responses.; Purge conversation history after every session regardless of user: This removes context, eliminating the benefits of stateful design.

Misconception tags: Confusing stateless/log-less design with scalable session management; Ignoring intent tracking

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order007-conversation-context-history-intent-state-management.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Persisting state and detected intents with a stable user identifier allows accurate state management and intent tracking across sessions.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order007-conversation-context-history-intent-state-management.md
   Evidence span: Store history and detected intents with each user for cross-session continuity

### P1-AIP-D3-085

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-085 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.2: Build interactive AI systems to maintain context and improve user interactions with FMs (for example, by using Step Functions for clarification workflows, Amazon Comprehend for intent recognition, DynamoDB for conversation history storage). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order007 |
| `accelerated_day` | Day 3 |
| `topic` | Conversation context, history, intent, and state management |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | comprehend-languages |
| `raw_source` | 2026-06-30T051420Z-openai-gpt-4.1-day-03-order007.md item 9 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051420Z |
| `raw_run_id` | order007 |

Stem:

Your AI assistant provides support in several languages using Amazon Comprehend for language and intent detection. You discover the model is misclassifying intent for languages not on the supported list. What should you do to improve intent recognition reliability?

Options:

1. Filter out or branch on inputs in unsupported languages before running intent detection.
2. Continue to process all messages with Comprehend, regardless of language.
3. Retrain Comprehend using your own language datasets.
4. Disable conversation history tracking in DynamoDB for unsupported languages.

Correct answer: Filter out or branch on inputs in unsupported languages before running intent detection.

Rationale: Filtering or handling unsupported languages before intent detection ensures that only compatible messages are processed, avoiding misclassification.

Distractors: Continue to process all messages with Comprehend, regardless of language.: Processing messages in unsupported languages leads to unreliable results.; Retrain Comprehend using your own language datasets.: You cannot train new languages into Comprehend; must use supported languages.; Disable conversation history tracking in DynamoDB for unsupported languages.: History tracking is unrelated to language support or intent detection performance.

Misconception tags: Assuming Comprehend can process all language inputs

Source trace:

https://docs.aws.amazon.com/comprehend/latest/dg/how-languages.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Handling only supported languages as recommended prevents unreliable intent detection processing for unsupported languages.
   Source: https://docs.aws.amazon.com/comprehend/latest/dg/how-languages.html
   Evidence span: If a language is not supported, Comprehend will not produce results for language-specific APIs.

### P1-AIP-D3-086

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-086 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.2: Build interactive AI systems to maintain context and improve user interactions with FMs (for example, by using Step Functions for clarification workflows, Amazon Comprehend for intent recognition, DynamoDB for conversation history storage). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order007 |
| `accelerated_day` | Day 3 |
| `topic` | Conversation context, history, intent, and state management |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order007-local-artifact |
| `raw_source` | 2026-06-30T051420Z-openai-gpt-4.1-day-03-order007.md item 10 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051420Z |
| `raw_run_id` | order007 |

Stem:

A legal advice chatbot must track intent and maintain conversation state through complex multi-turn exchanges, including clarifications and corrections. You already use DynamoDB for message history and Amazon Comprehend for intent detection. Which architectural pattern is most suitable for managing dynamic state transitions and contextually branching conversations?

Options:

1. Use AWS Step Functions to orchestrate the conversation flow, invoking Lambda for stateful transitions based on user input and tracked intent.
2. Store a serialized conversation object in a single DynamoDB item and parse it on each message.
3. Leverage Comprehend’s topic modeling to drive branching logic directly.
4. Assign separate DynamoDB tables for each possible intent.

Correct answer: Use AWS Step Functions to orchestrate the conversation flow, invoking Lambda for stateful transitions based on user input and tracked intent.

Rationale: Step Functions coordinate branching, multi-step processes, allowing integration of stateful transitions and external intent recognition.

Distractors: Store a serialized conversation object in a single DynamoDB item and parse it on each message.: This scales poorly, increases item size, and complicates access.; Leverage Comprehend’s topic modeling to drive branching logic directly.: Comprehend does not natively control state transitions or branch conversations.; Assign separate DynamoDB tables for each possible intent.: This adds unnecessary complexity and hinders generic intent/state tracking.

Misconception tags: Overloading database design; Misusing intent detection as workflow engine

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order007-conversation-context-history-intent-state-management.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Step Functions provides the recommended orchestration for complex, dynamic, stateful conversational flows with intent/context management.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order007-conversation-context-history-intent-state-management.md
   Evidence span: Step Functions can coordinate clarification workflows and context branching using Lambda and DynamoDB state

### P1-AIP-D3-087

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-087 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.2: Build interactive AI systems to maintain context and improve user interactions with FMs (for example, by using Step Functions for clarification workflows, Amazon Comprehend for intent recognition, DynamoDB for conversation history storage). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order007 |
| `accelerated_day` | Day 3 |
| `topic` | Conversation context, history, intent, and state management |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | dynamodb-core-components |
| `raw_source` | 2026-06-30T051420Z-openai-gpt-4.1-day-03-order007.md item 11 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051420Z |
| `raw_run_id` | order007 |

Stem:

A customer service assistant maintains session continuity for users switching devices, such as from desktop to mobile. Which design choice enables a seamless user experience?

Options:

1. Identify and partition conversation records by user ID rather than device or session ID, ensuring history is accessible regardless of device.
2. Partition conversation state by device ID, requiring users to re-authenticate on each device.
3. Use a non-persistent, device-local cache to store conversation state.
4. Purge the DynamoDB conversation table at regular intervals to keep it small.

Correct answer: Identify and partition conversation records by user ID rather than device or session ID, ensuring history is accessible regardless of device.

Rationale: Partitioning by user ID ensures that all conversation history is accessible to the user regardless of device or session, supporting seamless continuity.

Distractors: Partition conversation state by device ID, requiring users to re-authenticate on each device.: This fragments history and forces unnecessary re-authentication.; Use a non-persistent, device-local cache to store conversation state.: Device-local caches cannot support cross-device session continuity.; Purge the DynamoDB conversation table at regular intervals to keep it small.: Purging history removes necessary conversation context for ongoing sessions across devices.

Misconception tags: Confusing device, session, and user identity

Source trace:

https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Partitioning by user ID aligns data model and access patterns for seamless, cross-device conversation continuity.
   Source: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html
   Evidence span: Items in a table are uniquely identified by the primary key

### P1-AIP-D3-088

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-088 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.2: Build interactive AI systems to maintain context and improve user interactions with FMs (for example, by using Step Functions for clarification workflows, Amazon Comprehend for intent recognition, DynamoDB for conversation history storage). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order007 |
| `accelerated_day` | Day 3 |
| `topic` | Conversation context, history, intent, and state management |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | comprehend-languages |
| `raw_source` | 2026-06-30T051420Z-openai-gpt-4.1-day-03-order007.md item 12 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051420Z |
| `raw_run_id` | order007 |

Stem:

A voice assistant uses Comprehend for language and intent detection. After a system update, user feedback reports that intent recognition accuracy for Spanish has dropped significantly. What is the FIRST action you should take to diagnose the problem?

Options:

1. Verify using the Comprehend documentation that Spanish is still a supported language and review service health in the intended region.
2. Retrain the language model using more recent Spanish data.
3. Switch to a third-party service for all Spanish language utterances.
4. Disable support for Spanish until further notice.

Correct answer: Verify using the Comprehend documentation that Spanish is still a supported language and review service health in the intended region.

Rationale: You must first check service documentation and health to rule out configuration, coverage, or service issues before making architectural or operational changes.

Distractors: Retrain the language model using more recent Spanish data.: Comprehend's base models are managed; you cannot retrain for native language support.; Switch to a third-party service for all Spanish language utterances.: This is drastic and should only be considered after confirming the problem is not a misconfiguration.; Disable support for Spanish until further notice.: Disabling Spanish unnecessarily reduces coverage and should be a last resort, not a first diagnostic step.

Misconception tags: Assuming retrainability of managed services

Source trace:

https://docs.aws.amazon.com/comprehend/latest/dg/how-languages.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Confirming up-to-date language support and health ensures correct diagnosis before taking disruptive actions.
   Source: https://docs.aws.amazon.com/comprehend/latest/dg/how-languages.html
   Evidence span: See the list of supported languages for each feature.

### P1-AIP-D3-089

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-089 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.5: Enhance FM performance to refine prompts iteratively and improve response quality beyond basic prompting techniques (for example, by using structured input components, output format specifications, chain-of-thought instruction patterns, feedback loops). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order008 |
| `accelerated_day` | Day 3 |
| `topic` | Advanced prompt engineering and iterative refinement |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Causal; Tacit |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | optimize |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order008-local-artifact |
| `raw_source` | 2026-06-30T051507Z-openai-gpt-4.1-day-03-order008.md item 1 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051507Z |
| `raw_run_id` | order008 |

Stem:

An enterprise GenAI team is consistently getting incorrect entity extraction results from their FM on financial texts, even after basic instructions are added to the prompt. Which iterative prompt refinement approach is most likely to improve model accuracy?

Options:

1. Introduce output format specifications and request chain-of-thought reasoning for each entity.
2. Switch from structured input to free-text instructions.
3. Expand the prompt to include more general example documents.
4. Reduce the context window to the shortest possible length.

Correct answer: Introduce output format specifications and request chain-of-thought reasoning for each entity.

Rationale: Combining structured output expectations with explicit reasoning steps helps guide the model and reduces ambiguity, leading to higher extraction accuracy.

Distractors: Switch from structured input to free-text instructions.: Free-text instructions make outputs less predictable and are less effective than structure for repetitive extraction tasks.; Expand the prompt to include more general example documents.: More examples increase context size but may add unrelated noise and distract the model from the specific extraction task.; Reduce the context window to the shortest possible length.: Short context limits the information the FM uses and is likely to degrade extraction accuracy, not improve it.

Misconception tags: Assuming more data always helps; Ignoring output guidance; Neglecting iterative prompt techniques

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order008-advanced-prompt-engineering-iterative-refinement.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The artifact explicitly calls out format specification and chain-of-thought reasoning as key to advancing extraction prompt effectiveness with FMs.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order008-advanced-prompt-engineering-iterative-refinement.md
   Evidence span: Chain-of-thought instructions and output format specifications can iteratively improve model output quality for structured tasks.

### P1-AIP-D3-090

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-090 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.5: Enhance FM performance to refine prompts iteratively and improve response quality beyond basic prompting techniques (for example, by using structured input components, output format specifications, chain-of-thought instruction patterns, feedback loops). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order008 |
| `accelerated_day` | Day 3 |
| `topic` | Advanced prompt engineering and iterative refinement |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Causal; Tacit |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order008-local-artifact |
| `raw_source` | 2026-06-30T051507Z-openai-gpt-4.1-day-03-order008.md item 2 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051507Z |
| `raw_run_id` | order008 |

Stem:

Your model is consistently adding irrelevant details in generated responses, even after providing examples in the prompt. Which prompt engineering strategy best addresses this?

Options:

1. Specify explicit output constraints and expected field names.
2. Provide the FM with additional negative examples.
3. Switch the FM to a smaller context window.
4. Disable feedback loops to reduce model drift.

Correct answer: Specify explicit output constraints and expected field names.

Rationale: Explicit output constraints guide the FM to avoid unnecessary elaboration and generate targeted content.

Distractors: Provide the FM with additional negative examples.: Negative examples help but are weaker than explicit output constraints for precision requirements.; Switch the FM to a smaller context window.: Reducing context window may cut out essential instructions, potentially worsening accuracy.; Disable feedback loops to reduce model drift.: Feedback loops, when properly used, actually improve iterative performance rather than degrade it.

Misconception tags: Confusing example-based prompting with explicit constraints; Belief context window size alone controls output specificity

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order008-advanced-prompt-engineering-iterative-refinement.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The artifact notes output specification as the primary method to constrain generated content, supporting the keyed answer.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order008-advanced-prompt-engineering-iterative-refinement.md
   Evidence span: Output format specifications can be used to tightly constrain FM responses and limit off-topic details.

### P1-AIP-D3-091

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-091 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.5: Enhance FM performance to refine prompts iteratively and improve response quality beyond basic prompting techniques (for example, by using structured input components, output format specifications, chain-of-thought instruction patterns, feedback loops). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order008 |
| `accelerated_day` | Day 3 |
| `topic` | Advanced prompt engineering and iterative refinement |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Causal; Tacit |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order008-local-artifact |
| `raw_source` | 2026-06-30T051507Z-openai-gpt-4.1-day-03-order008.md item 3 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051507Z |
| `raw_run_id` | order008 |

Stem:

After multiple iterative prompt changes, your team's FM is still returning unordered lists when you require a numbered step-by-step list. What is the most direct next action?

Options:

1. Edit the prompt to explicitly require a numbered, ordered list and add an example.
2. Switch to a different FM provider that prefers numbered lists.
3. Shorten the prompt by removing prior context.
4. Add a feedback loop asking the model to self-correct if the output is unordered.

Correct answer: Edit the prompt to explicitly require a numbered, ordered list and add an example.

Rationale: Explicitly specifying the desired format and demonstrating with an example is the most reliable way to enforce output structure.

Distractors: Switch to a different FM provider that prefers numbered lists.: Model choice is less critical than explicit prompt guidance for output formatting.; Shorten the prompt by removing prior context.: Loss of instructions or examples makes formatting errors more likely.; Add a feedback loop asking the model to self-correct if the output is unordered.: While helpful, this is less direct and less reliable than prompt specification.

Misconception tags: Thinking model choice fixes prompt engineering problems; Ignoring format demonstration

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order008-advanced-prompt-engineering-iterative-refinement.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Directly specifying format requirements with examples is a best practice confirmed in the teaching artifact.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order008-advanced-prompt-engineering-iterative-refinement.md
   Evidence span: Use explicit output format and guidance in your prompt to get consistent, structured responses.

### P1-AIP-D3-092

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-092 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.5: Enhance FM performance to refine prompts iteratively and improve response quality beyond basic prompting techniques (for example, by using structured input components, output format specifications, chain-of-thought instruction patterns, feedback loops). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order008 |
| `accelerated_day` | Day 3 |
| `topic` | Advanced prompt engineering and iterative refinement |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Causal; Tacit |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | optimize |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order008-local-artifact |
| `raw_source` | 2026-06-30T051507Z-openai-gpt-4.1-day-03-order008.md item 4 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051507Z |
| `raw_run_id` | order008 |

Stem:

A team wants to improve summarization quality in an FM-driven customer support app. They notice repetitive information and lack of focus in summaries. Which advanced prompt engineering intervention is most likely to increase summary quality?

Options:

1. Integrate feedback loops that rate and filter summaries based on relevance.
2. Only provide more example summaries in the prompt.
3. Switch the FM to a smaller parameter count for more concise answers.
4. Lower the response temperature to its minimum value.

Correct answer: Integrate feedback loops that rate and filter summaries based on relevance.

Rationale: Feedback loops allow iterative improvement by reinforcing relevant and focused summaries, reducing noise.

Distractors: Only provide more example summaries in the prompt.: Examples can help, but feedback-driven refinement is much more effective for iterative quality gains.; Switch the FM to a smaller parameter count for more concise answers.: Model size does not guarantee improved summary focus.; Lower the response temperature to its minimum value.: Temperature tuning may make output more deterministic but does not specifically improve summarization focus.

Misconception tags: Assuming model parameters or temperature drive output quality more than prompt iteration; Forgetting iterative feedback loops

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order008-advanced-prompt-engineering-iterative-refinement.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The artifact describes feedback loops as the recommended method for iterative quality improvements in prompt engineering.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order008-advanced-prompt-engineering-iterative-refinement.md
   Evidence span: Iteratively improve FM outputs using feedback loops that evaluate and correct output relevance and quality.

### P1-AIP-D3-093

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-093 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.5: Enhance FM performance to refine prompts iteratively and improve response quality beyond basic prompting techniques (for example, by using structured input components, output format specifications, chain-of-thought instruction patterns, feedback loops). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order008 |
| `accelerated_day` | Day 3 |
| `topic` | Advanced prompt engineering and iterative refinement |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Causal; Tacit |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order008-local-artifact |
| `raw_source` | 2026-06-30T051507Z-openai-gpt-4.1-day-03-order008.md item 5 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051507Z |
| `raw_run_id` | order008 |

Stem:

Which combination of advanced prompt engineering techniques is most effective for creating a robust FM-based information extraction workflow?

Options:

1. Chain-of-thought instructions and structured output specifications
2. Increasing the max_tokens parameter and removing output constraints
3. Adding random negative sampling and omitting examples
4. Using as few examples as possible and maximally open-ended prompts

Correct answer: Chain-of-thought instructions and structured output specifications

Rationale: This combination guides both reasoning and output clarity, reducing extraction ambiguity and error.

Distractors: Increasing the max_tokens parameter and removing output constraints: Removing constraints leads to unpredictable, unstructured output.; Adding random negative sampling and omitting examples: Omitting examples and relying purely on negative sampling makes extraction less robust.; Using as few examples as possible and maximally open-ended prompts: Open-ended prompts reduce reliability and increase extraction errors.

Misconception tags: Misunderstanding prompt structure's importance; Belief that length trumps technique

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order008-advanced-prompt-engineering-iterative-refinement.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The source backs up the effectiveness of this combination for clarity and precision in extraction tasks.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order008-advanced-prompt-engineering-iterative-refinement.md
   Evidence span: Combine chain-of-thought prompting and specific output formats for robust information extraction.

### P1-AIP-D3-094

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-094 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.5: Enhance FM performance to refine prompts iteratively and improve response quality beyond basic prompting techniques (for example, by using structured input components, output format specifications, chain-of-thought instruction patterns, feedback loops). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order008 |
| `accelerated_day` | Day 3 |
| `topic` | Advanced prompt engineering and iterative refinement |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Causal; Tacit |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order008-local-artifact |
| `raw_source` | 2026-06-30T051507Z-openai-gpt-4.1-day-03-order008.md item 6 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051507Z |
| `raw_run_id` | order008 |

Stem:

Your organization observes that slight changes in the prompt wording cause FM outputs to swing unpredictably. What advanced prompt engineering strategy can increase consistency of outputs?

Options:

1. Parameterize critical parts of the prompt and standardize formatting.
2. Reduce FM inference temperature to zero.
3. Use zero-shot prompting exclusively.
4. Switch to a different FM vendor.

Correct answer: Parameterize critical parts of the prompt and standardize formatting.

Rationale: Parameterization with standardized inputs ensures consistent structure and reduces unintended ambiguity.

Distractors: Reduce FM inference temperature to zero.: While lowering temperature can help, parameterization directly addresses prompt-induced variance.; Use zero-shot prompting exclusively.: Zero-shot approaches tend to be less stable than structured, parameterized prompts.; Switch to a different FM vendor.: Changing vendors does not address prompt structure issues—the problem is not provider-specific.

Misconception tags: Overreliance on temperature adjustment; FM provider fallacy

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order008-advanced-prompt-engineering-iterative-refinement.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Artifact evidence clearly states parameterization and structure improve prompt consistency.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order008-advanced-prompt-engineering-iterative-refinement.md
   Evidence span: Use parameterized templates and structure to reduce output variability from prompt changes.

### P1-AIP-D3-095

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-095 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.5: Enhance FM performance to refine prompts iteratively and improve response quality beyond basic prompting techniques (for example, by using structured input components, output format specifications, chain-of-thought instruction patterns, feedback loops). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order008 |
| `accelerated_day` | Day 3 |
| `topic` | Advanced prompt engineering and iterative refinement |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Causal; Tacit |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | implement |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order008-local-artifact |
| `raw_source` | 2026-06-30T051507Z-openai-gpt-4.1-day-03-order008.md item 7 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051507Z |
| `raw_run_id` | order008 |

Stem:

You want your FM to provide a detailed explanation of its answer as part of every response. Your initial prompts yield only simple answers. What should you do to achieve your goal?

Options:

1. Instruct the FM in the prompt to provide step-by-step reasoning using chain-of-thought.
2. Increase the inference temperature above default.
3. Remove all output constraints so the FM is free to elaborate.
4. Add more context documents to the prompt input.

Correct answer: Instruct the FM in the prompt to provide step-by-step reasoning using chain-of-thought.

Rationale: Requesting chain-of-thought reasoning in the prompt encourages FMs to explain their answers in detail.

Distractors: Increase the inference temperature above default.: Higher temperature increases randomness, not reasoned explanation.; Remove all output constraints so the FM is free to elaborate.: Removing constraints does not guarantee explanations and may hurt response structure.; Add more context documents to the prompt input.: More context may distract or overwhelm the FM, not improve reasoning.

Misconception tags: Equating randomness with reasoning; Assuming increased context guarantees detail

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order008-advanced-prompt-engineering-iterative-refinement.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Explicitly requesting reasoning steps is a proven advanced prompting technique per the resource.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order008-advanced-prompt-engineering-iterative-refinement.md
   Evidence span: Chain-of-thought instructions encourage step-by-step explanations in FM responses.

### P1-AIP-D3-096

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-096 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.5: Enhance FM performance to refine prompts iteratively and improve response quality beyond basic prompting techniques (for example, by using structured input components, output format specifications, chain-of-thought instruction patterns, feedback loops). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order008 |
| `accelerated_day` | Day 3 |
| `topic` | Advanced prompt engineering and iterative refinement |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Causal; Tacit |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | optimize |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order008-local-artifact |
| `raw_source` | 2026-06-30T051507Z-openai-gpt-4.1-day-03-order008.md item 8 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051507Z |
| `raw_run_id` | order008 |

Stem:

A developer needs to iteratively improve the factuality of FM responses in their knowledge assistant. Which workflow offers the best solution?

Options:

1. Introduce a feedback loop to rank outputs and adjust prompts based on factual correctness.
2. Switch to a prompt without any context and rely on the FM's pretraining.
3. Use as many diverse context sources as possible for each prompt regardless of length.
4. Manually curate each FM response after generation.

Correct answer: Introduce a feedback loop to rank outputs and adjust prompts based on factual correctness.

Rationale: Feedback loops allow automated, systematic iterative refinement to optimize for factual accuracy.

Distractors: Switch to a prompt without any context and rely on the FM's pretraining.: Lack of context reduces the model's ability to generate current, accurate answers.; Use as many diverse context sources as possible for each prompt regardless of length.: Excessive, unfiltered context makes it hard for the FM to focus and can harm results.; Manually curate each FM response after generation.: Manual curation is not scalable or iterative, unlike feedback-driven workflows.

Misconception tags: Ignoring feedback loop benefits; Assuming raw model knowledge suffices

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order008-advanced-prompt-engineering-iterative-refinement.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Introducing feedback loops is the workflow explicitly described for quality/factuality improvement.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order008-advanced-prompt-engineering-iterative-refinement.md
   Evidence span: Automate iterative prompt refinement using feedback or ranking based on target response criteria.

### P1-AIP-D3-097

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-097 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.5: Enhance FM performance to refine prompts iteratively and improve response quality beyond basic prompting techniques (for example, by using structured input components, output format specifications, chain-of-thought instruction patterns, feedback loops). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order008 |
| `accelerated_day` | Day 3 |
| `topic` | Advanced prompt engineering and iterative refinement |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Causal; Tacit |
| `question_format` | multiple-response |
| `difficulty` | exam-plus |
| `cognitive_demand` | implement |
| `estimated_time_seconds` | 180 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order008-local-artifact |
| `raw_source` | 2026-06-30T051507Z-openai-gpt-4.1-day-03-order008.md item 9 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051507Z |
| `raw_run_id` | order008 |

Stem:

A GenAI developer wants to reduce hallucinations in RAG responses using prompt engineering alone. Which techniques should they use? (Select TWO.)

Options:

1. Enforce strict output formatting corresponding to source citations.
2. Request the FM reason step-by-step before generating an answer.
3. Add more unrelated context documents to the prompt.
4. Reduce the inference temperature to its absolute minimum.
5. Rely on zero-shot prompting only.

Correct answer: Enforce strict output formatting corresponding to source citations.; Request the FM reason step-by-step before generating an answer.

Rationale: Combining explicit citation format requirements with chain-of-thought reasoning minimizes hallucinations by anchoring answers to sources and requiring stepwise logic.

Distractors: Add more unrelated context documents to the prompt.: Irrelevant context may increase hallucinations by distracting the FM.; Reduce the inference temperature to its absolute minimum.: Although lowering temperature can reduce randomness, it does not ensure factuality or citation.; Rely on zero-shot prompting only.: Zero-shot prompting is less controlled and more prone to hallucinations.

Misconception tags: Assuming model temperature or zero-shot solves hallucination risk

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order008-advanced-prompt-engineering-iterative-refinement.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Both citing sources by format and stepwise reasoning are advanced prompt techniques shown to reduce hallucinations in the artifact.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order008-advanced-prompt-engineering-iterative-refinement.md
   Evidence span: Use chain-of-thought steps and strict output structure for attribution to mitigate hallucination risk.

### P1-AIP-D3-098

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-098 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.5: Enhance FM performance to refine prompts iteratively and improve response quality beyond basic prompting techniques (for example, by using structured input components, output format specifications, chain-of-thought instruction patterns, feedback loops). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order008 |
| `accelerated_day` | Day 3 |
| `topic` | Advanced prompt engineering and iterative refinement |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Causal; Tacit |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order008-local-artifact |
| `raw_source` | 2026-06-30T051507Z-openai-gpt-4.1-day-03-order008.md item 10 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051507Z |
| `raw_run_id` | order008 |

Stem:

During a prompt refinement session, your FM model unexpectedly returns very verbose, unfocused summaries. You have already provided one example summary. What is the next best step?

Options:

1. Add output length constraints and request a summary in a fixed word range.
2. Increase the number of example summaries in the prompt.
3. Switch to free-form output and remove all output-specific instructions.
4. Request more context documents for the same summary task.

Correct answer: Add output length constraints and request a summary in a fixed word range.

Rationale: Explicitly constraining output length is a key prompt engineering technique for controlling verbosity and focus.

Distractors: Increase the number of example summaries in the prompt.: More examples may help marginally, but explicit constraints will directly shape output length.; Switch to free-form output and remove all output-specific instructions.: Removing constraints will worsen verbosity and focus, not improve.; Request more context documents for the same summary task.: Increasing context may increase verbosity by giving the FM more material to include.

Misconception tags: Assuming examples alone control output verbosity

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order008-advanced-prompt-engineering-iterative-refinement.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The resource states length/word count constraints help control verbosity in FM output.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order008-advanced-prompt-engineering-iterative-refinement.md
   Evidence span: Prompt engineering can directly shape output length and scope by specifying constraints.

### P1-AIP-D3-099

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-099 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.5: Enhance FM performance to refine prompts iteratively and improve response quality beyond basic prompting techniques (for example, by using structured input components, output format specifications, chain-of-thought instruction patterns, feedback loops). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order008 |
| `accelerated_day` | Day 3 |
| `topic` | Advanced prompt engineering and iterative refinement |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Causal; Tacit |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order008-local-artifact |
| `raw_source` | 2026-06-30T051507Z-openai-gpt-4.1-day-03-order008.md item 11 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051507Z |
| `raw_run_id` | order008 |

Stem:

A product manager wants to enable non-technical users to customize AI assistant prompt outputs by changing response structure and tone. What is the most maintainable approach for supporting this?

Options:

1. Expose prompt parameters such as tone and format as input variables in a parameterized template.
2. Let users edit free-text prompts in the configuration file.
3. Require users to provide feedback loops and rank outputs.
4. Restrict output formatting and tone to fixed values to prevent variability.

Correct answer: Expose prompt parameters such as tone and format as input variables in a parameterized template.

Rationale: Parameterized prompt templates enable controlled, consistent customization without exposing low-level implementation or risking errors.

Distractors: Let users edit free-text prompts in the configuration file.: Free-form editing by non-technical users is error-prone and less maintainable.; Require users to provide feedback loops and rank outputs.: Feedback mechanisms improve output, but are too complex for non-technical users to manage.; Restrict output formatting and tone to fixed values to prevent variability.: This approach sacrifices needed flexibility and does not enable user-level customization.

Misconception tags: Belief only technical users can configure prompts; Neglecting parameterization for customization

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order008-advanced-prompt-engineering-iterative-refinement.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The artifact details parameterized structure as the best practice for customizable prompts.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order008-advanced-prompt-engineering-iterative-refinement.md
   Evidence span: Parameterized and structured prompts support easy customization at deployment time.

### P1-AIP-D3-100

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-100 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.5: Enhance FM performance to refine prompts iteratively and improve response quality beyond basic prompting techniques (for example, by using structured input components, output format specifications, chain-of-thought instruction patterns, feedback loops). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order008 |
| `accelerated_day` | Day 3 |
| `topic` | Advanced prompt engineering and iterative refinement |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Causal; Tacit |
| `question_format` | multiple-response |
| `difficulty` | exam-plus |
| `cognitive_demand` | implement |
| `estimated_time_seconds` | 180 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order008-local-artifact |
| `raw_source` | 2026-06-30T051507Z-openai-gpt-4.1-day-03-order008.md item 12 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051507Z |
| `raw_run_id` | order008 |

Stem:

Which advanced prompt engineering practices collectively increase the reliability and auditability of AI-generated outputs in regulated environments? (Select TWO.)

Options:

1. Define and enforce output schemas for every prompt.
2. Use traceable chain-of-thought reasoning instructions.
3. Allow only zero-shot, unrestricted generations.
4. Never modify prompts after deployment.
5. Allow FMs to self-determine format and logic per request.

Correct answer: Define and enforce output schemas for every prompt.; Use traceable chain-of-thought reasoning instructions.

Rationale: Output schemas ensure outputs always match required standards, and traceable reasoning allows for justification—both critical in regulated use cases.

Distractors: Allow only zero-shot, unrestricted generations.: Unconstrained, zero-shot outputs are neither reliable nor auditable.; Never modify prompts after deployment.: Lack of prompt iteration is unsuitable for evolving regulatory needs.; Allow FMs to self-determine format and logic per request.: Self-determined outputs break auditability and reliability assurances.

Misconception tags: Confusing flexibility with auditability; Forgetting formal structure's compliance benefit

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order008-advanced-prompt-engineering-iterative-refinement.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Defining schemas and traceable reasoning is directly recommended in the artifact for regulated environments.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order008-advanced-prompt-engineering-iterative-refinement.md
   Evidence span: Output schemas and reasoning structure are highlighted for accountability in high-governance settings.

### P1-AIP-D3-101

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-101 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.5: Enhance FM performance to refine prompts iteratively and improve response quality beyond basic prompting techniques (for example, by using structured input components, output format specifications, chain-of-thought instruction patterns, feedback loops). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order008 |
| `accelerated_day` | Day 3 |
| `topic` | Advanced prompt engineering and iterative refinement |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Causal; Tacit |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | optimize |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order008-local-artifact |
| `raw_source` | 2026-06-30T051507Z-openai-gpt-4.1-day-03-order008.md item 13 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051507Z |
| `raw_run_id` | order008 |

Stem:

A technical lead observes that team members keep iterating prompts but ignore model response failures when actual data is missing or ambiguous. To robustly improve output quality beyond prompt language, what should the team focus on in conjunction with iterative prompt engineering?

Options:

1. Implement application-level feedback and validation of FM responses.
2. Only continue prompt iteration cycles until outputs are satisfactory.
3. Switch to a more powerful FM with more training data.
4. Expand the context to cover as many knowledge domains as possible.

Correct answer: Implement application-level feedback and validation of FM responses.

Rationale: App-level feedback and validation are necessary companions to prompt iteration for dependable, correct outputs—prompt language alone is insufficient.

Distractors: Only continue prompt iteration cycles until outputs are satisfactory.: Prompt refinement can help, but without validation and feedback, errors may persist undetected.; Switch to a more powerful FM with more training data.: A bigger model doesn't solve issues from data ambiguity or missing context.; Expand the context to cover as many knowledge domains as possible.: Adding more domains can confuse the FM and decrease precision of answers.

Misconception tags: Overestimating prompt iteration effectiveness alone; Ignoring need for validation and feedback

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order008-advanced-prompt-engineering-iterative-refinement.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: This recommendation is explicitly stated in the artifact, supporting the correct answer.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order008-advanced-prompt-engineering-iterative-refinement.md
   Evidence span: Iterative refinement should be coupled with application-level validation and end-user feedback for best quality.

### P1-AIP-D3-102

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-102 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.3: Implement comprehensive prompt management and governance systems to ensure consistency and oversight of FM operations (for example, by using Amazon Bedrock Prompt Management to create parameterized templates and approval workflows, Amazon S3 to store template repositories, AWS CloudTrail to track usage, Amazon CloudWatch Logs to log access). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order009 |
| `accelerated_day` | Day 3 |
| `topic` | Prompt versioning, repositories, approvals, and governance |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Normative; Institutional; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order009-local-artifact |
| `raw_source` | 2026-06-30T051603Z-openai-gpt-4.1-day-03-order009.md item 1 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051603Z |
| `raw_run_id` | order009 |

Stem:

A company is deploying a GenAI application and wants to maintain strict oversight over prompt updates. In their governance plan, which control is most effective for ensuring changes to critical prompts are tracked and traceable when using Amazon Bedrock Prompt Management?

Options:

1. Enabling AWS CloudTrail to log all prompt template operations.
2. Relying solely on version identifiers in template names.
3. Using IAM roles to restrict access to the prompt builder UI.
4. Storing prompt templates in a shared Google Drive folder.

Correct answer: Enabling AWS CloudTrail to log all prompt template operations.

Rationale: AWS CloudTrail provides detailed logs of all operations, ensuring traceability and accountability for changes made to prompt templates.

Distractors: Relying solely on version identifiers in template names.: Version identifiers help with organization but do not provide traceability or audit logs.; Using IAM roles to restrict access to the prompt builder UI.: IAM roles limit access but do not ensure changes are tracked after access is granted.; Storing prompt templates in a shared Google Drive folder.: Google Drive is not integrated with AWS control and does not offer the necessary integration or logging.

Misconception tags: auditability-vs-versioning; IAM-is-not-audit

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order009-prompt-versioning-repositories-approvals-governance.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: CloudTrail integration ensures every prompt operation is logged, enabling audits and compliance reviews as per governance standards.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order009-prompt-versioning-repositories-approvals-governance.md
   Evidence span: Enable AWS CloudTrail to provide an audit trail of prompt management operations for traceability requirements.

### P1-AIP-D3-103

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-103 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.3: Implement comprehensive prompt management and governance systems to ensure consistency and oversight of FM operations (for example, by using Amazon Bedrock Prompt Management to create parameterized templates and approval workflows, Amazon S3 to store template repositories, AWS CloudTrail to track usage, Amazon CloudWatch Logs to log access). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order009 |
| `accelerated_day` | Day 3 |
| `topic` | Prompt versioning, repositories, approvals, and governance |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Normative; Institutional; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | implement |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order009-local-artifact |
| `raw_source` | 2026-06-30T051603Z-openai-gpt-4.1-day-03-order009.md item 2 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051603Z |
| `raw_run_id` | order009 |

Stem:

Your GenAI team is experiencing drift in prompt consistency across staging and production environments. You want to standardize prompt management while maintaining quick access for different development teams. Which mechanism best supports prompt consistency, access control, and automated promotion to production?

Options:

1. Storing prompt templates as parameterized files in Amazon S3 with approval workflow integration.
2. Allowing individual developers to manage local prompt files on their laptops.
3. Using a shared Slack channel to exchange updated prompt snippets.
4. Emailing prompt text to a pipeline admin for manual deployment.

Correct answer: Storing prompt templates as parameterized files in Amazon S3 with approval workflow integration.

Rationale: Storing prompts in S3 with integrated approval workflows standardizes location and versioning while allowing access control and promoting discipline.

Distractors: Allowing individual developers to manage local prompt files on their laptops.: This is prone to inconsistency and lacks central control.; Using a shared Slack channel to exchange updated prompt snippets.: Slack does not provide versioning or approval controls.; Emailing prompt text to a pipeline admin for manual deployment.: This is error-prone and untracked, lacking automation and governance.

Misconception tags: local-practices-vs-cloud-repo; manual-deployment

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order009-prompt-versioning-repositories-approvals-governance.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: S3 repositories with workflow integration provide both versioning and approval controls, as recommended for prompt governance.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order009-prompt-versioning-repositories-approvals-governance.md
   Evidence span: Store prompt templates in Amazon S3 and integrate with approval workflows for controlled promotion.

### P1-AIP-D3-104

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-104 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.3: Implement comprehensive prompt management and governance systems to ensure consistency and oversight of FM operations (for example, by using Amazon Bedrock Prompt Management to create parameterized templates and approval workflows, Amazon S3 to store template repositories, AWS CloudTrail to track usage, Amazon CloudWatch Logs to log access). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order009 |
| `accelerated_day` | Day 3 |
| `topic` | Prompt versioning, repositories, approvals, and governance |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Normative; Institutional; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order009-local-artifact |
| `raw_source` | 2026-06-30T051603Z-openai-gpt-4.1-day-03-order009.md item 3 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051603Z |
| `raw_run_id` | order009 |

Stem:

A regulated enterprise must restrict who can update prompts and ensure those changes are only pushed to production after formal approval. Using Amazon Bedrock Prompt Management, which combination most conservatively enforces this policy?

Options:

1. Configure approval workflows and restrict write permissions on production prompt repositories.
2. Allow all team members editor access to the production prompt repository.
3. Enable public read/write access on S3 buckets where prompts reside.
4. Use version control comments to signal approvals instead of workflows.

Correct answer: Configure approval workflows and restrict write permissions on production prompt repositories.

Rationale: This configuration ensures only authorized changes are promoted following formal approval steps, fulfilling regulatory and governance needs.

Distractors: Allow all team members editor access to the production prompt repository.: This bypasses governance, increasing risks of unauthorized changes.; Enable public read/write access on S3 buckets where prompts reside.: This is highly insecure and violates compliance requirements.; Use version control comments to signal approvals instead of workflows.: Comments cannot enforce actual approval or block deployment.

Misconception tags: approval-vs-access-control; comments-not-approvals

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order009-prompt-versioning-repositories-approvals-governance.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Approval workflows combined with permission restrictions directly address regulatory requirements for change control.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order009-prompt-versioning-repositories-approvals-governance.md
   Evidence span: Establish approval workflows and restrict production write access to enforce prompt governance.

### P1-AIP-D3-105

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-105 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.3: Implement comprehensive prompt management and governance systems to ensure consistency and oversight of FM operations (for example, by using Amazon Bedrock Prompt Management to create parameterized templates and approval workflows, Amazon S3 to store template repositories, AWS CloudTrail to track usage, Amazon CloudWatch Logs to log access). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order009 |
| `accelerated_day` | Day 3 |
| `topic` | Prompt versioning, repositories, approvals, and governance |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Normative; Institutional; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order009-local-artifact |
| `raw_source` | 2026-06-30T051603Z-openai-gpt-4.1-day-03-order009.md item 4 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051603Z |
| `raw_run_id` | order009 |

Stem:

A GenAI platform team needs to track which prompts led to unexpected model behaviors in production. What is the most efficient way to capture usage and enable rapid auditing of prompt activity?

Options:

1. Enable event logging (such as AWS CloudTrail and CloudWatch Logs) for all prompt management operations.
2. Rely on model inference logs without prompt context.
3. Manually review deployed prompt template files for each incident.
4. Use spreadsheet tracking with manually updated logs.

Correct answer: Enable event logging (such as AWS CloudTrail and CloudWatch Logs) for all prompt management operations.

Rationale: Centralized event logging provides prompt usage context and audit trails essential for incident analysis.

Distractors: Rely on model inference logs without prompt context.: Model inference logs alone lack necessary prompt template context for full audit.; Manually review deployed prompt template files for each incident.: Manual review is inefficient, error-prone, and not real-time.; Use spreadsheet tracking with manually updated logs.: Manual logs cannot scale or ensure reliability/auditability.

Misconception tags: logs-vs-inference-output; manual-vs-automated-audit

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order009-prompt-versioning-repositories-approvals-governance.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: CloudTrail and CloudWatch Logs are designed to correlate prompt management actions with downstream model behaviors.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order009-prompt-versioning-repositories-approvals-governance.md
   Evidence span: Use CloudTrail and CloudWatch Logs to capture prompt management activity and correlate to incidents.

### P1-AIP-D3-106

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-106 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.3: Implement comprehensive prompt management and governance systems to ensure consistency and oversight of FM operations (for example, by using Amazon Bedrock Prompt Management to create parameterized templates and approval workflows, Amazon S3 to store template repositories, AWS CloudTrail to track usage, Amazon CloudWatch Logs to log access). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order009 |
| `accelerated_day` | Day 3 |
| `topic` | Prompt versioning, repositories, approvals, and governance |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Normative; Institutional; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | judge |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order009-local-artifact |
| `raw_source` | 2026-06-30T051603Z-openai-gpt-4.1-day-03-order009.md item 5 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051603Z |
| `raw_run_id` | order009 |

Stem:

You have defined critical business prompts as parameterized templates in Amazon Bedrock Prompt Management. Which policy configuration best ensures that only QA-approved, unchanged prompt templates are deployed to production?

Options:

1. Require template approval and enforce repository immutability until passed checks are complete.
2. Allow direct manual edits in production after development testing.
3. Use a shared repository and trust developers to only make approved changes.
4. Configure templates to allow dynamic overwrites based on latest test run.

Correct answer: Require template approval and enforce repository immutability until passed checks are complete.

Rationale: Approval and immutability settings ensure only authorized and tested prompt templates reach production unchanged.

Distractors: Allow direct manual edits in production after development testing.: Manual edits risk bypassing QA and result in inconsistent deployments.; Use a shared repository and trust developers to only make approved changes.: Trust alone doesn't guarantee compliance; lacks enforceable policy.; Configure templates to allow dynamic overwrites based on latest test run.: Dynamic overwrites can introduce unapproved changes.

Misconception tags: QA-policy-vs-trust; immutability-vs-live-edit

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order009-prompt-versioning-repositories-approvals-governance.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Combining approval with immutability prevents unauthorized or untested prompt modifications in production.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order009-prompt-versioning-repositories-approvals-governance.md
   Evidence span: Require prompt approval workflows and lock production templates until approval and checks are complete.

### P1-AIP-D3-107

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-107 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.3: Implement comprehensive prompt management and governance systems to ensure consistency and oversight of FM operations (for example, by using Amazon Bedrock Prompt Management to create parameterized templates and approval workflows, Amazon S3 to store template repositories, AWS CloudTrail to track usage, Amazon CloudWatch Logs to log access). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order009 |
| `accelerated_day` | Day 3 |
| `topic` | Prompt versioning, repositories, approvals, and governance |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Normative; Institutional; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order009-local-artifact |
| `raw_source` | 2026-06-30T051603Z-openai-gpt-4.1-day-03-order009.md item 6 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051603Z |
| `raw_run_id` | order009 |

Stem:

During a prompt versioning review, your team finds multiple copies of similar templates with inconsistent identifiers. What is the best step to improve oversight and enable reliable governance of prompt changes?

Options:

1. Adopt a structured versioning schema and enforce parameterized template storage in a centralized repository.
2. Switch to using unstructured file names in a flat S3 bucket.
3. Assign version numbers only informally in Slack messages.
4. Let each microservice independently index their own prompt reference set.

Correct answer: Adopt a structured versioning schema and enforce parameterized template storage in a centralized repository.

Rationale: Structured versioning and centralized storage support consistent tracking, governance, and seamless auditability across teams.

Distractors: Switch to using unstructured file names in a flat S3 bucket.: Unstructured names make governance and search difficult.; Assign version numbers only informally in Slack messages.: Informal processes cannot be enforced or audited.; Let each microservice independently index their own prompt reference set.: Decentralizing indexing introduces risk of inconsistency.

Misconception tags: naming-vs-schema; independent-indexing

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order009-prompt-versioning-repositories-approvals-governance.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: A versioning schema in a central repository both enforces structure and simplifies oversight.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order009-prompt-versioning-repositories-approvals-governance.md
   Evidence span: Implement version control schema and centralized parameterized template repository for prompt management.

### P1-AIP-D3-108

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-108 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.3: Implement comprehensive prompt management and governance systems to ensure consistency and oversight of FM operations (for example, by using Amazon Bedrock Prompt Management to create parameterized templates and approval workflows, Amazon S3 to store template repositories, AWS CloudTrail to track usage, Amazon CloudWatch Logs to log access). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order009 |
| `accelerated_day` | Day 3 |
| `topic` | Prompt versioning, repositories, approvals, and governance |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Normative; Institutional; Embedded |
| `question_format` | multiple-response |
| `difficulty` | hard |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order009-local-artifact |
| `raw_source` | 2026-06-30T051603Z-openai-gpt-4.1-day-03-order009.md item 7 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051603Z |
| `raw_run_id` | order009 |

Stem:

A GenAI application receives a critical security finding related to prompt tampering. Which combination of governance controls should you deploy to address both unauthorized edits and forensic investigation requirements? (Select TWO.)

Options:

1. Enable AWS CloudTrail for prompt repository actions
2. Enforce approval workflows for prompt updates
3. Allow open access to prompt editing for rapid innovation
4. Disable versioning to save storage costs
5. Log prompt usage in Amazon CloudWatch Logs

Correct answer: Enable AWS CloudTrail for prompt repository actions; Enforce approval workflows for prompt updates

Rationale: CloudTrail provides forensic audit data, while approval workflows prevent unauthorized prompt changes before production.

Distractors: Allow open access to prompt editing for rapid innovation: Open access directly increases security risk, counter to the scenario's requirements.; Disable versioning to save storage costs: Versioning is required for traceability and cannot be sacrificed for cost here.; Log prompt usage in Amazon CloudWatch Logs: Prompt usage logs are helpful, but do not prevent unauthorized edits.

Misconception tags: logging-vs-authorization; approvals-vs-open-access

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order009-prompt-versioning-repositories-approvals-governance.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: CloudTrail ensures auditable actions and approval workflows ensure that only authorized changes are made to production prompts.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order009-prompt-versioning-repositories-approvals-governance.md
   Evidence span: Deploy CloudTrail and approval workflows to ensure security and traceability for prompt management.

### P1-AIP-D3-109

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-109 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.3: Implement comprehensive prompt management and governance systems to ensure consistency and oversight of FM operations (for example, by using Amazon Bedrock Prompt Management to create parameterized templates and approval workflows, Amazon S3 to store template repositories, AWS CloudTrail to track usage, Amazon CloudWatch Logs to log access). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order009 |
| `accelerated_day` | Day 3 |
| `topic` | Prompt versioning, repositories, approvals, and governance |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Normative; Institutional; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | optimize |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order009-local-artifact |
| `raw_source` | 2026-06-30T051603Z-openai-gpt-4.1-day-03-order009.md item 8 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051603Z |
| `raw_run_id` | order009 |

Stem:

After rolling out a new prompt version, users report unexpected model outputs tied to the update. Which governance process most effectively supports a controlled rollback and prevents similar incidents?

Options:

1. Maintain strict versioning of all prompt templates with approval checkpoints and rollback procedures.
2. Replace the broken prompt with an ad hoc hot patch.
3. Overwrite the broken prompt in-place and skip version control for faster recovery.
4. Ask users to refresh their browser cache to receive the corrected prompt.

Correct answer: Maintain strict versioning of all prompt templates with approval checkpoints and rollback procedures.

Rationale: This approach ensures you can track, approve, and revert prompts systematically, limiting risk and supporting accountability.

Distractors: Replace the broken prompt with an ad hoc hot patch.: Hot patches may introduce new errors and bypass established governance.; Overwrite the broken prompt in-place and skip version control for faster recovery.: Skipping version control removes the ability to audit or roll back.; Ask users to refresh their browser cache to receive the corrected prompt.: Browser cache refresh does not address governance or prompt state.

Misconception tags: hotfix-vs-versioned-rollback; blaming-cache

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order009-prompt-versioning-repositories-approvals-governance.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Strict template versioning and checkpointing enable dependable, auditable rollback and issue prevention.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order009-prompt-versioning-repositories-approvals-governance.md
   Evidence span: Use versioning, approvals, and structured rollback to handle prompt changes cleanly.

### P1-AIP-D3-110

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-110 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.3: Implement comprehensive prompt management and governance systems to ensure consistency and oversight of FM operations (for example, by using Amazon Bedrock Prompt Management to create parameterized templates and approval workflows, Amazon S3 to store template repositories, AWS CloudTrail to track usage, Amazon CloudWatch Logs to log access). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order009 |
| `accelerated_day` | Day 3 |
| `topic` | Prompt versioning, repositories, approvals, and governance |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Normative; Institutional; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order009-local-artifact |
| `raw_source` | 2026-06-30T051603Z-openai-gpt-4.1-day-03-order009.md item 9 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051603Z |
| `raw_run_id` | order009 |

Stem:

Your organization's GenAI audit uncovered gaps in documentation of who approved prompt changes. Which additional governance measure will directly address this traceability gap?

Options:

1. Integrate approval metadata and approver identity storage in the prompt repository.
2. Allow code reviews to implicitly substitute for formal approvals.
3. Expect engineering managers to remember which prompts they approved.
4. Remove prompt approvals for efficiency.

Correct answer: Integrate approval metadata and approver identity storage in the prompt repository.

Rationale: Storing approver metadata provides traceable, auditable records about who approved which prompt and when.

Distractors: Allow code reviews to implicitly substitute for formal approvals.: Code reviews are necessary, but do not provide explicit, trusted audit records for prompt governance.; Expect engineering managers to remember which prompts they approved.: Memory is unreliable; compliance demands retrievable audit trails.; Remove prompt approvals for efficiency.: This process increases risk and reduces compliance, contrary to requirements.

Misconception tags: implicit-vs-explicit-approvals; memory-vs-metadata

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order009-prompt-versioning-repositories-approvals-governance.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Explicit metadata for approvals addresses traceability and regulatory requirements.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order009-prompt-versioning-repositories-approvals-governance.md
   Evidence span: Record approval status and approver details alongside the template for auditability.

### P1-AIP-D3-111

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-111 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.3: Implement comprehensive prompt management and governance systems to ensure consistency and oversight of FM operations (for example, by using Amazon Bedrock Prompt Management to create parameterized templates and approval workflows, Amazon S3 to store template repositories, AWS CloudTrail to track usage, Amazon CloudWatch Logs to log access). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order009 |
| `accelerated_day` | Day 3 |
| `topic` | Prompt versioning, repositories, approvals, and governance |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Normative; Institutional; Embedded |
| `question_format` | multiple-response |
| `difficulty` | medium |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order009-local-artifact |
| `raw_source` | 2026-06-30T051603Z-openai-gpt-4.1-day-03-order009.md item 10 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051603Z |
| `raw_run_id` | order009 |

Stem:

The GenAI platform lead wants to improve efficiency for developers updating prompt templates while minimizing risk of unwanted changes in production. Which two practices best enable rapid, safe iteration within an approved governance framework? (Select TWO.)

Options:

1. Use development branches or workspaces for experimentation.
2. Require production repository changes to go through formal approval workflows.
3. Allow direct edits to production templates for minor bug fixes.
4. Permit anyone to merge changes into production for faster turnaround.
5. Track all prompt template changes with version control.

Correct answer: Use development branches or workspaces for experimentation.; Require production repository changes to go through formal approval workflows.

Rationale: Experimentation in isolated branches supports efficiency, while formal approvals for production ensure risk controls.

Distractors: Allow direct edits to production templates for minor bug fixes.: Direct edits jeopardize governance and control.; Permit anyone to merge changes into production for faster turnaround.: Open merging without approvals undermines all oversight.; Track all prompt template changes with version control.: Version control alone is not sufficient without workflow for approvals.

Misconception tags: dev-branch-vs-prod; approval-vs-open-merges

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order009-prompt-versioning-repositories-approvals-governance.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: This is the recommended governance pattern for balancing agility and production safety in prompt management.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order009-prompt-versioning-repositories-approvals-governance.md
   Evidence span: Develop in isolated branches and enforce approval-controlled promotion to production.

### P1-AIP-D3-112

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-112 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.3: Implement comprehensive prompt management and governance systems to ensure consistency and oversight of FM operations (for example, by using Amazon Bedrock Prompt Management to create parameterized templates and approval workflows, Amazon S3 to store template repositories, AWS CloudTrail to track usage, Amazon CloudWatch Logs to log access). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order009 |
| `accelerated_day` | Day 3 |
| `topic` | Prompt versioning, repositories, approvals, and governance |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Normative; Institutional; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | implement |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order009-local-artifact |
| `raw_source` | 2026-06-30T051603Z-openai-gpt-4.1-day-03-order009.md item 11 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051603Z |
| `raw_run_id` | order009 |

Stem:

While auditing prompt management governance, your team finds several legacy templates with no clear record of their usage or deployment dates. Beyond implementing approvals and logs, what is the most defensible action to address future ambiguity in template deployment history?

Options:

1. Enforce metadata labeling for all templates, including deployment date and usage status.
2. Delete all legacy prompts lacking audit data.
3. Move all templates to a private folder accessible only to platform admins.
4. Disable prompt version control to avoid confusion.

Correct answer: Enforce metadata labeling for all templates, including deployment date and usage status.

Rationale: Comprehensive metadata labeling creates a durable, audit-friendly record for each prompt.

Distractors: Delete all legacy prompts lacking audit data.: This loses potential business knowledge and cannot prevent recurrence.; Move all templates to a private folder accessible only to platform admins.: Limiting access does not restore or track historical data.; Disable prompt version control to avoid confusion.: Disabling versioning further reduces traceability.

Misconception tags: audit-metadata-vs-restriction; deletion-vs-tracking

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order009-prompt-versioning-repositories-approvals-governance.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Adding metadata provides auditability and supports future clarity on prompt deployment.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order009-prompt-versioning-repositories-approvals-governance.md
   Evidence span: Label all templates with deployment status and dates to maintain governance records.

### P1-AIP-D3-113

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-113 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.3: Implement comprehensive prompt management and governance systems to ensure consistency and oversight of FM operations (for example, by using Amazon Bedrock Prompt Management to create parameterized templates and approval workflows, Amazon S3 to store template repositories, AWS CloudTrail to track usage, Amazon CloudWatch Logs to log access). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order009 |
| `accelerated_day` | Day 3 |
| `topic` | Prompt versioning, repositories, approvals, and governance |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Normative; Institutional; Embedded |
| `question_format` | multiple-response |
| `difficulty` | hard |
| `cognitive_demand` | integrate |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order009-local-artifact |
| `raw_source` | 2026-06-30T051603Z-openai-gpt-4.1-day-03-order009.md item 12 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051603Z |
| `raw_run_id` | order009 |

Stem:

A target state for GenAI prompt management requires both multi-environment pipelines and compliance with change management policies. Which architecture components together provide versioning, access control, and end-to-end auditability? (Select THREE.)

Options:

1. Centralized version-controlled prompt repositories (e.g., Amazon S3)
2. Approval workflow systems for promotion to production
3. Integrated event logging (e.g., CloudTrail/CloudWatch)
4. Developer file shares with open edit access
5. Strictly manual code review processes

Correct answer: Centralized version-controlled prompt repositories (e.g., Amazon S3); Approval workflow systems for promotion to production; Integrated event logging (e.g., CloudTrail/CloudWatch)

Rationale: These three together provide governance, audit, and workflow compliance for multi-stage GenAI prompt operations.

Distractors: Developer file shares with open edit access: Open access undermines governance and auditability.; Strictly manual code review processes: Manual review cannot enforce comprehensive traceability or policy compliance alone.

Misconception tags: open-edit-vs-controlled; manual-review-vs-automated-audit

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order009-prompt-versioning-repositories-approvals-governance.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: These controls are directly specified for comprehensive prompt management covering provenance, approval, and audit.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order009-prompt-versioning-repositories-approvals-governance.md
   Evidence span: Central repo, approval workflow, and event/audit logs are required for robust governance.

### P1-AIP-D3-114

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-114 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.3: Implement comprehensive prompt management and governance systems to ensure consistency and oversight of FM operations (for example, by using Amazon Bedrock Prompt Management to create parameterized templates and approval workflows, Amazon S3 to store template repositories, AWS CloudTrail to track usage, Amazon CloudWatch Logs to log access). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order009 |
| `accelerated_day` | Day 3 |
| `topic` | Prompt versioning, repositories, approvals, and governance |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Normative; Institutional; Embedded |
| `question_format` | multiple-response |
| `difficulty` | medium |
| `cognitive_demand` | optimize |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order009-local-artifact |
| `raw_source` | 2026-06-30T051603Z-openai-gpt-4.1-day-03-order009.md item 13 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051603Z |
| `raw_run_id` | order009 |

Stem:

You are optimizing a GenAI prompt repository for controlled template evolution, regulatory compliance, and continuous improvement. Which two practices most directly advance those objectives? (Select TWO.)

Options:

1. Retain all previous prompt template versions with metadata documenting changes and rationale.
2. Implement notifications for team members when production prompts are updated.
3. Allow direct edits to production templates with no approval.
4. Operate without explicit version numbers for templates.
5. Store prompt templates only in developer home directories.

Correct answer: Retain all previous prompt template versions with metadata documenting changes and rationale.; Implement notifications for team members when production prompts are updated.

Rationale: Version retention and update notifications support traceability, continuous improvement, and compliance.

Distractors: Allow direct edits to production templates with no approval.: This undermines controlled evolution and regulatory compliance.; Operate without explicit version numbers for templates.: Lack of versioning breaks traceability.; Store prompt templates only in developer home directories.: Decentralized, isolated storage undermines governance.

Misconception tags: versioning-vs-edit; notifications-vs-rumor

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order009-prompt-versioning-repositories-approvals-governance.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Retaining versions with documented rationale and alerting stakeholders support change tracking and rapid response.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order009-prompt-versioning-repositories-approvals-governance.md
   Evidence span: Retain all prompt versions and implement notification systems for governance and improvement.

### P1-AIP-D3-115

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-115 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.4: Develop quality assurance systems to ensure prompt effectiveness and reliability for FMs (for example, by using Lambda functions to verify expected output, Step Functions to test edge cases, CloudWatch to test prompt regression). |
| `secondary_exam_skills` | Skill 5.1.4: Create systematic quality assurance processes to maintain consistent performance standards for FMs (for example, by using continuous evaluation workflows, regression testing for model outputs, automated quality gates for deployments). |
| `learning_unit` | Day03-order010 |
| `accelerated_day` | Day 3 |
| `topic` | Prompt regression testing and quality assurance |
| `knowledge_category` | Skill; Knowledge |
| `knowledge_type` | Procedural; Causal; Strategic |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | implement |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order010-local-artifact |
| `raw_source` | 2026-06-30T051656Z-openai-gpt-4.1-day-03-order010.md item 1 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051656Z |
| `raw_run_id` | order010 |

Stem:

A GenAI development team notices that recent changes to prompt structures have resulted in inconsistent model responses for a critical business use case. The team wants to ensure future prompt modifications do not introduce unexpected errors before deployment. Which approach best meets the need for systematic prompt regression testing and catch regressions early?

Options:

1. Implement a Lambda-based automated test suite to verify prompt output against expected baselines before deploying prompt changes.
2. Manually review all prompt changes by multiple stakeholders after each update to verify correct responses.
3. Schedule periodic user acceptance testing sessions after every deployment to catch regression issues.
4. Enable CloudWatch alarms for model API latency and error spikes only.

Correct answer: Implement a Lambda-based automated test suite to verify prompt output against expected baselines before deploying prompt changes.

Rationale: Automated, Lambda-based regression testing ensures every prompt variation is validated against expected results prior to deployment, efficiently preventing regressions.

Distractors: Manually review all prompt changes by multiple stakeholders after each update to verify correct responses.: Manual review is slow, error-prone, and unscalable; it is much less effective than automated regression testing at catching subtle issues.; Schedule periodic user acceptance testing sessions after every deployment to catch regression issues.: User acceptance testing may catch some issues, but it is reactive and inefficient for regression catching; it is not systematic or automated.; Enable CloudWatch alarms for model API latency and error spikes only.: Alarms for latency and error spikes do not assess model output content, so they won't catch functional prompt regressions.

Misconception tags: Manual testing suffices; Reliance on non-output metrics

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order010-prompt-regression-testing-quality-assurance.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The artifact directly recommends using automated Lambda tests for regression checking, rather than relying on manual or reactive approaches.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order010-prompt-regression-testing-quality-assurance.md
   Evidence span: Automated Lambda tests can check prompt outputs against baseline expectations before deployment.

### P1-AIP-D3-116

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-116 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.4: Develop quality assurance systems to ensure prompt effectiveness and reliability for FMs (for example, by using Lambda functions to verify expected output, Step Functions to test edge cases, CloudWatch to test prompt regression). |
| `secondary_exam_skills` | Skill 5.1.4: Create systematic quality assurance processes to maintain consistent performance standards for FMs (for example, by using continuous evaluation workflows, regression testing for model outputs, automated quality gates for deployments). |
| `learning_unit` | Day03-order010 |
| `accelerated_day` | Day 3 |
| `topic` | Prompt regression testing and quality assurance |
| `knowledge_category` | Skill; Knowledge |
| `knowledge_type` | Procedural; Causal; Strategic |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | implement |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order010-local-artifact |
| `raw_source` | 2026-06-30T051656Z-openai-gpt-4.1-day-03-order010.md item 2 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051656Z |
| `raw_run_id` | order010 |

Stem:

An organization needs to ensure rapid detection when a prompt modification causes model responses to deviate unexpectedly. They want all model integrations, including obscure API clients, to be covered by their QA process. What should the team put in place to meet these needs?

Options:

1. Deploy a continuous integration (CI) pipeline that triggers regression tests on prompt changes, using test cases for all supported clients.
2. Rely on user feedback and post-deployment bug reports to catch prompt regressions in production.
3. Manually sample model outputs for key prompts on a regular schedule.
4. Enable logging of prompt changes, but do not implement regression tests.

Correct answer: Deploy a continuous integration (CI) pipeline that triggers regression tests on prompt changes, using test cases for all supported clients.

Rationale: A CI pipeline with regression tests ensures prompt modifications are automatically validated across all model integrations before changes are released.

Distractors: Rely on user feedback and post-deployment bug reports to catch prompt regressions in production.: This approach is reactive and risky, allowing prompt regressions to impact users before they're detected.; Manually sample model outputs for key prompts on a regular schedule.: Manual sampling is insufficient to catch all regressions, especially on less-used API clients.; Enable logging of prompt changes, but do not implement regression tests.: Logging is useful for audit, but it does nothing to prevent regressions from going live.

Misconception tags: Reliance on post-deployment reports; Manual spot-checking is enough

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order010-prompt-regression-testing-quality-assurance.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The artifact promotes CI-triggered regression tests for prompt QA, covering all supported interfaces.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order010-prompt-regression-testing-quality-assurance.md
   Evidence span: Continuous integration workflows should trigger regression tests to validate prompt changes before deployment.

### P1-AIP-D3-117

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-117 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.4: Develop quality assurance systems to ensure prompt effectiveness and reliability for FMs (for example, by using Lambda functions to verify expected output, Step Functions to test edge cases, CloudWatch to test prompt regression). |
| `secondary_exam_skills` | Skill 5.1.4: Create systematic quality assurance processes to maintain consistent performance standards for FMs (for example, by using continuous evaluation workflows, regression testing for model outputs, automated quality gates for deployments). |
| `learning_unit` | Day03-order010 |
| `accelerated_day` | Day 3 |
| `topic` | Prompt regression testing and quality assurance |
| `knowledge_category` | Skill; Knowledge |
| `knowledge_type` | Procedural; Causal; Strategic |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order010-local-artifact |
| `raw_source` | 2026-06-30T051656Z-openai-gpt-4.1-day-03-order010.md item 4 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051656Z |
| `raw_run_id` | order010 |

Stem:

A team notices that prompt changes occasionally break rare edge case queries that are not covered by basic test cases. How should the quality assurance system be improved to guard against regressions for these cases?

Options:

1. Expand regression test coverage to include edge case prompts and use Step Functions for orchestrating scenario-based test workflows.
2. Focus only on the most common user queries to improve QA test efficiency.
3. Increase the number of manual reviews for each prompt change.
4. Rely on CloudWatch error metrics as the primary detection signal for regressions.

Correct answer: Expand regression test coverage to include edge case prompts and use Step Functions for orchestrating scenario-based test workflows.

Rationale: Testing edge cases and orchestrating scenario-based workflows ensures comprehensive regression coverage as supported in the artifact.

Distractors: Focus only on the most common user queries to improve QA test efficiency.: Limiting testing to only common queries won't catch edge case failures.; Increase the number of manual reviews for each prompt change.: Manual reviews are not scalable or reliable for covering edge cases.; Rely on CloudWatch error metrics as the primary detection signal for regressions.: CloudWatch error metrics do not proactively test prompt output quality.

Misconception tags: Ignoring edge cases; Manual review sufficiency

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order010-prompt-regression-testing-quality-assurance.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Expanding tests and using Step Functions for edge cases is called out in the source for thorough regression QA.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order010-prompt-regression-testing-quality-assurance.md
   Evidence span: Use Step Functions to test edge cases and orchestrate workflow-based prompt tests.

### P1-AIP-D3-118

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-118 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.4: Develop quality assurance systems to ensure prompt effectiveness and reliability for FMs (for example, by using Lambda functions to verify expected output, Step Functions to test edge cases, CloudWatch to test prompt regression). |
| `secondary_exam_skills` | Skill 5.1.4: Create systematic quality assurance processes to maintain consistent performance standards for FMs (for example, by using continuous evaluation workflows, regression testing for model outputs, automated quality gates for deployments). |
| `learning_unit` | Day03-order010 |
| `accelerated_day` | Day 3 |
| `topic` | Prompt regression testing and quality assurance |
| `knowledge_category` | Skill; Knowledge |
| `knowledge_type` | Procedural; Causal; Strategic |
| `question_format` | multiple-response |
| `difficulty` | medium |
| `cognitive_demand` | implement |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order010-local-artifact |
| `raw_source` | 2026-06-30T051656Z-openai-gpt-4.1-day-03-order010.md item 5 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051656Z |
| `raw_run_id` | order010 |

Stem:

When implementing prompt regression testing for a critical GenAI-powered insurance assistant, which practices improve both reliability and prompt effectiveness? (Select TWO.)

Options:

1. Define a baseline set of expected outputs for key prompts and automate the comparison.
2. Trigger regression tests only after customer complaints are received.
3. Integrate regression tests into the deployment pipeline before production updates.
4. Log only the prompt inputs to audit changes.
5. Outsource all prompt reviews to a third-party annotation vendor.

Correct answer: Define a baseline set of expected outputs for key prompts and automate the comparison.; Integrate regression tests into the deployment pipeline before production updates.

Rationale: These practices ensure that prompt changes are checked for effectiveness and reliability prior to deployment, as well as measured against known expectations.

Distractors: Trigger regression tests only after customer complaints are received.: This approach is reactive and can cause failures to reach production.; Log only the prompt inputs to audit changes.: Logging aids audit but doesn't guarantee effectiveness or reliability.; Outsource all prompt reviews to a third-party annotation vendor.: Outsourcing does not ensure systematic, automated QA that can block regressions.

Misconception tags: Audit vs. proactive QA; Reactive only testing

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order010-prompt-regression-testing-quality-assurance.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The source clearly calls for expected-output baselines and pipeline-integrated regression checks.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order010-prompt-regression-testing-quality-assurance.md
   Evidence span: Baseline definition and CI/CD-integrated regression tests are best practices for reliability and effectiveness.

### P1-AIP-D3-119

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-119 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.4: Develop quality assurance systems to ensure prompt effectiveness and reliability for FMs (for example, by using Lambda functions to verify expected output, Step Functions to test edge cases, CloudWatch to test prompt regression). |
| `secondary_exam_skills` | Skill 5.1.4: Create systematic quality assurance processes to maintain consistent performance standards for FMs (for example, by using continuous evaluation workflows, regression testing for model outputs, automated quality gates for deployments). |
| `learning_unit` | Day03-order010 |
| `accelerated_day` | Day 3 |
| `topic` | Prompt regression testing and quality assurance |
| `knowledge_category` | Skill; Knowledge |
| `knowledge_type` | Procedural; Causal; Strategic |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order010-local-artifact |
| `raw_source` | 2026-06-30T051656Z-openai-gpt-4.1-day-03-order010.md item 6 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051656Z |
| `raw_run_id` | order010 |

Stem:

A GenAI project’s model accuracy dropped after a new prompt template was deployed. The regression test suite had passed. Investigation shows the test suite only uses static, high-frequency prompt cases. What could best address this blind spot?

Options:

1. Expand regression test cases to cover edge scenarios and rare usage patterns.
2. Increase the number of static prompt test cases for high-frequency inputs.
3. Switch to entirely manual prompt validation before deployment.
4. Reduce the frequency of deployments to decrease the chance of regressions.

Correct answer: Expand regression test cases to cover edge scenarios and rare usage patterns.

Rationale: Edge cases and rare queries often reveal regressions missed by only validating frequent query types.

Distractors: Increase the number of static prompt test cases for high-frequency inputs.: This does not address blind spots for rare or edge queries.; Switch to entirely manual prompt validation before deployment.: Manual review is not scalable or reliable for comprehensive QA.; Reduce the frequency of deployments to decrease the chance of regressions.: This delays feature delivery but does not mitigate coverage gaps.

Misconception tags: Focusing only on common usage; Overreliance on manual QA

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order010-prompt-regression-testing-quality-assurance.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The artifact states regression QA must include edge and rare cases to avoid blind spots.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order010-prompt-regression-testing-quality-assurance.md
   Evidence span: Include edge scenarios in regression QA for full coverage.

### P1-AIP-D3-120

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-120 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.4: Develop quality assurance systems to ensure prompt effectiveness and reliability for FMs (for example, by using Lambda functions to verify expected output, Step Functions to test edge cases, CloudWatch to test prompt regression). |
| `secondary_exam_skills` | Skill 5.1.4: Create systematic quality assurance processes to maintain consistent performance standards for FMs (for example, by using continuous evaluation workflows, regression testing for model outputs, automated quality gates for deployments). |
| `learning_unit` | Day03-order010 |
| `accelerated_day` | Day 3 |
| `topic` | Prompt regression testing and quality assurance |
| `knowledge_category` | Skill; Knowledge |
| `knowledge_type` | Procedural; Causal; Strategic |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order010-local-artifact |
| `raw_source` | 2026-06-30T051656Z-openai-gpt-4.1-day-03-order010.md item 7 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051656Z |
| `raw_run_id` | order010 |

Stem:

You are architecting a QA process for prompts used by a multi-national customer support bot. What is the primary advantage of integrating automated prompt regression testing into the continuous deployment pipeline?

Options:

1. It detects prompt output regressions before they reach users, enabling faster remediation.
2. It allows direct, manual review by every regional stakeholder before releases.
3. It reduces the need for error logging and monitoring after deployment.
4. It makes the deployment pipeline immune to errors caused by underlying model updates.

Correct answer: It detects prompt output regressions before they reach users, enabling faster remediation.

Rationale: Automated regression QA in the pipeline catches output problems prior to deployments, reducing user impact and enabling quick fixes.

Distractors: It allows direct, manual review by every regional stakeholder before releases.: Manual review is not automated QA and does not scale; automated regression is the advantage.; It reduces the need for error logging and monitoring after deployment.: Monitoring remains important regardless of regression QA.; It makes the deployment pipeline immune to errors caused by underlying model updates.: Regression QA doesn't guarantee immunity to all model-level changes.

Misconception tags: Manual review is central; QA eliminates monitoring needs

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order010-prompt-regression-testing-quality-assurance.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Prompt regression testing as part of CI/CD provides pre-deployment protection and speeds remediation, per the artifact.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order010-prompt-regression-testing-quality-assurance.md
   Evidence span: Regression testing in pipelines prevents new prompt bugs from reaching production.

### P1-AIP-D3-121

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-121 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.4: Develop quality assurance systems to ensure prompt effectiveness and reliability for FMs (for example, by using Lambda functions to verify expected output, Step Functions to test edge cases, CloudWatch to test prompt regression). |
| `secondary_exam_skills` | Skill 5.1.4: Create systematic quality assurance processes to maintain consistent performance standards for FMs (for example, by using continuous evaluation workflows, regression testing for model outputs, automated quality gates for deployments). |
| `learning_unit` | Day03-order010 |
| `accelerated_day` | Day 3 |
| `topic` | Prompt regression testing and quality assurance |
| `knowledge_category` | Skill; Knowledge |
| `knowledge_type` | Procedural; Causal; Strategic |
| `question_format` | multiple-response |
| `difficulty` | hard |
| `cognitive_demand` | optimize |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order010-local-artifact |
| `raw_source` | 2026-06-30T051656Z-openai-gpt-4.1-day-03-order010.md item 9 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051656Z |
| `raw_run_id` | order010 |

Stem:

A prompt QA team struggles with long-term drift in prompt output quality due to periodic model updates by a third-party FM provider. What techniques should the team employ to systematically detect when model drift causes output regressions? (Select TWO.)

Options:

1. Maintain a rolling baseline of expected prompt outputs and alert when significant deviations are detected.
2. Run scheduled regression tests that execute against the current production model version.
3. Allow model providers to submit change logs and update test cases only based on those change logs.
4. Monitor only API response times and error rates.
5. Restrict regression tests to initial model deployment, skipping subsequent updates.

Correct answer: Maintain a rolling baseline of expected prompt outputs and alert when significant deviations are detected.; Run scheduled regression tests that execute against the current production model version.

Rationale: Ongoing baselines and scheduled live-model regression tests are the only systematic ways to catch drift-induced regressions.

Distractors: Allow model providers to submit change logs and update test cases only based on those change logs.: Provider change logs may not capture regressions affecting prompts; test should be empirical.; Monitor only API response times and error rates.: Output regressions are not revealed by response times or errors alone.; Restrict regression tests to initial model deployment, skipping subsequent updates.: Skipping post-deployment regression tests allows unnoticed drift.

Misconception tags: Error vs output metrics; Single deployment sufficiency

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order010-prompt-regression-testing-quality-assurance.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Scheduled regression and rolling baseline comparison provides systematic detection as described in the artifact.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order010-prompt-regression-testing-quality-assurance.md
   Evidence span: Regression tests and rolling baseline detection catch model drift and output changes.

### P1-AIP-D3-122

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-122 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.6: Design complex prompt systems to handle sophisticated tasks with FMs (for example, by using Amazon Bedrock Prompt Flows for sequential prompt chains, conditional branching based on model responses, reusable prompt components, integrated pre-processing and post-processing steps). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order011 |
| `accelerated_day` | Day 3 |
| `topic` | Prompt chaining, branching, and Bedrock Prompt Flows |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Conceptual; Procedural; Strategic; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | bedrock-prompt-flows-branching |
| `raw_source` | 2026-06-30T051742Z-openai-gpt-4.1-day-03-order011.md item 1 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051742Z |
| `raw_run_id` | order011 |

Stem:

A team builds a legal document review agent using Amazon Bedrock Prompt Flows. The system needs to answer initial user queries, then—if a risk factor is detected in the response—branch to a subflow that requests additional user confirmation. Which Bedrock Prompt Flows feature most directly enables this multi-path behavior?

Options:

1. Configuring a conditional branching node based on model output
2. Creating a feedback loop using output format specifications
3. Using only single-step chains with embedded prompts
4. Chaining multiple models in parallel and merging their responses

Correct answer: Configuring a conditional branching node based on model output

Rationale: Conditional branching nodes enable the prompt flow to execute different paths depending on outcomes from model responses, supporting use cases like confirmation dialogs when certain criteria are detected.

Distractors: Creating a feedback loop using output format specifications: Feedback loops support iterative refinement, not explicit branching to a subflow based on a condition in the response.; Using only single-step chains with embedded prompts: Single-step chains do not allow multi-path flows, which are required for responsive behaviors based on detected risks.; Chaining multiple models in parallel and merging their responses: Parallel model execution merges outputs but does not implement scenario-based branching; dynamic control is needed.

Misconception tags: Assuming sequential chaining is adequate for all dynamic prompt logic

Source trace:

https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-flows-branching.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The source documents that conditional branching nodes drive path selection based on model response outcomes, making them necessary for multi-path prompt logic when conditions are detected.
   Source: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-flows-branching.html
   Evidence span: Conditional branches in prompt flows allow your automation to continue along different paths depending on the results of a previous step.

### P1-AIP-D3-123

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-123 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.6: Design complex prompt systems to handle sophisticated tasks with FMs (for example, by using Amazon Bedrock Prompt Flows for sequential prompt chains, conditional branching based on model responses, reusable prompt components, integrated pre-processing and post-processing steps). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order011 |
| `accelerated_day` | Day 3 |
| `topic` | Prompt chaining, branching, and Bedrock Prompt Flows |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Conceptual; Procedural; Strategic; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | design |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | bedrock-prompt-flows-branching |
| `raw_source` | 2026-06-30T051742Z-openai-gpt-4.1-day-03-order011.md item 2 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051742Z |
| `raw_run_id` | order011 |

Stem:

You are tasked with designing a prompt flow for a customer support AI that starts with a classification prompt, then either routes to a retrieval step or escalates to a human if the confidence score is below a threshold. What approach should you adopt in Bedrock Prompt Flows to handle this scenario?

Options:

1. Implement a branching node that evaluates the model’s confidence score
2. Implement an unconditional prompt chaining sequence of three steps
3. Add a feedback loop for the end-user at every step regardless of confidence
4. Combine all possible responses into a single prompt for the FM

Correct answer: Implement a branching node that evaluates the model’s confidence score

Rationale: Branching nodes can evaluate the model output and route to different steps, allowing escalation or alternate actions if a confidence threshold is met or missed.

Distractors: Implement an unconditional prompt chaining sequence of three steps: Unconditional chains cannot perform routing decisions based on model output such as confidence scores.; Add a feedback loop for the end-user at every step regardless of confidence: Constant feedback at every step increases complexity and may frustrate users without addressing the need for conditional routing.; Combine all possible responses into a single prompt for the FM: Combining all responses makes logic unwieldy and bypasses the advantage of structured control in prompt flows.

Misconception tags: Confusing unconditional chaining with decision-based branching

Source trace:

https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-flows-branching.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The source describes branching logic based on model outputs, such as confidence, which matches the need to escalate or reroute in the described scenario.
   Source: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-flows-branching.html
   Evidence span: You can add branching logic based on result variables, such as a model's confidence score.

### P1-AIP-D3-124

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-124 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.6: Design complex prompt systems to handle sophisticated tasks with FMs (for example, by using Amazon Bedrock Prompt Flows for sequential prompt chains, conditional branching based on model responses, reusable prompt components, integrated pre-processing and post-processing steps). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order011 |
| `accelerated_day` | Day 3 |
| `topic` | Prompt chaining, branching, and Bedrock Prompt Flows |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Conceptual; Procedural; Strategic; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | bedrock-prompt-flows-components |
| `raw_source` | 2026-06-30T051742Z-openai-gpt-4.1-day-03-order011.md item 3 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051742Z |
| `raw_run_id` | order011 |

Stem:

You need to set up an Amazon Bedrock Prompt Flow that allows dynamic preprocessing of input data, ensures multi-step reasoning, and includes a reusable evaluation component. Which design correctly applies Prompt Flow features?

Options:

1. Use pre-processing and post-processing steps with reusable component nodes connected to the main prompt chain
2. Build a single prompt template that accepts all raw user input and output in one step
3. Configure branching logic exclusively for output format enforcement
4. Deploy multiple Prompt Flows, each with its own preprocessing script and isolated evaluation stage

Correct answer: Use pre-processing and post-processing steps with reusable component nodes connected to the main prompt chain

Rationale: Preprocessing and post-processing components can be integrated as nodes in a prompt flow, promoting code reuse and modularity for complex logic.

Distractors: Build a single prompt template that accepts all raw user input and output in one step: This approach eliminates the benefits of modularity, reuse, and multi-step logic, reducing flexibility.; Configure branching logic exclusively for output format enforcement: Branching logic is used for conditional path selection rather than solely output formatting.; Deploy multiple Prompt Flows, each with its own preprocessing script and isolated evaluation stage: This increases duplication and overhead, rather than leveraging reusable components for shared flow logic.

Misconception tags: Assuming monolithic prompts are optimal for all use cases

Source trace:

https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-flows-components.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Using reusable component nodes for pre/post-processing aligns with the Prompt Flows design pattern for modular, multi-step, and maintainable pipelines.
   Source: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-flows-components.html
   Evidence span: Reusable components can modularize logic, such as pre-processing or evaluation, and are connected as nodes in the flow.

### P1-AIP-D3-125

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-125 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.6: Design complex prompt systems to handle sophisticated tasks with FMs (for example, by using Amazon Bedrock Prompt Flows for sequential prompt chains, conditional branching based on model responses, reusable prompt components, integrated pre-processing and post-processing steps). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order011 |
| `accelerated_day` | Day 3 |
| `topic` | Prompt chaining, branching, and Bedrock Prompt Flows |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Conceptual; Procedural; Strategic; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | design |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | bedrock-prompt-flows-branching |
| `raw_source` | 2026-06-30T051742Z-openai-gpt-4.1-day-03-order011.md item 4 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051742Z |
| `raw_run_id` | order011 |

Stem:

A Bedrock Prompt Flow must switch between three different summarization strategies based on user input complexity, and later merge their outputs for a unified response. What is the correct architecture pattern for this requirement?

Options:

1. Use branching nodes for strategy selection and a merging node to consolidate outputs
2. Sequence the summarization strategies without branching, then select the best summary in the final prompt
3. Create parallel prompt chains and discard two of the responses
4. Implement a single summarization strategy for all inputs

Correct answer: Use branching nodes for strategy selection and a merging node to consolidate outputs

Rationale: Branching nodes selectively route input to the right summarization strategy, and a merge node unifies the outputs before presenting the response.

Distractors: Sequence the summarization strategies without branching, then select the best summary in the final prompt: Sequential processing of all strategies is inefficient and discards the benefit of conditional routing.; Create parallel prompt chains and discard two of the responses: Running all strategies in parallel wastes compute and does not use merge logic properly.; Implement a single summarization strategy for all inputs: This disregards the scenario's explicit need to select and merge between multiple strategies.

Misconception tags: Misapplying parallelism or linear chains in place of branching and merging

Source trace:

https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-flows-branching.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Branch and merge nodes are the supported method in Prompt Flows for conditionally choosing between strategies then unifying responses.
   Source: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-flows-branching.html
   Evidence span: Branching and merging nodes allow you to control flow based on logic, then combine results.

### P1-AIP-D3-126

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-126 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.6: Design complex prompt systems to handle sophisticated tasks with FMs (for example, by using Amazon Bedrock Prompt Flows for sequential prompt chains, conditional branching based on model responses, reusable prompt components, integrated pre-processing and post-processing steps). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order011 |
| `accelerated_day` | Day 3 |
| `topic` | Prompt chaining, branching, and Bedrock Prompt Flows |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Conceptual; Procedural; Strategic; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | design |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | bedrock-prompt-flows-branching |
| `raw_source` | 2026-06-30T051742Z-openai-gpt-4.1-day-03-order011.md item 5 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051742Z |
| `raw_run_id` | order011 |

Stem:

A generative AI application built on Bedrock Prompt Flows begins with a data validation node, then conditionally processes either structured data or free text through different downstream chains. What aspect of Prompt Flows enables this targeted path execution?

Options:

1. Conditional branching driven by evaluation of the input type
2. Mandatory sequential execution of all processing nodes
3. Single-path chaining regardless of input content
4. Prompt templates that embed both data pipelines inline

Correct answer: Conditional branching driven by evaluation of the input type

Rationale: Conditional branching nodes can direct flow to different paths depending on evaluated input, such as distinguishing between structured and unstructured content.

Distractors: Mandatory sequential execution of all processing nodes: Executing all nodes regardless of need is inefficient and does not allow targeted processing.; Single-path chaining regardless of input content: A single path ignores the requirement to handle different data types distinctly.; Prompt templates that embed both data pipelines inline: Embedding pipelines inline increases complexity and impedes separation of concerns, instead of leveraging the flow’s routing features.

Misconception tags: Believing prompt flows must process data in fixed sequences

Source trace:

https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-flows-branching.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Conditional branching provides differentiated processing based on evaluated conditions such as input data type.
   Source: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-flows-branching.html
   Evidence span: Conditional branches allow flows to process input differently depending on validation outcomes.

### P1-AIP-D3-127

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-127 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.6: Design complex prompt systems to handle sophisticated tasks with FMs (for example, by using Amazon Bedrock Prompt Flows for sequential prompt chains, conditional branching based on model responses, reusable prompt components, integrated pre-processing and post-processing steps). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order011 |
| `accelerated_day` | Day 3 |
| `topic` | Prompt chaining, branching, and Bedrock Prompt Flows |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Conceptual; Procedural; Strategic; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | design |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | bedrock-prompt-flows-branching |
| `raw_source` | 2026-06-30T051742Z-openai-gpt-4.1-day-03-order011.md item 6 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051742Z |
| `raw_run_id` | order011 |

Stem:

A retail chatbot requires two steps: first, a product search; second, a follow-up reasoning prompt that adapts based on product type. How should a Bedrock Prompt Flow implement this adaptive follow-up based on the model output's product type?

Options:

1. Add a branching component that examines the product type and routes to specific sub-prompts
2. Use a single prompt that incorporates all possible follow-up instructions using if-else logic in prompt text
3. Execute both follow-up reasoning prompts in parallel and merge their outputs
4. Modify the product search prompt to attempt follow-up reasoning inline

Correct answer: Add a branching component that examines the product type and routes to specific sub-prompts

Rationale: A branching node allows downstream prompts to adapt based on prior model output, supporting distinct follow-ups for different product types.

Distractors: Use a single prompt that incorporates all possible follow-up instructions using if-else logic in prompt text: This increases prompt complexity and is not as maintainable as routing at the flow level.; Execute both follow-up reasoning prompts in parallel and merge their outputs: This unnecessarily spends compute and doesn't allow adaptive, type-specific processing.; Modify the product search prompt to attempt follow-up reasoning inline: Combining unrelated steps reduces separation of concerns and flexibility.

Misconception tags: Embedding all logic in a single prompt instead of flow control

Source trace:

https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-flows-branching.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Branching nodes support separated sub-prompts by examining model-generated attributes.
   Source: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-flows-branching.html
   Evidence span: Branching components allow the flow to separate execution paths based on model output such as extracted types.

### P1-AIP-D3-128

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-128 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.6: Design complex prompt systems to handle sophisticated tasks with FMs (for example, by using Amazon Bedrock Prompt Flows for sequential prompt chains, conditional branching based on model responses, reusable prompt components, integrated pre-processing and post-processing steps). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order011 |
| `accelerated_day` | Day 3 |
| `topic` | Prompt chaining, branching, and Bedrock Prompt Flows |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Conceptual; Procedural; Strategic; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | bedrock-prompt-flows |
| `raw_source` | 2026-06-30T051742Z-openai-gpt-4.1-day-03-order011.md item 7 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051742Z |
| `raw_run_id` | order011 |

Stem:

You run a Bedrock Prompt Flow with four chained nodes: two model prompts, an evaluation step, and a summarization node. During runs, only partial outputs are appearing from the summarization node. Which flow design issue is the most likely cause?

Options:

1. The flow fails to properly pass outputs between nodes, breaking the chain
2. A missing branching node that should route to alternative summarizers
3. All steps are running in required sequence, so there is no issue
4. Summarization must always immediately follow input, not other prompts

Correct answer: The flow fails to properly pass outputs between nodes, breaking the chain

Rationale: Broken or misconfigured flow connections prevent downstream nodes from receiving necessary intermediate outputs for summarization.

Distractors: A missing branching node that should route to alternative summarizers: Branching is only needed for conditional logic, not in a straightforward chain.; All steps are running in required sequence, so there is no issue: Partial output is a sign of improper flow design, regardless of correct sequence.; Summarization must always immediately follow input, not other prompts: Summarization can validly follow intermediate transforms or evaluations.

Misconception tags: Mistaking correct step ordering for correct data wiring

Source trace:

https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-flows.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Misconfigured wiring interrupts the flow, preventing summarization from accessing required prior results as documented.
   Source: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-flows.html
   Evidence span: Proper flow chaining requires outputs to be wired as inputs for downstream nodes.

### P1-AIP-D3-129

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-129 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.6: Design complex prompt systems to handle sophisticated tasks with FMs (for example, by using Amazon Bedrock Prompt Flows for sequential prompt chains, conditional branching based on model responses, reusable prompt components, integrated pre-processing and post-processing steps). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order011 |
| `accelerated_day` | Day 3 |
| `topic` | Prompt chaining, branching, and Bedrock Prompt Flows |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Conceptual; Procedural; Strategic; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | implement |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | bedrock-prompt-flows-components |
| `raw_source` | 2026-06-30T051742Z-openai-gpt-4.1-day-03-order011.md item 8 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051742Z |
| `raw_run_id` | order011 |

Stem:

A team needs beginner developers to rapidly author reusable language evaluation steps that can be incorporated across multiple Prompt Flows. Which approach best leverages Bedrock Prompt Flow’s strengths for this requirement?

Options:

1. Develop custom reusable components for evaluation logic and share them across flows
2. Duplicate the evaluation step by manually copying the node into every flow
3. Define the evaluation logic inside each unique main prompt template
4. Request all evaluation from the model directly without structuring it in the flow

Correct answer: Develop custom reusable components for evaluation logic and share them across flows

Rationale: Custom components encapsulate logic in a reusable way, promoting consistency and maintainability across flows.

Distractors: Duplicate the evaluation step by manually copying the node into every flow: Manual duplication creates overhead and maintenance risk.; Define the evaluation logic inside each unique main prompt template: Embedding logic in each template reduces reusability and central management.; Request all evaluation from the model directly without structuring it in the flow: This removes control and transparency from the flow design.

Misconception tags: Believing code or node duplication is the only way to reuse logic

Source trace:

https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-flows-components.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Custom components bring reusability and encapsulation per the source, aligning to reusing evaluation logic between flows.
   Source: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-flows-components.html
   Evidence span: Reusable components can be integrated as nodes in prompt flows to modularize evaluation logic.

### P1-AIP-D3-130

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-130 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.6: Design complex prompt systems to handle sophisticated tasks with FMs (for example, by using Amazon Bedrock Prompt Flows for sequential prompt chains, conditional branching based on model responses, reusable prompt components, integrated pre-processing and post-processing steps). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order011 |
| `accelerated_day` | Day 3 |
| `topic` | Prompt chaining, branching, and Bedrock Prompt Flows |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Conceptual; Procedural; Strategic; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | compare |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | bedrock-prompt-flows |
| `raw_source` | 2026-06-30T051742Z-openai-gpt-4.1-day-03-order011.md item 9 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051742Z |
| `raw_run_id` | order011 |

Stem:

A workflow requires chaining multiple LLM prompts with data transformation and business rules enforced between each step. What is the main advantage of using Bedrock Prompt Flows over embedding all sub-logic in a single monolithic prompt?

Options:

1. It enables granular visibility, error handling, and modular updates of each business rule and transformation step
2. It reduces total latency by always executing all sub-steps in parallel
3. It avoids the need for separate evaluation steps by relying on LLM output consistency
4. It creates a single, unstructured pipeline so prompt complexity is minimized

Correct answer: It enables granular visibility, error handling, and modular updates of each business rule and transformation step

Rationale: Bedrock Prompt Flows modularize logic, making review, debugging, and updates more manageable and transparent.

Distractors: It reduces total latency by always executing all sub-steps in parallel: Flows do not necessarily parallelize all sub-steps, as chaining is typically sequential.; It avoids the need for separate evaluation steps by relying on LLM output consistency: Dedicated evaluation nodes improve reliability and monitoring.; It creates a single, unstructured pipeline so prompt complexity is minimized: Unstructured pipelines remove the key benefits of flow modularity.

Misconception tags: Overestimating the simplicity gained by collapsing all logic into a single prompt

Source trace:

https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-flows.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The documentation states Prompt Flows modularize pipeline logic for visibility, error handling, and maintainability.
   Source: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-flows.html
   Evidence span: Prompt Flows break down pipelines into modular, reviewable nodes with clear visibility at each step.

### P1-AIP-D3-131

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-131 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.6: Design complex prompt systems to handle sophisticated tasks with FMs (for example, by using Amazon Bedrock Prompt Flows for sequential prompt chains, conditional branching based on model responses, reusable prompt components, integrated pre-processing and post-processing steps). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order011 |
| `accelerated_day` | Day 3 |
| `topic` | Prompt chaining, branching, and Bedrock Prompt Flows |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Conceptual; Procedural; Strategic; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | bedrock-prompt-flows-components |
| `raw_source` | 2026-06-30T051742Z-openai-gpt-4.1-day-03-order011.md item 10 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051742Z |
| `raw_run_id` | order011 |

Stem:

In a complex prompt pipeline implemented with Bedrock Prompt Flows, you need to invoke an external API after obtaining an intermediate model result and pass its output back to the next prompt node. Which technique supports this requirement?

Options:

1. Insert a function component node between the two prompt nodes to call the external API
2. Replace the downstream prompt with an integrated API fetch prompt
3. Run the API call separately outside of Prompt Flows and manually inject results
4. Attach multiple outputs from the first prompt node directly to all following nodes

Correct answer: Insert a function component node between the two prompt nodes to call the external API

Rationale: Function component nodes can call external APIs and then return their results to downstream prompt nodes in the flow.

Distractors: Replace the downstream prompt with an integrated API fetch prompt: This replaces the flexibility of flow automation and is not modular.; Run the API call separately outside of Prompt Flows and manually inject results: This approach defeats the purpose of a managed flow and increases overhead.; Attach multiple outputs from the first prompt node directly to all following nodes: Attaching outputs does not perform external API calls or data enrichment.

Misconception tags: Assuming outside workflow injection is necessary for non-LLM operations

Source trace:

https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-flows-components.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Function nodes support API calls and integration within prompt flows as described by the documentation.
   Source: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-flows-components.html
   Evidence span: Components can encapsulate function steps, such as API calls, and chain results to downstream nodes.

### P1-AIP-D3-132

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-132 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.6: Design complex prompt systems to handle sophisticated tasks with FMs (for example, by using Amazon Bedrock Prompt Flows for sequential prompt chains, conditional branching based on model responses, reusable prompt components, integrated pre-processing and post-processing steps). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order011 |
| `accelerated_day` | Day 3 |
| `topic` | Prompt chaining, branching, and Bedrock Prompt Flows |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Conceptual; Procedural; Strategic; Embedded |
| `question_format` | multiple-response |
| `difficulty` | hard |
| `cognitive_demand` | implement |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | bedrock-prompt-flows-branching |
| `raw_source` | 2026-06-30T051742Z-openai-gpt-4.1-day-03-order011.md item 11 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051742Z |
| `raw_run_id` | order011 |

Stem:

Select ALL valid applications of branching in Amazon Bedrock Prompt Flows for professional RAG implementations. (Choose TWO.)

Options:

1. Routing based on detected answer ambiguity in model output
2. Dynamically switching between vector search and keyword search logic
3. Merging outputs from parallel nodes before final output
4. Automatically retrying failed prompt executions without error handling
5. Selecting subflows based on user intent classified by a prior prompt

Correct answer: Routing based on detected answer ambiguity in model output; Selecting subflows based on user intent classified by a prior prompt

Rationale: Branching supports conditional routing based on model output (like ambiguity) and the results of intent classification, enabling dynamic selection of subflows.

Distractors: Dynamically switching between vector search and keyword search logic: While theoretically possible, switching between retrieval strategies is usually handled outside the prompt flow, not within branching nodes.; Merging outputs from parallel nodes before final output: Merging is a separate node type, different from branching logic.; Automatically retrying failed prompt executions without error handling: Retries require explicit error handling, not pure branching nodes.

Misconception tags: Confusing merging, retry logic, and dynamic orchestration with branching capability

Source trace:

https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-flows-branching.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Branching nodes support conditional path selection based on ambiguity in output or intent classification.
   Source: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-flows-branching.html
   Evidence span: Branching enables dynamic routing based on result variables such as ambiguity or intent.

### P1-AIP-D3-133

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-133 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.6: Design complex prompt systems to handle sophisticated tasks with FMs (for example, by using Amazon Bedrock Prompt Flows for sequential prompt chains, conditional branching based on model responses, reusable prompt components, integrated pre-processing and post-processing steps). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order011 |
| `accelerated_day` | Day 3 |
| `topic` | Prompt chaining, branching, and Bedrock Prompt Flows |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Conceptual; Procedural; Strategic; Embedded |
| `question_format` | multiple-response |
| `difficulty` | hard |
| `cognitive_demand` | implement |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | bedrock-prompt-flows-branching |
| `raw_source` | 2026-06-30T051742Z-openai-gpt-4.1-day-03-order011.md item 12 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051742Z |
| `raw_run_id` | order011 |

Stem:

A Bedrock Prompt Flow handles: 1) data processing, 2) classification by an LLM, and 3) invoking a different summarizer depending on the classification result. Which of the following are BEST practices for this branching scenario? (Choose TWO.)

Options:

1. Use a branching node after the classification step to select the appropriate summarizer
2. Create separate prompt flows for each possible classification result
3. Embed conditional summarizer logic directly inside the classification prompt template
4. Wire all summarizers to receive data regardless of classification outcome
5. Clearly define output variables from the classification node for branch decisions

Correct answer: Use a branching node after the classification step to select the appropriate summarizer; Clearly define output variables from the classification node for branch decisions

Rationale: Branching nodes after classification ensure only the appropriate summarizer is triggered. Defining clear output variables supports clean, maintainable routing logic.

Distractors: Create separate prompt flows for each possible classification result: This causes duplication and maintenance risk; branching within a single flow is more efficient.; Embed conditional summarizer logic directly inside the classification prompt template: Separating logic across nodes is better than embedding control logic inside prompt templates.; Wire all summarizers to receive data regardless of classification outcome: Processing all summarizers on every run is inefficient and unnecessary.

Misconception tags: Believing all logic must be either duplicated or embedded in templates

Source trace:

https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-flows-branching.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Proper branching and variable definition make the flow maintainable and efficient as described.
   Source: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-flows-branching.html
   Evidence span: Use branching logic and output variables to control execution paths following a classification step.

### P1-AIP-D3-134

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-134 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.6: Design complex prompt systems to handle sophisticated tasks with FMs (for example, by using Amazon Bedrock Prompt Flows for sequential prompt chains, conditional branching based on model responses, reusable prompt components, integrated pre-processing and post-processing steps). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order011 |
| `accelerated_day` | Day 3 |
| `topic` | Prompt chaining, branching, and Bedrock Prompt Flows |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Conceptual; Procedural; Strategic; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | bedrock-prompt-flows |
| `raw_source` | 2026-06-30T051742Z-openai-gpt-4.1-day-03-order011.md item 13 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051742Z |
| `raw_run_id` | order011 |

Stem:

Your Prompt Flow contains a pre-processing node, a language model node, and a post-processing node. You observe that the post-processing step sometimes receives null data. What is the most likely cause in the flow configuration?

Options:

1. The output variable from the language model node is not properly mapped to the post-processing node
2. Post-processing is only permitted after a branching node
3. Pre-processing overwrites all downstream variables by default
4. The flow is invalid without a merge node

Correct answer: The output variable from the language model node is not properly mapped to the post-processing node

Rationale: Improper mapping or missing connection between nodes can cause post-processing to receive no data.

Distractors: Post-processing is only permitted after a branching node: Post-processing can follow any node, not just branching nodes.; Pre-processing overwrites all downstream variables by default: Pre-processing does not overwrite unless specifically configured to do so.; The flow is invalid without a merge node: Merge nodes are only required for flows that converge multiple branches.

Misconception tags: Assuming flow infrastructure enforces correct wiring automatically

Source trace:

https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-flows.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Lack of output mapping is a documented cause of null inputs for downstream flow nodes.
   Source: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-flows.html
   Evidence span: Nodes must be wired with correct variable mappings to ensure downstream nodes get the required input.

### P1-AIP-D3-135

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-135 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 2: Implementation and Integration |
| `exam_task` | Task 2.4: Implement FM API integrations. |
| `exam_skill` | Skill 2.4.1: Create flexible model interaction systems (for example, by using Amazon Bedrock APIs to manage synchronous requests from various compute environments, language-specific AWS SDKs and Amazon SQS for asynchronous processing, API Gateway to provide custom API clients with request validation). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order012 |
| `accelerated_day` | Day 3 |
| `topic` | Synchronous FM API integration |
| `knowledge_category` | Skill; Representation / Location |
| `knowledge_type` | Procedural; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | optimize |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | lambda-provisioned-concurrency |
| `raw_source` | 2026-06-30T051823Z-openai-gpt-4.1-day-03-order012.md item 1 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051823Z |
| `raw_run_id` | order012 |

Stem:

A retail application integrates with Amazon Bedrock for product description generation via an API Gateway endpoint backed by a Lambda function. Customers report increased latency during periods of high request volume. Which approach best improves response times for synchronous FM API integration?

Options:

1. Enable provisioned concurrency for the Lambda function behind the API Gateway.
2. Increase the API Gateway timeout to a higher value.
3. Switch from synchronous to asynchronous invocation via Amazon SQS.
4. Reduce the payload size in the API Gateway integration request.

Correct answer: Enable provisioned concurrency for the Lambda function behind the API Gateway.

Rationale: Provisioned concurrency ensures that a set number of Lambda instances are always warm and ready, minimizing cold start latency during high-traffic periods.

Distractors: Increase the API Gateway timeout to a higher value.: This changes the permitted function execution time, not function startup latency; customers will still experience cold start delays.; Switch from synchronous to asynchronous invocation via Amazon SQS.: This breaks the synchronous design required by the application, introducing delays for the end-user.; Reduce the payload size in the API Gateway integration request.: Smaller payloads can offer marginal improvements, but they do not address the primary latency caused by cold starts.

Misconception tags: cold start; latency; synchronous vs asynchronous

Source trace:

https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The source states provisioned concurrency reduces startup time, directly addressing the latency observed in synchronous workflows.
   Source: https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html
   Evidence span: Provisioned concurrency keeps functions initialized and ready to respond in double-digit milliseconds.

### P1-AIP-D3-136

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-136 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 2: Implementation and Integration |
| `exam_task` | Task 2.4: Implement FM API integrations. |
| `exam_skill` | Skill 2.4.1: Create flexible model interaction systems (for example, by using Amazon Bedrock APIs to manage synchronous requests from various compute environments, language-specific AWS SDKs and Amazon SQS for asynchronous processing, API Gateway to provide custom API clients with request validation). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order012 |
| `accelerated_day` | Day 3 |
| `topic` | Synchronous FM API integration |
| `knowledge_category` | Skill; Representation / Location |
| `knowledge_type` | Procedural; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | api-gateway-request-validation |
| `raw_source` | 2026-06-30T051823Z-openai-gpt-4.1-day-03-order012.md item 2 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051823Z |
| `raw_run_id` | order012 |

Stem:

An engineering team must provide robust request validation on their API Gateway endpoint in front of a Lambda that queries Amazon Bedrock synchronously. Which API Gateway feature should they enable to reject invalid requests before reaching Lambda?

Options:

1. API Gateway request validation
2. WAF (Web Application Firewall) integration
3. Lambda function input data schema checking
4. Service Quotas enforcement

Correct answer: API Gateway request validation

Rationale: API Gateway’s built-in request validation checks the structure and/or content of requests, rejecting malformed requests before they reach Lambda.

Distractors: WAF (Web Application Firewall) integration: WAF blocks malicious traffic but is not intended for API data schema validation.; Lambda function input data schema checking: This approach validates input after the request already reaches Lambda, wasting compute if the request can be validated earlier.; Service Quotas enforcement: Quotas restrict throughput, not request validity.

Misconception tags: request validation; API Gateway capability; input schema

Source trace:

https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-method-request-validation.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The cited documentation confirms API Gateway handles request validation before the request is sent to Lambda.
   Source: https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-method-request-validation.html
   Evidence span: API Gateway can be configured to validate incoming requests before they reach backend integrations.

### P1-AIP-D3-137

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-137 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 2: Implementation and Integration |
| `exam_task` | Task 2.4: Implement FM API integrations. |
| `exam_skill` | Skill 2.4.1: Create flexible model interaction systems (for example, by using Amazon Bedrock APIs to manage synchronous requests from various compute environments, language-specific AWS SDKs and Amazon SQS for asynchronous processing, API Gateway to provide custom API clients with request validation). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order012 |
| `accelerated_day` | Day 3 |
| `topic` | Synchronous FM API integration |
| `knowledge_category` | Skill; Representation / Location |
| `knowledge_type` | Procedural; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | optimize |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | lambda-provisioned-concurrency |
| `raw_source` | 2026-06-30T051823Z-openai-gpt-4.1-day-03-order012.md item 3 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051823Z |
| `raw_run_id` | order012 |

Stem:

A developer configures synchronous FM API integration using Amazon Bedrock, API Gateway (HTTP API), and AWS Lambda. Demand surges during a viral campaign. The Lambda function experiences scaling delays resulting in occasional timeouts at the API Gateway. What should the developer do to ensure consistently low latencies?

Options:

1. Increase Lambda provisioned concurrency for the function.
2. Increase the burst limit in API Gateway.
3. Switch to a REST API Gateway instead of HTTP API.
4. Add a retry policy to the API Gateway integration.

Correct answer: Increase Lambda provisioned concurrency for the function.

Rationale: Provisioned concurrency proactively initializes Lambda environments, reducing cold starts and latency spikes under heavy demand.

Distractors: Increase the burst limit in API Gateway.: Increasing burst limits can help with throttling, but does not resolve Lambda startup delays.; Switch to a REST API Gateway instead of HTTP API.: Switching API Gateway types will not change function cold start behavior.; Add a retry policy to the API Gateway integration.: Retries alone would not eliminate latency caused by cold starts; they may increase perceived delays.

Misconception tags: cold start; API Gateway vs Lambda limits

Source trace:

https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The evidence confirms provisioned concurrency directly addresses startup delays, preventing timeouts due to Lambda scaling.
   Source: https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html
   Evidence span: Provisioned concurrency initializes a requested number of execution environments so that they are prepared to respond immediately.

### P1-AIP-D3-138

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-138 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 2: Implementation and Integration |
| `exam_task` | Task 2.4: Implement FM API integrations. |
| `exam_skill` | Skill 2.4.1: Create flexible model interaction systems (for example, by using Amazon Bedrock APIs to manage synchronous requests from various compute environments, language-specific AWS SDKs and Amazon SQS for asynchronous processing, API Gateway to provide custom API clients with request validation). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order012 |
| `accelerated_day` | Day 3 |
| `topic` | Synchronous FM API integration |
| `knowledge_category` | Skill; Representation / Location |
| `knowledge_type` | Procedural; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | api-gateway-limits |
| `raw_source` | 2026-06-30T051823Z-openai-gpt-4.1-day-03-order012.md item 4 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051823Z |
| `raw_run_id` | order012 |

Stem:

A team is building a synchronous GenAI inference API for internal users. To maintain stable performance, they need to enforce maximum payload sizes and limit incoming calls. Which combination of API Gateway features should they use?

Options:

1. Request validation and throttling limits
2. Custom domain names and usage plans
3. API logging and caching
4. Enable WAF and custom request headers

Correct answer: Request validation and throttling limits

Rationale: Request validation lets you constrain payload size and schema; throttling provides systematic control over the rate of incoming calls.

Distractors: Custom domain names and usage plans: Custom domains help with routing and branding; usage plans manage access but do not throttle at the method level.; API logging and caching: Logging helps monitor and caching can improve speed, but neither restricts payload size or limits requests.; Enable WAF and custom request headers: WAF addresses security, not payload size, and custom headers do not enforce API-level limits.

Misconception tags: payload vs security limits; API Gateway core features

Source trace:

https://docs.aws.amazon.com/apigateway/latest/developerguide/limits.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Enabling request validation and throttling directly implements request and payload limits as required by the scenario.
   Source: https://docs.aws.amazon.com/apigateway/latest/developerguide/limits.html
   Evidence span: API Gateway enforces limits on payload size and request rates through request validation and throttling.

### P1-AIP-D3-139

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-139 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 2: Implementation and Integration |
| `exam_task` | Task 2.4: Implement FM API integrations. |
| `exam_skill` | Skill 2.4.1: Create flexible model interaction systems (for example, by using Amazon Bedrock APIs to manage synchronous requests from various compute environments, language-specific AWS SDKs and Amazon SQS for asynchronous processing, API Gateway to provide custom API clients with request validation). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order012 |
| `accelerated_day` | Day 3 |
| `topic` | Synchronous FM API integration |
| `knowledge_category` | Skill; Representation / Location |
| `knowledge_type` | Procedural; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | lambda-provisioned-concurrency |
| `raw_source` | 2026-06-30T051823Z-openai-gpt-4.1-day-03-order012.md item 5 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051823Z |
| `raw_run_id` | order012 |

Stem:

While integrating Bedrock FMs using synchronous Lambda invocations behind API Gateway, a sudden surge in traffic leads to intermittent throttling errors. After reviewing API Gateway quotas, the team decides to investigate Lambda configurations. Which Lambda metric or feature should they focus on first to reduce throttling?

Options:

1. Provisioned concurrency settings
2. Lambda memory allocation
3. Lambda environment variables
4. Lambda function timeout

Correct answer: Provisioned concurrency settings

Rationale: Provisioned concurrency assures enough ready-to-serve Lambda containers to meet surge demand, reducing request throttling when traffic spikes.

Distractors: Lambda memory allocation: Memory allocation affects function execution speed, but not capacity under surge; throttling is typically a result of insufficient concurrent instances.; Lambda environment variables: Environment variables do not impact scale or capacity.; Lambda function timeout: A shorter timeout doesn't prevent throttling due to scaling issues—it may just fail faster.

Misconception tags: concurrency vs speed; Lambda scaling

Source trace:

https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Provisioned concurrency directly addresses scaling issues leading to throttling when handling synchronous high traffic.
   Source: https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html
   Evidence span: Provisioned concurrency enables Lambda to serve predictable levels of traffic with reduced throttling risks.

### P1-AIP-D3-140

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-140 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 2: Implementation and Integration |
| `exam_task` | Task 2.4: Implement FM API integrations. |
| `exam_skill` | Skill 2.4.1: Create flexible model interaction systems (for example, by using Amazon Bedrock APIs to manage synchronous requests from various compute environments, language-specific AWS SDKs and Amazon SQS for asynchronous processing, API Gateway to provide custom API clients with request validation). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order012 |
| `accelerated_day` | Day 3 |
| `topic` | Synchronous FM API integration |
| `knowledge_category` | Skill; Representation / Location |
| `knowledge_type` | Procedural; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | api-gateway-request-validation |
| `raw_source` | 2026-06-30T051823Z-openai-gpt-4.1-day-03-order012.md item 6 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051823Z |
| `raw_run_id` | order012 |

Stem:

You must secure your synchronous GenAI API (API Gateway + Lambda + Bedrock) such that only well-formed requests reach the Lambda function. Which API Gateway configuration allows you to reject non-JSON requests without invoking downstream compute?

Options:

1. Enable body validation in API Gateway method request validation
2. Require an API key and usage plan
3. Enable detailed CloudWatch logging
4. Set Lambda function policy to allow only JSON input

Correct answer: Enable body validation in API Gateway method request validation

Rationale: API Gateway’s method request validation can enforce content-type and body schema policies, immediately rejecting invalid JSON without cost or latency to Lambda.

Distractors: Require an API key and usage plan: API keys restrict access per user, not enforce content validation.; Enable detailed CloudWatch logging: Logging tracks requests but doesn't block malformed or non-JSON requests.; Set Lambda function policy to allow only JSON input: Lambda policies govern permissions, not content validation.

Misconception tags: method validation vs access control; Lambda policies scope

Source trace:

https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-method-request-validation.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Request validation in API Gateway provides the correct, pre-invocation enforcement for JSON format.
   Source: https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-method-request-validation.html
   Evidence span: Request validation can be configured on method requests to enforce content types and request body schemas.

### P1-AIP-D3-141

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-141 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 2: Implementation and Integration |
| `exam_task` | Task 2.4: Implement FM API integrations. |
| `exam_skill` | Skill 2.4.1: Create flexible model interaction systems (for example, by using Amazon Bedrock APIs to manage synchronous requests from various compute environments, language-specific AWS SDKs and Amazon SQS for asynchronous processing, API Gateway to provide custom API clients with request validation). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order012 |
| `accelerated_day` | Day 3 |
| `topic` | Synchronous FM API integration |
| `knowledge_category` | Skill; Representation / Location |
| `knowledge_type` | Procedural; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | lambda-provisioned-concurrency |
| `raw_source` | 2026-06-30T051823Z-openai-gpt-4.1-day-03-order012.md item 7 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051823Z |
| `raw_run_id` | order012 |

Stem:

Your company is integrating a front-end web portal with an FM backend via synchronous Bedrock API calls, exposed through API Gateway with Lambda. Executives require near-instant responses for all users, at any scale. What feature must you configure to guarantee this requirement?

Options:

1. Provisioned concurrency for the Lambda function
2. Enable logging in API Gateway
3. Set up an API Gateway usage plan
4. Increase Lambda timeout duration

Correct answer: Provisioned concurrency for the Lambda function

Rationale: Only provisioned concurrency pre-initializes Lambda containers to avoid cold starts, ensuring all requests receive low-latency responses even during burst loads.

Distractors: Enable logging in API Gateway: Logging assists in monitoring but does not improve real-time responsiveness.; Set up an API Gateway usage plan: Usage plans limit calls but do not guarantee responsiveness.; Increase Lambda timeout duration: Longer timeouts do not prevent slow start or high-latency, but only extend maximum allowed run time.

Misconception tags: resource allocation vs access limits; real-time latency

Source trace:

https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Provisioned concurrency is required for consistent, low-latency Lambda execution under any scale.
   Source: https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html
   Evidence span: Provisioned concurrency keeps environments initialized and prepared to respond immediately.

### P1-AIP-D3-142

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-142 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 2: Implementation and Integration |
| `exam_task` | Task 2.4: Implement FM API integrations. |
| `exam_skill` | Skill 2.4.1: Create flexible model interaction systems (for example, by using Amazon Bedrock APIs to manage synchronous requests from various compute environments, language-specific AWS SDKs and Amazon SQS for asynchronous processing, API Gateway to provide custom API clients with request validation). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order012 |
| `accelerated_day` | Day 3 |
| `topic` | Synchronous FM API integration |
| `knowledge_category` | Skill; Representation / Location |
| `knowledge_type` | Procedural; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | api-gateway-limits |
| `raw_source` | 2026-06-30T051823Z-openai-gpt-4.1-day-03-order012.md item 8 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051823Z |
| `raw_run_id` | order012 |

Stem:

A synchronous Bedrock API is exposed via API Gateway. During performance tuning, developers want to know the maximum payload size allowed in a single request. Which documentation section should they consult for this exact figure?

Options:

1. API Gateway endpoint quotas and limits
2. Amazon Bedrock model parameters reference
3. Lambda maximum event size
4. API Gateway logging best practices

Correct answer: API Gateway endpoint quotas and limits

Rationale: API Gateway documentation specifically lists hard quotas on payload size for integrations, establishing the external request limit.

Distractors: Amazon Bedrock model parameters reference: Bedrock defines model-specific input constraints, but the request must first fit under API Gateway's limits.; Lambda maximum event size: Lambda event size is relevant to payload handoff but not to the actual API request size limit.; API Gateway logging best practices: Logging best practices provide observability, not operational limits.

Misconception tags: service boundaries; limit enforcement location

Source trace:

https://docs.aws.amazon.com/apigateway/latest/developerguide/limits.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The API Gateway limits documentation establishes the top allowable input size, upstream from Lambda and Bedrock.
   Source: https://docs.aws.amazon.com/apigateway/latest/developerguide/limits.html
   Evidence span: API Gateway imposes maximum payload size on incoming requests.

### P1-AIP-D3-143

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-143 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 2: Implementation and Integration |
| `exam_task` | Task 2.4: Implement FM API integrations. |
| `exam_skill` | Skill 2.4.1: Create flexible model interaction systems (for example, by using Amazon Bedrock APIs to manage synchronous requests from various compute environments, language-specific AWS SDKs and Amazon SQS for asynchronous processing, API Gateway to provide custom API clients with request validation). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order012 |
| `accelerated_day` | Day 3 |
| `topic` | Synchronous FM API integration |
| `knowledge_category` | Skill; Representation / Location |
| `knowledge_type` | Procedural; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | optimize |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | lambda-provisioned-concurrency |
| `raw_source` | 2026-06-30T051823Z-openai-gpt-4.1-day-03-order012.md item 9 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051823Z |
| `raw_run_id` | order012 |

Stem:

Your Lambda-based synchronous FM API behind API Gateway needs to meet strict sub-100ms response SLAs during business hours, even with unpredictable traffic spikes. What is the most effective Lambda configuration to achieve this goal?

Options:

1. Set the desired provisioned concurrency high enough to handle peak load.
2. Allocate maximum memory for the Lambda function.
3. Deploy multiple Lambda functions across regions.
4. Enable Lambda VPC integration.

Correct answer: Set the desired provisioned concurrency high enough to handle peak load.

Rationale: Provisioned concurrency pre-warms Lambda execution environments, eliminating cold start delays that would break the strict SLA.

Distractors: Allocate maximum memory for the Lambda function.: More memory increases processing speed, not readiness or scaling capacity.; Deploy multiple Lambda functions across regions.: Regional deployments help with redundancy but not with cold start latency in a single region.; Enable Lambda VPC integration.: VPC integration is relevant for networking, but can slow performance if not carefully optimized.

Misconception tags: performance vs readiness; cold start risk; multi-region confusion

Source trace:

https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Provisioned concurrency is specifically designed to maintain fast response times regardless of unpredictable scales.
   Source: https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html
   Evidence span: "provisioned concurrency enables double-digit millisecond start times for functions at any scale"

### P1-AIP-D3-144

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-144 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 2: Implementation and Integration |
| `exam_task` | Task 2.4: Implement FM API integrations. |
| `exam_skill` | Skill 2.4.1: Create flexible model interaction systems (for example, by using Amazon Bedrock APIs to manage synchronous requests from various compute environments, language-specific AWS SDKs and Amazon SQS for asynchronous processing, API Gateway to provide custom API clients with request validation). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order012 |
| `accelerated_day` | Day 3 |
| `topic` | Synchronous FM API integration |
| `knowledge_category` | Skill; Representation / Location |
| `knowledge_type` | Procedural; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | implement |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | api-gateway-request-validation |
| `raw_source` | 2026-06-30T051823Z-openai-gpt-4.1-day-03-order012.md item 10 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051823Z |
| `raw_run_id` | order012 |

Stem:

A team integrates an external system with a synchronous Bedrock API via API Gateway and Lambda. The system occasionally sends malformed requests that break JSON structure. Which configuration prevents these bad payloads from reaching Lambda or Bedrock?

Options:

1. Enable request validation on the API Gateway integration method.
2. Use Lambda handler code to parse and reject malformed JSON.
3. Configure Bedrock API to reject invalid payloads directly.
4. Deploy WAF rules for content inspection.

Correct answer: Enable request validation on the API Gateway integration method.

Rationale: API Gateway’s request validation stops malformed requests at the entry point, sparing Lambda and Bedrock unnecessary load.

Distractors: Use Lambda handler code to parse and reject malformed JSON.: Lambda code validation comes after the request has already triggered compute cost.; Configure Bedrock API to reject invalid payloads directly.: Bedrock receives requests only after they pass through upstream layers; payloads should be cleaned sooner.; Deploy WAF rules for content inspection.: WAF helps with security threats, not structured schema/JSON validation.

Misconception tags: validation layer; cost minimization; defensive design

Source trace:

https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-method-request-validation.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: API Gateway's request validation is recommended to catch schema errors before triggering downstream execution.
   Source: https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-method-request-validation.html
   Evidence span: Request validation can be used to enforce input schema on requests.

### P1-AIP-D3-145

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-145 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 2: Implementation and Integration |
| `exam_task` | Task 2.4: Implement FM API integrations. |
| `exam_skill` | Skill 2.4.1: Create flexible model interaction systems (for example, by using Amazon Bedrock APIs to manage synchronous requests from various compute environments, language-specific AWS SDKs and Amazon SQS for asynchronous processing, API Gateway to provide custom API clients with request validation). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order012 |
| `accelerated_day` | Day 3 |
| `topic` | Synchronous FM API integration |
| `knowledge_category` | Skill; Representation / Location |
| `knowledge_type` | Procedural; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | implement |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | lambda-provisioned-concurrency |
| `raw_source` | 2026-06-30T051823Z-openai-gpt-4.1-day-03-order012.md item 11 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051823Z |
| `raw_run_id` | order012 |

Stem:

A developer is integrating Lambda with API Gateway for low-latency, synchronous Bedrock inference. How can they guarantee Lambda functions won't experience cold start latency for requests routed via API Gateway during heavy usage?

Options:

1. Configure provisioned concurrency at a suitable value for the Lambda function.
2. Configure a scheduled CloudWatch event to invoke the function regularly.
3. Enable dead-letter queues for the Lambda function.
4. Use Lambda@Edge to distribute invocation traffic.

Correct answer: Configure provisioned concurrency at a suitable value for the Lambda function.

Rationale: Provisioned concurrency pre-initializes Lambda execution environments so invocations are instantly served without cold start delays, even under load.

Distractors: Configure a scheduled CloudWatch event to invoke the function regularly.: Ping events may reduce cold starts but do not scale for variable load or guarantee readiness at arbitrary times.; Enable dead-letter queues for the Lambda function.: DLQs help handle failures, not cold start performance.; Use Lambda@Edge to distribute invocation traffic.: Lambda@Edge optimizes global network placement, not start time for a specific Lambda in a region.

Misconception tags: provisioned concurrency vs keep-alive; latency root cause

Source trace:

https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Provisioned concurrency is the AWS-recommended approach to eliminate cold start latency.
   Source: https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html
   Evidence span: Provisioned concurrency maintains a pool of initialized environments ready for immediate service.

### P1-AIP-D3-146

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-146 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 2: Implementation and Integration |
| `exam_task` | Task 2.4: Implement FM API integrations. |
| `exam_skill` | Skill 2.4.1: Create flexible model interaction systems (for example, by using Amazon Bedrock APIs to manage synchronous requests from various compute environments, language-specific AWS SDKs and Amazon SQS for asynchronous processing, API Gateway to provide custom API clients with request validation). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order012 |
| `accelerated_day` | Day 3 |
| `topic` | Synchronous FM API integration |
| `knowledge_category` | Skill; Representation / Location |
| `knowledge_type` | Procedural; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | api-gateway-limits |
| `raw_source` | 2026-06-30T051823Z-openai-gpt-4.1-day-03-order012.md item 13 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051823Z |
| `raw_run_id` | order012 |

Stem:

A developer is troubleshooting an intermittent 413 Payload Too Large error for their synchronous Bedrock API behind API Gateway and Lambda. What is the most likely cause, and where should they look first?

Options:

1. API Gateway request and response payload limits are being exceeded.
2. Lambda’s memory allocation is too low for handling the payload.
3. Bedrock’s individual model input parameter size is being exceeded.
4. Downstream service concurrency limits have been hit.

Correct answer: API Gateway request and response payload limits are being exceeded.

Rationale: The 413 error from API Gateway specifically indicates the payload exceeds API Gateway’s hard-coded limits—not Lambda or Bedrock constraints.

Distractors: Lambda’s memory allocation is too low for handling the payload.: Memory shortage might result in timeouts or errors, but not a 413 error code.; Bedrock’s individual model input parameter size is being exceeded.: Bedrock returns model-specific error responses, not the 413 error which is produced upstream by API Gateway.; Downstream service concurrency limits have been hit.: Concurrency issues manifest as throttling or timeout errors, not 413 payload errors.

Misconception tags: error code source; API Gateway limits vs downstream

Source trace:

https://docs.aws.amazon.com/apigateway/latest/developerguide/limits.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The official documentation links 413 errors specifically with exceeding payload limits at the API Gateway stage.
   Source: https://docs.aws.amazon.com/apigateway/latest/developerguide/limits.html
   Evidence span: "API Gateway returns 413 (Payload Too Large) if the payload exceeds the configured quota."

### P1-AIP-D3-147

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-147 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 2: Implementation and Integration |
| `exam_task` | Task 2.4: Implement FM API integrations. |
| `exam_skill` | Skill 2.4.1: Create flexible model interaction systems (for example, by using Amazon Bedrock APIs to manage synchronous requests from various compute environments, language-specific AWS SDKs and Amazon SQS for asynchronous processing, API Gateway to provide custom API clients with request validation). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order013 |
| `accelerated_day` | Day 3 |
| `topic` | Asynchronous FM processing |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Conceptual; Procedural; Conditional; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | lambda-sqs-event-source |
| `raw_source` | 2026-06-30T051911Z-openai-gpt-4.1-day-03-order013.md item 1 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051911Z |
| `raw_run_id` | order013 |

Stem:

A generative AI application runs an Amazon Bedrock-augmented backend. To ensure requests are not lost if the FM has variable response times, a developer places incoming requests on an SQS queue and invokes Lambda functions for downstream processing. After a scaling event, some requests are being lost. What is the MOST likely cause?

Options:

1. The Lambda function's batch size is too large for the number of available function instances.
2. There is no dead-letter queue configured for the SQS queue.
3. API Gateway request validation is not properly configured.
4. The SQS queue is configured with a delay period that is too short.

Correct answer: The Lambda function's batch size is too large for the number of available function instances.

Rationale: If the batch size is too large and Lambda cannot scale quickly enough, some messages can exceed their visibility timeout before processing, leading to dropped or re-queued requests.

Distractors: There is no dead-letter queue configured for the SQS queue.: A missing dead-letter queue means failed messages are not retained for further inspection, but does not itself cause message loss or timeouts.; API Gateway request validation is not properly configured.: API Gateway is not involved in SQS-to-Lambda event processing, so its validation does not impact backend message loss.; The SQS queue is configured with a delay period that is too short.: Delay periods only affect when messages become visible, not the risk of loss during batch consumption and scaling.

Misconception tags: batching; scaling; queue processing

Source trace:

https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html#events-sqs-eventsource-mapping

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The cited source describes the risk when batch size exceeds scaling capacity, matching the described loss scenario.
   Source: https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html#events-sqs-eventsource-mapping
   Evidence span: Carefully consider the batch size when configuring an SQS event source mapping to ensure messages can be processed before their visibility timeout expires.

### P1-AIP-D3-148

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-148 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 2: Implementation and Integration |
| `exam_task` | Task 2.4: Implement FM API integrations. |
| `exam_skill` | Skill 2.4.1: Create flexible model interaction systems (for example, by using Amazon Bedrock APIs to manage synchronous requests from various compute environments, language-specific AWS SDKs and Amazon SQS for asynchronous processing, API Gateway to provide custom API clients with request validation). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order013 |
| `accelerated_day` | Day 3 |
| `topic` | Asynchronous FM processing |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Conceptual; Procedural; Conditional; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | lambda-sqs-event-source |
| `raw_source` | 2026-06-30T051911Z-openai-gpt-4.1-day-03-order013.md item 3 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051911Z |
| `raw_run_id` | order013 |

Stem:

A SaaS platform sends thousands of inference requests to an Amazon Bedrock FM through Lambda functions triggered by SQS messages. There is a sudden spike in the number of Lambda invocations and message re-drives. What is the MOST probable root cause?

Options:

1. The Lambda function failed its execution, so the SQS messages became visible again and were retried.
2. SQS automatically deletes messages after the first processing attempt.
3. The API Gateway endpoint rate limited requests, causing message duplication.
4. Lambda scaled faster than the SQS queue could handle.

Correct answer: The Lambda function failed its execution, so the SQS messages became visible again and were retried.

Rationale: A failed Lambda execution for a message causes SQS to make the message visible again, triggering another Lambda invocation due to retry semantics.

Distractors: SQS automatically deletes messages after the first processing attempt.: SQS only deletes a message after a Lambda function has successfully processed and deleted it; otherwise, retries happen.; The API Gateway endpoint rate limited requests, causing message duplication.: API Gateway throttling is not directly related to Lambda retries from SQS triggers.; Lambda scaled faster than the SQS queue could handle.: SQS is a managed service and can handle rapid scaling, but failed Lambda executions—not scaling—drive re-invocations.

Misconception tags: SQS retry behavior; message lifecycle; Lambda failure

Source trace:

https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html#events-sqs-eventsource-mapping

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The behavior of making messages visible and triggering retries for failed executions is described and matched in the AWS Lambda documentation.
   Source: https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html#events-sqs-eventsource-mapping
   Evidence span: When your function successfully processes a batch, Lambda deletes its messages from the queue…If your function returns an error for a batch, Lambda returns the entire batch to the queue.

### P1-AIP-D3-149

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-149 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 2: Implementation and Integration |
| `exam_task` | Task 2.4: Implement FM API integrations. |
| `exam_skill` | Skill 2.4.1: Create flexible model interaction systems (for example, by using Amazon Bedrock APIs to manage synchronous requests from various compute environments, language-specific AWS SDKs and Amazon SQS for asynchronous processing, API Gateway to provide custom API clients with request validation). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order013 |
| `accelerated_day` | Day 3 |
| `topic` | Asynchronous FM processing |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Conceptual; Procedural; Conditional; Embedded |
| `question_format` | multiple-response |
| `difficulty` | medium |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | lambda-sqs-event-source |
| `raw_source` | 2026-06-30T051911Z-openai-gpt-4.1-day-03-order013.md item 4 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051911Z |
| `raw_run_id` | order013 |

Stem:

You are designing a GenAI batch inference pipeline where compute resources must not block on FM responses. The team suggests using Amazon SQS with Lambda, but wants to guarantee at-least-once delivery and error capture. Which actions should you recommend? (Select TWO.)

Options:

1. Configure a dead-letter queue for the SQS queue.
2. Ensure the Lambda function deletes messages from the queue only upon successful processing.
3. Enable SQS FIFO queue semantics.
4. Increase SQS message retention to 14 days.
5. Set Lambda batch window to 60 seconds.

Correct answer: Configure a dead-letter queue for the SQS queue.; Ensure the Lambda function deletes messages from the queue only upon successful processing.

Rationale: A DLQ guarantees errors are captured after retry exhaustion. Proper deletion on successful completion ensures at-least-once delivery; if not, messages are retried.

Distractors: Enable SQS FIFO queue semantics.: FIFO queues are for ordering and exactly-once processing, not required for at-least-once guarantees and error capture.; Increase SQS message retention to 14 days.: Longer retention helps with debugging but is not required for core delivery guarantees.; Set Lambda batch window to 60 seconds.: Batch window tuning affects batching efficiency, not delivery guarantee or error handling.

Misconception tags: DLQ purpose; Lambda-SQS integration; delivery semantics

Source trace:

https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html#events-sqs-eventsource-mapping

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The documentation recommends using DLQs and deleting messages upon successful Lambda processing to achieve both error capture and delivery guarantees.
   Source: https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html#events-sqs-eventsource-mapping
   Evidence span: Configure a dead-letter queue...Lambda deletes messages from the queue only after successful processing.

### P1-AIP-D3-150

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-150 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 2: Implementation and Integration |
| `exam_task` | Task 2.4: Implement FM API integrations. |
| `exam_skill` | Skill 2.4.1: Create flexible model interaction systems (for example, by using Amazon Bedrock APIs to manage synchronous requests from various compute environments, language-specific AWS SDKs and Amazon SQS for asynchronous processing, API Gateway to provide custom API clients with request validation). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order013 |
| `accelerated_day` | Day 3 |
| `topic` | Asynchronous FM processing |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Conceptual; Procedural; Conditional; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | step-functions-overview |
| `raw_source` | 2026-06-30T051911Z-openai-gpt-4.1-day-03-order013.md item 5 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051911Z |
| `raw_run_id` | order013 |

Stem:

An enterprise GenAI system processes documents through asynchronous Bedrock API calls. The team wants to sequence processing, add timeouts, and handle retryable failure conditions across multiple microservices. Which AWS component or pattern is MOST suitable?

Options:

1. Step Functions' workflow orchestration for microservice integration
2. Direct invocation of Bedrock from each microservice
3. A single Lambda function polling an SQS queue
4. Manual coordination via a database and batch scripts

Correct answer: Step Functions' workflow orchestration for microservice integration

Rationale: Step Functions enables orchestration, parallelization, timeout control, and error/retry policies across distributed and asynchronous services.

Distractors: Direct invocation of Bedrock from each microservice: Direct invocation lacks orchestration, retry, and timeout management across services.; A single Lambda function polling an SQS queue: Polling is a batch pattern and not a robust, multi-stage orchestrator.; Manual coordination via a database and batch scripts: Manual methods reduce reliability and lack native AWS orchestration/control.

Misconception tags: manual orchestration; retry vs. workflow; error handling

Source trace:

https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Step Functions is the recommended AWS managed workflow orchestrator, offering timeouts and retries natively.
   Source: https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html
   Evidence span: Step Functions coordinates the components of distributed applications and microservices using visual workflows.

### P1-AIP-D3-151

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-151 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 2: Implementation and Integration |
| `exam_task` | Task 2.4: Implement FM API integrations. |
| `exam_skill` | Skill 2.4.1: Create flexible model interaction systems (for example, by using Amazon Bedrock APIs to manage synchronous requests from various compute environments, language-specific AWS SDKs and Amazon SQS for asynchronous processing, API Gateway to provide custom API clients with request validation). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order013 |
| `accelerated_day` | Day 3 |
| `topic` | Asynchronous FM processing |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Conceptual; Procedural; Conditional; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | lambda-sqs-event-source |
| `raw_source` | 2026-06-30T051911Z-openai-gpt-4.1-day-03-order013.md item 6 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051911Z |
| `raw_run_id` | order013 |

Stem:

A large document analysis batch job uses Lambda triggered by SQS. After a spike in job volume, some messages stay in the SQS queue for a long time and are not processed until nearly the retention limit. What is the MOST likely misconfiguration?

Options:

1. Lambda’s concurrency isn’t high enough to keep up with the arrival rate.
2. SQS FIFO queue is causing delays due to sequencing.
3. Bedrock FM API throttling is causing Lambda failures.
4. Step Functions wait tasks are holding messages intentionally.

Correct answer: Lambda’s concurrency isn’t high enough to keep up with the arrival rate.

Rationale: If Lambda can’t scale quickly enough to process incoming SQS messages, messages accumulate in the queue and may approach retention limits.

Distractors: SQS FIFO queue is causing delays due to sequencing.: Sequencing delays can occur in FIFO, but standard queues are more common for large-scale ingestion and do not enforce strict order.; Bedrock FM API throttling is causing Lambda failures.: Throttling may cause retries, but the primary symptom is message backlog, indicating Lambda's scaling is insufficient.; Step Functions wait tasks are holding messages intentionally.: Wait tasks would be visible as part of a Step Functions workflow, not in direct Lambda-SQS patterns.

Misconception tags: Lambda scaling; queue backlog; retention

Source trace:

https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html#events-sqs-eventsource-mapping

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: AWS documentation clarifies that Lambda concurrency controls message throughput for SQS triggers.
   Source: https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html#events-sqs-eventsource-mapping
   Evidence span: If your Lambda function can't scale up to match the arrival rate, messages might accumulate in the queue.

### P1-AIP-D3-152

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-152 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 2: Implementation and Integration |
| `exam_task` | Task 2.4: Implement FM API integrations. |
| `exam_skill` | Skill 2.4.1: Create flexible model interaction systems (for example, by using Amazon Bedrock APIs to manage synchronous requests from various compute environments, language-specific AWS SDKs and Amazon SQS for asynchronous processing, API Gateway to provide custom API clients with request validation). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order013 |
| `accelerated_day` | Day 3 |
| `topic` | Asynchronous FM processing |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Conceptual; Procedural; Conditional; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | lambda-sqs-event-source |
| `raw_source` | 2026-06-30T051911Z-openai-gpt-4.1-day-03-order013.md item 7 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051911Z |
| `raw_run_id` | order013 |

Stem:

A developer designs an async pipeline where Bedrock FM inference requests are enqueued to SQS and processed by Lambda. They notice the same message is sometimes processed by two Lambda invocations nearly simultaneously. What is the MOST likely explanation?

Options:

1. The message's visibility timeout was set too short, causing multiple Lambda invocations before the first finishes.
2. Lambda concurrency is set too high for the SQS batch window.
3. API Gateway did not acknowledge the SQS message receipt.
4. There is no deduplication configured for Lambda.

Correct answer: The message's visibility timeout was set too short, causing multiple Lambda invocations before the first finishes.

Rationale: A short visibility timeout allows the same SQS message to become visible and trigger another Lambda invocation before the previous run completes.

Distractors: Lambda concurrency is set too high for the SQS batch window.: High concurrency may saturate workers but does not by itself cause duplicate message processing.; API Gateway did not acknowledge the SQS message receipt.: API Gateway is not in the SQS-Lambda processing path.; There is no deduplication configured for Lambda.: Lambda processes all visible messages; deduplication is handled via SQS for FIFO queues only.

Misconception tags: visibility timeout; duplicate processing; SQS-Lambda integration

Source trace:

https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html#events-sqs-eventsource-mapping

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: AWS documentation states that insufficient visibility timeout can result in overlapping Lambda invocations for the same message.
   Source: https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html#events-sqs-eventsource-mapping
   Evidence span: If your function doesn't delete the message before the visibility timeout expires, the message becomes available to be processed again.

### P1-AIP-D3-153

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-153 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 2: Implementation and Integration |
| `exam_task` | Task 2.4: Implement FM API integrations. |
| `exam_skill` | Skill 2.4.1: Create flexible model interaction systems (for example, by using Amazon Bedrock APIs to manage synchronous requests from various compute environments, language-specific AWS SDKs and Amazon SQS for asynchronous processing, API Gateway to provide custom API clients with request validation). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order013 |
| `accelerated_day` | Day 3 |
| `topic` | Asynchronous FM processing |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Conceptual; Procedural; Conditional; Embedded |
| `question_format` | multiple-response |
| `difficulty` | medium |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | lambda-sqs-event-source |
| `raw_source` | 2026-06-30T051911Z-openai-gpt-4.1-day-03-order013.md item 8 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051911Z |
| `raw_run_id` | order013 |

Stem:

A customer asks how to prevent message loss when using SQS and Lambda for asynchronous Bedrock inference jobs, even if their Lambda code encounters errors randomly. Which steps form the minimal AWS-recommended configuration? (Select TWO.)

Options:

1. Set a dead-letter queue for the primary SQS queue.
2. Set an SQS visibility timeout greater than the expected Lambda processing time.
3. Configure Lambda event source mapping to poll SQS with a batch size of 1.
4. Use SQS FIFO queues exclusively.
5. Set Lambda reserved concurrency to the maximum supported.

Correct answer: Set a dead-letter queue for the primary SQS queue.; Set an SQS visibility timeout greater than the expected Lambda processing time.

Rationale: A DLQ captures unprocessable messages after retries, and the correct visibility timeout reduces the risk of the same message becoming visible while still being processed.

Distractors: Configure Lambda event source mapping to poll SQS with a batch size of 1.: A batch size of 1 is not required for durability and may be suboptimal for performance.; Use SQS FIFO queues exclusively.: FIFO queues provide ordering, unrelated to error recovery or message loss.; Set Lambda reserved concurrency to the maximum supported.: Reserved concurrency improves scaling but does not ensure durability or error handling alone.

Misconception tags: DLQ; visibility timeout; durability

Source trace:

https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html#events-sqs-eventsource-mapping

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: AWS guidance recommends DLQs and proper visibility timeout as best practice for lossless async processing.
   Source: https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html#events-sqs-eventsource-mapping
   Evidence span: Set the visibility timeout on the source queue to at least six times the timeout you configure for your function…Use DLQs to capture failed messages.

### P1-AIP-D3-154

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-154 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 2: Implementation and Integration |
| `exam_task` | Task 2.4: Implement FM API integrations. |
| `exam_skill` | Skill 2.4.1: Create flexible model interaction systems (for example, by using Amazon Bedrock APIs to manage synchronous requests from various compute environments, language-specific AWS SDKs and Amazon SQS for asynchronous processing, API Gateway to provide custom API clients with request validation). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order013 |
| `accelerated_day` | Day 3 |
| `topic` | Asynchronous FM processing |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Conceptual; Procedural; Conditional; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | step-functions-overview |
| `raw_source` | 2026-06-30T051911Z-openai-gpt-4.1-day-03-order013.md item 9 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051911Z |
| `raw_run_id` | order013 |

Stem:

A generative AI company leverages Step Functions to coordinate multiple asynchronous tasks: document extraction, Bedrock model invocation, and post-processing. Occasionally, a failure in document extraction leads to silent process drops. What is the MOST effective configuration to address this?

Options:

1. Add Catch and Retry policies in the Step Functions state machine for the document extraction step.
2. Increase Lambda function memory for document extraction.
3. Switch from Step Functions to a polling model based on SQS events.
4. Configure SQS queue capacity for the post-processing step.

Correct answer: Add Catch and Retry policies in the Step Functions state machine for the document extraction step.

Rationale: Catch and Retry policies ensure that failures are detected and retried or handled appropriately rather than dropped silently.

Distractors: Increase Lambda function memory for document extraction.: More memory might prevent some failures but does not provide error handling or tracing.; Switch from Step Functions to a polling model based on SQS events.: Switching removes orchestration and may worsen error tracing.; Configure SQS queue capacity for the post-processing step.: This only affects queue size for later steps, not error handling in the extraction task.

Misconception tags: workflow error handling; Step Functions vs. polling; Catch/Retry policies

Source trace:

https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: AWS guides show Step Functions state machines use Catch and Retry to robustly handle failures in individual steps.
   Source: https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html
   Evidence span: State machines can include error handling, retry, and catch mechanisms for robust workflows.

### P1-AIP-D3-155

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-155 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 2: Implementation and Integration |
| `exam_task` | Task 2.4: Implement FM API integrations. |
| `exam_skill` | Skill 2.4.1: Create flexible model interaction systems (for example, by using Amazon Bedrock APIs to manage synchronous requests from various compute environments, language-specific AWS SDKs and Amazon SQS for asynchronous processing, API Gateway to provide custom API clients with request validation). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order013 |
| `accelerated_day` | Day 3 |
| `topic` | Asynchronous FM processing |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Conceptual; Procedural; Conditional; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order013-local-artifact |
| `raw_source` | 2026-06-30T051911Z-openai-gpt-4.1-day-03-order013.md item 10 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051911Z |
| `raw_run_id` | order013 |

Stem:

A team needs to decouple API-facing workloads from long-running generative AI jobs, guaranteeing API latency SLAs even when FM processing is slow. Which asynchronous AWS design pattern provides the MOST consistency for this requirement?

Options:

1. API Gateway triggers SQS, then a Lambda function processes SQS messages for Bedrock inference.
2. API Gateway calls Bedrock FM synchronously within a Lambda.
3. Step Functions synchronous Express workflow.
4. Direct invocation of Bedrock FM endpoints from API Gateway.

Correct answer: API Gateway triggers SQS, then a Lambda function processes SQS messages for Bedrock inference.

Rationale: Placing a queue between frontend and backend decouples requesters from slow workers; the API returns immediately while the heavy work is processed asynchronously.

Distractors: API Gateway calls Bedrock FM synchronously within a Lambda.: Synchronous invocation blocks until FM completes, violating latency SLAs under load.; Step Functions synchronous Express workflow.: Synchronous Express workflows block clients until completion unless managed with an async handoff pattern.; Direct invocation of Bedrock FM endpoints from API Gateway.: Direct synchronous calls prevent decoupling and guarantee potentially high latency.

Misconception tags: async queuing; SLAs; frontend/backend decoupling

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order013-asynchronous-fm-processing.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The referenced artifact highlights queue-first async patterns for API/foundation model decoupling.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order013-asynchronous-fm-processing.md
   Evidence span: Queue-based architectures decouple API clients from long-running inference tasks, improving SLA adherence.

### P1-AIP-D3-156

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-156 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 2: Implementation and Integration |
| `exam_task` | Task 2.4: Implement FM API integrations. |
| `exam_skill` | Skill 2.4.1: Create flexible model interaction systems (for example, by using Amazon Bedrock APIs to manage synchronous requests from various compute environments, language-specific AWS SDKs and Amazon SQS for asynchronous processing, API Gateway to provide custom API clients with request validation). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order013 |
| `accelerated_day` | Day 3 |
| `topic` | Asynchronous FM processing |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Conceptual; Procedural; Conditional; Embedded |
| `question_format` | multiple-response |
| `difficulty` | hard |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order013-local-artifact |
| `raw_source` | 2026-06-30T051911Z-openai-gpt-4.1-day-03-order013.md item 11 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051911Z |
| `raw_run_id` | order013 |

Stem:

Your async Amazon Bedrock FM pipeline includes SQS, Lambda, and Step Functions for complex coordination. Failure notifications are needed for unprocessable jobs. Which mechanisms are BEST for robust, observable error handling? (Select TWO.)

Options:

1. Configure Step Functions to send failure notifications via SNS on error.
2. Configure a dead-letter queue for SQS and alert on DLQ message arrival.
3. Increase Lambda batch size to buffer more messages.
4. Rely exclusively on CloudWatch Lambda error metrics.
5. Restrict Step Functions state retries to a single attempt.

Correct answer: Configure Step Functions to send failure notifications via SNS on error.; Configure a dead-letter queue for SQS and alert on DLQ message arrival.

Rationale: SNS notifications and DLQ alerts provide explicit, actionable signals for async processing failures.

Distractors: Increase Lambda batch size to buffer more messages.: Batch size tuning is relevant for throughput, not error handling.; Rely exclusively on CloudWatch Lambda error metrics.: Metrics provide insight but lack immediate notification and robust job tracing.; Restrict Step Functions state retries to a single attempt.: Reducing retries does not surface errors; it merely abandons retries sooner.

Misconception tags: alerting; observability; DLQ

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order013-asynchronous-fm-processing.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The artifact prescribes DLQ+SNS for robust observability in asynchronous error scenarios.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order013-asynchronous-fm-processing.md
   Evidence span: Combine DLQ and event-driven notifications (such as SNS) for error handling in orchestrated async pipelines.

### P1-AIP-D3-157

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-157 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 2: Implementation and Integration |
| `exam_task` | Task 2.4: Implement FM API integrations. |
| `exam_skill` | Skill 2.4.1: Create flexible model interaction systems (for example, by using Amazon Bedrock APIs to manage synchronous requests from various compute environments, language-specific AWS SDKs and Amazon SQS for asynchronous processing, API Gateway to provide custom API clients with request validation). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order013 |
| `accelerated_day` | Day 3 |
| `topic` | Asynchronous FM processing |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Conceptual; Procedural; Conditional; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order013-local-artifact |
| `raw_source` | 2026-06-30T051911Z-openai-gpt-4.1-day-03-order013.md item 12 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051911Z |
| `raw_run_id` | order013 |

Stem:

A developer wants to parallelize hundreds of asynchronous Bedrock FM inference jobs using AWS managed services in a cost-optimized and scalable way. Which option is MOST aligned with AWS recommendations?

Options:

1. Use SQS with Lambda for parallel job invocation and auto scaling.
2. Dedicate a single EC2 instance to run multiple inference jobs as background threads.
3. Invoke API Gateway synchronous endpoints from a central orchestrator.
4. Use Step Functions synchronous state machines.

Correct answer: Use SQS with Lambda for parallel job invocation and auto scaling.

Rationale: SQS-to-Lambda is a cost-efficient pattern for parallelizing tasks while leveraging AWS managed auto scaling.

Distractors: Dedicate a single EC2 instance to run multiple inference jobs as background threads.: Single EC2 instances do not scale easily and will likely lead to bottlenecks.; Invoke API Gateway synchronous endpoints from a central orchestrator.: Synchronous workflows may limit throughput and block resources.; Use Step Functions synchronous state machines.: Synchronous executions are limited in duration and costlier for long jobs compared to decoupled async event-driven patterns.

Misconception tags: scalability; cost optimization; parallelization

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order013-asynchronous-fm-processing.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The referenced source affirms SQS+Lambda as AWS's recommended approach to scalable, cost-aware async job parallelization.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order013-asynchronous-fm-processing.md
   Evidence span: SQS with Lambda enables high-scale, event-driven parallel execution for asynchronous jobs.

### P1-AIP-D3-158

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-158 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 2: Implementation and Integration |
| `exam_task` | Task 2.4: Implement FM API integrations. |
| `exam_skill` | Skill 2.4.1: Create flexible model interaction systems (for example, by using Amazon Bedrock APIs to manage synchronous requests from various compute environments, language-specific AWS SDKs and Amazon SQS for asynchronous processing, API Gateway to provide custom API clients with request validation). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order013 |
| `accelerated_day` | Day 3 |
| `topic` | Asynchronous FM processing |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Conceptual; Procedural; Conditional; Embedded |
| `question_format` | multiple-response |
| `difficulty` | hard |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | sqs-message-lifecycle |
| `raw_source` | 2026-06-30T051911Z-openai-gpt-4.1-day-03-order013.md item 13 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051911Z |
| `raw_run_id` | order013 |

Stem:

A Bedrock-powered GenAI batch process has unpredictable peak load periods and must never drop jobs. Which SQS configuration settings should the team review to minimize risk of lost or unprocessed messages? (Select TWO.)

Options:

1. Increase SQS message retention period to its maximum value.
2. Monitor and adjust Lambda concurrency relative to queue depth.
3. Change to an SQS FIFO queue configuration.
4. Reduce the visibility timeout for rapid redelivery.
5. Turn off DLQ to minimize system complexity.

Correct answer: Increase SQS message retention period to its maximum value.; Monitor and adjust Lambda concurrency relative to queue depth.

Rationale: Longer retention allows recovery after backlogs, and adjusting concurrency ensures Lambda can keep up with spikes, minimizing loss risk.

Distractors: Change to an SQS FIFO queue configuration.: FIFO queues are for ordering, not for loss avoidance, and might reduce throughput.; Reduce the visibility timeout for rapid redelivery.: Too short a visibility timeout risks duplicate processing and doesn't prevent loss.; Turn off DLQ to minimize system complexity.: DLQ provides error capture—turning it off increases loss risk, not reduces it.

Misconception tags: retention period; scaling; DLQ role

Source trace:

https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-message-lifecycle.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Official documentation covers both retention and concurrency as essential to avoid backlog-related loss in async processing.
   Source: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-message-lifecycle.html
   Evidence span: You can configure the message retention period from one minute to 14 days. Monitor your Lambda concurrency to match SQS throughput.

### P1-AIP-D3-159

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-159 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 2: Implementation and Integration |
| `exam_task` | Task 2.4: Implement FM API integrations. |
| `exam_skill` | Skill 2.4.2: Develop real-time AI interaction systems to provide immediate feedback from FM (for example, by using Amazon Bedrock streaming APIs for incremental response delivery, WebSockets or server-sent events to generate text in real time, API Gateway to implement chunked transfer encoding). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order014 |
| `accelerated_day` | Day 3 |
| `topic` | Streaming responses, WebSockets, and server-sent events |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Causal; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | api-gateway-chunked-transfer |
| `raw_source` | 2026-06-30T051954Z-openai-gpt-4.1-day-03-order014.md item 1 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051954Z |
| `raw_run_id` | order014 |

Stem:

A development team is building a real-time chat application powered by a generative AI model. Users expect to see message responses appear incrementally as the FM generates text. The current API Gateway HTTP API sends full responses only after the Lambda has completed execution. What configuration should be enabled to improve the real-time feedback in the application?

Options:

1. Enable chunked transfer encoding on the API Gateway HTTP API integration.
2. Switch the integration type to AWS_PROXY without enabling streaming on Lambda.
3. Use REST API instead of HTTP API for streaming support.
4. Increase Lambda memory allocation to speed up function execution.

Correct answer: Enable chunked transfer encoding on the API Gateway HTTP API integration.

Rationale: Chunked transfer encoding allows API Gateway to stream data to the client as it becomes available from the backend Lambda, delivering incremental FM responses.

Distractors: Switch the integration type to AWS_PROXY without enabling streaming on Lambda.: Using AWS_PROXY enables passthrough to Lambda but doesn't enable streaming; chunked transfer encoding is required for real-time delivery.; Use REST API instead of HTTP API for streaming support.: Streaming support via chunked transfer encoding is available with HTTP APIs; REST APIs do not provide this benefit for Lambda integrations.; Increase Lambda memory allocation to speed up function execution.: While this might decrease Lambda execution time, it does not enable incremental/streaming response delivery to the user.

Misconception tags: confusing integration type with streaming capability; assuming memory allocation enables streaming

Source trace:

https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-chunked-transfer.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The source confirms that enabling chunked transfer encoding on HTTP APIs causes incremental data to be sent to clients during processing.
   Source: https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-chunked-transfer.html
   Evidence span: "With chunked transfer encoding, your backend can send a response to API Gateway before it has finished processing the request. API Gateway then passes the response to the client as soon as it's available."

### P1-AIP-D3-160

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-160 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 2: Implementation and Integration |
| `exam_task` | Task 2.4: Implement FM API integrations. |
| `exam_skill` | Skill 2.4.2: Develop real-time AI interaction systems to provide immediate feedback from FM (for example, by using Amazon Bedrock streaming APIs for incremental response delivery, WebSockets or server-sent events to generate text in real time, API Gateway to implement chunked transfer encoding). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order014 |
| `accelerated_day` | Day 3 |
| `topic` | Streaming responses, WebSockets, and server-sent events |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Causal; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | lambda-response-streaming |
| `raw_source` | 2026-06-30T051954Z-openai-gpt-4.1-day-03-order014.md item 2 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051954Z |
| `raw_run_id` | order014 |

Stem:

You are troubleshooting a GenAI web app where users see a long delay before receiving any FM output, even when using Lambda and API Gateway HTTP APIs. You want the interface to display model output tokens as they are generated. Which configuration change will most likely resolve the issue?

Options:

1. Enable Lambda response streaming in the Lambda function configuration.
2. Decrease Lambda timeout to enforce faster responses.
3. Upgrade the API Gateway REST API to the latest version.
4. Add a VPC endpoint for Lambda to reduce network hops.

Correct answer: Enable Lambda response streaming in the Lambda function configuration.

Rationale: Enabling Lambda response streaming allows Lambda to return chunks of data as they are generated, supporting real-time incremental FM responses.

Distractors: Decrease Lambda timeout to enforce faster responses.: Lowering the timeout doesn't enable incremental responses; it may cause timeouts before data is returned.; Upgrade the API Gateway REST API to the latest version.: REST APIs do not support streaming integration; the problem is with the lack of streaming rather than API version.; Add a VPC endpoint for Lambda to reduce network hops.: VPC endpoints may reduce latency, but do not provide token-level streaming or incremental output.

Misconception tags: confusing latency with streaming; believing API version alone enables streaming

Source trace:

https://docs.aws.amazon.com/lambda/latest/dg/configuration-response-streaming.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The source shows that activating Lambda response streaming enables progressive and incremental client updates.
   Source: https://docs.aws.amazon.com/lambda/latest/dg/configuration-response-streaming.html
   Evidence span: "Lambda response streaming enables a function to progressively stream response data to clients. This reduces the time to first byte and enables incremental updates."

### P1-AIP-D3-161

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-161 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 2: Implementation and Integration |
| `exam_task` | Task 2.4: Implement FM API integrations. |
| `exam_skill` | Skill 2.4.2: Develop real-time AI interaction systems to provide immediate feedback from FM (for example, by using Amazon Bedrock streaming APIs for incremental response delivery, WebSockets or server-sent events to generate text in real time, API Gateway to implement chunked transfer encoding). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order014 |
| `accelerated_day` | Day 3 |
| `topic` | Streaming responses, WebSockets, and server-sent events |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Causal; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | api-gateway-chunked-transfer |
| `raw_source` | 2026-06-30T051954Z-openai-gpt-4.1-day-03-order014.md item 3 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051954Z |
| `raw_run_id` | order014 |

Stem:

A GenAI developer is designing a real-time document summarization tool that displays summarization results as the model produces them. Which approach will provide the best user experience for low-latency incremental response delivery?

Options:

1. Configure API Gateway HTTP API with chunked transfer encoding and integrate with a Lambda function using Lambda response streaming.
2. Deploy a traditional REST API that collects the full FM response before sending it to the client.
3. Use API Gateway with an SQS integration for buffering responses.
4. Invoke the FM in a step function and return results after all steps complete.

Correct answer: Configure API Gateway HTTP API with chunked transfer encoding and integrate with a Lambda function using Lambda response streaming.

Rationale: Combining chunked transfer encoding and Lambda response streaming allows clients to receive summarization data progressively as it is generated.

Distractors: Deploy a traditional REST API that collects the full FM response before sending it to the client.: REST APIs buffer output and do not deliver incremental results; users see results only at the end.; Use API Gateway with an SQS integration for buffering responses.: SQS is intended for asynchronous processing, not real-time streaming; it increases latency.; Invoke the FM in a step function and return results after all steps complete.: This approach returns only the final output; it doesn't provide real-time, incremental updates.

Misconception tags: believing async processing gives streaming UX; confusing REST API with streaming

Source trace:

https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-chunked-transfer.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: This configuration supports progressive FM response delivery, which is cited in the source as the goal of chunked transfer encoding.
   Source: https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-chunked-transfer.html
   Evidence span: "With chunked transfer encoding... API Gateway then passes the response to the client as soon as it's available."

### P1-AIP-D3-162

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-162 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 2: Implementation and Integration |
| `exam_task` | Task 2.4: Implement FM API integrations. |
| `exam_skill` | Skill 2.4.2: Develop real-time AI interaction systems to provide immediate feedback from FM (for example, by using Amazon Bedrock streaming APIs for incremental response delivery, WebSockets or server-sent events to generate text in real time, API Gateway to implement chunked transfer encoding). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order014 |
| `accelerated_day` | Day 3 |
| `topic` | Streaming responses, WebSockets, and server-sent events |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Causal; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | lambda-response-streaming |
| `raw_source` | 2026-06-30T051954Z-openai-gpt-4.1-day-03-order014.md item 4 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051954Z |
| `raw_run_id` | order014 |

Stem:

A GenAI API team wants to reduce time-to-first-byte (TTFB) for user-facing FM responses. They already use Lambda and API Gateway HTTP API. Which configuration should be reviewed first when aiming for incremental results?

Options:

1. Review the Lambda function's response streaming configuration.
2. Switch to using API Gateway REST API instead of HTTP API.
3. Increase the connection timeout for the client.
4. Enable synchronous invocation for the Lambda function.

Correct answer: Review the Lambda function's response streaming configuration.

Rationale: Without enabling Lambda response streaming, API Gateway cannot deliver incremental results regardless of other settings.

Distractors: Switch to using API Gateway REST API instead of HTTP API.: REST APIs do not support Lambda response streaming with incremental delivery.; Increase the connection timeout for the client.: This might prevent disconnects but doesn't affect incremental delivery.; Enable synchronous invocation for the Lambda function.: Synchronous invocation is required, but alone does not stream data if Lambda response streaming is not enabled.

Misconception tags: overreliance on API Gateway type; assuming timeouts impact streaming logic

Source trace:

https://docs.aws.amazon.com/lambda/latest/dg/configuration-response-streaming.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Enabling Lambda response streaming is necessary for progressive, low-TTFB delivery, as established by the source.
   Source: https://docs.aws.amazon.com/lambda/latest/dg/configuration-response-streaming.html
   Evidence span: "Lambda response streaming enables a function to progressively stream response data to clients."

### P1-AIP-D3-163

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-163 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 2: Implementation and Integration |
| `exam_task` | Task 2.4: Implement FM API integrations. |
| `exam_skill` | Skill 2.4.2: Develop real-time AI interaction systems to provide immediate feedback from FM (for example, by using Amazon Bedrock streaming APIs for incremental response delivery, WebSockets or server-sent events to generate text in real time, API Gateway to implement chunked transfer encoding). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order014 |
| `accelerated_day` | Day 3 |
| `topic` | Streaming responses, WebSockets, and server-sent events |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Causal; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | api-gateway-chunked-transfer |
| `raw_source` | 2026-06-30T051954Z-openai-gpt-4.1-day-03-order014.md item 5 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051954Z |
| `raw_run_id` | order014 |

Stem:

A generative AI service provides users with real-time updates as model output is generated. The team uses API Gateway HTTP API integrated with a Lambda function but notices that the clients only see the response after Lambda finishes execution. Which combination of changes is required to enable real-time updates?

Options:

1. Enable chunked transfer encoding on API Gateway and Lambda response streaming on the Lambda function.
2. Add an EventBridge trigger to the Lambda function and increase the client polling rate.
3. Switch to using REST API and increase the payload size limit.
4. Reduce the Lambda function's execution memory for quicker cold starts.

Correct answer: Enable chunked transfer encoding on API Gateway and Lambda response streaming on the Lambda function.

Rationale: Both chunked transfer encoding in API Gateway and Lambda response streaming must be enabled to pass data incrementally to the client.

Distractors: Add an EventBridge trigger to the Lambda function and increase the client polling rate.: EventBridge triggers and client polling do not provide true streaming; these only provide periodic batch updates.; Switch to using REST API and increase the payload size limit.: REST APIs do not enable incremental server push; payload size limit does not affect real-time streaming.; Reduce the Lambda function's execution memory for quicker cold starts.: Execution memory only affects Lambda start-up time and not message streaming.

Misconception tags: selecting size limits instead of streaming features; confusing triggers with real-time streaming

Source trace:

https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-chunked-transfer.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The source confirms both configurations are needed together to enable full end-to-end streaming from Lambda through API Gateway.
   Source: https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-chunked-transfer.html
   Evidence span: "To stream responses to clients, both Lambda's response streaming and API Gateway's chunked transfer encoding must be enabled."

### P1-AIP-D3-164

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-164 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 2: Implementation and Integration |
| `exam_task` | Task 2.4: Implement FM API integrations. |
| `exam_skill` | Skill 2.4.2: Develop real-time AI interaction systems to provide immediate feedback from FM (for example, by using Amazon Bedrock streaming APIs for incremental response delivery, WebSockets or server-sent events to generate text in real time, API Gateway to implement chunked transfer encoding). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order014 |
| `accelerated_day` | Day 3 |
| `topic` | Streaming responses, WebSockets, and server-sent events |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Causal; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order014-local-artifact |
| `raw_source` | 2026-06-30T051954Z-openai-gpt-4.1-day-03-order014.md item 6 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051954Z |
| `raw_run_id` | order014 |

Stem:

An AI developer is asked to build a web client that receives incremental updates directly as a generative model processes a prompt. Which protocol should be implemented in the client to maintain a persistent, two-way connection for full-duplex communication?

Options:

1. WebSockets
2. HTTP long polling
3. Server-Sent Events (SSE)
4. Standard HTTPS with REST API

Correct answer: WebSockets

Rationale: WebSockets provide persistent, full-duplex channels, enabling simultaneous send/receive for real-time, bidirectional streaming.

Distractors: HTTP long polling: Long polling simulates streaming but reconstructs the channel after each delivery and is not fully bidirectional.; Server-Sent Events (SSE): SSE supports streaming but only for server-to-client (one-way) updates, not full-duplex.; Standard HTTPS with REST API: REST APIs support request-response but do not provide persistent connections or stateful two-way streaming.

Misconception tags: confusing bidirectional with server-push; thinking REST can stream incrementally

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order014-streaming-websockets-server-sent-events.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The source explicitly outlines WebSockets as the protocol for persistent, bidirectional streaming.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order014-streaming-websockets-server-sent-events.md
   Evidence span: "WebSockets enable persistent, full-duplex communication channels that allow both client and server to send messages independently at any time."

### P1-AIP-D3-165

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-165 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 2: Implementation and Integration |
| `exam_task` | Task 2.4: Implement FM API integrations. |
| `exam_skill` | Skill 2.4.2: Develop real-time AI interaction systems to provide immediate feedback from FM (for example, by using Amazon Bedrock streaming APIs for incremental response delivery, WebSockets or server-sent events to generate text in real time, API Gateway to implement chunked transfer encoding). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order014 |
| `accelerated_day` | Day 3 |
| `topic` | Streaming responses, WebSockets, and server-sent events |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Causal; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order014-local-artifact |
| `raw_source` | 2026-06-30T051954Z-openai-gpt-4.1-day-03-order014.md item 7 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051954Z |
| `raw_run_id` | order014 |

Stem:

A product team is evaluating patterns to provide live updates from a generating FM to a browser-based dashboard. The communication should allow the server to push new tokens to the client as soon as they are available. The client can live without sending data back to the server post-request. Which approach is most suitable?

Options:

1. Use Server-Sent Events (SSE) to stream server updates to the client.
2. Implement WebSocket connections for both server and client communication.
3. Rely on HTTP polling at short intervals.
4. Batch all FM outputs and deliver upon completion to the client.

Correct answer: Use Server-Sent Events (SSE) to stream server updates to the client.

Rationale: SSE efficiently delivers server-originated, push-only, real-time updates to the client—ideal for FM token streaming without client-to-server transmission.

Distractors: Implement WebSocket connections for both server and client communication.: WebSockets provide two-way communication, which is unnecessary if the client does not send data post-request, adding complexity.; Rely on HTTP polling at short intervals.: Polling increases server load and yields higher latency compared to streaming options.; Batch all FM outputs and deliver upon completion to the client.: Batching doesn't allow real-time updates as tokens become available.

Misconception tags: selecting unnecessary full-duplex solutions; confusing polling with real-time streaming

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order014-streaming-websockets-server-sent-events.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The source identifies SSE as the best fit for server-push streaming scenarios lacking client push requirements.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order014-streaming-websockets-server-sent-events.md
   Evidence span: "SSE is ideal for server-to-client real-time event streaming when bidirectional communication isn't needed."

### P1-AIP-D3-166

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-166 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 2: Implementation and Integration |
| `exam_task` | Task 2.4: Implement FM API integrations. |
| `exam_skill` | Skill 2.4.2: Develop real-time AI interaction systems to provide immediate feedback from FM (for example, by using Amazon Bedrock streaming APIs for incremental response delivery, WebSockets or server-sent events to generate text in real time, API Gateway to implement chunked transfer encoding). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order014 |
| `accelerated_day` | Day 3 |
| `topic` | Streaming responses, WebSockets, and server-sent events |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Causal; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | api-gateway-chunked-transfer |
| `raw_source` | 2026-06-30T051954Z-openai-gpt-4.1-day-03-order014.md item 8 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051954Z |
| `raw_run_id` | order014 |

Stem:

A SaaS platform needs to deliver generative AI completions to thousands of web clients with minimal latency as text is generated. The team prefers the server to initiate the data transmission, with clients receiving chunks in real time. Which factor must be considered when using chunked transfer encoding with API Gateway HTTP APIs?

Options:

1. Chunked transfer encoding delivers incremental responses to connected HTTP clients and may require clients to handle partial JSON fragments until completion.
2. API Gateway REST APIs provide built-in chunked transfer encoding for Lambda integrations.
3. Chunked transfer encoding guarantees delivery of all chunks even if a client disconnects early.
4. Chunked transfer encoding requires all responses to be transformed into string literals on the server.

Correct answer: Chunked transfer encoding delivers incremental responses to connected HTTP clients and may require clients to handle partial JSON fragments until completion.

Rationale: API Gateway HTTP API's chunked transfer encoding streams partial responses; clients might see incomplete JSON until the stream ends.

Distractors: API Gateway REST APIs provide built-in chunked transfer encoding for Lambda integrations.: Only HTTP APIs—not REST APIs—support chunked transfer encoding for Lambda streaming.; Chunked transfer encoding guarantees delivery of all chunks even if a client disconnects early.: If a client disconnects, remaining chunks are lost; delivery is not guaranteed.; Chunked transfer encoding requires all responses to be transformed into string literals on the server.: Chunked responses just need to be serializable to bytes; they do not force string-representation of all responses.

Misconception tags: assuming REST APIs support chunked transfer encoding; assuming guaranteed delivery in streaming

Source trace:

https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-chunked-transfer.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The source confirms that chunked transfer encoding streams incomplete fragments and requires special client handling.
   Source: https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-chunked-transfer.html
   Evidence span: "Clients may receive incomplete JSON responses until all chunks are received and combined."

### P1-AIP-D3-167

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-167 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 2: Implementation and Integration |
| `exam_task` | Task 2.4: Implement FM API integrations. |
| `exam_skill` | Skill 2.4.2: Develop real-time AI interaction systems to provide immediate feedback from FM (for example, by using Amazon Bedrock streaming APIs for incremental response delivery, WebSockets or server-sent events to generate text in real time, API Gateway to implement chunked transfer encoding). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order014 |
| `accelerated_day` | Day 3 |
| `topic` | Streaming responses, WebSockets, and server-sent events |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Causal; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | compare |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order014-local-artifact |
| `raw_source` | 2026-06-30T051954Z-openai-gpt-4.1-day-03-order014.md item 9 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051954Z |
| `raw_run_id` | order014 |

Stem:

A GenAI developer needs to choose between Server-Sent Events (SSE) and WebSockets to deliver FM tokens to web clients in real time. Which of the following scenarios justifies using WebSockets over SSE for incremental FM delivery?

Options:

1. If the client must also send messages to the server after initial connection is established.
2. If only the server needs to push data to multiple clients at once with no reply required.
3. If strict message order is unnecessary and delivery can be occasional.
4. If a stateless request/response architecture is sufficient.

Correct answer: If the client must also send messages to the server after initial connection is established.

Rationale: WebSockets enable two-way communication, which is necessary when clients need to send data to servers as well as receive.

Distractors: If only the server needs to push data to multiple clients at once with no reply required.: SSE is sufficient and simpler for one-way server-to-client streaming.; If strict message order is unnecessary and delivery can be occasional.: Neither SSE nor WebSockets is needed if real-time guarantees aren't required.; If a stateless request/response architecture is sufficient.: Standard HTTP is appropriate instead of stateful streaming.

Misconception tags: misjudging duplex requirements; defaulting to WebSockets for all streaming

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order014-streaming-websockets-server-sent-events.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Source clearly states WebSockets are justified for bidirectional needs—i.e., client-initiated server messaging after initial connect.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order014-streaming-websockets-server-sent-events.md
   Evidence span: "Choose WebSockets if your application needs full-duplex (bidirectional) communication; prefer SSE if only server-to-client messages are needed."

### P1-AIP-D3-168

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-168 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 2: Implementation and Integration |
| `exam_task` | Task 2.4: Implement FM API integrations. |
| `exam_skill` | Skill 2.4.2: Develop real-time AI interaction systems to provide immediate feedback from FM (for example, by using Amazon Bedrock streaming APIs for incremental response delivery, WebSockets or server-sent events to generate text in real time, API Gateway to implement chunked transfer encoding). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order014 |
| `accelerated_day` | Day 3 |
| `topic` | Streaming responses, WebSockets, and server-sent events |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Causal; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | api-gateway-chunked-transfer |
| `raw_source` | 2026-06-30T051954Z-openai-gpt-4.1-day-03-order014.md item 10 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051954Z |
| `raw_run_id` | order014 |

Stem:

A support engineer is investigating why a client receives an incomplete JSON payload during an FM streaming session over HTTP API. Which factor is most likely at play?

Options:

1. Streaming with chunked transfer encoding delivers partial data as chunks, so clients may see incomplete JSON until the full stream is complete.
2. The Lambda function memory allocation is too low for the response body.
3. REST APIs buffer outputs, never exposing incomplete responses.
4. WebSocket protocol always ensures JSON messages are atomically delivered.

Correct answer: Streaming with chunked transfer encoding delivers partial data as chunks, so clients may see incomplete JSON until the full stream is complete.

Rationale: Chunked transfer sends output in sequential pieces, so the total message is not formed into valid JSON until all chunks arrive.

Distractors: The Lambda function memory allocation is too low for the response body.: Low memory could cause failures, but does not relate to incomplete streaming fragments.; REST APIs buffer outputs, never exposing incomplete responses.: Incomplete output fragments only occur with streaming; REST APIs do not expose partial responses.; WebSocket protocol always ensures JSON messages are atomically delivered.: WebSockets provide full-duplex but require special application logic for message boundaries—not automatically atomic delivery.

Misconception tags: confusing REST vs streaming APIs; assuming JSON is always all-or-nothing

Source trace:

https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-chunked-transfer.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The source shows chunked transfer sends part of the data as it's generated, leading to initially incomplete JSON at the client.
   Source: https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-chunked-transfer.html
   Evidence span: "Clients may receive incomplete JSON responses until all chunks are received and combined."

### P1-AIP-D3-169

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-169 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 2: Implementation and Integration |
| `exam_task` | Task 2.4: Implement FM API integrations. |
| `exam_skill` | Skill 2.4.2: Develop real-time AI interaction systems to provide immediate feedback from FM (for example, by using Amazon Bedrock streaming APIs for incremental response delivery, WebSockets or server-sent events to generate text in real time, API Gateway to implement chunked transfer encoding). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order014 |
| `accelerated_day` | Day 3 |
| `topic` | Streaming responses, WebSockets, and server-sent events |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Causal; Embedded |
| `question_format` | multiple-response |
| `difficulty` | hard |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order014-local-artifact |
| `raw_source` | 2026-06-30T051954Z-openai-gpt-4.1-day-03-order014.md item 11 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051954Z |
| `raw_run_id` | order014 |

Stem:

A SaaS engineering team is optimizing a GenAI-powered real-time dashboard. They plan to migrate from standard REST API responses to streaming. Which changes should they implement to minimize both latency and coupling for server-to-client FM token delivery? (Select TWO.)

Options:

1. Implement Server-Sent Events for one-way token streaming.
2. Enable chunked transfer encoding with HTTP API Gateway.
3. Switch to API Gateway REST API with long polling.
4. Use SQS as the transport to batch token messages.
5. Adopt Lambda response streaming in backend functions.

Correct answer: Implement Server-Sent Events for one-way token streaming.; Enable chunked transfer encoding with HTTP API Gateway.

Rationale: SSE is the simplest standards-based way for server-push streaming with minimal client coupling; chunked transfer encoding with HTTP API Gateway enables incremental streaming.

Distractors: Switch to API Gateway REST API with long polling.: REST API and long polling do not provide real-time messaging and increase latency versus streaming methods.; Use SQS as the transport to batch token messages.: SQS introduces buffer latency—not immediate streaming.; Adopt Lambda response streaming in backend functions.: Lambda response streaming is effective, but alone doesn't provide streaming to clients unless the API gateway and/or client also support stream consumption.

Misconception tags: choosing async batching for real-time streaming; believing REST with polling gives low latency

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order014-streaming-websockets-server-sent-events.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Both methods are cited as recommended for low-latency, decoupled, push-based delivery from server to client.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order014-streaming-websockets-server-sent-events.md
   Evidence span: "SSE and HTTP API chunked transfer encoding are recommended for one-way, low-latency streaming."

### P1-AIP-D3-170

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-170 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 2: Implementation and Integration |
| `exam_task` | Task 2.4: Implement FM API integrations. |
| `exam_skill` | Skill 2.4.2: Develop real-time AI interaction systems to provide immediate feedback from FM (for example, by using Amazon Bedrock streaming APIs for incremental response delivery, WebSockets or server-sent events to generate text in real time, API Gateway to implement chunked transfer encoding). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day03-order014 |
| `accelerated_day` | Day 3 |
| `topic` | Streaming responses, WebSockets, and server-sent events |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Causal; Embedded |
| `question_format` | multiple-response |
| `difficulty` | hard |
| `cognitive_demand` | compare |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order014-local-artifact |
| `raw_source` | 2026-06-30T051954Z-openai-gpt-4.1-day-03-order014.md item 12 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T051954Z |
| `raw_run_id` | order014 |

Stem:

A platform team must design a scalable architecture to stream FM-generated data to mobile and web clients, ensuring the solution is cost-effective, browser-compatible, and easy to integrate. Which two mechanisms fit these constraints? (Select TWO.)

Options:

1. Server-Sent Events (SSE)
2. WebSockets via API Gateway WebSocket API
3. HTTP API chunked transfer encoding
4. SFTP file drop
5. API Gateway REST API with synchronous Lambda invocation

Correct answer: Server-Sent Events (SSE); HTTP API chunked transfer encoding

Rationale: Both SSE and HTTP API chunked transfer encoding offer streaming with wide browser support and minimal setup; WebSockets are less compatible with older browsers and require more state handling.

Distractors: WebSockets via API Gateway WebSocket API: WebSockets are powerful but complex to scale for large, multi-platform client bases; also less browser-compatible and costlier to maintain state.; SFTP file drop: SFTP is for batch and file transfer, not real-time streaming.; API Gateway REST API with synchronous Lambda invocation: REST API invocation provides batching, not progressive streaming.

Misconception tags: believing WebSockets are always the best streaming fit; choosing batch options for streaming requirements

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order014-streaming-websockets-server-sent-events.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Source lists SSE and HTTP API chunked transfer encoding for scalable, browser-friendly, client streaming.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order014-streaming-websockets-server-sent-events.md
   Evidence span: "SSE and HTTP API chunked transfer encoding are broadly compatible with browsers, easy to implement, and cost-effective for most use-cases."

### P1-AIP-D3-171

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-171 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.3: Implement data validation and processing pipelines for FM consumption. |
| `exam_skill` | Skill 1.3.3: Format input data for FM inference according to model-specific requirements (for example, by using JSON formatting for Amazon Bedrock API requests, structured data preparation for SageMaker AI endpoints, conversation formatting for dialog-based applications). |
| `secondary_exam_skills` | Skill 2.5.1: Create FM API interfaces to address the specific requirements of GenAI workloads (for example, by using API Gateway to handle streaming responses, token limit management, retry strategies to handle model timeouts).; Skill 5.2.1: Resolve content handling issues to ensure that necessary information is processed completely in FM interactions (for example, by using context window overflow diagnostics, dynamic chunking strategies, prompt design optimization, truncation-related error analysis). |
| `learning_unit` | Day03-order015 |
| `accelerated_day` | Day 3 |
| `topic` | Token limits, request validation, and response handling |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Declarative; Procedural; Causal |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | implement |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | bedrock-conversation |
| `raw_source` | 2026-06-30T052035Z-openai-gpt-4.1-day-03-order015.md item 7 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T052035Z |
| `raw_run_id` | order015 |

Stem:

A workload using Bedrock's conversation API occasionally throws validation errors when switching from single-message to conversation mode. Which step is required for consistent operation across both modes?

Options:

1. Format each conversation turn as a separate JSON object in the request payload.
2. Set the 'conversation' flag to false to toggle back to stateless requests.
3. Increase model maximum token parameter for conversation mode.
4. Move prompt truncation logic to the post-processing step.

Correct answer: Format each conversation turn as a separate JSON object in the request payload.

Rationale: Bedrock conversation API requires each turn to be a distinct, structured object; this fixes common validation failures.

Distractors: Set the 'conversation' flag to false to toggle back to stateless requests.: Turning off conversation mode defeats the goal; it avoids the actual requirement.; Increase model maximum token parameter for conversation mode.: The limit is set by the model and cannot be increased for conversation mode.; Move prompt truncation logic to the post-processing step.: Truncation should occur before request submission, not after FM response.

Misconception tags: Payload structure; Request/response confusion

Source trace:

https://docs.aws.amazon.com/bedrock/latest/userguide/conversation.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: This is based on the Bedrock documentation's requirements for conversation payloads.
   Source: https://docs.aws.amazon.com/bedrock/latest/userguide/conversation.html
   Evidence span: Each message in the conversation history must be formatted as a separate object.

### P1-AIP-D3-172

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-172 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 2: Implementation and Integration |
| `exam_task` | Task 2.4: Implement FM API integrations. |
| `exam_skill` | Skill 2.4.3: Create resilient FM systems to ensure reliable operations (for example, by using the AWS SDK for exponential backoff, API Gateway to manage rate limiting, fallback mechanisms for graceful degradation, AWS X-Ray to provide observability across service boundaries). |
| `secondary_exam_skills` | Skill 2.5.1: Create FM API interfaces to address the specific requirements of GenAI workloads (for example, by using API Gateway to handle streaming responses, token limit management, retry strategies to handle model timeouts). |
| `learning_unit` | Day03-order016 |
| `accelerated_day` | Day 3 |
| `topic` | Retries, exponential backoff, rate limiting, and timeouts |
| `knowledge_category` | Skill; Knowledge |
| `knowledge_type` | Procedural; Causal; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | optimize |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | aws-retry-behavior |
| `raw_source` | 2026-06-30T052118Z-openai-gpt-4.1-day-03-order016.md item 1 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T052118Z |
| `raw_run_id` | order016 |

Stem:

A generative AI application built on AWS frequently encounters transient 5xx errors from a foundation model API integration. The solution currently retries calls without any delay. What is the best next step to increase success rates and avoid overloading upstream services?

Options:

1. Implement exponential backoff between retries to space requests appropriately.
2. Double the number of parallel requests to increase total throughput.
3. Switch to a round-robin DNS approach for endpoint selection.
4. Decrease the SDK retry count to minimize repeated requests.

Correct answer: Implement exponential backoff between retries to space requests appropriately.

Rationale: Exponential backoff ensures that retries do not occur in rapid succession, which both increases the chance of recovery from transient faults and helps avoid overwhelming upstream dependencies.

Distractors: Double the number of parallel requests to increase total throughput.: Sending more parallel requests in the face of 5xx errors increases load on unhealthy infrastructure, worsening the situation.; Switch to a round-robin DNS approach for endpoint selection.: Round-robin DNS has no effect unless multiple endpoints are available and healthy; it doesn’t address transient error retry logic.; Decrease the SDK retry count to minimize repeated requests.: Reducing retries might lower system pressure but does not improve recovery or overall reliability.

Misconception tags: retry logic; SDK configuration; overloading

Source trace:

https://docs.aws.amazon.com/sdkref/latest/guide/feature-retry-behavior.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The SDK documentation specifies exponential backoff as the recommended retry strategy to mitigate transient errors without overloading services.
   Source: https://docs.aws.amazon.com/sdkref/latest/guide/feature-retry-behavior.html
   Evidence span: Exponential backoff increases the waiting time exponentially with each attempt.

### P1-AIP-D3-173

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-173 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 2: Implementation and Integration |
| `exam_task` | Task 2.4: Implement FM API integrations. |
| `exam_skill` | Skill 2.4.3: Create resilient FM systems to ensure reliable operations (for example, by using the AWS SDK for exponential backoff, API Gateway to manage rate limiting, fallback mechanisms for graceful degradation, AWS X-Ray to provide observability across service boundaries). |
| `secondary_exam_skills` | Skill 2.5.1: Create FM API interfaces to address the specific requirements of GenAI workloads (for example, by using API Gateway to handle streaming responses, token limit management, retry strategies to handle model timeouts). |
| `learning_unit` | Day03-order016 |
| `accelerated_day` | Day 3 |
| `topic` | Retries, exponential backoff, rate limiting, and timeouts |
| `knowledge_category` | Skill; Knowledge |
| `knowledge_type` | Procedural; Causal; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | api-gateway-throttling |
| `raw_source` | 2026-06-30T052118Z-openai-gpt-4.1-day-03-order016.md item 2 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T052118Z |
| `raw_run_id` | order016 |

Stem:

Your GenAI workload using API Gateway begins returning HTTP 429 errors for some users during high-traffic periods. What is the most direct architectural change to reliably reduce these errors?

Options:

1. Adjust throttling settings in API Gateway to match expected peak load.
2. Switch to a Lambda authorizer to filter traffic before invocation.
3. Move the GenAI API to an EC2 instance with higher compute.
4. Add a load balancer in front of the API Gateway to distribute requests.

Correct answer: Adjust throttling settings in API Gateway to match expected peak load.

Rationale: API Gateway throttling controls directly determine how many requests per second are allowed; mismatched settings will lead to throttling and 429 errors.

Distractors: Switch to a Lambda authorizer to filter traffic before invocation.: A Lambda authorizer controls access but does not affect API-level rate limits or reduce throttling errors.; Move the GenAI API to an EC2 instance with higher compute.: Upgrading compute increases backend capacity, not API Gateway's rate limits.; Add a load balancer in front of the API Gateway to distribute requests.: A load balancer does not increase the throughput limit of the API Gateway itself.

Misconception tags: rate limiting; throttling; API Gateway config

Source trace:

https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The documentation clearly states that API Gateway throttles at configured rates, and correct settings are required to meet traffic demands.
   Source: https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html
   Evidence span: "API Gateway throttles requests to prevent your backend from being overwhelmed."

### P1-AIP-D3-174

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-174 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 2: Implementation and Integration |
| `exam_task` | Task 2.4: Implement FM API integrations. |
| `exam_skill` | Skill 2.4.3: Create resilient FM systems to ensure reliable operations (for example, by using the AWS SDK for exponential backoff, API Gateway to manage rate limiting, fallback mechanisms for graceful degradation, AWS X-Ray to provide observability across service boundaries). |
| `secondary_exam_skills` | Skill 2.5.1: Create FM API interfaces to address the specific requirements of GenAI workloads (for example, by using API Gateway to handle streaming responses, token limit management, retry strategies to handle model timeouts). |
| `learning_unit` | Day03-order016 |
| `accelerated_day` | Day 3 |
| `topic` | Retries, exponential backoff, rate limiting, and timeouts |
| `knowledge_category` | Skill; Knowledge |
| `knowledge_type` | Procedural; Causal; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | aws-retry-behavior |
| `raw_source` | 2026-06-30T052118Z-openai-gpt-4.1-day-03-order016.md item 3 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T052118Z |
| `raw_run_id` | order016 |

Stem:

You are deploying a GenAI-powered recommendation engine that integrates with Amazon Bedrock via API Gateway. To handle unpredictable spikes and transient FM API timeouts, which mechanism should you include in your AWS SDK configuration?

Options:

1. Enable automatic retries with exponential backoff.
2. Disable request retries to ensure low latency.
3. Increase the API Gateway burst limit only.
4. Disable error handling logic in the client.

Correct answer: Enable automatic retries with exponential backoff.

Rationale: Automatic retries with exponential backoff handle transient errors and network timeouts in a robust way, as recommended in AWS SDK guidance.

Distractors: Disable request retries to ensure low latency.: This sacrifices reliability and doesn’t address transient errors.; Increase the API Gateway burst limit only.: Burst limits help with short spikes but don’t solve client-side transient faults or timeouts.; Disable error handling logic in the client.: Eliminating client-side error handling makes the system fragile.

Misconception tags: SDK retries; timeout mitigation; burst vs. backoff

Source trace:

https://docs.aws.amazon.com/sdkref/latest/guide/feature-retry-behavior.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Enabling automatic retries with exponential backoff in the SDK is specifically recommended to manage transient errors and API timeouts.
   Source: https://docs.aws.amazon.com/sdkref/latest/guide/feature-retry-behavior.html
   Evidence span: "The AWS SDK offers configurable automatic retry logic with exponential backoff..."

### P1-AIP-D3-175

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-175 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 2: Implementation and Integration |
| `exam_task` | Task 2.4: Implement FM API integrations. |
| `exam_skill` | Skill 2.4.3: Create resilient FM systems to ensure reliable operations (for example, by using the AWS SDK for exponential backoff, API Gateway to manage rate limiting, fallback mechanisms for graceful degradation, AWS X-Ray to provide observability across service boundaries). |
| `secondary_exam_skills` | Skill 2.5.1: Create FM API interfaces to address the specific requirements of GenAI workloads (for example, by using API Gateway to handle streaming responses, token limit management, retry strategies to handle model timeouts). |
| `learning_unit` | Day03-order016 |
| `accelerated_day` | Day 3 |
| `topic` | Retries, exponential backoff, rate limiting, and timeouts |
| `knowledge_category` | Skill; Knowledge |
| `knowledge_type` | Procedural; Causal; Conditional |
| `question_format` | multiple-response |
| `difficulty` | hard |
| `cognitive_demand` | optimize |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | api-gateway-throttling |
| `raw_source` | 2026-06-30T052118Z-openai-gpt-4.1-day-03-order016.md item 4 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T052118Z |
| `raw_run_id` | order016 |

Stem:

A conversational AI system built on AWS fails with frequent 'Rate Exceeded' errors from API Gateway during user traffic surges. Which combination of approaches can most directly address both immediate and long-term reliability? (Select TWO.)

Options:

1. Implement server-side queuing or request scheduling upstream of API Gateway.
2. Tune API Gateway's rate and burst settings based on observed workloads.
3. Increase the timeout value for downstream model inference.
4. Increase the concurrency of all backend Lambda functions.
5. Disable exponential backoff in API clients and use immediate retries.

Correct answer: Implement server-side queuing or request scheduling upstream of API Gateway.; Tune API Gateway's rate and burst settings based on observed workloads.

Rationale: Queuing or scheduling prevents request surges from overwhelming API Gateway, while tuning rate/burst settings aligns Gateway limits with observed real-world usage.

Distractors: Increase the timeout value for downstream model inference.: Longer timeouts do not solve request throttling or API Gateway's rate-exceed errors.; Increase the concurrency of all backend Lambda functions.: Boosting Lambda concurrency will not help if API Gateway is still enforcing limits higher up.; Disable exponential backoff in API clients and use immediate retries.: Removing backoff is likely to worsen throttling and rate-exceed circumstances.

Misconception tags: API Gateway limits; throttling; retry design

Source trace:

https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: API Gateway documentation recommends queueing and careful matching of rate/burst settings to handle variable loads and suppress throttling errors.
   Source: https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html
   Evidence span: "Tune rate and burst settings; consider application-layer queuing upstream..."

### P1-AIP-D3-176

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-176 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 2: Implementation and Integration |
| `exam_task` | Task 2.4: Implement FM API integrations. |
| `exam_skill` | Skill 2.4.3: Create resilient FM systems to ensure reliable operations (for example, by using the AWS SDK for exponential backoff, API Gateway to manage rate limiting, fallback mechanisms for graceful degradation, AWS X-Ray to provide observability across service boundaries). |
| `secondary_exam_skills` | Skill 2.5.1: Create FM API interfaces to address the specific requirements of GenAI workloads (for example, by using API Gateway to handle streaming responses, token limit management, retry strategies to handle model timeouts). |
| `learning_unit` | Day03-order016 |
| `accelerated_day` | Day 3 |
| `topic` | Retries, exponential backoff, rate limiting, and timeouts |
| `knowledge_category` | Skill; Knowledge |
| `knowledge_type` | Procedural; Causal; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | judge |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order016-local-artifact |
| `raw_source` | 2026-06-30T052118Z-openai-gpt-4.1-day-03-order016.md item 5 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T052118Z |
| `raw_run_id` | order016 |

Stem:

After integrating exponential backoff in your GenAI client, you notice a sharp increase in user latency during peak periods. What is the main tradeoff introduced by this retry strategy?

Options:

1. Higher reliability at the cost of increased response times.
2. Security of the API is compromised.
3. API Gateway rate limits are bypassed.
4. Inference accuracy is reduced.

Correct answer: Higher reliability at the cost of increased response times.

Rationale: Exponential backoff increases user-perceived latency in exchange for greater robustness and fewer fatal errors in transient failure scenarios.

Distractors: Security of the API is compromised.: Backoff does not impact security posture or authorization.; API Gateway rate limits are bypassed.: Exponential backoff does not circumvent API Gateway controls, just staggers client requests.; Inference accuracy is reduced.: Retries affect reliability, not the underlying model’s response quality.

Misconception tags: availability vs. latency; retry-impact-tradeoff

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order016-retries-backoff-rate-limiting-timeouts.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Increasing reliability by spacing retry attempts can result in longer total request-response cycles under failure, as described in the source.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order016-retries-backoff-rate-limiting-timeouts.md
   Evidence span: Exponential backoff increases reliability but can increase end-to-end latency.

### P1-AIP-D3-177

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-177 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 2: Implementation and Integration |
| `exam_task` | Task 2.4: Implement FM API integrations. |
| `exam_skill` | Skill 2.4.3: Create resilient FM systems to ensure reliable operations (for example, by using the AWS SDK for exponential backoff, API Gateway to manage rate limiting, fallback mechanisms for graceful degradation, AWS X-Ray to provide observability across service boundaries). |
| `secondary_exam_skills` | Skill 2.5.1: Create FM API interfaces to address the specific requirements of GenAI workloads (for example, by using API Gateway to handle streaming responses, token limit management, retry strategies to handle model timeouts). |
| `learning_unit` | Day03-order016 |
| `accelerated_day` | Day 3 |
| `topic` | Retries, exponential backoff, rate limiting, and timeouts |
| `knowledge_category` | Skill; Knowledge |
| `knowledge_type` | Procedural; Causal; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | api-gateway-throttling |
| `raw_source` | 2026-06-30T052118Z-openai-gpt-4.1-day-03-order016.md item 6 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T052118Z |
| `raw_run_id` | order016 |

Stem:

A data scientist notices that GenAI requests to a Bedrock model are being rejected with API Gateway 429 errors, even though the downstream Lambda function is rarely at full concurrency. What primary issue should be investigated?

Options:

1. Check if API Gateway rate/burst limits are lower than Lambda's processing capacity.
2. Examine whether Lambda provisioned concurrency is set too low.
3. Investigate if the Bedrock model endpoint is unhealthy.
4. Review IAM policies attached to Lambda for resource constraints.

Correct answer: Check if API Gateway rate/burst limits are lower than Lambda's processing capacity.

Rationale: If API Gateway's limits are lower than backend capacity, requests are throttled before reaching Lambda, causing 429s despite Lambda availability.

Distractors: Examine whether Lambda provisioned concurrency is set too low.: Provisioned concurrency would cause Lambda-side throttling, but not 429s from API Gateway.; Investigate if the Bedrock model endpoint is unhealthy.: Unhealthy endpoints may cause 5xx errors, not 429 rate-limit errors.; Review IAM policies attached to Lambda for resource constraints.: IAM policies do not control API Gateway throttling or request rate.

Misconception tags: rate limiting; API Gateway vs Lambda; throttling

Source trace:

https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The documentation clarifies that throttling occurs at the gateway even if backend systems are not bottlenecked.
   Source: https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html
   Evidence span: Throttling is applied at the API Gateway level.

### P1-AIP-D3-178

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-178 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 2: Implementation and Integration |
| `exam_task` | Task 2.4: Implement FM API integrations. |
| `exam_skill` | Skill 2.4.3: Create resilient FM systems to ensure reliable operations (for example, by using the AWS SDK for exponential backoff, API Gateway to manage rate limiting, fallback mechanisms for graceful degradation, AWS X-Ray to provide observability across service boundaries). |
| `secondary_exam_skills` | Skill 2.5.1: Create FM API interfaces to address the specific requirements of GenAI workloads (for example, by using API Gateway to handle streaming responses, token limit management, retry strategies to handle model timeouts). |
| `learning_unit` | Day03-order016 |
| `accelerated_day` | Day 3 |
| `topic` | Retries, exponential backoff, rate limiting, and timeouts |
| `knowledge_category` | Skill; Knowledge |
| `knowledge_type` | Procedural; Causal; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | optimize |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | aws-retry-behavior |
| `raw_source` | 2026-06-30T052118Z-openai-gpt-4.1-day-03-order016.md item 7 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T052118Z |
| `raw_run_id` | order016 |

Stem:

Your development team implements a fixed retry interval of 100ms for API calls to Foundation Model endpoints. They've noticed that errors sometimes cluster, and overall throughput suffers. What AWS SDK retry strategy strongly mitigates this problem?

Options:

1. Switch to exponential backoff with jitter.
2. Decrease the fixed retry interval to 50ms.
3. Add additional default retries without changing delay logic.
4. Use round-robin selection for different Foundation Model endpoints.

Correct answer: Switch to exponential backoff with jitter.

Rationale: Exponential backoff (with optional jitter) prevents retry storms and error clustering by spreading out retry attempts randomly over increasing intervals.

Distractors: Decrease the fixed retry interval to 50ms.: A shorter fixed retry interval increases the risk of repeated collisions and overload.; Add additional default retries without changing delay logic.: More retries without smarter backoff compounds the issue.; Use round-robin selection for different Foundation Model endpoints.: This is only effective if there are multiple endpoints and does not address retry timing.

Misconception tags: backoff algorithm; fixed interval

Source trace:

https://docs.aws.amazon.com/sdkref/latest/guide/feature-retry-behavior.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The SDK documentation posts exponential backoff with jitter as optimal to control both average load and collision in distributed retry events.
   Source: https://docs.aws.amazon.com/sdkref/latest/guide/feature-retry-behavior.html
   Evidence span: "AWS SDKs implement exponential backoff and recommend jitter to reduce collision."

### P1-AIP-D3-179

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-179 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 2: Implementation and Integration |
| `exam_task` | Task 2.4: Implement FM API integrations. |
| `exam_skill` | Skill 2.4.3: Create resilient FM systems to ensure reliable operations (for example, by using the AWS SDK for exponential backoff, API Gateway to manage rate limiting, fallback mechanisms for graceful degradation, AWS X-Ray to provide observability across service boundaries). |
| `secondary_exam_skills` | Skill 2.5.1: Create FM API interfaces to address the specific requirements of GenAI workloads (for example, by using API Gateway to handle streaming responses, token limit management, retry strategies to handle model timeouts). |
| `learning_unit` | Day03-order016 |
| `accelerated_day` | Day 3 |
| `topic` | Retries, exponential backoff, rate limiting, and timeouts |
| `knowledge_category` | Skill; Knowledge |
| `knowledge_type` | Procedural; Causal; Conditional |
| `question_format` | multiple-response |
| `difficulty` | hard |
| `cognitive_demand` | optimize |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order016-local-artifact |
| `raw_source` | 2026-06-30T052118Z-openai-gpt-4.1-day-03-order016.md item 8 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T052118Z |
| `raw_run_id` | order016 |

Stem:

A large-scale AI workload faces unpredictable timeouts due to transient model inference slowdowns. Which set of changes will provide the most balanced resilience with minimal unnecessary backend load? (Select TWO.)

Options:

1. Implement exponential backoff in client-side retry logic.
2. Monitor error patterns and adjust maximum retry attempts.
3. Set API Gateway rate limits to the absolute maximum allowed.
4. Increase static retry delay to a fixed high value for all errors.
5. Configure clients to not retry upon timeout errors.

Correct answer: Implement exponential backoff in client-side retry logic.; Monitor error patterns and adjust maximum retry attempts.

Rationale: Exponential backoff avoids retry storms; monitoring and tuning retries ensures balance between resilience and backend load.

Distractors: Set API Gateway rate limits to the absolute maximum allowed.: Setting rate limits high risks backend overload and does not address resilience.; Increase static retry delay to a fixed high value for all errors.: High static delay adds latency without adapting to error conditions.; Configure clients to not retry upon timeout errors.: No retries drops resilience to transient outage.

Misconception tags: retry configuration; latency vs. resilience

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order016-retries-backoff-rate-limiting-timeouts.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Both solutions are directly described as best practice in the local source for managing transient timeouts and balancing load.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order016-retries-backoff-rate-limiting-timeouts.md
   Evidence span: Use exponential backoff and fine-tune retry strategies based on workload analysis.

### P1-AIP-D3-180

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-180 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 2: Implementation and Integration |
| `exam_task` | Task 2.4: Implement FM API integrations. |
| `exam_skill` | Skill 2.4.3: Create resilient FM systems to ensure reliable operations (for example, by using the AWS SDK for exponential backoff, API Gateway to manage rate limiting, fallback mechanisms for graceful degradation, AWS X-Ray to provide observability across service boundaries). |
| `secondary_exam_skills` | Skill 2.5.1: Create FM API interfaces to address the specific requirements of GenAI workloads (for example, by using API Gateway to handle streaming responses, token limit management, retry strategies to handle model timeouts). |
| `learning_unit` | Day03-order016 |
| `accelerated_day` | Day 3 |
| `topic` | Retries, exponential backoff, rate limiting, and timeouts |
| `knowledge_category` | Skill; Knowledge |
| `knowledge_type` | Procedural; Causal; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order016-local-artifact |
| `raw_source` | 2026-06-30T052118Z-openai-gpt-4.1-day-03-order016.md item 9 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T052118Z |
| `raw_run_id` | order016 |

Stem:

A GenAI solution uses API Gateway in front of a Bedrock-powered inference service. After deploying a new client application, you're seeing an increase in 429 (Too Many Requests) errors during model calls even though peak throughput hasn't increased. Which client misconfiguration is the most likely root cause?

Options:

1. The client is retrying failed requests without exponential backoff.
2. The API Gateway endpoint is misconfigured for HTTPS.
3. IAM credentials used by the client are expired.
4. The client is not specifying the required Accept header.

Correct answer: The client is retrying failed requests without exponential backoff.

Rationale: Clients that retry rapidly without backoff can overwhelm rate limits, causing more 429 errors even under moderate steady load.

Distractors: The API Gateway endpoint is misconfigured for HTTPS.: This would cause failed requests, but not isolated throttling errors.; IAM credentials used by the client are expired.: Expired credentials result in authentication errors, not 429s.; The client is not specifying the required Accept header.: This typically yields a 406 (Not Acceptable), not 429.

Misconception tags: retry-backoff; client throttling

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order016-retries-backoff-rate-limiting-timeouts.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: This client-side anti-pattern is explicitly called out in the topic artifact as a typical root cause of unwanted 429 errors.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order016-retries-backoff-rate-limiting-timeouts.md
   Evidence span: Rapid, bursty retries from clients can create throttling errors even below theoretical limits.

### P1-AIP-D3-181

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-181 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 2: Implementation and Integration |
| `exam_task` | Task 2.4: Implement FM API integrations. |
| `exam_skill` | Skill 2.4.3: Create resilient FM systems to ensure reliable operations (for example, by using the AWS SDK for exponential backoff, API Gateway to manage rate limiting, fallback mechanisms for graceful degradation, AWS X-Ray to provide observability across service boundaries). |
| `secondary_exam_skills` | Skill 2.5.1: Create FM API interfaces to address the specific requirements of GenAI workloads (for example, by using API Gateway to handle streaming responses, token limit management, retry strategies to handle model timeouts). |
| `learning_unit` | Day03-order016 |
| `accelerated_day` | Day 3 |
| `topic` | Retries, exponential backoff, rate limiting, and timeouts |
| `knowledge_category` | Skill; Knowledge |
| `knowledge_type` | Procedural; Causal; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order016-local-artifact |
| `raw_source` | 2026-06-30T052118Z-openai-gpt-4.1-day-03-order016.md item 10 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T052118Z |
| `raw_run_id` | order016 |

Stem:

You are tasked with reducing model inference latency spikes in your GenAI API. You already use exponential backoff and have tuned Gateway limits, but users still see random slowdowns. What is the next best step?

Options:

1. Instrument API Gateway and client with end-to-end timing and trace logging.
2. Disable exponential backoff retries to reduce duplicated calls.
3. Switch all request-response interactions from synchronous to asynchronous.
4. Ignore intermittent latency, as transient fluctuations are expected.

Correct answer: Instrument API Gateway and client with end-to-end timing and trace logging.

Rationale: Adding end-to-end observability helps pinpoint specific sources and timing of latency spikes, enabling focused remediation.

Distractors: Disable exponential backoff retries to reduce duplicated calls.: This would lower overall resilience and doesn’t address source of spikes.; Switch all request-response interactions from synchronous to asynchronous.: This could help but is a large architectural change not justified by symptoms described.; Ignore intermittent latency, as transient fluctuations are expected.: Ignoring user-impacting spikes isn’t appropriate for production reliability.

Misconception tags: root cause analysis; instrumentation vs. guessing

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order016-retries-backoff-rate-limiting-timeouts.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: This remediation is specifically described in the source as the next step when basic tuning can't resolve performance issues.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order016-retries-backoff-rate-limiting-timeouts.md
   Evidence span: Trace logging and detailed timing are required to locate latency sources.

### P1-AIP-D3-182

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-182 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 2: Implementation and Integration |
| `exam_task` | Task 2.4: Implement FM API integrations. |
| `exam_skill` | Skill 2.4.3: Create resilient FM systems to ensure reliable operations (for example, by using the AWS SDK for exponential backoff, API Gateway to manage rate limiting, fallback mechanisms for graceful degradation, AWS X-Ray to provide observability across service boundaries). |
| `secondary_exam_skills` | Skill 2.5.1: Create FM API interfaces to address the specific requirements of GenAI workloads (for example, by using API Gateway to handle streaming responses, token limit management, retry strategies to handle model timeouts). |
| `learning_unit` | Day03-order016 |
| `accelerated_day` | Day 3 |
| `topic` | Retries, exponential backoff, rate limiting, and timeouts |
| `knowledge_category` | Skill; Knowledge |
| `knowledge_type` | Procedural; Causal; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | judge |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | aws-retry-behavior |
| `raw_source` | 2026-06-30T052118Z-openai-gpt-4.1-day-03-order016.md item 11 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T052118Z |
| `raw_run_id` | order016 |

Stem:

A team implements a retry strategy for GenAI API calls and configures the maximum retry attempts to 20 for each request. As load increases, the backend experiences resource exhaustion. What is the main risk of this configuration?

Options:

1. Unreasonably high retry count can cause cascading retries under stress, worsening overload.
2. Reducing retry count below five leads to loss of all resilience.
3. Retry settings are required to be equal across all AWS SDKs.
4. Model accuracy is affected by the retry count.

Correct answer: Unreasonably high retry count can cause cascading retries under stress, worsening overload.

Rationale: Very high retry limits can balloon load during outages, aggravating backend failures, as described in AWS SDK best practices.

Distractors: Reducing retry count below five leads to loss of all resilience.: Resilience is a spectrum and context-specific; very high or low values are both risky.; Retry settings are required to be equal across all AWS SDKs.: This is not enforced and has no technical basis.; Model accuracy is affected by the retry count.: Retry count affects system reliability, not model inference accuracy.

Misconception tags: retry storm; SDK configuration; backpressure

Source trace:

https://docs.aws.amazon.com/sdkref/latest/guide/feature-retry-behavior.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: AWS recommends that retry counts be balanced to avoid system overload during periods of stress, as documented.
   Source: https://docs.aws.amazon.com/sdkref/latest/guide/feature-retry-behavior.html
   Evidence span: "Excessive retries under high load can cause resource exhaustion."

### P1-AIP-D3-183

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-183 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 2: Implementation and Integration |
| `exam_task` | Task 2.4: Implement FM API integrations. |
| `exam_skill` | Skill 2.4.3: Create resilient FM systems to ensure reliable operations (for example, by using the AWS SDK for exponential backoff, API Gateway to manage rate limiting, fallback mechanisms for graceful degradation, AWS X-Ray to provide observability across service boundaries). |
| `secondary_exam_skills` | Skill 2.5.1: Create FM API interfaces to address the specific requirements of GenAI workloads (for example, by using API Gateway to handle streaming responses, token limit management, retry strategies to handle model timeouts). |
| `learning_unit` | Day03-order016 |
| `accelerated_day` | Day 3 |
| `topic` | Retries, exponential backoff, rate limiting, and timeouts |
| `knowledge_category` | Skill; Knowledge |
| `knowledge_type` | Procedural; Causal; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order016-local-artifact |
| `raw_source` | 2026-06-30T052118Z-openai-gpt-4.1-day-03-order016.md item 12 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T052118Z |
| `raw_run_id` | order016 |

Stem:

A GenAI API client receives consistent timeouts after three retry attempts when calling a Bedrock-powered inference endpoint behind API Gateway. The API Gateway burst and rate limits are sufficient. What is the most likely remaining cause?

Options:

1. The backend model endpoint or Lambda function is underprovisioned or experiencing high latency.
2. API Gateway has too low a quota for the expected traffic.
3. The SDK retry configuration uses exponential backoff.
4. The client is not passing required custom headers.

Correct answer: The backend model endpoint or Lambda function is underprovisioned or experiencing high latency.

Rationale: If Gateway limits are adequate and timeouts still occur, the most probable cause is delay in backend processing, requiring further capacity analysis.

Distractors: API Gateway has too low a quota for the expected traffic.: The scenario pre-states these limits are sufficient.; The SDK retry configuration uses exponential backoff.: Exponential backoff is intended to help, not hurt, reliability.; The client is not passing required custom headers.: Missing headers would typically result in 4xx errors, not timeouts.

Misconception tags: backend bottleneck vs. rate limiting

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order016-retries-backoff-rate-limiting-timeouts.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The evidence from the scenario and source points directly to backend slowdowns when retries/timeouts persist despite correct Gateway settings.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order016-retries-backoff-rate-limiting-timeouts.md
   Evidence span: Timeouts with sufficient API Gateway limits suggest backend slowness.

### P1-AIP-D3-184

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-184 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 2: Implementation and Integration |
| `exam_task` | Task 2.4: Implement FM API integrations. |
| `exam_skill` | Skill 2.4.3: Create resilient FM systems to ensure reliable operations (for example, by using the AWS SDK for exponential backoff, API Gateway to manage rate limiting, fallback mechanisms for graceful degradation, AWS X-Ray to provide observability across service boundaries). |
| `secondary_exam_skills` | Skill 2.5.1: Create FM API interfaces to address the specific requirements of GenAI workloads (for example, by using API Gateway to handle streaming responses, token limit management, retry strategies to handle model timeouts). |
| `learning_unit` | Day03-order016 |
| `accelerated_day` | Day 3 |
| `topic` | Retries, exponential backoff, rate limiting, and timeouts |
| `knowledge_category` | Skill; Knowledge |
| `knowledge_type` | Procedural; Causal; Conditional |
| `question_format` | multiple-response |
| `difficulty` | hard |
| `cognitive_demand` | optimize |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order016-local-artifact |
| `raw_source` | 2026-06-30T052118Z-openai-gpt-4.1-day-03-order016.md item 13 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T052118Z |
| `raw_run_id` | order016 |

Stem:

You want to ensure resilience of your GenAI API under unpredictable load but wish to avoid unnecessary latency and resource waste. What combination of architectural best practices should you employ? (Select THREE.)

Options:

1. Tune API Gateway throttling (rate and burst) to align with back-end capacity.
2. Use exponential backoff with jitter for retries in all API clients.
3. Set strict maximum retry counts for all client libraries.
4. Disable API Gateway throttling to maximize request throughput.
5. Adjust Lambda concurrency settings to prevent downstream bottlenecks.

Correct answer: Tune API Gateway throttling (rate and burst) to align with back-end capacity.; Use exponential backoff with jitter for retries in all API clients.; Set strict maximum retry counts for all client libraries.

Rationale: These actions demonstrate proactive, balanced resilience—controlling surge behavior at the API, spacing retries, and limiting retry storms.

Distractors: Disable API Gateway throttling to maximize request throughput.: Disabling throttling exposes all downstream services to overload.; Adjust Lambda concurrency settings to prevent downstream bottlenecks.: While necessary, Lambda concurrency must be coordinated, not simply maximized, to avoid shifts in failure domains.

Misconception tags: resilience tuning; over-tuning; retry configuration

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order016-retries-backoff-rate-limiting-timeouts.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Each recommended technique is explicitly described in the artifact as essential for balancing resilience and efficiency under variable workloads.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order016-retries-backoff-rate-limiting-timeouts.md
   Evidence span: Resilience needs tuning both at the request entry points and in client retry configuration.

### P1-AIP-D3-185

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-185 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.2: Select and configure FMs. |
| `exam_skill` | Skill 1.2.3: Design resilient AI systems to ensure continuous operation during service disruptions (for example, by using AWS Step Functions circuit breaker patterns, Amazon Bedrock Cross-Region Inference for models that have limited regional availability, cross-Region model deployment, graceful degradation strategies). |
| `secondary_exam_skills` | Skill 2.4.3: Create resilient FM systems to ensure reliable operations (for example, by using the AWS SDK for exponential backoff, API Gateway to manage rate limiting, fallback mechanisms for graceful degradation, AWS X-Ray to provide observability across service boundaries). |
| `learning_unit` | Day03-order017 |
| `accelerated_day` | Day 3 |
| `topic` | Fallbacks, circuit breakers, and graceful degradation |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Causal; Strategic |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order017-local-artifact |
| `raw_source` | 2026-06-30T052157Z-openai-gpt-4.1-day-03-order017.md item 1 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T052157Z |
| `raw_run_id` | order017 |

Stem:

An AWS Generative AI application running on multiple Regions relies on a foundation model available only in a subset of regions. The workload requires high availability even if a regional outage occurs. What architecture pattern best maintains service continuity for FM inference requests?

Options:

1. Implement cross-Region failover with Bedrock Cross-Region Inference and a graceful degradation mechanism.
2. Deploy the application only in a single Region with the FM and rely on retry logic.
3. Implement a local fallback model trained on previous data using Lambda in Regions without Bedrock.
4. Route all FM inference requests to a standby secondary Region using Route 53 latency-based DNS.

Correct answer: Implement cross-Region failover with Bedrock Cross-Region Inference and a graceful degradation mechanism.

Rationale: This option ensures resilience by using Bedrock's cross-Region inference and provides graceful degradation, maintaining service even during outages in the primary Region.

Distractors: Deploy the application only in a single Region with the FM and rely on retry logic.: Retries alone do not address regional outages and do not provide resilience if the region is unavailable.; Implement a local fallback model trained on previous data using Lambda in Regions without Bedrock.: A locally-trained fallback may reduce accuracy and does not provide the intended FM inference capabilities or align with compliance for regulated workloads.; Route all FM inference requests to a standby secondary Region using Route 53 latency-based DNS.: Route 53 based DNS alone does not solve the FM's limited regional availability problem unless combined with cross-Region inference or model deployment.

Misconception tags: Overreliance on retry logic; Ignoring FM regional constraints

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order017-fallbacks-circuit-breakers-graceful-degradation.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Choosing Bedrock Cross-Region Inference allows requests to move seamlessly during regional problems, supporting high availability. Graceful degradation ensures the application can still return a result if even the secondary region fails.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order017-fallbacks-circuit-breakers-graceful-degradation.md
   Evidence span: Bedrock Cross-Region Inference and graceful degradation patterns are recommended for FMs with limited regional presence.

### P1-AIP-D3-186

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-186 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.2: Select and configure FMs. |
| `exam_skill` | Skill 1.2.3: Design resilient AI systems to ensure continuous operation during service disruptions (for example, by using AWS Step Functions circuit breaker patterns, Amazon Bedrock Cross-Region Inference for models that have limited regional availability, cross-Region model deployment, graceful degradation strategies). |
| `secondary_exam_skills` | Skill 2.4.3: Create resilient FM systems to ensure reliable operations (for example, by using the AWS SDK for exponential backoff, API Gateway to manage rate limiting, fallback mechanisms for graceful degradation, AWS X-Ray to provide observability across service boundaries). |
| `learning_unit` | Day03-order017 |
| `accelerated_day` | Day 3 |
| `topic` | Fallbacks, circuit breakers, and graceful degradation |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Causal; Strategic |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | implement |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order017-local-artifact |
| `raw_source` | 2026-06-30T052157Z-openai-gpt-4.1-day-03-order017.md item 2 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T052157Z |
| `raw_run_id` | order017 |

Stem:

A development team is designing an FM-powered chatbot for a critical application. They want to ensure that if the FM experiences service disruptions, the application can continue to respond with a useful but less capable answer. Which strategy best achieves this goal?

Options:

1. Implement a fallback workflow using Step Functions to return canned responses when FM inference fails.
2. Increase the FM API retry attempts to the maximum allowed.
3. Use exponential backoff in the retry settings.
4. Switch to a smaller FM model hosted locally for all queries.

Correct answer: Implement a fallback workflow using Step Functions to return canned responses when FM inference fails.

Rationale: A fallback mechanism allows the application to continue responding with pre-defined messages, maintaining basic functionality and graceful degradation.

Distractors: Increase the FM API retry attempts to the maximum allowed.: Excessive retries waste time and may not help during a prolonged outage, and do not provide a response if the FM remains unavailable.; Use exponential backoff in the retry settings.: Exponential backoff is useful to prevent overload but does not provide grace when the FM is down.; Switch to a smaller FM model hosted locally for all queries.: Running all queries on a smaller local model degrades normal service unnecessarily, instead of only during FM outages.

Misconception tags: Overemphasis on retries; Not distinguishing between fallback and overall model change

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order017-fallbacks-circuit-breakers-graceful-degradation.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: A Step Functions fallback flow provides a controlled, predictable response when the FM fails, ensuring continuity even under error conditions.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order017-fallbacks-circuit-breakers-graceful-degradation.md
   Evidence span: Graceful degradation can include returning template or canned responses via fallback logic during FM service disruptions.

### P1-AIP-D3-187

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-187 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.2: Select and configure FMs. |
| `exam_skill` | Skill 1.2.3: Design resilient AI systems to ensure continuous operation during service disruptions (for example, by using AWS Step Functions circuit breaker patterns, Amazon Bedrock Cross-Region Inference for models that have limited regional availability, cross-Region model deployment, graceful degradation strategies). |
| `secondary_exam_skills` | Skill 2.4.3: Create resilient FM systems to ensure reliable operations (for example, by using the AWS SDK for exponential backoff, API Gateway to manage rate limiting, fallback mechanisms for graceful degradation, AWS X-Ray to provide observability across service boundaries). |
| `learning_unit` | Day03-order017 |
| `accelerated_day` | Day 3 |
| `topic` | Fallbacks, circuit breakers, and graceful degradation |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Causal; Strategic |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | aws-retry-circuit-breaker |
| `raw_source` | 2026-06-30T052157Z-openai-gpt-4.1-day-03-order017.md item 3 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T052157Z |
| `raw_run_id` | order017 |

Stem:

An AI team is implementing a circuit breaker for their GenAI API integration. What scenario should trigger the circuit breaker to open and invoke an alternate path?

Options:

1. Repeated FM API response timeouts beyond a threshold over a sliding window.
2. A single failed request to the FM API.
3. Short bursts of high latency under the threshold.
4. Exceeding the rate limit for one second on the FM API.

Correct answer: Repeated FM API response timeouts beyond a threshold over a sliding window.

Rationale: A circuit breaker is designed to open in response to repeated failures over time, protecting the system from prolonged stress.

Distractors: A single failed request to the FM API.: A single failure may be transient and is not enough evidence for a systemic problem; circuit breakers require a pattern of failures.; Short bursts of high latency under the threshold.: These do not indicate persistent failure and should not open the circuit.; Exceeding the rate limit for one second on the FM API.: Momentary rate limit overages are better handled through backoff rather than opening the circuit.

Misconception tags: Reacting to single failures as systemic; Confusing backoff/rate limits with circuit breaker criteria

Source trace:

https://docs.aws.amazon.com/general/latest/gr/api-retries.html#api-retries-circuit-breaker

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The correct trigger is a sustained period of errors, which is the exact purpose of a circuit breaker mechanism as described in the AWS retry documentation.
   Source: https://docs.aws.amazon.com/general/latest/gr/api-retries.html#api-retries-circuit-breaker
   Evidence span: Circuit breaker patterns prevent continuous retries when repeated errors are detected over a window of time.

### P1-AIP-D3-188

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-188 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.2: Select and configure FMs. |
| `exam_skill` | Skill 1.2.3: Design resilient AI systems to ensure continuous operation during service disruptions (for example, by using AWS Step Functions circuit breaker patterns, Amazon Bedrock Cross-Region Inference for models that have limited regional availability, cross-Region model deployment, graceful degradation strategies). |
| `secondary_exam_skills` | Skill 2.4.3: Create resilient FM systems to ensure reliable operations (for example, by using the AWS SDK for exponential backoff, API Gateway to manage rate limiting, fallback mechanisms for graceful degradation, AWS X-Ray to provide observability across service boundaries). |
| `learning_unit` | Day03-order017 |
| `accelerated_day` | Day 3 |
| `topic` | Fallbacks, circuit breakers, and graceful degradation |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Causal; Strategic |
| `question_format` | multiple-choice |
| `difficulty` | exam-plus |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 180 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order017-local-artifact |
| `raw_source` | 2026-06-30T052157Z-openai-gpt-4.1-day-03-order017.md item 4 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T052157Z |
| `raw_run_id` | order017 |

Stem:

A customer wants to minimize the impact of FM inference service outages on their public-facing question-answer bot. Which combination of mechanisms collectively provides the most resilient user experience?

Options:

1. Implement circuit breaker logic, cross-Region failover, and a response fallback to cached answers.
2. Only increase FM API retry count and timeout duration.
3. Use Bedrock in multiple Regions, but without a fallback or degraded mode.
4. Handle all errors by showing a generic error message to the user.

Correct answer: Implement circuit breaker logic, cross-Region failover, and a response fallback to cached answers.

Rationale: Combining circuit breakers, cross-Region FM access, and fallback outputs ensures high availability, resilience, and user-friendliness even under failures.

Distractors: Only increase FM API retry count and timeout duration.: This still leaves the user with no answer during sustained outages and can increase perceived latency.; Use Bedrock in multiple Regions, but without a fallback or degraded mode.: This avoids single-Region failure but still risks total disruption if all FMs are unavailable or a network partition occurs.; Handle all errors by showing a generic error message to the user.: This provides no useful fallback and leads to poor user experience.

Misconception tags: Thinking retries alone are enough; Not designing for degraded service

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order017-fallbacks-circuit-breakers-graceful-degradation.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: AWS guidance is clear that layered resilience—circuit breaker, failover, and fallback—provides robust mitigation against outages.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order017-fallbacks-circuit-breakers-graceful-degradation.md
   Evidence span: Combining circuit breakers, regional failover, and fallbacks maximizes resilience.

### P1-AIP-D3-189

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-189 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.2: Select and configure FMs. |
| `exam_skill` | Skill 1.2.3: Design resilient AI systems to ensure continuous operation during service disruptions (for example, by using AWS Step Functions circuit breaker patterns, Amazon Bedrock Cross-Region Inference for models that have limited regional availability, cross-Region model deployment, graceful degradation strategies). |
| `secondary_exam_skills` | Skill 2.4.3: Create resilient FM systems to ensure reliable operations (for example, by using the AWS SDK for exponential backoff, API Gateway to manage rate limiting, fallback mechanisms for graceful degradation, AWS X-Ray to provide observability across service boundaries). |
| `learning_unit` | Day03-order017 |
| `accelerated_day` | Day 3 |
| `topic` | Fallbacks, circuit breakers, and graceful degradation |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Causal; Strategic |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | optimize |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order017-local-artifact |
| `raw_source` | 2026-06-30T052157Z-openai-gpt-4.1-day-03-order017.md item 5 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T052157Z |
| `raw_run_id` | order017 |

Stem:

A team notices that their RAG application returns generic error messages to end-users whenever FM capacity errors occur. Which change can improve user experience by aligning with graceful degradation best practices?

Options:

1. Add a fallback path that delivers a contextually appropriate summary or previously cached answer.
2. Suppress all error messages and return null responses.
3. Display the raw FM API error to end-users for transparency.
4. Permanently switch to a rule-based system.

Correct answer: Add a fallback path that delivers a contextually appropriate summary or previously cached answer.

Rationale: Providing a meaningful fallback gives users valuable information even during failures, instead of abrupt or unhelpful error messages.

Distractors: Suppress all error messages and return null responses.: This leads to user confusion and does not maintain engagement.; Display the raw FM API error to end-users for transparency.: Raw errors confuse users and expose internal details, violating best practices.; Permanently switch to a rule-based system.: This removes the benefits of GenAI except in failure scenarios, which isn't balanced graceful degradation.

Misconception tags: Treating any error as a reason to revert to rule-based system; Displaying technical errors to end-users

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order017-fallbacks-circuit-breakers-graceful-degradation.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Graceful degradation focuses on satisfying user intent even under error by returning meaningful fallback data.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order017-fallbacks-circuit-breakers-graceful-degradation.md
   Evidence span: Fallbacks should provide user-appropriate alternatives, such as cached or summary responses.

### P1-AIP-D3-190

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-190 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.2: Select and configure FMs. |
| `exam_skill` | Skill 1.2.3: Design resilient AI systems to ensure continuous operation during service disruptions (for example, by using AWS Step Functions circuit breaker patterns, Amazon Bedrock Cross-Region Inference for models that have limited regional availability, cross-Region model deployment, graceful degradation strategies). |
| `secondary_exam_skills` | Skill 2.4.3: Create resilient FM systems to ensure reliable operations (for example, by using the AWS SDK for exponential backoff, API Gateway to manage rate limiting, fallback mechanisms for graceful degradation, AWS X-Ray to provide observability across service boundaries). |
| `learning_unit` | Day03-order017 |
| `accelerated_day` | Day 3 |
| `topic` | Fallbacks, circuit breakers, and graceful degradation |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Causal; Strategic |
| `question_format` | multiple-response |
| `difficulty` | exam-plus |
| `cognitive_demand` | design |
| `estimated_time_seconds` | 180 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order017-local-artifact |
| `raw_source` | 2026-06-30T052157Z-openai-gpt-4.1-day-03-order017.md item 6 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T052157Z |
| `raw_run_id` | order017 |

Stem:

You are architecting an enterprise workflow that relies on a Bedrock-hosted FM. To maximize overall uptime across unpredictable failure events, which set of practices covers SI resilient operations as recommended in AWS guidance? (Select TWO.)

Options:

1. Use a circuit breaker that triggers on sustained FM API errors.
2. Deploy failover logic to route requests to a secondary Region where available.
3. Implement only aggressive retry logic with no alternate path.
4. Require manual operator intervention upon FM errors.
5. Add a fallback handler to return historical responses or approximate answers.

Correct answer: Use a circuit breaker that triggers on sustained FM API errors.; Add a fallback handler to return historical responses or approximate answers.

Rationale: Circuit breakers and fallback handling are both explicitly mentioned as resilient strategies for continuous operation even during failures.

Distractors: Deploy failover logic to route requests to a secondary Region where available.: While important, failover alone does not fully meet the guidance unless combined with circuit breaker or graceful fallback.; Implement only aggressive retry logic with no alternate path.: Retries do not cover persistent outages or allow for fallback behavior.; Require manual operator intervention upon FM errors.: Manual steps do not align with automated, resilient design for high-availability workloads.

Misconception tags: Only relying on retries; Thinking manual ops provide resilience

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order017-fallbacks-circuit-breakers-graceful-degradation.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Both circuit breakers and fallback logic are required for resilient, unattended AI workflows according to AWS resilience guidance.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order017-fallbacks-circuit-breakers-graceful-degradation.md
   Evidence span: Circuit breaker and fallback handlers are best practices for resilient FM operations.

### P1-AIP-D3-191

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-191 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.2: Select and configure FMs. |
| `exam_skill` | Skill 1.2.3: Design resilient AI systems to ensure continuous operation during service disruptions (for example, by using AWS Step Functions circuit breaker patterns, Amazon Bedrock Cross-Region Inference for models that have limited regional availability, cross-Region model deployment, graceful degradation strategies). |
| `secondary_exam_skills` | Skill 2.4.3: Create resilient FM systems to ensure reliable operations (for example, by using the AWS SDK for exponential backoff, API Gateway to manage rate limiting, fallback mechanisms for graceful degradation, AWS X-Ray to provide observability across service boundaries). |
| `learning_unit` | Day03-order017 |
| `accelerated_day` | Day 3 |
| `topic` | Fallbacks, circuit breakers, and graceful degradation |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Causal; Strategic |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | optimize |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | aws-retry-circuit-breaker |
| `raw_source` | 2026-06-30T052157Z-openai-gpt-4.1-day-03-order017.md item 7 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T052157Z |
| `raw_run_id` | order017 |

Stem:

In a multi-step workflow, you want to prevent downstream service overload caused by circuit breaker misconfiguration. What is the most appropriate practice for tuning the circuit breaker in your Step Functions state machine?

Options:

1. Set thresholds based on empirical error rates over a realistic monitoring window.
2. Configure the circuit breaker to open after a single error event.
3. Disable the circuit breaker in favor of constant retry.
4. Remove fallback logic and only alert operations staff.

Correct answer: Set thresholds based on empirical error rates over a realistic monitoring window.

Rationale: Using empirical data ensures the circuit breaker only activates under true systemic conditions and prevents false positives or unnecessary interruptions.

Distractors: Configure the circuit breaker to open after a single error event.: This risks opening the breaker on transient issues and causing excessive fallback mode activation.; Disable the circuit breaker in favor of constant retry.: This allows overload and cascading failures in the event of persistent errors.; Remove fallback logic and only alert operations staff.: Alerts are important but removing fallback undermines resilience and user experience.

Misconception tags: Misusing circuit breaker thresholds; Relying on operators instead of automation

Source trace:

https://docs.aws.amazon.com/general/latest/gr/api-retries.html#api-retries-circuit-breaker

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Proper circuit breaker tuning as per AWS best practices uses observed error data to minimize service interruption.
   Source: https://docs.aws.amazon.com/general/latest/gr/api-retries.html#api-retries-circuit-breaker
   Evidence span: Tune circuit breaker triggers to measured error rates, not individual events.

### P1-AIP-D3-192

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-192 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.2: Select and configure FMs. |
| `exam_skill` | Skill 1.2.3: Design resilient AI systems to ensure continuous operation during service disruptions (for example, by using AWS Step Functions circuit breaker patterns, Amazon Bedrock Cross-Region Inference for models that have limited regional availability, cross-Region model deployment, graceful degradation strategies). |
| `secondary_exam_skills` | Skill 2.4.3: Create resilient FM systems to ensure reliable operations (for example, by using the AWS SDK for exponential backoff, API Gateway to manage rate limiting, fallback mechanisms for graceful degradation, AWS X-Ray to provide observability across service boundaries). |
| `learning_unit` | Day03-order017 |
| `accelerated_day` | Day 3 |
| `topic` | Fallbacks, circuit breakers, and graceful degradation |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Causal; Strategic |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | implement |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | aws-retry-circuit-breaker |
| `raw_source` | 2026-06-30T052157Z-openai-gpt-4.1-day-03-order017.md item 8 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T052157Z |
| `raw_run_id` | order017 |

Stem:

Your FM workflow uses AWS SDKs and Step Functions to orchestrate multi-API calls. Which action helps prevent runaway retries and service collapse during extended backend disruption?

Options:

1. Implement a circuit breaker that halts retries and invokes fallback after repeated failures.
2. Disable the SDK retry mechanism entirely.
3. Set a very high retry count with no limit to maximize success chance.
4. Add extra sleep between retries instead of using circuit breakers.

Correct answer: Implement a circuit breaker that halts retries and invokes fallback after repeated failures.

Rationale: Circuit breakers are designed for this use-case: they prevent runaway retry storms and allow a fallback or alternate workflow.

Distractors: Disable the SDK retry mechanism entirely.: This removes resilience for transient failures and does not address repeat failures.; Set a very high retry count with no limit to maximize success chance.: Unlimited retries risk service overload and delay fallback, not graceful handling.; Add extra sleep between retries instead of using circuit breakers.: Sleep helps, but without a breaker, it cannot halt retries during persistent outage.

Misconception tags: Thinking more retries is always better; Forgetting fallback necessity

Source trace:

https://docs.aws.amazon.com/general/latest/gr/api-retries.html#api-retries-circuit-breaker

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Circuit breakers directly address the runaway retry problem by interrupting the retry loop and activating fallback logic.
   Source: https://docs.aws.amazon.com/general/latest/gr/api-retries.html#api-retries-circuit-breaker
   Evidence span: Circuit breakers halt retries after repeated failures and push alternate flows.

### P1-AIP-D3-193

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-193 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.2: Select and configure FMs. |
| `exam_skill` | Skill 1.2.3: Design resilient AI systems to ensure continuous operation during service disruptions (for example, by using AWS Step Functions circuit breaker patterns, Amazon Bedrock Cross-Region Inference for models that have limited regional availability, cross-Region model deployment, graceful degradation strategies). |
| `secondary_exam_skills` | Skill 2.4.3: Create resilient FM systems to ensure reliable operations (for example, by using the AWS SDK for exponential backoff, API Gateway to manage rate limiting, fallback mechanisms for graceful degradation, AWS X-Ray to provide observability across service boundaries). |
| `learning_unit` | Day03-order017 |
| `accelerated_day` | Day 3 |
| `topic` | Fallbacks, circuit breakers, and graceful degradation |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Causal; Strategic |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | design |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order017-local-artifact |
| `raw_source` | 2026-06-30T052157Z-openai-gpt-4.1-day-03-order017.md item 9 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T052157Z |
| `raw_run_id` | order017 |

Stem:

A financial services GenAI application must meet regulatory uptime guarantees. Which architecture ensures compliance if the Bedrock-hosted FM becomes unavailable in the region during a trading day?

Options:

1. Route inference requests to a secondary region's Bedrock endpoint via cross-region failover, with a local fallback estimator for last-resort scenarios.
2. Keep retrying the primary Bedrock region until it recovers.
3. Return error codes to users indicating service disruption.
4. Switch all traffic to a local rule-based engine immediately.

Correct answer: Route inference requests to a secondary region's Bedrock endpoint via cross-region failover, with a local fallback estimator for last-resort scenarios.

Rationale: Cross-region failover maximizes upstream availability, and a last-resort local fallback ensures a usable response under all failure states.

Distractors: Keep retrying the primary Bedrock region until it recovers.: Persistent retries delay failover and do not meet uptime or compliance, risking SLA breach.; Return error codes to users indicating service disruption.: Error codes violate continuous operation and degrade user trust.; Switch all traffic to a local rule-based engine immediately.: Using the fallback exclusively ignores regional FM availability that may still exist.

Misconception tags: Retrying indefinitely instead of failing over; Assuming fallback is always primary

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order017-fallbacks-circuit-breakers-graceful-degradation.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Combining cross-Region failover with fallback meets strict uptime and compliance needs and is supported by architectural best practices.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order017-fallbacks-circuit-breakers-graceful-degradation.md
   Evidence span: Use cross-Region failover first and only use local fallback if all FMs are unavailable.

### P1-AIP-D3-194

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-194 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.2: Select and configure FMs. |
| `exam_skill` | Skill 1.2.3: Design resilient AI systems to ensure continuous operation during service disruptions (for example, by using AWS Step Functions circuit breaker patterns, Amazon Bedrock Cross-Region Inference for models that have limited regional availability, cross-Region model deployment, graceful degradation strategies). |
| `secondary_exam_skills` | Skill 2.4.3: Create resilient FM systems to ensure reliable operations (for example, by using the AWS SDK for exponential backoff, API Gateway to manage rate limiting, fallback mechanisms for graceful degradation, AWS X-Ray to provide observability across service boundaries). |
| `learning_unit` | Day03-order017 |
| `accelerated_day` | Day 3 |
| `topic` | Fallbacks, circuit breakers, and graceful degradation |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Causal; Strategic |
| `question_format` | multiple-response |
| `difficulty` | exam-plus |
| `cognitive_demand` | design |
| `estimated_time_seconds` | 180 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order017-local-artifact |
| `raw_source` | 2026-06-30T052157Z-openai-gpt-4.1-day-03-order017.md item 10 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T052157Z |
| `raw_run_id` | order017 |

Stem:

An AI development lead wants to ensure the system meets business SLAs even if all regional Bedrock FMs are temporarily unreachable. Which strategies should they adopt? (Select TWO.)

Options:

1. Implement a local fallback component that generates a degraded answer.
2. Deliver a static status page to all users until FM service is restored.
3. Configure a circuit breaker to invoke fallback after repeated errors.
4. Eliminate timeouts to maximize response wait time.
5. Increase retry attempts in the SDK configuration.

Correct answer: Implement a local fallback component that generates a degraded answer.; Configure a circuit breaker to invoke fallback after repeated errors.

Rationale: The combination of circuit breaker logic and local fallback ensures SLA compliance under FM service outages.

Distractors: Deliver a static status page to all users until FM service is restored.: This option offers no graceful degradation or continuity, just a static outage message.; Eliminate timeouts to maximize response wait time.: This increases user frustration and violates SLA response guarantees.; Increase retry attempts in the SDK configuration.: Retries alone do not guarantee SLA compliance if the service is still unavailable.

Misconception tags: Assuming long waits are acceptable; Thinking retries guarantee high availability

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order017-fallbacks-circuit-breakers-graceful-degradation.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Combining these two controls provides resilience at both API and application levels according to AWS recommendations.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order017-fallbacks-circuit-breakers-graceful-degradation.md
   Evidence span: Circuit breaker and fallback logic together maintain SLA even during complete FM outages.

### P1-AIP-D3-195

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-195 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.2: Select and configure FMs. |
| `exam_skill` | Skill 1.2.3: Design resilient AI systems to ensure continuous operation during service disruptions (for example, by using AWS Step Functions circuit breaker patterns, Amazon Bedrock Cross-Region Inference for models that have limited regional availability, cross-Region model deployment, graceful degradation strategies). |
| `secondary_exam_skills` | Skill 2.4.3: Create resilient FM systems to ensure reliable operations (for example, by using the AWS SDK for exponential backoff, API Gateway to manage rate limiting, fallback mechanisms for graceful degradation, AWS X-Ray to provide observability across service boundaries). |
| `learning_unit` | Day03-order017 |
| `accelerated_day` | Day 3 |
| `topic` | Fallbacks, circuit breakers, and graceful degradation |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Causal; Strategic |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | optimize |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order017-local-artifact |
| `raw_source` | 2026-06-30T052157Z-openai-gpt-4.1-day-03-order017.md item 11 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T052157Z |
| `raw_run_id` | order017 |

Stem:

Your prompt workflow uses Step Functions to orchestrate aggregation, retrieval, and FM inference. Occasionally, the Bedrock FM becomes unresponsive for several minutes, affecting downstream tasks. What should you do to minimize overall workflow disruption and latency?

Options:

1. Configure a circuit breaker in the FM inference state to trigger a fallback after repeated failures.
2. Rely purely on exponential backoff with aggressive retries.
3. Remove all fallbacks to simplify the workflow.
4. Switch the retrieval step to use only keyword search until the FM recovers.

Correct answer: Configure a circuit breaker in the FM inference state to trigger a fallback after repeated failures.

Rationale: This architecture quickly bypasses FM unavailability by routing to a fallback, preserving the workflow and reducing the impact of the FM outage.

Distractors: Rely purely on exponential backoff with aggressive retries.: This delays downstream work and increases overall workflow latency without addressing persistent FM unavailability.; Remove all fallbacks to simplify the workflow.: Without fallbacks, the workflow stalls entirely during FM outages.; Switch the retrieval step to use only keyword search until the FM recovers.: Retrieval changes do not address FM inference failures and leave the downstream process blocked.

Misconception tags: Confusing retrieval with inference failover; Believing retries alone solve workflow resilience

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order017-fallbacks-circuit-breakers-graceful-degradation.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: AWS guidance advocates for circuit breakers plus fallback in long-running orchestrations to minimize impact from slow or failing components.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order017-fallbacks-circuit-breakers-graceful-degradation.md
   Evidence span: Step Functions allow circuit breaker patterns and fallback states to minimize disruption from persistent FM errors.

### P1-AIP-D3-196

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-196 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.2: Select and configure FMs. |
| `exam_skill` | Skill 1.2.3: Design resilient AI systems to ensure continuous operation during service disruptions (for example, by using AWS Step Functions circuit breaker patterns, Amazon Bedrock Cross-Region Inference for models that have limited regional availability, cross-Region model deployment, graceful degradation strategies). |
| `secondary_exam_skills` | Skill 2.4.3: Create resilient FM systems to ensure reliable operations (for example, by using the AWS SDK for exponential backoff, API Gateway to manage rate limiting, fallback mechanisms for graceful degradation, AWS X-Ray to provide observability across service boundaries). |
| `learning_unit` | Day03-order017 |
| `accelerated_day` | Day 3 |
| `topic` | Fallbacks, circuit breakers, and graceful degradation |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Causal; Strategic |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | design |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order017-local-artifact |
| `raw_source` | 2026-06-30T052157Z-openai-gpt-4.1-day-03-order017.md item 12 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T052157Z |
| `raw_run_id` | order017 |

Stem:

You are consulting for an enterprise building a high-availability AI service on AWS. Their main concern is ensuring user workflows do not completely fail when a new model launch causes accidental Bedrock downtime. What is the MOST reliable way to handle this?

Options:

1. Introduce circuit breaker logic and automated fallback to cached or approximate responses.
2. Add more concurrent requests to Bedrock to test for service availability.
3. Have users submit support tickets if their queries fail.
4. Disable fallback features to catch all errors up front.

Correct answer: Introduce circuit breaker logic and automated fallback to cached or approximate responses.

Rationale: Combining circuit breakers and automated fallback meets reliability and high availability requirements by ensuring a response even during unexpected outages.

Distractors: Add more concurrent requests to Bedrock to test for service availability.: This increases load and can make an outage worse; it is not a resilience strategy.; Have users submit support tickets if their queries fail.: Manual incident triage breaks the user experience and fails high-availability goals.; Disable fallback features to catch all errors up front.: Doing so removes the ability to degrade gracefully or provide alternative responses.

Misconception tags: Testing for errors instead of mitigating them; Assuming manual triage equals high availability

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order017-fallbacks-circuit-breakers-graceful-degradation.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Resilience best practice is to combine circuit breaker and fallback so outages are shielded from users by providing degraded but timely responses.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order017-fallbacks-circuit-breakers-graceful-degradation.md
   Evidence span: Circuit breaker and fallback logic are at the core of high-availability GenAI architecture.

### P1-AIP-D3-197

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-197 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 2: Implementation and Integration |
| `exam_task` | Task 2.4: Implement FM API integrations. |
| `exam_skill` | Skill 2.4.3: Create resilient FM systems to ensure reliable operations (for example, by using the AWS SDK for exponential backoff, API Gateway to manage rate limiting, fallback mechanisms for graceful degradation, AWS X-Ray to provide observability across service boundaries). |
| `secondary_exam_skills` | Skill 2.5.6: Improve troubleshooting efficiency for FM applications (for example, by using CloudWatch Logs Insights to analyze prompts and responses, X-Ray to trace FM API calls, Amazon Q Developer to implement GenAI-specific error pattern recognition).; Skill 4.3.1: Create holistic observability systems to provide complete visibility into FM application performance (for example, by using operational metrics, performance tracing, FM interaction tracing, business impact metrics with custom dashboards). |
| `learning_unit` | Day03-order018 |
| `accelerated_day` | Day 3 |
| `topic` | Distributed tracing and FM API observability |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Diagnostic; Causal; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | xray-console |
| `raw_source` | 2026-06-30T052243Z-openai-gpt-4.1-day-03-order018.md item 1 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T052243Z |
| `raw_run_id` | order018 |

Stem:

A generative AI application deployed on AWS Bedrock begins experiencing intermittent latency spikes during inference. You enable AWS X-Ray on the application and want to understand the exact service in the pipeline that causes the bottleneck. What should you do next in the X-Ray console to diagnose this issue efficiently?

Options:

1. Use the X-Ray service map to drill down into individual segment traces and analyze duration outliers.
2. Filter traces by request metadata and export raw trace data to Amazon S3 for offline analysis.
3. Configure custom annotations in your application code to tag traces with model names.
4. Use X-Ray Insights to detect anomalies in Lambda cold start times.

Correct answer: Use the X-Ray service map to drill down into individual segment traces and analyze duration outliers.

Rationale: The service map and segment drill-down in X-Ray enable you to directly visualize latency bottlenecks between services by mapping duration spikes to specific pipeline segments.

Distractors: Filter traces by request metadata and export raw trace data to Amazon S3 for offline analysis.: Exporting data enables advanced analysis but is much slower and doesn't immediately highlight service-level bottlenecks as required in this scenario.; Configure custom annotations in your application code to tag traces with model names.: Annotations enhance filtering but don’t directly identify latency spikes or which service caused them.; Use X-Ray Insights to detect anomalies in Lambda cold start times.: X-Ray Insights highlights anomalies but is not specifically tuned for tracing service-to-service latency in user-defined pipelines.

Misconception tags: Exporting trace data is always the fastest way to troubleshoot.; Annotations reveal bottlenecks automatically.

Source trace:

https://docs.aws.amazon.com/xray/latest/devguide/xray-console.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The X-Ray service map and trace drill-down let you quickly identify latency bottlenecks, as supported by the official documentation.
   Source: https://docs.aws.amazon.com/xray/latest/devguide/xray-console.html
   Evidence span: With the service map, you can visualize, drill down into service nodes... to troubleshoot bottlenecks.

### P1-AIP-D3-198

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-198 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 2: Implementation and Integration |
| `exam_task` | Task 2.4: Implement FM API integrations. |
| `exam_skill` | Skill 2.4.3: Create resilient FM systems to ensure reliable operations (for example, by using the AWS SDK for exponential backoff, API Gateway to manage rate limiting, fallback mechanisms for graceful degradation, AWS X-Ray to provide observability across service boundaries). |
| `secondary_exam_skills` | Skill 2.5.6: Improve troubleshooting efficiency for FM applications (for example, by using CloudWatch Logs Insights to analyze prompts and responses, X-Ray to trace FM API calls, Amazon Q Developer to implement GenAI-specific error pattern recognition).; Skill 4.3.1: Create holistic observability systems to provide complete visibility into FM application performance (for example, by using operational metrics, performance tracing, FM interaction tracing, business impact metrics with custom dashboards). |
| `learning_unit` | Day03-order018 |
| `accelerated_day` | Day 3 |
| `topic` | Distributed tracing and FM API observability |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Diagnostic; Causal; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | cloudwatch-dashboards |
| `raw_source` | 2026-06-30T052243Z-openai-gpt-4.1-day-03-order018.md item 2 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T052243Z |
| `raw_run_id` | order018 |

Stem:

You are asked to customize observability for a generative AI workload that orchestrates multiple Bedrock API calls along with calls to external services. The operations team requires a dashboard with unified, real-time metrics—including FM response times, integration failures, and business-level indicators. What is the most effective AWS-native approach?

Options:

1. Develop a CloudWatch dashboard with custom widgets aggregating logs, metrics, and business KPIs.
2. Export application logs to S3 and use Athena to query and visualize results.
3. Send all logs to Amazon SQS for downstream batch processing.
4. Create a static webpage that refreshes metrics on demand from log files.

Correct answer: Develop a CloudWatch dashboard with custom widgets aggregating logs, metrics, and business KPIs.

Rationale: CloudWatch dashboards are designed to combine metrics, logs, and custom KPIs from multiple services in a unified, interactive view.

Distractors: Export application logs to S3 and use Athena to query and visualize results.: Athena is powerful for ad-hoc querying, but not for unified, real-time, interactive dashboards as required.; Send all logs to Amazon SQS for downstream batch processing.: SQS is for message queuing, not for dashboarding or real-time aggregation.; Create a static webpage that refreshes metrics on demand from log files.: Static pages do not provide scalable, AWS-integrated real-time observability.

Misconception tags: Static dashboards from log files are sufficient; S3/Athena is preferred for real-time monitoring

Source trace:

https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: CloudWatch dashboards aggregate different AWS metrics, logs, and custom KPIs into real-time, interactive visualizations.
   Source: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html
   Evidence span: CloudWatch dashboards are customizable home pages in the CloudWatch console that you can use to monitor your resources in a single view...

### P1-AIP-D3-199

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-199 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 2: Implementation and Integration |
| `exam_task` | Task 2.4: Implement FM API integrations. |
| `exam_skill` | Skill 2.4.3: Create resilient FM systems to ensure reliable operations (for example, by using the AWS SDK for exponential backoff, API Gateway to manage rate limiting, fallback mechanisms for graceful degradation, AWS X-Ray to provide observability across service boundaries). |
| `secondary_exam_skills` | Skill 2.5.6: Improve troubleshooting efficiency for FM applications (for example, by using CloudWatch Logs Insights to analyze prompts and responses, X-Ray to trace FM API calls, Amazon Q Developer to implement GenAI-specific error pattern recognition).; Skill 4.3.1: Create holistic observability systems to provide complete visibility into FM application performance (for example, by using operational metrics, performance tracing, FM interaction tracing, business impact metrics with custom dashboards). |
| `learning_unit` | Day03-order018 |
| `accelerated_day` | Day 3 |
| `topic` | Distributed tracing and FM API observability |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Diagnostic; Causal; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | analyze |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | cloudwatch-dashboards |
| `raw_source` | 2026-06-30T052243Z-openai-gpt-4.1-day-03-order018.md item 4 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T052243Z |
| `raw_run_id` | order018 |

Stem:

You are developing a GenAI-powered customer support system that repeatedly provides delayed responses to certain intents. To identify where delays occur, which CloudWatch dashboard feature is essential for correlating model latency with specific user intents and time periods?

Options:

1. Multi-metric line graphs with widgets sorted by intent and time
2. Log Streams filters grouped by runtime environment
3. Alarm history tables for model error rates
4. Percentile distribution scatter plots of memory usage

Correct answer: Multi-metric line graphs with widgets sorted by intent and time

Rationale: Multi-metric dashboards enable parallel visualization of model latency against intent and time, allowing for quick correlation.

Distractors: Log Streams filters grouped by runtime environment: Grouping logs by environment doesn't directly surface latency per intent and time.; Alarm history tables for model error rates: Alarms show threshold breaches, but do not correlate latency and business-specific context.; Percentile distribution scatter plots of memory usage: Memory usage scatter plots are useful for performance analysis but not for correlating user intent latency.

Misconception tags: Alarms provide root-cause correlation; Memory usage is the only metric for latency

Source trace:

https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: CloudWatch dashboards can combine multiple metrics such as latency, intent, and timestamp for meaningful correlation, as described in the docs.
   Source: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html
   Evidence span: You can display multiple metrics in the same graph, including metrics from different services, for comparison.

### P1-AIP-D3-200

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-200 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 2: Implementation and Integration |
| `exam_task` | Task 2.4: Implement FM API integrations. |
| `exam_skill` | Skill 2.4.3: Create resilient FM systems to ensure reliable operations (for example, by using the AWS SDK for exponential backoff, API Gateway to manage rate limiting, fallback mechanisms for graceful degradation, AWS X-Ray to provide observability across service boundaries). |
| `secondary_exam_skills` | Skill 2.5.6: Improve troubleshooting efficiency for FM applications (for example, by using CloudWatch Logs Insights to analyze prompts and responses, X-Ray to trace FM API calls, Amazon Q Developer to implement GenAI-specific error pattern recognition).; Skill 4.3.1: Create holistic observability systems to provide complete visibility into FM application performance (for example, by using operational metrics, performance tracing, FM interaction tracing, business impact metrics with custom dashboards). |
| `learning_unit` | Day03-order018 |
| `accelerated_day` | Day 3 |
| `topic` | Distributed tracing and FM API observability |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Diagnostic; Causal; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | xray-console |
| `raw_source` | 2026-06-30T052243Z-openai-gpt-4.1-day-03-order018.md item 6 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T052243Z |
| `raw_run_id` | order018 |

Stem:

During an outage of a downstream payment service, your distributed AI application suddenly accumulates throttling errors and retry storms visible in the X-Ray console. Which visualization or tab will most quickly help you identify the affected service and the propagation of failures?

Options:

1. Service Map with highlighted error nodes and trace paths
2. Trace List grouped by API Gateway execution time
3. CloudWatch Dashboard with transaction counters
4. Alarm Status widget in CloudWatch

Correct answer: Service Map with highlighted error nodes and trace paths

Rationale: X-Ray’s service map visually surfaces error nodes and propagates failure information for rapid diagnosis during cascading outages.

Distractors: Trace List grouped by API Gateway execution time: The trace list shows specific traces but lacks the high-level cross-service error propagation view.; CloudWatch Dashboard with transaction counters: Transaction counters may spike, but they do not show root-cause propagation links.; Alarm Status widget in CloudWatch: Alarms highlight symptom metrics, but not cross-service causality or error pathways.

Misconception tags: Counters and alarms show root cause; Trace list is faster than the service map

Source trace:

https://docs.aws.amazon.com/xray/latest/devguide/xray-console.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The X-Ray service map highlights error nodes and dependency paths for cascading failure analysis.
   Source: https://docs.aws.amazon.com/xray/latest/devguide/xray-console.html
   Evidence span: The service map helps you visualize relationships between services and quickly spot errors or bottlenecks.

### P1-AIP-D3-201

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-201 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 2: Implementation and Integration |
| `exam_task` | Task 2.4: Implement FM API integrations. |
| `exam_skill` | Skill 2.4.3: Create resilient FM systems to ensure reliable operations (for example, by using the AWS SDK for exponential backoff, API Gateway to manage rate limiting, fallback mechanisms for graceful degradation, AWS X-Ray to provide observability across service boundaries). |
| `secondary_exam_skills` | Skill 2.5.6: Improve troubleshooting efficiency for FM applications (for example, by using CloudWatch Logs Insights to analyze prompts and responses, X-Ray to trace FM API calls, Amazon Q Developer to implement GenAI-specific error pattern recognition).; Skill 4.3.1: Create holistic observability systems to provide complete visibility into FM application performance (for example, by using operational metrics, performance tracing, FM interaction tracing, business impact metrics with custom dashboards). |
| `learning_unit` | Day03-order018 |
| `accelerated_day` | Day 3 |
| `topic` | Distributed tracing and FM API observability |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Diagnostic; Causal; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | xray-console |
| `raw_source` | 2026-06-30T052243Z-openai-gpt-4.1-day-03-order018.md item 7 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T052243Z |
| `raw_run_id` | order018 |

Stem:

While analyzing prompt failures in a GenAI API, you need to track prompt payload content, user IDs, and FM model name across the distributed logs and traces for a recent production incident. Which feature of AWS X-Ray or CloudWatch best supports this kind of search and correlation?

Options:

1. X-Ray annotations and filter expressions
2. X-Ray service map error percent coloring
3. CloudWatch alarm actions
4. CloudWatch default metric graphs

Correct answer: X-Ray annotations and filter expressions

Rationale: Annotations allow injection of custom key-value fields (e.g., user ID, prompt) into traces; filter expressions enable powerful querying for correlation.

Distractors: X-Ray service map error percent coloring: Error coloring is good for surface anomalies but not for searching fields or correlating context across traces.; CloudWatch alarm actions: Alarm actions can trigger responses but don’t provide correlation of detailed log or trace data.; CloudWatch default metric graphs: Graphs track standard metrics, not payload or custom fields correlation.

Misconception tags: Error coloring exposes payload-level detail; Metric graphs surface prompt content

Source trace:

https://docs.aws.amazon.com/xray/latest/devguide/xray-console.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Annotations and filter expressions in X-Ray enable detailed search and correlation by custom attributes.
   Source: https://docs.aws.amazon.com/xray/latest/devguide/xray-console.html
   Evidence span: You can use annotations to record information... you can use filter expressions to find traces that match specific conditions.

### P1-AIP-D3-202

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-202 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 2: Implementation and Integration |
| `exam_task` | Task 2.4: Implement FM API integrations. |
| `exam_skill` | Skill 2.4.3: Create resilient FM systems to ensure reliable operations (for example, by using the AWS SDK for exponential backoff, API Gateway to manage rate limiting, fallback mechanisms for graceful degradation, AWS X-Ray to provide observability across service boundaries). |
| `secondary_exam_skills` | Skill 2.5.6: Improve troubleshooting efficiency for FM applications (for example, by using CloudWatch Logs Insights to analyze prompts and responses, X-Ray to trace FM API calls, Amazon Q Developer to implement GenAI-specific error pattern recognition).; Skill 4.3.1: Create holistic observability systems to provide complete visibility into FM application performance (for example, by using operational metrics, performance tracing, FM interaction tracing, business impact metrics with custom dashboards). |
| `learning_unit` | Day03-order018 |
| `accelerated_day` | Day 3 |
| `topic` | Distributed tracing and FM API observability |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Diagnostic; Causal; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | implement |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | cloudwatch-dashboards |
| `raw_source` | 2026-06-30T052243Z-openai-gpt-4.1-day-03-order018.md item 8 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T052243Z |
| `raw_run_id` | order018 |

Stem:

A team is responsible for several GenAI-powered REST APIs running across different AWS accounts. Management requests an integrated dashboard summarizing real-time FM API health, error rates, and business indicators without granting access to each account’s console. What is the most suitable AWS-native solution?

Options:

1. Create a cross-account CloudWatch dashboard and share it using resource policies
2. Enable X-Ray in all accounts and export trace summaries to S3
3. Develop custom log shipper Lambda functions for each account
4. Query account-specific logs directly from a centralized VPC

Correct answer: Create a cross-account CloudWatch dashboard and share it using resource policies

Rationale: CloudWatch dashboards can aggregate and share metrics from multiple AWS accounts via cross-account access, providing secure and consolidated visibility.

Distractors: Enable X-Ray in all accounts and export trace summaries to S3: Exporting trace summaries lacks immediate dashboard visualization and native cross-account aggregation.; Develop custom log shipper Lambda functions for each account: Custom shipping is complex, error-prone, and less secure than native dashboarding.; Query account-specific logs directly from a centralized VPC: Direct querying does not provide a dashboard or proper cross-account integration.

Misconception tags: Trace exports provide unified dashboards; Log shippers replace dashboard features

Source trace:

https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: CloudWatch dashboards with cross-account resource policies enable the requested visibility securely and natively.
   Source: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html
   Evidence span: You can share CloudWatch dashboards across AWS accounts by using resource policies.

### P1-AIP-D3-203

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-203 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 2: Implementation and Integration |
| `exam_task` | Task 2.4: Implement FM API integrations. |
| `exam_skill` | Skill 2.4.3: Create resilient FM systems to ensure reliable operations (for example, by using the AWS SDK for exponential backoff, API Gateway to manage rate limiting, fallback mechanisms for graceful degradation, AWS X-Ray to provide observability across service boundaries). |
| `secondary_exam_skills` | Skill 2.5.6: Improve troubleshooting efficiency for FM applications (for example, by using CloudWatch Logs Insights to analyze prompts and responses, X-Ray to trace FM API calls, Amazon Q Developer to implement GenAI-specific error pattern recognition).; Skill 4.3.1: Create holistic observability systems to provide complete visibility into FM application performance (for example, by using operational metrics, performance tracing, FM interaction tracing, business impact metrics with custom dashboards). |
| `learning_unit` | Day03-order018 |
| `accelerated_day` | Day 3 |
| `topic` | Distributed tracing and FM API observability |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Diagnostic; Causal; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | optimize |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | cloudwatch-dashboards |
| `raw_source` | 2026-06-30T052243Z-openai-gpt-4.1-day-03-order018.md item 12 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T052243Z |
| `raw_run_id` | order018 |

Stem:

After a new FM model version deploys, your observability dashboard’s error count spikes. Traces show new response patterns, but your dashboards don't surface business-level impact. What dashboard enhancement addresses this visibility gap for leadership?

Options:

1. Add custom widgets that calculate business KPIs (e.g., revenue impact, orders affected) using metric math or Lambda metric ingestion.
2. Increase the polling frequency of infrastructure-level error counters.
3. Create a separate dashboard for every microservice.
4. Display only model-internal metrics such as token generation speed.

Correct answer: Add custom widgets that calculate business KPIs (e.g., revenue impact, orders affected) using metric math or Lambda metric ingestion.

Rationale: Business KPIs captured in dashboard custom widgets enable leadership to quickly connect technical errors to business outcomes.

Distractors: Increase the polling frequency of infrastructure-level error counters.: Higher polling velocity doesn't introduce business context.; Create a separate dashboard for every microservice.: More dashboards lowers clarity; still no business KPI surface.; Display only model-internal metrics such as token generation speed.: Model metrics aren't aligned with business impact visibility required by leadership.

Misconception tags: Operative KPIs replace business metrics; Separation yields better impact awareness

Source trace:

https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Adding business KPIs using widgets and metric math surfaces business impact alongside technical metrics, per CloudWatch documentation.
   Source: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html
   Evidence span: You can add widgets to display custom metrics, including business-level KPIs, to CloudWatch dashboards.

### P1-AIP-D3-204

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-204 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 2: Implementation and Integration |
| `exam_task` | Task 2.4: Implement FM API integrations. |
| `exam_skill` | Skill 2.4.3: Create resilient FM systems to ensure reliable operations (for example, by using the AWS SDK for exponential backoff, API Gateway to manage rate limiting, fallback mechanisms for graceful degradation, AWS X-Ray to provide observability across service boundaries). |
| `secondary_exam_skills` | Skill 2.5.6: Improve troubleshooting efficiency for FM applications (for example, by using CloudWatch Logs Insights to analyze prompts and responses, X-Ray to trace FM API calls, Amazon Q Developer to implement GenAI-specific error pattern recognition).; Skill 4.3.1: Create holistic observability systems to provide complete visibility into FM application performance (for example, by using operational metrics, performance tracing, FM interaction tracing, business impact metrics with custom dashboards). |
| `learning_unit` | Day03-order018 |
| `accelerated_day` | Day 3 |
| `topic` | Distributed tracing and FM API observability |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Diagnostic; Causal; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | xray-console |
| `raw_source` | 2026-06-30T052243Z-openai-gpt-4.1-day-03-order018.md item 13 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T052243Z |
| `raw_run_id` | order018 |

Stem:

You're investigating intermittent errors in a multi-step GenAI pipeline. You need to confirm whether API timeouts correlate with downstream FM retries and to visually verify the causal path. What is the best X-Ray console approach to accomplish this end-to-end investigation?

Options:

1. Select problematic traces from the trace list and examine segment timelines for retry and timeout patterns.
2. Use alarm status summaries to identify error timing across services.
3. Filter logs for HTTP 504 entries and cross-reference in the dashboard.
4. Rely on default service map node coloring to surface causality.

Correct answer: Select problematic traces from the trace list and examine segment timelines for retry and timeout patterns.

Rationale: Reviewing segment timelines within traces shows the precise timing and order of retries and timeouts across pipeline steps for true causality visualization.

Distractors: Use alarm status summaries to identify error timing across services.: Alarms surface incidents but lack segment-level causality or retry visibility.; Filter logs for HTTP 504 entries and cross-reference in the dashboard.: Filtering for HTTP 504 entries helps spot symptoms, but correlation across pipeline steps is inefficient and indirect.; Rely on default service map node coloring to surface causality.: Node coloring only highlights error counts or percentages, not the temporal chain of events.

Misconception tags: Node coloring alone proves causality; Alarm status replaces trace timeline analysis

Source trace:

https://docs.aws.amazon.com/xray/latest/devguide/xray-console.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Selecting and examining the trace timeline gives exact causal sequencing, as described in the X-Ray documentation.
   Source: https://docs.aws.amazon.com/xray/latest/devguide/xray-console.html
   Evidence span: In the trace list, you can find traces that show error patterns and examine their segment timelines for root cause.

### P1-AIP-D3-205

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-205 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.4: Develop quality assurance systems to ensure prompt effectiveness and reliability for FMs (for example, by using Lambda functions to verify expected output, Step Functions to test edge cases, CloudWatch to test prompt regression). |
| `secondary_exam_skills` | Skill 5.1.4: Create systematic quality assurance processes to maintain consistent performance standards for FMs (for example, by using continuous evaluation workflows, regression testing for model outputs, automated quality gates for deployments). |
| `learning_unit` | Day03-order010 |
| `accelerated_day` | Day 3 |
| `topic` | Prompt regression testing and quality assurance |
| `knowledge_category` | Skill; Knowledge |
| `knowledge_type` | Procedural; Causal; Strategic |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | optimize |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order010-local-artifact |
| `raw_source` | 2026-06-30T052342Z-openai-gpt-4.1-day-03-order010-top-up-5.md item 1 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T052342Z |
| `raw_run_id` | order010-top-up-5 |

Stem:

A global retailer recently overhauled its FM prompt templates. Following this, they observe that expected outputs remain correct for standard test cases, but subtle language ambiguities now cause inconsistent model behavior in certain regions. What is the most effective action to systematically prevent such regressions in the future?

Options:

1. Expand the regression test suite to include region-specific and edge case prompts drawn from real-world usage.
2. Rely exclusively on passing standard prompt test cases from the main business workflow.
3. Increase logging for failed prompt outputs without modifying the test process.
4. Reduce deployment frequency to allow more time for post-deployment monitoring.

Correct answer: Expand the regression test suite to include region-specific and edge case prompts drawn from real-world usage.

Rationale: By incorporating region-specific and less common prompts into regression tests, the organization can detect contextual and language-based regressions before deployment, not just for the main business workflow.

Distractors: Rely exclusively on passing standard prompt test cases from the main business workflow.: This approach misses regressions outside the core workflow, as evidenced by missed language-specific issues.; Increase logging for failed prompt outputs without modifying the test process.: Logging alone identifies failures post-factum but does not stop regressions from reaching production.; Reduce deployment frequency to allow more time for post-deployment monitoring.: Slowing deployments delays detection and does not directly address prompt test coverage gaps.

Misconception tags: Over-reliance on standard test cases; Missing regional and contextual diversity in regression testing

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order010-prompt-regression-testing-quality-assurance.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Expanding regression coverage to real usage and regional edge cases captures regressions standard tests miss, just as the scenario requires.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order010-prompt-regression-testing-quality-assurance.md
   Evidence span: Regression tests should cover edge cases and real-world context, not just common flows.

### P1-AIP-D3-206

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-206 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.4: Develop quality assurance systems to ensure prompt effectiveness and reliability for FMs (for example, by using Lambda functions to verify expected output, Step Functions to test edge cases, CloudWatch to test prompt regression). |
| `secondary_exam_skills` | Skill 5.1.4: Create systematic quality assurance processes to maintain consistent performance standards for FMs (for example, by using continuous evaluation workflows, regression testing for model outputs, automated quality gates for deployments). |
| `learning_unit` | Day03-order010 |
| `accelerated_day` | Day 3 |
| `topic` | Prompt regression testing and quality assurance |
| `knowledge_category` | Skill; Knowledge |
| `knowledge_type` | Procedural; Causal; Strategic |
| `question_format` | multiple-response |
| `difficulty` | medium |
| `cognitive_demand` | implement |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order010-local-artifact |
| `raw_source` | 2026-06-30T052342Z-openai-gpt-4.1-day-03-order010-top-up-5.md item 2 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T052342Z |
| `raw_run_id` | order010-top-up-5 |

Stem:

An insurance company is enhancing its prompt quality assurance pipeline. After recent failures due to prompt changes that affected specific downstream analytics, what combination of strategies best increases confidence in prompt stability before each release? (Select TWO.)

Options:

1. Automate regression testing for all major and minor prompt updates
2. Periodically review a small random sample of past prompts for failures
3. Incorporate verification Lambda functions that check downstream output structure
4. Manually inspect output responses for selected business-critical queries
5. Add approval gates for prompt changes that require business sign-off

Correct answer: Automate regression testing for all major and minor prompt updates; Incorporate verification Lambda functions that check downstream output structure

Rationale: Automation ensures regressions are caught early and consistently; using Lambda functions to formally check outputs prevents failures due to output structure changes.

Distractors: Periodically review a small random sample of past prompts for failures: Limited manual sampling leaves large gaps where regressions can sneak in undetected.; Manually inspect output responses for selected business-critical queries: Manual inspection is inconsistent and won’t scale across updates and edge cases.; Add approval gates for prompt changes that require business sign-off: Gating changes improves governance but does not automatically detect technical regressions or output failures.

Misconception tags: Manual QA sufficiency; Confusing approvals with regression automation

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order010-prompt-regression-testing-quality-assurance.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The source emphasizes automating regression checks and using Lambda for output verification to reliably catch technical and business regressions.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order010-prompt-regression-testing-quality-assurance.md
   Evidence span: Automated regression tests and Lambda-based output verification are essential for prompt QA.

### P1-AIP-D3-207

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-207 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.4: Develop quality assurance systems to ensure prompt effectiveness and reliability for FMs (for example, by using Lambda functions to verify expected output, Step Functions to test edge cases, CloudWatch to test prompt regression). |
| `secondary_exam_skills` | Skill 5.1.4: Create systematic quality assurance processes to maintain consistent performance standards for FMs (for example, by using continuous evaluation workflows, regression testing for model outputs, automated quality gates for deployments). |
| `learning_unit` | Day03-order010 |
| `accelerated_day` | Day 3 |
| `topic` | Prompt regression testing and quality assurance |
| `knowledge_category` | Skill; Knowledge |
| `knowledge_type` | Procedural; Causal; Strategic |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order010-local-artifact |
| `raw_source` | 2026-06-30T052342Z-openai-gpt-4.1-day-03-order010-top-up-5.md item 3 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T052342Z |
| `raw_run_id` | order010-top-up-5 |

Stem:

A startup’s product pipeline pushes prompt template updates several times per week via a CI/CD system. On one occasion, a bug in a prompt broke a rare user flow in production, bypassing the test stage. How should the QA design be improved to prevent recurrence of this issue?

Options:

1. Add coverage for rare and previously failing user flows to the automated regression suite
2. Require all prompt changes to be manually reviewed before merge
3. Increase the frequency of production deployments for faster feedback
4. Rely on monitoring downstream applications for error feedback after release

Correct answer: Add coverage for rare and previously failing user flows to the automated regression suite

Rationale: Expanding regression coverage to include rare and historical failures proactively prevents similar issues from reaching production.

Distractors: Require all prompt changes to be manually reviewed before merge: Manual review alone is inconsistent and may miss subtle or rare failures detectable by automated tests.; Increase the frequency of production deployments for faster feedback: Faster deployments reduce detection latency but do not fix the underlying lack of regression test coverage.; Rely on monitoring downstream applications for error feedback after release: Post-release error monitoring alerts after user impact instead of preventing regressions upfront.

Misconception tags: Over-reliance on manual review; Treating post-production monitoring as proactive QA

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order010-prompt-regression-testing-quality-assurance.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Testing for rare and past failures in regression suites ensures those issues are caught before deployment.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order010-prompt-regression-testing-quality-assurance.md
   Evidence span: Prompt regressions are minimized by adding edge and historical failure cases to regression test coverage.

### P1-AIP-D3-208

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-208 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.4: Develop quality assurance systems to ensure prompt effectiveness and reliability for FMs (for example, by using Lambda functions to verify expected output, Step Functions to test edge cases, CloudWatch to test prompt regression). |
| `secondary_exam_skills` | Skill 5.1.4: Create systematic quality assurance processes to maintain consistent performance standards for FMs (for example, by using continuous evaluation workflows, regression testing for model outputs, automated quality gates for deployments). |
| `learning_unit` | Day03-order010 |
| `accelerated_day` | Day 3 |
| `topic` | Prompt regression testing and quality assurance |
| `knowledge_category` | Skill; Knowledge |
| `knowledge_type` | Procedural; Causal; Strategic |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | implement |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order010-local-artifact |
| `raw_source` | 2026-06-30T052342Z-openai-gpt-4.1-day-03-order010-top-up-5.md item 4 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T052342Z |
| `raw_run_id` | order010-top-up-5 |

Stem:

A development team wants to reduce the risk of prompt-related outages after deploying new prompt templates for their GenAI-driven helpdesk chatbot. Which approach best provides continual assurance that critical bot behaviors remain reliable release after release?

Options:

1. Introduce continuous automated regression testing in the deployment pipeline covering all critical frontend use cases
2. Schedule quarterly manual reviews of chat transcript outputs for anomalies
3. Increase verbosity of production logging to detect rare prompt-related failures
4. Rely on canary deployments only for validating new prompt releases

Correct answer: Introduce continuous automated regression testing in the deployment pipeline covering all critical frontend use cases

Rationale: Automated regression tests ensure new prompt versions do not introduce failures by running checks for all mission-critical functions as part of each release.

Distractors: Schedule quarterly manual reviews of chat transcript outputs for anomalies: Manual, infrequent reviews offer only opportunistic detection and risk long periods of undetected regressions.; Increase verbosity of production logging to detect rare prompt-related failures: Better logging aids post-hoc analysis, but does not prevent the introduction of regressions in the first place.; Rely on canary deployments only for validating new prompt releases: Canary releases help catch issues but lack exhaustive, systematic coverage essential for critical business behaviors.

Misconception tags: Delaying QA to production; Canary-only validation sufficiency

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order010-prompt-regression-testing-quality-assurance.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Integrating regression testing with automated pipelines ensures systematic protection against regressions on every release.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order010-prompt-regression-testing-quality-assurance.md
   Evidence span: Continuous regression testing provides assurance for prompt reliability in automated pipelines.

### P1-AIP-D3-209

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-209 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.6: Implement prompt engineering strategies and governance for FM interactions. |
| `exam_skill` | Skill 1.6.4: Develop quality assurance systems to ensure prompt effectiveness and reliability for FMs (for example, by using Lambda functions to verify expected output, Step Functions to test edge cases, CloudWatch to test prompt regression). |
| `secondary_exam_skills` | Skill 5.1.4: Create systematic quality assurance processes to maintain consistent performance standards for FMs (for example, by using continuous evaluation workflows, regression testing for model outputs, automated quality gates for deployments). |
| `learning_unit` | Day03-order010 |
| `accelerated_day` | Day 3 |
| `topic` | Prompt regression testing and quality assurance |
| `knowledge_category` | Skill; Knowledge |
| `knowledge_type` | Procedural; Causal; Strategic |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | optimize |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | day03-order010-local-artifact |
| `raw_source` | 2026-06-30T052342Z-openai-gpt-4.1-day-03-order010-top-up-5.md item 5 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T052342Z |
| `raw_run_id` | order010-top-up-5 |

Stem:

An e-commerce company’s LLM-powered recommendations engine suffers a drop in personalization quality a week after a prompt template update. Their regression suite covers the most common queries. Which improvement will best prevent this quality degradation from recurring in the future?

Options:

1. Continuously update regression test datasets to include emerging query patterns and edge user behaviors
2. Only test prompts during off-peak hours to avoid impacting live customers
3. Increase the minimum passing score for model response relevance in the current tests
4. Manually audit outputs flagged by customer support for a month after every change

Correct answer: Continuously update regression test datasets to include emerging query patterns and edge user behaviors

Rationale: By updating regression data to reflect current and unforeseen user behavior, the QA process can proactively catch regressions as user patterns evolve.

Distractors: Only test prompts during off-peak hours to avoid impacting live customers: Testing timing does not address regression detection gap for new or rare queries.; Increase the minimum passing score for model response relevance in the current tests: Higher thresholds won't reveal regressions in uncovered query types.; Manually audit outputs flagged by customer support for a month after every change: Manual audits address some issues after user impact; they do not systematically prevent regressions.

Misconception tags: Static test suite sufficiency; Mistaking timing or score threshold for coverage breadth

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order010-prompt-regression-testing-quality-assurance.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Regularly refreshing regression suites keeps tests relevant and reduces the risk of degrading response quality from unseen patterns.
   Source: docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order010-prompt-regression-testing-quality-assurance.md
   Evidence span: Continuously refreshing test data is key to maintaining prompt QA as user behavior evolves.

### P1-AIP-D3-210

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-210 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.3: Implement data validation and processing pipelines for FM consumption. |
| `exam_skill` | Skill 1.3.3: Format input data for FM inference according to model-specific requirements (for example, by using JSON formatting for Amazon Bedrock API requests, structured data preparation for SageMaker AI endpoints, conversation formatting for dialog-based applications). |
| `secondary_exam_skills` | Skill 2.5.1: Create FM API interfaces to address the specific requirements of GenAI workloads (for example, by using API Gateway to handle streaming responses, token limit management, retry strategies to handle model timeouts).; Skill 5.2.1: Resolve content handling issues to ensure that necessary information is processed completely in FM interactions (for example, by using context window overflow diagnostics, dynamic chunking strategies, prompt design optimization, truncation-related error analysis). |
| `learning_unit` | Day03-order015 |
| `accelerated_day` | Day 3 |
| `topic` | Token limits, request validation, and response handling |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Declarative; Procedural; Causal |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | bedrock-model-parameters |
| `raw_source` | 2026-06-30T052440Z-openai-gpt-4.1-day-03-order015-top-up-12.md item 1 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T052440Z |
| `raw_run_id` | order015-top-up-12 |

Stem:

A developer notices that a Bedrock-powered customer support chatbot sometimes returns responses with missing or incomplete information when users submit lengthy multi-turn questions containing significant context. What design change should they prioritize to ensure the chatbot consistently returns relevant and complete responses without API errors?

Options:

1. Implement dynamic prompt truncation based on model token limit parameters.
2. Increase the allowed API payload size in the Bedrock console.
3. Reduce model temperature to minimize hallucinations.
4. Disable response streaming to maximize context retention.

Correct answer: Implement dynamic prompt truncation based on model token limit parameters.

Rationale: Bedrock models enforce token limits per request; exceeding these limits leads to incomplete answers or request errors. Dynamic truncation ensures both context and user input fit the model's requirements for a reliable response.

Distractors: Increase the allowed API payload size in the Bedrock console.: API payload size cannot override model token limits; adjusting it does not directly affect model context handling.; Reduce model temperature to minimize hallucinations.: Lowering temperature may improve answer consistency, but does not address the root problem of context truncation due to token overflow.; Disable response streaming to maximize context retention.: Response streaming formats output, but does not let you pass more tokens or solve over-limit input issues.

Misconception tags: API configuration vs model limits; Token truncation causes

Source trace:

https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Model token limits require prompt design to avoid overflows; dynamic truncation is the effective remediation for fitting input/context within the model's window.
   Source: https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html
   Evidence span: Each foundation model enforces its own maximum token limits for input and output.

### P1-AIP-D3-211

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-211 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.3: Implement data validation and processing pipelines for FM consumption. |
| `exam_skill` | Skill 1.3.3: Format input data for FM inference according to model-specific requirements (for example, by using JSON formatting for Amazon Bedrock API requests, structured data preparation for SageMaker AI endpoints, conversation formatting for dialog-based applications). |
| `secondary_exam_skills` | Skill 2.5.1: Create FM API interfaces to address the specific requirements of GenAI workloads (for example, by using API Gateway to handle streaming responses, token limit management, retry strategies to handle model timeouts).; Skill 5.2.1: Resolve content handling issues to ensure that necessary information is processed completely in FM interactions (for example, by using context window overflow diagnostics, dynamic chunking strategies, prompt design optimization, truncation-related error analysis). |
| `learning_unit` | Day03-order015 |
| `accelerated_day` | Day 3 |
| `topic` | Token limits, request validation, and response handling |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Declarative; Procedural; Causal |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | implement |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | bedrock-model-parameters |
| `raw_source` | 2026-06-30T052440Z-openai-gpt-4.1-day-03-order015-top-up-12.md item 3 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T052440Z |
| `raw_run_id` | order015-top-up-12 |

Stem:

A Bedrock-based document summarizer frequently returns error messages related to exceeding the model’s token limit when users upload very large files for processing. What operational response will most reliably prevent these errors when scaling to many simultaneous users?

Options:

1. Pre-process documents to chunk and summarize before forming model input within the per-request token limit.
2. Upgrade to a higher-capacity endpoint without re-designing the prompt.
3. Increase the number of concurrent API requests to batch process more documents.
4. Ignore token limit warnings, since the model will auto-truncate the context anyway.

Correct answer: Pre-process documents to chunk and summarize before forming model input within the per-request token limit.

Rationale: The only way to ensure requests are accepted is to fit the token window, often by chunking large content before inference. Bedrock models have fixed per-request token limits.

Distractors: Upgrade to a higher-capacity endpoint without re-designing the prompt.: Endpoint capacity affects throughput— not model context limits.; Increase the number of concurrent API requests to batch process more documents.: Concurrency/parallelism increases scale but won't affect per-request token enforcement.; Ignore token limit warnings, since the model will auto-truncate the context anyway.: Ignoring warnings will not prevent failures or incomplete outputs; auto-truncation may lose important context.

Misconception tags: token windows vs infra scaling; auto-truncation trap

Source trace:

https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Chunking and pre-summarizing ensure the request never surpasses the model's strict token window.
   Source: https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html
   Evidence span: Each request must not exceed the model’s token limit. Split large inputs as needed.

### P1-AIP-D3-212

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-212 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.3: Implement data validation and processing pipelines for FM consumption. |
| `exam_skill` | Skill 1.3.3: Format input data for FM inference according to model-specific requirements (for example, by using JSON formatting for Amazon Bedrock API requests, structured data preparation for SageMaker AI endpoints, conversation formatting for dialog-based applications). |
| `secondary_exam_skills` | Skill 2.5.1: Create FM API interfaces to address the specific requirements of GenAI workloads (for example, by using API Gateway to handle streaming responses, token limit management, retry strategies to handle model timeouts).; Skill 5.2.1: Resolve content handling issues to ensure that necessary information is processed completely in FM interactions (for example, by using context window overflow diagnostics, dynamic chunking strategies, prompt design optimization, truncation-related error analysis). |
| `learning_unit` | Day03-order015 |
| `accelerated_day` | Day 3 |
| `topic` | Token limits, request validation, and response handling |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Declarative; Procedural; Causal |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | bedrock-conversation |
| `raw_source` | 2026-06-30T052440Z-openai-gpt-4.1-day-03-order015-top-up-12.md item 4 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T052440Z |
| `raw_run_id` | order015-top-up-12 |

Stem:

An engineering team’s Bedrock-powered Q&A bot sometimes answers incompletely or with reduced accuracy after several turns of a long conversation. What is the most probable cause, and the recommended mitigation?

Options:

1. Conversation plus user input exceeded the model's token context window; introduce summarization or truncation of earlier conversation turns.
2. The model's temperature is too high; decrease temperature to improve answer accuracy.
3. Random API latency spikes; retry incomplete responses via exponential backoff.
4. User prompts were malformed; add stricter JSON schema validation.

Correct answer: Conversation plus user input exceeded the model's token context window; introduce summarization or truncation of earlier conversation turns.

Rationale: When the context window is exceeded, FMs drop the oldest content—leading to incomplete answers. Summarizing or truncating conversation history keeps the relevant context in scope.

Distractors: The model's temperature is too high; decrease temperature to improve answer accuracy.: Temperature affects randomness, not context retention or cutoff.; Random API latency spikes; retry incomplete responses via exponential backoff.: Latency may cause retries, but incomplete answers stem from input context overflow.; User prompts were malformed; add stricter JSON schema validation.: JSON validation prevents format errors, not missing context from too-long inputs.

Misconception tags: context window overflow; parameter confusion

Source trace:

https://docs.aws.amazon.com/bedrock/latest/userguide/conversation.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Summarization and truncation control context window use, ensuring relevant turns are kept.
   Source: https://docs.aws.amazon.com/bedrock/latest/userguide/conversation.html
   Evidence span: If combined input exceeds the model’s token window, older content may be dropped.

### P1-AIP-D3-213

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-213 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.3: Implement data validation and processing pipelines for FM consumption. |
| `exam_skill` | Skill 1.3.3: Format input data for FM inference according to model-specific requirements (for example, by using JSON formatting for Amazon Bedrock API requests, structured data preparation for SageMaker AI endpoints, conversation formatting for dialog-based applications). |
| `secondary_exam_skills` | Skill 2.5.1: Create FM API interfaces to address the specific requirements of GenAI workloads (for example, by using API Gateway to handle streaming responses, token limit management, retry strategies to handle model timeouts).; Skill 5.2.1: Resolve content handling issues to ensure that necessary information is processed completely in FM interactions (for example, by using context window overflow diagnostics, dynamic chunking strategies, prompt design optimization, truncation-related error analysis). |
| `learning_unit` | Day03-order015 |
| `accelerated_day` | Day 3 |
| `topic` | Token limits, request validation, and response handling |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Declarative; Procedural; Causal |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | bedrock-model-parameters |
| `raw_source` | 2026-06-30T052440Z-openai-gpt-4.1-day-03-order015-top-up-12.md item 5 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T052440Z |
| `raw_run_id` | order015-top-up-12 |

Stem:

A GenAI batch processing pipeline combines system-generated text and user inputs to construct prompts for Bedrock model inference. After a recent update, the pipeline produces frequent validation failures with larger input payloads. Which debugging step is most likely to reveal the root cause?

Options:

1. Compare total token count (system + user input) to the FM model's maximum context window per request.
2. Check for incorrect AWS credentials in API Gateway.
3. Increase CloudWatch log verbosity for output responses.
4. Switch to synchronous mode to isolate processing delays.

Correct answer: Compare total token count (system + user input) to the FM model's maximum context window per request.

Rationale: Prompt construction must fit within model token limits; exceeding these limits causes request validation errors. Auditing token totals is key.

Distractors: Check for incorrect AWS credentials in API Gateway.: Credentials problems manifest as authentication errors, not validation errors tied to token limits.; Increase CloudWatch log verbosity for output responses.: More logging helps troubleshooting, but unless you check token limits you may not see the source.; Switch to synchronous mode to isolate processing delays.: Sync/async mode changes processing pattern but not context validation.

Misconception tags: validation errors vs infra errors; token count audit

Source trace:

https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Examining aggregate token usage (system plus user input) is essential to diagnose validation failures from exceeding the context window.
   Source: https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html
   Evidence span: The maximum context window includes all prompt components.

### P1-AIP-D3-214

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-214 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.3: Implement data validation and processing pipelines for FM consumption. |
| `exam_skill` | Skill 1.3.3: Format input data for FM inference according to model-specific requirements (for example, by using JSON formatting for Amazon Bedrock API requests, structured data preparation for SageMaker AI endpoints, conversation formatting for dialog-based applications). |
| `secondary_exam_skills` | Skill 2.5.1: Create FM API interfaces to address the specific requirements of GenAI workloads (for example, by using API Gateway to handle streaming responses, token limit management, retry strategies to handle model timeouts).; Skill 5.2.1: Resolve content handling issues to ensure that necessary information is processed completely in FM interactions (for example, by using context window overflow diagnostics, dynamic chunking strategies, prompt design optimization, truncation-related error analysis). |
| `learning_unit` | Day03-order015 |
| `accelerated_day` | Day 3 |
| `topic` | Token limits, request validation, and response handling |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Declarative; Procedural; Causal |
| `question_format` | multiple-response |
| `difficulty` | medium |
| `cognitive_demand` | implement |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | bedrock-conversation |
| `raw_source` | 2026-06-30T052440Z-openai-gpt-4.1-day-03-order015-top-up-12.md item 6 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T052440Z |
| `raw_run_id` | order015-top-up-12 |

Stem:

A conversational application using Bedrock is required to guarantee that user prompts are always accepted by the model without truncation or rejection. Which two actions most directly accomplish this for varied user message lengths? (Select TWO.)

Options:

1. Dynamically count tokens and pre-truncate input to fit within model limits.
2. Remove or summarize older conversation turns to prioritize current context.
3. Allow the model to automatically discard tokens beyond the context window.
4. Add API Gateway request validation with a fixed byte-size constraint instead of tokenwise.
5. Increase response temperature to encourage concise answers.

Correct answer: Dynamically count tokens and pre-truncate input to fit within model limits.; Remove or summarize older conversation turns to prioritize current context.

Rationale: Token-based truncation guarantees adherence to model limits, and summarizing/removing older turns maintains context relevance for variable-length inputs.

Distractors: Allow the model to automatically discard tokens beyond the context window.: Auto-discard may lead to unpredictable omissions and ignored key context.; Add API Gateway request validation with a fixed byte-size constraint instead of tokenwise.: Byte-size validation does not enforce actual model token constraints.; Increase response temperature to encourage concise answers.: Temperature influences randomness, not context/acceptance of long prompts.

Misconception tags: byte size vs token count; context management

Source trace:

https://docs.aws.amazon.com/bedrock/latest/userguide/conversation.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Both pre-truncation and historical summarization are the only consistent ways to stay within token limits when context and user message lengths vary.
   Source: https://docs.aws.amazon.com/bedrock/latest/userguide/conversation.html
   Evidence span: Best practice: maintain context by fitting conversation history and new input within the allowed token window.

### P1-AIP-D3-215

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-215 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.3: Implement data validation and processing pipelines for FM consumption. |
| `exam_skill` | Skill 1.3.3: Format input data for FM inference according to model-specific requirements (for example, by using JSON formatting for Amazon Bedrock API requests, structured data preparation for SageMaker AI endpoints, conversation formatting for dialog-based applications). |
| `secondary_exam_skills` | Skill 2.5.1: Create FM API interfaces to address the specific requirements of GenAI workloads (for example, by using API Gateway to handle streaming responses, token limit management, retry strategies to handle model timeouts).; Skill 5.2.1: Resolve content handling issues to ensure that necessary information is processed completely in FM interactions (for example, by using context window overflow diagnostics, dynamic chunking strategies, prompt design optimization, truncation-related error analysis). |
| `learning_unit` | Day03-order015 |
| `accelerated_day` | Day 3 |
| `topic` | Token limits, request validation, and response handling |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Declarative; Procedural; Causal |
| `question_format` | multiple-response |
| `difficulty` | hard |
| `cognitive_demand` | optimize |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | bedrock-conversation |
| `raw_source` | 2026-06-30T052440Z-openai-gpt-4.1-day-03-order015-top-up-12.md item 9 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T052440Z |
| `raw_run_id` | order015-top-up-12 |

Stem:

A conversation-aware Bedrock application must maintain context across user sessions while avoiding frequent context overflows and response truncations. Which two techniques will help you most reliably handle these challenges? (Select TWO.)

Options:

1. Implement rolling window context management with summarization of older turns.
2. Design prompts to include only recent exchanges when the token window nears its limit.
3. Disable all input validation to favor conversational flexibility.
4. Configure maximum output tokens to be half the input limit.
5. Automatically insert system warnings if the token window nears capacity.

Correct answer: Implement rolling window context management with summarization of older turns.; Design prompts to include only recent exchanges when the token window nears its limit.

Rationale: A rolling context strategy and limiting prompt history when near the token window cap both maximize context retention and minimize truncation.

Distractors: Disable all input validation to favor conversational flexibility.: Skipping validation increases errors and risks breaking the conversation flow.; Configure maximum output tokens to be half the input limit.: Output token limits must ensure space for answers but do not by themselves solve the context fitting issue.; Automatically insert system warnings if the token window nears capacity.: Warnings inform but do not solve context fitting or operational overflow.

Misconception tags: context truncation prevention; token management

Source trace:

https://docs.aws.amazon.com/bedrock/latest/userguide/conversation.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Both approaches keep conversation context within the allowed token scope for continuities and accurate responses.
   Source: https://docs.aws.amazon.com/bedrock/latest/userguide/conversation.html
   Evidence span: To avoid truncation, include only as much context as fits within the available window, using rolling history or summarization as needed.

### P1-AIP-D3-216

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-216 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.3: Implement data validation and processing pipelines for FM consumption. |
| `exam_skill` | Skill 1.3.3: Format input data for FM inference according to model-specific requirements (for example, by using JSON formatting for Amazon Bedrock API requests, structured data preparation for SageMaker AI endpoints, conversation formatting for dialog-based applications). |
| `secondary_exam_skills` | Skill 2.5.1: Create FM API interfaces to address the specific requirements of GenAI workloads (for example, by using API Gateway to handle streaming responses, token limit management, retry strategies to handle model timeouts).; Skill 5.2.1: Resolve content handling issues to ensure that necessary information is processed completely in FM interactions (for example, by using context window overflow diagnostics, dynamic chunking strategies, prompt design optimization, truncation-related error analysis). |
| `learning_unit` | Day03-order015 |
| `accelerated_day` | Day 3 |
| `topic` | Token limits, request validation, and response handling |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Declarative; Procedural; Causal |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | implement |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | bedrock-model-parameters |
| `raw_source` | 2026-06-30T052440Z-openai-gpt-4.1-day-03-order015-top-up-12.md item 10 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T052440Z |
| `raw_run_id` | order015-top-up-12 |

Stem:

A GenAI service team observes production requests to a Bedrock FM sometimes return a 400 validation error, while requests with similar but slightly shorter content always succeed. Which immediate validation check should they automate in their client library?

Options:

1. Token-counting each constructed prompt and enforcing the model’s documented token limit.
2. Adding an exponential backoff retry handler to absorb intermittent errors.
3. Forcing API requests to be synchronous only.
4. Appending a static system prompt to all requests for improved validation.

Correct answer: Token-counting each constructed prompt and enforcing the model’s documented token limit.

Rationale: Requests exceeding per-model token windows are systematically rejected; counting tokens prevents this error class.

Distractors: Adding an exponential backoff retry handler to absorb intermittent errors.: Retrying cannot overcome consistent and deterministic validation failures.; Forcing API requests to be synchronous only.: SYNC/ASYNC processing method does not change input validity.; Appending a static system prompt to all requests for improved validation.: A static prompt may improve structure or guidance but does not enforce token windows.

Misconception tags: retry vs prevention; system prompt misunderstanding

Source trace:

https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Token-counting is a direct and necessary method for guaranteeing model input fits within allowed limits.
   Source: https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html
   Evidence span: Maximum token limits are enforced on model input for each request.

### P1-AIP-D3-217

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-217 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.3: Implement data validation and processing pipelines for FM consumption. |
| `exam_skill` | Skill 1.3.3: Format input data for FM inference according to model-specific requirements (for example, by using JSON formatting for Amazon Bedrock API requests, structured data preparation for SageMaker AI endpoints, conversation formatting for dialog-based applications). |
| `secondary_exam_skills` | Skill 2.5.1: Create FM API interfaces to address the specific requirements of GenAI workloads (for example, by using API Gateway to handle streaming responses, token limit management, retry strategies to handle model timeouts).; Skill 5.2.1: Resolve content handling issues to ensure that necessary information is processed completely in FM interactions (for example, by using context window overflow diagnostics, dynamic chunking strategies, prompt design optimization, truncation-related error analysis). |
| `learning_unit` | Day03-order015 |
| `accelerated_day` | Day 3 |
| `topic` | Token limits, request validation, and response handling |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Declarative; Procedural; Causal |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | optimize |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | bedrock-model-parameters |
| `raw_source` | 2026-06-30T052440Z-openai-gpt-4.1-day-03-order015-top-up-12.md item 11 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T052440Z |
| `raw_run_id` | order015-top-up-12 |

Stem:

An LLM-integrated workflow on Bedrock processes user questions and multi-step task context for document generation. Developers see unexpected truncation of model outputs when large documents are involved. What adjustment should be prioritized for optimal output completeness?

Options:

1. Decrease the size of the context fed to the model or allocate more output tokens if supported.
2. Switch to an asynchronous submission strategy.
3. Enable streaming responses to prevent cutoff.
4. Set model temperature higher to encourage longer completions.

Correct answer: Decrease the size of the context fed to the model or allocate more output tokens if supported.

Rationale: Too much context leaves too few output tokens. Reducing input or increasing allowed output is necessary to avoid output truncation.

Distractors: Switch to an asynchronous submission strategy.: Submission model affects throughput, not output length for FM calls.; Enable streaming responses to prevent cutoff.: Streaming affects delivery timing, not allocated output token space.; Set model temperature higher to encourage longer completions.: Temperature adds randomness, not output length.

Misconception tags: output token mechanics; async/streaming confusion

Source trace:

https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Reducing input or increasing output allocation resolves truncation when output tokens are limited by window size.
   Source: https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html
   Evidence span: If the combined input/output token total exceeds the window, output is truncated.

### P1-AIP-D3-218

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-218 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.3: Implement data validation and processing pipelines for FM consumption. |
| `exam_skill` | Skill 1.3.3: Format input data for FM inference according to model-specific requirements (for example, by using JSON formatting for Amazon Bedrock API requests, structured data preparation for SageMaker AI endpoints, conversation formatting for dialog-based applications). |
| `secondary_exam_skills` | Skill 2.5.1: Create FM API interfaces to address the specific requirements of GenAI workloads (for example, by using API Gateway to handle streaming responses, token limit management, retry strategies to handle model timeouts).; Skill 5.2.1: Resolve content handling issues to ensure that necessary information is processed completely in FM interactions (for example, by using context window overflow diagnostics, dynamic chunking strategies, prompt design optimization, truncation-related error analysis). |
| `learning_unit` | Day03-order015 |
| `accelerated_day` | Day 3 |
| `topic` | Token limits, request validation, and response handling |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Declarative; Procedural; Causal |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | bedrock-model-parameters |
| `raw_source` | 2026-06-30T052440Z-openai-gpt-4.1-day-03-order015-top-up-12.md item 12 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T052440Z |
| `raw_run_id` | order015-top-up-12 |

Stem:

You implement a generic SaaS FM API client and want to guarantee that user submissions never lead to FM model rejection from input that is too long, regardless of client language. Which design pattern most effectively guarantees this requirement?

Options:

1. Integrate language-specific tokenization and maximum-token enforcement for each supported Bedrock FM as part of the client library.
2. Pass all user input directly and handle failures as they occur.
3. Increase the max HTTP payload size at the load balancer tier.
4. Hardcode string-length checks in each client, regardless of FM or language.

Correct answer: Integrate language-specific tokenization and maximum-token enforcement for each supported Bedrock FM as part of the client library.

Rationale: Tokenization is FM-specific and differs across languages; only accurate tokenization and enforcement can guarantee requests fit the model’s window.

Distractors: Pass all user input directly and handle failures as they occur.: This is reactive and allows preventable errors to reach FM APIs.; Increase the max HTTP payload size at the load balancer tier.: HTTP payload size is not related to token window enforcement.; Hardcode string-length checks in each client, regardless of FM or language.: String length is not synonymous with token count, which is what models enforce.

Misconception tags: token vs character count; API input workflow

Source trace:

https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Correct tokenization and checking are necessary and must be FM- and language-aware for robust client-side validation.
   Source: https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html
   Evidence span: Tokenization and max-token parameters depend on both the FM and the request language.

### P1-AIP-D3-219

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-219 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 2: Implementation and Integration |
| `exam_task` | Task 2.4: Implement FM API integrations. |
| `exam_skill` | Skill 2.4.3: Create resilient FM systems to ensure reliable operations (for example, by using the AWS SDK for exponential backoff, API Gateway to manage rate limiting, fallback mechanisms for graceful degradation, AWS X-Ray to provide observability across service boundaries). |
| `secondary_exam_skills` | Skill 2.5.6: Improve troubleshooting efficiency for FM applications (for example, by using CloudWatch Logs Insights to analyze prompts and responses, X-Ray to trace FM API calls, Amazon Q Developer to implement GenAI-specific error pattern recognition).; Skill 4.3.1: Create holistic observability systems to provide complete visibility into FM application performance (for example, by using operational metrics, performance tracing, FM interaction tracing, business impact metrics with custom dashboards). |
| `learning_unit` | Day03-order018 |
| `accelerated_day` | Day 3 |
| `topic` | Distributed tracing and FM API observability |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Diagnostic; Causal; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | xray-console |
| `raw_source` | 2026-06-30T052520Z-openai-gpt-4.1-day-03-order018-top-up-4.md item 1 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T052520Z |
| `raw_run_id` | order018-top-up-4 |

Stem:

A GenAI workflow uses AWS Lambda and AWS Bedrock in separate microservices. After rolling out a new FM model version, users report intermittent failures. CloudWatch dashboards show stable system resource metrics but increasing errors related to model invocation. You must rapidly pinpoint where failures originate, spanning several services. What is the most direct X-Ray console feature or workflow to use?

Options:

1. Use the X-Ray service map to visualize and filter traces by error status between microservices.
2. Download all raw trace JSON data for local log analysis.
3. Configure CloudWatch metric alarms for error rates on all Lambda functions.
4. Correlate CloudWatch Logs with Kinesis Data Streams real-time analytics.

Correct answer: Use the X-Ray service map to visualize and filter traces by error status between microservices.

Rationale: The X-Ray service map visually shows inter-service communication and error paths. Filtering by error status helps quickly identify where failures occur, even across service boundaries.

Distractors: Download all raw trace JSON data for local log analysis.: This approach is slow and reduces X-Ray's value. The scenario prioritizes rapid diagnosis, not manual analysis.; Configure CloudWatch metric alarms for error rates on all Lambda functions.: Metric alarms show error trends but do not quickly reveal cross-service failure paths or the upstream cause of failures.; Correlate CloudWatch Logs with Kinesis Data Streams real-time analytics.: Kinesis and CloudWatch Logs correlation is complex and indirect, not a direct or visual way to trace service-to-service failures.

Misconception tags: Mistaking metrics or alarms for trace-level causal analysis; Assuming log analytics can replace distributed visual tracing

Source trace:

https://docs.aws.amazon.com/xray/latest/devguide/xray-console.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The X-Ray service map's visualization and filtering capabilities allow for rapid identification of inter-service error origins, as described in the documentation.
   Source: https://docs.aws.amazon.com/xray/latest/devguide/xray-console.html
   Evidence span: The service map provides a visual representation of requests flowing through your application, including errors and latency between services.

### P1-AIP-D3-220

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-220 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 2: Implementation and Integration |
| `exam_task` | Task 2.4: Implement FM API integrations. |
| `exam_skill` | Skill 2.4.3: Create resilient FM systems to ensure reliable operations (for example, by using the AWS SDK for exponential backoff, API Gateway to manage rate limiting, fallback mechanisms for graceful degradation, AWS X-Ray to provide observability across service boundaries). |
| `secondary_exam_skills` | Skill 2.5.6: Improve troubleshooting efficiency for FM applications (for example, by using CloudWatch Logs Insights to analyze prompts and responses, X-Ray to trace FM API calls, Amazon Q Developer to implement GenAI-specific error pattern recognition).; Skill 4.3.1: Create holistic observability systems to provide complete visibility into FM application performance (for example, by using operational metrics, performance tracing, FM interaction tracing, business impact metrics with custom dashboards). |
| `learning_unit` | Day03-order018 |
| `accelerated_day` | Day 3 |
| `topic` | Distributed tracing and FM API observability |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Diagnostic; Causal; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | cloudwatch-dashboards |
| `raw_source` | 2026-06-30T052520Z-openai-gpt-4.1-day-03-order018-top-up-4.md item 2 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T052520Z |
| `raw_run_id` | order018-top-up-4 |

Stem:

A development team has configured CloudWatch dashboards for a GenAI API, but business stakeholders want to view both technical and business metrics in one place, including model latency and conversion rates from user queries. Which CloudWatch dashboard strategy most directly meets this requirement with minimal maintenance?

Options:

1. Add custom widgets that combine CloudWatch metrics (for latency) and business KPIs (from custom metrics) into a single dashboard.
2. Export all technical metrics to an external BI tool for full business visibility.
3. Rely solely on built-in AWS service dashboards, as these automatically include business indicators.
4. Set up alerts for model latency, emailing PDF reports of metrics to stakeholders weekly.

Correct answer: Add custom widgets that combine CloudWatch metrics (for latency) and business KPIs (from custom metrics) into a single dashboard.

Rationale: CloudWatch dashboards can include custom widgets aggregating both built-in and custom metrics, allowing technical and business data to be viewed together easily.

Distractors: Export all technical metrics to an external BI tool for full business visibility.: This introduces extra integration and maintenance overhead, rather than using native CloudWatch dashboard capabilities.; Rely solely on built-in AWS service dashboards, as these automatically include business indicators.: Service dashboards only cover technical metrics; they do not automatically display application-specific business KPIs.; Set up alerts for model latency, emailing PDF reports of metrics to stakeholders weekly.: Emailing reports with alerts is not interactive or real-time and does not give stakeholders unified access.

Misconception tags: Assuming native dashboards auto-aggregate all business data; Believing export to BI tool is simpler than native widgets

Source trace:

https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Combining custom and built-in widgets on CloudWatch dashboards directly enables mixed visibility as outlined in the documentation.
   Source: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html
   Evidence span: You can add custom widgets to your dashboard to display your own metrics, business KPIs, and graphs for your application.

### P1-AIP-D3-221

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-221 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 2: Implementation and Integration |
| `exam_task` | Task 2.4: Implement FM API integrations. |
| `exam_skill` | Skill 2.4.3: Create resilient FM systems to ensure reliable operations (for example, by using the AWS SDK for exponential backoff, API Gateway to manage rate limiting, fallback mechanisms for graceful degradation, AWS X-Ray to provide observability across service boundaries). |
| `secondary_exam_skills` | Skill 2.5.6: Improve troubleshooting efficiency for FM applications (for example, by using CloudWatch Logs Insights to analyze prompts and responses, X-Ray to trace FM API calls, Amazon Q Developer to implement GenAI-specific error pattern recognition).; Skill 4.3.1: Create holistic observability systems to provide complete visibility into FM application performance (for example, by using operational metrics, performance tracing, FM interaction tracing, business impact metrics with custom dashboards). |
| `learning_unit` | Day03-order018 |
| `accelerated_day` | Day 3 |
| `topic` | Distributed tracing and FM API observability |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Diagnostic; Causal; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | xray-console |
| `raw_source` | 2026-06-30T052520Z-openai-gpt-4.1-day-03-order018-top-up-4.md item 3 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T052520Z |
| `raw_run_id` | order018-top-up-4 |

Stem:

You're building an end-to-end GenAI application where latency spikes are hard to diagnose because some API calls are external, and others are to AWS services. What sequence of actions in the X-Ray console helps you most efficiently distinguish between external dependency bottlenecks and AWS service delays affecting the FM pipeline?

Options:

1. In the X-Ray trace details, use the timeline and annotation panes to compare durations of downstream AWS services and external API segments.
2. Only use X-Ray error filter expressions to surface failed traces, ignoring successful calls.
3. Rely on CloudWatch dashboard summary widgets to infer external vs. internal latency causes.
4. Configure CloudWatch alarms for each Lambda and FM invocation, and assume the service with the greatest number of alarms is the cause.

Correct answer: In the X-Ray trace details, use the timeline and annotation panes to compare durations of downstream AWS services and external API segments.

Rationale: The X-Ray trace timeline and annotation panes provide detailed breakdowns of all segment durations, making it possible to pinpoint which calls are responsible for latency, whether AWS or external.

Distractors: Only use X-Ray error filter expressions to surface failed traces, ignoring successful calls.: This misses investigating slow but successful traces, which may identify bottlenecks not generating exceptions.; Rely on CloudWatch dashboard summary widgets to infer external vs. internal latency causes.: CloudWatch dashboards lack per-request trace granularity needed to attribute specific latency to AWS or external services.; Configure CloudWatch alarms for each Lambda and FM invocation, and assume the service with the greatest number of alarms is the cause.: Alarm volume does not provide direct evidence for which service is creating latency; it may reflect error frequency but not duration or cause.

Misconception tags: Mistaking error rate for latency source; Assuming dashboards show per-request segment duration; Neglecting analysis of successful slow traces

Source trace:

https://docs.aws.amazon.com/xray/latest/devguide/xray-console.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: The X-Ray trace detail view, with its timing and annotation panes, provides the needed breakdown to distinguish bottlenecks by segment—a documented capability.
   Source: https://docs.aws.amazon.com/xray/latest/devguide/xray-console.html
   Evidence span: A trace timeline helps you identify the timing and duration of each downstream call made by your application, including external calls and AWS services.

### P1-AIP-D3-222

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D3-222 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 2: Implementation and Integration |
| `exam_task` | Task 2.4: Implement FM API integrations. |
| `exam_skill` | Skill 2.4.3: Create resilient FM systems to ensure reliable operations (for example, by using the AWS SDK for exponential backoff, API Gateway to manage rate limiting, fallback mechanisms for graceful degradation, AWS X-Ray to provide observability across service boundaries). |
| `secondary_exam_skills` | Skill 2.5.6: Improve troubleshooting efficiency for FM applications (for example, by using CloudWatch Logs Insights to analyze prompts and responses, X-Ray to trace FM API calls, Amazon Q Developer to implement GenAI-specific error pattern recognition).; Skill 4.3.1: Create holistic observability systems to provide complete visibility into FM application performance (for example, by using operational metrics, performance tracing, FM interaction tracing, business impact metrics with custom dashboards). |
| `learning_unit` | Day03-order018 |
| `accelerated_day` | Day 3 |
| `topic` | Distributed tracing and FM API observability |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Diagnostic; Causal; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-30 |
| `source_trace_status` | needs-final-source-check |
| `source_contract_version` | source-grounded-v1 |
| `allowed_source_id` | cloudwatch-dashboards |
| `raw_source` | 2026-06-30T052520Z-openai-gpt-4.1-day-03-order018-top-up-4.md item 4 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-30T052520Z |
| `raw_run_id` | order018-top-up-4 |

Stem:

A GenAI team is introducing a new business metric for user engagement and wants to track it side-by-side with FM-specific latency and error metrics, surfacing all in a unified monitoring interface with drill-down capability for operators. What is the best CloudWatch dashboard design pattern to recommend?

Options:

1. Define a custom metric for user engagement and add it as a separate graph alongside FM latency and error metrics in the same CloudWatch dashboard.
2. Send the user engagement metric to Amazon SNS and link CloudWatch dashboards by alarm name.
3. Use only prebuilt CloudWatch metrics; customize dashboard colors to differentiate engagement from latency/error metrics.
4. Aggregate all business and technical metrics into a single CloudWatch composite alarm and display alarm state history.

Correct answer: Define a custom metric for user engagement and add it as a separate graph alongside FM latency and error metrics in the same CloudWatch dashboard.

Rationale: CloudWatch dashboards allow display of any custom or built-in metric in user-defined widgets. This makes it straightforward to visualize business and technical metrics side-by-side with drill-down support.

Distractors: Send the user engagement metric to Amazon SNS and link CloudWatch dashboards by alarm name.: SNS is for notifications, not metric display or dashboard integration.; Use only prebuilt CloudWatch metrics; customize dashboard colors to differentiate engagement from latency/error metrics.: Engagement requires a custom metric, and color changes alone can't add new data for visualization.; Aggregate all business and technical metrics into a single CloudWatch composite alarm and display alarm state history.: Composite alarms only show status and cannot display trends or values for business and technical metrics together.

Misconception tags: Assuming alarms and SNS can replace custom metrics in dashboards; Thinking dashboard color coding adds missing metrics

Source trace:

https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day-03-answer-guidance.md

Atomic claims:

1. Claim: Adding custom metrics to CloudWatch dashboards allows visualization of both business and FM performance data in a unified, interactive interface.
   Source: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html
   Evidence span: You can display multiple metrics in a dashboard...including custom business metrics, all in the same dashboard for an application.

## Culled Items

| Raw source | Curriculum order | Stem excerpt | Reasons | Evidence |
|---|---|---|---|---|
| `2026-06-30T051656Z-openai-gpt-4.1-day-03-order010.md item 3` | Day03-order010 | A developer is tasked with verifying that recent prompt updates for a finance chatbot do not cause failures on previously functioning que... | keyword-trivia stem | keyword-trivia stem: matched weak stem pattern(s): which aws service; stem="A developer is tasked with verifying that recent prompt updates for a finance chatbot do not cause failures on previously functioning queries. Which AWS service combination is most suitable for automating regression checks at scale?" |
| `2026-06-30T051656Z-openai-gpt-4.1-day-03-order010.md item 8` | Day03-order010 | A company wants to automate prompt regression testing for all prompt template changes but also wants to collect and analyze statistics on... | keyword-trivia stem | keyword-trivia stem: matched weak stem pattern(s): which aws service; stem="A company wants to automate prompt regression testing for all prompt template changes but also wants to collect and analyze statistics on test results over time. Which AWS services should be used together for this goal? (Select TWO.)" |
| `2026-06-30T051656Z-openai-gpt-4.1-day-03-order010.md item 10` | Day03-order010 | Which feature of prompt regression testing is most essential in preventing repeated introduction of old errors when prompt designs evolve... | schema defect, source-grounding defect | schema defect: source_trace must use official AWS docs URLs, resolving local docs/... paths, the canonical objectives JSON, or explicit NONE/source_trace_needed<br>schema defect: source_trace references non-resolving local path(s): docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day03-order010-prompt-regression-testing-quality-assurance.md<br>source-grounding defect: source_contract_version=''<br>source-grounding defect: allowed_source_id is not in allowlist: ''<br>source-grounding defect: atomic_claims[1].source is not in topic allowlist: 'docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day03-order010-prompt-regression-testing-quality-assurance.md' |
| `2026-06-30T051656Z-openai-gpt-4.1-day-03-order010.md item 11` | Day03-order010 | A downstream application throws exceptions after a new prompt template is deployed, even though prompt regression tests passed on expecte... | schema defect, source-grounding defect | schema defect: source_trace must use official AWS docs URLs, resolving local docs/... paths, the canonical objectives JSON, or explicit NONE/source_trace_needed<br>schema defect: source_trace references non-resolving local path(s): docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day03-order010-prompt-regression-testing-quality-assurance.md<br>source-grounding defect: source_contract_version=''<br>source-grounding defect: allowed_source_id is not in allowlist: ''<br>source-grounding defect: atomic_claims[1].source is not in topic allowlist: 'docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day03-order010-prompt-regression-testing-quality-assurance.md' |
| `2026-06-30T051656Z-openai-gpt-4.1-day-03-order010.md item 12` | Day03-order010 | Which two practices most effectively minimize risk and maintain confidence in the quality of prompts before every GenAI service productio... | schema defect, source-grounding defect | schema defect: source_trace must use official AWS docs URLs, resolving local docs/... paths, the canonical objectives JSON, or explicit NONE/source_trace_needed<br>schema defect: source_trace references non-resolving local path(s): docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day03-order010-prompt-regression-testing-quality-assurance.md<br>source-grounding defect: source_contract_version=''<br>source-grounding defect: allowed_source_id is not in allowlist: ''<br>source-grounding defect: atomic_claims[1].source is not in topic allowlist: 'docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day03-order010-prompt-regression-testing-quality-assurance.md' |
| `2026-06-30T051656Z-openai-gpt-4.1-day-03-order010.md item 13` | Day03-order010 | Your team leverages CI/CD to deploy new prompt templates for a smart legal assistant on a weekly cadence. Which QA control is BEST to inc... | schema defect, source-grounding defect | schema defect: source_trace must use official AWS docs URLs, resolving local docs/... paths, the canonical objectives JSON, or explicit NONE/source_trace_needed<br>schema defect: source_trace references non-resolving local path(s): docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day03-order010-prompt-regression-testing-quality-assurance.md<br>source-grounding defect: source_contract_version=''<br>source-grounding defect: allowed_source_id is not in allowlist: ''<br>source-grounding defect: atomic_claims[1].source is not in topic allowlist: 'docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day03-order010-prompt-regression-testing-quality-assurance.md' |
| `2026-06-30T051823Z-openai-gpt-4.1-day-03-order012.md item 12` | Day03-order012 | You are tasked with implementing a production-grade synchronous FM API: API Gateway sits in front of a Lambda function which calls Bedroc... | schema defect, source-grounding defect | schema defect: source_trace must use official AWS docs URLs, resolving local docs/... paths, the canonical objectives JSON, or explicit NONE/source_trace_needed<br>schema defect: source_trace references non-resolving local path(s): docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day03-order012-synchronous-fm-api-integration.md<br>source-grounding defect: source_contract_version=''<br>source-grounding defect: allowed_source_id is not in allowlist: ''<br>source-grounding defect: atomic_claims[1].source is not in topic allowlist: 'docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day03-order012-synchronous-fm-api-integration.md' |
| `2026-06-30T051911Z-openai-gpt-4.1-day-03-order013.md item 2` | Day03-order013 | An AWS developer is tasked with orchestrating a multi-stage asynchronous generative AI workflow that requires integrating Bedrock API cal... | keyword-trivia stem | keyword-trivia stem: matched weak stem pattern(s): which aws service; stem="An AWS developer is tasked with orchestrating a multi-stage asynchronous generative AI workflow that requires integrating Bedrock API calls, document parsing, and post-processing in a fault-tolerant way. Which AWS service or pattern BEST supports this requi..." |
| `2026-06-30T052035Z-openai-gpt-4.1-day-03-order015.md item 1` | Day03-order015 | A financial advice chatbot using Amazon Bedrock begins returning truncated responses when complex user questions are submitted. The FM is... | schema defect, source-grounding defect | schema defect: source_trace must use official AWS docs URLs, resolving local docs/... paths, the canonical objectives JSON, or explicit NONE/source_trace_needed<br>schema defect: source_trace references non-resolving local path(s): docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day03-order015-token-limits-request-validation-response-handling.md<br>source-grounding defect: source_contract_version=''<br>source-grounding defect: allowed_source_id is not in allowlist: ''<br>source-grounding defect: atomic_claims[1].source is not in topic allowlist: 'docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day03-order015-token-limits-request-validation-response-handling.md' |
| `2026-06-30T052035Z-openai-gpt-4.1-day-03-order015.md item 2` | Day03-order015 | Your API client for Bedrock models is occasionally returning 400 errors when submitting requests with large documents as context. The mod... | schema defect, source-grounding defect | schema defect: source_trace must use official AWS docs URLs, resolving local docs/... paths, the canonical objectives JSON, or explicit NONE/source_trace_needed<br>schema defect: source_trace references non-resolving local path(s): docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day03-order015-token-limits-request-validation-response-handling.md<br>source-grounding defect: source_contract_version=''<br>source-grounding defect: allowed_source_id is not in allowlist: ''<br>source-grounding defect: atomic_claims[1].source is not in topic allowlist: 'docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day03-order015-token-limits-request-validation-response-handling.md' |
| `2026-06-30T052035Z-openai-gpt-4.1-day-03-order015.md item 3` | Day03-order015 | A GenAI application forwards complex user queries and their full conversation context to an Amazon Bedrock FM. Users report that the mode... | schema defect, source-grounding defect | schema defect: source_trace must use official AWS docs URLs, resolving local docs/... paths, the canonical objectives JSON, or explicit NONE/source_trace_needed<br>schema defect: source_trace references non-resolving local path(s): docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day03-order015-token-limits-request-validation-response-handling.md<br>source-grounding defect: source_contract_version=''<br>source-grounding defect: allowed_source_id is not in allowlist: ''<br>source-grounding defect: atomic_claims[1].source is not in topic allowlist: 'docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day03-order015-token-limits-request-validation-response-handling.md' |
| `2026-06-30T052035Z-openai-gpt-4.1-day-03-order015.md item 4` | Day03-order015 | When integrating a new FM endpoint in Bedrock, your QA workflow must check that all input prompts are properly formatted and validated be... | schema defect, source-grounding defect | schema defect: source_trace must use official AWS docs URLs, resolving local docs/... paths, the canonical objectives JSON, or explicit NONE/source_trace_needed<br>schema defect: source_trace references non-resolving local path(s): docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day03-order015-token-limits-request-validation-response-handling.md<br>source-grounding defect: source_contract_version=''<br>source-grounding defect: allowed_source_id is not in allowlist: ''<br>source-grounding defect: atomic_claims[1].source is not in topic allowlist: 'docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day03-order015-token-limits-request-validation-response-handling.md' |
| `2026-06-30T052035Z-openai-gpt-4.1-day-03-order015.md item 5` | Day03-order015 | A Bedrock-powered generative API is experiencing inconsistent behavior: some requests are rejected with a message about exceeding the con... | schema defect, source-grounding defect | schema defect: source_trace must use official AWS docs URLs, resolving local docs/... paths, the canonical objectives JSON, or explicit NONE/source_trace_needed<br>schema defect: source_trace references non-resolving local path(s): docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day03-order015-token-limits-request-validation-response-handling.md<br>source-grounding defect: source_contract_version=''<br>source-grounding defect: allowed_source_id is not in allowlist: ''<br>source-grounding defect: atomic_claims[1].source is not in topic allowlist: 'docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day03-order015-token-limits-request-validation-response-handling.md' |
| `2026-06-30T052035Z-openai-gpt-4.1-day-03-order015.md item 6` | Day03-order015 | You are designing a prompt management workflow for a customer service bot using Bedrock FMs. The support staff sometimes request that out... | schema defect, source-grounding defect | schema defect: source_trace must use official AWS docs URLs, resolving local docs/... paths, the canonical objectives JSON, or explicit NONE/source_trace_needed<br>schema defect: source_trace references non-resolving local path(s): docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day03-order015-token-limits-request-validation-response-handling.md<br>source-grounding defect: source_contract_version=''<br>source-grounding defect: allowed_source_id is not in allowlist: ''<br>source-grounding defect: atomic_claims[1].source is not in topic allowlist: 'docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day03-order015-token-limits-request-validation-response-handling.md' |
| `2026-06-30T052035Z-openai-gpt-4.1-day-03-order015.md item 8` | Day03-order015 | You are troubleshooting a GenAI application using Bedrock and discover that when prompts include large code examples, responses are delay... | schema defect, source-grounding defect | schema defect: source_trace must use official AWS docs URLs, resolving local docs/... paths, the canonical objectives JSON, or explicit NONE/source_trace_needed<br>schema defect: source_trace references non-resolving local path(s): docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day03-order015-token-limits-request-validation-response-handling.md<br>source-grounding defect: source_contract_version=''<br>source-grounding defect: allowed_source_id is not in allowlist: ''<br>source-grounding defect: atomic_claims[1].source is not in topic allowlist: 'docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day03-order015-token-limits-request-validation-response-handling.md' |
| `2026-06-30T052035Z-openai-gpt-4.1-day-03-order015.md item 9` | Day03-order015 | A GenAI developer is integrating Bedrock and must design robust error handling for content window overflow and request validation failure... | schema defect, source-grounding defect | schema defect: source_trace must use official AWS docs URLs, resolving local docs/... paths, the canonical objectives JSON, or explicit NONE/source_trace_needed<br>schema defect: source_trace references non-resolving local path(s): docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day03-order015-token-limits-request-validation-response-handling.md<br>source-grounding defect: source_contract_version=''<br>source-grounding defect: allowed_source_id is not in allowlist: ''<br>source-grounding defect: atomic_claims[1].source is not in topic allowlist: 'docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day03-order015-token-limits-request-validation-response-handling.md' |
| `2026-06-30T052035Z-openai-gpt-4.1-day-03-order015.md item 10` | Day03-order015 | A Bedrock-based QA chatbot receives occasional complaints that important citation links are missing in the returned answers whenever the ... | schema defect, source-grounding defect | schema defect: source_trace must use official AWS docs URLs, resolving local docs/... paths, the canonical objectives JSON, or explicit NONE/source_trace_needed<br>schema defect: source_trace references non-resolving local path(s): docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day03-order015-token-limits-request-validation-response-handling.md<br>source-grounding defect: source_contract_version=''<br>source-grounding defect: allowed_source_id is not in allowlist: ''<br>source-grounding defect: atomic_claims[1].source is not in topic allowlist: 'docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day03-order015-token-limits-request-validation-response-handling.md' |
| `2026-06-30T052035Z-openai-gpt-4.1-day-03-order015.md item 11` | Day03-order015 | While developing an FM-powered summarization endpoint, you want to validate that your client will always reject requests that could trigg... | schema defect, source-grounding defect | schema defect: source_trace must use official AWS docs URLs, resolving local docs/... paths, the canonical objectives JSON, or explicit NONE/source_trace_needed<br>schema defect: source_trace references non-resolving local path(s): docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day03-order015-token-limits-request-validation-response-handling.md<br>source-grounding defect: source_contract_version=''<br>source-grounding defect: allowed_source_id is not in allowlist: ''<br>source-grounding defect: atomic_claims[1].source is not in topic allowlist: 'docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day03-order015-token-limits-request-validation-response-handling.md' |
| `2026-06-30T052035Z-openai-gpt-4.1-day-03-order015.md item 12` | Day03-order015 | A workflow using Bedrock repeatedly returns authentication errors for seemingly well-formed requests. Upon closer inspection, developers ... | schema defect, source-grounding defect | schema defect: source_trace must use official AWS docs URLs, resolving local docs/... paths, the canonical objectives JSON, or explicit NONE/source_trace_needed<br>schema defect: source_trace references non-resolving local path(s): docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day03-order015-token-limits-request-validation-response-handling.md<br>source-grounding defect: source_contract_version=''<br>source-grounding defect: allowed_source_id is not in allowlist: ''<br>source-grounding defect: atomic_claims[1].source is not in topic allowlist: 'docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day03-order015-token-limits-request-validation-response-handling.md' |
| `2026-06-30T052035Z-openai-gpt-4.1-day-03-order015.md item 13` | Day03-order015 | You are asked to improve an internal GenAI FAQ tool built on Bedrock FMs, which occasionally skips over important sections of a long inpu... | schema defect, source-grounding defect | schema defect: source_trace must use official AWS docs URLs, resolving local docs/... paths, the canonical objectives JSON, or explicit NONE/source_trace_needed<br>schema defect: source_trace references non-resolving local path(s): docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day03-order015-token-limits-request-validation-response-handling.md<br>source-grounding defect: source_contract_version=''<br>source-grounding defect: allowed_source_id is not in allowlist: ''<br>source-grounding defect: atomic_claims[1].source is not in topic allowlist: 'docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day03-order015-token-limits-request-validation-response-handling.md' |
| `2026-06-30T052243Z-openai-gpt-4.1-day-03-order018.md item 3` | Day03-order018 | A FinTech company running a multi-step FM workflow notices that several transaction-related API calls sometimes fail, but the missing tra... | keyword-trivia stem | keyword-trivia stem: matched weak stem pattern(s): which aws service; stem="A FinTech company running a multi-step FM workflow notices that several transaction-related API calls sometimes fail, but the missing transactions are not traceable in logs. You need to enable distributed tracing to visualize end-to-end user journeys and sp..." |
| `2026-06-30T052243Z-openai-gpt-4.1-day-03-order018.md item 5` | Day03-order018 | Your team manages a Bedrock-integrated AI platform running on multiple AWS regions. They want to ensure traceability and observability ac... | schema defect, source-grounding defect | schema defect: source_trace must use official AWS docs URLs, resolving local docs/... paths, the canonical objectives JSON, or explicit NONE/source_trace_needed<br>schema defect: source_trace references non-resolving local path(s): docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day03-order018-distributed-tracing-fm-api-observability.md<br>source-grounding defect: source_contract_version=''<br>source-grounding defect: allowed_source_id is not in allowlist: ''<br>source-grounding defect: atomic_claims[1].source is not in topic allowlist: 'docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day03-order018-distributed-tracing-fm-api-observability.md' |
| `2026-06-30T052243Z-openai-gpt-4.1-day-03-order018.md item 9` | Day03-order018 | Your FM-powered microservices architecture emits large volumes of application and API logs. The operations team wants real-time alerts wh... | schema defect, source-grounding defect | schema defect: source_trace must use official AWS docs URLs, resolving local docs/... paths, the canonical objectives JSON, or explicit NONE/source_trace_needed<br>schema defect: source_trace references non-resolving local path(s): docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day03-order018-distributed-tracing-fm-api-observability.md<br>source-grounding defect: source_contract_version=''<br>source-grounding defect: allowed_source_id is not in allowlist: ''<br>source-grounding defect: atomic_claims[1].source is not in topic allowlist: 'docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day03-order018-distributed-tracing-fm-api-observability.md' |
| `2026-06-30T052243Z-openai-gpt-4.1-day-03-order018.md item 10` | Day03-order018 | A distributed RAG application’s API latency suddenly increases. You observe longer duration segments in the X-Ray segment timeline, parti... | schema defect, source-grounding defect | schema defect: source_trace must use official AWS docs URLs, resolving local docs/... paths, the canonical objectives JSON, or explicit NONE/source_trace_needed<br>schema defect: source_trace references non-resolving local path(s): docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day03-order018-distributed-tracing-fm-api-observability.md<br>source-grounding defect: source_contract_version=''<br>source-grounding defect: allowed_source_id is not in allowlist: ''<br>source-grounding defect: atomic_claims[1].source is not in topic allowlist: 'docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day03-order018-distributed-tracing-fm-api-observability.md' |
| `2026-06-30T052243Z-openai-gpt-4.1-day-03-order018.md item 11` | Day03-order018 | Your monitoring solution for a distributed generative AI pipeline must provide both real-time visual feedback for operators and support a... | schema defect, source-grounding defect | schema defect: source_trace must use official AWS docs URLs, resolving local docs/... paths, the canonical objectives JSON, or explicit NONE/source_trace_needed<br>schema defect: source_trace references non-resolving local path(s): docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day03-order018-distributed-tracing-fm-api-observability.md<br>source-grounding defect: source_contract_version=''<br>source-grounding defect: allowed_source_id is not in allowlist: ''<br>source-grounding defect: atomic_claims[1].source is not in topic allowlist: 'docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day03-order018-distributed-tracing-fm-api-observability.md' |
| `2026-06-30T052440Z-openai-gpt-4.1-day-03-order015-top-up-12.md item 2` | Day03-order015 | A GenAI developer is integrating Bedrock's conversation API for a knowledge assistant. They want to ensure each API request is validated ... | schema defect, source-grounding defect | schema defect: source_trace must use official AWS docs URLs, resolving local docs/... paths, the canonical objectives JSON, or explicit NONE/source_trace_needed<br>schema defect: source_trace references non-resolving local path(s): docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day03-order015-token-limits-request-validation-response-handling.md<br>source-grounding defect: source_contract_version=''<br>source-grounding defect: allowed_source_id is not in allowlist: ''<br>source-grounding defect: atomic_claims[1].source is not in topic allowlist: 'docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day03-order015-token-limits-request-validation-response-handling.md' |
| `2026-06-30T052440Z-openai-gpt-4.1-day-03-order015-top-up-12.md item 7` | Day03-order015 | You’re building a Bedrock GenAI endpoint for business draft generation. User complaints indicate the API sometimes rejects requests with ... | schema defect, source-grounding defect | schema defect: source_trace must use official AWS docs URLs, resolving local docs/... paths, the canonical objectives JSON, or explicit NONE/source_trace_needed<br>schema defect: source_trace references non-resolving local path(s): docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day03-order015-token-limits-request-validation-response-handling.md<br>source-grounding defect: source_contract_version=''<br>source-grounding defect: allowed_source_id is not in allowlist: ''<br>source-grounding defect: atomic_claims[1].source is not in topic allowlist: 'docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day03-order015-token-limits-request-validation-response-handling.md' |
| `2026-06-30T052440Z-openai-gpt-4.1-day-03-order015-top-up-12.md item 8` | Day03-order015 | During prompt testing for an FAQ support bot using Bedrock, you notice that several requests with complex input structures are accepted b... | schema defect, source-grounding defect | schema defect: source_trace must use official AWS docs URLs, resolving local docs/... paths, the canonical objectives JSON, or explicit NONE/source_trace_needed<br>schema defect: source_trace references non-resolving local path(s): docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day03-order015-token-limits-request-validation-response-handling.md<br>source-grounding defect: source_contract_version=''<br>source-grounding defect: allowed_source_id is not in allowlist: ''<br>source-grounding defect: atomic_claims[1].source is not in topic allowlist: 'docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day03-order015-token-limits-request-validation-response-handling.md' |
