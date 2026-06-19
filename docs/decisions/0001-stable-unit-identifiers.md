# Decision 0001: Stable Unit Identifiers

## Status

Accepted on June 15, 2026.

## Decision

Use a stable unit identifier in the form `L<layer>-U<two-digit sequence>` for
every AIP-C01 learning unit. Example: `L0-U01`.

The same identifier must connect:

`source objective -> curriculum definition -> Teacher Kit -> Student Kit ->
learner artifact -> assessment -> remediation -> generated artifact`

Directory names may append a readable slug, but the identifier must remain the
first component. Unit identity does not change when titles or wording are
refined.

## Rationale

The project needs reliable traceability across several artifact families.
Stable identifiers make coverage review, cross-linking, generation, and later
automation possible without depending on titles as keys.

## Consequences

- Curriculum, teacher, and student materials must use the same ID.
- New units receive IDs from the established dependency order.
- Generated files should include the unit ID in their filenames or metadata.
- A unit split or merge requires an explicit mapping decision rather than
  silently reusing an old identifier.

