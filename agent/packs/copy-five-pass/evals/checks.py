"""Five passes over a draft. Draft header (first lines): 'context: external|internal', optional 'approved_by: NAME'.
Pass 1 evidence, 2 unresolved, 3 filler, 4 plain reading, 5 authority.
A clean result means only that these patterns were absent. It never certifies voice or quality."""
import re
FILLER = ["game-changer", "game changer", "unlock", "seamless", "delve", "revolutionary", "in today's fast-paced", "cutting-edge", "leverage"]
META = [r"as requested", r"for your review", r"draft version", r"still needs a pass", r"note to (the )?(reader|reviewer)", r"could(n't| not) verify", r"research limit", r"internal process"]
EN_TERMS = ["workflow", "harness", "pipeline", "onboarding", "feedback", "insight", "engagement", "dashboard", "benchmark"]

def _sentences(text):
    body = re.sub(r"^(\w+):.*$", "", text, flags=re.M)
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+|\n+", body) if s.strip()]

def check(text):
    out = []
    ctx = re.search(r"^context:\s*(\w+)", text, re.M)
    for s in _sentences(text):
        if re.search(r"\d+(\.\d+)?\s*(%|x\b|k\b|m\b)|\$\d", s) and "[src:" not in s:
            out.append(("FAIL", "P1-number-without-source", s[:50]))
        if re.search(r"\b(the first|the only|the best|never before)\b", s, re.I) and "[src:" not in s:
            out.append(("FAIL", "P1-superlative-without-source", s[:50]))
        if re.search(r"\b(most powerful|world[- ]class|best[- ]in[- ]class|state[- ]of[- ]the[- ]art)\b", s, re.I) and "[src:" not in s:
            out.append(("FAIL", "P1-slop-superlative", s[:50]))
        if len(s.split()) > 40:
            out.append(("WARN", "P4-long-sentence", s[:50]))
    if re.search(r"\b(TODO|TBD|XXX|lorem ipsum)\b|\[placeholder", text, re.I):
        out.append(("FAIL", "P2-unresolved", "placeholder or TODO left in"))
    low = text.lower()
    if any(f in low for f in FILLER):
        out.append(("WARN", "P3-filler", "filler phrase present"))
    words = max(1, len(text.split()))
    if text.count("\u2014") * 1000 / words > 1:
        out.append(("WARN", "P3-dash-budget", "more than about 1 em dash per 1000 words"))
    lang = re.search(r"^language:\s*(\w+)", text, re.M)
    if ctx and ctx.group(1).lower() == "external":
        for pat in META:
            m = re.search(pat, text, re.I)
            if m:
                out.append(("FAIL", "P3-meta-commentary", m.group(0)[:50]))
                break
    if lang and lang.group(1).lower() not in ("en", "eng", "english"):
        hits = [term for term in EN_TERMS if re.search(r"\b" + re.escape(term) + r"s?\b", text, re.I)]
        if hits:
            out.append(("FAIL", "P3-language-mix", "english terms in " + lang.group(1) + " copy: " + ", ".join(hits[:3])))
    if ctx and ctx.group(1).lower() == "external" and not re.search(r"^approved_by:\s*\S+", text, re.M):
        out.append(("FAIL", "P5-external-without-approval", "external copy needs approved_by"))
    if not ctx:
        out.append(("FAIL", "P5-context-missing", "add 'context: external' or 'context: internal'"))
    return out
