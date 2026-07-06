# Source Material Inventory

This directory contains research, prior planning artifacts, and reference
inputs. Spreadsheet files are generated or manually assembled views; they are
not the sole source of truth for the curriculum.

## Current Inputs

| File | Role | Workbook sheets or scope |
|---|---|---|
| `AIP-C01_Teaching_Strategy.md` | Prior AIP-C01 curriculum and progression strategy | Dependencies, foundations, methods, assessment, and adaptation |
| `AIP-C01_Curriculum_Dependency_and_Mastery_Matrix.xlsx` | Curriculum planning view | Curriculum Matrix; Skill Coverage; Summary; Legend; Sources; Skill-Topic Map |
| `AIP-C01_Topics_Learning_Order_With_Knowledge_Type.xlsx` | Ordered topic and knowledge-type view | AIP-C01 topic learning order |
| `AIP-C01_Assessment_and_Progression_Kit.xlsx` | Assessment and learner-progression view | Curriculum and coverage views; diagnostic; scoring; learner progress; recommended start |
| `AIP-C01_Layer_0_Foundations_Mastery_Kit_FIXED.xlsx` | Layer 0 learner-management and assessment prototype | Open-first guidance; entry interpretation; learning plan; topic checks; exercises; exit assessment; remediation; progression; sources; answer keys and rubrics |
| `ai-professional-01.pdf` | Source of record for the attached AIP-C01 exam guide | Official syllabus snapshot supplied for Pilot1 rebuild |
| `ai-professional-01.extracted.md` | Searchable extracted transcript of the exam guide | Human-readable audit view with page boundaries preserved |
| `ai-professional-01.objectives.json` | Canonical machine-readable official syllabus/objective source | Official domains, tasks, Skill X.Y.Z statements, and domain weights |
| `ai-professional-01.extraction-meta.json` | Extraction provenance metadata | Source PDF SHA-256, extraction tool, generated files, and normalization notes |
| `question-generation-prompts.txt` | Attached question-generation prompt list | Candidate prompt batches for exam-prep question gathering |

## AIP-C01 Syllabus Source Contract

For future AIP-C01 work, use these files in this order:

1. `ai-professional-01.objectives.json` for official domains, tasks, skills,
   domain weights, and any syllabus/objective mapping.
2. `ai-professional-01.extracted.md` for quick human search, wording checks,
   and page-level audit.
3. `ai-professional-01.pdf` as the source of record when regenerating or
   auditing the derived files.

Do not re-extract or paraphrase the PDF for objective-tagged curriculum,
question-bank, prompt-generation, review, or remediation work unless the
derived files are being regenerated with
`scripts/pilot1_aip_c01/extract_aip_c01_exam_guide.py`.

If the source PDF changes, regenerate all derived files and verify that the
SHA-256 in `ai-professional-01.extraction-meta.json` matches the new PDF.

## Intake Notes

- These files were present and inventoried on June 15, 2026.
- The attached syllabus PDF and prompt list were copied into this directory on
  June 18, 2026.
- The exam-guide transcript, objective JSON, and extraction metadata were
  derived from `ai-professional-01.pdf` with `scripts/pilot1_aip_c01/extract_aip_c01_exam_guide.py`.
- Some workbook sheet names are abbreviated in this inventory for readability.
- The workbooks should inform the canonical Markdown curriculum model, but
  future design decisions must be recorded under `docs/`.
- Technical claims about AWS require verification against current official AWS
  sources before publication in the AIP-C01 kits.
