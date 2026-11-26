#!/usr/bin/env python3
"""Keep the Wikipedia "Signs of AI writing" candidate list current.

Owner request (2026-11-26): tie the writing-pattern deny candidates to
https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing and update regularly
through a script, because that page updates all the time.

What this does:
  1. Pins the page's current revision (id + timestamp) via the MediaWiki API.
  2. Fetches that exact revision's full wikitext in one call.
  3. Extracts, deterministically:
     - vocabulary candidates from every "Words to watch" box (with each term's
       qualifier and source section);
     - a pattern index from the level-3 section headings, grouped by parent.
  4. Writes knowledge/voice/refs/wiki-ai-signs-candidates.txt with full
     provenance in the header, and prints a unified diff against the previous
     file.

What this does NOT do:
  - It does not touch scripts/local/denylist.txt. That file is the privacy
    guard (client names, secrets); this list is writing patterns. Separate
    checks, per the owner 2026-11-26.
  - It does not ban anything. Per refs/anti-pattern-method.md, a candidate tell
    is not a personal ban. Adoption goes through ban_list.py (a word is banned
    only if he never uses it in corpus/raw) and his confirmation.

Exit codes: 0 = no change; 1 = additions only (written; skim the diff);
2 = removals or changed entries (written; REVIEW REQUIRED - the source dropped
or reworded a pattern, so any local use of it needs a human look).
--dry-run prints the diff and the would-be exit code without writing.
--self-test runs the extractor on a saved fixture of real wikitext, no network.

Run cadence: the page is edited most weeks (sometimes daily). Rerun weekly,
and before publishing prose. Stdlib only.
"""
import datetime as dt
import difflib
import json
import os
import re
import sys
import urllib.parse
import urllib.request

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
OUT = os.path.join(ROOT, 'knowledge', 'voice', 'refs', 'wiki-ai-signs-candidates.txt')
FIXTURE = os.path.join(os.path.dirname(__file__), 'fixtures', 'wiki-signs-sample.json')
PAGE = 'Wikipedia:Signs of AI writing'
PAGE_URL = 'https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing'
API = 'https://en.wikipedia.org/w/api.php'
UA = {'User-Agent': 'kairon-harness-wiki-signs-updater/1.0 (contact: github.com/K41R0N)'}
META_PARENTS = {'Notes', 'References', 'See also', 'Further reading', 'External links'}
VERSION = 2


def get_json(params):
    url = API + '?' + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def fetch_page():
    """Return (revid, rev_timestamp, full wikitext, toc) for the pinned current revision.

    toc is the API's own clean section list: [(parent_title, title)] for level-3+
    sections under non-meta level-2 parents, in document order."""
    meta = get_json({'action': 'query', 'prop': 'revisions', 'titles': PAGE,
                     'rvprop': 'ids|timestamp', 'rvlimit': 1, 'format': 'json', 'formatversion': '2'})
    rev = meta['query']['pages'][0]['revisions'][0]
    revid, revts = rev['revid'], rev['timestamp']
    body = get_json({'action': 'parse', 'oldid': revid, 'prop': 'wikitext|sections',
                     'format': 'json', 'formatversion': '2'})
    toc, parent = [], ''
    for sec in body['parse']['sections']:
        if sec['level'] == '2':
            parent = sec['line']
        elif int(sec['level']) >= 3 and parent and parent not in META_PARENTS:
            toc.append((parent, sec['line']))
    return revid, revts, body['parse']['wikitext'], toc


def split_sections(wikitext, toc):
    """Split full wikitext into (parent, clean_title, section_text), aligned by title.

    The wikitext is cut at every heading; each level-3+ chunk's own heading is
    cleaned and matched against the API toc in document order. Chunks whose
    heading is not in the toc (level-3+ children of meta parents such as
    Notes, which fetch_page excludes) are dropped, so one excluded child can
    never shift the pairing of every later eligible section."""
    chunks, buf = [], []
    for line in wikitext.splitlines():
        if re.match(r'^={2,6}\s*.+?\s*=+\s*$', line):
            if buf:
                chunks.append(buf)
            buf = [line]
        elif buf:
            buf.append(line)
    if buf:
        chunks.append(buf)
    # drop chunks before the first level-3 heading (lead + level-2-only text)
    chunks = [c for c in chunks if re.match(r'^={3,6}\s*.+?\s*=+\s*$', c[0])]
    sections, ti = [], 0
    for c in chunks:
        title = clean_text(re.sub(r'^=+\s*|\s*=+$', '', c[0]))
        k = ti
        while k < len(toc) and toc[k][1] != title:
            k += 1
        if k < len(toc):
            # matched: pair with the toc entry, continue after it; an
            # unmatched (meta-parented) chunk is dropped without consuming
            # toc entries, so later eligible sections keep their titles
            sections.append((toc[k][0], toc[k][1], '\n'.join(c)))
            ti = k + 1
    return sections


def strip_templates(s):
    """Remove balanced {{...}} spans (citations etc.) and <ref> tags."""
    out, i, depth = [], 0, 0
    while i < len(s):
        if s.startswith('{{', i):
            depth += 1
            i += 2
        elif s.startswith('}}', i) and depth:
            depth -= 1
            i += 2
        elif depth == 0:
            out.append(s[i])
            i += 1
        else:
            i += 1
    s = ''.join(out)
    s = re.sub(r'<ref\b[^>]*/>', ' ', s)                 # self-closing first
    s = re.sub(r'<ref\b[^>]*>.*?</ref>', ' ', s, flags=re.S)  # then paired
    s = re.sub(r'<ref\b[^>]*>', ' ', s)                  # then anything malformed
    return s


def strong_spans(wikitext):
    """Yield the inner text of every {{strong|...}} following a 'Words to watch:' label."""
    for m in re.finditer(r'Words to watch:', wikitext):
        i = wikitext.find('{{strong|', m.end())
        if i == -1:
            continue
        start = i + len('{{strong|')
        j, depth = start, 1
        while j < len(wikitext) and depth:
            if wikitext.startswith('{{', j):
                depth += 1
                j += 2
            elif wikitext.startswith('}}', j):
                depth -= 1
                j += 2
            else:
                j += 1
        yield wikitext[start:j - 2]



def clean_text(s):
    """Normalize wikitext residue in headings and terms."""
    s = s.replace('{{=}}', '=')
    s = re.sub(r'<span\b[^>]*>\s*</span>', ' ', s)
    s = re.sub(r'<var\b[^>]*>(.*?)</var>', r'\1', s, flags=re.S)
    s = re.sub(r'<[^>]+>', ' ', s)
    s = s.replace('&nbsp;', ' ').replace("''", '')
    s = re.sub(r'\s+', ' ', s).strip(" ,;'")
    return s

def split_candidates(text):
    """Split a span on top-level commas only.

    Commas inside ''italics'', [[links]] or (qualifiers) belong to a single
    candidate (''I cannot offer medical advice, but I can...'' is one term,
    not two)."""
    parts, buf = [], []
    i, link, paren, ital = 0, 0, 0, False
    while i < len(text):
        if text.startswith("''", i):
            ital = not ital
            buf.append("''")
            i += 2
            continue
        if text.startswith('[[', i):
            link += 1
            buf.append('[[')
            i += 2
            continue
        if text.startswith(']]', i) and link:
            link -= 1
            buf.append(']]')
            i += 2
            continue
        c = text[i]
        if c == '(' and not link:
            paren += 1
        elif c == ')' and paren:
            paren -= 1
        if c == ',' and not ital and not link and not paren:
            parts.append(''.join(buf))
            buf = []
        else:
            buf.append(c)
        i += 1
    parts.append(''.join(buf))
    return parts


def vocab_from(strong_text):
    """Split a strong span into candidate terms, keeping qualifiers."""
    text = strip_templates(strong_text)
    terms = []
    for part in split_candidates(text):
        part = re.sub(r'\[\[(?:[^]|]*\|)?([^]|]*)\]\]', r'\1', part)
        part = clean_text(part)
        if part and len(part) > 1:
            terms.append(part)
    return terms


def heading_of(wikitext):
    m = re.match(r'\s*===\s*(.+?)\s*===\s*$', wikitext.splitlines()[0] if wikitext else '')
    return clean_text(m.group(1)) if m else '(untitled section)'


def extract(sections):
    """sections: [(parent, heading, wikitext)] -> (vocab entries, pattern entries)."""
    vocab, patterns = [], []
    for parent, heading, wikitext in sections:
        if parent:
            patterns.append(f'{parent} / {heading}')
        for span in strong_spans(wikitext):
            for term in vocab_from(span):
                vocab.append((term, heading))
    return vocab, patterns


def render(revid, revts, fetched_ts, vocab, patterns):
    lines = [
        '# Wikipedia "Signs of AI writing" - candidate extraction',
        f'# Source: {PAGE_URL} (oldid {revid}, revision {revts})',
        f'# Fetched: {fetched_ts} by scripts/local/voice/wiki_signs_update.py v{VERSION}',
        '# Status: CANDIDATES ONLY. A candidate tell is not a personal ban',
        '# (refs/anti-pattern-method.md). Bans require zero use in corpus/raw via',
        '# ban_list.py plus his confirmation. This file is not the privacy denylist.',
        '# Update: rerun the script weekly or before publishing prose; it diffs',
        '# against this file and exit 2 flags removed/changed entries for review.',
        '',
        '## Vocabulary candidates (from "Words to watch" boxes)',
    ]
    lines += [f'- {t}  [{src}]' for t, src in vocab]
    lines += ['', '## Pattern index (section headings)']
    lines += [f'- {p}' for p in patterns]
    return '\n'.join(lines) + '\n'


def entries_of(text):
    return [l for l in text.splitlines() if l.startswith('- ')]


def main(argv):
    if '--self-test' in argv:
        data = json.load(open(FIXTURE))
        sections = [(s['parent'], heading_of(s['wikitext']), s['wikitext']) for s in data['sections']]
        vocab, patterns = extract(sections)
        terms = {t for t, _ in vocab}
        assert 'delve' in terms and 'tapestry (as an abstract noun)' in terms, \
            f'vocab extraction broke: {sorted(terms)}'
        assert any(t.startswith('serves as/stands as') for t in terms), \
            f'sec-17 phrase groups missing: {sorted(terms)}'
        assert any(p.endswith('/ Rule of three') for p in patterns), \
            f'pattern index broke: {patterns}'
        assert 'I cannot offer medical advice, but I can...' in terms, \
            f'comma inside italic candidate split: {sorted(t for t in terms if "medical" in t or "but I can" in t)}'
        sc = data['split_case']
        toc = [(p, t) for p, t in sc['toc']]
        got = split_sections(sc['wikitext'], toc)
        assert [(p, t) for p, t, _ in got] == [tuple(x) for x in sc['toc']], \
            f'section alignment broke: {[(p, t) for p, t, _ in got]}'
        v2, _ = extract(got)
        t2 = {t for t, _ in v2}
        assert t2 == {'alpha', 'omega'}, \
            f'excluded meta child leaked or eligible section dropped: {sorted(t2)}'
        print(f'self-test OK: {len(vocab)} vocab candidates, {len(patterns)} pattern entries from fixture')
        return 0

    revid, revts, wikitext, toc = fetch_page()
    vocab, patterns = extract(split_sections(wikitext, toc))
    fetched = dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    new = render(revid, revts, fetched, vocab, patterns)
    old = open(OUT).read() if os.path.exists(OUT) else ''

    if old:
        diff = list(difflib.unified_diff(old.splitlines(), new.splitlines(),
                                         'previous', f'oldid {revid}', lineterm=''))
        removed = set(entries_of(old)) - set(entries_of(new))
        added = set(entries_of(new)) - set(entries_of(old))
    else:
        diff, removed, added = [], set(), set(entries_of(new))

    print('\n'.join(diff) if diff else '(no entry changes)')
    print(f'\nsource revision: {revid} ({revts}); {len(vocab)} vocab candidates, {len(patterns)} pattern entries')
    rc = 2 if removed else (1 if added else 0)
    if removed:
        print('REVIEW REQUIRED - source removed or reworded these entries:')
        for e in sorted(removed):
            print('  ' + e)
    if '--dry-run' in argv:
        print(f'dry-run: would exit {rc}; file not written')
        return rc
    tmp = OUT + '.tmp'
    open(tmp, 'w').write(new)
    os.replace(tmp, OUT)
    print(f'wrote {os.path.relpath(OUT, ROOT)}; exit {rc}')
    return rc


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
