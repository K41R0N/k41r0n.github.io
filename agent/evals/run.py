#!/usr/bin/env python3
"""Eval runner v0. Deterministic: no network, no models.
Each pack has evals/checks.py with check(text) -> list of (level, id, message)
and fixtures/<name>.md with fixtures/<name>.expect (one expected id per line, or the word clean).
A fixture passes when the set of ids found equals the expected set.
Exit code is nonzero if any fixture differs from its expectation, or a pack has no failing fixture."""
import importlib.util, os, sys, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load(path):
    spec = importlib.util.spec_from_file_location("checks", path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

def main(argv):
    only = argv[1] if len(argv) > 1 else None
    bad = 0
    for pack in sorted(glob.glob(os.path.join(ROOT, "packs", "*"))):
        if not os.path.isdir(pack): continue
        name = os.path.basename(pack)
        if only and only != name: continue
        try:
            mod = load(os.path.join(pack, "evals", "checks.py"))
        except Exception as e:
            print(f"BLOCK {name} - checks failed to load: {e}"); bad += 1; continue
        fixtures = sorted(glob.glob(os.path.join(pack, "fixtures", "*.md")))
        has_fail = False
        if not fixtures:
            print(f"FAIL {name} - no fixtures"); bad += 1; continue
        for fx in fixtures:
            fname = os.path.basename(fx)
            text = open(fx, encoding="utf-8").read()
            try:
                found = {i for (_lvl, i, _m) in mod.check(text)}
                exp = {l.strip() for l in open(fx[:-3] + ".expect") if l.strip()}
            except Exception as e:
                print(f"BLOCK {name} {fname} - check errored or expectation unreadable: {e}"); bad += 1; continue
            exp = set() if exp == {"clean"} else exp
            if exp: has_fail = True
            if found == exp:
                print(f"PASS {name} {fname} - found {sorted(found) or 'clean'}")
            else:
                bad += 1
                print(f"FAIL {name} {fname} - expected {sorted(exp) or 'clean'}, found {sorted(found) or 'clean'}")
        if not has_fail:
            bad += 1; print(f"FAIL {name} - no fixture that fails on purpose")
    print("RESULT", "all as expected" if bad == 0 else f"{bad} problem(s)")
    return 1 if bad else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
