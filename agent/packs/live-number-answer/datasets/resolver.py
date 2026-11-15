#!/usr/bin/env python3
"""Dataset-agnostic metric resolver for the live-number-answer pack.
Stdlib only, deterministic, no network: reachability is declared input, as the
probe records it. The method code holds no dataset facts; any register that
matches the schema works unchanged.

Derived formula schema: exactly "A / B", a ratio of the metric's two declared
components in declared order. Malformed formulas, unsupported operators, and
cyclic derived inputs (a component that is itself derived) reject the register
at load. A zero denominator or a reachable-but-unfetched value defers instead
of raising."""
import json

DEFERRAL = "cannot report {metric}: its sources could not be reached; retry when the source is back"

def _parse_formula(entry, derived_ids):
    """Validate a derived entry. Returns (numerator, denominator)."""
    formula = entry.get("formula")
    comps = entry.get("components")
    if not isinstance(formula, str) or not isinstance(comps, list) or len(comps) != 2:
        raise ValueError("derived metric needs a formula string and exactly two components")
    parts = formula.split()
    if len(parts) != 3 or parts[1] != "/":
        raise ValueError(f"unsupported formula {formula!r}: only the ratio 'A / B' is supported")
    if parts[0] != comps[0] or parts[2] != comps[1]:
        raise ValueError(f"formula {formula!r} does not match declared components {comps!r}")
    for c in comps:
        if c in derived_ids:
            raise ValueError(f"cyclic derived input: component {c!r} is itself derived")
    return comps[0], comps[1]

def load_register(path):
    with open(path, encoding="utf-8") as f:
        reg = json.load(f)
    derived_ids = {m for m, e in reg["metrics"].items() if e.get("kind") == "derived"}
    for mid, entry in reg["metrics"].items():
        if entry.get("kind") == "derived":
            try:
                _parse_formula(entry, derived_ids)
            except ValueError as e:
                raise ValueError(f"{mid}: {e}")
    return reg

def resolve(register, metric, reachable, fetched, _seen=None):
    """Resolve one metric. reachable: {source: bool}. fetched: {metric: number}.
    Returns (status, payload): ('ok', {'value': v, 'source': s}) or
    ('defer', message) or ('derived', {'value': v, 'components': {...}})."""
    entry = register["metrics"].get(metric)
    if entry is None:
        return ("defer", DEFERRAL.format(metric=metric) + "; metric not in register")
    if entry["kind"] == "derived":
        seen = (_seen or set()) | {metric}
        comps = {}
        for c in entry["components"]:
            if c in seen:
                return ("defer", DEFERRAL.format(metric=metric) + f"; cyclic derived input {c}")
            st, pl = resolve(register, c, reachable, fetched, seen)
            if st not in ("ok",):
                return ("defer", DEFERRAL.format(metric=metric) + f"; component {c} unavailable")
            comps[c] = pl["value"]
        num, den = _parse_formula(entry, set())
        if comps[den] == 0:
            return ("defer", DEFERRAL.format(metric=metric) + f"; denominator {den} is zero")
        return ("derived", {"value": comps[num] / comps[den], "components": comps})
    canonical = entry["canonical"]
    # Reachability semantics: only an explicit True counts as reachable.
    # False and unknown (missing) both fail closed toward fallback or deferral.
    values = fetched.get("_values", {})
    if reachable.get(canonical) is True:
        if metric not in fetched:
            return ("defer", DEFERRAL.format(metric=metric) + "; canonical value unavailable (not fetched)")
        payload = {"value": fetched[metric], "source": canonical}
        fallback = entry.get("fallback")
        if fallback and reachable.get(fallback) is True:
            other = values.get((metric, fallback))
            if other is not None and other != fetched[metric]:
                payload["note"] = "sources disagree; canonical used, discrepancy noted"
        return ("ok", payload)
    fallback = entry.get("fallback")
    if fallback and reachable.get(fallback) is True:
        if metric not in fetched:
            return ("defer", DEFERRAL.format(metric=metric) + "; fallback value unavailable (not fetched)")
        return ("ok", {"value": fetched[metric], "source": fallback, "note": "canonical unreachable; pre-decided fallback used"})
    return ("defer", DEFERRAL.format(metric=metric))
