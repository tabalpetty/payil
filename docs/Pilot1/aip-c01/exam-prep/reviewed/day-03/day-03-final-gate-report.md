# Day 3 Final Gate Report

Generated: 2026-06-30

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
| coverage_gate | fail |
| distribution_gate | pass |
| approved_output_gate | pass |
| cost_gate | pass |
| iteration_gate | pass |
| automation_tail_gate | fail |
| human_resolution_gate | pending |

## Coverage

| Curriculum order | Reviewed count | Target | Status |
|---|---:|---:|---|
| Day03-order001 | 13 | 10 | pass |
| Day03-order002 | 13 | 10 | pass |
| Day03-order003 | 13 | 10 | pass |
| Day03-order004 | 12 | 10 | pass |
| Day03-order005 | 13 | 10 | pass |
| Day03-order006 | 12 | 10 | pass |
| Day03-order007 | 12 | 10 | pass |
| Day03-order008 | 13 | 10 | pass |
| Day03-order009 | 13 | 10 | pass |
| Day03-order010 | 12 | 10 | pass |
| Day03-order011 | 13 | 10 | pass |
| Day03-order012 | 12 | 10 | pass |
| Day03-order013 | 12 | 10 | pass |
| Day03-order014 | 12 | 10 | pass |
| Day03-order015 | 10 | 10 | pass |
| Day03-order016 | 13 | 10 | pass |
| Day03-order017 | 12 | 10 | pass |
| Day03-order018 | 12 | 10 | pass |

## Distribution

- Difficulty: `{'medium': 129, 'hard': 81, 'exam-plus': 12}`
- Question format: `{'multiple-choice': 178, 'multiple-response': 44}`
- Cognitive demand: `{'select': 14, 'optimize': 48, 'configure': 47, 'design': 10, 'implement': 29, 'diagnose': 48, 'explain': 1, 'compare': 4, 'integrate': 2, 'judge': 18, 'analyze': 1}`
- Answer positions: `{'1': 45, '2': 45, '3': 44, '4': 44, 'multiple-response': 44}`
- Maximum single-answer position share: `0.2528`

## Traceability

- Objective mismatches: `none`
- Missing remediation targets: `none`
- Missing source traces: `none`
- Topic/skill mismatches: `none`
- Missing mapped skills: `{'Day03-order001': ['4.2.2'], 'Day03-order004': ['1.4.5'], 'Day03-order006': ['5.2.4'], 'Day03-order010': ['5.1.4'], 'Day03-order015': ['2.5.1', '5.2.1'], 'Day03-order016': ['2.5.1'], 'Day03-order017': ['2.4.3'], 'Day03-order018': ['2.5.6', '4.3.1']}`
- Source trace status: `{'source-verified': 52, 'needs-human-source-review': 170}`
- Claim verification status: `{'verified': 52, 'unresolved': 170}`
- Teaching substrate missing: `none`
- Approved-output regressions: `none`

## Automation Tail Thresholds

- Thresholds: `{'llm_repair_tail_max_ratio': 0.15, 'human_source_review_tail_max_ratio': 0.05}`
- Metrics: `{'llm_repair_tail_count': 170, 'llm_repair_tail_ratio': 0.7658, 'human_review_tail_count': 170, 'human_review_tail_ratio': 0.7658}`
- Breaches: `['llm_repair_tail 170/222 (76.6%) > 15%', 'human_review_tail 170/222 (76.6%) > 5%']`

## Cost Summary

- API calls recorded: `21`
- Token totals: `{'input_tokens': 425399, 'output_tokens': 107670, 'total_tokens': 533069, 'candidate_count': 250}`
- Missing cost telemetry: `none`
- Iteration summary: `{'observed_iterations': 0, 'configured_max_iterations': 3, 'blocked': False, 'within_limit': True}`

Dollar cost is not estimated here because no versioned model-price table
is configured in the repository. Token usage is recorded for budget
reconciliation.

## Remaining Work

- Blockers: `['coverage_gate', 'automation_tail_gate']`
- Pending gates: `['factual_verification_gate', 'human_resolution_gate']`
