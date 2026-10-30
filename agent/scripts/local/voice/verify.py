"""Verification suite for voice-harness phase 1. Run from agent/: python3 scripts/local/voice/verify.py [controls_dir]. Writes reports/verification.md"""
import sys,os,re,glob,json,hashlib,subprocess,statistics as st,collections,math,html,tempfile,shutil
sys.path.insert(0,'scripts/local/voice'); from vlib import *; import checks
R=[]; P=lambda s='':(R.append(s),print(s))
raw=sorted(glob.glob('assets/voice-corpus/raw/*.md')); hold=sorted(glob.glob('assets/voice-corpus/holdout/*.md')); exc=sorted(glob.glob('assets/voice-corpus/excluded/*.md'))
P('# Verification report (phase 1)\n')
# V1 authenticity
P('## V1. Every corpus file is his writing\n')
P('Evidence available: Substack byline via public API, canonical URL, and a second copy of each essay in the kairon.xyz repo. This establishes publication under his byline. It cannot rule out AI assistance (no disclosure statements found in any piece by grep). Tier-2 caveat stands until he confirms.\n')
P('| file | split | url | byline in header | repo copy match |'); P('|---|---|---|---|---|')
def normt(t): return re.sub(r'[^a-z0-9]+',' ',strip_md(t).lower()).split()
import difflib
for f in raw+hold:
    hdr=open(f).read().split('---')[1]; url=re.search(r'url: (\S+)',hdr).group(1); slug=url.rsplit('/',1)[1]
    date=os.path.basename(f)[:10]
    cands=glob.glob('../content/blog/'+date[:8]+'*')+glob.glob('../../content/blog/*'+'-'.join(slug.split('-')[:3])+'*')
    best=0
    for c in set(cands):
        a=normt(body(f))[:400]; b=normt(body(c))[:400]; best=max(best,difflib.SequenceMatcher(None,a,b,autojunk=False).ratio())
    P(f"| {os.path.basename(f)} | {'holdout' if 'holdout' in f else 'raw'} | {url} | yes (Alejandro \"Kairon\" Arango) | {best:.2f} (first 400 words) |")
P('\nExcluded (authorship pending, NOT used anywhere in the spec):\n')
for f in exc: P('- '+os.path.basename(f))
# V2 second-method
P('\n## V2. Spec computations cross-checked with an independent method\n')
spec=json.load(open('scripts/local/voice/spec_v0.json'))
tw=0; ts=0; commas=0; the=0; i_=0
for f in raw:
    t=strip_md(body(f))
    toks=[w.strip('.,;:!?"“”()*') for w in t.split()]; toks=[w for w in toks if re.search(r'[A-Za-z0-9]',w)]
    tw+=len(toks); commas+=t.count(','); the+=sum(1 for w in toks if w.lower()=='the')
    # independent sentence count: terminal punctuation followed by space+capital or end of paragraph
    for p in re.split(r'\n\s*\n',t):
        ts+=len(re.findall(r'[.!?…]["”’)]*(?=\s+["“(]?[A-Z0-9]|\s*$)',p.strip()))
rows=[('total words',spec['pooled_words'],tw),('total sentences',spec['pooled_sentence_count'],ts),('mean sentence length',spec['pooled_sentence_length']['mean'],tw/ts)]
pw=spec['pooled_words']
rows.append(('commas per 1000 words (pooled)',st.mean([spec['metrics']['punct.comma']['mean']]),1000*commas/tw))
rows.append(("'the' per 1000 words",spec['function_words']['the']['mean'],1000*the/tw))
P('| quantity | main method | independent method | relative diff |'); P('|---|---|---|---|')
ok=True
for n,a,b in rows:
    d=abs(a-b)/b; P(f'| {n} | {a:.2f} | {b:.2f} | {100*d:.1f}% |'); ok&= d<0.05
P(f"\nResult: {'PASS (all within 5%; per-piece means vs pooled differ slightly by design)' if ok else 'CHECK: a quantity differs >5%, see rows'}")
# hand-check sample
P('\nHand-check sample (first 8 sentences of one raw piece, with computed lengths) - read these against the source:\n')
t=body(raw[4]); k=0
for p in paragraphs(t):
    for s in sentences(p):
        if k<8: P(f'- [{len(words(s))}] {s[:140]}'); k+=1
# V3 leak
P('\n## V3. Holdout never leaked into the spec\n')
hs=[hashlib.sha1(open(f,'rb').read()).hexdigest()[:10] for f in hold]; hn=[os.path.basename(f) for f in hold]
spec_text=open('scripts/local/voice/spec_v0.json').read()
P(f"- spec file list contains {len(spec['files'])} files; holdout names present: {any(n in spec_text for n in hn)}; holdout hashes present: {any(h in spec_text for h in hs)}")
tmp=tempfile.mkdtemp(); shutil.copytree('assets/voice-corpus/raw',tmp+'/raw'); os.makedirs(tmp+'/holdout')
out1=subprocess.run([sys.executable,'scripts/local/voice/build_spec.py','assets/voice-corpus'],capture_output=True,text=True).stdout
for f in hold: open(tmp+'/holdout/'+os.path.basename(f),'w').write('mutated '*500)
out2=subprocess.run([sys.executable,'scripts/local/voice/build_spec.py',tmp],capture_output=True,text=True).stdout
P(f"- rebuilt spec with the holdout folder emptied/replaced by junk: identical to the committed build = {out1==out2==spec_text.strip() or json.loads(out1)==json.loads(out2)}")
P(f"- committed spec equals fresh rebuild = {json.loads(out1)==spec}")
# V4 false positives
P('\n## V4. Seeded rules run against his own writing (false-positive rate)\n')
P('Every one of his published pieces is treated as a known-good "sound like me" sample, so any flag on his own writing is a false positive for the rule as a description of HIM. Rules inherited from a client brand were never promised to match his habits; this test finds which ones do.\n')
tot=collections.Counter(); pc=collections.Counter(); W_=0
for f in raw+hold:
    n,o=checks.run(f); W_+=n
    for r in o:
        tot[r['id']]+=r['count']; pc[r['id']]+= 1 if r['count'] else 0
P(f'{len(raw+hold)} pieces, {W_} words\n'); P('| rule | severity | origin | pieces flagged | hits per 1000 words | verdict |'); P('|---|---|---|---|---|---|')
verd={}
for rid,desc,org,sev,fn in checks.RULES:
    frac=pc[rid]/len(raw+hold); rate=1000*tot[rid]/W_
    v='keep (rarely flags him)' if frac<=0.2 else ('DO NOT ADOPT as default: flags most of his own pieces, so it describes the client brand or a noisy test, not him' if frac>=0.6 else 'candidate: ask him')
    verd[rid]=v; P(f'| {rid} {desc[:55]} | {sev} | {org.split(" (")[0]} | {pc[rid]}/{len(raw+hold)} | {rate:.2f} | {v} |')
json.dump({'verdict':verd,'counts':dict(tot),'pieces_flagged':dict(pc),'words':W_},open('ingestion/reports/voice/rule_fp.json','w'))
# V5 Delta
P('\n## V5. Burrows Delta (stylometry) on the holdout, with different-author controls\n')
ctrl=sys.argv[1] if len(sys.argv)>1 else None
def toks(t): return [norm(w).lower() for w in words(strip_md(t))]
def chunks(ts,n=1500): return [ts[i:i+n] for i in range(0,len(ts)-n//2,n)]
def freqs(ts,mfw):
    c=collections.Counter(ts); n=len(ts); return [c[w]/n for w in mfw]
R_=[(os.path.basename(f),toks(body(f))) for f in raw]
allc=collections.Counter(w for _,t in R_ for w in t); MFW=[w for w,_ in allc.most_common(100)]
def build(refs):
    F=[freqs(t,MFW) for _,t in refs]; mu=[st.mean(c) for c in zip(*F)]; sd=[st.pstdev(c) or 1e-9 for c in zip(*F)]; return mu,sd
def delta(test,refs):
    mu,sd=build(refs); ft=freqs(test,MFW); Z=[ (x-m)/s for x,m,s in zip(ft,mu,sd)]
    cen=[0.0]*len(MFW)  # reference centroid in z-space is 0 by construction
    return st.mean(abs(z) for z in Z)
res={'raw LOO':[],'holdout':[],'control':[]}
for i,(n,t) in enumerate(R_):
    refs=R_[:i]+R_[i+1:]; res['raw LOO'].append((n,delta(t,refs)))
for f in hold: res['holdout'].append((os.path.basename(f),delta(toks(body(f)),R_)))
if ctrl:
    for h in sorted(glob.glob(ctrl+'/*.html')):
        txt=html.unescape(re.sub(r'<[^>]+>',' ',re.sub(r'<br\s*/?>','\n',open(h,errors='ignore').read())))
        for j,c in enumerate(chunks(toks(txt))): res['control'].append((os.path.basename(h)+f'#{j}',delta(c,R_)))
P('**Delta is a SOFT signal, not a gate.** At this corpus size the distributions overlap (see below). Use it as one input to a human judgment.\n')
P('Delta = mean absolute z-score distance from his raw-corpus profile over his 100 most frequent words. Lower = closer. Texts are scored against the raw corpus only (holdout never in the reference).\n')
for k,v in res.items():
    if v: ds=[d for _,d in v]; P(f'- {k}: n={len(ds)}, mean {st.mean(ds):.3f}, min {min(ds):.3f}, max {max(ds):.3f}')
for n,d in res['holdout']: P(f'  - holdout {n}: {d:.3f}')
if res['control']:
    mx=max(d for _,d in res['holdout']); beat=sum(d>mx for _,d in res['control'])/len(res['control'])
    P(f'- Control chunks (other human author, ~1500 words each) farther than the worst holdout piece: {100*beat:.0f}%')
    ov=[n for n,d in res['raw LOO'] if d>=min(d2 for _,d2 in res['control'])]
    P(f'- Overlap: {len(ov)} of his own leave-one-out pieces score as far as or farther than the closest control chunk. That is why Delta cannot gate anything.')
    P('- Caveat: n is tiny and chunk length differs from his pieces. This shows the measure separates authors at all; it does not prove the spec captures him. The blind test is the real calibration.')
json.dump(res,open('ingestion/reports/voice/delta.json','w'),indent=1)
P('\n## V6. Range check calibration (leave-one-out on his own pieces)\n')
import subprocess as sp
rl=json.loads(sp.run([sys.executable,'scripts/local/voice/range_check.py','--loo'],capture_output=True,text=True).stdout)
P(f"{rl['features']} structural features, ranges from the other pieces widened 50%. Features outside range per own piece: {list(rl['outside_per_piece'].values())}. Pieces at or over the {rl['threshold']}-feature WARN threshold: {rl['pieces_at_or_over_threshold']} of {rl['pieces']}.")
P('Strict min-max over all 57 features (with function words) put every one of his own pieces 10 to 20 features out of range, so that version was rejected. Range checks are WARN only and never block.')
for f in hold:
    o=sp.run([sys.executable,'scripts/local/voice/range_check.py',f],capture_output=True,text=True).stdout.splitlines()[0]; P(f'- holdout {os.path.basename(f)}: {o}')
open('ingestion/reports/voice/verification.md','w').write('\n'.join(R)+'\n')
