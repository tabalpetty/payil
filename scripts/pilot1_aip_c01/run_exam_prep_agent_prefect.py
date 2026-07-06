#!/usr/bin/env python3
"""Run the exam-prep production workflow for one accelerated day with Prefect.

This is an orchestrator over the existing unit-level scripts. It does not
replace their review gates, and it does not declare a bank approved when final
source verification or final gates block.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path

try:
    from prefect import flow, get_run_logger, task
except ModuleNotFoundError as exc:  # pragma: no cover - exercised by CLI use.
    raise SystemExit(
        "Prefect is not installed. Install it with:\n\n"
        "  python3 -m pip install -r requirements-prefect.txt\n\n"
        "Then rerun this command."
    ) from exc


ROOT = Path(__file__).resolve().parents[2]
EXAM_PREP = ROOT / "docs/Pilot1/aip-c01/exam-prep"


@dataclass
class StepResult:
    name: str
    command: list[str]
    returncode: int
    stdout: str
    stderr: str
    status: str


@dataclass
class AgentReport:
    day: int
    target: int
    status: str
    started_at_utc: str
    finished_at_utc: str
    completed_steps: list[str]
    blocked_step: str | None
    outputs: dict[str, str]
    step_results: list[StepResult]
    next_action: str


def utc_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def day_slug(day: int) -> str:
    return f"day-{day:02d}"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def reviewed_dir(day: int) -> Path:
    return EXAM_PREP / f"reviewed/{day_slug(day)}"


def outputs_for_day(day: int) -> dict[str, str]:
    slug = day_slug(day)
    return {
        "topic_briefs": rel(EXAM_PREP / f"topic-briefs/{slug}"),
        "prompt_pack": rel(EXAM_PREP / f"{slug}-question-generation-prompts.md"),
        "raw_dir": rel(EXAM_PREP / f"raw/{slug}"),
        "logs_dir": rel(EXAM_PREP / f"logs/{slug}"),
        "reviewed_dir": rel(reviewed_dir(day)),
        "normalized_bank": rel(reviewed_dir(day) / f"{slug}-normalized-draft-question-bank.md"),
        "candidate_bank": rel(reviewed_dir(day) / f"{slug}-reviewed-candidate-bank.md"),
        "reviewed_bank": rel(reviewed_dir(day) / f"{slug}-reviewed-question-bank.md"),
        "source_verification": rel(reviewed_dir(day) / f"{slug}-source-verification.json"),
        "source_url_verification": rel(reviewed_dir(day) / f"{slug}-source-url-verification.json"),
        "claim_source_verification": rel(reviewed_dir(day) / f"{slug}-claim-source-verification.json"),
        "source_review_triage": rel(reviewed_dir(day) / f"{slug}-source-review-triage.json"),
        "grounded_claim_judge": rel(reviewed_dir(day) / f"{slug}-grounded-claim-judge.json"),
        "answer_position_report": rel(reviewed_dir(day) / f"{slug}-answer-position-report.md"),
        "final_gate_report": rel(reviewed_dir(day) / f"{slug}-final-gate-report.md"),
        "final_gates_json": rel(reviewed_dir(day) / f"{slug}-final-gates.json"),
        "agent_report": rel(reviewed_dir(day) / f"{slug}-exam-prep-agent-run-report.json"),
    }


def execute_command(name: str, command: list[str], allow_failure: bool = False) -> StepResult:
    print(f"[{name}] {' '.join(command)}", flush=True)
    completed = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=False)
    if completed.stdout:
        print(completed.stdout, end="", flush=True)
    if completed.stderr:
        print(completed.stderr, end="", file=sys.stderr, flush=True)

    status = "completed" if completed.returncode == 0 else "blocked"
    result = StepResult(
        name=name,
        command=command,
        returncode=completed.returncode,
        stdout=completed.stdout,
        stderr=completed.stderr,
        status=status,
    )
    if completed.returncode != 0 and not allow_failure:
        raise RuntimeError(f"{name} failed with exit code {completed.returncode}")
    return result


@task(retries=0)
def run_step(name: str, command: list[str], allow_failure: bool = False) -> StepResult:
    logger = get_run_logger()
    logger.info("running %s: %s", name, " ".join(command))
    completed = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=False)
    if completed.stdout:
        logger.info("%s stdout:\n%s", name, completed.stdout.strip())
    if completed.stderr:
        logger.warning("%s stderr:\n%s", name, completed.stderr.strip())

    status = "completed" if completed.returncode == 0 else "blocked"
    result = StepResult(
        name=name,
        command=command,
        returncode=completed.returncode,
        stdout=completed.stdout,
        stderr=completed.stderr,
        status=status,
    )

    if completed.returncode != 0 and not allow_failure:
        raise RuntimeError(f"{name} failed with exit code {completed.returncode}")
    return result


@task
def write_report(report: AgentReport) -> str:
    out = reviewed_dir(report.day) / f"{day_slug(report.day)}-exam-prep-agent-run-report.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(asdict(report), indent=2), encoding="utf-8")
    return rel(out)


@task
def final_status(day: int, step_results: list[StepResult]) -> tuple[str, str, str | None]:
    gates_path = reviewed_dir(day) / f"{day_slug(day)}-final-gates.json"
    source_path = reviewed_dir(day) / f"{day_slug(day)}-source-verification.json"

    for result in step_results:
        if result.returncode != 0:
            if result.name in {"source-url-verification", "claim-source-verification", "source-verification"}:
                return (
                    "needs-human-source-review",
                    "Resolve source URL or claim-verification items, then rerun final gates.",
                    result.name,
                )
            if result.name == "build-prompt-pack-check":
                return (
                    "blocked",
                    "Map Day topic briefs to official objectives, then rerun the agent.",
                    result.name,
                )
            if result.name in {"generate-raw-candidates", "top-up-loop"}:
                return (
                    "blocked",
                    "Resolve generation failure. Check API key, model, logs, and prompt pack.",
                    result.name,
                )
            return ("blocked", f"Resolve failed step: {result.name}.", result.name)

    if source_path.exists():
        source = json.loads(source_path.read_text(encoding="utf-8"))
        counts = source.get("status_counts") or source.get("source_trace_status_counts") or {}
        if not counts and source.get("results"):
            counts = {}
            for item in source["results"]:
                status = item.get("status", "unknown")
                counts[status] = int(counts.get(status, 0)) + 1
        unresolved = int(counts.get("needs-human-source-review", 0)) + int(counts.get("needs-source-check", 0))
        if unresolved:
            return (
                "needs-human-source-review",
                "Resolve source-verification ledger items, then rerun final gates.",
                "source-verification",
            )

    if gates_path.exists():
        gates = json.loads(gates_path.read_text(encoding="utf-8"))
        completion = gates.get("completion_status", "unknown")
        if completion == "approved":
            return ("approved", "No required next action.", None)
        return (
            completion if completion in {"blocked", "pending"} else "blocked",
            "Open the final gate report and clear the listed blockers.",
            "final-gates",
        )

    return ("reviewed-candidate", "Final gate output was not found; inspect reviewed outputs.", None)


def make_report(
    *,
    day: int,
    target: int,
    status: str,
    started: str,
    results: list[StepResult],
    next_action: str,
    blocked_step: str | None,
) -> AgentReport:
    return AgentReport(
        day=day,
        target=target,
        status=status,
        started_at_utc=started,
        finished_at_utc=utc_iso(),
        completed_steps=[result.name for result in results if result.returncode == 0],
        blocked_step=blocked_step,
        outputs=outputs_for_day(day),
        step_results=results,
        next_action=next_action,
    )


def write_report_sync(report: AgentReport) -> str:
    out = reviewed_dir(report.day) / f"{day_slug(report.day)}-exam-prep-agent-run-report.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(asdict(report), indent=2), encoding="utf-8")
    return rel(out)


def run_exam_prep_agent_local(
    *,
    day: int,
    target: int = 10,
    per_topic: int = 12,
    max_iterations: int = 3,
    generate: bool = False,
    dry_run_generation: bool = False,
    force_briefs: bool = False,
    stop_after_planning: bool = False,
) -> AgentReport:
    started = utc_iso()
    results: list[StepResult] = []

    build_briefs = [sys.executable, "scripts/pilot1_aip_c01/build_exam_prep_day.py", "--day", str(day), "--plan"]
    if force_briefs:
        build_briefs.append("--force")
    results.append(execute_command("build-topic-briefs", build_briefs))
    results.append(execute_command("map-topic-brief-objectives", [sys.executable, "scripts/pilot1_aip_c01/map_exam_prep_topic_briefs.py", "--day", str(day)]))

    results.append(
        execute_command(
            "build-prompt-pack-check",
            [sys.executable, "scripts/pilot1_aip_c01/build_exam_prep_prompts.py", "--day", str(day), "--per-topic", str(per_topic), "--check"],
            allow_failure=True,
        )
    )
    if results[-1].returncode != 0 or stop_after_planning:
        status, next_action, blocked_step = final_status.fn(day, results)
        report = make_report(
            day=day,
            target=target,
            status=status if not stop_after_planning else "planning-complete",
            started=started,
            results=results,
            blocked_step=blocked_step,
            next_action=next_action
            if not stop_after_planning
            else "Prompt readiness passed. Rerun with --dry-run-generation to write prompts, or --generate to call the LLM.",
        )
        write_report_sync(report)
        return report

    results.append(
        execute_command(
            "build-prompt-pack",
            [sys.executable, "scripts/pilot1_aip_c01/build_exam_prep_prompts.py", "--day", str(day), "--per-topic", str(per_topic)],
        )
    )

    if generate or dry_run_generation:
        generation = [sys.executable, "scripts/pilot1_aip_c01/generate_exam_prep_questions.py", "--day", str(day), "--all-topics"]
        if dry_run_generation:
            generation.append("--dry-run")
        results.append(execute_command("generate-raw-candidates", generation, allow_failure=True))
        if dry_run_generation and results[-1].returncode == 0:
            report = make_report(
                day=day,
                target=target,
                status="generation-dry-run-complete",
                started=started,
                results=results,
                blocked_step=None,
                next_action="Inspect dry-run prompt files, then rerun with --generate when ready to call the LLM.",
            )
            write_report_sync(report)
            return report
        if results[-1].returncode != 0:
            status, next_action, blocked_step = final_status.fn(day, results)
            report = make_report(
                day=day,
                target=target,
                status=status,
                started=started,
                results=results,
                blocked_step=blocked_step,
                next_action=next_action,
            )
            write_report_sync(report)
            return report

    results.append(execute_command("normalize", [sys.executable, "scripts/pilot1_aip_c01/normalize_exam_prep_questions.py", "--day", str(day)]))
    results.append(execute_command("review-cull", [sys.executable, "scripts/pilot1_aip_c01/review_exam_prep_questions.py", "--day", str(day)]))

    topup = [
        sys.executable,
        "scripts/pilot1_aip_c01/run_exam_prep_topup_loop.py",
        "--day",
        str(day),
        "--target",
        str(target),
        "--max-iterations",
        str(max_iterations),
    ]
    if dry_run_generation:
        topup.append("--dry-run")
    results.append(execute_command("top-up-loop", topup, allow_failure=True))
    if results[-1].returncode != 0:
        status, next_action, blocked_step = final_status.fn(day, results)
        report = make_report(
            day=day,
            target=target,
            status=status,
            started=started,
            results=results,
            blocked_step=blocked_step,
            next_action=next_action,
        )
        write_report_sync(report)
        return report

    results.append(execute_command("write-review-outputs", [sys.executable, "scripts/pilot1_aip_c01/write_exam_prep_review_outputs.py", "--day", str(day), "--target", str(target)]))
    results.append(execute_command("rebalance-answer-positions", [sys.executable, "scripts/pilot1_aip_c01/rebalance_exam_prep_answer_positions.py", "--day", str(day)]))
    results.append(
        execute_command(
            "source-url-verification",
            [sys.executable, "scripts/pilot1_aip_c01/verify_exam_prep_source_urls.py", "--day", str(day), "--write"],
            allow_failure=True,
        )
    )
    results.append(
        execute_command(
            "claim-source-verification",
            [sys.executable, "scripts/pilot1_aip_c01/verify_exam_prep_claims_with_sources.py", "--day", str(day), "--write"],
            allow_failure=True,
        )
    )
    results.append(
        execute_command(
            "source-review-triage",
            [sys.executable, "scripts/pilot1_aip_c01/triage_exam_prep_source_review.py", "--day", str(day), "--write"],
        )
    )
    results.append(
        execute_command(
            "source-verification",
            [sys.executable, "scripts/pilot1_aip_c01/verify_exam_prep_sources.py", "--day", str(day), "--initialize-ledger", "--write"],
            allow_failure=True,
        )
    )
    if results[-1].returncode != 0:
        status, next_action, blocked_step = final_status.fn(day, results)
        report = make_report(
            day=day,
            target=target,
            status=status,
            started=started,
            results=results,
            blocked_step=blocked_step,
            next_action=next_action,
        )
        write_report_sync(report)
        return report
    results.append(execute_command("final-gates", [sys.executable, "scripts/pilot1_aip_c01/run_exam_prep_final_gates.py", "--day", str(day), "--target", str(target)]))

    status, next_action, blocked_step = final_status.fn(day, results)
    report = make_report(
        day=day,
        target=target,
        status=status,
        started=started,
        results=results,
        blocked_step=blocked_step,
        next_action=next_action,
    )
    write_report_sync(report)
    return report


@flow(name="payil-exam-prep-agent")
def run_exam_prep_agent(
    day: int,
    target: int = 10,
    per_topic: int = 12,
    max_iterations: int = 3,
    generate: bool = False,
    dry_run_generation: bool = False,
    force_briefs: bool = False,
    stop_after_planning: bool = False,
) -> AgentReport:
    started = utc_iso()
    results: list[StepResult] = []

    build_briefs = [sys.executable, "scripts/pilot1_aip_c01/build_exam_prep_day.py", "--day", str(day), "--plan"]
    if force_briefs:
        build_briefs.append("--force")
    results.append(run_step("build-topic-briefs", build_briefs))
    results.append(run_step("map-topic-brief-objectives", [sys.executable, "scripts/pilot1_aip_c01/map_exam_prep_topic_briefs.py", "--day", str(day)]))

    results.append(
        run_step(
            "build-prompt-pack-check",
            [sys.executable, "scripts/pilot1_aip_c01/build_exam_prep_prompts.py", "--day", str(day), "--per-topic", str(per_topic), "--check"],
            allow_failure=True,
        )
    )
    if results[-1].returncode != 0 or stop_after_planning:
        status, next_action, blocked_step = final_status(day, results)
        report = AgentReport(
            day=day,
            target=target,
            status=status if not stop_after_planning else "planning-complete",
            started_at_utc=started,
            finished_at_utc=utc_iso(),
            completed_steps=[result.name for result in results if result.returncode == 0],
            blocked_step=blocked_step,
            outputs=outputs_for_day(day),
            step_results=results,
            next_action=next_action
            if not stop_after_planning
            else "Prompt readiness passed. Rerun with --dry-run-generation to write prompts, or --generate to call the LLM.",
        )
        write_report(report)
        return report

    results.append(
        run_step(
            "build-prompt-pack",
            [sys.executable, "scripts/pilot1_aip_c01/build_exam_prep_prompts.py", "--day", str(day), "--per-topic", str(per_topic)],
        )
    )

    if generate or dry_run_generation:
        generation = [sys.executable, "scripts/pilot1_aip_c01/generate_exam_prep_questions.py", "--day", str(day), "--all-topics"]
        if dry_run_generation:
            generation.append("--dry-run")
        results.append(run_step("generate-raw-candidates", generation, allow_failure=True))
        if dry_run_generation and results[-1].returncode == 0:
            report = AgentReport(
                day=day,
                target=target,
                status="generation-dry-run-complete",
                started_at_utc=started,
                finished_at_utc=utc_iso(),
                completed_steps=[result.name for result in results if result.returncode == 0],
                blocked_step=None,
                outputs=outputs_for_day(day),
                step_results=results,
                next_action="Inspect dry-run prompt files, then rerun with --generate when ready to call the LLM.",
            )
            write_report(report)
            return report
        if results[-1].returncode != 0:
            status, next_action, blocked_step = final_status(day, results)
            report = AgentReport(
                day=day,
                target=target,
                status=status,
                started_at_utc=started,
                finished_at_utc=utc_iso(),
                completed_steps=[result.name for result in results if result.returncode == 0],
                blocked_step=blocked_step,
                outputs=outputs_for_day(day),
                step_results=results,
                next_action=next_action,
            )
            write_report(report)
            return report

    results.append(run_step("normalize", [sys.executable, "scripts/pilot1_aip_c01/normalize_exam_prep_questions.py", "--day", str(day)]))
    results.append(run_step("review-cull", [sys.executable, "scripts/pilot1_aip_c01/review_exam_prep_questions.py", "--day", str(day)]))

    topup = [
        sys.executable,
        "scripts/pilot1_aip_c01/run_exam_prep_topup_loop.py",
        "--day",
        str(day),
        "--target",
        str(target),
        "--max-iterations",
        str(max_iterations),
    ]
    if dry_run_generation:
        topup.append("--dry-run")
    results.append(run_step("top-up-loop", topup, allow_failure=True))
    if results[-1].returncode != 0:
        status, next_action, blocked_step = final_status(day, results)
        report = AgentReport(
            day=day,
            target=target,
            status=status,
            started_at_utc=started,
            finished_at_utc=utc_iso(),
            completed_steps=[result.name for result in results if result.returncode == 0],
            blocked_step=blocked_step,
            outputs=outputs_for_day(day),
            step_results=results,
            next_action=next_action,
        )
        write_report(report)
        return report

    results.append(run_step("write-review-outputs", [sys.executable, "scripts/pilot1_aip_c01/write_exam_prep_review_outputs.py", "--day", str(day), "--target", str(target)]))
    results.append(run_step("rebalance-answer-positions", [sys.executable, "scripts/pilot1_aip_c01/rebalance_exam_prep_answer_positions.py", "--day", str(day)]))
    results.append(
        run_step(
            "source-url-verification",
            [sys.executable, "scripts/pilot1_aip_c01/verify_exam_prep_source_urls.py", "--day", str(day), "--write"],
            allow_failure=True,
        )
    )
    results.append(
        run_step(
            "claim-source-verification",
            [sys.executable, "scripts/pilot1_aip_c01/verify_exam_prep_claims_with_sources.py", "--day", str(day), "--write"],
            allow_failure=True,
        )
    )
    results.append(
        run_step(
            "source-review-triage",
            [sys.executable, "scripts/pilot1_aip_c01/triage_exam_prep_source_review.py", "--day", str(day), "--write"],
        )
    )
    results.append(
        run_step(
            "source-verification",
            [sys.executable, "scripts/pilot1_aip_c01/verify_exam_prep_sources.py", "--day", str(day), "--initialize-ledger", "--write"],
            allow_failure=True,
        )
    )
    if results[-1].returncode != 0:
        status, next_action, blocked_step = final_status(day, results)
        report = AgentReport(
            day=day,
            target=target,
            status=status,
            started_at_utc=started,
            finished_at_utc=utc_iso(),
            completed_steps=[result.name for result in results if result.returncode == 0],
            blocked_step=blocked_step,
            outputs=outputs_for_day(day),
            step_results=results,
            next_action=next_action,
        )
        write_report(report)
        return report
    results.append(run_step("final-gates", [sys.executable, "scripts/pilot1_aip_c01/run_exam_prep_final_gates.py", "--day", str(day), "--target", str(target)]))

    status, next_action, blocked_step = final_status(day, results)
    report = AgentReport(
        day=day,
        target=target,
        status=status,
        started_at_utc=started,
        finished_at_utc=utc_iso(),
        completed_steps=[result.name for result in results if result.returncode == 0],
        blocked_step=blocked_step,
        outputs=outputs_for_day(day),
        step_results=results,
        next_action=next_action,
    )
    write_report(report)
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--day", type=int, required=True, choices=range(1, 8))
    parser.add_argument("--target", type=int, default=10)
    parser.add_argument("--per-topic", type=int, default=12)
    parser.add_argument("--max-iterations", type=int, default=3)
    parser.add_argument("--generate", action="store_true", help="Call the LLM generation adapter. Requires OPENAI_API_KEY.")
    parser.add_argument("--dry-run-generation", action="store_true", help="Write generation prompts without calling the LLM.")
    parser.add_argument("--force-briefs", action="store_true", help="Regenerate topic briefs even if files exist.")
    parser.add_argument("--stop-after-planning", action="store_true", help="Stop after brief/prompt readiness checks.")
    parser.add_argument("--local-engine", action="store_true", help="Run the same workflow without Prefect's local API server.")
    args = parser.parse_args()

    if args.generate and args.dry_run_generation:
        parser.error("Use only one of --generate or --dry-run-generation.")
    if args.generate and not os.environ.get("OPENAI_API_KEY") and not (ROOT / ".env.local").exists():
        parser.error("OPENAI_API_KEY is not set. Use --dry-run-generation to inspect prompts.")

    runner = run_exam_prep_agent_local if args.local_engine else run_exam_prep_agent
    report = runner(
        day=args.day,
        target=args.target,
        per_topic=args.per_topic,
        max_iterations=args.max_iterations,
        generate=args.generate,
        dry_run_generation=args.dry_run_generation,
        force_briefs=args.force_briefs,
        stop_after_planning=args.stop_after_planning,
    )
    print(json.dumps({"status": report.status, "next_action": report.next_action, "outputs": report.outputs}, indent=2))
    ok_statuses = {
        "approved",
        "planning-complete",
        "generation-dry-run-complete",
        "reviewed-candidate",
        "needs-human-source-review",
    }
    return 0 if report.status in ok_statuses else 2


if __name__ == "__main__":
    raise SystemExit(main())
