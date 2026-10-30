"""Compute voice-spec metrics from corpus/raw ONLY. Usage: build_spec.py [corpus_dir] > json"""
import sys,glob,json,os,hashlib,statistics as st
sys.path.insert(0,os.path.dirname(__file__)); from vlib import *
root=sys.argv[1] if len(sys.argv)>1 else os.path.join(os.path.dirname(__file__),'..','..','..','assets','voice-corpus')
files=sorted(glob.glob(os.path.join(root,'raw','*.md')))
assert files and not any('holdout' in f for f in files)
import datetime
HALF_LIFE_MONTHS=12.0  # recency weighting: a piece 12 months older than the newest counts half as much
dates={os.path.basename(f):datetime.date.fromisoformat(os.path.basename(f)[:10]) for f in files}
newest=max(dates.values())
W={k:0.5**(((newest-d).days/30.4375)/HALF_LIFE_MONTHS) for k,d in dates.items()}
per={}
for f in files:
    t=body(f); fp,n=func_profile(t); ls=sent_lens(t)
    paras=paragraphs(t); psl=[len(sentences(p)) for p in paras]
    per[os.path.basename(f)]={'words':n,'sha1':hashlib.sha1(open(f,'rb').read()).hexdigest()[:10],
      'sent_mean':st.mean(ls),'sent_median':st.median(ls),'sent_sd':st.pstdev(ls),'sent_n':len(ls),
      'sent_lt8_share':sum(l<8 for l in ls)/len(ls),'sent_gt25_share':sum(l>25 for l in ls)/len(ls),'sent_gt32_share':sum(l>32 for l in ls)/len(ls),
      'para_n':len(paras),'para_sent_mean':st.mean(psl),'para_1sent_share':sum(x==1 for x in psl)/len(psl),'para_5plus_share':sum(x>=5 for x in psl)/len(psl),
      'punct':punct(t),'lex':lexical(t),'func':fp}
def agg(get):
    d=dist([get(v) for v in per.values()])
    ks=list(per); vals=[get(per[k]) for k in ks]; ws=[W[k] for k in ks]; tw_=sum(ws)
    wm=sum(v*w for v,w in zip(vals,ws))/tw_
    d['wmean']=wm; d['wsd']=(sum(w*(v-wm)**2 for v,w in zip(vals,ws))/tw_)**0.5
    return d
spec={'weighting':{'method':'exponential recency, half-life %.0f months, relative to newest raw piece (%s)'%(HALF_LIFE_MONTHS,newest),'weights':{k:round(w,3) for k,w in W.items()},'applies_to':'wmean and wsd (piece-level mean and between-piece sd). min/max range stays unweighted across all raw pieces. Pooled sentence distribution is weighted by piece weight.'},'files':{k:{'words':v['words'],'sha1':v['sha1']} for k,v in per.items()},'metrics':{}}
M=spec['metrics']
for k in ['sent_mean','sent_median','sent_sd','sent_lt8_share','sent_gt25_share','sent_gt32_share','para_sent_mean','para_1sent_share','para_5plus_share']:
    M[k]=agg(lambda v,k=k:v[k])
for grp in ['punct','lex']:
    for k in next(iter(per.values()))[grp]:
        M[grp+'.'+k]=agg(lambda v,g=grp,k=k:v[g][k])
M2={}
for w in FUNC: M2[w]=agg(lambda v,w=w:v['func'][w])
spec['function_words']=M2
# pooled sentence lengths
allls=[]; allw=[]
for f in files:
    l=sent_lens(body(f)); allls+=l; allw+=[W[os.path.basename(f)]]*len(l)
spec['pooled_sentence_length']=dist(allls); spec['pooled_sentence_count']=len(allls)
sw=sorted(zip(allls,allw)); tot=sum(w for _,w in sw); acc=0; wq={}
for v,w in sw:
    acc+=w
    for q in (.1,.5,.9):
        if q not in wq and acc/tot>=q: wq[q]=v
spec['pooled_sentence_length_weighted']={'mean':sum(v*w for v,w in sw)/tot,'p10':wq[.1],'median':wq[.5],'p90':wq[.9]}
spec['pooled_words']=sum(v['words'] for v in per.values())
print(json.dumps(spec,indent=1))
