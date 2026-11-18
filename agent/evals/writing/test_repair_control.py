import unittest
import test_writing as fixtures
import writing as w

class RepairControlTests(unittest.TestCase):
    setUp=fixtures.LoopTests.setUp
    build=fixtures.LoopTests.build
    # Run these first against the baseline as the failing control.
    def test_final_writer_then_readonly_verification(self):
        d,b=self.build()
        self.assertEqual(w.sequence(b)[-3:], ['subtract','verify-final','judge'])
    def test_construction_sources_in_packet(self):
        d,b=self.build()
        c=w.read(w.prepare(d)['context']['path'])
        self.assertIn('construction-original',c['methods'])
    def test_architecture_not_only_word_list(self):
        self.assertTrue(hasattr(w,'architecture_metrics'))
