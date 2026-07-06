#!/usr/bin/env python3
"""Fetch and verify official AWS documentation URLs used by exam-prep items."""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import date
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
EXAM_PREP = ROOT / "docs/Pilot1/aip-c01/exam-prep"
AWS_URL_RE = re.compile(r"https://docs\.aws\.amazon\.com/[^\s`<>),;]+")


def day_slug(day: int) -> str:
    return f"day-{day:02d}"


def reviewed_dir(day: int) -> Path:
    return EXAM_PREP / f"reviewed/{day_slug(day)}"


def bank_path(day: int) -> Path:
    return reviewed_dir(day) / f"{day_slug(day)}-reviewed-question-bank.md"


def ledger_path(day: int) -> Path:
    return reviewed_dir(day) / f"{day_slug(day)}-claim-verification-ledger.json"


def cache_dir(day: int) -> Path:
    return reviewed_dir(day) / "source-cache"


def report_json_path(day: int) -> Path:
    return reviewed_dir(day) / f"{day_slug(day)}-source-url-verification.json"


def report_md_path(day: int) -> Path:
    return reviewed_dir(day) / f"{day_slug(day)}-source-url-verification-report.md"


def url_cache_name(url: str) -> str:
    parsed = urllib.parse.urlsplit(url)
    no_fragment = urllib.parse.urlunsplit((parsed.scheme, parsed.netloc, parsed.path, parsed.query, ""))
    digest = hashlib.sha256(no_fragment.encode("utf-8")).hexdigest()[:16]
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", parsed.path.strip("/")).strip("-")[:80]
    return f"{slug or 'aws-doc'}-{digest}.txt"


def extract_urls(day: int) -> list[str]:
    texts = []
    if bank_path(day).exists():
        texts.append(bank_path(day).read_text(encoding="utf-8"))
    if ledger_path(day).exists():
        texts.append(ledger_path(day).read_text(encoding="utf-8"))
    urls = set()
    for text in texts:
        for match in AWS_URL_RE.finditer(text):
            urls.add(clean_url(match.group(0)))
    return sorted(urls)


def clean_url(url: str) -> str:
    return url.strip().rstrip(".,);]}\"'")


def html_to_text(raw: bytes, content_type: str) -> str:
    text = raw.decode("utf-8", errors="replace")
    if "html" not in content_type.lower() and "<html" not in text[:500].lower():
        return text
    text = re.sub(r"(?is)<(script|style|noscript).*?</\1>", " ", text)
    text = re.sub(r"(?is)<[^>]+>", " ", text)
    text = html.unescape(text)
    return re.sub(r"\s+", " ", text).strip()


def anchor_exists(raw_text: str, fragment: str) -> bool | None:
    if not fragment:
        return None
    needle = urllib.parse.unquote(fragment)
    patterns = [
        rf'id=["\']{re.escape(needle)}["\']',
        rf'name=["\']{re.escape(needle)}["\']',
        re.escape(needle),
    ]
    return any(re.search(pattern, raw_text, flags=re.IGNORECASE) for pattern in patterns)


def fetch_url(url: str, *, timeout: int, use_cache: bool, day: int) -> dict[str, Any]:
    parsed = urllib.parse.urlsplit(url)
    no_fragment = urllib.parse.urlunsplit((parsed.scheme, parsed.netloc, parsed.path, parsed.query, ""))
    out = cache_dir(day) / url_cache_name(url)
    if use_cache and out.exists():
        cached = out.read_text(encoding="utf-8", errors="replace")
        return {
            "url": url,
            "url_without_fragment": no_fragment,
            "status": "reachable",
            "http_status": "cached",
            "final_url": no_fragment,
            "cache_path": str(out.relative_to(ROOT)),
            "text_length": len(cached),
            "fragment": parsed.fragment,
            "fragment_found": None if not parsed.fragment else "not-checked-from-cache",
            "error": "",
        }

    request = urllib.request.Request(
        no_fragment,
        headers={
            "User-Agent": "payil-aip-c01-source-verifier/1.0",
            "Accept": "text/html,text/plain,application/xhtml+xml",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            raw = response.read()
            final_url = response.geturl()
            http_status = getattr(response, "status", 200)
            content_type = response.headers.get("content-type", "")
    except urllib.error.HTTPError as exc:
        return {
            "url": url,
            "url_without_fragment": no_fragment,
            "status": "unreachable",
            "http_status": exc.code,
            "final_url": no_fragment,
            "cache_path": "",
            "text_length": 0,
            "fragment": parsed.fragment,
            "fragment_found": None,
            "error": str(exc),
        }
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        return {
            "url": url,
            "url_without_fragment": no_fragment,
            "status": "unreachable",
            "http_status": "",
            "final_url": no_fragment,
            "cache_path": "",
            "text_length": 0,
            "fragment": parsed.fragment,
            "fragment_found": None,
            "error": str(exc),
        }

    raw_text = raw.decode("utf-8", errors="replace")
    text = html_to_text(raw, content_type)
    cache_dir(day).mkdir(parents=True, exist_ok=True)
    out.write_text(text + "\n", encoding="utf-8")
    final_host = urllib.parse.urlsplit(final_url).netloc
    status = "reachable" if http_status < 400 and final_host.endswith("amazon.com") else "unreachable"
    return {
        "url": url,
        "url_without_fragment": no_fragment,
        "status": status,
        "http_status": http_status,
        "final_url": final_url,
        "cache_path": str(out.relative_to(ROOT)),
        "text_length": len(text),
        "fragment": parsed.fragment,
        "fragment_found": anchor_exists(raw_text, parsed.fragment),
        "error": "" if status == "reachable" else f"unexpected final host/status: {final_host}/{http_status}",
    }


def render_report(day: int, results: list[dict[str, Any]]) -> str:
    reachable = sum(1 for result in results if result["status"] == "reachable")
    lines = [
        f"# Day {day} Source URL Verification Report",
        "",
        f"Generated: {date.today().isoformat()}",
        "",
        f"- URLs checked: {len(results)}",
        f"- Reachable: {reachable}",
        f"- Needs review: {len(results) - reachable}",
        "",
        "| Status | HTTP | URL | Cache | Error |",
        "|---|---:|---|---|---|",
    ]
    for result in results:
        lines.append(
            "| {status} | {http_status} | {url} | {cache_path} | {error} |".format(
                status=result["status"],
                http_status=result["http_status"],
                url=result["url"],
                cache_path=result["cache_path"] or "",
                error=str(result["error"]).replace("|", "\\|"),
            )
        )
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--day", type=int, required=True, choices=range(1, 8))
    parser.add_argument("--write", action="store_true", help="Write report files and source cache.")
    parser.add_argument("--timeout", type=int, default=20)
    parser.add_argument("--sleep", type=float, default=0.1, help="Delay between network requests.")
    parser.add_argument("--no-cache", action="store_true", help="Refetch even when cached text exists.")
    args = parser.parse_args()

    urls = extract_urls(args.day)
    results = []
    for index, url in enumerate(urls, start=1):
        result = fetch_url(url, timeout=args.timeout, use_cache=not args.no_cache, day=args.day)
        results.append(result)
        print(f"[{index}/{len(urls)}] {result['status']} {url}")
        if args.sleep and index < len(urls):
            time.sleep(args.sleep)

    payload = {
        "day": args.day,
        "generated": date.today().isoformat(),
        "results": results,
        "status_counts": dict(sorted({status: sum(1 for r in results if r["status"] == status) for status in {r["status"] for r in results}}.items())),
    }
    if args.write:
        reviewed_dir(args.day).mkdir(parents=True, exist_ok=True)
        report_json_path(args.day).write_text(json.dumps(payload, indent=2), encoding="utf-8")
        report_md_path(args.day).write_text(render_report(args.day, results), encoding="utf-8")

    unresolved = sum(1 for result in results if result["status"] != "reachable")
    print(f"urls={len(results)} reachable={len(results) - unresolved} needs_review={unresolved}")
    if args.write:
        print(f"report={report_md_path(args.day).relative_to(ROOT)}")
    return 0 if unresolved == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
