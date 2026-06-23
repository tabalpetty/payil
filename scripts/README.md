# Scripts

Utility scripts for maintaining and generating Pilot1 artifacts.

## AIP-C01 Source Extraction

Use `extract_aip_c01_exam_guide.py` to regenerate durable derived sources from
the official AIP-C01 exam-guide PDF.

```bash
python3 scripts/extract_aip_c01_exam_guide.py
python3 scripts/extract_aip_c01_exam_guide.py --check
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

## Exam-Prep Agent Planning

Use `build_exam_prep_day.py` to convert curriculum-map rows into deterministic
exam-prep topic briefs for a given accelerated day. This is the first coded
slice of the exam-prep agent. It does not call an LLM and does not approve
question-bank items.

```bash
# Inspect readiness without writing files.
python3 scripts/build_exam_prep_day.py --day 2 --check

# Write topic briefs and an index.
python3 scripts/build_exam_prep_day.py --day 2 --plan
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

Use `build_exam_prep_prompts.py` to generate a day-specific raw
question-generation prompt pack from mapped topic briefs.

```bash
# Inspect prompt-pack readiness without writing files.
python3 scripts/build_exam_prep_prompts.py --day 2 --check

# Write the Day 2 prompt pack.
python3 scripts/build_exam_prep_prompts.py --day 2
```

Generated prompt packs are written to:

```text
docs/Pilot1/aip-c01/exam-prep/day-02-question-generation-prompts.md
```

The prompt-pack builder does not call an LLM. It preserves official objective
fields from mapped topic briefs and sets a default target of 12 raw candidates
per curriculum-order topic.

Use `generate_exam_prep_questions.py` to execute a generated prompt pack and
save raw responses with honest provenance. Use `--dry-run` to save the exact
prompt without calling an LLM.

```bash
# Save the full Day 2 prompt without calling the API.
python3 scripts/generate_exam_prep_questions.py --day 2 --batch balanced --dry-run

# Save one topic prompt without calling the API.
python3 scripts/generate_exam_prep_questions.py --day 2 --topic Day02-order001 --dry-run

# Generate the full Day 2 raw draft pool when OPENAI_API_KEY is set.
python3 scripts/generate_exam_prep_questions.py --day 2 --batch balanced

# Generate all Day 2 topic prompts sequentially when OPENAI_API_KEY is set.
python3 scripts/generate_exam_prep_questions.py --day 2 --all-topics
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
python3 scripts/normalize_exam_prep_questions.py --day 2
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
python3 scripts/review_exam_prep_questions.py --day 2
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
python3 scripts/generate_exam_prep_questions.py --day 2 --top-up-topic Day02-order002 --count 3 --dry-run
python3 scripts/generate_exam_prep_questions.py --day 2 --top-up-topic Day02-order010 --count 4 --dry-run
```

Use `run_exam_prep_topup_loop.py` to automate that cycle. It repeatedly
normalizes, reviews, checks the per-topic target, generates feedback-informed
top-ups for short topics, and repeats until the target is met or the maximum
iteration count is reached.

```bash
python3 scripts/run_exam_prep_topup_loop.py --day 2 --target 10 --max-iterations 3
```

The loop writes human and JSONL progress logs under:

```text
docs/Pilot1/aip-c01/exam-prep/logs/day-02/
```

Use `write_exam_prep_review_outputs.py` after coverage passes to write the
Step 12 review outputs: reviewed question bank, separate cull log, and review
checks. This step does not perform final source verification.

```bash
python3 scripts/write_exam_prep_review_outputs.py --day 2 --target 10
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
coverage, distribution, approved-output regressions, iteration status, and
recorded token usage. It reports factual verification separately; a bank with
`needs-final-source-check` items remains pending final source verification.

```bash
python3 scripts/run_exam_prep_final_gates.py --day 2 --target 10
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
python3 scripts/generate_day01_questions.py --batch balanced --dry-run

# Generate the full 120-question Day 1 draft pool.
python3 scripts/generate_day01_questions.py --batch balanced

# Generate smaller batches if the model struggles with 120 items at once.
python3 scripts/generate_day01_questions.py --batch foundations
python3 scripts/generate_day01_questions.py --batch system-map
python3 scripts/generate_day01_questions.py --batch applied-foundations

# Generate exactly one topic-level prompt, 12 questions.
python3 scripts/generate_day01_questions.py --topic Day01-order001

# Generate a smaller top-up set for an under-filled topic.
# Use a surplus over the exact deficit because review will cull weak items.
python3 scripts/generate_day01_questions.py --top-up-topic Day01-order005 --count 4

# Generate all ten Day 1 topic-level prompts sequentially, 12 questions each.
python3 scripts/generate_day01_questions.py --all-topics
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
python3 scripts/review_day01_questions.py
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
