"""Checks for a drafted answer to a question put to Alejandro (family, friend, client).
Header lines: asker, level (plain|technical), sent_as (draft|him), approved_by (needed when sent_as: him).
Body sections as lines: 'Answer:' (then text), 'Sure:', 'Checked:', 'Not known:', 'Needs him:' (yes|no).
A clean result means only that these patterns were absent. It never certifies that the advice is right or sounds like him."""
import re
RISKY = r"\b(invest|investment|lawyer|legal|contract|diagnos\w*|medication|prescription|tax|lawsuit|loan|mortgage)\b"
JARGON = r"\b(harness|agentic|LLM|S[0-4]|L[0-5]|pipeline|embedding|prompt)\b"

def _hdr(text, key):
    m = re.search(rf"^{key}:\s*(.+)$", text, re.M | re.I)
    return m.group(1).strip() if m else None

def _answer(text):
    m = re.search(r"^Answer:\s*\n?(.*?)(?=^\w[\w ]*:\s|\Z)", text, re.M | re.S)
    return m.group(1).strip() if m else ""

def check(text):
    out = []
    for sec in ["Answer", "Sure", "Checked", "Not known", "Needs him"]:
        if not re.search(rf"^{sec}:", text, re.M):
            out.append(("FAIL", f"AA1-section-missing-{sec.lower().replace(' ', '-')}", sec))
    ans = _answer(text)
    level = (_hdr(text, "level") or "").lower()
    sure = _hdr(text, "Sure") or ""
    checked = (_hdr(text, "Checked") or "").lower()
    needs = (_hdr(text, "Needs him") or "").lower()
    if len(ans.split()) > 200:
        out.append(("WARN", "AA2-answer-too-long", f"{len(ans.split())} words"))
    if ans.count("?") > 2:
        out.append(("WARN", "AA3-too-many-questions", "ask fewer, sharper questions"))
    if level == "plain" and re.search(JARGON, ans, re.I):
        out.append(("WARN", "AA4-jargon-for-plain-asker", "use plain words"))
    for s in re.split(r"(?<=[.!?])\s+", ans):
        if re.search(r"\d+(\.\d+)?\s*(%|x\b)|\$\d", s) and "[src:" not in s:
            out.append(("FAIL", "AA5-number-without-source", s[:50]))
    if sure.lower() not in ("", "none") and checked in ("", "nothing", "none"):
        out.append(("FAIL", "AA6-sure-without-checking", "claims certainty but checked nothing"))
    if re.search(RISKY, ans, re.I) and needs.startswith("no"):
        out.append(("FAIL", "AA7-risky-topic-not-sent-to-him", "money, legal or health advice needs his judgment"))
    if (_hdr(text, "sent_as") or "").lower() == "him" and not re.search(r"^approved_by:\s*\S+", text, re.M):
        out.append(("FAIL", "AA8-in-his-name-without-yes", "nothing goes out in his name without his yes"))
    return out
