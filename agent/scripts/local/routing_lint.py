#!/usr/bin/env python3
"""Routing lint. Deterministic: no network, no models, stdlib only.

Keeps the brain's routing layer honest:
1. Every repo-relative markdown link in the routing docs resolves to a real file.
2. Every pack under agent/packs/ is routed in agent/packs/index.md and listed in agent/MANIFEST.md.
3. Every skill under agent/skills/ is routed in agent/README.md or agent/skills/README.md.
4. agent/knowledge/methodologies/method-corpus.json is structurally valid:
   required fields, controlled vocabularies, ISO dates, public locations exist,
   every pack has a corpus entry, non-public entries carry no repo path,
   every entry has aliases, aliases are unique across entries with no
   cross-entry substrings, and no bare private-locator-shaped tokens appear.
4b. knowledge/methodologies/routing-cases.json covers every corpus entry and
   each case is executed against the real router (scripts/local/route.py).
4c. When scripts/local/denylist.txt exists, its tokens must not appear in any
   tracked agent file.
5. Migrated pointer files (from the retired methods repo) keep their pointer
   marker and never re-introduce the stale claims that caused the 2026-11-13/14
   routing failures.

Prints one PASS/FAIL line per check, like evals/run.py. Exit nonzero on any FAIL.
Fail closed: an unreadable file is a FAIL, never a skip.
"""
import json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # agent/
REPO = os.path.dirname(ROOT)  # repo root; corpus locations are repo-relative
ROUTING_DOCS = [
    "README.md", "index.md", "AGENTS.md", "CHARTER.md", "HOW-TO-USE-THIS-BRAIN.md",
    "CLAUDE.md",
    "knowledge/methodologies/method-sources.md",
    "packs/index.md", "skills/README.md",
]
POINTER_FILES = [
    "CLAUDE.md",
    "packs/AGENTS.md", "packs/CHARTER.md", "packs/README.md", "packs/HOW-TO-USE-THIS-BRAIN.md",
]
POINTER_MARKER = "Pointer file."
STALE_PHRASES = [
    "private harness repo",
    "This repo holds Alejandro Arango's methods",
    "14 packs",
    "Nothing lands on the default branch except through a pull request he merges",
]
CONFIDENCE = {"operator_reported", "confirmed", "reference", "inferred", "conversation"}
ACCESS = {"public", "private-map", "locked"}
STATUS = {"current", "draft", "held", "retired"}
ISO = re.compile(r"^\d{4}-\d{2}-\d{2}$")
LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
# Backticked path tokens: contain a slash or end in a known extension, no spaces.
BACKTICK = re.compile(r"`([^`]+)`")
PATHISH = re.compile(r"^[./A-Za-z0-9_*-]+(/[./A-Za-z0-9_*-]+)*/?$")
PATH_EXT = (".md", ".py", ".sh", ".yaml", ".yml", ".json", ".txt")
# Named on purpose, never expected in a fresh clone: generated build output and
# the G14 research agent's own external boot file.
NON_REPO_TOKENS = {"dist/", "dist", "admin/config.yml", "SOUL.md", "~/.openclaw/shared/outbox/staged-research/"}

def path_candidates(text):
    for m in BACKTICK.finditer(text):
        tok = m.group(1).strip()
        if " " in tok or not PATHISH.match(tok):
            continue
        if "/" not in tok and not tok.endswith(PATH_EXT):
            continue
        if tok in NON_REPO_TOKENS:
            continue
        yield tok

def resolves(doc_rel, tok):
    import glob as g
    bases = [os.path.dirname(os.path.join(ROOT, doc_rel)), ROOT, REPO]
    for base in bases:
        if g.glob(os.path.normpath(os.path.join(base, tok))):
            return True
    return False

bad = 0
def report(ok, name, detail):
    global bad
    print(("PASS" if ok else "FAIL"), name, "-", detail)
    if not ok: bad += 1

def read(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
        return f.read()

# 1. Links in routing docs resolve
for doc in ROUTING_DOCS:
    try:
        text = read(doc)
    except Exception as e:
        report(False, "links " + doc, f"unreadable: {e}"); continue
    broken = []
    for m in LINK.finditer(text):
        target = m.group(1).split("#")[0].strip()
        if not target or re.match(r"^[a-z]+:", target) or target.startswith("#"):
            continue
        if not resolves(doc, target):
            broken.append(target)
    for tok in set(path_candidates(text)) - set(broken):
        if not resolves(doc, tok):
            broken.append(tok)
    report(not broken, "links " + doc, "all resolve" if not broken else "broken: " + ", ".join(sorted(set(broken))))

# 2. Packs routed and manifest-listed
pack_dirs = sorted(d for d in os.listdir(os.path.join(ROOT, "packs"))
                   if os.path.isdir(os.path.join(ROOT, "packs", d)))
try:
    pack_index = read("packs/index.md"); manifest = read("MANIFEST.md")
except Exception as e:
    report(False, "packs coverage", f"index or manifest unreadable: {e}"); pack_index = manifest = ""
for p in pack_dirs:
    report(p in pack_index, "pack routed " + p, "in packs/index.md" if p in pack_index else "missing from packs/index.md")
    report(p in manifest, "pack manifest " + p, "in MANIFEST.md" if p in manifest else "missing from MANIFEST.md")

# 3. Skills routed
skill_dirs = sorted(d for d in os.listdir(os.path.join(ROOT, "skills"))
                    if os.path.isdir(os.path.join(ROOT, "skills", d)))
try:
    readme = read("README.md"); skills_readme = read("skills/README.md")
except Exception as e:
    report(False, "skills coverage", f"README unreadable: {e}"); readme = skills_readme = ""
for s in skill_dirs:
    ok = s in readme or s in skills_readme
    report(ok, "skill routed " + s, "routed" if ok else "missing from README.md and skills/README.md")

# 4. Corpus registry
try:
    corpus = json.loads(read("knowledge/methodologies/method-corpus.json"))
except Exception as e:
    report(False, "corpus registry", f"unreadable or invalid JSON: {e}"); corpus = None
if corpus is not None:
    entries = corpus.get("entries")
    report(isinstance(entries, list) and len(entries) > 0, "corpus registry", f"{len(entries) if isinstance(entries, list) else 0} entries")
    if isinstance(entries, list):
        required = {"id", "title", "area", "access", "location", "answers", "confidence", "status", "verified"}
        ids = set()
        for e in entries:
            eid = e.get("id", "<no id>")
            missing = required - set(e)
            if missing:
                report(False, "corpus entry " + eid, "missing fields: " + ", ".join(sorted(missing))); continue
            problems = []
            if eid in ids: problems.append("duplicate id")
            ids.add(eid)
            if e["access"] not in ACCESS: problems.append("bad access " + e["access"])
            if e["confidence"] not in CONFIDENCE: problems.append("bad confidence " + e["confidence"])
            if e["status"] not in STATUS: problems.append("bad status " + e["status"])
            if not ISO.match(e["verified"]): problems.append("verified not ISO date")
            if e["access"] == "public":
                if e["location"] in ("private-map", "locked", "retired"):
                    problems.append("public entry without a repo path")
                elif not os.path.exists(os.path.join(REPO, e["location"])):
                    problems.append("location does not exist: " + e["location"])
            else:
                if os.sep in e["location"] or e["location"].endswith(".md"):
                    problems.append("non-public entry carries a path: " + e["location"])
            aliases = e.get("aliases")
            if not aliases or not all(isinstance(a, str) and a.strip() for a in aliases):
                problems.append("missing or empty aliases (route.py depends on them)")
            blob = json.dumps(e)
            if re.search(r"drive\.google|docs\.google|[0-9a-f]{40}", blob):
                problems.append("private locator leaked into registry")
            # Bare-token scan: private locators (Drive file ids and kin) are long
            # runs of alnum/underscore with no hyphens. Never allowed in the
            # public registry, whatever their shape.
            for field in (e["id"], e["title"], e["answers"], e["location"], *(aliases or [])):
                for tok in re.findall(r"[A-Za-z0-9_]{25,}", field):
                    if "-" not in tok:
                        problems.append(f"bare private-locator-shaped token in {eid}: {tok[:12]}...")
            report(not problems, "corpus entry " + eid, "ok" if not problems else "; ".join(problems))
        corpus_packs = {e["location"].split("agent/packs/")[1].strip("/") for e in entries
                        if e.get("area") == "packs" and "agent/packs/" in e.get("location", "")}
        for p in pack_dirs:
            report(p in corpus_packs, "corpus pack " + p, "registered" if p in corpus_packs else "missing from method-corpus.json")
        retired = [e for e in entries if e.get("status") == "retired"]
        for e in retired:
            report(e["access"] != "public", "corpus retired " + e["id"], "retired entry not routable")
        # Alias sanity: unique across entries, and no alias of one entry is a
        # substring of a different entry's alias (that would hide matches or
        # force avoidable ties).
        owner_of = {}
        alias_problems = []
        for e in entries:
            for a in e.get("aliases", []):
                key = a.lower().strip()
                if key in owner_of and owner_of[key] != e["id"]:
                    alias_problems.append(f"alias '{a}' claimed by both {owner_of[key]} and {e['id']}")
                owner_of.setdefault(key, e["id"])
        flat = [(e["id"], a.lower().strip()) for e in entries for a in e.get("aliases", [])]
        for i, (id1, a1) in enumerate(flat):
            for id2, a2 in flat[i + 1:]:
                if id1 != id2 and a1 != a2 and (a1 in a2 or a2 in a1):
                    alias_problems.append(f"cross-entry substring aliases: '{a1}' ({id1}) vs '{a2}' ({id2})")
        report(not alias_problems, "corpus alias uniqueness", "ok" if not alias_problems else "; ".join(alias_problems))

# 4b. Behavioral routing cases execute against the real router.
try:
    sys.path.insert(0, os.path.join(ROOT, "scripts", "local"))
    import importlib
    route_mod = importlib.import_module("route")
except Exception as e:
    route_mod = None
    report(False, "router import", f"scripts/local/route.py not importable: {e}")
if route_mod is not None:
    try:
        cases_doc = json.loads(read("knowledge/methodologies/routing-cases.json"))
        cases = cases_doc["cases"]
        entries = json.loads(read("knowledge/methodologies/method-corpus.json"))["entries"]
        by_id = {e["id"]: e for e in entries}
        covered = {c.get("expected") for c in cases}
        missing = [eid for eid in by_id if eid not in covered]
        report(not missing, "routing-case coverage",
               "every corpus entry has a case" if not missing else "no case for: " + ", ".join(missing))
        for c in cases:
            code, out = route_mod.route(c["input"], entries)
            if c["expected"] == "recovery":
                ok = code == 2 and out.startswith("RECOVERY")
                report(ok, "routing case: " + c["input"][:48],
                       "recovery as expected" if ok else f"expected recovery, got exit {code}: {out.splitlines()[0]}")
            else:
                ok = code == 0 and f"ROUTE: {c['expected']}" in out
                for extra in c.get("also", []):
                    ok = ok and extra in out
                report(ok, "routing case: " + c["input"][:48],
                       "routed to " + c["expected"] if ok else f"expected {c['expected']} (+{c.get('also')}), got exit {code}: {out.splitlines()[0]}")
        # Behavior categories must each be present AND honestly classified -
        # deleting the hard cases (uncovered, tie, negation, multi-intent) is a
        # lint failure, not a smaller suite. Classification is recomputed from
        # router behavior, not trusted from the label.
        def classify(c):
            scored = route_mod.match(c["input"], entries)
            if c["expected"] != "recovery":
                return "multi-intent" if c.get("also") else "entry"
            if route_mod.negated(c["input"]):
                return "negation"
            if not scored:
                return "uncovered"
            top = scored[0][0]
            if sum(1 for s, _e in scored if s == top) > 1:
                return "tie"
            return "other-recovery"
        required = {"uncovered", "tie", "negation", "multi-intent"}
        present = set()
        mislabeled = []
        for c in cases:
            actual = classify(c)
            present.add(actual)
            declared = c.get("category")
            if declared and declared != actual:
                mislabeled.append(f"{c['input'][:40]}: declared {declared}, behaves as {actual}")
        missing_cats = sorted(required - present)
        report(not missing_cats and not mislabeled, "routing behavior categories",
               "all categories present and correctly classified" if not missing_cats and not mislabeled
               else ("missing: " + ", ".join(missing_cats) if missing_cats else "")
                    + ("; mislabeled: " + "; ".join(mislabeled) if mislabeled else ""))
    except Exception as e:
        report(False, "routing cases", f"could not run: {e}")

# 4c. Optional denylist: exact private tokens that must never appear in tracked
# agent files. Active only when scripts/local/denylist.txt exists (one token per line).
deny = os.path.join(ROOT, "scripts", "local", "denylist.txt")
if os.path.exists(deny):
    tokens = [t.strip() for t in open(deny, encoding="utf-8") if t.strip() and not t.startswith("#")]
    hits = []
    for dirpath, _dirs, files in os.walk(ROOT):
        for fn in files:
            fp = os.path.join(dirpath, fn)
            rel = os.path.relpath(fp, ROOT)
            if rel == os.path.join("scripts", "local", "denylist.txt"):
                continue
            try:
                text = open(fp, encoding="utf-8").read()
            except Exception:
                continue
            for t in tokens:
                if t in text:
                    hits.append(f"{t} in {rel}")
    report(not hits, "denylist scan", "clean" if not hits else "; ".join(hits))

# 5. Pointer files stay pointers
for rel in POINTER_FILES:
    try:
        text = read(rel)
    except Exception as e:
        report(False, "pointer " + rel, f"unreadable: {e}"); continue
    problems = []
    if POINTER_MARKER not in text: problems.append("pointer marker missing")
    for phrase in STALE_PHRASES:
        if phrase in text: problems.append("stale claim reintroduced: " + phrase)
    report(not problems, "pointer " + rel, "ok" if not problems else "; ".join(problems))

print("RESULT", "all as expected" if bad == 0 else f"{bad} problem(s)")
sys.exit(1 if bad else 0)
