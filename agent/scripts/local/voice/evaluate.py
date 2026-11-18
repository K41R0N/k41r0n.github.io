"""Author-grounded pair evaluation. Offline, no judge calls, no random fallback.

This validates imported evidence and computes agreement. It cannot authenticate a
local file's author. The caller must verify original-channel provenance before
importing labels. Defaults deliberately have NO quality-pass threshold.
"""
from pathlib import Path
import hashlib
import json
import math
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from writing import Block, need, read, file_ref, checked, quote, nonempty, policy


def evaluate(dataset_path):
    dataset_path = Path(dataset_path).resolve()
    d = read(dataset_path)
    need(d.get('schema') == 'author-eval/v1', 'unknown author evaluation schema')
    need(d.get('provenance_reviewed') is True, 'original-channel label provenance has not been reviewed')
    need(nonempty(d.get('provenance_reviewer')) and nonempty(d.get('label_import_source')), 'label importer/source missing')
    # Reference and candidate sets are immutable and disjoint by BOTH ID and bytes.
    splits = d.get('splits', {})
    need(set(splits) == {'train', 'calibration', 'test'}, 'explicit train/calibration/test partitions required')
    seen_ids = set(); seen_hashes = set(); split_cases = {}
    for split, cases in splits.items():
        need(isinstance(cases, list) and cases, f'empty {split} split')
        local_ids = set(); local_hashes = set()
        for case in cases:
            need(case['id'] not in seen_ids and case['id'] not in local_ids, 'case ID leaks across splits or duplicated')
            need(case.get('exposure') == ('unseen-test' if split == 'test' else split), 'spent or relabeled holdout')
            need(case['register'] == d['register'], 'mixed register evaluation')
            local_ids.add(case['id'])
            for ref in case['artifacts']:
                checked(ref)
                need(ref['sha256'] not in seen_hashes, 'same content leaks across splits')
                need(ref['sha256'] not in local_hashes, 'duplicate candidate inflates case count within split')
                local_hashes.add(ref['sha256'])
        seen_ids |= local_ids; seen_hashes |= local_hashes
        split_cases[split] = {c['id']:c for c in cases}
    used = d.get('guide_inputs', [])
    need(used and all(x in split_cases['train'] for x in used), 'guide may use training cases only')
    need(not (set(d.get('prior_exposed_ids', [])) & set(split_cases['test'])), 'test was previously exposed')
    need(not (set(d.get('prior_exposed_hashes', [])) & {r['sha256'] for c in split_cases['test'].values() for r in c['artifacts']}), 'test bytes were previously exposed')
    refs = [file_ref(dataset_path), file_ref(checked(d['guide'])), file_ref(checked(d['rubric']))]
    out = {}
    for split in ('calibration', 'test'):
        cases = split_cases[split]
        labels = d.get('labels', {}).get(split, [])
        predictions = d.get('predictions', {}).get(split, [])
        need({x['case'] for x in labels} == set(cases) and len(labels)==len(cases), f'{split}: incomplete or duplicate labels')
        need({x['case'] for x in predictions} == set(cases) and len(predictions)==len(cases), f'{split}: incomplete or duplicate predictions')
        labels = {x['case']:x for x in labels}; predictions = {x['case']:x for x in predictions}
        agree=0; inconsistent=0; abstentions=0; n=len(cases); sqerr=0.0
        for cid, case in cases.items():
            label=labels[cid]; pred=predictions[cid]
            choices={a['sha256'] for a in case['artifacts']}
            need(len(choices)==2, 'pair must contain two distinct candidates')
            choices.add('tie')
            need(label.get('choice') in choices, 'invalid author label')
            need(nonempty(label.get('original_message_id')), 'author choice lacks original-channel reference')
            quote(label['evidence'],label.get('evidence_quote'))
            need(nonempty(label.get('reason')), 'author preference reason required')
            refs += [file_ref(checked(label['evidence']))] + case['artifacts']
            need(pred.get('guide_sha256')==d['guide']['sha256'] and pred.get('rubric_sha256')==d['rubric']['sha256'], 'prediction uses stale guide/rubric')
            orders=pred.get('orders',[])
            need(len(orders)==2 and all(isinstance(o.get('order'),list) and len(o['order'])==2 for o in orders) and orders[0]['order']==list(reversed(orders[1]['order'])) and set(orders[0]['order'])==choices-{'tie'}, 'both blinded orders required')
            for o in orders:
                need(o.get('choice') in choices|{'abstain'}, 'invalid judgment; never use random fallback')
                need(nonempty(o.get('rationale')), 'judgment needs rationale')
                need(isinstance(o.get('confidence'),(float,int)) and not isinstance(o['confidence'],bool) and math.isfinite(o['confidence']) and 0<=o['confidence']<=1, 'invalid confidence')
                quote(o['evidence'], o.get('evidence_quote')); refs.append(o['evidence'])
            a,b=orders
            inconsistent += a['choice']!=b['choice']
            abstentions += a['choice']=='abstain' or b['choice']=='abstain'
            right=(a['choice']==b['choice']==label['choice'])
            agree += right
            sqerr += (a['confidence']-int(a['choice']==label['choice']))**2
        # Wilson interval conveys small-sample uncertainty, not voice accuracy.
        phat=agree/n; z=1.96; den=1+z*z/n
        center=(phat+z*z/(2*n))/den
        half=z*((phat*(1-phat)/n+z*z/(4*n*n))**0.5)/den
        out[split]={'cases':n,'both_orders_agree_with_author':agree,'agreement':phat,
                    'agreement_wilson95':[max(0,center-half),min(1,center+half)],
                    'order_inconsistency':inconsistent/n,'abstention_cases':abstentions,
                    'brier_first_order':sqerr/n}
    limits=policy()['calibration']
    configured=all(limits.get(k) is not None for k in ('min_author_cases','minimum_agreement','maximum_position_inconsistency'))
    passed=configured and all(m['cases']>=limits['min_author_cases'] and m['agreement']>=limits['minimum_agreement'] and m['order_inconsistency']<=limits['maximum_position_inconsistency'] and m['abstention_cases']==0 for m in out.values())
    return {'schema':'author-eval-result/v1','state':'shadow-pass' if passed else 'calibration-insufficient',
            'quality_pass':False,'mode':limits['mode'],'metrics':out,'evidence':refs,
            'thresholds':limits,'limitations':'Imported-label provenance must be verified outside this evaluator; resemblance agreement is not publish approval or writing accuracy.'}

if __name__=='__main__':
    try:
        result=evaluate(sys.argv[1]); print(json.dumps(result,indent=2)); sys.exit(0 if result['state']=='shadow-pass' else 1)
    except (Block,ValueError,KeyError,TypeError,OSError,IndexError) as e:
        print(json.dumps({'state':'blocked','reason':str(e)})); sys.exit(1)
