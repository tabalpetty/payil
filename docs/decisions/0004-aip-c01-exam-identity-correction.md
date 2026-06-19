# Decision 0004: AIP-C01 Exam Identity Correction

## Status

Accepted on June 18, 2026.

## Decision

The reference implementation targets **AWS Certified Generative AI Developer -
Professional (AIP-C01)**.

Any project material that describes the target as AWS Certified AI
Practitioner, AIF-C01, foundational, or practitioner-level is incorrect unless
it is explicitly comparing AIP-C01 with another certification.

## Rationale

The project source materials and repository structure were created for
AIP-C01. During exam-preparation documentation work, AIF-C01 information was
incorrectly introduced from the AWS Certified AI Practitioner guide. That
created a serious alignment error because AIP-C01 and AIF-C01 have different
candidate expectations, domains, question counts, duration, passing score, and
depth of skill.

AIP-C01 is a professional exam for candidates who perform a GenAI developer
role and implement production-grade GenAI solutions on AWS. The curriculum,
teacher kit, student kit, exam-prep materials, question-bank tags, practice
tests, and readiness gates must align to the AIP-C01 exam guide.

## Consequences

- AIF-C01 and AWS Certified AI Practitioner references must be removed from
  AIP-C01 materials unless used only for explicit comparison.
- The official AIP-C01 exam guide is the authority for exam identity, candidate
  assumptions, domain names, task statements, question formats, timing, scoring,
  and pass/fail criteria.
- Existing Layer 0 materials may be retained only as prerequisite/foundation
  material if they support the professional exam dependency path.
- Existing Teacher Kit and Student Kit content must be audited against the
  official AIP-C01 domain/task/skill outline before being treated as valid
  exam-aligned material.
- Future generated questions must use AIP-C01, not AIF-C01, in prompts,
  manifests, source traces, and item IDs.
