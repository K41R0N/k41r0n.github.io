"""Find [ALEJANDRO: ...] placeholders. Stdlib only.
When the source material does not say what he thinks about a result, an opinion or a framing, the draft leaves [ALEJANDRO: your take] instead of guessing it.
Usage: placeholders.py draft.md [--final]    lists them; with --final exits 1 if any remain (an unresolved placeholder blocks the final gate)."""
import sys,re
def find(t): return re.findall(r'\[ALEJANDRO:[^\]]*\]',t)
if __name__=='__main__':
    if len(sys.argv)<2: sys.exit(__doc__)
    f=find(open(sys.argv[1]).read())
    for x in f: print(x)
    print(f'{len(f)} placeholder(s)')
    sys.exit(1 if f and '--final' in sys.argv else 0)
