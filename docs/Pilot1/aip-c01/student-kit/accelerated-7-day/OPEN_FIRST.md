# Open First: AIP-C01 Accelerated 7-Day Path

## What This Is

This is the student entry point for the accelerated AIP-C01 path.

Use this path only if you already have relevant AWS, application architecture,
data, security, operations, or AI/ML experience and can commit at least six
active learning hours per day for seven days.

This path is not easier than the self-paced route. It is denser.

Because this is the first pilot, you may be playing three roles yourself:

- **Student:** learns, attempts, struggles, explains, builds, and records gaps.
- **Teacher:** selects prompts, gives hints, asks follow-up questions, and
  chooses remediation.
- **Examiner:** judges evidence, scores practice, enforces gates, and refuses
  premature readiness.

Do not blend these roles at the same moment. The path works better if you
switch deliberately:

1. As student, attempt the work without looking ahead at ideal answers.
2. As teacher, review the attempt and ask what would improve learning.
3. As examiner, decide whether the evidence meets the standard.

## Start Here

Do these in order.

1. Read this file completely.
2. Open [entry-diagnostic.md](entry-diagnostic.md).
3. Complete the diagnostic before starting Day 1.
4. Decide one of:
   - `Enter accelerated path`
   - `Enter with warnings`
   - `Use self-paced path`
5. If you enter the accelerated path, read the Day 1 study guide:
   [study-guides/day-01-foundations-system-map-invocation-prompt.md](study-guides/day-01-foundations-system-map-invocation-prompt.md).
6. Review the Day 1 presentation:
   [presentations/day-01-slides.md](presentations/day-01-slides.md).
7. Then open
   [day-01-system-map-invocation-prompt.md](day-01-system-map-invocation-prompt.md).
8. After every timed practice set or weak scenario answer, update
   [daily-error-log.md](daily-error-log.md).

## Before You Begin

Create a working copy of each artifact you fill in. The files in this folder
are templates. Keep them clean if you want to reuse them later.

Recommended working folder:

```text
docs/Pilot1/aip-c01/student-kit/accelerated-7-day/my-run/
```

For each day, copy the template into `my-run/` and fill that copy. If you are
working directly in Markdown, one simple naming pattern is:

```text
my-run/my-day-01-system-map-invocation-prompt.md
my-run/my-day-02-rag-design-worksheet.md
...
my-run/daily-error-log.md
```

If you prefer paper or a note-taking app, that is fine. The important thing is
that your work is inspectable at the end of each day.

## How To Use AI During The Pilot

You can use an AI tutor, but be careful about timing.

Good uses:

- ask for an explanation after you have tried to explain the idea yourself;
- ask for a scenario after you have read the day's goal;
- ask for critique after you have completed an artifact section;
- ask for a near-miss scenario to test conditional knowledge;
- ask for remediation matched to a gap type.

Bad uses:

- asking AI to fill the artifact before you attempt it;
- accepting a fluent explanation as proof that you understand it;
- skipping the error log because AI explained the answer;
- letting AI declare you ready without checking the gates.

Recommended prompt after completing a section:

```text
Act as my AIP-C01 examiner. Review this answer for correctness, missing
constraints, weak assumptions, and exam-relevant gaps. Classify each gap by
knowledge type: recall, conceptual, procedural, conditional, causal,
diagnostic, governance, or metacognitive. Do not rewrite the answer for me
until after you critique it.
```

## What You Must Produce

By the end of the week, you should have:

- completed the entry diagnostic;
- completed Day 1 through Day 7 artifacts;
- maintained the daily error log;
- remediated severe gaps;
- completed a simulated exam or staged equivalent;
- made a final `Ready`, `Remediate`, or `Do not schedule` decision.

Your artifacts do not need to be beautiful. They do need to be specific. A
vague answer such as "use monitoring" or "apply security controls" is not
enough. Name the signal, control, owner, evidence, failure mode, or tradeoff.

## Daily Routine

Each day follows the same rhythm:

| Stage | What you do |
|---|---|
| Study guide | Read the day's guide, then close it and reconstruct the key model. |
| Presentation | Review the slide outline and explain it aloud. |
| Diagnostic warm-up | Recall yesterday's weak areas and mark confidence. |
| Mental model | Draw, explain, or reconstruct the day's core model. |
| Applied work | Fill the day's artifact with scenario-specific decisions. |
| Scenario judgment | Choose an option, reject alternatives, and defend the choice. |
| Failure or governance pass | Add safety, security, governance, operations, or diagnostic depth. |
| Timed practice | Answer tagged exam-style questions under time pressure. |
| Error analysis | Classify misses and assign remediation. |

## Detailed Daily Operating Instructions

### 1. Diagnostic Warm-Up

Spend 15-20 minutes before the main work.

Do this closed-book:

- recall the three most important ideas from yesterday;
- explain one thing you got wrong yesterday;
- answer 3-5 short prompts from the prior day's weak areas;
- mark confidence before checking yourself: low, medium, or high.

Why this matters:

If confidence is high and accuracy is low, the issue is not only content. It is
metacognitive calibration. Record that in the error log.

### 2. Mental Model

Before reading too much or asking AI for a polished explanation, draw or write
your current model. It can be rough.

Examples:

- Day 1: draw the GenAI system map.
- Day 2: draw the RAG data and retrieval flow.
- Day 3: draw the API path and failure handling.
- Day 4: draw the model routing and agent/tool boundary.
- Day 5: draw the control layers.
- Day 6: draw the monitoring and troubleshooting loop.
- Day 7: draw the final architecture.

Then compare your model against sources, notes, or AI critique. The mismatch is
where learning happens.

### 3. Applied Work

Fill the day's artifact with a concrete scenario in mind. If no scenario is
provided, choose one and keep it consistent.

Good scenario examples:

- HR policy assistant over internal documents;
- customer support assistant using a knowledge base;
- developer assistant that can call read-only tools;
- compliance document summarizer;
- incident triage assistant using logs and runbooks.

Avoid answering only in abstractions. The artifact should show decisions for a
realistic case.

### 4. Scenario Judgment

For at least one major decision each day, include:

- chosen option;
- rejected alternatives;
- why the rejected alternatives are tempting;
- what assumption would make a rejected option correct;
- what would change under cost, latency, safety, jurisdiction, or quality
  pressure.

This is where accelerated learning becomes professional-level exam readiness.

### 5. Failure Or Governance Pass

After your first design answer, ask:

- where can this fail?
- who owns the control?
- what evidence proves the control worked?
- what is logged?
- what is the user-visible behavior?
- what residual risk remains?

Add these directly to the artifact. Do not leave them as mental notes.

### 6. Timed Practice

Use tagged questions if available. If the question bank is not ready, create or
ask for a small scenario set for the day's topic.

Minimum daily practice:

| Day | Minimum practice |
|---:|---|
| 1 | 10-15 questions or scenarios |
| 2 | 15-20 questions or scenarios |
| 3 | 15-20 questions or scenarios |
| 4 | 20 questions or scenarios |
| 5 | 20 questions or scenarios |
| 6 | 20-25 questions or scenarios |
| 7 | Full simulated exam or staged equivalent |

Always record guessed answers. A correct guess is still a gap until you can
explain why the right answer is right and why the distractors are wrong.

### 7. Error Analysis

For every miss or weak answer, classify the gap:

- **Recall:** I forgot a term, service, feature, or fact.
- **Conceptual:** I could not explain how the pieces relate.
- **Procedural:** I knew the idea but not how to do or specify it.
- **Conditional:** I chose the wrong option for the situation.
- **Causal:** I did not understand why the outcome happened.
- **Diagnostic:** I jumped to a fix without evidence.
- **Governance:** I omitted owner, control, evidence, approval, or residual
  risk.
- **Metacognitive:** I was overconfident, underconfident, or studied the wrong
  thing.

Then choose a remediation. Do not write "review topic" unless you specify what
kind of review and how you will prove repair.

## Completion Rules

A day is not complete just because you read the material.

A day counts only when:

- the daily artifact is filled in;
- at least one choice includes rejected alternatives;
- safety, security, governance, or operations implications are addressed;
- timed practice is completed;
- misses are recorded in the error log;
- severe gaps have remediation actions.

## How To Judge Your Own Artifact

Use this quick rubric at the end of each day.

| Score | Meaning | Standard |
|---:|---|---|
| 0 | Missing | The section is blank or mostly generic. |
| 1 | Weak | The answer names ideas but lacks scenario-specific reasoning. |
| 2 | Usable | The answer makes a reasonable choice and gives some rationale. |
| 3 | Strong | The answer includes tradeoffs, rejected alternatives, risks, evidence, and remediation. |

For the day to pass:

- no critical section should be `0`;
- most sections should be `2` or higher;
- at least one major decision should be `3`;
- severe security, governance, retrieval, integration, or diagnostic gaps must
  be remediated or carried forward explicitly.

## Go/No-Go Standard

At the end of Day 7, choose honestly:

| Decision | Meaning |
|---|---|
| `Ready` | You met score, domain, timing, artifact, and error-analysis gates. |
| `Remediate` | You have localized gaps that need targeted repair before the exam. |
| `Do not schedule` | You have major gaps in core domains or scenario reasoning. |

Do not use elapsed time as proof of readiness. Seven days completed is not the
same thing as exam readiness.

## What To Do If You Fall Behind

Do not silently compress the remaining days.

Use this rule:

- If you miss minor declarative material, carry it into retrieval practice.
- If you miss a daily artifact, pause the calendar and finish it.
- If you have severe gaps in RAG, integration, safety/security/governance, or
  troubleshooting, do not proceed as though the gap is harmless.
- If you cannot complete Day 1 or Day 2 artifacts with usable quality, switch
  to the self-paced path.

The pilot is allowed to reveal that the 7-day path is too dense. That is useful
data, not failure.

## Pilot Notes

Because this is the first run, keep a separate note called `pilot-notes.md`.
Record:

- where instructions were unclear;
- where you needed examples but did not have them;
- where the workload was unrealistic;
- where the artifact helped you think;
- where the artifact felt like paperwork;
- where the teacher/examiner role needed more guidance;
- what should be changed before another learner tries this.

## First Action

Open and complete:

[entry-diagnostic.md](entry-diagnostic.md)
