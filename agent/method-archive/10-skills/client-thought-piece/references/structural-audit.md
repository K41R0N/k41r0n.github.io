# Structural Audit: Measure, Don't Eyeball

Added 2026-08-25 after the John op-ed failure. What happened: V1 got a full structural review, then V2 fixed the argument, facts, compliance, and voice, and never re-ran the subtraction. The rewrite came out 300 words LONGER, with 22 of 35 paragraphs ending on a shaped line, 10 meta signposts, 4 manufactured punch-paragraphs, a closed ring, and 2 corpus collisions. the author caught it in one read: "This didn't follow the anti LLM pass in our methodology."

Two rules fall out of that, and they are the point of this file.

**Rule 1: the subtraction pass is always the LAST pass.** Any substantive rewrite (argument, facts, compliance, voice) re-opens it. Fix rounds regrow tells, because rewriting under pressure produces signposts, punch-paragraphs, and re-landed favorite lines. A fix round that grows the word count is presumptively regrowing tells.

**Rule 2: measure before and after.** Counting beats judgment. Run the script below on the draft before the subtraction pass and again after, and report both sets of numbers in the delivery note. Never claim the pass ran without the numbers.

## The measurement script

Adapt paths and the ring/collision tokens per piece; the counters are the stable part.

```python
import re
t = open(PATH).read()
body = t.split('---\n')[1]          # body between rules; adjust per file
paras = [p.strip() for p in body.split('\n\n')
         if p.strip() and not p.startswith(('#','>','*'))]
sents = [s for p in paras for s in re.split(r'(?<=[.?!])\s+', p)]

# 1. Shaped vs flat endings: final-sentence word counts per paragraph.
finals = [len(re.split(r'(?<=[.?!"])\s+', p)[-1].split()) for p in paras]
# <=8 words = likely punch; 9-15 = likely shaped; judge >15 by hand.

# 2. One-sentence punch paragraphs.
punch = sum(1 for p in paras if len(re.split(r'(?<=[.?!])\s+', p)) == 1)

# 3. Negation-correction patterns (then read each hit; only true
#    corrections count against budget).
neg = len(re.findall(
  r"(?<=[.\n])\s*(?:It|That|They|This) (?:did|is|was|are|were|do|does) not\."
  r"|\bnot [^.]{0,50}\b(?:but|It is|It was)\b", body, re.I))

# 4. Meta signposts: the essay narrating its own argument.
meta = len(re.findall(
  r"Here is the (?:argument|version|part)|Which is why I|What I would point out"
  r"|So let me|put the hard part|step back and|worth pausing|That is the claim",
  body, re.I))

# 5. Ring check: do the opening paragraph's key tokens recur in the final one?
# 6. Corpus collisions: grep the draft against references/corpus-registry.md.
# 7. Word count vs previous version. Growth in a fix round = warning.

print(len(paras), 'paras;', sum(len(s.split()) for s in sents), 'words')
print('finals:', sorted(finals), '| punch paras:', punch,
      '| neg hits:', neg, '| meta:', meta)
```

## Thresholds (from the pieces that cleared)

| Measure | Essay / op-ed | Manifesto |
|---|---|---|
| Paragraphs ending flat (long, factual, unshaped) | at least a third | at least a quarter (declaration density is genre-native, but 6 shaped in 10 new paragraphs was the ceiling a verifier passed) |
| One-sentence punch paragraphs | ≤1, and it must be the answer to the hardest objection, never a restated subhead | ≤1 outside a deliberate refusals set |
| True negation-corrections in new material | ≤1 | ≤1 (seed instances stay; seeds win) |
| Meta signposts | 0 | 0 |
| Ring composition | at most a third of a set; break the ring when a review flags it and end forward | seed's call |
| Corpus collisions | 0, always | 0, always |
| Word count through a fix round | flat or down; every cut comes from scaffolding, never the argument | same |

## What the pass cuts, in practice (John op-ed V3, 11 edits)

Signpost paragraphs announcing the argument's shape; punch paragraphs duplicating their own subhead; "So let me put the hard part on the table myself" throat-clearing before a concession (just concede); flattening manufactured snaps into the preceding sentence; recasting any line whose shape already landed in another byline; breaking the ring and ending forward. The verified deltas: shaped endings 22/35 → 14/31 flat-ending equivalent, meta 10 → 0, punch 4 → 1, negation pattern hits 40 → 2, ring broken, collisions 0, words 2,492 → 2,297.
