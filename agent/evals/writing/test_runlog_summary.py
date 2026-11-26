"""Synthetic tests for scripts/local/runlog_summary.py. Fixture-free.
Run: python3 -m unittest discover -s agent/evals/writing -v
"""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'scripts/local'))

import runlog_summary as rs

TABLE = """# Run log

| Run | Date | Deliverable | Surface | Outcome | Edit distance | Cause | His minutes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| wr-0000 | 2026-10-28 | alpha | site | rejected | heavy | slop / generic -> RULE | 9 |
| wr-0001 | 2026-10-29 | beta | site | accepted-minor-edits | light | - | 6 |
| wr-0002 | 2026-10-29 | gamma | dom | not recorded | - | - | - |
| wr-0003 | 2026-10-30 | delta | dom | pending | - | - | - |
"""


class DeriveTests(unittest.TestCase):
    def setUp(self):
        self.rows = rs.parse_rows(TABLE)
        self.d = rs.derive(self.rows)

    def test_parses_rows_and_orders_by_run_id(self):
        self.assertEqual([r['run'] for r in self.rows], ['wr-0000', 'wr-0001', 'wr-0002', 'wr-0003'])

    def test_only_ruled_outcomes_count(self):
        self.assertEqual(self.d['ruled'], 2)
        self.assertEqual(self.d['accepted'], 1)

    def test_unruled_rows_are_listed_never_counted(self):
        self.assertEqual(sorted(self.d['unruled']), ['wr-0002', 'wr-0003'])

    def test_streak_counts_trailing_accepted(self):
        self.assertEqual(self.d['streak'], 1)

    def test_streak_breaks_on_rejection(self):
        d = rs.derive(rs.parse_rows(TABLE.replace('accepted-minor-edits', 'rejected')))
        self.assertEqual(d['streak'], 0)

    def test_cause_histogram_keys_leading_term(self):
        self.assertEqual(self.d['hist'], {'slop': 1})


class CheckTests(unittest.TestCase):
    FILE = TABLE + """
## Rolling summary

    runs ruled: 2
    acceptance rate: 50% (1 of 2)
    gate streak (accepted with at most minor edits, trailing): 1
    cause histogram (ruled, not accepted): slop 1
    unruled runs (never counted): wr-0002, wr-0003
"""

    def test_check_passes_when_summary_matches_rows(self):
        out = rs.check(self.FILE, rs.derive(rs.parse_rows(TABLE)))
        self.assertTrue(all(l.startswith('PASS') for l in out), out)

    def test_check_fails_when_summary_is_stale(self):
        stale = self.FILE.replace('acceptance rate: 50%', 'acceptance rate: 0%')
        out = rs.check(stale, rs.derive(rs.parse_rows(TABLE)))
        self.assertTrue(any('acceptance rate' in l and l.startswith('FAIL') for l in out), out)

    def test_check_fails_when_block_missing(self):
        out = rs.check(TABLE, rs.derive(rs.parse_rows(TABLE)))
        self.assertTrue(any(l.startswith('FAIL') for l in out), out)


if __name__ == '__main__':
    unittest.main()
