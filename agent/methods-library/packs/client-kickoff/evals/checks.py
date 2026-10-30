"""Checks for a client kickoff plan.
Sections: '## Agenda' ('- 0-10 | topic'), '## Working agreement' ('- approver: X'), '## Success', '## Access', '## After the call', header 'publishing in week 1: none'.
A clean result means only that these patterns are absent. It never judges whether the plan fits the client."""
import re

def _sections(text):
    parts = re.split(r"^## (.+?)\s*$", text, flags=re.M)
    return {parts[i].strip(): parts[i + 1] for i in range(1, len(parts) - 1, 2)}

def _items(body):
    return [l.strip() for l in body.splitlines() if l.strip().startswith("- ")]

def check(text):
    out = []
    sec = _sections(text)
    spans = []
    for a in _items(sec.get("Agenda", "")):
        m = re.match(r"-\s*(\d+)\s*-\s*(\d+)\s*\|", a)
        if m: spans.append((int(m.group(1)), int(m.group(2))))
    ok = bool(spans) and spans[0][0] == 0 and spans[-1][1] == 60 and all(spans[i][1] == spans[i + 1][0] for i in range(len(spans) - 1))
    if not ok:
        out.append(("FAIL", "KO1-agenda-not-60-min", "time boxes must run 0 to 60 with no gap or overlap"))
    wa = sec.get("Working agreement", "")
    m = re.search(r"approver:\s*(.+)", wa)
    if not m or not m.group(1).strip() or re.search(r",|\band\b|/", m.group(1)):
        out.append(("FAIL", "KO2-approver-not-one-person", "name exactly one person who approves"))
    if not re.search(r"90 days", sec.get("Success", "")):
        out.append(("FAIL", "KO3-no-90-day-success-question", "ask what outcome in 90 days makes the partnership a success"))
    if not re.search(r"preference:\s*\S", sec.get("Access", "")):
        out.append(("FAIL", "KO4-access-preference-not-asked", "ask delegated or full access and record the preference"))
    if not re.search(r"summary", sec.get("After the call", ""), re.I):
        out.append(("FAIL", "KO5-no-after-call-summary", "send next steps and timelines right after"))
    if not re.search(r"^publishing in week 1:\s*none", text, re.M | re.I):
        out.append(("FAIL", "KO6-publishing-in-week-1", "week one is audit and strategy, nothing publishes"))
    return out
