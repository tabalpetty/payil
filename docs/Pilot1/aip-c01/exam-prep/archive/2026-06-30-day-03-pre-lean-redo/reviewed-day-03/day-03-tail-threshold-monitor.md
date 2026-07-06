# Day 3 Tail Threshold Monitor

Generated: 2026-06-29

Status: `breach`

## Thresholds

| Tail | Limit | Actual | Count | Status |
|---|---:|---:|---:|---|
| LLM repair/judge tail | 15% | 72.2% | 153/212 | breach |
| Human source-review tail | 5% | 72.2% | 153/212 | breach |

## Breaches

- llm_repair_tail: 153/212 (72.2%) exceeds 15%. Too many items require LLM repair/judgment after deterministic verification.
- human_review_tail: 153/212 (72.2%) exceeds 5%. Too many reviewed items still require human source review.
