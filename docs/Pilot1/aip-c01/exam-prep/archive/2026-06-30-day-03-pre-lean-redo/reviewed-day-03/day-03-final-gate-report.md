# Day 3 Final Gate Report

Generated: 2026-06-29

Completion status: `blocked`

## Gate Summary

| Gate | Status |
|---|---|
| teaching_substrate_gate | pass |
| source_objective_gate | pass |
| raw_provenance_gate | pass |
| schema_gate | pass |
| traceability_gate | pass |
| factual_verification_gate | pending |
| review_evidence_gate | pass |
| coverage_gate | pass |
| distribution_gate | pass |
| approved_output_gate | pass |
| cost_gate | pass |
| iteration_gate | pass |
| automation_tail_gate | fail |
| human_resolution_gate | pending |

## Coverage

| Curriculum order | Reviewed count | Target | Status |
|---|---:|---:|---|
| Day03-order001 | 10 | 10 | pass |
| Day03-order002 | 11 | 10 | pass |
| Day03-order003 | 12 | 10 | pass |
| Day03-order004 | 12 | 10 | pass |
| Day03-order005 | 12 | 10 | pass |
| Day03-order006 | 12 | 10 | pass |
| Day03-order007 | 11 | 10 | pass |
| Day03-order008 | 12 | 10 | pass |
| Day03-order009 | 11 | 10 | pass |
| Day03-order010 | 12 | 10 | pass |
| Day03-order011 | 11 | 10 | pass |
| Day03-order012 | 12 | 10 | pass |
| Day03-order013 | 12 | 10 | pass |
| Day03-order014 | 14 | 10 | pass |
| Day03-order015 | 13 | 10 | pass |
| Day03-order016 | 12 | 10 | pass |
| Day03-order017 | 11 | 10 | pass |
| Day03-order018 | 12 | 10 | pass |

## Distribution

- Difficulty: `{'hard': 98, 'medium': 83, 'exam-plus': 31}`
- Question format: `{'multiple-choice': 161, 'multiple-response': 51}`
- Cognitive demand: `{'diagnose': 57, 'select': 35, 'optimize': 18, 'configure': 17, 'judge': 25, 'integrate': 18, 'implement': 23, 'compare': 9, 'explain': 9, 'analyze': 1}`
- Answer positions: `{'1': 41, '2': 40, '3': 40, '4': 40, 'multiple-response': 51}`
- Maximum single-answer position share: `0.2547`

## Traceability

- Objective mismatches: `none`
- Missing remediation targets: `none`
- Missing source traces: `none`
- Topic/skill mismatches: `none`
- Missing mapped skills: `none`
- Source trace status: `{'needs-human-source-review': 153, 'source-verified': 59}`
- Claim verification status: `{'unresolved': 153, 'verified': 59}`
- Teaching substrate missing: `none`
- Approved-output regressions: `none`

## Automation Tail Thresholds

- Thresholds: `{'llm_repair_tail_max_ratio': 0.15, 'human_source_review_tail_max_ratio': 0.05}`
- Metrics: `{'llm_repair_tail_count': 153, 'llm_repair_tail_ratio': 0.7217, 'human_review_tail_count': 153, 'human_review_tail_ratio': 0.7217}`
- Breaches: `['llm_repair_tail 153/212 (72.2%) > 15%', 'human_review_tail 153/212 (72.2%) > 5%']`

## Cost Summary

- API calls recorded: `66`
- Token totals: `{'input_tokens': 1104750, 'output_tokens': 545015, 'total_tokens': 1649765, 'candidate_count': 819}`
- Missing cost telemetry: `none`
- Iteration summary: `{'observed_iterations': 3, 'configured_max_iterations': 3, 'blocked': False, 'within_limit': True}`

Dollar cost is not estimated here because no versioned model-price table
is configured in the repository. Token usage is recorded for budget
reconciliation.

## Remaining Work

- Blockers: `['automation_tail_gate']`
- Pending gates: `['factual_verification_gate', 'human_resolution_gate']`
