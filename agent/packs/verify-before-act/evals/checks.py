"""Checks for a verify-before-act note. Header 'mode: investigate|change'.
Sections: '## Claims' ('- claim: X | check: how | result: confirmed|contradicted|unchecked'),
'## Signals' ('- signal: X | classified: expected|consequence|known-defect|false-alarm|unknown'),
'## Findings' ('- finding: X | independent-confirmation: yes ...'), '## Change' ('- change: X'), '## Verify' ('- verify: X').
A clean result means only that these patterns were absent. It never certifies that the diagnosis is right."""
import re
VERDICTS = ("expected", "consequence", "known-defect", "false-alarm", "unknown")

def _sections(text):
    parts = re.split(r"^## (.+?)\s*$", text, flags=re.M)
    return {parts[i].strip(): parts[i + 1] for i in range(1, len(parts) - 1, 2)}

def _items(body):
    return [l.strip() for l in body.splitlines() if l.strip().startswith("- ")]

def check(text):
    out = []
    sec = _sections(text)
    mode = (re.search(r"^mode:\s*(\w+)", text, re.M) or [None, ""])[1]
    if mode not in ("investigate", "change"): out.append(("FAIL", "VA0-mode-missing", "mode: investigate or change"))
    claims = _items(sec.get("Claims", ""))
    for c in claims:
        if "| check:" not in c or "| result:" not in c:
            out.append(("FAIL", "VA1-claim-without-check", c[:50]))
    changes = _items(sec.get("Change", ""))
    if mode == "investigate" and changes:
        out.append(("FAIL", "VA2-change-in-investigation", "investigation and change are separate turns"))
    if len(changes) > 1:
        out.append(("FAIL", "VA3-more-than-one-change", f"{len(changes)} changes in one turn"))
    if changes and any("result: unchecked" in c or "result: contradicted" in c for c in claims):
        out.append(("FAIL", "VA4-change-on-unverified-claim", "do not act on a claim that is unchecked or contradicted"))
    for s in _items(sec.get("Signals", "")):
        m = re.search(r"\| classified:\s*([\w-]+)", s)
        if not m or m.group(1) not in VERDICTS:
            out.append(("FAIL", "VA5-signal-unclassified", s[:50]))
    for f in _items(sec.get("Findings", "")):
        if re.search(r"\b(broken|corrupt|failed|down)\b", f, re.I) and not re.search(r"independent-confirmation:\s*yes", f):
            out.append(("FAIL", "VA6-alarm-without-independent-confirmation", f[:50]))
    if changes and not _items(sec.get("Verify", "")):
        out.append(("FAIL", "VA7-change-without-verification", "check the result before the next change"))
    return out
