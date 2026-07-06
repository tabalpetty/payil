# Day 2 Study Guide: Data, Embeddings, Vector Stores, And Basic RAG

## What You Are Learning Today

Day 2 teaches the retrieval foundation for GenAI systems. Retrieval-augmented
generation, or RAG, gives the model selected external context at inference time
instead of expecting the model to know, remember, or search every source by
itself.

The exam expects more than the phrase "use RAG." You need to reason about data
quality, preprocessing, model-specific input formatting, embeddings, chunking,
metadata, vector-store architecture, indexing, semantic retrieval, and the
basic RAG request path.

By the end of today, you should be able to explain and defend this chain:

```text
Source data
  -> validation and monitoring
  -> preprocessing and normalization
  -> chunking and segmentation
  -> metadata and access labels
  -> embedding generation
  -> vector/index storage
  -> query embedding
  -> retrieval, filtering, and ranking
  -> prompt context assembly
  -> model answer with citations
  -> evaluation, monitoring, and repair
```

If a RAG answer is bad, the model may not be the root cause. The source data,
chunking, metadata, embedding model, index freshness, filters, ranking, prompt
assembly, or evaluation set may be the real failure point.

Acceleration note: Day 2 can be intense, but it should not be thin. If you
cannot defend the data-quality checks, chunking decision, metadata/access
labels, embedding/search behavior, and basic RAG path, extend the study block
or record explicit remediation. Retrieval gaps compound quickly on Day 3.

## Day 2 Scenario

Use this shared scenario in the artifacts and answer guidance.

A company is building an internal policy assistant. Employees ask questions
about HR, travel, security, and procurement policies. Source content includes
PDFs, HTML pages, spreadsheets, tables, screenshots, and policy updates from
several teams. Answers must cite approved sources, respect employee
entitlements, avoid stale policy versions, and produce evidence for audit.

## Data Quality Validation And Monitoring

Data quality is not a one-time cleanup step. It is a control loop:

```text
inspect source -> detect issue -> repair or quarantine -> ingest -> monitor
```

Common validation checks:

| Check | What it catches | Repair or control |
|---|---|---|
| Duplicate detection | Same document, chunk, or policy loaded multiple times | Deduplicate by source ID, checksum, version, or canonical URL. |
| Freshness check | Expired or superseded policy content | Use effective date, owner, version, and lifecycle status. |
| Metadata completeness | Missing owner, title, access group, source, or effective date | Block ingestion or route to steward for completion. |
| Format validation | Broken extraction, unreadable PDFs, malformed CSV, bad encoding | Reprocess, convert format, or quarantine. |
| Conflict check | Two sources answer the same question differently | Prefer authoritative source hierarchy or flag for owner review. |
| Sensitive-data check | PII, secrets, customer data, confidential terms | Redact, restrict, encrypt, or exclude from retrieval. |
| Access-label check | Content lacks entitlement or audience labels | Do not make the content retrievable until labels exist. |

Monitoring repeats selected checks after ingestion. A strong monitoring plan
names the signal, threshold, owner, and action. Example: "If more than 2% of
new chunks lack access labels, pause ingestion and notify the content steward."

## Preprocessing For Text, Images, Audio, Tables, And Tabular Data

Preprocessing converts source material into a form the retrieval system can
index and use safely.

| Source type | Typical preprocessing | Common risk |
|---|---|---|
| Text or HTML | Remove boilerplate, preserve headings, normalize whitespace, keep source URL and section IDs | Stripping headings can destroy retrieval context. |
| PDF | Extract text, tables, page numbers, headings, and citations when possible | Bad OCR or reading order can produce misleading chunks. |
| Image or screenshot | OCR text, extract captions/alt text, preserve image reference | Important visual context may be lost if only OCR text is used. |
| Audio or video | Transcribe, segment by speaker/time, preserve timestamps | Transcription errors can corrupt policy meaning. |
| Tables/spreadsheets | Preserve headers, units, row/column labels, and sheet names | Flattening a table without labels can make values meaningless. |
| Tabular records | Normalize fields, types, keys, dates, and null values | Inconsistent schema can break filtering or joins. |

Use a decision table for preprocessing:

| Condition | Preprocessing decision |
|---|---|
| The document has stable headings | Preserve headings and section hierarchy for chunking. |
| The source has tables | Extract tables with headers and units; do not treat values as plain paragraphs only. |
| The source has images with important text | OCR and keep image/page reference. |
| The source has sensitive fields | Redact, mask, or apply access labels before retrieval. |
| The source is low quality or ambiguous | Quarantine or require owner review before ingestion. |

## Model-Specific Input Formatting And Data Normalization

Every embedding or generation model expects inputs in a supported shape. The
exact API schema varies by model, but the stable habit is the same:

1. know the model task;
2. know the input type and limits;
3. normalize content before sending it;
4. preserve traceability to the source;
5. validate output shape before downstream use.

Useful normalization fields:

| Field | Why it matters |
|---|---|
| `source_id` | Links chunks back to the original document. |
| `chunk_id` | Identifies the retrievable unit. |
| `title` and `section` | Help the answer cite and explain source context. |
| `effective_date` and `version` | Support freshness filtering. |
| `owner` | Supports stewardship and audit. |
| `access_group` or entitlement label | Prevents unauthorized retrieval. |
| `modality` | Records whether content came from text, table, image, audio, or mixed source. |
| normalized text | Input actually embedded or retrieved. |

Do not send raw, unbounded, or unlabeled source content into embedding or
generation steps. A normalized record makes later retrieval, filtering,
debugging, and citation possible.

An input limit is the maximum size, format, or token/file boundary accepted by
the selected embedding, parsing, ingestion, or generation step. If a source,
chunk, table, image, or prompt context exceeds that limit, split, transform,
summarize, or quarantine it before sending it downstream.

## Embeddings And Vector Similarity

An embedding is a numeric representation of content. Similar meanings should
land closer together in vector space than unrelated meanings. A vector search
system compares query embeddings to document or chunk embeddings and returns
nearby candidates.

Key terms:

| Term | Plain meaning | Why it matters |
|---|---|---|
| Embedding model | Model that turns text, image, or other input into vectors | Must fit the content language, modality, and task. |
| Vector | Numeric representation of input content | Used for similarity search. |
| Vector store | System that stores vectors and metadata for retrieval | Must support indexing, filtering, scaling, access, and recovery needs. |
| Similarity metric | Method for comparing vectors, such as cosine similarity or distance | The retrieval score depends on the metric and embedding behavior. |
| Semantic search | Search by meaning rather than only exact keywords | Helps when wording differs between query and source. |

Embeddings do not understand authorization, freshness, or source authority by
themselves. Those require metadata, filters, policies, and evaluation.

## Chunking And Segmentation

Chunking divides source material into retrievable units. The best chunk is
large enough to preserve meaning and small enough to retrieve precisely.

| Approach | Works well when | Risk |
|---|---|---|
| Fixed-size chunking | Content is regular and simple | Can split meaning across boundaries. |
| Section-based chunking | Documents have headings and stable structure | Poor headings or inconsistent structure can hurt quality. |
| Hierarchical chunking | You need document, section, and paragraph context | More complex indexing and context assembly. |
| Semantic chunking | Meaning boundaries matter more than size | Requires more processing and validation. |
| Table-aware chunking | Tables carry important policy values | Values become misleading if headers, units, or row labels are lost. |

Use this cause-effect rule:

| Chunking change | Likely effect | Risk to test |
|---|---|---|
| Chunks too small | Precise retrieval but missing context | Answer may cite a fragment without the rule or exception. |
| Chunks too large | More context per hit | Retrieval may return irrelevant text and waste context window. |
| Preserve headings | Better source meaning and citation | Bad headings can mislead ranking. |
| Add overlap | Reduces boundary loss | Increases duplicate retrieval and index size. |

## Metadata Design And Filtering

Metadata is a control surface. It supports filtering, ranking, security,
freshness, audit, and operations.

Strong metadata fields for the policy assistant:

| Field | Used for | Example |
|---|---|---|
| `source_id` | citation and audit | `hr-remote-work-2026` |
| `source_type` | filtering and processing | `policy_pdf`, `spreadsheet`, `html_page` |
| `owner` | stewardship | `HR Policy` |
| `effective_date` | freshness | `2026-01-01` |
| `version` | conflict resolution | `v3` |
| `access_group` | security filtering | `employees`, `managers`, `finance` |
| `jurisdiction` | conditional retrieval | `US`, `EU`, `India` |
| `topic` | ranking and browse support | `travel`, `security`, `benefits` |
| `source_url` or `page` | citation | canonical URL or page number |

Filtering rules should happen before the model sees the context. If a user is
not entitled to a document, do not rely on the model to hide it after
retrieval.

## Vector-Store Technologies And Architecture

Day 2 does not require deep vendor comparison. It does require the architecture
questions.

| Decision | What to ask |
|---|---|
| Managed vs self-managed | Who operates scaling, patching, backups, and availability? |
| Metadata filtering | Can the store filter by access group, freshness, owner, or jurisdiction? |
| Hybrid retrieval | Do we need keyword plus vector search? |
| Index lifecycle | How are new, changed, and retired documents handled? |
| Security | How are IAM, network path, encryption, and resource policies applied? |
| Observability | Can we inspect query latency, hit quality, errors, and index freshness? |
| Recovery | Can the index be rebuilt from source records and embedding jobs? |

AWS-relevant options to recognize include Amazon Bedrock Knowledge Bases for a
managed RAG path, Amazon OpenSearch Service for search/vector-search
architectures, and other supported vector-store choices depending on the
service and account configuration. Verify current service availability before
making a production decision.

Hybrid keyword-plus-vector retrieval appears here only as an architecture
requirement to recognize. Day 3 covers hybrid search and custom scoring in more
implementation depth.

## Vector Indexing, Sharding, Scaling, And Performance

Index design affects retrieval speed, quality, and operations.

| Concern | Meaning | Evidence to inspect |
|---|---|---|
| Index freshness | Whether latest documents are searchable | Ingestion timestamp, changed-document count, failed jobs. |
| Query latency | Time to retrieve candidates | p50/p95 retrieval latency, timeout rate. |
| Recall quality | Whether relevant chunks appear | Golden retrieval set and missed-source review. |
| Filter selectivity | Whether filters narrow the search too much or too little | Results count before/after filters. |
| Scale and partitioning | Whether corpus size affects search performance | index size, shard/partition health, memory/capacity metrics. |
| Rebuild path | Whether the index can be recovered | source records, embedding job logs, infrastructure config. |

Day 2 does not ask you to tune a production index. It asks you to know which
operational signals would reveal a broken or unhealthy retrieval layer.

## Basic Semantic Retrieval

Basic semantic retrieval turns a user query into a retrieval request.

```text
user query
  -> normalize query
  -> embed query
  -> apply entitlement/freshness filters
  -> retrieve top candidates
  -> rank/select context
  -> assemble prompt context with citations
```

Retrieval test cases should include:

| Test type | Purpose |
|---|---|
| Happy path | The obvious source is retrieved. |
| Paraphrase | The query uses different wording than the source. |
| Missing context | No relevant source should be retrieved or the answer should escalate. |
| Access control | Unauthorized content must not be returned. |
| Freshness | Retired or superseded content should not be selected. |

## Basic RAG Design

RAG is not just "put a vector store in front of the model." A strong basic RAG
design names the request path, data path, controls, evaluation, and tradeoffs.

Minimal request path:

```text
authenticated user
  -> application validates request
  -> retrieval query is built
  -> filters apply entitlement and freshness
  -> relevant chunks are retrieved
  -> prompt context is assembled with source IDs
  -> model generates answer
  -> output is validated for source grounding and policy constraints
  -> logs/evaluation records are stored without leaking sensitive content
```

Basic RAG tradeoffs:

| Decision | Tradeoff |
|---|---|
| Smaller chunks | More precise retrieval but higher risk of missing context. |
| Larger chunks | More context but more irrelevant text and token cost. |
| Strict filters | Better security/freshness but possible empty results. |
| Broad filters | Better recall but greater risk of irrelevant or unauthorized context. |
| Managed RAG service | Faster integration and less infrastructure work. |
| Custom retrieval architecture | More control but more operational responsibility. |

## Common Misconceptions

| Misconception | Better view |
|---|---|
| RAG means the model searches the documents. | The application retrieves context and gives selected context to the model. |
| A vector store fixes bad data. | Bad data and missing metadata still produce poor retrieval. |
| Bigger chunks are always safer. | Large chunks can dilute relevance and waste context. |
| Embeddings enforce security. | Authorization needs metadata, filters, IAM, and application controls. |
| One good answer proves retrieval works. | Retrieval needs a golden set with happy, paraphrase, missing-context, access, and freshness cases. |
| If the answer is wrong, change the model first. | Inspect data, chunking, filters, index freshness, and retrieved context before blaming the model. |

## Source Notes

Official AWS documentation to check when making live service decisions:

- Amazon Bedrock Knowledge Bases User Guide:
  <https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html>
- Amazon Bedrock data sources for knowledge bases:
  <https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-ds.html>
- Amazon Bedrock supported models and Regions for knowledge bases:
  <https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-supported.html>
- Amazon Bedrock build a knowledge base by connecting to a data source:
  <https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-build.html>
- Amazon OpenSearch Service vector search:
  <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/vector-search.html>
- Amazon S3 User Guide:
  <https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html>

## Teach-Back

Close the guide and explain:

1. Why data validation is part of RAG quality.
2. How preprocessing changes by modality.
3. Why chunking and metadata are design decisions.
4. Why retrieval failure can look like model failure.
5. How you would test whether a basic RAG path is working.

Then complete the Day 2 focused artifacts.
