#!/usr/bin/env python3
"""Run a grounded judge over unresolved claim/source evidence."""

from __future__ import annotations

import argparse
import json
import os
import re
from collections import Counter
from datetime import date
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[2]
EXAM_PREP = ROOT / "docs/Pilot1/aip-c01/exam-prep"
LOCAL_ENV = ROOT / ".env.local"
DEFAULT_MODEL = "gpt-4.1"
STOP_WORDS = {
    "about", "after", "again", "answer", "because", "before", "claim",
    "correct", "could", "each", "from", "have", "into", "more", "most",
    "must", "only", "option", "question", "rationale", "should", "source",
    "than", "that", "their", "then", "these", "this", "through", "when",
    "where", "which", "while", "with", "without", "would", "your",
}


def day_slug(day: int) -> str:
    return f"day-{day:02d}"


def reviewed_dir(day: int) -> Path:
    return EXAM_PREP / f"reviewed/{day_slug(day)}"


def ledger_path(day: int) -> Path:
    return reviewed_dir(day) / f"{day_slug(day)}-claim-verification-ledger.json"


def claim_report_path(day: int) -> Path:
    return reviewed_dir(day) / f"{day_slug(day)}-claim-source-verification.json"


def url_report_path(day: int) -> Path:
    return reviewed_dir(day) / f"{day_slug(day)}-source-url-verification.json"


def output_json_path(day: int) -> Path:
    return reviewed_dir(day) / f"{day_slug(day)}-grounded-claim-judge.json"


def output_md_path(day: int) -> Path:
    return reviewed_dir(day) / f"{day_slug(day)}-grounded-claim-judge-report.md"


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


def classify(source: str, evidence: str) -> str:
    lowered = (source or "").strip().lower()
    if lowered == "source_trace_needed":
        return "C"
    if lowered == "none" or not lowered:
        return "E"
    if source.startswith("https://docs.aws.amazon.com/"):
        return "A" if evidence.strip() else "D"
    if source.startswith("docs/"):
        return "B" if evidence.strip() else "F"
    return "F"


def load_url_sources(day: int) -> dict[str, str]:
    path = url_report_path(day)
    if not path.exists():
        return {}
    report = json.loads(path.read_text(encoding="utf-8"))
    sources: dict[str, str] = {}
    for result in report.get("results", []):
        if result.get("status") != "reachable" or not result.get("cache_path"):
            continue
        cache_path = ROOT / result["cache_path"]
        if cache_path.exists():
            text = cache_path.read_text(encoding="utf-8", errors="replace")
            sources[result["url"]] = text
            sources[result.get("url_without_fragment", result["url"])] = text
    return sources


def load_source_text(day: int, source: str, url_sources: dict[str, str]) -> str:
    if source.startswith("https://docs.aws.amazon.com/"):
        return url_sources.get(source) or url_sources.get(source.split("#", 1)[0], "")
    if source.startswith("docs/"):
        path = ROOT / source
        if path.exists():
            return path.read_text(encoding="utf-8", errors="replace")
    return ""


def claim_terms(claim: str) -> list[str]:
    words = re.findall(r"[A-Za-z][A-Za-z0-9-]{3,}", claim.lower())
    result: list[str] = []
    for word in words:
        word = word.strip("-")
        if word not in STOP_WORDS and word not in result:
            result.append(word)
    return result


def compact(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def source_excerpt(claim: str, source_text: str, existing_evidence: str, limit: int) -> str:
    text = compact(source_text)
    if not text:
        return compact(existing_evidence)[:limit]
    evidence = compact(existing_evidence)
    if evidence and evidence in text:
        index = text.find(evidence)
        start = max(0, index - limit // 3)
        return text[start : start + limit]
    terms = claim_terms(claim)
    lowered = text.lower()
    best_index = 0
    best_score = -1
    window = min(limit, len(text))
    step = max(500, window // 4)
    for index in range(0, max(len(text) - window + 1, 1), step):
        sample = lowered[index : index + window]
        score = sum(1 for term in terms if term in sample)
        if score > best_score:
            best_score = score
            best_index = index
    return text[best_index : best_index + limit]


def openai_responses_create(api_key: str, model: str, prompt: str, timeout: int) -> dict[str, Any]:
    payload = {
        "model": model,
        "input": [{"role": "user", "content": [{"type": "input_text", "text": prompt}]}],
    }
    request = Request(
        "https://api.openai.com/v1/responses",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
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
    return "\n\n".join(chunks) if chunks else json.dumps(response)


def parse_json_object(text: str) -> dict[str, Any]:
    cleaned = text.strip()
    cleaned = re.sub(r"^```(?:json)?", "", cleaned).strip()
    cleaned = re.sub(r"```$", "", cleaned).strip()
    match = re.search(r"\{.*\}", cleaned, flags=re.DOTALL)
    if not match:
        raise ValueError("judge response did not contain a JSON object")
    return json.loads(match.group(0))


def judge_prompt(item: dict[str, Any], claim: dict[str, Any], excerpt: str) -> str:
    return "\n".join(
        [
            "You are a strict grounded source judge for an exam-prep question bank.",
            "Decide whether the source excerpt supports the claim.",
            "",
            "Rules:",
            "- Use only the provided source excerpt.",
            "- Do not use outside knowledge.",
            "- SUPPORTED means the claim is directly supported or is a very close paraphrase.",
            "- REFUTED means the source contradicts the claim.",
            "- INSUFFICIENT means the source is relevant but does not prove the claim.",
            "- Be conservative. If the source is a blank worksheet or only teaches a method without the claimed AWS fact, choose INSUFFICIENT.",
            "- Return only compact JSON with keys: verdict, confidence, evidence_quote, reasoning, recommended_action.",
            "- verdict must be one of: supported, refuted, insufficient.",
            "- confidence must be a number from 0 to 1.",
            "",
            f"Item: {item.get('item_id')}",
            f"Learning unit: {item.get('learning_unit')}",
            f"Source: {claim.get('source')}",
            "",
            "Claim:",
            str(claim.get("claim", "")),
            "",
            "Source excerpt:",
            excerpt,
        ]
    )


def load_unresolved_items(day: int, buckets: set[str], limit: int | None) -> list[dict[str, Any]]:
    path = claim_report_path(day)
    if not path.exists():
        raise SystemExit(f"Missing claim source verification report: {path}")
    data = json.loads(path.read_text(encoding="utf-8"))
    url_sources = load_url_sources(day)
    selected: list[dict[str, Any]] = []
    for item in data.get("items", []):
        if item.get("verdict") != "unresolved":
            continue
        claims = item.get("claims", [])
        if not claims:
            continue
        claim = claims[0]
        source = str(claim.get("source", "") or "")
        evidence = str(claim.get("evidence", "") or "")
        bucket = classify(source, evidence)
        if bucket not in buckets:
            continue
        source_text = load_source_text(day, source, url_sources)
        selected.append({"item": item, "claim": claim, "bucket": bucket, "source_text": source_text})
        if limit is not None and len(selected) >= limit:
            break
    return selected


def render_report(day: int, results: list[dict[str, Any]]) -> str:
    counts = Counter(result.get("verdict", "missing") for result in results)
    lines = [
        f"# Day {day} Grounded Claim Judge Report",
        "",
        f"Generated: {date.today().isoformat()}",
        "",
        f"- Supported: {counts['supported']}",
        f"- Refuted: {counts['refuted']}",
        f"- Insufficient: {counts['insufficient']}",
        f"- Errors: {counts['error']}",
        "",
        "| Bucket | Item | Verdict | Confidence | Action | Reasoning |",
        "|---|---|---|---:|---|---|",
    ]
    for result in results:
        lines.append(
            "| {bucket} | {item_id} | {verdict} | {confidence} | {action} | {reasoning} |".format(
                bucket=result.get("bucket"),
                item_id=result.get("item_id"),
                verdict=result.get("verdict"),
                confidence=result.get("confidence", ""),
                action=str(result.get("recommended_action", "")).replace("|", "\\|"),
                reasoning=str(result.get("reasoning", "")).replace("|", "\\|"),
            )
        )
    return "\n".join(lines) + "\n"


def render_dry_run_report(day: int, prompts: list[dict[str, str]]) -> str:
    lines = [
        f"# Day {day} Grounded Claim Judge Dry Run",
        "",
        f"Generated: {date.today().isoformat()}",
        "",
        f"- Judge prompts prepared: {len(prompts)}",
        "- No model call was made.",
        "- No claim ledger changes were applied.",
        "",
        "| Bucket | Item | Prompt characters |",
        "|---|---|---:|",
    ]
    for prompt in prompts:
        lines.append(
            f"| {prompt.get('bucket')} | {prompt.get('item_id')} | {len(prompt.get('prompt', ''))} |"
        )
    return "\n".join(lines) + "\n"


def apply_supported(day: int, results: list[dict[str, Any]], min_confidence: float) -> int:
    path = ledger_path(day)
    ledger = json.loads(path.read_text(encoding="utf-8"))
    by_id = {result["item_id"]: result for result in results}
    applied = 0
    for item in ledger.get("items", []):
        result = by_id.get(item.get("item_id"))
        if not result:
            continue
        if result.get("verdict") != "supported" or float(result.get("confidence", 0)) < min_confidence:
            continue
        for claim in item.get("claims", []):
            claim["verdict"] = "supported"
            claim["evidence"] = result.get("evidence_quote", "")
            claim["verification_method"] = "grounded LLM source judge"
            claim["verification_note"] = result.get("reasoning", "")
            claim["judge_confidence"] = result.get("confidence")
        item["verdict"] = "verified"
        applied += 1
    ledger["status"] = "verified" if all(item.get("verdict") == "verified" for item in ledger.get("items", [])) else "in-progress"
    ledger["last_grounded_claim_judge"] = date.today().isoformat()
    path.write_text(json.dumps(ledger, indent=2) + "\n", encoding="utf-8")
    return applied


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--day", type=int, required=True, choices=range(1, 8))
    parser.add_argument("--buckets", nargs="+", default=["A"], choices=["A", "B", "C", "D", "E", "F"])
    parser.add_argument("--limit", type=int)
    parser.add_argument("--model", default=os.environ.get("OPENAI_MODEL", DEFAULT_MODEL))
    parser.add_argument("--timeout", type=int, default=60)
    parser.add_argument("--excerpt-chars", type=int, default=12000)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--apply-supported", action="store_true")
    parser.add_argument("--min-confidence", type=float, default=0.92)
    args = parser.parse_args()

    selected = load_unresolved_items(args.day, set(args.buckets), args.limit)
    api_key = env_value("OPENAI_API_KEY")
    if not args.dry_run and not api_key:
        raise SystemExit("OPENAI_API_KEY is not set. Use --dry-run to inspect judge prompts.")

    results: list[dict[str, Any]] = []
    prompts: list[dict[str, str]] = []
    for record in selected:
        item = record["item"]
        claim = record["claim"]
        excerpt = source_excerpt(
            str(claim.get("claim", "")),
            record["source_text"],
            str(claim.get("evidence", "")),
            args.excerpt_chars,
        )
        prompt = judge_prompt(item, claim, excerpt)
        if args.dry_run:
            prompts.append({"item_id": item.get("item_id", ""), "bucket": record["bucket"], "prompt": prompt})
            continue
        try:
            response = openai_responses_create(api_key or "", args.model, prompt, args.timeout)
            parsed = parse_json_object(extract_output_text(response))
            verdict = str(parsed.get("verdict", "")).lower()
            if verdict not in {"supported", "refuted", "insufficient"}:
                verdict = "error"
            result = {
                "item_id": item.get("item_id"),
                "learning_unit": item.get("learning_unit"),
                "bucket": record["bucket"],
                "source": claim.get("source"),
                "verdict": verdict,
                "confidence": parsed.get("confidence", 0),
                "evidence_quote": parsed.get("evidence_quote", ""),
                "reasoning": parsed.get("reasoning", ""),
                "recommended_action": parsed.get("recommended_action", ""),
            }
        except (json.JSONDecodeError, ValueError) as exc:
            result = {
                "item_id": item.get("item_id"),
                "learning_unit": item.get("learning_unit"),
                "bucket": record["bucket"],
                "source": claim.get("source"),
                "verdict": "error",
                "confidence": 0,
                "evidence_quote": "",
                "reasoning": str(exc),
                "recommended_action": "rerun judge or send to human review",
            }
        results.append(result)

    output = {
        "day": args.day,
        "generated": date.today().isoformat(),
        "model": args.model,
        "buckets": args.buckets,
        "dry_run": args.dry_run,
        "results": results,
        "prompts": prompts if args.dry_run else [],
    }
    if args.write:
        output_json_path(args.day).write_text(json.dumps(output, indent=2), encoding="utf-8")
        report = render_dry_run_report(args.day, prompts) if args.dry_run else render_report(args.day, results)
        output_md_path(args.day).write_text(report, encoding="utf-8")
    applied = 0
    if args.apply_supported:
        applied = apply_supported(args.day, results, args.min_confidence)

    counts = Counter(result.get("verdict", "prompt") for result in results)
    if args.dry_run:
        print(f"dry_run_prompts={len(prompts)}")
    else:
        print(
            f"supported={counts['supported']} refuted={counts['refuted']} "
            f"insufficient={counts['insufficient']} errors={counts['error']} applied={applied}"
        )
    if args.write:
        print(f"report={output_md_path(args.day).relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
