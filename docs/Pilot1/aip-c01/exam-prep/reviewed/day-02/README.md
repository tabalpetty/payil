# Reviewed Day 2

This folder contains the normalized input, reviewed-candidate pass, top-up
feedback, Step 12 review outputs, Step 13 source verification, and final gates
for Day 2 exam-prep review.

- `day-02-normalized-draft-question-bank.md`: schema-shaped draft candidates; not approved.
- `day-02-normalization-report.md`: counts, parse status, and normalization warnings.
- `day-02-reviewed-candidate-bank.md`: Step 9 reviewed-candidate pass with cull evidence and top-up guidance.
- `day-02-review-feedback.json`: machine-readable review feedback consumed by top-up generation.
- `day-02-reviewed-question-bank.md`: Step 12 reviewed bank form for final gates.
- `day-02-cull-log.md`: Step 12 standalone cull log with evidence.
- `day-02-review-output-checks.md`: Step 12 human-readable review-output checks.
- `day-02-review-output-checks.json`: Step 12 machine-readable review-output checks.
- `day-02-source-verification-report.md`: Step 13 source-verification report.
- `day-02-source-verification.json`: Step 13 machine-readable source-verification results.
- `day-02-final-gate-report.md`: Step 13 final gate report.
- `day-02-final-gates.json`: Step 13 machine-readable final gate results.

Step 13 currently reports `completion_status=complete` for the reviewed bank.
If the project wants a separately named approved bank, promote this
source-verified reviewed bank without regenerating Step 12 outputs.
