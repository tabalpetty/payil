# Pilot1 AIP-C01 Accelerated Path Design

## Purpose

This document defines the design rules for the Pilot1 AIP-C01 accelerated path.
The companion file, [accelerated-7-day-plan.md](accelerated-7-day-plan.md),
turns these rules into a daily schedule.

The accelerated path is not a shorter beginner course. It is a high-intensity
conversion path for a learner who already has enough technical foundation to
learn AIP-C01-specific GenAI, AWS, integration, governance, operations, and exam
reasoning quickly.

The path may compress calendar time and reduce repetition on already-mastered
material. It must not compress away the knowledge types that make the exam
professional-level:

- conceptual models;
- procedural implementation ability;
- conditional and strategic decision-making;
- safety, security, and governance judgment;
- operational and diagnostic reasoning;
- exam-format fluency.

## Target Learner Profile

The accelerated learner should already have most of the following:

| Prior capability | Expected starting point |
|---|---|
| AWS fundamentals | Understands IAM, compute, storage, networking, APIs, monitoring, logging, and cost at a working level. |
| Application architecture | Can reason about synchronous, asynchronous, streaming, event-driven, and API-based systems. |
| Data systems | Understands structured and unstructured data, metadata, data quality, indexing, synchronization, and basic search concepts. |
| Security basics | Understands authentication, authorization, least privilege, encryption, secrets, network boundaries, and auditability. |
| Operations | Can interpret logs, metrics, traces, latency, throughput, errors, retries, throttling, and incidents. |
| AI/ML or GenAI baseline | Has enough familiarity with models, inference, prompts, embeddings, evaluation, and model limitations to learn quickly. |
| Learning maturity | Can learn from dense material, repair gaps independently, and tolerate scenario-based ambiguity. |

If the learner lacks several of these, the self-paced path is the safer default.

## Entry Diagnostic

Before starting the 7-day path, the learner should complete an entry diagnostic.
The goal is not to produce a final score. The goal is to decide whether the
learner can safely enter the accelerated route and which gaps must be repaired
immediately.

### Diagnostic Sections

| Section | Knowledge types tested | Evidence required | Accelerated-route decision |
|---|---|---|---|
| AWS platform baseline | Declarative, conceptual, conditional | Classify services and choose basic AWS patterns for scenarios. | Severe gaps require prerequisite repair before Day 1. |
| API and application integration | Conceptual, procedural, conditional | Explain request/response, async, streaming, retry, timeout, and failure-handling patterns. | Gaps become Day 3 and Day 4 risk items. |
| Data and retrieval baseline | Conceptual, causal, procedural | Explain chunking, metadata, embeddings, search, synchronization, and retrieval failure modes. | Severe gaps require Day 2 expansion. |
| Security and governance baseline | Normative, institutional, conditional | Map access, data protection, logging, audit, ownership, and approval responsibilities. | Severe gaps require Day 5 expansion and cross-day reminders. |
| Operations and troubleshooting | Causal, diagnostic, strategic | Interpret symptoms, identify evidence, propose likely causes, and define prevention. | Severe gaps require Day 6 expansion. |
| Exam-style reasoning | Conditional, strategic, metacognitive | Answer scenario questions, reject distractors, state assumptions, and classify misses. | Weak performance requires daily timed practice from Day 1. |

### Diagnostic Output

The learner should produce a one-page readiness note:

- `Enter accelerated path`: prerequisites are strong enough.
- `Enter with warnings`: path is possible, but named gap areas must be remediated
  during the week.
- `Use self-paced path`: prerequisite gaps are too large for a reliable 7-day
  attempt.

The note should identify:

- top three risk areas;
- required Day 1 or Day 2 repairs;
- whether extra evening remediation time is needed;
- whether the learner should delay scheduling the exam.

## Non-Skippable Foundations

Even in the accelerated path, the following foundations must be taught or
verified. They are load-bearing: later decisions depend on them.

| Foundation | Why it cannot be skipped | Primary teaching method |
|---|---|---|
| AIP-C01 service and system map | The learner must place services, controls, data flows, and responsibilities in the right part of the architecture. | Concept map reconstruction and service-role classification. |
| Foundation model behavior | Model limits, parameters, context, output variation, and inference behavior affect every later design choice. | Diagram, prediction, short experiments, and retrieval practice. |
| Prompt and output control baseline | Prompt design, templates, structured output, and regression examples appear across integration, safety, and evaluation. | Worked examples, contrastive prompt repair, and mini regression set. |
| Data quality and retrieval basics | RAG, embeddings, metadata, chunking, and vector stores are central to the largest domain area. | RAG flow diagram, chunking decision cases, and retrieval failure diagnosis. |
| Security boundary model | IAM, network, data, model, tool, and application boundaries are cross-cutting. | Threat-model sketch and control placement exercise. |
| Governance and evidence model | Professional GenAI systems require ownership, policy mapping, traceability, audit evidence, and human oversight. | Policy-to-control mapping and stakeholder responsibility exercise. |
| Operational signals | Cost, latency, throughput, quality, drift, hallucination, retrieval health, and tool failures must be observable. | Dashboard design, symptom-to-signal mapping, and incident reconstruction. |
| Exam scenario reasoning | AIP-C01 readiness requires choosing among plausible options under constraints. | Timed scenarios, distractor rejection, and structured error analysis. |

## Acceleration Rules

The path accelerates by changing delivery intensity, not by lowering the
capability standard. Complete and wholesome learning remains the intent in both
the self-paced and accelerated routes.

Six active learning hours is a floor, not a promise that every day fits neatly
inside six hours. Dense days may reasonably require seven to eight hours. If a
topic needs more time than the accelerated day can responsibly hold, the course
should still provide the learning material and explicitly label the topic as
requiring extra remediation time or self-paced continuation.

### What Can Be Compressed

- introductory explanations when the diagnostic shows prior mastery;
- long-form beginner readings;
- repeated practice on already-mastered declarative material;
- isolated service tours that do not connect to AIP-C01 decisions;
- optional enrichment that does not support exam or professional performance.

### What Cannot Be Compressed Away

- the first correct mental model of a GenAI application on AWS;
- teaching material needed to complete a required learner artifact;
- at least one meaningful RAG/data design artifact;
- at least one integration/resilience decision artifact;
- at least one safety, security, and governance control artifact;
- at least one operations and troubleshooting artifact;
- knowledge-type-matched activities, including configuration inspection for
  embedded knowledge and diagnostic work for troubleshooting knowledge;
- timed exam practice with error analysis;
- remediation of severe gaps in safety, security, governance, retrieval,
  integration, or troubleshooting.

### When A Topic Does Not Fit The Accelerated Day

Do not delete or thin the topic to preserve the calendar. Instead:

- create the full material required for mastery;
- state the expected extra time or prerequisite assumption;
- mark whether the topic is completed in-session, completed as evening
  extension, or carried into self-paced remediation;
- preserve the same assessment and remediation expectations.

## Method Mix By Knowledge Type

Each day should include several teaching modes. The dominant mode changes with
the day, but the path should never become seven days of reading and quizzes.

| Knowledge need | Accelerated teaching method | Evidence |
|---|---|---|
| Declarative | Retrieval cards, short closed-book quizzes, service-role classification. | Accurate recall without notes and correct service placement. |
| Conceptual | System maps, diagrams, comparison tables, teach-back. | Reconstructs the model and explains relationships. |
| Procedural | Guided inspection, minimal labs, partially completed examples, implementation sketches. | Performs or correctly specifies the workflow. |
| Conditional | Contrasting scenarios and choose-or-reject exercises. | Selects an option and rejects alternatives with rationale. |
| Causal and diagnostic | Failure injection, symptom tables, trace/log/metric interpretation. | Identifies likely cause, evidence, fix, and prevention. |
| Strategic | Architecture decision records, tradeoff reviews, changed-constraint scenarios. | Defends a coherent approach under ambiguity. |
| Normative and institutional | Policy-to-control mapping, RACI, mock audit evidence. | Names owners, controls, evidence, residual risk, and escalation. |
| Metacognitive | Confidence marking, error log, miss classification, remediation plan. | Explains why misses happened and what will change. |

## Daily Teaching Pattern

Every accelerated day should follow the same broad learning rhythm while
changing the content and dominant method.

| Stage | Time box | Purpose | Typical method |
|---|---:|---|---|
| Diagnostic warm-up | 15-20 min | Surface prior knowledge and yesterday's unresolved gaps. | Retrieval, confidence marking, short scenarios. |
| Mental model build | 60-90 min | Establish the day's conceptual frame. | Diagram, comparison, self-explanation, teach-back. |
| Applied work | 90-120 min | Convert the model into usable procedure or design. | Lab, walkthrough, configuration review, artifact creation. |
| Scenario judgment | 60-90 min | Practise conditional and strategic choices. | Contrasting cases, decision record, tradeoff defense. |
| Failure or governance pass | 30-60 min | Add safety, operations, diagnostic, or governance depth. | Threat model, control mapping, incident analysis. |
| Timed exam practice | 30-60 min | Build format fluency and coverage awareness. | Tagged question set. |
| Error analysis and carryover | 30-45 min | Convert misses into tomorrow's remediation plan. | Error log and gap-specific remediation. |

## Remediation Rules

Accelerated remediation must be targeted. Repeating the same material is not
enough.

| Gap type | Symptom | Remediation |
|---|---|---|
| Recall gap | Learner recognizes a term but cannot produce it or place it. | Retrieval cards, compact reference, closed-book retry. |
| Conceptual gap | Learner memorizes parts but cannot explain relationships. | Rebuild diagram, compare adjacent concepts, teach-back. |
| Procedural gap | Learner understands the idea but cannot perform or specify the workflow. | Worked example, guided completion, independent variant. |
| Conditional gap | Learner knows options but chooses the wrong one for constraints. | Contrasting cases and forced rejection of alternatives. |
| Causal gap | Learner knows symptoms but cannot explain mechanism. | Predict-observe-explain and cause/evidence table. |
| Diagnostic gap | Learner jumps to fixes without evidence. | Incident reconstruction and evidence-first root cause analysis. |
| Governance gap | Learner names controls but omits owner, evidence, approval, or residual risk. | Policy-to-control-to-evidence map and RACI repair. |
| Metacognitive gap | Learner is overconfident or cannot explain misses. | Confidence calibration and miss taxonomy review. |

## Go/No-Go Rules

At the end of Day 7, the learner receives one of three decisions.

| Decision | Criteria |
|---|---|
| `Ready` | Meets the simulated exam score, domain minimum, timing, artifact, and error-analysis gates. |
| `Remediate` | Has localized gaps that can be repaired with targeted work before scheduling or attempting the exam. |
| `Do not schedule` | Has major gaps in retrieval, integration, safety/security/governance, operations, troubleshooting, or scenario reasoning. |

The accelerated path should be honest. A learner who completes seven intense
days but cannot meet the gates should not be declared ready.

## Relationship To Other Pilot1 Artifacts

- The accelerated path uses the same source identity and traceability standards
  as the self-paced route.
- The accelerated path uses the same mastery standard as the self-paced route.
- The 7-day calendar plan is a schedule view of this design.
- Exam-prep materials support the path but do not replace teaching materials.
- Teacher and student kits should mark whether each unit is used in the
  self-paced path, the accelerated path, or both.
