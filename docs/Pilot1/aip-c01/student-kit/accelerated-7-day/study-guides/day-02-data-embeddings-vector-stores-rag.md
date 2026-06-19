# Day 2 Study Guide: Data, Embeddings, Vector Stores, And Basic RAG

## What You Are Learning Today

Day 2 teaches the retrieval foundation. Retrieval-augmented generation, or RAG,
is a way to give the model relevant external context at inference time instead
of expecting the model to already know or remember everything.

The exam expects more than the phrase "use RAG." You need to reason about data
quality, chunking, metadata, embeddings, vector stores, filtering, access, and
retrieval failure.

## The Core Mental Model

```text
Source documents
  -> validation and cleaning
  -> segmentation/chunking
  -> metadata assignment
  -> embedding generation
  -> vector/index storage
  -> query transformation
  -> retrieval/filtering/ranking
  -> prompt context assembly
  -> model answer
  -> citation/evaluation/monitoring
```

RAG quality depends on the entire chain. If the answer is bad, the model may
not be the root cause.

## Data Preparation

Data must be suitable for model consumption and retrieval.

Check for:

- duplicates;
- stale documents;
- conflicting versions;
- missing titles, dates, owners, or access labels;
- inconsistent formatting;
- tables or images that need special handling;
- PII or confidential content;
- documents that should not be visible to all users.

Bad data produces bad retrieval. Bad retrieval produces bad model context. Bad
context produces plausible but weak answers.

## Chunking

Chunking divides content into retrievable units.

| Approach | Works well when | Risk |
|---|---|---|
| Fixed-size chunking | Content is regular and simple. | Can split meaning across boundaries. |
| Section-based chunking | Documents have headings and stable structure. | Poor headings or inconsistent formatting can hurt quality. |
| Hierarchical chunking | You need section-level and paragraph-level context. | More complex indexing and retrieval behavior. |
| Semantic chunking | Meaning boundaries matter more than size. | Requires more processing and validation. |

The right chunking strategy depends on the content and query patterns.

## Metadata

Metadata is not decoration. It enables filtering, access control, ranking, and
audit.

Useful metadata can include:

- document type;
- source system;
- owner;
- creation date;
- effective date;
- version;
- jurisdiction;
- confidentiality label;
- user group or entitlement;
- topic or product area.

If retrieval must respect authorization, metadata and access control design are
part of security, not only search quality.

## Embeddings And Vector Stores

An embedding represents content as numbers so semantically similar items can be
searched. A vector store indexes those embeddings for retrieval.

Key decisions:

- which embedding model to use;
- how to chunk before embedding;
- what metadata to attach;
- how and when to refresh the index;
- whether to combine vector search with keyword search;
- how to prevent unauthorized retrieval;
- how to evaluate retrieval quality.

## Retrieval Failure Modes

| Symptom | Possible cause |
|---|---|
| Relevant document is not retrieved. | Bad chunking, bad metadata, weak query, stale index, poor embedding fit. |
| Irrelevant document is retrieved. | Weak ranking, ambiguous query, missing filters, noisy corpus. |
| User sees unauthorized content. | Access control not enforced during retrieval. |
| Answer cites stale content. | Index refresh or document lifecycle problem. |
| Answer is plausible but unsupported. | Retrieved context was insufficient or ignored. |

## Decision Rule

When asked to design RAG, do not jump straight to the vector store. Walk the
chain:

1. What data is trusted?
2. How is it cleaned and segmented?
3. What metadata is required?
4. How are embeddings generated?
5. How is retrieval filtered and ranked?
6. How is retrieved context assembled?
7. How are answers evaluated and monitored?

## Teach-Back

Close the guide and explain:

1. Why chunking is a design decision, not a mechanical step.
2. How metadata supports both quality and security.
3. Why a retrieval failure may look like a model failure.
4. How you would test whether RAG is working.

Then fill the Day 2 RAG worksheet.

