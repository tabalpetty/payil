# Day01-order005: Trust Boundaries, IAM, And Data Protection

## Traceability

| Field | Value |
|---|---|
| Curriculum order | Day01-order005 |
| Section | Layer 0 - GenAI and AWS foundations |
| Topic | IAM, trust boundaries, least privilege, networking, and data-protection fundamentals |
| Knowledge category | Knowledge |
| Knowledge type | Conceptual; Conditional; Normative |
| Artifact family | Policy/risk review; decision table; concept map |

## Purpose

Establish the security boundary model that will be reused in RAG, agents,
governance, and operations.

## Artifact A: Trust Boundary Diagram

Describe the trust boundaries in a GenAI application.

```text
User
  -> application boundary
  -> identity/authorization boundary
  -> data/retrieval boundary
  -> model/tool boundary
  -> logging/audit boundary
```

My trust-boundary notes:

```text

```

## Artifact B: Control Placement

| Concern | Control | Where it belongs | Why |
|---|---|---|---|
| User authentication |  |  |  |
| Least privilege |  |  |  |
| Network isolation |  |  |  |
| Sensitive data exposure |  |  |  |
| Logging privacy |  |  |  |
| Unauthorized retrieval |  |  |  |

## Artifact C: Risk Review

| Risk | Likelihood | Impact | Control | Residual risk |
|---|---|---|---|---|
|  | Low / medium / high | Low / medium / high |  |  |
|  | Low / medium / high | Low / medium / high |  |  |
|  | Low / medium / high | Low / medium / high |  |  |

## Self-Check

| Question | My answer |
|---|---|
| What does least privilege mean for model and data access? |  |
| Why are logs both useful and risky? |  |
| What security control is non-negotiable in my example scenario? |  |
