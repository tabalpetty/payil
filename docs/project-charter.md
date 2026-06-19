# Project Charter

## Purpose

Most teaching systems treat every part of a subject as though it were the same
kind of knowledge and teach it through one repeated format. This project aims to
build a reusable alternative: a system that selects teaching methods according
to the type of knowledge being developed while preserving a carefully designed
sequence based on the subject's internal structure.

Pilot1, the AWS Certified Generative AI Developer - Professional (AIP-C01)
implementation, is the first implementation and validation case, not the limit
of the methodology.

The practical aim is to create a Curriculum Architecture Kit that helps a
designer turn any serious body of knowledge into a coherent teaching system:
not just a syllabus, a slide deck, or a bank of questions, but an aligned set of
learning units, teacher supports, learner materials, activities, artifacts,
assessments, remediation routes, and progression rules. The kit should be
usable for technical certification programs, professional training, academic
courses, apprenticeship-style learning, or other domains where learners must
develop usable capability rather than simply encounter information.

The project begins from a simple observation: different kinds of learning fail
in different ways. A learner who cannot remember a term needs a different
intervention from a learner who can recite the term but cannot apply it, choose
between alternatives, diagnose a failure, use a tool, defend a tradeoff, or
recognize a pattern in context. A strong curriculum must therefore make the
intended use of knowledge explicit, teach in forms that match that use, and
collect evidence that the learner can perform, decide, explain, create, or
coordinate as required.

The Pilot1 AIP-C01 reference implementation gives the architecture a demanding
test case. The AWS Certified Generative AI Developer - Professional domain
includes foundation-model integration, data management, compliance,
implementation, application integration, AI safety, security, governance,
operational optimization, testing, validation, and troubleshooting. That
mixture makes it a useful proving ground for a subject-agnostic method because
it requires conceptual understanding, implementation skill, architecture
judgment, diagnosis, and exam readiness rather than one repeated activity
pattern.

## Problem Statement

Conventional curriculum production often starts by converting source material
into modules, lessons, readings, videos, and quizzes. This creates visible
content quickly, but it can hide several design problems:

- topic order may follow the source document rather than prerequisite logic;
- unit boundaries may reflect chapter headings rather than coherent learner
  capabilities;
- teaching methods may be selected by habit, convenience, or format
  consistency rather than by learning need;
- assessment may measure recognition when the real goal is explanation,
  selection, execution, diagnosis, judgment, or transfer;
- remediation may repeat the same content instead of addressing the specific
  gap that blocked mastery;
- source objectives may become disconnected from activities, artifacts,
  rubrics, and progression decisions.

This project addresses those problems by making curriculum architecture
explicit. It treats a course as a designed learning system with traceable
relationships among domain structure, knowledge type, teaching method,
practice, assessment, remediation, and progression.

## Intended Users

The primary users of the Curriculum Architecture Kit are curriculum designers,
instructional designers, teachers, tutors, coaches, and AI-assisted education
builders who need a principled way to design learning experiences across
subjects. They may use the kit to create a new course, improve an existing
one, audit alignment, or build reusable teacher and learner packages.

The Pilot1 AIP-C01 Teacher Kit is intended for a human instructor, coach,
study-group leader, or AI tutor that needs enough structure to conduct the unit
without reconstructing the lesson from scattered assets. The Pilot1 AIP-C01
Student Kit is intended for learners who need a guided path through
explanation, examples, practice, artifact creation, assessment, remediation,
and reassessment.

The Pilot1 AIP-C01 Exam Preparation materials are intended for learners who
have studied the concepts and now need to prove exam readiness under conditions
that resemble the real certification exam. Exam preparation is related to
teaching, but it has a different purpose: it builds speed, stamina,
question-format fluency, distractor resistance, domain coverage awareness, and
confidence under timed conditions.

## What We Are Building

The project has two connected products.

First, it builds a subject-agnostic Curriculum Architecture Kit. This kit
defines the concepts, process, schemas, decision rules, templates, and review
criteria for designing a multi-method teaching system. It should explain how to
move from source objectives and domain analysis to learning units, method
selection, teaching sequences, assessment contracts, remediation design, and
traceability.

Second, it builds Pilot1, an AIP-C01 reference implementation. This
implementation is not a separate course-generation exercise; it is the
laboratory in which the generic architecture is tested. The Pilot1 AIP-C01 work
should expose whether the generic method is clear enough, complete enough, and
practical enough to produce real teacher and learner materials.

The relationship between the two products is reciprocal. The generic kit gives
Pilot1 its structure. Pilot1 gives the generic kit evidence, examples,
pressure tests, and lessons learned.

## Governing Model

The system separates three design questions:

1. **What order should learning follow?**
   The domain model, prerequisites, dependencies, and desired proficiency
   determine the sequence and learning layers.
2. **How should each unit be taught?**
   The unit's dominant and secondary knowledge types determine the teaching
   methods and learning activities.
3. **How is readiness to progress established?**
   Observable mastery evidence, aligned assessment, and remediation determine
   progression.
4. **What pacing tracks are supported?**
   The curriculum states which timelines it supports, what learner assumptions
   each timeline makes, and which mastery gates remain unchanged across tracks.

These questions must remain connected. A unit's position in the sequence
should be justified by dependency logic. Its methods should be justified by
what learners must actually be able to do. Its assessment should elicit the
same kind of performance that the unit claims to teach. Its remediation should
respond to the specific reason a learner fell short.

The governing model can be summarized as:

> Domain structure determines learning order. Knowledge type determines
> teaching method. Mastery evidence determines progression.

## Deliverable Architecture

### Curriculum Architecture Kit

A subject-agnostic methodology for:

- mapping a domain and its boundaries;
- identifying prerequisites and dependencies;
- designing learning layers and progression;
- classifying knowledge using distinct classification axes;
- selecting and blending teaching methods;
- defining proficiency and mastery evidence;
- aligning teaching, artifacts, assessment, and remediation;
- producing teacher and student materials;
- evaluating and improving the teaching system;
- capturing lessons learned from reference implementations.

The kit should be detailed enough that another designer can apply it without
private context from this project. It should include definitions, design rules,
schemas, examples, quality checks, and enough explanation to prevent common
misuses, such as collapsing all knowledge into a single taxonomy or defaulting
to one activity format for every unit.

The kit is a durable project asset. Implementation mistakes, useful
remediation patterns, efficiency gains, and design improvements should be
recorded in `docs/curriculum-architecture-kit/lessons-learned.md` and folded
back into the specification when they become reusable guidance.

### Pilot1 AIP-C01 Teacher Kit

The AIP-C01-specific package used by a teacher, coach, or AI tutor. It includes
lesson plans, explanations, demonstrations, diagrams, worked examples,
questions, scenarios, lab guidance, misconceptions, answer keys, rubrics, and
remediation playbooks.

The Teacher Kit should be executable, not merely referential. A teacher should
be able to open a unit, understand what preparation is required, see the
intended teaching sequence, know what to say or draw or demonstrate, recognize
likely learner responses, administer the assessment, choose remediation, and
record progression evidence.

### Pilot1 AIP-C01 Student Kit

The AIP-C01-specific learner experience. It includes study guides, conceptual
models, diagrams, examples, retrieval practice, labs, investigations, cases,
FAQs, reference material, artifacts, assessments, and remediation activities.

The Student Kit should feel like a complete learning path rather than a folder
of readings. It should help the learner build a mental model, practice in
useful forms, produce artifacts or observable performances, compare their work
against criteria, and repair specific gaps before moving forward.

Pilot1 will support two curriculum-level pacing tracks:

- **Self-paced track:** the default route. Materials, practice, assessment, and
  remediation are available, and learners progress on their own schedule while
  preserving mastery gates.
- **7-day accelerated track:** a compressed route for ambitious learners who
  already have relevant prerequisites, can commit at least six hours of active
  learning per day, and have enough technical maturity to learn from dense
  material, labs, scenarios, and exam-style review without extensive handholding.

The 7-day track must call out its assumptions clearly at the curriculum level.
It may compress practice and increase intensity, but it must not lower the
mastery standard or exam-readiness threshold.

### Pilot1 AIP-C01 Exam Preparation

The AIP-C01-specific exam-readiness layer. It includes an exam-format summary,
question-bank schema, tagged practice questions, timed quizzes, full-length
simulated exams, scoring rules, review workflows, and remediation links back to
the learning units.

Exam preparation must not replace teaching. It should begin from the current
official exam guide, including question formats, timing, domain weightings,
pass/fail reporting, and scoring model. Practice tests should simulate the
actual exam experience closely enough to reveal readiness gaps, while using a
slightly stricter internal readiness threshold than the official passing
standard.

## Scope And Boundaries

The project is intentionally broader than a single certification prep guide,
but narrower than a universal theory of learning.

In scope:

- the reusable architecture for designing teaching systems;
- the classification and method-selection model used by that architecture;
- Pilot1 AIP-C01 curriculum modeling, teacher materials, and student
  materials;
- Pilot1 AIP-C01 exam preparation materials, including tagged question banks
  and timed simulated exams;
- two Pilot1 pacing tracks: self-paced and 7-day accelerated;
- traceability from official source objectives to instruction, artifacts,
  assessment, and remediation;
- pilot-unit validation before broader generation;
- decision records for important architecture, terminology, or process changes.

Out of scope for the current phase:

- generating an entire Pilot1 AIP-C01 course before the pilot pattern is
  proven;
- treating exam familiarity as the only goal of learning;
- using question-bank performance as a substitute for unit mastery evidence;
- replacing all teaching with reading, flashcards, or multiple-choice drills;
- attempting to support every possible learner timeline;
- building a production learning-management platform;
- making AWS-specific assumptions part of the generic methodology unless they
  have been abstracted into subject-agnostic design rules.

## Knowledge Model

Knowledge classification is multidimensional.

### Cognitive Function

- Declarative: facts, terminology, and propositions.
- Conceptual: relationships, models, categories, and frameworks.
- Procedural: methods, techniques, and executable skills.
- Conditional or contextual: when and where an approach is appropriate.
- Causal or mechanistic: why outcomes occur and how systems behave.
- Strategic: planning, problem framing, heuristics, and prioritization.
- Metacognitive: monitoring and regulating one's own understanding.
- Normative or ethical: what ought to be done and how values are balanced.
- Social or relational: who has relevant knowledge, authority, or influence.

### Representation And Locus

- Explicit: articulated and codified.
- Tacit: judgment that is difficult to articulate fully.
- Implicit: automatic, often unconscious patterns and habits.
- Embodied: grounded in perception and physical coordination.
- Embedded: encoded partly in tools, platforms, configurations, and workflows.
- Collective or institutional: distributed across roles, policies, systems, and
  shared organizational practice.

### Separate Overlays

- Subject domain identifies the field to which knowledge belongs.
- Proficiency describes the level of mastery, from awareness through expertise.

Neither should be treated as a cognitive knowledge type.

The knowledge model exists to protect design judgment. It prevents the project
from asking a single label to do too much work. For example, "AI governance" is
a subject-domain label, not by itself a cognitive function. A governance unit
may require declarative knowledge of terms, conceptual knowledge of control
relationships, conditional judgment about when controls apply, institutional
knowledge about ownership and evidence, and normative reasoning about tradeoffs.
Those distinctions should shape the teaching sequence and assessment design.

## Method Library

The system will map knowledge needs to methods including:

- retrieval practice and spaced repetition;
- diagrams, concept maps, comparison, and self-explanation;
- demonstration, guided practice, fading support, and independent performance;
- contrasting cases, decision tables, and defended choices;
- prediction, controlled experiments, failure injection, and diagnosis;
- policy cases, role-play, control mapping, and mock audits;
- expert think-alouds, critique, apprenticeship, and repeated case exposure;
- calibration, evidence-based reflection, and learning-strategy adjustment.

The library is extensible. A unit may use several methods when justified by its
knowledge composition.

Method choice should be explained in plain learning terms. The point is not to
make every unit novel or elaborate. The point is to select the simplest set of
methods that can reliably develop the target capability. A mostly declarative
unit may need concise explanation and retrieval practice. A diagnostic unit may
need prediction, observation, trace interpretation, and failure analysis. A
strategic or conditional unit may need contrasting cases and defended choices.
A tool-embedded unit may need direct interaction with a realistic environment.

## Design Commitments

The project makes the following commitments:

- **Capability before content volume.** A unit is finished when it produces
  usable capability and evidence, not when a planned amount of content has been
  delivered.
- **Alignment before polish.** Attractive materials are valuable only when they
  support the intended learning, practice, evidence, and remediation.
- **Traceability before convenience.** Source objectives must remain connected
  to units, activities, artifacts, assessments, and remediation paths.
- **Pilot before scale.** A complete unit is more valuable than many partial
  outlines because it reveals where the architecture works and where it breaks.
- **Subject-agnostic method, subject-specific fidelity.** The generic kit must
  avoid unnecessary AWS assumptions, while Pilot1 must use accurate, current
  AWS-specific sources.
- **Teaching quality over template completion.** Templates are aids to thought,
  not proof that learning has been designed well.
- **Exam readiness after learning.** Timed exam simulation is necessary for
  certification preparation, but it should verify and sharpen taught capability
  rather than become the curriculum itself.
- **Explicit pacing assumptions.** Pilot1 supports a self-paced route and a
  7-day accelerated route. The accelerated route must state prerequisite,
  maturity, and time-commitment assumptions before the learner begins.
- **Lessons learned into the kit.** Reusable findings from Pilot1, including
  mistakes and remediations, must be captured and used to improve the
  Curriculum Architecture Kit.

## Traceability And Source Use

Traceability is a core product requirement. Each Pilot1 AIP-C01 unit should
preserve a chain from official source objective to curriculum capability,
learning unit, teacher activity, student activity, learner artifact, assessment
criterion, remediation route, and reassessment. Stable unit identifiers support
this chain across curriculum definitions, teacher materials, student materials,
and any generated views.

For AIP-C01 technical claims, official and current AWS sources are the
authoritative reference. Secondary explanations may be useful for orientation,
but they should not become the basis for certification-specific claims unless
they are checked against official sources.

For AIP-C01 exam-preparation claims, the current official AWS exam guide is the
authoritative source for exam code, candidate expectations, question types,
domain weightings, timing, scoring, and pass/fail criteria. Question-bank
items must trace to exam-guide tasks and to the learning unit that teaches the
underlying capability.

Generated spreadsheets, documents, slide decks, or dashboards are views of the
source model. They may help review, delivery, or navigation, but they should
not become the only place where curriculum truth exists.

## Validation Strategy

1. Specify the reusable teaching-system architecture.
2. Choose one bounded Pilot1 AIP-C01 pilot unit with meaningful knowledge
   diversity.
3. Build its curriculum definition, teacher package, and student package.
4. Review the pilot for teaching quality, alignment, usability, and mastery
   evidence.
5. Revise the generic methodology using what the implementation reveals.
6. Scale only after the pilot demonstrates a complete learning experience.

Validation should inspect both educational quality and operational usability.
The pilot should answer questions such as:

- Can a designer understand why the unit exists and why it appears where it
  does in the sequence?
- Are the dominant and secondary knowledge types stated clearly enough to guide
  method choice?
- Does the teacher package contain actual teachable material, not just
  instructions to create it later?
- Does the student package give learners enough guidance, practice, and
  feedback to produce the target evidence?
- Does the assessment measure the intended form of use?
- Do remediation paths address distinct gaps rather than repeating the same
  explanation?
- Does the generic kit need clearer rules, examples, or schemas based on what
  the pilot exposed?

## Expected Evolution

The project should evolve iteratively. Early work should favor clarity,
coherence, and a fully usable pilot over comprehensive coverage. As lessons are
learned, they should be folded back into the Curriculum Architecture Kit and,
when significant, recorded in `docs/decisions/`.

Later expansion may include more Pilot1 AIP-C01 units, additional
subject-domain pilots, generated review views, richer templates, instructor
calibration tools, learner progress records, or automation that checks
traceability. Those should be added after the core architecture has been
demonstrated through complete unit design.

## Success Criteria

The project succeeds when:

- another designer can use the Curriculum Architecture Kit on a different
  subject without relying on hidden project context;
- teaching methods vary for principled reasons rather than novelty alone;
- each Pilot1 AIP-C01 unit contains real learner-facing instruction and
  practice;
- teachers can diagnose and remediate distinct kinds of learning gaps;
- learners can demonstrate transfer, judgment, and performance rather than only
  recall;
- learners can handle exam-style questions under timed conditions with an
  internal readiness standard that is stricter than the official pass
  threshold;
- every AIP-C01 exam objective remains traceable through the system.

The deeper success condition is that the project changes the default design
question from "What content should we cover?" to "What capability must the
learner develop, what kind of knowledge does that require, how should it be
taught, and what evidence will show that it can be used?"
