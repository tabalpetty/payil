# Day 3 Question Generation Improvement Experiment Log

Status: consultation draft  
Course instance: Pilot1 AIP-C01  
Scope: Day 3 exam-prep question bank generation and source verification  
Purpose: summarize what we tried to improve Day 3 question quality, how each attempt failed or partially worked, and what measurable result we got.

## Context For External Reviewers

Payil is a curriculum-generation project. The broader goal is to build a subject-agnostic Curriculum Architecture Kit: a reusable way to design rich learning systems with study guides, activities, assessments, remediation, teacher materials, student materials, and exam-preparation artifacts.

Pilot1 is the first implementation of that architecture. It targets AWS Certified AI Practitioner, also known as AIP-C01. The pilot includes a 7-day accelerated learning path. Day 3 is one day inside that accelerated path and covers a subset of the AIP-C01 domain objectives.

The specific problem in this memo is exam-prep question generation for Day 3. We are using LLM-assisted generation to create difficult, realistic, certification-style questions. The desired questions should not be simple reading-check questions. They should test applied understanding, misconceptions, decision boundaries, and real AI/ML tradeoffs.

However, because this is certification preparation, every correct answer must also be defensible. For AWS factual claims, the answer should be grounded in official or otherwise trusted source material. The system therefore tries to preserve traceability from:

- AIP-C01 objective
- Day 3 topic
- generated question
- correct answer
- rationale
- source URL or local source path
- evidence span
- verification status

The quality target is not merely "generate many questions." A usable question bank should satisfy all of these:

| Requirement | Meaning |
|---|---|
| Topic coverage | Each Day 3 topic has enough usable questions. |
| Skill coverage | Official AIP-C01 skills mapped to Day 3 are represented. |
| Question quality | Questions are tough, realistic, and conceptually meaningful. |
| Source defensibility | Correct answers are supported by trusted evidence. |
| Low human-review burden | Automation should leave only a small review tail for humans. |

The core tension: attempts to make the generation more source-grounded sometimes made the prompts heavier and the questions more compliance-shaped. Attempts to make the prompts leaner improved candidate survival but did not solve source verification. This memo records those attempts and their results.

## Executive Summary

The Day 3 question-generation work improved some mechanical parts of the pipeline, but it did not solve the core problem: producing tough, high-quality questions whose correct answers are defensibly grounded in authoritative sources with low human-review burden.

The main pattern is clear:

- Prompt changes improved formatting, coverage count, and sometimes culling rate.
- URL checks confirmed that many cited URLs are reachable.
- Source verification remained the failure point.
- The stricter we made the source contract, the more visible the grounding weakness became.
- The later lean prompt improved generation focus and reduced schema burden, but it still produced a very large unresolved source-verification tail.

Current active Day 3 status is not review-ready.

The current active Day 3 bank has:

| Metric | Result |
|---|---:|
| Normalized candidates | 250 |
| Reviewed candidates | 222 |
| Culled candidates | 28 |
| Topics with count coverage | 18/18 |
| Reachable source URLs | 20/20 |
| Source-verified items | 52 |
| Needs human source review | 170 |
| Human-review tail | 170/222 = 76.6% |
| Final gate status | Blocked |

The most important conclusion: prompt-only improvement has not been enough. We need a different generation architecture that starts from problem/challenge understanding plus curated source evidence, not just from source URLs or a source catalog.

## What We Tried

| # | Attempt | Intended Improvement | Result | How It Failed Or Partially Failed |
|---:|---|---|---|---|
| 1 | Baseline Day 3 generation with tough/tricky question prompts | Produce enough exam-like questions per Day 3 topic | Generated a sizable Day 3 bank, but many items required source review | It could create plausible questions, but source grounding was weak. Many citations or source traces were not machine-verifiable. |
| 2 | Increased per-topic volume and top-up generation | Ensure each Day 3 topic had at least the required number of usable questions | Coverage by topic count became achievable after top-ups | More questions did not mean better grounded questions. Volume helped count coverage but did not reduce source-verification failures. |
| 3 | Stronger prompt guardrails: tricky, tough, no easy trivia, at least 10 per topic | Improve intellectual demand and reduce shallow recall questions | Some shallow items were culled; current lean redo shows only 4 keyword-trivia defects after strict review | Guardrails helped with one visible quality defect, but they did not make answers source-defensible. The model could still write plausible but poorly grounded scenarios. |
| 4 | Continuous-learning prompt updates from prior review defects | Feed lessons learned back into later Day 3 generation | Defect awareness was added to prompts and scripts | This improved process awareness but did not automatically fix the underlying generation behavior. The model still produced many items whose source evidence could not be verified deterministically. |
| 5 | Full source-grounded generation contract | Force each item to include source contract fields, allowed source ID, source trace, evidence span, and atomic claims | Produced 212 reviewed candidates after strict review | Source verification still failed badly: 59 source-verified, 153 needing human source review. Human-review tail was 72.2%. The prompt contract produced more fields, but not reliably verifiable evidence. |
| 6 | Course-level source catalog | Avoid ad hoc citations and make all generations cite from a known course source list | Created/used `source-catalog.json` and moved toward allowlisted sources | The catalog helped define allowed sources, but source URLs alone were not enough. The model needed exact source evidence, not just source names or URLs. Also, some local teaching docs were weak support for AWS factual claims. |
| 7 | Machine URL verification | Remove dead or hallucinated URLs from the review burden | Older strict run: 55/55 URLs reachable. Current lean redo: 20/20 URLs reachable | URL reachability is necessary but insufficient. A reachable AWS page does not prove that the item's answer is supported by the cited evidence span. |
| 8 | Source-review triage buckets | Understand why `needs-human-source-review` remained high | Earlier unresolved items split into buckets including AWS-grounded, local-grounded, placeholders, fetch failures, and `NONE` | Triage clarified the failure shape but did not itself fix generation. It showed many items had source text or local sources available, yet no decisive support verdict. |
| 9 | Placeholder/source-trace cleanup in prompts | Eliminate `source_trace_needed`, vague source traces, and unsupported claims | Reduced obvious placeholder-style failures in the current lean redo | The newer failure shifted from missing source traces to evidence not being strong enough or not being fetched/matched for deterministic verification. |
| 10 | Grounded LLM judge proposal | Use another model pass to decide whether source evidence supports a claim | Not adopted as the main fix because it increases LLM dependency | The user correctly challenged this as using more LLM calls to repair LLM-created defects. It may still be useful for a small semantic tail, but it should not be the primary quality strategy. |
| 11 | Automation tail thresholds | Make unacceptable human-review burden visible and blocking | Added threshold monitoring: LLM repair/judge tail <= 15%, human source-review tail <= 5% | This succeeded as a detection/gating improvement, not as a generation improvement. It now blocks Day 3 correctly instead of letting a weak bank appear review-ready. |
| 12 | Lean focused prompt | Reduce cognitive load on the model by asking only for question, answer, source trace, evidence span, and defensible answer | Current redo produced 250 normalized candidates, 222 reviewed, 28 culled | It improved schema/culling behavior compared with the full-contract run, but worsened or failed the source tail: only 52 verified, 170 unresolved, 76.6% human-review tail. |
| 13 | Post-generation enrichment pass | Let scripts fill metadata, remediation fields, difficulty, cognitive demand, source contract version, and atomic claims after the LLM writes the core item | Enrichment worked mechanically and reduced prompt burden | It cannot invent true source grounding. If the generated evidence span is weak or mismatched, enrichment only makes the item more structured, not more correct. |
| 14 | Top-up generation under lean prompts | Repair short topics without regenerating everything | Added top-ups for short topics and reached per-topic count coverage | First top-up normalization treated suffixes such as `order015-top-up-12` as separate topic IDs, causing false culls. This was patched. Count coverage passed, but source verification remained blocked. |
| 15 | Normalizer patch for top-up run IDs | Correctly map top-up files back to their base Day 3 topic | Fixed topic mapping for top-up files | This fixed a pipeline bug, not question quality. It helped coverage accounting but not source defensibility. |
| 16 | Source ledger initializer patch | Use generated atomic claims instead of generic keyed-answer claims | Source-verified count improved from 24 to 52 | Still left 170 unresolved. This showed that some verification failure was caused by ledger initialization, but most failure remained in evidence quality or verifier/source mismatch. |
| 17 | Strict final gate after lean redo | Prevent false "review ready" status | Final status is now blocked with clear blockers | This is the correct gate behavior, but it confirms the generation strategy is still not producing a review-ready Day 3 bank. |

## Detailed Observed Results

### Full Source-Grounded Contract Run

This was the heavier prompt version. It asked the model to produce the full structure up front, including source contract fields and atomic claims.

Observed results:

| Metric | Result |
|---|---:|
| Strict-reviewed candidates | 212 |
| Culled candidates | 607 |
| Per-topic coverage | Complete |
| Reachable AWS URLs | 55/55 |
| Source-verified items | 59 |
| Needs human source review | 153 |
| Human-review tail | 153/212 = 72.2% |
| Status | Blocked / pending final source verification |

Failure mode:

The model complied with the larger schema often enough to produce candidates, but the source evidence was not reliably strong, exact, or machine-verifiable. The large schema also appeared to burden generation, increasing culls and making the prompt more about satisfying fields than writing excellent questions.

### Lean Focused Redo

This was the later attempt to reduce prompt burden. The model was asked for fewer fields:

- question stem
- options
- correct answer
- rationale
- misconception tags
- source trace
- evidence span
- defensible correct answer
- defensibility check/risk

Scripts then enriched the item with metadata and generated atomic claims.

Observed results:

| Metric | Result |
|---|---:|
| Raw/normalized candidates | 250 |
| Reviewed candidates | 222 |
| Culled candidates | 28 |
| Topic count coverage | Complete after top-ups |
| Reachable source URLs | 20/20 |
| Source-verified items | 52 |
| Needs human source review | 170 |
| Human-review tail | 170/222 = 76.6% |
| Final status | Blocked |

Failure mode:

The lean prompt improved candidate survival and reduced obvious formatting/schema issues. It did not improve source-verification performance. The current bank still has too many items whose claims cannot be deterministically supported by their cited evidence.

## Current Day 3 Blockers

| Blocker | Meaning |
|---|---|
| `automation_tail_gate` | Too many items still need LLM repair/judgment or human source review. Current tail is 76.6%, far above the accepted thresholds. |
| `coverage_gate` | Some official mapped skills remain uncovered even though topic-level count coverage is complete. |
| `factual_verification_gate` | Too many claims remain unresolved by source verification. |
| `human_resolution_gate` | Human review queue is far too large for the desired automation model. |

## Why The Attempts Failed

### 1. We used source references when the model needed source evidence.

A source catalog or URL tells the model where truth may live. It does not give the model the exact evidence needed to defend the answer. The model then improvises from its latent knowledge and produces plausible source traces that are not always verifiable.

### 2. We mixed two hard tasks in one generation step.

We asked the model to do both:

- write tough, realistic, tricky exam questions
- produce audit-grade source grounding

The model can often do each separately, but doing both in one pass degraded reliability. The full-contract prompt overloaded the model; the lean prompt improved focus but still lacked source evidence.

### 3. Local teaching documents are not always valid primary evidence for AWS factual claims.

Local study guides and worksheets are useful learning artifacts, but they are not always authoritative enough to prove AWS technical facts. Items grounded only in local material often remain weak unless the local material itself contains sourced evidence.

### 4. URL reachability was mistaken for source support.

The URL verifier proved that cited pages exist. It did not prove the cited page supports the correct answer. This is a different and harder requirement.

### 5. Deterministic verification is conservative.

The deterministic verifier can miss semantically valid support if the evidence phrase is paraphrased, too broad, or split across multiple passages. However, the size of the unresolved tail is too large to blame only on verifier strictness.

### 6. Prompt improvements became process-compliance improvements, not necessarily question-quality improvements.

Some changes made the item easier to audit. That is useful, but it can pull attention away from the real goal: intellectually demanding questions about realistic AI/ML problems, with AWS-grounded answers.

## What Actually Improved

Not everything failed. These improvements are real:

| Improvement | Value |
|---|---|
| Tail thresholds | Prevent weak banks from being called review-ready. |
| URL verifier | Catches dead or fake URLs cheaply. |
| Source catalog | Establishes the beginning of source governance. |
| Lean prompt | Produces more structurally usable candidates than the full-contract prompt. |
| Post-generation enrichment | Reduces prompt clutter and centralizes metadata rules in code. |
| Top-up normalization patch | Fixed false topic culls caused by top-up run IDs. |
| Ledger initializer patch | Improved verified count from 24 to 52 by using generated atomic claims. |

These are infrastructure improvements. They do not yet solve high-quality grounded question generation.

## What Did Not Improve Enough

| Area | Current Problem |
|---|---|
| Source defensibility | 170 of 222 current reviewed items still need human source review. |
| Human-review burden | 76.6% tail is far above the 5% threshold. |
| Automated semantic support | Deterministic checks cannot verify most generated evidence spans. |
| Official skill coverage | Some mapped skills remain uncovered even after topic count coverage. |
| Quality-vs-grounding balance | Grounding prompts risk making questions source-shaped rather than problem-shaped. |

## Better Hypothesis For The Next Design

The next design should not be "generate from a source catalog." It should be:

1. Identify the real AI/LLM problem or challenge.
2. Map that problem to an AIP-C01 objective.
3. Retrieve or prepare a small set of exact AWS-backed source cards.
4. Generate tough questions using those source cards as evidence, not just as URLs.
5. Require each correct answer to cite one or more exact source-card excerpts.
6. Run deterministic verification against those exact excerpts.
7. Use an LLM judge only for the small remaining semantic tail.

The key shift is from URL-grounded generation to evidence-card-grounded generation.

## Suggested External Consultation Questions

1. Are we failing primarily because the generator lacks exact source evidence, or because the verifier is too strict?
2. What is the right source-card format for generating tough certification questions without making them shallow document lookup questions?
3. Should local teaching material ever be allowed as primary support for AWS factual claims, or only as secondary learning context?
4. How should we separate "question quality review" from "source defensibility review" so one does not distort the other?
5. What is a reasonable automated source-verification threshold for a certification-prep question bank?
6. Should the pipeline generate questions from real-world AI problem patterns first, then bind to AWS evidence, rather than starting from documents?
7. How should official objective/skill coverage be enforced without overloading the generation prompt?

## Recommendation

Do not continue full-day Day 3 regeneration with more prompt tweaks.

Recommended next experiment:

1. Pick one Day 3 canary topic.
2. Build 5-8 source cards manually or semi-automatically from authoritative AWS documentation.
3. Each source card should contain:
   - source ID
   - AWS URL
   - exact excerpt
   - supported concept
   - common misconception or decision boundary
   - related AIP-C01 objective/skill
4. Generate 10 tough questions from those source cards.
5. Require each question to cite source card ID and exact excerpt.
6. Run deterministic verification.
7. Scale only if:
   - reviewed item count >= 10
   - source-verified >= 95%
   - human-review tail <= 5%
   - no obvious quality collapse into keyword trivia

This keeps quality as the primary goal while making source grounding auditable by construction.
