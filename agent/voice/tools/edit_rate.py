"""Edit rate between a draft and his final edit. Stdlib only. Deterministic.
Usage: edit_rate.py draft.md final.md [--hunks]
Words are whitespace tokens. added = tokens in his final that the draft lacked; cut = draft tokens he removed.
rate = (added + cut) / draft_words. The source article does not give its formula, so this definition is ours:
compare it only against itself, never against another system's percentage."""
import sys,json,difflib,re
sys.path.insert(0,__import__('os').path.dirname(__file__)); from vlib import body
def toks(path): return re.sub(r'\s+',' ',body(path)).strip().split(' ')
def hunks(a,b):
    sm=difflib.SequenceMatcher(None,a,b,autojunk=False); out=[]
    for op,i1,i2,j1,j2 in sm.get_opcodes():
        if op=='equal': continue
        out.append({'n':len(out)+1,'op':op,'draft':' '.join(a[i1:i2]),'final':' '.join(b[j1:j2]),'cut':i2-i1,'added':j2-j1})
    return out
def measure(dpath,fpath):
    a,b=toks(dpath),toks(fpath); h=hunks(a,b)
    cut=sum(x['cut'] for x in h); add=sum(x['added'] for x in h)
    return {'draft_words':len(a),'added':add,'cut':cut,'rate':round((add+cut)/max(1,len(a)),4),'hunks':h}
if __name__=='__main__':
    if len(sys.argv)<3: sys.exit(__doc__)
    r=measure(sys.argv[1],sys.argv[2])
    if '--hunks' in sys.argv: print(json.dumps(r,indent=1))
    else: print(f"draft_words={r['draft_words']} added={r['added']} cut={r['cut']} rate={r['rate']*100:.1f}% hunks={len(r['hunks'])}")
