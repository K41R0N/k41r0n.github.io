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
    """Yield (label, ok, reason) per pinned file record.

    A section may pin several files (each `File:`/`Published file:` record
    with its own `Current SHA-256`). Every record is verified, paired with
    the first pin between it and the next record, so a drifted later file in
    a multi-record section cannot pass unchecked.
    """
    text = open(os.path.join(ROOT, relpath), encoding='utf-8').read()
    sections = re.split(r'\n## ', text)
    pin_re = re.compile(r'Current SHA-256: `([0-9a-f]{64})`')
    for sec in sections[1:]:
        records = []
        for pat in entry_file_patterns:
            for m in re.finditer(pat, sec, flags=re.M):
                records.append((m.start(), m.end(), m.group(1)))
        records.sort()
        for i, (start, end, target) in enumerate(records):
            bound = records[i + 1][0] if i + 1 < len(records) else len(sec)
            cur = pin_re.search(sec, end, bound)
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


def expected_targets():
    """Independently maintained inventory: the pinned files as they exist on disk.

    The logs pin every file under these roots, so the on-disk listing is the
    completeness reference: a log truncated after its first complete section
    still has recognized > 0, but no longer covers files this inventory names.
    """
    ps = ['CONTROLLER.md', 'README.md']
    ps_root = os.path.join(ROOT, 'packs/process-standardization')
    skills = os.path.join(ps_root, 'skills')
    if os.path.isdir(skills):
        for dirpath, _, files in os.walk(skills):
            for f in files:
                if f == 'SKILL.md':
                    ps.append(os.path.relpath(os.path.join(dirpath, f), ps_root))
    cm_root = os.path.join(ROOT, 'packs/copywriting-methods', 'sources')
    cm = []
    for dirpath, _, files in os.walk(cm_root):
        for f in files:
            cm.append('agent/' + os.path.relpath(os.path.join(dirpath, f), ROOT))
    return sorted(ps), sorted(cm)


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
        recognized = 0
        # process-standardization: file path is in the section heading
        if 'process-standardization' in relpath:
            for sec in re.split(r'\n## ', text)[1:]:
                title = sec.split('\n', 1)[0].strip()
                m = re.match(r'^`([^`]+)`$', title)
                if not m:
                    continue
                recognized += 1
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
                recognized += 1
                print(('PASS' if ok else 'FAIL'), label, '-', reason)
                bad += 0 if ok else 1
        if recognized == 0:
            # A truncated or format-drifted log compares nothing and must not
            # report clean: the full intended scope has to be recognized first.
            print(f'FAIL {relpath} - no recognized entries; log truncated or entry format drifted, intended scope unverified')
            bad += 1
    # Completeness against the independent on-disk inventory: a partially
    # truncated log still recognizes its surviving sections, so zero-entry
    # rejection alone is not enough; missing targets must be named.
    exp_ps, exp_cm = expected_targets()
    for relpath, pats in jobs:
        text = open(os.path.join(ROOT, relpath), encoding='utf-8').read()
        if 'process-standardization' in relpath:
            logged = set()
            for sec in re.split(r'\n## ', text)[1:]:
                m = re.match(r'^`([^`]+)`$', sec.split('\n', 1)[0].strip())
                if m:
                    logged.add(m.group(1))
            missing = [t for t in exp_ps if t not in logged]
        else:
            logged = set()
            for pat in pats:
                for m in re.finditer(pat, text, flags=re.M):
                    logged.add(m.group(1))
            missing = [t for t in exp_cm if t not in logged]
        for t in missing:
            print(f'FAIL {relpath} - pinned file has no log entry: {t} (log truncated or entry dropped)')
            bad += 1
    print('RESULT', 'all pinned files verified' if not bad else f'{bad} pin(s) failed')
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
