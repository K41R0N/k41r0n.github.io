#!/usr/bin/env python3
"""Derive the rolling summary in routines/writing-runs.md from its run rows.

The summary is evidence for the task-register gates; a hand-maintained
summary drifts (it froze at "2 runs, 0%" while rows sat unruled for weeks).
This script derives the numbers from the table itself:

- ruled runs: outcome is accepted / accepted-minor-edits / edited / rejected
- unruled runs: anything else (pending, not recorded, unknown) - listed, never
  counted; a missing ruling stays unknown, it is never treated as rejection
  or acceptance
- acceptance rate over ruled runs (accepted and accepted-minor-edits count)
- gate streak: trailing ruled runs (by run id) accepted with at most minor
  edits
- cause histogram over ruled non-accepted rows, keyed by the cause's leading
  term

Usage:
  python3 scripts/local/runlog_summary.py              print the derived summary
  python3 scripts/local/runlog_summary.py --check      FAIL if the file's
      Rolling summary block disagrees on the numeric lines (drift guard)

Deterministic: no network, no models, stdlib only.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LOG = ROOT / 'routines' / 'writing-runs.md'
RULED = {'accepted', 'accepted-minor-edits', 'edited', 'rejected'}
COUNTED = {'accepted', 'accepted-minor-edits'}


def parse_rows(text):
    rows = []
    for line in text.splitlines():
        if not line.startswith('| wr-'):
            continue
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        if len(cells) < 8:
            continue
        rows.append({'run': cells[0], 'date': cells[1], 'outcome': cells[4], 'cause': cells[6]})
    rows.sort(key=lambda r: r['run'])
    return rows


def derive(rows):
    ruled = [r for r in rows if r['outcome'].lower() in RULED]
    unruled = [r['run'] for r in rows if r['outcome'].lower() not in RULED]
    n = len(ruled)
    acc = sum(1 for r in ruled if r['outcome'].lower() in COUNTED)
    streak = 0
    for r in reversed(ruled):
        if r['outcome'].lower() in COUNTED:
            streak += 1
        else:
            break
    hist = {}
    for r in ruled:
        if r['outcome'].lower() in COUNTED:
            continue
        key = re.split(r'\s*[/(]', r['cause'])[0].strip().lower() or 'uncategorized'
        hist[key] = hist.get(key, 0) + 1
    return {'ruled': n, 'accepted': acc, 'streak': streak, 'hist': hist, 'unruled': unruled}


def render(d):
    pct = round(100 * d['accepted'] / d['ruled']) if d['ruled'] else 0
    hist = ', '.join(f'{k} {v}' for k, v in sorted(d['hist'].items())) or 'none'
    lines = [
        f"runs ruled: {d['ruled']}",
        f"acceptance rate: {pct}% ({d['accepted']} of {d['ruled']})",
        f"gate streak (accepted with at most minor edits, trailing): {d['streak']}",
        f"cause histogram (ruled, not accepted): {hist}",
        f"unruled runs (never counted): {', '.join(d['unruled']) or 'none'}",
    ]
    return lines


def check(text, d):
    """Compare the derived numbers against the file's Rolling summary block."""
    m = re.search(r'## Rolling summary\n\n((?:    .+\n)+)', text)
    if not m:
        return ['FAIL rolling-summary - no Rolling summary block found']
    block = m.group(1)
    out = []
    pct = round(100 * d['accepted'] / d['ruled']) if d['ruled'] else 0
    pairs = [
        ('runs ruled', rf'runs (?:ruled|at current depth):\s*(\d+)', str(d['ruled'])),
        ('acceptance rate', rf'acceptance rate:\s*(\d+)%', str(pct)),
        ('streak', r'streak[^\n]*?(\d+)(?:/2)?', str(d['streak'])),
    ]
    for label, pat, want in pairs:
        mm = re.search(pat, block)
        if not mm:
            out.append(f'FAIL rolling-summary - cannot locate "{label}" line')
        elif mm.group(1) != want:
            out.append(f'FAIL rolling-summary - {label}: file says {mm.group(1)}, rows derive {want}')
        else:
            out.append(f'PASS rolling-summary - {label} matches the rows ({want})')
    return out


def main(argv):
    text = LOG.read_text(encoding='utf-8')
    d = derive(parse_rows(text))
    if '--check' in argv[1:]:
        out = check(text, d)
        for line in out:
            print(line)
        return 1 if any(l.startswith('FAIL') for l in out) else 0
    print('Derived from the run rows (edit rows, then paste or verify with --check):')
    for line in render(d):
        print('   ', line)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
