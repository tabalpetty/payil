# Agent Creation Progress

## Upstream Layers

These layers sit before the numbered exam-prep production steps. They protect
against the most expensive failure mode: building a complete-looking workflow
from an incomplete or wrong source decomposition.

| Layer | What It Means | Current Status |
|---:|---|---|
| -2 | Confirm source identity and legitimacy before extraction | completed - AIP-C01 source identity checkpoint exists at `docs/Pilot1/aip-c01/curriculum-model/source-identity-checkpoint.md`; official source URL, local PDF snapshot, extracted transcript, and objective JSON are recorded. A reusable Source Identity Workbench V1 is implemented at `docs/curriculum-architecture-kit/tools/source-identity-workbench/`. |
| -1 | Extract the official source faithfully into reusable structured/text forms | completed - AIP-C01 PDF was converted into `ai-professional-01.extracted.md`, `ai-professional-01.objectives.json`, and `ai-professional-01.extraction-meta.json`; the missing-PDF-extractor lesson has been captured in the kit. |
| 0 | Audit source-to-decomposition coverage before downstream generation | completed - the canonical source-to-topic matrix records all 98 official skills across 226 relationships and accounts for all 133 curriculum topics. The strict audit passes task coverage, skill coverage, and topic traceability. |

## Progress Table

| Step | What It Means | Current Status |
|---:|---|---|
| 1 | List Day 2-Day 7 topics | completed - already done in the curriculum map. |
| 2 | Classify each topic by knowledge type and artifact type | completed - already done in the curriculum map. |
| 3 | Create teaching material, artifacts, and answer guidance for the day | in-progress - complete for Day 1 and Day 2; not yet complete for Day 3-Day 7 at Day 1/2 quality. |
| 4 | Convert each topic into an exam-prep topic brief | completed - coded and run for Day 2. Briefs are in `topic-briefs/day-02/`. |
| 5 | Map each topic brief to official exam objectives | completed - done for Day 2. All 10 briefs now include official `exam_domain`, `exam_task`, and `exam_skill` values from the AIP-C01 guide. |
| 6 | Generate prompts for raw question candidates | completed - coded and run for Day 2. Prompt pack is `day-02-question-generation-prompts.md` with a 120-candidate raw-generation target. |
| 7 | Generate or manually add raw question candidates | completed - Day 2 has 131 raw candidates after feedback-informed top-ups, with at least 12 raw candidates per topic. |
| 8 | Normalize raw questions into the bank schema | completed - coded and run for Day 2. Normalized 131 draft candidates with zero parse errors into `reviewed/day-02/`. |
| 9 | Review and cull weak, duplicate, or unsupported questions | completed - coded and run for Day 2. Produced 118 reviewed candidates and culled 13 with auditable evidence. Final source approval remains Step 13 work. |
| 10 | Check coverage: at least 10 approved items per topic | in-progress - aggregate topic volume is 11-12 reviewed candidates per topic, but approved coverage is not complete because mapped-skill coverage and atomic-claim verification still fail. |
| 11 | Top up topics that are short | completed - implemented a loop that normalizes, reviews, generates feedback-informed top-ups for short topics, and repeats until coverage passes or max iterations is reached. |
| 12 | Write reviewed question bank, cull log, and checks | completed - coded and run for Day 2. Wrote reviewed bank, cull log, and review-output checks. |
| 13 | Run final gates: traceability, source checks, distribution, and cost | in-progress - gate enforcement is corrected and rerun. Answer positions are rebalanced and the distribution gate passes. Day 2 remains blocked on atomic-claim verification and topic-skill drift/missing skill coverage. Cost telemetry and iteration-limit checks pass. |

## Current Action

in-progress - Layer 0 remains complete, but the corrected Step 13 gate has
withdrawn Day 2 production approval. The bank has 118 reviewed candidates, yet
all require atomic-claim evidence, 12 items carry an off-map topic/skill pair,
and four mapped topic-skill obligations are untested. The existing bank's
multiple-choice keys are now balanced `23/23/23/22` across positions 1-4.

## Next Action

in-progress - Source verification has now been run: the claim-verification
ledger is built and all 118 items returned `needs-human-source-review` (0
auto-verified). Remaining work is to (1) repair or regenerate the Day 2 items
needed for mapped-skill coverage and to drop the off-map `1.5.6` tag on
order010, and (2) resolve the 118 human-source-review verdicts so items can move
to `source-verified`. Rerun final gates only after those repairs.
