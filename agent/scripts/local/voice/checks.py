"""Deterministic check layer v0. Each rule: id, source, severity, test. Usage: checks.py file.md [--json]
Rules are PROPOSED (Tier 2) until Alejandro confirms. Rules marked origin=client-brand are ported from a client brand harness and are NOT assumed to be his personal habits."""
import sys,re,os,json
sys.path.insert(0,os.path.dirname(__file__)); from vlib import *
def W(t): return words(strip_md(t))
BANNED_FILLER=['very','really','quite','just','actually','simply','arguably','perhaps']
BANNED_AI=['seamless','seamlessly','robust','unlock','leverage','leveraging','utilize','utilise','harness','empower','streamline','delve','tapestry','realm','pivotal','crucial','testament','landmark','foster','elevate','bolster','underscore','underscores','underscoring']
SOFT=["in essence","essentially","more specifically","what this means in practice","it's worth noting","it’s worth noting","at the end of the day","when it comes to","it's important to note","it’s important to note","in today's fast-paced","in today’s fast-paced"]
FALSE_DEPTH=["at its core","the real question is","here's the thing","here’s the thing","let's dive in","let’s dive in"]
WRAPPER=[r'\bthis matters because\b',r'\bthis reflects a broader\b',r'\ba testament to\b',r'\bmarks a shift\b']
TRANSITION=[r'(?:^|\n)\s*(?:Additionally|Furthermore|Moreover|In conclusion)\b']
def lines(t): return strip_md(t)
def hits(rx,t,flags=re.I): return len(re.findall(rx,t,flags))
def _wiki_w08_forms():
    """Zero-use forms from the Wikipedia watch-list evidence file, or None if absent."""
    p = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'knowledge', 'voice', 'refs', 'wiki-ai-signs-evidence.json')
    p = os.path.normpath(p)
    if not os.path.exists(p):
        return None
    try:
        ev = json.load(open(p))
    except Exception:
        return None
    forms = set()
    for e in ev.get('entries', []):
        if e.get('kind') == 'uncheckable':
            continue
        for f, c in e.get('form_class', {}).items():
            if c == 'zero_use':
                forms.add((e.get('kind'), f))
    return sorted(forms)


WIKI_W08 = _wiki_w08_forms()


def _w08_count(t):
    """Flag only candidates he never uses in corpus/raw (per-form), never every wiki word."""
    if WIKI_W08 is None:
        return 0
    c = 0
    for kind, f in WIKI_W08:
        if kind == 'word':
            c += hits(r'\b' + re.escape(f.lower()) + r'\b', lines(t))
        else:
            c += lines(t).lower().count(f.lower())
    return c


RULES=[
 # id, description, origin, severity, fn(text)->count
 ('P01','no em dash','client-brand (Sky writing-mechanics)','FAIL',lambda t:t.count('—')),
 ('P02','no en dash','client-brand (Sky writing-mechanics)','FAIL',lambda t:t.count('–')),
 ('P03','no exclamation marks','client-brand (Sky writing-mechanics)','FAIL',lambda t:t.count('!')),
 ('P04','no hashtags','client-brand (Sky writing-mechanics)','FAIL',lambda t:hits(r'(?<![\w&])#[A-Za-z]',lines(t))),
 ('W01','banned filler: '+', '.join(BANNED_FILLER),'client-brand (Sky writing-mechanics)','WARN',lambda t:sum(hits(r'\b'+w+r'\b',lines(t)) for w in BANNED_FILLER)),
 ('W02','banned AI lexicon','client-brand + craft tell catalog','WARN',lambda t:sum(hits(r'\b'+w+r'\b',lines(t)) for w in BANNED_AI)),
 ('W03','soft fillers','client-brand (check 11)','WARN',lambda t:sum(lines(t).lower().count(p) for p in SOFT)),
 ('W04','false-depth openers','craft tell catalog','WARN',lambda t:sum(lines(t).lower().count(p) for p in FALSE_DEPTH)),
 ('W05','interpretive wrapper phrases','craft tell catalog (strongest tell)','WARN',lambda t:sum(hits(p,lines(t)) for p in WRAPPER)),
 ('W06','Additionally/Furthermore/Moreover/In conclusion','client-brand (check 04)','WARN',lambda t:sum(hits(p,lines(t)) for p in TRANSITION)),
 ('W07','hedging stack: 2+ of may/might/could/potentially/arguably in one sentence','craft tell catalog','WARN',lambda t:sum(1 for p in paragraphs(t) for s in sentences(p) if hits(r'\b(may|might|could|potentially|arguably)\b',s)>=2)),
 ('W08','Wikipedia watch-list candidates he never uses in corpus/raw (per-form; unconfirmed, revision-pinned)','wikipedia-watch-list x corpus/raw (refs/wiki-ai-signs-evidence.json)','WARN',_w08_count),
 ('S01','sentence over 32 words (hard cap)','client-brand (Sky writing-mechanics)','FAIL',lambda t:sum(1 for l in sent_lens(t) if l>32)),
 ('S02','participial significance ending (, reflecting/underscoring/highlighting/demonstrating/cementing)','craft tell catalog','WARN',lambda t:hits(r', (?:reflecting|underscoring|highlighting|demonstrating|cementing|showcasing)\b',lines(t))),
 ('S03','copula avoidance (serves as / stands as / boasts)','craft tell catalog','WARN',lambda t:hits(r'\b(?:serves as|stands as|boasts)\b',lines(t))),
 ('R01','burstiness: has a sentence under 8 words (piece-level, 0 hits = pass)','craft burstiness floor','FAIL',lambda t:0 if any(l<8 for l in sent_lens(t)) else 1),
 ('R02','burstiness: has a sentence over 25 words (piece-level)','craft burstiness floor','FAIL',lambda t:0 if any(l>25 for l in sent_lens(t)) else 1),
 ('R03','four consecutive sentences each within 3 words of the previous (metronome run)','craft burstiness floor (tightened from 3 to 4 after v0 test flagged 10/11 of his pieces)','WARN',lambda t:sum(1 for p in [sent_lens(t)] for i in range(len(p)-3) if all(abs(p[i+j]-p[i+j+1])<=3 for j in range(3)))),
 ('R04','paragraph mass uniform: share of 2-4 sentence paragraphs > 0.85 (piece-level)','craft tell catalog','WARN',lambda t:1 if (lambda ps:ps and sum(2<=x<=4 for x in ps)/len(ps)>0.85)([len(sentences(p)) for p in paragraphs(t)]) else 0),
 ('R05','bold lead-in stacks (3+ "**Lead:** sentence")','craft tell catalog','WARN',lambda t:1 if hits(r'^\*\*[^*\n]+:\*\*\s',t,re.M)>=3 else 0),
]
def run(path, scope="personal"):
    if scope not in ("personal", "client-candidate"):
        raise ValueError("unknown rule scope")
    t=body(path); n=len(W(t)); out=[]
    for rid,desc,origin,sev,fn in RULES:
        # Client bans and unconfirmed rhythm prescriptions are observations, not personal failures.
        if scope == 'personal':
            sev = 'INFO' if ('client-brand' in origin or rid in ('R01','R02','W08')) else 'WARN'
        c=fn(t); out.append({'id':rid,'desc':desc,'origin':origin,'severity':sev,'count':c,'per_1000_words':1000*c/max(1,n)})
    return n,out
if __name__=='__main__':
    scope="client-candidate" if "--scope=client-candidate" in sys.argv else "personal"
    n,o=run(sys.argv[1], scope)
    if '--json' in sys.argv: print(json.dumps(o,indent=1))
    else:
        print(f'{sys.argv[1]}  ({n} words)')
        for r in o:
            if r['count']: print(f"  {r['severity']} {r['id']} x{r['count']}  {r['desc']}")
