# Day 3 Exam-Prep Review Outputs

This folder contains generated review artifacts for the day. Early in
the pipeline it contains normalized draft candidates; after the review
and source gates run it also contains reviewed candidate banks, cull
logs, source-verification reports, and gate status files.

- `day-03-normalized-draft-question-bank.md`: schema-shaped draft candidates; not approved.
- `day-03-normalization-report.md`: counts, parse status, and normalization warnings.
- `day-03-reviewed-question-bank.md`: reviewed candidates when present; not learner-release approved until final gates pass.
- `day-03-review-output-checks.md`: deterministic review-output checks when present.
- `day-03-answer-position-report.md`: answer-position distribution after rebalancing when present.
- `day-03-source-verification-report.md`: human source-review status when present.
- `day-03-claim-verification-ledger.json`: item-level claim verification worklist when present.

Do not publish reviewed candidates to learners until source verification
and final gates have passed.
