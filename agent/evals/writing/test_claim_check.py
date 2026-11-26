"""Synthetic contract tests for scripts/local/claim_check.py. No fixture is
owner prose, gold or calibration.
Run: python3 -m unittest discover -s agent/evals/writing -v
"""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'scripts/local'))
sys.path.insert(0, str(Path(__file__).resolve().parent))

import writing as w
import claim_check as cc
import test_writing as _tw


def _helpers():
    return _tw.LoopTests(methodName='run')


class ClaimCheckTests(unittest.TestCase):
    def setUp(self):
        self.h = _helpers()
        self.h.setUp()

    def tearDown(self):
        self.h.tearDown()

    def build(self, *a, **k):
        return self.h.build(*a, **k)

    def receipt(self, *a, **k):
        return self.h.receipt(*a, **k)

    def add(self, *a, **k):
        return self.h.add(*a, **k)

    def finish(self, *a, **k):
        return self.h.finish(*a, **k)

    def verify(self, d, claims=(), complete=False):
        return cc.verify(d, list(claims), complete)

    def test_claimed_step_with_recorded_receipt_passes(self):
        d, b = self.build(mode='review')
        self.add(d, self.receipt(d, b))  # orient
        res = self.verify(d, ['orient'])
        self.assertEqual(len(res), 1)
        self.assertTrue(res[0][0], res)

    def test_unrecorded_step_fails(self):
        d, b = self.build(mode='review')
        self.add(d, self.receipt(d, b))  # orient only
        res = self.verify(d, ['judge'])
        self.assertFalse(res[0][0])
        self.assertIn('no recorded passing receipt', res[0][2])

    def test_claimed_step_outside_plan_fails(self):
        d, b = self.build(mode='review')
        res = self.verify(d, ['publish'])
        self.assertFalse(res[0][0])
        self.assertIn('not a step this brief plans', res[0][2])

    def test_complete_claim_on_finished_run_passes(self):
        d, b = self.build(mode='review')
        self.finish(d, b)
        res = self.verify(d, complete=True)
        self.assertTrue(res[0][0], res)
        self.assertIn('uncalibrated', res[0][2])

    def test_complete_claim_on_partial_run_fails_with_next_step(self):
        d, b = self.build(mode='review')
        self.add(d, self.receipt(d, b))
        res = self.verify(d, complete=True)
        self.assertFalse(res[0][0])
        self.assertIn('steps recorded', res[0][2])

    def test_tampered_receipt_fails_closed(self):
        d, b = self.build(mode='review')
        self.add(d, self.receipt(d, b))
        _, s, _ = w.load(d)
        receipt_path = Path(s['receipts'][0]['path'])
        r = json.loads(receipt_path.read_text())
        r['rationale'] = 'Tampered after recording.'
        receipt_path.write_text(json.dumps(r, indent=2) + '\n')
        res = self.verify(d, ['orient'], complete=True)
        self.assertTrue(all(not ok for ok, _l, _r in res))
        self.assertTrue(any('unreadable or tampered' in reason for _o, _l, reason in res))

    def test_tampered_brief_fails_closed(self):
        d, b = self.build(mode='review')
        self.add(d, self.receipt(d, b))
        bp = d / 'brief.json'
        brief = json.loads(bp.read_text())
        brief['objective'] = 'Tampered objective.'
        bp.write_text(json.dumps(brief, indent=2) + '\n')
        res = self.verify(d, ['orient'])
        self.assertFalse(res[0][0])
        self.assertIn('unreadable or tampered', res[0][2])

    def test_cli_exit_codes(self):
        d, b = self.build(mode='review')
        self.add(d, self.receipt(d, b))
        self.assertEqual(cc.main(['claim_check.py', str(d), '--claim', 'orient']), 0)
        self.assertEqual(cc.main(['claim_check.py', str(d), '--claim', 'judge']), 1)
        self.assertEqual(cc.main(['claim_check.py', str(d)]), 64)


if __name__ == '__main__':
    unittest.main()
