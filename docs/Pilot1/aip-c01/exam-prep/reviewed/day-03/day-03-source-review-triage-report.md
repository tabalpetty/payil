# Day 3 Source Review Triage

Generated: 2026-06-30

This report breaks unresolved source-review items into next-action buckets.
It is not an approval report; it is a work queue for reducing
`needs-human-source-review`.

## Summary

| Bucket | Count | Meaning | Next action |
|---|---:|---|---|
| A | 0 | AWS URL with fetched evidence | Run grounded judge; likely highest auto-clear yield. |
| B | 86 | Local teaching source with fetched evidence | Run grounded judge, but prefer AWS reassignment for AWS factual claims. |
| C | 0 | source_trace_needed placeholder | Retrieve/propose a real source, then fetch and judge. |
| D | 82 | AWS URL without fetched evidence | Retry fetch or reject/reassign dead URLs before human review. |
| E | 0 | NONE source marker | Apply policy: judgment item, rewrite, or cull. |
| F | 2 | Other unsupported source condition | Inspect source token and normalize to an accepted source type. |

## Items

| Bucket | Item | Unit | Evidence | Coverage | Source | Note |
|---|---|---|---:|---:|---|---|
| B | P1-AIP-D3-002 | Day03-order001 | 600 | 0.273 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order001-hybrid-search-custom-scoring.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-004 | Day03-order001 | 600 | 0.286 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order001-hybrid-search-custom-scoring.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-007 | Day03-order001 | 600 | 0.375 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order001-hybrid-search-custom-scoring.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-008 | Day03-order001 | 600 | 0.3 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order001-hybrid-search-custom-scoring.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-009 | Day03-order001 | 600 | 0.273 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order001-hybrid-search-custom-scoring.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-011 | Day03-order001 | 600 | 0.333 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order001-hybrid-search-custom-scoring.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-013 | Day03-order001 | 600 | 0.25 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order001-hybrid-search-custom-scoring.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-015 | Day03-order002 | 124 | 0.273 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order002-reranking.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-017 | Day03-order002 | 524 | 0.3 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order002-reranking.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-018 | Day03-order002 | 524 | 0.083 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order002-reranking.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-019 | Day03-order002 | 524 | 0.083 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order002-reranking.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-020 | Day03-order002 | 524 | 0.167 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order002-reranking.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-021 | Day03-order002 | 524 | 0.1 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order002-reranking.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-023 | Day03-order002 | 524 | 0.25 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order002-reranking.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-025 | Day03-order002 | 524 | 0.375 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order002-reranking.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-027 | Day03-order003 | 599 | 0.273 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order003-query-expansion-decomposition-transformation.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-028 | Day03-order003 | 600 | 0.111 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order003-query-expansion-decomposition-transformation.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-029 | Day03-order003 | 600 | 0.25 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order003-query-expansion-decomposition-transformation.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-030 | Day03-order003 | 600 | 0.2 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order003-query-expansion-decomposition-transformation.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-031 | Day03-order003 | 600 | 0.375 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order003-query-expansion-decomposition-transformation.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-032 | Day03-order003 | 599 | 0.286 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order003-query-expansion-decomposition-transformation.md | insufficient lexical support for conservative auto-approval |
| F | P1-AIP-D3-033 | Day03-order003 | 0 | 0.0 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order003-query-expansion-decomposition-transformation.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-034 | Day03-order003 | 600 | 0.25 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order003-query-expansion-decomposition-transformation.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-035 | Day03-order003 | 600 | 0.1 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order003-query-expansion-decomposition-transformation.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-036 | Day03-order003 | 600 | 0.222 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order003-query-expansion-decomposition-transformation.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-037 | Day03-order003 | 600 | 0.143 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order003-query-expansion-decomposition-transformation.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-038 | Day03-order003 | 600 | 0.25 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order003-query-expansion-decomposition-transformation.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-039 | Day03-order003 | 600 | 0.125 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order003-query-expansion-decomposition-transformation.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-044 | Day03-order004 | 600 | 0.25 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order004-vector-store-ingestion-synchronization-refresh-maintenance.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-046 | Day03-order004 | 600 | 0.3 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order004-vector-store-ingestion-synchronization-refresh-maintenance.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-048 | Day03-order004 | 600 | 0.143 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order004-vector-store-ingestion-synchronization-refresh-maintenance.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-049 | Day03-order004 | 600 | 0.125 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order004-vector-store-ingestion-synchronization-refresh-maintenance.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-052 | Day03-order005 | 599 | 0.3 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order005-retrieval-apis-function-interfaces-mcp-access.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-054 | Day03-order005 | 599 | 0.273 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order005-retrieval-apis-function-interfaces-mcp-access.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-055 | Day03-order005 | 599 | 0.091 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order005-retrieval-apis-function-interfaces-mcp-access.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-058 | Day03-order005 | 599 | 0.286 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order005-retrieval-apis-function-interfaces-mcp-access.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-059 | Day03-order005 | 599 | 0.2 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order005-retrieval-apis-function-interfaces-mcp-access.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-060 | Day03-order005 | 599 | 0.3 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order005-retrieval-apis-function-interfaces-mcp-access.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-064 | Day03-order005 | 599 | 0.2 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order005-retrieval-apis-function-interfaces-mcp-access.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-065 | Day03-order006 | 600 | 0.091 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order006-rag-quality-evaluation-retrieval-troubleshooting.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-067 | Day03-order006 | 230 | 0.25 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order006-rag-quality-evaluation-retrieval-troubleshooting.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-068 | Day03-order006 | 600 | 0.333 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order006-rag-quality-evaluation-retrieval-troubleshooting.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-069 | Day03-order006 | 495 | 0.273 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order006-rag-quality-evaluation-retrieval-troubleshooting.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-070 | Day03-order006 | 600 | 0.333 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order006-rag-quality-evaluation-retrieval-troubleshooting.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-071 | Day03-order006 | 171 | 0.1 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order006-rag-quality-evaluation-retrieval-troubleshooting.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-073 | Day03-order006 | 600 | 0.2 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order006-rag-quality-evaluation-retrieval-troubleshooting.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-074 | Day03-order006 | 600 | 0.222 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order006-rag-quality-evaluation-retrieval-troubleshooting.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-075 | Day03-order006 | 600 | 0.125 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order006-rag-quality-evaluation-retrieval-troubleshooting.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-076 | Day03-order006 | 495 | 0.222 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order006-rag-quality-evaluation-retrieval-troubleshooting.md | insufficient lexical support for conservative auto-approval |
| D | P1-AIP-D3-077 | Day03-order007 | 0 | 0.0 | https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html | AWS URL was not fetched/reachable |
| D | P1-AIP-D3-078 | Day03-order007 | 0 | 0.0 | https://docs.aws.amazon.com/comprehend/latest/dg/how-languages.html | AWS URL was not fetched/reachable |
| B | P1-AIP-D3-079 | Day03-order007 | 600 | 0.214 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order007-conversation-context-history-intent-state-management.md | insufficient lexical support for conservative auto-approval |
| D | P1-AIP-D3-080 | Day03-order007 | 0 | 0.0 | https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html | AWS URL was not fetched/reachable |
| D | P1-AIP-D3-081 | Day03-order007 | 0 | 0.0 | https://docs.aws.amazon.com/comprehend/latest/dg/how-languages.html | AWS URL was not fetched/reachable |
| D | P1-AIP-D3-082 | Day03-order007 | 0 | 0.0 | https://docs.aws.amazon.com/comprehend/latest/dg/how-languages.html | AWS URL was not fetched/reachable |
| D | P1-AIP-D3-083 | Day03-order007 | 0 | 0.0 | https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html | AWS URL was not fetched/reachable |
| D | P1-AIP-D3-085 | Day03-order007 | 0 | 0.0 | https://docs.aws.amazon.com/comprehend/latest/dg/how-languages.html | AWS URL was not fetched/reachable |
| D | P1-AIP-D3-087 | Day03-order007 | 0 | 0.0 | https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html | AWS URL was not fetched/reachable |
| D | P1-AIP-D3-088 | Day03-order007 | 0 | 0.0 | https://docs.aws.amazon.com/comprehend/latest/dg/how-languages.html | AWS URL was not fetched/reachable |
| B | P1-AIP-D3-089 | Day03-order008 | 523 | 0.273 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order008-advanced-prompt-engineering-iterative-refinement.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-090 | Day03-order008 | 558 | 0.273 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order008-advanced-prompt-engineering-iterative-refinement.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-091 | Day03-order008 | 523 | 0.3 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order008-advanced-prompt-engineering-iterative-refinement.md | insufficient lexical support for conservative auto-approval |
| F | P1-AIP-D3-093 | Day03-order008 | 0 | 0.0 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order008-advanced-prompt-engineering-iterative-refinement.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-095 | Day03-order008 | 558 | 0.111 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order008-advanced-prompt-engineering-iterative-refinement.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-096 | Day03-order008 | 174 | 0.111 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order008-advanced-prompt-engineering-iterative-refinement.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-098 | Day03-order008 | 558 | 0.2 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order008-advanced-prompt-engineering-iterative-refinement.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-099 | Day03-order008 | 558 | 0.25 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order008-advanced-prompt-engineering-iterative-refinement.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-100 | Day03-order008 | 558 | 0.111 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order008-advanced-prompt-engineering-iterative-refinement.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-101 | Day03-order008 | 558 | 0.2 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order008-advanced-prompt-engineering-iterative-refinement.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-102 | Day03-order009 | 600 | 0.231 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order009-prompt-versioning-repositories-approvals-governance.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-105 | Day03-order009 | 599 | 0.273 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order009-prompt-versioning-repositories-approvals-governance.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-106 | Day03-order009 | 599 | 0.333 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order009-prompt-versioning-repositories-approvals-governance.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-107 | Day03-order009 | 600 | 0.222 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order009-prompt-versioning-repositories-approvals-governance.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-110 | Day03-order009 | 600 | 0.286 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order009-prompt-versioning-repositories-approvals-governance.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-112 | Day03-order009 | 600 | 0.222 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order009-prompt-versioning-repositories-approvals-governance.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-114 | Day03-order009 | 600 | 0.1 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order009-prompt-versioning-repositories-approvals-governance.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-115 | Day03-order010 | 600 | 0.214 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order010-prompt-regression-testing-quality-assurance.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-118 | Day03-order010 | 157 | 0.286 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order010-prompt-regression-testing-quality-assurance.md | insufficient lexical support for conservative auto-approval |
| D | P1-AIP-D3-122 | Day03-order011 | 0 | 0.0 | https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-flows-branching.html | AWS URL was not fetched/reachable |
| D | P1-AIP-D3-123 | Day03-order011 | 0 | 0.0 | https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-flows-branching.html | AWS URL was not fetched/reachable |
| D | P1-AIP-D3-124 | Day03-order011 | 0 | 0.0 | https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-flows-components.html | AWS URL was not fetched/reachable |
| D | P1-AIP-D3-125 | Day03-order011 | 0 | 0.0 | https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-flows-branching.html | AWS URL was not fetched/reachable |
| D | P1-AIP-D3-126 | Day03-order011 | 0 | 0.0 | https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-flows-branching.html | AWS URL was not fetched/reachable |
| D | P1-AIP-D3-127 | Day03-order011 | 0 | 0.0 | https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-flows-branching.html | AWS URL was not fetched/reachable |
| D | P1-AIP-D3-128 | Day03-order011 | 0 | 0.0 | https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-flows.html | AWS URL was not fetched/reachable |
| D | P1-AIP-D3-129 | Day03-order011 | 0 | 0.0 | https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-flows-components.html | AWS URL was not fetched/reachable |
| D | P1-AIP-D3-130 | Day03-order011 | 0 | 0.0 | https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-flows.html | AWS URL was not fetched/reachable |
| D | P1-AIP-D3-131 | Day03-order011 | 0 | 0.0 | https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-flows-components.html | AWS URL was not fetched/reachable |
| D | P1-AIP-D3-132 | Day03-order011 | 0 | 0.0 | https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-flows-branching.html | AWS URL was not fetched/reachable |
| D | P1-AIP-D3-133 | Day03-order011 | 0 | 0.0 | https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-flows-branching.html | AWS URL was not fetched/reachable |
| D | P1-AIP-D3-134 | Day03-order011 | 0 | 0.0 | https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-flows.html | AWS URL was not fetched/reachable |
| D | P1-AIP-D3-135 | Day03-order012 | 0 | 0.0 | https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html | AWS URL was not fetched/reachable |
| D | P1-AIP-D3-136 | Day03-order012 | 0 | 0.0 | https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-method-request-validation.html | AWS URL was not fetched/reachable |
| D | P1-AIP-D3-137 | Day03-order012 | 0 | 0.0 | https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html | AWS URL was not fetched/reachable |
| D | P1-AIP-D3-138 | Day03-order012 | 0 | 0.0 | https://docs.aws.amazon.com/apigateway/latest/developerguide/limits.html | AWS URL was not fetched/reachable |
| D | P1-AIP-D3-139 | Day03-order012 | 0 | 0.0 | https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html | AWS URL was not fetched/reachable |
| D | P1-AIP-D3-140 | Day03-order012 | 0 | 0.0 | https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-method-request-validation.html | AWS URL was not fetched/reachable |
| D | P1-AIP-D3-141 | Day03-order012 | 0 | 0.0 | https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html | AWS URL was not fetched/reachable |
| D | P1-AIP-D3-142 | Day03-order012 | 0 | 0.0 | https://docs.aws.amazon.com/apigateway/latest/developerguide/limits.html | AWS URL was not fetched/reachable |
| D | P1-AIP-D3-143 | Day03-order012 | 0 | 0.0 | https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html | AWS URL was not fetched/reachable |
| D | P1-AIP-D3-144 | Day03-order012 | 0 | 0.0 | https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-method-request-validation.html | AWS URL was not fetched/reachable |
| D | P1-AIP-D3-145 | Day03-order012 | 0 | 0.0 | https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html | AWS URL was not fetched/reachable |
| D | P1-AIP-D3-146 | Day03-order012 | 0 | 0.0 | https://docs.aws.amazon.com/apigateway/latest/developerguide/limits.html | AWS URL was not fetched/reachable |
| D | P1-AIP-D3-147 | Day03-order013 | 0 | 0.0 | https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html#events-sqs-eventsource-mapping | AWS URL was not fetched/reachable |
| D | P1-AIP-D3-148 | Day03-order013 | 0 | 0.0 | https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html#events-sqs-eventsource-mapping | AWS URL was not fetched/reachable |
| D | P1-AIP-D3-149 | Day03-order013 | 0 | 0.0 | https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html#events-sqs-eventsource-mapping | AWS URL was not fetched/reachable |
| D | P1-AIP-D3-150 | Day03-order013 | 0 | 0.0 | https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html | AWS URL was not fetched/reachable |
| D | P1-AIP-D3-151 | Day03-order013 | 0 | 0.0 | https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html#events-sqs-eventsource-mapping | AWS URL was not fetched/reachable |
| D | P1-AIP-D3-152 | Day03-order013 | 0 | 0.0 | https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html#events-sqs-eventsource-mapping | AWS URL was not fetched/reachable |
| D | P1-AIP-D3-153 | Day03-order013 | 0 | 0.0 | https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html#events-sqs-eventsource-mapping | AWS URL was not fetched/reachable |
| D | P1-AIP-D3-154 | Day03-order013 | 0 | 0.0 | https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html | AWS URL was not fetched/reachable |
| B | P1-AIP-D3-155 | Day03-order013 | 593 | 0.333 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order013-asynchronous-fm-processing.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-157 | Day03-order013 | 593 | 0.111 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order013-asynchronous-fm-processing.md | insufficient lexical support for conservative auto-approval |
| D | P1-AIP-D3-158 | Day03-order013 | 0 | 0.0 | https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-message-lifecycle.html | AWS URL was not fetched/reachable |
| D | P1-AIP-D3-159 | Day03-order014 | 0 | 0.0 | https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-chunked-transfer.html | AWS URL was not fetched/reachable |
| D | P1-AIP-D3-160 | Day03-order014 | 0 | 0.0 | https://docs.aws.amazon.com/lambda/latest/dg/configuration-response-streaming.html | AWS URL was not fetched/reachable |
| D | P1-AIP-D3-161 | Day03-order014 | 0 | 0.0 | https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-chunked-transfer.html | AWS URL was not fetched/reachable |
| D | P1-AIP-D3-162 | Day03-order014 | 0 | 0.0 | https://docs.aws.amazon.com/lambda/latest/dg/configuration-response-streaming.html | AWS URL was not fetched/reachable |
| D | P1-AIP-D3-163 | Day03-order014 | 0 | 0.0 | https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-chunked-transfer.html | AWS URL was not fetched/reachable |
| D | P1-AIP-D3-166 | Day03-order014 | 0 | 0.0 | https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-chunked-transfer.html | AWS URL was not fetched/reachable |
| D | P1-AIP-D3-168 | Day03-order014 | 0 | 0.0 | https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-chunked-transfer.html | AWS URL was not fetched/reachable |
| B | P1-AIP-D3-170 | Day03-order014 | 599 | 0.333 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order014-streaming-websockets-server-sent-events.md | insufficient lexical support for conservative auto-approval |
| D | P1-AIP-D3-171 | Day03-order015 | 0 | 0.0 | https://docs.aws.amazon.com/bedrock/latest/userguide/conversation.html | AWS URL was not fetched/reachable |
| D | P1-AIP-D3-172 | Day03-order016 | 0 | 0.0 | https://docs.aws.amazon.com/sdkref/latest/guide/feature-retry-behavior.html | AWS URL was not fetched/reachable |
| D | P1-AIP-D3-173 | Day03-order016 | 0 | 0.0 | https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html | AWS URL was not fetched/reachable |
| D | P1-AIP-D3-174 | Day03-order016 | 0 | 0.0 | https://docs.aws.amazon.com/sdkref/latest/guide/feature-retry-behavior.html | AWS URL was not fetched/reachable |
| D | P1-AIP-D3-175 | Day03-order016 | 0 | 0.0 | https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html | AWS URL was not fetched/reachable |
| B | P1-AIP-D3-176 | Day03-order016 | 51 | 0.231 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order016-retries-backoff-rate-limiting-timeouts.md | insufficient lexical support for conservative auto-approval |
| D | P1-AIP-D3-177 | Day03-order016 | 0 | 0.0 | https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html | AWS URL was not fetched/reachable |
| D | P1-AIP-D3-178 | Day03-order016 | 0 | 0.0 | https://docs.aws.amazon.com/sdkref/latest/guide/feature-retry-behavior.html | AWS URL was not fetched/reachable |
| B | P1-AIP-D3-180 | Day03-order016 | 582 | 0.273 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order016-retries-backoff-rate-limiting-timeouts.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-181 | Day03-order016 | 337 | 0.2 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order016-retries-backoff-rate-limiting-timeouts.md | insufficient lexical support for conservative auto-approval |
| D | P1-AIP-D3-182 | Day03-order016 | 0 | 0.0 | https://docs.aws.amazon.com/sdkref/latest/guide/feature-retry-behavior.html | AWS URL was not fetched/reachable |
| B | P1-AIP-D3-183 | Day03-order016 | 582 | 0.25 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order016-retries-backoff-rate-limiting-timeouts.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-184 | Day03-order016 | 51 | 0.167 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order016-retries-backoff-rate-limiting-timeouts.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-185 | Day03-order017 | 600 | 0.25 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order017-fallbacks-circuit-breakers-graceful-degradation.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-186 | Day03-order017 | 600 | 0.267 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order017-fallbacks-circuit-breakers-graceful-degradation.md | insufficient lexical support for conservative auto-approval |
| D | P1-AIP-D3-187 | Day03-order017 | 0 | 0.0 | https://docs.aws.amazon.com/general/latest/gr/api-retries.html#api-retries-circuit-breaker | AWS URL was not fetched/reachable |
| B | P1-AIP-D3-188 | Day03-order017 | 600 | 0.25 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order017-fallbacks-circuit-breakers-graceful-degradation.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-189 | Day03-order017 | 600 | 0.308 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order017-fallbacks-circuit-breakers-graceful-degradation.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-190 | Day03-order017 | 600 | 0.25 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order017-fallbacks-circuit-breakers-graceful-degradation.md | insufficient lexical support for conservative auto-approval |
| D | P1-AIP-D3-191 | Day03-order017 | 0 | 0.0 | https://docs.aws.amazon.com/general/latest/gr/api-retries.html#api-retries-circuit-breaker | AWS URL was not fetched/reachable |
| D | P1-AIP-D3-192 | Day03-order017 | 0 | 0.0 | https://docs.aws.amazon.com/general/latest/gr/api-retries.html#api-retries-circuit-breaker | AWS URL was not fetched/reachable |
| B | P1-AIP-D3-193 | Day03-order017 | 600 | 0.077 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order017-fallbacks-circuit-breakers-graceful-degradation.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-194 | Day03-order017 | 600 | 0.111 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order017-fallbacks-circuit-breakers-graceful-degradation.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-195 | Day03-order017 | 600 | 0.231 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order017-fallbacks-circuit-breakers-graceful-degradation.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-196 | Day03-order017 | 365 | 0.286 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order017-fallbacks-circuit-breakers-graceful-degradation.md | insufficient lexical support for conservative auto-approval |
| D | P1-AIP-D3-197 | Day03-order018 | 0 | 0.0 | https://docs.aws.amazon.com/xray/latest/devguide/xray-console.html | AWS URL was not fetched/reachable |
| D | P1-AIP-D3-198 | Day03-order018 | 0 | 0.0 | https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html | AWS URL was not fetched/reachable |
| D | P1-AIP-D3-199 | Day03-order018 | 0 | 0.0 | https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html | AWS URL was not fetched/reachable |
| D | P1-AIP-D3-200 | Day03-order018 | 0 | 0.0 | https://docs.aws.amazon.com/xray/latest/devguide/xray-console.html | AWS URL was not fetched/reachable |
| D | P1-AIP-D3-201 | Day03-order018 | 0 | 0.0 | https://docs.aws.amazon.com/xray/latest/devguide/xray-console.html | AWS URL was not fetched/reachable |
| D | P1-AIP-D3-202 | Day03-order018 | 0 | 0.0 | https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html | AWS URL was not fetched/reachable |
| D | P1-AIP-D3-203 | Day03-order018 | 0 | 0.0 | https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html | AWS URL was not fetched/reachable |
| D | P1-AIP-D3-204 | Day03-order018 | 0 | 0.0 | https://docs.aws.amazon.com/xray/latest/devguide/xray-console.html | AWS URL was not fetched/reachable |
| B | P1-AIP-D3-207 | Day03-order010 | 600 | 0.182 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order010-prompt-regression-testing-quality-assurance.md | insufficient lexical support for conservative auto-approval |
| B | P1-AIP-D3-209 | Day03-order010 | 600 | 0.214 | docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-03-artifacts/day03-order010-prompt-regression-testing-quality-assurance.md | insufficient lexical support for conservative auto-approval |
| D | P1-AIP-D3-210 | Day03-order015 | 0 | 0.0 | https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html | AWS URL was not fetched/reachable |
| D | P1-AIP-D3-211 | Day03-order015 | 0 | 0.0 | https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html | AWS URL was not fetched/reachable |
| D | P1-AIP-D3-212 | Day03-order015 | 0 | 0.0 | https://docs.aws.amazon.com/bedrock/latest/userguide/conversation.html | AWS URL was not fetched/reachable |
| D | P1-AIP-D3-213 | Day03-order015 | 0 | 0.0 | https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html | AWS URL was not fetched/reachable |
| D | P1-AIP-D3-214 | Day03-order015 | 0 | 0.0 | https://docs.aws.amazon.com/bedrock/latest/userguide/conversation.html | AWS URL was not fetched/reachable |
| D | P1-AIP-D3-215 | Day03-order015 | 0 | 0.0 | https://docs.aws.amazon.com/bedrock/latest/userguide/conversation.html | AWS URL was not fetched/reachable |
| D | P1-AIP-D3-216 | Day03-order015 | 0 | 0.0 | https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html | AWS URL was not fetched/reachable |
| D | P1-AIP-D3-217 | Day03-order015 | 0 | 0.0 | https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html | AWS URL was not fetched/reachable |
| D | P1-AIP-D3-218 | Day03-order015 | 0 | 0.0 | https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html | AWS URL was not fetched/reachable |
| D | P1-AIP-D3-219 | Day03-order018 | 0 | 0.0 | https://docs.aws.amazon.com/xray/latest/devguide/xray-console.html | AWS URL was not fetched/reachable |
| D | P1-AIP-D3-220 | Day03-order018 | 0 | 0.0 | https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html | AWS URL was not fetched/reachable |
| D | P1-AIP-D3-221 | Day03-order018 | 0 | 0.0 | https://docs.aws.amazon.com/xray/latest/devguide/xray-console.html | AWS URL was not fetched/reachable |
| D | P1-AIP-D3-222 | Day03-order018 | 0 | 0.0 | https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html | AWS URL was not fetched/reachable |
