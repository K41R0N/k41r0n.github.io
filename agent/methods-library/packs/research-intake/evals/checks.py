"""Checks for a research-intake canvas ('data binge mode').
Format: header 'topic:' and 'mode: binge'; '## Entries' with lines '- e1 | source: ... | text';
sorting sections '## Labels', '## Topics', '## Use cases', '## People', '## Entities' (lines list entry ids);
'## Threads' lines '- name | e1, e2'; '## Unsorted' (ids that fit nowhere yet); a line 'Unread:'; '## Outputs' lines '- kind | status: proposed'.
A clean result means only that these patterns were absent. It never certifies that the threads are right."""
import re

SORT = ["Labels", "Topics", "Use cases", "People", "Entities"]

def _sections(text):
    parts = re.split(r"^## (.+?)\s*$", text, flags=re.M)
    return {parts[i].strip(): parts[i + 1] for i in range(1, len(parts) - 1, 2)}

def check(text):
    out = []
    if not re.search(r"^topic:\s*\S", text, re.M): out.append(("FAIL", "RI1-topic-missing", "add 'topic:'"))
    sec = _sections(text)
    entries = [l for l in sec.get("Entries", "").splitlines() if l.strip().startswith("- ")]
    ids = set()
    if not entries: out.append(("FAIL", "RI2-no-entries", "nothing was taken in"))
    for l in entries:
        m = re.match(r"-\s*(e\d+)\s*\|", l.strip())
        if not m: out.append(("FAIL", "RI2-bad-entry", l[:40])); continue
        ids.add(m.group(1))
        if not re.search(r"\|\s*source:\s*\S", l): out.append(("FAIL", "RI3-entry-without-source", m.group(1)))
    placed = set()
    for name in SORT + ["Unsorted"]:
        placed |= set(re.findall(r"\be\d+\b", sec.get(name, "")))
    if ids - placed: out.append(("FAIL", "RI4-entry-dropped", ",".join(sorted(ids - placed))))
    cited = set(re.findall(r"\be\d+\b", "".join(sec.get(n, "") for n in SORT + ["Unsorted", "Threads"])))
    if cited - ids: out.append(("FAIL", "RI5-dangling-id", ",".join(sorted(cited - ids))))
    for l in sec.get("Threads", "").splitlines():
        if l.strip().startswith("-") and len(set(re.findall(r"\be\d+\b", l))) < 2:
            out.append(("FAIL", "RI6-thread-needs-two-entries", l[:40]))
    if re.search(r"[\w.+-]+@[\w-]+\.[\w.]+|\+?\d[\d\s().-]{8,}\d", sec.get("People", "")):
        out.append(("FAIL", "RI7-contact-details-in-people", "names only; keep contact details in the source"))
    if not re.search(r"^Unread:", text, re.M): out.append(("FAIL", "RI8-unread-line-missing", "add 'Unread: none' or list them"))
    for l in sec.get("Outputs", "").splitlines():
        if l.strip().startswith("-") and not re.search(r"status:\s*proposed", l):
            out.append(("FAIL", "RI9-output-not-proposed", l[:40]))
    return out
