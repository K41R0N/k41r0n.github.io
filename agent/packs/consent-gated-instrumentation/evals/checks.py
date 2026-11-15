"""Checks for a consent-gated-instrumentation note. Header 'change: <what>'.
Sections: '## Scopes' ('- vendor: X | scope: Y | state: granted|denied|missing'),
'## Decisions' ('- decision: enabled|blocked | side-effect: Z | basis: granted|denied|missing'),
'## Migration' ('- record: R | review: reviewed|pending | carried: yes|no').
The check reads the note's structure only. It does not enforce or observe any runtime behavior.
A clean result means only that these patterns were absent."""
import re

def _sections(text):
    parts = re.split(r"^## (.+?)\s*$", text, flags=re.M)
    return {parts[i].strip(): parts[i + 1] for i in range(1, len(parts) - 1, 2)}

def _items(body):
    return [l.strip() for l in body.splitlines() if l.strip().startswith("- ")]

def check(text):
    out = []
    sec = _sections(text)
    if not re.search(r"^change:\s*\S", text, re.M):
        out.append(("FAIL", "CG0-change-missing", "name the instrumentation change"))
    scopes = _items(sec.get("Scopes", ""))
    if not scopes:
        out.append(("FAIL", "CG1-no-scopes", "per-vendor scopes with recorded states required"))
    for s in scopes:
        if not re.search(r"\| state:\s*(granted|denied|missing)", s):
            out.append(("FAIL", "CG2-scope-without-state", s[:60]))
    for d in _items(sec.get("Decisions", "")):
        m = re.search(r"decision:\s*(enabled|blocked).*?\| basis:\s*(granted|denied|missing)", d)
        if not m:
            out.append(("FAIL", "CG3-decision-without-basis", d[:60]))
            continue
        decision, basis = m.group(1), m.group(2)
        if decision == "enabled" and basis != "granted":
            out.append(("FAIL", "CG4-enabled-without-grant", d[:60]))
    for r in _items(sec.get("Migration", "")):
        if re.search(r"carried:\s*yes", r) and "review: reviewed" not in r:
            out.append(("FAIL", "CG5-carried-without-review", r[:60]))
    return out
