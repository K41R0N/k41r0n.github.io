"""Checks for a small campaign plan written for a beginner.
Header 'asker: beginner|informed'. Sections: '## The one thing' (one line), '## Who it is for' (one line),
'## The one idea' (one line), '## The one action' (one line), '## What we are not' (at least one '- not:'),
'## Where' ('- place: X | job: Y', each with one job), '## How we will know' ('- measure: X | target: N | by: date').
A clean result means only that these patterns are absent. It never judges whether the campaign will work."""
import re
JARGON = ["funnel", "kpi", "icp", "gtm", "engagement rate", "conversion", "impressions", "cta", "omnichannel"]

def _sections(text):
    parts = re.split(r"^## (.+?)\s*$", text, flags=re.M)
    return {parts[i].strip(): parts[i + 1] for i in range(1, len(parts) - 1, 2)}

def _items(body):
    return [l.strip() for l in body.splitlines() if l.strip().startswith("- ")]

def _lines(body):
    return [l for l in body.splitlines() if l.strip()]

def check(text):
    out = []
    sec = _sections(text)
    for name in ("The one thing", "Who it is for", "The one idea", "The one action"):
        if len(_lines(sec.get(name, ""))) != 1:
            out.append(("FAIL", "CB1-not-exactly-one", name))
    if not any(l.startswith("- not:") for l in _items(sec.get("What we are not", ""))):
        out.append(("FAIL", "CB2-no-what-we-are-not", "say one thing the campaign will not claim or chase"))
    for p in _items(sec.get("Where", "")):
        if not re.search(r"place:\s*\S.*\|\s*job:\s*[^|,]+$", p) or " and " in p.split("job:")[-1]:
            out.append(("FAIL", "CB3-place-without-one-job", p[:50]))
    if not _items(sec.get("Where", "")):
        out.append(("FAIL", "CB3-place-without-one-job", "list where it runs"))
    ms = _items(sec.get("How we will know", ""))
    if not ms:
        out.append(("FAIL", "CB4-measure-incomplete", "no measures"))
    for m in ms:
        if not re.search(r"measure:\s*\S.*\|\s*target:\s*\d.*\|\s*by:\s*\d{4}-\d{2}-\d{2}", m):
            out.append(("FAIL", "CB4-measure-incomplete", m[:50]))
    if re.search(r"^asker:\s*(beginner|informed)", text, re.M):
        low = text.lower()
        for w in JARGON:
            if re.search(rf"\b{re.escape(w)}\b", low):
                out.append(("FAIL", "CB5-jargon-for-beginner", w)); break
    return out
