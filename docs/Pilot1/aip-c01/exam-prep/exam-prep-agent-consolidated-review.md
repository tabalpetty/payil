# Exam-Prep Production Agent — Consolidated Review

> Engineering disposition and post-fix rerun:
> [exam-prep-agent-review-disposition.md](exam-prep-agent-review-disposition.md).
> The original findings below are retained as the review record.

**Status as of:** 2026-06-23 (working tree, branch `main`, uncommitted)
**Scope:** Architecture, cost model, implementation scripts, the Day 2 first
production run, and the syllabus→topic coverage decomposition.
**Subject of review:**

- `docs/Pilot1/aip-c01/exam-prep/exam-prep-agent-architecture.md` (+ `.drawio`)
- `scripts/` pipeline (`generate_/normalize_/review_/run_*_exam_prep_*.py`, `build_exam_prep_day.py`)
- `docs/Pilot1/aip-c01/exam-prep/reviewed/day-02/*` (first run output)
- `docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md`
  and the `source-to-decomposition-coverage-audit.*` layer

## How To Read This Document

This is a single cohesive review consolidating every finding raised across the
review cycles. It merges:

- findings that are **still open** (the bulk of this document), and
- findings that were **raised earlier and are now verified closed** (Appendix A,
  retained so the team has the full trail and does not regress them).

### Method

All quantitative claims were **recomputed independently from source artifacts**
(the official objectives JSON, the produced bank, and the gate/verifier code),
not taken from the run's own gate report. This is deliberate: a run's gate JSON
describes what the pipeline *believes*, not what it *did*, and several findings
below are cases where those diverge.

### Severity

| Level | Meaning |
|---|---|
| 🔴 High | Defeats a core guarantee of the agent (coverage, factual integrity, or an enforced gate). Must fix before any bank is called "approved/production-complete." |
| 🟠 Medium | Materially weakens a gate, metric, or output; does not by itself invalidate the bank but erodes trust in the pipeline's verdicts. |
| 🟡 Low | Precision, evidence-quality, or hygiene issue. |
| ✅ Good | Working as intended; called out to prevent regression. |

### Finding ID scheme

- `COV-n` — coverage / syllabus-decomposition findings.
- `IMP-n` — implementation / first-run findings.
- Appendix A retains the original `ARCH-/DIAG-/SCOPE-/COST-` IDs from the
  architecture and cost reviews (all verified closed).

---

## Executive Summary

**Verdict:** The architecture and cost design are sound and fully reviewed-closed
(Appendix A). The **syllabus→topic decomposition is structurally complete** —
independently confirmed 98/98 official skills mapped. However, the agent is **not
yet production-grade**, for two distinct reasons:

1. **The downstream coverage guarantee is missing.** Decomposition coverage
   (every skill maps to a topic) is achieved, but the pipeline gates per *topic*,
   never per *skill*. The Day 2 run already demonstrated silent skill drift that
   no gate caught (COV-2).
2. **Several architecture controls were closed in the spec but are stubbed,
   decorative, or hard-coded in the code.** The factual verifier, the
   answer-position gate, and the iteration gate all *appear* in the pipeline and
   report `pass`/`pending` while not actually doing their job (IMP-1, IMP-3,
   IMP-4).

The first run is **honest about being incomplete** (the bank is marked
`pending-final-source-verification`, items `reviewed` not approved), which is the
main thing currently preventing an unverified, biased bank from shipping.

### Open findings count

| Area | 🔴 High | 🟠 Medium | 🟡 Low |
|---|---:|---:|---:|
| Coverage (`COV`) | 1 | 2 | 2 |
| Implementation (`IMP`) | 3 | 3 | 1 |

(One coverage finding, COV-1, is ✅ Good and recorded to prevent regression.)

### Cross-cutting insight (most important takeaway)

Three architecture findings the team correctly resolved **in the design** are
**reopened by the implementation**:

| Design finding (closed) | Implementation reality (open) |
|---|---|
| ARCH-A: add an Atomic Claim Verifier | IMP-1: verifier is a stub; verifies nothing |
| ARCH-B: add distribution gate incl. answer-position | IMP-3: position balance computed but not gated |
| ARCH-E: bound top-up loop at 3 iterations | IMP-4: `iteration_gate` hard-coded `pass`; a topic hit iteration 4 |

The spec is good; the code does not yet honor it. Reviewing the gate **report**
would have missed all three — they are only visible in the gate **code**.

---

## 1. Coverage — Syllabus → Topic Decomposition

Context: the official AIP-C01 syllabus is **5 domains, 20 tasks, 98 skills**
(`X.Y.Z`). Every downstream step (topic briefs, generation, review, coverage
gate) is keyed by curriculum topic, so the topic decomposition determines whether
the syllabus is actually covered.

### COV-1 — Structural skill coverage is complete ✅ Good

Independently recomputed from `ai-professional-01.objectives.json` against
`source-to-topic-traceability-matrix.md`:

- **98 of 98** official skills appear in the matrix (0 orphaned).
- 226 skill→topic relationships; **130 of 133** topics mapped (3 foundation/
  integration topics legitimately unmapped).
- The deferrals register exists and is empty (no skills silently dropped).

The team's new coverage-audit layer is the right artifact and its headline claim
("98 of 98") is **true**. Retain and protect this. The remaining coverage
findings are about *quality and enforcement*, not structural gaps.

### COV-2 — No skill-level coverage gate; skill drift already occurred 🔴 High

The pipeline's coverage gate is **per topic** (`approved_items_per_curriculum_
order >= 10`), never **per skill**. A topic can be "complete" while a mapped
skill receives zero items.

This is not hypothetical. Tracing Day 2 topic→mapped-skill→tested-skill:

| Topic | Mapped skills | Skills tested in bank | Untested mapped skills |
|---|---|---|---|
| Day02-order010 (Basic RAG) | `1.4.1, 1.5.3` | `1.1.1, 1.5.6` | **`1.4.1, 1.5.3` (both)** |

`order010`'s generated items drifted entirely off its mapped skills, and **no
gate detected it**. Day 2's syllabus coverage survived only because `order007`
redundantly tests `1.4.1/1.5.3`. For any skill without that redundancy (see
COV-3), the same drift would produce a real, undetected coverage hole.

**Why it matters:** this is the exact failure mode the decomposition work is meant
to prevent — topic-level "complete" masking a skill with zero questions.

**Direction:** add a per-skill coverage gate — for every mapped skill, assert
≥1 approved item carries that `exam_skill`; block on drift.

### COV-3 — 32 of 98 skills map to exactly one topic (no redundancy) 🟠 Med-High

Topics-per-skill ranges 1–6. **32 skills are single-topic**, e.g. `1.3.1, 1.3.2,
1.3.4, 1.4.2, 1.4.3, 1.4.4, 1.4.5, 1.5.1, 1.5.2, 1.5.5, 1.6.1–1.6.4, 1.6.6,
2.1.2, 2.1.5, 2.1.7, 2.2.2, 2.4.2, 2.4.4, 2.5.2–2.5.4, 3.1.1, 3.1.4, 3.2.3,
3.4.2, 4.1.4` (and more).

Combined with COV-2 and the observed drift, these are single points of failure:
if the one topic carrying the skill drifts, the skill gets zero coverage with no
second topic to catch it.

**Direction:** mark single-topic skills as "must-not-drift" and verify each is
explicitly tested.

### COV-4 — Overloaded topics cannot cover their skills 🟠 Medium

Some topics carry far more skills than a per-topic question budget (~10–12) can
exercise:

| Topic | Skills mapped |
|---|---:|
| Day07-order004 | 11 |
| Day06-order033 | 7 |
| Day07-order001 | 7 |
| Day07-order002 | 6 |
| Day06-order032 | 5 |

At ~10–12 items/topic, an 11-skill topic yields <1 item/skill. The integration
days (6–7) are most exposed.

**Direction:** set per-skill sub-quotas for multi-skill topics, or split them.

### COV-5 — Coverage audit asserts rather than shows task evidence 🟡 Low

In `source-to-decomposition-coverage-audit.json`, every task's `evidence` is the
same generic pointer to `accelerated-7-day-plan.md`, not the specific topics
covering it. The granular evidence exists (in the traceability matrix), but the
audit JSON is effectively self-certifying.

**Direction:** cite matrix rows (specific topics) per task/skill in the audit.

### COV-6 — Some Day-2 skill mappings look imprecise 🟡 Low

Spot-check: embeddings (`order004`)→`1.5.2` and chunking (`order005`)→`1.5.1` are
tagged to *retrieval* (Task 1.5) skills, where vector-store (Task 1.4) skills look
like a closer fit. "Present in the matrix" does not guarantee "correctly mapped."

**Direction:** human correctness pass over the mapping, prioritizing the
single-topic skills (COV-3) where a wrong mapping has no backup.

---

## 2. Implementation — Pipeline & Day 2 First Run

The full workflow exists and ran end-to-end (objective extraction → 10 topic
briefs → prompts → per-topic generation → normalize → review/cull → bounded
top-up → gates → reports), parameterized by day. The defects below concern the
controls that separate a *candidate* bank from an *approved* one.

Reference run output: `reviewed/day-02/day-02-final-gates.json`,
`day-02-reviewed-question-bank.md` (119 items), `day-02-cull-log.md`.

### IMP-1 — Atomic Claim Verifier (§9A) is a stub 🔴 High

`review_exam_prep_questions.py:376` hard-codes every item's `source_trace_status`
to `needs-final-source-check`. There is no source retrieval, no comparison against
official documentation, and no `verified/contradicted` classification. Result: all
**119/119** items are unverified; `factual_verification_gate: pending`;
`completion_status: pending-final-source-verification`.

The headline control from ARCH-A exists as a stage name only. The bank's factual
correctness is currently unestablished.

**Direction:** implement retrieval-and-compare for source-sensitive atomic claims,
or label the bank "unverified candidate" wherever it is referenced.

### IMP-2 — Denylist over-culls real, examinable concepts 🔴 High

The `HIGH_RISK_UNSUPPORTED_PATTERNS` denylist culled valid capabilities as
"unsupported high-risk claim": **MCP, function calling, OpenSearch hybrid search,
Rekognition frame extraction**. These are real and examinable. Two problems:

- the cull *reason code* is factually wrong (they are not unsupported), and
- these culls feed prompt-improvement, training the generator to avoid valid
  topics.

(Separately, some of these items legitimately leaked reviewer meta-text — see
IMP-7 — but that is a different defect being caught for the wrong stated reason.)

**Direction:** split three distinct cull reasons the denylist conflates —
out-of-scope-for-day, unverified, genuinely false — and allowlist known-real terms
out of the risk denylist.

### IMP-3 — Answer-position balance is computed but not gated 🔴 High

`run_exam_prep_final_gates.py:280`:

```python
"distribution_gate": "pass" if len(difficulty) >= 2 and len(cognitive) >= 4 and "multiple-response" in format_counts else "review"
```

Answer-position balance is **computed and printed** but is **not** in the pass
condition. The Day 2 distribution: of matched single-answer MC items, **71 of 74
(96%) have the correct answer in position 1**. The gate reported `pass`.

**Direction:** wire position balance into the gate (after fixing IMP-6), and treat
any reported-but-unenforced metric as advisory only.

### IMP-4 — `iteration_gate` is hard-coded `pass` 🟠 Medium

`run_exam_prep_final_gates.py:283` returns the literal `"iteration_gate": "pass"`
— it checks nothing. Meanwhile `order010` reached `top-up-4`, above the documented
`max_top_up_iterations_per_topic = 3`. The gate cannot fail when it should.

**Direction:** derive the gate from observed top-up iteration counts; ban literal
verdicts in gate code.

### IMP-5 — Cost telemetry is incomplete 🟠 Medium

`final-gates.json → cost_summary.api_calls: 2` (~23.5k tokens) for a 119-item
bank. Only the two top-up calls were logged; the initial generation of ~115 items
produced no token telemetry. The cost gate's `recorded` status reflects a small
fraction of real spend.

**Direction:** instrument every call path; assert logged-call count reconciles
with generated-item count before trusting the cost gate.

### IMP-6 — Answer-position parser fails on 19% of items 🟠 Medium

`answer_position_counts.not-matched: 23` (of 119). Correct answers are restated as
full text and the matcher cannot map ~1 in 5 to an option position. The metric
behind IMP-3 is itself unreliable, so any gate built on it would be blind to a
fifth of the bank.

**Direction:** make the matcher robust (or emit position as structured data at
generation time) before enforcing IMP-3.

### IMP-7 — Generator leaks reviewer meta-text into learner-visible fields 🟡 Low

Generated items contained reviewer-facing commentary (e.g. "reviewer should
confirm…", "reviewer must ensure … is current") inside options and source traces.
The denylist caught some only incidentally.

**Direction:** forbid meta-commentary in learner-visible fields in the generation
prompt; detect/flag meta-text explicitly in deterministic review.

---

## 3. Strengths — Do Not Regress

- **Structural skill coverage (COV-1)** — 98/98 mapped, canonical traceability
  matrix, explicit deferrals register.
- **End-to-end pipeline** faithfully realizes the architecture's component
  decomposition; parameterized by day.
- **Provenance honesty** — every item carries `raw_provider/raw_model/
  raw_created_utc/raw_run_id`; raw files honestly named; dry-runs separated.
  `raw_provenance_gate` genuinely passes.
- **Append-only item IDs** (`P1-AIP-D2-NNN`) per the agreed scheme.
- **Auditable cull evidence** — reason codes + evidence excerpts + prompt-
  improvement signals.
- **Honest incompleteness** — the bank refuses to mark itself approved while
  source verification is pending. This is currently the load-bearing safeguard;
  preserve it.

---

## 4. Prioritized Remediation (review recommendation)

1. **COV-2** — add a per-skill coverage gate (≥1 approved item per mapped skill;
   block on drift). Highest leverage: closes the gap between "decomposition
   complete" and "syllabus actually covered."
2. **IMP-1** — implement §9A factual verification for real, or mark the bank
   unverified everywhere it is referenced.
3. **IMP-3 + IMP-6** — fix the position parser, then enforce answer-position
   balance in the distribution gate.
4. **IMP-2** — fix denylist precision (scope vs unverified vs false; allowlist
   real capabilities).
5. **COV-3 / COV-4** — flag the 32 single-topic skills as must-not-drift; add
   per-skill sub-quotas for overloaded topics.
6. **IMP-4** — make `iteration_gate` check real state.
7. **IMP-5** — capture all generation calls in cost telemetry.
8. **COV-5 / COV-6 / IMP-7** — granular audit evidence; correctness pass on
   mappings; forbid generator meta-text.

---

## Appendix A — Previously Raised, Verified Closed

Retained for the full trail and to prevent regression. Each was confirmed
resolved in a prior review cycle. **Note the three flagged `(reopened)`: closed in
the design, but not honored by the implementation (see §2).**

### Architecture review

| ID | Finding | Resolution | Status |
|---|---|---|---|
| ARCH-A | Novel hallucination passes denylist; need generator≠judge independence + factual verification | §9A Atomic Claim Verifier + independence rule added to spec | Closed in design — **reopened by IMP-1** |
| ARCH-B | Coverage gate ignored distribution & domain weighting | Distribution gate + answer-position + domain-weight rules added to spec | Closed in design — **reopened by IMP-3** |
| ARCH-C | `needs-source-check` resolution did not scale | 9A resolution table; unresolved flags block completion | Closed |
| ARCH-D | `item_id` stability across top-ups unspecified | Append-only `P1-AIP-D{day}-{NNN}` scheme; honored in run | Closed |
| ARCH-E | Top-up loop unbounded | `max_top_up_iterations_per_topic = 3` + escalation | Closed in design — **reopened by IMP-4** |
| ARCH-F | Per-topic knowledge-type mix ungated | Knowledge-type coverage added to distribution checks | Closed in design (enforcement shares IMP-3 risk) |

### Diagram fidelity

| ID | Finding | Status |
|---|---|---|
| DIAG-1 | "Official AWS docs / source notes" input missing from diagram | Closed |
| DIAG-2 | Human AWS-claim approval edge not wired | Closed |
| DIAG-3 | Outputs merged top-up guidance | Closed |

### Scoping

| ID | Finding | Status |
|---|---|---|
| SCOPE-1 | Practice bank vs exam simulation use undefined | Closed (Intended Bank Uses) |
| SCOPE-2 | Honest generator-of-record unstated | Closed |

### Cost model

| ID | Finding | Status |
|---|---|---|
| COST-1 | Cost mixed into content-quality gates | Closed (separate Production Gates) |
| COST-2 | Workflow under-represented pre-spend gating | Closed (pre-spend checks at each spend point) |
| COST-3 | Cost-estimation basis undefined | Closed (estimation formula added) |
| COST-4 | Human cost cannot be auto-gated | Closed (tracked-not-gated, stated) |
| COST-5 | Phase-2 manual run has little to meter | Closed (load-bearing in Phase 3, stated) |

---

## Appendix B — Evidence & Reproduction

Key figures in this review were produced by:

- **Syllabus counts (5/20/98):** parse `domains[].tasks[].skills[]` in
  `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`.
- **Skill coverage (98/98), single-topic skills (32), topics-per-skill,
  overloaded topics:** parse skill IDs (`\d+\.\d+\.\d+`) and `Day0N-orderNNN`
  tokens from `source-to-topic-traceability-matrix.md`; set-compare against the
  98 official skill IDs.
- **Day-2 topic→skill drift (COV-2):** intersect matrix-mapped skills per
  `Day02-orderNN` against `Skill X.Y.Z` tags per `learning_unit` in
  `reviewed/day-02/day-02-reviewed-question-bank.md`.
- **Position bias / distribution / cost figures:** `reviewed/day-02/
  day-02-final-gates.json` (`answer_position_counts`, `difficulty_counts`,
  `cost_summary`), cross-checked against the bank text.
- **Gate/verifier defects (IMP-1/3/4):** read
  `scripts/run_exam_prep_final_gates.py` lines 280, 283 and
  `scripts/review_exam_prep_questions.py` line 376.

All counts were recomputed from these artifacts rather than read from the run's
gate summary.
