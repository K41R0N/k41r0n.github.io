"""Checks for a live-number-answer note. Headers 'probe: ran|skipped' and 'dataset: <id>'.
Sections: '## Sources' ('- source: X | reachable: yes|no|unknown | role: canonical|fallback'),
'## Values' ('- value: metric = n | source: id | as-of: YYYY-MM-DD | status: ok|stale|partial|unavailable|manual|error [| final: yes]'),
'## Refusals' ('- refused: metric | reason: why'), '## Verify' ('- verify: what the human confirms').
A clean result means only that these patterns were absent. It never certifies that the numbers are right."""
import re
STATUSES = ("ok", "stale", "partial", "unavailable", "manual", "error")

def _sections(text):
    parts = re.split(r"^## (.+?)\s*$", text, flags=re.M)
    return {parts[i].strip(): parts[i + 1] for i in range(1, len(parts) - 1, 2)}

def _items(body):
    return [l.strip() for l in body.splitlines() if l.strip().startswith("- ")]

def check(text):
    out = []
    sec = _sections(text)
    probe = (re.search(r"^probe:\s*(\w+)", text, re.M) or [None, ""])[1]
    if probe not in ("ran", "skipped"):
        out.append(("FAIL", "LN0-probe-missing", "probe: ran or probe: skipped, declared"))
    if not re.search(r"^dataset:\s*\S+", text, re.M):
        out.append(("FAIL", "LN0-dataset-missing", "name the dataset register"))
    sources = {}
    for s in _items(sec.get("Sources", "")):
        m = re.match(r"- source:\s*(\S+).*?\| reachable:\s*(yes|no|unknown)", s)
        if m:
            sources[m.group(1)] = m.group(2)
        else:
            out.append(("FAIL", "LN1-source-undeclared", s[:60]))
    for v in _items(sec.get("Values", "")):
        m = re.match(r"- value:\s*(.+?)\s*=\s*(\S+).*?\| source:\s*(\S+).*?\| as-of:\s*(\d{4}-\d{2}-\d{2}).*?\| status:\s*(\w+)", v)
        if not m:
            out.append(("FAIL", "LN2-value-without-source-or-asof", v[:60]))
            continue
        metric, _num, src, _date, status = m.groups()
        if status not in STATUSES:
            out.append(("FAIL", "LN3-status-invalid", v[:60]))
        if src in sources and sources[src] == "no":
            out.append(("FAIL", "LN4-unreachable-source-used", f"{metric} cites {src}, declared unreachable"))
        if status == "stale" and "| final: yes" in v:
            out.append(("FAIL", "LN5-stale-pasted-as-final", v[:60]))
        if re.search(r"approximately|about |~", _num):
            out.append(("FAIL", "LN6-estimate-wording", v[:60]))
    refused = _items(sec.get("Refusals", ""))
    for r in refused:
        if "| reason:" not in r:
            out.append(("FAIL", "LN7-refusal-without-reason", r[:60]))
    ok_values = [v for v in _items(sec.get("Values", "")) if "| status: ok" in v]
    if ok_values and not _items(sec.get("Verify", "")):
        out.append(("FAIL", "LN8-verify-missing", "ok values need the human-verify step"))
    return out
