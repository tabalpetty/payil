# Day01-order008: Basic Amazon Bedrock Model Invocation

## Traceability

| Field | Value |
|---|---|
| Curriculum order | Day01-order008 |
| Section | Layer 0 - GenAI and AWS foundations |
| Topic | Basic Amazon Bedrock model invocation |
| Knowledge category | Skill; Representation / Location |
| Knowledge type | Procedural; Embedded |
| Artifact family | Lab worksheet or runbook; console/API configuration record or inspection worksheet |

## Purpose

Create evidence that you understand the basic shape of a Bedrock model
invocation, even if you are inspecting a faithful example rather than running
live AWS calls.

## Reference Invocation Examples

Use these examples as the concrete artifact to inspect. Do not treat the model
ID as a promise that the same model is available in every account or region;
verify current model availability when running a live call.

### Converse-Style Request

```json
{
  "modelId": "us.anthropic.claude-3-5-sonnet-20240620-v1:0",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "text": "Summarize the incident ticket in three bullet points."
        }
      ]
    }
  ],
  "inferenceConfig": {
    "maxTokens": 300,
    "temperature": 0.2,
    "topP": 0.9
  }
}
```

### InvokeModel-Style Body

```json
{
  "anthropic_version": "bedrock-2023-05-31",
  "max_tokens": 300,
  "temperature": 0.2,
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Return JSON with keys: summary, risk, next_action."
        }
      ]
    }
  ]
}
```

### What To Inspect

| Element | Evidence to record |
|---|---|
| Model identifier | Which model, inference profile, provisioned throughput, or endpoint is being addressed. |
| Caller permission | Which execution role or identity can invoke the model. |
| Request body | Whether the JSON shape matches the selected API/model. |
| Parameters | Why `maxTokens`, `temperature`, and `topP` fit the task. |
| Response handling | How the application extracts, validates, and stores the answer. |
| Error handling | What the application does for access denied, validation, throttling, timeout, and malformed output. |

Official AWS source check:

- `InvokeModel`: <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModel.html>
- `Converse`: <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html>

## Artifact A: Invocation Runbook

| Step | Action | Notes/evidence |
|---:|---|---|
| 1 | Choose model or endpoint. |  |
| 2 | Confirm caller permissions. |  |
| 3 | Prepare request body. |  |
| 4 | Set inference parameters. |  |
| 5 | Invoke model/API. |  |
| 6 | Parse response. |  |
| 7 | Validate output shape. |  |
| 8 | Record logs/metrics/errors. |  |

## Artifact B: Configuration / Inspection Record

| Field | Value |
|---|---|
| Model/provider |  |
| Invocation API or method |  |
| Input shape |  |
| Output shape |  |
| Permissions required |  |
| Region/account assumption |  |
| Logging evidence |  |
| Error or failure mode |  |

## Artifact C: Failure Handling

| Failure | How detected | Response |
|---|---|---|
| Permission denied |  |  |
| Invalid request shape |  |  |
| Throttling |  |  |
| Timeout |  |  |
| Malformed output |  |  |

## Self-Check

| Question | My answer |
|---|---|
| What must exist before invocation can succeed? |  |
| What is embedded platform knowledge here? |  |
| Which error would I know how to investigate first? |  |
