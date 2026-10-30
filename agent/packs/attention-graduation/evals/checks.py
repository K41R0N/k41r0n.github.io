"""Checks for an attention-graduation capability profile.
Input is a markdown profile with lines like:  depth: D2 / mode: E3 / manual_runs: 3 / and slot lines '- strategize: D2'."""
import re
SLOTS = ["strategize", "suspect", "anticipate", "act", "react", "recognize", "calculate"]
CAP = {1: 4, 2: 3, 3: 2, 4: 1, 5: 0}  # depth -> lowest inference mode number allowed (E4 down to E0)

def _field(text, key):
    m = re.search(rf"^{key}:\s*(\S+)", text, re.M | re.I)
    return m.group(1) if m else None

def check(text):
    out = []
    depth = _field(text, "depth"); mode = _field(text, "mode"); runs = _field(text, "manual_runs")
    d = int(depth[1]) if depth and re.fullmatch(r"D[1-5]", depth) else None
    e = int(mode[1]) if mode and re.fullmatch(r"E[0-4]", mode) else None
    if d is None: out.append(("FAIL", "AG1-depth-missing", "depth must be D1 to D5"))
    if e is None: out.append(("FAIL", "AG2-mode-missing", "mode must be E0 to E4"))
    slots = {}
    for s in SLOTS:
        m = re.search(rf"^-\s*{s}:\s*D([1-5])", text, re.M | re.I)
        if m: slots[s] = int(m.group(1))
        else: out.append(("FAIL", f"AG3-slot-missing-{s}", f"slot {s} has no depth"))
    if d and len(slots) == len(SLOTS) and d != min(slots.values()):
        out.append(("FAIL", "AG4-depth-not-lowest-slot", f"declared D{d}, lowest slot is D{min(slots.values())}"))
    if d and e is not None and e < CAP[d]:
        out.append(("FAIL", "AG5-mode-below-cap", f"D{d} may not run below E{CAP[d]}; declared E{e}"))
    if e is not None and e <= 1 and (runs is None or not runs.isdigit() or int(runs) < 2):
        out.append(("FAIL", "AG6-script-before-two-runs", "scripted modes need two identical manual runs first"))
    return out
