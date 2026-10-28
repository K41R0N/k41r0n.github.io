---
type: Finding
title: Voice measurements from his essays
date: 2026-10-28
source: "Measured by tools/build_spec.py over corpus/raw (9 essays, 14,754 words, 736 sentences). Rendered in canon/voice-spec.md. Reports in reports/verification.md."
status: Measured; Tier 2 (proposed) until he confirms
---
# Voice measurements from his essays

- Register: essay. First person plural and singular mixed (we/our 18.7 per 1000 words, I 17.2).
- Sentence length: mean 20.0 words. 28% of sentences run over 25 words, 10% under 8.
- Paragraphs: 36% are one sentence (0.361 weighted, 0.359 unweighted). Across single essays the share ranges from 18% to 49%. Paragraphs of 5+ sentences are almost absent.
- "But": 6.5 per 1000 words. 6% of sentences start with it.
- Dashes: em dash about 0.07 per 1000 words (2 in the raw set). Total dash-like marks are 6 in 16.9k words across all 11 essays: em 2, en 1, spaced hyphen " - " 3. His steer: the spaced hyphen is his dash and the em dash is effectively absent. The sample is small (3 spaced hyphens), so the rule stays a budget, not a ban.
- Client-brand voice rules do NOT fit his own voice. 32-word hard cap: fails 11 of 11 pieces (13% of his sentences exceed it). Banned-filler list: hits 11 of 11 (6.6 per 1000 words). 20-word target: 42% of his sentences exceed it. These are recorded in canon/do-dont.md section B as NOT adopted, pending his decision (see finding 07).
- Stability over time: the essays run 2025-06-04 to 2026-09-20 (about 15 months). Evidence: applying recency weighting moves each metric by at most about 1 point, and all 9 leave-one-out range checks stay inside the ranges (0 of 9 reach the 3-feature WARN). No formal drift or trend test was run, so "stable" means no difference found, not a proven absence of change.
- Caveat: Burrows Delta is a soft signal only (3 of 9 of his pieces overlap the control range).
