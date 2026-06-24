import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_script(name: str):
    path = ROOT / "scripts" / f"{name}.py"
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


gates = load_script("run_exam_prep_final_gates")
prompts = load_script("build_exam_prep_prompts")


class ExamPrepGateTests(unittest.TestCase):
    def test_single_answer_position_matches_normalized_text(self):
        item = """Options:

1. First choice.
2. Second choice.
3. Third choice.
4. Fourth choice.

Correct answer: Option 2: Second choice

Rationale: Because.
"""
        self.assertEqual(gates.correct_answer_index(item, "multiple-choice"), "2")

    def test_multiple_response_uses_format_not_answer_punctuation(self):
        item = """Options:

1. First choice.
2. Second choice.
3. Third choice.
4. Fourth choice.

Correct answer: First choice.; Third choice.

Rationale: Because.
"""
        self.assertEqual(
            gates.correct_answer_index(item, "multiple-response"),
            "multiple-response",
        )

    def test_day_two_skill_mapping_is_loaded(self):
        mapping = gates.mapped_skills_by_topic(2)
        self.assertEqual(mapping["Day02-order001"], {"1.3.1"})
        self.assertEqual(mapping["Day02-order010"], {"1.4.1", "1.5.3"})

    def test_cost_telemetry_covers_current_external_sources(self):
        bank = gates.reviewed_bank_path(2).read_text(encoding="utf-8")
        fields = [gates.parse_fields(item) for item in gates.parse_items(bank)]
        summary = gates.cost_summary(2, fields)
        self.assertTrue(summary["telemetry_complete"])
        self.assertGreaterEqual(summary["api_calls"], 12)

    def test_iteration_summary_uses_loop_events(self):
        summary = gates.iteration_summary(2)
        self.assertEqual(summary["observed_iterations"], 1)
        self.assertEqual(summary["configured_max_iterations"], 3)
        self.assertTrue(summary["within_limit"])

    def test_prompt_mappings_come_from_canonical_matrix(self):
        briefs = {brief.order: brief for brief in prompts.load_briefs(2)}
        order010_skills = {
            gates.skill_id(mapping.skill)
            for mapping in briefs["Day02-order010"].objective_mappings
        }
        self.assertEqual(order010_skills, {"1.4.1", "1.5.3"})
        self.assertNotIn("1.5.6", order010_skills)

    def test_current_bank_answer_positions_are_balanced(self):
        result = gates.run_gates(2, 10)
        self.assertEqual(
            result["answer_position_counts"],
            {"1": 23, "2": 23, "3": 23, "4": 22, "multiple-response": 27},
        )
        self.assertEqual(result["gate_status"]["distribution_gate"], "pass")


if __name__ == "__main__":
    unittest.main()
