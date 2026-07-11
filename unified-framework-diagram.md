# Unified Framework: Murai + Capability-Driven Learning

*How the production engine and the learner experience merge at the knowledge type*

---

## System Architecture

```mermaid
flowchart TD
    subgraph MURAI["🟡 MURAI — Production Side"]
        direction TB
        M0["Classifies what to teach<br/>and validates content integrity"]
        A1["Axis 1 · Cognitive Function (9 types)"]
        A2["Axis 2 · Representation & Locus (6 types)"]
        A3["Axis 3 · Subject Domain"]
        A4["Axis 4 · Proficiency Level (5 stages)"]
        MQ["Output · 14 quality gates + traceability chain"]
    end

    subgraph SPEC["🔵 CAPABILITY-DRIVEN SPEC — Learner Side"]
        direction TB
        S0["Structures how the learner<br/>experiences each unit"]
        T1["Tier 1 · Capability — what you can do"]
        T2["Tier 2 · Skill — the tactical how"]
        T3["Tier 3 · Task — deliberate practice"]
        T4["Tier 4 · Concept — the underlying why"]
        VL["Engine · Verification Loop at every capability"]
    end

    MURAI --> MERGE
    SPEC --> MERGE

    subgraph MERGE["🟢 MERGE POINT — Knowledge Type Determines Everything"]
        direction TB
        MP["Murai Axis 1 classifies the knowledge type<br/>→ Spec selects which tier leads<br/>→ Verification Loop proves it"]
    end

    MERGE --> PIPELINE

    subgraph PIPELINE["🟢 UNIFIED PRODUCTION PIPELINE"]
        direction LR
        P1["Source<br/>Objectives"] --> P2["4-Axis<br/>Classification"]
        P2 --> P3["Tier<br/>Selection"]
        P3 --> P4["Four-Tier<br/>Unit"]
        P4 --> P5["Verification<br/>Loop"]
        P5 --> P6["14 + 1<br/>Gates"]
    end

    PIPELINE --> OUTCOMES

    subgraph OUTCOMES["🟢 LEARNER OUTCOMES"]
        direction LR
        O1["Knowledge<br/>─────<br/>Every skill covered,<br/>no gaps"]
        O2["Proficiency<br/>─────<br/>Every capability<br/>demonstrated"]
        O3["Muscle Memory<br/>─────<br/>Procedural skills<br/>drilled in context"]
        O4["Clarity<br/>─────<br/>Deep mental models<br/>from predict-check"]
    end

    style MURAI fill:#F5EDD2,stroke:#D4A94A,stroke-width:2px,color:#1C1C1E
    style SPEC fill:#DAE8F0,stroke:#7BACC8,stroke-width:2px,color:#1C1C1E
    style MERGE fill:#D5EDE2,stroke:#5AAF7C,stroke-width:2px,color:#1C1C1E
    style PIPELINE fill:#D5EDE2,stroke:#5AAF7C,stroke-width:2px,color:#1C1C1E
    style OUTCOMES fill:#D5EDE2,stroke:#5AAF7C,stroke-width:2px,color:#1C1C1E
```

---

## Knowledge Type Mapping (The Merge Table)

This is the central mechanism. Murai classifies what kind of knowledge each topic is, and that classification determines which tier leads the learner experience and which verification pattern proves competence.

| Murai Classifies | Spec Structures | Verification Pattern | Learner Outcome |
|---|---|---|---|
| **Declarative** (facts, rules) | Concept tier primary | Recall check | Knowledge |
| **Procedural** (methods) | Task tier primary | Command check | Muscle memory |
| **Conceptual** (models) | Concept + Skill co-primary | Predict then confirm | Clarity |
| **Conditional** (when/where) | Capability tier primary | Scenario decision | Judgment |
| **Causal** (explain, predict) | Concept tier primary | Intentional failure | Troubleshooting |
| **Strategic** (plan, adapt) | Capability tier primary | Design review | Architecture |
| **Tacit** (judgment) | Task tier, varied contexts | Pattern recognition | Intuition |
| **Embedded** (in tools) | Task tier primary | Tool output check | Proficiency |

> *Murai's Axis 1 (cognitive function) selects which tier leads. The Spec structures the unit. The Loop proves it.*

---

## Quality Gates (14 existing + 1 new)

| # | Gate | Source |
|---|---|---|
| 1 | teaching_substrate | Murai |
| 2 | source_objective | Murai |
| 3 | raw_provenance | Murai |
| 4 | schema | Murai |
| 5 | traceability | Murai |
| 6 | factual_verification | Murai |
| 7 | review_evidence | Murai |
| 8 | coverage | Murai |
| 9 | distribution | Murai |
| 10 | approved_output | Murai |
| 11 | cost | Murai |
| 12 | iteration | Murai |
| 13 | automation_tail | Murai |
| 14 | human_resolution | Murai |
| **15** | **tier_completeness** | **NEW — Unified** |

> *Gate 15: Every topic must produce a complete Four-Tier unit with a Verification Loop matching the dominant knowledge type.*

---

## Legend

- **Ochre / Yellow** — Murai: production and validation
- **Blue** — Capability-Driven Spec: learner structure
- **Green** — Unified: where both systems merge
