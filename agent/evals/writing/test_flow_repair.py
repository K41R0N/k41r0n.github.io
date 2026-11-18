import copy
import hashlib
from pathlib import Path
import unittest
import test_writing as fixtures
import writing as w

class RepairTests(unittest.TestCase):
    setUp=fixtures.LoopTests.setUp
    build=fixtures.LoopTests.build
    receipt=fixtures.LoopTests.receipt
    synthetic_development=fixtures.LoopTests.synthetic_development
    add=fixtures.LoopTests.add
    finish=fixtures.LoopTests.finish

    def advance(self,d,b,step):
        while w.state(d).get('next')!=step:self.add(d,self.receipt(d,b))
    def test_final_verifier_is_not_a_selectable_core_topic(self):
        d,b=self.build();b['review_plan'][0]['topic']='verify-final'
        p=self.base/'bad-final-plan.json';w.write(p,b)
        with self.assertRaisesRegex(w.Block,'topic selection'):w.init(self.base/'bad-final-plan',p)
    def test_forward_intent_cannot_be_skipped(self):
        d,b=self.build();r=self.receipt(d,b);del r['construction_intent']
        with self.assertRaisesRegex(w.Block,'forward construction'):self.add(d,r)
    def test_located_not_fully_read_original_blocks(self):
        d,b=self.build();b['private_methods']['construction-original']['read_status']='located'
        p=self.base/'unread.json';w.write(p,b)
        with self.assertRaisesRegex(w.Block,'not included/read'):w.init(self.base/'unread',p)
    def test_original_wrong_hash_blocks(self):
        d,b=self.build();b['private_methods']['construction-original']['sha256']='0'*64
        p=self.base/'stale.json';w.write(p,b)
        with self.assertRaisesRegex(w.Block,'stale'):w.init(self.base/'stale',p)
    def test_missing_original_scope_boundary_blocks(self):
        d,b=self.build();del b['private_methods']['construction-original']['scope_boundary']
        p=self.base/'scope.json';w.write(p,b)
        with self.assertRaisesRegex(w.Block,'provenance incomplete'):w.init(self.base/'scope',p)
    def test_full_sources_loaded_at_construction_and_final_stages(self):
        d,b=self.build(mode='new')
        for stage,sid in [('big-idea','construction-original'),('structure','transition-original'),('subtract','structural-audit-original'),('verify-final','review-protocol-original')]:
            self.advance(d,b,stage);c=w.read(w.prepare(d)['context']['path'])
            self.assertEqual(c['methods'][sid],Path(b['private_methods'][sid]['path']).read_text())
    def test_missing_current_construction_blocks(self):
        d,b=self.build(mode='new');self.advance(d,b,'structure');r=self.receipt(d,b);del r['construction']
        with self.assertRaisesRegex(w.Block,'construction plan'):self.add(d,r)
    def test_stale_paragraph_map_blocks_final(self):
        d,b=self.build();self.advance(d,b,'verify-final');r=self.receipt(d,b)
        r['paragraph_moves'][0]['paragraph_sha256']='0'*64
        with self.assertRaisesRegex(w.Block,'paragraph map'):self.add(d,r)
    def test_stale_subtraction_counters_block(self):
        d,b=self.build();self.advance(d,b,'subtract');r=self.receipt(d,b);r['subtraction']['before']['words']+=1
        with self.assertRaisesRegex(w.Block,'counters'):self.add(d,r)
    def test_subtraction_requires_preservation_and_both_verdicts(self):
        for key in ['preservation','pattern_verdict','repeat_verdict']:
            d,b=self.build();self.advance(d,b,'subtract');r=self.receipt(d,b);del r['subtraction'][key]
            with self.assertRaisesRegex(w.Block,'subtraction missing'):self.add(d,r)
    def test_final_verifier_cannot_rewrite(self):
        d,b=self.build();self.advance(d,b,'verify-final');r=self.receipt(d,b)
        p=self.base/'rewrite.md';p.write_text(fixtures.OTHER);r['after']=w.file_ref(p)
        with self.assertRaisesRegex(w.Block,'reviewer diagnoses'):self.add(d,r)
    def test_final_verifier_requires_knock_on_read(self):
        d,b=self.build();self.advance(d,b,'verify-final');r=self.receipt(d,b);del r['knock_on_read']
        with self.assertRaisesRegex(w.Block,'knock_on_read'):self.add(d,r)
    def test_revision_reopens_subtraction_and_verification(self):
        d,b=self.build();self.finish(d,b)
        replacement=self.base/'replacement.md';replacement.write_text(fixtures.OTHER)
        w.revise(d,replacement,'Synthetic revision invalidates final evidence after changed content.')
        self.assertEqual(w.state(d)['next'],'orient')
        self.assertEqual(w.read(d/'run.json')['receipts'],[])
        self.assertIn('subtract',w.sequence(b));self.assertIn('verify-final',w.sequence(b))
    def test_writer_receives_findings_but_fresh_critic_does_not(self):
        d,b=self.build();self.advance(d,b,'decontaminate');r=self.receipt(d,b)
        _,s,_=w.load(d);sid='method:anti-patterns';src=Path(s['snapshot'][sid]['path']).read_text()
        clause=next(x for x in src.splitlines() if len(x)>40)[:80]
        finding={'materiality':'material','draft_quote':fixtures.TEXT[:60],'reason':'Synthetic reviewer names the upstream procedural cause.','source':sid,'source_clause':clause}
        r['decision']='fail';r['ranked_findings']=[finding];r['adjudications']=[{'finding_index':0,'materiality':'material','decision':'reject','counterevidence':'Synthetic exact source and seed justify rejection of this finding.','reason':'Synthetic preservation reason keeps the original instruction.','seed_preservation':'Synthetic authentic seed remains unchanged for inspection.','source':sid,'source_clause':clause}]
        with self.assertRaisesRegex(w.Block,'failed; revise'):self.add(d,r)
        w.revise(d,b['artifact'],'Synthetic revision must receive exact ranked finding, not summary.')
        c=w.read(w.prepare(d)['context']['path']);self.assertEqual(c['revision_findings'][0]['findings'],[finding])
        rr=self.receipt(d,b);del rr['revision_findings_seen']
        with self.assertRaisesRegex(w.Block,'actual revision findings'):self.add(d,rr)
        self.add(d,self.receipt(d,b));c=w.read(w.prepare(d)['context']['path'])
        self.assertEqual(c['revision_findings'],[])
    def test_architecture_counts_do_not_impose_personal_budgets(self):
        t='Notice what happens. It is not a valve but a pump.\n\nA, B and C happen.'
        m=w.architecture_metrics(t);self.assertGreater(m['meta_candidates'],0);self.assertGreater(m['contrast_candidates'],0)
        self.assertNotIn('quality_pass',m);self.assertNotIn('FAIL',str(m))

    def test_passing_review_cannot_hide_findings(self):
        d,b=self.build();self.advance(d,b,'decontaminate');r=self.receipt(d,b)
        r['ranked_findings']=[{}]
        with self.assertRaisesRegex(w.Block,'exactly one adjudication'):self.add(d,r)
    def test_empty_adjudication_is_rejected(self):
        d,b=self.build();self.advance(d,b,'decontaminate');r=self.receipt(d,b)
        r.update(decision='fail',ranked_findings=[{}],adjudications=[{}])
        with self.assertRaisesRegex(w.Block,'finding index'):self.add(d,r)
    def test_unbound_adjudication_source_is_rejected(self):
        d,b=self.build();self.advance(d,b,'decontaminate');r=self.receipt(d,b)
        r.update(decision='fail',ranked_findings=[{}],adjudications=[{'finding_index':0,'decision':'repair','reason':'Synthetic rationale for a specific reviewer finding.','seed_preservation':'Synthetic author seed remains preserved unchanged.','source':'input:notes:0','source_clause':fixtures.TEXT[:60]}])
        with self.assertRaisesRegex(w.Block,'adjudication method'):self.add(d,r)
    def test_fresh_critic_not_anchored_to_writer_intent_or_metrics(self):
        d,b=self.build();self.add(d,self.receipt(d,b))
        c=w.read(w.prepare(d)['context']['path'])
        self.assertEqual(c['construction_intent'],{});self.assertEqual(c['architecture_diagnostics'],{})
    def test_subtraction_receives_diagnostics_only_at_its_stage(self):
        d,b=self.build();self.advance(d,b,'subtract');c=w.read(w.prepare(d)['context']['path'])
        self.assertEqual(c['architecture_diagnostics'],w.architecture_metrics(fixtures.TEXT))
    def test_literal_metric_fixture_independent_expected_values(self):
        m=w.architecture_metrics('Notice what moves. It is not a tap but a pump.\n\nOne, two and three work.')
        self.assertEqual(m['words'],16);self.assertEqual(m['paragraphs'],2)
        self.assertEqual(m['meta_candidates'],1);self.assertEqual(m['contrast_candidates'],1)
        self.assertEqual(m['questions'],0);self.assertEqual(m['one_sentence_paragraphs'],1)

    def finding_receipt(self,d,b,materiality='advisory',decision='repair'):
        self.advance(d,b,'decontaminate');r=self.receipt(d,b);_,s,_=w.load(d)
        sid='method:anti-patterns';src=Path(s['snapshot'][sid]['path']).read_text();clause=next(x for x in src.splitlines() if len(x)>40)[:80]
        r['ranked_findings']=[{'materiality':materiality,'draft_quote':fixtures.TEXT[:60],'reason':'Synthetic reviewer finding for explicit disposition testing.','source':sid,'source_clause':clause}]
        r['adjudications']=[{'finding_index':0,'materiality':materiality,'decision':decision,'reason':'Synthetic explicit disposition preserves a bounded concern.','seed_preservation':'Synthetic author seed stays unchanged throughout this decision.','source':sid,'source_clause':clause,'counterevidence':'Synthetic counterevidence supports rejection without relabeling.','owner':'Synthetic task coordinator','destination':'Private retained final review record for coordinator follow-up'}]
        return r
    def test_advisory_pass_retained_without_forced_revision(self):
        d,b=self.build();r=self.finding_receipt(d,b);self.add(d,r);self.finish(d,b)
        _,s,_=w.load(d);records=w.retained_findings(s)
        self.assertEqual(records[0]['findings'],r['ranked_findings']);self.assertEqual(s['round'],1)
        from unittest.mock import patch
        with patch.object(w,'state',return_value={'state':'process-complete'}):
            result=w.packet(d,self.base/'synthetic-private-packet.json')
        self.assertEqual(result['retained_review_findings'],records)
        self.assertNotIn('predicted_edits',str(records))
    def test_material_rejection_pass_retained_with_counterevidence(self):
        d,b=self.build();r=self.finding_receipt(d,b,'material','reject');self.add(d,r);self.finish(d,b)
        _,s,_=w.load(d);self.assertEqual(w.retained_findings(s)[0]['adjudications'],r['adjudications'])
    def test_accepted_material_cannot_pass(self):
        d,b=self.build();r=self.finding_receipt(d,b,'material','repair')
        with self.assertRaisesRegex(w.Block,'material repair blocks'):self.add(d,r)
    def test_material_cannot_be_downgraded_in_adjudication(self):
        d,b=self.build();r=self.finding_receipt(d,b,'material','repair');r['adjudications'][0]['materiality']='advisory'
        with self.assertRaisesRegex(w.Block,'cannot downgrade'):self.add(d,r)
    def test_material_defer_cannot_pass_and_needs_owner(self):
        d,b=self.build();r=self.finding_receipt(d,b,'material','defer');del r['adjudications'][0]['owner']
        with self.assertRaisesRegex(w.Block,'owner and destination'):self.add(d,r)
        r['adjudications'][0]['owner']='Synthetic task coordinator'
        with self.assertRaisesRegex(w.Block,'material repair blocks'):self.add(d,r)
    def test_final_round_material_failure_preserved_for_escalation(self):
        d,b=self.build()
        for _ in range(2):w.revise(d,b['artifact'],'Synthetic controlled revision tests final round escalation.')
        r=self.finding_receipt(d,b,'material','repair');r['decision']='fail'
        with self.assertRaisesRegex(w.Block,'failed; revise'):self.add(d,r)
        with self.assertRaisesRegex(w.Block,'escalate with preserved findings'):w.revise(d,b['artifact'],'Synthetic extra pass must not bypass final-round escalation.')
        _,s,_=w.load(d);self.assertEqual(s['round'],3);self.assertTrue(w.retained_findings(s))
