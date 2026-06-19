# Decision 0006: Pilot Source Material Boundary

## Status

Accepted on June 18, 2026.

## Decision

Move Pilot1 AIP-C01 source materials from the top-level `source-material/`
directory into:

`docs/Pilot1/aip-c01/source-material/`

Remove the top-level `source-material/` directory.

## Rationale

The source files are useful for rebuilding Pilot1 because they are aligned to
AWS Certified Generative AI Developer - Professional (AIP-C01). However, they
are implementation-specific artifacts, not generic Curriculum Architecture Kit
materials.

Keeping them under Pilot1 preserves a tight repository structure:

- reusable methodology stays in `docs/curriculum-architecture-kit/`;
- Pilot1 implementation inputs and outputs stay in `docs/Pilot1/aip-c01/`;
- decision records stay in `docs/decisions/`.

## Consequences

- Future AIP-C01 rebuild work should read trusted project inputs from
  `docs/Pilot1/aip-c01/source-material/`.
- Do not recreate a top-level `source-material/` directory unless a future
  project-wide source area is explicitly needed.
- Generated spreadsheets remain planning views, not the sole source of truth.
