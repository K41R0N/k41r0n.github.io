"""Checks for an analytics-report-discipline note. Headers 'report: <name>' and 'window: <period>'.
Sections: '## Period' ('- period: label | state: open|closed | comparable: yes|no'),
'## Numbers' ('- value: metric = n | source: s | as-of: date | status: ok|stale|partial|unavailable|manual|error'),
'## Interpretation', '## Actions' ('- action: what | rank: n'),
'## Thresholds' ('- flag: metric breached threshold | hypothesis: one line'),
'## Open-decisions' ('- decision: what | default: current | alternates: others'),
'## Corrections' ('- correction: what was wrong | fix: what changed'),
'## Uncaptured' ('- source: name | status: uncaptured | capture-plan: how').
A clean result means only that these patterns were absent. It never certifies the analysis."""
import re
STATUSES = ("ok", "stale", "partial", "unavailable", "manual", "error")

def _sections(text):
    parts = re.split(r"^## (.+?)\s*$", text, flags=re.M)
    return {parts[i].strip(): parts[i + 1] for i in range(1, len(parts) - 1, 2)}

def _items(body):
    return [l.strip() for l in body.splitlines() if l.strip().startswith("- ")]

def check(text):
    out = []
    sec = _sections(text)
    if not re.search(r"^report:\s*\S", text, re.M):
        out.append(("FAIL", "AR0-report-missing", "name the report"))
    period = _items(sec.get("Period", ""))
    if not period:
        out.append(("FAIL", "AR1-period-untyped", "period with open-or-closed state required"))
    for p in period:
        if not re.search(r"\| state:\s*(open|closed)", p):
            out.append(("FAIL", "AR1-period-untyped", p[:60]))
    for n in _items(sec.get("Numbers", "")):
        if re.search(r"\bbecause\b|\bmeans\b|\bdriven by\b", n, re.I):
            out.append(("FAIL", "AR2-numbers-carry-interpretation", n[:60]))
        if not re.search(r"\| source:\s*\S+.*?\| as-of:\s*\d{4}-\d{2}-\d{2}.*?\| status:\s*(%s)" % "|".join(STATUSES), n):
            out.append(("FAIL", "AR3-value-incomplete", n[:60]))
    for t in _items(sec.get("Thresholds", "")):
        if "| hypothesis:" not in t:
            out.append(("FAIL", "AR4-threshold-cause-unlabeled", t[:60]))
    for c in _items(sec.get("Changes", "")):
        if "| cause:" in c and "| evidence:" not in c:
            out.append(("FAIL", "AR5-cause-without-evidence", c[:60]))
    for d in _items(sec.get("Open-decisions", "")):
        if "| default:" not in d:
            out.append(("FAIL", "AR6-open-decision-without-default", d[:60]))
    for u in _items(sec.get("Uncaptured", "")):
        if "status: uncaptured" in u and "| capture-plan:" not in u:
            out.append(("FAIL", "AR7-uncaptured-without-plan", u[:60]))
    actions = _items(sec.get("Actions", ""))
    for a in actions:
        if not re.search(r"\| rank:\s*\d+", a):
            out.append(("FAIL", "AR8-action-unranked", a[:60]))
    return out

# Every check ID this module can emit. evals/coverage_check.py enforces that each
# carries at least one fixture whose run through check() produces it (the runner's
# found == expected rule is the proof of signal), or an explicit CONDITIONAL reason.
CHECK_IDS = [
    "AR0-report-missing",
    "AR1-period-untyped",
    "AR2-numbers-carry-interpretation",
    "AR3-value-incomplete",
    "AR4-threshold-cause-unlabeled",
    "AR5-cause-without-evidence",
    "AR6-open-decision-without-default",
    "AR7-uncaptured-without-plan",
    "AR8-action-unranked"
]
CONDITIONAL = {}
