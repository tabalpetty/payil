# Source-To-Decomposition Coverage Audit

Generated: 2026-06-29

## Verdict

- `overall_status`: `complete`
- `task_coverage_status`: `pass`
- `skill_coverage_status`: `pass`
- `topic_traceability_status`: `pass`

This is an upstream Layer 0 gate. It checks whether the official source
objectives are represented by the decomposition before topic briefs,
question prompts, question banks, or teaching packages are generated.

## Inputs

- Official objectives: `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- Curriculum topic map: `docs/Pilot1/aip-c01/curriculum-model/aip-c01-topic-knowledge-category-map.md`
- Accelerated plan: `docs/Pilot1/aip-c01/curriculum-model/accelerated-7-day-plan.md`
- Source-to-topic matrix: `docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md`
- Deferrals file: `docs/Pilot1/aip-c01/curriculum-model/source-to-decomposition-deferrals.md`

## Counts

| Measure | Count |
|---|---:|
| Official domains | 5 |
| Official tasks | 20 |
| Official skills | 98 |
| Curriculum topic rows | 133 |
| Covered or deferred tasks | 20 |
| Covered or deferred skills | 98 |

## Topic Rows By Day

| Day | Topic rows |
|---|---:|
| Day 1 | 10 |
| Day 2 | 10 |
| Day 3 | 18 |
| Day 4 | 35 |
| Day 5 | 22 |
| Day 6 | 33 |
| Day 7 | 5 |

## Task Coverage

The accelerated plan references every official task ID. This means the
day-level plan has not silently dropped an official task.

| Task | Status | Evidence |
|---|---|---|
| Task 1.1 | covered | docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day01-order006; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day07-order001; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day07-order002; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day07-order003; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day07-order004 |
| Task 1.2 | covered | docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day01-order007; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day03-order017; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day04-order001; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day04-order002; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day04-order003; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day04-order005; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day04-order009; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day04-order010; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day07-order002 |
| Task 1.3 | covered | docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day02-order001; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day02-order002; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day02-order003; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day03-order015 |
| Task 1.4 | covered | docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day02-order006; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day02-order007; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day02-order008; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day02-order010; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day03-order004 |
| Task 1.5 | covered | docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day02-order004; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day02-order005; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day02-order007; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day02-order009; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day02-order010; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day03-order001; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day03-order002; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day03-order003; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day03-order005; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day04-order025 |
| Task 1.6 | covered | docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day01-order002; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day01-order009; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day03-order007; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day03-order008; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day03-order009; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day03-order010; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day03-order011 |
| Task 2.1 | covered | docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day04-order004; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day04-order023; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day04-order024; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day04-order025; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day04-order026; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day04-order027; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day04-order028; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day04-order029; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day04-order030; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day04-order031; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day04-order032; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day04-order033 |
| Task 2.2 | covered | docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day01-order008; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day04-order002; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day04-order004; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day04-order006; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day04-order007; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day04-order008; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day06-order003; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day07-order002 |
| Task 2.3 | covered | docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day01-order004; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day01-order005; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day04-order013; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day04-order014; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day04-order015; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day04-order016; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day04-order017; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day04-order018; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day04-order019; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day04-order020; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day04-order021; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day05-order009; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day07-order001; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day07-order004 |
| Task 2.4 | covered | docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day01-order004; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day01-order008; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day03-order012; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day03-order013; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day03-order014; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day03-order016; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day03-order017; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day03-order018; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day04-order003 |
| Task 2.5 | covered | docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day01-order004; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day03-order015; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day03-order016; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day03-order018; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day04-order011; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day04-order012; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day04-order013; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day04-order022; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day04-order026; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day04-order033; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day06-order028; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day06-order031; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day06-order033 |
| Task 3.1 | covered | docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day05-order001; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day05-order002; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day05-order003; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day05-order004; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day05-order005; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day05-order006; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day05-order007 |
| Task 3.2 | covered | docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day01-order005; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day05-order008; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day05-order009; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day05-order010; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day05-order011; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day05-order012 |
| Task 3.3 | covered | docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day05-order013; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day05-order014; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day05-order015; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day05-order016; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day05-order017; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day05-order018; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day05-order022; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day07-order002; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day07-order004 |
| Task 3.4 | covered | docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day04-order034; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day05-order014; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day05-order017; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day05-order019; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day05-order020; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day05-order021; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day05-order022 |
| Task 4.1 | covered | docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day01-order002; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day04-order002; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day06-order001; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day06-order002; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day06-order003; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day06-order004; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day06-order005; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day06-order006; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day06-order007; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day07-order002 |
| Task 4.2 | covered | docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day01-order002; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day03-order001; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day06-order005; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day06-order006; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day06-order007; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day06-order008; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day06-order009; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day06-order010; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day06-order011; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day06-order032; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day07-order002 |
| Task 4.3 | covered | docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day03-order018; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day04-order034; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day06-order012; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day06-order013; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day06-order014; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day06-order015; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day06-order016; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day06-order017; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day06-order031; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day06-order032; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day06-order033; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day07-order004 |
| Task 5.1 | covered | docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day01-order010; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day03-order006; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day03-order010; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day04-order001; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day04-order002; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day04-order010; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day04-order021; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day04-order035; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day06-order017; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day06-order018; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day06-order019; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day06-order020; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day06-order021; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day06-order022; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day06-order023; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day06-order024; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day06-order025; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day06-order026; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day06-order031; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day07-order004 |
| Task 5.2 | covered | docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day01-order002; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day03-order006; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day03-order015; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day06-order027; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day06-order028; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day06-order029; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day06-order030; docs/Pilot1/aip-c01/curriculum-model/source-to-topic-traceability-matrix.md#Day06-order033 |

## Skill Coverage

Layer 0 requires either explicit coverage or explicit deferral for each
official skill. Evidence must come from the canonical source-to-topic
matrix or an explicit deferral.

No missing or undeferred skills.

## Topic Traceability

The curriculum topic map should carry explicit source objective coverage,
such as official task IDs, skill IDs, or a link to a source-to-topic
coverage map. The audit also accepts explicitly classified foundation
and cross-objective integration topics.

All topic rows have explicit source traceability.

## Deferrals

No explicit deferrals were found.

## Required Next Action

No decomposition repair is required. Regenerate the traceability
matrix and rerun this audit whenever the official objectives or
curriculum topic decomposition changes.
