#!/usr/bin/env python3
"""Generate raw AIP-C01 question candidates from day prompt packs.

This is the reusable Step 7 adapter. It saves raw model output with provenance
and can also write dry-run prompt files without calling an LLM.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[2]
EXAM_PREP = ROOT / "docs/Pilot1/aip-c01/exam-prep"
DEFAULT_MODEL = "gpt-4.1"
LOCAL_ENV = ROOT / ".env.local"


def day_slug(day: int) -> str:
    return f"day-{day:02d}"


def day_label(day: int) -> str:
    return f"Day{day:02d}"


def prompt_pack_path(day: int) -> Path:
    return EXAM_PREP / f"{day_slug(day)}-question-generation-prompts.md"


def review_feedback_path(day: int) -> Path:
    return EXAM_PREP / f"reviewed/{day_slug(day)}/{day_slug(day)}-review-feedback.json"


def raw_dir(day: int) -> Path:
    return EXAM_PREP / f"raw/{day_slug(day)}"


def log_dir(day: int) -> Path:
    return EXAM_PREP / f"logs/{day_slug(day)}"


def utc_stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H%M%SZ")


def utc_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        raise SystemExit(f"Missing required file: {path}")


def env_value(name: str) -> str | None:
    value = os.environ.get(name)
    if value:
        return value
    if not LOCAL_ENV.exists():
        return None
    for line in LOCAL_ENV.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or "=" not in stripped:
            continue
        key, raw_value = stripped.split("=", 1)
        if key.strip() == name:
            return raw_value.strip().strip('"').strip("'")
    return None


def extract_section(markdown: str, heading: str) -> str:
    pattern = re.compile(
        rf"^##+ {re.escape(heading)}\n(?P<body>.*?)(?=^##+ |\Z)",
        re.MULTILINE | re.DOTALL,
    )
    match = pattern.search(markdown)
    if not match:
        raise SystemExit(f"Could not find section: {heading}")
    return match.group("body").strip()


def sections_for_day(day: int) -> tuple[dict[str, str], dict[str, str]]:
    pack = read_text(prompt_pack_path(day))
    batch_sections: dict[str, str] = {}
    topic_sections: dict[str, str] = {}
    for match in re.finditer(r"^## (?P<heading>.+)$", pack, flags=re.MULTILINE):
        heading = match.group("heading")
        if heading.startswith("Prompt 1:"):
            batch_sections["balanced"] = heading
        elif heading.startswith("Topic Prompt:"):
            topic_match = re.search(rf"{day_label(day)}-order\d{{3}}", heading)
            if topic_match:
                topic_sections[topic_match.group(0)] = heading
    if "balanced" not in batch_sections:
        raise SystemExit(f"Prompt pack has no balanced prompt: {prompt_pack_path(day)}")
    if not topic_sections:
        raise SystemExit(f"Prompt pack has no topic prompts: {prompt_pack_path(day)}")
    return batch_sections, dict(sorted(topic_sections.items()))


def build_prompt(day: int, section_heading: str) -> str:
    pack = read_text(prompt_pack_path(day))
    selected = extract_section(pack, section_heading)

    return "\n".join(
        [
            "You are generating raw draft practice-question candidates for a curriculum repository.",
            "",
            f"Follow the complete Day {day} prompt pack below, especially the lean output schema,",
            "global guardrails, question quality requirements, source defense,",
            "and official objective scope. Then execute the",
            "selected prompt.",
            "",
            "IMPORTANT:",
            "- Return only the generated draft questions and any compact batch metadata.",
            "- Do not say you cannot source-review the items; discard or rewrite unsupported items.",
            "- Do not mark anything as approved.",
            "- Do not include copied official exam questions or third-party question-bank content.",
            "- Preserve exact official objective values from the selected prompt.",
            "- Never place reviewer instructions or verification commentary in learner-visible stems, options, answers, rationales, or source traces.",
            "- Put any reviewer-only concern in generation_notes.",
            "",
            f"===== DAY {day} PROMPT PACK =====",
            pack,
            "",
            "===== SELECTED PROMPT TO EXECUTE =====",
            selected,
            "",
        ]
    )


def build_top_up_prompt(day: int, section_heading: str, topic: str, count: int) -> str:
    base_prompt = build_prompt(day, section_heading)
    feedback = render_review_feedback_for_topic(day, topic)
    return "\n".join(
        [
            base_prompt,
            "===== TOP-UP OVERRIDE =====",
            f"Generate exactly {count} questions for {topic}, not the full default",
            "topic count. New items must use different scenarios, constraints,",
            "misconceptions, and answer patterns from prior generated output.",
            "",
            feedback,
        ]
    )


def render_review_feedback_for_topic(day: int, topic: str) -> str:
    path = review_feedback_path(day)
    if not path.exists():
        return "===== REVIEW FEEDBACK FROM PRIOR PASS =====\nNo prior review-feedback JSON was found for this day.\n"

    feedback = json.loads(path.read_text(encoding="utf-8"))
    topic_summary = feedback.get("summary_by_topic", {}).get(topic, {})
    top_up = feedback.get("top_up_guidance", {}).get(topic, {})
    reviewed = feedback.get("reviewed_stems_by_topic", {}).get(topic, [])
    culled = [
        item
        for item in feedback.get("culled_items", [])
        if item.get("curriculum_order") == topic
    ]
    global_signals = feedback.get("prompt_improvement_signals", [])

    lines = [
        "===== REVIEW FEEDBACK FROM PRIOR PASS =====",
        "",
        "Use this feedback to avoid repeating failed patterns from the previous review pass.",
        "",
        f"Topic review status for {topic}:",
        f"- reviewed_candidates: {topic_summary.get('reviewed_candidates', 'unknown')}",
        f"- deficit_to_10: {top_up.get('deficit_to_10', 'unknown')}",
        f"- recommended_raw_top_up: {top_up.get('recommended_raw_top_up', 'unknown')}",
        "",
        "Global prompt-improvement signals:",
    ]
    for signal in global_signals:
        if signal.get("failure_reason") == "unsupported high-risk claim":
            continue
        lines.append(
            f"- {signal.get('failure_reason')}: {signal.get('prompt_adjustment')} "
            f"(count={signal.get('count')})"
        )

    lines.extend(["", "Already reviewed stems for this topic. Do not duplicate or lightly paraphrase these:"])
    for item in reviewed[:15]:
        lines.append(f"- {item.get('item_id')}: {truncate(item.get('stem', ''), 260)}")

    lines.extend(["", "Rejected stems and cull evidence for this topic. Avoid these failure modes:"])
    actionable_culls = [
        item
        for item in culled
        if item.get("reasons") != ["unsupported high-risk claim"]
    ]
    if actionable_culls:
        for item in actionable_culls[:15]:
            evidence = " | ".join(str(entry) for entry in item.get("evidence", []))
            lines.append(
                f"- raw_source={item.get('raw_source')}; reasons={', '.join(item.get('reasons', []))}; "
                f"stem={truncate(item.get('stem', ''), 240)}; evidence={truncate(evidence, 320)}"
            )
    else:
        lines.append("- No currently actionable culled stems for this topic in the prior pass.")

    lines.extend(
        [
            "",
            "Top-up-specific instructions:",
            "- Do not create service-name lookup questions.",
            "- Do not use high-risk service-capability claims unless the exact official AWS source is named in `source_trace`.",
            "- Do not place phrases such as 'reviewer should confirm' or 'verify against current documentation' in learner-visible fields.",
            "- Prefer decision, diagnosis, tradeoff, or first-action questions grounded in the topic brief.",
            "",
        ]
    )
    return "\n".join(lines)


def truncate(value: str, limit: int) -> str:
    compact = " ".join(value.split())
    return compact if len(compact) <= limit else compact[: limit - 3] + "..."


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


def count_candidate_items(text: str) -> int:
    return len(re.findall(r'"stem"\s*:', text))


def safe_model_name(model: str) -> str:
    return re.sub(r"[^A-Za-z0-9_.-]+", "-", model).strip("-")


class RunLogger:
    def __init__(self, day: int, run_label: str) -> None:
        directory = log_dir(day)
        directory.mkdir(parents=True, exist_ok=True)
        stamp = utc_stamp()
        safe_label = re.sub(r"[^A-Za-z0-9_.-]+", "-", run_label).strip("-")
        self.text_path = directory / f"{stamp}-{day_slug(day)}-{safe_label}.log"
        self.jsonl_path = directory / f"{stamp}-{day_slug(day)}-{safe_label}.jsonl"

    def emit(self, event: str, message: str, **fields: object) -> None:
        record = {
            "timestamp_utc": utc_iso(),
            "event": event,
            "message": message,
            **fields,
        }
        human_fields = " ".join(f"{key}={value}" for key, value in fields.items())
        human_line = f"{record['timestamp_utc']} {event} - {message}"
        if human_fields:
            human_line += f" {human_fields}"
        with self.text_path.open("a", encoding="utf-8") as handle:
            handle.write(human_line + "\n")
        with self.jsonl_path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")
        print(human_line, flush=True)


def write_raw_response(day: int, run_id: str, model: str, prompt: str, response: dict[str, Any]) -> Path:
    out_dir = raw_dir(day)
    out_dir.mkdir(parents=True, exist_ok=True)
    stamp = utc_stamp()
    path = out_dir / f"{stamp}-openai-{safe_model_name(model)}-{day_slug(day)}-{run_id}.md"
    output_text = extract_output_text(response)
    metadata = {
        "provider": "openai",
        "model": model,
        "run_id": run_id,
        "created_utc": stamp,
        "status": "raw-draft",
        "accelerated_day": f"Day {day}",
        "prompt_pack": str(prompt_pack_path(day).relative_to(ROOT)),
        "provenance": "external LLM generation",
    }

    path.write_text(
        "\n".join(
            [
                f"# Raw Day {day} Question Generation Response",
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


def write_dry_run(day: int, run_id: str, model: str, prompt: str) -> Path:
    out_dir = raw_dir(day)
    out_dir.mkdir(parents=True, exist_ok=True)
    stamp = utc_stamp()
    path = out_dir / f"{stamp}-dry-run-openai-{safe_model_name(model)}-{day_slug(day)}-{run_id}-prompt.md"
    metadata = {
        "provider": "openai",
        "model": model,
        "run_id": run_id,
        "created_utc": stamp,
        "status": "dry-run-prompt",
        "accelerated_day": f"Day {day}",
        "prompt_pack": str(prompt_pack_path(day).relative_to(ROOT)),
        "provenance": "prompt only; no LLM call",
    }
    path.write_text(
        "\n".join(
            [
                f"# Dry Run Day {day} Prompt",
                "",
                "## Metadata",
                "",
                "```json",
                json.dumps(metadata, indent=2),
                "```",
                "",
                "## Prompt That Would Be Sent",
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


def run_specs(args: argparse.Namespace) -> list[tuple[str, str, str | None, int | None]]:
    batch_sections, topic_sections = sections_for_day(args.day)
    if args.top_up_topic:
        return [
            (
                f"{args.top_up_topic.lower().replace(day_label(args.day).lower() + '-', '')}-top-up-{args.count}",
                topic_sections[args.top_up_topic],
                args.top_up_topic,
                args.count,
            )
        ]
    if args.all_topics:
        return [
            (topic.lower().replace(day_label(args.day).lower() + "-", ""), heading, None, None)
            for topic, heading in topic_sections.items()
        ]
    if args.topic:
        return [(args.topic.lower().replace(day_label(args.day).lower() + "-", ""), topic_sections[args.topic], None, None)]
    batch = args.batch or "balanced"
    return [(batch, batch_sections[batch], None, None)]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--day", type=int, required=True, choices=range(1, 8), help="Accelerated day number.")
    target = parser.add_mutually_exclusive_group()
    target.add_argument("--batch", choices=["balanced"], help="Prompt batch to execute.")
    target.add_argument("--topic", help="Single topic prompt to execute, such as Day02-order001.")
    target.add_argument("--all-topics", action="store_true", help="Execute all topic prompts sequentially.")
    target.add_argument("--top-up-topic", help="Generate a smaller top-up set for one topic.")
    parser.add_argument("--count", type=int, default=2, help="Number of questions for --top-up-topic. Defaults to 2.")
    parser.add_argument(
        "--model",
        default=os.environ.get("OPENAI_MODEL", DEFAULT_MODEL),
        help=f"OpenAI model to use. Defaults to OPENAI_MODEL or {DEFAULT_MODEL}.",
    )
    parser.add_argument("--dry-run", action="store_true", help="Write prompts without calling the API.")
    parser.add_argument("--timeout", type=int, default=900, help="API timeout in seconds.")
    args = parser.parse_args()

    _, topic_sections = sections_for_day(args.day)
    valid_topics = set(topic_sections)
    if args.topic and args.topic not in valid_topics:
        raise SystemExit(f"Unknown topic for Day {args.day}: {args.topic}")
    if args.top_up_topic and args.top_up_topic not in valid_topics:
        raise SystemExit(f"Unknown top-up topic for Day {args.day}: {args.top_up_topic}")

    api_key = env_value("OPENAI_API_KEY")
    if not args.dry_run and not api_key:
        raise SystemExit("OPENAI_API_KEY is not set. Use --dry-run to inspect prompts without calling the API.")

    runs = run_specs(args)
    if args.all_topics:
        run_label = "all-topics"
    elif args.topic:
        run_label = args.topic.lower()
    elif args.top_up_topic:
        run_label = f"{args.top_up_topic.lower()}-top-up-{args.count}"
    else:
        run_label = args.batch or "balanced"
    logger = RunLogger(args.day, run_label)
    logger.emit(
        "run-start",
        "generation run started",
        day=args.day,
        model=args.model,
        dry_run=args.dry_run,
        run_count=len(runs),
        log_file=str(logger.text_path.relative_to(ROOT)),
        jsonl_file=str(logger.jsonl_path.relative_to(ROOT)),
    )

    total_candidates = 0
    run_started = time.time()
    for index, (run_id, section, top_up_topic, top_up_count) in enumerate(runs, start=1):
        logger.emit(
            "run-item-start",
            "preparing prompt section",
            index=index,
            total=len(runs),
            run_id=run_id,
            section=section,
        )
        if top_up_topic and top_up_count:
            prompt = build_top_up_prompt(args.day, section, top_up_topic, top_up_count)
        else:
            prompt = build_prompt(args.day, section)

        if args.dry_run:
            path = write_dry_run(args.day, run_id, args.model, prompt)
            logger.emit(
                "file-written",
                "dry-run prompt saved",
                index=index,
                total=len(runs),
                run_id=run_id,
                path=str(path.relative_to(ROOT)),
            )
            continue

        logger.emit(
            "api-request-start",
            "calling OpenAI Responses API",
            index=index,
            total=len(runs),
            run_id=run_id,
            timeout_seconds=args.timeout,
        )
        started = time.time()
        response = openai_responses_create(api_key or "", args.model, prompt, args.timeout)
        elapsed = time.time() - started
        output_text = extract_output_text(response)
        candidate_count = count_candidate_items(output_text)
        total_candidates += candidate_count
        usage = response.get("usage", {})
        logger.emit(
            "api-request-complete",
            "OpenAI response received",
            index=index,
            total=len(runs),
            run_id=run_id,
            elapsed_seconds=round(elapsed, 1),
            candidate_count=candidate_count,
            response_status=response.get("status"),
            input_tokens=usage.get("input_tokens"),
            output_tokens=usage.get("output_tokens"),
            total_tokens=usage.get("total_tokens"),
        )
        path = write_raw_response(args.day, run_id, args.model, prompt, response)
        logger.emit(
            "file-written",
            "raw response saved",
            index=index,
            total=len(runs),
            run_id=run_id,
            path=str(path.relative_to(ROOT)),
            candidate_count=candidate_count,
        )
    logger.emit(
        "run-complete",
        "generation run completed",
        elapsed_seconds=round(time.time() - run_started, 1),
        run_count=len(runs),
        total_candidates=total_candidates,
        log_file=str(logger.text_path.relative_to(ROOT)),
        jsonl_file=str(logger.jsonl_path.relative_to(ROOT)),
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
