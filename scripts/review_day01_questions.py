#!/usr/bin/env python3
"""Normalize and review raw Day 1 question candidates.

This script promotes raw candidates into a reviewed markdown bank only when
they pass conservative structural and quality checks. It also records culled
items so reviewers can see why raw output was not approved.
"""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "docs/Pilot1/aip-c01/exam-prep/raw/day-01"
OUT = ROOT / "docs/Pilot1/aip-c01/exam-prep/reviewed/day-01/day-01-reviewed-question-bank.md"

STUDY_GUIDE = "docs/Pilot1/aip-c01/student-kit/accelerated-7-day/study-guides/day-01-foundations-system-map-invocation-prompt.md"
EXAM_OBJECTIVES = "docs/Pilot1/aip-c01/source-material/ai-professional-01.objectives.json"
MAP = "docs/Pilot1/aip-c01/curriculum-model/aip-c01-topic-knowledge-category-map.md"
ANSWER_GUIDANCE = "docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day-01-answer-guidance.md"


TOPICS: dict[str, dict[str, Any]] = {
    "Day01-order001": {
        "topic": "Foundation models and GenAI fundamentals",
        "domain": "Domain 1: Foundation Model Integration, Data Management, and Compliance",
        "task": "Task 1.1: Analyze requirements and design GenAI solutions.",
        "skill": "Skill 1.1.1: Create comprehensive architectural designs that align with specific business needs and technical constraints (for example, by using appropriate FMs, integration patterns, deployment strategies).",
        "local_skill": "Distinguish model behavior from application responsibilities",
        "types": "Declarative; Conceptual",
        "remediation": "docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order001-foundation-models-genai-fundamentals.md",
        "sources": [
            f"Official AIP-C01 objectives JSON: `{EXAM_OBJECTIVES}`",
            f"`{STUDY_GUIDE}`",
            f"`{MAP}`",
        ],
    },
    "Day01-order002": {
        "topic": "Tokens, context windows, inference, temperature, top-k, and top-p",
        "domain": "Domain 1: Foundation Model Integration, Data Management, and Compliance",
        "task": "Task 1.6: Implement prompt engineering strategies and governance for FM interactions.",
        "skill": "Skill 1.6.5: Enhance FM performance to refine prompts iteratively and improve response quality beyond basic prompting techniques (for example, by using structured input components, output format specifications, chain-of-thought instruction patterns, feedback loops).",
        "local_skill": "Predict effects of token and inference-parameter choices",
        "types": "Declarative; Conceptual; Causal",
        "remediation": "docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order002-tokens-context-inference-parameters.md",
        "sources": [
            f"Official AIP-C01 objectives JSON: `{EXAM_OBJECTIVES}`",
            f"`{STUDY_GUIDE}`",
        ],
    },
    "Day01-order003": {
        "topic": "AWS GenAI service landscape",
        "domain": "Domain 1: Foundation Model Integration, Data Management, and Compliance",
        "task": "Task 1.1: Analyze requirements and design GenAI solutions.",
        "skill": "Skill 1.1.1: Create comprehensive architectural designs that align with specific business needs and technical constraints (for example, by using appropriate FMs, integration patterns, deployment strategies).",
        "local_skill": "Classify AWS services by role in a GenAI application",
        "types": "Declarative; Conceptual; Embedded",
        "remediation": "docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order003-aws-genai-service-landscape.md",
        "sources": [
            f"Official AIP-C01 objectives JSON: `{EXAM_OBJECTIVES}`",
            "AWS Bedrock User Guide: <https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html>",
            "AWS Lambda Developer Guide: <https://docs.aws.amazon.com/lambda/latest/dg/welcome.html>",
            "Amazon CloudWatch User Guide: <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html>",
            f"`{STUDY_GUIDE}`",
        ],
    },
    "Day01-order004": {
        "topic": "API, event-driven, serverless, container, and workflow fundamentals",
        "domain": "Domain 2: Implementation and Integration",
        "task": "Task 2.5: Implement application integration patterns and development tools.",
        "skill": "Skill 2.5.1: Create FM API interfaces to address the specific requirements of GenAI workloads (for example, by using API Gateway to handle streaming responses, token limit management, retry strategies to handle model timeouts).",
        "local_skill": "Select synchronous, asynchronous, event-driven, or workflow patterns",
        "types": "Conceptual; Conditional",
        "remediation": "docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order004-application-integration-patterns.md",
        "sources": [
            f"Official AIP-C01 objectives JSON: `{EXAM_OBJECTIVES}`",
            "AWS Step Functions Developer Guide: <https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html>",
            "Amazon SQS Developer Guide: <https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html>",
            f"`{STUDY_GUIDE}`",
        ],
    },
    "Day01-order005": {
        "topic": "IAM, trust boundaries, least privilege, networking, and data protection",
        "domain": "Domain 3: AI Safety, Security, and Governance",
        "task": "Task 3.2: Implement data security and privacy controls.",
        "skill": "Skill 3.2.1: Develop protected AI environments to ensure comprehensive security for FM deployments (for example, by using VPC endpoints to isolate networks, IAM policies to enforce secure data access patterns, AWS Lake Formation to provide granular data access, CloudWatch to monitor data access).",
        "local_skill": "Place IAM, data-protection, logging, and retrieval controls",
        "types": "Conceptual; Conditional; Normative",
        "remediation": "docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order005-trust-boundaries-iam-data-protection.md",
        "sources": [
            f"Official AIP-C01 objectives JSON: `{EXAM_OBJECTIVES}`",
            "AWS IAM User Guide: <https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html>",
            "AWS Bedrock Guardrails documentation: <https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html>",
            f"`{STUDY_GUIDE}`",
        ],
    },
    "Day01-order006": {
        "topic": "GenAI requirements analysis and basic solution architecture",
        "domain": "Domain 1: Foundation Model Integration, Data Management, and Compliance",
        "task": "Task 1.1: Analyze requirements and design GenAI solutions.",
        "skill": "Skill 1.1.1: Create comprehensive architectural designs that align with specific business needs and technical constraints (for example, by using appropriate FMs, integration patterns, deployment strategies).",
        "local_skill": "Convert requirements into a basic GenAI architecture",
        "types": "Conceptual; Conditional; Strategic",
        "remediation": "docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order006-requirements-basic-solution-architecture.md",
        "sources": [
            f"Official AIP-C01 objectives JSON: `{EXAM_OBJECTIVES}`",
            "AWS Well-Architected Framework: <https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html>",
            f"`{STUDY_GUIDE}`",
        ],
    },
    "Day01-order007": {
        "topic": "Foundation-model capabilities, limitations, and basic model selection",
        "domain": "Domain 1: Foundation Model Integration, Data Management, and Compliance",
        "task": "Task 1.2: Select and configure FMs.",
        "skill": "Skill 1.2.1: Assess and choose FMs to ensure optimal alignment with specific business use cases and technical requirements (for example, by using performance benchmarks, capability analysis, limitation evaluation).",
        "local_skill": "Select a model based on task, quality, latency, cost, context, and safety",
        "types": "Declarative; Conditional; Strategic",
        "remediation": "docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order007-model-capabilities-limitations-selection.md",
        "sources": [
            f"Official AIP-C01 objectives JSON: `{EXAM_OBJECTIVES}`",
            "Amazon Bedrock model evaluation docs: <https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html>",
            f"`{STUDY_GUIDE}`",
        ],
    },
    "Day01-order008": {
        "topic": "Basic Amazon Bedrock model invocation",
        "domain": "Domain 2: Implementation and Integration",
        "task": "Task 2.4: Implement FM API integrations.",
        "skill": "Skill 2.4.1: Create flexible model interaction systems (for example, by using Amazon Bedrock APIs to manage synchronous requests from various compute environments, language-specific AWS SDKs and Amazon SQS for asynchronous processing, API Gateway to provide custom API clients with request validation).",
        "local_skill": "Inspect basic Amazon Bedrock invocation requirements",
        "types": "Procedural; Embedded",
        "remediation": "docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order008-basic-bedrock-model-invocation.md",
        "sources": [
            f"Official AIP-C01 objectives JSON: `{EXAM_OBJECTIVES}`",
            "AWS Bedrock `InvokeModel` API Reference: <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModel.html>",
            "AWS Bedrock `Converse` API Reference: <https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html>",
        ],
    },
    "Day01-order009": {
        "topic": "Prompt fundamentals, instructions, templates, and structured outputs",
        "domain": "Domain 1: Foundation Model Integration, Data Management, and Compliance",
        "task": "Task 1.6: Implement prompt engineering strategies and governance for FM interactions.",
        "skill": "Skill 1.6.1: Create effective model instruction frameworks to control FM behavior and outputs (for example, by using Amazon Bedrock Prompt Management to enforce role definitions, Amazon Bedrock Guardrails to enforce responsible AI guidelines, template configurations to format responses).",
        "local_skill": "Design a prompt baseline with boundaries and structured output",
        "types": "Conceptual; Procedural; Causal",
        "remediation": "docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order009-prompt-fundamentals-structured-output.md",
        "sources": [
            f"Official AIP-C01 objectives JSON: `{EXAM_OBJECTIVES}`",
            "Amazon Bedrock Prompt Management User Guide: <https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html>",
            f"`{STUDY_GUIDE}`",
        ],
    },
    "Day01-order010": {
        "topic": "Basic GenAI evaluation concepts and golden datasets",
        "domain": "Domain 5: Testing, Validation, and Troubleshooting",
        "task": "Task 5.1: Implement evaluation systems for GenAI.",
        "skill": "Skill 5.1.1: Develop comprehensive assessment frameworks to evaluate the quality and effectiveness of FM outputs beyond traditional ML evaluation approaches (for example, by using metrics for relevance, factual accuracy, consistency, and fluency).",
        "local_skill": "Build a golden dataset that tests expected behavior and failure modes",
        "types": "Conceptual; Procedural",
        "remediation": "docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order010-basic-evaluation-golden-datasets.md",
        "sources": [
            f"Official AIP-C01 objectives JSON: `{EXAM_OBJECTIVES}`",
            "Amazon Bedrock Model Evaluation User Guide: <https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html>",
            f"`{STUDY_GUIDE}`",
        ],
    },
}

WEAK_STEM_PATTERNS = [
    "which of the following best describes",
    "what is a key benefit",
    "what does increasing the temperature",
    "what is a token",
    "where in an aws solution",
    "which aws service should they use directly",
    "which aws services provide managed apis",
]

OUTDATED_OR_UNVERIFIED_PATTERNS = [
    "as of early 2024",
    "no current support",
    "does not currently",
    "bedrock currently does not",
    "bedrock does not yet",
    "sagemaker jumpstart",
    "bedrock + glue",
]

PROMPT_ADJUSTMENTS = {
    "not scenario-based": "Require a concrete actor, workload, goal, constraint, and tradeoff in the stem.",
    "recall-only item": "Ask the learner to select, diagnose, configure, judge, or choose a first action instead of defining a term.",
    "keyword-trivia stem": "Ban glossary-style stem openers and require distractors that fail because of a constraint.",
    "outdated or unverified technical claim": "Avoid time-bound service-capability claims unless the exact official AWS source is named.",
    "duplicate-pattern": "Show prior approved stems to the generator and require a different scenario, constraint, and tested misconception.",
}

STOP_WORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "because",
    "best",
    "by",
    "for",
    "from",
    "in",
    "is",
    "it",
    "of",
    "on",
    "or",
    "should",
    "that",
    "the",
    "their",
    "to",
    "what",
    "which",
    "with",
    "you",
    "your",
}


@dataclass
class Candidate:
    raw: dict[str, Any]
    source_file: str
    raw_index: int


@dataclass
class CullRecord:
    candidate: Candidate
    reasons: list[str]
    evidence: list[str]


@dataclass
class ApprovedStem:
    stem: str
    source_file: str
    raw_index: int
    key: str
    terms: set[str]


def strip_line_comments(text: str) -> str:
    out: list[str] = []
    in_str = False
    escaped = False
    i = 0
    while i < len(text):
        ch = text[i]
        if ch == '"' and not escaped:
            in_str = not in_str
        if not in_str and ch == "/" and i + 1 < len(text) and text[i + 1] == "/":
            while i < len(text) and text[i] != "\n":
                i += 1
            continue
        out.append(ch)
        escaped = ch == "\\" and not escaped
        if ch != "\\":
            escaped = False
        i += 1
    return "".join(out)


def output_text(path: Path) -> str:
    text = path.read_text(encoding="utf-8", errors="replace")
    match = re.search(r"## Raw Response JSON\n\n```json\n(?P<body>.*)\n```\s*$", text, re.S)
    if match:
        response = json.loads(match.group("body"))
        chunks = [
            content["text"]
            for item in response.get("output", [])
            for content in item.get("content", [])
            if content.get("type") == "output_text"
        ]
        if chunks:
            return "\n\n".join(chunks)

    match = re.search(r"## Raw Response Text\n\n(?P<body>.*?)(?:\n## Raw Response JSON\n|\Z)", text, re.S)
    return match.group("body") if match else text


def raw_metadata(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8", errors="replace")
    match = re.search(r"## Metadata\n\n```json\n(?P<body>.*?)\n```", text, re.S)
    if not match:
        return {}
    try:
        metadata = json.loads(match.group("body"))
    except json.JSONDecodeError:
        return {}
    return metadata if isinstance(metadata, dict) else {}


def repair_known_json_breaks(text: str) -> str:
    return text.replace('text and "foundational\' AI models', "text and foundational AI models")


def parse_jsonish(text: str) -> Any | None:
    cleaned = strip_line_comments(repair_known_json_breaks(text.strip()))
    for candidate in (
        cleaned,
        cleaned[cleaned.find("[") : cleaned.rfind("]") + 1] if "[" in cleaned and "]" in cleaned else "",
        cleaned[cleaned.find("{") : cleaned.rfind("}") + 1] if "{" in cleaned and "}" in cleaned else "",
    ):
        if not candidate:
            continue
        try:
            return json.loads(candidate)
        except json.JSONDecodeError:
            continue
    return None


def parse_raw_file(path: Path) -> list[dict[str, Any]]:
    text = output_text(path)
    items: list[dict[str, Any]] = []

    whole = parse_jsonish(text)
    if isinstance(whole, list):
        items.extend(x for x in whole if isinstance(x, dict))
    elif isinstance(whole, dict) and isinstance(whole.get("questions"), list):
        items.extend(x for x in whole["questions"] if isinstance(x, dict))

    if items:
        return items

    for block in re.findall(r"```(?:json)?\s*(.*?)```", text, re.S):
        parsed = parse_jsonish(block)
        if isinstance(parsed, list):
            items.extend(x for x in parsed if isinstance(x, dict))
        elif isinstance(parsed, dict) and isinstance(parsed.get("questions"), list):
            items.extend(x for x in parsed["questions"] if isinstance(x, dict))
    return items


def load_candidates() -> list[Candidate]:
    candidates: list[Candidate] = []
    for path in sorted(RAW_DIR.glob("*day01-*.md")):
        if "dry-run" in path.name:
            continue
        for idx, item in enumerate(parse_raw_file(path), 1):
            candidates.append(Candidate(item, path.name, idx))
    return candidates


def source_file_provenance() -> dict[str, dict[str, str]]:
    provenance: dict[str, dict[str, str]] = {}
    for path in sorted(RAW_DIR.glob("*day01-*.md")):
        if "dry-run" in path.name:
            continue
        metadata = raw_metadata(path)
        provenance[path.name] = {
            "provider": str(metadata.get("provider", "unknown")),
            "model": str(metadata.get("model", "unknown")),
            "run_id": str(metadata.get("run_id", "unknown")),
        }
    return provenance


def normalize_list(value: Any) -> list[str]:
    if isinstance(value, list):
        return [str(x) for x in value]
    if value is None:
        return []
    return [str(value)]


def is_scenario_based(stem: str) -> bool:
    lowered = stem.lower()
    signals = [
        "a team",
        "a company",
        "an enterprise",
        "a developer",
        "a customer",
        "your team",
        "you are",
        "you need",
        "you want",
        "your application",
        "your bedrock",
        "your genai",
        "an app",
        "an organization",
        "a regulated",
        "a genai",
        "an llm",
        "after ",
        "when ",
    ]
    return any(signal in lowered for signal in signals)


def normalized_stem_key(stem: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9]+", " ", stem.lower())).strip()


def stem_terms(stem: str) -> set[str]:
    return {
        token
        for token in re.findall(r"[a-z0-9]+", stem.lower())
        if len(token) > 2 and token not in STOP_WORDS
    }


def duplicate_match(stem: str, approved_stems: list[ApprovedStem]) -> tuple[str, ApprovedStem, float] | None:
    stem_key = normalized_stem_key(stem)
    terms = stem_terms(stem)
    for approved in approved_stems:
        if stem_key and stem_key == approved.key:
            return ("exact", approved, 1.0)

    if len(terms) < 8:
        return None
    for approved in approved_stems:
        overlap = len(terms & approved.terms)
        union = len(terms | approved.terms)
        if union and overlap / union >= 0.72:
            return ("near", approved, overlap / union)
    return None


def table_cell(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", "<br>")


def truncate(value: str, limit: int) -> str:
    compact = " ".join(value.split())
    if len(compact) > limit:
        return compact[: limit - 3] + "..."
    return compact


def review(candidate: Candidate) -> tuple[bool, list[str], list[str]]:
    item = candidate.raw
    reasons: list[str] = []
    evidence: list[str] = []
    order = item.get("curriculum_order")
    stem = str(item.get("stem", "")).strip()
    lowered = stem.lower()

    def reject(reason: str, detail: str) -> None:
        reasons.append(reason)
        evidence.append(f"{reason}: {detail}")

    if order not in TOPICS:
        reject("unknown curriculum_order", f"raw curriculum_order={order!r}")
    if not stem:
        reject("missing stem", "stem field is empty or absent")
    if item.get("question_format") not in {"multiple-choice", "multiple-response"}:
        if item.get("question_type") in {"multiple-choice", "multiple-response"}:
            item["question_format"] = item["question_type"]
        else:
            reject(
                "missing or invalid question_format",
                f"question_format={item.get('question_format')!r}; question_type={item.get('question_type')!r}",
            )
    if not item.get("options") or not item.get("correct_answer"):
        missing = []
        if not item.get("options"):
            missing.append("options")
        if not item.get("correct_answer"):
            missing.append("correct_answer")
        reject("missing options or correct_answer", f"missing={', '.join(missing)}")
    if not item.get("rationale_correct") or not item.get("rationale_distractors"):
        missing = []
        if not item.get("rationale_correct"):
            missing.append("rationale_correct")
        if not item.get("rationale_distractors"):
            missing.append("rationale_distractors")
        reject("missing rationale", f"missing={', '.join(missing)}")
    if str(item.get("difficulty", "")).lower() == "easy":
        reject("easy item", f"difficulty={item.get('difficulty')!r}; Day 1 review requires medium or harder")
    if str(item.get("cognitive_demand", "")).lower() == "recall":
        reject("recall-only item", f"cognitive_demand={item.get('cognitive_demand')!r}")
    if not is_scenario_based(stem) and str(item.get("cognitive_demand", "")).lower() in {"recall", "explain"}:
        reject(
            "not scenario-based",
            "stem lacks scenario signals such as actor, workload, constraint, or event; "
            f"cognitive_demand={item.get('cognitive_demand')!r}",
        )
    weak_matches = [pattern for pattern in WEAK_STEM_PATTERNS if pattern in lowered]
    if weak_matches:
        reject("keyword-trivia stem", f"matched weak stem pattern(s): {', '.join(weak_matches)}")

    searchable = " ".join(
        [
            stem,
            str(item.get("rationale_correct", "")),
            distractor_text(item),
            " ".join(str(x) for x in normalize_list(item.get("options"))),
            str(item.get("source_trace_needed", "")),
        ]
    ).lower()
    stale_matches = [pattern for pattern in OUTDATED_OR_UNVERIFIED_PATTERNS if pattern in searchable]
    if stale_matches:
        reject(
            "outdated or unverified technical claim",
            f"matched stale/unverified claim pattern(s): {', '.join(stale_matches)}",
        )

    return not reasons, reasons, evidence


def option_lines(item: dict[str, Any]) -> list[str]:
    options = normalize_list(item.get("options"))
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lines: list[str] = []
    for idx, option in enumerate(options):
        lines.append(f"{letters[idx]}. {option}")
        lines.append("")
    return lines


def correct_answer_text(item: dict[str, Any]) -> str:
    answer = item.get("correct_answer")
    if isinstance(answer, list):
        return ", ".join(str(x) for x in answer)
    return str(answer)


def distractor_text(item: dict[str, Any]) -> str:
    distractors = item.get("rationale_distractors", {})
    if isinstance(distractors, dict):
        return " ".join(f"{key}: {value}" for key, value in distractors.items())
    return str(distractors)


def normalize_item(candidate: Candidate, item_id: str) -> str:
    raw = candidate.raw
    order = raw["curriculum_order"]
    topic = TOPICS[order]
    fmt = raw.get("question_format") or raw.get("question_type")
    difficulty = str(raw.get("difficulty", "medium")).lower()
    demand = str(raw.get("cognitive_demand", "judge")).lower()
    stem = str(raw.get("stem", "")).strip()

    lines = [
        f"### {item_id}",
        "",
        "| Field | Value |",
        "|---|---|",
        f"| `item_id` | {item_id} |",
        "| `status` | approved |",
        "| `official_exam_code` | AIP-C01 |",
        f"| `exam_domain` | {topic['domain']} |",
        f"| `exam_task` | {topic['task']} |",
        f"| `exam_skill` | {topic['skill']} |",
        f"| `exam_skill_local` | {topic['local_skill']} |",
        f"| `learning_unit` | {order} |",
        "| `accelerated_day` | Day 1 |",
        f"| `knowledge_type` | {topic['types']} |",
        f"| `question_format` | {fmt} |",
        f"| `difficulty` | {difficulty} |",
        f"| `cognitive_demand` | {demand} |",
        "| `estimated_time_seconds` | 120 |",
        f"| `last_reviewed` | {date.today().isoformat()} |",
        f"| `raw_source` | `{candidate.source_file}` item {candidate.raw_index} |",
        "",
        "Stem:",
        "",
        stem,
        "",
        "Options:",
        "",
        *option_lines(raw),
        f"Correct answer: {correct_answer_text(raw)}",
        "",
        f"Rationale: {str(raw.get('rationale_correct', '')).strip()}",
        "",
        f"Distractors: {distractor_text(raw)}",
        "",
        f"Misconception tags: {', '.join(f'`{x}`' for x in normalize_list(raw.get('misconception_tags')))}",
        "",
        "Source trace:",
        "",
    ]
    lines.extend(f"- {source}" for source in topic["sources"])
    lines.extend(
        [
            "",
            "Remediation target:",
            "",
            f"- `{topic['remediation']}`",
            f"- `{ANSWER_GUIDANCE}`",
            "",
        ]
    )
    return "\n".join(lines)


def render() -> str:
    candidates = load_candidates()
    provenance = source_file_provenance()
    raw_counts = Counter(c.raw.get("curriculum_order", "unknown") for c in candidates)

    approved: list[Candidate] = []
    culled: list[CullRecord] = []
    approved_stems: dict[str, list[ApprovedStem]] = defaultdict(list)
    for candidate in candidates:
        ok, reasons, evidence = review(candidate)
        order = candidate.raw.get("curriculum_order", "unknown")
        stem = str(candidate.raw.get("stem", "")).strip()
        match = duplicate_match(stem, approved_stems[order]) if ok else None
        if match:
            match_type, approved_match, similarity = match
            ok = False
            reasons.append("duplicate-pattern")
            evidence.append(
                "duplicate-pattern: "
                f"match_type={match_type}; similarity={similarity:.2f}; "
                f"candidate_stem=\"{truncate(stem, 300)}\"; "
                f"matched_approved_source=`{approved_match.source_file}` item {approved_match.raw_index}; "
                f"matched_approved_stem=\"{truncate(approved_match.stem, 300)}\""
            )
        if ok:
            approved.append(candidate)
            approved_stems[order].append(
                ApprovedStem(
                    stem=stem,
                    source_file=candidate.source_file,
                    raw_index=candidate.raw_index,
                    key=normalized_stem_key(stem),
                    terms=stem_terms(stem),
                )
            )
        else:
            culled.append(CullRecord(candidate, reasons, evidence))

    approved.sort(key=lambda c: (c.raw.get("curriculum_order", ""), c.source_file, c.raw_index))
    approved_counts = Counter(c.raw.get("curriculum_order", "unknown") for c in approved)
    culled_counts = Counter(record.candidate.raw.get("curriculum_order", "unknown") for record in culled)
    cull_reason_counts = Counter(reason for record in culled for reason in record.reasons)

    lines = [
        "# Day 1 Reviewed Question Bank",
        "",
        "## Review Status",
        "",
        "This file is a normalized reviewed bank generated from preserved raw Day 1",
        "question-candidate responses. It approves only candidates that pass",
        "schema, scenario, traceability, and quality checks. It remains partial",
        "until each Day 1 curriculum-order topic has at least 10 approved items.",
        "",
        f"Review date: {date.today().isoformat()}",
        "",
        "## Source Raw Files",
        "",
    ]
    for path in sorted(RAW_DIR.glob("*day01-*.md")):
        if "dry-run" not in path.name:
            lines.append(f"- `{path.relative_to(ROOT)}`")

    lines.extend(
        [
            "",
            "## Raw Source Provenance",
            "",
            "| Raw file | Provider | Model | Run ID |",
            "|---|---|---|---|",
        ]
    )
    for source_file, metadata in provenance.items():
        lines.append(
            f"| `{source_file}` | {metadata['provider']} | {metadata['model']} | {metadata['run_id']} |"
        )

    lines.extend(
        [
            "",
            "## Coverage Notes",
            "",
            "Primary Day 1 official coverage:",
            "",
            "- Task 1.1: Analyze requirements and design GenAI solutions.",
            "- Task 1.2: Select and configure FMs.",
            "- Task 1.6: Implement prompt engineering strategies and governance for FM interactions.",
            "- Task 2.4: Implement FM API integrations.",
            "- Task 2.5: Implement application integration patterns and development tools.",
            "",
            "Seeded cross-domain foundations:",
            "",
            "- Task 3.2: Implement data security and privacy controls.",
            "- Task 5.1: Implement evaluation systems for GenAI.",
            "",
            "The `exam_task` and `exam_skill` fields use official statements extracted",
            f"from `{EXAM_OBJECTIVES}`. The `exam_skill_local` field is an editorial",
            "description of the narrower reviewed focus tested by the item.",
            "",
            "## Review Summary",
            "",
            "| Curriculum order | Raw parsed | Approved | Culled | Completion target | Status |",
            "|---|---:|---:|---:|---:|---|",
        ]
    )
    for order in sorted(TOPICS):
        status = "complete" if approved_counts[order] >= 10 else "partial"
        lines.append(
            f"| {order} | {raw_counts[order]} | {approved_counts[order]} | {culled_counts[order]} | 10 | {status} |"
        )

    lines.extend(
        [
            "",
            "## Prompt Improvement Signals",
            "",
            "Review culls are treated as prompt-improvement data before the next",
            "generation or top-up pass. The next prompt should explicitly address",
            "the highest-frequency failure reasons below instead of only asking for",
            "more questions.",
            "",
            "| Failure reason | Count | Prompt adjustment |",
            "|---|---:|---|",
        ]
    )
    for reason, count in cull_reason_counts.most_common():
        adjustment = PROMPT_ADJUSTMENTS.get(reason, "Add a specific prompt guardrail or reviewer check for this failure mode.")
        lines.append(f"| {reason} | {count} | {adjustment} |")

    lines.extend(
        [
            "",
            "## Top-Up Guidance",
            "",
            "The completion target is 10 approved items per curriculum-order topic.",
            "Generate a surplus over the exact deficit because the review pass is",
            "expected to cull weak, duplicate, or unverifiable candidates.",
            "",
            "| Curriculum order | Approved | Deficit | Recommended raw top-up |",
            "|---|---:|---:|---:|",
        ]
    )
    for order in sorted(TOPICS):
        deficit = max(0, 10 - approved_counts[order])
        recommended = 0 if deficit == 0 else max(deficit + 2, round(deficit * 1.5))
        lines.append(f"| {order} | {approved_counts[order]} | {deficit} | {recommended} |")

    lines.extend(
        [
            "",
            "## Review Rules Applied",
            "",
            "- Approved items must use the required schema fields or a repairable equivalent.",
            "- Approved items must be scenario-based rather than keyword-trivia recall.",
            "- Approved items must not duplicate or closely mirror an already approved item for the same topic.",
            "- Every cull must include audit evidence explaining the failed rule.",
            "- Duplicate culls must show the rejected stem and the matched approved stem as audit evidence.",
            "- Approved items must have plausible options, correct answers, and distractor rationales.",
            "- Items with stale claims such as `as of early 2024` or unsupported service-limit claims are culled.",
            "- Remediation targets are mapped to existing Day 1 artifact files and answer guidance.",
            "- Source traces are normalized to the official exam guide, AWS documentation, and Day 1 learning materials.",
            "",
            "## Approved Items",
            "",
        ]
    )
    for idx, candidate in enumerate(approved, 1):
        lines.append(normalize_item(candidate, f"P1-AIP-D1-{idx:03d}"))

    lines.extend(
        [
            "## Culled Items",
            "",
            "| Raw source | Curriculum order | Stem excerpt | Reasons | Evidence |",
            "|---|---|---|---|---|",
        ]
    )
    for record in culled:
        candidate = record.candidate
        stem = table_cell(truncate(str(candidate.raw.get("stem", "")), 120))
        evidence = "<br>".join(table_cell(item) for item in record.evidence) if record.evidence else ""
        lines.append(
            f"| `{candidate.source_file}` item {candidate.raw_index} | {candidate.raw.get('curriculum_order', 'unknown')} | {stem} | {', '.join(record.reasons)} | {evidence} |"
        )

    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(render(), encoding="utf-8")
    print(OUT.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
