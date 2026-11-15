"""Checks for a knowledge-edit-discipline note. Headers 'file: <path>' and 'reason: <why>'.
Sections: '## Audit' ('- audited: what was listed/read'), '## Archive' ('- archive: path | date: YYYY-MM-DD'),
'## Change' ('- change: what'), '## Verify' ('- verify: re-read result | result: landed|failed'),
'## Indexes' ('- index: name | updated: yes|no').
A clean result means only that these patterns were absent. It never certifies that the edit was right."""
import re

def _sections(text):
    parts = re.split(r"^## (.+?)\s*$", text, flags=re.M)
    return {parts[i].strip(): parts[i + 1] for i in range(1, len(parts) - 1, 2)}

def _items(body):
    return [l.strip() for l in body.splitlines() if l.strip().startswith("- ")]

def check(text):
    out = []
    sec = _sections(text)
    if not re.search(r"^file:\s*\S+", text, re.M):
        out.append(("FAIL", "KE0-file-missing", "name the destination file"))
    if not re.search(r"^reason:\s*\S", text, re.M):
        out.append(("FAIL", "KE0-reason-missing", "state the reason for the change"))
    if not _items(sec.get("Audit", "")):
        out.append(("FAIL", "KE1-no-audit", "audit the destination before writing"))
    arch = _items(sec.get("Archive", ""))
    changes = _items(sec.get("Change", ""))
    if changes and not arch:
        out.append(("FAIL", "KE2-overwrite-without-archive", "versioned dated archive copy before any overwrite"))
    for a in arch:
        if not re.search(r"\| date:\s*\d{4}-\d{2}-\d{2}", a):
            out.append(("FAIL", "KE3-archive-undated", a[:60]))
    verify = _items(sec.get("Verify", ""))
    if changes and not verify:
        out.append(("FAIL", "KE4-no-post-write-verify", "re-read the written file"))
    for v in verify:
        if "result: failed" in v and not re.search(r"restored|restore", v):
            out.append(("FAIL", "KE5-failed-verify-without-restore", "stop, restore from the archive copy, report"))
    if changes and not _items(sec.get("Indexes", "")):
        out.append(("FAIL", "KE6-indexes-stale", "update routing and retrieval indexes after the edit"))
    return out
