#!/usr/bin/env python3
"""Deterministic first stop for method and delivery questions.

Usage: python3 scripts/local/route.py "<the ask>"

Matches the ask against the alias phrases in
knowledge/methodologies/method-corpus.json. Prints exactly one of:

- ROUTE: the single corpus entry that answers the ask, with where to read
  it and the access rule that travels with it, or
- RECOVERY: the recovery contract steps (check the corpus index AND the
  private source map, declare what was checked and not located, open
  loop, and a question only if one genuinely remains). Zero matches, or a tie,
always lands here - the
  router never picks the nearest entry by mood.

Deterministic: no network, no models, stdlib only. It is a first stop,
not semantic search; an unmatched ask is a declared gap, not a failure
to hide. Behavioral cases live in knowledge/methodologies/routing-cases.json
and are enforced by routing_lint.py.
"""
import json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # agent/
REGISTRY = os.path.join(ROOT, "knowledge", "methodologies", "method-corpus.json")

ACCESS_GUIDANCE = {
    "public": "Read it in this repo; it is writable only via the normal lanes (PR).",
    "private-map": "Exact paths live in the private source map (Kairon Drive, reference folder). Re-read the source fresh - never cite from memory. Reference-only: read, never push.",
    "locked": "LOCKED client material: private reconciliation reads only. Never copy contents, never name it in public output.",
}

def load_registry(path=REGISTRY):
    with open(path, encoding="utf-8") as f:
        return json.load(f)["entries"]

def match(intent, entries):
    """Return [(score, entry)] for entries whose aliases appear in the intent, best first."""
    hay = intent.lower()
    scored = []
    for e in entries:
        hits = [a for a in e.get("aliases", []) if a.lower() in hay]
        if hits:
            scored.append((len(hits), e))
    scored.sort(key=lambda s: (-s[0], s[1]["id"]))
    return scored

def recovery(intent, candidates=(), note=None):
    lines = [
        f"RECOVERY: no unique corpus entry answers: {intent}",
    ]
    if note:
        lines.append(note)
    lines += [
        "Do not guess a path and do not route by nearest name. The contract:",
        "1. Check the corpus index (knowledge/methodologies/method-sources.md table / method-corpus.json).",
        "2. Check the private source map (Kairon Drive, reference folder).",
        "3. Only then declare: which sources were checked and what they did NOT locate - never 'no method exists'.",
        "4. Add an open loop in decisions/open-loops.md. Ask him only if a genuinely",
   "   unresolved user-owned fact or decision remains - never a mandatory question,",
   "   and never an absence claim, when the index and map already settle it.",
    ]
    if candidates:
        lines.append("Adjacent entries that partially matched (leads to read, not routes):")
        for e in candidates:
            lines.append(f"- {e['id']}: {e['answers']}")
    return "\n".join(lines)

# Wording this deterministic matcher cannot interpret. When an ask excludes or
# negates, substring hits point at the excluded thing itself - the one route
# guaranteed wrong - so negated asks always go to recovery with the matches
# named as leads to check by reading, never as routes.
NEGATION = ("not ", "n't", "other than", "except", "instead of", "avoid",
            "without", "anything but", "rather than", "exclude", "apart from")

def negated(intent):
    return any(cue in intent.lower() for cue in NEGATION)

def route(intent, entries=None):
    entries = entries if entries is not None else load_registry()
    scored = match(intent, entries)
    if negated(intent):
        return 2, recovery(intent, candidates=[e for _s, e in scored],
                          note="Negation or exclusion wording detected: this matcher cannot interpret it, "
                               "and the excluded topic is exactly what substring matching would hit.")
    if not scored:
        return 2, recovery(intent)
    top = scored[0][0]
    best = [s for s in scored if s[0] == top]
    if len(best) > 1:
        return 2, recovery(intent, candidates=[e for _s, e in best])
    e = best[0][1]
    lines = [
        f"ROUTE: {e['id']}",
        f"Title: {e['title']}",
        f"Answers: {e['answers']}",
        f"Confidence: {e['confidence']} | Status: {e['status']} | Verified: {e['verified']}",
    ]
    if e["status"] == "retired":
        lines.append("RETIRED: do not route here. Canonical home: this repo's agent/.")
    elif e["access"] == "public":
        lines.append(f"Read: {e['location']} (repo-relative)")
        lines.append(ACCESS_GUIDANCE["public"])
    else:
        lines.append(ACCESS_GUIDANCE[e["access"]])
    others = [x for _s, x in scored[1:]]
    if others:
        lines.append("Also matched (if the ask has several intents, route each one):")
        for x in others:
            lines.append(f"- {x['id']}: {x['answers']}")
    return 0, "\n".join(lines)

if __name__ == "__main__":
    if len(sys.argv) < 2 or not sys.argv[1].strip():
        print("usage: python3 scripts/local/route.py \"<the ask>\"")
        sys.exit(64)
    code, out = route(sys.argv[1])
    print(out)
    sys.exit(code)
