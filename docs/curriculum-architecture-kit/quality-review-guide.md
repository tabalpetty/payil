# Quality Review Guide

## Purpose

This guide describes how to review teaching-system artifacts for quality:
study material, learner worksheets/artifacts, answer guidance, exam-question
banks, curriculum maps, and the source-of-truth spine that links them.

It has two parts:

- **Part 1 - General review methodology** is subject-agnostic and durable. It
  belongs to the Curriculum Architecture Kit and should be reused by every
  pilot.
- **Part 2 - Applied to Pilot1 (AIP-C01)** binds the general method to this
  pilot's specific files, schema, and recurring failure modes. Treat it as the
  worked example, not a limit on what to check.

Related kit documents: [teaching-system-specification.md](teaching-system-specification.md),
[curriculum-map-construction-guide.md](curriculum-map-construction-guide.md),
[curriculum-production-agent-architecture.md](curriculum-production-agent-architecture.md),
[lessons-learned.md](lessons-learned.md). When a review reveals a reusable
lesson, record it in the lessons register and, if needed, fold it back into the
relevant spec.

---

# Part 1 - General Review Methodology

## Reviewer Mindset

Quality review is not proofreading and it is not approval-by-default. The job
is to find the gap between what a deliverable claims to be and what it actually
is, and to say so with evidence.

Operating principles:

- **Independence.** Review against the source of truth and the specification,
  not against the author's intent or your own memory. Open the files. Do not
  grade from assumption.
- **Evidence over impression.** Every finding cites a file, line, or command
  output. "This feels thin" is a hypothesis; quote the text that proves it.
- **Constructive skepticism.** Try to refute important claims and locate the
  teaching behind each activity, but do not manufacture defects to make the
  review look rigorous. Default unresolved factual claims to uncertain until
  the source confirms them; explicitly pass work that satisfies the standard.
- **Severity honesty.** Separate real defects from cosmetic nits from
  consciously-deferred scope. Do not inflate nits; do not bury defects.
- **No silent pass.** If you bounded coverage (sampled, checked only one day,
  skipped a section), say so. A review that hides its own gaps is a defect.
- **Faithful reporting.** If something is wrong, state it plainly with the
  evidence. If something is genuinely done, say so without hedging.

## What To Look For - General Issue Taxonomy

These are the cross-cutting failure classes. They apply to almost any artifact.

### 1. Factual correctness and hallucination

- Fabricated entities: services, APIs, parameters, model IDs, function names,
  config keys that do not exist or are misnamed.
- Plausible-but-wrong claims: technically-shaped statements that are simply
  untrue (the most dangerous class, because they read as authoritative).
- Stale/time-bound claims: "as of <year>", "currently does not support",
  "not yet available" - these rot. Flag every temporal claim and verify it.
- Invented references: links, citations, file paths, or doc URLs that do not
  resolve. A citation that does not exist is worse than no citation.
- Over-precise numbers: limits, quotas, prices, token counts stated as fact
  without a source. Verify or soften.

### 2. Bias

- Vendor/tool bias: presenting one product as the answer when the scenario
  allows alternatives; missing "reject when" conditions.
- Difficulty/representation bias (assessment): answer-position clustering,
  one obviously-correct option, distractors that are not plausibly tempting,
  over-representation of one sub-topic.
- Cultural/contextual bias: examples, names, or assumptions that only work in
  one locale or background when the material claims general applicability.
- Framing bias: leading questions, or teaching that asserts a contested
  practice as the single correct one.

### 3. Internal consistency and traceability

- Source drift: the artifact disagrees with the source-of-truth document
  (classification, ordering, naming, scope).
- Cross-file contradiction: two documents that must agree, do not (e.g. a
  plan says one thing, the map another).
- ID/tag drift: identifiers, tags, or controlled-vocabulary terms used
  inconsistently or invented beyond the defined set.
- Header-vs-body mismatch: the artifact promises (in a header, index, or
  metadata block) something the body does not deliver.

### 4. Completeness and coverage

- Missing prescribed elements: the spec/map requires N artifacts/sections/
  fields and fewer exist.
- Silent truncation: "top N", sampling, or a stopped-early process presented
  as if it were exhaustive.
- Coverage math that does not reconcile (e.g. raw minus culled does not equal
  approved).

### 5. Pedagogical soundness

- Method-type fit: the teaching/assessment method matches the knowledge type
  it targets (see the kit's governing rule: knowledge type chooses method).
- Teach/practice/feedback separation: exposition, retrieval practice, and
  answer calibration are distinct and present; a worksheet is not mistaken for
  teaching, and teaching is not just a blank worksheet.
- Altitude/cognitive load: depth matches the learner level and the time
  budget; not too shallow to build the skill, not so dense it cannot be done.
- Assessment quality: items are scenario-based where required, test the
  intended cognitive demand, and are not keyword-recall trivia.

### 6. Structure and mechanics

- Schema conformance: required fields/sections present and correctly typed.
- Link integrity: every referenced file/anchor exists.
- Naming conventions: file and identifier naming follows the documented
  pattern.

## Review Techniques - A Toolkit, Not A Checklist

Pick and combine techniques to fit the artifact. The point is to attack the
material from more than one direction; a single pass in a single direction
misses whole failure classes. Invent new techniques in this spirit.

### Inversion / reverse test

Run the dependency backwards. If artifact B is supposed to be completable using
artifact A, take each activity in B and try to complete it using only A. Where
you cannot, A has a teaching gap or B over-asks.

- *Example (this project):* take each worksheet activity and try to answer it
  using only the study guide + answer guidance. A blank you cannot fill from
  the taught material is a defect in the teaching, the worksheet, or both.
- Include glossary rows, retrieval cards, table labels, self-check prompts,
  and source-note labels in the reverse test. A term that appears in a
  worksheet but is only implied in the guide is still under-taught.
- Generalizes to: can the exam questions be answered from the study material?
  Can the runbook be executed from the reference docs cited? Can the exit-check
  be met by someone who only did the prescribed activities?

### Forward / sufficiency test

The complement of inversion. Walk the intended learner path forward and ask at
each step whether the prior material is sufficient to succeed at the next.
Surfaces "artifact without teaching" and ordering/prerequisite breaks.

### Triangulation against the source of truth

When three or more documents derive from one source, check them pairwise *and*
against the source. Drift usually hides in the second-order copy (the document
derived from the document derived from the source).

### Adversarial claim refutation

For each factual or evaluative claim, spawn a skeptic whose job is to refute it,
defaulting to "wrong/uncertain" unless the source proves otherwise. Useful for
plausible-but-wrong detection. For high-stakes claims, use multiple skeptics
with *different lenses* (correctness, security, does-it-reproduce) rather than
repeating the same check.

### Final fact-check gate

For generated assessment banks, treat final source/fact checking as the
learner-trust gate. Do not accept a bank as complete merely because schema,
coverage, and review culls passed. Confirm that every item has no unresolved
source marker and that learner-visible claims are verified or explicitly routed
to human review.

Check the full item: stem, options, correct rationale, distractor rationales,
misconception tags, source trace, and remediation target. Include operational
and remediation claims, not only product-capability claims. If final fact
checking rejects an item, verify that the cull log records the challenged claim
and evidence, then recompute coverage after the cull.

### Temporal-claim sweep

Grep for date and recency markers ("as of", "currently", "not yet", year
numbers) and verify each. Time-bound claims are the highest-rot, lowest-effort
defects to catch.

### Forward-reference sweep

Find concepts that are intentionally introduced before their full treatment.
Each one should be labeled as a forward reference and should name where the
learner will go deeper. This prevents a worksheet row from accidentally asking
for future-day depth.

### Reference/link existence sweep

Mechanically extract every referenced path/URL and confirm it resolves. Cheap,
fully automatable, catches an entire defect class (hallucinated links).

Also verify citation labels. A URL that resolves but is mislabeled can still
mislead the learner or maintainer about what source was checked.

### Implementation vs self-report check

For agent-generated artifacts, do not rely only on the agent's report. Open the
gate or verifier code when possible, and independently recompute key metrics
from the produced artifact. Look especially for decorative metrics that are
printed but not enforced, hard-coded `pass` statuses, placeholder verifiers,
and telemetry that covers only part of the run.

### Header-vs-body promise audit

Compare every "this contains / you will find / artifacts to create" promise
against what the body delivers. Mismatches are either missing content or an
over-claiming header - both are findings.

### Coverage matrix

Build a table of required-elements (rows) x present/absent (columns). Forces
every gap to become visible instead of being lost in prose. The deliverable of
many reviews should itself be a matrix.

### Cull / reconciliation audit (for filtered sets)

When a process narrows raw -> approved (questions, candidates, items), verify
the arithmetic, demand a per-item reason for each drop, and check that the stated
filter rules actually match what was dropped (and what survived - a rule that
should have culled a survivor is a missed defect).

Also check whether the cull summary fed the next generation or top-up prompt.
A workflow that keeps generating more candidates without addressing the prior
failure reasons is not improving; it is only increasing volume.

### Generated-material provenance audit

For AI-assisted, imported, scraped, or transformed materials, verify the three
layers exist where practical:

```text
prompt/source -> raw response or gathered material -> reviewed normalized artifact
```

Check that provenance labels are honest, provider/model metadata is not used
for content from another origin, and raw material is not presented as approved
curriculum content.

### Generated-workflow cost audit

For workflows that generate, review, verify, or top up materials through paid
models, APIs, or human review, check that the run records budget, stage-level
spend, soft-threshold warnings, hard-stop behavior, and authorized overages.
An agent that can loop should have a cost stop condition as well as a quality
stop condition.

### Distribution audit (for assessment banks)

Check spread, not just presence: difficulty mix, cognitive-demand mix,
answer-position balance, per-topic counts, duplicate-stem detection. Quality
hides in the distribution, not the individual item.

### Atomic technical-claim audit

For technical or high-rot domains, extract concrete factual claims from stems,
options, rationales, distractor rationales, and source notes. Verify claims
against official sources where possible. A clean stale-phrase or denylist scan
only proves known bad patterns were absent; it does not prove new claims are
true. Unresolved `needs-source-check` items should not appear in a bank marked
complete.

### Controlled-vocabulary conformance

When the project defines a fixed taxonomy/term set, verify every use conforms.
Flag outliers and short-form/long-form divergence. A one-off term is often a
typo or a concept that escaped the model.

### Regression on recheck

A recheck is not done when the reported fixes look correct in isolation. A fix
can correct one item and silently break another - delete teaching another
worksheet depended on, displace a section, shift a tag, introduce a new stale
claim. Verifying only the changed spot is how a "clean recheck" ships a new
defect.

On every recheck:

1. **Establish the blast radius first.** Compare against the prior reviewed
   state (git diff, or file-size/line-count deltas) to see *which files
   actually changed*, not just which were supposed to. A fix that was meant to
   touch one file but edited three is itself a finding.
2. **If changes are additive and confined**, previously-passing checks on
   untouched files cannot regress - say so, with the evidence (sizes unchanged),
   and scope the re-run accordingly. Do not assume confinement; prove it.
3. **Re-run the prior green checks, not only the changed spot.** At minimum the
   cheap mechanical sweeps (schema/tag conformance, link existence, temporal
   claims, structure/heading integrity) over the whole deliverable. These are
   automatable and catch collateral damage for almost no cost.
4. **Confirm the fix did what it claimed** and moved the item's rating, without
   over-correcting (e.g. a definition added in the wrong section, or a forward
   reference that now contradicts another day).
5. **Report net effect**, not just "fixed": state explicitly that no
   previously-passing item regressed, or name the one that did.

Keep a record of the prior pass (ratings, counts, sizes) so "did anything move"
is answerable mechanically rather than from memory.

### Reviewer calibration / self-disposition

A disposition reply - where the authors accept, dispute, or correct your
findings - is the highest-signal feedback a reviewer gets: a domain expert
adversarially checking your work. Do not treat it only as defenses to overcome.
Disputed findings cluster into recurring reviewer error-modes, and capturing the
pattern turns one-off corrections into calibration. Apply the same disciplines to
your own findings that you demand of the artifact's self-report.

Recurring error-modes to self-check before delivery:

- **Wrong-target-check** - calling a mapping or claim wrong by judging it against
  your *assumption* of the target, without reading the target's actual
  definition. (Recompute from source applies to your own finding too.)
- **Overstated verb** - "stub / verifies nothing / does nothing" when the thing
  does *less than required* but not *nothing*. Calibrate the verb to the evidence;
  only claim zero when you have shown zero.
- **Too-absolute** - "cannot / never / always" where the boundary case is
  reachable (e.g. 11 skills across 12 questions *can* be one each). Prefer
  "cannot do *well* / leaves no surplus."
- **Wrong-evidence** - citing an artifact name or field whose semantics you never
  confirmed (a filename token, a status string). A correct conclusion from wrong
  evidence is still a process miss - verify the evidence, not just the verdict.
- **Stale-snapshot** - quoting a count or state from an earlier pass. Re-snapshot
  at delivery time.

The loop:

1. **Self-disposition pass before sending.** For each of your own findings, write
   the authors' strongest rebuttal and try to defeat it. What survives ships;
   what does not gets downgraded or dropped.
2. **Tag each finding's confidence** (verified / inferred / suspected) so authors
   can triage, and so low-confidence findings are not stated as fact.
3. **After the real disposition, categorize every *valid* dispute** by error-mode
   above. The histogram over time exposes your systematic biases - that is the
   feedback signal. A finding the authors correctly overturned is not wasted
   experience; it is the most useful data point in the cycle.

## Severity Calibration

Label every finding. Suggested ladder:

- **Defect** - factually wrong, broken, missing required element, or unteachable.
  Must fix before the deliverable counts as done.
- **Nit** - cosmetic, stylistic, or a header-vs-body mismatch with no learner
  impact. Fix opportunistically.
- **Deferred-by-design** - a known, conscious scope limit (e.g. "minimum
  viable slice"). Not a defect; record it so it is not silently forgotten.

Do not let a long list of nits hide one defect, and do not promote a nit to a
defect to pad the review.

## Reporting Format

- Lead with the verdict and the single most important finding.
- Prefer a crisp table: one row per item reviewed, a fitness/severity column,
  and a notes column stating what is good, what is lacking, and where to
  improve.
- Quote evidence (file:line or command output) for each non-trivial finding.
- State coverage and its limits explicitly.
- End with a short, prioritized list of concrete next actions.

## When Is A Review Done

A review is complete when: every required element has been checked or its
omission noted; each finding has a severity and evidence; the source-of-truth
has been consulted (not assumed); and at least one inversion/adversarial pass
has been run, not just a forward read.

---

# Part 2 - Applied To Pilot1 (AIP-C01)

This part binds Part 1 to the AIP-C01 pilot. It will reference pilot-specific
paths; the techniques above are the durable part.

## The Source-Of-Truth Chain

Review derived documents against their upstream source, in this order:

```text
source-material/AIP-C01_Topics_Learning_Order_With_Knowledge_Type.xlsx   (133 topics: order, topic, knowledge type, teaching method)
  -> curriculum-model/aip-c01-topic-knowledge-category-map.md            (two-axis classification + "Artifact To Create" per topic)
  -> curriculum-model/accelerated-7-day-plan.md                          (day assignment, focus, exit checks)
  -> student-kit/accelerated-7-day/...                                   (study guides, artifacts/worksheets, answer guidance)
  -> exam-prep/...                                                       (raw -> reviewed question bank)
```

The xlsx is the spine. The category map is the primary contract for "which
artifact should exist for each topic and why". When a student-kit artifact and
the map disagree, the map wins unless the map itself is wrong against the xlsx.

## The Student-Kit Three-Layer Model

For each day, three distinct layers must each exist and be reviewed differently:

| Layer | File pattern | What it is | Primary review technique |
|---|---|---|---|
| Teach | `study-guides/day-NN-*.md` | Exposition - the actual teaching | Forward/sufficiency test; factual correctness |
| Practice | `day-NN-artifacts/dayNN-orderNNN-*.md` | Blank retrieval/self-explanation worksheets | Inversion test; method-type fit |
| Feedback | `day-NN-artifacts/day-NN-answer-guidance.md` | Worked exemplars / "what a 3 looks like" | Does every worksheet leg have an exemplar? |

A common confusion to pre-empt: the worksheet files only ask questions *by
design* - they are the practice layer, not the teaching. The review question is
not "does the worksheet teach" but "can the worksheet be completed from the
teach + feedback layers" (the inversion test).

## Student-Kit Review Checklist

For each day:

1. **Map conformance.** Every topic in the day's order range has an artifact;
   each artifact's `Knowledge category` and `Knowledge type` fields match the
   category map exactly; the prescribed "Artifact To Create" forms are present
   (or a deliberate, noted substitution per the map's artifact-selection rule).
2. **Inversion (fitness) test.** Every worksheet activity is completable from
   the study guide + answer guidance. Note any leg that is not.
3. **Teaching depth.** Adequate for every topic; intentional depth variation is
   fine, but flag any topic grazing the surface relative to what its worksheet
   demands.
4. **Forward references.** A worksheet must not require a concept taught only on
   a later day without labeling it a forward reference.
5. **Factual correctness.** Service roles, API names, request shapes, model
   IDs, parameters, and source URLs are accurate.
6. **Three-layer completeness.** Teach, practice, and feedback all present for
   the day.

## Exam-Prep Review Checklist

1. **Reviewed set exists.** `exam-prep/reviewed/day-NN/` is populated; raw is
   not the deliverable.
2. **Schema conformance.** Each item has the required fields (stable `item_id`,
   `status`, `exam_domain`/`exam_task`, `knowledge_type`, `difficulty`,
   `cognitive_demand`, real `source_trace`, real `remediation_target`).
3. **Tag reconciliation.** Domain/task/knowledge-type tags match the curriculum
   map; no invented categories; domain and task are mutually consistent.
4. **Link integrity.** Every `source_trace` and `remediation_target` path
   exists in the repo; source traces are *relevant* to the item, not boilerplate.
5. **Quality rules.** Scenario-based where required; no easy/keyword-recall
   trivia in the approved set; distractors are plausibly wrong for a real reason.
6. **Distribution.** Per-topic counts, difficulty spread, and cognitive-demand
   spread are sane; no duplicate stems.
7. **Cull reconciliation.** raw - culled = approved; each cull has a reason; the
   cull rules match what was actually dropped (and what survived).
8. **Temporal-claim sweep.** No stale dated claims in rationales/distractors.

## Known Recurring Failure Modes In This Pilot

History from prior reviews - check these first, they have bitten before:

- **Hallucinated remediation/source links** in raw question output (pointing to
  files that do not exist under different names). Always run the link-existence
  sweep on the reviewed bank.
- **Stale "as of early 2024 / does not yet support" claims**, especially the
  false "Bedrock has no VPC endpoint support" line. Bedrock *does* support VPC
  interface endpoints via PrivateLink. Run the temporal-claim sweep.
- **Header-vs-body artifact gaps** in the student kit: an artifact's
  `Artifact family` header lists a form (concept map, decision table, recall
  cards) the body does not deliver. Decide: add the form, or trim the header.
- **Controlled-vocabulary divergence**: the xlsx uses short forms (`Normative`,
  `Institutional`) vs the 15-type taxonomy's long forms (`Normative / Ethical`,
  `Institutional / Collective`); and a stray `Explicit` token appears at xlsx
  index 131 (likely should be `Implicit`). Artifacts mirror the xlsx, so they
  inherit the divergence.
- **Teaching concentrated in one guide**: early Day-1 versions taught only the
  first couple of topics richly and left the rest as blank worksheets over
  untaught material. The fix is the inversion test, applied per topic.

## Reusable Command Recipes

Read-only sweeps used in prior reviews. Adjust paths per day.

Link-existence sweep over a question bank:

```bash
F=docs/Pilot1/aip-c01/exam-prep/reviewed/day-01/day-01-reviewed-question-bank.md
grep -oE '`docs/Pilot1/[^`]+\.(md|pdf)`' "$F" | tr -d '`' | sort -u | while read f; do
  [ -f "$f" ] && echo "OK   $f" || echo "MISS $f"
done
```

Temporal / stale-claim sweep:

```bash
grep -niE 'as of (early |late )?[0-9]{4}|currently does not|does not yet|no current support' "$F"
```

Item-count and schema-field presence (each should match item count):

```bash
grep -oE 'P1-AIP-D1-[0-9]+' "$F" | sort -u | wc -l
for fld in item_id status exam_domain exam_task difficulty cognitive_demand; do
  printf "%-18s %s\n" "$fld" "$(grep -cE "\`$fld\`" "$F")"
done
```

Difficulty / cognitive-demand distribution and duplicate-stem check:

```bash
grep -E '\| `difficulty` \|' "$F" | sed -E 's/.*\| (.*) \|/\1/' | sort | uniq -c
grep -E '\| `cognitive_demand` \|' "$F" | sed -E 's/.*\| (.*) \|/\1/' | sort | uniq -c
grep -A2 '^Stem:' "$F" | grep -vE '^Stem:|^--|^$' | sort | uniq -d
```

Reading the xlsx spine (no external libraries needed):

```bash
python3 - <<'PY'
import zipfile, xml.etree.ElementTree as ET
f="docs/Pilot1/aip-c01/source-material/AIP-C01_Topics_Learning_Order_With_Knowledge_Type.xlsx"
z=zipfile.ZipFile(f); ns={'m':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
ss=["".join(t.text or "" for t in si.iter('{%s}t'%ns['m']))
    for si in ET.fromstring(z.read('xl/sharedStrings.xml')).findall('m:si',ns)]
sh=ET.fromstring(z.read('xl/worksheets/sheet1.xml'))
def col(r): 
    c="".join(ch for ch in r if ch.isalpha()); n=0
    for ch in c: n=n*26+ord(ch)-64
    return n
for row in sh.iter('{%s}row'%ns['m']):
    cells={}
    for cc in row.findall('m:c',ns):
        v=cc.find('m:v',ns)
        cells[col(cc.get('r'))]=ss[int(v.text)] if (v is not None and cc.get('t')=='s') else (v.text if v is not None else "")
    print([cells.get(i,"") for i in range(1,7)])
PY
```

## Reporting Template For This Pilot

Default to a per-topic (or per-item) table:

| Topic / item | Fitness or severity | Notes - good / lacking / where to improve |
|---|---|---|

Lead with the verdict, fence coverage ("Day 1 only; bank sampled at N items"),
and close with a prioritized fix list ordered by learner impact.
