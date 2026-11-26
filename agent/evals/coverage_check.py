#!/usr/bin/env python3
"""Per-check fixture coverage for the pack evals.

The eval runner proves a fixture's expected IDs are the exact set its run
through check() produces, so an ID listed in a .expect file is a proven
signal, not text presence. This script closes the remaining gap: every ID a
pack's checks.py declares in CHECK_IDS must be exercised by at least one
fixture, or carry an explicit CONDITIONAL reason (a dependent check whose
trigger cannot stand alone). It also fails on stale .expect IDs the module
no longer declares, and on literal check IDs in the source missing from
CHECK_IDS (registry drift).

Run: python3 evals/coverage_check.py   (also wired into evals/run.py)
Prints PASS/FAIL per pack; exit nonzero on any failure.
"""
import glob
import importlib.util
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load(path):
    spec = importlib.util.spec_from_file_location('checks_cov', path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def main():
    bad = 0
    for cp in sorted(glob.glob(os.path.join(ROOT, 'packs', '*', 'evals', 'checks.py'))):
        pack = cp.split(os.sep)[-3]
        src = open(cp, encoding='utf-8').read()
        mod = load(cp)
        declared = list(getattr(mod, 'CHECK_IDS', []))
        conditional = dict(getattr(mod, 'CONDITIONAL', {}))
        problems = []
        if not declared:
            problems.append('no CHECK_IDS registry')
        expected = set()
        for e in glob.glob(os.path.join(ROOT, 'packs', pack, 'fixtures', '*.expect')):
            for line in open(e, encoding='utf-8'):
                line = line.strip()
                if line and line != 'clean':
                    expected.add(line)
        for cid in declared:
            if cid in conditional:
                if not str(conditional[cid]).strip():
                    problems.append(f'{cid}: CONDITIONAL reason is empty')
            elif cid not in expected:
                problems.append(f'{cid}: declared but no fixture exercises it')
        for cid in sorted(expected - set(declared)):
            problems.append(f'{cid}: fixture expects an ID the module does not declare')
        for cid in sorted(set(re.findall(r'(?<!f)"([A-Z]{1,5}\d+-[a-z0-9][a-z0-9-]*)"', src)) - set(declared)):
            problems.append(f'{cid}: literal ID in source missing from CHECK_IDS')
        for cid in sorted(set(conditional) - set(declared)):
            problems.append(f'{cid}: CONDITIONAL entry not in CHECK_IDS')
        if problems:
            bad += 1
            for p in problems:
                print(f'FAIL {pack} - {p}')
        else:
            print(f'PASS {pack} - {len(declared)} checks, all exercised or accounted')
    print('RESULT', 'all covered' if not bad else f'{bad} pack(s) with coverage gaps')
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
