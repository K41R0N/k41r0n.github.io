"""Structural checks for process-standardization plans and artifacts.

A clean result proves only that required procedural safeguards are present;
it does not certify the correctness, usefulness, or quality of the method.
"""
import re

REQUIRED_METHOD = [
    ("PS1-bootstrap", r"^# Bootstrap\s*$"),
    ("PS2-extraction", r"^# Interview extraction\s*$"),
    ("PS3-synthesis", r"^# Cross-interview synthesis\s*$"),
    ("PS4-manifest", r"^# Action manifest\s*$"),
    ("PS5-sop", r"^# SOP drafting\s*$"),
    ("PS6-review", r"^# Interviewee review summary\s*$"),
    ("PS7-playbook", r"^# Playbook assembly\s*$"),
    ("PS8-audit", r"^# Process-standardization audit \(read-only\)\s*$"),
]
REQUIRED_GUARDS = [
    ("PS9-traceability", r"traceab"),
    ("PS10-variants", r"PRESERVE-VARIANT"),
    ("PS11-no-invention", r"do not invent|never fabricate"),
    ("PS12-fact-inference", r"FACT.*INFERENCE|FACT.*inference"),
    ("PS13-clean-run", r"clean run|clean pipeline"),
    ("PS14-no-patch", r"patch-mode|patch flow|patching"),
]


def check(text):
    out = []
    for name, pattern in REQUIRED_METHOD:
        if not re.search(pattern, text, re.M | re.I):
            out.append(("FAIL", name, "required stage section missing"))
    for name, pattern in REQUIRED_GUARDS:
        if not re.search(pattern, text, re.I | re.S):
            out.append(("FAIL", name, "required method safeguard missing"))
    return out
