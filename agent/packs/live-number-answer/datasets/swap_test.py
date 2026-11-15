#!/usr/bin/env python3
"""Reuse and boundary test for the live-number-answer pack.
Resolves metrics from two different invented dataset registers with the same
unedited resolver, then covers boundary failures. Prints one line per case and
exits nonzero on any mismatch. Actual tested behavior, not a design claim."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from resolver import load_register, resolve, DEFERRAL

DEMO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "demo")
bad = 0

def expect(label, got, want):
    global bad
    ok = got == want
    if not ok:
        bad += 1
    print(("PASS" if ok else "FAIL"), label, "-", got if ok else f"got {got!r}, want {want!r}")

alpha = load_register(os.path.join(DEMO, "alpha.json"))
beta = load_register(os.path.join(DEMO, "beta.json"))

# 1. Same method, dataset alpha, canonical reachable
st, pl = resolve(alpha, "opens", {"mail-api": True}, {"opens": 4120})
expect("alpha canonical", (st, pl["source"], pl["value"]), ("ok", "mail-api", 4120))

# 2. Same unedited method, dataset beta
st, pl = resolve(beta, "visits", {"door-log": True}, {"visits": 87})
expect("beta canonical (swap, no method edits)", (st, pl["source"], pl["value"]), ("ok", "door-log", 87))

# 3. Boundary: canonical unreachable, pre-decided fallback used and declared
st, pl = resolve(alpha, "opens", {"mail-api": False, "csv-export": True}, {"opens": 4100})
expect("fallback declared", (st, pl["source"], "note" in pl), ("ok", "csv-export", True))

# 4. Boundary: all sources unreachable -> fixed deferral, no substitution
st, pl = resolve(alpha, "opens", {"mail-api": False, "csv-export": False}, {"opens": 3900})
expect("deferral, no substitution", (st, pl == DEFERRAL.format(metric="opens")), ("defer", True))

# 5. Derived metric computed from components, never fetched directly
st, pl = resolve(alpha, "open-rate", {"mail-api": True}, {"opens": 4120, "subscribers": 10000})
expect("derived from components", (st, round(pl["value"], 4), pl["components"]), ("derived", 0.412, {"opens": 4120, "subscribers": 10000}))

# 6. Boundary: derived metric defers when a component is unavailable
st, pl = resolve(beta, "visits-per-member", {"door-log": False, "paper-sheet": False}, {})
expect("derived defers on missing component", st, "defer")

# 7. Ambiguity: sources disagree, canonical used, discrepancy noted
st, pl = resolve(alpha, "opens", {"mail-api": True, "csv-export": True},
                 {"opens": 4120, "_values": {("opens", "csv-export"): 3999}})
expect("discrepancy: canonical used, noted", (st, pl["source"], pl["value"], "discrepancy" in pl.get("note", "")), ("ok", "mail-api", 4120, True))

# 8. Boundary: unknown reachability fails closed (no ok from an unprobed source)
st, pl = resolve(alpha, "opens", {}, {"opens": 4120})
expect("unknown reachability defers", st, "defer")

# 9. Swap integrity: register schema is the only coupling - beta works with alpha values absent
st, pl = resolve(beta, "members", {"door-log": True}, {"members": 120})
expect("beta stock metric, same unedited code", (st, pl["source"], pl["value"]), ("ok", "door-log", 120))

# 10. Negative: malformed formula rejects the register at load
import json, tempfile
def load_bad(metrics):
    reg = {"dataset": "bad", "sources": {"s1": {"kind": "api"}},
           "metrics": metrics}
    p = os.path.join(tempfile.mkdtemp(), "bad.json")
    with open(p, "w") as f:
        json.dump(reg, f)
    return load_register(p)

try:
    load_bad({"d": {"kind": "derived", "components": ["a"], "formula": "a"}})
    expect("malformed formula rejected", "no error", "ValueError")
except ValueError:
    expect("malformed formula rejected", "ValueError", "ValueError")

# 11. Negative: unsupported operator rejected at load, not silently ignored
try:
    load_bad({"a": {"kind": "flow", "canonical": "s1"}, "b": {"kind": "flow", "canonical": "s1"},
              "d": {"kind": "derived", "components": ["a", "b"], "formula": "a * b"}})
    expect("unsupported operator rejected", "no error", "ValueError")
except ValueError:
    expect("unsupported operator rejected", "ValueError", "ValueError")

# 12. Negative: cyclic derived input (component itself derived) rejected at load
try:
    load_bad({"a": {"kind": "flow", "canonical": "s1"}, "b": {"kind": "flow", "canonical": "s1"},
              "d": {"kind": "derived", "components": ["a", "b"], "formula": "a / b"},
              "e": {"kind": "derived", "components": ["d", "b"], "formula": "d / b"}})
    expect("cyclic derived input rejected", "no error", "ValueError")
except ValueError:
    expect("cyclic derived input rejected", "ValueError", "ValueError")

# 13. Negative: zero denominator defers, never raises
st, pl = resolve(alpha, "open-rate", {"mail-api": True}, {"opens": 4120, "subscribers": 0})
expect("zero denominator defers", (st, "denominator" in pl and "zero" in pl), ("defer", True))

# 14. Negative: reachable canonical but value not fetched defers, no KeyError
st, pl = resolve(alpha, "opens", {"mail-api": True}, {})
expect("unfetched canonical defers", (st, "unavailable" in pl), ("defer", True))

print("RESULT", "all as expected" if bad == 0 else f"{bad} problem(s)")
sys.exit(1 if bad else 0)
