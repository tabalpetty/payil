# Day 1 Slides: Foundations, System Map, Invocation, Prompt

## Slide 1: Today's Job

- Build the mental map for GenAI applications on AWS.
- Separate model, prompt, retrieval, orchestration, controls, and evaluation.
- Produce a system map and prompt baseline.

## Slide 2: The Model Is Not The App

```text
User -> app/API -> prompt/context -> model -> validation -> response
                  -> logs/metrics/evaluation/audit
```

- The model generates.
- The application governs, validates, routes, logs, and recovers.

## Slide 3: Key Concepts

- Token
- Context window
- Temperature
- Top-p/top-k
- Prompt template
- Structured output
- Regression example

## Slide 4: AWS Roles

- Model access
- Retrieval/data
- Compute
- Orchestration
- API boundary
- Security
- Observability
- Governance

## Slide 5: Minimal Invocation

- Caller has permission.
- Model or endpoint is selected.
- Input shape matches API/model expectation.
- Parameters are chosen intentionally.
- Response is validated and logged.
- Failures are handled.

## Slide 6: Prompt As Asset

- Owned
- Versioned
- Tested
- Approved
- Monitored
- Rolled back when needed

## Slide 7: Artifact Prompt

Fill:

- system map;
- service role table;
- FM behavior table;
- invocation record;
- prompt regression mini-set.

