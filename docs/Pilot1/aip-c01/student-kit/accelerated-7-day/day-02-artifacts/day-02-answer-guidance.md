# Day 2 Answer Guidance And Exemplars

## How To Use This File

Attempt the blank artifacts first. Use this file only after you have produced
your own answer. Its job is calibration: it shows what a strong answer sounds
like and why it earns mastery evidence.

For Day 2, a score of `3` means the answer connects data, metadata, retrieval,
security, freshness, and evaluation. A weak answer says "use RAG" without
showing how retrieval context is prepared, controlled, tested, and repaired.

## Shared Scenario For Exemplars

A company is building an internal policy assistant. Employees ask questions
about HR, travel, security, and procurement policies. Source content includes
PDFs, HTML pages, spreadsheets, tables, screenshots, and policy updates from
several teams. Answers must cite approved sources, respect employee
entitlements, avoid stale policy versions, and produce evidence for audit.

## Day02-order001: Data-Quality Validation And Monitoring

Strong validation runbook excerpt:

| Step | Action | Evidence to record |
|---:|---|---|
| 2 | Check duplicates and versions. | Compare source IDs, canonical URLs, checksums, and version fields; keep only the approved current version. |
| 3 | Check required metadata. | Block records missing owner, effective date, access group, or source URL. |
| 7 | Record owner, threshold, and monitoring action. | If more than 2% of new chunks lack access labels, pause ingestion and notify the content steward. |

Strong cause-effect row:

| Data issue | Likely retrieval or answer effect | Repair or control |
|---|---|---|
| Stale policy version | The assistant cites an outdated rule even if the model summarizes correctly. | Filter by effective date/version and retire superseded chunks during ingestion. |

What makes this strong:

- treats data quality as a retrieval control;
- names observable evidence, not only a general cleanup idea.

## Day02-order002: Multimodal Data Preprocessing

Strong decision table excerpt:

| Source type | Preprocessing needed | Why | Reject or avoid |
|---|---|---|---|
| PDF | Extract text with page numbers, headings, table structure, and source URL. | Citations and chunk boundaries need page/section traceability. | Do not ingest OCR text if reading order is broken. |
| Table or spreadsheet | Preserve headers, units, row labels, sheet name, and effective date. | Values are meaningless without labels and units. | Do not flatten cells into unlabeled prose. |
| Image or screenshot | OCR visible text and preserve image/page reference. | Policy screenshots may contain text not present elsewhere. | Do not treat OCR as trusted if confidence is low. |

What makes this strong:

- chooses preprocessing from modality;
- protects meaning and traceability before retrieval.

## Day02-order003: Input Formatting And Normalization

Strong normalized record:

| Field | Value | Why it is needed |
|---|---|---|
| `source_id` | `hr-remote-work-2026` | Links chunks to the authoritative policy. |
| `chunk_id` | `hr-remote-work-2026-sec-3-p2` | Identifies the retrievable unit. |
| `title` | Remote Work Policy | Supports citation and user trust. |
| `effective_date` | `2026-01-01` | Enables freshness filtering. |
| `access_group` | `employees` | Prevents retrieval for unauthorized users. |
| `modality` | `pdf_text` | Records extraction path and limits. |
| normalized text | "Employees may request..." | The text embedded and retrieved by the system. |

What makes this strong:

- keeps source traceability and retrieval input together;
- includes fields for citation, freshness, and access control.

## Day02-order004: Embeddings And Vector Similarity

Strong concept-map notes:

```text
The policy chunk is converted by an embedding model into a vector. The user
query is embedded with the same compatible approach. Semantic search compares
the query vector with chunk vectors and returns nearby chunks. Metadata filters
still decide whether the user is allowed to retrieve each candidate.
```

Strong boundary notes:

| Embeddings help with | Embeddings do not solve by themselves |
|---|---|
| Finding relevant text when query wording differs from the source. | Authorization, freshness, source authority, or data lifecycle. |
| Grouping semantically related policy chunks. | Whether a policy is current or approved. |

What makes this strong:

- explains the retrieval mechanism;
- avoids treating embeddings as security or governance controls.

## Day02-order005: Document Chunking And Segmentation

Strong decision table excerpt:

| Approach | Strength | Weakness | Use or reject for the policy assistant? |
|---|---|---|---|
| Section-based chunking | Preserves policy headings and exceptions. | Depends on clean document structure. | Use for well-structured HR and travel policies. |
| Fixed-size chunking | Simple and predictable. | Can split rules from exceptions. | Reject as the primary strategy for policy PDFs. |
| Table-aware chunking | Preserves headers, units, and row labels. | Requires extra extraction logic. | Use for reimbursement tables and procurement thresholds. |

Strong cause-effect row:

| Chunking change | Predicted effect | Risk to test |
|---|---|---|
| Make chunks smaller | Retrieval may be more precise. | The answer may miss an exception in the next paragraph. |
| Add overlap | Boundary cases are less likely to lose context. | Duplicate chunks may crowd out diverse results. |

What makes this strong:

- connects chunking choice to source structure and failure modes;
- tests the decision instead of assuming one default.

## Day02-order006: Metadata Design And Filtering

Strong metadata schema excerpt:

| Metadata field | Type | Required? | Used for filtering, ranking, security, or audit? |
|---|---|---|---|
| `source_id` | string | Yes | citation and audit |
| `effective_date` | date | Yes | freshness filtering |
| `version` | string | Yes | conflict resolution and audit |
| `access_group` | string/list | Yes | security filtering |
| `jurisdiction` | string/list | Conditional | conditional retrieval |
| `source_url` or page | string | Yes | citation |

Strong filter decision:

| Scenario | Filter needed | Why | Risk if missing |
|---|---|---|---|
| User is in a restricted employee group | `access_group` entitlement filter before retrieval | Unauthorized chunks must never enter prompt context. | The model may summarize content the user cannot view. |

What makes this strong:

- treats metadata as a control surface;
- places security filtering before prompt assembly.

## Day02-order007: Vector-Store Architecture

Strong architecture decision matrix excerpt:

| Requirement | Architecture implication | Candidate choice | Rejected alternative |
|---|---|---|---|
| Managed RAG integration | Prefer a managed path if default ingestion, retrieval, and service integration are enough. | Bedrock Knowledge Bases candidate | Fully custom service if the team lacks operations capacity. |
| Hybrid keyword + vector retrieval | Need search architecture that supports both semantic and lexical signals. | OpenSearch-style search/vector architecture candidate | Vector-only path if exact policy IDs or terms matter. |
| Strict access control | Metadata filtering and IAM/resource controls must be first-class. | Store with filter and access-control support | Store that only returns nearest vectors without secure filters. |

Strong mini ADR:

```text
Decision: Use a managed RAG path for the pilot and preserve normalized source
records so the index can be rebuilt.
Tradeoff: Faster integration and less infrastructure work, but less custom
ranking control than a custom retrieval service.
Evidence needed: Verify metadata filters, source sync behavior, latency, and
retrieval quality on the golden retrieval set.
```

What makes this strong:

- chooses from requirements, not service popularity;
- keeps verification work explicit.

## Day02-order008: Vector Indexing, Scaling, And Performance

Strong operations runbook excerpt:

| Step | Action | Evidence |
|---:|---|---|
| 3 | Check index freshness and changed-document counts. | Latest source update timestamp is later than latest index update; failed sync count is zero. |
| 4 | Check query latency and timeout rate. | p95 retrieval latency and timeout alarms remain within the target. |
| 5 | Check retrieval quality on a golden set. | Expected source appears in top results for happy-path and paraphrase queries. |

Strong cause-effect row:

| Operational condition | Likely effect | Evidence to inspect |
|---|---|---|
| Filter is too narrow | Correct source exists but no chunks are returned. | Compare results before and after the filter; inspect entitlement metadata. |

What makes this strong:

- identifies operational evidence;
- links performance and freshness to user-visible retrieval failures.

## Day02-order009: Basic Semantic Retrieval

Strong retrieval runbook excerpt:

| Step | Action | Evidence |
|---:|---|---|
| 3 | Apply access and freshness filters. | Query includes caller entitlement and current-version constraints. |
| 4 | Retrieve top candidate chunks. | Top results include source IDs, scores, and metadata. |
| 6 | Record failure signal if expected context is missing. | Log expected source, returned source IDs, filters, and query text. |

Strong retrieval test case:

| Test type | Test query | Expected retrieved content | Filter expectation | Failure signal |
|---|---|---|---|---|
| Paraphrase | "Can I expense home internet?" | Remote-work reimbursement policy section | employee access, current version | Exact "home internet" wording missing but semantically related section should appear. |
| Access control | "Show finance travel exception rules" from non-finance user | No restricted finance-only content | finance-only chunks excluded | Any restricted chunk in results is a failure. |

What makes this strong:

- tests meaning, not only exact keywords;
- includes security and freshness as retrieval tests.

## Day02-order010: Basic RAG Design

Strong RAG architecture summary:

```text
The user is authenticated before retrieval. The application normalizes the
question, embeds the query, applies entitlement and current-version filters,
retrieves policy chunks with source IDs, builds a prompt using only those
chunks, invokes the model, validates that the answer cites retrieved sources,
and records sanitized logs plus retrieval-test evidence.
```

Strong strategic tradeoff:

| Decision | Option A | Option B | Chosen option and why |
|---|---|---|---|
| Filtering | Strict filters | Broad filters | Strict filters for employee policy answers because unauthorized context is a higher risk than an empty answer. |
| Evaluation | Manual review only | Golden retrieval and answer set | Golden set because retrieval regressions need repeatable evidence. |

What makes this strong:

- integrates data, retrieval, prompt assembly, and validation;
- makes the security and evaluation tradeoffs visible.

## Calibration Rubric

| Score | Evidence |
|---:|---|
| 3 | Scenario-specific, technically plausible, includes data/retrieval controls, rationale, failure mode, and evidence to inspect. |
| 2 | Mostly correct but generic, missing a key field, weak on why, or incomplete on evidence. |
| 1 | Recognizes terms but cannot connect data preparation to retrieval and answer quality. |
| 0 | Blank, unsafe, technically wrong, or contradicts the scenario. |

## Reassessment Path

If your answer scores below `3`, classify the gap first.

| Gap | Remediation |
|---|---|
| Data-quality gap | Rebuild the validation runbook and add one monitoring threshold. |
| Preprocessing gap | Fill the modality decision table for PDF, table, and image sources. |
| Metadata/security gap | Add `access_group`, `effective_date`, `version`, and citation fields to the schema. |
| Chunking gap | Add one too-small and one too-large failure case. |
| Vector-store architecture gap | Write a mini ADR with one chosen and one rejected option. |
| Retrieval-testing gap | Add happy-path, paraphrase, missing-context, access-control, and freshness tests. |
