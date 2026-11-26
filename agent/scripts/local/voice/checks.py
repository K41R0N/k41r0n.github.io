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
W08_DIR = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
W08_EVIDENCE = os.path.join(W08_DIR, 'knowledge', 'voice', 'refs', 'wiki-ai-signs-evidence.json')
W08_CANDIDATES = os.path.join(W08_DIR, 'knowledge', 'voice', 'refs', 'wiki-ai-signs-candidates.txt')
W08_CORPUS = os.path.join(W08_DIR, 'assets', 'voice-corpus', 'raw')


def _w08_sha(paths):
    import hashlib
    h = hashlib.sha256()
    for p in paths:
        h.update(os.path.basename(p).encode() + b'\0' + open(p, 'rb').read() + b'\0')
    return h.hexdigest()


def w08_state():
    """(forms, status, detail). status is 'ok', 'unavailable' or 'stale'.

    Advisory only: when the evidence file is missing, unreadable, or no longer
    matches the candidates file or the raw corpus it was built from, no form is
    flagged and the state says so out loud instead of reading as a clean pass.
    Only forms with auto_flag and zero corpus use are ever flagged."""
    import glob
    if not os.path.exists(W08_EVIDENCE):
        return [], 'unavailable', 'evidence file missing (run wiki_candidate_evidence.py)'
    try:
        ev = json.load(open(W08_EVIDENCE))
        entries = ev['entries']
    except Exception as e:
        return [], 'unavailable', f'evidence file unreadable ({type(e).__name__})'
    try:
        if ev.get('candidates_sha256') != _w08_sha([W08_CANDIDATES]):
            return [], 'stale', 'candidates file changed since the evidence was built; rerun wiki_candidate_evidence.py'
        if ev.get('corpus_sha256') != _w08_sha(sorted(glob.glob(os.path.join(W08_CORPUS, '*.md')))):
            return [], 'stale', 'raw corpus changed since the evidence was built; rerun wiki_candidate_evidence.py'
    except OSError as e:
        return [], 'unavailable', f'cannot verify evidence inputs ({type(e).__name__})'
    forms = set()
    for e in entries:
        if e.get('kind') == 'uncheckable':
            continue
        for f, c in e.get('form_class', {}).items():
            if c == 'zero_use' and e.get('auto_flag', {}).get(f, False):
                forms.add((e.get('kind'), f))
    return sorted(forms), 'ok', f"revision {ev.get('source_oldid','?')}, {len(ev.get('corpus_files', []))} raw essays"


def _w08_count(t):
    """Flag only candidates he never uses in corpus/raw (per-form), never every wiki word."""
    forms, status, _ = w08_state()
    if status != 'ok':
        return 0
    text = re.sub(r'\s+', ' ', lines(t).lower())   # stripped + normalized once per run
    c = 0
    for kind, f in forms:
        norm_f = re.sub(r'\s+', ' ', f.lower())
        c += len(re.findall(r"(?<![a-z0-9'])" + re.escape(norm_f) + r"(?![a-z0-9'])", text))
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
 ('W08','Wikipedia watch-list candidates he never uses in corpus/raw (per-form; unconfirmed, revision-pinned)','wikipedia-watch-list x corpus/raw (refs/wiki-ai-signs-evidence.json)','INFO',_w08_count),
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
        c=fn(t); row={'id':rid,'desc':desc,'origin':origin,'severity':sev,'count':c,'per_1000_words':1000*c/max(1,n)}
        if rid=='W08':
            _,row['status'],row['detail']=w08_state()
        out.append(row)
    return n,out
if __name__=='__main__':
    scope="client-candidate" if "--scope=client-candidate" in sys.argv else "personal"
    n,o=run(sys.argv[1], scope)
    if '--json' in sys.argv: print(json.dumps(o,indent=1))
    else:
        print(f'{sys.argv[1]}  ({n} words)')
        for r in o:
            if r['count']: print(f"  {r['severity']} {r['id']} x{r['count']}  {r['desc']}")
            if r['id']=='W08' and r['status']!='ok': print(f"  INFO W08 {r['status'].upper()}: {r['detail']} (advisory check did not run; not a clean pass)")
