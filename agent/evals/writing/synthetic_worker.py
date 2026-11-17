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

if len(sys.argv)>1:
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
if s=='orient':
    r['conflicts_resolved']=True
    r['input_applications']=[{'input':key,'quote':source[:60],'use':'Synthetic input-role coverage, not evidence of author voice.'} for key,source in c['inputs'].items()]
if s=='big-idea':r['big_idea']=draft.split('.')[0]+'.'
if s in ['facts','compliance','legal','data-accuracy','judge']:
    r.update(claim_inventory_complete=True,claims=[],no_factual_claims_reason='Synthetic procedure has no changing external factual claims.')
if s in ['creative','big-idea-review','ogilvy']:
    r['lenses']={name:'Synthetic lens field tests schema completion without quality claims.' for name in c['output_contract']['lenses']}
    r['ogilvy']={name:'Synthetic question field tests all five questions without quality claims.' for name in c['output_contract']['ogilvy']}
if s in ['structure','page','positioning','clarity']:
    r['paragraph_moves']=[{'paragraph_sha256':hashlib.sha256(p.encode()).hexdigest(),'move':'Synthetic procedural paragraph advances the maintenance record.'} for p in draft.split('\n\n')]
    r['page_rule_scope']='Landing-page ratios do not govern this synthetic instruction.'
if s in ['voice','tone','judge']:
    r['voice_evidence']=[{'input':key,'source_quote':source[:60],'draft_quote':q,'comparison':'Synthetic comparison proves schema use, not resemblance or taste.'} for key,source in c['inputs'].items() if any(key.startswith('input:'+role+':') for role in ('voice','register','corrections'))]
    r['dimensions']={name:{'score':3,'quote':q,'reason':'Synthetic score is not an author judgment or calibrated label.'} for name in c['output_contract']['voice_dimensions']}
if s=='judge':
    module_path=Path(snapshot['helper:voice/checks.py']['path'])
    sys.path.insert(0,str(module_path.parent))
    import checks
    _,rows=checks.run(ref['path'])
    sid='method:review-method';src=Path(snapshot[sid]['path']).read_text();clause=next(x for x in src.splitlines() if len(x)>40)[:80]
    r['critical_method_coverage']={k:{'draft_quote':q,'assessment':'Synthetic crucial-method review coverage only.','source':sid,'source_quote':clause} for k in ['llm-patterns','ogilvy','sutherland-reframe']}
    r.update(top_fixes=[],fidelity_failures=0,open_findings=[],worst_lines_assessment='Synthetic canned assessment for software testing only.',overall=5,predicted_edits='Synthetic predictions, not guesses at Alejandro edits.')
    r['warning_adjudications']={x['id']:{'count':x['count'],'reviewer':'synthetic-human-reviewer','reason':'Synthetic disposition tests the process schema only.'} for x in rows if x['count'] and x['severity']=='WARN'}
json.dump(r,sys.stdout)
