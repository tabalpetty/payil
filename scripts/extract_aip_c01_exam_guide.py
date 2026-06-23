#!/usr/bin/env python3
"""Create durable derived sources from the AIP-C01 exam-guide PDF.

The PDF remains the source of record. This script creates:

- a searchable normalized transcript with page boundaries;
- a machine-readable objective map for official domains, tasks, and skills;
- provenance metadata tying the derived files back to the PDF hash.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "docs/Pilot1/aip-c01/source-material"
SOURCE_PDF = SOURCE_DIR / "ai-professional-01.pdf"
TRANSCRIPT_MD = SOURCE_DIR / "ai-professional-01.extracted.md"
OBJECTIVES_JSON = SOURCE_DIR / "ai-professional-01.objectives.json"
META_JSON = SOURCE_DIR / "ai-professional-01.extraction-meta.json"

LIGATURES = {
    "\ufb00": "ff",
    "\ufb01": "fi",
    "\ufb02": "fl",
    "\ufb03": "ffi",
    "\ufb04": "ffl",
}

UNICODE_NORMALIZATIONS = {
    "\u2010": "-",
    "\u2011": "-",
    "\u2012": "-",
    "\u2013": "-",
    "\u2014": "-",
    "\u2018": "'",
    "\u2019": "'",
    "\u201c": '"',
    "\u201d": '"',
}


def normalize_text(text: str) -> str:
    for source, replacement in LIGATURES.items():
        text = text.replace(source, replacement)
    for source, replacement in UNICODE_NORMALIZATIONS.items():
        text = text.replace(source, replacement)
    return text


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def extract_pages(pdf_path: Path) -> list[dict[str, object]]:
    reader = PdfReader(str(pdf_path))
    pages: list[dict[str, object]] = []
    for index, page in enumerate(reader.pages, start=1):
        raw = page.extract_text() or ""
        pages.append(
            {
                "page_number": index,
                "text": normalize_text(raw).strip(),
            }
        )
    return pages


def render_transcript(pages: list[dict[str, object]], pdf_hash: str) -> str:
    generated = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    lines = [
        "# AIP-C01 Exam Guide Extracted Transcript",
        "",
        "## Provenance",
        "",
        f"- Source PDF: `ai-professional-01.pdf`",
        f"- Source PDF SHA-256: `{pdf_hash}`",
        "- Extraction tool: `pypdf`",
        f"- Generated UTC: `{generated}`",
        "- Normalizations: ligatures expanded; typographic quotes and dash variants normalized; page boundaries preserved.",
        "",
        "## Transcript",
        "",
    ]
    for page in pages:
        lines.extend(
            [
                f"### Page {page['page_number']}",
                "",
                "```text",
                str(page["text"]),
                "```",
                "",
            ]
        )
    return "\n".join(lines)


def clean_objective_lines(pages: list[dict[str, object]]) -> list[str]:
    text = "\n".join(str(page["text"]) for page in pages)
    outline_marker = "The exam has the following content domains and weightings:"
    outline_start = text.find(outline_marker)
    if outline_start == -1:
        raise SystemExit("Could not locate the objective outline marker in the extracted PDF text.")
    start = text.find("\nContent Domain 1:", outline_start)
    if start != -1:
        start += 1
    end = text.find("Technologies and concepts that might appear on the exam", start)
    if start == -1 or end == -1 or end <= start:
        raise SystemExit("Could not locate the objective outline in the extracted PDF text.")

    lines: list[str] = []
    for raw_line in text[start:end].splitlines():
        line = re.sub(r"\s+", " ", raw_line).strip()
        if not line:
            continue
        if line == "AWS Certified Generative AI Developer - Professional Exam Guide (AIP-C01)":
            continue
        if re.fullmatch(r"Content outline \d+", line):
            continue
        if re.fullmatch(r"Content Domain \d+: .+ \d+", line) and "(%" not in line:
            continue
        if re.fullmatch(r"Task \d+\.\d+: .+ \d+", line):
            continue
        lines.append(line)
    return lines


def join_wrapped_objective_lines(lines: list[str]) -> list[str]:
    joined: list[str] = []
    for line in lines:
        starts_new = (
            line.startswith("Content Domain ")
            or line.startswith("Task ")
            or line.startswith("• Skill ")
        )
        if starts_new or not joined:
            joined.append(line)
        else:
            previous = joined[-1]
            if previous.endswith("-"):
                joined[-1] = previous + line
            else:
                joined[-1] = previous + " " + line
    return joined


def extract_domain_weights(pages: list[dict[str, object]]) -> dict[str, int]:
    text = "\n".join(str(page["text"]) for page in pages)
    weights: dict[str, int] = {}
    for match in re.finditer(
        r"• Content Domain (\d+): .*? \((\d+)% of\s+scored content\)",
        text,
        flags=re.DOTALL,
    ):
        domain_id, weight = match.groups()
        weights[domain_id] = int(weight)
    return weights


def parse_objectives(pages: list[dict[str, object]], pdf_hash: str) -> dict[str, object]:
    objective_lines = join_wrapped_objective_lines(clean_objective_lines(pages))
    domain_weights = extract_domain_weights(pages)
    domains: list[dict[str, object]] = []
    current_domain: dict[str, object] | None = None
    current_task: dict[str, object] | None = None

    domain_re = re.compile(r"Content Domain (\d+): (.+?)(?: \((\d+)% of scored content\))?$")
    task_re = re.compile(r"Task (\d+\.\d+): (.+)$")
    skill_re = re.compile(r"• Skill (\d+\.\d+\.\d+): (.+)$")

    for line in objective_lines:
        domain_match = domain_re.match(line)
        if domain_match:
            current_task = None
            domain_id, title, weight = domain_match.groups()
            current_domain = {
                "domain_id": domain_id,
                "domain": f"Content Domain {domain_id}: {title}",
                "weight_percent": int(weight) if weight else domain_weights.get(domain_id),
                "tasks": [],
            }
            domains.append(current_domain)
            continue

        task_match = task_re.match(line)
        if task_match:
            if current_domain is None:
                raise SystemExit(f"Task found before domain: {line}")
            task_id, title = task_match.groups()
            current_task = {
                "task_id": task_id,
                "task": f"Task {task_id}: {title}",
                "skills": [],
            }
            current_domain["tasks"].append(current_task)
            continue

        skill_match = skill_re.match(line)
        if skill_match:
            if current_task is None:
                raise SystemExit(f"Skill found before task: {line}")
            skill_id, text = skill_match.groups()
            current_task["skills"].append(
                {
                    "skill_id": skill_id,
                    "skill": f"Skill {skill_id}: {text}",
                }
            )

    return {
        "exam_code": "AIP-C01",
        "source_pdf": "ai-professional-01.pdf",
        "source_pdf_sha256": pdf_hash,
        "extraction_tool": "pypdf",
        "normalizations": [
            "ligatures expanded",
            "typographic quotes normalized",
            "dash variants normalized",
            "wrapped objective lines rejoined",
            "page headers and footers removed from objective records",
        ],
        "domains": domains,
    }


def write_json(path: Path, data: dict[str, object]) -> None:
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Validate existing derived files without rewriting them.")
    args = parser.parse_args()

    if not SOURCE_PDF.exists():
        raise SystemExit(f"Missing source PDF: {SOURCE_PDF}")

    pdf_hash = sha256(SOURCE_PDF)
    pages = extract_pages(SOURCE_PDF)
    objectives = parse_objectives(pages, pdf_hash)
    transcript = render_transcript(pages, pdf_hash)
    meta = {
        "source_pdf": "ai-professional-01.pdf",
        "source_pdf_sha256": pdf_hash,
        "page_count": len(pages),
        "extraction_tool": "pypdf",
        "generated_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "derived_files": [
            "ai-professional-01.extracted.md",
            "ai-professional-01.objectives.json",
        ],
        "normalizations": objectives["normalizations"],
    }

    if args.check:
        required = [TRANSCRIPT_MD, OBJECTIVES_JSON, META_JSON]
        missing = [str(path.relative_to(ROOT)) for path in required if not path.exists()]
        errors: list[str] = []
        if not missing:
            existing_objectives = json.loads(OBJECTIVES_JSON.read_text(encoding="utf-8"))
            existing_meta = json.loads(META_JSON.read_text(encoding="utf-8"))
            existing_transcript = TRANSCRIPT_MD.read_text(encoding="utf-8")
            task_count = sum(len(domain["tasks"]) for domain in existing_objectives["domains"])
            skill_count = sum(
                len(task["skills"])
                for domain in existing_objectives["domains"]
                for task in domain["tasks"]
            )
            if existing_objectives.get("source_pdf_sha256") != pdf_hash:
                errors.append("objectives JSON source hash does not match current PDF")
            if existing_meta.get("source_pdf_sha256") != pdf_hash:
                errors.append("metadata source hash does not match current PDF")
            if pdf_hash not in existing_transcript:
                errors.append("transcript does not record current PDF hash")
            if len(existing_objectives["domains"]) != 5 or task_count != 20 or skill_count != 98:
                errors.append(
                    f"unexpected objective counts: {len(existing_objectives['domains'])} domains, "
                    f"{task_count} tasks, {skill_count} skills"
                )
        if missing or errors:
            print("Derived source check failed.")
            print(f"missing: {missing}")
            print(f"errors: {errors}")
            return 1
        print("Derived source check passed.")
        return 0

    TRANSCRIPT_MD.write_text(transcript, encoding="utf-8")
    write_json(OBJECTIVES_JSON, objectives)
    write_json(META_JSON, meta)

    task_count = sum(len(domain["tasks"]) for domain in objectives["domains"])
    skill_count = sum(
        len(task["skills"])
        for domain in objectives["domains"]
        for task in domain["tasks"]
    )
    print(f"Wrote {TRANSCRIPT_MD.relative_to(ROOT)}")
    print(f"Wrote {OBJECTIVES_JSON.relative_to(ROOT)}")
    print(f"Wrote {META_JSON.relative_to(ROOT)}")
    print(f"Extracted {len(objectives['domains'])} domains, {task_count} tasks, {skill_count} skills.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
