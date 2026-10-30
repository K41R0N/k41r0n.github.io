"""Checks for an audience-listening note.
Sections: '## Starting point', '## Sources' ('- claim: X | source: URL or doc'),
'## Hits' ('- date: D | source: S | who: W | said: T' plus optional '| engagement: N | read-at: D' and '| venue: social | primary: URL'),
'## Not verified', '## Skip'. A clean result means only that these patterns are absent. It never judges whether the audience read is right."""
import re

def _sections(text):
    parts = re.split(r"^## (.+?)\s*$", text, flags=re.M)
    return {parts[i].strip(): parts[i + 1] for i in range(1, len(parts) - 1, 2)}

def _items(body):
    return [l.strip() for l in body.splitlines() if l.strip().startswith("- ")]

def check(text):
    out = []
    sec = _sections(text)
    for c in _items(sec.get("Sources", "")):
        if not re.search(r"\|\s*source:\s*\S", c):
            out.append(("FAIL", "AL1-claim-without-source", c[:50]))
    for h in _items(sec.get("Hits", "")):
        missing = [k for k in ("date", "source", "who", "said") if not re.search(rf"\b{k}:\s*\S", h)]
        if missing:
            out.append(("FAIL", "AL2-hit-missing-field", f"{','.join(missing)}: {h[:40]}"))
        if re.search(r"engagement:\s*\S", h) and not re.search(r"read-at:\s*\S", h):
            out.append(("FAIL", "AL3-engagement-without-read-time", h[:50]))
        if re.search(r"venue:\s*social", h) and not re.search(r"primary:\s*\S", h):
            out.append(("FAIL", "AL4-headline-without-primary-source", h[:50]))
    if not _items(sec.get("Not verified", "")):
        out.append(("FAIL", "AL5-no-not-verified", "list what you could not confirm, or write '- none found'"))
    if "Skip" not in sec:
        out.append(("FAIL", "AL6-no-skip-list", "say what you deliberately ignore"))
    return out
