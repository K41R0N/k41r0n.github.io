"""Offline tests for the prospect-research check-before-recommendation gate."""
import importlib.util
import unittest
from pathlib import Path

SCRIPT = Path(__file__).with_name("check_brief.py")
spec = importlib.util.spec_from_file_location("check_brief", SCRIPT)
check_brief = importlib.util.module_from_spec(spec)
spec.loader.exec_module(check_brief)
FIXTURES = SCRIPT.parent.parent / "fixtures"


class BriefGateTests(unittest.TestCase):
    def result(self, name):
        return check_brief.inspect((FIXTURES / name).read_text(encoding="utf-8"))

    def test_complete_generic_brief_passes_format_gate(self):
        self.assertEqual(self.result("good.md")["status"], "PASS")

    def test_explicit_unknown_goal_is_valid_bounded_brief(self):
        r = self.result("missing-goal.md")
        self.assertEqual(r["status"], "PASS")
        self.assertTrue(r["recommendation_ready"])

    def test_unsupported_pain_is_flagged(self):
        r = self.result("pain-claim.md")
        self.assertIn("PR3-pain-asserted-without-validation", {i["id"] for i in r["issues"]})
        self.assertFalse(r["recommendation_ready"])

    def test_private_detail_blocks_recommendation(self):
        r = self.result("private-detail.md")
        self.assertFalse(r["recommendation_ready"])
        self.assertIn("PR4-private-detail", {i["id"] for i in r["issues"]})

    def test_tag_without_source_blocks_recommendation(self):
        r = self.result("tag-without-source.md")
        self.assertFalse(r["recommendation_ready"])
        self.assertIn("PR2-evidence-tag-without-source", {i["id"] for i in r["issues"]})

    def test_empty_required_sections_block(self):
        r = self.result("empty-sections.md")
        self.assertEqual(r["status"], "BLOCK")
        self.assertIn("PR1-missing-business-model", {i["id"] for i in r["issues"]})

    def test_ledger_row_without_source_blocks(self):
        r = self.result("ledger-row-without-source.md")
        self.assertIn("PR2-evidence-tag-without-source", {i["id"] for i in r["issues"]})

    def test_valid_hypothesis_does_not_hide_separate_pain_claim(self):
        r = self.result("unsupported-claim-next-to-valid-hypothesis.md")
        self.assertIn("PR3-pain-asserted-without-validation", {i["id"] for i in r["issues"]})

    def test_absence_statement_is_not_a_private_detail(self):
        r = self.result("no-private-detail.md")
        self.assertEqual(r["status"], "PASS")


if __name__ == "__main__":
    unittest.main()
