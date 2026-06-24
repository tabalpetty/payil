# Exam-Prep Agent Consolidated Review Disposition

Date: 2026-06-23

This document records the engineering disposition of findings in
`exam-prep-agent-consolidated-review.md` after checking the current code and
rerunning the Day 2 gates.

## Correct Findings Fixed

| Finding | Disposition |
|---|---|
| COV-2 | Fixed. Final gates now validate each `(learning_unit, exam_skill)` pair against the canonical source-to-topic matrix and require at least one primary item for every skill mapped to each topic. |
| COV-3 | Fixed by enforcement. Single-topic skills are reported as `must_not_drift_skills` and are protected by the same per-skill coverage gate. |
| COV-4 | Fixed as a minimum sub-quota. Every mapped skill needs at least one primary item even when a topic maps to many skills. |
| COV-5 | Fixed. The Layer 0 audit now cites the specific curriculum orders from the traceability matrix as task evidence. |
| IMP-1 | Fixed conservatively. Source-file presence and service-name matching can no longer produce `source-verified`. Verification now requires an item-level atomic-claim ledger with source, evidence, and supported verdicts. |
| IMP-2 | Fixed. Legitimate concepts such as MCP, function calling, hybrid search, and frame extraction are no longer automatically classified as unsupported. Reviewer meta-text has a separate deterministic cull reason. |
| IMP-3 | Fixed. Answer-position parsing and balance are enforced by the distribution gate. |
| IMP-4 | Fixed. The iteration gate derives its verdict from structured top-up-loop events and the configured maximum. |
| IMP-5 | Fixed. Cost telemetry is reconstructed from all raw API response records and reconciled against external raw sources used by reviewed items. |
| IMP-6 | Fixed. Correct-answer matching normalizes labels and punctuation and uses `question_format` to identify multiple-response items. The current bank has zero unmatched answers. |
| IMP-7 | Fixed. Prompts prohibit reviewer commentary in learner-visible fields, and deterministic review now culls it under `reviewer meta-text`. |

## Incorrect Or Overstated Findings

### COV-6: Day 2 embedding and chunking mappings are imprecise

**Disposition:** Incorrect.

- `Day02-order004` maps to official Skill `1.5.2`, whose official wording is
  selecting and configuring embedding solutions.
- `Day02-order005` maps to official Skill `1.5.1`, whose official wording is
  document segmentation.

Task 1.4 covers vector-store solutions. Moving these two topics there would be
less faithful to the official objective hierarchy.

### IMP-4 evidence: `order010-top-up-4` proves iteration four

**Disposition:** Incorrect evidence; valid underlying gate defect.

The suffix `top-up-4` records the number of requested top-up candidates, not
the loop iteration. Structured loop logs show one observed iteration against a
configured maximum of three. The prior hard-coded iteration verdict was still
wrong and has been replaced with event-derived enforcement.

### IMP-1 wording: the verifier was a pure stub that verified nothing

**Disposition:** Overstated.

The verifier checked source-trace presence, rejected phrases, known bad claim
patterns, local source availability, and service-term presence. Those checks
were useful screening, but they did not justify the stronger
`source-verified` label because they did not compare atomic claims with
evidence. The corrected implementation retains screening and requires a claim
ledger before verification.

### COV-4 wording: overloaded topics cannot cover their skills

**Disposition:** Too absolute.

An 11-skill topic with 12 questions can technically provide one item per skill,
but it has almost no surplus for review culls or difficulty variation. The
engineering response is a per-skill minimum plus surplus planning, not an
assumption that coverage is impossible.

### Review snapshot: 119 items and pending source verification

**Disposition:** Stale count/status, though the quality concern was valid.

The current reviewed bank contains 118 items. The earlier blanket
`source-verified` result has now been withdrawn: all 118 correctly remain
`needs-human-source-review` until atomic-claim evidence is recorded.

## Current Verified Result

The corrected Day 2 gate result is `blocked`.

Passing controls:

- teaching substrate;
- official objective existence;
- raw provenance;
- schema;
- review evidence;
- approved-output regression scan;
- complete cost telemetry: 13 API calls and 203,304 tokens recorded;
- iteration limit: 1 observed iteration of 3 allowed.

Blocking or pending controls:

- 12 `Day02-order010` items use off-map primary Skill `1.5.6`;
- mapped primary-skill coverage is missing for `1.3.4`, `1.5.3` under
  `Day02-order007`, and `1.4.1`/`1.5.3` under `Day02-order010`;
- all 118 items await atomic-claim verification.

The bank is therefore a reviewed candidate bank, not a production-approved
bank.

The answer-position defect is now repaired in both production directions:

- the prompt builder requires balanced positions during generation; and
- an auditable deterministic transformation rebalanced the existing 91
  multiple-choice items to `23/23/23/22` across positions 1-4.

The distribution gate now passes with a maximum position share of `0.2527`.

Historical cull logs retain their original evidence for auditability. The
top-up prompt planner now ignores the legacy `unsupported high-risk claim`
signal and ignores historical culls whose only reason was that obsolete label.
Those records remain auditable but no longer train future generation away from
legitimate concepts.

Cost telemetry reports 13 API calls while the logs directory contains 8 JSONL
files because early generation responses preserved provider usage inside the
raw response files even when no corresponding progress log survived. The cost
gate reconstructs telemetry from all 13 raw API response records and
reconciles those records against the raw sources used by reviewed items.
