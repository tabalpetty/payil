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

### 2026-06-20: Do Not Let Artifact Coverage Outrun Teaching Coverage

**What happened:** Day 1 of the AIP-C01 pilot had a strong curriculum map and
focused artifacts for every ordered topic, but the study guide initially taught
only the earliest foundation topics in depth. Later artifacts asked learners to
complete control-placement, invocation, model-selection, and golden-dataset
work before the corresponding concepts and procedures were explicitly taught.

**Why it matters:** A visible workbook can create a false sense of curriculum
completion. If the learner is asked to produce evidence before receiving
adequate exposition, demonstrations, examples, or answer guidance, the system
has recreated the "artifact without teaching" failure that the architecture is
meant to prevent.

**Reusable lesson:** For every learning artifact, require a teaching-coverage
check before marking a unit deliverable. Run the check in reverse: for every
worksheet row, activity, self-check, or artifact prompt, ask whether a learner
can complete it using the provided study material, worked examples, and answer
guidance without unstated outside knowledge.

- the dominant and secondary knowledge types are taught in matching forms;
- the artifact has at least one worked or partially worked exemplar;
- procedural or embedded topics include a concrete reference artifact to
  inspect;
- the answer guidance shows what strong evidence looks like;
- remediation routes point to existing teaching material, not imagined files.

Do not accept `mostly yes`, `borderline`, or `adequate but unsupported row` as
a release state for self-study material. If the artifact asks for it, the
teaching system must ground it.

**Kit update needed:** Yes. Add a unit-readiness gate requiring reverse
activity-to-teaching validation, teaching coverage, exemplars, and
remediation-target validation before artifacts or question-bank items are
considered complete.

### 2026-06-21: Treat Review Culls As Prompt-Improvement Data

**What happened:** The Day 1 AIP-C01 question bank had enough raw material to
start review, but the approved bank stayed below the target of 10 items per
topic after weak, duplicate, recall-only, and unverifiable items were culled.
The largest rejection patterns were glossary-style stems, recall-only cognitive
demand, and stale or unsupported AWS service-capability claims.

**Why it matters:** A strict review pass is doing its job when it protects the
learner from weak practice items. But if the rejection reasons are only logged
as a postmortem, the next generation pass is likely to repeat the same failure
patterns. Completion targets need both quality gates and a feedback loop that
changes future prompts.

**Reusable lesson:** Generated assessment workflows should record cull reasons
as structured improvement signals before more generation. The next prompt
should explicitly address the highest-frequency failure modes, reject known bad
stem patterns, require source-checkable technical claims, and over-generate
above the approved-item target to account for expected review loss.

**Kit update needed:** Yes. Add a continuous-improvement gate for generated
question banks: review cull summary -> prompt revision -> surplus top-up
generation -> review rerun -> completion check.

### 2026-06-21: Keep Item Provenance Separate From Review Approval

**What happened:** During the Day 1 AIP-C01 question-bank top-up, the execution
environment did not have an external LLM API key. A manual/Codex-authored
top-up set was added and passed through the same reviewer, but its initial raw
filename and metadata implied OpenAI generation. The questions were not reused
rejections, but the provenance label was still misleading until corrected.

**Why it matters:** Review approval answers "is this item good enough to use?"
Provenance answers "where did this item come from?" Those are different audit
questions. A strong review pass does not justify ambiguous origin metadata,
especially in a system that preserves raw responses and uses traceability as a
governing principle.

**Reusable lesson:** Every raw assessment input must declare its real origin:
external LLM generation, manual authoring, Codex-assisted authoring, imported
source, transformed item, or reviewer rewrite. The reviewed bank may approve
items from more than one origin, but it must preserve the origin honestly and
must not use provider/model labels for content that did not come from that
provider/model.

**Kit update needed:** Yes. Add a provenance rule to generated-material and
question-bank workflows: raw source metadata is mandatory; provenance and
review status are separate fields; any manual or assisted top-up must be
explicitly labeled before normalization into reviewed outputs.

### 2026-06-21: Verify Source Extraction Before Claiming Objective Traceability

**What happened:** Day 1 question-bank items initially traced to official
domains and tasks, but their `exam_skill` values were local paraphrases rather
than official Skill X.Y.Z statements. A coverage note incorrectly suggested
that the official PDF did not expose skill bullets as structured text. Later
review showed that the source PDF did contain extractable skill bullets; the
missing piece was the PDF extraction mechanism used earlier, not the source
itself.

**Why it matters:** Traceability is only as strong as the source extraction
pipeline. If the project claims objective-level alignment while extracting
only coarse sections, later audits cannot answer whether every official skill
is covered. Worse, an inaccurate note about source limitations can become a
false reason to stop improving the traceability chain.

**Reusable lesson:** Before generating or reviewing objective-tagged artifacts,
run a source-extraction readiness check on every official PDF or structured
source. Confirm that the required levels of hierarchy are extractable, such as
domain, task, skill, subskill, standard, or rubric criterion. Preserve the
extraction method, tool/library, source file, and any known gaps. If extraction
fails, label the limitation as a tooling/process gap unless the source itself
has been verified to lack the information.

**Kit update needed:** Yes. Add a source-extraction readiness gate to the
exam-readiness and traceability workflow: official objectives must be extracted
to the deepest level used by downstream fields before item generation, review,
coverage claims, or remediation routing are marked complete.

### 2026-06-21: Make Reviewer Decisions Auditable, Not Merely Labeled

**What happened:** The Day 1 reviewer initially grouped culled questions by
reason, but some cull entries only showed labels such as `duplicate-pattern`,
`not scenario-based`, or `keyword-trivia stem`. Review feedback clarified that
every rejection should include enough evidence for a future maintainer to
understand the decision without reverse-engineering the script.

**Why it matters:** A strict review process builds trust only when its
decisions are explainable. Labels are useful for aggregation and prompt
improvement, but they are not sufficient audit evidence. A duplicate rejection
should show both stems; a stale-claim rejection should show the matched phrase;
a schema rejection should show the missing field.

**Reusable lesson:** Reviewer output should include both structured reason
codes and human-auditable evidence. Each culled item should state the
observable fact that triggered the rejection: field value, missing field,
matched pattern, source mismatch, duplicate comparison, unsupported claim, or
quality-rule violation.

**Kit update needed:** Yes. Add an audit-evidence requirement to generated
assessment review workflows and any other review gate that can reject
artifacts. Review summaries should support both aggregate improvement and
item-level explanation.

### 2026-06-21: Review Every Teaching Surface In An Assessment Item

**What happened:** Day 1 item `P1-AIP-D1-023` had a defensible correct answer,
but one distractor rationale claimed that Amazon Bedrock had no VPC endpoint
support "as of early 2024." That statement was false and stale. The automated
review had already culled sibling items with similar stale phrases, but the
filter looked at stems, options, correct-answer rationales, and source hints
without scanning distractor rationales, so the false teaching survived inside
an approved item.

**Why it matters:** Distractor rationales are teaching material. A practice
question can have the right answer while still teaching a wrong fact in its
explanation. Review scopes that inspect only stems or correct rationales leave
room for false claims, stale service limitations, or misleading misconceptions
to enter the learner experience.

**Reusable lesson:** Assessment review must scan every learner-visible text
surface: stem, options, correct answer, correct rationale, distractor
rationales, misconception tags, source traces, and remediation links. Stale
claim filters and source checks should apply to the full item, not only the
main prompt or the correct explanation.

**Kit update needed:** Yes. Add a full-item review-scope rule to generated
assessment workflows. Any automated reviewer should treat distractor
rationales as first-class teaching content and include them in stale-claim,
source-check, duplication, and quality scans where relevant.

### 2026-06-21: Test Review Rules Against Approved Output

**What happened:** After the false Bedrock VPC endpoint rationale in
`P1-AIP-D1-023` was found, the reviewer was broadened to scan distractor
rationales. The fix was verified by scanning the approved Day 1 bank for the
same stale patterns that had caused sibling items to be culled, such as
`as of early 2024`, `no current support`, and `Bedrock does not yet`.

**Why it matters:** A review rule can be written down and still miss content if
the implementation checks the wrong fields or only catches one wording variant.
Auditing only the cull log confirms that some bad items were rejected; it does
not prove that the same failure pattern is absent from the approved bank.

**Reusable lesson:** Every automated review pass should end with an
approved-output regression check for known rejected patterns. For stale claims,
schema drift, duplicate stems, source-trace gaps, and provenance problems, scan
the normalized approved artifact and fail the pass if a disqualifying pattern
survives.

**Kit update needed:** Yes. Add post-review negative-control checks to
assessment review workflows. Completion gates should require both an auditable
cull log and a clean scan of approved content for the failure patterns that the
reviewer claims to reject.

### 2026-06-22: Ground Every Term And Label Every Forward Reference

**What happened:** Day 2 passed the main reverse test, but review found three
small release-quality gaps: a retrieval-card term (`Input limit`) appeared in
an artifact before it was explicitly defined in the study guide; hybrid
keyword-plus-vector retrieval appeared in the vector-store architecture topic
without a clear "deeper on Day 3" label; and Bedrock Knowledge Bases source
notes needed URL verification plus a more accurate label for the supported
models and Regions page.

**Why it matters:** A self-study learner treats every glossary row, retrieval
card, source note, and worksheet prompt as something they are expected to use
now. Undefined terms create avoidable friction. Unlabeled forward references
can pull learners into future-day depth too early. Source-note labels that are
close but not exact weaken audit trust even when the URL resolves.

**Reusable lesson:** During reverse review, check every learner-facing term,
retrieval card, glossary row, table label, and source note. Each term must be
explicitly taught or removed. Each future-depth concept must be labeled as a
forward reference with the later unit/day that teaches it. Each source note
must have both a resolving URL and a label that accurately describes the page.

**Kit update needed:** Yes. Add term-grounding, forward-reference labeling,
and source-note URL/label verification to the unit-readiness gate and quality
review guide before generating subsequent day materials.

### 2026-06-22: Denylist Review Is Not Factual Verification

**What happened:** The exam-prep agent architecture correctly included stale
phrase scans and approved-output regression checks, but review noted a central
risk: a novel, confidently wrong technical claim could pass every denylist if
it did not match a known bad phrase. If the same model family generated and
judged the item, the judgment review could share the same blind spot.

**Why it matters:** Generated assessment items often contain atomic technical
claims about services, APIs, limits, Regions, security behavior, or current
availability. A clean banned-phrase scan means only that known bad patterns
were not found. It does not prove that new claims are true.

**Reusable lesson:** Generated assessment workflows need an explicit
source-verification path for atomic technical claims. Use official-source
retrieval/checking where possible, reviewer independence for judgment passes,
and a rule that unresolved `needs-source-check` items cannot enter a complete
bank. Distribution gates should also check difficulty, cognitive demand,
answer-position balance, and knowledge-type coverage so a bank does not pass
only by item count.

**Kit update needed:** Yes. Add source-sensitive claim verification,
reviewer-independence guidance, unresolved-source-check handling, and
distribution gates to the generic question-bank review rules.

### 2026-06-22: Generated Workflows Need Cost Gates

**What happened:** The exam-prep agent design initially governed quality,
traceability, provenance, top-up loops, and factual verification, but did not
include an explicit cost section. Review noted that generation, judgment
review, adversarial review, claim verification, top-ups, and human residual
review can multiply cost quickly.

**Why it matters:** A quality workflow can still fail operationally if it has
no budget, telemetry, or stop condition. Without cost gates, an agent may
continue generating low-yield top-ups, rerunning reviews, or escalating human
checks without making the spend visible.

**Reusable lesson:** Generated-material workflows should track cost by stage,
set soft and hard budget thresholds, estimate top-up/review cost before
continuing, and report cost per approved artifact or topic. A complete run
should state that it stayed within budget or record the authorized overage.

**Kit update needed:** Yes. Add budget telemetry and cost gates to generated
question-bank and generated-material workflow guidance.

### 2026-06-23: Treat Final Fact Checking As The Learner-Trust Gate

**What happened:** The Day 2 exam-prep agent flow initially had a final gate
for traceability, source checks, distribution, and cost, but source
verification was not yet functional. When the fact-checker was implemented, it
verified 118 items and culled one additional item, `P1-AIP-D2-083`, because
the item taught an unsupported operational remediation: increasing OpenSearch
shard count as the best response to `Too many open files`.

**Why it matters:** Final fact checking is one of the most important learner
protection steps in generated assessment workflows. A question can have a
plausible shape, good metadata, and enough topical coverage while still
teaching a false technical rule in the correct rationale, distractor rationale,
or remediation explanation. From the learner's perspective, this is worse than
a weak question: it creates a misconception.

**Reusable lesson:** Treat final source/fact checking as a non-negotiable
release gate, not as a bookkeeping step. Generation, normalization, and review
create candidates; final fact checking earns learner trust. The gate must:

- reject unresolved source markers;
- reject stale or current-capability claims without evidence;
- verify source-sensitive service, API, security, networking, operational, and
  remediation claims against trusted sources or route them to human review;
- cull unsupported or contradicted items instead of patching them with weak
  citations;
- add every final-stage cull to the cull log with observable evidence; and
- recompute coverage after final-stage culls before declaring a bank complete.

**Kit update needed:** Yes. Strengthen question-bank completion rules,
quality-review guidance, and generated-agent workflow templates so final
fact-checking is required before any bank is labeled complete or approved.

### 2026-06-23: Audit Source-To-Decomposition Coverage Before Generation

**What happened:** While designing upstream layers for the exam-prep agent, the
project recognized that every downstream artifact depends on the original
source decomposition. The AIP-C01 accelerated plan references all 20 official
tasks, but the topic map does not yet explicitly record official Skill X.Y.Z
coverage or deferrals for all 98 official skills.

**Why it matters:** If decomposition silently misses an official objective,
later topic briefs, lessons, artifacts, question banks, remediation routes, and
coverage reports can all appear complete while never touching the missing
objective. Late checks around question-bank coverage are too far downstream to
repair a missing source-to-topic bridge cheaply.

**Reusable lesson:** Add a Layer 0 source-to-decomposition coverage gate after
source extraction and before curriculum generation. The gate should compare
the official source hierarchy against the curriculum decomposition and require
each official objective to be covered or explicitly deferred. Day-level task
coverage is useful, but it is not enough when downstream artifacts claim
skill-level traceability.

**Kit update needed:** Yes. The teaching-system specification now includes a
source-to-decomposition coverage rule, and Pilot1 has a reusable audit script
plus a deferrals register.

### 2026-06-23: Do Not Confuse Source Presence With Claim Verification

**What happened:** An assessment verifier marked items `source-verified` when
their source traces existed, risky phrases were absent, and mentioned service
names appeared somewhere in a trusted corpus. Those checks were useful
screening but did not prove the item's specific capability, limitation,
comparison, causal, or remediation claims.

**Why it matters:** A green factual-verification gate can be more dangerous than
an explicit pending state if its evidence does not support its label. Learners
may be taught a false rule even though every referenced file exists.

**Reusable lesson:** Require item-level atomic-claim records for generated
assessment content. Each material claim needs a trusted source, concise
evidence, and a supported, contradicted, or unresolved verdict. Missing evidence
must block approval. Also verify objective alignment at the relationship level:
an official skill may exist globally while still being invalid for the item's
curriculum topic.

**Kit update needed:** Yes. Assessment-agent templates and quality gates should
separate source presence, source relevance, and claim verification, and should
enforce topic-to-objective relationships rather than checking identifiers only
against global lists.

### 2026-06-23: Orchestrate Curriculum Production As A Multi-Agent System

**What happened:** High-quality Day 1 and Day 2 materials required a repeated
sequence of source checking, decomposition, teaching, artifact design, answer
guidance, independent review, revision, fact checking, reverse testing,
assessment production, and lessons capture. The exam-prep agent automated only
the assessment branch and correctly treated study material as an upstream
dependency.

**Why it matters:** A single authoring prompt cannot reliably own source
authority, curriculum order, teaching depth, activity design, answer
calibration, independent review, factual verification, and release judgment.
Combining all roles also lets a model approve its own assumptions and makes
partial workflow state difficult to audit.

**Reusable lesson:** Use one deterministic production orchestrator with bounded
worker roles. Keep authoring, independent semantic review, deterministic
validation, factual verification, and release authority separate. Teaching
must precede dependent activities; guidance must precede self-assessment;
assessment must consume a passed teaching substrate. Preserve raw author and
review output, normalize findings, bound revision loops, and let confirmed
defects improve prompts, tests, specifications, and lessons at the appropriate
level.

**Kit update needed:** Yes. The kit now includes a project-level Curriculum
Production Agent Architecture and a decision record for the multi-agent
authority model.
