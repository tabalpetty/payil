# Day 2 Reviewed Candidate Bank

## Review Status

This file is a review/cull pass over normalized draft candidates.
Items marked `reviewed` passed automated schema, scenario, duplicate,
and stale/risky-claim checks, but still require the final source and
coverage gates before being treated as approved question-bank content.

Review date: 2026-06-23
Input: `docs/Pilot1/aip-c01/exam-prep/reviewed/day-02/day-02-normalized-draft-question-bank.md`
Machine-readable feedback: `docs/Pilot1/aip-c01/exam-prep/reviewed/day-02/day-02-review-feedback.json`

## Review Summary

| Curriculum order | Raw normalized | Reviewed candidates | Culled | Completion target | Status |
|---|---:|---:|---:|---:|---|
| Day02-order001 | 13 | 12 | 1 | 10 | candidate-complete |
| Day02-order002 | 15 | 12 | 3 | 10 | candidate-complete |
| Day02-order003 | 12 | 12 | 0 | 10 | candidate-complete |
| Day02-order004 | 13 | 11 | 2 | 10 | candidate-complete |
| Day02-order005 | 12 | 12 | 0 | 10 | candidate-complete |
| Day02-order006 | 12 | 12 | 0 | 10 | candidate-complete |
| Day02-order007 | 12 | 11 | 1 | 10 | candidate-complete |
| Day02-order008 | 13 | 13 | 0 | 10 | candidate-complete |
| Day02-order009 | 12 | 12 | 0 | 10 | candidate-complete |
| Day02-order010 | 17 | 12 | 5 | 10 | candidate-complete |

## Prompt Improvement Signals

| Failure reason | Count | Prompt adjustment |
|---|---:|---|
| unsupported high-risk claim | 8 | Ask the generator to avoid high-risk service-capability claims unless it cites an exact official source for review. |
| keyword-trivia stem | 4 | Ban glossary-style or service-name stems; require a professional scenario with a constraint-driven decision. |
| stale or risky technical claim | 1 | Avoid dated or capability-boundary claims unless the exact current AWS source is provided. |

## Top-Up Guidance

| Curriculum order | Reviewed candidates | Deficit to 10 | Recommended raw top-up |
|---|---:|---:|---:|
| Day02-order001 | 12 | 0 | 0 |
| Day02-order002 | 12 | 0 | 0 |
| Day02-order003 | 12 | 0 | 0 |
| Day02-order004 | 11 | 0 | 0 |
| Day02-order005 | 12 | 0 | 0 |
| Day02-order006 | 12 | 0 | 0 |
| Day02-order007 | 11 | 0 | 0 |
| Day02-order008 | 13 | 0 | 0 |
| Day02-order009 | 12 | 0 | 0 |
| Day02-order010 | 12 | 0 | 0 |

## Review Rules Applied

- Required schema fields must be present after normalization.
- Stems must be scenario-based and avoid keyword-trivia patterns.
- `easy` and `recall` items are culled.
- Exact and near-duplicate stems are culled within the same curriculum-order topic.
- Duplicate culls include both the rejected stem and matched reviewed stem.
- Dated, stale, or high-risk unsupported service-capability claims are culled.
- Source traces and remediation targets must be present; final source verification remains a later gate.

## Reviewed Candidates

### P1-AIP-D2-001

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-001 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.3: Implement data validation and processing pipelines for FM consumption. |
| `exam_skill` | Skill 1.3.1: Create comprehensive data validation workflows to ensure data meets quality standards for FM consumption (for example, by using AWS Glue Data Quality, SageMaker Data Wrangler, custom Lambda functions, Amazon CloudWatch metrics). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day02-order001 |
| `accelerated_day` | Day 2 |
| `topic` | Data-quality validation and monitoring |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Causal; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T051527Z-openai-gpt-4.1-day-02-order001.md item 1 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T051527Z |
| `raw_run_id` | order001 |

Stem:

A data engineering team uses AWS Glue Data Quality to validate customer purchase records before feeding them to a foundation model for personalized recommendations. The model’s output quality has degraded, and monitoring dashboards show a recent spike in missing values for key columns, but no schema drift. Which action should the team take FIRST?

Options:

1. Investigate and remediate the data source responsible for the missing values.
2. Increase the sample size in Glue Data Quality checks.
3. Retrain the foundation model with more recent data.
4. Fine-tune the Glue job to ignore missing values during processing.

Correct answer: Investigate and remediate the data source responsible for the missing values.

Rationale: Addressing the root cause of the missing values in the data source is the logical first step before any downstream retraining or pipeline changes.

Distractors: Increase the sample size in Glue Data Quality checks.: Increasing sample size can help catch issues but does not address the spike in missing values, which is already observed.; Retrain the foundation model with more recent data.: Retraining with flawed data perpetuates or worsens the problem, instead of fixing it.; Fine-tune the Glue job to ignore missing values during processing.: Ignoring missing values might degrade model performance further, not solve the quality issue.

Misconception tags: Ignoring upstream data quality issues; Premature model blaming

Source trace:

AWS Glue Data Quality documentation for handling missing values; focused artifact

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order001-data-quality-validation-monitoring.md

### P1-AIP-D2-002

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-002 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.3: Implement data validation and processing pipelines for FM consumption. |
| `exam_skill` | Skill 1.3.1: Create comprehensive data validation workflows to ensure data meets quality standards for FM consumption (for example, by using AWS Glue Data Quality, SageMaker Data Wrangler, custom Lambda functions, Amazon CloudWatch metrics). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day02-order001 |
| `accelerated_day` | Day 2 |
| `topic` | Data-quality validation and monitoring |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Causal; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T051527Z-openai-gpt-4.1-day-02-order001.md item 3 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T051527Z |
| `raw_run_id` | order001 |

Stem:

During data exploration, your team notices that SageMaker Data Wrangler’s data quality report for the training dataset highlights outlier values in several numeric columns, not previously flagged in the raw S3 files. Which is the MOST likely explanation?

Options:

1. Data Wrangler applies additional statistical validation beyond schema checks.
2. The raw data in S3 does not support profiling outlier values.
3. SageMaker Data Wrangler cannot read S3 data directly.
4. The outliers are only introduced during data processing in Data Wrangler.

Correct answer: Data Wrangler applies additional statistical validation beyond schema checks.

Rationale: SageMaker Data Wrangler provides advanced profiling, detecting not only basic schema violations but also distributional anomalies like outliers.

Distractors: The raw data in S3 does not support profiling outlier values.: Profiling isn’t a property of the storage format; S3 is agnostic—it’s the tool that detects outliers.; SageMaker Data Wrangler cannot read S3 data directly.: Data Wrangler is designed to import data from S3 among other sources.; The outliers are only introduced during data processing in Data Wrangler.: The outliers most likely exist in the raw data; Data Wrangler merely detects them.

Misconception tags: Confusing storage with content semantics; Blaming the tool rather than understanding its capabilities

Source trace:

SageMaker Data Wrangler documentation; focused artifact

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order001-data-quality-validation-monitoring.md

### P1-AIP-D2-003

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-003 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.3: Implement data validation and processing pipelines for FM consumption. |
| `exam_skill` | Skill 1.3.1: Create comprehensive data validation workflows to ensure data meets quality standards for FM consumption (for example, by using AWS Glue Data Quality, SageMaker Data Wrangler, custom Lambda functions, Amazon CloudWatch metrics). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day02-order001 |
| `accelerated_day` | Day 2 |
| `topic` | Data-quality validation and monitoring |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Causal; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | explain |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T051527Z-openai-gpt-4.1-day-02-order001.md item 4 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T051527Z |
| `raw_run_id` | order001 |

Stem:

A team is evaluating candidate foundation model input data in an Amazon S3 bucket. They want to automate regular checks for new data files containing unexpected null values and take corrective action. Which solution MOST directly enables automated detection and remediation?

Options:

1. Build a Glue Data Quality rule set and trigger a Lambda function when a rule fails.
2. Manually inspect S3 files each day for null values before running the pipeline.
3. Set up Amazon CloudWatch Events on S3 file creation to trigger data processing jobs.
4. Configure S3 object lock to prevent ingestion of files with null values.

Correct answer: Build a Glue Data Quality rule set and trigger a Lambda function when a rule fails.

Rationale: Combining Glue Data Quality for detection and Lambda for automated remediation provides a scalable, automated approach.

Distractors: Manually inspect S3 files each day for null values before running the pipeline.: Manual inspection is error-prone and doesn’t scale.; Set up Amazon CloudWatch Events on S3 file creation to trigger data processing jobs.: Events on file creation trigger jobs but don’t check content for nulls unless integrated with data quality validation.; Configure S3 object lock to prevent ingestion of files with null values.: S3 object lock can prevent deletion or overwrites, not content validation.

Misconception tags: Relying on manual inspection; Overestimating S3 content validation capabilities

Source trace:

Glue Data Quality documentation; study guide

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order001-data-quality-validation-monitoring.md

### P1-AIP-D2-004

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-004 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.3: Implement data validation and processing pipelines for FM consumption. |
| `exam_skill` | Skill 1.3.1: Create comprehensive data validation workflows to ensure data meets quality standards for FM consumption (for example, by using AWS Glue Data Quality, SageMaker Data Wrangler, custom Lambda functions, Amazon CloudWatch metrics). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day02-order001 |
| `accelerated_day` | Day 2 |
| `topic` | Data-quality validation and monitoring |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Causal; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T051527Z-openai-gpt-4.1-day-02-order001.md item 5 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T051527Z |
| `raw_run_id` | order001 |

Stem:

A generative AI application periodically pulls data from a relational database into Amazon S3. Foundation model accuracy recently declined. On review, you find a spike in referential integrity issues and duplicate records. Which approach should you implement FIRST to ensure only high-quality data is sent to the model?

Options:

1. Add data quality rules in AWS Glue to detect and block records with integrity violations before exporting.
2. Add an S3 lifecycle policy to automatically expire old data.
3. Increase batch job frequency to send fresher data.
4. Manually review all exported records each cycle before S3 ingestion.

Correct answer: Add data quality rules in AWS Glue to detect and block records with integrity violations before exporting.

Rationale: Data quality rules can automatically prevent corrupt or duplicate data from entering downstream processing.

Distractors: Add an S3 lifecycle policy to automatically expire old data.: Expiration only manages data at rest; it doesn’t prevent bad data ingestion.; Increase batch job frequency to send fresher data.: Fresher data is not helpful if referential integrity and duplication errors persist.; Manually review all exported records each cycle before S3 ingestion.: Manual review is slow and unscalable.

Misconception tags: Prioritizing freshness over integrity; Relying on manual review in scalable pipelines

Source trace:

AWS Glue Data Quality referential integrity rule docs; focused artifact

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order001-data-quality-validation-monitoring.md

### P1-AIP-D2-005

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-005 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.3: Implement data validation and processing pipelines for FM consumption. |
| `exam_skill` | Skill 1.3.1: Create comprehensive data validation workflows to ensure data meets quality standards for FM consumption (for example, by using AWS Glue Data Quality, SageMaker Data Wrangler, custom Lambda functions, Amazon CloudWatch metrics). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day02-order001 |
| `accelerated_day` | Day 2 |
| `topic` | Data-quality validation and monitoring |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Causal; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T051527Z-openai-gpt-4.1-day-02-order001.md item 6 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T051527Z |
| `raw_run_id` | order001 |

Stem:

You are tasked with providing real-time alerting for data quality issues detected during ingestion of social media posts into S3, which are processed by a foundation model for content moderation. Which AWS-native solution enables near real-time alerting based on data quality rules?

Options:

1. Configure AWS Glue Data Quality to publish rule evaluation metrics to Amazon CloudWatch and set up CloudWatch alarms.
2. Schedule a daily SageMaker Data Wrangler flow to check for data quality issues and email the team.
3. Set up Athena queries to run weekly and detect bad records, then send SNS notifications.
4. Deploy a custom Lambda that runs once per day to scan S3 content for anomalies.

Correct answer: Configure AWS Glue Data Quality to publish rule evaluation metrics to Amazon CloudWatch and set up CloudWatch alarms.

Rationale: Glue Data Quality provides native integration with CloudWatch for fast alerting, suitable for operational triggers.

Distractors: Schedule a daily SageMaker Data Wrangler flow to check for data quality issues and email the team.: Daily batch detection is not near real-time and introduces alerting delays.; Set up Athena queries to run weekly and detect bad records, then send SNS notifications.: Weekly detection is too infrequent for real-time operations.; Deploy a custom Lambda that runs once per day to scan S3 content for anomalies.: Once per day is not real-time and custom code may re-implement what Glue offers natively.

Misconception tags: Confusing periodic batch jobs with real-time alerting; Choosing manual over built-in metrics integration

Source trace:

Glue Data Quality + CloudWatch metrics documentation; study guide

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order001-data-quality-validation-monitoring.md

### P1-AIP-D2-006

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-006 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.3: Implement data validation and processing pipelines for FM consumption. |
| `exam_skill` | Skill 1.3.1: Create comprehensive data validation workflows to ensure data meets quality standards for FM consumption (for example, by using AWS Glue Data Quality, SageMaker Data Wrangler, custom Lambda functions, Amazon CloudWatch metrics). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day02-order001 |
| `accelerated_day` | Day 2 |
| `topic` | Data-quality validation and monitoring |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Causal; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | implement |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T051527Z-openai-gpt-4.1-day-02-order001.md item 7 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T051527Z |
| `raw_run_id` | order001 |

Stem:

You are implementing a data validation pipeline for tabular user activity logs. The logs must be checked for column-level nulls, data type mismatches, and sudden distribution changes. Which configuration provides the most scalable and maintainable validation workflow?

Options:

1. Develop Glue Data Quality rule sets and orchestrate checks as part of your ETL job.
2. Write custom Python scripts in Lambda to scan each file for the required issues.
3. Use SageMaker Studio to interactively review sample logs each week.
4. Manually export query results from Athena and inspect them in spreadsheets.

Correct answer: Develop Glue Data Quality rule sets and orchestrate checks as part of your ETL job.

Rationale: Glue Data Quality allows rule-based, repeatable, and scalable validation directly integrated into ETL processes.

Distractors: Write custom Python scripts in Lambda to scan each file for the required issues.: Custom scripts are labor-intensive, error-prone, and less maintainable than a managed solution.; Use SageMaker Studio to interactively review sample logs each week.: Interactive review is insufficient for production-scale, continuous ingestion.; Manually export query results from Athena and inspect them in spreadsheets.: Manual inspection is not scalable or automated.

Misconception tags: Preferring custom code over managed pipeline; Relying on manual or interactive steps

Source trace:

Glue Data Quality, ETL rule orchestration docs; answer guidance

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order001-data-quality-validation-monitoring.md

### P1-AIP-D2-007

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-007 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.3: Implement data validation and processing pipelines for FM consumption. |
| `exam_skill` | Skill 1.3.1: Create comprehensive data validation workflows to ensure data meets quality standards for FM consumption (for example, by using AWS Glue Data Quality, SageMaker Data Wrangler, custom Lambda functions, Amazon CloudWatch metrics). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day02-order001 |
| `accelerated_day` | Day 2 |
| `topic` | Data-quality validation and monitoring |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Causal; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | judge |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T051527Z-openai-gpt-4.1-day-02-order001.md item 8 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T051527Z |
| `raw_run_id` | order001 |

Stem:

A team ingests customer support chat data from multiple regions into a data lake backed by Amazon S3. After deploying a new data generator, they see sudden inconsistencies in language codes and missing conversation IDs. Which validation step is MOST likely to help prevent poor model performance in downstream FM-based summarization?

Options:

1. Add Glue Data Quality rule sets for allowed language codes and presence of conversation IDs.
2. Increase the foundation model’s context window to absorb more chat history.
3. Configure S3 event notifications to trigger retraining on every new file.
4. Enable CloudTrail logging on data generator API calls.

Correct answer: Add Glue Data Quality rule sets for allowed language codes and presence of conversation IDs.

Rationale: Validating input constraints at the ingestion step helps catch non-conforming records before they degrade downstream FM inference.

Distractors: Increase the foundation model’s context window to absorb more chat history.: Expanding context does not clean up errors in structure or key fields.; Configure S3 event notifications to trigger retraining on every new file.: Automated retraining on bad data compounds errors, rather than fixing them.; Enable CloudTrail logging on data generator API calls.: CloudTrail logs help trace changes, but do not validate or fix data content.

Misconception tags: Assuming downstream tuning can fix upstream quality issues; Over-automating retraining

Source trace:

Glue Data Quality conditional checks docs; focused artifact

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order001-data-quality-validation-monitoring.md

### P1-AIP-D2-008

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-008 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.3: Implement data validation and processing pipelines for FM consumption. |
| `exam_skill` | Skill 1.3.1: Create comprehensive data validation workflows to ensure data meets quality standards for FM consumption (for example, by using AWS Glue Data Quality, SageMaker Data Wrangler, custom Lambda functions, Amazon CloudWatch metrics). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day02-order001 |
| `accelerated_day` | Day 2 |
| `topic` | Data-quality validation and monitoring |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Causal; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | exam-plus |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 180 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T051527Z-openai-gpt-4.1-day-02-order001.md item 9 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T051527Z |
| `raw_run_id` | order001 |

Stem:

While onboarding a new supplier's product catalog, extensive manual corrections are required after ingestion due to data type mismatches and inconsistent field delimiters. Existing automated checks use Lambda functions integrated with CloudWatch. What is the MOST effective technical step to reduce ongoing manual corrections?

Options:

1. Implement AWS Glue Data Quality rule sets for all schema and content checks, replacing custom Lambda code.
2. Increase CloudWatch alarm sensitivity to notify earlier on all Lambda failures.
3. Add a SageMaker Data Wrangler job to reformat ingested data after detection.
4. Schedule manual data audits before every model inference step.

Correct answer: Implement AWS Glue Data Quality rule sets for all schema and content checks, replacing custom Lambda code.

Rationale: Glue Data Quality provides out-of-the-box rules for schema and content validation, reducing custom code maintenance and improving coverage.

Distractors: Increase CloudWatch alarm sensitivity to notify earlier on all Lambda failures.: Alarming sooner doesn’t prevent errors; it just signals them.; Add a SageMaker Data Wrangler job to reformat ingested data after detection.: Reformatting after detection still leaves messy data to correct; validation up front is better.; Schedule manual data audits before every model inference step.: Manual audits are not scalable and defeat pipeline automation.

Misconception tags: Over-reliance on alarms/manual review; Not replacing brittle custom code with managed validation

Source trace:

Glue Data Quality rules vs. Lambda documentation; focused artifact

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order001-data-quality-validation-monitoring.md

### P1-AIP-D2-009

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-009 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.3: Implement data validation and processing pipelines for FM consumption. |
| `exam_skill` | Skill 1.3.1: Create comprehensive data validation workflows to ensure data meets quality standards for FM consumption (for example, by using AWS Glue Data Quality, SageMaker Data Wrangler, custom Lambda functions, Amazon CloudWatch metrics). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day02-order001 |
| `accelerated_day` | Day 2 |
| `topic` | Data-quality validation and monitoring |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Causal; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T051527Z-openai-gpt-4.1-day-02-order001.md item 10 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T051527Z |
| `raw_run_id` | order001 |

Stem:

You discover that a downstream LLM inference pipeline is returning inconsistent summaries for similar customer reviews. After checking the code base, you suspect data quality issues. What is the MOST effective first step to identify root causes?

Options:

1. Run data quality profiling using AWS Glue Data Quality on recent customer reviews.
2. Tune the LLM to better handle noisy input.
3. Increase the sample size in the test dataset.
4. Add more layers to the LLM architecture.

Correct answer: Run data quality profiling using AWS Glue Data Quality on recent customer reviews.

Rationale: Profiling helps to diagnose potential schema, content, or distribution issues affecting consistency.

Distractors: Tune the LLM to better handle noisy input.: Improving the model without addressing upstream data issues is unlikely to fix the problem.; Increase the sample size in the test dataset.: Sample size does not fix underlying data quality issues.; Add more layers to the LLM architecture.: Increasing model size is of little use if input data is faulty.

Misconception tags: Blaming the model before inspecting the data; Confusing model capacity with input data quality

Source trace:

Glue Data Quality profiling docs; study guide

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order001-data-quality-validation-monitoring.md

### P1-AIP-D2-010

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-010 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.3: Implement data validation and processing pipelines for FM consumption. |
| `exam_skill` | Skill 1.3.1: Create comprehensive data validation workflows to ensure data meets quality standards for FM consumption (for example, by using AWS Glue Data Quality, SageMaker Data Wrangler, custom Lambda functions, Amazon CloudWatch metrics). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day02-order001 |
| `accelerated_day` | Day 2 |
| `topic` | Data-quality validation and monitoring |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Causal; Embedded |
| `question_format` | multiple-response |
| `difficulty` | hard |
| `cognitive_demand` | integrate |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T051527Z-openai-gpt-4.1-day-02-order001.md item 11 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T051527Z |
| `raw_run_id` | order001 |

Stem:

A team is designing an automated pipeline for text ingestion and validation prior to FM inference. Data comes from multiple formats and sources (CSV, JSON, API streams). Which of the following practices will BEST ensure high data quality with minimal manual intervention? (Select TWO.)

Options:

1. Implement schema validation and null-checks in Glue Data Quality rule sets for each data source.
2. Configure CloudWatch metrics to monitor failed validation rules and trigger remediation.
3. Rely solely on API contract guarantees from upstream systems.
4. Perform one-time manual data inspection after pipeline launch.
5. Add duplicate record detection to the validation workflow.

Correct answer: Implement schema validation and null-checks in Glue Data Quality rule sets for each data source.; Add duplicate record detection to the validation workflow.

Rationale: Schema, null, and duplicate checks are crucial for preventing downstream errors and ensuring consistent input for FMs.

Distractors: Configure CloudWatch metrics to monitor failed validation rules and trigger remediation.: Metrics and alarms provide monitoring, but without strong data quality rules, issues may remain undetected.; Rely solely on API contract guarantees from upstream systems.: Upstream API guarantees are helpful, but direct validation is necessary to catch unanticipated errors.; Perform one-time manual data inspection after pipeline launch.: Manual and one-time checks are insufficient for ongoing assurance.

Misconception tags: Over-reliance on contractual guarantees; Confusing monitoring with validation

Source trace:

Glue Data Quality rules, deduplication docs; answer guidance

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order001-data-quality-validation-monitoring.md

### P1-AIP-D2-011

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-011 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.3: Implement data validation and processing pipelines for FM consumption. |
| `exam_skill` | Skill 1.3.1: Create comprehensive data validation workflows to ensure data meets quality standards for FM consumption (for example, by using AWS Glue Data Quality, SageMaker Data Wrangler, custom Lambda functions, Amazon CloudWatch metrics). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day02-order001 |
| `accelerated_day` | Day 2 |
| `topic` | Data-quality validation and monitoring |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Causal; Embedded |
| `question_format` | multiple-response |
| `difficulty` | hard |
| `cognitive_demand` | optimize |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T051527Z-openai-gpt-4.1-day-02-order001.md item 12 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T051527Z |
| `raw_run_id` | order001 |

Stem:

A genomics project processes petabyte-scale sample data for input to a foundation model. Data arrives as CSVs with variable schema and inconsistent delimiters. Which TWO technical controls, if added to the pipeline, would MOST improve automated data validation accuracy before FM ingestion?

Options:

1. Use Glue Data Quality rule sets to enforce schema and delimiter consistency before ingestion.
2. Integrate automatic schema inference and mismatch reporting into ETL jobs.
3. Rely on API-level logging to track incoming files.
4. Perform daily manual audits using Athena queries.
5. Pause ingestion jobs whenever a file size anomaly is detected.

Correct answer: Use Glue Data Quality rule sets to enforce schema and delimiter consistency before ingestion.; Integrate automatic schema inference and mismatch reporting into ETL jobs.

Rationale: Automated rules and schema inference help identify mismatches and inconsistencies prior to model input, vital for scalable genomics use cases.

Distractors: Rely on API-level logging to track incoming files.: Logging is valuable for tracking, but not for content quality assurance.; Perform daily manual audits using Athena queries.: Manual approaches are not feasible at petabyte scale.; Pause ingestion jobs whenever a file size anomaly is detected.: Size checks don't ensure schema or delimiter validity.

Misconception tags: Relying on logs or file size heuristics; Manual approaches for big data pipelines

Source trace:

Glue Data Quality delimiter checking docs; focused artifact

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order001-data-quality-validation-monitoring.md

### P1-AIP-D2-012

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-012 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.3: Implement data validation and processing pipelines for FM consumption. |
| `exam_skill` | Skill 1.3.1: Create comprehensive data validation workflows to ensure data meets quality standards for FM consumption (for example, by using AWS Glue Data Quality, SageMaker Data Wrangler, custom Lambda functions, Amazon CloudWatch metrics). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day02-order001 |
| `accelerated_day` | Day 2 |
| `topic` | Data-quality validation and monitoring |
| `knowledge_category` | Skill; Knowledge; Representation / Location |
| `knowledge_type` | Procedural; Causal; Embedded |
| `question_format` | multiple-response |
| `difficulty` | exam-plus |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 180 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T051527Z-openai-gpt-4.1-day-02-order001.md item 13 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T051527Z |
| `raw_run_id` | order001 |

Stem:

You are investigating inconsistent document summaries generated by a Bedrock-hosted FM. Analysis reveals a correlation with spikes in S3 ingestion activity. Which TWO actions would MOST likely help uncover the true cause? (Select TWO.)

Options:

1. Review recent Glue Data Quality rule evaluation reports for ingestion windows with elevated activity.
2. Check for S3 object versioning or overwrite anomalies during spike periods.
3. Retrain the model using only data from non-spike periods.
4. Increase the number of parallel S3 ingestion jobs.
5. Disable all data validation steps temporarily to isolate FM output.

Correct answer: Review recent Glue Data Quality rule evaluation reports for ingestion windows with elevated activity.; Check for S3 object versioning or overwrite anomalies during spike periods.

Rationale: Rule evaluation results and storage anomalies may expose ingestion or data integrity issues driving output inconsistency.

Distractors: Retrain the model using only data from non-spike periods.: Model retraining before understanding the data issues is premature.; Increase the number of parallel S3 ingestion jobs.: Higher parallelism may worsen consistency issues if the cause is data or ordering related.; Disable all data validation steps temporarily to isolate FM output.: Disabling validation may mask root causes and further degrade quality.

Misconception tags: Disabling validation to debug model; Blaming models before reviewing data

Source trace:

Glue Data Quality spike event documentation; answer guidance

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order001-data-quality-validation-monitoring.md

### P1-AIP-D2-013

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-013 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.3: Implement data validation and processing pipelines for FM consumption. |
| `exam_skill` | Skill 1.3.2: Create data processing workflows to handle complex data types including text, image, audio, and tabular data with specialized processing requirements for FM consumption (for example, by using Amazon Bedrock multimodal models, SageMaker Processing, AWS Transcribe, advanced multimodal pipeline architectures). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day02-order002 |
| `accelerated_day` | Day 2 |
| `topic` | Text, image, audio, and tabular-data preprocessing |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T051621Z-openai-gpt-4.1-day-02-order002.md item 1 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T051621Z |
| `raw_run_id` | order002 |

Stem:

An ML engineer is building a pipeline to process scanned PDF invoices for a procurement FM solution. After integrating the latest model, they notice high rates of misclassification in fields extracted from the images. Which preprocessing step should the engineer prioritize to improve extraction accuracy before FM inference?

Options:

1. Apply image binarization and orientation correction to the scanned PDFs before text extraction.
2. Increase FM context window size during inference.
3. Add entity recognition post-processing after FM inference.
4. Directly pass raw images without preprocessing to the FM endpoint.

Correct answer: Apply image binarization and orientation correction to the scanned PDFs before text extraction.

Rationale: Image binarization and orientation correction enhances the quality and alignment of text in scanned PDFs, which significantly improves text extraction (e.g., via OCR) and downstream FM processing.

Distractors: Increase FM context window size during inference.: This does not address extraction errors caused by raw image quality or improper orientation; it only influences how much context the model can process.; Add entity recognition post-processing after FM inference.: Post-processing can't correct errors that originate from poor text extraction; the underlying text must be clean before entity recognition is effective.; Directly pass raw images without preprocessing to the FM endpoint.: Skipping preprocessing leads to higher extraction errors since FMs may not inherently handle raw or misaligned images as effectively as specialized preprocessing workflows.

Misconception tags: Skipping data cleaning; Blaming the model for input-preprocessing failures

Source trace:

source: study guide, AWS Textract docs for preprocessing recommendations

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order002-multimodal-data-preprocessing.md

### P1-AIP-D2-014

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-014 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.3: Implement data validation and processing pipelines for FM consumption. |
| `exam_skill` | Skill 1.3.2: Create data processing workflows to handle complex data types including text, image, audio, and tabular data with specialized processing requirements for FM consumption (for example, by using Amazon Bedrock multimodal models, SageMaker Processing, AWS Transcribe, advanced multimodal pipeline architectures). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day02-order002 |
| `accelerated_day` | Day 2 |
| `topic` | Text, image, audio, and tabular-data preprocessing |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T051621Z-openai-gpt-4.1-day-02-order002.md item 4 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T051621Z |
| `raw_run_id` | order002 |

Stem:

A team needs to preprocess tabular purchase records from CSV files for ingestion into a Bedrock FM that expects structured JSON input. Which approach best addresses data normalization and format conversion?

Options:

1. Build a SageMaker Processing pipeline to transform the CSV files into normalized JSON objects.
2. Directly upload the raw CSV files to the Bedrock endpoint.
3. Use AWS Transcribe to convert the CSV data into text.
4. Ingest the CSV into Redshift and issue SQL queries without further conversion.

Correct answer: Build a SageMaker Processing pipeline to transform the CSV files into normalized JSON objects.

Rationale: SageMaker Processing is suited for custom data transformation workflows such as normalizing tabular CSV data and converting it to the expected JSON format.

Distractors: Directly upload the raw CSV files to the Bedrock endpoint.: FM endpoints expecting structured JSON will fail or produce errors if fed raw CSV instead.; Use AWS Transcribe to convert the CSV data into text.: Transcribe is designed to process audio files into text and is not applicable for tabular or structured data transformations.; Ingest the CSV into Redshift and issue SQL queries without further conversion.: Redshift is a data warehouse, but FMs require data in the specific API format, not queried records.

Misconception tags: Service/format mismatch; Skipping data normalization

Source trace:

source: Bedrock API input requirements for tabular data

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order002-multimodal-data-preprocessing.md

### P1-AIP-D2-015

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-015 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.3: Implement data validation and processing pipelines for FM consumption. |
| `exam_skill` | Skill 1.3.2: Create data processing workflows to handle complex data types including text, image, audio, and tabular data with specialized processing requirements for FM consumption (for example, by using Amazon Bedrock multimodal models, SageMaker Processing, AWS Transcribe, advanced multimodal pipeline architectures). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day02-order002 |
| `accelerated_day` | Day 2 |
| `topic` | Text, image, audio, and tabular-data preprocessing |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T051621Z-openai-gpt-4.1-day-02-order002.md item 5 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T051621Z |
| `raw_run_id` | order002 |

Stem:

A company implements a multimodal RAG pipeline to summarize research articles containing both text and annotated diagrams. The FM output consistently omits key information from diagrams. What preprocessing enhancement will most likely improve summary completeness?

Options:

1. Integrate an image-to-text extraction step that converts annotated diagrams to text before FM ingestion.
2. Fine-tune the FM exclusively on text paragraphs.
3. Reduce the chunk size for text segments prior to FM inference.
4. Increase the model's temperature parameter during generation.

Correct answer: Integrate an image-to-text extraction step that converts annotated diagrams to text before FM ingestion.

Rationale: Extracting information from diagrams to text allows the FM to access diagram content, facilitating more complete and accurate summaries.

Distractors: Fine-tune the FM exclusively on text paragraphs.: This ignores content in diagrams and further skews results toward textual content.; Reduce the chunk size for text segments prior to FM inference.: Chunk size impacts tokenization but doesn't address missing diagram content.; Increase the model's temperature parameter during generation.: Temperature controls output diversity, not the completeness of input coverage.

Misconception tags: Forgetting cross-modal extraction; Thinking text-only fixes multimodal issues

Source trace:

source: study guide, Bedrock multimodal documentation

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-02-data-embeddings-vector-stores-rag.md

### P1-AIP-D2-016

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-016 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.3: Implement data validation and processing pipelines for FM consumption. |
| `exam_skill` | Skill 1.3.2: Create data processing workflows to handle complex data types including text, image, audio, and tabular data with specialized processing requirements for FM consumption (for example, by using Amazon Bedrock multimodal models, SageMaker Processing, AWS Transcribe, advanced multimodal pipeline architectures). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day02-order002 |
| `accelerated_day` | Day 2 |
| `topic` | Text, image, audio, and tabular-data preprocessing |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Conditional |
| `question_format` | multiple-response |
| `difficulty` | hard |
| `cognitive_demand` | implement |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T051621Z-openai-gpt-4.1-day-02-order002.md item 6 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T051621Z |
| `raw_run_id` | order002 |

Stem:

You are preparing a pipeline for ingesting customer feedback, including voice messages, attached images, and tabular survey results, into a Bedrock FM. Which TWO preprocessing steps are required to enable consistent semantic search across all data types? (Select TWO.)

Options:

1. Transcribe voice messages to text using AWS Transcribe.
2. Convert tabular survey results into structured JSON records.
3. Convert images to base64 and pass them directly to the Bedrock FM without further processing.
4. Aggregate all raw input types into a single PDF before submitting to the FM.
5. Skip normalization of tabular data as FMs handle raw CSV natively.

Correct answer: Transcribe voice messages to text using AWS Transcribe.; Convert tabular survey results into structured JSON records.

Rationale: Transcribing voice to text enables text-based semantic search, and structuring tabular data in JSON ensures FM can process and index responses uniformly.

Distractors: Convert images to base64 and pass them directly to the Bedrock FM without further processing.: Base64 conversion does not prepare the content for semantic search; semantic info must be extracted (e.g., OCR, captioning).; Aggregate all raw input types into a single PDF before submitting to the FM.: PDF aggregation conflates modalities and may hinder downstream processing or semantic indexing.; Skip normalization of tabular data as FMs handle raw CSV natively.: FMs typically require well-structured and normalized data; skipping this reduces search effectiveness.

Misconception tags: Misunderstanding input prep for semantic retrieval; Assuming FMs handle all raw data natively

Source trace:

source: Bedrock input data requirements and study guide for semantic search

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order002-multimodal-data-preprocessing.md

### P1-AIP-D2-017

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-017 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.3: Implement data validation and processing pipelines for FM consumption. |
| `exam_skill` | Skill 1.3.2: Create data processing workflows to handle complex data types including text, image, audio, and tabular data with specialized processing requirements for FM consumption (for example, by using Amazon Bedrock multimodal models, SageMaker Processing, AWS Transcribe, advanced multimodal pipeline architectures). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day02-order002 |
| `accelerated_day` | Day 2 |
| `topic` | Text, image, audio, and tabular-data preprocessing |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T051621Z-openai-gpt-4.1-day-02-order002.md item 7 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T051621Z |
| `raw_run_id` | order002 |

Stem:

A data pipeline for journal articles uses SageMaker Processing to clean up OCR-extracted text data before further FM ingestion. Recently, output quality dropped, with incoherent text and frequent tokens like "fi" and "fl" appearing mid-word (e.g., "effi cient"). What root cause should the team address?

Options:

1. OCR software failed to merge or normalize frequently ligatured character sequences.
2. FM prompt length exceeds the context window.
3. FM model was updated without retraining.
4. Tabular data was concatenated incorrectly.

Correct answer: OCR software failed to merge or normalize frequently ligatured character sequences.

Rationale: Post-OCR text often contains fragmented ligatures like "fi" and "fl," which must be normalized to ensure data quality before FM processing.

Distractors: FM prompt length exceeds the context window.: This would cause truncation, not mid-word ligature errors.; FM model was updated without retraining.: Model updates do not introduce character ligature artifacts; this is a preprocessing defect.; Tabular data was concatenated incorrectly.: Concatenation errors would show up as layout or delimiter problems, not mid-word letter splits.

Misconception tags: Misattribution of FM errors to model or data ingestion; Ignoring OCR edge cases

Source trace:

source: OCR postprocessing challenges in preprocessing pipelines

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day-02-answer-guidance.md

### P1-AIP-D2-018

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-018 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.3: Implement data validation and processing pipelines for FM consumption. |
| `exam_skill` | Skill 1.3.2: Create data processing workflows to handle complex data types including text, image, audio, and tabular data with specialized processing requirements for FM consumption (for example, by using Amazon Bedrock multimodal models, SageMaker Processing, AWS Transcribe, advanced multimodal pipeline architectures). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day02-order002 |
| `accelerated_day` | Day 2 |
| `topic` | Text, image, audio, and tabular-data preprocessing |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | judge |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T051621Z-openai-gpt-4.1-day-02-order002.md item 9 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T051621Z |
| `raw_run_id` | order002 |

Stem:

A customer wants to run a multimodal sentiment analysis model using Amazon Bedrock. Their dataset consists of user reviews (text), uploaded screenshots (images), and survey responses in Excel spreadsheets. Which preprocessing action could cause downstream errors if overlooked?

Options:

1. Failing to convert Excel survey responses to structured JSON before FM ingestion.
2. Applying NLP preprocessing steps to screenshot image data.
3. Normalizing text to lowercase before providing data to the FM.
4. Creating embeddings for each record prior to Bedrock API requests.

Correct answer: Failing to convert Excel survey responses to structured JSON before FM ingestion.

Rationale: Structured survey data (from Excel) must be converted to the expected structured input format (e.g., JSON) for the model to parse input meaningfully.

Distractors: Applying NLP preprocessing steps to screenshot image data.: Although unnecessary, applying NLP preprocessing to images doesn't cause an error—images are simply ignored by NLP steps.; Normalizing text to lowercase before providing data to the FM.: Lowercasing is standard and seldom causes FM errors.; Creating embeddings for each record prior to Bedrock API requests.: Embeddings are typically generated after ingestion or within the workflow, not a strict preprocessing requirement.

Misconception tags: Ignoring data type boundaries; Forgetting format conversion

Source trace:

source: Bedrock input requirements for structured/tabular data

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order002-multimodal-data-preprocessing.md

### P1-AIP-D2-019

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-019 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.3: Implement data validation and processing pipelines for FM consumption. |
| `exam_skill` | Skill 1.3.2: Create data processing workflows to handle complex data types including text, image, audio, and tabular data with specialized processing requirements for FM consumption (for example, by using Amazon Bedrock multimodal models, SageMaker Processing, AWS Transcribe, advanced multimodal pipeline architectures). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day02-order002 |
| `accelerated_day` | Day 2 |
| `topic` | Text, image, audio, and tabular-data preprocessing |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T051621Z-openai-gpt-4.1-day-02-order002.md item 10 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T051621Z |
| `raw_run_id` | order002 |

Stem:

A solutions architect is designing a scalable preprocessing workflow for user-uploaded resumes received as PDF files containing both text and images. The downstream FM application requires both structured text and image features. Which workflow is most appropriate?

Options:

1. Use Textract to extract structured text and Rekognition to process embedded images from the PDFs.
2. Use AWS Transcribe to process the PDF files directly.
3. Send the PDFs as-is to the FM, relying on its built-in preprocessing.
4. Convert PDFs to CSV and import into SageMaker Studio.

Correct answer: Use Textract to extract structured text and Rekognition to process embedded images from the PDFs.

Rationale: Textract specializes in extracting structured text from PDFs, and Rekognition can process and extract features from images embedded in the documents, providing data in the formats required.

Distractors: Use AWS Transcribe to process the PDF files directly.: Transcribe is for audio data, not PDFs.; Send the PDFs as-is to the FM, relying on its built-in preprocessing.: Relying on an FM's internal preprocessing for multi-format PDF extraction is unreliable and likely insufficient.; Convert PDFs to CSV and import into SageMaker Studio.: Conversion to CSV may lose structural and image information; this is not standard practice for resume parsing.

Misconception tags: Confusing service function; Mistaking FM for a multipurpose extractor

Source trace:

source: AWS Textract and Rekognition limitations and workflow examples

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day-02-answer-guidance.md

### P1-AIP-D2-020

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-020 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.3: Implement data validation and processing pipelines for FM consumption. |
| `exam_skill` | Skill 1.3.2: Create data processing workflows to handle complex data types including text, image, audio, and tabular data with specialized processing requirements for FM consumption (for example, by using Amazon Bedrock multimodal models, SageMaker Processing, AWS Transcribe, advanced multimodal pipeline architectures). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day02-order002 |
| `accelerated_day` | Day 2 |
| `topic` | Text, image, audio, and tabular-data preprocessing |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Conditional |
| `question_format` | multiple-response |
| `difficulty` | exam-plus |
| `cognitive_demand` | integrate |
| `estimated_time_seconds` | 180 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T051621Z-openai-gpt-4.1-day-02-order002.md item 11 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T051621Z |
| `raw_run_id` | order002 |

Stem:

An enterprise is designing an end-to-end pipeline to process customer support tickets containing free-form text, screenshots, and tabular error logs for subsequent FM-driven troubleshooting. Which THREE preprocessing actions should be implemented to support optimal FM inference? (Select THREE.)

Options:

1. Extract and normalize text from free-form ticket fields using a SageMaker Processing job.
2. Apply OCR to screenshots to extract textual context for the FM.
3. Ingest error log spreadsheets as-is since FMs can directly process them without transformation.
4. Transform error logs from spreadsheet format to structured JSON.
5. Aggregate text, OCR output, and structured logs into a unified input for FM inference.

Correct answer: Extract and normalize text from free-form ticket fields using a SageMaker Processing job.; Apply OCR to screenshots to extract textual context for the FM.; Transform error logs from spreadsheet format to structured JSON.

Rationale: Text normalization ensures input consistency; OCR enables the FM to access information in screenshots; converting logs to JSON provides structure, all supporting robust FM operations.

Distractors: Ingest error log spreadsheets as-is since FMs can directly process them without transformation.: Raw spreadsheets often require formatting and may not be correctly interpreted by the FM pipeline.; Aggregate text, OCR output, and structured logs into a unified input for FM inference.: While aggregation is important, it's not a preprocessing step but a final input packaging step after extraction and transformation.

Misconception tags: Assuming FMs natively handle raw spreadsheets; Equating final packaging with preprocessing

Source trace:

source: Bedrock and SageMaker recommendations for tabular, image, and text input handling

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order002-multimodal-data-preprocessing.md

### P1-AIP-D2-021

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-021 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.3: Implement data validation and processing pipelines for FM consumption. |
| `exam_skill` | Skill 1.3.2: Create data processing workflows to handle complex data types including text, image, audio, and tabular data with specialized processing requirements for FM consumption (for example, by using Amazon Bedrock multimodal models, SageMaker Processing, AWS Transcribe, advanced multimodal pipeline architectures). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day02-order002 |
| `accelerated_day` | Day 2 |
| `topic` | Text, image, audio, and tabular-data preprocessing |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T051621Z-openai-gpt-4.1-day-02-order002.md item 12 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T051621Z |
| `raw_run_id` | order002 |

Stem:

A data engineer must design a preprocessing workflow to accommodate real-time social media text, user-uploaded images, and voice comments for a Bedrock FM marketing analytics solution. What is the most appropriate AWS tool combination for this requirement?

Options:

1. SageMaker Processing, Amazon Rekognition, and AWS Transcribe
2. Amazon Comprehend, AWS Glue, and AWS Lambda
3. Amazon Textract, Aurora, and Amazon Polly
4. AWS DataSync, S3 Select, and AWS CloudTrail

Correct answer: SageMaker Processing, Amazon Rekognition, and AWS Transcribe

Rationale: SageMaker Processing is flexible for text, Rekognition handles image analysis, and Transcribe processes audio—all aligned to their respective modality requirements.

Distractors: Amazon Comprehend, AWS Glue, and AWS Lambda: Comprehend is not for images or audio; Glue/Lambda lack built-in multimodal support.; Amazon Textract, Aurora, and Amazon Polly: Textract is for document OCR, Polly is text-to-speech, Aurora is a database—all mismatched for preprocessing real-time multimodal data.; AWS DataSync, S3 Select, and AWS CloudTrail: These services are for data movement, querying, and logging—not preprocessing or feature extraction.

Misconception tags: Service selection trap; Choosing general-purpose over specialized tools

Source trace:

source: AWS documentation (Rekognition, Transcribe, SageMaker Processing)

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-02-data-embeddings-vector-stores-rag.md

### P1-AIP-D2-022

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-022 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.3: Implement data validation and processing pipelines for FM consumption. |
| `exam_skill` | Skill 1.3.3: Format input data for FM inference according to model-specific requirements (for example, by using JSON formatting for Amazon Bedrock API requests, structured data preparation for SageMaker AI endpoints, conversation formatting for dialog-based applications). |
| `secondary_exam_skills` | Skill 1.3.4: Enhance input data quality to improve FM response quality and consistency (for example, by using Amazon Bedrock to reformat text, Amazon Comprehend to extract entities, Lambda functions to normalize data). |
| `learning_unit` | Day02-order003 |
| `accelerated_day` | Day 2 |
| `topic` | Model-specific input formatting and data normalization |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Declarative; Procedural; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T051717Z-openai-gpt-4.1-day-02-order003.md item 1 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T051717Z |
| `raw_run_id` | order003 |

Stem:

A team is preparing input data to send to an Amazon Bedrock FM endpoint using the InvokeModel API. Their raw dataset is a mix of plain strings and nested dictionaries. What is the most appropriate next step to ensure the model's input meets Bedrock's requirements?

Options:

1. Convert each data item to a JSON-encoded string respecting model's expected schema before sending
2. Send the plain strings and nested dictionaries directly; Bedrock will parse all native Python formats
3. Serialize the data as CSV and attach it to the request's body parameter
4. Base64 encode each dictionary and send as part of a binary input parameter

Correct answer: Convert each data item to a JSON-encoded string respecting model's expected schema before sending

Rationale: Bedrock APIs expect input in a model-specific JSON structure; ensuring all data is encoded in the correct JSON format is essential before submission.

Distractors: Send the plain strings and nested dictionaries directly; Bedrock will parse all native Python formats: Tempting, but Bedrock APIs require JSON—not Python-native formats—as input.; Serialize the data as CSV and attach it to the request's body parameter: CSV is not a supported input format for Bedrock model APIs and would result in a request error.; Base64 encode each dictionary and send as part of a binary input parameter: Base64 encoding does not fit Bedrock's input expectations. Input must be structured as a JSON object.

Misconception tags: Assuming service accepts raw Python/CSV; Skipping format validation

Source trace:

https://docs.aws.amazon.com/bedrock/latest/userguide/model-invoke.html, study_guide, focused_artifact

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order003-input-formatting-normalization.md

### P1-AIP-D2-023

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-023 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.3: Implement data validation and processing pipelines for FM consumption. |
| `exam_skill` | Skill 1.3.3: Format input data for FM inference according to model-specific requirements (for example, by using JSON formatting for Amazon Bedrock API requests, structured data preparation for SageMaker AI endpoints, conversation formatting for dialog-based applications). |
| `secondary_exam_skills` | Skill 1.3.4: Enhance input data quality to improve FM response quality and consistency (for example, by using Amazon Bedrock to reformat text, Amazon Comprehend to extract entities, Lambda functions to normalize data). |
| `learning_unit` | Day02-order003 |
| `accelerated_day` | Day 2 |
| `topic` | Model-specific input formatting and data normalization |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Declarative; Procedural; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T051717Z-openai-gpt-4.1-day-02-order003.md item 2 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T051717Z |
| `raw_run_id` | order003 |

Stem:

You are designing a Lambda function to normalize dates from various formats in a dataset before sending it to a dialog FM for intent detection. Which normalization strategy is most appropriate for maximizing model consistency?

Options:

1. Standardize all dates to ISO 8601 (YYYY-MM-DD) format regardless of input variant
2. Pass dates as-is for the FM to learn variants during training
3. Map all dates to localized long-form text (e.g., 'January 1st, 2023')
4. Remove all date fields to avoid input ambiguity

Correct answer: Standardize all dates to ISO 8601 (YYYY-MM-DD) format regardless of input variant

Rationale: Using a consistent, unambiguous date format reduces ambiguity, benefiting FM consistency and downstream processing.

Distractors: Pass dates as-is for the FM to learn variants during training: Tempting, but model-inference pipelines expect normalized inputs; not all inference endpoints are retrained on-the-fly.; Map all dates to localized long-form text (e.g., 'January 1st, 2023'): Localized formats introduce parsing complexity and ambiguity.; Remove all date fields to avoid input ambiguity: Removes potentially valuable information needed for downstream tasks.

Misconception tags: Assuming FMs handle all normalization; Dropping fields unnecessarily

Source trace:

study_guide, focused_artifact, answer_guidance

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order003-input-formatting-normalization.md

### P1-AIP-D2-024

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-024 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.3: Implement data validation and processing pipelines for FM consumption. |
| `exam_skill` | Skill 1.3.3: Format input data for FM inference according to model-specific requirements (for example, by using JSON formatting for Amazon Bedrock API requests, structured data preparation for SageMaker AI endpoints, conversation formatting for dialog-based applications). |
| `secondary_exam_skills` | Skill 1.3.4: Enhance input data quality to improve FM response quality and consistency (for example, by using Amazon Bedrock to reformat text, Amazon Comprehend to extract entities, Lambda functions to normalize data). |
| `learning_unit` | Day02-order003 |
| `accelerated_day` | Day 2 |
| `topic` | Model-specific input formatting and data normalization |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Declarative; Procedural; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | implement |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T051717Z-openai-gpt-4.1-day-02-order003.md item 3 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T051717Z |
| `raw_run_id` | order003 |

Stem:

A data scientist is using SageMaker Processing to prepare structured input for an AI endpoint that expects all missing numerical values as zeroes and all text fields trimmed of whitespace. Which step should be implemented in the processing script to ensure FM compatibility?

Options:

1. Impute missing numerical values with zero and strip whitespace from all string fields
2. Leave missing values as null and preserve all whitespace to avoid data loss
3. Convert missing fields into the string 'missing' for all columns
4. Encode all fields as base64 to ensure safe transport

Correct answer: Impute missing numerical values with zero and strip whitespace from all string fields

Rationale: The FM expects zero-imputation and trimmed strings. This ensures input matches expectations and prevents unpredictable inference behavior.

Distractors: Leave missing values as null and preserve all whitespace to avoid data loss: Nulls may not be supported by the endpoint, and extra whitespace can degrade text processing.; Convert missing fields into the string 'missing' for all columns: May cause confusion in downstream logic expecting numerical values.; Encode all fields as base64 to ensure safe transport: Base64 encoding is unnecessary unless sending binary data.

Misconception tags: Overtrusting endpoint defaults; Improper imputation

Source trace:

study_guide, focused_artifact

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order003-input-formatting-normalization.md

### P1-AIP-D2-025

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-025 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.3: Implement data validation and processing pipelines for FM consumption. |
| `exam_skill` | Skill 1.3.3: Format input data for FM inference according to model-specific requirements (for example, by using JSON formatting for Amazon Bedrock API requests, structured data preparation for SageMaker AI endpoints, conversation formatting for dialog-based applications). |
| `secondary_exam_skills` | Skill 1.3.4: Enhance input data quality to improve FM response quality and consistency (for example, by using Amazon Bedrock to reformat text, Amazon Comprehend to extract entities, Lambda functions to normalize data). |
| `learning_unit` | Day02-order003 |
| `accelerated_day` | Day 2 |
| `topic` | Model-specific input formatting and data normalization |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Declarative; Procedural; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T051717Z-openai-gpt-4.1-day-02-order003.md item 4 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T051717Z |
| `raw_run_id` | order003 |

Stem:

You are debugging a classification FM endpoint that returns inconsistent results on seemingly similar user utterances. After reviewing the invocation logs, you notice significant variance in input string capitalization and punctuation. What is the most likely root cause?

Options:

1. Input normalization steps are missing, leading to inconsistent representations before inference
2. The FM’s training data is corrupted, causing unpredictable answers
3. bedrock:InvokeModel is being rate-limited, truncating responses
4. The endpoint is using unsupported language codes in the input payload

Correct answer: Input normalization steps are missing, leading to inconsistent representations before inference

Rationale: Inconsistent input string capitalization and punctuation cause FMs to interpret otherwise similar utterances differently; normalization is critical.

Distractors: The FM’s training data is corrupted, causing unpredictable answers: Training data issues are less likely than inconsistent inference inputs given the logs.; bedrock:InvokeModel is being rate-limited, truncating responses: Rate-limiting would manifest as errors, not inconsistent logic.; The endpoint is using unsupported language codes in the input payload: Not relevant, as issue is with capitalization and punctuation, not language settings.

Misconception tags: Blaming the model before checking pre-processing; Ignoring input normalization

Source trace:

focused_artifact, answer_guidance

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day-02-answer-guidance.md

### P1-AIP-D2-026

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-026 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.3: Implement data validation and processing pipelines for FM consumption. |
| `exam_skill` | Skill 1.3.3: Format input data for FM inference according to model-specific requirements (for example, by using JSON formatting for Amazon Bedrock API requests, structured data preparation for SageMaker AI endpoints, conversation formatting for dialog-based applications). |
| `secondary_exam_skills` | Skill 1.3.4: Enhance input data quality to improve FM response quality and consistency (for example, by using Amazon Bedrock to reformat text, Amazon Comprehend to extract entities, Lambda functions to normalize data). |
| `learning_unit` | Day02-order003 |
| `accelerated_day` | Day 2 |
| `topic` | Model-specific input formatting and data normalization |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Declarative; Procedural; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | judge |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T051717Z-openai-gpt-4.1-day-02-order003.md item 5 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T051717Z |
| `raw_run_id` | order003 |

Stem:

A team is migrating from a legacy on-prem intent recognition system to use Amazon Bedrock with a conversational FM. The legacy system allowed multi-turn conversation context to be provided as a single large string. Bedrock’s model expects a structured list of user/assistant message objects. What is the most important change to the input pipeline to meet Bedrock’s requirements?

Options:

1. Reformat incoming conversation history into a JSON array of message objects with explicit roles
2. Pre-tokenize the conversation using a third-party tokenizer and send as base64
3. Aggregate all conversation turns into a single, newline-delimited string and send as input
4. Send each message turn as a separate request to Bedrock

Correct answer: Reformat incoming conversation history into a JSON array of message objects with explicit roles

Rationale: Bedrock FMs (especially for chat) expect multi-turn context in a JSON format where each turn is an object specifying 'user' or 'assistant'.

Distractors: Pre-tokenize the conversation using a third-party tokenizer and send as base64: Unnecessary and unsupported; Bedrock expects JSON, not pre-tokenized/base64-encoded data.; Aggregate all conversation turns into a single, newline-delimited string and send as input: Loses role information; not in the format Bedrock requires and may degrade model performance.; Send each message turn as a separate request to Bedrock: Breaks up the conversation context and prevents the model from leveraging prior turns.

Misconception tags: Mapping monolithic design to structured API; Misunderstanding conversation formatting

Source trace:

https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-messages.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-02-data-embeddings-vector-stores-rag.md

### P1-AIP-D2-027

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-027 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.3: Implement data validation and processing pipelines for FM consumption. |
| `exam_skill` | Skill 1.3.3: Format input data for FM inference according to model-specific requirements (for example, by using JSON formatting for Amazon Bedrock API requests, structured data preparation for SageMaker AI endpoints, conversation formatting for dialog-based applications). |
| `secondary_exam_skills` | Skill 1.3.4: Enhance input data quality to improve FM response quality and consistency (for example, by using Amazon Bedrock to reformat text, Amazon Comprehend to extract entities, Lambda functions to normalize data). |
| `learning_unit` | Day02-order003 |
| `accelerated_day` | Day 2 |
| `topic` | Model-specific input formatting and data normalization |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Declarative; Procedural; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T051717Z-openai-gpt-4.1-day-02-order003.md item 6 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T051717Z |
| `raw_run_id` | order003 |

Stem:

You are tasked with integrating Amazon Comprehend entity extraction to enhance data quality before sending customer support transcripts to an FM endpoint for summarization. Which pre-processing step most reliably improves downstream FM consistency for entity names?

Options:

1. Normalize extracted entity names so each appears in a standardized canonical form
2. Discard entity names as FMs can always resolve references based on context
3. Embed raw transcripts directly without modification
4. Substitute all identified entities with random placeholders for anonymization

Correct answer: Normalize extracted entity names so each appears in a standardized canonical form

Rationale: Standardizing entity names ensures the FM receives consistent references, reducing ambiguity in summarization.

Distractors: Discard entity names as FMs can always resolve references based on context: FM outputs may become inconsistent or ambiguous if entity forms vary in input.; Embed raw transcripts directly without modification: Misses the opportunity to resolve inconsistencies, reducing summarization quality.; Substitute all identified entities with random placeholders for anonymization: Anonymization is sometimes needed, but here the goal is consistency, not removing identity.

Misconception tags: Overtrusting FM context handling; Confusing normalization and anonymization

Source trace:

focused_artifact

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order003-input-formatting-normalization.md

### P1-AIP-D2-028

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-028 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.3: Implement data validation and processing pipelines for FM consumption. |
| `exam_skill` | Skill 1.3.3: Format input data for FM inference according to model-specific requirements (for example, by using JSON formatting for Amazon Bedrock API requests, structured data preparation for SageMaker AI endpoints, conversation formatting for dialog-based applications). |
| `secondary_exam_skills` | Skill 1.3.4: Enhance input data quality to improve FM response quality and consistency (for example, by using Amazon Bedrock to reformat text, Amazon Comprehend to extract entities, Lambda functions to normalize data). |
| `learning_unit` | Day02-order003 |
| `accelerated_day` | Day 2 |
| `topic` | Model-specific input formatting and data normalization |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Declarative; Procedural; Embedded |
| `question_format` | multiple-response |
| `difficulty` | exam-plus |
| `cognitive_demand` | integrate |
| `estimated_time_seconds` | 180 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T051717Z-openai-gpt-4.1-day-02-order003.md item 7 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T051717Z |
| `raw_run_id` | order003 |

Stem:

You are designing a data-preprocessing pipeline to prepare news articles for Amazon Bedrock for topic classification. The content arrives with non-ASCII characters, inconsistent formatting, and embedded HTML tags. Which combination of pre-processing actions would maximize FM performance?

Options:

1. Remove HTML tags
2. Normalize Unicode to standard ASCII where possible
3. Retain all formatting and HTML for maximum context
4. Trim leading/trailing whitespace
5. Ensure the input payload is structured in JSON matching Bedrock requirements

Correct answer: Remove HTML tags; Normalize Unicode to standard ASCII where possible; Trim leading/trailing whitespace; Ensure the input payload is structured in JSON matching Bedrock requirements

Rationale: Cleaning and normalizing text, as well as structuring the payload to model/API requirements, prevents parsing issues and ensures consistent model performance.

Distractors: Retain all formatting and HTML for maximum context: HTML and inconsistent formatting often introduce noise that degrades FM output quality.

Misconception tags: Believing model benefits from raw/noisy input; Overlooking structural API constraints

Source trace:

focused_artifact, answer_guidance

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day-02-answer-guidance.md

### P1-AIP-D2-029

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-029 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.3: Implement data validation and processing pipelines for FM consumption. |
| `exam_skill` | Skill 1.3.3: Format input data for FM inference according to model-specific requirements (for example, by using JSON formatting for Amazon Bedrock API requests, structured data preparation for SageMaker AI endpoints, conversation formatting for dialog-based applications). |
| `secondary_exam_skills` | Skill 1.3.4: Enhance input data quality to improve FM response quality and consistency (for example, by using Amazon Bedrock to reformat text, Amazon Comprehend to extract entities, Lambda functions to normalize data). |
| `learning_unit` | Day02-order003 |
| `accelerated_day` | Day 2 |
| `topic` | Model-specific input formatting and data normalization |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Declarative; Procedural; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T051717Z-openai-gpt-4.1-day-02-order003.md item 8 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T051717Z |
| `raw_run_id` | order003 |

Stem:

A developer wants to use Bedrock to format prompt strings for downstream FMs as part of an inference pipeline. Which benefit does using Bedrock's prompt formatting functionality provide over ad-hoc string concatenation?

Options:

1. It automatically structures prompts according to model's requirements and reduces inconsistencies
2. It guarantees lowest inference latency for all FMs
3. It enables direct integration with OpenSearch without custom adapters
4. It prevents any potential data drift in model usage

Correct answer: It automatically structures prompts according to model's requirements and reduces inconsistencies

Rationale: Bedrock prompt formatting utilities help ensure that prompts are constructed as expected by the target FM, reducing inconsistencies from manual string handling.

Distractors: It guarantees lowest inference latency for all FMs: Prompt formatting does not impact latency directly.; It enables direct integration with OpenSearch without custom adapters: Prompt formatting is unrelated to OpenSearch integration.; It prevents any potential data drift in model usage: Formatting reduces inconsistency, but drift relates to data and model evolution, not string formatting.

Misconception tags: Equating formatting with performance; Confusing formatting and system integration

Source trace:

study_guide

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-02-data-embeddings-vector-stores-rag.md

### P1-AIP-D2-030

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-030 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.3: Implement data validation and processing pipelines for FM consumption. |
| `exam_skill` | Skill 1.3.3: Format input data for FM inference according to model-specific requirements (for example, by using JSON formatting for Amazon Bedrock API requests, structured data preparation for SageMaker AI endpoints, conversation formatting for dialog-based applications). |
| `secondary_exam_skills` | Skill 1.3.4: Enhance input data quality to improve FM response quality and consistency (for example, by using Amazon Bedrock to reformat text, Amazon Comprehend to extract entities, Lambda functions to normalize data). |
| `learning_unit` | Day02-order003 |
| `accelerated_day` | Day 2 |
| `topic` | Model-specific input formatting and data normalization |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Declarative; Procedural; Embedded |
| `question_format` | multiple-response |
| `difficulty` | hard |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T051717Z-openai-gpt-4.1-day-02-order003.md item 9 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T051717Z |
| `raw_run_id` | order003 |

Stem:

You are configuring a pipeline to feed structured tabular data for regression to a SageMaker AI endpoint. Which actions are essential to ensure input data aligns with the model's expectations for robust inference?

Options:

1. Normalize all numeric fields to a standard range or distribution as used during training
2. Validate input schema and data types match the model’s input signature
3. Provide all string columns in uppercase for consistency
4. Standardize missing values handling as per model requirements
5. Base64 encode the DataFrame before POSTing as the payload

Correct answer: Normalize all numeric fields to a standard range or distribution as used during training; Validate input schema and data types match the model’s input signature; Standardize missing values handling as per model requirements

Rationale: Maintaining feature scaling, matching expected input schemas, and handling nulls are all critical for accurate model inference.

Distractors: Provide all string columns in uppercase for consistency: Case normalization applies only if required or valuable for downstream logic.; Base64 encode the DataFrame before POSTing as the payload: Not typically required unless sending binary data. SageMaker expects certain encodings based on endpoint config.

Misconception tags: Ignoring feature scaling; Unnecessary base64 encoding

Source trace:

focused_artifact, answer_guidance

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order003-input-formatting-normalization.md

### P1-AIP-D2-031

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-031 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.3: Implement data validation and processing pipelines for FM consumption. |
| `exam_skill` | Skill 1.3.3: Format input data for FM inference according to model-specific requirements (for example, by using JSON formatting for Amazon Bedrock API requests, structured data preparation for SageMaker AI endpoints, conversation formatting for dialog-based applications). |
| `secondary_exam_skills` | Skill 1.3.4: Enhance input data quality to improve FM response quality and consistency (for example, by using Amazon Bedrock to reformat text, Amazon Comprehend to extract entities, Lambda functions to normalize data). |
| `learning_unit` | Day02-order003 |
| `accelerated_day` | Day 2 |
| `topic` | Model-specific input formatting and data normalization |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Declarative; Procedural; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T051717Z-openai-gpt-4.1-day-02-order003.md item 10 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T051717Z |
| `raw_run_id` | order003 |

Stem:

An application normalizes all input text to lowercase before sending prompts to a text generation FM. What is a potential risk of this approach?

Options:

1. Loss of important semantic cues such as proper nouns, acronyms, or emphasis
2. Increased computational cost with no benefit
3. Greater model hallucination due to normalization
4. Violation of Bedrock API security requirements

Correct answer: Loss of important semantic cues such as proper nouns, acronyms, or emphasis

Rationale: Lowercasing can remove distinctions critical for names, acronyms, or context, potentially degrading FM output clarity.

Distractors: Increased computational cost with no benefit: Lowercasing is computationally trivial.; Greater model hallucination due to normalization: Hallucination isn't directly related to letter case normalization.; Violation of Bedrock API security requirements: Text normalization doesn't affect API security per se.

Misconception tags: Assuming normalization can't harm semantics

Source trace:

focused_artifact

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day-02-answer-guidance.md

### P1-AIP-D2-032

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-032 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.3: Implement data validation and processing pipelines for FM consumption. |
| `exam_skill` | Skill 1.3.3: Format input data for FM inference according to model-specific requirements (for example, by using JSON formatting for Amazon Bedrock API requests, structured data preparation for SageMaker AI endpoints, conversation formatting for dialog-based applications). |
| `secondary_exam_skills` | Skill 1.3.4: Enhance input data quality to improve FM response quality and consistency (for example, by using Amazon Bedrock to reformat text, Amazon Comprehend to extract entities, Lambda functions to normalize data). |
| `learning_unit` | Day02-order003 |
| `accelerated_day` | Day 2 |
| `topic` | Model-specific input formatting and data normalization |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Declarative; Procedural; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T051717Z-openai-gpt-4.1-day-02-order003.md item 11 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T051717Z |
| `raw_run_id` | order003 |

Stem:

During batch inference using SageMaker, you observe that text summaries generated by your FM endpoint are much shorter for some records, even though the prompts and input lengths are similar. Your pipeline includes custom Lambda normalization before submission. What is a likely explanation?

Options:

1. The normalization script is inadvertently truncating or stripping key content during processing
2. The FM endpoint is running out of available tokens for each request
3. Bedrock API is returning only partial responses due to rate limits
4. The batch processing job is using inconsistent model versions

Correct answer: The normalization script is inadvertently truncating or stripping key content during processing

Rationale: If normalization removes or shortens input, model outputs will shrink regardless of the supplied prompts.

Distractors: The FM endpoint is running out of available tokens for each request: Not indicated as input lengths are similar; token limit issues would affect both.; Bedrock API is returning only partial responses due to rate limits: Rate limiting would result in errors or cut responses for all, not a subset.; The batch processing job is using inconsistent model versions: Would generally yield stylistic/quality differences—not strictly shorter outputs.

Misconception tags: Ignoring processing pipeline errors

Source trace:

study_guide, focused_artifact

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-02-data-embeddings-vector-stores-rag.md

### P1-AIP-D2-033

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-033 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.3: Implement data validation and processing pipelines for FM consumption. |
| `exam_skill` | Skill 1.3.3: Format input data for FM inference according to model-specific requirements (for example, by using JSON formatting for Amazon Bedrock API requests, structured data preparation for SageMaker AI endpoints, conversation formatting for dialog-based applications). |
| `secondary_exam_skills` | Skill 1.3.4: Enhance input data quality to improve FM response quality and consistency (for example, by using Amazon Bedrock to reformat text, Amazon Comprehend to extract entities, Lambda functions to normalize data). |
| `learning_unit` | Day02-order003 |
| `accelerated_day` | Day 2 |
| `topic` | Model-specific input formatting and data normalization |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Declarative; Procedural; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | implement |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T051717Z-openai-gpt-4.1-day-02-order003.md item 12 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T051717Z |
| `raw_run_id` | order003 |

Stem:

A business analyst is using Amazon Bedrock to request text completions from an FM and is seeing frequent JSON parsing errors. What is the most likely cause?

Options:

1. The input payload does not match the JSON schema expected by the selected Bedrock FM
2. The FM is unable to process any text input longer than 100 tokens
3. Bedrock does not support synchronous text completion requests
4. The FM endpoint requires all payloads to be base64 encoded

Correct answer: The input payload does not match the JSON schema expected by the selected Bedrock FM

Rationale: Parsing errors commonly result from mismatched input structure rather than size or encoding issues.

Distractors: The FM is unable to process any text input longer than 100 tokens: Token limits may matter, but this error is more consistent with schema mismatch.; Bedrock does not support synchronous text completion requests: Bedrock supports synchronous invocation; this option is incorrect.; The FM endpoint requires all payloads to be base64 encoded: Payloads must typically be in JSON, not base64-encoded unless binary data.

Misconception tags: Misunderstanding API error sources

Source trace:

study_guide, focused_artifact

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-02-data-embeddings-vector-stores-rag.md

### P1-AIP-D2-034

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-034 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.2: Select and configure optimal embedding solutions to create efficient vector representations for semantic search (for example, by using Amazon Titan embeddings based on dimensionality and domain fit, by evaluating performance characteristics of Amazon Bedrock embedding models, by using Lambda functions to batch generate embeddings). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day02-order004 |
| `accelerated_day` | Day 2 |
| `topic` | Embeddings and vector-similarity fundamentals |
| `knowledge_category` | Knowledge |
| `knowledge_type` | Declarative; Conceptual |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T051804Z-openai-gpt-4.1-day-02-order004.md item 1 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T051804Z |
| `raw_run_id` | order004 |

Stem:

Your team is enhancing a product search engine using Amazon Bedrock embedding models. The product catalog covers both technical documentation and creative marketing descriptions. Which factor should most influence your choice of embedding model?

Options:

1. The domain fit between the embedding model and your catalog content types.
2. The embedding model's default output dimensionality.
3. Whether the model supports multilingual inputs.
4. The model's real-time batch processing throughput.

Correct answer: The domain fit between the embedding model and your catalog content types.

Rationale: Selecting an embedding model whose training and capabilities align with your actual data domain (technical docs & creative marketing) will yield better semantic representations, improving retrieval relevance.

Distractors: The embedding model's default output dimensionality.: Dimensionality matters, but only after domain fit is established; a high or low dimension does not guarantee effectiveness for your data type.; Whether the model supports multilingual inputs.: Multilingual support is valuable if your use case involves multiple languages, but is not the key factor unless your catalog actually requires it.; The model's real-time batch processing throughput.: Throughput is an operational concern, but addressing retrieval relevance starts with domain fit. Scaling can be managed with operational design.

Misconception tags: Confusing feature checklist with fit-for-purpose; Ignoring domain alignment for embeddings

Source trace:

Amazon Bedrock documentation, Bedrock embedding model selection guide

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order004-embeddings-vector-similarity.md

### P1-AIP-D2-035

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-035 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.2: Select and configure optimal embedding solutions to create efficient vector representations for semantic search (for example, by using Amazon Titan embeddings based on dimensionality and domain fit, by evaluating performance characteristics of Amazon Bedrock embedding models, by using Lambda functions to batch generate embeddings). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day02-order004 |
| `accelerated_day` | Day 2 |
| `topic` | Embeddings and vector-similarity fundamentals |
| `knowledge_category` | Knowledge |
| `knowledge_type` | Declarative; Conceptual |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T051804Z-openai-gpt-4.1-day-02-order004.md item 2 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T051804Z |
| `raw_run_id` | order004 |

Stem:

A semantic search API based on Amazon Titan embeddings is returning results that are mostly relevant but occasionally mixes up very similar product names. What is the most likely technical cause?

Options:

1. The embedding vectors for similar product names are not sufficiently separated in the embedding space.
2. The retrieval index is not refreshing on schedule.
3. The search is case-sensitive due to input preprocessing.
4. The model does not support batch embedding generation.

Correct answer: The embedding vectors for similar product names are not sufficiently separated in the embedding space.

Rationale: Semantic similarity depends on the vector separation. If similar names yield close embeddings, retrieval may confuse them unless the embedding model or data processing is improved.

Distractors: The retrieval index is not refreshing on schedule.: Index staleness causes outdated results, not confusion among similar entries.; The search is case-sensitive due to input preprocessing.: Case sensitivity impacts exact string match, not vector-based similarity.; The model does not support batch embedding generation.: Batching affects throughput, not search accuracy.

Misconception tags: Confusing vector similarity with index staleness

Source trace:

Amazon Titan embedding documentation, semantic vector search troubleshooting guide

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day-02-answer-guidance.md

### P1-AIP-D2-036

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-036 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.2: Select and configure optimal embedding solutions to create efficient vector representations for semantic search (for example, by using Amazon Titan embeddings based on dimensionality and domain fit, by evaluating performance characteristics of Amazon Bedrock embedding models, by using Lambda functions to batch generate embeddings). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day02-order004 |
| `accelerated_day` | Day 2 |
| `topic` | Embeddings and vector-similarity fundamentals |
| `knowledge_category` | Knowledge |
| `knowledge_type` | Declarative; Conceptual |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T051804Z-openai-gpt-4.1-day-02-order004.md item 5 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T051804Z |
| `raw_run_id` | order004 |

Stem:

A team's vector search performance degrades as the number of documents grows into millions. The retrieval system uses default embeddings from an Amazon Bedrock model. What foundational factor should be evaluated first?

Options:

1. The domain and dimensionality fit of the embedding model for the growing corpus size.
2. The choice of network protocol between microservices.
3. The availability zone distribution of compute resources.
4. Whether the embedding vectors are encrypted at rest.

Correct answer: The domain and dimensionality fit of the embedding model for the growing corpus size.

Rationale: If embeddings are not optimal for the domain or have suboptimal dimensionality, search quality and performance can deteriorate as data scales.

Distractors: The choice of network protocol between microservices.: This affects latency, not semantic similarity or search relevance.; The availability zone distribution of compute resources.: Resource placement impacts fault tolerance, not core vector search performance.; Whether the embedding vectors are encrypted at rest.: Encryption is essential for security, but does not influence retrieval performance.

Misconception tags: Confusing infra-level with ML-representation issues; Missing root cause in semantic pipeline

Source trace:

Amazon Bedrock documentation on embedding models, vector database scaling guides

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-02-data-embeddings-vector-stores-rag.md

### P1-AIP-D2-037

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-037 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.2: Select and configure optimal embedding solutions to create efficient vector representations for semantic search (for example, by using Amazon Titan embeddings based on dimensionality and domain fit, by evaluating performance characteristics of Amazon Bedrock embedding models, by using Lambda functions to batch generate embeddings). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day02-order004 |
| `accelerated_day` | Day 2 |
| `topic` | Embeddings and vector-similarity fundamentals |
| `knowledge_category` | Knowledge |
| `knowledge_type` | Declarative; Conceptual |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | explain |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T051804Z-openai-gpt-4.1-day-02-order004.md item 6 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T051804Z |
| `raw_run_id` | order004 |

Stem:

A data science lead asserts that cosine similarity will always yield the best results for semantic search using any embedding model. How should you assess this claim?

Options:

1. Cosine similarity is commonly used, but the actual effectiveness depends on how the embedding model’s geometry represents semantic similarity.
2. Cosine similarity is always superior to all other similarity metrics for embedding-based search.
3. You should use Euclidean distance instead since it is designed for high-dimensional data.
4. The choice of similarity metric has no impact on search results.

Correct answer: Cosine similarity is commonly used, but the actual effectiveness depends on how the embedding model’s geometry represents semantic similarity.

Rationale: Different models may encode semantic similarity in ways that suit cosine, Euclidean, or other metrics; best practice is empirical alignment, not assumption.

Distractors: Cosine similarity is always superior to all other similarity metrics for embedding-based search.: No single metric fits all embedding models; model training may favor a specific geometry.; You should use Euclidean distance instead since it is designed for high-dimensional data.: Euclidean distance may not be suitable depending on normalization and model design.; The choice of similarity metric has no impact on search results.: Metric choice is fundamental to semantic retrieval success.

Misconception tags: Assuming universal best practice; Overgeneralizing model metric compatibility

Source trace:

Amazon Bedrock/Titan embedding tutorials, vector similarity best-practices docs

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order004-embeddings-vector-similarity.md

### P1-AIP-D2-038

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-038 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.2: Select and configure optimal embedding solutions to create efficient vector representations for semantic search (for example, by using Amazon Titan embeddings based on dimensionality and domain fit, by evaluating performance characteristics of Amazon Bedrock embedding models, by using Lambda functions to batch generate embeddings). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day02-order004 |
| `accelerated_day` | Day 2 |
| `topic` | Embeddings and vector-similarity fundamentals |
| `knowledge_category` | Knowledge |
| `knowledge_type` | Declarative; Conceptual |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T051804Z-openai-gpt-4.1-day-02-order004.md item 7 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T051804Z |
| `raw_run_id` | order004 |

Stem:

A developer wants to store document embeddings generated by Amazon Titan in a vector database. Which factor is least likely to be handled by the embedding model itself?

Options:

1. Enforcing fine-grained access control on embedded data.
2. Ensuring consistent vector dimensions.
3. Capturing semantic similarity for domain-specific language.
4. Outputting in a standard vector serialization format.

Correct answer: Enforcing fine-grained access control on embedded data.

Rationale: Embedding models only generate semantic representations. Data access/security is managed by storage or application layers, not the embedding model.

Distractors: Ensuring consistent vector dimensions.: Embedding models produce fixed-dimension vectors for compatibility.; Capturing semantic similarity for domain-specific language.: Domain-appropriate embeddings reflect semantic similarity.; Outputting in a standard vector serialization format.: Supported output formats ensure downstream compatibility.

Misconception tags: Attributing authorization to embedding model; Confusing representation with access control

Source trace:

Amazon Titan embedding documentation; vector database security practices

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day-02-answer-guidance.md

### P1-AIP-D2-039

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-039 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.2: Select and configure optimal embedding solutions to create efficient vector representations for semantic search (for example, by using Amazon Titan embeddings based on dimensionality and domain fit, by evaluating performance characteristics of Amazon Bedrock embedding models, by using Lambda functions to batch generate embeddings). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day02-order004 |
| `accelerated_day` | Day 2 |
| `topic` | Embeddings and vector-similarity fundamentals |
| `knowledge_category` | Knowledge |
| `knowledge_type` | Declarative; Conceptual |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | compare |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T051804Z-openai-gpt-4.1-day-02-order004.md item 8 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T051804Z |
| `raw_run_id` | order004 |

Stem:

You are comparing semantic retrieval results using embeddings generated by two different Amazon Bedrock models. Both pass basic functional tests, but one yields noticeably more relevant results for legal documents. Which is the most likely explanation?

Options:

1. The more relevant embedding model has been pretrained or fine-tuned on legal-domain content.
2. The less relevant model uses higher-dimensional embeddings.
3. The underlying vector database is misconfigured.
4. Vector similarity metric differs between the two runs.

Correct answer: The more relevant embedding model has been pretrained or fine-tuned on legal-domain content.

Rationale: Domain-specific pretraining or fine-tuning enables the embedding model to recognize and encode relevant legal concepts and vocabulary with greater accuracy.

Distractors: The less relevant model uses higher-dimensional embeddings.: Dimension alone does not determine relevance; embedding quality and domain fit are primary.; The underlying vector database is misconfigured.: A misconfigured database could affect recall, but functional tests would usually fail in those cases.; Vector similarity metric differs between the two runs.: Comparing results for the same metric ensures metric is not the cause. The scenario states both models passed functional tests.

Misconception tags: Confusing vector dimension with relevance; Ignoring domain pretraining

Source trace:

Amazon Bedrock documentation, model card details

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order004-embeddings-vector-similarity.md

### P1-AIP-D2-040

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-040 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.2: Select and configure optimal embedding solutions to create efficient vector representations for semantic search (for example, by using Amazon Titan embeddings based on dimensionality and domain fit, by evaluating performance characteristics of Amazon Bedrock embedding models, by using Lambda functions to batch generate embeddings). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day02-order004 |
| `accelerated_day` | Day 2 |
| `topic` | Embeddings and vector-similarity fundamentals |
| `knowledge_category` | Knowledge |
| `knowledge_type` | Declarative; Conceptual |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | integrate |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T051804Z-openai-gpt-4.1-day-02-order004.md item 9 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T051804Z |
| `raw_run_id` | order004 |

Stem:

A developer is asked why semantic search results from the team’s knowledge base sometimes omit recently uploaded documents, even though embeddings are generated immediately upon upload. Which is the most likely reason?

Options:

1. The vector index is not updated or reloaded after new embeddings are generated.
2. The embedding model fails to recognize domain-specific content.
3. Cosine similarity is not correctly implemented.
4. Lambda function concurrency is too low.

Correct answer: The vector index is not updated or reloaded after new embeddings are generated.

Rationale: For new documents to be searchable, their embeddings must be added to the vector index. Simply generating embeddings is insufficient.

Distractors: The embedding model fails to recognize domain-specific content.: That would cause retrieval of less relevant documents, not omission from the results.; Cosine similarity is not correctly implemented.: If this were true, all search results would be degraded.; Lambda function concurrency is too low.: This could delay processing, but if embedding exists, the index update remains key.

Misconception tags: Assuming embedding generation alone suffices; Omitting index update action

Source trace:

Vector store index update documentation

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day-02-answer-guidance.md

### P1-AIP-D2-041

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-041 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.2: Select and configure optimal embedding solutions to create efficient vector representations for semantic search (for example, by using Amazon Titan embeddings based on dimensionality and domain fit, by evaluating performance characteristics of Amazon Bedrock embedding models, by using Lambda functions to batch generate embeddings). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day02-order004 |
| `accelerated_day` | Day 2 |
| `topic` | Embeddings and vector-similarity fundamentals |
| `knowledge_category` | Knowledge |
| `knowledge_type` | Declarative; Conceptual |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T051804Z-openai-gpt-4.1-day-02-order004.md item 10 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T051804Z |
| `raw_run_id` | order004 |

Stem:

A company’s semantic search pipeline uses Amazon Bedrock for embeddings and a managed vector database. Some users report that search results lack context-sensitive matches (for example, 'Apple' as a company vs. fruit). Which is the best course of action?

Options:

1. Assess if the embedding model sufficiently encodes disambiguating context and consider using prompt engineering or model selection tuned for disambiguation.
2. Switch to a traditional keyword-based search engine.
3. Increase the vector dimensionality during storage.
4. Disable stop-word removal in preprocessing.

Correct answer: Assess if the embedding model sufficiently encodes disambiguating context and consider using prompt engineering or model selection tuned for disambiguation.

Rationale: Contextual embedding models or prompt engineering may increase the ability to distinguish between meanings of ambiguous words, improving semantic matches.

Distractors: Switch to a traditional keyword-based search engine.: Keyword search can worsen context ambiguity because it cannot resolve meaning reliably.; Increase the vector dimensionality during storage.: Dimensionality does not guarantee disambiguation; the model's training and inference prompt context is more important.; Disable stop-word removal in preprocessing.: This affects low-value words, not the disambiguation of key terms.

Misconception tags: Assuming higher vector dimensions fix context; Confusing preprocessing with embedding quality

Source trace:

Amazon Bedrock embedding docs, prompt engineering for context disambiguation

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-02-data-embeddings-vector-stores-rag.md

### P1-AIP-D2-042

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-042 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.2: Select and configure optimal embedding solutions to create efficient vector representations for semantic search (for example, by using Amazon Titan embeddings based on dimensionality and domain fit, by evaluating performance characteristics of Amazon Bedrock embedding models, by using Lambda functions to batch generate embeddings). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day02-order004 |
| `accelerated_day` | Day 2 |
| `topic` | Embeddings and vector-similarity fundamentals |
| `knowledge_category` | Knowledge |
| `knowledge_type` | Declarative; Conceptual |
| `question_format` | multiple-response |
| `difficulty` | exam-plus |
| `cognitive_demand` | judge |
| `estimated_time_seconds` | 180 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T051804Z-openai-gpt-4.1-day-02-order004.md item 11 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T051804Z |
| `raw_run_id` | order004 |

Stem:

A team is evaluating potential embedding models for a new customer support chatbot that must handle product tech specs, installation instructions, and casual user queries. Which factors should they prioritize when selecting an embedding solution? (Select TWO.)

Options:

1. Alignment between the model’s pretraining corpus and the support document domains.
2. Embeddings' ability to handle multilingual queries.
3. The maximum throughput of the API during bulk processing.
4. The region(s) in which the embedding service is available.
5. Embedding model suitability for both formal technical text and informal language.

Correct answer: Alignment between the model’s pretraining corpus and the support document domains.; Embedding model suitability for both formal technical text and informal language.

Rationale: For a support chatbot, domain alignment ensures accurate semantic search, while the ability to handle both formal and informal text ensures broad coverage of varied user queries.

Distractors: Embeddings' ability to handle multilingual queries.: This is only critical if users regularly submit queries in multiple languages.; The maximum throughput of the API during bulk processing.: Throughput affects efficiency, but is not a primary relevance concern.; The region(s) in which the embedding service is available.: Region is an operational decision, not a semantic one unless low latency or compliance is paramount.

Misconception tags: Overvaluing throughput over semantic alignment; Confusing region/operational with embedding fitness

Source trace:

Amazon Bedrock embedding solution selection guides

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-02-data-embeddings-vector-stores-rag.md

### P1-AIP-D2-043

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-043 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.2: Select and configure optimal embedding solutions to create efficient vector representations for semantic search (for example, by using Amazon Titan embeddings based on dimensionality and domain fit, by evaluating performance characteristics of Amazon Bedrock embedding models, by using Lambda functions to batch generate embeddings). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day02-order004 |
| `accelerated_day` | Day 2 |
| `topic` | Embeddings and vector-similarity fundamentals |
| `knowledge_category` | Knowledge |
| `knowledge_type` | Declarative; Conceptual |
| `question_format` | multiple-response |
| `difficulty` | exam-plus |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 180 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T051804Z-openai-gpt-4.1-day-02-order004.md item 12 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T051804Z |
| `raw_run_id` | order004 |

Stem:

A financial analytics platform wants to maximize the relevance of retrieval-augmented search using document embeddings. Which practices can improve semantic retrieval performance? (Select TWO.)

Options:

1. Choose an embedding model trained or tuned for the financial domain.
2. Preprocess input text to remove extraneous formatting and unify terminology.
3. Select an embedding model with the highest available vector dimension.
4. Encrypt the vector store to protect sensitive embeddings.
5. Batch duplicate documents to create more vectors in the index.

Correct answer: Choose an embedding model trained or tuned for the financial domain.; Preprocess input text to remove extraneous formatting and unify terminology.

Rationale: Semantic retrieval is improved by domain-specific embeddings and normalization/unification to reduce term ambiguity.

Distractors: Select an embedding model with the highest available vector dimension.: Larger vector space does not guarantee better relevance.; Encrypt the vector store to protect sensitive embeddings.: Security is important but does not affect retrieval relevance.; Batch duplicate documents to create more vectors in the index.: Duplication only bloats the index, not performance.

Misconception tags: Assuming bigger-dimension embeddings always boost relevance; Confusing security or duplicate vectors with retrieval tuning

Source trace:

Domain-specific embedding best-practices; Bedrock embedding pipelines

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order004-embeddings-vector-similarity.md

### P1-AIP-D2-044

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-044 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.2: Select and configure optimal embedding solutions to create efficient vector representations for semantic search (for example, by using Amazon Titan embeddings based on dimensionality and domain fit, by evaluating performance characteristics of Amazon Bedrock embedding models, by using Lambda functions to batch generate embeddings). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day02-order004 |
| `accelerated_day` | Day 2 |
| `topic` | Embeddings and vector-similarity fundamentals |
| `knowledge_category` | Knowledge |
| `knowledge_type` | Declarative; Conceptual |
| `question_format` | multiple-response |
| `difficulty` | hard |
| `cognitive_demand` | compare |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T051804Z-openai-gpt-4.1-day-02-order004.md item 13 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T051804Z |
| `raw_run_id` | order004 |

Stem:

A hospital IT department is evaluating embedding methods for searching EMR (electronic medical records) across multiple languages and formats. In addition to confirming the embedding model's support for medical vocabularies, which considerations should factor into their embedding workflow? (Select TWO.)

Options:

1. Ensuring embeddings are generated consistently across all supported languages.
2. Batch generation of embeddings using Lambda functions for scalability.
3. Storing embeddings in plain-text format for maximum transparency.
4. Disabling any pre-tokenization steps for raw text.
5. Evaluating the model's handling of rare and out-of-vocabulary medical terms.

Correct answer: Ensuring embeddings are generated consistently across all supported languages.; Evaluating the model's handling of rare and out-of-vocabulary medical terms.

Rationale: Multilingual and specialized domain data require models capable of consistent embeddings across languages and proper handling of specialized/rare terms.

Distractors: Batch generation of embeddings using Lambda functions for scalability.: This is an implementation efficiency but does not impact semantic compatibility or accuracy.; Storing embeddings in plain-text format for maximum transparency.: Plain-text storage brings no semantic advantage and may raise security issues.; Disabling any pre-tokenization steps for raw text.: Proper tokenization is crucial for consistent embedding quality.

Misconception tags: Confusing workflow automation with semantic compatibility; Ignoring multilingual/rare word risks

Source trace:

Multilingual and domain vocabulary embedding guides; Bedrock/Titan healthcare embedding docs

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order004-embeddings-vector-similarity.md

### P1-AIP-D2-045

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-045 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.1: Develop effective document segmentation approaches to optimize retrieval performance for FM context augmentation (for example, by using Amazon Bedrock chunking capabilities, Lambda functions to implement fixed-size chunking, custom processing for hierarchical chunking based on content structure). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day02-order005 |
| `accelerated_day` | Day 2 |
| `topic` | Document chunking and segmentation |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Causal; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | implement |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T051845Z-openai-gpt-4.1-day-02-order005.md item 1 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T051845Z |
| `raw_run_id` | order005 |

Stem:

A retail company is building a RAG solution on AWS to answer customer queries about order policies. Their source documents include contracts, long FAQs, and some internal wikis. To maximize relevant information in the LLM context and avoid splitting meaningful paragraphs, what chunking strategy should they implement in their preprocessing pipeline?

Options:

1. Hierarchical chunking based on document structure, with paragraph-level segmentation wherever possible
2. Fixed-size chunking using a token count (e.g., 256 tokens per chunk)
3. Chunking based on arbitrary character count boundaries
4. No chunking; the entire document is embedded as a single vector

Correct answer: Hierarchical chunking based on document structure, with paragraph-level segmentation wherever possible

Rationale: Hierarchical chunking respects the underlying document structure and reduces the risk of splitting informative paragraphs, leading to more contextually relevant retrievals by the FM.

Distractors: Fixed-size chunking using a token count (e.g., 256 tokens per chunk): This can split paragraphs mid-sentence or disconnect related information, reducing semantic coherence.; Chunking based on arbitrary character count boundaries: This approach ignores document semantics and structure, resulting in difficult-to-retrieve or out-of-context chunks.; No chunking; the entire document is embedded as a single vector: Embedding full documents can exceed model or vector-store limits and makes it difficult to retrieve only the most relevant parts during RAG.

Misconception tags: Assuming one chunk size fits all; Ignoring document structure

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order005-document-chunking-segmentation.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order005-document-chunking-segmentation.md

### P1-AIP-D2-046

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-046 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.1: Develop effective document segmentation approaches to optimize retrieval performance for FM context augmentation (for example, by using Amazon Bedrock chunking capabilities, Lambda functions to implement fixed-size chunking, custom processing for hierarchical chunking based on content structure). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day02-order005 |
| `accelerated_day` | Day 2 |
| `topic` | Document chunking and segmentation |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Causal; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T051845Z-openai-gpt-4.1-day-02-order005.md item 2 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T051845Z |
| `raw_run_id` | order005 |

Stem:

You notice that retrieval queries against your RAG-enabled customer-support system often return either irrelevant chunks or split answers that are incomplete. The document pipeline uses only a simple character-based fixed-size chunking strategy. What is the most likely cause of the poor retrieval quality?

Options:

1. Chunk boundaries do not align with semantic units, causing loss of contextual meaning
2. The embedding model's dimensionality is too low for the domain
3. Customer queries use keywords not present in the original documents
4. The vector store lacks real-time synchronization with the source repository

Correct answer: Chunk boundaries do not align with semantic units, causing loss of contextual meaning

Rationale: Simple character-based chunking often splits sentences or semantic blocks, resulting in out-of-context chunks and degraded retrieval.

Distractors: The embedding model's dimensionality is too low for the domain: While embedding dimensionality can affect performance, the described symptoms directly point to chunk boundary issues.; Customer queries use keywords not present in the original documents: This may affect retrieval if queries are truly orthogonal, but the root problem described is about chunk splitting, not lexical coverage.; The vector store lacks real-time synchronization with the source repository: This would cause retrieval of stale data, not systematically split or irrelevant chunks.

Misconception tags: Attributing semantic mistakes to embedding configuration; Ignoring chunk boundary effects

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order005-document-chunking-segmentation.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order005-document-chunking-segmentation.md

### P1-AIP-D2-047

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-047 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.1: Develop effective document segmentation approaches to optimize retrieval performance for FM context augmentation (for example, by using Amazon Bedrock chunking capabilities, Lambda functions to implement fixed-size chunking, custom processing for hierarchical chunking based on content structure). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day02-order005 |
| `accelerated_day` | Day 2 |
| `topic` | Document chunking and segmentation |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Causal; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T051845Z-openai-gpt-4.1-day-02-order005.md item 3 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T051845Z |
| `raw_run_id` | order005 |

Stem:

A legal team is preparing long legal documents for ingestion into an FM-backed retrieval system. The documents are highly structured, often containing sections, subsections, and bullet points. Which method will best preserve the documents' original meaning and maximize retrieval relevance?

Options:

1. Custom chunking pipeline that segments documents at headers and subheaders
2. Uniform chunking with a fixed-size in tokens, regardless of structure
3. Line-by-line splitting of the document into individual sentences
4. Uploading full documents with no segmentation or chunking

Correct answer: Custom chunking pipeline that segments documents at headers and subheaders

Rationale: Segmenting documents at logical boundaries helps retain context and makes it easier to retrieve coherent, relevant passages.

Distractors: Uniform chunking with a fixed-size in tokens, regardless of structure: May split logical sections apart, reducing contextual understanding.; Line-by-line splitting of the document into individual sentences: Creates overly granular chunks, losing the broader context necessary in legal reasoning.; Uploading full documents with no segmentation or chunking: Large documents may exceed input limits and make retrieval of specific topics inefficient.

Misconception tags: One-size-fits-all chunking; Overly fine segmentation

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order005-document-chunking-segmentation.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order005-document-chunking-segmentation.md

### P1-AIP-D2-048

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-048 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.1: Develop effective document segmentation approaches to optimize retrieval performance for FM context augmentation (for example, by using Amazon Bedrock chunking capabilities, Lambda functions to implement fixed-size chunking, custom processing for hierarchical chunking based on content structure). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day02-order005 |
| `accelerated_day` | Day 2 |
| `topic` | Document chunking and segmentation |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Causal; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T051845Z-openai-gpt-4.1-day-02-order005.md item 4 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T051845Z |
| `raw_run_id` | order005 |

Stem:

A startup reports that their RAG solution frequently returns duplicate or overlapping information to the FM, resulting in bloated inputs and cost overruns. They currently use sliding window chunking with 80% overlap. What should they change in their chunking strategy?

Options:

1. Reduce chunk overlap to minimize redundancy and post-processing cost
2. Switch to no-overlap chunking, even if chunks become larger
3. Adopt random-sized chunking to introduce variability
4. Increase overlap even further for more context per chunk

Correct answer: Reduce chunk overlap to minimize redundancy and post-processing cost

Rationale: High overlap leads to redundancy and increased retrieval/inference costs; reducing overlap is recommended unless context retention is critical.

Distractors: Switch to no-overlap chunking, even if chunks become larger: No-overlap may sacrifice context; the primary issue is with excessive redundancy, not zero overlap.; Adopt random-sized chunking to introduce variability: Random sizing undermines predictability and efficient retrieval.; Increase overlap even further for more context per chunk: This would exacerbate redundancy and cost issues.

Misconception tags: Overlap solves all context problems; Chunk size equals retrieval relevance

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order005-document-chunking-segmentation.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order005-document-chunking-segmentation.md

### P1-AIP-D2-049

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-049 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.1: Develop effective document segmentation approaches to optimize retrieval performance for FM context augmentation (for example, by using Amazon Bedrock chunking capabilities, Lambda functions to implement fixed-size chunking, custom processing for hierarchical chunking based on content structure). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day02-order005 |
| `accelerated_day` | Day 2 |
| `topic` | Document chunking and segmentation |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Causal; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | compare |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T051845Z-openai-gpt-4.1-day-02-order005.md item 5 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T051845Z |
| `raw_run_id` | order005 |

Stem:

You are designing a chunking pipeline for a media company's RAG system. News articles range from a few paragraphs to dozens of pages. What is the best approach to provide flexible, contextually-coherent chunk sizes that adapt to document length?

Options:

1. Implement adaptive chunking, adjusting chunk size based on document structure and length
2. Enforce a strict chunk size (e.g., always 512 tokens) for all documents
3. Chunk each sentence as a separate unit for maximum granularity
4. Pre-merge all articles into a corpus and embed as a single large document

Correct answer: Implement adaptive chunking, adjusting chunk size based on document structure and length

Rationale: Adaptive chunking allows for optimized retrieval by matching chunk sizes to both document structure and length—handling small and large articles appropriately.

Distractors: Enforce a strict chunk size (e.g., always 512 tokens) for all documents: One-size-fits-all may fragment small articles or exceed context limits for larger ones.; Chunk each sentence as a separate unit for maximum granularity: Produces too many disconnected chunks, losing article-level context.; Pre-merge all articles into a corpus and embed as a single large document: Prevents effective retrieval of individual articles and will hit input size limitations.

Misconception tags: Uniform chunk size for heterogeneous sources; Sentence-level chunking always best

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order005-document-chunking-segmentation.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order005-document-chunking-segmentation.md

### P1-AIP-D2-050

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-050 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.1: Develop effective document segmentation approaches to optimize retrieval performance for FM context augmentation (for example, by using Amazon Bedrock chunking capabilities, Lambda functions to implement fixed-size chunking, custom processing for hierarchical chunking based on content structure). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day02-order005 |
| `accelerated_day` | Day 2 |
| `topic` | Document chunking and segmentation |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Causal; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | explain |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T051845Z-openai-gpt-4.1-day-02-order005.md item 6 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T051845Z |
| `raw_run_id` | order005 |

Stem:

A team creates vector embeddings from policy documents but retrieval often misses relevant context. Their chunking process segments each document into exactly 256-character chunks regardless of content. What is the principal drawback with this approach?

Options:

1. Character-based chunking can split sentences or topics, losing context for retrieval
2. It reduces chunk quantity, improving search times but hurting granularity
3. It standardizes chunk size across all documents, simplifying storage
4. The model embedding the chunks only supports JSON-formatted input

Correct answer: Character-based chunking can split sentences or topics, losing context for retrieval

Rationale: Breaking by character count can ignore natural breaks in information and result in poor semantic retrieval.

Distractors: It reduces chunk quantity, improving search times but hurting granularity: 256 characters is a small chunk; this actually increases chunk quantity, not the opposite.; It standardizes chunk size across all documents, simplifying storage: While storage may be uniform, it sacrifices retrieval quality due to poor alignment with semantics.; The model embedding the chunks only supports JSON-formatted input: Model format compatibility is unrelated to the chunking schema or input issues described.

Misconception tags: Equating structural and technical uniformity; Confusing input format with chunking approach

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order005-document-chunking-segmentation.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order005-document-chunking-segmentation.md

### P1-AIP-D2-051

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-051 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.1: Develop effective document segmentation approaches to optimize retrieval performance for FM context augmentation (for example, by using Amazon Bedrock chunking capabilities, Lambda functions to implement fixed-size chunking, custom processing for hierarchical chunking based on content structure). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day02-order005 |
| `accelerated_day` | Day 2 |
| `topic` | Document chunking and segmentation |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Causal; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T051845Z-openai-gpt-4.1-day-02-order005.md item 7 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T051845Z |
| `raw_run_id` | order005 |

Stem:

An AWS Generative AI team wants to optimize chunking for their specialized FM context. Their corpus consists of academic papers with consistent section headings and structure. Which approach should they choose to balance retrieval performance and storage requirements?

Options:

1. Segment documents at each major section heading and produce embeddings for each section
2. Create overlapping chunks with sliding windows for maximal context overlap
3. Break all documents into fixed 100-token chunks
4. Use a random chunking seed to create variable-sized chunks

Correct answer: Segment documents at each major section heading and produce embeddings for each section

Rationale: Section-based chunking retains topical context, improves retrieval and manages a predictable number of chunks per document.

Distractors: Create overlapping chunks with sliding windows for maximal context overlap: Maximizes context, but at the cost of greatly increased storage and retrieval latency.; Break all documents into fixed 100-token chunks: Could fragment logical sections, harming contextual integrity in retrieval.; Use a random chunking seed to create variable-sized chunks: Introduces inconsistency, making retrieval unpredictable and storage inefficient.

Misconception tags: Assuming overlap always improves quality; Random chunking increases diversity

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order005-document-chunking-segmentation.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order005-document-chunking-segmentation.md

### P1-AIP-D2-052

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-052 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.1: Develop effective document segmentation approaches to optimize retrieval performance for FM context augmentation (for example, by using Amazon Bedrock chunking capabilities, Lambda functions to implement fixed-size chunking, custom processing for hierarchical chunking based on content structure). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day02-order005 |
| `accelerated_day` | Day 2 |
| `topic` | Document chunking and segmentation |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Causal; Conditional |
| `question_format` | multiple-response |
| `difficulty` | hard |
| `cognitive_demand` | judge |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T051845Z-openai-gpt-4.1-day-02-order005.md item 8 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T051845Z |
| `raw_run_id` | order005 |

Stem:

A team is tasked with segmenting a corpus of technical manuals for use in an FM retrieval pipeline. They want to optimize for retrieval precision and minimize out-of-context results. Which approaches should the team prioritize? (Select TWO.)

Options:

1. Chunk documents at logical section and subsection boundaries
2. Implement minimal or no overlap unless context retention is essential
3. Always use maximum chunk overlap for context propagation
4. Split text arbitrarily after a set number of characters
5. Combine all documents into a single large context window

Correct answer: Chunk documents at logical section and subsection boundaries; Implement minimal or no overlap unless context retention is essential

Rationale: Both strategies preserve semantics and reduce the risk of redundant or irrelevant retrieval.

Distractors: Always use maximum chunk overlap for context propagation: Maximal overlap can create redundancy, bloat, and increased retrieval/inference load.; Split text arbitrarily after a set number of characters: Ignores document structure, increasing risk of out-of-context chunks.; Combine all documents into a single large context window: Unwieldy and unlikely to fit FM/model input windows; poor for targeted retrieval.

Misconception tags: Overlap always helps; Arbitrary chunking is sufficient

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order005-document-chunking-segmentation.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order005-document-chunking-segmentation.md

### P1-AIP-D2-053

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-053 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.1: Develop effective document segmentation approaches to optimize retrieval performance for FM context augmentation (for example, by using Amazon Bedrock chunking capabilities, Lambda functions to implement fixed-size chunking, custom processing for hierarchical chunking based on content structure). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day02-order005 |
| `accelerated_day` | Day 2 |
| `topic` | Document chunking and segmentation |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Causal; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T051845Z-openai-gpt-4.1-day-02-order005.md item 9 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T051845Z |
| `raw_run_id` | order005 |

Stem:

Your dataset contains short emails, entire books, and meeting transcripts. Which chunking architecture should you configure to best balance retrieval accuracy and computational efficiency for FM augmentation?

Options:

1. Apply dynamic chunking: use whole-text embedding for short documents and section-based chunking for long documents
2. Chunk all documents into equally sized, fixed-overlap windows regardless of document type
3. Always split text after a standard number of words, no matter the document length
4. Combine multiple documents into large super-chunks before embedding

Correct answer: Apply dynamic chunking: use whole-text embedding for short documents and section-based chunking for long documents

Rationale: Dynamic chunking adapts to document length and structure, combining retrieval accuracy and computational efficiency.

Distractors: Chunk all documents into equally sized, fixed-overlap windows regardless of document type: Ignores heterogeneity and results in poor optimization across the corpus.; Always split text after a standard number of words, no matter the document length: Risks breaking up contained ideas or failing to capture enough context for longer documents.; Combine multiple documents into large super-chunks before embedding: Destroys document boundaries, reducing retrieval precision.

Misconception tags: Uniform chunking for all document types; Super-chunking improves recall

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order005-document-chunking-segmentation.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order005-document-chunking-segmentation.md

### P1-AIP-D2-054

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-054 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.1: Develop effective document segmentation approaches to optimize retrieval performance for FM context augmentation (for example, by using Amazon Bedrock chunking capabilities, Lambda functions to implement fixed-size chunking, custom processing for hierarchical chunking based on content structure). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day02-order005 |
| `accelerated_day` | Day 2 |
| `topic` | Document chunking and segmentation |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Causal; Conditional |
| `question_format` | multiple-response |
| `difficulty` | exam-plus |
| `cognitive_demand` | integrate |
| `estimated_time_seconds` | 180 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T051845Z-openai-gpt-4.1-day-02-order005.md item 10 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T051845Z |
| `raw_run_id` | order005 |

Stem:

An enterprise is creating a chunking framework for a multilingual knowledge base with varying document lengths. To support efficient FM context augmentation and optimize retrieval, which considerations should they prioritize in their segmentation design? (Select THREE.)

Options:

1. Chunk at logical boundaries respecting language-specific structures
2. Allow document-type-specific chunking rules
3. Use identical token-based chunk sizes for all documents
4. Balance chunk size to avoid exceeding FM context window limits
5. Prioritize embedding full documents for smallest sources

Correct answer: Chunk at logical boundaries respecting language-specific structures; Allow document-type-specific chunking rules; Balance chunk size to avoid exceeding FM context window limits

Rationale: Respecting structure and language increases retrieval precision, document-type rules allow tuning, and respecting context size avoids truncation.

Distractors: Use identical token-based chunk sizes for all documents: Does not handle diversity; can lead to inefficient retrieval for varying lengths.; Prioritize embedding full documents for smallest sources: Can work for very short documents, but not a universal strategy and does not address segmentation for larger sources.

Misconception tags: Uniformity across languages; Universal chunk size suffices

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order005-document-chunking-segmentation.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order005-document-chunking-segmentation.md

### P1-AIP-D2-055

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-055 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.1: Develop effective document segmentation approaches to optimize retrieval performance for FM context augmentation (for example, by using Amazon Bedrock chunking capabilities, Lambda functions to implement fixed-size chunking, custom processing for hierarchical chunking based on content structure). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day02-order005 |
| `accelerated_day` | Day 2 |
| `topic` | Document chunking and segmentation |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Causal; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | predict |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T051845Z-openai-gpt-4.1-day-02-order005.md item 11 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T051845Z |
| `raw_run_id` | order005 |

Stem:

After redesigning their chunking pipeline to segment insurance policies by both section and subsection, a company sees an uptick in retrieval relevance, but also a moderate increase in the number of chunks stored. What should they expect as a long-term effect of this adjustment?

Options:

1. Retrieval performance and precision will improve, with manageable storage cost increase
2. Retrieval quality will worsen due to over-segmentation
3. Inference latency will skyrocket, making the system unusable
4. FM context windows will consistently be exceeded, causing input errors

Correct answer: Retrieval performance and precision will improve, with manageable storage cost increase

Rationale: Granular, structure-aware segmentation boosts retrieval relevance. The storage cost increase is expected, but manageable compared to the improvement.

Distractors: Retrieval quality will worsen due to over-segmentation: Segmentation at logical boundaries usually enhances, not degrades, retrieval for structured documents.; Inference latency will skyrocket, making the system unusable: Sensible segmentation won’t cause dramatic latency increases.; FM context windows will consistently be exceeded, causing input errors: Breaking at section/subsection level makes it easier to respect context limits.

Misconception tags: Assuming more chunks harm relevance; Overestimating storage/latency impact

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order005-document-chunking-segmentation.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order005-document-chunking-segmentation.md

### P1-AIP-D2-056

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-056 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.1: Develop effective document segmentation approaches to optimize retrieval performance for FM context augmentation (for example, by using Amazon Bedrock chunking capabilities, Lambda functions to implement fixed-size chunking, custom processing for hierarchical chunking based on content structure). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day02-order005 |
| `accelerated_day` | Day 2 |
| `topic` | Document chunking and segmentation |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Causal; Conditional |
| `question_format` | multiple-response |
| `difficulty` | hard |
| `cognitive_demand` | optimize |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T051845Z-openai-gpt-4.1-day-02-order005.md item 12 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T051845Z |
| `raw_run_id` | order005 |

Stem:

A life sciences research team must chunk diverse lab protocols, which vary wildly in length, format, and structure. What best practices should they apply to optimize semantic retrieval? (Select TWO.)

Options:

1. Analyze each protocol's structure and apply custom chunking rules based on layout
2. Set a variable chunk size threshold tuned by document type and structure
3. Impose a universal fixed-size chunk for all lab protocols
4. Favor maximum overlap in all chunking to avoid context loss
5. Ignore logical sectioning and chunk only on page breaks

Correct answer: Analyze each protocol's structure and apply custom chunking rules based on layout; Set a variable chunk size threshold tuned by document type and structure

Rationale: Structure-aware and adaptive strategies boost retrieval accuracy for complex, non-uniform scientific documents.

Distractors: Impose a universal fixed-size chunk for all lab protocols: Ignores the heterogeneity of protocol formats and lengths.; Favor maximum overlap in all chunking to avoid context loss: Excessive overlap can become costly and redundant, without guaranteeing semantic integrity.; Ignore logical sectioning and chunk only on page breaks: Page breaks usually don’t align with semantic boundaries, lowering retrieval precision.

Misconception tags: Fixed chunk size works for all; Maximize overlap at all costs

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order005-document-chunking-segmentation.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order005-document-chunking-segmentation.md

### P1-AIP-D2-057

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-057 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.4: Design and implement vector store solutions. |
| `exam_skill` | Skill 1.4.2: Develop comprehensive metadata frameworks to improve search precision and context awareness for FM interactions (for example, by using S3 object metadata for document timestamps, custom attributes for authorship information, tagging systems for domain classification). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day02-order006 |
| `accelerated_day` | Day 2 |
| `topic` | Metadata design and filtering |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T051925Z-openai-gpt-4.1-day-02-order006.md item 1 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T051925Z |
| `raw_run_id` | order006 |

Stem:

A team implements a vector store for FM-augmented Q&A over internal policy documents. Users from multiple departments need to receive contextually relevant answers and not see content from other departments. Which approach best ensures department-level access control during retrieval?

Options:

1. Tag documents in the vector store with department metadata and apply metadata filters at query time
2. Rely on embedding space distance to separate department content
3. Add department names to document text so FM-generated responses reflect access constraints
4. Configure per-user API keys for the vector store, without attaching metadata

Correct answer: Tag documents in the vector store with department metadata and apply metadata filters at query time

Rationale: This method uses metadata tags for department ownership and leverages metadata filtering during retrieval, enforcing access policies efficiently and precisely.

Distractors: Rely on embedding space distance to separate department content: Embeddings cluster by semantic similarity, not organizational boundaries, so this won't reliably restrict cross-department content.; Add department names to document text so FM-generated responses reflect access constraints: Adding department names to content does not enforce retrieval-time filters; it’s unreliable for access control.; Configure per-user API keys for the vector store, without attaching metadata: API keys may control access to the store itself but do not filter search results based on document metadata at query time.

Misconception tags: Confusing semantic search with access control; Assuming embeddings enforce data boundary

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order006-metadata-design-filtering.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order006-metadata-design-filtering.md

### P1-AIP-D2-058

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-058 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.4: Design and implement vector store solutions. |
| `exam_skill` | Skill 1.4.2: Develop comprehensive metadata frameworks to improve search precision and context awareness for FM interactions (for example, by using S3 object metadata for document timestamps, custom attributes for authorship information, tagging systems for domain classification). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day02-order006 |
| `accelerated_day` | Day 2 |
| `topic` | Metadata design and filtering |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T051925Z-openai-gpt-4.1-day-02-order006.md item 2 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T051925Z |
| `raw_run_id` | order006 |

Stem:

An enterprise vector search system is returning outdated financial documents when answering current events questions. Metadata for document upload time is available but not being used. What is the first configuration step to improve result freshness?

Options:

1. Incorporate document upload timestamps in metadata filters during query
2. Increase embedding dimensionality to improve semantic matching
3. Retrain the FM with more recent data
4. Switch to a non-semantic keyword search approach

Correct answer: Incorporate document upload timestamps in metadata filters during query

Rationale: Filtering results by upload timestamp ensures only recent documents are retrieved, directly targeting freshness.

Distractors: Increase embedding dimensionality to improve semantic matching: Higher dimensionality doesn't address recency; old documents may still be top matches.; Retrain the FM with more recent data: Retraining the FM is unnecessary for retrieval freshness if up-to-date metadata is already available.; Switch to a non-semantic keyword search approach: Keyword search still doesn't resolve the core freshness issue if metadata isn’t leveraged.

Misconception tags: Forgetting metadata as filtering lever; Blaming embedding settings for freshness issues

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order006-metadata-design-filtering.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order006-metadata-design-filtering.md

### P1-AIP-D2-059

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-059 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.4: Design and implement vector store solutions. |
| `exam_skill` | Skill 1.4.2: Develop comprehensive metadata frameworks to improve search precision and context awareness for FM interactions (for example, by using S3 object metadata for document timestamps, custom attributes for authorship information, tagging systems for domain classification). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day02-order006 |
| `accelerated_day` | Day 2 |
| `topic` | Metadata design and filtering |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Conditional |
| `question_format` | multiple-response |
| `difficulty` | hard |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T051925Z-openai-gpt-4.1-day-02-order006.md item 3 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T051925Z |
| `raw_run_id` | order006 |

Stem:

A compliance auditor needs to ensure only documents with verified authorship and explicit review dates are eligible for FM-based retrieval on a healthcare knowledge platform. Which metadata strategies should you implement to support these requirements? (Select TWO.)

Options:

1. Add custom metadata fields for author ID and review date during ingestion
2. Filter retrieval queries based on completeness of author and review metadata
3. Use only semantic similarity for all FM-based document retrieval
4. Require all documents to include access control lists in text body
5. Rely on S3 default system metadata only

Correct answer: Add custom metadata fields for author ID and review date during ingestion; Filter retrieval queries based on completeness of author and review metadata

Rationale: Creating and leveraging custom metadata ensures only documents with required attributes are considered in retrieval, directly supporting the compliance need.

Distractors: Use only semantic similarity for all FM-based document retrieval: Semantic similarity ignores compliance requirements around authorship and review attributes.; Require all documents to include access control lists in text body: Storing ACLs in the content is not enforceable by vector search filters and conflates data and metadata.; Rely on S3 default system metadata only: Default system metadata is not sufficient to guarantee presence of compliance-specific fields.

Misconception tags: Confusing semantic similarity with compliance filtering; Treating metadata as optional decoration

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order006-metadata-design-filtering.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order006-metadata-design-filtering.md

### P1-AIP-D2-060

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-060 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.4: Design and implement vector store solutions. |
| `exam_skill` | Skill 1.4.2: Develop comprehensive metadata frameworks to improve search precision and context awareness for FM interactions (for example, by using S3 object metadata for document timestamps, custom attributes for authorship information, tagging systems for domain classification). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day02-order006 |
| `accelerated_day` | Day 2 |
| `topic` | Metadata design and filtering |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T051925Z-openai-gpt-4.1-day-02-order006.md item 4 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T051925Z |
| `raw_run_id` | order006 |

Stem:

A team is designing a RAG solution using Amazon OpenSearch with semantic search for technical document retrieval. They want search results to reflect not only topic relevance but document source reliability, such as whether the document came from an internal or external repository. How should they design their metadata framework?

Options:

1. Implement a custom metadata field for source type and include it in query-time filtering or ranking
2. Increase the context window size to capture both topic and reliability in FM input
3. Store source reliability information only in document body for the FM to process
4. Rely on OpenSearch built-in scoring to handle both relevance and reliability

Correct answer: Implement a custom metadata field for source type and include it in query-time filtering or ranking

Rationale: Adding and using a source-type metadata field allows searches or re-ranking to account for reliability during retrieval, not just in final generation.

Distractors: Increase the context window size to capture both topic and reliability in FM input: A larger context window does not address retrieval filtering or ranking by source reliability.; Store source reliability information only in document body for the FM to process: Document body content is not leveraged by retrieval filters or ranking; info may be ignored at search level.; Rely on OpenSearch built-in scoring to handle both relevance and reliability: Built-in scoring defaults to similarity; it doesn’t factor in external reliability attributes unless explicitly included.

Misconception tags: Treating document body as a substitute for metadata; Assuming relevance scoring includes metadata by default

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order006-metadata-design-filtering.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order006-metadata-design-filtering.md

### P1-AIP-D2-061

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-061 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.4: Design and implement vector store solutions. |
| `exam_skill` | Skill 1.4.2: Develop comprehensive metadata frameworks to improve search precision and context awareness for FM interactions (for example, by using S3 object metadata for document timestamps, custom attributes for authorship information, tagging systems for domain classification). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day02-order006 |
| `accelerated_day` | Day 2 |
| `topic` | Metadata design and filtering |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | explain |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T051925Z-openai-gpt-4.1-day-02-order006.md item 5 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T051925Z |
| `raw_run_id` | order006 |

Stem:

During a post-incident review, a team discovers that confidential engineering documents were surfaced in search results for sales team queries. Which gap in metadata design most likely caused this issue?

Options:

1. Missing or improperly used document access-level metadata
2. Overly broad semantic embeddings in the vector store
3. Document titles do not specify access group
4. Outdated document versions in the index

Correct answer: Missing or improperly used document access-level metadata

Rationale: Access-level metadata enables document filtering by audience, preventing cross-group document leakage in retrieval.

Distractors: Overly broad semantic embeddings in the vector store: Embeddings affect similarity but not retrieval filtering for audience or confidentiality.; Document titles do not specify access group: Titles alone are insufficient for reliable filtering and shouldn't be the sole method of access control.; Outdated document versions in the index: Outdated versions do not directly cause confidentiality breaches related to access metadata.

Misconception tags: Relying on content or titles for access control; Ignoring metadata-based audience filtering

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order006-metadata-design-filtering.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order006-metadata-design-filtering.md

### P1-AIP-D2-062

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-062 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.4: Design and implement vector store solutions. |
| `exam_skill` | Skill 1.4.2: Develop comprehensive metadata frameworks to improve search precision and context awareness for FM interactions (for example, by using S3 object metadata for document timestamps, custom attributes for authorship information, tagging systems for domain classification). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day02-order006 |
| `accelerated_day` | Day 2 |
| `topic` | Metadata design and filtering |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | explain |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T051925Z-openai-gpt-4.1-day-02-order006.md item 6 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T051925Z |
| `raw_run_id` | order006 |

Stem:

A vector store used for RAG has implemented a tagging system to classify documents by domain and sensitivity. How does this improve FM-based search precision?

Options:

1. It enables filtering and prioritization based on document characteristics during search
2. It increases the semantic similarity between query and document embeddings
3. It automatically summarizes documents before retrieval
4. It causes the FM to ignore untagged documents in all queries

Correct answer: It enables filtering and prioritization based on document characteristics during search

Rationale: Tags allow retrieval to filter or re-rank documents by relevant attributes, sharpening result precision for the query.

Distractors: It increases the semantic similarity between query and document embeddings: Tagging does not affect the embedding vectors; it’s used outside of similarity computation.; It automatically summarizes documents before retrieval: Summarization is a separate pipeline step and not a function of tagging.; It causes the FM to ignore untagged documents in all queries: Tagged retrieval can be bypassed if not enforced. FM processes retrieved content and isn't aware of tags unless retrieval uses them.

Misconception tags: Assuming tagging changes embeddings; Confusing search filtering with generation behavior

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order006-metadata-design-filtering.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order006-metadata-design-filtering.md

### P1-AIP-D2-063

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-063 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.4: Design and implement vector store solutions. |
| `exam_skill` | Skill 1.4.2: Develop comprehensive metadata frameworks to improve search precision and context awareness for FM interactions (for example, by using S3 object metadata for document timestamps, custom attributes for authorship information, tagging systems for domain classification). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day02-order006 |
| `accelerated_day` | Day 2 |
| `topic` | Metadata design and filtering |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T051925Z-openai-gpt-4.1-day-02-order006.md item 7 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T051925Z |
| `raw_run_id` | order006 |

Stem:

You are designing a knowledge base to serve a multilingual, multi-domain enterprise environment. Which metadata design approach best supports filtering for both language and business unit, while also supporting future scaling?

Options:

1. Develop custom metadata attributes for language and business unit and implement query-time filtering using these attributes
2. Use only file path structure to infer language and business unit
3. Rely solely on semantic embeddings, assuming they cluster by language and domain
4. Use a single free-text metadata field for all document attributes

Correct answer: Develop custom metadata attributes for language and business unit and implement query-time filtering using these attributes

Rationale: Custom, independent metadata attributes allow flexible, granular filtering and easier future expansion, compared to merging attributes or inferring from structure.

Distractors: Use only file path structure to infer language and business unit: Paths can be inconsistent and are not enforced through the retrieval system.; Rely solely on semantic embeddings, assuming they cluster by language and domain: Embeddings may not align cleanly on language or domain clusters, and do not enable explicit filtering.; Use a single free-text metadata field for all document attributes: Free-text is error-prone, non-standardized, and complex to filter at scale.

Misconception tags: Overloading file structure or free-text metadata; Assuming embeddings can replace explicit metadata filtering

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order006-metadata-design-filtering.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order006-metadata-design-filtering.md

### P1-AIP-D2-064

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-064 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.4: Design and implement vector store solutions. |
| `exam_skill` | Skill 1.4.2: Develop comprehensive metadata frameworks to improve search precision and context awareness for FM interactions (for example, by using S3 object metadata for document timestamps, custom attributes for authorship information, tagging systems for domain classification). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day02-order006 |
| `accelerated_day` | Day 2 |
| `topic` | Metadata design and filtering |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T051925Z-openai-gpt-4.1-day-02-order006.md item 8 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T051925Z |
| `raw_run_id` | order006 |

Stem:

In a content archiving scenario, you need to guarantee that only documents newer than the company's annual retention threshold are considered during FM-augmented search. What is the most robust metadata-driven approach?

Options:

1. Enforce retention threshold using document creation-date metadata and filter queries accordingly
2. Add retention information as a disclaimer in the document text
3. Increase the semantic similarity threshold during retrieval
4. Exclude older documents manually from the index every year

Correct answer: Enforce retention threshold using document creation-date metadata and filter queries accordingly

Rationale: Creation-date metadata enables precise filtering based on business policy, automating compliance with retention.

Distractors: Add retention information as a disclaimer in the document text: Disclaimers in text do not impact automated retrieval; metadata filtering is more robust.; Increase the semantic similarity threshold during retrieval: Similarity threshold impacts content relevance, not document age or retention policies.; Exclude older documents manually from the index every year: Manual deletions are error-prone and do not scale; metadata-driven filtering is best practice.

Misconception tags: Conflating document metadata with in-content notes; Assuming manual operations are preferred over automation

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order006-metadata-design-filtering.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order006-metadata-design-filtering.md

### P1-AIP-D2-065

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-065 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.4: Design and implement vector store solutions. |
| `exam_skill` | Skill 1.4.2: Develop comprehensive metadata frameworks to improve search precision and context awareness for FM interactions (for example, by using S3 object metadata for document timestamps, custom attributes for authorship information, tagging systems for domain classification). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day02-order006 |
| `accelerated_day` | Day 2 |
| `topic` | Metadata design and filtering |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T051925Z-openai-gpt-4.1-day-02-order006.md item 9 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T051925Z |
| `raw_run_id` | order006 |

Stem:

A retail company wants to surface the right user manual for each product in customer self-service FM search. Manuals are similar in content and often cover multiple product variants. What is the best use of metadata to enable precise result filtering?

Options:

1. Assign metadata tags for each product variant and filter search by requested variant
2. Embed the product code into the manual text and rely on semantic similarity for retrieval
3. Use only manual titles for product identification
4. Do not use document metadata; allow FM to synthesize the most relevant manual

Correct answer: Assign metadata tags for each product variant and filter search by requested variant

Rationale: Variant-level metadata enables queries to return precisely the right manual based on explicit filters, preventing ambiguity.

Distractors: Embed the product code into the manual text and rely on semantic similarity for retrieval: Embedding codes in text may not yield reliable variant selection, especially for overlapping content.; Use only manual titles for product identification: Titles can be ambiguous and not standardized, which weakens filtering.; Do not use document metadata; allow FM to synthesize the most relevant manual: Without explicit metadata, the FM may combine or misinterpret variants, risking wrong information.

Misconception tags: Assuming semantic similarity replaces metadata filtering; Trusting document titles for precision filtering

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order006-metadata-design-filtering.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order006-metadata-design-filtering.md

### P1-AIP-D2-066

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-066 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.4: Design and implement vector store solutions. |
| `exam_skill` | Skill 1.4.2: Develop comprehensive metadata frameworks to improve search precision and context awareness for FM interactions (for example, by using S3 object metadata for document timestamps, custom attributes for authorship information, tagging systems for domain classification). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day02-order006 |
| `accelerated_day` | Day 2 |
| `topic` | Metadata design and filtering |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Conditional |
| `question_format` | multiple-response |
| `difficulty` | hard |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T051925Z-openai-gpt-4.1-day-02-order006.md item 10 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T051925Z |
| `raw_run_id` | order006 |

Stem:

A financial services application supports semantic retrieval for policy documentation and requires real-time filtering by region and compliance version. Which metadata practices should be used to support this? (Select TWO.)

Options:

1. Define structured metadata fields for region and compliance version during ingestion
2. Implement query-time filtering based on metadata for both attributes
3. Use only unstructured summary fields for document description
4. Rely on document content to indicate region and version
5. Aggregate all compliance information into a single large metadata blob

Correct answer: Define structured metadata fields for region and compliance version during ingestion; Implement query-time filtering based on metadata for both attributes

Rationale: These practices enable precise and maintainable filtering, meeting business constraints for real-time, multi-attribute retrieval.

Distractors: Use only unstructured summary fields for document description: Unstructured fields make filtering unreliable at query time.; Rely on document content to indicate region and version: Parsing text for attributes is error-prone; metadata is preferred.; Aggregate all compliance information into a single large metadata blob: Large blobs are hard to parse and filter, making real-time selection inefficient.

Misconception tags: Assuming free-text metadata is sufficient; Overloading a single blob vs. structured attributes

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order006-metadata-design-filtering.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order006-metadata-design-filtering.md

### P1-AIP-D2-067

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-067 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.4: Design and implement vector store solutions. |
| `exam_skill` | Skill 1.4.2: Develop comprehensive metadata frameworks to improve search precision and context awareness for FM interactions (for example, by using S3 object metadata for document timestamps, custom attributes for authorship information, tagging systems for domain classification). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day02-order006 |
| `accelerated_day` | Day 2 |
| `topic` | Metadata design and filtering |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T051925Z-openai-gpt-4.1-day-02-order006.md item 11 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T051925Z |
| `raw_run_id` | order006 |

Stem:

An internal audit identifies that most retrieved documents for an FM-powered legal chatbot are outdated, but newer versions exist in the vector store. What metadata-related oversight is most likely at fault?

Options:

1. Retrieval queries do not filter or rank by document version or update date metadata
2. Semantic embeddings do not distinguish between old and new information
3. The FM model lacks knowledge of complex legal changes
4. Default sort order favors longer documents over current ones

Correct answer: Retrieval queries do not filter or rank by document version or update date metadata

Rationale: Filtering or ranking by version/update metadata helps ensure the newest, most relevant document is retrieved, not the oldest.

Distractors: Semantic embeddings do not distinguish between old and new information: While embeddings reflect content, they do not encode recency unless filtered by metadata.; The FM model lacks knowledge of complex legal changes: The FM can only generate from retrieved input; retrieval filtering is the main control.; Default sort order favors longer documents over current ones: Length-based sorting does not address freshness control without relying on version/update metadata.

Misconception tags: Blaming embedding or FM for retrieval gaps; Overlooking metadata in version control

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order006-metadata-design-filtering.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order006-metadata-design-filtering.md

### P1-AIP-D2-068

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-068 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.4: Design and implement vector store solutions. |
| `exam_skill` | Skill 1.4.2: Develop comprehensive metadata frameworks to improve search precision and context awareness for FM interactions (for example, by using S3 object metadata for document timestamps, custom attributes for authorship information, tagging systems for domain classification). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day02-order006 |
| `accelerated_day` | Day 2 |
| `topic` | Metadata design and filtering |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Conditional |
| `question_format` | multiple-response |
| `difficulty` | hard |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T051925Z-openai-gpt-4.1-day-02-order006.md item 12 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T051925Z |
| `raw_run_id` | order006 |

Stem:

Your security team requires that FM-augmented retrieval systems do not leak customer-project documents during partner-facing search sessions. Which metadata-driven solutions should you apply to prevent this risk? (Select TWO.)

Options:

1. Tag all customer-project documents with a sensitivity level at ingestion
2. Enforce metadata-based filtering by sensitivity when partners search
3. Rely solely on user authentication for access control
4. Store customer information only in raw document text for privacy
5. Combine customer and partner documents in the same index without attribute distinction

Correct answer: Tag all customer-project documents with a sensitivity level at ingestion; Enforce metadata-based filtering by sensitivity when partners search

Rationale: These approaches ensure retrieval is restricted to appropriate sensitivity by tagging content and enforcing attribute-based filtering.

Distractors: Rely solely on user authentication for access control: Auth controls ingress to the system, but metadata filtering controls retrieval content.; Store customer information only in raw document text for privacy: Privacy is not enforced if content is in text and not filtered at the metadata layer.; Combine customer and partner documents in the same index without attribute distinction: Mixing data without separation or filtering risks accidental leakage.

Misconception tags: Confusing authentication with retrieval filtering; Ignoring attribute-based isolation in indices

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order006-metadata-design-filtering.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order006-metadata-design-filtering.md

### P1-AIP-D2-069

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-069 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.4: Design and implement vector store solutions. |
| `exam_skill` | Skill 1.4.1: Create advanced vector database architectures specifically for FM augmentation to enable efficient semantic retrieval beyond traditional search capabilities (for example, by using Amazon Bedrock Knowledge Bases for hierarchical organization, Amazon OpenSearch Service with the Neural plugin for Amazon Bedrock integration for topic-based segmentation, Amazon RDS with Amazon S3 document repositories, Amazon DynamoDB with vector databases for metadata and embeddings). |
| `secondary_exam_skills` | Skill 1.5.3: Deploy and configure vector search solutions to enable semantic search capabilities for FM augmentation (for example, by using OpenSearch Service with vector search capabilities, Amazon Aurora with the pgvector extension, Amazon Bedrock Knowledge Bases with managed vector store functionality). |
| `learning_unit` | Day02-order007 |
| `accelerated_day` | Day 2 |
| `topic` | Vector-store technologies and architecture |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Conceptual; Conditional; Strategic; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T052016Z-openai-gpt-4.1-day-02-order007.md item 1 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T052016Z |
| `raw_run_id` | order007 |

Stem:

A financial analytics team migrates from a traditional ML-driven search engine to a new semantic search platform for regulatory document retrieval. They want strong semantic similarity, must support hierarchical search (by regulation region and topic), and are using Amazon Bedrock models integrated with a vector database. Which architecture best covers these requirements and minimizes custom code?

Options:

1. Amazon Bedrock Knowledge Bases with hierarchical metadata and managed vector store
2. Amazon DynamoDB with custom embedding storage and regional region-index mapping
3. Amazon OpenSearch Service with Neural plugin and custom logic for region/topic filters
4. Amazon RDS with pgvector extension, S3 for storage, and Lambda ETL orchestration

Correct answer: Amazon Bedrock Knowledge Bases with hierarchical metadata and managed vector store

Rationale: Bedrock Knowledge Bases natively support hierarchical metadata for organization/region/topic and embed a managed vector store for semantic retrieval, requiring minimal custom code.

Distractors: Amazon DynamoDB with custom embedding storage and regional region-index mapping: Requires building embedding logic and search orchestration manually, and lacks hierarchical or semantic search features natively.; Amazon OpenSearch Service with Neural plugin and custom logic for region/topic filters: The Neural plugin provides semantic search, but adding hierarchical search for regulations by region and topic would need custom filters and coding.; Amazon RDS with pgvector extension, S3 for storage, and Lambda ETL orchestration: Combining RDS and S3 creates complexity in managing embeddings, metadata, and hierarchy; also, requires ETL ETL logic and manual orchestration.

Misconception tags: Confusing managed feature set with what must be built; Assuming all vector databases handle hierarchy

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-02-data-embeddings-vector-stores-rag.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order007-vector-store-architecture.md

### P1-AIP-D2-070

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-070 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.4: Design and implement vector store solutions. |
| `exam_skill` | Skill 1.4.1: Create advanced vector database architectures specifically for FM augmentation to enable efficient semantic retrieval beyond traditional search capabilities (for example, by using Amazon Bedrock Knowledge Bases for hierarchical organization, Amazon OpenSearch Service with the Neural plugin for Amazon Bedrock integration for topic-based segmentation, Amazon RDS with Amazon S3 document repositories, Amazon DynamoDB with vector databases for metadata and embeddings). |
| `secondary_exam_skills` | Skill 1.5.3: Deploy and configure vector search solutions to enable semantic search capabilities for FM augmentation (for example, by using OpenSearch Service with vector search capabilities, Amazon Aurora with the pgvector extension, Amazon Bedrock Knowledge Bases with managed vector store functionality). |
| `learning_unit` | Day02-order007 |
| `accelerated_day` | Day 2 |
| `topic` | Vector-store technologies and architecture |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Conceptual; Conditional; Strategic; Embedded |
| `question_format` | multiple-response |
| `difficulty` | exam-plus |
| `cognitive_demand` | judge |
| `estimated_time_seconds` | 180 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T052016Z-openai-gpt-4.1-day-02-order007.md item 2 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T052016Z |
| `raw_run_id` | order007 |

Stem:

An e-commerce company wants to implement a product recommendation engine using semantic search over product descriptions, reviews, and metadata. They want to maintain both semantic and keyword-based retrieval in a single solution with native AWS integration. Which technologies could satisfy these requirements? (Select TWO.)

Options:

1. Amazon OpenSearch Service with Neural plugin
2. Amazon RDS with pgvector extension
3. Amazon Bedrock Knowledge Bases
4. Amazon DynamoDB with custom vector extension
5. Amazon MemoryDB for Redis

Correct answer: Amazon OpenSearch Service with Neural plugin; Amazon Bedrock Knowledge Bases

Rationale: OpenSearch with Neural plugin supports both vector (semantic) and keyword (traditional) retrieval in one solution. Bedrock Knowledge Bases can manage semantic retrieval and typically connect to underlying stores that can perform keyword retrieval as well.

Distractors: Amazon RDS with pgvector extension: Supports semantic search but not traditional full-text keyword search or document field-based filtering natively.; Amazon DynamoDB with custom vector extension: Would require extensive custom development for both vector and text search, lacking built-in integration.; Amazon MemoryDB for Redis: Not purpose-built for vector similarity, full-text, or semantic retrieval at a scale required for product recommendations.

Misconception tags: Assuming pgvector or Redis natively blend keyword and vector search; Confusing managed search versus custom build

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-02-data-embeddings-vector-stores-rag.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order007-vector-store-architecture.md

### P1-AIP-D2-071

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-071 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.4: Design and implement vector store solutions. |
| `exam_skill` | Skill 1.4.1: Create advanced vector database architectures specifically for FM augmentation to enable efficient semantic retrieval beyond traditional search capabilities (for example, by using Amazon Bedrock Knowledge Bases for hierarchical organization, Amazon OpenSearch Service with the Neural plugin for Amazon Bedrock integration for topic-based segmentation, Amazon RDS with Amazon S3 document repositories, Amazon DynamoDB with vector databases for metadata and embeddings). |
| `secondary_exam_skills` | Skill 1.5.3: Deploy and configure vector search solutions to enable semantic search capabilities for FM augmentation (for example, by using OpenSearch Service with vector search capabilities, Amazon Aurora with the pgvector extension, Amazon Bedrock Knowledge Bases with managed vector store functionality). |
| `learning_unit` | Day02-order007 |
| `accelerated_day` | Day 2 |
| `topic` | Vector-store technologies and architecture |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Conceptual; Conditional; Strategic; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T052016Z-openai-gpt-4.1-day-02-order007.md item 3 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T052016Z |
| `raw_run_id` | order007 |

Stem:

A SaaS platform uses Amazon OpenSearch Service with the Neural plugin as its vector database for customer query semantic search. Retrieval accuracy sharply declines after switching to a third-party embedding model with different dimensionality. What is the most likely architectural issue?

Options:

1. The vector store's index was not rebuilt to match the new embedding dimensionality.
2. Bedrock Knowledge Bases were not reconfigured to support external embedding sources.
3. OpenSearch snapshot restore was not completed after new deployment.
4. IAM policies for customer data replication were not updated appropriately.

Correct answer: The vector store's index was not rebuilt to match the new embedding dimensionality.

Rationale: Vector database indexes must be rebuilt or adjusted to match the dimensionality of the vectors in use—otherwise, similarity search accuracy is degraded or fails.

Distractors: Bedrock Knowledge Bases were not reconfigured to support external embedding sources: Irrelevant—this is about OpenSearch index compatibility, not Knowledge Base integration.; OpenSearch snapshot restore was not completed after new deployment: Restoring a snapshot is not directly related to mismatched embedding dimensions causing accuracy problems.; IAM policies for customer data replication were not updated appropriately: IAM policies affect access and data movement, not vector space compatibility or retrieval accuracy.

Misconception tags: Confusing embedding model compatibility with system configuration; Blaming unrelated integration or access controls

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order007-vector-store-architecture.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day-02-answer-guidance.md

### P1-AIP-D2-072

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-072 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.4: Design and implement vector store solutions. |
| `exam_skill` | Skill 1.4.1: Create advanced vector database architectures specifically for FM augmentation to enable efficient semantic retrieval beyond traditional search capabilities (for example, by using Amazon Bedrock Knowledge Bases for hierarchical organization, Amazon OpenSearch Service with the Neural plugin for Amazon Bedrock integration for topic-based segmentation, Amazon RDS with Amazon S3 document repositories, Amazon DynamoDB with vector databases for metadata and embeddings). |
| `secondary_exam_skills` | Skill 1.5.3: Deploy and configure vector search solutions to enable semantic search capabilities for FM augmentation (for example, by using OpenSearch Service with vector search capabilities, Amazon Aurora with the pgvector extension, Amazon Bedrock Knowledge Bases with managed vector store functionality). |
| `learning_unit` | Day02-order007 |
| `accelerated_day` | Day 2 |
| `topic` | Vector-store technologies and architecture |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Conceptual; Conditional; Strategic; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | compare |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T052016Z-openai-gpt-4.1-day-02-order007.md item 4 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T052016Z |
| `raw_run_id` | order007 |

Stem:

A team is deciding between Amazon DynamoDB with a custom Lambda-based embedding pipeline and Amazon OpenSearch Service with the Neural plugin for semantic search. Their data is updated in real-time, search latency is critical, and custom ranking is required on certain fields. Which solution is more appropriate and why?

Options:

1. Amazon OpenSearch Service with Neural plugin, because it supports real-time ingestion and native vector + filter-based queries
2. Amazon DynamoDB with Lambda, because it scales better for real-time updates and natively supports custom Lambda ranking
3. Amazon DynamoDB, because its consistency and key/value retrievals outperform OpenSearch for complex ranking
4. Amazon OpenSearch Service with Neural plugin, because it can trigger Lambdas after every vector insert for custom ranking

Correct answer: Amazon OpenSearch Service with Neural plugin, because it supports real-time ingestion and native vector + filter-based queries

Rationale: OpenSearch with Neural plugin is optimized for semantic search with fast ingestion, native filtered queries, and support for ranking, making it ideal for latency-sensitive semantic retrieval.

Distractors: Amazon DynamoDB with Lambda, because it scales better for real-time updates and natively supports custom Lambda ranking: While DynamoDB is fast for transactional updates, adding semantic search and custom ranking would require significant workaround logic and orchestration.; Amazon DynamoDB, because its consistency and key/value retrievals outperform OpenSearch for complex ranking: DynamoDB excels at exact-match retrieval and transactional workloads, not in vector or custom ranked semantic search.; Amazon OpenSearch Service with Neural plugin, because it can trigger Lambdas after every vector insert for custom ranking: OpenSearch can trigger notifications, but custom ranking is handled in the search query pipeline, not by invoking Lambdas after every insert.

Misconception tags: Equating DynamoDB real-time scale with suitability for semantic query/ranking; Misunderstanding custom ranking workflow

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order007-vector-store-architecture.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day-02-answer-guidance.md

### P1-AIP-D2-073

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-073 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.4: Design and implement vector store solutions. |
| `exam_skill` | Skill 1.4.1: Create advanced vector database architectures specifically for FM augmentation to enable efficient semantic retrieval beyond traditional search capabilities (for example, by using Amazon Bedrock Knowledge Bases for hierarchical organization, Amazon OpenSearch Service with the Neural plugin for Amazon Bedrock integration for topic-based segmentation, Amazon RDS with Amazon S3 document repositories, Amazon DynamoDB with vector databases for metadata and embeddings). |
| `secondary_exam_skills` | Skill 1.5.3: Deploy and configure vector search solutions to enable semantic search capabilities for FM augmentation (for example, by using OpenSearch Service with vector search capabilities, Amazon Aurora with the pgvector extension, Amazon Bedrock Knowledge Bases with managed vector store functionality). |
| `learning_unit` | Day02-order007 |
| `accelerated_day` | Day 2 |
| `topic` | Vector-store technologies and architecture |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Conceptual; Conditional; Strategic; Embedded |
| `question_format` | multiple-response |
| `difficulty` | hard |
| `cognitive_demand` | integrate |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T052016Z-openai-gpt-4.1-day-02-order007.md item 5 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T052016Z |
| `raw_run_id` | order007 |

Stem:

Your legal research application must provide semantic retrieval over several million legal documents, support strict access controls by user role, and integrate with future Amazon Bedrock FM-based Q&A workflows. Which architectural elements are most essential in your vector-store solution? (Select TWO.)

Options:

1. A vector database with support for role-based metadata filtering
2. Managed service for vector and metadata storage, such as Bedrock Knowledge Bases
3. Direct mapping between embedding ID and user account in Amazon DynamoDB only
4. Storing embeddings as S3 object metadata without additional access controls
5. Automatic Lambda triggers on every query for security enforcement

Correct answer: A vector database with support for role-based metadata filtering; Managed service for vector and metadata storage, such as Bedrock Knowledge Bases

Rationale: Role-based filtering and managed metadata ensure compliance with access controls and scalability for large legal data sets. Bedrock Knowledge Bases streamline future FM integration and security.

Distractors: Direct mapping between embedding ID and user account in Amazon DynamoDB only: DynamoDB alone lacks native vector search and robust filtering—it can't support combined semantic retrieval and access control without heavy custom code.; Storing embeddings as S3 object metadata without additional access controls: S3 metadata is not a vector database and doesn't enforce nuanced user-based access at query time.; Automatic Lambda triggers on every query for security enforcement: Invoking Lambda per-query is inefficient compared to filtering at the vector database layer.

Misconception tags: Treating object metadata as a security solution; Assuming DynamoDB can replace a vector store

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-02-data-embeddings-vector-stores-rag.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order007-vector-store-architecture.md

### P1-AIP-D2-074

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-074 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.4: Design and implement vector store solutions. |
| `exam_skill` | Skill 1.4.1: Create advanced vector database architectures specifically for FM augmentation to enable efficient semantic retrieval beyond traditional search capabilities (for example, by using Amazon Bedrock Knowledge Bases for hierarchical organization, Amazon OpenSearch Service with the Neural plugin for Amazon Bedrock integration for topic-based segmentation, Amazon RDS with Amazon S3 document repositories, Amazon DynamoDB with vector databases for metadata and embeddings). |
| `secondary_exam_skills` | Skill 1.5.3: Deploy and configure vector search solutions to enable semantic search capabilities for FM augmentation (for example, by using OpenSearch Service with vector search capabilities, Amazon Aurora with the pgvector extension, Amazon Bedrock Knowledge Bases with managed vector store functionality). |
| `learning_unit` | Day02-order007 |
| `accelerated_day` | Day 2 |
| `topic` | Vector-store technologies and architecture |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Conceptual; Conditional; Strategic; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T052016Z-openai-gpt-4.1-day-02-order007.md item 6 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T052016Z |
| `raw_run_id` | order007 |

Stem:

A startup uses Amazon Aurora with pgvector extension for a small RAG-based chatbot. As user volume and complexity grow, they require managed scaling, semantic search, and integration with other AWS analytics services. What would be the best path forward?

Options:

1. Move to Amazon OpenSearch Service with Neural plugin to gain managed vector search scaling and analytics integration
2. Add Amazon Bedrock Knowledge Bases while leaving data in Aurora to leverage Bedrock’s managed vector interface
3. Implement a custom sharding layer on Aurora with pgvector for scaling
4. Use Amazon S3 with object-level metadata for embeddings

Correct answer: Move to Amazon OpenSearch Service with Neural plugin to gain managed vector search scaling and analytics integration

Rationale: OpenSearch Service provides scalable managed vector database operations, advanced semantic search, and integrates with AWS analytics services.

Distractors: Add Amazon Bedrock Knowledge Bases while leaving data in Aurora to leverage Bedrock’s managed vector interface: Bedrock Knowledge Bases may require data to be stored in a supported vector store for performance and integration, not simply pointing at Aurora.; Implement a custom sharding layer on Aurora with pgvector for scaling: Adds complexity and maintenance overhead, not a managed scaling path.; Use Amazon S3 with object-level metadata for embeddings: S3 cannot provide vector similarity search functionality.

Misconception tags: Assuming pgvector or S3 can scale like managed vector databases; Misunderstanding Bedrock Knowledge Base requirements

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order007-vector-store-architecture.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day-02-answer-guidance.md

### P1-AIP-D2-075

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-075 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.4: Design and implement vector store solutions. |
| `exam_skill` | Skill 1.4.1: Create advanced vector database architectures specifically for FM augmentation to enable efficient semantic retrieval beyond traditional search capabilities (for example, by using Amazon Bedrock Knowledge Bases for hierarchical organization, Amazon OpenSearch Service with the Neural plugin for Amazon Bedrock integration for topic-based segmentation, Amazon RDS with Amazon S3 document repositories, Amazon DynamoDB with vector databases for metadata and embeddings). |
| `secondary_exam_skills` | Skill 1.5.3: Deploy and configure vector search solutions to enable semantic search capabilities for FM augmentation (for example, by using OpenSearch Service with vector search capabilities, Amazon Aurora with the pgvector extension, Amazon Bedrock Knowledge Bases with managed vector store functionality). |
| `learning_unit` | Day02-order007 |
| `accelerated_day` | Day 2 |
| `topic` | Vector-store technologies and architecture |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Conceptual; Conditional; Strategic; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | judge |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T052016Z-openai-gpt-4.1-day-02-order007.md item 7 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T052016Z |
| `raw_run_id` | order007 |

Stem:

A media analytics company wants to provide semantic search for both text and image metadata at scale. Which vector-store integration approach should they prefer to maximize native AWS service compatibility and scalability with minimal custom orchestration?

Options:

1. Amazon Bedrock Knowledge Bases with managed vector store
2. Amazon DynamoDB with Lambda-based embedding processing
3. Amazon RDS with pgvector plus ETL jobs for indexing
4. OpenSearch deployed on EC2 with manual vector index management

Correct answer: Amazon Bedrock Knowledge Bases with managed vector store

Rationale: Bedrock Knowledge Bases provide native AWS service compatibility for scalable semantic search and can manage both text and, in many scenarios, image metadata embeddings with little custom orchestration.

Distractors: Amazon DynamoDB with Lambda-based embedding processing: Requires heavy lifting for vector similarity search and complex orchestration between DynamoDB, Lambda, and embedding models.; Amazon RDS with pgvector plus ETL jobs for indexing: Adds operational burden and does not natively scale vector search as required.; OpenSearch deployed on EC2 with manual vector index management: Manual setup loses managed service benefits and scalability, increasing risk of operational issues.

Misconception tags: Assuming DynamoDB or EC2 OpenSearch matches AWS managed solution benefits; Overvaluing DIY index management

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order007-vector-store-architecture.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day-02-answer-guidance.md

### P1-AIP-D2-076

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-076 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.4: Design and implement vector store solutions. |
| `exam_skill` | Skill 1.4.1: Create advanced vector database architectures specifically for FM augmentation to enable efficient semantic retrieval beyond traditional search capabilities (for example, by using Amazon Bedrock Knowledge Bases for hierarchical organization, Amazon OpenSearch Service with the Neural plugin for Amazon Bedrock integration for topic-based segmentation, Amazon RDS with Amazon S3 document repositories, Amazon DynamoDB with vector databases for metadata and embeddings). |
| `secondary_exam_skills` | Skill 1.5.3: Deploy and configure vector search solutions to enable semantic search capabilities for FM augmentation (for example, by using OpenSearch Service with vector search capabilities, Amazon Aurora with the pgvector extension, Amazon Bedrock Knowledge Bases with managed vector store functionality). |
| `learning_unit` | Day02-order007 |
| `accelerated_day` | Day 2 |
| `topic` | Vector-store technologies and architecture |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Conceptual; Conditional; Strategic; Embedded |
| `question_format` | multiple-response |
| `difficulty` | exam-plus |
| `cognitive_demand` | optimize |
| `estimated_time_seconds` | 180 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T052016Z-openai-gpt-4.1-day-02-order007.md item 8 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T052016Z |
| `raw_run_id` | order007 |

Stem:

Your content moderation platform must store billions of embeddings for real-time moderation and comply with strict access policies. Which strategies will help build a maintainable and scalable vector store architecture on AWS? (Select TWO.)

Options:

1. Leverage Amazon OpenSearch Service with Neural plugin for scalable, managed vector indexing
2. Implement role-based metadata filtering in the vector database layer
3. Store all embeddings as JSON blobs in S3 and run Athena queries for semantic retrieval
4. Keep user access checks in a separate Lambda unrelated to the vector store
5. Split embeddings into independent DynamoDB tables by user region

Correct answer: Leverage Amazon OpenSearch Service with Neural plugin for scalable, managed vector indexing; Implement role-based metadata filtering in the vector database layer

Rationale: OpenSearch with Neural plugin provides managed scalability for indexing huge numbers of vectors and supports fast queries. Implementing role-based metadata filtering at the vector database allows for secure, efficient access control.

Distractors: Store all embeddings as JSON blobs in S3 and run Athena queries for semantic retrieval: Athena is not intended or performant for vector similarity search; S3 is not a vector database.; Keep user access checks in a separate Lambda unrelated to the vector store: Access checks outside the vector database risk policy drift and inefficiency.; Split embeddings into independent DynamoDB tables by user region: Complicates scaling and search; DynamoDB is not optimized for semantic vector search.

Misconception tags: Using S3 or Athena for vector search; Outsourcing access control from vector database layer

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order007-vector-store-architecture.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day-02-answer-guidance.md

### P1-AIP-D2-077

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-077 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.4: Design and implement vector store solutions. |
| `exam_skill` | Skill 1.4.1: Create advanced vector database architectures specifically for FM augmentation to enable efficient semantic retrieval beyond traditional search capabilities (for example, by using Amazon Bedrock Knowledge Bases for hierarchical organization, Amazon OpenSearch Service with the Neural plugin for Amazon Bedrock integration for topic-based segmentation, Amazon RDS with Amazon S3 document repositories, Amazon DynamoDB with vector databases for metadata and embeddings). |
| `secondary_exam_skills` | Skill 1.5.3: Deploy and configure vector search solutions to enable semantic search capabilities for FM augmentation (for example, by using OpenSearch Service with vector search capabilities, Amazon Aurora with the pgvector extension, Amazon Bedrock Knowledge Bases with managed vector store functionality). |
| `learning_unit` | Day02-order007 |
| `accelerated_day` | Day 2 |
| `topic` | Vector-store technologies and architecture |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Conceptual; Conditional; Strategic; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | explain |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T052016Z-openai-gpt-4.1-day-02-order007.md item 9 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T052016Z |
| `raw_run_id` | order007 |

Stem:

A global help desk chatbot team is evaluating whether to switch from a self-managed OpenSearch cluster (deployed on EC2) to Amazon OpenSearch Service with the Neural plugin for their semantic vector store. Which is the strongest AWS-native rationale to make the switch?

Options:

1. Amazon OpenSearch Service provides managed scaling, built-in Neural plugin updates, and tight AWS integration.
2. A self-managed cluster offers improved AWS IAM integration and predictable maintenance costs.
3. Amazon OpenSearch Service Neural plugin allows deployment in on-premises environments.
4. Amazon OpenSearch Service with Neural plugin automatically manages hybrid batch/streaming ingestion out of the box.

Correct answer: Amazon OpenSearch Service provides managed scaling, built-in Neural plugin updates, and tight AWS integration.

Rationale: The managed service removes the burden of scaling, patching, and plugin management, while integrating well with AWS security and monitoring.

Distractors: A self-managed cluster offers improved AWS IAM integration and predictable maintenance costs.: The opposite is true—the managed service gives stronger IAM and integration with AWS services.; Amazon OpenSearch Service Neural plugin allows deployment in on-premises environments.: OpenSearch Service is AWS-managed and not for on-prem deployment.; Amazon OpenSearch Service with Neural plugin automatically manages hybrid batch/streaming ingestion out of the box.: You still need to design ingestion pipelines, but gain managed scaling and plugin management.

Misconception tags: Confusing managed versus self-managed plugin and scaling; Misunderstanding limits of OpenSearch Service deployment

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-02-data-embeddings-vector-stores-rag.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order007-vector-store-architecture.md

### P1-AIP-D2-078

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-078 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.4: Design and implement vector store solutions. |
| `exam_skill` | Skill 1.4.1: Create advanced vector database architectures specifically for FM augmentation to enable efficient semantic retrieval beyond traditional search capabilities (for example, by using Amazon Bedrock Knowledge Bases for hierarchical organization, Amazon OpenSearch Service with the Neural plugin for Amazon Bedrock integration for topic-based segmentation, Amazon RDS with Amazon S3 document repositories, Amazon DynamoDB with vector databases for metadata and embeddings). |
| `secondary_exam_skills` | Skill 1.5.3: Deploy and configure vector search solutions to enable semantic search capabilities for FM augmentation (for example, by using OpenSearch Service with vector search capabilities, Amazon Aurora with the pgvector extension, Amazon Bedrock Knowledge Bases with managed vector store functionality). |
| `learning_unit` | Day02-order007 |
| `accelerated_day` | Day 2 |
| `topic` | Vector-store technologies and architecture |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Conceptual; Conditional; Strategic; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | judge |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T052016Z-openai-gpt-4.1-day-02-order007.md item 10 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T052016Z |
| `raw_run_id` | order007 |

Stem:

A pharmaceutical research group is designing a knowledge base that must combine semantic search over documents with strict audit logging for compliance and support future extension to RAG-based workflows. Which AWS architecture balances regulatory requirements and FM scalability?

Options:

1. Implement Amazon Bedrock Knowledge Bases with managed vector store and enable CloudTrail for audit logging
2. Store all embeddings and logs as S3 objects with DynamoDB providing pointer mapping
3. Use Amazon OpenSearch Service with Neural plugin plus Glue Data Catalog for compliance
4. Deploy Amazon Aurora with pgvector for documents and Lambda for logging access events

Correct answer: Implement Amazon Bedrock Knowledge Bases with managed vector store and enable CloudTrail for audit logging

Rationale: Bedrock Knowledge Bases support scalable semantic search and integrate with AWS-native audit controls such as CloudTrail, meeting compliance needs and facilitating future RAG development.

Distractors: Store all embeddings and logs as S3 objects with DynamoDB providing pointer mapping: This design has limited ability for semantic search and centralized audit without intensive custom code.; Use Amazon OpenSearch Service with Neural plugin plus Glue Data Catalog for compliance: Glue Data Catalog alone doesn't handle access audit; OpenSearch provides search but not complete compliance features natively.; Deploy Amazon Aurora with pgvector for documents and Lambda for logging access events: Aurora + Lambda logging is ad hoc and does not provide centralized AWS auditing, nor is it optimized for FM scaling.

Misconception tags: Treating pointer mapping or Glue Data Catalog as full compliance systems; Ignoring managed audit integration

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-02-data-embeddings-vector-stores-rag.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order007-vector-store-architecture.md

### P1-AIP-D2-079

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-079 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.4: Design and implement vector store solutions. |
| `exam_skill` | Skill 1.4.1: Create advanced vector database architectures specifically for FM augmentation to enable efficient semantic retrieval beyond traditional search capabilities (for example, by using Amazon Bedrock Knowledge Bases for hierarchical organization, Amazon OpenSearch Service with the Neural plugin for Amazon Bedrock integration for topic-based segmentation, Amazon RDS with Amazon S3 document repositories, Amazon DynamoDB with vector databases for metadata and embeddings). |
| `secondary_exam_skills` | Skill 1.5.3: Deploy and configure vector search solutions to enable semantic search capabilities for FM augmentation (for example, by using OpenSearch Service with vector search capabilities, Amazon Aurora with the pgvector extension, Amazon Bedrock Knowledge Bases with managed vector store functionality). |
| `learning_unit` | Day02-order007 |
| `accelerated_day` | Day 2 |
| `topic` | Vector-store technologies and architecture |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Conceptual; Conditional; Strategic; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | exam-plus |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 180 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T052016Z-openai-gpt-4.1-day-02-order007.md item 12 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T052016Z |
| `raw_run_id` | order007 |

Stem:

A global knowledge repository team is configuring its Bedrock Knowledge Base to segment vector search by domain (product, HR, legal) and restrict content by region (EU, APAC, US). What is the most effective approach for achieving this using AWS-native design patterns?

Options:

1. Apply domain and region metadata as hierarchical attributes within Knowledge Base documents and use these for filtered vector queries
2. Maintain separate vector indexes for each domain-region combination, managed outside of Bedrock Knowledge Base
3. Write all domain and region info into S3 object keys, and point the Knowledge Base at matching S3 prefixes
4. Add domain and region fields to embedding vectors themselves, so the similarity search accounts for both

Correct answer: Apply domain and region metadata as hierarchical attributes within Knowledge Base documents and use these for filtered vector queries

Rationale: Hierarchical attributes and metadata filtering on the vector store provide efficient, scalable, and AWS-supported mechanisms for restricted and segmented retrieval.

Distractors: Maintain separate vector indexes for each domain-region combination, managed outside of Bedrock Knowledge Base: This increases operational complexity and loses the benefit of Bedrock's managed filtering capabilities.; Write all domain and region info into S3 object keys, and point the Knowledge Base at matching S3 prefixes: S3 prefixes are not a fine-grained filter mechanism for semantic vector search inside Bedrock Knowledge Bases.; Add domain and region fields to embedding vectors themselves, so the similarity search accounts for both: Embedding the filters in vector values breaks clean metadata filters and pollutes semantic similarity metrics.

Misconception tags: Confusing S3 prefixes or vector fields with robust metadata filtering; Thinking manual index management is preferred

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order007-vector-store-architecture.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day-02-answer-guidance.md

### P1-AIP-D2-080

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-080 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.4: Design and implement vector store solutions. |
| `exam_skill` | Skill 1.4.3: Implement high-performance vector database architectures to optimize semantic search performance at scale for FM retrieval (for example, by using OpenSearch sharding strategies, multi-index approaches for specialized domains, hierarchical indexing techniques). |
| `secondary_exam_skills` | Skill 1.4.5: Design and deploy data maintenance systems to ensure that vector stores contain current and accurate information for FM augmentation (for example, by using incremental update mechanisms, real-time change detection systems, automated synchronization workflows, scheduled refresh pipelines). |
| `learning_unit` | Day02-order008 |
| `accelerated_day` | Day 2 |
| `topic` | Vector indexing, sharding, scaling, and performance |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Conceptual; Procedural; Causal; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T052105Z-openai-gpt-4.1-day-02-order008.md item 1 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T052105Z |
| `raw_run_id` | order008 |

Stem:

A distributed semantic search application using Amazon OpenSearch Service experiences high query latency as data volume increases. The development team has noticed that only one shard per index is being utilized for queries. What is the most likely root cause?

Options:

1. All indices have too few shards, causing hot spot usage.
2. The embedding vectors are imbalanced across shards.
3. Only the primary shard is being used due to single-shard configuration.
4. Index replicas are overloaded, affecting search performance.

Correct answer: Only the primary shard is being used due to single-shard configuration.

Rationale: Using a single shard per index means all queries are routed to just one primary shard, which becomes a bottleneck as data scales.

Distractors: All indices have too few shards, causing hot spot usage.: While too few shards can create bottlenecks, the key issue in the scenario is routing all searches to the primary shard due to configuration, not uneven distribution.; The embedding vectors are imbalanced across shards.: Imbalanced distribution affects performance, but in the scenario, there is only a single shard, so no imbalance can exist across multiple shards.; Index replicas are overloaded, affecting search performance.: Replicas are for high availability and failover. Search queries route to primaries; replica overload would affect redundancy, not primary query latency.

Misconception tags: Shard configuration vs. data imbalance; Assuming replicas handle search by default

Source trace:

docs.aws.amazon.com/opensearch-service/latest/developerguide/index-management.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order008-vector-indexing-scaling-performance.md

### P1-AIP-D2-081

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-081 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.4: Design and implement vector store solutions. |
| `exam_skill` | Skill 1.4.3: Implement high-performance vector database architectures to optimize semantic search performance at scale for FM retrieval (for example, by using OpenSearch sharding strategies, multi-index approaches for specialized domains, hierarchical indexing techniques). |
| `secondary_exam_skills` | Skill 1.4.5: Design and deploy data maintenance systems to ensure that vector stores contain current and accurate information for FM augmentation (for example, by using incremental update mechanisms, real-time change detection systems, automated synchronization workflows, scheduled refresh pipelines). |
| `learning_unit` | Day02-order008 |
| `accelerated_day` | Day 2 |
| `topic` | Vector indexing, sharding, scaling, and performance |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Conceptual; Procedural; Causal; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T052105Z-openai-gpt-4.1-day-02-order008.md item 2 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T052105Z |
| `raw_run_id` | order008 |

Stem:

Your team is designing an OpenSearch-based vector store to serve high-throughput semantic retrieval for multiple product categories. Each category’s documents must be isolated with minimal cross-category query interference, while supporting rapid scaling and updates. Which architecture choice would most directly address these requirements?

Options:

1. Single index with multiple shards and a category_id field for filtering
2. Multi-index architecture, with a separate index for each product category
3. Hierarchical chunking inside a single global index
4. Single index with aggressive replica scaling

Correct answer: Multi-index architecture, with a separate index for each product category

Rationale: This approach provides true isolation and scaling for each category, preventing query interference and allowing per-category optimization and updates.

Distractors: Single index with multiple shards and a category_id field for filtering: Category-based filtering does not prevent cross-category resource contention; all data lives in one index and shares query resources.; Hierarchical chunking inside a single global index: Chunking affects data granularity, not isolation or architectural scaling between categories.; Single index with aggressive replica scaling: Replicas help with availability but do not provide isolation or dedicated scaling paths for different categories.

Misconception tags: Index isolation vs. data filtering; Replica vs. primary scaling

Source trace:

docs.aws.amazon.com/opensearch-service/latest/developerguide/sizing-domains.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-02-data-embeddings-vector-stores-rag.md

### P1-AIP-D2-082

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-082 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.4: Design and implement vector store solutions. |
| `exam_skill` | Skill 1.4.3: Implement high-performance vector database architectures to optimize semantic search performance at scale for FM retrieval (for example, by using OpenSearch sharding strategies, multi-index approaches for specialized domains, hierarchical indexing techniques). |
| `secondary_exam_skills` | Skill 1.4.5: Design and deploy data maintenance systems to ensure that vector stores contain current and accurate information for FM augmentation (for example, by using incremental update mechanisms, real-time change detection systems, automated synchronization workflows, scheduled refresh pipelines). |
| `learning_unit` | Day02-order008 |
| `accelerated_day` | Day 2 |
| `topic` | Vector indexing, sharding, scaling, and performance |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Conceptual; Procedural; Causal; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | explain |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T052105Z-openai-gpt-4.1-day-02-order008.md item 3 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T052105Z |
| `raw_run_id` | order008 |

Stem:

A retrieval pipeline reads streaming updates from S3 into OpenSearch vector indices. Lately, some document queries return out-of-date information. What maintenance strategy would minimize index staleness while balancing operational cost?

Options:

1. Increase the frequency of scheduled full reindexing jobs
2. Implement incremental update pipelines that push only changed documents to the index
3. Run real-time index flush commands on all OpenSearch nodes
4. Manually synchronize S3 and OpenSearch at the end of each day

Correct answer: Implement incremental update pipelines that push only changed documents to the index

Rationale: Incremental update pipelines ensure only updated or new documents are reindexed, minimizing staleness while keeping operational cost low compared to full reindexing.

Distractors: Increase the frequency of scheduled full reindexing jobs: Full reindexing can be very costly and time-intensive, especially as data grows, and is unnecessary for small updates.; Run real-time index flush commands on all OpenSearch nodes: Flush operations write in-memory data to disk but do not pull new data from external sources or address index freshness.; Manually synchronize S3 and OpenSearch at the end of each day: Manual sync is error-prone, does not scale, and introduces avoidable delays in propagating updates.

Misconception tags: Full reindexing vs. incremental updates; Flush commands vs. data ingest

Source trace:

docs.aws.amazon.com/opensearch-service/latest/developerguide/index-data.html#backing-up-index-data

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day-02-answer-guidance.md

### P1-AIP-D2-083

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-083 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.4: Design and implement vector store solutions. |
| `exam_skill` | Skill 1.4.3: Implement high-performance vector database architectures to optimize semantic search performance at scale for FM retrieval (for example, by using OpenSearch sharding strategies, multi-index approaches for specialized domains, hierarchical indexing techniques). |
| `secondary_exam_skills` | Skill 1.4.5: Design and deploy data maintenance systems to ensure that vector stores contain current and accurate information for FM augmentation (for example, by using incremental update mechanisms, real-time change detection systems, automated synchronization workflows, scheduled refresh pipelines). |
| `learning_unit` | Day02-order008 |
| `accelerated_day` | Day 2 |
| `topic` | Vector indexing, sharding, scaling, and performance |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Conceptual; Procedural; Causal; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T052105Z-openai-gpt-4.1-day-02-order008.md item 4 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T052105Z |
| `raw_run_id` | order008 |

Stem:

A semantic retrieval solution using OpenSearch Service begins failing to ingest new vectors under heavy load. The application logs show repeated 'Too many open files' errors on index nodes. What adjustment best addresses this scalability bottleneck?

Options:

1. Increase the shard count and distribute data more evenly across nodes
2. Reduce the replication factor for all indices
3. Switch to hierarchical document chunking
4. Disable automatic index refresh intervals

Correct answer: Increase the shard count and distribute data more evenly across nodes

Rationale: Distributing data with more shards reduces the pressure on nodes, avoids file handle exhaustion, and improves scalability.

Distractors: Reduce the replication factor for all indices: Lowering replication improves write throughput in some cases but does not resolve the open files issue caused by overloading primary nodes.; Switch to hierarchical document chunking: Changing chunking strategy affects retrieval context, not node-level file handle usage.; Disable automatic index refresh intervals: Disabling refresh may delay data visibility but does not reduce file descriptor usage per node.

Misconception tags: Replication vs. sharding; Chunking vs. file system limits

Source trace:

source_trace_needed

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order008-vector-indexing-scaling-performance.md

### P1-AIP-D2-084

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-084 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.4: Design and implement vector store solutions. |
| `exam_skill` | Skill 1.4.3: Implement high-performance vector database architectures to optimize semantic search performance at scale for FM retrieval (for example, by using OpenSearch sharding strategies, multi-index approaches for specialized domains, hierarchical indexing techniques). |
| `secondary_exam_skills` | Skill 1.4.5: Design and deploy data maintenance systems to ensure that vector stores contain current and accurate information for FM augmentation (for example, by using incremental update mechanisms, real-time change detection systems, automated synchronization workflows, scheduled refresh pipelines). |
| `learning_unit` | Day02-order008 |
| `accelerated_day` | Day 2 |
| `topic` | Vector indexing, sharding, scaling, and performance |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Conceptual; Procedural; Causal; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | integrate |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T052105Z-openai-gpt-4.1-day-02-order008.md item 5 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T052105Z |
| `raw_run_id` | order008 |

Stem:

A global enterprise needs fast vector-based search for multilingual documents across regions. Which architectural choice would optimize both query performance and data-residency compliance?

Options:

1. Deploy a single, large OpenSearch cluster in one region with high shard count
2. Deploy multiple OpenSearch clusters, one per region, each containing region-specific indices
3. Use a global index with centralized shard allocation optimized for East-West network traffic
4. Store all vectors in S3 and apply Lambda for search queries

Correct answer: Deploy multiple OpenSearch clusters, one per region, each containing region-specific indices

Rationale: Multiple regional clusters provide local low-latency search and ensure data residency compliance by storing data within regulatory boundaries.

Distractors: Deploy a single, large OpenSearch cluster in one region with high shard count: A single cluster increases latency for remote users and may violate data residency regulations.; Use a global index with centralized shard allocation optimized for East-West network traffic: Centralized shards reduce network latency marginally, but cannot address regulatory or true proximity concerns.; Store all vectors in S3 and apply Lambda for search queries: S3 is not optimized for low-latency, large-scale search, and Lambda is not suited for complex vector search workloads.

Misconception tags: Centralized vs. regional compliance; S3 as a search data store

Source trace:

docs.aws.amazon.com/opensearch-service/latest/developerguide/regional-endpoints.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-02-data-embeddings-vector-stores-rag.md

### P1-AIP-D2-085

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-085 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.4: Design and implement vector store solutions. |
| `exam_skill` | Skill 1.4.3: Implement high-performance vector database architectures to optimize semantic search performance at scale for FM retrieval (for example, by using OpenSearch sharding strategies, multi-index approaches for specialized domains, hierarchical indexing techniques). |
| `secondary_exam_skills` | Skill 1.4.5: Design and deploy data maintenance systems to ensure that vector stores contain current and accurate information for FM augmentation (for example, by using incremental update mechanisms, real-time change detection systems, automated synchronization workflows, scheduled refresh pipelines). |
| `learning_unit` | Day02-order008 |
| `accelerated_day` | Day 2 |
| `topic` | Vector indexing, sharding, scaling, and performance |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Conceptual; Procedural; Causal; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T052105Z-openai-gpt-4.1-day-02-order008.md item 6 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T052105Z |
| `raw_run_id` | order008 |

Stem:

You’re tasked with ingesting frequently changing knowledge base content into an OpenSearch vector store designed for rapid semantic search. Which mechanism will help maintain high data freshness with minimal manual oversight?

Options:

1. Configure an automated incremental update pipeline with change detection from the source
2. Schedule daily full index rebuilds via Lambda
3. Set the OpenSearch index to immutable mode
4. Increase the index replication factor

Correct answer: Configure an automated incremental update pipeline with change detection from the source

Rationale: Automated incremental updates ensure new and changed data are quickly reflected in the index without requiring full rebuilds or heavy manual effort.

Distractors: Schedule daily full index rebuilds via Lambda: Full rebuilds are costly, introduce longer update delays, and Lambda functions are not ideal for large data operations.; Set the OpenSearch index to immutable mode: Immutable mode prevents changes, which is contrary to the requirement for frequently updated content.; Increase the index replication factor: Replication boosts availability, not data freshness or update frequency.

Misconception tags: Replication vs. freshness; Immutable index misconception

Source trace:

source_trace_needed

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order008-vector-indexing-scaling-performance.md

### P1-AIP-D2-086

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-086 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.4: Design and implement vector store solutions. |
| `exam_skill` | Skill 1.4.3: Implement high-performance vector database architectures to optimize semantic search performance at scale for FM retrieval (for example, by using OpenSearch sharding strategies, multi-index approaches for specialized domains, hierarchical indexing techniques). |
| `secondary_exam_skills` | Skill 1.4.5: Design and deploy data maintenance systems to ensure that vector stores contain current and accurate information for FM augmentation (for example, by using incremental update mechanisms, real-time change detection systems, automated synchronization workflows, scheduled refresh pipelines). |
| `learning_unit` | Day02-order008 |
| `accelerated_day` | Day 2 |
| `topic` | Vector indexing, sharding, scaling, and performance |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Conceptual; Procedural; Causal; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | optimize |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T052105Z-openai-gpt-4.1-day-02-order008.md item 7 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T052105Z |
| `raw_run_id` | order008 |

Stem:

A knowledge-intensive GenAI system using vector retrieval on OpenSearch frequently experiences degraded query throughput during peak hours. Metrics show high CPU and memory use on a small subset of nodes. What revision will most directly improve throughput and balance resource usage?

Options:

1. Redistribute shards more evenly across all nodes
2. Switch from vector to lexical search mode
3. Reduce the index refresh interval
4. Increase document chunk size

Correct answer: Redistribute shards more evenly across all nodes

Rationale: Balancing shards across nodes ensures queries and indexing are spread evenly, reducing per-node resource contention and boosting throughput.

Distractors: Switch from vector to lexical search mode: This reduces the power and relevance of semantic search, not addressing scaling under semantic workloads.; Reduce the index refresh interval: Lower refresh intervals may actually increase load without altering load distribution.; Increase document chunk size: Larger chunks can reduce granularity and context effectiveness, and do not solve per-node resource bottlenecks.

Misconception tags: Shard placement vs. search strategy; Chunk size vs. performance

Source trace:

docs.aws.amazon.com/opensearch-service/latest/developerguide/shards.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day-02-answer-guidance.md

### P1-AIP-D2-087

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-087 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.4: Design and implement vector store solutions. |
| `exam_skill` | Skill 1.4.3: Implement high-performance vector database architectures to optimize semantic search performance at scale for FM retrieval (for example, by using OpenSearch sharding strategies, multi-index approaches for specialized domains, hierarchical indexing techniques). |
| `secondary_exam_skills` | Skill 1.4.5: Design and deploy data maintenance systems to ensure that vector stores contain current and accurate information for FM augmentation (for example, by using incremental update mechanisms, real-time change detection systems, automated synchronization workflows, scheduled refresh pipelines). |
| `learning_unit` | Day02-order008 |
| `accelerated_day` | Day 2 |
| `topic` | Vector indexing, sharding, scaling, and performance |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Conceptual; Procedural; Causal; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | compare |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T052105Z-openai-gpt-4.1-day-02-order008.md item 8 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T052105Z |
| `raw_run_id` | order008 |

Stem:

A developer must enable fast semantic search on hundreds of millions of scientific documents, while supporting domain-specific search optimizations. Which OpenSearch design most directly supports scalable performance and targeted optimizations?

Options:

1. Single global index with many shards
2. Multiple indices, one per scientific sub-domain
3. Single index per document type with massive over-sharding
4. One monolithic index with daily reindexing

Correct answer: Multiple indices, one per scientific sub-domain

Rationale: Using multiple indices by domain supports more granular optimizations and avoids bottlenecks of global over-sharding.

Distractors: Single global index with many shards: Oversharding can degrade cluster performance and does not provide domain-level optimization or isolation.; Single index per document type with massive over-sharding: Over-sharding creates unnecessary complexity and still lacks domain-level optimizations.; One monolithic index with daily reindexing: A large index slows queries and ingest, making daily reindexing operationally unscalable.

Misconception tags: Oversharding vs. multi-index design; Reindexing tradeoff

Source trace:

docs.aws.amazon.com/opensearch-service/latest/developerguide/bp-index-management.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day-02-answer-guidance.md

### P1-AIP-D2-088

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-088 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.4: Design and implement vector store solutions. |
| `exam_skill` | Skill 1.4.3: Implement high-performance vector database architectures to optimize semantic search performance at scale for FM retrieval (for example, by using OpenSearch sharding strategies, multi-index approaches for specialized domains, hierarchical indexing techniques). |
| `secondary_exam_skills` | Skill 1.4.5: Design and deploy data maintenance systems to ensure that vector stores contain current and accurate information for FM augmentation (for example, by using incremental update mechanisms, real-time change detection systems, automated synchronization workflows, scheduled refresh pipelines). |
| `learning_unit` | Day02-order008 |
| `accelerated_day` | Day 2 |
| `topic` | Vector indexing, sharding, scaling, and performance |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Conceptual; Procedural; Causal; Embedded |
| `question_format` | multiple-response |
| `difficulty` | hard |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T052105Z-openai-gpt-4.1-day-02-order008.md item 9 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T052105Z |
| `raw_run_id` | order008 |

Stem:

Your team manages an OpenSearch vector database cluster at scale. Which TWO strategies directly help optimize search performance and minimize cluster resource bottlenecks?

Options:

1. Evenly distributing primary shards across data nodes
2. Using multi-index design, with smaller indices per domain
3. Increasing the index refresh interval to 1 second
4. Storing large document vectors as in-place S3 references
5. Employing dedicated master nodes for heavy search traffic

Correct answer: Evenly distributing primary shards across data nodes; Using multi-index design, with smaller indices per domain

Rationale: Balanced sharding and multi-index architectures minimize resource contention, isolate workloads, and provide search optimization opportunities.

Distractors: Increasing the index refresh interval to 1 second: Lower intervals increase index overhead and may degrade performance as the index constantly refreshes.; Storing large document vectors as in-place S3 references: S3 is not a high-performance vector search store and accessing remote S3 references slows queries.; Employing dedicated master nodes for heavy search traffic: Master nodes manage cluster state but are not intended for search workloads; search performance is improved by data nodes.

Misconception tags: Dedicated master node misconception; S3 as high-performance vector store

Source trace:

source_trace_needed

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day-02-answer-guidance.md

### P1-AIP-D2-089

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-089 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.4: Design and implement vector store solutions. |
| `exam_skill` | Skill 1.4.3: Implement high-performance vector database architectures to optimize semantic search performance at scale for FM retrieval (for example, by using OpenSearch sharding strategies, multi-index approaches for specialized domains, hierarchical indexing techniques). |
| `secondary_exam_skills` | Skill 1.4.5: Design and deploy data maintenance systems to ensure that vector stores contain current and accurate information for FM augmentation (for example, by using incremental update mechanisms, real-time change detection systems, automated synchronization workflows, scheduled refresh pipelines). |
| `learning_unit` | Day02-order008 |
| `accelerated_day` | Day 2 |
| `topic` | Vector indexing, sharding, scaling, and performance |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Conceptual; Procedural; Causal; Embedded |
| `question_format` | multiple-response |
| `difficulty` | exam-plus |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 180 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T052105Z-openai-gpt-4.1-day-02-order008.md item 10 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T052105Z |
| `raw_run_id` | order008 |

Stem:

You are scaling a vector-enabled OpenSearch cluster for high availability and performance. Which THREE configuration or design choices help prevent search hot spots and maximize throughput?

Options:

1. Increase the number of primary shards with awareness of node count
2. Design indices based on data domain rather than single monolithic index
3. Allocate replicas for high-read workloads
4. Use hierarchical chunking for large documents before indexing
5. Schedule periodic shard rebalancing as data grows

Correct answer: Increase the number of primary shards with awareness of node count; Design indices based on data domain rather than single monolithic index; Schedule periodic shard rebalancing as data grows

Rationale: Sharding for node-awareness, domain-based indices, and scheduled rebalancing all directly prevent resource hot spots and enable sustainable scaling.

Distractors: Allocate replicas for high-read workloads: Replicas support high-availability and help with concurrent reads, but do not address hot spots due to primary shard overload or poor sharding strategy.; Use hierarchical chunking for large documents before indexing: Chunking helps with retrieval context but does not distribute query load at the cluster or node level directly.

Misconception tags: Replica vs. sharding confusion; Chunking vs. clustering

Source trace:

docs.aws.amazon.com/opensearch-service/latest/developerguide/shards.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order008-vector-indexing-scaling-performance.md

### P1-AIP-D2-090

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-090 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.4: Design and implement vector store solutions. |
| `exam_skill` | Skill 1.4.3: Implement high-performance vector database architectures to optimize semantic search performance at scale for FM retrieval (for example, by using OpenSearch sharding strategies, multi-index approaches for specialized domains, hierarchical indexing techniques). |
| `secondary_exam_skills` | Skill 1.4.5: Design and deploy data maintenance systems to ensure that vector stores contain current and accurate information for FM augmentation (for example, by using incremental update mechanisms, real-time change detection systems, automated synchronization workflows, scheduled refresh pipelines). |
| `learning_unit` | Day02-order008 |
| `accelerated_day` | Day 2 |
| `topic` | Vector indexing, sharding, scaling, and performance |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Conceptual; Procedural; Causal; Embedded |
| `question_format` | multiple-response |
| `difficulty` | exam-plus |
| `cognitive_demand` | optimize |
| `estimated_time_seconds` | 180 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T052105Z-openai-gpt-4.1-day-02-order008.md item 11 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T052105Z |
| `raw_run_id` | order008 |

Stem:

Your AI platform’s OpenSearch vector store supports multiple business units with dramatically different workloads. To optimize performance and minimize the risk of cross-team bottlenecks, which TWO approaches are most appropriate?

Options:

1. Create a separate index per business unit
2. Aggressively over-shard all indices regardless of node count
3. Dynamically allocate and rebalance shards based on observed workload
4. Centralize vector writes into a single shared write queue
5. Configure high replica counts across all indices

Correct answer: Create a separate index per business unit; Dynamically allocate and rebalance shards based on observed workload

Rationale: Per-business unit indices isolate workloads, while dynamic shard rebalancing addresses shifting bottlenecks as use patterns change.

Distractors: Aggressively over-shard all indices regardless of node count: Too many shards increase cluster overhead and degrade performance rather than improve scalability.; Centralize vector writes into a single shared write queue: Centralizing writes creates a bottleneck and single point of failure, hampering scalability.; Configure high replica counts across all indices: Replicas help with availability and read throughput within an index but do not address cross-unit workload separation or primary write bottlenecks.

Misconception tags: Over-sharding trap; Replica/read confusion

Source trace:

source_trace_needed

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-02-data-embeddings-vector-stores-rag.md

### P1-AIP-D2-091

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-091 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.4: Design and implement vector store solutions. |
| `exam_skill` | Skill 1.4.3: Implement high-performance vector database architectures to optimize semantic search performance at scale for FM retrieval (for example, by using OpenSearch sharding strategies, multi-index approaches for specialized domains, hierarchical indexing techniques). |
| `secondary_exam_skills` | Skill 1.4.5: Design and deploy data maintenance systems to ensure that vector stores contain current and accurate information for FM augmentation (for example, by using incremental update mechanisms, real-time change detection systems, automated synchronization workflows, scheduled refresh pipelines). |
| `learning_unit` | Day02-order008 |
| `accelerated_day` | Day 2 |
| `topic` | Vector indexing, sharding, scaling, and performance |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Conceptual; Procedural; Causal; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | judge |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T052105Z-openai-gpt-4.1-day-02-order008.md item 12 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T052105Z |
| `raw_run_id` | order008 |

Stem:

A retrieval team needs strict SLAs on OpenSearch vector search throughput during seasonal peaks. Which configuration should be considered LEAST effective in preventing search latency spikes?

Options:

1. Implement scheduled periodic shard rebalancing operations
2. Increase the number of replicas without adjusting primary shard allocation
3. Adopt a multi-index approach based on traffic domain
4. Use workload-aware sharding guided by query distribution metrics

Correct answer: Increase the number of replicas without adjusting primary shard allocation

Rationale: Adding replicas improves availability and read scaling only up to a point; if primary shards are not properly configured, search traffic can still bottleneck on hot primaries.

Distractors: Implement scheduled periodic shard rebalancing operations: Periodic rebalancing helps distribute load evenly across nodes, directly combating hot spots and improving throughput.; Adopt a multi-index approach based on traffic domain: Domains separated into indices allow traffic surges to be isolated and managed independently.; Use workload-aware sharding guided by query distribution metrics: Dynamic and metrics-guided sharding ensures hot data is properly distributed, minimizing search latency spikes.

Misconception tags: Replica scaling vs. primary bottleneck; Hot spot prevention

Source trace:

docs.aws.amazon.com/opensearch-service/latest/developerguide/shards.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order008-vector-indexing-scaling-performance.md

### P1-AIP-D2-092

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-092 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.4: Design and implement vector store solutions. |
| `exam_skill` | Skill 1.4.3: Implement high-performance vector database architectures to optimize semantic search performance at scale for FM retrieval (for example, by using OpenSearch sharding strategies, multi-index approaches for specialized domains, hierarchical indexing techniques). |
| `secondary_exam_skills` | Skill 1.4.5: Design and deploy data maintenance systems to ensure that vector stores contain current and accurate information for FM augmentation (for example, by using incremental update mechanisms, real-time change detection systems, automated synchronization workflows, scheduled refresh pipelines). |
| `learning_unit` | Day02-order008 |
| `accelerated_day` | Day 2 |
| `topic` | Vector indexing, sharding, scaling, and performance |
| `knowledge_category` | Knowledge; Skill; Representation / Location |
| `knowledge_type` | Conceptual; Procedural; Causal; Embedded |
| `question_format` | multiple-choice |
| `difficulty` | exam-plus |
| `cognitive_demand` | judge |
| `estimated_time_seconds` | 180 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T052105Z-openai-gpt-4.1-day-02-order008.md item 13 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T052105Z |
| `raw_run_id` | order008 |

Stem:

A GenAI RAG system’s OpenSearch domain has grown to handle billions of tokens in hundreds of indices. Recent operational reports show unpredictable search times and maintenance windows exceeding planned outages. Which design flaw is most likely contributing to these side effects?

Options:

1. Too many small shards causing excessive overhead and cluster management challenges
2. Infrequent index refresh intervals delaying visibility of new documents
3. Hierarchical document chunking applied before vectorization
4. Adding dedicated read-only replica nodes to the cluster

Correct answer: Too many small shards causing excessive overhead and cluster management challenges

Rationale: Over-sharding leads to resource exhaustion, maintenance complexity, and unpredictable cluster performance.

Distractors: Infrequent index refresh intervals delaying visibility of new documents: Refresh frequency affects ingestion latency, not long-term search time variability or management complexity.; Hierarchical document chunking applied before vectorization: Chunking affects retrieval granularity, not operational performance at the cluster level.; Adding dedicated read-only replica nodes to the cluster: Read replicas can help query throughput; adding replicas does not degrade performance unless cluster resources are exhausted for other reasons.

Misconception tags: Over-sharding vs. under-refresh; Chunking vs. sharding confusion

Source trace:

docs.aws.amazon.com/opensearch-service/latest/developerguide/bp-index-management.html

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-02-data-embeddings-vector-stores-rag.md

### P1-AIP-D2-093

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-093 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.3: Deploy and configure vector search solutions to enable semantic search capabilities for FM augmentation (for example, by using OpenSearch Service with vector search capabilities, Amazon Aurora with the pgvector extension, Amazon Bedrock Knowledge Bases with managed vector store functionality). |
| `secondary_exam_skills` | Skill 1.5.4: Create advanced search architectures to improve the relevance and accuracy of retrieved information for FM context (for example, by using OpenSearch for semantic search, hybrid search that combines keywords and vectors, Amazon Bedrock reranker models). |
| `learning_unit` | Day02-order009 |
| `accelerated_day` | Day 2 |
| `topic` | Basic semantic retrieval |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T052154Z-openai-gpt-4.1-day-02-order009.md item 1 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T052154Z |
| `raw_run_id` | order009 |

Stem:

A team is using Amazon Bedrock to integrate FM-powered Q&A into their internal document portal. They receive feedback that search results are often irrelevant, even though all documents are present in the vector store. What is the MOST likely cause?

Options:

1. Embeddings were generated using an unrelated domain model.
2. The vector search is not properly connected to the document source.
3. The FM was not fine-tuned on the internal document set.
4. OpenSearch is not configured with hybrid search enabled.

Correct answer: Embeddings were generated using an unrelated domain model.

Rationale: Using unrelated domain models for embedding generation results in vectors that do not capture the semantics of the target domain, degrading retrieval quality.

Distractors: The vector search is not properly connected to the document source.: This would cause missing documents rather than irrelevant results; the scenario states all documents are present in the vector store.; The FM was not fine-tuned on the internal document set.: Fine-tuning may improve response quality but is not required for semantic retrieval to work if embeddings are suitable.; OpenSearch is not configured with hybrid search enabled.: Hybrid search improves recall or relevance in some scenarios, but pure vector search will still return semantically similar documents if embeddings are quality.

Misconception tags: Embedding domain mismatch; Confusing model fine-tuning with vector quality

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order009-basic-semantic-retrieval.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-02-data-embeddings-vector-stores-rag.md

### P1-AIP-D2-094

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-094 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.3: Deploy and configure vector search solutions to enable semantic search capabilities for FM augmentation (for example, by using OpenSearch Service with vector search capabilities, Amazon Aurora with the pgvector extension, Amazon Bedrock Knowledge Bases with managed vector store functionality). |
| `secondary_exam_skills` | Skill 1.5.4: Create advanced search architectures to improve the relevance and accuracy of retrieved information for FM context (for example, by using OpenSearch for semantic search, hybrid search that combines keywords and vectors, Amazon Bedrock reranker models). |
| `learning_unit` | Day02-order009 |
| `accelerated_day` | Day 2 |
| `topic` | Basic semantic retrieval |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T052154Z-openai-gpt-4.1-day-02-order009.md item 2 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T052154Z |
| `raw_run_id` | order009 |

Stem:

A startup is deploying a GenAI chatbot using Amazon Bedrock and wants to improve the relevance of answers provided in a RAG pipeline. Which retrieval method should they configure to allow semantic similarity search between user questions and document passages?

Options:

1. Vector search using Bedrock Knowledge Bases
2. Keyword search on Amazon S3 object metadata
3. Scanning the entire S3 bucket using Lambda
4. Database search using SQL LIKE queries in Aurora

Correct answer: Vector search using Bedrock Knowledge Bases

Rationale: Vector search using Bedrock Knowledge Bases enables semantic similarity search between user inputs and document chunks through embeddings.

Distractors: Keyword search on Amazon S3 object metadata: Only matches text tokens and cannot perform true semantic similarity for retrieval-augmented generation.; Scanning the entire S3 bucket using Lambda: Not a search approach and does not leverage embeddings or semantic similarity.; Database search using SQL LIKE queries in Aurora: Performs exact or partial string matches and does not support semantic retrieval.

Misconception tags: Thinking that keyword or SQL searches provide semantic matching

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order009-basic-semantic-retrieval.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order009-basic-semantic-retrieval.md

### P1-AIP-D2-095

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-095 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.3: Deploy and configure vector search solutions to enable semantic search capabilities for FM augmentation (for example, by using OpenSearch Service with vector search capabilities, Amazon Aurora with the pgvector extension, Amazon Bedrock Knowledge Bases with managed vector store functionality). |
| `secondary_exam_skills` | Skill 1.5.4: Create advanced search architectures to improve the relevance and accuracy of retrieved information for FM context (for example, by using OpenSearch for semantic search, hybrid search that combines keywords and vectors, Amazon Bedrock reranker models). |
| `learning_unit` | Day02-order009 |
| `accelerated_day` | Day 2 |
| `topic` | Basic semantic retrieval |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | explain |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T052154Z-openai-gpt-4.1-day-02-order009.md item 3 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T052154Z |
| `raw_run_id` | order009 |

Stem:

A healthcare provider uses Amazon Aurora with the pgvector extension to support semantic retrieval for a GenAI-based patient Q&A system. Why is this approach superior to SQL text search for their use case?

Options:

1. It allows for retrieval based on meaning, not just keywords.
2. It prioritizes queries with the fewest spelling errors.
3. It automatically restricts results by patient privacy tags.
4. It supports scheduled document re-indexing out of the box.

Correct answer: It allows for retrieval based on meaning, not just keywords.

Rationale: Semantic vector search enables searching for conceptually similar content, not just exact tokens or strings.

Distractors: It prioritizes queries with the fewest spelling errors.: While tolerant of minor text variations via embeddings, the primary advantage is conceptual retrieval.; It automatically restricts results by patient privacy tags.: Security controls require explicit design; semantic retrieval does not enforce access control.; It supports scheduled document re-indexing out of the box.: Aurora with pgvector focuses on retrieval, not on document management or orchestration.

Misconception tags: Assuming semantic search handles all operational/security aspects

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order009-basic-semantic-retrieval.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day-02-answer-guidance.md

### P1-AIP-D2-096

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-096 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.3: Deploy and configure vector search solutions to enable semantic search capabilities for FM augmentation (for example, by using OpenSearch Service with vector search capabilities, Amazon Aurora with the pgvector extension, Amazon Bedrock Knowledge Bases with managed vector store functionality). |
| `secondary_exam_skills` | Skill 1.5.4: Create advanced search architectures to improve the relevance and accuracy of retrieved information for FM context (for example, by using OpenSearch for semantic search, hybrid search that combines keywords and vectors, Amazon Bedrock reranker models). |
| `learning_unit` | Day02-order009 |
| `accelerated_day` | Day 2 |
| `topic` | Basic semantic retrieval |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T052154Z-openai-gpt-4.1-day-02-order009.md item 4 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T052154Z |
| `raw_run_id` | order009 |

Stem:

A manufacturing firm's RAG pipeline uses OpenSearch with vector search enabled. Retrieval quality is poor for industry jargon, although the embedding model is state-of-the-art. Which adjustment is MOST likely to increase relevance for these specialized queries?

Options:

1. Switch to an embedding model trained on manufacturing domain data
2. Enable keyword filter queries only
3. Reduce the number of retrieved documents per query
4. Use database triggers to refresh the OpenSearch index hourly

Correct answer: Switch to an embedding model trained on manufacturing domain data

Rationale: Domain-specific embedding models better capture the meaning of industry jargon, improving retrieval quality.

Distractors: Enable keyword filter queries only: Removes semantic retrieval and relies solely on exact text matching, which misses jargon variations.; Reduce the number of retrieved documents per query: Narrows recall but does not solve the root problem of missing semantic similarity for domain language.; Use database triggers to refresh the OpenSearch index hourly: Keeps data up to date but does not affect the semantic alignment of embeddings and queries.

Misconception tags: Assuming model recency alone solves all domain fit issues; Confusing retrieval tuning with data/embedding alignment

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order009-basic-semantic-retrieval.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order009-basic-semantic-retrieval.md

### P1-AIP-D2-097

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-097 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.3: Deploy and configure vector search solutions to enable semantic search capabilities for FM augmentation (for example, by using OpenSearch Service with vector search capabilities, Amazon Aurora with the pgvector extension, Amazon Bedrock Knowledge Bases with managed vector store functionality). |
| `secondary_exam_skills` | Skill 1.5.4: Create advanced search architectures to improve the relevance and accuracy of retrieved information for FM context (for example, by using OpenSearch for semantic search, hybrid search that combines keywords and vectors, Amazon Bedrock reranker models). |
| `learning_unit` | Day02-order009 |
| `accelerated_day` | Day 2 |
| `topic` | Basic semantic retrieval |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T052154Z-openai-gpt-4.1-day-02-order009.md item 5 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T052154Z |
| `raw_run_id` | order009 |

Stem:

An ecommerce team is building a product assistant using Bedrock Knowledge Bases to answer customer questions. What is the PRIMARY advantage of using vector search over keyword-only search for this workflow?

Options:

1. It retrieves passages semantically similar to the user’s query.
2. It automatically tags documents with product categories.
3. It guarantees that only the latest product manuals are retrieved.
4. It reduces the document preprocessing steps needed.

Correct answer: It retrieves passages semantically similar to the user’s query.

Rationale: Vector search enables retrieval of contextually relevant content even when query terms differ from passage wording.

Distractors: It automatically tags documents with product categories.: Tagging requires explicit logic or metadata design; vector search does not assign categories.; It guarantees that only the latest product manuals are retrieved.: Freshness control requires filtering or metadata, not semantic similarity alone.; It reduces the document preprocessing steps needed.: Preprocessing is still needed for chunking, embedding generation, and metadata assignment.

Misconception tags: Assuming vector search handles freshness or tags

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order009-basic-semantic-retrieval.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-02-data-embeddings-vector-stores-rag.md

### P1-AIP-D2-098

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-098 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.3: Deploy and configure vector search solutions to enable semantic search capabilities for FM augmentation (for example, by using OpenSearch Service with vector search capabilities, Amazon Aurora with the pgvector extension, Amazon Bedrock Knowledge Bases with managed vector store functionality). |
| `secondary_exam_skills` | Skill 1.5.4: Create advanced search architectures to improve the relevance and accuracy of retrieved information for FM context (for example, by using OpenSearch for semantic search, hybrid search that combines keywords and vectors, Amazon Bedrock reranker models). |
| `learning_unit` | Day02-order009 |
| `accelerated_day` | Day 2 |
| `topic` | Basic semantic retrieval |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural |
| `question_format` | multiple-response |
| `difficulty` | hard |
| `cognitive_demand` | integrate |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T052154Z-openai-gpt-4.1-day-02-order009.md item 6 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T052154Z |
| `raw_run_id` | order009 |

Stem:

Which of the following are essential configuration steps when enabling semantic vector search for a RAG workflow with Amazon OpenSearch Service? (Select TWO.)

Options:

1. Generate document embeddings using a supported model
2. Configure a vector field in the OpenSearch index mapping
3. Enable S3 event notifications for index refresh
4. Add document access control lists to the OpenSearch index
5. Increase database cache size

Correct answer: Generate document embeddings using a supported model; Configure a vector field in the OpenSearch index mapping

Rationale: Embeddings must be generated for semantically meaningful vectors, and a vector field must exist in the index mapping for OpenSearch to store and retrieve vectors.

Distractors: Enable S3 event notifications for index refresh: Event notifications may help update content but are not required to enable vector search.; Add document access control lists to the OpenSearch index: Access control supports security but does not enable or configure semantic search.; Increase database cache size: Cache tuning can affect performance but is not related to vector search configuration.

Misconception tags: Believing access controls or cache tuning enables semantic search

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order009-basic-semantic-retrieval.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order009-basic-semantic-retrieval.md

### P1-AIP-D2-099

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-099 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.3: Deploy and configure vector search solutions to enable semantic search capabilities for FM augmentation (for example, by using OpenSearch Service with vector search capabilities, Amazon Aurora with the pgvector extension, Amazon Bedrock Knowledge Bases with managed vector store functionality). |
| `secondary_exam_skills` | Skill 1.5.4: Create advanced search architectures to improve the relevance and accuracy of retrieved information for FM context (for example, by using OpenSearch for semantic search, hybrid search that combines keywords and vectors, Amazon Bedrock reranker models). |
| `learning_unit` | Day02-order009 |
| `accelerated_day` | Day 2 |
| `topic` | Basic semantic retrieval |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | explain |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T052154Z-openai-gpt-4.1-day-02-order009.md item 7 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T052154Z |
| `raw_run_id` | order009 |

Stem:

A legal firm uses RAG with Amazon Aurora and the pgvector extension to retrieve relevant case studies. What happens if a user’s query is semantically very different from any document in the database, but vector search is still used?

Options:

1. The closest (least distant) document vectors will be returned, but results are likely irrelevant.
2. No results will be returned at all.
3. The query will trigger a fallback to keyword search automatically.
4. The database will prevent the query from running.

Correct answer: The closest (least distant) document vectors will be returned, but results are likely irrelevant.

Rationale: Vector search always returns the nearest neighbors; with no close semantic matches, irrelevant results are surfaced.

Distractors: No results will be returned at all.: Vector similarity search ranks all embeddings, so at least the closest matches will be returned.; The query will trigger a fallback to keyword search automatically.: Fallback logic must be manually implemented; there is no automatic fallback.; The database will prevent the query from running.: The engine does not block searches for low similarity queries.

Misconception tags: Assuming vector search returns nothing for distant queries; Expecting automatic fallback behavior

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order009-basic-semantic-retrieval.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day-02-answer-guidance.md

### P1-AIP-D2-100

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-100 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.3: Deploy and configure vector search solutions to enable semantic search capabilities for FM augmentation (for example, by using OpenSearch Service with vector search capabilities, Amazon Aurora with the pgvector extension, Amazon Bedrock Knowledge Bases with managed vector store functionality). |
| `secondary_exam_skills` | Skill 1.5.4: Create advanced search architectures to improve the relevance and accuracy of retrieved information for FM context (for example, by using OpenSearch for semantic search, hybrid search that combines keywords and vectors, Amazon Bedrock reranker models). |
| `learning_unit` | Day02-order009 |
| `accelerated_day` | Day 2 |
| `topic` | Basic semantic retrieval |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | judge |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T052154Z-openai-gpt-4.1-day-02-order009.md item 8 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T052154Z |
| `raw_run_id` | order009 |

Stem:

A financial data company wants to use RAG with OpenSearch Service and vector similarity search. The business requires (1) secure retrieval for regulated users and (2) the highest possible relevance. Which configuration is MOST likely to meet these requirements?

Options:

1. Combine vector search with document-level access filters and reranker models.
2. Enable vector search and disable all ACLs for faster retrieval.
3. Rely on OpenSearch’s default text search and avoid embeddings for simplicity.
4. Use embeddings only for indexing, but filter by timestamp fields only.

Correct answer: Combine vector search with document-level access filters and reranker models.

Rationale: Combining semantic similarity, secure access filtering, and post-processing rerankers optimizes both relevance and compliance in retrieval.

Distractors: Enable vector search and disable all ACLs for faster retrieval.: Removes security and compliance controls, violating business requirements.; Rely on OpenSearch’s default text search and avoid embeddings for simplicity.: Sacrifices semantic matching, reducing retrieval relevance.; Use embeddings only for indexing, but filter by timestamp fields only.: Timestamp filtering improves freshness but does not guarantee security or relevance.

Misconception tags: Assuming semantic search covers access control and security automatically

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order009-basic-semantic-retrieval.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-02-data-embeddings-vector-stores-rag.md

### P1-AIP-D2-101

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-101 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.3: Deploy and configure vector search solutions to enable semantic search capabilities for FM augmentation (for example, by using OpenSearch Service with vector search capabilities, Amazon Aurora with the pgvector extension, Amazon Bedrock Knowledge Bases with managed vector store functionality). |
| `secondary_exam_skills` | Skill 1.5.4: Create advanced search architectures to improve the relevance and accuracy of retrieved information for FM context (for example, by using OpenSearch for semantic search, hybrid search that combines keywords and vectors, Amazon Bedrock reranker models). |
| `learning_unit` | Day02-order009 |
| `accelerated_day` | Day 2 |
| `topic` | Basic semantic retrieval |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural |
| `question_format` | multiple-response |
| `difficulty` | hard |
| `cognitive_demand` | compare |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T052154Z-openai-gpt-4.1-day-02-order009.md item 9 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T052154Z |
| `raw_run_id` | order009 |

Stem:

A team is evaluating three approaches for improving semantic retrieval relevance in their Bedrock Knowledge Bases pipeline. Which strategies would directly increase the accuracy of results? (Select TWO.)

Options:

1. Implementing hybrid search that combines keyword and vector similarity
2. Switching to random document chunk order during embedding
3. Applying reranker models after initial retrieval
4. Reducing input document size without regard to logical boundaries
5. Increasing the maximum number of returned documents per query

Correct answer: Implementing hybrid search that combines keyword and vector similarity; Applying reranker models after initial retrieval

Rationale: Hybrid search covers cases where embeddings or keywords alone would miss relevant results. Rerankers reorder candidates for maximal relevance.

Distractors: Switching to random document chunk order during embedding: Randomizing chunk order breaks context and likely reduces retrieval quality.; Reducing input document size without regard to logical boundaries: Chunking without semantic boundaries harms retrieval accuracy.; Increasing the maximum number of returned documents per query: May improve recall, but dilutes relevance and does not optimize accuracy.

Misconception tags: Confusing recall with relevance; Assuming randomization or brute-force improves results

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order009-basic-semantic-retrieval.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order009-basic-semantic-retrieval.md

### P1-AIP-D2-102

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-102 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.3: Deploy and configure vector search solutions to enable semantic search capabilities for FM augmentation (for example, by using OpenSearch Service with vector search capabilities, Amazon Aurora with the pgvector extension, Amazon Bedrock Knowledge Bases with managed vector store functionality). |
| `secondary_exam_skills` | Skill 1.5.4: Create advanced search architectures to improve the relevance and accuracy of retrieved information for FM context (for example, by using OpenSearch for semantic search, hybrid search that combines keywords and vectors, Amazon Bedrock reranker models). |
| `learning_unit` | Day02-order009 |
| `accelerated_day` | Day 2 |
| `topic` | Basic semantic retrieval |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T052154Z-openai-gpt-4.1-day-02-order009.md item 10 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T052154Z |
| `raw_run_id` | order009 |

Stem:

A developer is asked why semantic vector search in their solution may still return imprecise answers after deploying Bedrock Knowledge Bases. Which action is MOST likely to improve result precision?

Options:

1. Increase the granularity of document chunking during preprocessing
2. Use an older embedding model for backward compatibility
3. Reduce the dimensionality of the embeddings
4. Rely on raw PDF blobs instead of chunked passage text

Correct answer: Increase the granularity of document chunking during preprocessing

Rationale: Smaller, context-aware chunks produce more focused embeddings, leading to more precise retrieval.

Distractors: Use an older embedding model for backward compatibility: Older models tend to lower retrieval performance.; Reduce the dimensionality of the embeddings: May cause loss of semantic resolution, not better accuracy.; Rely on raw PDF blobs instead of chunked passage text: Blobs create poorly-aligned embeddings, reducing precision.

Misconception tags: Conflating chunk size, embedding dimensionality, and retrieval precision

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order009-basic-semantic-retrieval.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day-02-answer-guidance.md

### P1-AIP-D2-103

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-103 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.3: Deploy and configure vector search solutions to enable semantic search capabilities for FM augmentation (for example, by using OpenSearch Service with vector search capabilities, Amazon Aurora with the pgvector extension, Amazon Bedrock Knowledge Bases with managed vector store functionality). |
| `secondary_exam_skills` | Skill 1.5.4: Create advanced search architectures to improve the relevance and accuracy of retrieved information for FM context (for example, by using OpenSearch for semantic search, hybrid search that combines keywords and vectors, Amazon Bedrock reranker models). |
| `learning_unit` | Day02-order009 |
| `accelerated_day` | Day 2 |
| `topic` | Basic semantic retrieval |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural |
| `question_format` | multiple-choice |
| `difficulty` | exam-plus |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 180 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T052154Z-openai-gpt-4.1-day-02-order009.md item 11 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T052154Z |
| `raw_run_id` | order009 |

Stem:

You are troubleshooting a Bedrock-powered RAG application where users report that queries about new policy documents are not returning expected results. All embeddings were generated last quarter. The source data is up to date in S3 and accessible. What is the MOST likely cause?

Options:

1. Vector embeddings have not been updated for the latest documents.
2. The Bedrock model is not fine-tuned for policy Q&A.
3. The S3 bucket uses an incompatible storage class.
4. OpenSearch index does not have search analyzers enabled.

Correct answer: Vector embeddings have not been updated for the latest documents.

Rationale: Unless embeddings are refreshed after new documents are added, semantic retrieval cannot surface up-to-date content.

Distractors: The Bedrock model is not fine-tuned for policy Q&A.: Fine-tuning affects answer quality, not the ability to retrieve new content if embeddings are missing.; The S3 bucket uses an incompatible storage class.: Assumes access is not a problem; scenario says S3 is accessible.; OpenSearch index does not have search analyzers enabled.: Search analyzers are relevant to keyword search, not semantic retrieval.

Misconception tags: Confusing answer generation with retrieval gaps; Assuming model tuning vs. data currency

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order009-basic-semantic-retrieval.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-02-data-embeddings-vector-stores-rag.md

### P1-AIP-D2-104

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-104 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.3: Deploy and configure vector search solutions to enable semantic search capabilities for FM augmentation (for example, by using OpenSearch Service with vector search capabilities, Amazon Aurora with the pgvector extension, Amazon Bedrock Knowledge Bases with managed vector store functionality). |
| `secondary_exam_skills` | Skill 1.5.4: Create advanced search architectures to improve the relevance and accuracy of retrieved information for FM context (for example, by using OpenSearch for semantic search, hybrid search that combines keywords and vectors, Amazon Bedrock reranker models). |
| `learning_unit` | Day02-order009 |
| `accelerated_day` | Day 2 |
| `topic` | Basic semantic retrieval |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural |
| `question_format` | multiple-response |
| `difficulty` | hard |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T052154Z-openai-gpt-4.1-day-02-order009.md item 12 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T052154Z |
| `raw_run_id` | order009 |

Stem:

A media company is designing a semantic retrieval layer for its FAQ chatbot using Amazon Aurora and pgvector. Which steps are REQUIRED to enable FM-powered semantic search in this architecture? (Select TWO.)

Options:

1. Storing document embeddings in Aurora along with content
2. Implementing vector similarity queries with pgvector functions
3. Using S3 event notifications for push updates
4. Enabling full-text search indexes
5. Deploying a synchronous SageMaker endpoint

Correct answer: Storing document embeddings in Aurora along with content; Implementing vector similarity queries with pgvector functions

Rationale: Semantic search requires both persistent vector storage and specialized similarity queries using pgvector.

Distractors: Using S3 event notifications for push updates: May be useful for syncing but not required to enable vector search.; Enabling full-text search indexes: Supports keyword search, not semantic vector search.; Deploying a synchronous SageMaker endpoint: Useful for embedding generation, but semantic search itself requires no endpoint at inference time.

Misconception tags: Equating full-text indexing or event hooks with semantic configuration

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order009-basic-semantic-retrieval.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day-02-answer-guidance.md

### P1-AIP-D2-105

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-105 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.6: Create consistent access mechanisms to enable seamless integration with FMs (for example, by using function calling interfaces for vector search, Model Context Protocol [MCP] clients for vector queries, standardized API patterns for retrieval augmentation). |
| `secondary_exam_skills` | Skill 1.1.1: Create comprehensive architectural designs that align with specific business needs and technical constraints (for example, by using appropriate FMs, integration patterns, deployment strategies). |
| `learning_unit` | Day02-order010 |
| `accelerated_day` | Day 2 |
| `topic` | Basic Retrieval-Augmented Generation |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Strategic |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T052302Z-openai-gpt-4.1-day-02-order010.md item 2 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T052302Z |
| `raw_run_id` | order010 |

Stem:

You are architecting a Retrieval-Augmented Generation (RAG) pipeline. The pipeline must allow future FM replacements without disrupting access patterns to the retrieval back end. Which design enables this flexibility?

Options:

1. Define a consistent retrieval interface with a function-calling protocol and abstract retrieval logic from the FM endpoint.
2. Embed context retrieval logic directly in the FM prompt and update it with each model change.
3. Use different custom APIs for each FM so that queries can be optimized per model.
4. Connect the FM to the vector database using hardcoded endpoint URLs from environment variables.

Correct answer: Define a consistent retrieval interface with a function-calling protocol and abstract retrieval logic from the FM endpoint.

Rationale: A standardized interface decouples retrieval and generation, allowing models to be swapped without major backend rewrites.

Distractors: Embed context retrieval logic directly in the FM prompt and update it with each model change.: Embedding logic in prompts tightly couples FM and retrieval and won't scale with changing models.; Use different custom APIs for each FM so that queries can be optimized per model.: Using different APIs hinders flexibility and increases maintenance.; Connect the FM to the vector database using hardcoded endpoint URLs from environment variables.: Hardcoded URLs reduce portability and increase risk during FM replacement.

Misconception tags: Hardcoding logic; Prompt-injection for orchestration

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order010-basic-rag-design.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order010-basic-rag-design.md

### P1-AIP-D2-106

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-106 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.6: Create consistent access mechanisms to enable seamless integration with FMs (for example, by using function calling interfaces for vector search, Model Context Protocol [MCP] clients for vector queries, standardized API patterns for retrieval augmentation). |
| `secondary_exam_skills` | Skill 1.1.1: Create comprehensive architectural designs that align with specific business needs and technical constraints (for example, by using appropriate FMs, integration patterns, deployment strategies). |
| `learning_unit` | Day02-order010 |
| `accelerated_day` | Day 2 |
| `topic` | Basic Retrieval-Augmented Generation |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Strategic |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T052302Z-openai-gpt-4.1-day-02-order010.md item 3 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T052302Z |
| `raw_run_id` | order010 |

Stem:

After deploying a basic RAG architecture, users notice that the FM sometimes hallucinates outdated facts, even though recent documents are added to the knowledge base. Which underlying architectural gap is most likely responsible?

Options:

1. The retrieval process does not enforce synchronization between the vector store and live source documents.
2. The FM is not fine-tuned for the customer’s domain and generates general knowledge instead.
3. The RAG pipeline lacks prompt engineering to emphasize retrieval grounding.
4. The system does not include an additional classifier model for relevance filtering.

Correct answer: The retrieval process does not enforce synchronization between the vector store and live source documents.

Rationale: If embedding/vector stores are not regularly refreshed from the primary content sources, retrieval can serve stale or missing information, leading to outdated FM responses.

Distractors: The FM is not fine-tuned for the customer’s domain and generates general knowledge instead.: Domain fine-tuning may improve accuracy but does not address content freshness in retrieval.; The RAG pipeline lacks prompt engineering to emphasize retrieval grounding.: Prompt engineering is important but secondary; failure to refresh data is a foundational architectural issue.; The system does not include an additional classifier model for relevance filtering.: A classifier may improve ranking but does not resolve staleness from lack of source-data synchronization.

Misconception tags: Assuming fine-tuning or prompts solve data freshness

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order010-basic-rag-design.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day-02-answer-guidance.md

### P1-AIP-D2-107

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-107 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.6: Create consistent access mechanisms to enable seamless integration with FMs (for example, by using function calling interfaces for vector search, Model Context Protocol [MCP] clients for vector queries, standardized API patterns for retrieval augmentation). |
| `secondary_exam_skills` | Skill 1.1.1: Create comprehensive architectural designs that align with specific business needs and technical constraints (for example, by using appropriate FMs, integration patterns, deployment strategies). |
| `learning_unit` | Day02-order010 |
| `accelerated_day` | Day 2 |
| `topic` | Basic Retrieval-Augmented Generation |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Strategic |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | explain |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T052302Z-openai-gpt-4.1-day-02-order010.md item 4 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T052302Z |
| `raw_run_id` | order010 |

Stem:

A new RAG-based document assistant is deployed using Amazon Bedrock Knowledge Bases. The development team wants consistent FM behavior when scaling to multiple business units with differing data privacy requirements. Which design best supports secure, seamless RAG for this scenario?

Options:

1. Apply metadata-based access controls on vector store queries and standardize API integration to filter context for each business unit.
2. Embed organization identifiers in the LLM prompt and rely on the FM to restrict context results accordingly.
3. Use a single shared vector store for all data and implement filtering in the client application.
4. Create separate endpoint APIs for each business unit, each backed by an isolated FM instance.

Correct answer: Apply metadata-based access controls on vector store queries and standardize API integration to filter context for each business unit.

Rationale: Access control at the retrieval/query layer ensures the FM receives only appropriate context for each business unit, in a scalable, manageable way using standardized APIs.

Distractors: Embed organization identifiers in the LLM prompt and rely on the FM to restrict context results accordingly.: The FM cannot enforce fine-grained access control on its own based on prompt content.; Use a single shared vector store for all data and implement filtering in the client application.: Client-side filtering risks leakage and does not enforce security at the data access layer.; Create separate endpoint APIs for each business unit, each backed by an isolated FM instance.: This approach does not scale and multiplies operational overhead.

Misconception tags: Assuming LLM can enforce business rules; Misplaced access control

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order010-basic-rag-design.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-02-data-embeddings-vector-stores-rag.md

### P1-AIP-D2-108

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-108 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.6: Create consistent access mechanisms to enable seamless integration with FMs (for example, by using function calling interfaces for vector search, Model Context Protocol [MCP] clients for vector queries, standardized API patterns for retrieval augmentation). |
| `secondary_exam_skills` | Skill 1.1.1: Create comprehensive architectural designs that align with specific business needs and technical constraints (for example, by using appropriate FMs, integration patterns, deployment strategies). |
| `learning_unit` | Day02-order010 |
| `accelerated_day` | Day 2 |
| `topic` | Basic Retrieval-Augmented Generation |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Strategic |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | judge |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T052302Z-openai-gpt-4.1-day-02-order010.md item 6 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T052302Z |
| `raw_run_id` | order010 |

Stem:

During a code review, a junior developer suggests invoking search APIs directly from within the FM inference handler so the model can locate and retrieve the information it needs. What is the primary architectural flaw in this approach?

Options:

1. It incorrectly assumes that the FM can autonomously conduct searches and navigate external APIs.
2. It requires each API to return inference-ready prompt text, which is not possible using standard vector stores.
3. It improves modularity but adds unnecessary cost and latency.
4. It implements a correct but less efficient approach to retrieval-augmented generation.

Correct answer: It incorrectly assumes that the FM can autonomously conduct searches and navigate external APIs.

Rationale: FM endpoints cannot independently interact with external APIs—retrieval orchestration and context injection must occur outside the FM.

Distractors: It requires each API to return inference-ready prompt text, which is not possible using standard vector stores.: Tempting, but vector stores can return text chunks—problem is not formatting but misplaced orchestration.; It improves modularity but adds unnecessary cost and latency.: This is not the core flaw; the flaw is in misunderstanding FM boundaries.; It implements a correct but less efficient approach to retrieval-augmented generation.: The approach is not correct at all—the architectural contract is violated.

Misconception tags: Assuming FM can do external retrieval itself

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order010-basic-rag-design.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day-02-answer-guidance.md

### P1-AIP-D2-109

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-109 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.6: Create consistent access mechanisms to enable seamless integration with FMs (for example, by using function calling interfaces for vector search, Model Context Protocol [MCP] clients for vector queries, standardized API patterns for retrieval augmentation). |
| `secondary_exam_skills` | Skill 1.1.1: Create comprehensive architectural designs that align with specific business needs and technical constraints (for example, by using appropriate FMs, integration patterns, deployment strategies). |
| `learning_unit` | Day02-order010 |
| `accelerated_day` | Day 2 |
| `topic` | Basic Retrieval-Augmented Generation |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Strategic |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | implement |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T052302Z-openai-gpt-4.1-day-02-order010.md item 8 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T052302Z |
| `raw_run_id` | order010 |

Stem:

A cross-functional AWS team needs to integrate a new document source into their RAG pipeline while maintaining consistent retrieval and FM consumption. What is the FIRST step to preserve seamless API-based retrieval augmentation?

Options:

1. Implement a document chunker that formats new source data to match retrieval interface requirements.
2. Update the FM architecture to directly ingest new documents without vectorization.
3. Configure FM endpoints to increase their maximum input context size for the new data.
4. Change the retrieval orchestration so that the FM initiates its own fetch of the new document type.

Correct answer: Implement a document chunker that formats new source data to match retrieval interface requirements.

Rationale: Consistent chunking and formatting allows the new source to be added to the retrieval pipeline, maintaining API compatibility and seamless augmentation.

Distractors: Update the FM architecture to directly ingest new documents without vectorization.: Skipping vectorization breaks the RAG paradigm and may overwhelm FM context windows.; Configure FM endpoints to increase their maximum input context size for the new data.: Attempting to increase FM context does not solve retrieval/formatting alignment.; Change the retrieval orchestration so that the FM initiates its own fetch of the new document type.: FM endpoints cannot independently initiate retrieval—this is a design misunderstanding.

Misconception tags: Skipping formatting/vectorization; Misunderstanding FM system boundaries

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order010-basic-rag-design.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order010-basic-rag-design.md

### P1-AIP-D2-110

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-110 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.6: Create consistent access mechanisms to enable seamless integration with FMs (for example, by using function calling interfaces for vector search, Model Context Protocol [MCP] clients for vector queries, standardized API patterns for retrieval augmentation). |
| `secondary_exam_skills` | Skill 1.1.1: Create comprehensive architectural designs that align with specific business needs and technical constraints (for example, by using appropriate FMs, integration patterns, deployment strategies). |
| `learning_unit` | Day02-order010 |
| `accelerated_day` | Day 2 |
| `topic` | Basic Retrieval-Augmented Generation |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Strategic |
| `question_format` | multiple-choice |
| `difficulty` | exam-plus |
| `cognitive_demand` | judge |
| `estimated_time_seconds` | 180 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T052302Z-openai-gpt-4.1-day-02-order010.md item 9 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T052302Z |
| `raw_run_id` | order010 |

Stem:

In a cost review, you find that RAG inference spends more on outbound network transfer fees than on FM inference. Each query retrieves dozens of full documents as context. Which architectural change best addresses this?

Options:

1. Restrict context retrieval to top-k most semantically similar chunks using Bedrock’s retrieval API.
2. Move the FM endpoint closer to the vector database using a private VPC endpoint.
3. Precompute and cache all likely context documents in an S3 bucket daily.
4. Switch from semantic search to keyword-based search to reduce chunk count.

Correct answer: Restrict context retrieval to top-k most semantically similar chunks using Bedrock’s retrieval API.

Rationale: Top-k retrieval limits outbound data by only sending the most relevant chunks, reducing network usage without sacrificing RAG answer quality.

Distractors: Move the FM endpoint closer to the vector database using a private VPC endpoint.: Proximity helps with latency but not overall data transfer if the volume of sent content is still excessive.; Precompute and cache all likely context documents in an S3 bucket daily.: This could add operational costs and does not trim query-time payload size.; Switch from semantic search to keyword-based search to reduce chunk count.: Keyword search may reduce results but lowers answer relevance, not addressing the optimization mandate.

Misconception tags: Confusing network optimization with protocol optimization; Believing switching to keyword search will lower network costs while keeping retrieval quality

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order010-basic-rag-design.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day-02-answer-guidance.md

### P1-AIP-D2-111

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-111 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.6: Create consistent access mechanisms to enable seamless integration with FMs (for example, by using function calling interfaces for vector search, Model Context Protocol [MCP] clients for vector queries, standardized API patterns for retrieval augmentation). |
| `secondary_exam_skills` | Skill 1.1.1: Create comprehensive architectural designs that align with specific business needs and technical constraints (for example, by using appropriate FMs, integration patterns, deployment strategies). |
| `learning_unit` | Day02-order010 |
| `accelerated_day` | Day 2 |
| `topic` | Basic Retrieval-Augmented Generation |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Strategic |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | configure |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T052302Z-openai-gpt-4.1-day-02-order010.md item 12 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T052302Z |
| `raw_run_id` | order010 |

Stem:

An engineering team must ensure low-latency, reliable retrieval of relevant chunks for each FM query in their Bedrock-based RAG pipeline. Which configuration best supports this requirement?

Options:

1. Tune the top-k retrieval parameter in Bedrock Knowledge Base API to minimize context size while retaining relevance.
2. Increase the FM’s maximum input context window to accept all retrieved content.
3. Remove retrieval orchestration and let the FM handle the search.
4. Configure S3 EventBridge triggers to push new documents to the FM immediately.

Correct answer: Tune the top-k retrieval parameter in Bedrock Knowledge Base API to minimize context size while retaining relevance.

Rationale: Adjusting top-k retrieval helps control retrieval latency and limits how much text the FM must process, improving end-to-end responsiveness.

Distractors: Increase the FM’s maximum input context window to accept all retrieved content.: Increasing input window does not solve the need to filter for relevance or meet latency targets.; Remove retrieval orchestration and let the FM handle the search.: FM endpoints cannot search data directly; they require properly orchestrated context injection.; Configure S3 EventBridge triggers to push new documents to the FM immediately.: Triggers help with ingest but do not address runtime retrieval configuration or latency.

Misconception tags: Ignoring FM/retrieval boundaries; Assuming larger context window is always better

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order010-basic-rag-design.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-02-data-embeddings-vector-stores-rag.md

### P1-AIP-D2-112

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-112 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.6: Create consistent access mechanisms to enable seamless integration with FMs (for example, by using function calling interfaces for vector search, Model Context Protocol [MCP] clients for vector queries, standardized API patterns for retrieval augmentation). |
| `secondary_exam_skills` | Skill 1.1.1: Create comprehensive architectural designs that align with specific business needs and technical constraints (for example, by using appropriate FMs, integration patterns, deployment strategies). |
| `learning_unit` | Day02-order010 |
| `accelerated_day` | Day 2 |
| `topic` | Basic Retrieval-Augmented Generation |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Strategic |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | optimize |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T052302Z-openai-gpt-4.1-day-02-order010.md item 13 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T052302Z |
| `raw_run_id` | order010 |

Stem:

A large organization is facing high latency in FM responses within its RAG workflow on AWS. The RAG system uses Amazon Bedrock with a managed knowledge base, but users report slow answer times. What is the FIRST tuning parameter to evaluate for overall response time optimization?

Options:

1. The top-k retrieval limit used for fetching context from the vector store.
2. The concurrency setting of the downstream FM inference endpoint.
3. The IAM policy permissions on the retrieval pipeline.
4. The batch size used by the document chunking Lambda.

Correct answer: The top-k retrieval limit used for fetching context from the vector store.

Rationale: Reducing the number of chunks (top-k) retrieved can have an immediate and significant impact on query performance and FM response times.

Distractors: The concurrency setting of the downstream FM inference endpoint.: While relevant, response times are often dominated by retrieval latency rather than FM inference at moderate scale.; The IAM policy permissions on the retrieval pipeline.: Permissions affect security, not response time.; The batch size used by the document chunking Lambda.: Chunking batch size relates to preprocessing throughput, not runtime latency.

Misconception tags: Confusing preprocessing performance with runtime tuning

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order010-basic-rag-design.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day-02-answer-guidance.md

### P1-AIP-D2-113

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-113 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.6: Create consistent access mechanisms to enable seamless integration with FMs (for example, by using function calling interfaces for vector search, Model Context Protocol [MCP] clients for vector queries, standardized API patterns for retrieval augmentation). |
| `secondary_exam_skills` | Skill 1.1.1: Create comprehensive architectural designs that align with specific business needs and technical constraints (for example, by using appropriate FMs, integration patterns, deployment strategies). |
| `learning_unit` | Day02-order010 |
| `accelerated_day` | Day 2 |
| `topic` | Basic Retrieval-Augmented Generation |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Strategic |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T060928Z-openai-gpt-4.1-day-02-order010-top-up-4.md item 1 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T060928Z |
| `raw_run_id` | order010-top-up-4 |

Stem:

A team is building a language support chatbot using a RAG pipeline on AWS. The business requires the ability to swap out the FM provider in the future without rewriting the retrieval and context-assembly logic. Which design pattern best ensures this separation and future portability?

Options:

1. Implement a service layer that exposes a standardized retrieval API and keeps FM consumption code separate from retrieval logic.
2. Hardcode vector store connection details within the FM inference script to ensure direct access to context.
3. Use in-FM prompt engineering to specify the retrieval and context-assembly instructions.
4. Integrate vector store and FM consumption flows tightly into a single Lambda for highest throughput.

Correct answer: Implement a service layer that exposes a standardized retrieval API and keeps FM consumption code separate from retrieval logic.

Rationale: A service layer with a standardized API abstracts retrieval and context construction, allowing the FM to be replaced without affecting retrieval logic—a best practice aligned with modular and maintainable RAG architectures.

Distractors: Hardcode vector store connection details within the FM inference script to ensure direct access to context.: Tempting since it provides a quick solution but tightly couples retrieval to FM code, making provider swaps difficult.; Use in-FM prompt engineering to specify the retrieval and context-assembly instructions.: Misconception that prompt engineering can manage external data retrieval—FMs do not inherently perform retrieval based on prompt instructions.; Integrate vector store and FM consumption flows tightly into a single Lambda for highest throughput.: Combining logic for performance sacrifices modularity and makes migrations harder; not best practice for future portability.

Misconception tags: Confusing prompt engineering with retrieval orchestration; Ignoring modular design for maintainability

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order010-basic-rag-design.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-02-data-embeddings-vector-stores-rag.md

### P1-AIP-D2-114

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-114 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.6: Create consistent access mechanisms to enable seamless integration with FMs (for example, by using function calling interfaces for vector search, Model Context Protocol [MCP] clients for vector queries, standardized API patterns for retrieval augmentation). |
| `secondary_exam_skills` | Skill 1.1.1: Create comprehensive architectural designs that align with specific business needs and technical constraints (for example, by using appropriate FMs, integration patterns, deployment strategies). |
| `learning_unit` | Day02-order010 |
| `accelerated_day` | Day 2 |
| `topic` | Basic Retrieval-Augmented Generation |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Strategic |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T060928Z-openai-gpt-4.1-day-02-order010-top-up-4.md item 2 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T060928Z |
| `raw_run_id` | order010-top-up-4 |

Stem:

A FinTech company notices inconsistent relevance in their FM-generated answers within their RAG workflow. Investigation shows that retrieval calls sometimes fetch context from the incorrect knowledge base. What is the most likely root cause?

Options:

1. Retrieval requests lack explicit knowledge base or domain parameters, causing ambiguous routing.
2. The FM is not capable of understanding multiple languages in retrieved content.
3. Context chunks are formatted in XML while the FM expects JSON input.
4. Vector embeddings are regenerated on every request, adding latency.

Correct answer: Retrieval requests lack explicit knowledge base or domain parameters, causing ambiguous routing.

Rationale: Ambiguous retrieval calls often default to an unintended source if request parameters do not make the intended knowledge base or domain unambiguous, leading to incorrect or irrelevant context.

Distractors: The FM is not capable of understanding multiple languages in retrieved content.: Multilingual support affects FM response quality, but does not cause context to be pulled from the wrong source.; Context chunks are formatted in XML while the FM expects JSON input.: Format mismatch can cause parsing errors, but not context misrouting.; Vector embeddings are regenerated on every request, adding latency.: Recalculation can cause performance issues but does not change the knowledge base from which data is fetched.

Misconception tags: Confusing context format issues with source-routing issues; Misattributing FM limitations to retrieval system problems

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order010-basic-rag-design.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day-02-answer-guidance.md

### P1-AIP-D2-115

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-115 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.6: Create consistent access mechanisms to enable seamless integration with FMs (for example, by using function calling interfaces for vector search, Model Context Protocol [MCP] clients for vector queries, standardized API patterns for retrieval augmentation). |
| `secondary_exam_skills` | Skill 1.1.1: Create comprehensive architectural designs that align with specific business needs and technical constraints (for example, by using appropriate FMs, integration patterns, deployment strategies). |
| `learning_unit` | Day02-order010 |
| `accelerated_day` | Day 2 |
| `topic` | Basic Retrieval-Augmented Generation |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Strategic |
| `question_format` | multiple-response |
| `difficulty` | hard |
| `cognitive_demand` | judge |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T060928Z-openai-gpt-4.1-day-02-order010-top-up-4.md item 3 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T060928Z |
| `raw_run_id` | order010-top-up-4 |

Stem:

A retailer’s RAG pipeline for product information must support consistent, adaptable access as new document types and knowledge repositories are added. Which architectural practices best enable ongoing extensibility while minimizing disruptions? (Select TWO.)

Options:

1. Use versioned, well-documented retrieval APIs to abstract vector store implementations.
2. Directly embed connection credentials to all knowledge sources within the FM prompt.
3. Implement modular adapters for new repository types following a common interface.
4. Hardcode repository identifiers in each retrieval call.
5. Design retrieval callbacks to return standardized context objects regardless of underlying source.

Correct answer: Use versioned, well-documented retrieval APIs to abstract vector store implementations.; Implement modular adapters for new repository types following a common interface.

Rationale: Versioned APIs and modular adapters enable extension and replacement of retrieval or storage backends without impacting existing integrations, supporting continuous evolution.

Distractors: Directly embed connection credentials to all knowledge sources within the FM prompt.: This is insecure and not extensible, creating a maintenance and security risk.; Hardcode repository identifiers in each retrieval call.: Hardcoding ties logic to current state, causing breakage or costly updates as repositories change.; Design retrieval callbacks to return standardized context objects regardless of underlying source.: While important for downstream consistency, this alone does not address extensibility in adapting to new repositories.

Misconception tags: Ignoring extensibility for operational ease; Overvaluing prompt-based dynamic connection

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order010-basic-rag-design.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order010-basic-rag-design.md

### P1-AIP-D2-116

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-116 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.5: Design retrieval mechanisms for FM augmentation. |
| `exam_skill` | Skill 1.5.6: Create consistent access mechanisms to enable seamless integration with FMs (for example, by using function calling interfaces for vector search, Model Context Protocol [MCP] clients for vector queries, standardized API patterns for retrieval augmentation). |
| `secondary_exam_skills` | Skill 1.1.1: Create comprehensive architectural designs that align with specific business needs and technical constraints (for example, by using appropriate FMs, integration patterns, deployment strategies). |
| `learning_unit` | Day02-order010 |
| `accelerated_day` | Day 2 |
| `topic` | Basic Retrieval-Augmented Generation |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Strategic |
| `question_format` | multiple-choice |
| `difficulty` | exam-plus |
| `cognitive_demand` | optimize |
| `estimated_time_seconds` | 180 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T060928Z-openai-gpt-4.1-day-02-order010-top-up-4.md item 4 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T060928Z |
| `raw_run_id` | order010-top-up-4 |

Stem:

A legal team requires that every FM response from a RAG-enabled assistant contains not just the relevant answer, but also supporting source citations extracted from multiple underlying repositories. What retrieval architecture best enforces this requirement in production while minimizing business risk and future maintenance burden?

Options:

1. Implement a context assembly layer that tags each chunk with its source metadata and enforces standardized citation in the assembled FM prompt.
2. Rely on the FM’s own language capabilities to infer citations from context, trusting natural language output.
3. Add manual post-processing logic after FM output to search and match cited facts with source repositories.
4. Embed all possible source references in every prompt, letting the FM choose what to cite.

Correct answer: Implement a context assembly layer that tags each chunk with its source metadata and enforces standardized citation in the assembled FM prompt.

Rationale: Only an explicit context assembly layer can guarantee structured, reliable citation for each fragment—avoiding user-driven errors, future drift, and audit gaps.

Distractors: Rely on the FM’s own language capabilities to infer citations from context, trusting natural language output.: It is unreliable to expect an FM to consistently infer all citation needs without programmatic enforcement.; Add manual post-processing logic after FM output to search and match cited facts with source repositories.: Post-processing is brittle and costly—matching after-the-fact is operationally risky and error-prone.; Embed all possible source references in every prompt, letting the FM choose what to cite.: This creates overwhelming and inconsistent prompts for the FM, which can lead to hallucinations or missing citations.

Misconception tags: Trusting model natural language output for policy compliance; Underestimating the importance of programmatic enforcement

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order010-basic-rag-design.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-02-data-embeddings-vector-stores-rag.md

### P1-AIP-D2-117

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-117 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.3: Implement data validation and processing pipelines for FM consumption. |
| `exam_skill` | Skill 1.3.2: Create data processing workflows to handle complex data types including text, image, audio, and tabular data with specialized processing requirements for FM consumption (for example, by using Amazon Bedrock multimodal models, SageMaker Processing, AWS Transcribe, advanced multimodal pipeline architectures). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day02-order002 |
| `accelerated_day` | Day 2 |
| `topic` | Text, image, audio, and tabular-data preprocessing |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | hard |
| `cognitive_demand` | diagnose |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T060943Z-openai-gpt-4.1-day-02-order002-top-up-3.md item 1 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T060943Z |
| `raw_run_id` | order002-top-up-3 |

Stem:

An AI team is seeing inconsistent foundation model outputs when dynamically merging tabular sales data with product catalog images as input to a Bedrock multimodal pipeline. The same table appears with different column orders in CSV files, and some images lack metadata. The FM response quality for certain products fluctuates as a result. What is the most likely root cause of this performance degradation?

Options:

1. Inconsistent input data ordering and missing image metadata are leading to unreliable feature extraction and context loss during preprocessing.
2. The foundation model API limit has been exceeded, resulting in dropped inputs during batch processing.
3. The images are in unsupported file formats and cause the FM to ignore them entirely.
4. The tabular data should be stored in a relational database before processing to ensure data integrity.

Correct answer: Inconsistent input data ordering and missing image metadata are leading to unreliable feature extraction and context loss during preprocessing.

Rationale: The inconsistent column ordering in tabular data and lack of image metadata can generate context misalignment or missing features during preprocessing, which undermines the FM's ability to merge information accurately across modalities.

Distractors: The foundation model API limit has been exceeded, resulting in dropped inputs during batch processing.: API rate limiting could drop requests, but the symptom here is input ordering and metadata variation, not API throttling.; The images are in unsupported file formats and cause the FM to ignore them entirely.: Unsupported formats would consistently cause missing image data, but the scenario mentions inconsistent—not missing—image context, which points to metadata issues, not outright format rejection.; The tabular data should be stored in a relational database before processing to ensure data integrity.: Storing tabular data in a database may help with integrity, but the pipeline described merges files on the fly; the real issue is not data storage method but input ordering and metadata loss.

Misconception tags: Overlooking ordering and metadata alignment; Attributing causality to model capability or API limits

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order002-multimodal-data-preprocessing.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order002-multimodal-data-preprocessing.md

### P1-AIP-D2-118

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-118 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.3: Implement data validation and processing pipelines for FM consumption. |
| `exam_skill` | Skill 1.3.2: Create data processing workflows to handle complex data types including text, image, audio, and tabular data with specialized processing requirements for FM consumption (for example, by using Amazon Bedrock multimodal models, SageMaker Processing, AWS Transcribe, advanced multimodal pipeline architectures). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day02-order002 |
| `accelerated_day` | Day 2 |
| `topic` | Text, image, audio, and tabular-data preprocessing |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Conditional |
| `question_format` | multiple-choice |
| `difficulty` | medium |
| `cognitive_demand` | select |
| `estimated_time_seconds` | 120 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T060943Z-openai-gpt-4.1-day-02-order002-top-up-3.md item 2 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T060943Z |
| `raw_run_id` | order002-top-up-3 |

Stem:

A retailer wants to use a Foundation Model to generate product descriptions from item specifications (tabular data), product images, and customer review audio snippets. The reviews are recorded by field reps using different smartphone apps, resulting in a variety of file formats and quality levels. What is the most important data preprocessing action to ensure the FM can use the review audio data effectively?

Options:

1. Normalize all audio files to a standard format and bitrate before transcription.
2. Group review audio files by field rep ID prior to processing.
3. Attach product images as base64-encoded strings to the tabular item data before FM ingest.
4. Use sentiment analysis models on the raw audio files before sending them to the FM.

Correct answer: Normalize all audio files to a standard format and bitrate before transcription.

Rationale: Audio normalization ensures that disparate inputs are compatible with downstream transcription services and the FM, mitigating quality and format variation that would otherwise degrade transcription and feature integration.

Distractors: Group review audio files by field rep ID prior to processing.: Grouping by field rep might help for analytics, but it does not address the audio quality and format inconsistencies central to preprocessing.; Attach product images as base64-encoded strings to the tabular item data before FM ingest.: While useful for image ingestion, this doesn't resolve the core challenge of audio preprocessing for transcription.; Use sentiment analysis models on the raw audio files before sending them to the FM.: Applying sentiment models directly to raw, unnormalized audio risks poor results due to format and quality variations, and typically raw audio must be transcribed and preprocessed first.

Misconception tags: Focusing on model usage over input normalization; Confusing grouping for preprocessing

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order002-multimodal-data-preprocessing.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order002-multimodal-data-preprocessing.md

### P1-AIP-D2-119

| Field | Value |
|---|---|
| `item_id` | P1-AIP-D2-119 |
| `status` | reviewed |
| `official_exam_code` | AIP-C01 |
| `exam_domain` | Content Domain 1: Foundation Model Integration, Data Management, and Compliance |
| `exam_task` | Task 1.3: Implement data validation and processing pipelines for FM consumption. |
| `exam_skill` | Skill 1.3.2: Create data processing workflows to handle complex data types including text, image, audio, and tabular data with specialized processing requirements for FM consumption (for example, by using Amazon Bedrock multimodal models, SageMaker Processing, AWS Transcribe, advanced multimodal pipeline architectures). |
| `secondary_exam_skills` | None. |
| `learning_unit` | Day02-order002 |
| `accelerated_day` | Day 2 |
| `topic` | Text, image, audio, and tabular-data preprocessing |
| `knowledge_category` | Knowledge; Skill |
| `knowledge_type` | Conceptual; Procedural; Conditional |
| `question_format` | multiple-response |
| `difficulty` | hard |
| `cognitive_demand` | judge |
| `estimated_time_seconds` | 150 |
| `last_reviewed` | 2026-06-23 |
| `source_trace_status` | needs-final-source-check |
| `raw_source` | 2026-06-23T060943Z-openai-gpt-4.1-day-02-order002-top-up-3.md item 3 |
| `raw_provider` | openai |
| `raw_model` | gpt-4.1 |
| `raw_created_utc` | 2026-06-23T060943Z |
| `raw_run_id` | order002-top-up-3 |

Stem:

A legal AI assistant is being designed to answer questions based on court transcripts (text), evidence images (JPEG/PNG), and time-stamped call logs (tabular data). The solution must prevent bias or omission due to inconsistent data quality and maximize reliability for downstream FM-driven analysis. Which TWO preprocessing controls best address these requirements?

Options:

1. Implement schema validation and type-checking for tabular call logs before ingestion.
2. Apply image resolution checks and standardize color profiles for evidence images.
3. Randomly sample 10% of transcripts for manual review after ingestion.
4. Augment images using synthetic overlays before FM embedding.
5. Re-sort the transcript text chronologically with automated timestamp alignment.

Correct answer: Implement schema validation and type-checking for tabular call logs before ingestion.; Apply image resolution checks and standardize color profiles for evidence images.

Rationale: Schema validation for tabular data and standardizing image quality help address inconsistencies that introduce bias or omissions in downstream FM analysis, promoting reliable context integration.

Distractors: Randomly sample 10% of transcripts for manual review after ingestion.: Sampling may help global QA but isn't a preprocessing control: it doesn't guarantee bias is prevented for unreviewed data or automate quality enforcement.; Augment images using synthetic overlays before FM embedding.: Augmenting with synthetic overlays could introduce new bias or distort evidence; it doesn't enforce quality consistency.; Re-sort the transcript text chronologically with automated timestamp alignment.: Chronologically sorting may help some applications, but unless the transcript is out of order, it does not directly address bias or data quality defects in the raw sources.

Misconception tags: Overreliance on manual sampling or postprocessing; Applying augmentation without quality control

Source trace:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order002-multimodal-data-preprocessing.md

Remediation target:

docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/day02-order002-multimodal-data-preprocessing.md

## Culled Items

| Raw source | Curriculum order | Stem excerpt | Reasons | Evidence |
|---|---|---|---|---|
| `2026-06-23T051527Z-openai-gpt-4.1-day-02-order001.md item 2` | Day02-order001 | An enterprise is building an ingestion pipeline for financial transaction data intended for use with an LLM via Amazon Bedrock. The team ... | keyword-trivia stem, stale or risky technical claim | keyword-trivia stem: matched weak stem pattern(s): which aws service; stem="An enterprise is building an ingestion pipeline for financial transaction data intended for use with an LLM via Amazon Bedrock. The team must implement automated monitoring to detect and alert on data anomalies, such as unexpected nulls and distribution shi..."<br>stale or risky technical claim: pattern=sagemaker studio classic; excerpt="e data quality integrated with amazon cloudwatch metrics aws lambda and step functions state machine for anomaly detection amazon sagemaker studio classic data profiler custom cloudwatch alarms configured on s3 putobject events aws glue data quality integrated with amazon clou..." |
| `2026-06-23T051621Z-openai-gpt-4.1-day-02-order002.md item 2` | Day02-order002 | A data scientist is designing a pipeline to convert podcast audio files into text summaries using an FM. What is the most suitable servic... | keyword-trivia stem | keyword-trivia stem: matched weak stem pattern(s): what is the most suitable service; stem="A data scientist is designing a pipeline to convert podcast audio files into text summaries using an FM. What is the most suitable service to use for automated audio-to-text conversion in this workflow?" |
| `2026-06-23T051621Z-openai-gpt-4.1-day-02-order002.md item 3` | Day02-order002 | A data engineering team must preprocess a diverse dataset comprising text documents, medical x-ray images, and call center audio recordin... | keyword-trivia stem | keyword-trivia stem: matched weak stem pattern(s): which aws service; stem="A data engineering team must preprocess a diverse dataset comprising text documents, medical x-ray images, and call center audio recordings for an FM-enabled analytics system. Which AWS services and architectural components should be included to handle prep..." |
| `2026-06-23T051621Z-openai-gpt-4.1-day-02-order002.md item 8` | Day02-order002 | You are building a pipeline to process incoming video files and need to extract both audio and image frames for FM-based content analysis... | unsupported high-risk claim | unsupported high-risk claim: pattern=frame extraction; excerpt="t analysis. which service combination will meet the preprocessing requirements most efficiently? use amazon rekognition for image frame extraction and aws transcribe for audio transcription. use amazon polly for audio extraction and aws glue for image extraction. use aws tran" |
| `2026-06-23T051804Z-openai-gpt-4.1-day-02-order004.md item 3` | Day02-order004 | You are tasked with deploying a cross-lingual semantic search system using an Amazon Bedrock embedding model. What limitation must you mo... | unsupported high-risk claim | unsupported high-risk claim: pattern=true bedrock model multilingual support limitations; excerpt="bedrock & titan embeddings multilingual capabilities documentation scenario: multilingual system design; reviewer should confirm true bedrock model multilingual support limitations." |
| `2026-06-23T051804Z-openai-gpt-4.1-day-02-order004.md item 4` | Day02-order004 | An e-learning company needs to batch generate vector embeddings for newly uploaded course transcripts. Which AWS service combination best... | keyword-trivia stem | keyword-trivia stem: matched weak stem pattern(s): which aws service; stem="An e-learning company needs to batch generate vector embeddings for newly uploaded course transcripts. Which AWS service combination best automates this embedding workflow for scale and flexibility?" |
| `2026-06-23T052016Z-openai-gpt-4.1-day-02-order007.md item 11` | Day02-order007 | Your product search platform needs to perform hybrid searches that blend both semantic and keyword search capabilities. Which AWS solutio... | unsupported high-risk claim | unsupported high-risk claim: pattern=hybrid support is current; excerpt="-guides/day-02-data-embeddings-vector-stores-rag.md hybrid search is a common requirement. reviewer must ensure neural/opensearch hybrid support is current." |
| `2026-06-23T052302Z-openai-gpt-4.1-day-02-order010.md item 1` | Day02-order010 | A team is building an enterprise Q&A system on AWS. They need to ensure that their Foundation Model only receives the most relevant conte... | unsupported high-risk claim | unsupported high-risk claim: pattern=mcp; excerpt="r retrieving contextual information for the fm through api integration? configure the solution to use the model context protocol (mcp) client to orchestrate vector queries and return top-k context chunks through a standardized api. add a lambda function that scra" |
| `2026-06-23T052302Z-openai-gpt-4.1-day-02-order010.md item 5` | Day02-order010 | A developer needs to design a RAG solution integrating with Amazon Bedrock and a managed vector store. The business case requires minimal... | unsupported high-risk claim | unsupported high-risk claim: pattern=function calling; excerpt="se requires minimal custom code for context retrieval and high developer productivity. which approach best achieves this? use the function calling interface supported by bedrock, connecting to the managed vector store using a standardized api pattern. build a custom context r" |
| `2026-06-23T052302Z-openai-gpt-4.1-day-02-order010.md item 7` | Day02-order010 | A company is designing a RAG workflow to support product-question answering using Bedrock and its managed Knowledge Base. Which options a... | unsupported high-risk claim | unsupported high-risk claim: pattern=mcp; excerpt="etrieval system? (select two.) leverage bedrock’s function-calling interface to obtain top relevant chunks for the fm prompt. use mcp-compliant clients to abstract vector queries and standardize data flow to the fm. allow the fm to parse entire document sets dire"; pattern=function calling; excerpt="cts/day02-order010-basic-rag-design.md tests multiple integration best-practices. reviewer to check current documentation for mcp/function calling support." |
| `2026-06-23T052302Z-openai-gpt-4.1-day-02-order010.md item 10` | Day02-order010 | A customer’s RAG deployment yields inconsistent results. Sometimes the FM answers correctly, but at other times it ignores highly relevan... | unsupported high-risk claim | unsupported high-risk claim: pattern=function calling; excerpt="s. vector search retrieves too many irrelevant chunks due to poor query tuning. the fm’s underlying architecture does not support function calling. apis return results in json format, which the fm cannot interpret. document embeddings are generated using inconsistent preproce" |
| `2026-06-23T052302Z-openai-gpt-4.1-day-02-order010.md item 11` | Day02-order010 | While supporting multiple RAG client applications, a central platform team needs all integrations to be reliable and future-proof. Which ... | unsupported high-risk claim | unsupported high-risk claim: pattern=mcp; excerpt="ration. embed all vector store credentials within the fm prompt for dynamic connection. require retrieval endpoints to conform to mcp protocol for all client integrations. standardize api contract for retrieval callbacks regardless of fm implementation.; require"; pattern=function calling; excerpt="d couples retrieval handlers too closely with fms.; use only function-calling-compatible interfaces for retrieval orchestration.: function calling is useful, but protocol-enforced compatibility brings more reliability across fms.; embed all vector store credentials within the" |
