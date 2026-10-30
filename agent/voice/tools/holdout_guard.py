"""Holdout guard. Stdlib only.
The writer never sees corpus/holdout. This flags any run of 8 consecutive words in the given files (prompts, inputs, drafts) that also appears in a holdout piece.
Usage: holdout_guard.py FILE... ; exit 1 on any overlap. Overlap does not prove the writer saw the holdout, but a clean result is required before a holdout test is trusted."""
import sys,os,re,glob
sys.path.insert(0,os.path.dirname(__file__)); from vlib import body,strip_md
N=8
def grams(t):
    w=re.findall(r"[a-z0-9']+",strip_md(t).lower().replace('’',"'")); return {' '.join(w[i:i+N]) for i in range(len(w)-N+1)}
def run(files,holdout=None):
    holdout=holdout or os.path.join(os.path.dirname(__file__),'..','corpus','holdout')
    H=set()
    for p in glob.glob(os.path.join(holdout,'*.md')): H|=grams(body(p))
    return {f:len(grams(open(f).read())&H) for f in files}
if __name__=='__main__':
    if len(sys.argv)<2: sys.exit(__doc__)
    r=run(sys.argv[1:]); bad=0
    for f,k in r.items(): print(f"{'OVERLAP' if k else 'ok     '} {f} ({k} shared {N}-grams)"); bad+=bool(k)
    sys.exit(1 if bad else 0)
