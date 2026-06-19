# Question Bank Specification

## Purpose

The Pilot1 question bank supports AIP-C01 exam readiness. It stores reviewed
practice items that are traceable to the official exam guide and to curriculum
units.

Raw LLM output, crawled questions, or manually drafted prompts are not approved
question-bank content until reviewed.

## Required Item Fields

| Field | Requirement |
|---|---|
| `item_id` | Stable identifier, such as `P1-AIP-D1-T15-001`. |
| `status` | `draft`, `reviewed`, `approved`, `retired`, or `needs-source-check`. |
| `official_exam_code` | `AIP-C01`. |
| `exam_domain` | Official domain number and name. |
| `exam_task` | Official task statement. |
| `exam_skill` | Official skill statement when applicable. |
| `learning_unit` | Curriculum unit ID when units exist. |
| `accelerated_day` | Day 1 through Day 7 in the accelerated path. |
| `knowledge_type` | Dominant knowledge type tested. |
| `question_format` | `multiple-choice` or `multiple-response`. |
| `difficulty` | `easy`, `medium`, `hard`, or `exam-plus`. |
| `cognitive_demand` | Recall, explain, implement, integrate, configure, select, diagnose, optimize, compare, or judge. |
| `stem` | Question prompt or scenario. |
| `options` | Answer options. |
| `correct_answer` | Correct option or options. |
| `rationale_correct` | Why the correct answer is correct. |
| `rationale_distractors` | Why each distractor is wrong or less appropriate. |
| `misconception_tags` | Misconception, trap, or tradeoff tested. |
| `source_trace` | Official AWS source or trusted project source supporting the claim. |
| `remediation_target` | Unit, section, lab, or remediation route. |
| `estimated_time_seconds` | Expected time for a prepared learner. |
| `last_reviewed` | Date the item was last checked. |

## Simulated Exam Rules

Full simulated exams should:

- use 75 questions;
- use a 180-minute timer;
- approximate official domain weighting;
- use only multiple-choice and multiple-response questions;
- include no copied official AWS practice questions, proprietary exam dumps, or
  third-party copyrighted question-bank content;
- produce a domain, task, confidence, and remediation report.

## Review Checklist

Before approval, confirm:

- the item maps to AIP-C01, not another AWS exam;
- the item is professional-level and scenario-based when appropriate;
- the correct answer is unambiguously best;
- distractors are plausible but defensibly wrong;
- the explanation teaches the relevant distinction;
- technical claims can be checked against official AWS sources;
- remediation points to a specific learning resource.
