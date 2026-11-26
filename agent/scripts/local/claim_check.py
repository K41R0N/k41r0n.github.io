#!/usr/bin/env python3
"""Verify completion claims about a writing run against its actual record.

A claim passes only when the run's own receipts prove it:

- --claim STEP: a receipt for STEP exists in the expected sequence, passes
  the full receipt contract validation (writing.py replay: schema, hashes,
  sequence position), and carries decision=pass.
- --complete: every step in the run's expected sequence has such a receipt.

This catches the failure classes that mere presence checks miss: missing
receipts, tampered or stale records (brief/snapshot/artifact hash mismatch),
incomplete sequences, and claims about steps the brief never planned. Any
error while loading or validating the record fails every claim (fail
closed); an unreadable record is never a pass.

A passing result means the RECORD supports the claim. It never certifies
output quality - run state itself reports quality as uncalibrated and the
author's ruling is a separate step (evals/contract.md rules 2 and 11).

Usage: python3 scripts/local/claim_check.py RUN_DIR [--claim STEP]... [--complete]
Prints one PASS/FAIL line per claim, with the reason. Exit nonzero on any
failed claim.
"""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import writing as w


def verify(run_dir, claims, complete):
    out = []
    try:
        d, s, b = w.load(run_dir)
        seq = w.replay(s, b)
        done = [w.read(w.checked(ref))['step'] for ref in s['receipts']]
    except Exception as e:
        for c in claims:
            out.append((False, c, f'record unreadable or tampered: {e}'))
        if complete:
            out.append((False, 'complete', f'record unreadable or tampered: {e}'))
        return out
    for c in claims:
        if c not in seq:
            out.append((False, c, f'not a step this brief plans (planned: {", ".join(seq)}); claim does not match the record'))
        elif c not in done:
            stop = done[-1] if done else 'no steps'
            out.append((False, c, f'no recorded passing receipt; the record stops at: {stop}'))
        else:
            out.append((True, c, 'recorded receipt validated: contract fields, hashes and pass decision'))
    if complete:
        if len(s['receipts']) == len(seq):
            out.append((True, 'complete',
                        f'all {len(seq)} steps recorded and validated; output quality stays uncalibrated - the author ruling is separate'))
        else:
            out.append((False, 'complete',
                        f'{len(s["receipts"])} of {len(seq)} steps recorded; next unrecorded step: {seq[len(s["receipts"])]}'))
    return out


def main(argv):
    p = argparse.ArgumentParser(description='Verify completion claims against a writing run record.')
    p.add_argument('run_dir')
    p.add_argument('--claim', action='append', default=[], metavar='STEP')
    p.add_argument('--complete', action='store_true')
    a = p.parse_args(argv[1:])
    if not a.claim and not a.complete:
        print('nothing claimed: pass --claim STEP and/or --complete')
        return 64
    bad = 0
    for ok, label, reason in verify(a.run_dir, a.claim, a.complete):
        print(('PASS' if ok else 'FAIL'), label, '-', reason)
        bad += 0 if ok else 1
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
