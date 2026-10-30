"""Checks for a note coaching someone to use AI better.
Sections: '## What they use it for' ('- use:', '- useful:'), '## Tasks' ('- task: X | kind: research|consistency|repetitive'),
'## Setup' ('- aid: timer|checker|format|process | for: X'), '## Theirs' (the 10% that stays theirs), '## Next step' (one item).
A clean result means only that these patterns are absent. It never judges whether the coaching is good or sounds like him."""
import re
KINDS = ("research", "consistency", "repetitive")
AIDS = ("timer", "checker", "format", "process")

def _sections(text):
    parts = re.split(r"^## (.+?)\s*$", text, flags=re.M)
    return {parts[i].strip(): parts[i + 1] for i in range(1, len(parts) - 1, 2)}

def _items(body):
    return [l.strip() for l in body.splitlines() if l.strip().startswith("- ")]

def check(text):
    out = []
    sec = _sections(text)
    asked = sec.get("What they use it for", "")
    if not (re.search(r"^- use:\s*\S", asked, re.M) and re.search(r"^- useful:\s*\S", asked, re.M)):
        out.append(("FAIL", "AC1-did-not-ask-first", "ask what they use it for and what is useful to them"))
    tasks = []
    for t in _items(sec.get("Tasks", "")):
        m = re.search(r"task:\s*([^|]+?)\s*\|\s*kind:\s*(\w+)", t)
        if not m or m.group(2) not in KINDS:
            out.append(("FAIL", "AC2-task-kind-missing", t[:50]))
        else:
            tasks.append(m.group(1).strip())
    fors = []
    for a in _items(sec.get("Setup", "")):
        m = re.search(r"aid:\s*(\w+)\s*\|\s*for:\s*(.+)", a)
        if not m or m.group(1) not in AIDS:
            out.append(("FAIL", "AC3-aid-not-a-known-kind", a[:50]))
        else:
            fors.append(m.group(2).strip())
    for t in tasks:
        if t not in fors:
            out.append(("FAIL", "AC4-task-without-setup", t[:40]))
    if not _items(sec.get("Theirs", "")):
        out.append(("FAIL", "AC5-no-part-that-stays-theirs", "name the 10% that is their insight and taste"))
    if len(_items(sec.get("Next step", ""))) != 1:
        out.append(("FAIL", "AC6-not-one-next-step", "exactly one next step"))
    return out
