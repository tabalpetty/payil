# Pilot1 AIP-C01 Scripts

This folder contains automation that is intentionally specific to the Pilot1
AIP-C01 implementation.

These scripts may depend on:

- `docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json`
- `docs/Pilot1/aip-c01/exam-prep/source-catalog.json`
- the Pilot1 accelerated 7-day curriculum structure
- AIP-C01 topic and objective IDs
- AWS documentation URL rules and AWS service terminology
- Pilot1 exam-prep review, top-up, and source-verification artifacts

Keep the generic Curriculum Architecture Kit free of these assumptions. If a
script becomes subject-agnostic, move it out of this folder and document the
generic contract separately.

Run commands from the repository root, for example:

```bash
python3 scripts/pilot1_aip_c01/run_exam_prep_agent_prefect.py --day 3 --local-engine
python3 scripts/pilot1_aip_c01/audit_source_decomposition_coverage.py --strict
```

Source verification for existing reviewed exam-prep banks is intentionally
split into three auditable layers:

```bash
python3 scripts/pilot1_aip_c01/verify_exam_prep_source_urls.py --day 3 --write
python3 scripts/pilot1_aip_c01/verify_exam_prep_claims_with_sources.py --day 3 --write
python3 scripts/pilot1_aip_c01/triage_exam_prep_source_review.py --day 3 --write
python3 scripts/pilot1_aip_c01/verify_exam_prep_sources.py --day 3 --initialize-ledger --write
```

The URL verifier checks and caches official AWS documentation URLs. The claim
verifier checks the item-level atomic-claim ledger against trusted local files
and cached AWS source text. The triage script splits unresolved items into
next-action buckets so the queue can be reduced mechanically where possible.
The final source verifier applies the release status to the reviewed bank and
keeps unresolved claims as `needs-human-source-review`.

Use the grounded judge only when intentionally spending model calls:

```bash
python3 scripts/pilot1_aip_c01/judge_exam_prep_claims_with_evidence.py --day 3 --buckets A --dry-run --limit 2 --write
python3 scripts/pilot1_aip_c01/judge_exam_prep_claims_with_evidence.py --day 3 --buckets A --write --apply-supported --min-confidence 0.92
```

It can auto-apply high-confidence `supported` judgments to the claim ledger.
`refuted` and `insufficient` judgments remain review/cull/rewrite work.

Prefer upstream source grounding before using the grounded judge. For new raw
generation, update the course source catalog first, build prompts from that
catalog, and require generated lean items to include:

- tough scenario stem, options, correct answer, and distractor explanations;
- exact allowed `source_trace` URL/path;
- `evidence_span`;
- `defensible_correct_answer`;
- `defensibility_check=pass`.

The normalizer fills mechanical curriculum metadata and derives
`source_contract_version=source-grounded-v1`, `allowed_source_id`, and
`atomic_claims` from the lean source fields and the course catalog.

The review script enforces this contract for new items and can enforce it for
older items with:

```bash
python3 scripts/pilot1_aip_c01/review_exam_prep_questions.py --day 3 --enforce-source-contract
```

When a generation/review pass discovers a useful new AWS source, add it to the
course catalog only after it has a reachable URL/path, a mapped curriculum
topic, and source-review evidence showing that it supports the intended claim
family.
