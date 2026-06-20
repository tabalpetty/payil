# Scripts

Utility scripts for maintaining and generating Pilot1 artifacts.

## Day 1 Question Generation

Use `generate_day01_questions.py` to send the Day 1 question-generation prompt
pack to the OpenAI API and save the raw response.

Required environment:

```bash
export OPENAI_API_KEY="..."
```

Optional environment:

```bash
export OPENAI_MODEL="gpt-4.1"
```

Examples:

```bash
# Save the exact prompt that would be sent, without calling the API.
python3 scripts/generate_day01_questions.py --batch balanced --dry-run

# Generate the full 100-question Day 1 draft pool.
python3 scripts/generate_day01_questions.py --batch balanced

# Generate smaller batches if the model struggles with 100 items at once.
python3 scripts/generate_day01_questions.py --batch foundations
python3 scripts/generate_day01_questions.py --batch system-map
python3 scripts/generate_day01_questions.py --batch applied-foundations

# Generate exactly one topic-level prompt, 10 questions.
python3 scripts/generate_day01_questions.py --topic Day01-order001

# Generate all ten Day 1 topic-level prompts sequentially, 10 questions each.
python3 scripts/generate_day01_questions.py --all-topics
```

Raw responses are written to:

```text
docs/Pilot1/aip-c01/exam-prep/raw/day-01/
```

Raw responses are not approved question-bank items. Normalize and review them
under:

```text
docs/Pilot1/aip-c01/exam-prep/reviewed/day-01/
```
