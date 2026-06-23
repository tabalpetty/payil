# Agent Creation Progress

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
| 9 | Review and cull weak, duplicate, or unsupported questions | completed - coded and run for Day 2. Reviewed 118 source-verified candidates and culled 13 with auditable evidence, including the Step 13 fact-check cull. |
| 10 | Check coverage: at least 10 approved items per topic | completed - Day 2 final source-verified coverage meets the target, with 11-12 items per topic after fact-check culling. |
| 11 | Top up topics that are short | completed - implemented a loop that normalizes, reviews, generates feedback-informed top-ups for short topics, and repeats until coverage passes or max iterations is reached. |
| 12 | Write reviewed question bank, cull log, and checks | completed - coded and run for Day 2. Wrote reviewed bank, cull log, and review-output checks. |
| 13 | Run final gates: traceability, source checks, distribution, and cost | completed - fact-check source verifier is coded and run for Day 2; final gates report `completion_status=complete`. |

## Current Action

completed - Day 2 exam-prep agent flow now has source verification and final
gates passing. The final bank contains 118 source-verified items, and every
topic remains above the 10-item target.

## Next Action

yet to start - Decide whether to promote the Day 2
source-verified reviewed bank into a separately named approved bank, or start
applying the same agent flow to Day 3.
