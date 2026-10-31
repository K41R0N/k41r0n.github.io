"""Mechanical checks for a prospect research brief. Clean means only listed patterns are absent."""
import re

SECTION_NAMES = ("Decision", "Business identity", "Stated goal and source", "Business model", "Operations", "Improvement hypotheses", "Sources", "Gaps")
LABELS = {"VERIFIED", "REPORTED", "INFERRED", "SIGNAL", "UNKNOWN"}


def sections(text):
    parts = re.split(r"(?im)^##\s+(.+?)\s*$", text)
    return {parts[i].strip().lower(): parts[i + 1].strip() for i in range(1, len(parts) - 1, 2)}


def check(text):
    out = []
    sec = sections(text)
    aliases = {
        "decision": ("decision",),
        "business identity": ("business identity", "identity status"),
        "stated goal and source": ("stated goal and source", "goal source"),
        "business model": ("business model",),
        "operations": ("operations",),
        "improvement hypotheses": ("improvement hypotheses", "candidate improvement"),
        "sources": ("sources",),
        "gaps": ("gaps", "unknowns"),
    }
    resolved = {}
    for name in SECTION_NAMES:
        candidates = aliases[name.lower()]
        body = next((sec[c] for c in candidates if c in sec), "")
        resolved[name.lower()] = body
        meaningful = [line.strip() for line in body.splitlines() if line.strip() and not line.strip().startswith("<!--")]
        # Explicit, sourced UNKNOWN claims count as filled fields, including the stated
        # goal when it is not known. Empty headings and placeholders do not.
        has_content = any(not re.match(r"(?i)^(?:VERIFIED|REPORTED|INFERRED|SIGNAL|UNKNOWN)\s*:\s*$", line) for line in meaningful)
        is_explicit_unknown = bool(re.search(r"(?im)^\s*(?:[-*]\s*)?UNKNOWN\s*:\s*\S", body))
        if not meaningful or (not has_content and not is_explicit_unknown):
            out.append(("FAIL", f"PR1-missing-{name.lower().replace(' ', '-')}", f"missing or empty {name}"))

    # Check inline evidence tags and ledger rows. Ledger columns follow the documented
    # id | claim | evidence label | source(s) format; UNKNOWN may be source-search record.
    for line in text.splitlines():
        tag = re.match(r"(?im)^\s*(?:[-*]\s*)?(VERIFIED|REPORTED|INFERRED|SIGNAL|UNKNOWN)\s*:\s*(.*)$", line)
        ledger = re.match(r"^\s*\|\s*[^|]+\|\s*[^|]+\|\s*(VERIFIED|REPORTED|INFERRED|SIGNAL|UNKNOWN)\s*\|\s*([^|]*)\|", line, re.I)
        if tag:
            label, payload = tag.group(1).upper(), tag.group(2)
            if label != "UNKNOWN" and not re.search(r"(?i)\b(?:source|url|publisher|premises)\b\s*[:=]\s*\S+", payload):
                out.append(("FAIL", "PR2-evidence-tag-without-source", line[:100]))
        elif ledger:
            label, source = ledger.group(1).upper(), ledger.group(2).strip()
            if label != "UNKNOWN" and not source:
                out.append(("FAIL", "PR2-evidence-tag-without-source", line[:100]))

    # Examine each improvement line separately, so an unrelated supported claim does not
    # excuse a second unsupported assertion. The warnings require human review.
    improvements = resolved.get("improvement hypotheses", "")
    for line in improvements.splitlines():
        if re.search(r"(?i)\b(?:painful|critical pain|must fix|needs to)\b", line) and not re.search(r"(?i)\b(?:hypothesis|validate|unknown|evidence)\b", line):
            out.append(("WARN", "PR3-pain-asserted-without-validation", line.strip()[:100]))

    # Only a concrete value after a sensitive field label is a failure. Explicit absence
    # statements such as “No personal phone collected” are not leaks.
    if re.search(r"(?i)\b(?:home address|personal phone|private email|password|ssn)\s*[:=]\s*(?!none\b|unknown\b|not collected\b|redacted\b|n/?a\b|$)\S+", text):
        out.append(("FAIL", "PR4-private-detail", "possible private personal detail"))
    return out
