# Exam Prep Agent Design Lessons

## Purpose

This document captures design lessons learned while reviewing the Exam Prep
Production Agent architecture.

It is narrower than the Curriculum Architecture Kit lessons register. The
focus here is agent architecture: how to design a governed agent that can
generate, review, normalize, verify, top up, and report exam-prep material
without hiding quality, provenance, cost, or factual-risk problems.

Primary architecture document:

[exam-prep-agent-architecture.md](exam-prep-agent-architecture.md)

Diagram:

[exam-prep-agent-architecture.drawio](exam-prep-agent-architecture.drawio)

## Lessons

### 1. Raw Generation Is Evidence, Not Approval

**Risk:** An agent that writes generated questions directly into a reviewed
bank blurs evidence collection with approval.

**Design rule:** Preserve raw candidates separately from reviewed normalized
items. Raw files need true provenance; reviewed banks need review status and
cull evidence.

**Applied in architecture:** `Raw Store`, `Normalizer`, provenance rules, and
reviewed-bank report sections.

### 2. Separate Deterministic Review From Judgment Review

**Risk:** LLM judgment is useful but nondeterministic. Mechanical checks should
not depend on semantic review.

**Design rule:** Keep schema validation, path existence, ID stability,
duplicate detection, stale-pattern scans, provenance checks, and count gates in
deterministic code. Use judgment review for scenario quality, distractor
plausibility, cognitive demand, and rationale quality.

**Applied in architecture:** `Deterministic Reviewer` and `Judgment Reviewer`.

### 3. A Denylist Is Not Factual Verification

**Risk:** A novel, confidently wrong technical claim can pass banned-phrase
scans if it does not match a known stale or false pattern.

**Design rule:** Add an atomic-claim verification stage for source-sensitive
claims. A clean stale-phrase scan means only that known patterns were absent,
not that every claim is true.

**Applied in architecture:** `Atomic Claim Verifier`, factual verification
gate, and unresolved `needs-source-check` handling.

### 4. Avoid Generator-Judge Correlation

**Risk:** If the same model family generates and reviews an item, the reviewer
may share the generator's blind spot.

**Design rule:** Use reviewer independence where possible: different
model/provider, adversarial review framing, multiple passes that default to
reject or source-check on uncertainty, or human review for residual
source-sensitive claims.

**Applied in architecture:** `Generation Adapter` and `Judgment Reviewer`
independence guidance.

### 5. Approved-Output Checks Catch Reviewer False Negatives

**Risk:** A review rule can be written correctly but implemented over the wrong
fields, letting a bad pattern survive in approved content.

**Design rule:** After review, scan the approved bank itself for known rejected
patterns, schema defects, duplicate stems, traceability gaps, provenance gaps,
and unresolved source-check flags.

**Applied in architecture:** `Approved-Output Checker`.

### 6. Cull Logs Must Improve The Next Prompt

**Risk:** If culls are only postmortem notes, the next generation pass repeats
the same mistakes.

**Design rule:** Aggregate cull reasons into prompt-improvement signals before
top-up generation. Include approved stems, rejected stems, dominant failure
patterns, and source-sensitive claims to avoid or verify.

**Applied in architecture:** `Cull Evidence Logger`, `Prompt Planner`, and
`Top-Up Planner`.

### 7. Completion Is More Than Item Count

**Risk:** A bank can reach `10` items per topic while still being poor:
all medium difficulty, all recall, answer positions clustered, or missing the
mapped knowledge-type demand.

**Design rule:** Keep the item-count gate, but add distribution gates:
difficulty spread, cognitive-demand spread, answer-position balance,
knowledge-type coverage, and official-domain coverage when assembling full
exam simulations.

**Applied in architecture:** `Coverage + Distribution Gate`.

### 8. State The Bank's Intended Use

**Risk:** Per-topic practice depth and full-exam simulation weighting are
different goals. Equal topic counts are useful for remediation, but official
exam simulations need domain/task weighting.

**Design rule:** State whether the reviewed bank is a per-topic practice pool,
a full simulation pool, or both. Use the right coverage rule for each use.

**Applied in architecture:** `Intended Bank Uses`.

### 9. Source-Check Flags Need A Resolution Policy

**Risk:** `needs-source-check` can become a parking lot. If unresolved flags
are allowed into approved banks, traceability looks present but factual
verification is incomplete.

**Design rule:** Define allowed statuses and actions:
`verified`, `unsupported`, `contradicted`, and `needs-human-review`.
Unresolved source-check or human-review flags cannot ship in a bank marked
complete.

**Applied in architecture:** `Atomic Claim Verifier` resolution table and
approved-output checks.

### 10. Item IDs Must Be Append-Only

**Risk:** Top-up loops can renumber or collide with existing IDs, making review
history and remediation references unstable.

**Design rule:** Allocate IDs monotonically and never reuse IDs from approved,
culled, retired, or rewritten items.

**Applied in architecture:** Normalizer append-only `P1-AIP-D{day}-{NNN}` ID
scheme.

### 11. Top-Up Loops Need Bounds

**Risk:** "Generate until complete" can become expensive or endless when a
topic is hard to fill.

**Design rule:** Set a maximum top-up iteration count per topic. After the
limit, escalate to human review and emit an incomplete-bank report with the
remaining blocker.

**Applied in architecture:** `max_top_up_iterations_per_topic = 3`.

### 12. Cost Is A Production Gate, Not A Content-Quality Gate

**Risk:** A bank can be educationally good but operationally unacceptable if
it exceeds budget or hides human review effort.

**Design rule:** Track cost by stage, run pre-spend checks before generation
and review loops, set soft and hard thresholds, and report cost per approved
item/topic. Treat cost as a production-completion gate rather than a content
quality verdict.

**Applied in architecture:** `Cost Monitor` and `Production Gates`.

### 13. Human Review Should Be Exposed, Not Hidden

**Risk:** An agent can appear autonomous by burying the places where human
judgment is still required.

**Design rule:** Make human review points explicit: prompt pack approval,
first cull summary review, residual source-sensitive claims, budget overages,
and incomplete-topic escalation.

**Applied in architecture:** `Human Review Points`.

### 14. Diagram Fidelity Matters

**Risk:** Architecture prose may contain a control that the diagram omits,
making the control easy to forget during implementation.

**Design rule:** Important controls should appear in both the document and the
diagram: official source inputs, claim verification, cost monitoring, top-up
guidance, and human review edges.

**Applied in architecture:** Updated draw.io lanes, nodes, and edges.

### 15. Long-Running Agent Steps Need Heartbeats

**Risk:** A long LLM generation or review run can appear stuck when stdout is
buffered or a single request takes a long time. This creates unnecessary
operator anxiety and makes it hard to decide whether to wait, interrupt, or
recover.

**Design rule:** Long-running steps must emit timestamped progress events to a
run log before and after each meaningful milestone. For generation, log
`run-start`, `run-item-start`, `api-request-start`, `api-request-complete`,
`file-written`, and `run-complete`. Write both a human-readable `.log` and a
machine-readable `.jsonl` stream so a monitor can draw a progress bar without
interrupting the process.

**Applied in architecture:** `scripts/generate_exam_prep_questions.py` writes
progress logs under `exam-prep/logs/day-XX/` and flushes console progress
messages immediately.

## Implementation Review Lessons (Day 2 First Run)

Lessons 1-15 came from reviewing the architecture. The lessons below came from
reviewing the first *implementation* and its Day 2 production run. The recurring
theme: a control can be present in the workflow and still not do its job. The
architecture was sound; the gaps were all in the distance between "stage exists"
and "stage works."

### 16. A Metric That Is Computed But Not Gated Is Decorative

**Symptom (Day 2 run):** Answer-position balance was computed and printed in the
gate report, but the `distribution_gate` pass condition only checked difficulty
spread, cognitive-demand spread, and multiple-response presence. A bank with
~96% of single-answer items in position A passed the gate as `pass`.

**Lesson:** Every metric a gate reports must either be part of the pass/fail
condition or be explicitly labeled report-only. A printed number next to a
`pass` reads as "checked and fine" even when nothing checked it.

**Required fix:** Diff "what is measured" against "what is enforced" for every
gate; wire reported distributions into the pass condition or mark them advisory.

### 17. Distinguish "Stage Present" From "Stage Functional"

**Symptom:** The `Atomic Claim Verifier` stage existed and ran, but it performed
no source retrieval or comparison; it blanket-marked all 119 items
`needs-final-source-check`. The factual-verification gate stayed `pending`, so
the highest-value control was effectively absent while appearing in the pipeline.

**Lesson:** A verifier that defers 100% of its inputs is not verifying. Track a
control's implementation status separately from its presence in the workflow,
and never let a stage name imply a capability the code does not yet have.

**Required fix:** Report per-stage functional status (real vs stub vs deferred),
and make the run summary foreground stubbed controls.

### 18. A Keyword Denylist Mislabels Real Concepts As Risky

**Symptom:** Items mentioning MCP, function calling, OpenSearch hybrid search,
and Rekognition frame extraction were culled as `unsupported high-risk claim` -
but these are real, examinable capabilities. The denylist conflated "term I
cannot verify" with "term that is wrong," and feeding those culls into
prompt-improvement trains the generator to avoid valid topics.

**Lesson:** Separate three distinct cull reasons that a denylist collapses into
one: out-of-scope-for-day, factually risky/unverified, and genuinely false. A
keyword ban must never be reported as a factual judgment.

**Required fix:** Reason-code culls precisely; keep an allowlist of known-real
terms out of the risk denylist; route scope issues to a scope check, not the
claim verifier.

### 19. A Hard-Coded Gate Verdict Is An Anti-Gate

**Symptom:** `iteration_gate` returned the literal `"pass"` unconditionally,
while a topic's logs (`order010-top-up-4`) suggested the top-up loop exceeded the
documented maximum of 3. The gate asserted success instead of checking it.

**Lesson:** A gate whose value is a literal rather than a computed check gives
false assurance and will never fail when it should. Audit every gate for whether
it reads state or hard-codes a verdict.

**Required fix:** Every gate must derive its status from observed run state;
ban literal pass values in gate code.

### 20. A Gate Is Only As Trustworthy As Its Telemetry Coverage

**Symptom:** The cost summary captured 2 top-up API calls (~23k tokens) and
omitted the initial generation of ~115 items. `api_calls: 2` for a 119-item bank
is not credible cost, so the cost gate's `recorded` status was based on a small
fraction of real spend.

**Lesson:** When instrumentation is opt-in per call path, some paths will be
missed, and any gate built on that telemetry silently under-reports.

**Required fix:** Assert telemetry completeness (for example, logged-call count
reconciles with generated-item count) before trusting a cost or coverage gate.

### 21. Honest Incompleteness Is The Safety Net - Do Not Let A Green Dashboard Bury It

**Symptom (positive, with a caveat):** The run correctly refused to mark the bank
approved (`completion_status: pending-final-source-verification`) and labeled
items `reviewed`, not approved - this prevented an unverified bank from shipping.
But the same `final-gates.json` showed most gates as `pass`, so a quick read of
the dashboard looked reassuring despite a stubbed verifier and a severe position
bias.

**Lesson:** The refuse-mostly-complete gate did its job even when downstream
controls were stubbed - preserve it. The danger is a dashboard of greens sitting
next to one honest `pending`; readers trust the greens.

**Required fix:** Gate dashboards should foreground the worst status, not an
aggregate of passes, and should name which controls were stubbed or deferred.

### 22. Forbid Generator Meta-Text In Learner-Visible Fields

**Symptom:** Generated items leaked reviewer-facing meta-commentary
("reviewer should confirm...", "reviewer must ensure ... is current") into
options and source traces. The denylist caught some only incidentally.

**Lesson:** The generator should never address the reviewer inside item content.
Relying on a risk denylist to catch this is accidental, not systematic.

**Required fix:** Generation prompts must forbid meta-commentary in
learner-visible fields, and deterministic review should detect and flag meta-text
explicitly rather than catch it by coincidence.

### 23. Trust The Implementation, Not Its Self-Report

**Symptom:** The gate JSON reported `distribution_gate: pass` and
`approved_output_gate: pass`; only reading the gate *code* revealed the
position-balance metric was never enforced.

**Lesson:** A run's own gate report describes what it believes, not what it did.
Reviewing the gate report alone would have missed every implementation defect
above.

**Required fix:** Implementation review must open the gate/verifier code and
independently recompute key metrics from the produced artifacts, not accept the
run's summary. (This generalizes beyond agents and is worth folding into the
quality review guide's techniques as an "implementation vs self-report" check.)

### 24. Final Fact Checking Is The Learner-Trust Gate

**Symptom:** Step 13 initially existed as a final gate, but claim-level source
verification was not functional. When the verifier was implemented, it found
that `P1-AIP-D2-083` should not be rescued with a citation: the item claimed
that increasing OpenSearch shard count was the best response to `Too many open
files`, a precise operational remediation that was unsupported and could teach
the wrong mental model.

**Lesson:** The final source/fact-check stage is not administrative cleanup.
It is the learner-protection gate. A weak item wastes practice time; a wrong
rationale trains the learner toward a false operational rule. Generation,
normalization, and review produce candidates. A bank earns learner trust only
after final fact checking can either verify each item or cull it with evidence.

**Required fix:** Treat Step 13 as non-negotiable for every day. It must reject
unresolved source markers, stale/current-capability claims without evidence,
unsupported service/API/operational claims, and known bad remediation patterns.
Any item culled during Step 13 must be added to the cull log with observable
evidence, and coverage must be recomputed after the cull before the bank can be
called complete.

## Implementation Checklist

Before implementing or running the agent for a new day, confirm:

- raw provenance is defined before the first candidate file is written;
- generation and judgment roles are independent enough for the risk level;
- atomic claim verification has official-source access or a human residual
  path;
- item IDs are append-only;
- top-up loops have a maximum iteration count;
- long-running generation/review steps emit progress logs and heartbeat events;
- distribution gates are configured for the bank's intended use;
- cost budget, soft threshold, hard cap, and telemetry fields are configured;
- report sections include provenance, culls, claim verification, distribution,
  cost, top-up guidance, and approved-output checks;
- final fact checking has a real verifier or explicit human-review path; it is
  not allowed to be a placeholder stage.

After a run, before trusting the gate report, also confirm:

- every reported metric is either enforced by a gate or labeled report-only
  (no decorative metrics, especially answer-position balance);
- no gate returns a hard-coded verdict; each derives status from run state;
- the claim verifier actually retrieved and compared sources, rather than
  blanket-marking items `needs-source-check`;
- Step 13 source/fact checking has zero unresolved source markers before a bank
  is called complete;
- any Step 13 factual cull appears in the cull log with the stem, challenged
  claim/rationale, and review finding;
- per-topic coverage was recomputed after final fact-check culls;
- telemetry is complete (logged calls reconcile with generated items) before
  trusting the cost gate;
- cull reason codes are precise (scope vs unverified vs false), and no real
  capability was culled as a high-risk claim;
- the gate dashboard foregrounds the worst status and names stubbed or deferred
  controls, so a row of `pass` cannot mask one `pending`;
- key metrics were independently recomputed from the produced bank, not taken
  from the run's own summary.
