"""Synthetic contract tests for the Wikipedia watch-list evidence and checks.py W08.
No fixture is Alejandro prose. Run: python3 -m unittest discover -s agent/evals/writing -v
"""
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'scripts/local/voice'))
import checks
import wiki_candidate_evidence as wce

CANDIDATES = """# synthetic
# Source: https://example.invalid (oldid 111, revision 2026-01-01T00:00:00Z)

## Vocabulary candidates (from "Words to watch" boxes)
- zebrafish  [Synthetic]
- sturdy  [Synthetic]
- quokka/sturdy  [Synthetic]
- wombat/numbat  [Synthetic]
- is a marsupial of  [Synthetic]
- a sturdy/hardy role/moment  [Synthetic]
- as a quokka, I can...  [Synthetic]
- plainword (as a noun)  [Synthetic]
- refers to  [Synthetic]
- ends the  [Synthetic]
- added [coverage/citations]  [Synthetic]

## Pattern index (section headings)
- Synthetic / Heading
"""
CORPUS = "I keep a sturdy bucket and a plainword jar. The numbat story is old but the quokka is new here."


class W08Tests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='w08-')
        self.addCleanup(self.tmp.cleanup)
        d = Path(self.tmp.name)
        (d / 'raw').mkdir()
        (d / 'raw' / 'a.md').write_text(CORPUS + ' She ends')
        (d / 'raw' / 'b.md').write_text('the start of a story.')
        (d / 'excluded').mkdir()
        (d / 'excluded' / 'x.md').write_text('zebrafish zebrafish unverified authorship')
        self.cand = d / 'cand.txt'
        self.cand.write_text(CANDIDATES)
        self.evp = d / 'ev.json'
        self.raw = d / 'raw'
        self.ev = wce.build(str(self.cand), str(self.raw))
        self.evp.write_text(json.dumps(self.ev))
        self.saved = (checks.W08_EVIDENCE, checks.W08_CANDIDATES, checks.W08_CORPUS)
        checks.W08_EVIDENCE, checks.W08_CANDIDATES, checks.W08_CORPUS = str(self.evp), str(self.cand), str(self.raw)
        self.addCleanup(lambda: setattr(checks, 'W08_EVIDENCE', self.saved[0]) or setattr(checks, 'W08_CANDIDATES', self.saved[1]) or setattr(checks, 'W08_CORPUS', self.saved[2]))

    def classes(self):
        return {e['term']: e['class'] for e in self.ev['entries']}

    def row(self, text, scope='personal'):
        f = Path(self.tmp.name) / 'draft.md'
        f.write_text(text)
        _, rows = checks.run(str(f), scope)
        return next(r for r in rows if r['id'] == 'W08')

    def test_classes_zero_used_mixed_uncheckable(self):
        c = self.classes()
        self.assertEqual(c['zebrafish'], 'zero_use')
        self.assertEqual(c['sturdy'], 'used')
        self.assertEqual(c['quokka/sturdy'], 'used')
        self.assertEqual(c['wombat/numbat'], 'mixed')
        self.assertEqual(c['a sturdy/hardy role/moment'], 'uncheckable')
        self.assertEqual(c['as a quokka, I can...'], 'uncheckable')

    def test_mixed_slash_group_is_per_form(self):
        e = next(x for x in self.ev['entries'] if x['term'] == 'wombat/numbat')
        self.assertEqual(e['form_class'], {'wombat': 'zero_use', 'numbat': 'used'})
        self.assertEqual(self.row('A wombat appears.')['count'], 1)
        self.assertEqual(self.row('The numbat story is old.')['count'], 0)

    def test_zero_use_word_flagged_used_word_not(self):
        self.assertEqual(self.row('A zebrafish swims.')['count'], 1)
        self.assertEqual(self.row('A sturdy bucket and a plainword jar.')['count'], 0)

    def test_phrase_literal_flagged_slash_template_not(self):
        self.assertEqual(self.row('The cat is a marsupial of note.')['count'], 1)
        self.assertEqual(self.row('This sturdy role is a hardy moment.')['count'], 0)

    def test_phrase_matches_on_word_boundaries(self):
        self.assertEqual(self.row('She prefers to wait.')['count'], 0)
        self.assertEqual(self.row('This refers to the draft.')['count'], 1)

    def test_phrase_split_across_line_break_matches(self):
        self.assertEqual(self.row('The cat is a\nmarsupial of note.')['count'], 1)

    def test_corpus_match_cannot_span_documents(self):
        # a.md ends with "she ends" and b.md starts "the start": "ends the" never occurs inside one document
        self.assertEqual(self.classes()['ends the'], 'zero_use')

    def test_mandatory_placeholder_entries_are_evidence_only(self):
        self.assertEqual(self.classes()['added [coverage/citations]'], 'uncheckable')
        self.assertEqual(self.row('We added a table.')['count'], 0)

    def test_revision_capture_excludes_paren_and_empty_corpus_fails(self):
        self.assertEqual(self.ev['source_revision'], '2026-01-01T00:00:00Z')
        empty = Path(self.tmp.name) / 'empty'
        empty.mkdir()
        with self.assertRaises(SystemExit):
            wce.build(str(self.cand), str(empty))

    def test_excluded_dir_never_read(self):
        self.assertEqual(self.ev['corpus_files'], ['a.md', 'b.md'])
        self.assertEqual(self.classes()['zebrafish'], 'zero_use')

    def test_missing_evidence_reports_unavailable_not_clean(self):
        self.evp.unlink()
        r = self.row('A zebrafish swims.')
        self.assertEqual((r['status'], r['count']), ('unavailable', 0))
        self.assertIn('missing', r['detail'])

    def test_unreadable_evidence_reports_unavailable(self):
        self.evp.write_text('{not json')
        self.assertEqual(self.row('A zebrafish swims.')['status'], 'unavailable')

    def test_stale_candidates_or_corpus_reports_stale(self):
        self.cand.write_text(CANDIDATES + '- newword  [Synthetic]\n')
        self.assertEqual(self.row('A zebrafish swims.')['status'], 'stale')
        self.cand.write_text(CANDIDATES)
        (self.raw / 'c.md').write_text('another essay')
        self.assertEqual(self.row('A zebrafish swims.')['status'], 'stale')

    def test_advisory_in_every_scope(self):
        for scope in ('personal', 'client-candidate'):
            self.assertEqual(self.row('A zebrafish swims.', scope)['severity'], 'INFO')


if __name__ == '__main__':
    unittest.main()
