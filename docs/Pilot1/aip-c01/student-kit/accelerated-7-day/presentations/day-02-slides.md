# Day 2 Slides: Data, Embeddings, Vector Stores, RAG

## Slide 1: Today's Job

- Design a basic RAG system.
- Explain how data quality, chunking, metadata, embeddings, and retrieval shape answer quality.

## Slide 2: RAG Flow

```text
documents -> clean -> chunk -> metadata -> embed -> index
query -> retrieve/filter/rank -> context -> model -> answer
```

## Slide 3: Data Quality

- Duplicates
- Staleness
- Missing metadata
- Conflicts
- PII
- Unauthorized content

## Slide 4: Chunking Decisions

- Fixed-size
- Section-based
- Hierarchical
- Semantic

Question: what does the user need retrieved as one meaningful unit?

## Slide 5: Metadata Is Control

- Filtering
- Ranking
- Security
- Freshness
- Audit
- Ownership

## Slide 6: Failure Modes

- Relevant content missing
- Irrelevant content retrieved
- Unauthorized content retrieved
- Stale content used
- Unsupported answer generated

## Slide 7: Artifact Prompt

Fill:

- data-quality checks;
- chunking decision;
- metadata schema;
- vector-store design;
- retrieval test cases;
- failure diagnosis.

