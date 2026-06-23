#!/usr/bin/env python3
"""Run normalize/review/top-up loops until per-topic coverage is satisfied."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
EXAM_PREP = ROOT / "docs/Pilot1/aip-c01/exam-prep"


def day_slug(day: int) -> str:
    return f"day-{day:02d}"


def utc_stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H%M%SZ")


def utc_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def feedback_path(day: int) -> Path:
    return EXAM_PREP / f"reviewed/{day_slug(day)}/{day_slug(day)}-review-feedback.json"


class LoopLogger:
    def __init__(self, day: int) -> None:
        directory = EXAM_PREP / f"logs/{day_slug(day)}"
        directory.mkdir(parents=True, exist_ok=True)
        stamp = utc_stamp()
        self.text_path = directory / f"{stamp}-{day_slug(day)}-topup-loop.log"
        self.jsonl_path = directory / f"{stamp}-{day_slug(day)}-topup-loop.jsonl"

    def emit(self, event: str, message: str, **fields: object) -> None:
        record = {"timestamp_utc": utc_iso(), "event": event, "message": message, **fields}
        details = " ".join(f"{key}={value}" for key, value in fields.items())
        line = f"{record['timestamp_utc']} {event} - {message}"
        if details:
            line += f" {details}"
        with self.text_path.open("a", encoding="utf-8") as handle:
            handle.write(line + "\n")
        with self.jsonl_path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")
        print(line, flush=True)


def run_command(args: list[str], logger: LoopLogger, event_name: str) -> None:
    logger.emit(event_name, "command started", command=" ".join(args))
    completed = subprocess.run(args, cwd=ROOT, text=True, capture_output=True, check=False)
    if completed.stdout:
        for line in completed.stdout.splitlines():
            logger.emit(event_name, "stdout", line=line)
    if completed.stderr:
        for line in completed.stderr.splitlines():
            logger.emit(event_name, "stderr", line=line)
    if completed.returncode != 0:
        logger.emit(event_name, "command failed", returncode=completed.returncode)
        raise SystemExit(completed.returncode)
    logger.emit(event_name, "command completed", returncode=completed.returncode)


def load_feedback(day: int) -> dict[str, Any]:
    path = feedback_path(day)
    if not path.exists():
        raise SystemExit(f"Missing review feedback file: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def short_topics(feedback: dict[str, Any], target: int) -> dict[str, int]:
    result: dict[str, int] = {}
    for topic, summary in feedback.get("summary_by_topic", {}).items():
        reviewed = int(summary.get("reviewed_candidates", 0))
        if reviewed < target:
            result[topic] = target - reviewed
    return result


def top_up_count(deficit: int, minimum_surplus: int) -> int:
    return max(deficit + minimum_surplus, round(deficit * 1.5))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--day", type=int, required=True, choices=range(1, 8))
    parser.add_argument("--target", type=int, default=10, help="Minimum reviewed candidates per topic.")
    parser.add_argument("--max-iterations", type=int, default=3, help="Maximum top-up iterations.")
    parser.add_argument("--minimum-surplus", type=int, default=2, help="Extra raw items above each deficit.")
    parser.add_argument("--dry-run", action="store_true", help="Write top-up prompts without calling the LLM.")
    args = parser.parse_args()

    logger = LoopLogger(args.day)
    logger.emit(
        "loop-start",
        "top-up loop started",
        day=args.day,
        target=args.target,
        max_iterations=args.max_iterations,
        dry_run=args.dry_run,
        log_file=str(logger.text_path.relative_to(ROOT)),
        jsonl_file=str(logger.jsonl_path.relative_to(ROOT)),
    )

    for iteration in range(1, args.max_iterations + 1):
        logger.emit("iteration-start", "normalizing and reviewing", iteration=iteration)
        run_command(
            [sys.executable, "scripts/normalize_exam_prep_questions.py", "--day", str(args.day)],
            logger,
            "normalize",
        )
        run_command(
            [sys.executable, "scripts/review_exam_prep_questions.py", "--day", str(args.day)],
            logger,
            "review",
        )
        feedback = load_feedback(args.day)
        shorts = short_topics(feedback, args.target)
        if not shorts:
            logger.emit("loop-complete", "coverage target satisfied", iteration=iteration)
            return 0

        logger.emit("coverage-short", "topics remain short", iteration=iteration, short_topics=shorts)
        if args.dry_run and iteration == args.max_iterations:
            logger.emit("loop-blocked", "dry-run reached max iterations with short topics", short_topics=shorts)
            return 2

        for topic, deficit in sorted(shorts.items()):
            count = top_up_count(deficit, args.minimum_surplus)
            command = [
                sys.executable,
                "scripts/generate_exam_prep_questions.py",
                "--day",
                str(args.day),
                "--top-up-topic",
                topic,
                "--count",
                str(count),
            ]
            if args.dry_run:
                command.append("--dry-run")
            logger.emit("top-up-start", "generating feedback-informed top-up", topic=topic, deficit=deficit, count=count)
            run_command(command, logger, "top-up")

        logger.emit("iteration-complete", "top-ups complete; next iteration will re-normalize and re-review", iteration=iteration)

    feedback = load_feedback(args.day)
    shorts = short_topics(feedback, args.target)
    if shorts:
        logger.emit("loop-blocked", "maximum iterations reached with short topics", short_topics=shorts)
        return 2
    logger.emit("loop-complete", "coverage target satisfied")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
