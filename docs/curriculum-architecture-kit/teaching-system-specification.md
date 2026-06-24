# Teaching System Specification

## Purpose

This specification defines a subject-agnostic method for turning a body of
knowledge into a coherent, multi-method teaching system. It governs curriculum
architecture, teacher materials, student materials, assessment, remediation,
exam preparation where relevant, and validation.

The central design rule is:

> Domain structure determines learning order. Knowledge type determines
> teaching method. Mastery evidence determines progression.

The specification does not prescribe novelty for its own sake. Method variety
must follow the learning need of the unit.

For the multi-agent production implementation of this specification, see
[curriculum-production-agent-architecture.md](curriculum-production-agent-architecture.md).

## 1. Design Axes

Keep the following axes separate. A unit is described across all four rather
than assigned one label from a flat taxonomy.

### 1.1 Cognitive function

| Type | Learner capability |
|---|---|
| Declarative | Recall facts, terms, rules, and propositions. |
| Conceptual | Explain relationships, categories, models, and frameworks. |
| Procedural | Execute a method, technique, or skill. |
| Conditional or contextual | Select when and where an approach applies. |
| Causal or mechanistic | Explain, predict, and manipulate system behavior. |
| Strategic | Frame problems, plan, prioritize, and adapt an approach. |
| Metacognitive | Monitor and regulate one's own understanding and performance. |
| Normative or ethical | Judge what ought to be done amid competing values. |
| Social or relational | Locate and coordinate relevant expertise or authority. |

### 1.2 Representation and locus

| Type | Where or how the knowledge exists |
|---|---|
| Explicit | Codified in language, diagrams, procedures, or records. |
| Tacit | Present in judgment that cannot be fully articulated. |
| Implicit | Expressed as automatic patterns or habits. |
| Embodied | Grounded in perception and physical coordination. |
| Embedded | Encoded partly in tools, platforms, configurations, or workflows. |
| Collective or institutional | Distributed across people, roles, policies, systems, and practices. |

### 1.3 Subject domain

The subject-domain axis identifies the field in which the knowledge is used.
It may include several interacting domains. Domain labels describe content,
not cognitive function.

### 1.4 Proficiency

| Level | Observable behavior |
|---|---|
| Awareness | Recognizes relevant terms, objects, and situations. |
| Foundational | Explains core ideas and completes simple bounded work. |
| Competent | Performs standard work with limited guidance. |
| Proficient | Selects, adapts, and defends approaches under varied conditions. |
| Expert | Handles ambiguity, diagnoses novel problems, and creates reusable patterns. |

These are reference levels. A project may rename or refine them, but must use
observable behavior rather than time spent or content completed.

## 2. Curriculum Architecture Process

Apply these stages in order. Revisit earlier stages when implementation
reveals a mistaken assumption.

1. Define the mission, learner population, domain boundaries, and target uses.
2. Inventory source objectives and required real-world capabilities.
3. Decompose the domain into observable learning capabilities.
4. Record hard and soft prerequisites with reasons.
5. Build the dependency graph and derive a defensible learning order.
6. Group capabilities into coherent, teachable learning units.
7. Set the required proficiency and mastery evidence for each unit.
8. Classify each unit across the four design axes.
9. Select primary and supporting teaching methods.
10. Create aligned teacher and student packages.
11. Define supported pacing tracks and their learner assumptions.
12. Design assessment, gap diagnosis, remediation, and reassessment.
13. If the program prepares learners for an external exam, design the
    exam-readiness layer from the official exam specification.
14. Validate a complete pilot before scaling the curriculum.
15. Capture reusable lessons, mistakes, remediations, and efficiencies in the
    kit lessons-learned register.

### 2.0 Source identity tooling rule

Before source extraction or syllabus decomposition, confirm source identity in
a dedicated upstream checkpoint. Tooling for this checkpoint may be interactive,
but it must preserve the trust boundary:

- the browser or client collects intent, displays evidence, and records human
  confirmation;
- the server or trusted backend fetches official sources, follows redirects,
  computes checksums, extracts metadata, compares claims, and writes the
  canonical checkpoint;
- local browser storage is for transparent drafts only, not authoritative
  source truth;
- service-worker caching should be limited to the app shell and non-sensitive
  static assets unless the user explicitly opts in;
- browser permissions should be avoided unless a user action clearly requires
  them.

For a cautious user, a curriculum source-identity tool should not unexpectedly
ask for push notifications, file-system access, background sync, persistent
storage, or clipboard access. Prefer in-app polling or server-sent events for
job progress before using browser push. If push or real-time sync is added, it
should support a clear asynchronous or multi-user need rather than be enabled
by default.

The checkpoint output must clearly say whether the source is approved,
rejected, or still needs review. Do not start extraction or decomposition from
an unapproved source unless the risk is explicit and recorded.

### 2.0.1 Source-to-decomposition coverage rule

After faithful source extraction and before downstream generation, run a
source-to-decomposition coverage audit. The audit must compare the official
source hierarchy against the curriculum decomposition and show, for each
official objective, whether it is covered, intentionally deferred, or missing.

For external exams or standards, audit at the deepest official objective level
the curriculum will claim, such as domain, task, skill, subskill, standard, or
rubric criterion. Do not rely on day-level summaries alone when downstream
artifacts will tag finer-grained objectives.

The coverage audit should produce both a human-readable report and a
machine-readable result. Treat it as a blocking gate when:

- an official objective is neither covered nor explicitly deferred;
- a curriculum topic has no source-objective trace;
- a deferral lacks a reason and planned handling path;
- downstream topic briefs, prompts, assessments, or remediation would need to
  invent official objective tags after decomposition.

This gate protects against the right-to-left failure mode: if decomposition
misses an official objective, every later step can appear complete while never
teaching, practicing, assessing, or remediating that objective.

### 2.1 Dependency rule

Every dependency edge must identify a reason, such as conceptual, procedural,
architectural, diagnostic, operational, governance, or cognitive-load
dependency. Mark it as hard or soft. Resolve circular dependencies through
staged introduction rather than hiding the cycle.

### 2.2 Unit boundary rule

A learning unit should be small enough to produce coherent mastery evidence
and large enough to support meaningful use. A syllabus bullet, chapter, or
lecture is not automatically a learning unit.

### 2.3 Pacing-track rule

Do not assume all learners have the same available timeline. A curriculum may
support a small number of named pacing tracks instead of trying to fit every
possible duration.

Each supported pacing track must state:

- expected prior knowledge;
- expected learner maturity or independence;
- daily or weekly active-learning commitment;
- whether teaching support is assumed;
- what is compressed, skipped, deferred, or intensified;
- risks of the pacing track;
- minimum mastery and exam-readiness gates that are not lowered by speed.

Pacing changes route, density, sequencing, support, and practice volume. It
must not silently lower the mastery standard.

### 2.4 Generated-material governance rule

When generated, imported, scraped, or AI-assisted material is used to create
teaching-system artifacts, separate the evidence from the approved artifact.
Use three layers:

```text
prompt/source -> raw response or gathered material -> reviewed normalized artifact
```

This rule applies beyond question banks. It can apply to draft lessons, slide
outlines, worksheets, rubrics, examples, scenarios, remediation notes, and
exam-prep items.

At minimum:

- preserve the prompt, source, import path, or authoring context;
- preserve the raw response or gathered material when practical;
- label true provenance, such as external LLM generation, manual authoring,
  Codex-assisted authoring, imported source, transformed source, or reviewer
  rewrite;
- do not treat generated or gathered material as approved curriculum content
  until it has been reviewed against the relevant specification;
- keep provider/model metadata only for content actually produced by that
  provider/model;
- normalize approved material into the appropriate durable artifact or schema;
- track generation/review cost where the workflow can multiply calls or human
  effort, including run budget, soft and hard thresholds, stage-level spend,
  and any authorized overage.

### 2.5 Explainable curriculum-map rule

After the dependency order, pacing tracks, knowledge profile, and artifact
families are defined, create an explainable curriculum map.

The map is not merely a planning spreadsheet. It is a confidence-building
artifact for teachers, learners, examiners, and future curriculum designers. It
shows why each topic appears where it appears, what kind of learning it
requires, and what evidence the learner will create.

At minimum, the map should include:

| Column | Purpose |
|---|---|
| Curriculum order | Shows the topic's position in the selected route, such as `Day01-order001` or `Module03-order004`. |
| Section or layer | Shows the dependency layer, domain section, or curriculum block. |
| Topic | Names the learnable capability or topic. |
| Source objectives | Records covered official objective IDs or links to the source-to-topic coverage map. |
| Knowledge category | Separates knowledge, skill, representation/location, social/organizational, and embodied-skill categories. |
| Knowledge type | Names the specific types, such as conceptual, procedural, diagnostic, embedded, or institutional. |
| Artifact to create | States the learner work product or evidence form aligned to the category/type mix. |

The order column must be derived from prerequisite and foundation logic first,
then from the selected pacing track. A fast path may compress topics into fewer
days or modules, but it must preserve the internal logic: foundations first,
then capabilities that build on them, then integration and transfer.

The artifact column must be derived from the knowledge profile rather than
from convenience. For example:

- declarative topics produce recall evidence;
- conceptual topics produce diagrams, concept maps, or explanations;
- procedural and embedded topics produce labs, runbooks, or configuration
  records;
- conditional and strategic topics produce decision tables, tradeoff matrices,
  or architecture decision records;
- causal and diagnostic topics produce cause-effect worksheets, incident
  reconstructions, or troubleshooting records;
- normative and institutional topics produce policy-to-control maps, RACI
  charts, audit-evidence checklists, or risk reviews;
- metacognitive topics produce error logs and confidence-calibration records.

This map should be created before large-scale student or teacher material
generation. It prevents hidden assumptions from being buried inside lessons,
slides, labs, or practice questions.

## 3. Learning Unit Schema

Every unit must define:

| Field | Requirement |
|---|---|
| Unit ID and title | Stable identifier and learner-meaningful name. |
| Source traceability | Source objectives, standards, or capabilities covered. |
| Purpose | Why the capability matters and where it is used. |
| Prerequisites | Hard and soft dependencies with reasons. |
| Outcomes | Observable learner performances. |
| Knowledge profile | Dominant and secondary cognitive types; relevant locus types and domains. |
| Target proficiency | Required level expressed as behavior. |
| Primary method | Method chosen for the dominant learning need. |
| Supporting methods | Methods justified by secondary types or transfer needs. |
| Teaching sequence | Ordered explanation, modeling, activity, feedback, and practice. |
| Learner artifact | Work product or observable performance created by the learner. |
| Mastery evidence | Criteria showing the outcome can be used as required. |
| Assessment | Authentic elicitation of the mastery evidence. |
| Gap model | Anticipated misconception, recall, execution, selection, or judgment failures. |
| Remediation | Gap-specific teaching and practice. |
| Reassessment | A fresh opportunity that tests the same capability without copying the first task. |

## 4. Method Selection

### 4.1 Method families

| Learning need | Primary methods | Suitable evidence |
|---|---|---|
| Declarative | Retrieval practice, spaced repetition, concise reference, discrimination practice | Accurate unaided recall and recognition among plausible alternatives |
| Conceptual | Diagrams, concept maps, analogy, contrasting examples, self-explanation, reconstruction | Explanation, classification, model reconstruction, transfer to a new example |
| Procedural | Demonstration, worked example, guided practice, fading support, varied independent practice | Successful independent performance under stated conditions |
| Conditional or strategic | Contrasting cases, decision tables, constraint changes, defended choices, critique | Selection with reasons, rejection of alternatives, adaptation when assumptions change |
| Causal or diagnostic | Predict-observe-explain, controlled experiment, failure injection, trace analysis, incident reconstruction | Prediction, isolation of cause, correction, and prevention reasoning |
| Normative or institutional | Dilemmas, stakeholder role-play, policy-to-control mapping, RACI, mock audit | Defensible judgment, ownership model, control evidence, residual-risk statement |
| Tacit or pattern recognition | Expert think-aloud, weak-versus-strong comparison, repeated varied cases, coaching, apprenticeship | Improved cue recognition and judgment across unfamiliar cases |
| Metacognitive | Confidence calibration, error analysis, evidence-based reflection, strategy adjustment | Accurate self-assessment and a tested change in learning or work strategy |
| Embedded | Direct tool use, build-observe-modify tasks, configuration inspection, repair exercises | Effective operation, modification, or repair of the real or faithful system |
| Embodied or implicit | Demonstration, imitation, frequent rehearsal, immediate sensory feedback, stable cues | Fluent performance and reliable automatic behavior |

### 4.2 Dominant and secondary types

The dominant type identifies the capability whose failure would most directly
prevent successful use. It selects the primary method and main mastery
evidence. Secondary types identify supporting instruction and practice.

Do not allocate methods by counting labels. State the rationale in terms of
what the learner must do.

### 4.3 Blended-method rule

A blended unit must remain a coherent sequence, not a collection of activities.
Use this default progression when it fits:

1. Orient the learner with purpose and a mental model.
2. Establish essential vocabulary or rules.
3. Model the target reasoning or performance.
4. Guide initial practice with feedback.
5. Vary conditions and reduce support.
6. Require an artifact or independent performance.
7. Assess transfer in the intended form of use.
8. Diagnose gaps, remediate, and reassess.

Omit stages that add no learning value. Add stages when tacit, embodied,
institutional, or high-risk performance requires more exposure.

### 4.4 Artifact derivation rule

Do not choose learner artifacts by habit. Choose them from the knowledge
category and type that must be evidenced.

Use this default mapping unless the domain gives a stronger reason to adapt it:

| Category | Type | Default learner artifact |
|---|---|---|
| Knowledge | Declarative | Retrieval cards, glossary recall sheet, closed-book quiz record. |
| Knowledge | Conceptual | Concept map, architecture diagram, comparison table, teach-back note. |
| Knowledge | Conditional | Decision table, contrasting-scenario worksheet, choose-and-reject record. |
| Knowledge | Causal | Cause-effect diagram, predict-observe-explain worksheet, experiment log. |
| Knowledge | Normative | Policy/risk review, ethics case analysis, responsible-practice checklist. |
| Skill | Procedural | Lab worksheet, runbook, worked example, independent task record. |
| Skill | Diagnostic | Troubleshooting worksheet, incident reconstruction, root-cause postmortem. |
| Skill | Strategic | Architecture decision record, tradeoff matrix, planning brief. |
| Skill | Metacognitive | Error log, confidence-calibration note, learning adjustment record. |
| Representation / Location | Explicit | Documentation map, reference checklist, standard operating procedure. |
| Representation / Location | Tacit | Expert critique notes, weak-vs-strong case comparison, case library entry. |
| Representation / Location | Implicit | Habit checklist, review rubric, cue-and-feedback record. |
| Representation / Location | Embedded | Console/API configuration record, tool inspection worksheet, build-observe-modify log. |
| Representation / Location | Institutional / Collective | RACI chart, policy-to-control evidence map, ownership and escalation register. |
| Social / Organizational | Social / Relational | Stakeholder map, ownership register, escalation path. |
| Embodied Skill | Embodied | Practice log, performance checklist, coaching notes. |

When a unit has multiple types, combine artifact families rather than creating
unrelated paperwork. Prioritize the artifact that best exposes the failure mode
that would prevent real use. A diagnostic-procedural-embedded topic, for
example, usually needs a troubleshooting worksheet plus a configuration or
inspection record, not only a quiz.

## 5. Package Schemas

### 5.1 Curriculum definition

The curriculum definition is the source of truth shared by teacher and student
packages. It contains the learning-unit schema, dependency position, coverage,
method rationale, mastery contract, and traceability links.

### 5.2 Teacher package

Each teacher package must contain actual instructional support:

- an open-first instructor runbook that identifies the preparation,
  step-by-step teaching sequence, expected learner responses, diagnostic
  signals, supporting files, progression decision, and required records;
- lesson purpose, outcomes, prerequisites, and estimated learning conditions;
- explanation sequence and conceptual models;
- demonstrations, worked examples, and think-aloud notes;
- questions to ask and evidence to listen or look for;
- activities with facilitation and feedback instructions;
- likely misconceptions and diagnostic prompts;
- adaptation guidance for prior knowledge and common gaps;
- artifact specifications, assessment administration, answer guidance, and
  rubrics;
- remediation routes and reassessment guidance.

A label such as "teach with a diagram" is incomplete unless the diagram,
its teaching purpose, and its use are supplied.

The runbook is the authoritative entry point for conducting a unit. Lesson
plans may provide compact planning views, and teaching guides may provide deep
content references, but the teacher should not have to reconstruct the lesson
sequence by navigating among them.

### 5.3 Student package

Each student package must contain the complete learner experience:

- an open-first learner guide that gives the sequence, required materials,
  artifact, mastery standard, and exact starting activity;
- a purpose statement and prerequisite check;
- explanations and mental models;
- examples, comparisons, and demonstrations appropriate to the unit;
- guided and independent activities;
- reference or retrieval materials where needed;
- artifact instructions and quality criteria;
- practice with actionable feedback;
- mastery assessment;
- gap-specific remediation and reassessment instructions.

The package may use guides, diagrams, cards, labs, investigations, scenarios,
audio, video, discussion, or other media. Media are chosen for learning
function and accessibility, not decorative variety.

### 5.4 Unit readiness gate

A unit is not ready merely because every mapped topic has a learner artifact.
Before marking a unit complete, check that artifact coverage does not outrun
teaching coverage.

For every learner artifact, confirm:

- the relevant dominant and secondary knowledge types are taught explicitly;
- every worksheet row, activity, self-check, and artifact prompt can be
  completed from the provided study material, examples, and answer guidance;
- every glossary term, retrieval card, table term, and learner-facing label is
  explicitly taught, linked to teaching, or removed;
- every future-depth concept is labeled as a forward reference with the later
  unit, module, or day that teaches it;
- the learner has seen at least one worked, partially worked, or contrastive
  exemplar before being asked to self-assess;
- procedural and embedded topics include a concrete reference artifact,
  demonstration, tool/API example, configuration, or faithful simulation to
  inspect;
- answer guidance or a rubric shows what strong, partial, and weak evidence
  look like;
- remediation targets point to existing files, sections, activities, or
  teacher actions.
- source notes and citations resolve, and their labels accurately describe the
  linked source.

If any check fails, or if the reverse activity-to-teaching test is only
`mostly yes` or `borderline`, the artifact remains a draft prompt for work,
not a complete teaching-system component.

## 6. Mastery, Assessment, and Remediation

### 6.1 Mastery contract

Before content is produced, define:

- the performance or artifact;
- the conditions, tools, references, and constraints;
- the quality criteria and minimum standard;
- the degree of independence required;
- the transfer distance from practiced examples;
- the consequences and remediation route for each important gap.

### 6.2 Alignment rule

Assess knowledge in the form in which it must be used. A recognition question
cannot by itself establish procedural performance, strategic judgment, tacit
cue recognition, or institutional coordination.

Multiple-choice questions may assess selected declarative, conceptual, and
conditional distinctions, but must not become the default evidence for every
unit.

### 6.3 Exam-readiness rule

When a course prepares learners for an external certification or standardized
exam, exam preparation is a separate layer from mastery teaching.

Unit mastery assessment asks whether the learner can use the capability in the
form required by the subject. Exam-readiness assessment asks whether the
learner can demonstrate exam-format performance under timed conditions.

Exam preparation must begin with the current official exam specification. At
minimum, record:

- exam code and source version or access date;
- intended candidate and prerequisite assumptions;
- number of questions and time limit;
- scored and unscored item structure, if published;
- allowed question formats;
- domain weightings and task statements;
- official pass/fail criteria and reporting model;
- calculator, navigation, review, language, or delivery constraints when
  relevant.

Before using official objectives as tags, run a source-extraction readiness
check. Confirm that the source format and extraction method expose the deepest
objective level the curriculum will claim, such as domain, task, skill,
subskill, standard, or rubric criterion. Record the source file or URL,
access date or version, extraction tool or method, extracted hierarchy, and
known gaps. If an extraction pass misses data that exists in the source, treat
that as a tooling/process gap rather than a source limitation.

Practice tests should simulate the official format closely enough to reveal
readiness gaps, but internal readiness gates should be slightly stricter than
the published passing standard. For example, if the official exam reports a
minimum passing scaled score, the curriculum may require a higher practice
test score, stable performance across domains, and completion within the time
limit before recommending that the learner schedule the exam.

Question banks must be tagged so performance can be diagnosed. Recommended
tags include:

- exam domain and task statement;
- learning unit ID;
- source objective or source reference;
- knowledge type;
- question format;
- difficulty;
- cognitive demand;
- misconception or distractor pattern;
- remediation target;
- item status, review date, and source trace.

Question-bank provenance must be explicit and must remain separate from review
status. Raw item inputs should state whether they came from an external LLM
generation, manual authoring, Codex-assisted authoring, imported source,
transformation of an existing item, or reviewer rewrite. A reviewed bank may
approve items from multiple origins, but provider/model metadata must only be
used for content actually produced by that provider/model.

Question-bank review must be auditable. Rejected or culled items should carry
both a structured reason code and a human-readable evidence note. The evidence
should cite the concrete field value, missing field, matched stem pattern,
matched source phrase, duplicate comparison, unsupported claim, or other
observable fact that caused the rejection.

Generated question-bank workflows must use review culls as improvement data.
Before any regeneration or top-up pass, summarize culls by reason and revise
the next prompt or authoring brief to address the dominant failure patterns.
Include approved stems, rejected stem excerpts, source-sensitive claims to
verify, and the minimum surplus needed above the exact deficit so review can
cull weak, duplicate, or unverifiable items without leaving the bank short.

The continuous-improvement loop is:

```text
review cull summary -> prompt or brief revision -> surplus top-up generation
-> review rerun -> coverage and approved-output checks
```

Question-bank review must cover the full item, not only the stem or correct
answer. Review source accuracy, stale claims, duplication, and teaching quality
across learner-visible text surfaces: stem, options, correct rationale,
distractor rationales, misconception tags, source traces, and remediation
links. Distractor rationales are teaching content and can fail an item even
when the keyed answer is defensible.

Known-pattern scans are not factual verification. For source-sensitive or
high-rot technical claims, extract atomic claims and verify them against
official sources when possible. Examples include service limits, supported
formats, Region availability, API fields, security behavior, networking
support, data-residency claims, and capability comparisons. Unresolved
`needs-source-check` claims should be held out of any bank marked complete.
When LLMs are used for generation and judgment, reduce correlated blind spots
with a different reviewer model/provider, adversarial review framing, multiple
review passes, or human review for residual source-sensitive claims.

Final fact checking is a learner-trust gate. A question bank must not be marked
complete or approved until every learner-visible item has either passed source
verification or been removed/resolved with human review. This includes
operational and remediation claims, not only service-capability claims. If
final fact checking culls an item, add the cull to the audit log with the stem,
challenged claim or rationale, and review finding, then recompute per-topic
coverage before declaring the bank complete.

Question-bank completion should include distribution checks, not only item
counts. Review difficulty spread, cognitive-demand spread, answer-position
balance, per-topic knowledge-type coverage, and any official-domain weighting
needed for the bank's intended use. A per-topic practice bank may deliberately
use equal topic counts; a full exam simulation pool should support official
domain/task weighting.

After review, run negative-control checks against the approved bank for known
rejected patterns. A review pass is incomplete if a phrase, schema defect,
duplicate pattern, stale claim, source-trace gap, or provenance problem that is
treated as disqualifying in the cull log still appears in approved content.

Question-bank review is not remediation by itself. After a practice exam, the
learner should receive a gap report that links missed or weak items back to
specific learning units, explanations, activities, labs, retrieval practice, or
additional exam-format drills.

### 6.4 Gap model

At minimum, distinguish:

| Gap | Typical response |
|---|---|
| Recall | Retrieval with spacing and discrimination practice. |
| Conceptual model | Alternate explanation, comparison, reconstruction, and teach-back. |
| Procedure | Re-demonstration of the failed step, focused rehearsal, then faded support. |
| Conditional selection | Contrasting cases and explicit comparison of cues and constraints. |
| Causal diagnosis | Prediction, controlled variation, trace interpretation, and root-cause practice. |
| Strategic judgment | Expert think-aloud, critique, and additional cases with changed assumptions. |
| Normative or institutional | Stakeholder, policy, ownership, evidence, and residual-risk analysis. |
| Embedded system use | Direct inspection and repair in the relevant tool or faithful environment. |
| Metacognitive calibration | Compare confidence with evidence and test a revised strategy. |

Remediation must teach the missing capability differently or more precisely;
it is not merely repetition of the original material.

### 6.5 Reassessment rule

Reassessment must preserve the target capability and standard while changing
surface details. Record whether the learner succeeded independently and
whether the improvement transfers beyond the remediated example.

## 7. Traceability

Maintain a traceability chain from:

`source objective -> capability -> dependency position -> learning unit ->
teaching activity -> learner artifact -> assessment criterion -> remediation`

Use stable identifiers. Generated spreadsheets, documents, presentations, and
dashboards are views of this model, not the sole source of truth.

## 8. Adaptation

Adaptation may change route, pace, scaffolding, practice volume, examples, or
medium. It must not silently lower the mastery standard.

Use diagnostic evidence to support:

- testing out of already-mastered units;
- prerequisite repair before dependent work;
- extra practice for a specific gap;
- alternate representation or explanation;
- additional varied cases for transfer and judgment;
- accessibility accommodations that preserve the intended capability.

## 9. Pacing Models

A curriculum should distinguish learning architecture from calendar plan. The
architecture defines dependencies, units, mastery evidence, remediation, and
assessment. A pacing model maps that architecture onto a learner timeline.

When timelines vary widely, prefer a small number of explicit pacing tracks to
an implied one-size-fits-all plan. A useful minimum is:

- **self-paced track:** materials and mastery gates are available, and learners
  progress on their own schedule;
- **accelerated track:** a compressed plan for learners who meet stated
  prerequisites and can commit significant active-learning time.

Every accelerated track must include a suitability warning. It should identify
the assumed background and the daily effort required. It should also preserve
the same mastery and exam-readiness gates as the self-paced track. Speed may
increase intensity, but it must not redefine success as mere exposure.

## 10. Pilot Validation

Before scaling, implement one bounded unit across the curriculum definition,
teacher package, and student package. Prefer a unit with several knowledge
types and a meaningful learner artifact.

Review the pilot against these criteria:

1. The learning order and prerequisites are defensible.
2. Method choices follow the knowledge profile and intended use.
3. The package contains real teaching, not only design instructions.
4. Teacher and student materials agree on outcomes and mastery.
5. The learner performs, decides, explains, or creates in the required form.
6. Feedback identifies actionable gaps.
7. Remediation addresses distinct gaps and leads to reassessment.
8. Source-to-assessment traceability is complete.
9. The experience is usable without hidden author context.
10. Lessons from implementation are captured for revision of this kit.

## 11. Scale Gate

Do not generate the full course merely because templates exist. Scale only
after the pilot has been taught or realistically walked through, major gaps
have been repaired, and the generic specification has been revised with the
lessons learned.

## 12. Kit Stewardship

The Curriculum Architecture Kit is the durable reusable asset. Pilot
implementations may be revised, regenerated, or discarded, but reusable
learning from those pilots should strengthen the kit.

Keep generic methodology and pilot implementation artifacts separate. The kit
may contain subject-agnostic specifications, templates, review methods,
quality gates, examples, and distilled lessons. Pilot directories should
contain subject-specific source material, curriculum models, teacher kits,
student kits, exam-prep banks, raw generated outputs, and implementation
decisions. Do not move pilot-specific facts, service choices, exam details, or
day plans into the generic kit unless they are clearly labeled as examples and
the reusable rule is stated independently.

Maintain a lessons-learned register for:

- source or exam identity errors;
- scope mistakes and boundary confusion;
- teaching patterns that worked or failed;
- assessment and remediation improvements;
- workflow efficiencies;
- traceability failures;
- validation checks that should become standard practice.

When a lesson is specific to one subject, keep it in the pilot materials. When
it applies across subjects or future implementations, record it in the kit and
revise this specification or related templates when the lesson becomes stable
guidance.
