"""Synthetic contract tests only. No fixture is Alejandro prose, gold or calibration.
Run: python3 -m unittest discover -s agent/evals/writing -v
"""
import copy
import datetime as dt
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'scripts/local'))
import writing as w
sys.path.insert(0,str(ROOT/'scripts/local/voice'))
import checks
import evaluate as ev

TEXT='The repair team checks the small valve before opening the main supply. Record the pressure.\n\nA separate inspector reads the gauge and records the result in the maintenance book so the next shift can repeat the same check without guessing which valve was inspected.'
OTHER='The reading group compares two accounts before discussing the ending. Record the difference.\n\nEach participant names the sentence supporting their reading and explains how the narrator changes the scene so the group can distinguish a stated fact from an interpretation.'

class LoopTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(prefix='writing-contract-')
        self.addCleanup(self.tmp.cleanup)
        self.base=Path(self.tmp.name)
    def build(self, mode='review', register='synthetic-maintenance', content=TEXT, scope='personal'):
        d=self.base/('run-'+str(len(list(self.base.iterdir()))))
        a=self.base/(d.name+'-artifact.md'); a.write_text(content)
        roles={}
        for role in ['notes','voice','register','corrections','facts']:
            p=self.base/(d.name+'-'+role+'.md')
            p.write_text(f'SYNTHETIC {role} evidence for a contract test. Never author material or quality evidence. '+content)
            roles[role]=[str(p)]
        if scope=='client':
            cp=self.base/(d.name+'-policy.json');w.write(cp,{'schema':'writing-client-policy/v1','source_ref':'Synthetic policy fixture, no actual client authority.','rule_severities':{rid:'INFO' for rid,*_ in checks.RULES}});roles['client_policy']=[str(cp)]
        b={'voice_owner':'Synthetic fixture subject, not Alejandro','mode':mode,'scope':scope,'voice_target':'author','reader':'The assigned maintenance inspector','already-believes':'The supply must remain closed until inspection','action':'Record the pressure before opening supply','channel':'A synthetic maintenance instruction sheet','register':register,'objective':'Test evidence gates without producing author prose','risk-owner':'The synthetic fixture coordinator','inputs':roles,'artifact':str(a),'format':'essay','author_guideline_overlay':True,'author_overlay_reason':'Synthetic client fixture selects client-only voice policy explicitly.','review_plan':[{'topic':topic,'reason':'Synthetic topic applicability exercises source-grounded selection.','source_ref':'synthetic-original-review-selection'} for topic in ['decontaminate','creative','tone','compliance','page']]}
        bp=self.base/(d.name+'-brief.json');w.write(bp,b)
        # Only the init authority hold is lifted inside this test process. No production policy edit.
        cfg=w.policy(); cfg['new_voice_writing_enabled']=True
        with patch.object(w,'policy',return_value=cfg): w.init(d,bp)
        return d,b
    def receipt(self,d,b,step=None):
        _,s,_=w.load(d);seq=w.sequence(b);step=step or seq[len(s['receipts'])]
        ref=w.artifact(s);draft=Path(ref['path']).read_text();q=draft[:60]
        prepared=w.prepare(d)['context']
        r={'prepared_packet':prepared,'step':step,'before':ref,'after':ref,'actor':'synthetic-independent-reviewer' if step in w.REVIEW else 'synthetic-fixture-writer','turn':'synthetic-turn-'+str(len(s['receipts'])),'source_ref':'fixture-only-source-reference','rationale':'Synthetic process contract exercise, not a quality judgment.','decision':'pass','context_reset':True,'applications':[]}
        for sid in w.required_methods(step,b):
            src=Path(s['snapshot']['method:'+sid]['path']).read_text()
            clause=next(x for x in src.splitlines() if len(x)>40 and not x.startswith('source:'))[:80]
            r['applications'].append({'source':sid,'method_quote':clause,'draft_quote':q,'application':'Synthetic span mapping exercises schema and hashes only.'})
        if step=='orient':
            r['conflicts_resolved']=True;r['input_applications']=[]
            for key,src in s['snapshot'].items():
                if key.startswith('input:'):
                    r['input_applications'].append({'input':key,'quote':Path(src['path']).read_text()[:60],'use':'Synthetic role selection checks coverage without quality claims.'})
        if step=='big-idea':r['big_idea']=draft.split('.')[0]+'.'
        if step in ['facts','compliance','legal','data-accuracy','judge']:
            r['claim_inventory_complete']=True;r['claims']=[];r['no_factual_claims_reason']='Synthetic procedural fixture asserts no changing external facts.'
        if step in ['creative','big-idea-review','ogilvy']:
            r['lenses']={x:'Synthetic response checks that no lens can be omitted.' for x in w.LENSES}
            r['ogilvy']={x:'Synthetic response checks all five questions are retained.' for x in w.OGILVY}
        if step in ['structure','page','positioning','clarity']:
            r['paragraph_moves']=[{'paragraph_sha256':hashlib.sha256(p.encode()).hexdigest(),'move':'Synthetic instruction advances the recorded procedure.'} for p in draft.split('\n\n')]
            r['page_rule_scope']='Landing-page conversion ratios do not govern this synthetic instruction.'
        if step in ['voice','tone','judge']:
            r['voice_evidence']=[{'input':key,'source_quote':Path(src['path']).read_text()[:60],'draft_quote':q,'comparison':'Synthetic sample-to-draft comparison checks the evidence contract only.'} for key,src in s['snapshot'].items() if any(key.startswith('input:'+role+':') for role in ('voice','register','corrections'))]
            r['dimensions']={x:{'score':3,'quote':q,'reason':'Synthetic schema field, not author voice evidence.'} for x in w.policy()['voice_dimensions']}
        if step=='judge':
            sid='method:review-method';src=Path(s['snapshot'][sid]['path']).read_text();clause=next(x for x in src.splitlines() if len(x)>40)[:80]
            r['critical_method_coverage']={k:{'draft_quote':q,'assessment':'Synthetic crucial-method review coverage only.','source':sid,'source_quote':clause} for k in ['llm-patterns','ogilvy','sutherland-reframe']}
            r.update(top_fixes=[],fidelity_failures=0,open_findings=[],worst_lines_assessment='Synthetic review validates the verdict contract only.',overall=5,predicted_edits='Synthetic prediction, never an author-approved result.')
            _,rows=checks.run(ref['path']);r['warning_adjudications']={x['id']:{'count':x['count'],'reviewer':'synthetic-human-reviewer','reason':'Synthetic disposition only; no quality or authorship claim.'} for x in rows if x['count'] and x['severity']=='WARN'}
        return r
    def add(self,d,r):
        p=self.base/'incoming.json';w.write(p,r);return w.record(d,p)
    def finish(self,d,b):
        while w.state(d)['state']=='blocked':self.add(d,self.receipt(d,b))
    def test_full_review_loop_two_registers(self):
        for reg,t in [('synthetic-maintenance',TEXT),('synthetic-reading',OTHER)]:
            d,b=self.build(register=reg,content=t);self.finish(d,b)
            self.assertEqual(w.state(d)['state'],'evidence-complete-attested')
            with self.assertRaisesRegex(w.Block,'incomplete'):w.packet(d,self.base/(reg+'.json'))
            self.assertEqual(w.state(d)['quality'],'uncalibrated')
    def test_client_uses_selected_sources_not_personal_canon(self):
        d,b=self.build(scope='client');_,state,_=w.load(d)
        self.assertIn('method:voice-spec',state['snapshot'])
        self.assertTrue(any(k.startswith('measurement:') for k in state['snapshot']))
        self.finish(d,b)
        self.assertEqual(w.state(d)['state'],'evidence-complete-attested')
    def test_review_selection_changes_actual_sequence(self):
        d,b=self.build();bp=self.base/'alternate.json'
        b['review_plan']=[{'topic':topic,'reason':'Synthetic piece-specific review requirement.','source_ref':'synthetic-original-review-selection'} for topic in ['data-accuracy','legal','clarity','positioning','ogilvy']]
        w.write(bp,b);other=self.base/'alternate-run';w.init(other,bp)
        self.assertEqual(w.sequence(b),['orient','data-accuracy','legal','clarity','positioning','ogilvy','judge'])
        self.finish(other,b)
        self.assertEqual(w.state(other)['state'],'evidence-complete-attested')
    def test_duplicate_review_topic_rejected(self):
        d,b=self.build();b['review_plan'][1]=b['review_plan'][0];bp=self.base/'duplicate.json';w.write(bp,b)
        with self.assertRaisesRegex(w.Block,'distinct'):w.init(self.base/'bad-plan',bp)
    def test_client_explicit_author_overlay(self):
        d,b=self.build(scope='client');b['author_guideline_overlay']=True;bp=self.base/'overlay.json';w.write(bp,b)
        other=self.base/'overlay-run';w.init(other,bp);_,s,_=w.load(other)
        self.assertIn('method:voice-spec',s['snapshot']);self.assertTrue(any(x.startswith('measurement:') for x in s['snapshot']))
        self.finish(other,b)
    def test_client_overlay_cannot_be_implicit(self):
        d,b=self.build(scope='client');del b['author_guideline_overlay'];bp=self.base/'implicit.json';w.write(bp,b)
        with self.assertRaisesRegex(w.Block,'overlay'):w.init(self.base/'implicit-run',bp)
    def test_client_false_overlay_is_not_self_exemption(self):
        d,b=self.build(scope='client');b['author_guideline_overlay']=False;bp=self.base/'false-overlay.json';w.write(bp,b)
        with self.assertRaisesRegex(w.Block,'requires author-guideline'):w.init(self.base/'false-overlay',bp)
    def test_final_judge_cannot_omit_crucial_coverage(self):
        d,b=self.build()
        while w.state(d).get('next')!='judge':self.add(d,self.receipt(d,b))
        r=self.receipt(d,b);del r['critical_method_coverage']
        with self.assertRaisesRegex(w.Block,'crucial method coverage'):self.add(d,r)
    def test_cli_incomplete_packet_fails(self):
        d,b=self.build();p=subprocess.run([sys.executable,str(ROOT/'scripts/local/writing.py'),'packet',str(d),'--output',str(self.base/'out.json')],capture_output=True,text=True)
        self.assertNotEqual(p.returncode,0);self.assertIn('incomplete',p.stdout)
    def test_cli_progress_is_not_completion(self):
        d,b=self.build();p=subprocess.run([sys.executable,str(ROOT/'scripts/local/writing.py'),'status',str(d)],capture_output=True,text=True)
        self.assertNotEqual(p.returncode,0);self.assertEqual(json.loads(p.stdout)['next'],'orient')
    def test_cli_stale_artifact_fails(self):
        d,b=self.build();Path(b['artifact']).write_text('Changed artifact invalidates a pending run.')
        p=subprocess.run([sys.executable,str(ROOT/'scripts/local/writing.py'),'prepare',str(d)],capture_output=True,text=True)
        self.assertNotEqual(p.returncode,0);self.assertIn('stale artifact',p.stdout)
    def test_full_twelve_stage_new_loop_contract_only(self):
        d,b=self.build(mode='new');self.finish(d,b)
        self.assertEqual(len(w.read(d/'run.json')['receipts']),12)
    def test_production_new_writing_hold(self):
        d,b=self.build();b['mode']='new';p=self.base/'newbrief.json';w.write(p,b)
        with self.assertRaisesRegex(w.Block,'paused'):w.init(self.base/'blocked-new',p)
    def test_missing_step_blocks_packet(self):
        d,b=self.build()
        with self.assertRaisesRegex(w.Block,'incomplete'):w.packet(d,self.base/'packet.json')
    def test_out_of_order(self):
        d,b=self.build()
        with self.assertRaisesRegex(w.Block,'expected orient'):self.add(d,self.receipt(d,b,'tone'))
    def test_missing_method_application(self):
        d,b=self.build();r=self.receipt(d,b);r['applications'].pop()
        with self.assertRaisesRegex(w.Block,'missing required'):self.add(d,r)
    def test_irrelevant_method(self):
        d,b=self.build();self.add(d,self.receipt(d,b));r=self.receipt(d,b)
        r['applications'][0]['source']='draft-method'
        with self.assertRaisesRegex(w.Block,'irrelevant method'):self.add(d,r)
    def test_missing_correction_source_application(self):
        d,b=self.build();r=self.receipt(d,b);r['input_applications']=[x for x in r['input_applications'] if ':corrections:' not in x['input']]
        with self.assertRaisesRegex(w.Block,'every selected'):self.add(d,r)
    def test_forged_quote(self):
        d,b=self.build();r=self.receipt(d,b);r['applications'][0]['draft_quote']='This quotation never existed in the actual draft.'
        with self.assertRaisesRegex(w.Block,'quote absent'):self.add(d,r)
    def test_changed_input(self):
        d,b=self.build();Path(b['inputs']['notes'][0]).write_text('Changed after source selection.')
        with self.assertRaisesRegex(w.Block,'stale artifact'):w.state(d)
    def test_changed_draft_after_complete(self):
        d,b=self.build();self.finish(d,b);Path(b['artifact']).write_text('A different artifact after reviews passed.')
        with self.assertRaisesRegex(w.Block,'stale artifact'):w.packet(d,self.base/'packet.json')
    def test_changed_receipt(self):
        d,b=self.build();self.add(d,self.receipt(d,b));p=Path(w.read(d/'run.json')['receipts'][0]['path']);p.write_text('{}')
        with self.assertRaisesRegex(w.Block,'stale artifact'):w.state(d)
    def test_failed_review_cannot_advance(self):
        d,b=self.build();r=self.receipt(d,b);r['decision']='fail'
        with self.assertRaisesRegex(w.Block,'failed'):self.add(d,r)
        with self.assertRaisesRegex(w.Block,'failed'):self.add(d,self.receipt(d,b))
    def test_three_round_limit(self):
        d,b=self.build()
        for _ in range(2):w.revise(d,b['artifact'],'Synthetic upstream structural correction, not a word patch.')
        with self.assertRaisesRegex(w.Block,'three rounds'):w.revise(d,b['artifact'],'One more synthetic revision would exceed the budget.')
    def test_same_turn_rejected(self):
        d,b=self.build();self.add(d,self.receipt(d,b));r=self.receipt(d,b);r['turn']='synthetic-turn-0'
        with self.assertRaisesRegex(w.Block,'distinct turns'):self.add(d,r)
    def test_writer_self_review_rejected(self):
        d,b=self.build();self.add(d,self.receipt(d,b));r=self.receipt(d,b);r['actor']='synthetic-fixture-writer'
        with self.assertRaisesRegex(w.Block,'own reviewer'):self.add(d,r)
    def test_review_cannot_silently_rewrite(self):
        d,b=self.build();self.add(d,self.receipt(d,b));r=self.receipt(d,b);p=self.base/'rewrite.md';p.write_text(OTHER);r['after']=w.file_ref(p)
        with self.assertRaisesRegex(w.Block,'separate round'):self.add(d,r)
    def test_ogilvy_missing_question_blocks(self):
        d,b=self.build()
        for _ in range(2):self.add(d,self.receipt(d,b))
        r=self.receipt(d,b);del r['ogilvy']['wish-i-thought-of-it']
        with self.assertRaisesRegex(w.Block,'all five'):self.add(d,r)
    def test_unresolved_placeholder_blocks(self):
        d,b=self.build(content=TEXT+'\n\n[UNVERIFIED: missing source]')
        for _ in range(6):self.add(d,self.receipt(d,b))
        with self.assertRaisesRegex(w.Block,'placeholder'):self.add(d,self.receipt(d,b))
    def test_fidelity_overrides_high_score(self):
        d,b=self.build()
        for _ in range(6):self.add(d,self.receipt(d,b))
        r=self.receipt(d,b);r['fidelity_failures']=1;r['overall']=10
        with self.assertRaisesRegex(w.Block,'fidelity failure'):self.add(d,r)
    def test_top_fix_cap(self):
        d,b=self.build()
        for _ in range(6):self.add(d,self.receipt(d,b))
        r=self.receipt(d,b);r['top_fixes']=['Synthetic detailed proposed correction.']*4
        with self.assertRaisesRegex(w.Block,'top 3'):self.add(d,r)
    def test_personal_lint_is_not_client_cap(self):
        p=self.base/'long.md';p.write_text(' '.join(['word']*40)+'.')
        _,a=checks.run(p);_,b=checks.run(p,'client-candidate')
        self.assertEqual(next(x for x in a if x['id']=='S01')['severity'],'INFO')
        self.assertEqual(next(x for x in b if x['id']=='S01')['severity'],'FAIL')
    def test_missing_prepared_context_blocks(self):
        d,b=self.build();r=self.receipt(d,b);r['prepared_packet']={}
        with self.assertRaisesRegex(w.Block,'path and sha256'):self.add(d,r)
    def test_changed_prepared_context_blocks(self):
        d,b=self.build();r=self.receipt(d,b);Path(r['prepared_packet']['path']).write_text('{}')
        with self.assertRaisesRegex(w.Block,'stale artifact'):self.add(d,r)
    def test_numerical_claim_cannot_hide_in_no_claims(self):
        d,b=self.build(content=TEXT+' The gauge reached 17 units before the test ended.')
        for _ in range(4):self.add(d,self.receipt(d,b))
        with self.assertRaisesRegex(w.Block,'numerical claim'):self.add(d,self.receipt(d,b))
    def test_claim_cannot_cite_voice_examples_as_facts(self):
        d,b=self.build()
        for _ in range(4):self.add(d,self.receipt(d,b))
        r=self.receipt(d,b);r['claims']=[{'draft_quote':TEXT[:60],'source':'input:voice:0','source_quote':TEXT[:60],'scope_and_caveat':'Synthetic source scope limitation is explicit.','verified_at':dt.datetime.now(dt.timezone.utc).isoformat()}]
        with self.assertRaisesRegex(w.Block,'not voice examples'):self.add(d,r)
    def test_fact_verification_expiry(self):
        d,b=self.build()
        for _ in range(4):self.add(d,self.receipt(d,b))
        r=self.receipt(d,b);r['claims']=[{'draft_quote':TEXT[:60],'source':'input:facts:0','source_quote':TEXT[:60],'scope_and_caveat':'Synthetic source scope limitation is explicit.','verified_at':'2020-01-01T00:00:00+00:00'}]
        with self.assertRaisesRegex(w.Block,'stale or in future'):self.add(d,r)
    def test_prediction_seal_binds_untouched_draft(self):
        import ledger
        d=self.base/'pair';d.mkdir();(d/'draft.md').write_text(TEXT);(d/'predictions.md').write_text('Synthetic predicted edits, not an author judgment.')
        self.assertTrue(ledger.seal(d).startswith('SEALED'))
        self.assertTrue(ledger.seal(d).startswith('FAIL'))
        (d/'draft.md').write_text(OTHER);(d/'final.md').write_text(OTHER);(d/'classes.md').write_text('')
        result,probs=ledger.score(d)
        self.assertIn('draft.md changed after sealing',probs)
    def test_empty_lint_no_division_error(self):
        p=self.base/'empty.md';p.write_text('');self.assertEqual(checks.run(p)[0],0)
    def test_unknown_scope_rejected(self):
        with self.assertRaisesRegex(ValueError,'unknown'):checks.run('unused',scope='automatic')
    def test_private_run_cannot_live_in_repo(self):
        with self.assertRaisesRegex(w.Block,'outside'):w.private_dir(ROOT/'assets'/'new-run')

class DispatchCLITests(unittest.TestCase):
    setUp=LoopTests.setUp
    build=LoopTests.build
    receipt=LoopTests.receipt
    add=LoopTests.add

    # Reuse only fixture construction, not the inherited tests a second time.
    def fixture_host(self):
        import shutil
        repo=self.base/'fixture-repo';shutil.copytree(ROOT,repo/'agent',ignore=shutil.ignore_patterns('__pycache__'))
        root=repo/'agent';pol=root/'harness/specs/writing-loop.json';cfg=w.read(pol)
        worker=root/'evals/writing/synthetic_worker.py'
        cfg['new_voice_writing_enabled']=True
        cfg['executors']={role:{'worker_id':'synthetic-'+role+'-executor','command':[sys.executable,str(worker)],'pinned_files':[w.file_ref(worker)],'timeout_seconds':10,'confinement':w.file_ref('/usr/bin/bwrap')} for role in ['writer','reviewer']}
        w.write(pol,cfg)
        return root
    def call(self,root,*args):
        p=subprocess.run([sys.executable,str(root/'scripts/local/writing.py'),*map(str,args)],capture_output=True,text=True)
        return p,json.loads(p.stdout)
    def test_worker_cannot_read_known_absolute_prior_critique(self):
        root=self.fixture_host();_,brief=self.build();bp=self.base/'probe-brief.json';w.write(bp,brief)
        run=self.base/'probe-run'
        secret=run/'prior-judge-predictions.txt'
        pol=root/'harness/specs/writing-loop.json';cfg=w.read(pol)
        for adapter in cfg['executors'].values():adapter['command'].append(str(secret))
        w.write(pol,cfg)
        self.call(root,'init',run,'--brief',bp)
        secret.write_text('PRIVATE previous judge rationale and sealed predictions')
        proc,result=self.call(root,'execute',run)
        self.assertEqual(proc.returncode,0,proc.stdout);self.assertEqual(result['next'],'decontaminate')
    def test_missing_confinement_blocks_dispatch(self):
        root=self.fixture_host();_,brief=self.build();bp=self.base/'unconfined.json';w.write(bp,brief)
        run=self.base/'unconfined-run'
        pol=root/'harness/specs/writing-loop.json';cfg=w.read(pol)
        for adapter in cfg['executors'].values():adapter.pop('confinement')
        w.write(pol,cfg)
        self.call(root,'init',run,'--brief',bp)
        proc,result=self.call(root,'execute',run)
        self.assertNotEqual(proc.returncode,0);self.assertIn('confinement',result['reason'])
    def test_end_to_end_cli_dispatch_isolated_twelve_passes(self):
        root=self.fixture_host();_,brief=self.build();brief['mode']='new';p=self.base/'cli-brief.json';w.write(p,brief)
        run=self.base/'cli-run';proc,result=self.call(root,'init',run,'--brief',p)
        self.assertEqual(result['next'],'orient')
        turns=[]
        for _ in range(12):
            proc,result=self.call(root,'execute',run)
            state=w.read(run/'run.json');receipt=w.read(state['receipts'][-1]['path'])
            self.assertEqual(proc.returncode,0,proc.stdout)
            self.assertEqual(receipt['execution']['mode'],'dispatched');self.assertEqual(receipt['execution']['exit_code'],0)
            self.assertTrue(receipt['turn'].startswith('writing-invocation-'))
            self.assertNotEqual(receipt['actor'],'this-claim-must-be-overwritten');turns.append(receipt['turn'])
        self.assertEqual(len(set(turns)),12);self.assertEqual(proc.returncode,0);self.assertEqual(result['state'],'process-complete')
        self.assertEqual(result['quality'],'uncalibrated')
        proc,packet=self.call(root,'packet',run,'--output',self.base/'cli-packet.json')
        self.assertEqual(proc.returncode,0);self.assertEqual(packet['state'],'draft-for-author-evaluation')
        proc,sealed=self.call(root,'seal-author',run);self.assertEqual(proc.returncode,0)
        self.assertEqual(sealed['state'],'sealed-before-author-edit')
        final=self.base/'synthetic-final.md';final.write_text(TEXT)
        classes=self.base/'synthetic-classes.md';classes.write_text('')
        original=self.base/'synthetic-original.txt';original.write_text('Synthetic feedback evidence, never an authenticated owner decision.')
        proof=self.base/'synthetic-provenance.json';w.write(proof,{'original_feedback_id':'synthetic-not-owner-original','identity_checked_by':'synthetic-fixture-checker','independent_classifier':'synthetic-independent-classifier','author_edit_at':dt.datetime.now(dt.timezone.utc).isoformat(),'original_evidence':w.file_ref(original),'evidence_quote':'Synthetic feedback evidence','final_sha256':w.digest(final)})
        proc,scored=self.call(root,'score-author',run,'--final',final,'--classes',classes,'--provenance',proof)
        self.assertEqual(proc.returncode,0);self.assertEqual(scored['state'],'author-feedback-recorded');self.assertFalse(scored['quality_pass'])
        proc,repeated=self.call(root,'seal-author',run);self.assertNotEqual(proc.returncode,0)
    def test_existing_verification_runs_in_isolated_copy(self):
        root=self.fixture_host()
        p=subprocess.run([sys.executable,str(root/'scripts/local/voice/verify.py')],cwd=root,capture_output=True,text=True)
        self.assertEqual(p.returncode,0,p.stderr)
        self.assertIn('committed spec equals fresh rebuild = True',p.stdout)
        self.assertTrue((root/'ingestion/reports/voice/reports/verification.md').is_file())
    def test_production_dispatch_not_configured_blocks(self):
        d,b=self.build()
        with self.assertRaisesRegex(w.Block,'no approved production'):w.execute(d)
    def test_receipt_cannot_claim_runner_execution(self):
        d,b=self.build();r=self.receipt(d,b);r['execution']={'mode':'dispatched'}
        with self.assertRaisesRegex(w.Block,'runner-owned'):self.add(d,r)

class EvaluationTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(prefix='eval-contract-');self.addCleanup(self.tmp.cleanup);self.base=Path(self.tmp.name)
    def file(self,name,body):
        p=self.base/name;p.write_text(body);return w.file_ref(p)
    def dataset(self):
        d={'schema':'author-eval/v1','register':'synthetic-test-only','provenance_reviewed':True,'provenance_reviewer':'Synthetic fixture reviewer, not an owner','label_import_source':'Synthetic fixture, NOT authenticated author evidence','splits':{},'labels':{},'predictions':{},'guide_inputs':['train-case'],'prior_exposed_ids':[],'prior_exposed_hashes':[]}
        d['guide']=self.file('guide.md','Synthetic guide for exercising the evaluator contract.')
        d['rubric']=self.file('rubric.md','Synthetic rubric for exercising the evaluator contract.')
        for split in ['train','calibration','test']:
            arts=[self.file(split+x+'.md',f'{split} synthetic candidate {x} text, not author prose.') for x in ['A','B']]
            cid=split+'-case';d['splits'][split]=[{'id':cid,'register':d['register'],'exposure':'unseen-test' if split=='test' else split,'artifacts':arts}]
            if split=='train':continue
            e=self.file(split+'-label.md','Synthetic preference declaration for contract testing only.')
            d['labels'][split]=[{'case':cid,'choice':arts[0]['sha256'],'original_message_id':'synthetic-NOT-an-owner-message','evidence':e,'evidence_quote':'Synthetic preference declaration','reason':'Synthetic fixture checks numeric calculation, not taste.'}]
            js=self.file(split+'-judge.md','Synthetic judgment trace for evaluator schema testing only.')
            order=[a['sha256'] for a in arts]
            d['predictions'][split]=[{'case':cid,'guide_sha256':d['guide']['sha256'],'rubric_sha256':d['rubric']['sha256'],'orders':[{'order':o,'choice':order[0],'confidence':0.8,'rationale':'Synthetic rationale for a deterministic test only.','evidence':js,'evidence_quote':'Synthetic judgment trace'} for o in [order,order[::-1]]]}]
        return d
    def run_eval(self,d):
        p=self.base/'dataset.json';w.write(p,d);return ev.evaluate(p)
    def test_perfect_synthetic_scores_never_quality_pass(self):
        r=self.run_eval(self.dataset());self.assertFalse(r['quality_pass']);self.assertEqual(r['state'],'calibration-insufficient');self.assertEqual(r['metrics']['test']['agreement'],1)
    def test_order_bias_counted(self):
        d=self.dataset();pred=d['predictions']['test'][0];pred['orders'][1]['choice']=pred['orders'][1]['order'][0]
        self.assertEqual(self.run_eval(d)['metrics']['test']['order_inconsistency'],1)
    def test_invalid_judgment_no_fallback(self):
        d=self.dataset();d['predictions']['test'][0]['orders'][0]['choice']='garbage'
        with self.assertRaisesRegex(w.Block,'invalid judgment'):self.run_eval(d)
    def test_cross_split_leak_blocks(self):
        d=self.dataset();d['splits']['test'][0]['artifacts'][0]=d['splits']['train'][0]['artifacts'][0]
        with self.assertRaisesRegex(w.Block,'content leaks'):self.run_eval(d)
    def test_spent_holdout_blocks(self):
        d=self.dataset();d['prior_exposed_ids']=['test-case']
        with self.assertRaisesRegex(w.Block,'previously exposed'):self.run_eval(d)
    def test_stale_guide_blocks(self):
        d=self.dataset();Path(d['guide']['path']).write_text('A changed guide invalidates recorded judgments.')
        with self.assertRaisesRegex(w.Block,'stale artifact'):self.run_eval(d)
    def test_missing_label_blocks(self):
        d=self.dataset();d['labels']['test']=[]
        with self.assertRaisesRegex(w.Block,'incomplete'):self.run_eval(d)
    def test_missing_original_provenance_blocks(self):
        d=self.dataset();d['provenance_reviewed']=False
        with self.assertRaisesRegex(w.Block,'provenance'):self.run_eval(d)

if __name__=='__main__':unittest.main()
