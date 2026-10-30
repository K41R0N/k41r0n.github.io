"""Checks for an interview plan. Format: rounds start with '## Round N'. Questions are lines like
'Q1 [describe] What happened last time?'. Optional 'Unread: ...' line lists sources not read."""
import re
LADDER = ["describe", "explain", "predict", "estimate", "delegate"]
JARGON = [r"\bS[0-4]\b", r"\bL[0-5]\b", r"\bQ-?\d+\b"]

def check(text):
    out = []
    rounds = re.split(r"^## Round \d+.*$", text, flags=re.M)[1:]
    if not rounds: out.append(("FAIL", "DI0-no-rounds", "no '## Round N' sections"))
    seen = -1
    for r, body in enumerate(rounds, 1):
        qs = re.findall(r"^Q\d+\s*\[(\w+)\]\s*(.+)$", body, re.M)
        if len(qs) > 3: out.append(("FAIL", "DI1-too-many-questions", f"round {r} has {len(qs)} questions, max 3"))
        for tag, q in qs:
            t = tag.lower()
            if t not in LADDER:
                out.append(("FAIL", "DI2-bad-tag", f"unknown level {tag}")); continue
            i = LADDER.index(t)
            if i > seen + 1: out.append(("FAIL", "DI2-ladder-skip", f"{t} asked before {LADDER[seen+1]} was reached"))
            seen = max(seen, i)
            if not q.strip().endswith("?"): out.append(("WARN", "DI3-not-a-question", q[:40]))
            if any(re.search(j, q) for j in JARGON): out.append(("FAIL", "DI4-jargon", q[:40]))
    if not re.search(r"^Unread:", text, re.M): out.append(("FAIL", "DI5-unread-line-missing", "add 'Unread: none' or list them"))
    return out
