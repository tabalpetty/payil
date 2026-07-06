# Scripts

Utility scripts for maintaining and generating project artifacts.

Pilot1/AIP-C01-specific automation lives under
`scripts/pilot1_aip_c01/`. That folder is allowed to encode AIP-C01 source
paths, AWS documentation rules, exam-prep workflows, and other pilot-instance
assumptions. Keep subject-agnostic utilities outside that folder when they are
introduced.

## AIP-C01 Source Extraction

Use `extract_aip_c01_exam_guide.py` to regenerate durable derived sources from
the official AIP-C01 exam-guide PDF.

```bash
python3 scripts/pilot1_aip_c01/extract_aip_c01_exam_guide.py
python3 scripts/pilot1_aip_c01/extract_aip_c01_exam_guide.py --check
```

Generated files:

```text
docs/Pilot1/aip-c01/source-material/ai-professional-01.extracted.md
docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json
docs/Pilot1/aip-c01/source-material/ai-professional-01.extraction-meta.json
```

For official domain, task, Skill X.Y.Z, and domain-weight references, future
curriculum and exam-prep scripts should read
`ai-professional-01.objectives.json` first. The PDF remains the source of
record; the Markdown transcript is the human-readable audit view.

## Source-To-Decomposition Coverage Audit

Use `audit_source_decomposition_coverage.py` after source extraction and before
topic briefs, prompt packs, question banks, or teaching-package generation.
This Layer 0 gate checks whether official source objectives are represented in
the curriculum decomposition or explicitly deferred.

```bash
# Regenerate the canonical skill-to-topic relationships when source objectives
# or the curriculum decomposition changes.
python3 scripts/pilot1_aip_c01/export_source_topic_traceability_matrix.py

# Write the audit report and machine-readable result.
python3 scripts/pilot1_aip_c01/audit_source_decomposition_coverage.py

# Use strict mode in automation to fail when Layer 0 is incomplete.
python3 scripts/pilot1_aip_c01/audit_source_decomposition_coverage.py --strict
```

Generated files:

```text
docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md
docs/Pilot1/aip-c01/curriculum-model/source-to-decomposition-coverage-audit.md
docs/Pilot1/aip-c01/curriculum-model/source-to-decomposition-coverage-audit.json
```

Intentional gaps belong in:

```text
docs/Pilot1/aip-c01/curriculum-model/source-to-decomposition-deferrals.md
```

The AIP-C01 audit verifies task coverage, every official Skill X.Y.Z
relationship, and traceability for every curriculum topic. Mapped curriculum
coverage and delivered teaching-package coverage remain separate measures.

## Exam-Prep Prefect Orchestrator

Use `run_exam_prep_agent_prefect.py` when you want one workflow manager to
coordinate the existing exam-prep unit scripts for a day.

Install Prefect first:

```bash
python3 -m pip install -r requirements-prefect.txt
```

Planning-only run:

```bash
python3 scripts/pilot1_aip_c01/run_exam_prep_agent_prefect.py --day 3 --stop-after-planning
```

Dry-run generation path:

```bash
python3 scripts/pilot1_aip_c01/run_exam_prep_agent_prefect.py --day 3 --dry-run-generation
```

Full generation path, when `OPENAI_API_KEY` is set:

```bash
python3 scripts/pilot1_aip_c01/run_exam_prep_agent_prefect.py --day 3 --generate
```

The Prefect flow runs:

```text
build topic briefs
-> map topic briefs to official objectives
-> check prompt readiness
-> build prompt pack
-> generate raw candidates, if requested
-> normalize
-> review/cull
-> top-up loop
-> write reviewed outputs
-> answer-position rebalance
-> source URL verification/cache
-> claim source verification
-> source review triage
-> source verification
-> final gates
-> agent run report
```

The review and source-verification gates reject phantom citations. A
`source_trace` must use an official source URL, a resolving local `docs/...`
path, the canonical objectives JSON path, or an explicit unresolved marker such
as `NONE`/`source_trace_needed`. Prose labels like "AWS service documentation"
are not accepted as citations. Source verification also syncs the claim ledger
from the final reviewed bank and records a content hash per item, so a ledger
record for an older item cannot satisfy a rewritten item with the same ID.
Before the final source gate, the orchestrator machine-checks official AWS
documentation URLs and caches their extracted text, then checks the item-level
claim ledger against local trusted sources and cached AWS source text. This
keeps existing banks auditable and gives future generation runs a clearer
contract: generate source-backed atomic claims up front; let verification audit
them.
The triage step splits unresolved source-review work into buckets such as
AWS evidence already fetched, local evidence already fetched, source
placeholders, fetch gaps, and `NONE` policy cases. This is the report humans
and follow-up automation should use instead of treating every unresolved item
as the same problem.

Run source checks directly when auditing an existing bank:

```bash
python3 scripts/pilot1_aip_c01/verify_exam_prep_source_urls.py --day 3 --write
python3 scripts/pilot1_aip_c01/verify_exam_prep_claims_with_sources.py --day 3 --write
python3 scripts/pilot1_aip_c01/triage_exam_prep_source_review.py --day 3 --write
python3 scripts/pilot1_aip_c01/verify_exam_prep_sources.py --day 3 --initialize-ledger --write
```

Run the optional grounded judge on already-fetched AWS evidence first:

```bash
# Inspect prompts without calling the API.
python3 scripts/pilot1_aip_c01/judge_exam_prep_claims_with_evidence.py --day 3 --buckets A --limit 2 --dry-run --write

# Apply only high-confidence supported judgments to the claim ledger.
python3 scripts/pilot1_aip_c01/judge_exam_prep_claims_with_evidence.py --day 3 --buckets A --write --apply-supported --min-confidence 0.92
python3 scripts/pilot1_aip_c01/verify_exam_prep_sources.py --day 3 --initialize-ledger --write
```

Do not auto-apply `refuted` or `insufficient` judgments as approvals. Use them
to cull, rewrite, or reassign sources.

The orchestrator reports honest final status:

| Status | Meaning |
|---|---|
| `planning-complete` | Topic briefs/prompt readiness were checked; usually objective mapping is next. |
| `reviewed-candidate` | Reviewed materials exist, but final approval was not reached. |
| `needs-human-source-review` | Source-verification ledger still has unresolved claims. |
| `blocked` | A hard gate or script step failed. |
| `approved` | Final gates passed. |

Run reports are written to:

```text
docs/Pilot1/aip-c01/exam-prep/reviewed/day-NN/day-NN-exam-prep-agent-run-report.json
```

The orchestrator does not bypass gates. In particular, unresolved atomic
source claims remain blockers for production approval.

## Student Artifact Method-Fit Audit

Use `audit_student_artifact_method_fit.py` before calling a day's focused
student artifacts review-ready. It turns lessons from prior reviews into a
deterministic gate, starting with the `Embedded` knowledge type.

```bash
python3 scripts/pilot1_aip_c01/audit_student_artifact_method_fit.py --day 3
python3 scripts/pilot1_aip_c01/audit_student_artifact_method_fit.py --day 4
```

The audit checks the curriculum map for topics whose knowledge type includes
`Embedded`, then verifies that each matching focused artifact has an explicit
`Embedded Inspection Record` with an observable inspection prompt. This is what
prevents Day 4+ generation from repeating the Day 3 regression where embedded
topics drifted into ordinary design tables.

## Exam-Prep Agent Planning

Use `build_exam_prep_day.py` to convert curriculum-map rows into deterministic
exam-prep topic briefs for a given accelerated day. This is the first coded
slice of the exam-prep agent. It does not call an LLM and does not approve
question-bank items.

```bash
# Inspect readiness without writing files.
python3 scripts/pilot1_aip_c01/build_exam_prep_day.py --day 2 --check

# Write topic briefs and an index.
python3 scripts/pilot1_aip_c01/build_exam_prep_day.py --day 2 --plan
```

Generated briefs are written to:

```text
docs/Pilot1/aip-c01/exam-prep/topic-briefs/day-02/
```

Before using briefs for prompt generation, fill official `exam_domain`,
`exam_task`, and `exam_skill` mappings from
`docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`. The
script intentionally marks those fields as `needs-objective-mapping` instead
of inventing traceability tags.

After a brief is mapped, rerunning `--plan` will not overwrite it. Use
`--force` only when intentionally regenerating mapped briefs.

Use `map_exam_prep_topic_briefs.py` to fill objective mappings from the
canonical source-to-topic traceability matrix.

```bash
python3 scripts/pilot1_aip_c01/map_exam_prep_topic_briefs.py --day 3 --check
python3 scripts/pilot1_aip_c01/map_exam_prep_topic_briefs.py --day 3
```

Use `build_exam_prep_prompts.py` to generate a day-specific raw
question-generation prompt pack from mapped topic briefs.

Before building prompts, update the course source catalog:

```text
docs/Pilot1/aip-c01/exam-prep/source-catalog.json
```

The catalog is the upstream source-grounding contract for the whole course.
Each topic maps to allowed source IDs from the shared source registry.
Generated lean items must choose one allowed source by using its exact
`source_value` in `source_trace`, include an `evidence_span`, and provide a
defensible correct answer. The normalizer then derives
`source_contract_version=source-grounded-v1`, `allowed_source_id`, and
`atomic_claims` from the catalog and lean source fields. The prompt builder
stops when a topic is missing from the catalog or references an invalid source.

The catalog is allowed to grow. If study-guide or question-bank work discovers
a new topic/source pair, promote it only after the URL/path is reachable,
relevant to a mapped topic, and verified by the source-review workflow.

```bash
# Inspect prompt-pack readiness without writing files.
python3 scripts/pilot1_aip_c01/build_exam_prep_prompts.py --day 2 --check

# Write the Day 2 prompt pack.
python3 scripts/pilot1_aip_c01/build_exam_prep_prompts.py --day 2
```

Generated prompt packs are written to:

```text
docs/Pilot1/aip-c01/exam-prep/day-02-question-generation-prompts.md
```

The prompt-pack builder does not call an LLM. It preserves official objective
fields from mapped topic briefs and sets a default target of 12 raw candidates
per curriculum-order topic.

For new generation, the normalizer enriches lean items into the full review
schema by filling mechanical metadata from topic briefs and source fields from
the course catalog. The reviewer culls any `source-grounded-v1` item that uses
a source outside the topic allowlist, omits atomic claim evidence, or falls back
to `NONE`/`source_trace_needed`. Older raw items are not retroactively rejected
unless review is run with `--enforce-source-contract`.

Use `generate_exam_prep_questions.py` to execute a generated prompt pack and
save raw responses with honest provenance. Use `--dry-run` to save the exact
prompt without calling an LLM.

```bash
# Save the full Day 2 prompt without calling the API.
python3 scripts/pilot1_aip_c01/generate_exam_prep_questions.py --day 2 --batch balanced --dry-run

# Save one topic prompt without calling the API.
python3 scripts/pilot1_aip_c01/generate_exam_prep_questions.py --day 2 --topic Day02-order001 --dry-run

# Generate the full Day 2 raw draft pool when OPENAI_API_KEY is set.
python3 scripts/pilot1_aip_c01/generate_exam_prep_questions.py --day 2 --batch balanced

# Generate all Day 2 topic prompts sequentially when OPENAI_API_KEY is set.
python3 scripts/pilot1_aip_c01/generate_exam_prep_questions.py --day 2 --all-topics
```

Raw Day 2 responses and dry-run prompt records are written to:

```text
docs/Pilot1/aip-c01/exam-prep/raw/day-02/
```

Every generation run also writes progress logs:

```text
docs/Pilot1/aip-c01/exam-prep/logs/day-02/
```

Each run creates a human-readable `.log` file and a machine-readable `.jsonl`
event stream. The generator prints the log path at `run-start`, then writes
events such as `run-item-start`, `api-request-start`, `api-request-complete`,
`file-written`, and `run-complete`. A monitor can tail the `.jsonl` file to
draw a progress bar without interrupting the generation process.

Example monitor command:

```bash
tail -f docs/Pilot1/aip-c01/exam-prep/logs/day-02/*.jsonl
```

Use `normalize_exam_prep_questions.py` to parse raw topic-level LLM responses
and write a schema-shaped draft bank for review. This step does not approve
items, source-check claims, or cull duplicates; it prepares a consistent review
input while preserving raw provenance.

```bash
python3 scripts/pilot1_aip_c01/normalize_exam_prep_questions.py --day 2
```

Normalized Day 2 draft outputs are written to:

```text
docs/Pilot1/aip-c01/exam-prep/reviewed/day-02/day-02-normalized-draft-question-bank.md
docs/Pilot1/aip-c01/exam-prep/reviewed/day-02/day-02-normalization-report.md
```

The normalization report must show zero parse errors before the review/cull
step begins. Candidate counts are raw-input counts only; they do not satisfy
the `>=10 approved items per topic` completion rule until the reviewer approves
them.

Use `review_exam_prep_questions.py` to run the generic review/cull pass over a
normalized draft bank. The output promotes passing items to `reviewed`
candidate status and logs every cull with audit evidence. It does not perform
the final source-verification gate.

```bash
python3 scripts/pilot1_aip_c01/review_exam_prep_questions.py --day 2
```

Reviewed Day 2 candidate output is written to:

```text
docs/Pilot1/aip-c01/exam-prep/reviewed/day-02/day-02-reviewed-candidate-bank.md
docs/Pilot1/aip-c01/exam-prep/reviewed/day-02/day-02-review-feedback.json
```

If any topic has fewer than 10 reviewed candidates, use the file's top-up
guidance before trying to finalize the day's bank. The JSON feedback file is
also consumed automatically by `generate_exam_prep_questions.py` when
`--top-up-topic` is used. Top-up prompts include the topic deficit, dominant
cull reasons, already-reviewed stems, rejected stems, and cull evidence so the
next generation pass can avoid repeating the same failures.

```bash
python3 scripts/pilot1_aip_c01/generate_exam_prep_questions.py --day 2 --top-up-topic Day02-order002 --count 3 --dry-run
python3 scripts/pilot1_aip_c01/generate_exam_prep_questions.py --day 2 --top-up-topic Day02-order010 --count 4 --dry-run
```

Use `run_exam_prep_topup_loop.py` to automate that cycle. It repeatedly
normalizes, reviews, checks the per-topic target, generates feedback-informed
top-ups for short topics, and repeats until the target is met or the maximum
iteration count is reached.

```bash
python3 scripts/pilot1_aip_c01/run_exam_prep_topup_loop.py --day 2 --target 10 --max-iterations 3
```

The loop writes human and JSONL progress logs under:

```text
docs/Pilot1/aip-c01/exam-prep/logs/day-02/
```

Use `write_exam_prep_review_outputs.py` after coverage passes to write the
Step 12 review outputs: reviewed question bank, separate cull log, and review
checks. This step does not perform final source verification.

```bash
python3 scripts/pilot1_aip_c01/write_exam_prep_review_outputs.py --day 2 --target 10
```

Day 2 review outputs are written to:

```text
docs/Pilot1/aip-c01/exam-prep/reviewed/day-02/day-02-reviewed-question-bank.md
docs/Pilot1/aip-c01/exam-prep/reviewed/day-02/day-02-cull-log.md
docs/Pilot1/aip-c01/exam-prep/reviewed/day-02/day-02-review-output-checks.md
docs/Pilot1/aip-c01/exam-prep/reviewed/day-02/day-02-review-output-checks.json
```

Use `run_exam_prep_final_gates.py` to run Step 13 final gates over the reviewed
bank. This checks objective traceability, remediation links, schema status,
coverage, distribution, approved-output regressions, iteration status, recorded
token usage, and automation-tail thresholds.

Tail thresholds are now hard process-quality gates:

- LLM repair/judge tail must be `<= 15%` of reviewed items.
- Human source-review tail must be `<= 5%` of reviewed items.

A bank with a small residual source-verification tail remains pending final
source verification. A bank that breaches either threshold is blocked because
the generation/review process moved too much work downstream.

```bash
python3 scripts/pilot1_aip_c01/run_exam_prep_final_gates.py --day 2 --target 10
```

To run the tail monitor directly:

```bash
python3 scripts/pilot1_aip_c01/monitor_exam_prep_tail_thresholds.py --day 2 --write
```

Final gate outputs are written to:

```text
docs/Pilot1/aip-c01/exam-prep/reviewed/day-02/day-02-final-gate-report.md
docs/Pilot1/aip-c01/exam-prep/reviewed/day-02/day-02-final-gates.json
```

## Day 1 Question Generation

Use `generate_day01_questions.py` to send the Day 1 question-generation prompt
pack to the OpenAI API and save the raw response.

Required environment:

```bash
export OPENAI_API_KEY="..."
```

Optional environment:

```bash
export OPENAI_MODEL="gpt-4.1"
```

Examples:

```bash
# Save the exact prompt that would be sent, without calling the API.
python3 scripts/pilot1_aip_c01/generate_day01_questions.py --batch balanced --dry-run

# Generate the full 120-question Day 1 draft pool.
python3 scripts/pilot1_aip_c01/generate_day01_questions.py --batch balanced

# Generate smaller batches if the model struggles with 120 items at once.
python3 scripts/pilot1_aip_c01/generate_day01_questions.py --batch foundations
python3 scripts/pilot1_aip_c01/generate_day01_questions.py --batch system-map
python3 scripts/pilot1_aip_c01/generate_day01_questions.py --batch applied-foundations

# Generate exactly one topic-level prompt, 12 questions.
python3 scripts/pilot1_aip_c01/generate_day01_questions.py --topic Day01-order001

# Generate a smaller top-up set for an under-filled topic.
# Use a surplus over the exact deficit because review will cull weak items.
python3 scripts/pilot1_aip_c01/generate_day01_questions.py --top-up-topic Day01-order005 --count 4

# Generate all ten Day 1 topic-level prompts sequentially, 12 questions each.
python3 scripts/pilot1_aip_c01/generate_day01_questions.py --all-topics
```

Raw responses are written to:

```text
docs/Pilot1/aip-c01/exam-prep/raw/day-01/
```

Raw candidate files must preserve true provenance. Use OpenAI provider/model
metadata only for responses actually returned by the OpenAI API. Manual,
Codex-authored, reviewer-authored, imported, or transformed top-ups should use
honest metadata and filenames before running review.

Raw responses are not approved question-bank items. Normalize and review them
under:

```text
docs/Pilot1/aip-c01/exam-prep/reviewed/day-01/
```

## Day 1 Question Review

Use `review_day01_questions.py` to parse preserved raw responses, apply the
review/cull rules, normalize approved items to the question-bank schema, and
rewrite the reviewed Day 1 bank.

```bash
python3 scripts/pilot1_aip_c01/review_day01_questions.py
```

Run this after adding new raw top-up responses.

Before reviewing a new day, confirm that
`source-material/ai-professional-01.objectives.json` exposes every objective
level used by the schema. For AIP-C01 that includes official domain, task, and
Skill X.Y.Z statements. Do not treat missing objective output as missing source
content until the extraction script and metadata have been checked.

Reviewer checks must scan the full item, including distractor rationales. A
false or stale service claim in a distractor explanation is still approved
teaching content if it enters the reviewed bank.

After the review pass, run an approved-output check for known rejected
patterns. If a stale phrase, duplicate stem pattern, schema defect, missing
traceability field, or provenance problem appears in the approved section, the
bank is still failing review even if the cull log contains related rejects.

The reviewed bank includes a `Prompt Improvement Signals` section that groups
culled items by reason and a `Top-Up Guidance` section that recommends raw
top-up counts. Read those sections before regenerating; the next prompt should
address the dominant cull reasons instead of only increasing volume.

Top-up prompts automatically include approved stems and rejected stem excerpts
for the selected topic when the reviewed Day 1 bank exists. The review script
also rejects exact or near-duplicate stems for the same curriculum-order topic,
so novelty is enforced during review rather than trusted to the prompt alone.
When this happens, the cull log includes duplicate evidence: the rejected stem,
the matched approved source, the matched approved stem, and whether the match
was exact or near-duplicate.
