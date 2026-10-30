"""Range check: WARN-level only. Compares a draft's features with his own min-max across raw pieces.
Features: 25 structural/punctuation/pronoun/discourse rates (no function words). Usage: range_check.py draft.md        (against corpus/raw)
       range_check.py --loo           (leave-one-out evaluation on his own pieces, writes reports/range_loo.json)
A single feature outside range is normal even for his own pieces (see --loo). Flag only at THRESHOLD or more features out. Never blocks."""
import sys,os,glob,json,statistics as st
sys.path.insert(0,os.path.dirname(__file__)); from vlib import *
THRESHOLD=3
WIDEN=0.5  # ranges widened by 50% of min-max span each side; chosen from the leave-one-out test, see reports/range_loo.json
def feats(text):
    ls=sent_lens(text); ps=[len(sentences(p)) for p in paragraphs(text)]; fp,_=func_profile(text)
    f={'sent_mean':st.mean(ls),'sent_sd':st.pstdev(ls),'sent_lt8_share':sum(l<8 for l in ls)/len(ls),'sent_gt25_share':sum(l>25 for l in ls)/len(ls),
       'para_sent_mean':st.mean(ps),'para_1sent_share':sum(x==1 for x in ps)/len(ps)}
    for k,v in punct(text).items():
        if k in('comma','semicolon','colon','question','contraction','paren_open','oxford_comma_per_1000'): f['punct.'+k]=v
    for k,v in lexical(text).items():
        if k in('mattr500','first_person_I_per_1000','second_person_you_per_1000','we_per_1000','disc_but_per_1000','disc_and_per_1000','disc_so_per_1000','disc_actually_per_1000','disc_really_per_1000','disc_still_per_1000','sent_start_but_share','sent_start_and_share'): f['lex.'+k]=v
    for w in []: #function words are excluded: too noisy at this corpus size, they live in the Delta soft signal
      pass
    for w in []: f['fw.'+w]=fp[w]
    return f
def ranges(files):
    F=[feats(body(f)) for f in files]
    r={}
    for k in F[0]:
        lo=min(x[k] for x in F); hi=max(x[k] for x in F); w=(hi-lo)*WIDEN; r[k]=(lo-w,hi+w)
    return r
def outside(f,R): return {k:(f[k],R[k]) for k in R if not(R[k][0]<=f[k]<=R[k][1])}
raw=sorted(glob.glob(os.path.join(os.path.dirname(__file__),'..','corpus','raw','*.md')))
def main():
  if '--loo' in sys.argv:
      res={}
      for i,f in enumerate(raw):
          R=ranges(raw[:i]+raw[i+1:]); o=outside(feats(body(f)),R); res[os.path.basename(f)]=sorted(o)
      n=len(next(iter([feats(body(raw[0]))])))
      tot=sum(len(v) for v in res.values()); out={'features':n,'pieces':len(raw),'outside_per_piece':{k:len(v) for k,v in res.items()},'total_outside':tot,'details':res,'threshold':THRESHOLD,'pieces_at_or_over_threshold':sum(len(v)>=THRESHOLD for v in res.values())}
      json.dump(out,open(os.path.join(os.path.dirname(__file__),'..','reports','range_loo.json'),'w'),indent=1)
      print(json.dumps({k:out[k] for k in out if k!='details'},indent=1))
  else:
      R=ranges(raw); o=outside(feats(body(sys.argv[1])),R)
      print(f'{len(o)} of {len(R)} features outside his own range'+(f' -> WARN (threshold {THRESHOLD})' if len(o)>=THRESHOLD else ' -> ok'))
      for k,(v,r) in sorted(o.items()): print(f'  {k}: {v:.3f} not in {r[0]:.3f}..{r[1]:.3f}')

if __name__=='__main__': main()
