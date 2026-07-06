# Pilot1 (AIP-C01) — Review: Days 1–3 Student Kits + Day 3 Question Bank

**Date:** 2026-06-29
**Pass:** quality review + constructive-adversarial pass, run under the
quality-first intent (below). Every metric was recomputed from source; automated
and self-reported pass/fail results were independently re-verified. Each finding
carries a **confidence tag** — *Verified* (checked against ground truth),
*Inferred* (reasoned from indirect evidence), *Sampled* (verified on a sample,
extrapolated to the rest) — and the findings were run through a self-disposition
pass (steelman each, keep what survives).
**Scope:** Day 1, Day 2, Day 3 student kits (teach / practice / feedback layers)
and the Day 3 exam-prep question bank.

> **Guiding intent (governs every recommendation).** Complete, wholesome
> learning on **both** the regular and accelerated paths. Quality is **never**
> cut to fit a time target. The accelerated path may flex to ~8 h/day within
> reason; genuine overflow is **called out**, not trimmed. Fill the quality,
> label the time.

---

## Headline

| Target | Verdict | One-line |
|---|---|---|
| Day 1 student kit | ✅ Passes | Gold standard for the `Embedded` knowledge type. |
| Day 2 student kit | ✅ Passes | Consistent, acceptable `Embedded` treatment. |
| Day 3 student kit | ❌ Not yet | One regression (D3-1) + small depth/labeling gaps. |
| Day 3 question bank | ⛔ Correctly **blocked** | Gate working as designed; 3 fixes needed. |

The most important *new* result: applying the Day-3 method-fit lens **backwards**
to Days 1–2 shows they **pass** it — which proves Day 3's main gap is a
**regression**, and makes the fix light (restore an existing pattern, not invent
new content).

---

## The `Embedded` / config-inspection lens (cross-day)

Several topics each day carry the `Embedded` / `Representation-Location`
knowledge type, whose method-fit — per the kit's governing rule *knowledge type →
teaching method* — is **inspecting real tool/console/API config**. Count of
worksheets that actually ship an Embedded/Inspection-Record artifact:

| Day | Embedded-typed topics | Worksheets with an Inspection-Record artifact | Result |
|---|---|---|---|
| Day 1 | 2 (order003, 008) | **3** | ✅ honored — order003 pre-names AWS services; order008 ships real Converse/InvokeModel JSON + model IDs + official doc links |
| Day 2 | 4 (order001, 003, 007, 008) | **4** | ✅ honored — every Embedded topic has an explicit "Embedded Inspection Record" + inspect-a-real-surface instruction (vendor-neutral on names, which is fine) |
| Day 3 | 8 (order004, 005, 009, 011, 012, 013, 014, 018) | **0** | ❌ regression — design tables only; header still claims the config-inspection form |

Day 3 should **restore the Days 1–2 Inspection-Record pattern**. It does *not*
need full AWS specifics (Day 2 proved vendor-neutral is acceptable); it needs the
inspection artifact back.

---

## Day 1 student kit — ✅ Passes

- **Map conformance** exact; teach / practice / feedback all present; per-topic
  worked exemplars in the answer guidance.
- **Gold standard for `Embedded`:**
  [order003](day-01-artifacts/day01-order003-aws-genai-service-landscape.md)
  has an inspection table pre-named with real AWS services per role (Bedrock,
  SageMaker, Lambda, API Gateway, Step Functions, OpenSearch / Bedrock KB,
  CloudWatch / X-Ray, IAM / VPC endpoints);
  [order008](day-01-artifacts/day01-order008-basic-bedrock-model-invocation.md)
  ships real Converse and InvokeModel JSON, a real model ID, and official AWS
  doc links — each with a verify-currency caveat.
- Temporal / stale sweep: clean. Unchanged since its prior clean review; no
  regression.

## Day 2 student kit — ✅ Passes

- **Map conformance** exact; three layers present; 258-line answer guidance with
  a worked exemplar per topic on a shared scenario.
- **`Embedded` honored consistently:** every Embedded-typed topic
  ([order001](day-02-artifacts/day02-order001-data-quality-validation-monitoring.md),
  [order007](day-02-artifacts/day02-order007-vector-store-architecture.md#L30),
  order008) carries an explicit "Embedded Inspection Record" artifact plus an
  instruction to inspect a real source/config surface. Vendor-neutral on service
  names — acceptable, and arguably better for staleness resistance.
- Temporal / stale sweep: clean. Unchanged since its prior clean review; no
  regression.

---

## Day 3 student kit — ❌ Not yet

### What is already strong (keep)

- **Map conformance on the classification fields is exact: 18/18** — every
  worksheet's `Knowledge category` + `Knowledge type` match the
  [category map](../../curriculum-model/aip-c01-topic-knowledge-category-map.md)
  rows order001–018.
- **Practice layer complete and consistent** — all 18 worksheets follow the same
  form; the self-scaffolding tables are the correct method-fit for the
  `Procedural` / `Conditional` topics.
- **Daily roll-up present and conformant** —
  [day-03-integration-decision-record.md](day-03-integration-decision-record.md)
  (Parts A–E + exit check) matches the plan's prescribed daily artifact.
- **[order006](day-03-artifacts/day03-order006-rag-quality-evaluation-retrieval-troubleshooting.md)
  is a model topic** — honors its `Tacit` / `Diagnostic` types honestly
  (symptom-to-layer table + one-fix-at-a-time runbook + incident note) and does
  not fake a form it never claimed.
- **Temporal / hallucination risk near-zero** — no stale dated claims; the
  worksheets are near-vendor-neutral, so the Day-1 fabricated-service traps don't
  apply.
- **Remediation sections** partially compensate for the missing exemplars by
  naming the failure mode to avoid.

### Findings

| # | Severity | Confidence | Finding | Evidence |
|---|---|---|---|---|
| D3-1 | **Defect (top)** | Verified | **`Embedded` Inspection-Record artifact dropped — a regression from Days 1–2.** 8 Day-3 topics carry the `Embedded` type and list "console/API configuration record or inspection worksheet" as an artifact family, but **0 of 18** Day-3 worksheets contain that artifact (vs 3/10 Day 1, 4/10 Day 2). Day 3 claims the form in the header but delivers only design tables. Breaks *knowledge type → method*. **Scope check (steelman survived):** of the 8 (order004, 005, 009, 011, 012, 013, 014, 018), **7 are genuinely config-inspectable** (vector store, retrieval API/MCP, Bedrock Prompt Flows, sync/async/streaming FM API, CloudWatch/X-Ray tracing); only order009 leans governance — so the regression holds across the set. Fix is light: restore the Days 1–2 pattern. | counts Day1=3 / Day2=4 / Day3=0 (full grep) |
| D3-2 | **Defect** | Verified | **Teaching layer too thin for the 18 topics, and breaks a cross-day promise.** The study guide is a ~100-line skeleton; topics the worksheets demand are never taught: **MCP** (order005), **Bedrock Prompt Flows** (order011), **reranking mechanics** (order002), **distributed-tracing spans** (order018), **RACI** (order009). Separately, Day 2 explicitly promises Day 3 covers hybrid search "in more implementation depth" — Day 3 delivers it as one table row. | [day-03 study guide](study-guides/day-03-advanced-retrieval-prompt-governance-api-resilience.md) (read in full); promise at [day-02 SG L213-215](study-guides/day-02-data-embeddings-vector-stores-rag.md#L213) |
| D3-3 | **Defect** | Verified | **Feedback layer has no worked anchor.** The answer-guidance makes a *deliberate, defensible* choice — "criteria, not one perfect answer," because Day 3 topics need tradeoff judgment. But as a pure rubric with zero worked instances, a solo learner cannot self-calibrate. Day 2 proved exemplars and divergence coexist. Fix: add 1–2 worked exemplars on a shared scenario, framed as "one strong answer among several." | [day-03-answer-guidance.md](day-03-artifacts/day-03-answer-guidance.md) (43 lines) vs Day 2 (258 lines, per-topic) |
| D3-4 | Nit (partly addressed) | Verified | **Day 3's time cost is acknowledged but not quantified.** The [README](README.md#L7) now states the quality-first intent ("compresses calendar time, not teaching quality… expect dense days to take 7–8 hours… keep the material and record overflow… don't skip evidence of mastery") — lands the intent. Remaining: no per-day time estimate (Day 3, the densest day at 18 worksheets, isn't specifically flagged), and the [plan Time Budget](../../curriculum-model/accelerated-7-day-plan.md#L37) still says a fixed "6 hours/day", now inconsistent with the README. **Do not trim content** — just label and reconcile. | README L7-12 vs plan L37-53 (both read) |
| D3-5 | Nit | Verified | **order011 header-vs-body.** Claims `Architecture decision record` + `configuration inspection worksheet`; body is Flow Sketch / Step Contract / Branching Decision — no ADR structure, no Prompt Flows config. Add the forms or trim the header. | [order011 L12](day-03-artifacts/day03-order011-prompt-chaining-branching-bedrock-prompt-flows.md#L12) |
| D3-6 | Nit | Verified | **Slides are a skeleton** (~1 KB). Acceptable as an outline, consistent with prior days; flagged for parity. | [day-03-slides.md](presentations/day-03-slides.md) |

### Day 3 student-kit fixes (by leverage)

1. **Restore the Embedded Inspection-Record artifact (D3-1)** to the 8
   Embedded-typed worksheets — the pattern Days 1–2 already use. Minimum: an
   "inspect a real config/source surface and record the observable fact" table.
   Stronger (Day-1 order003 style): pre-name the AWS surfaces (Bedrock KB
   ingestion-job status, OpenSearch `knn` index params, `InvokeModel` /
   `Converse` shape, CloudWatch / X-Ray) with a verify-currency caveat.
2. **Expand the teaching layer (D3-2)** — teach MCP, Bedrock Prompt Flows,
   reranking (recall-vs-precision / bi- vs cross-encoder), distributed-tracing
   spans, and RACI; deliver the hybrid implementation depth Day 2 promised.
3. **Add 1–2 worked exemplars (D3-3)** on a shared scenario, framed as "one
   strong answer among several" — preserves divergence, gives a calibration
   anchor.
4. **Label the time and reconcile the plan (D3-4);** trim/fill order011's header
   (D3-5); optionally flesh out slides (D3-6).

---

## Day 3 question bank — ⛔ Correctly blocked

**NOT learner-ready, and correctly BLOCKED by its own final gate** — the same
expected state as the Day 2 run (gate enforces, human verification pending), not
new breakage. Three fixes are required regardless of the verification outcome.

### Recomputed numbers (independently verified)

- **342 approved items**, all 18 topics present (≥10 each; order003 & order006 at
  the 11 floor). Cull math reconciles: 391 − 49 = 342.
- **Difficulty:** hard 157 / medium 130 / exam-plus 55; **no `easy`.**
- **Cognitive demand:** spread across diagnose / select / judge / optimize /
  etc.; **no `recall`.**
- **Duplicate stems:** 0.
- **`knowledge_type` / skill tags** conform to the curriculum map; no off-map
  skill tag (the prior Day-2 order010 off-map failure did **not** recur).
- **Temporal sweep clean;** the known-false "Bedrock has no VPC endpoint
  support" claim is **absent**.
- **Source verification: 342 / 342 = `needs-human-source-review`** (0 verified)
  → gate returns blocked.

### Findings

| # | Severity | Confidence | Finding | Evidence |
|---|---|---|---|---|
| QB-1 | **Blocking (by-design)** | Verified | Bank not learner-ready: final source-verification gate blocked; **0/342 verified, 342/342 unverified**. The gate *enforces correctly* (returncode 2, pipeline stopped) — same as Day 2. The open work is resolving the 342 human verdicts, not a code bug. | run-report status; bank: 342× the status field (grep -c = 342) |
| QB-2 | **Defect** | Verified | **Answer-position clustering: ~98% of single-answer items put the correct answer in position 1** (231 of 235 matched; 89% even counting 24 unparsed). The Day-2 rebalancer (which fixed Day 2 to ~25% each) did **not** run / is non-functional for Day 3. *Steelman considered & rejected:* "maybe rebalancing is a deliberately-later step" — doesn't hold; 98% is extreme regardless of stage, and Day 2 ran the rebalancer **before** producing its reviewed bank. Test-taking heuristic beats knowledge → teaching-integrity failure. | independently computed: pos1 231 / pos2 2 / pos3 1 / pos4 1 |
| QB-3 | **Defect** | Verified | **12 items have malformed `source_trace` paths** (the files DO exist — the *paths* are broken): 10 omit the `day-03-artifacts/` directory segment (order006 ×3, order010 ×7), 2 are bare filenames (order008). Their topic-siblings were culled for the same class of defect — inconsistent. | literal-path sweep: `MISS .../accelerated-7-day/day03-order006-*.md` ×3, `…order010-*.md` ×7; 2× bare `focused_artifact: day03-order008-*.md` |
| QB-4 | **Defect (gate gap)** | Verified | The review gate checks `source_trace` / `remediation_target` are **non-empty** (only rejects empty or the literal `"MISSING"`), never that the **path resolves** — which is why QB-3 survived. Harden it to fail on non-existent paths. | `scripts/pilot1_aip_c01/review_exam_prep_questions.py:370-373` (read directly) |
| QB-5 | **Defect (factual)** | Verified (this item); rate over others Sampled | **The keyed-correct answer is itself wrong.** order014 item P1-AIP-D3-150: correct answer = "Configure Lambda as an API Gateway HTTP integration with direct streaming enabled," rationale "Lambda's streamed HTTP responses (available through API Gateway)." **No such feature** — Lambda response streaming is via Function URLs / `InvokeWithResponseStream`; API Gateway buffers. Its source trace ("AWS Lambda streaming via API Gateway documentation") cites a doc that effectively does not exist. Shows why the 342-item human review matters — I read this one; I did **not** fact-check the other ~330. | bank L8196-8215 (read directly) |
| QB-6 | Nit (corrected) | Verified | **Earlier overstated by the first pass.** The checks file is *not* all-green: it marks "Final source verification \| **pending** \| needs-final-source-check: 342." So it does surface that the final gate is incomplete — though it says "pending," not "blocked," and doesn't point to the run-report's hard stop. Minor clarity gap, not a misleading all-pass. | [checks L12](../../exam-prep/reviewed/day-03/day-03-review-output-checks.md) (read directly) |
| QB-7 | Nit | Verified | Bank `README.md` stale ("contains the draft-normalized input for the review pass," lists 2 files, not the 14-file reviewed/blocked state); run report references `day-03-final-gate-report.md` / `…gates.json` that **do not exist** (gate never reached). | README L1-7; run-report L28-29; `ls` confirms no final-gate files |

### Gate enforcement (enforcing vs decorative)

- **Enforcing (good):** `verify_exam_prep_sources.py` blocks unless
  `needs-human-source-review == 0`. It did its job; source *presence* never
  counts as *verified* — correct design.
- **Partially decorative:** `review-output-checks` "required fields present" is
  presence-only (QB-4), so it green-lit the 12 broken paths (QB-3). (The checks
  file *does* mark final source verification "pending," so it is not a pure
  all-green — corrected at QB-6.)

### Question-bank fixes (priority)

1. **Do not ship.** Resolve the 342-item source-verification ledger (the gate's
   `next_action`), then re-run the final gate.
2. **Fix the answer-position rebalancer (QB-2)** and re-run over the whole bank —
   ~98% pos-1 must drop to ~25% each before this is usable for practice.
3. **Repair/cull the 12 malformed source-trace paths (QB-3)** — add the missing
   `day-03-artifacts/` segment or drop, consistent with how their siblings were
   culled.
4. **Harden the review gate (QB-4)** to fail on non-resolving trace/remediation
   paths so QB-3 cannot recur silently.
5. **Correct the order014 Lambda-streaming claim (QB-5);** refresh the bank
   README and checks-file presentation to state the blocked status (QB-6, QB-7).

---

## Coverage / limits

- **Student kits:** all Day-1/2/3 traceability fields checked vs the map; the
  Embedded/Inspection-Record count is a full grep over all three days; Day-1/2
  re-read focused on the 6 Embedded-typed worksheets; temporal sweep exhaustive.
  Days 1–2 non-Embedded checks rely on their prior clean reviews (artifacts
  unchanged since).
- **Question bank:** schema / distribution / position / links / temporal /
  cull-math checked **exhaustively** over all 342 items; QB-1–QB-7 each
  independently verified against source (recomputed metrics, read the gate
  script, read the flagged item and the checks/README files directly) — this
  recheck **corrected the first automated pass** on QB-2 (89→98%), QB-3 (14
  "missing files" → 12 malformed paths), and QB-6 ("all-green" → marks
  verification "pending"). Atomic factual correctness is **Sampled**: I read ~10
  items and verified QB-5 on one of them; the remaining ~330 are the human
  source review the gate is (correctly) demanding — deliberately not verified
  here, and tagged accordingly rather than asserted.
