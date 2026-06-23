# Exam Prep Production Agent Architecture

## Purpose

The Exam Prep Production Agent produces review-ready exam-prep material for a
curriculum day at the same quality bar as the approved Day 1 bank.

The agent is not a question generator. It is a governed production workflow
that uses generation, deterministic review, traceability checks, top-up loops,
and approved-output regression checks to create an auditable question bank.

First implementation target:

```text
Pilot1 AIP-C01 Day 2 exam prep
```

Reusable target:

```text
Any curriculum day with a map, teaching materials, official objectives, and a
question-bank schema.
```

Diagram source:

[exam-prep-agent-architecture.drawio](exam-prep-agent-architecture.drawio)

Agent design lessons:

[exam-prep-agent-design-lessons.md](exam-prep-agent-design-lessons.md)

## Design Goals

- Produce at least `10` approved items per curriculum-order topic.
- Preserve raw provenance separately from review approval.
- Trace every approved item to official domain, task, skill, curriculum topic,
  knowledge type, source trace, and remediation target.
- Cull weak, duplicate, stale, unsupported, or schema-drifted items with
  auditable evidence.
- Feed cull reasons back into top-up prompts.
- Verify novel source-sensitive technical claims against official sources
  rather than relying only on banned-phrase scans.
- Enforce distribution quality, including difficulty, cognitive demand,
  answer-position balance, and official-domain coverage appropriate to the
  intended bank use.
- Track cost by stage and stop or escalate when budget thresholds are reached.
- Refuse to mark a bank complete until approved-output checks pass.
- Keep LLM generation useful but bounded by deterministic quality gates.

## Non-Goals

- The agent does not replace the teaching kit. It assumes the day already has
  study guide, artifacts, and answer guidance that pass the reverse-test rule.
- The agent does not trust raw LLM output as approved content.
- The agent does not lower completion targets when review culls heavily.
- The agent does not claim current AWS service facts without source trace or
  explicit source-check status.
- The agent does not treat absence of a banned phrase as proof that an item is
  factually current.

## Intended Bank Uses

The per-day reviewed bank serves two related but different purposes:

| Use | Coverage rule |
|---|---|
| Per-topic practice and remediation | At least `10` approved items per curriculum-order topic. |
| Full exam simulation assembly | Sample from reviewed items using official domain weighting, question format mix, difficulty spread, and timing constraints. |

The `10`-per-topic rule is a production-depth rule for daily practice. It is
not the same as full-exam weighting. A full simulated exam should be assembled
from the reviewed pool using the official exam guide's domain and task
distribution rather than taking equal counts from every curriculum topic.

## Inputs

| Input | Purpose |
|---|---|
| Curriculum map | Determines day topics, order, knowledge types, and expected artifact evidence. |
| Study guide | Supplies the teaching material that remediation should route back to. |
| Focused artifacts | Reveal the mastery evidence each topic expects. |
| Answer guidance | Shows what strong evidence and misconceptions look like. |
| Official exam guide extraction | Supplies official domain, task, and Skill X.Y.Z statements. |
| Question-bank specification | Defines schema, completion target, provenance, and review rules. |
| Prior reviewed banks | Supply quality exemplars, approved stems, rejected patterns, and duplicate guards. |
| Official AWS docs or source notes | Support current technical claims where service behavior matters. |

For Pilot1 Day 2, the generator-of-record must be stated before raw files are
created. If the run uses Codex-assisted authoring or manual top-up instead of
an external LLM API, the raw metadata and filenames must say so from the first
candidate file.

## Outputs

| Output | Path pattern |
|---|---|
| Day prompt pack | `exam-prep/day-NN-question-generation-prompts.md` |
| Raw candidate files | `exam-prep/raw/day-NN/*.md` |
| Reviewed bank | `exam-prep/reviewed/day-NN/day-NN-reviewed-question-bank.md` |
| Reviewed README | `exam-prep/reviewed/day-NN/README.md` |
| Cull log with evidence | Section inside reviewed bank |
| Prompt improvement signals | Section inside reviewed bank |
| Top-up guidance | Section inside reviewed bank |
| Approved-output checks | Section inside reviewed bank or generated review report |
| Cost summary | Section inside reviewed bank or generated run report |

## Component Architecture

### 1. Orchestrator

Coordinates the run for one day.

Responsibilities:

- validate requested day;
- load configuration and paths;
- load run budget, per-stage budgets, and escalation thresholds;
- call each stage in order;
- stop on hard gate failures;
- stop or ask for human approval when cost thresholds are reached;
- run top-up loops until completion or clear blocker;
- write a final run summary.

Example command shape:

```bash
python3 scripts/build_exam_prep_day.py --day 02 --plan
python3 scripts/build_exam_prep_day.py --day 02 --generate
python3 scripts/build_exam_prep_day.py --day 02 --review
python3 scripts/build_exam_prep_day.py --day 02 --top-up
python3 scripts/build_exam_prep_day.py --day 02 --check
```

### 2. Source Loader

Reads and normalizes local project inputs.

Responsibilities:

- parse curriculum-order rows for the requested day;
- read study guide, artifacts, and answer guidance;
- read official exam objectives from
  `source-material/ai-professional-01.objectives.json`;
- read question-bank specification;
- read existing reviewed banks for style and duplicate protection;
- verify remediation target files exist.

### 3. Topic Brief Builder

Creates one compact generation/review brief per curriculum-order topic.

Each brief should include:

```text
curriculum_order
topic
knowledge category/type
artifact evidence
official exam domain/task/skill
study guide remediation target
artifact remediation target
answer-guidance remediation target
concepts/procedures to test
common misconceptions
source-sensitive AWS claims
prior approved stems
prior rejected stem excerpts
```

### 4. Prompt Planner

Builds generation prompts from topic briefs and prior review feedback.

Prompt requirements:

- request surplus candidates, usually `12-15` per topic;
- require scenario-based items;
- avoid recall-only and keyword-trivia stems;
- require official objective traceability;
- require remediation targets that exist;
- require distractor rationales;
- include topic-specific rejected patterns to avoid;
- include existing approved stems for duplicate avoidance;
- flag source-sensitive AWS claims for source-checking.

### 5. Generation Adapter

Obtains candidate items.

Supported origins:

- external LLM generation;
- manual authoring;
- Codex-assisted authoring;
- reviewer-authored top-up;
- imported or transformed source.

The adapter must preserve true provenance. Provider/model metadata may only be
used for content actually produced by that provider/model.

The adapter must also return cost telemetry where available: model/provider,
input tokens, output tokens, request count, estimated cost, cached-token
discounts if applicable, and any retrieval/API charges the provider exposes.

The generation adapter should not be the only semantic judge of its own work.
If an LLM generates candidates, the judgment review should use one of:

- a different model/provider;
- an adversarial "refute this item" review prompt;
- a two-pass reviewer where the second pass defaults to reject or
  `needs-source-check` on uncertainty;
- a human reviewer for source-sensitive residuals.

This reduces correlated hallucination, where the same model family generates a
plausible false claim and then accepts it during review.

### 6. Raw Store

Persists candidate output verbatim.

Rules:

- raw output is evidence, not approved content;
- raw files must include provider/model/timestamp/provenance metadata;
- prompt text or prompt reference must be recoverable;
- raw files are never silently rewritten into "approved" form.

### 7. Normalizer

Converts raw candidates into the reviewed-bank schema.

Required normalized fields include:

- `item_id`;
- `status`;
- `curriculum_order`;
- `official_exam_code`;
- `exam_domain`;
- `exam_task`;
- `exam_skill`;
- `exam_skill_local` when useful;
- `knowledge_type`;
- `difficulty`;
- `stem`;
- `options`;
- `correct_answer`;
- `rationale_correct`;
- `rationale_distractors`;
- `misconception_tags`;
- `source_trace`;
- `remediation_target`;
- `raw_source`;
- `review_notes`.

Item IDs must be append-only and stable across top-up loops. For Pilot1, use:

```text
P1-AIP-D{day_number}-{NNN}
```

Rules:

- allocate the next free monotonic `NNN` for the day;
- never renumber approved or culled items after publication;
- never reuse an ID from a culled, retired, or rewritten item;
- top-up passes allocate from the next free block;
- item ID stability is checked before report writing.

### 8. Deterministic Reviewer

Applies checks that should not depend on LLM judgment.

Checks:

- schema completeness;
- stable item IDs;
- official domain/task/skill consistency;
- remediation target file existence;
- source trace presence;
- raw provenance presence;
- approved item counts per curriculum-order topic;
- difficulty and cognitive-demand field presence;
- exact duplicate stems;
- near-duplicate stems by normalized text similarity;
- stale or banned phrase scan across all learner-visible item surfaces;
- answer-position distribution for multiple-choice items;
- no hallucinated filenames;
- cull evidence presence.

The deterministic reviewer is not a factual verifier by itself. A clean
denylist scan means "no known rejected pattern was found," not "all technical
claims are true."

### 9. Judgment Reviewer

Uses LLM or human review for quality checks that require semantic judgment.

Checks:

- scenario realism;
- professional-level difficulty;
- correct answer uniquely best;
- distractors plausible but defensibly wrong;
- rationale teaches the intended distinction;
- item tests the intended knowledge type;
- item routes misses to the right remediation unit;
- item avoids pure recall when the topic requires conditional, procedural,
  causal, diagnostic, strategic, or normative evidence.

Judgment review may recommend edits, but the edited item must re-enter the
normalization and deterministic review path.

Judgment review should explicitly mark atomic technical claims that require
source verification. Examples include:

- service limits, quotas, supported file types, and Region support;
- API names, request fields, parameters, and response shapes;
- service capability comparisons;
- security, networking, encryption, IAM, or data-residency claims;
- dated or recency-sensitive availability statements.

When in doubt, mark the claim `needs-source-check` instead of approving it.

### 9A. Atomic Claim Verifier

The Atomic Claim Verifier checks source-sensitive technical claims against
official sources before approval.

Responsibilities:

- extract atomic claims from stems, options, correct rationales, distractor
  rationales, source traces, remediation notes, and review notes;
- retrieve or open the cited official source when available;
- compare the claim against current official documentation;
- classify each claim as `verified`, `unsupported`, `contradicted`, or
  `needs-human-review`;
- write claim-level evidence into review notes or cull evidence.

Resolution rule:

| Claim status | Action |
|---|---|
| `verified` | Item can continue through review. |
| `unsupported` | Cull or rewrite with a valid source trace, then rerun review. |
| `contradicted` | Cull; do not approve. |
| `needs-human-review` | Hold item out of approved bank until resolved. |

Unresolved `needs-source-check` or `needs-human-review` flags cannot ship in a
complete bank. They may appear only in an explicitly incomplete review slice.

### 10. Cull Evidence Logger

Writes auditable rejection records.

Every cull must include:

- structured reason code;
- human-readable explanation;
- observable evidence;
- raw source reference;
- topic;
- whether the failure should feed prompt improvement.

Examples:

```text
reason: duplicate-pattern
evidence:
  rejected_stem: ...
  matched_approved_stem: ...
  matched_item_id: ...
  match_type: near-duplicate
```

```text
reason: stale-claim
evidence:
  field: rationale_distractors
  matched_phrase: "as of early 2024"
  why_disqualifying: date-bound service limitation without current source trace
```

### 11. Coverage Gate

Determines whether the day is complete.

Minimum completion rule:

```text
approved_items_per_curriculum_order >= 10
```

For Day 2, with 10 curriculum-order topics:

```text
minimum approved items = 100
```

If any topic is short, the day is incomplete and the agent must produce top-up
guidance.

The coverage gate also checks distribution quality:

| Distribution check | Minimum expectation |
|---|---|
| Difficulty spread | Each completed topic should include more than one difficulty level unless a documented reason says otherwise. |
| Cognitive-demand spread | Each topic's approved set should reflect its mapped knowledge types, not collapse into recall-only items. |
| Knowledge-type coverage | Procedural, embedded, causal, conditional, strategic, diagnostic, or normative topics must include items that exercise those demands. |
| Answer-position balance | Correct answers should not cluster in one option position. |
| Bank-level official-domain coverage | Full exam simulation pools should approximate official domain weighting; daily practice banks may be equal per topic but must state that use. |

### 12. Top-Up Planner

Uses review failures to generate better candidates for underfilled topics.

Top-up prompt inputs:

- topic brief;
- approved count and deficit;
- highest-frequency cull reasons;
- examples of rejected stems;
- approved stems to avoid duplicating;
- source-sensitive claims to verify;
- requested surplus over exact deficit.

Top-up loops are bounded. Default maximum:

```text
max_top_up_iterations_per_topic = 3
```

After the maximum, unresolved deficits trigger human escalation and an
incomplete-bank report with the remaining blocker, not indefinite generation.

Top-up planning must also check remaining budget. If the expected top-up and
review cost would exceed the run budget, the agent should either reduce scope
to a documented incomplete slice or ask for human approval before spending.

The top-up loop repeats:

```text
generate -> raw store -> normalize -> review -> coverage gate
```

### 13. Approved-Output Checker

Scans the approved bank after review.

This is the regression check that catches false negatives in the reviewer.

Checks:

- no stale/banned phrases in approved stems, options, rationales, tags, source
  traces, or remediation notes;
- no missing official objective fields;
- no task/skill prefix mismatch;
- no duplicate or near-duplicate approved stems;
- no remediation target points to a missing file;
- no raw provenance gaps;
- no source-sensitive claim lacks source trace or `needs-source-check` status.
- no unresolved `needs-source-check` or `needs-human-review` flags in a bank
  marked complete;
- distribution gates still pass after final culls.

The bank cannot be marked complete if a disqualifying pattern survives in the
approved section.

### 14. Cost Monitor

Tracks spend and effort across the run.

Cost categories:

| Category | Examples |
|---|---|
| Generation | Candidate-item LLM calls, prompt-pack generation, top-up generation. |
| Judgment review | LLM or human semantic review passes, adversarial review. |
| Claim verification | Official-doc retrieval, source-check LLM calls, human residual review. |
| Deterministic processing | Usually local and cheap, but record if external services are used. |
| Human review | Time spent approving prompts, residual claims, or incomplete-bank decisions. |

Budget controls:

- set a run budget before generation starts;
- set optional per-stage budgets for generation, review, verification, and
  top-up;
- estimate cost before each generation, review, claim-verification, and top-up
  loop;
- stop automatically at a hard budget cap;
- warn at a soft threshold, such as 80% of the run budget;
- record cost per approved item and cost per curriculum-order topic;
- report when a cheaper mode was used, such as smaller review model,
  deterministic-only rerun, or human-authored top-up.

Cost estimates should use the best available basis at the time:

```text
estimated cost =
  planned candidate count
  x historical or configured cost per candidate
  x expected review/verification passes
```

When token telemetry is available, replace estimates with actual input/output
token and request costs. Human-review cost is tracked as effort and reported,
but it is gated by human approval rather than automatically stopped like token
or API spend.

In the Phase 2 Day 2 pilot, cost telemetry may be mostly manual because the
run can be manual or semi-automatic. The Cost Monitor becomes load-bearing in
Phase 3 when repeated LLM generation, judgment review, claim verification, and
top-up loops are automated.

Completion rule:

```text
The bank is not "production complete" unless the report states either:
  - cost was within budget, or
  - the authorized overage and reason are recorded.
```

### 15. Report Writer

Writes the reviewed package.

Required report sections:

- run metadata;
- raw source provenance table;
- coverage summary;
- approved-output checks;
- claim-verification summary;
- distribution summary;
- cost summary;
- prompt improvement signals;
- top-up guidance;
- review rules;
- approved items;
- culled items with evidence.

## Workflow

```text
Start day run
  -> Load inputs
  -> Build topic briefs
  -> Plan prompts
  -> Pre-spend cost check
  -> Generate candidates
  -> Store raw output
  -> Normalize candidates
  -> Deterministic review
  -> Pre-spend cost check
  -> Judgment review
  -> Pre-spend cost check
  -> Atomic claim verification for source-sensitive claims
  -> Update cost monitor
  -> Log culls with evidence
  -> Write reviewed bank draft
  -> Run coverage and distribution gates
       -> if incomplete: estimate top-up cost, then top-up loop
       -> if complete: approved-output checks
  -> Write final reviewed package
```

## Quality Gates

| Gate | Complete only if |
|---|---|
| Teaching substrate gate | Study guide, artifacts, and answer guidance exist and pass the reverse-test rule. |
| Source objective gate | `ai-professional-01.objectives.json` exists and exposes official domain, task, and Skill X.Y.Z statements. |
| Raw provenance gate | Every raw candidate source is honestly labeled. |
| Schema gate | Every approved item conforms to the question-bank schema. |
| Traceability gate | Every approved item maps to official objective, curriculum topic, source trace, and remediation target. |
| Factual verification gate | Every source-sensitive atomic technical claim is verified, culled, rewritten, or held out of the complete bank. |
| Review-evidence gate | Every culled item has reason code and observable evidence. |
| Coverage gate | Each curriculum-order topic has at least 10 approved items. |
| Distribution gate | Difficulty, cognitive-demand, knowledge-type, answer-position, and intended-use coverage checks pass. |
| Approved-output gate | Approved section is clean for known rejected patterns and regression checks. |

## Production Gates

These gates determine whether a run is operationally complete. They do not
change whether the reviewed bank is educationally good; they decide whether it
can be called a completed production run.

| Gate | Complete only if |
|---|---|
| Cost gate | Run cost is within budget, or authorized overage is recorded. |
| Iteration gate | Top-up loops stop at the configured maximum or have explicit approval to continue. |
| Human-resolution gate | Human residual reviews needed for source claims, budget overages, or incomplete topics are recorded. |

## Failure Modes And Agent Response

| Failure | Agent response |
|---|---|
| Teaching material missing for a topic | Stop and report teaching substrate blocker. |
| Official skill extraction missing | Stop or mark bank as source-incomplete; do not invent official skills. |
| Raw generation under-delivers | Generate surplus top-up candidates for affected topics. |
| Review culls heavily | Feed cull reasons into revised topic prompts. |
| Duplicate stems recur | Include approved and rejected stems in top-up prompts and tighten duplicate checks. |
| AWS service claim cannot be verified | Cull, rewrite with source evidence, or hold out as `needs-human-review`; do not approve as fact. |
| Approved-output check fails | Reopen review and cull or fix affected approved items. |
| Coverage remains short after `3` top-up iterations for a topic | Escalate to human review and emit incomplete reviewed slice with explicit blocker and top-up guidance. |
| Cost reaches soft threshold | Warn and require the next top-up/review plan to estimate remaining spend. |
| Cost reaches hard budget cap | Stop generation/review loops and emit incomplete slice or request explicit budget approval. |

## Implementation Plan

### Phase 1: Generalize The Day 1 Reviewer

Refactor Day 1-specific review code into day-parameterized modules:

```text
scripts/exam_prep_schema.py
scripts/exam_prep_sources.py
scripts/exam_prep_review.py
scripts/build_exam_prep_day.py
```

Keep deterministic checks in code.

Add deterministic distribution checks, append-only item ID allocation, and a
claim-verification interface before using the agent for a full Day 2 bank.
Add cost telemetry fields even if early runs estimate cost manually.

### Phase 2: Day 2 Production Run

Use the agent manually or semi-automatically to produce Day 2:

```text
Day 2 topic briefs
Day 2 prompt pack
Day 2 raw candidates
Day 2 reviewed bank
Day 2 cull evidence
Day 2 top-up loops
Day 2 approved-output checks
```

Before the first Day 2 raw file is written, record whether candidates are
external-LLM generated, Codex-assisted, manual, or mixed-origin.

### Phase 3: Agent Loop

Add orchestration for repeated top-up and review cycles, with a hard stop when
blocked by missing source material, missing teaching substrate, or persistent
coverage shortfall.

## Human Review Points

The agent should expose review points rather than hide them:

- before first generation prompt pack is used;
- after first cull summary;
- before approving unresolved source-sensitive AWS claims after automated
  verification;
- before exceeding the hard budget cap or continuing after a soft-threshold
  warning;
- after top-up pass if a topic remains short;
- before marking the final bank complete.

## Why This Architecture Matches The Day 1 Lessons

- It treats raw generation as evidence, not approval.
- It makes provenance explicit.
- It requires official skill-level traceability.
- It logs culls with evidence.
- It uses culls to improve prompts.
- It scans every learner-visible item surface.
- It tests the approved output for patterns the reviewer claims to reject.
- It adds claim verification so unknown false claims do not survive merely
  because no known banned phrase matched.
- It adds distribution gates so a bank is not complete merely because each
  topic has enough items.
- It refuses `mostly complete` as a completion state when the target is a full
  reviewed bank.
