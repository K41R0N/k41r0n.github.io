#!/usr/bin/env python3
"""Verify the current-state pins in the source-fidelity (redaction) logs.

Both logs pin private source material by hash as provenance; those source
hashes are NOT re-verifiable from this repo and this script does not pretend
otherwise. What it enforces is the drift guard: every entry that names a file
in this repo must carry a `Current SHA-256` field, and that field must match
the file's bytes today. A legitimate edit then fails this check until the log
records the change (follow-on note + re-pinned Current hash), which is the
intended upkeep cycle - never a silent repin.

Logs covered:
- packs/process-standardization/docs/redaction-log.md  (## `path` entries)
- packs/copywriting-methods/redaction-log.md           (Published file /
  File: entries under each ## section)

Run: python3 scripts/local/source_log_check.py  (also wired into evals/run.py)
Prints PASS/FAIL per entry; exit nonzero on any failure.
"""
import hashlib
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # agent/


def check_log(relpath, entry_file_patterns):
    """Yield (label, ok, reason) per pinned file."""
    text = open(os.path.join(ROOT, relpath), encoding='utf-8').read()
    sections = re.split(r'\n## ', text)
    for sec in sections[1:]:
        title = sec.split('\n', 1)[0].strip()
        target = None
        for pat in entry_file_patterns:
            m = re.search(pat, sec)
            if m:
                target = m.group(1)
                break
        if not target:
            continue
        cur = re.search(r'Current SHA-256: `([0-9a-f]{64})`', sec)
        rel = target[len('agent/'):] if target.startswith('agent/') else target
        path = os.path.join(ROOT, rel)
        label = f'{relpath.split("/")[1]}:{target}'
        if not cur:
            yield label, False, 'no Current SHA-256 field (pin the verified current state with its change note)'
        elif not os.path.exists(path):
            yield label, False, f'file missing: {rel}'
        else:
            actual = hashlib.sha256(open(path, 'rb').read()).hexdigest()
            if actual == cur.group(1):
                yield label, True, 'matches'
            else:
                yield label, False, f'current file is {actual[:12]}... but log pins {cur.group(1)[:12]}...; record the change, do not silently repin'


def main():
    bad = 0
    jobs = [
        ('packs/process-standardization/docs/redaction-log.md',
         [r'^`([^`]+)`'], ),  # section title is the repo-relative path
        ('packs/copywriting-methods/redaction-log.md',
         [r'Published file: `([^`]+)`', r'File: `(agent/packs/copywriting-methods/[^`]+)`']),
    ]
    for relpath, pats in jobs:
        text = open(os.path.join(ROOT, relpath), encoding='utf-8').read()
        # process-standardization: file path is in the section heading
        if 'process-standardization' in relpath:
            for sec in re.split(r'\n## ', text)[1:]:
                title = sec.split('\n', 1)[0].strip()
                m = re.match(r'^`([^`]+)`$', title)
                if not m:
                    continue
                rel = m.group(1)
                cur = re.search(r'Current SHA-256: `([0-9a-f]{64})`', sec)
                path = os.path.join(ROOT, 'packs/process-standardization', rel)
                label = f'process-standardization:{rel}'
                if not cur:
                    print(f'FAIL {label} - no Current SHA-256 field'); bad += 1
                elif not os.path.exists(path):
                    print(f'FAIL {label} - file missing: {rel}'); bad += 1
                else:
                    actual = hashlib.sha256(open(path, 'rb').read()).hexdigest()
                    if actual == cur.group(1):
                        print(f'PASS {label}')
                    else:
                        print(f'FAIL {label} - drifted (log pins {cur.group(1)[:12]}..., file is {actual[:12]}...); record the change, do not silently repin'); bad += 1
        else:
            for label, ok, reason in check_log(relpath, pats):
                print(('PASS' if ok else 'FAIL'), label, '-', reason)
                bad += 0 if ok else 1
    print('RESULT', 'all pinned files verified' if not bad else f'{bad} pin(s) failed')
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
