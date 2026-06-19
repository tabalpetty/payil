# Day 6 Study Guide: Optimization, Monitoring, Evaluation, And Troubleshooting

## What You Are Learning Today

Day 6 builds operational judgment. You will learn to reason about cost,
latency, quality, monitoring, evaluation, and troubleshooting.

The core rule is evidence before fixes.

## Optimization Tradeoffs

Optimization usually changes more than one dimension.

| Action | Likely benefit | Possible cost |
|---|---|---|
| Use a smaller model | Lower cost and latency. | Lower quality on hard tasks. |
| Route by task type | Better cost-quality balance. | More routing complexity. |
| Compress prompts | Lower token cost and latency. | Loss of useful context. |
| Prune retrieved context | Less noise and lower cost. | Missing needed evidence. |
| Cache outputs | Lower latency and cost for repeated requests. | Staleness and invalidation risk. |
| Batch processing | Better throughput/cost. | Worse interactivity. |
| Provision throughput | Predictable capacity. | Commitment and utilization risk. |

Always ask: what metric improves, what metric may degrade, and what evidence
will show the difference?

## Monitoring

A GenAI dashboard should cover both system and model behavior.

Signals:

- request volume;
- latency;
- error rate;
- throttling;
- token usage;
- cost;
- model route distribution;
- retrieval hit quality;
- citation coverage;
- hallucination or factuality indicators;
- safety violations;
- tool-call behavior;
- user feedback;
- business outcome.

## Evaluation

Evaluation is how you decide whether the system is good enough.

Evaluation types:

- prompt regression;
- RAG retrieval evaluation;
- human evaluation;
- LLM-as-judge with caution and calibration;
- agent task success evaluation;
- canary tests;
- synthetic users;
- deployment validation.

Each evaluation needs a dataset, metric, threshold, frequency, and owner.

## Troubleshooting

Use a disciplined sequence:

```text
Symptom
  -> impact
  -> first evidence
  -> hypotheses
  -> evidence that rules hypotheses in/out
  -> root cause
  -> immediate fix
  -> prevention
  -> follow-up test
```

Do not jump from symptom to fix.

## Common Diagnostic Splits

| Symptom | Ask |
|---|---|
| Bad answer | Is it prompt, model, retrieval, data, or evaluation? |
| Irrelevant citations | Is it chunking, metadata, query, ranking, or corpus quality? |
| Latency spike | Is it model, network, retrieval, tool, quota, or concurrency? |
| Cost spike | Is it token count, traffic, model route, retries, or context size? |
| Agent loop | Is the stopping condition, tool result, memory, or plan faulty? |

## Teach-Back

Close the guide and explain:

1. Why optimization is a tradeoff, not a single best practice.
2. What belongs on a GenAI operations dashboard.
3. How evaluation differs from monitoring.
4. How to diagnose a bad RAG answer without guessing.

Then fill the Day 6 operations and troubleshooting pack.

