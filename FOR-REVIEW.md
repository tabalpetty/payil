# For the Reviewer — Start Here

Thank you for reviewing this work. This document is the map: what the project is,
what state it's in, where to start reading, and the caveats you should know before
you judge anything.

This is a public, docs-first repository. Everything referenced below is in the tree
exactly where the links point, so you can read it on GitHub directly. Build/dependency
folders (`node_modules`, `__pycache__`, `.next`) are git-ignored and not part of the
review.

---

## 1. What this project is (in one minute)

**payil** is a subject-agnostic **Curriculum Architecture Kit** — a method for
designing a multi-method teaching system around how knowledge actually works,
instead of converting a syllabus into uniform reading + multiple-choice. Its
governing rule is:

> **Domain structure determines learning order. Knowledge type determines teaching
> method. Mastery evidence determines progression.**

There are **two products**, and the distinction matters for review:

1. **The reusable Kit** (subject-agnostic) — [`docs/curriculum-architecture-kit/`](docs/curriculum-architecture-kit/).
   This is the durable intellectual contribution.
2. **Pilot1** (a deliberately disposable laboratory) — [`docs/Pilot1/aip-c01/`](docs/Pilot1/aip-c01/). It
   applies the Kit to a hard real target: the **AWS Certified Generative AI
   Developer – Professional (AIP-C01)** exam. Pilot1 exists to pressure-test the
   Kit, not to be a finished course.

A third strand is a **production-agent architecture**: an orchestrated
author → review → verify → release pipeline (with deterministic quality gates)
for generating teaching and assessment material. The exam-prep question-bank agent
is its first concrete implementation, and [`scripts/`](scripts/) is the running code.

---

## 2. Status at a glance (honest snapshot, 2026-06-23)

| Area | State |
|---|---|
| Kit methodology (spec, construction guide, production architecture) | **Mature**, internally consistent |
| Curriculum model (AIP-C01) | **Complete** — 133 dependency-ordered topics, two-axis knowledge classification, 5 domains / 20 tasks / **98 official skills mapped across 226 relationships**; Layer 0 source-decomposition audit **passes** |
| Student Kit | **Days 1–2 built** and pass content-quality review; **Days 3–7** have study guides + slides + learner worksheets, but not yet the full per-topic artifact/answer-guidance treatment |
| Teacher Kit | Accelerated 7-day facilitator guide in place |
| Exam Prep — Day 1 | **Approved** reviewed bank: 100 items, 10 per topic |
| Exam Prep — Day 2 | **First full agent-pipeline run; 118 items; final gate = `blocked`** (see §4) |
| Live pilot with real learners | **Not yet run** (the `my-run/` workbook is an intentionally blank template) |

The accelerated-track readiness gate is deliberately stricter than the real exam:
**≥82% overall, ≥72% per domain, completed in ≤170 minutes**, plus written error
analysis.

---

## 3. Where to start — pick your lens

You don't need to read everything. Choose the path that matches what you're
evaluating.

**A. "Is the *method* sound and reusable?"** (the core IP)
1. [`docs/project-charter.md`](docs/project-charter.md) — purpose, governing model, scope.
2. [`docs/curriculum-architecture-kit/teaching-system-specification.md`](docs/curriculum-architecture-kit/teaching-system-specification.md) — the spec: knowledge taxonomy, method library, schemas.
3. [`docs/curriculum-architecture-kit/curriculum-map-construction-guide.md`](docs/curriculum-architecture-kit/curriculum-map-construction-guide.md) — how ordering/classification/artifact choice is made explainable.
4. [`docs/curriculum-architecture-kit/quality-review-guide.md`](docs/curriculum-architecture-kit/quality-review-guide.md) and [`lessons-learned.md`](docs/curriculum-architecture-kit/lessons-learned.md) — how quality is checked, and what pilots have taught.

**B. "Is the *production agent / automation* well-designed?"**
1. [`docs/curriculum-architecture-kit/curriculum-production-agent-architecture.md`](docs/curriculum-architecture-kit/curriculum-production-agent-architecture.md) — the generic author/review/verify/release workflow.
2. [`docs/Pilot1/aip-c01/exam-prep/exam-prep-agent-architecture.md`](docs/Pilot1/aip-c01/exam-prep/exam-prep-agent-architecture.md) (+ the [`.drawio`](docs/Pilot1/aip-c01/exam-prep/exam-prep-agent-architecture.drawio) diagram) — the concrete exam-prep agent.
3. [`scripts/README.md`](scripts/README.md) then the pipeline scripts ([`build_exam_prep_day.py`](scripts/build_exam_prep_day.py) orchestrates; `generate_/normalize_/review_/run_*_final_gates/verify_*`). [`tests/test_exam_prep_agent_gates.py`](tests/test_exam_prep_agent_gates.py) shows the gates are enforced, not decorative.
4. [`docs/Pilot1/aip-c01/exam-prep/exam-prep-agent-design-lessons.md`](docs/Pilot1/aip-c01/exam-prep/exam-prep-agent-design-lessons.md).

**C. "Is the *Pilot1 application* faithful and traceable?"**
1. [`docs/Pilot1/aip-c01/README.md`](docs/Pilot1/aip-c01/README.md).
2. Curriculum model: [`accelerated-path-design.md`](docs/Pilot1/aip-c01/curriculum-model/accelerated-path-design.md), [`accelerated-7-day-plan.md`](docs/Pilot1/aip-c01/curriculum-model/accelerated-7-day-plan.md), [`aip-c01-topic-knowledge-category-map.md`](docs/Pilot1/aip-c01/curriculum-model/aip-c01-topic-knowledge-category-map.md).
3. Traceability evidence: [`source-to-topic-traceability-matrix.md`](docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md) and [`source-to-decomposition-coverage-audit.md`](docs/Pilot1/aip-c01/curriculum-model/source-to-decomposition-coverage-audit.md) (98/98 skills accounted for).
4. A built unit end-to-end: the Day 2 [study guide](docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-02-data-embeddings-vector-stores-rag.md) → [`day-02-artifacts/`](docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-artifacts/) (incl. `day-02-answer-guidance.md`) → [`day-02-rag-design-worksheet.md`](docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-02-rag-design-worksheet.md) → teacher [`facilitator-guide.md`](docs/Pilot1/aip-c01/teacher-kit/accelerated-7-day/facilitator-guide.md).

**D. "Is the *exam-prep output* trustworthy, and is the governance real?"** (most scrutiny here)
1. [`docs/Pilot1/aip-c01/exam-prep/README.md`](docs/Pilot1/aip-c01/exam-prep/README.md) and [`question-bank-specification.md`](docs/Pilot1/aip-c01/exam-prep/question-bank-specification.md).
2. The approved example: [`reviewed/day-01/day-01-reviewed-question-bank.md`](docs/Pilot1/aip-c01/exam-prep/reviewed/day-01/day-01-reviewed-question-bank.md) (100 items).
3. The Day 2 run — **read the gate report first**:
   [`reviewed/day-02/day-02-final-gate-report.md`](docs/Pilot1/aip-c01/exam-prep/reviewed/day-02/day-02-final-gate-report.md) → then the
   [`reviewed-question-bank.md`](docs/Pilot1/aip-c01/exam-prep/reviewed/day-02/day-02-reviewed-question-bank.md), the [`cull-log.md`](docs/Pilot1/aip-c01/exam-prep/reviewed/day-02/day-02-cull-log.md), and the [`source-verification-report.md`](docs/Pilot1/aip-c01/exam-prep/reviewed/day-02/day-02-source-verification-report.md).
4. Live status & adjudication: [`exam-prep-agent-open-items.md`](docs/Pilot1/aip-c01/exam-prep/exam-prep-agent-open-items.md) (the **single source of current status**) and [`exam-prep-agent-review-disposition.md`](docs/Pilot1/aip-c01/exam-prep/exam-prep-agent-review-disposition.md).

**E. "Why was it built this way?"** → the ADRs in [`docs/decisions/`](docs/decisions/) (`0001`–`0009`).

---

## 4. The Day 2 exam-prep run is `blocked` — and that's the point

The single most important thing to understand: **the latest Day 2 exam-prep run did
not pass its release gates, and we are showing it to you unedited.** This is a
feature of the design, not a failure we forgot to fix — the gates are meant to stop
an incomplete-or-wrong bank from being labeled "approved." The authoritative record
is [`day-02-final-gate-report.md`](docs/Pilot1/aip-c01/exam-prep/reviewed/day-02/day-02-final-gate-report.md).

Latest result (118 reviewed items):

- **Passing (9 gates):** teaching-substrate, source-objective, raw-provenance,
  schema, review-evidence, **distribution** (answer keys balanced `23/23/23/22`,
  max single-position share `0.2527` — an earlier run was badly clustered at
  `0.934` and was fixed by a generation-side rebalancer), approved-output, cost
  (13 API calls / 203,304 tokens), iteration (1 of 3 allowed).
- **Failing (2 gates):**
  - *traceability* — 12 Day02-order010 items are tagged to an **off-map** skill
    (`1.5.6`) that order010 doesn't own.
  - *coverage* — three mapped skills lack a primary item in their topic
    (order003→`1.3.4`, order007→`1.5.3`, order010→`1.4.1`+`1.5.3`).
- **Pending (2 gates):** *factual-verification* — the verifier **has been run**, but
  it auto-confirmed **0 of 118** items; all 118 are routed to
  `needs-human-source-review` (the design refuses to call source presence "verified").
  *human-resolution* is gated on that.

What this demonstrates: deterministic gates that genuinely enforce, plus an honest
open-items tracker. The remaining work to reach an approved Day 2 bank is itemized
in [`exam-prep-agent-open-items.md`](docs/Pilot1/aip-c01/exam-prep/exam-prep-agent-open-items.md) (items O-2, O-3).

---

## 5. Flags & caveats (please read before judging)

- **Some review notes are deliberately retained as *superseded* history.**
  [`exam-prep-agent-consolidated-review.md`](docs/Pilot1/aip-c01/exam-prep/exam-prep-agent-consolidated-review.md)
  is the original first-run critique; its figures (e.g. a "119-item bank", "not
  production-grade") are **out of date by design**. It carries a SUPERSEDED banner.
  For current truth, read the **disposition** and **open-items** files instead.
- **[`docs/decisions/conversation-handoff.md`](docs/decisions/conversation-handoff.md) is a historical handoff**, not current
  status. It predates the numbered ADRs; it has a dated status note pointing to the
  live trackers.
- **Primary vs. intermediate files in [`reviewed/day-02/`](docs/Pilot1/aip-c01/exam-prep/reviewed/day-02/).** The *primary* artifacts
  are the gate report, the `reviewed-question-bank.md`, the `cull-log.md`, and the
  `source-verification-report.md`. The `*-normalized-draft-*` and
  `*-reviewed-candidate-*` banks are large intermediate pipeline stages kept for
  auditability — you don't need to read them unless you're checking the cull math.
- **Generated spreadsheets/PDF are *views*, not the source of truth.** The canonical
  machine-readable source of the official exam objectives is
  [`source-material/ai-professional-01.objectives.json`](docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json)
  (with [`ai-professional-01.extracted.md`](docs/Pilot1/aip-c01/source-material/ai-professional-01.extracted.md) for human wording and the `.pdf` as the
  audit source of record). The `.xlsx` files are planning views.
- **Days 3–7 worksheets look "empty" on purpose.** Files like
  `day-03-integration-decision-record.md` are learner *evidence templates*; the
  teaching content for those days lives in [`study-guides/`](docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/) and [`presentations/`](docs/Pilot1/aip-c01/student-kit/accelerated-7-day/presentations/).
- **Pilot1 is intentionally disposable.** Critiquing AIP-C01 content is welcome, but
  the deeper question is whether the *Kit* (the reusable method) holds up — Pilot1 is
  the stress test, not the product.

---

## 6. How to verify our claims independently (optional)

The status claims above are recomputed from artifacts, not self-reported. If you
want to reproduce them, clone the repo and run from its root (Python 3):

```bash
# Layer 0: every official skill is mapped or explicitly deferred
python3 scripts/audit_source_decomposition_coverage.py --strict

# Re-run the Day 2 exam-prep release gates (regenerates the gate report/JSON)
python3 scripts/run_exam_prep_final_gates.py

# The enforcing-gate unit tests
python3 -m pytest tests/test_exam_prep_agent_gates.py
```

The captured outputs of those runs are already committed in
[`reviewed/day-02/`](docs/Pilot1/aip-c01/exam-prep/reviewed/day-02/) (`*.json` and `*-report.md`), so you can also just read them.

---

## 7. What feedback would help us most

- Is the **knowledge-type → teaching-method** mapping in the spec convincing, or does
  it over-claim? Where would a designer in a *different* subject get stuck?
- Are the **deterministic release gates** the right ones, set at the right strictness?
  (See the gate list in §4 and [`question-bank-specification.md`](docs/Pilot1/aip-c01/exam-prep/question-bank-specification.md).) What's missing?
- Is **traceability** (official skill → topic → activity → assessment item →
  remediation) actually preserved end-to-end, or does it break somewhere?
- Is the **Day 2 "blocked" disposition** the right call, or are we being too strict
  / not strict enough?

---

## 8. Repository map

```
README.md                      project front page + status
FOR-REVIEW.md                  this guide
AGENTS.md                      working rules / governing principles
docs/
  project-charter.md
  decisions/                   ADRs 0001–0009 + conversation-handoff (historical)
  curriculum-architecture-kit/ THE REUSABLE KIT
    teaching-system-specification.md
    curriculum-map-construction-guide.md
    curriculum-production-agent-architecture.md
    quality-review-guide.md
    lessons-learned.md
    tools/source-identity-workbench/   (V1 source-vetting web tool)
  Pilot1/aip-c01/              THE AIP-C01 LABORATORY
    curriculum-model/          topic map, traceability matrix, coverage audit
    student-kit/               7-day study guides, slides, per-topic artifacts
    teacher-kit/               facilitator guide
    exam-prep/                 agent architecture, specs, review notes, status trackers
      reviewed/day-01/         APPROVED bank (100 items)
      reviewed/day-02/         first agent run — gate = blocked (start at gate report)
      topic-briefs/, raw/      pipeline inputs/outputs (auditability)
    source-material/           official AIP-C01 objectives (json/md/pdf) + planning views
scripts/                       the production-agent pipeline (Python)
tests/                         enforcing-gate unit tests
```
