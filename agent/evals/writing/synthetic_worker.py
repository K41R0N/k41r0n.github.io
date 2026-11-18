#!/usr/bin/env python3
"""SYNTHETIC WORKER FIXTURE. Not a writer, reviewer, model or author-quality test.
Its canned judgments exercise subprocess dispatch and evidence schemas only.
Never configure it as a production executor.
"""
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

if len(sys.argv)>1 and not sys.argv[1].startswith('--'):
    # Active regression probe: known absolute run-history path must be masked.
    try:
        Path(sys.argv[1]).read_text()
    except (FileNotFoundError,PermissionError):
        pass
    else:
        raise RuntimeError('Prior private critique was readable from worker')
    if list(Path.cwd().iterdir()):
        raise RuntimeError('Worker scratch was not empty')
c=json.load(sys.stdin)
s=c['step'];draft=c['artifact_text'];q=draft[:60];ref=c['before'];snapshot=c['snapshot']
r={'step':s,'before':ref,'after':ref,'actor':'this-claim-must-be-overwritten','turn':'this-claim-must-also-be-overwritten','source_ref':'synthetic-not-owner-evidence','rationale':'Synthetic subprocess fixture only, not a semantic evaluation.','decision':'pass','context_reset':False,'applications':[]}
for sid,source in c['methods'].items():
    clause=next(line for line in source.splitlines() if len(line)>40 and not line.startswith('source:'))[:80]
    r['applications'].append({'source':sid,'method_quote':clause,'draft_quote':q,'application':'Synthetic source mapping exercises the validator without judging taste.'})
if s in ('big-idea','structure','creative','judge'):
    frames=[{'frame':'Synthetic alternative '+str(i)+' for contract validation only','consequence':'Synthetic consequence for evidence schema testing only.'} for i in range(3)]
    r['development']={'guiding_question':'Synthetic fixture inquiry, not an author position.','reframes':frames,'selected_frame':frames[0]['frame'],'selection_reason':'Synthetic selection reason exercises shape only.','scope_boundary':'No author quality or creative success established.','source_anchor':{'input':'input:notes:0','quote':q,'relation':'Synthetic input relation, not a real author inference.'},**{k:{'draft_quote':q,'reasoning':'Synthetic schema field, not substantive editorial evidence.'} for k in ['implication','strongest_objection','example_warrant','gained_ground']}}
if s=='orient':
    r['construction_intent']={k:'Synthetic forward construction intent before procedural prose.' for k in ('guiding_question','section_progression','source_use')}
    r['conflicts_resolved']=True
    r['input_applications']=[{'input':key,'quote':source[:60],'use':'Synthetic input-role coverage, not evidence of author voice.'} for key,source in c['inputs'].items()]
if s=='big-idea':r['big_idea']=draft.split('.')[0]+'.'
if s in ['facts','compliance','legal','data-accuracy','judge']:
    r.update(claim_inventory_complete=True,claims=[],no_factual_claims_reason='Synthetic procedure has no changing external factual claims.')
if s in ['creative','big-idea-review','ogilvy']:
    r['lenses']={name:'Synthetic lens field tests schema completion without quality claims.' for name in c['output_contract']['lenses']}
    r['ogilvy']={name:'Synthetic question field tests all five questions without quality claims.' for name in c['output_contract']['ogilvy']}
if s in ['structure','page','positioning','clarity','subtract','verify-final','judge']:
    r['paragraph_moves']=[{'paragraph_sha256':hashlib.sha256(p.strip().encode()).hexdigest(),'move':'Synthetic procedural paragraph advances the maintenance record.'} for p in draft.split('\n\n') if p.strip()]
    r['page_rule_scope']='Landing-page ratios do not govern this synthetic instruction.'
if s in ['voice','tone','judge']:
    r['voice_evidence']=[{'input':key,'source_quote':source[:60],'draft_quote':q,'comparison':'Synthetic comparison proves schema use, not resemblance or taste.'} for key,source in c['inputs'].items() if any(key.startswith('input:'+role+':') for role in ('voice','register','corrections'))]
    r['dimensions']={name:{'score':3,'quote':q,'reason':'Synthetic score is not an author judgment or calibrated label.'} for name in c['output_contract']['voice_dimensions']}
if s=='judge':
    module_path=Path(snapshot['helper:voice/checks.py']['path'])
    sys.path.insert(0,str(module_path.parent))
    import checks
    current=Path.cwd()/'synthetic-current.md';current.write_text(draft)
    _,rows=checks.run(current)
    sid='method:review-method';src=Path(snapshot[sid]['path']).read_text();clause=next(x for x in src.splitlines() if len(x)>40)[:80]
    r['critical_method_coverage']={k:{'draft_quote':q,'assessment':'Synthetic crucial-method review coverage only.','source':sid,'source_quote':clause} for k in ['llm-patterns','ogilvy','sutherland-reframe']}
    r.update(top_fixes=[],fidelity_failures=0,open_findings=[],worst_lines_assessment='Synthetic canned assessment for software testing only.',overall=5,predicted_edits='Synthetic predictions, not guesses at Alejandro edits.')
    r['warning_adjudications']={x['id']:{'count':x['count'],'reviewer':'synthetic-human-reviewer','reason':'Synthetic disposition tests the process schema only.'} for x in rows if x['count'] and x['severity']=='WARN'}
r.update(ranked_findings=[],adjudications=[])
if c.get('revision_findings'):
    r['revision_findings_seen']=c['revision_findings'];r['revision_adjudication']='Synthetic accepted/rejected fix and seed-preservation rationale.'
if '--write-artifact' in sys.argv or '--bad-output-hash' in sys.argv:
    output=Path.cwd()/'synthetic-output.md'
    output.write_text(draft+'\n')
    r['after']={'path':str(output),'sha256':hashlib.sha256(output.read_bytes()).hexdigest()}
if '--bad-output-hash' in sys.argv:r['after']['sha256']='0'*64
if '--external-artifact' in sys.argv:r['after']=snapshot['input:notes:0']
spec=importlib.util.spec_from_file_location('synthetic_runner',snapshot['runner']['path'])
w=importlib.util.module_from_spec(spec);spec.loader.exec_module(w)
if s in ('big-idea','structure','subtract'):
    r['construction']={'artifact':r['after'],'section_advances':[{'draft_quote':q,'new_inference':'Synthetic section gains procedural clarity only.'}],'hard_joints':[],'joint_selection_reason':'Synthetic short fixture has no difficult argumentative joins.'}
if s=='subtract':
    r['subtraction']={'before':w.architecture_metrics(draft),'after':w.architecture_metrics(Path(r['after']['path']).read_text()),**{k:'Synthetic diagnostic review only, no personal budgets.' for k in ('preservation','pattern_verdict','repeat_verdict','word_delta_reason')}}
if s=='verify-final':r.update(verification_artifact=ref,**{k:'Synthetic final-byte verification, not author quality evidence.' for k in ('fix_verification','knock_on_read','source_preservation','voice_risks')})
if '--retain-advisory' in sys.argv:
    if c.get('role')=='reviewer' and (c.get('revision_findings') or c.get('construction_intent') or c.get('architecture_diagnostics')):
        raise RuntimeError('Fresh critic contaminated by writer intent/findings/metrics')
    if s=='decontaminate':
        sid='method:anti-patterns';source=c['methods']['anti-patterns'];clause=next(line for line in source.splitlines() if len(line)>40)[:80]
        r['ranked_findings']=[{'materiality':'advisory','draft_quote':q,'reason':'Synthetic optional alternative, not an accepted material defect.','source':sid,'source_clause':clause}]
        r['adjudications']=[{'finding_index':0,'materiality':'advisory','decision':'reject','reason':'Synthetic current text remains justified by the source.','counterevidence':'Synthetic procedural wording already preserves the required action.','seed_preservation':'Synthetic original phrase remains unchanged in the artifact.','source':sid,'source_clause':clause}]
json.dump(r,sys.stdout)
