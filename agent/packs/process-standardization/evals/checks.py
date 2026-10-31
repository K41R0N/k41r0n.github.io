"""Structural checks for the preserved process-standardization source documents."""
from pathlib import Path
import hashlib
import re

REQUIRED_DOCS = [
    "CONTROLLER.md",
    "README.md",
    "skills/action-manifest/SKILL.md",
    "skills/cross-interview-synthesis/SKILL.md",
    "skills/interview-extraction/SKILL.md",
    "skills/interviewee-review-summary/SKILL.md",
    "skills/playbook-assembler/SKILL.md",
    "skills/process-standardization-audit/SKILL.md",
    "skills/process-standardization-bootstrap/SKILL.md",
    "skills/sop-drafter/SKILL.md",
]


def check(text):
    """Check a fixture-shaped output includes core procedural safeguards."""
    required = [
        ("PS1-traceability", r"traceab"),
        ("PS2-no-invention", r"do not invent|never fabricate"),
        ("PS3-variants", r"PRESERVE-VARIANT|role-specific differences"),
        ("PS4-fact-inference", r"FACT.*INFERENCE|FACT.*inference"),
        ("PS5-review", r"review"),
        ("PS6-clean-run", r"clean run|clean pipeline"),
    ]
    return [("FAIL", rule, "required method safeguard missing")
            for rule, pattern in required if not re.search(pattern, text, re.I | re.S)]


def check_source_tree(pack_dir):
    """Return missing files and redaction-log hash mismatches for all source docs."""
    pack_dir = Path(pack_dir)
    log = (pack_dir / "docs/redaction-log.md").read_text(encoding="utf-8")
    issues = []
    for relative in REQUIRED_DOCS:
        path = pack_dir / relative
        if not path.is_file():
            issues.append(f"missing:{relative}")
            continue
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        if digest not in log:
            issues.append(f"unlogged-hash:{relative}")
    return issues
