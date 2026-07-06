# Pilot1 AIP-C01 Accelerated 7-Day Plan

## Purpose

This is the first Pilot1 curriculum path. It defines a compressed route for
preparing for **AWS Certified Generative AI Developer - Professional
(AIP-C01)**.

Use this calendar plan together with
[accelerated-path-design.md](accelerated-path-design.md), which defines the
learner assumptions, entry diagnostic, non-skippable foundations, compression
rules, remediation model, and go/no-go criteria for the accelerated route.

The plan is not a beginner route. It assumes the learner is already technically
mature and can spend a concentrated week converting existing AWS, software,
data, or AI/ML experience into AIP-C01-specific performance.

## Suitability Warning

Use this route only if all of the following are true:

- You can commit at least six hours of active learning per day for seven days,
  with the expectation that dense days may require seven to eight hours.
- You have prior experience building or operating production-grade
  applications on AWS or comparable open-source/cloud technologies.
- You understand basic AWS compute, storage, networking, IAM, monitoring, and
  cost concepts.
- You have at least general familiarity with APIs, JSON, event-driven systems,
  CI/CD, logs, metrics, and troubleshooting.
- You have enough AI/ML or data experience to learn GenAI-specific systems
  quickly.
- You can work through dense professional-level material without extensive
  handholding.

This route compresses calendar time. It does not lower teaching quality,
mastery gates, source-traceability requirements, or exam-readiness standards.
If a topic requires more time than the accelerated day can reasonably hold, the
material is still created and the plan must call out the extra time,
remediation, or self-paced continuation required.

## Time Budget

Minimum daily commitment:

```text
6 active learning hours/day x 7 days = 42 active hours
```

Expected range:

```text
6-8 active learning hours/day depending on diagnostic gaps and topic density
```

Recommended daily shape:

| Block | Duration | Purpose |
|---|---:|---|
| Teach and map | 90 min | Build or repair the mental model for the day's domains. |
| Build or inspect | 120 min | Complete a lab, design sketch, configuration review, or guided implementation. |
| Scenario judgment | 90 min | Work through professional scenario decisions and tradeoffs. |
| Exam practice | 45 min | Timed questions tagged to the day's domains. |
| Error analysis | 45 min | Record misses, causes, remediation, and next-day carryover. |

## Readiness Gates

The learner is not ready merely because seven days have elapsed.

Minimum accelerated-route gates:

- complete every daily artifact;
- remediate all severe gaps in security, safety, governance, integration, RAG,
  and troubleshooting;
- score at least `82%` overall on a full-length simulated exam;
- score at least `72%` in every official domain;
- finish the simulated exam in `170` minutes or less;
- explain why missed or guessed answers were wrong and what knowledge would
  have prevented the miss.

## Official Domain Weighting

| Domain | Weight | Accelerated-route treatment |
|---|---:|---|
| Domain 1: Foundation Model Integration, Data Management, and Compliance | 31% | Heavy coverage on Days 1-3, reinforced throughout. |
| Domain 2: Implementation and Integration | 26% | Heavy coverage on Days 3-4, reinforced in labs and scenarios. |
| Domain 3: AI Safety, Security, and Governance | 20% | Heavy coverage on Day 5, cross-cutting every day. |
| Domain 4: Operational Efficiency and Optimization for GenAI Applications | 12% | Heavy coverage on Day 6, introduced earlier through model and retrieval choices. |
| Domain 5: Testing, Validation, and Troubleshooting | 11% | Heavy coverage on Day 6, exam synthesis on Day 7. |

## Daily Plan

### Day 1: Foundations, AWS GenAI Map, Invocation, And Prompt Baseline

**Purpose:** Establish enough shared language and AWS service orientation to
move quickly into professional-level tasks.

**Primary official coverage:**

- cross-domain prerequisites;
- Domain 1 Task 1.1 and Task 1.2 foundations;
- Domain 1 Task 1.6 prompt foundations;
- Domain 2 Task 2.4 basic FM API integration;
- Domain 2 Task 2.5 basic application integration pattern selection.

**Learning focus:**

- foundation models, inference, customization, and model limits;
- tokens, context windows, temperature, top-k, top-p, and output behavior;
- in-scope AWS service map for GenAI systems;
- Amazon Bedrock invocation shape;
- prompt instructions, templates, structured output, and golden datasets.

**Active work:**

- draw an AIP-C01 GenAI system map;
- classify services by role: model access, retrieval, orchestration, compute,
  storage, observability, security, and governance;
- inspect or perform a basic Bedrock request/response flow;
- create a tiny prompt regression set with expected outputs.

**Quality note:**

Day 1 is foundational. Do not rush past it to protect the calendar. If the
learner cannot explain the system map, invocation path, prompt/output controls,
and evaluation baseline, extend Day 1 or record explicit remediation before
continuing. Later days depend on this mental model.

**Daily artifact:**

- one-page system map plus a minimal invocation and prompt-evaluation record.

**Exit check:**

- explain the difference among model, prompt, retrieval, orchestration,
  application logic, evaluation, and control;
- classify ten service-use scenarios with rationale;
- answer a timed Day 1 practice set and record gaps.

### Day 2: Data Preparation, Vector Stores, Embeddings, And Basic RAG

**Purpose:** Build the retrieval and data foundation that supports the largest
official domain.

**Primary official coverage:**

- Domain 1 Task 1.3;
- Domain 1 Task 1.4;
- Domain 1 Task 1.5.

**Learning focus:**

- data validation workflows for FM consumption;
- text, image, audio, and tabular preprocessing boundaries;
- model-specific input formatting and normalization;
- embeddings and vector similarity;
- chunking, segmentation, metadata, filtering, and vector-store architecture;
- basic semantic retrieval and basic RAG.

**Active work:**

- repair defective records for FM consumption;
- design a metadata schema for a retrieval corpus;
- compare fixed, hierarchical, and semantic chunking decisions;
- sketch or build a basic RAG flow using Bedrock Knowledge Bases or an
  equivalent faithful simulation.

**Quality note:**

Day 2 carries the retrieval foundation for the rest of the course. Do not
compress away data-quality reasoning, chunking tradeoffs, metadata/access
labels, embedding/search behavior, or the basic RAG request path. If the
learner cannot diagnose where a bad RAG answer failed, extend the day or carry
the gap as named remediation.

**Daily artifact:**

- RAG design worksheet with data-quality checks, chunking choice, metadata
  fields, vector-store choice, and retrieval test cases.

**Exit check:**

- defend a chunking, embedding, vector-store, and metadata design for a
  scenario;
- identify where data quality, sync, or retrieval failure would appear;
- answer a timed Day 2 practice set and record gaps.

### Day 3: Advanced Retrieval, Prompt Governance, API Patterns, And Resilience

**Purpose:** Connect retrieval and prompt systems to real application
integration patterns.

**Primary official coverage:**

- Domain 1 Task 1.5 and Task 1.6;
- Domain 2 Task 2.4;
- Domain 2 Task 2.5;
- early Domain 5 troubleshooting signals.

**Learning focus:**

- hybrid search, reranking, query expansion, decomposition, and transformation;
- vector-store ingestion, synchronization, refresh, and maintenance;
- prompt management, versioning, approval, governance, and regression testing;
- synchronous, asynchronous, and streaming FM API integration;
- request validation, response handling, retries, rate limits, timeouts,
  fallbacks, circuit breakers, and graceful degradation.

**Active work:**

- compare retrieval strategies for a scenario with changing constraints;
- design a prompt-management and regression workflow;
- design API behavior for sync, async, and streaming use cases;
- run a failure-mode table for throttling, timeout, malformed response, and
  region/model unavailability.

**Focused-artifact tiering:**

Day 3 contains more focused topics than Days 1 and 2. The tiering below is
pacing guidance, not a quality reduction. All Day 3 topics remain in scope.
Complete the focused Day 3 artifacts as:

- **Core in-session:** order001, order002, order004, order006, order009, order010,
  order012, order013, order016, order017, order018.
- **Guided inspection:** order005, order011, order014, order015.
- **Compressed but assessed:** order003, order007, order008.

This tiering preserves the same mastery standard while preventing the 18-topic
practice layer from silently overrunning the day. If the learner cannot
complete the compressed topics with acceptable self-check evidence, the day
extends toward the seven-to-eight-hour range or those topics become named
remediation carryover. They are not silently skipped.

**Daily artifact:**

- integration decision record covering retrieval, prompt governance, API
  pattern, and resilience decisions.

**Exit check:**

- choose the right integration pattern for five application scenarios;
- explain how failures are detected, retried, routed, or degraded;
- answer a timed Day 3 practice set and record gaps.

### Day 4: Deployment, Model Routing, Enterprise Integration, And Agents

**Purpose:** Cover the implementation-heavy core of the professional exam.

**Primary official coverage:**

- Domain 1 Task 1.2;
- Domain 2 Task 2.1;
- Domain 2 Task 2.2;
- Domain 2 Task 2.3;
- Domain 2 Task 2.5.

**Learning focus:**

- model benchmarking, model selection, routing, cascading, and provider
  switching;
- cross-Region inference, resilience, on-demand, provisioned throughput,
  SageMaker endpoints, and hybrid deployment choices;
- FM customization deployment and lifecycle management;
- enterprise integration, identity federation, RBAC, hybrid/on-premises/edge
  constraints, GenAI gateways, IaC, CI/CD, deployment gates, and rollback;
- function calling, tool schemas, MCP, single-agent workflows, agent memory,
  stopping conditions, human-in-the-loop, and multi-agent tradeoffs.

**Active work:**

- design a model-routing policy for cost, latency, quality, and resilience;
- compare Bedrock, SageMaker AI endpoint, and hybrid deployment choices;
- write a tool schema with parameter validation and authorization boundaries;
- design an agent workflow with stopping conditions and human escalation.

**Daily artifact:**

- model-and-agent implementation architecture with deployment, routing,
  security boundary, and rollback notes.

**Exit check:**

- defend deployment and agent choices under changed requirements;
- identify where tool-use failures and boundary violations occur;
- answer a timed Day 4 practice set and record gaps.

### Day 5: Safety, Security, Privacy, Governance, And Responsible AI

**Purpose:** Make safety and governance operational rather than decorative.

**Primary official coverage:**

- Domain 3 Task 3.1;
- Domain 3 Task 3.2;
- Domain 3 Task 3.3;
- Domain 3 Task 3.4.

**Learning focus:**

- input/output filtering and moderation;
- grounding, factual verification, hallucination reduction, and deterministic
  output controls;
- prompt injection, jailbreaks, adversarial testing, safety classifiers, and
  defense-in-depth architecture;
- VPC endpoints, IAM, granular data access, PII discovery, masking,
  anonymization, redaction, retention, logging privacy, and lifecycle controls;
- data lineage, model cards, audit logging, governance operating models,
  policy-to-control mapping, monitoring, transparency, fairness, and
  regulatory readiness.

**Active work:**

- map an end-to-end threat model for a GenAI application;
- design guardrails and validation checks for unsafe or unsupported outputs;
- write an IAM/data-access control sketch for RAG and agent flows;
- create a policy-to-control mapping and audit evidence checklist.

**Daily artifact:**

- safety, security, and governance control pack for one GenAI scenario.

**Exit check:**

- explain how a prompt injection or data exposure attempt is blocked, detected,
  logged, and remediated;
- identify which controls belong in app logic, IAM, networking, data layer,
  model layer, and governance process;
- answer a timed Day 5 practice set and record gaps.

### Day 6: Cost, Performance, Monitoring, Evaluation, And Troubleshooting

**Purpose:** Build operational judgment and diagnostic fluency.

**Primary official coverage:**

- Domain 4 Task 4.1;
- Domain 4 Task 4.2;
- Domain 4 Task 4.3;
- Domain 5 Task 5.1;
- Domain 5 Task 5.2.

**Learning focus:**

- token estimation, tracking, pruning, compression, response limits, and
  context-window optimization;
- cost-effective model selection, tiered routing, caching, batching,
  throughput, concurrency, capacity planning, provisioned throughput, latency,
  streaming, parallelism, and precomputation;
- retrieval and vector-index performance optimization;
- FM parameter optimization and A/B testing;
- operational metrics, logs, traces, dashboards, token/cost/latency monitoring,
  hallucination/drift monitoring, vector health, tool/agent observability,
  business impact, compliance, and forensic traceability;
- model-output quality metrics, Bedrock Model Evaluations, human evaluation,
  LLM-as-judge, RAG evaluation, agent evaluation, canary tests, regression
  tests, synthetic users, and deployment validation;
- troubleshooting context overflow, API integration, prompt issues, retrieval
  failures, agent/tool issues, cost, latency, throughput, scaling, and
  end-to-end incidents.

**Active work:**

- build a cost-quality-latency decision matrix;
- create a monitoring and evaluation dashboard design;
- diagnose a broken RAG or agent incident from symptoms to root cause;
- write a postmortem with prevention controls.

**Daily artifact:**

- operations and troubleshooting pack: metrics, evaluation harness, incident
  diagnosis, root cause, and prevention plan.

**Exit check:**

- select the best optimization under cost, latency, quality, and compliance
  constraints;
- diagnose five failure scenarios and name the evidence that proves the cause;
- answer a timed Day 6 practice set and record gaps.

### Day 7: Full Integration, Exam Simulation, And Final Remediation

**Purpose:** Convert domain knowledge into integrated professional exam
performance.

**Primary official coverage:**

- all domains;
- cross-domain scenario judgment;
- exam-style timing and remediation.

**Learning focus:**

- end-to-end architecture design;
- business, technical, security, cost, and governance tradeoff analysis;
- architecture decision records;
- production-readiness review;
- mixed-domain AIP-C01 scenario practice.

**Active work:**

- complete one end-to-end GenAI architecture case;
- write and review an architecture decision record;
- complete one timed full-length simulated exam or a staged equivalent if the
  question bank is not yet built;
- perform structured error analysis and targeted remediation.

**Daily artifact:**

- final architecture decision record plus exam-readiness gap report.

**Exit check:**

- meet the accelerated-route readiness gates;
- produce a final go/no-go recommendation:
  - `Ready`: meets score, domain, pacing, and reasoning gates;
  - `Remediate`: localized gaps remain and require targeted work;
  - `Do not schedule`: major domain, implementation, safety, or diagnostic
    gaps remain.

## Question-Prompt Coverage

The attached prompt file supports practice-question gathering for these major
accelerated-path areas:

| Prompt topic | Accelerated-path use |
|---|---|
| Data Preparation | Day 2 |
| Retrieval Augmented Generation | Day 2 and Day 3 |
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

## Added Guardrails

These guardrails are intentionally added beyond a simple calendar plan:

- **No passive-only days.** Every day requires an artifact, scenario judgment,
  timed practice, and error analysis.
- **Security and governance are cross-cutting.** They appear explicitly on Day
  5 but must be considered in every design, integration, and operations day.
- **The 7-day route cannot certify readiness by attendance.** Readiness depends
  on gates, not elapsed time.
- **The question bank is not the curriculum.** Exam prompts support readiness
  practice but do not replace teaching, labs, artifacts, or remediation.
