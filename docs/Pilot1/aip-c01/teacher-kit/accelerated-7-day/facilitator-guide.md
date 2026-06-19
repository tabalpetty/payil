# AIP-C01 Accelerated 7-Day Facilitator Guide

## Purpose

This guide helps a teacher, coach, or AI tutor run the accelerated path without
letting it collapse into passive reading and quizzes.

Use it with the student artifacts in
`docs/Pilot1/aip-c01/student-kit/accelerated-7-day/`.

For the first pilot, the same person may act as student, teacher, and examiner.
That is acceptable, but the roles must be separated deliberately. The student
attempts. The teacher supports learning. The examiner judges evidence.

## Facilitator Priorities

1. Protect the accelerated route assumptions.
2. Keep each day multi-method: map, build, decide, diagnose, practise, reflect.
3. Ask for evidence, not confidence.
4. Force rejected alternatives in scenario decisions.
5. Treat safety, security, governance, and operations as cross-cutting.
6. Remediate by gap type.
7. Do not declare readiness unless the gates are met.

## Role Separation For A Solo Pilot

Use three passes for each major artifact section.

### Pass 1: Student Mode

The learner fills the section without looking for a perfect answer.

Rules:

- write the first attempt from current understanding;
- mark confidence before checking;
- include assumptions;
- do not ask AI to complete the section;
- do not polish weak understanding into vague professional language.

The product of student mode is an honest attempt.

### Pass 2: Teacher Mode

The teacher reviews the attempt to improve learning.

Teacher questions:

- What is the learner trying to say?
- Which knowledge type is weak?
- Is the gap recall, concept, procedure, condition, cause, diagnosis,
  governance, or metacognition?
- What hint would help without giving away the whole answer?
- What example, diagram, or contrasting case would repair the gap?
- Should the learner retry now or continue and revisit later?

The product of teacher mode is targeted support.

### Pass 3: Examiner Mode

The examiner decides whether the evidence is good enough.

Examiner questions:

- Is the answer specific to the scenario?
- Are the chosen and rejected options both explained?
- Are tradeoffs named?
- Are safety, security, governance, and operations considered where relevant?
- Is there observable evidence, or only confidence?
- Would this reasoning survive a changed constraint?
- Is this good enough to move on, or should remediation happen first?

The product of examiner mode is a pass, revise, or remediate decision.

Do not let teacher sympathy override examiner standards. Also do not let
examiner severity prevent learning. The teacher helps; the examiner verifies.

## Daily Facilitation Pattern

| Stage | Facilitator action |
|---|---|
| Diagnostic warm-up | Ask 3-5 recall or scenario prompts from yesterday's gaps. Require confidence marking. |
| Mental model build | Have the learner draw or reconstruct the model before showing a finished version. |
| Applied work | Let the learner fill the artifact. Intervene with hints only after observing the failure mode. |
| Scenario judgment | Require chosen option, rejected alternatives, assumptions, and changed-constraint response. |
| Failure/governance pass | Ask where the design fails, who owns the control, and what evidence proves it. |
| Timed practice | Keep it timed. Untimed practice does not test exam pacing. |
| Error analysis | Classify misses and assign targeted remediation before moving on. |

## Expanded Daily Runbook

### Before The Day Starts

Check:

- yesterday's artifact;
- yesterday's error log;
- severe unresolved gaps;
- today's daily artifact;
- today's likely high-risk knowledge types.

Write a short daily intention:

```text
Today I must be able to...
The most likely failure mode is...
I will know I am ready to stop today when...
```

### During Mental Model Work

Do not begin by lecturing. Begin by asking the learner to produce the current
model.

Accept rough sketches. Reject empty abstraction.

Good evidence:

- arrows showing data or control flow;
- named services or components;
- trust boundaries;
- decision points;
- failure points;
- owners or evidence where governance matters.

Weak evidence:

- a list of services without relationships;
- a generic paragraph that could apply to any system;
- unexplained arrows;
- missing security or operational boundary.

### During Applied Work

Let the learner struggle productively. Intervene when the struggle becomes
unproductive.

Use hints in this order:

1. Ask what the decision depends on.
2. Ask what the alternatives are.
3. Ask what evidence would distinguish the alternatives.
4. Offer a smaller example.
5. Show a partial pattern.
6. Only then provide a direct explanation.

### During Scenario Judgment

Every major decision should include:

- chosen option;
- rejected alternative;
- why the rejected alternative is plausible;
- condition that would reverse the decision;
- risk introduced by the chosen option.

If an answer does not reject alternatives, it is not yet professional scenario
reasoning.

### During Failure Or Governance Review

Force the design through this checklist:

| Question | Why it matters |
|---|---|
| What can go wrong? | Exposes causal and diagnostic understanding. |
| How would we know? | Forces observability and evidence. |
| Who owns the control? | Tests institutional knowledge. |
| What is logged? | Supports audit and troubleshooting. |
| What is the user told? | Tests product and safety behavior. |
| What remains risky? | Prevents fake certainty. |

### During Timed Practice

Record:

- answer chosen;
- confidence before reveal;
- whether the answer was guessed;
- why the right answer is right;
- why each attractive distractor is wrong;
- what knowledge would have prevented the miss.

For a correct but guessed answer, still create an error-log entry.

## Day-Specific Checks

| Day | Artifact | Must-see evidence |
|---:|---|---|
| 0 | Entry diagnostic | Honest route decision and top three risk areas. |
| 1 | System map, invocation, prompt baseline | Correct service placement, model behavior explanation, minimal prompt regression set. |
| 2 | RAG design worksheet | Defended chunking, metadata, vector-store, and retrieval test design. |
| 3 | Integration decision record | API pattern choice, prompt governance, resilience behavior, rejected alternatives. |
| 4 | Model and agent implementation architecture | Routing policy, deployment choice, tool boundaries, stopping conditions. |
| 5 | Safety, security, governance control pack | Threat model, control placement, owner, evidence, residual risk. |
| 6 | Operations and troubleshooting pack | Monitoring signals, evaluation harness, evidence-first incident diagnosis. |
| 7 | Final architecture and readiness | Integrated ADR, production readiness review, simulated exam gate decision. |

## Day-Specific Facilitation Notes

### Day 0: Entry Diagnostic

Be strict. The diagnostic is not a motivational ritual. It determines whether
the path is suitable.

Watch for:

- broad AWS familiarity but weak GenAI specifics;
- strong model knowledge but weak AWS integration;
- strong conceptual answers but weak operations;
- confidence without evidence.

Decision guidance:

- choose `Enter accelerated path` only when gaps are manageable;
- choose `Enter with warnings` when the path is possible but risky;
- choose `Use self-paced path` when prerequisite gaps would consume the week.

### Day 1: System Map, Invocation, Prompt Baseline

The learner must form the architecture vocabulary of the week.

Do not accept a service list as a system map. The map must show relationships:
client, application, model, retrieval, controls, observability, governance.

Critical misses:

- cannot explain tokens or context windows;
- cannot separate model, prompt, retrieval, orchestration, and app logic;
- cannot identify where permissions and logs appear.

### Day 2: RAG Design

The learner must reason about data, chunking, metadata, embeddings, vector
stores, and retrieval failure.

Push hard on:

- why a chunking strategy fits the content;
- how metadata supports filtering, ranking, security, and audit;
- how stale, unauthorized, or irrelevant retrieval would be detected.

Critical misses:

- treats RAG as "just add documents";
- ignores access control in retrieval;
- cannot diagnose irrelevant retrieval.

### Day 3: Integration Decision Record

The learner must connect retrieval and prompts to application patterns.

Push hard on:

- sync versus async versus streaming;
- prompt versioning and regression;
- retry, timeout, throttling, fallback, and graceful degradation.

Critical misses:

- chooses API pattern without latency/user-experience rationale;
- ignores malformed responses;
- has no rollback for prompt changes.

### Day 4: Model, Deployment, And Agents

The learner must handle implementation choices and agent boundaries.

Push hard on:

- model routing by cost, latency, quality, and risk;
- deployment options and operational implications;
- tool schemas, authorization boundaries, stopping conditions, and human
  escalation.

Critical misses:

- gives tools broad authority;
- has no loop prevention;
- cannot explain when routing or fallback changes.

### Day 5: Safety, Security, Governance

The learner must make governance concrete.

Push hard on:

- preventive, detective, and responsive controls;
- owner, evidence, approval, residual risk;
- prompt injection, data exposure, PII, logging privacy, and human oversight.

Critical misses:

- names controls without owners;
- names policies without evidence;
- treats guardrails as the only safety layer.

### Day 6: Operations And Troubleshooting

The learner must become evidence-first.

Push hard on:

- cost, latency, quality, and compliance tradeoffs;
- dashboard signals;
- evaluation datasets and thresholds;
- root cause before fix.

Critical misses:

- recommends fixes without evidence;
- cannot distinguish retrieval failure from prompt/model failure;
- ignores token/cost instrumentation.

### Day 7: Integration And Readiness

The learner must prove synthesis.

Push hard on:

- end-to-end architecture under changed constraints;
- production readiness;
- timed exam performance;
- quality of error analysis.

Critical misses:

- passes practice but cannot explain misses;
- meets overall score but fails a domain;
- has unresolved severe gaps in safety, security, governance, integration, RAG,
  or troubleshooting.

## Question Stems

Use these repeatedly.

- What would make the opposite choice correct?
- Which assumption is doing the most work here?
- Where would this fail first in production?
- What evidence would prove your diagnosis?
- Which control prevents this, which detects it, and which responds to it?
- Who owns this decision?
- What must be logged for audit or incident reconstruction?
- What would you change if cost, latency, safety, or jurisdiction changed?
- Why is the rejected option tempting?
- What knowledge gap caused this miss?

## Scoring Daily Artifacts

Use this 0-3 rubric for major sections.

| Score | Meaning | Evidence |
|---:|---|---|
| 0 | Missing | Blank, copied, or generic. |
| 1 | Weak | Names relevant ideas but does not apply them to the scenario. |
| 2 | Usable | Makes a defensible choice with some rationale and evidence. |
| 3 | Strong | Includes tradeoffs, rejected alternatives, risks, evidence, and remediation. |

Daily pass standard:

- no critical section is `0`;
- most major sections are `2` or above;
- at least one major decision is `3`;
- severe gaps are remediated or explicitly carried forward;
- the error log is updated.

If the learner scores many `1`s, do not move on casually. Decide whether to
repeat the artifact, add a focused remediation block, or switch to self-paced.

## Remediation Routing

| Observed failure | Likely gap | Facilitator response |
|---|---|---|
| Names services but misplaces them in architecture | Conceptual | Rebuild the system map and ask for data/control flow. |
| Chooses an answer by keyword matching | Conditional | Present a near-identical case where the other option is correct. |
| Recommends fixes before checking evidence | Diagnostic | Stop and require symptom, signal, hypothesis, evidence, fix. |
| Omits owner or evidence for controls | Institutional/governance | Add RACI and audit-evidence fields before accepting the answer. |
| Cannot perform a workflow after explaining it | Procedural | Use worked example, partial completion, then independent variant. |
| Overconfident after repeated misses | Metacognitive | Require confidence calibration and a changed study action. |

## Solo Examiner Checklist

When you are grading your own work, read the artifact as if someone else wrote
it. Ask:

- Could I defend this answer without notes?
- Is this answer specific enough that a reviewer can see the design?
- Did I name evidence, or only intent?
- Did I reject plausible alternatives?
- Did I address the highest-risk failure mode?
- Did I include security/governance/operations where relevant?
- Did I update the error log honestly?

If the answer feels "probably fine" but you cannot point to evidence, mark it
weak and remediate.

## Final Readiness Standard

The learner is `Ready` only if all are true:

- all daily artifacts are complete enough to review;
- severe gaps are remediated or absent;
- simulated exam score is at least `82%`;
- every domain score is at least `72%`;
- timing is within `170` minutes;
- missed and guessed answers have credible explanations;
- the learner can defend an end-to-end architecture under changed constraints.

If these are not true, choose `Remediate` or `Do not schedule`.
