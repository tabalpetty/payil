# Curriculum Architecture Kit Lessons Learned

## Purpose

This register captures reusable lessons from pilots, mistakes, reviews,
remediations, and efficiency improvements.

The Curriculum Architecture Kit is the durable asset of this project. Pilot
implementations are laboratories. When a pilot reveals a better rule, missing
guardrail, common failure mode, useful template, or workflow improvement, record
it here and later fold it into the appropriate kit specification or template.

## How To Use This Register

Add an entry when:

- an implementation mistake reveals a missing guardrail;
- source identity, exam identity, or scope confusion causes rework;
- a teaching or assessment pattern works better than expected;
- a workflow reduces wasted effort;
- a remediation path improves learner progress;
- a validation check catches a design problem;
- a lesson should transfer to future subjects or pilots.

Each entry should state:

- what happened;
- why it matters;
- what changed or should change;
- whether the kit specification needs an update.

## Lessons

### 2026-06-18: Separate Generic Architecture From Pilot Artifacts

**What happened:** Early AIP-C01 implementation artifacts were generated under
`docs/aip-c01/` and later deleted after an exam-identity correction.

**Why it matters:** A pilot can be reset or regenerated, but the Curriculum
Architecture Kit should remain stable, reusable, and protected from
implementation-specific churn.

**Reusable lesson:** Put pilot artifacts under an explicit pilot directory,
such as `docs/Pilot1/aip-c01/`, while keeping
`docs/curriculum-architecture-kit/` subject-agnostic.

**Kit update needed:** Yes. Add or preserve explicit deliverable-boundary rules
that separate the generic kit from pilot implementations.

### 2026-06-18: Verify Exam Identity Before Building Exam Prep

**What happened:** A wrong exam identity was temporarily introduced into
exam-prep planning. The target was corrected to AWS Certified Generative AI
Developer - Professional (AIP-C01), and the contaminated implementation
artifacts were removed.

**Why it matters:** Exam name, code, level, domains, question formats, timing,
and passing score shape the curriculum model, question bank, practice tests,
and readiness gates. A wrong exam identity contaminates many downstream
artifacts.

**Reusable lesson:** Before generating curriculum or exam-prep materials,
create an exam/source identity checkpoint that records official name, code,
source URL, access date, candidate profile, domain outline, question formats,
duration, and scoring.

**Kit update needed:** Yes. Strengthen the exam-readiness rule and source
inventory process with an identity checkpoint before generation.

### 2026-06-18: Raw Provider Responses Are Evidence, Not Source Of Truth

**What happened:** The project adopted a workflow where LLM or web-generated
question candidates should be stored as whole raw responses before being parsed
into reviewed question-bank items.

**Why it matters:** Preserving whole raw responses keeps provenance clear,
avoids unnecessary chunking, and separates evidence collection from approved
curriculum content.

**Reusable lesson:** Maintain three layers for generated or gathered materials:
prompt/source, raw response, and reviewed normalized artifact.

**Kit update needed:** Yes. Add this pattern to future question-bank or
generated-material workflows.

### 2026-06-18: Do Not Assume One Learner Timeline

**What happened:** The project identified an implicit assumption that all
learners have the same available timeline for learning.

**Why it matters:** Real learners have different time constraints. A single
calendar plan can either overwhelm busy learners or underspecify expectations
for accelerated learners.

**Reusable lesson:** Separate curriculum architecture from pacing. Support a
small number of explicit pacing tracks, each with stated assumptions, time
commitments, risks, and unchanged mastery gates.

**Kit update needed:** Yes. Add pacing-track rules to the teaching-system
specification and require accelerated plans to state prerequisites and active
learning commitments.

### 2026-06-19: Make Curriculum Ordering And Artifact Logic Explainable

**What happened:** While building the AIP-C01 accelerated path, the project
created a topic map that combined curriculum placement, section/layer, topic,
knowledge category, knowledge type, and artifact-to-create. The map used the
existing prerequisite-oriented topic order, assigned each topic into the 7-day
accelerated route, and derived artifact families from the knowledge
category/type mix.

**Why it matters:** Teachers and learners need to trust the system. A syllabus
or calendar alone does not explain why a topic appears on a given day, why a
specific teaching method is used, or why a learner is asked to create a
particular artifact. The map makes the design inspectable: sequence comes from
dependencies and pacing, methods come from knowledge type, and artifacts come
from the evidence needed for mastery.

**Reusable lesson:** Every serious implementation should include an explainable
curriculum map before generating large volumes of lessons, slides, labs, or
practice questions. The map should show:

- route/order identifier, such as `Day01-order001`;
- section or dependency layer;
- topic or learnable capability;
- knowledge category;
- knowledge type;
- artifact to create;
- the rule used to assign order and derive artifacts.

**Kit update needed:** Yes. Add an explainable curriculum-map rule and artifact
derivation rule to the teaching-system specification, and provide a reusable
construction guide/template.
