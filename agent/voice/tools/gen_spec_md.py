import json,sys
s=json.load(open('tools/spec_v0.json')); M=s['metrics']; F=s['function_words']
def r(k,d=2):
    v=M[k]; return f"{v['wmean']:.{d}f} | {v['mean']:.{d}f} | {v['min']:.{d}f} to {v['max']:.{d}f} | {v['wsd']:.{d}f}"
o=[]
o.append('''---
type: VoiceSpec
title: "Voice spec v0, Alejandro Arango, register: essay"
confidence: proposed
tier: 2
approver: Alejandro Arango
status: PROPOSED. Measured, not yet confirmed by the approver. Nothing here is a rule until he confirms it.
built_from: corpus/raw/ only (9 essays, all confirmed by him as fully his prose on 2026-10-28). Recency weighting applied at his request. Holdout (2 essays) excluded and verified absent (reports/verification.md V3).
generated_by: tools/build_spec.py -> tools/spec_v0.json -> tools/gen_spec_md.py
---
# Voice spec v0 (essay register)

**What this is.** Measured habits from nine of his own Substack essays, about %d words and %d sentences. Each row shows the recency-weighted mean (the headline number, see Weighting), the plain mean, the lowest and highest piece, and the weighted spread between pieces. The range is the point: a draft is "in voice" for a metric when it lands inside his own min-to-max, not when it hits the mean.

**What this is not.** Not a style guide and not proof of voice. It covers the measurable half only (see HARNESS.md section 1). Corpus is small: with n=9 the ranges are wide and will move when more of his writing is added. Registers other than essay (thesis pages, short posts, about copy) have no measured spec yet because no verified self-written samples exist.

## Weighting (his instruction: more recent essays carry higher priority)
Method: exponential recency weight with a 12-month half-life, relative to the newest raw essay. A piece 12 months older than the newest counts half as much. Weights by piece are in `tools/spec_v0.json` under `weighting`. The 12-month half-life is my choice, not his. It is mild on purpose: the corpus is small and one essay (2026-09-20) sits about a year after the rest. He can set a different half-life (one constant in `tools/build_spec.py`). Min and max ranges stay unweighted across all nine pieces, because a range is about what he has done, not what he does most recently.

## Sentence rhythm
| metric | recency-weighted mean | unweighted mean | range across pieces | weighted between-piece sd |
|---|---|---|---|---|''' % (s['pooled_words'],s['pooled_sentence_count']))
for k,l in [('sent_mean','mean sentence length (words)'),('sent_median','median sentence length'),('sent_sd','sentence length sd (burstiness)'),('sent_lt8_share','share under 8 words'),('sent_gt25_share','share over 25 words'),('sent_gt32_share','share over 32 words')]:
    d=3 if 'share' in k else 2; o.append(f'| {l} | {r(k,d)} |')
p=s['pooled_sentence_length']; o.append(f"\nPooled sentence lengths: median {p['median']:.0f}, 10th percentile {p['p10']}, 90th percentile {p['p90']}, longest {p['max']}.\n")
o.append('## Paragraph shape\n| metric | mean | range | sd |\n|---|---|---|---|')
for k,l in [('para_sent_mean','sentences per paragraph'),('para_1sent_share','share of one-sentence paragraphs'),('para_5plus_share','share of 5+ sentence paragraphs')]: o.append(f'| {l} | {r(k,3 if "share" in k else 2)} |')
o.append('\n## Punctuation and typography (per 1000 words)\n| metric | mean | range | sd |\n|---|---|---|---|')
for k in M:
    if k.startswith('punct.'): o.append(f"| {k[6:].replace('_',' ')} | {r(k)} |")
o.append('\nNote: curly and straight apostrophes and quotes both appear, which is a Substack/CMS artifact and not a decision. Do not treat either as voice. Dashes: em dash %.2f per 1000 words, essentially absent; spaced hyphen as dash %.2f.\n' % (M['punct.em_dash']['mean'],M['punct.spaced_hyphen_dash']['mean']))
o.append('## Person, discourse markers, lexical variety\n| metric | mean | range | sd |\n|---|---|---|---|')
for k in M:
    if k.startswith('lex.'): o.append(f"| {k[4:].replace('_',' ')} | {r(k)} |")
o.append('\n## Function-word profile (per 1000 words)\nHighest-frequency function words with his mean and range. These are the habits stylometry relies on. Full table in tools/spec_v0.json.\n\n| word | mean | range |\n|---|---|---|')
for w,v in sorted(F.items(),key=lambda x:-x[1]['mean'])[:40]: o.append(f"| {w} | {v['mean']:.1f} | {v['min']:.1f} to {v['max']:.1f} |")
o.append('\n## Things that stand out against the client rule set (read before adopting any rule)\n- Sentences over 32 words are about %.0f%% of his sentences (range %.0f%% to %.0f%% by piece). A 32-word hard cap would fail every piece he has published.\n- "We/our/us" runs %.0f per 1000 words and "I" %.0f. Both are habits to preserve in drafts; why he uses them is for him to say.\n- One-sentence paragraphs are %.0f%% of his paragraphs; paragraphs of 5+ sentences are almost absent. His paragraph range is 1 to 4 sentences, not 1 to 8.\n- He uses "really", "actually", "just", "very" at a combined rate of about 6.7 per 1000 words (the client banned-filler list). That list does not describe him.\n- Semicolons %.1f and colons %.1f per 1000 words: both used, moderately.\n' % (100*M['sent_gt32_share']['mean'],100*M['sent_gt32_share']['min'],100*M['sent_gt32_share']['max'],M['lex.we_per_1000']['mean'],M['lex.first_person_I_per_1000']['mean'],100*M['para_1sent_share']['mean'],M['punct.semicolon']['mean'],M['punct.colon']['mean']))
print('\n'.join(o))
