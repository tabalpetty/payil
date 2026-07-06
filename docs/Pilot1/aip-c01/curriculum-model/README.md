# Pilot1 AIP-C01 Curriculum Model

This directory will contain the curriculum model for **AWS Certified Generative
AI Developer - Professional (AIP-C01)**.

Start with:

- [source-identity-checkpoint.md](source-identity-checkpoint.md)
- [accelerated-path-design.md](accelerated-path-design.md)
- [accelerated-7-day-plan.md](accelerated-7-day-plan.md)
- [aip-c01-topic-knowledge-category-map.md](aip-c01-topic-knowledge-category-map.md)
- [source-to-topic-traceability-matrix.md](source-to-topic-traceability-matrix.md)
- [source-to-decomposition-coverage-audit.md](source-to-decomposition-coverage-audit.md)
- [source-to-decomposition-deferrals.md](source-to-decomposition-deferrals.md)

## Supported Pacing Tracks

Pilot1 supports two pacing tracks.

### Self-Paced Track

The self-paced track is the default route. Learners use the available
materials, activities, assessments, remediation, and exam-prep resources on
their own schedule.

Mastery gates still apply. A learner progresses when evidence shows readiness,
not merely because they have spent time with the material.

### 7-Day Accelerated Track

The 7-day accelerated track is a compressed route for ambitious learners.

It assumes:

- relevant prerequisite knowledge before starting;
- at least six hours of active learning per day for seven days;
- enough technical maturity to work through dense professional-level material;
- independence in labs, documentation review, scenario analysis, and exam-style
  reasoning;
- willingness to use evenings or extra time for remediation if gaps appear.

This route increases intensity. It does not lower mastery gates or
exam-readiness standards.

## Curriculum Modeling Rule

When units are generated, each unit should identify how it appears in the
self-paced route and whether it is included, compressed, deferred, or used as
review in the 7-day accelerated route.

## Source-To-Decomposition Coverage Gate

Before generating downstream topic briefs, prompt packs, question banks, or
teaching packages for new days, run:

```bash
python3 scripts/pilot1_aip_c01/audit_source_decomposition_coverage.py --strict
```

The gate compares the official AIP-C01 objective hierarchy in
`docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
against the curriculum decomposition. An official objective must be explicitly
covered or explicitly deferred. Day-level task coverage alone is not enough
when downstream artifacts claim skill-level traceability.
