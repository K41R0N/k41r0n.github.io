"""Checks for a strategy canvas. Sections ('## ...'): Strategic Snapshot, 1 Lean Canvas, 2 Value Proposition,
3 ICP Definition, 4 Empathy Map, 5 Positioning, 6 Positioning Statement, 7 Narrative.
Every bullet in modules 1-7 ends with a tag: [Sourced: where], [Inferred], or [Gap].
Header: 'status: draft|proposed|approved' ('approved' needs 'approved_by:').
A clean result means only that these patterns were absent. It never certifies that the strategy is right."""
import re

REQUIRED = [("Snapshot", r"Strategic Snapshot"), ("Lean", r"Lean Canvas"), ("ValueProp", r"Value Proposition"),
            ("ICP", r"ICP Definition"), ("Empathy", r"Empathy Map"), ("Positioning", r"^\s*5\b.*Positioning"),
            ("Statement", r"Positioning Statement"), ("Narrative", r"Narrative")]

def _sections(text):
    parts = re.split(r"^## (.+?)\s*$", text, flags=re.M)
    return [(parts[i].strip(), parts[i + 1]) for i in range(1, len(parts) - 1, 2)]

def check(text):
    out = []
    secs = _sections(text)
    heads = [h for h, _ in secs]
    for key, pat in REQUIRED:
        if not any(re.search(pat, h, re.I) for h in heads):
            out.append(("FAIL", f"SC1-module-missing-{key.lower()}", key))
    st = re.search(r"^status:\s*(\w+)", text, re.M)
    if not st: out.append(("FAIL", "SC2-status-missing", "add status: draft, proposed or approved"))
    elif st.group(1) == "approved" and not re.search(r"^approved_by:\s*\S+", text, re.M):
        out.append(("FAIL", "SC2-approved-without-approver", "approved needs approved_by"))
    for h, body in secs:
        if re.search(r"Snapshot", h): continue
        for l in body.splitlines():
            if not re.match(r"\s*[-*]\s+\S", l): continue
            if "KR:" in l or l.strip().startswith(("- Goal", "* Goal")): continue
            if not re.search(r"\[(Sourced: ?\S.*|Inferred.*|Gap.*)\]\s*$", l):
                if re.search(r"\[Sourced:?\s*\]\s*$", l): out.append(("FAIL", "SC4-sourced-without-source", l[:50]))
                else: out.append(("FAIL", "SC3-untagged-bullet", l[:50]))
    for h, body in secs:
        if re.search(r"Positioning Statement", h) and not all(w in body for w in ("For ", " who ", "Unlike")):
            out.append(("FAIL", "SC5-statement-incomplete", "needs For ... who ... Unlike ..."))
    for l in text.splitlines():
        if re.match(r"\s*[-*]\s*Goal:", l) and not re.search(r"KR:.*\d", l):
            out.append(("FAIL", "SC6-goal-without-measurable-result", l[:50]))
    snap = "".join(b for h, b in secs if "Snapshot" in h)
    if not re.search(r"Spokesperson:", snap):
        out.append(("WARN", "SC7-no-spokesperson", "name who speaks publicly for the client before positioning"))
    return out
