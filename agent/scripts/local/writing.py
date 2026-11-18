#!/usr/bin/env python3
"""One offline entrypoint for the existing copy-draft / copy-review / writer-judge loop.

No generation, model API, publication or approval side effects. Evidence is private.
Run from any directory. See routines/writer-judge-loop.md for the receipt contract.
"""
import argparse
import datetime as dt
import hashlib
import json
from pathlib import Path
import re
import sys
import subprocess
import uuid
import os
import shutil
import tempfile

ROOT = Path(__file__).resolve().parents[2]
POLICY = ROOT / 'harness/specs/writing-loop.json'
CATALOG = ROOT / 'knowledge/voice/writing-source-catalog.json'
STEPS = ['orient', 'big-idea', 'facts', 'voice', 'structure', 'risk',
         'decontaminate', 'creative', 'tone', 'compliance', 'page', 'judge']
REVIEW = set(STEPS[6:]) | {'big-idea-review','ogilvy','positioning','clarity','legal','data-accuracy'}
LENSES = ['reframe', 'behavioral-economics', 'cultural-tension', 'metaphor', 'contrarian']
OGILVY = ['gasp', 'wish-i-thought-of-it', 'unique', 'strategy-fit', 'thirty-years']
BUCKETS = ['voice-rule', 'structure', 'fidelity', 'banned-phrase']
class Block(ValueError):
    pass

def need(ok, why):
    if not ok:
        raise Block(why)

def read(p):
    return json.loads(Path(p).read_text(encoding='utf-8'))

def digest(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def text(p):
    return Path(p).read_text(encoding='utf-8')

def write(p, obj):
    p = Path(p)
    tmp = p.with_suffix('.tmp')
    tmp.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + '\n')
    tmp.replace(p)

def nonempty(v):
    return isinstance(v, str) and len(v.strip()) >= 12 and not re.fullmatch(r'(?i)(?:pass|done|n/?a|ok|true|yes|no)[.! ]*', v.strip())

def file_ref(p):
    p = Path(p).resolve()
    need(p.is_file(), f'missing file: {p}')
    return {'path': str(p), 'sha256': digest(p)}

def checked(ref):
    need(isinstance(ref, dict) and set(ref) == {'path', 'sha256'}, 'expected path and sha256 reference')
    p = Path(ref['path'])
    need(p.is_file() and digest(p) == ref['sha256'], f'missing or stale artifact: {p}')
    return p

def quote(ref, q):
    p = checked(ref)
    need(isinstance(q, str) and len(q.strip()) >= 16 and q in text(p), f'evidence quote absent or too short: {p}')

def private_dir(d):
    d = Path(d).resolve()
    need(not d.is_relative_to(ROOT.parent), 'run data must stay outside the repository')
    return d

def policy():
    return read(POLICY)

def required_methods(step, brief):
    catalog=read(CATALOG)
    allowed={x['id'] for x in catalog['sources'] if (brief['scope'] in x['scopes'] or (brief.get('author_guideline_overlay') is True and 'personal' in x['scopes']))}
    return [x for x in catalog['steps'][step] if x in allowed]

def snapshot(brief):
    cat = read(CATALOG)
    refs = {'runner': file_ref(__file__), 'policy': file_ref(POLICY), 'catalog': file_ref(CATALOG)}
    for helper in ('writing_claude_adapter.py', 'voice/checks.py', 'voice/evaluate.py', 'voice/placeholders.py', 'voice/holdout_guard.py', 'voice/vlib.py', 'voice/ledger.py', 'voice/edit_rate.py', 'voice/build_spec.py', 'voice/gen_spec_md.py', 'voice/spec_v0.json'):
        refs['helper:' + helper] = file_ref(ROOT / 'scripts/local' / helper)
    if brief['scope']=='personal' or brief.get('author_guideline_overlay') is True:
        for raw in sorted((ROOT/'assets/voice-corpus/raw').glob('*.md')):
            refs['measurement:raw:'+raw.name]=file_ref(raw)
        rebuild=subprocess.run([sys.executable,str(ROOT/'scripts/local/voice/build_spec.py')],capture_output=True,text=True,check=True)
        need(json.loads(rebuild.stdout)==read(ROOT/'scripts/local/voice/spec_v0.json'), 'voice measurement spec is stale; rebuild and reconcile first')
        markdown=subprocess.run([sys.executable,str(ROOT/'scripts/local/voice/gen_spec_md.py')],capture_output=True,text=True,check=True)
        need(markdown.stdout==text(ROOT/'knowledge/voice/voice-spec.md'), 'voice Markdown and numerical spec disagree')
    for s in cat['sources']:
        if s.get('required') and (brief['scope'] in s['scopes'] or (brief.get('author_guideline_overlay') is True and 'personal' in s['scopes'])):
            refs['method:' + s['id']] = file_ref(ROOT / s['path'])
    for kind in ('notes', 'voice', 'register', 'corrections', 'facts') + (('client_policy',) if brief['scope']=='client' else ()):
        need(brief['inputs'].get(kind), f'missing input role: {kind}')
    for kind, paths in brief['inputs'].items():
        need(isinstance(paths, list) and paths, f'empty input list: {kind}')
        for i, p in enumerate(paths):
            need(not any(x in str(p).lower() for x in ('/holdout/', '/excluded/')), 'writer may not read holdout or unverified corpus')
            ref=file_ref(p)
            private_test_hashes={digest(f) for split in ('holdout','excluded') for f in (ROOT/'assets/voice-corpus'/split).glob('*.md')}
            need(ref['sha256'] not in private_test_hashes, 'renamed test/unverified corpus input')
            refs[f'input:{kind}:{i}'] = ref
    return refs

def init(d, brief_path):
    d = private_dir(d)
    need(not d.exists(), 'run directory already exists')
    b = read(brief_path)
    need(b.get('mode') in ('new', 'review'), 'mode must be new or review')
    need(b.get('scope') in ('personal', 'client'), 'scope must be personal or client')
    for k in ('reader', 'already-believes', 'action', 'channel', 'register', 'objective', 'risk-owner', 'voice_owner'):
        need(nonempty(b.get(k)), f'brief incomplete: {k}')
    plan=b.get('review_plan',[])
    need(isinstance(plan,list) and len(plan)==5 and all(isinstance(p,dict) and isinstance(p.get('topic'),str) for p in plan) and len({p['topic'] for p in plan})==5, 'select five distinct review topics for this piece')
    for item in plan:
        need(item.get('topic') in REVIEW-{'judge'} and nonempty(item.get('reason')) and nonempty(item.get('source_ref')), 'review-topic selection needs applicability and source provenance')
    need(b.get('voice_target') == 'author', 'voice_target must be author; no anonymous generic voice')
    if b['mode'] == 'new':
        need(policy()['new_voice_writing_enabled'], 'voice writing remains paused; new drafts are not authorized')
    need(b.get('format') in ('essay', 'short-post', 'landing-page', 'email'), 'unknown format; resolve before proceeding')
    if b['scope']=='client':
        need(b.get('author_guideline_overlay') is True and nonempty(b.get('author_overlay_reason')), 'author-target client run requires author-guideline overlay; no self-exemption by prose rationale')
    refs = snapshot(b)
    initial = file_ref(b['artifact'])
    d.mkdir(parents=True)
    write(d / 'brief.json', b)
    write(d / 'run.json', {'version': 1, 'brief_sha256': digest(d / 'brief.json'), 'snapshot': refs,
                          'initial': initial, 'round': 1, 'receipts': [], 'history': []})
    return state(d)

def load(d):
    d = private_dir(d)
    s = read(d / 'run.json')
    need(digest(d / 'brief.json') == s['brief_sha256'], 'brief changed; start a new run')
    for ref in s['snapshot'].values():
        checked(ref)
    checked(s['initial'])
    for old_round in s['history']:
        checked(old_round['initial'])
        for ref in (old_round.get('author_seal') or {}).values(): checked(ref)
        for ref in old_round['receipts']:
            rr = read(checked(ref)); checked(rr['before']); checked(rr['after'])
    for ref in s['receipts']:
        checked(ref)
    return d, s, read(d / 'brief.json')

def sequence(b):
    reviews=[x['topic'] for x in b['review_plan']]+['judge']
    return STEPS[:6]+reviews if b['mode']=='new' else ['orient']+reviews

def artifact(s):
    return read(s['receipts'][-1]['path'])['after'] if s['receipts'] else s['initial']

def development(r, step, snapshot):
    """Validate required editorial work, never certify its semantic quality."""
    if step not in ('big-idea', 'structure', 'creative', 'judge'):
        return
    d = r.get('development', {})
    need(isinstance(d, dict), 'development evidence must be an object')
    for key in ('guiding_question', 'selected_frame', 'selection_reason', 'scope_boundary'):
        need(nonempty(d.get(key)), 'development missing ' + key)
    frames = d.get('reframes', [])
    need(isinstance(frames, list) and 3 <= len(frames) <= 5, 'develop 3-5 alternative reframes, not lens labels')
    need(all(nonempty(x.get('frame')) and nonempty(x.get('consequence')) for x in frames), 'every reframe needs an actual consequence')
    need(len({x['frame'].strip().lower() for x in frames}) == len(frames), 'duplicate reframes cannot substitute for alternatives')
    need(d['selected_frame'] in [x['frame'] for x in frames], 'selected frame must be one of the alternatives')
    for key in ('implication', 'strongest_objection', 'example_warrant', 'gained_ground'):
        item = d.get(key, {})
        need(isinstance(item, dict) and nonempty(item.get('reasoning')), 'development missing reasoned ' + key)
        quote(r['after'], item.get('draft_quote'))
    anchor = d.get('source_anchor', {})
    need(anchor.get('input') in snapshot and anchor['input'].startswith(('input:notes:', 'input:facts:')), 'development anchor must be source substance, not a voice sample')
    quote(snapshot[anchor['input']], anchor.get('quote'))
    need(nonempty(anchor.get('relation')), 'explain source-to-development relation without inventing stance')

def validate_receipt(r, step, s, b):
    need(r.get('step') == step, f'expected {step}, not {r.get("step")}')
    prepared=read(checked(r['prepared_packet']))
    need(prepared['step']==step and prepared['before']==artifact(s) and prepared['snapshot']==s['snapshot'], 'prepared context mismatches pass, artifact or sources')
    need(r.get('before') == artifact(s), 'receipt does not consume the preceding artifact')
    checked(r['before']); checked(r['after'])
    for k in ('actor', 'turn', 'source_ref', 'rationale'):
        need(nonempty(r.get(k)), f'receipt lacks {k}')
    # A source_ref is audit provenance, not authentication. Never turns into owner authority.
    need(r.get('decision') in ('pass', 'fail'), 'explicit pass/fail required; no implicit pass')
    need(r.get('context_reset') is True, 'each pass requires a fresh context')
    prior = [read(p['path']) for p in s['receipts']]
    need(r['turn'] not in [p['turn'] for p in prior], 'passes must use distinct turns')
    if step in REVIEW:
        need(r['before'] == r['after'], 'reviewer diagnoses; revise in a separate round, not inside critique')
        writers = {p['actor'] for p in prior if p['step'] not in REVIEW}
        need(r['actor'] not in writers, 'writer cannot be its own reviewer')
    need(r.get('applications'), 'no source applications')
    required = required_methods(step, b)
    applied = set()
    for a in r['applications']:
        sid = 'method:' + a['source']
        need(sid in s['snapshot'], 'unregistered method or factual source laundered as method')
        need(a['source'] in required, f'irrelevant method for {step}: {a["source"]}')
        quote(s['snapshot'][sid], a.get('method_quote'))
        quote(r['after'], a.get('draft_quote'))
        need(nonempty(a.get('application')), 'source must be applied, not merely listed')
        applied.add(a['source'])
    need(applied == set(required), f'missing required method applications: {sorted(set(required)-applied)}')
    development(r, step, s['snapshot'])
    if step == 'orient':
        used = set()
        for a in r.get('input_applications', []):
            key = a['input']
            need(key.startswith('input:') and key in s['snapshot'], 'invalid input source/role')
            quote(s['snapshot'][key], a.get('quote'))
            need(nonempty(a.get('use')), 'state how this input steers the piece')
            used.add(key)
        need(used == {k for k in s['snapshot'] if k.startswith('input:')}, 'orientation must use every selected source, sample and correction')
        need(r.get('conflicts_resolved') is True, 'source/rule scope conflict remains unresolved')
    if step == 'big-idea':
        need(isinstance(r.get('big_idea'), str) and 1 <= len(r['big_idea'].split()) <= 15, 'big idea must have 1-15 words')
        need(r['big_idea'] in text(r['after']['path']), 'big idea absent from artifact')
    if step in ('facts', 'compliance', 'legal', 'data-accuracy', 'judge'):
        need(r.get('claim_inventory_complete') is True, 'claim inventory not attested complete')
        for c in r.get('claims', []):
            quote(r['after'], c.get('draft_quote'))
            need(c.get('source') in s['snapshot'] and c['source'].startswith('input:facts:'), 'claim must cite facts, not voice examples or methods')
            need('/voice-corpus/' not in s['snapshot'][c['source']]['path'], 'voice corpus cannot supply factual claims or stories')
            quote(s['snapshot'][c['source']], c.get('source_quote'))
            need(nonempty(c.get('scope_and_caveat')), 'claim scope/caveat missing')
            asof = dt.datetime.fromisoformat(c['verified_at'])
            need(asof.tzinfo is not None and dt.datetime.fromisoformat(prepared['prepared_at']) <= asof <= dt.datetime.now(dt.timezone.utc), 'claim verification stale or in future')
        need(r.get('claims') or nonempty(r.get('no_factual_claims_reason')), 'claims cannot disappear silently')
        number_rx=r'\b\d[\d,.%/:-]*\b'
        for match in re.finditer(number_rx, text(r['after']['path'])):
            need(any(match.group() in re.findall(number_rx,c['draft_quote']) and match.group() in re.findall(number_rx,c['source_quote']) for c in r.get('claims', [])), 'unmapped or changed numerical claim')
        for quoted in re.findall(r'[\"“]([^\"”\n]{16,})[\"”]', text(r['after']['path'])):
            need(any(quoted in c['draft_quote'] and quoted in c['source_quote'] for c in r.get('claims', [])), 'quotation lacks verbatim factual provenance')
    if step in ('creative','big-idea-review','ogilvy'):
        fields=[('lenses', LENSES), ('ogilvy', OGILVY)] if step=='creative' else [('ogilvy', OGILVY)]
        for key, names in fields:
            need(set(r.get(key, {})) == set(names), f'{key}: all five required')
            need(all(nonempty(v) for v in r[key].values()), f'{key}: explain each judgment')
    if step in ('structure', 'page','positioning','clarity'):
        paras = [p.strip() for p in re.split(r'\n\s*\n', text(r['after']['path'])) if p.strip()]
        moves = r.get('paragraph_moves', [])
        need(len(moves) == len(paras), 'name each paragraph move; do not replace structural review with a word sweep')
        for p, m in zip(paras, moves):
            need(m.get('paragraph_sha256') == hashlib.sha256(p.encode()).hexdigest() and nonempty(m.get('move')), 'paragraph map missing, stale or reordered')
        if b['format'] != 'landing-page':
            need(nonempty(r.get('page_rule_scope')), 'explain why landing-page pronoun/CTA rules do not govern this format')
    if step in ('voice', 'tone', 'judge'):
        applied_inputs=set()
        for evidence in r.get('voice_evidence',[]):
            key=evidence['input']
            need(key in s['snapshot'] and any(key.startswith('input:'+role+':') for role in ('voice','register','corrections')), 'wrong voice evidence role')
            quote(s['snapshot'][key], evidence.get('source_quote'))
            quote(r['after'], evidence.get('draft_quote'))
            need(nonempty(evidence.get('comparison')), 'voice comparison must name what fits or fails')
            applied_inputs.add(key)
        need(applied_inputs=={key for key in s['snapshot'] if any(key.startswith('input:'+role+':') for role in ('voice','register','corrections'))}, 'voice evaluation must apply actual selected samples, register and corrections')
        dims = policy()['voice_dimensions']
        need(set(r.get('dimensions', {})) == set(dims), 'all voice dimensions require quoted evaluation')
        for dim in r['dimensions'].values():
            need(type(dim.get('score')) is int and 1 <= dim['score'] <= 5, 'dimension score must be integer 1-5')
            quote(r['after'], dim.get('quote'))
            need(nonempty(dim.get('reason')), 'dimension needs a reason grounded in the selected register')
    if step == 'judge':
        coverage=r.get('critical_method_coverage',{})
        need(set(coverage)=={'llm-patterns','ogilvy','sutherland-reframe'}, 'final review must surface crucial method coverage, not silently omit it from selected five')
        for item in coverage.values():
            quote(r['after'],item.get('draft_quote'));need(nonempty(item.get('assessment')), 'critical method coverage needs grounded assessment')
            need(item.get('source') in s['snapshot'] and item['source'].startswith('method:'), 'critical method source missing');quote(s['snapshot'][item['source']],item.get('source_quote'))
        need(isinstance(r.get('top_fixes'), list) and len(r['top_fixes']) <= 3, 'judge feedback capped at top 3 fixes')
        need(all(nonempty(x) for x in r['top_fixes']), 'fixes need substance')
        need(type(r.get('fidelity_failures')) is int and r['fidelity_failures']>=0, 'explicit fidelity failure count required')
        need(isinstance(r.get('open_findings'),list), 'explicit review findings required')
        if r['decision']=='pass':
            need(r['fidelity_failures'] == 0, 'fidelity failure blocks completion regardless of score')
            need(r['open_findings'] == [] and r['top_fixes']==[], 'unresolved review findings block completion')
        need(nonempty(r.get('worst_lines_assessment')), 'worst-lines review missing')
        need(type(r.get('overall')) is int and 1 <= r['overall'] <= 10, 'overall verdict 1-10 required')
        # Save predictions before an author final exists. Hash/time alone do not authenticate authorship.
        need(nonempty(r.get('predicted_edits')), 'sealed author-edit predictions missing')
        if r['decision']=='fail': return r
        sys.path.insert(0, str(ROOT / 'scripts/local/voice'))
        import checks, holdout_guard
        need(not re.search(r'\[(?:UNVERIFIED|VERIFY|TBD|ALEJANDRO:)[^\]]*\]|\{\{.+?\}\}', text(r['after']['path']), re.I), 'unresolved source or author placeholder')
        _, rows = checks.run(r['after']['path'], 'personal' if b['scope']=='personal' else 'client-candidate')
        if b['scope']=='client':
            active=read(checked(s['snapshot']['input:client_policy:0']))
            need(active.get('schema')=='writing-client-policy/v1' and nonempty(active.get('source_ref')), 'client policy needs current source provenance')
            severities=active.get('rule_severities',{})
            need(set(severities)=={x['id'] for x in rows} and all(v in ('INFO','WARN','FAIL') for v in severities.values()), 'client must explicitly select scoped rule severities; no personal or candidate defaults')
            for row in rows: row['severity']=severities[row['id']]
        need(not [x for x in rows if x['severity']=='FAIL' and x['count']], 'encoded scoped lint failure')
        warns = {x['id']:x['count'] for x in rows if x['severity']=='WARN' and x['count']}
        calls=r.get('warning_adjudications', {})
        need(set(calls)==set(warns), 'every contextual lint warning needs human adjudication')
        for wid, count in warns.items():
            need(calls[wid].get('count')==count and nonempty(calls[wid].get('reason')) and nonempty(calls[wid].get('reviewer')), 'warning adjudication stale or incomplete')
        overlaps=holdout_guard.run([r['after']['path']])
        need(not any(overlaps.values()), 'shared holdout 8-gram: independent review required; not proof of copying')
    return r

def replay(s, b):
    shadow = dict(s, receipts=[])
    seq = sequence(b)
    for i, ref in enumerate(s['receipts']):
        need(i < len(seq), 'too many receipts')
        r = read(checked(ref))
        execution=r.get('execution',{})
        if execution.get('mode')=='dispatched':
            for pin in execution['pinned_files']: checked(pin)
            checked(execution['confinement'])
            stdout=checked(execution['stdout'])
            need(execution['exit_code']==0 and execution['context_sha256']==r['prepared_packet']['sha256'], 'failed or unrelated worker invocation')
            need(r['turn']==execution['invocation_id'] and r['actor']==execution['worker_id'], 'execution identity changed')
        validate_receipt(r, seq[i], shadow, b)
        need(r['decision'] == 'pass', f'{r["step"]} failed; revise, do not advance')
        shadow['receipts'].append(ref)
    return seq

def receipt_contract(step):
    # This is the worker-facing output shape; validate_receipt owns strict semantics.
    fields={
        'step':'Exact current step', 'before':'Packet before path+sha256 object',
        'after':'Reviewers: identical to before; writers: actual next artifact reference. Dispatched writers create new files in cwd scratch; the runner preserves them before cleanup.',
        'rationale':'Substantive judgment scoped to this step', 'decision':'pass or fail',
        'applications':'List of {source: method ID, method_quote: exact source span, draft_quote: exact current span, application: reasoning}'
    }
    if step in ('big-idea','structure','creative','judge'):
        fields['development']={'guiding_question':'Actual inquiry', 'reframes':'3-5 distinct {frame, consequence} alternatives', 'selected_frame':'Exact chosen frame', 'selection_reason':'Why it serves this brief', 'scope_boundary':'What is not established or authorized', 'source_anchor':'{input: notes/facts key, quote: exact source span, relation: source vs new reasoning}', 'implication':'{draft_quote, reasoning}', 'strongest_objection':'{draft_quote, reasoning}', 'example_warrant':'{draft_quote, reasoning: what example establishes and cannot establish}', 'gained_ground':'{draft_quote, reasoning: what reader can now conclude}'}
    if step=='orient':fields.update(conflicts_resolved='boolean',input_applications='List of {input: packet input key, quote: exact input span, use: application}')
    if step=='big-idea':fields['big_idea']='1-15 words, verbatim in artifact'
    if step in ('facts','compliance','legal','data-accuracy','judge'):
        fields.update(claim_inventory_complete='boolean',claims='List of {draft_quote, source: input:facts:N, source_quote, scope_and_caveat, verified_at: timezone-aware current verification time}. Do not fake retrieval. Offline-only evidence may require fail.',no_factual_claims_reason='Substantive reason only if claims truly absent')
    if step=='creative':fields['lenses']='Object with exactly all five named lens keys and substantive values'
    if step in ('creative','big-idea-review','ogilvy'):fields['ogilvy']='Object with exactly all five Ogilvy question keys and substantive values'
    if step in ('structure','page','positioning','clarity'):
        fields.update(paragraph_moves='List in paragraph order of {paragraph_sha256, move: structural purpose}',page_rule_scope='Explain applicability of landing-page-only rules')
    if step in ('voice','tone','judge'):
        fields.update(voice_evidence='List for every voice/register/corrections input of {input, source_quote, draft_quote, comparison}',dimensions='Object for all named voice dimensions: {score: integer 1-5, quote: exact draft span, reason}')
    if step=='judge':
        fields.update(critical_method_coverage='Object with exactly llm-patterns, ogilvy, sutherland-reframe; each {draft_quote, assessment, source: method snapshot key, source_quote}. Explicitly apply these crucial checks even if not separate topics. Do not invent an exemption.',top_fixes='List, at most three; must be empty to pass',fidelity_failures='Nonnegative integer; must be zero to pass',open_findings='List; must be empty to pass',worst_lines_assessment='Substantive judgment',overall='Integer 1-10, not author accuracy',predicted_edits='Substantive sealed edit predictions',warning_adjudications='Object keyed by warning rule ID, each {count, reviewer, reason}; unresolved human review requires fail')
    return fields

def prepare(d):
    d, s, b = load(d)
    seq=replay(s,b)
    need(len(s['receipts'])<len(seq), 'no remaining pass to prepare')
    step=seq[len(s['receipts'])]
    method_ids=required_methods(step,b)
    # Deliberately omit prior critiques, predictions and any author-final files.
    path=d / ('round-%02d-context-%s.json' % (s['round'],step))
    prepared_at=read(path)['prepared_at'] if path.exists() else dt.datetime.now(dt.timezone.utc).isoformat()
    bundle={'prepared_at':prepared_at,'schema':'writing-context/v1','step':step,'role':'reviewer' if step in REVIEW else 'writer',
            'before':artifact(s),'snapshot':s['snapshot'],'brief':b,'artifact_text':text(checked(artifact(s))),
            'methods':{sid:text(checked(s['snapshot']['method:'+sid])) for sid in method_ids},
            'inputs':{key:text(checked(ref)) for key,ref in s['snapshot'].items() if key.startswith('input:')},
            'receipt_fields':receipt_contract(step),
            'output_contract':{'voice_dimensions':policy()['voice_dimensions'],'lenses':LENSES,'ogilvy':OGILVY},
            'instruction':'Use a fresh turn and the whole piece. Apply only the named core review topic. Quote source clauses and artifact spans. Do not infer author opinions. Reviewers diagnose; they do not rewrite. Prior judge reports are withheld.'}
    path=d / ('round-%02d-context-%s.json' % (s['round'],step))
    if path.exists():
        need(read(path)==bundle, 'prepared bundle changed; do not overwrite')
    else: write(path,bundle)
    return {'state':'prepared','step':step,'context':file_ref(path)}

def record(d, receipt, _execution=None):
    d, s, b = load(d)
    seq = replay(s, b)
    need(len(s['receipts']) < len(seq), 'all passes already recorded')
    incoming=read(receipt)
    need('execution' not in incoming, 'execution provenance is runner-owned, never supplied by a receipt')
    r = validate_receipt(incoming, seq[len(s['receipts'])], s, b)
    r['execution']=_execution or {'mode':'attested'}
    dest = d / f'round-{s["round"]:02d}-{len(s["receipts"]):02d}-{r["step"]}.json'
    need(not dest.exists(), 'receipt already exists; no overwrite')
    r['recorded_at'] = dt.datetime.now(dt.timezone.utc).isoformat()
    write(dest, r)
    s['receipts'].append(file_ref(dest)); write(d / 'run.json', s)
    return state(d)

def revise(d, new_artifact, reason):
    d, s, b = load(d)
    need(nonempty(reason), 'revision must state upstream cause')
    need(s['round'] < policy()['max_rounds'], 'three rounds exhausted; escalate to author instead of polishing flat')
    # Validate artifacts even if a judgment failed; preserve failed rounds as evidence.
    for ref in s['receipts']:
        r = read(ref['path']); checked(r['before']); checked(r['after'])
    s['history'].append({'round': s['round'], 'receipts': s['receipts'], 'reason': reason, 'initial': s['initial'], 'author_seal': s.pop('author_seal',None), 'author_binding': s.pop('author_binding',None)})
    s.pop('evaluation', None)
    s['round'] += 1; s['receipts'] = []; s['initial'] = file_ref(new_artifact)
    write(d / 'run.json', s)
    return state(d)

def state(d):
    d, s, b = load(d)
    seq = replay(s, b)
    checked(artifact(s))
    if len(s['receipts']) < len(seq):
        return {'state': 'blocked', 'next': seq[len(s['receipts'])], 'round': s['round']}
    dispatched=all(read(ref['path']).get('execution',{}).get('mode')=='dispatched' for ref in s['receipts'])
    return {'state': 'process-complete' if dispatched else 'evidence-complete-attested', 'artifact': artifact(s), 'quality': 'uncalibrated',
            'next': 'author-grounded evaluation; no publication or send authority', 'round': s['round']}

def execute(d):
    d, s, b = load(d)
    seq=replay(s,b)
    need(len(s['receipts'])<len(seq), 'no remaining pass')
    step=seq[len(s['receipts'])]
    role='reviewer' if step in REVIEW else 'writer'
    adapter=policy().get('executors',{}).get(role)
    need(adapter, 'no approved production '+role+' adapter configured; cannot claim actual execution from attested receipts')
    need(nonempty(adapter.get('worker_id')), 'worker identity missing')
    command=adapter.get('command')
    need(isinstance(command,list) and command and all(isinstance(x,str) for x in command), 'executor requires a pinned argv array, never shell text')
    pins=adapter.get('pinned_files',[])
    need(pins, 'executor must pin its adapter source files')
    for pin in pins: checked(pin)
    need(Path(command[0]).is_absolute() and Path(command[0]).is_file(), 'executor binary must be an explicit local path')
    need(Path(command[0]).name not in ('sh','bash','zsh','fish','powershell'), 'shell executors are not allowed')
    entry=Path(command[1]).resolve() if len(command)>1 else Path(command[0]).resolve()
    need(str(entry) in {str(Path(pin['path']).resolve()) for pin in pins}, 'executed adapter source is not pinned')
    context=prepare(d)['context']
    invocation='writing-invocation-'+str(uuid.uuid4())
    # A new process receives only the current context packet on stdin, never prior judge reports.
    # The adapter must not resume sessions. No production adapter ships enabled here.
    confinement=adapter.get('confinement',{})
    sandbox=checked(confinement) if confinement else None
    need(sandbox and sandbox.is_absolute() and sandbox.name=='bwrap', 'executor requires pinned bubblewrap run-history confinement; cwd/stdin withholding alone is insufficient')
    # The run directory is hidden even at its absolute path; scratch is the only
    # writable host mount. Root remains read-only for installed runtime/auth.
    # This is history confinement, not a complete data/credential sandbox.
    with tempfile.TemporaryDirectory(prefix='writing-worker-') as scratch:
        isolated=[str(sandbox),'--ro-bind','/','/','--tmpfs',str(d),'--bind',scratch,scratch,'--chdir',scratch,'--unshare-pid','--die-with-parent','--']+command
        result=subprocess.run(isolated,input=text(context['path']),capture_output=True,text=True,
                              cwd=scratch,env={'PATH':os.environ.get('PATH',''),'LANG':'C.UTF-8'},
                              timeout=adapter.get('timeout_seconds',120),check=False)
        stdout=d/(invocation+'-stdout.json');stdout.write_text(result.stdout)
        stderr=d/(invocation+'-stderr.txt');stderr.write_text(result.stderr)
        need(result.returncode==0, 'worker failed; see private invocation logs, no fallback or advancement')
        incoming=json.loads(result.stdout)
        need(isinstance(incoming,dict), 'worker returned no receipt object')
        if incoming.get('after') != artifact(s):
            need(role=='writer', 'reviewer diagnoses; cannot create a replacement artifact')
            output=checked(incoming['after']).resolve()
            need(output.is_relative_to(Path(scratch).resolve()), 'new worker artifact must live in its writable scratch')
            saved=d/(invocation+'-artifact.md')
            need(not saved.exists(), 'worker artifact already preserved; no overwrite')
            shutil.copyfile(output,saved)
            need(digest(saved)==incoming['after']['sha256'], 'worker artifact changed while preserving it')
            incoming['after']=file_ref(saved)
    incoming.pop('execution',None)
    incoming['actor']=adapter['worker_id'];incoming['turn']=invocation
    incoming['source_ref']='runner dispatch '+invocation
    incoming['prepared_packet']=context;incoming['context_reset']=True
    path=d/(invocation+'-receipt.json');write(path,incoming)
    provenance={'mode':'dispatched','invocation_id':invocation,'worker_id':adapter['worker_id'],
                'pinned_files':pins,'command':command,'stdout':file_ref(stdout),'stderr':file_ref(stderr),'exit_code':result.returncode,
                'context_sha256':context['sha256'],'confinement':confinement,'isolation':'read-only root; run history hidden; private writable scratch'}
    return record(d,path,_execution=provenance)

def seal_author(d):
    need(state(d)['state']=='process-complete', 'dispatch and all passes must finish before sealing author feedback')
    d,s,b=load(d)
    pair=d/('author-round-%02d' % s['round'])
    need(not pair.exists(), 'author pair already exists; no overwrite or resealing')
    pair.mkdir()
    judge=read(s['receipts'][-1]['path'])
    shutil.copyfile(checked(artifact(s)),pair/'draft.md')
    (pair/'predictions.md').write_text(judge['predicted_edits'])
    sys.path.insert(0,str(ROOT/'scripts/local/voice'))
    import ledger
    result=ledger.seal(pair)
    need(result.startswith('SEALED'),result)
    s['author_seal']={name:file_ref(pair/name) for name in ('draft.md','predictions.md','SEAL.txt')}
    s['author_binding']={'round':s['round'],'artifact':artifact(s)}
    write(d/'run.json',s)
    return {'state':'sealed-before-author-edit','evidence':s['author_seal'],'next':'author edits; preserve original-channel provenance and independent hunk classification'}

def score_author(d, final, classes, provenance):
    need(state(d)['state']=='process-complete', 'complete current round before author feedback')
    d,s,b=load(d)
    need(s.get('author_binding')=={'round':s['round'],'artifact':artifact(s)}, 'author seal not bound to current round/artifact')
    need(s.get('author_seal'), 'seal predictions and draft before importing an author final')
    for ref in s['author_seal'].values(): checked(ref)
    pair=Path(s['author_seal']['draft.md']['path']).parent
    need(not (pair/'final.md').exists(), 'author final already imported; no overwrite')
    file_ref(final);file_ref(classes);file_ref(provenance)
    proof=read(provenance)
    for key in ('original_feedback_id','identity_checked_by','independent_classifier'):
        need(nonempty(proof.get(key)), 'author feedback lacks '+key)
    quote(proof['original_evidence'],proof.get('evidence_quote'))
    sealed=re.search(r'sealed:\s*(\S+)',text(pair/'SEAL.txt')).group(1)
    authored=dt.datetime.fromisoformat(proof['author_edit_at'])
    need(authored.tzinfo is not None and dt.datetime.fromisoformat(sealed)<=authored<=dt.datetime.now(dt.timezone.utc), 'author edit predates seal or is in future')
    writers={read(ref['path'])['actor'] for ref in s['receipts'] if read(ref['path'])['step'] not in REVIEW}
    need(proof['independent_classifier'] not in writers, 'writer cannot independently classify its own edits')
    sys.path.insert(0,str(ROOT/'scripts/local/voice'))
    import ledger
    with tempfile.TemporaryDirectory(prefix='author-import-check-') as scratch:
        candidate=Path(scratch)
        for name in ('draft.md','predictions.md','SEAL.txt'): shutil.copyfile(pair/name,candidate/name)
        shutil.copyfile(final,candidate/'final.md');shutil.copyfile(classes,candidate/'classes.md')
        # Imported chronology comes from checked original provenance, not copy-time filesystem precision.
        os.utime(candidate/'final.md',(authored.timestamp(),authored.timestamp()))
        need(proof.get('final_sha256')==digest(candidate/'final.md'), 'author evidence does not bind the imported final')
        metrics,failures=ledger.score(candidate)
        if failures:
            attempt=d/('author-import-failed-'+str(uuid.uuid4())+'.json')
            write(attempt,{'state':'blocked-author-evaluation','failures':failures,'final_sha256':digest(candidate/'final.md'),'classes_sha256':digest(candidate/'classes.md')})
            return {'state':'blocked-author-evaluation','failures':failures,'attempt':file_ref(attempt),'quality_pass':False}
        shutil.copyfile(candidate/'final.md',pair/'final.md')
        shutil.copyfile(candidate/'classes.md',pair/'classes.md')
    report={'state':'blocked-author-evaluation' if failures else 'author-feedback-recorded',
            'edit_metrics':metrics,'failures':failures,'provenance_status':'imported and independently attested, not authenticated by a local file',
            'evidence':{'final':file_ref(pair/'final.md'),'classes':file_ref(pair/'classes.md'),'provenance':file_ref(provenance),'original':proof['original_evidence']},
            'quality_pass':False,'next':'compound scoped candidate rules; no publication or graduation from these numbers'}
    write(pair/'author-evaluation.json',report)
    return report

def evaluation(d, dataset):
    need(state(d)['state']=='process-complete', 'process incomplete; evaluation cannot replace required passes')
    d, s, b = load(d)
    sys.path.insert(0, str(ROOT / 'scripts/local/voice'))
    from evaluate import evaluate
    data=read(dataset)
    need(data.get('register')==b['register'], 'calibration register differs from the writing run')
    binding=data.get('run_binding',{})
    snap_hash=hashlib.sha256(json.dumps(s['snapshot'],sort_keys=True).encode()).hexdigest()
    need(binding.get('artifact_sha256')==artifact(s)['sha256'] and binding.get('snapshot_sha256')==snap_hash, 'evaluation is unrelated to the current artifact or frozen process')
    expected={k:v['sha256'] for k,v in s['snapshot'].items() if any(k.startswith('input:'+role+':') for role in ('voice','register','corrections'))}
    need(binding.get('voice_source_hashes')==expected, 'evaluation guide lineage differs from selected voice sources')
    for role in ('writer_version','judge_version','settings_version'):
        need(nonempty(data.get(role)), 'evaluation lacks frozen '+role)
    result = evaluate(dataset)
    result['artifact'] = artifact(s)
    dest=d / ('evaluation-round-%02d.json' % s['round'])
    need(not dest.exists(), 'evaluation already exists; preserve it, do not retune on test')
    write(dest, result); s['evaluation']=file_ref(dest); write(d/'run.json',s)
    return result

def packet(d, destination):
    status = state(d)
    need(status['state'] == 'process-complete', 'required work incomplete; no handoff packet')
    d, s, b = load(d)
    # This command cannot label a piece final or authorize sending it.
    evalref=s.get('evaluation')
    if evalref:
        ev=read(checked(evalref))
        need(ev['artifact']==artifact(s), 'evaluation is for a different artifact')
        for ref in ev['evidence']: checked(ref)
    result = dict(status, evaluation=evalref, state='draft-for-author-evaluation', scope=b['scope'], review_plan=b['review_plan'],
                  critical_review_coverage={topic:any(x['topic'] in covers for x in b['review_plan']) for topic,covers in {'llm-patterns':['decontaminate'],'ogilvy':['ogilvy','creative','big-idea-review'],'sutherland-reframe':['creative']}.items()},
                  author_guideline_overlay=(b['scope']=='personal' or b.get('author_guideline_overlay') is True), author_overlay_reason=b.get('author_overlay_reason'),
                  limitations=['Mechanical evidence cannot certify taste, voice or semantic relevance.',
                               'Turn IDs and source references are auditable declarations, not authenticated identities.',
                               'Author calibration and exact final approval remain required.'],
                  evidence={k: v['sha256'] for k,v in s['snapshot'].items()},
                  receipt_hashes=[r['sha256'] for r in s['receipts']])
    out = Path(destination).resolve()
    need(not out.is_relative_to(ROOT.parent), 'packet may contain private data; keep outside repo')
    need(not out.exists(), 'packet already exists; no overwrite')
    write(out, result)
    return result

def readiness():
    cfg = policy()
    missing = [role for role in ('writer', 'reviewer') if not cfg.get('executors', {}).get(role)]
    return {'state': 'blocked-production' if missing or not cfg['new_voice_writing_enabled'] else 'host-conformance-required',
            'missing_executor_roles': missing, 'author_writing_hold': not cfg['new_voice_writing_enabled'],
            'host_verified': False, 'quality': 'uncalibrated',
            'manual_path': 'Supervised stages may be documented honestly outside dispatched execution; never claim software process completion.',
            'next': 'Resolve actual host conformance and source-grounded scope, not an activation flag flip.'}

def main():
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest='cmd', required=True)
    sub.add_parser('readiness')
    for cmd in ('init', 'record', 'status', 'prepare', 'execute', 'revise', 'packet', 'evaluate', 'seal-author', 'score-author'):
        c = sub.add_parser(cmd); c.add_argument('directory')
        if cmd == 'init': c.add_argument('--brief', required=True)
        if cmd == 'record': c.add_argument('--receipt', required=True)
        if cmd == 'evaluate': c.add_argument('--dataset', required=True)
        if cmd == 'score-author':
            c.add_argument('--final',required=True);c.add_argument('--classes',required=True);c.add_argument('--provenance',required=True)
        if cmd == 'revise': c.add_argument('--artifact', required=True); c.add_argument('--reason', required=True)
        if cmd == 'packet': c.add_argument('--output', required=True)
    a = p.parse_args()
    try:
        if a.cmd == 'readiness': result = readiness()
        elif a.cmd == 'init': result = init(a.directory, a.brief)
        elif a.cmd == 'record': result = record(a.directory, a.receipt)
        elif a.cmd == 'prepare': result = prepare(a.directory)
        elif a.cmd == 'execute': result = execute(a.directory)
        elif a.cmd == 'revise': result = revise(a.directory, a.artifact, a.reason)
        elif a.cmd == 'packet': result = packet(a.directory, a.output)
        elif a.cmd == 'evaluate': result = evaluation(a.directory, a.dataset)
        elif a.cmd == 'seal-author': result = seal_author(a.directory)
        elif a.cmd == 'score-author': result = score_author(a.directory,a.final,a.classes,a.provenance)
        else: result = state(a.directory)
        print(json.dumps(result, indent=2))
        if a.cmd in ('init','record','execute','revise'):
            return 0  # Successful transition; JSON states remaining work explicitly.
        return 1 if result['state'] in ('blocked', 'blocked-production', 'host-conformance-required', 'calibration-insufficient', 'evidence-complete-attested', 'blocked-author-evaluation') else 0
    except (Block, KeyError, TypeError, ValueError, OSError, subprocess.SubprocessError) as e:
        print(json.dumps({'state': 'blocked', 'reason': str(e)})); return 1
if __name__ == '__main__':
    sys.exit(main())
