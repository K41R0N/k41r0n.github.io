"""Mechanical checks for a prospect research brief. Clean means only the listed patterns were absent."""
import re

REQUIRED = [
    ("scope", r"^## (?:1\. )?Decision|^## Decision", "decision"),
    ("identity", r"business identity|identity status", "business identity"),
    ("goal", r"stated goal|goal source|goal:", "stated goal and source"),
    ("model", r"business model", "business model"),
    ("operations", r"operations", "operations"),
    ("improvements", r"improvement hypothes|candidate improvement", "improvement hypotheses"),
    ("sources", r"sources?", "sources"),
    ("gaps", r"gaps|unknown", "gaps/unknowns"),
]


def check(text):
    out = []
    low = text.lower()
    for key, pattern, label in REQUIRED:
        if not re.search(pattern, low, re.I | re.M):
            out.append(("FAIL", f"PR1-missing-{key}", f"missing {label}"))
    for match in re.finditer(r"(?im)^\s*(?:[-*]\s*)?(?:VERIFIED|REPORTED|INFERRED|SIGNAL|UNKNOWN)\s*:\s*([^\n]*)", text):
        row = match.group(0)
        if re.search(r"(?i)\b(?:source|url|publisher|premises)\b\s*[:=]\s*\S+", row) is None:
            out.append(("FAIL", "PR2-evidence-tag-without-source", row[:80]))
    sections = re.split(r"(?im)^##\s+", text)
    improvement = next((part for part in sections if re.search(r"(?i)improvement hypoth|candidate improvement", part[:100])), "")
    if re.search(r"(?i)\b(?:painful|critical pain|must fix|needs to)\b", improvement) and not re.search(r"(?i)\b(?:hypothesis|validate|unknown|evidence)\b", improvement):
        out.append(("WARN", "PR3-pain-asserted-without-validation", "pain language needs hypothesis/evidence/validation framing"))
    if re.search(r"(?i)\b(?:home address|personal phone|private email|password|ssn)\s*[:=]?\s*\S+", text):
        out.append(("FAIL", "PR4-private-detail", "possible private personal detail"))
    return out
