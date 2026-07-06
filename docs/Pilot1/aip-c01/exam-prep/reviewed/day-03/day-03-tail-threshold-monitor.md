# Day 3 Tail Threshold Monitor

Generated: 2026-06-30

Status: `breach`

## Thresholds

| Tail | Limit | Actual | Count | Status |
|---|---:|---:|---:|---|
| LLM repair/judge tail | 15% | 76.6% | 170/222 | breach |
| Human source-review tail | 5% | 76.6% | 170/222 | breach |

## Breaches

- llm_repair_tail: 170/222 (76.6%) exceeds 15%. Too many items require LLM repair/judgment after deterministic verification.
- human_review_tail: 170/222 (76.6%) exceeds 5%. Too many reviewed items still require human source review.
