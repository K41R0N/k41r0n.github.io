"""Synthetic contract tests for the structure-review topic and essay construction routing.
Behavior tests through the runner: method selection, essay gating, fresh-critic isolation
and required construction evidence. No fixture is author prose or quality evidence.
Run: python3 -m unittest discover -s agent/evals/writing -v
"""
import unittest
import test_writing as fixtures
import writing as w

TOPICS = ['decontaminate', 'creative', 'tone', 'compliance', 'page']

class StructureReviewTests(unittest.TestCase):
    setUp = fixtures.LoopTests.setUp
    build = fixtures.LoopTests.build
    receipt = fixtures.LoopTests.receipt
    synthetic_development = fixtures.LoopTests.synthetic_development
    add = fixtures.LoopTests.add
    finish = fixtures.LoopTests.finish

    def advance(self, d, b, step):
        while w.state(d).get('next') != step:
            self.add(d, self.receipt(d, b))

    def plan(self, topics):
        return [{'topic': t, 'reason': 'Synthetic topic applicability exercises source-grounded selection.',
                 'source_ref': 'synthetic-original-review-selection'} for t in topics]

    def test_essay_brief_without_structure_review_blocks(self):
        d, b = self.build()
        b['review_plan'] = self.plan(TOPICS)
        p = self.base / 'no-structure.json'; w.write(p, b)
        with self.assertRaisesRegex(w.Block, 'structure-review'):
            w.init(self.base / 'no-structure', p)

    def test_non_essay_brief_may_omit_structure_review(self):
        d, b = self.build()
        b['format'] = 'short-post'; b['review_plan'] = self.plan(TOPICS)
        p = self.base / 'short-post.json'; w.write(p, b)
        run = self.base / 'short-post-run'; w.init(run, p)
        self.assertEqual(w.state(run)['next'], 'orient')

    def test_structure_review_is_fresh_critic_pass(self):
        d, b = self.build(); self.advance(d, b, 'structure-review')
        context = w.read(w.prepare(d)['context']['path'])
        self.assertEqual(context['role'], 'reviewer')
        self.assertEqual(context['construction_intent'], {})
        self.assertEqual(context['architecture_diagnostics'], {})
        self.assertEqual(context['revision_findings'], [])

    def test_structure_review_requires_ordered_paragraph_moves(self):
        d, b = self.build(); self.advance(d, b, 'structure-review'); r = self.receipt(d, b)
        r['paragraph_moves'][0]['paragraph_sha256'] = '0' * 64
        with self.assertRaisesRegex(w.Block, 'paragraph map'):
            self.add(d, r)

    def test_structure_review_binds_construction_method_sources(self):
        d, b = self.build(); self.advance(d, b, 'structure-review')
        required = w.required_methods('structure-review', b)
        self.assertIn('construction-original', required)
        self.assertIn('structural-audit-original', required)
        self.assertIn('transition-original', required)
        r = self.receipt(d, b)
        r['applications'] = [a for a in r['applications'] if a['source'] != 'construction-original']
        with self.assertRaisesRegex(w.Block, 'missing required'):
            self.add(d, r)

    def test_structure_review_cannot_rewrite(self):
        d, b = self.build(); self.advance(d, b, 'structure-review'); r = self.receipt(d, b)
        p = self.base / 'rewrite.md'; p.write_text(fixtures.OTHER); r['after'] = w.file_ref(p)
        with self.assertRaisesRegex(w.Block, 'reviewer diagnoses'):
            self.add(d, r)

    def test_structure_review_requires_findings_schema(self):
        d, b = self.build(); self.advance(d, b, 'structure-review'); r = self.receipt(d, b)
        del r['ranked_findings']
        with self.assertRaisesRegex(w.Block, 'review findings'):
            self.add(d, r)

    def test_full_run_with_structure_review_completes(self):
        d, b = self.build(); self.finish(d, b)
        steps = [w.read(x['path'])['step'] for x in w.read(d / 'run.json')['receipts']]
        self.assertIn('structure-review', steps)
        self.assertEqual(w.state(d)['state'], 'evidence-complete-attested')

if __name__ == '__main__':
    unittest.main()
