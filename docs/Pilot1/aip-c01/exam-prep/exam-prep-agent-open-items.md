# Exam-Prep Agent — Open Items & Status Tracker

**Last updated:** 2026-06-23 (post answer-position rebalance + source-verification run, re-reviewed against the latest final-gate artifacts)
**Current Day 2 gate result:** `blocked` (correctly — both failing gates verified real)
**Source of record:** [`reviewed/day-02/day-02-final-gate-report.md`](reviewed/day-02/day-02-final-gate-report.md) (latest run)
**Companion docs:** [consolidated review](exam-prep-agent-consolidated-review.md) ·
[engineering disposition](exam-prep-agent-review-disposition.md)

This is the live record of what is still open, blocked, deferred, or decided.
IDs are stable across review docs (`COV-`/`IMP-` from the consolidated review;
`O-`/`D-`/`C-`/`N-` introduced here for tracking). Status is recomputed from the
current code, bank, and gate artifacts — not from any prior run summary.

## Status Legend

| Status | Meaning |
|---|---|
| 🔴 Blocked | Currently fails/pends a gate; bank cannot be approved until cleared. |
| 🟠 Open | Work owed to reach approved; not necessarily a gate failure today. |
| 🟣 Decision | A design choice to confirm intentionally; not a defect. |
| ⏭ Carry-over | Valid beyond Day 2; enforcement exists, will bite as later days are built. |
| 📝 Doc nit | Documentation-only correction. |
| ✅ Closed | Verified resolved this cycle (kept to prevent regression). |
| ⊘ Withdrawn | Finding retracted after adjudication. |

---

## 1. Blocked / Pending Items (current Day 2 gate = `blocked`)

| ID | Gate | Status | Detail | Evidence |
|---|---|---|---|---|
| B-1 | `traceability_gate` | 🔴 Blocked (fail) | `Day02-order010` items (`P1-AIP-D2-105`–`116`, 12 items) tagged to **off-map** Skill `1.5.6` (order010 does not map to it). | `topic_skill_mismatches` |
| B-2 | `coverage_gate` | 🔴 Blocked (fail) | Missing primary-skill coverage: **order003→`1.3.4`**, **order007→`1.5.3`**, **order010→`1.4.1`+`1.5.3`**. | `missing_mapped_skills` (independently reconciled — exact match) |
| B-4 | `factual_verification_gate` | 🔴 Pending | Verifier **has been run** (`day-02-source-verification.json` + report + claim ledger exist), but **0 of 118** items auto-verified; all 118 = `needs-human-source-review` (claim verdicts unresolved). | `source_trace_status_counts` |
| B-5 | `human_resolution_gate` | 🔴 Pending | Gated on B-4 (source residuals + blockers unresolved). | derived |

**Passing gates (do not regress):** teaching_substrate, source_objective,
raw_provenance, schema, review_evidence, **`distribution_gate`** (see B-3 in
§6 — answer positions now `23/23/23/22`, max single-position share `0.2527`),
approved_output, `cost_gate` (telemetry_complete: 13 calls / 203,304 tokens),
`iteration_gate` (1 observed iteration of 3 allowed).

## 2. Still-Open Work (to reach an approved Day 2 bank)

| ID | Status | Item | Notes |
|---|---|---|---|
| O-2 | 🟠 Open | **Resolve atomic-claim verification** for all 118 items (clears B-4/B-5). | `verify_exam_prep_sources.py` + the claim ledger have now been **run**, but every item returned `needs-human-source-review` (no auto-verification). Remaining work is the human source-review pass that supplies/confirms claim evidence so items can move to `source-verified`. |
| O-3 | 🟠 Open | **Repair order010 + the skill gaps** (clears B-1/B-2). | Regenerate `Day02-order010` onto its mapped skills `1.4.1`/`1.5.3` and drop off-map `1.5.6`; add a primary item for `1.3.4` (order003) and `1.5.3` (order007). |

## 3. Design Decisions To Confirm

| ID | Status | Decision | Trade-off |
|---|---|---|---|
| D-1 | 🟣 Decision | **Per-(topic, skill) coverage vs syllabus coverage.** The gate requires every mapped skill to have a primary item **in each topic that maps it**. | `1.5.3` is already covered globally (order009 primary-tests it), yet order007/order010 are flagged. Stricter guarantee (each topic exercises its mapped skills) but can pressure near-duplicate items across skill-sharing topics. Confirm strict, or relax to "covered in ≥1 mapped topic." |
| D-2 | 🟣 Decision | **Position threshold `≤ 0.50`.** | Lenient vs random ≈ 0.25 for 4 options. With O-1 landed the bank now sits at `0.2527`; consider tightening the threshold toward `~0.30` now that generation balances positions. |

## 4. Carry-Overs (Days 3–7)

Enforcement now exists for both; recorded so they are addressed as later days are
built rather than rediscovered.

| ID | Status | Item | State |
|---|---|---|---|
| C-1 | ⏭ Carry-over | **32 of 98 skills map to exactly one topic** (COV-3). Single points of failure if their one topic drifts. | `must_not_drift_skills` is now computed by the gate; verify each is primary-tested when its day is built. |
| C-2 | ⏭ Carry-over | **Overloaded topics** carry up to 11 skills (COV-4: Day07-order004=11, Day06-order033/Day07-order001=7). | Per-skill minimum is enforced; needs **surplus planning** so a multi-skill topic generates enough items per skill (not just ≥1). |

## 5. Documentation Nits (in the disposition doc)

| ID | Status | Item |
|---|---|---|
| N-1 | 📝 Doc nit | `exam-prep-agent-review-disposition.md` lines 103–105: self-contradictory sentence ("ignores the legacy signal **and** culls based only on that obsolete reason"). Code is correct; the sentence should be rewritten. |
| N-2 | 📝 Doc nit | Cost shows **13 calls** but only **8 `.jsonl` logs** exist; "reconstructed from raw API records" is plausible but the 8-vs-13 relationship should be stated so the number is auditable. |

## 6. Verified Closed This Cycle (do not regress)

| ID | Item | Verification |
|---|---|---|
| B-3 / O-1 | **Answer-position balance** (was `distribution_gate` blocker). | `scripts/rebalance_exam_prep_answer_positions.py` has landed; the bank's single-answer keys are now `23/23/23/22` across positions 1–4, max single-position share `0.2527` (≤ `0.50`). `distribution_gate` = **pass**. Was previously `0.934` (85 of 91 in position 1). |
| COV-2 | Per-skill coverage gate | Implemented + enforcing (`coverage_gate` includes `missing_mapped_skills`); independently reconciled. |
| COV-3 | Single-topic skill tracking | `must_not_drift_skills` computed. |
| IMP-1 | Real claim-ledger verifier (mechanism) | `verify_exam_prep_sources.py` (`source-verified` vs `needs-human-source-review`); items carry the ledger status. *(Verification has now been run; resolving the verdicts = O-2.)* |
| IMP-2 | Denylist over-cull removed | `HIGH_RISK_UNSUPPORTED` no longer active; survives only in historical logs. |
| IMP-3 | Answer-position gate | `distribution_gate` enforces `position_ok`. *(Generator-side balance landed — see B-3/O-1.)* |
| IMP-4 | Iteration gate | Event-derived (`iteration["within_limit"]`), no literal verdict. |
| IMP-5 | Cost telemetry | Complete capture (13 calls / 203k tokens); `cost_gate` checks completeness. |
| IMP-6 | Position parser | 0 unmatched answers in current bank. |
| — | Append-only IDs (ARCH-D) | 119→118 drop is one culled item (id 83), **not reused**. |
| — | Regression (schema/provenance/links/temporal/dups) | All prior-green checks still pass; no collateral breakage. |

## 7. Withdrawn

| ID | Item | Reason |
|---|---|---|
| ⊘ COV-6 | "Day 2 embedding/chunking mappings imprecise" | **Incorrect.** Official skill text confirms `1.5.2` = *select/configure embedding solutions* and `1.5.1` = *document segmentation*; order004→1.5.2 and order005→1.5.1 are faithful to the official hierarchy. |

---

### Path to "approved" (summary)

`blocked` → clear **O-3** (repair order010 and the 3 skill gaps → clears
B-1/B-2) + **O-2** (resolve the 118 `needs-human-source-review` verdicts →
clears B-4/B-5) → re-run gates. The answer-position blocker (B-3/O-1) is now
**resolved** and `distribution_gate` passes. Decisions **D-1/D-2** and
carry-overs **C-1/C-2** should be settled before scaling to Days 3–7. Doc nits
**N-1/N-2** are cleanup.
