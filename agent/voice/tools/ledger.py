"""Sealed edit predictions and the trust metric. Stdlib only.
A piece folder holds: draft.md, predictions.md (written by the judge BEFORE he sees the draft), SEAL.txt, final.md (his edit), classes.md.
  ledger.py seal DIR    needs predictions.md and NO final.md yet. Writes SEAL.txt (sha256 + time).
  ledger.py score DIR   checks the seal, then reads classes.md and writes ledger.md.
  ledger.py batch DIR... [-- DIR...]   edit rate and predicted share per batch, to see whether an update helped.
classes.md has one line per hunk from `edit_rate.py draft final --hunks`:  H<n> | <bucket> | predicted: yes|no | note
buckets: voice-rule, structure, fidelity, banned-phrase.
Deciding 'predicted' and the bucket is a judgment step. A reviewer other than the writer does it and he can audit it.
The metric says when he may step out of the loop. It never certifies a draft as his."""
import sys,os,re,json,hashlib,datetime
sys.path.insert(0,os.path.dirname(__file__)); from edit_rate import measure
BUCKETS=('voice-rule','structure','fidelity','banned-phrase')
def sha(p): return hashlib.sha256(open(p,'rb').read()).hexdigest()
def seal(d):
    p=os.path.join(d,'predictions.md')
    if not os.path.exists(p): return 'FAIL: predictions.md missing'
    if os.path.exists(os.path.join(d,'final.md')): return 'FAIL: final.md already exists; predictions cannot be sealed after his edit'
    t=datetime.datetime.now(datetime.timezone.utc).isoformat()
    open(os.path.join(d,'SEAL.txt'),'w').write(f'sha256: {sha(p)}\nsealed: {t}\n'); return 'SEALED '+t
def parse_classes(path):
    rows={}
    for l in open(path).read().splitlines():
        m=re.match(r'H(\d+)\s*\|\s*([\w-]+)\s*\|\s*predicted:\s*(yes|no)\b',l)
        if m: rows[int(m.group(1))]=(m.group(2),m.group(3))
    return rows
def score(d):
    probs=[]; sp=os.path.join(d,'SEAL.txt')
    if not os.path.exists(sp): return None,['no SEAL.txt: predictions were never sealed']
    s=open(sp).read(); h=re.search(r'sha256:\s*(\w+)',s).group(1); t=re.search(r'sealed:\s*(\S+)',s).group(1)
    if sha(os.path.join(d,'predictions.md'))!=h: probs.append('predictions.md changed after sealing')
    fp=os.path.join(d,'final.md')
    if not os.path.exists(fp): return None,probs+['final.md missing']
    if datetime.datetime.fromtimestamp(os.path.getmtime(fp),datetime.timezone.utc)<datetime.datetime.fromisoformat(t): probs.append('final.md is older than the seal')
    m=measure(os.path.join(d,'draft.md'),fp); rows=parse_classes(os.path.join(d,'classes.md')) if os.path.exists(os.path.join(d,'classes.md')) else {}
    ids={x['n'] for x in m['hunks']}
    for n in sorted(ids-set(rows)): probs.append(f'hunk H{n} has no class line')
    for n,(b,_) in rows.items():
        if b not in BUCKETS: probs.append(f'H{n}: unknown bucket {b}')
        if n not in ids: probs.append(f'H{n}: no such hunk')
    by={b:sum(1 for x in rows.values() if x[0]==b) for b in BUCKETS}; pred=sum(1 for x in rows.values() if x[1]=='yes')
    res={'rate':m['rate'],'hunks':len(ids),'by_bucket':by,'predicted':pred,'predicted_share':round(pred/len(ids),3) if ids else None}
    return res,probs
def main(a):
    if a[0]=='seal': print(seal(a[1])); return 0
    if a[0]=='score':
        r,p=score(a[1])
        if r:
            open(os.path.join(a[1],'ledger.md'),'w').write('# Ledger\n'+json.dumps(r,indent=1)+'\n'+''.join(f'- PROBLEM: {x}\n' for x in p))
            print(json.dumps(r))
        for x in p: print('PROBLEM:',x)
        return 1 if p else 0
    if a[0]=='batch':
        groups=[[]]
        for x in a[1:]:
            if x=='--': groups.append([])
            else: groups[-1].append(x)
        bad=0
        for i,g in enumerate(groups,1):
            rs=[]
            for d in g:
                r,p=score(d); bad+=bool(p)
                if r: rs.append(r)
            if rs:
                mr=sum(x['rate'] for x in rs)/len(rs); ps=[x['predicted_share'] for x in rs if x['predicted_share'] is not None]
                print(f"batch {i}: pieces={len(rs)} mean_edit_rate={mr*100:.1f}% mean_predicted_share={(sum(ps)/len(ps)*100 if ps else 0):.0f}%")
        return 1 if bad else 0
    print(__doc__); return 2
if __name__=='__main__': sys.exit(main(sys.argv[1:]))
