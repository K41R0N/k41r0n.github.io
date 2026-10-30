"""Checks for a clear-message note (how to say something so the listener gets it).
Header 'asker: beginner|informed|expert'. Sections: '## The point' (one sentence), '## Who is listening' ('- listener:', '- doubts:'),
'## Proof' ('- proof: X | source: Y'), '## This not that' ('- not: X | instead: Y'), '## Analogy' (optional, '- like: X'), '## Say it in one sentence'.
A clean result means only that these patterns are absent. It never judges whether the message is true or lands."""
import re
ADJ = ["amazing", "revolutionary", "world-class", "best-in-class", "innovative", "seamless", "cutting-edge", "next-generation", "unparalleled"]

def _sections(text):
    parts = re.split(r"^## (.+?)\s*$", text, flags=re.M)
    return {parts[i].strip(): parts[i + 1] for i in range(1, len(parts) - 1, 2)}

def _items(body):
    return [l.strip() for l in body.splitlines() if l.strip().startswith("- ")]

def _sentences(body):
    return [s for s in re.split(r"(?<=[.!?])\s+", body.strip()) if s]

def check(text):
    out = []
    sec = _sections(text)
    if len(_sentences(sec.get("The point", ""))) != 1:
        out.append(("FAIL", "CM1-point-not-one-sentence", "state the point in exactly one sentence"))
    who = sec.get("Who is listening", "")
    if not (re.search(r"^- listener:\s*\S", who, re.M) and re.search(r"^- doubts:\s*\S", who, re.M)):
        out.append(("FAIL", "CM2-listener-or-doubts-missing", "name who is listening and what they doubt"))
    proofs = _items(sec.get("Proof", ""))
    if not proofs or any(not re.search(r"proof:\s*\S.*\|\s*source:\s*\S", p) for p in proofs):
        out.append(("FAIL", "CM3-proof-without-source", "each proof needs a source"))
    low = text.lower()
    for w in ADJ:
        if re.search(rf"\b{re.escape(w)}\b", low):
            out.append(("FAIL", "CM4-adjective-instead-of-proof", w)); break
    tn = _items(sec.get("This not that", ""))
    if not tn or any(not re.search(r"not:\s*\S.*\|\s*instead:\s*\S", t) for t in tn):
        out.append(("FAIL", "CM5-no-this-not-that", "give at least one 'not X | instead Y'"))
    one = _sentences(sec.get("Say it in one sentence", ""))
    if len(one) != 1 or len(one[0].split()) > 25:
        out.append(("FAIL", "CM6-not-one-short-sentence", "one sentence, 25 words or fewer"))
    return out
