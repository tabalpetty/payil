#!/usr/bin/env python3
"""Generate raw Day 1 AIP-C01 question candidates with the OpenAI API.

The script intentionally saves raw model output as evidence. It does not
approve, normalize, or source-check question-bank items.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import textwrap
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[2]
PROMPT_PACK = ROOT / "docs/Pilot1/aip-c01/exam-prep/day-01-question-generation-prompts.md"
RAW_DIR = ROOT / "docs/Pilot1/aip-c01/exam-prep/raw/day-01"
REVIEWED_BANK = ROOT / "docs/Pilot1/aip-c01/exam-prep/reviewed/day-01/day-01-reviewed-question-bank.md"
DEFAULT_MODEL = "gpt-4.1"

BATCH_TO_SECTION = {
    "balanced": "Prompt 1: Day 1 Balanced Mini-Batch",
    "foundations": "Prompt 2: Day 1 Foundation Concepts",
    "system-map": "Prompt 3: Day 1 AWS System Map And Architecture",
    "applied-foundations": "Prompt 4: Day 1 Model Selection, Bedrock Invocation, Prompting, Evaluation",
}

TOPIC_TO_SECTION = {
    "Day01-order001": "Topic Prompt: Day01-order001 Foundation Models And GenAI Fundamentals",
    "Day01-order002": "Topic Prompt: Day01-order002 Tokens Context Inference Parameters",
    "Day01-order003": "Topic Prompt: Day01-order003 AWS GenAI Service Landscape",
    "Day01-order004": "Topic Prompt: Day01-order004 Application Integration Patterns",
    "Day01-order005": "Topic Prompt: Day01-order005 Trust Boundaries IAM Data Protection",
    "Day01-order006": "Topic Prompt: Day01-order006 Requirements Basic Solution Architecture",
    "Day01-order007": "Topic Prompt: Day01-order007 Model Capabilities Limitations Selection",
    "Day01-order008": "Topic Prompt: Day01-order008 Basic Bedrock Model Invocation",
    "Day01-order009": "Topic Prompt: Day01-order009 Prompt Fundamentals Structured Output",
    "Day01-order010": "Topic Prompt: Day01-order010 Basic Evaluation Golden Datasets",
}


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        raise SystemExit(f"Missing required file: {path}")


def extract_section(markdown: str, heading: str) -> str:
    pattern = re.compile(
        rf"^##+ {re.escape(heading)}\n(?P<body>.*?)(?=^##+ |\Z)",
        re.MULTILINE | re.DOTALL,
    )
    match = pattern.search(markdown)
    if not match:
        raise SystemExit(f"Could not find section: {heading}")
    return match.group("body").strip()


def prior_stems_for_topic(topic: str) -> list[str]:
    if not REVIEWED_BANK.exists():
        return []

    text = read_text(REVIEWED_BANK)
    stems: list[str] = []
    for block in re.split(r"^### ", text, flags=re.MULTILINE):
        if f"| `learning_unit` | {topic} |" not in block:
            continue
        match = re.search(r"\nStem:\n\n(?P<stem>.*?)(?=\n\nOptions:\n)", block, re.DOTALL)
        if match:
            stems.append(" ".join(match.group("stem").split()))

    cull_table = text.split("## Culled Items", 1)[-1]
    for line in cull_table.splitlines():
        if f"| {topic} |" not in line:
            continue
        parts = [part.strip() for part in line.strip().strip("|").split("|")]
        if len(parts) >= 3 and parts[2] != "Stem excerpt":
            stems.append(parts[2].replace("\\|", "|"))

    return stems


def build_prompt(section_heading: str) -> str:
    pack = read_text(PROMPT_PACK)
    selected = extract_section(pack, section_heading)

    return textwrap.dedent(
        f"""\
        You are generating raw draft practice-question candidates for a curriculum repository.

        Follow the complete Day 1 prompt pack below, especially the output schema,
        global guardrails, and question quality requirements. Then execute the
        selected batch prompt.

        IMPORTANT:
        - Return only the generated draft questions and any compact batch metadata.
        - Do not say you cannot source-review the items; instead mark source_trace_needed.
        - Do not mark anything as approved.
        - Do not include copied official exam questions or third-party question-bank content.

        ===== DAY 1 PROMPT PACK =====
        {pack}

        ===== SELECTED BATCH TO EXECUTE =====
        {selected}
        """
    )


def build_top_up_prompt(section_heading: str, topic: str, count: int) -> str:
    pack = read_text(PROMPT_PACK)
    selected = extract_section(pack, section_heading)
    prior_stems = prior_stems_for_topic(topic)
    prior_stem_block = "\n".join(f"- {stem}" for stem in prior_stems) or "- No reviewed-bank stems found yet."

    return textwrap.dedent(
        f"""\
        You are generating raw draft practice-question candidates for a curriculum repository.

        Follow the complete Day 1 prompt pack below, especially the output schema,
        global guardrails, and question quality requirements. Then execute the
        selected topic prompt as a top-up generation.

        IMPORTANT:
        - Generate exactly {count} additional draft questions for {topic}.
        - Return only a JSON array of the generated draft questions.
        - Do not repeat stems, scenarios, constraints, misconceptions, or answer
          patterns from prior raw or reviewed output.
        - Make every item scenario-based and professional-level.
        - Avoid glossary stems such as "Which AWS service...", "What is...",
          "Which best describes...", or other keyword-recognition items.
        - Avoid stale service-capability claims such as "currently does not
          support" unless the exact official AWS source is identified in
          source_trace_needed.
        - Do not say you cannot source-review the items; instead mark source_trace_needed.
        - Do not mark anything as approved.
        - Do not include copied official exam questions or third-party question-bank content.

        ===== DAY 1 PROMPT PACK =====
        {pack}

        ===== SELECTED TOPIC PROMPT TO EXECUTE AS TOP-UP =====
        {selected}

        ===== EXISTING STEMS AND REJECTED STEM EXCERPTS TO AVOID =====
        {prior_stem_block}

        ===== TOP-UP OVERRIDE =====
        Generate exactly {count} questions for {topic}, not the full default topic count.
        """
    )


def openai_responses_create(api_key: str, model: str, prompt: str, timeout: int) -> dict[str, Any]:
    payload = {
        "model": model,
        "input": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_text",
                        "text": prompt,
                    }
                ],
            }
        ],
    }

    request = Request(
        "https://api.openai.com/v1/responses",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )

    try:
        with urlopen(request, timeout=timeout) as response:
            return json.loads(response.read().decode("utf-8"))
    except HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise SystemExit(f"OpenAI API error {exc.code}:\n{body}") from exc
    except URLError as exc:
        raise SystemExit(f"Network error calling OpenAI API: {exc}") from exc


def extract_output_text(response: dict[str, Any]) -> str:
    chunks: list[str] = []
    for item in response.get("output", []):
        for content in item.get("content", []):
            if content.get("type") == "output_text" and "text" in content:
                chunks.append(content["text"])
    if chunks:
        return "\n\n".join(chunks)
    return json.dumps(response, indent=2)


def safe_model_name(model: str) -> str:
    return re.sub(r"[^A-Za-z0-9_.-]+", "-", model).strip("-")


def write_raw_response(run_id: str, model: str, prompt: str, response: dict[str, Any]) -> Path:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H%M%SZ")
    path = RAW_DIR / f"{stamp}-openai-{safe_model_name(model)}-day01-{run_id}.md"

    output_text = extract_output_text(response)
    metadata = {
        "provider": "openai",
        "model": model,
        "run_id": run_id,
        "created_utc": stamp,
        "status": "raw-draft",
        "prompt_pack": str(PROMPT_PACK.relative_to(ROOT)),
    }

    path.write_text(
        "\n".join(
            [
                "# Raw Day 1 Question Generation Response",
                "",
                "## Metadata",
                "",
                "```json",
                json.dumps(metadata, indent=2),
                "```",
                "",
                "## Prompt Sent",
                "",
                "```text",
                prompt,
                "```",
                "",
                "## Raw Response Text",
                "",
                output_text,
                "",
                "## Raw Response JSON",
                "",
                "```json",
                json.dumps(response, indent=2),
                "```",
                "",
            ]
        ),
        encoding="utf-8",
    )
    return path


def write_dry_run(run_id: str, model: str, prompt: str) -> Path:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H%M%SZ")
    path = RAW_DIR / f"{stamp}-dry-run-openai-{safe_model_name(model)}-day01-{run_id}-prompt.md"
    path.write_text(
        "\n".join(
            [
                "# Dry Run Prompt",
                "",
                f"- run_id: `{run_id}`",
                f"- model: `{model}`",
                f"- created_utc: `{stamp}`",
                "",
                "```text",
                prompt,
                "```",
                "",
            ]
        ),
        encoding="utf-8",
    )
    return path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    target = parser.add_mutually_exclusive_group()
    target.add_argument(
        "--batch",
        choices=sorted(BATCH_TO_SECTION),
        help="Prompt batch to execute.",
    )
    target.add_argument(
        "--topic",
        choices=sorted(TOPIC_TO_SECTION),
        help="Single Day 1 topic prompt to execute.",
    )
    target.add_argument(
        "--all-topics",
        action="store_true",
        help="Execute all ten Day 1 topic prompts sequentially.",
    )
    target.add_argument(
        "--top-up-topic",
        choices=sorted(TOPIC_TO_SECTION),
        help="Generate a smaller top-up set for one Day 1 topic.",
    )
    parser.add_argument(
        "--count",
        type=int,
        default=2,
        help="Number of questions for --top-up-topic. Defaults to 2.",
    )
    parser.add_argument(
        "--model",
        default=os.environ.get("OPENAI_MODEL", DEFAULT_MODEL),
        help=f"OpenAI model to use. Defaults to OPENAI_MODEL or {DEFAULT_MODEL}.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Write the prompt that would be sent without calling the API.",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=900,
        help="API timeout in seconds. Large question batches may take a while.",
    )
    args = parser.parse_args()

    api_key = os.environ.get("OPENAI_API_KEY")
    if not args.dry_run and not api_key:
        raise SystemExit("OPENAI_API_KEY is not set. Use --dry-run to inspect the prompt without calling the API.")

    if args.top_up_topic:
        runs = [
            (
                f"{args.top_up_topic.lower().replace('day01-', '')}-top-up-{args.count}",
                TOPIC_TO_SECTION[args.top_up_topic],
                args.top_up_topic,
                args.count,
            )
        ]
    elif args.all_topics:
        runs = [
            (topic.lower().replace("day01-", ""), section, None, None)
            for topic, section in TOPIC_TO_SECTION.items()
        ]
    elif args.topic:
        runs = [(args.topic.lower().replace("day01-", ""), TOPIC_TO_SECTION[args.topic], None, None)]
    else:
        batch = args.batch or "balanced"
        runs = [(batch, BATCH_TO_SECTION[batch], None, None)]

    for run_id, section, top_up_topic, top_up_count in runs:
        if top_up_topic and top_up_count:
            prompt = build_top_up_prompt(section, top_up_topic, top_up_count)
        else:
            prompt = build_prompt(section)
        if args.dry_run:
            path = write_dry_run(run_id, args.model, prompt)
            print(path.relative_to(ROOT))
            continue

        started = time.time()
        response = openai_responses_create(api_key or "", args.model, prompt, args.timeout)
        path = write_raw_response(run_id, args.model, prompt, response)
        elapsed = time.time() - started
        print(path.relative_to(ROOT))
        print(f"elapsed_seconds={elapsed:.1f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
