"""Ban list from zero-use words only. Stdlib only.
Usage: ban_list.py [corpus_dir] [candidates.txt]   (default corpus: ../corpus/raw; candidates: one word per line, else the built-in list)
A word goes on the ban list only if he never uses it in corpus/raw. A word he does use is NOT banned, whatever people say about AI.
Absence in a small corpus is weak evidence, so the output shows corpus size; confirm with him before adopting."""
import sys,os,re,glob
sys.path.insert(0,os.path.dirname(__file__)); from vlib import body,strip_md
CAND="delve crucial moreover furthermore additionally testament seamless seamlessly robust foster elevate navigate imagine leverage unlock utilize empower streamline tapestry realm pivotal bolster underscore harness landscape journey".split()
def run(corpus,cands):
    txt=' '.join(strip_md(body(p)).lower() for p in sorted(glob.glob(os.path.join(corpus,'*.md'))))
    n=len(re.findall(r"[a-z0-9']+",txt)); out=[]
    for w in cands: out.append((w,len(re.findall(r'\b'+re.escape(w.lower())+r'\b',txt))))
    return n,out
if __name__=='__main__':
    c=sys.argv[1] if len(sys.argv)>1 else os.path.join(os.path.dirname(__file__),'..','..','..','assets','voice-corpus','raw')
    cands=[l.strip() for l in open(sys.argv[2])] if len(sys.argv)>2 else CAND
    n,o=run(c,[x for x in cands if x])
    print(f'corpus words: {n}')
    for w,k in o: print(f"{'BAN ' if k==0 else 'KEEP'} {w:14s} his uses: {k}")
