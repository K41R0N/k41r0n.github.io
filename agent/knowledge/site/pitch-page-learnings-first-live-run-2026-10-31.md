---
id: 01M6A786VZPKK0B7F5EQ3NG8H0
type: Learning
title: "Pitch page retrospective: first live prospect run, 2026-10-31"
description: "What failed, what the owner corrected verbatim, and what the accepted result did well in the first live run of the pitch-website skill on a real business."
confidence: confirmed
source: "Owner corrections on WhatsApp 2026-10-31 16:33-19:09 COT; accepted page archived verbatim in the private Drive pitch-archive and anonymized under skills/pitch-website/examples/2026-10-31-cafeteria/"
updated: 2026-10-31
class: S0
tags: [copy, verification, attention]
---

# Pitch page retrospective: first live prospect run (2026-10-31)

## Purpose and status

Dated record of the first end-to-end live run of `skills/pitch-website` on a real business: a specialty coffee shop the owner had walked into that same morning. Research brief, then pitch page, then nine owner corrections, then acceptance and this archival request. The business is anonymized here per the no-prospect-names rule; the verbatim page, photo, and provenance live in the private Drive archive (pitch-archive folder).

This record is about process quality. It is not a positioning statement, not a validated offer, and not evidence of business results.

## The run

- 16:33 - Owner kickoff, with visit photos: "Check out [the café]. I was there today." and "Run the whole pitch, and apply their design language using impeccable and the awwwards plugin." (Business name redacted per the no-prospect-names rule.)
- 16:42 - Research brief and first page delivered for review. Verified facts about the business; goals, decision-makers and internal numbers explicitly not public, so the pitch asked before assuming.
- 16:56 to 18:42 - nine corrections (log below).
- 18:52 - final version delivered: Spanish throughout, interactive five-stage walkthrough, plain words.
- 19:09 - owner accepted the result and asked for this record: "Ok, store this example and document what we learned, we wanna get better at getting these website pitches quicker, in less turns, more accurately, making good use of our whole methodology book, and understanding who we're talking to and why."

## Correction log, verbatim, in order

1. 16:56 - "Where's the page? You didn't use here.now"
   What was wrong: the first version went to a hosted File instead of the established page publisher. Root cause: deployment surface assumed, not confirmed.
2. 17:03 - "Why do you keep adding all those meta commentary notes? I told you, you're undermining the pitch"
   What was wrong: process and status notes on the reader-facing page. A repeat of the rule set the same day on the earlier explainer page. Root cause: the gate existed in the skill but did not block the publish.
3. 17:04 - "Also, you didn't use any of the pitch, that page barely has any information, and it doesn't talk about how I could help them"
   What was wrong: context without an actual offering. Root cause: same enforcement gap.
4. 17:11 - "This is fluffy and vague, what do we have our method library for? Can't we do a better job of pitching? Think through how I'd set up tools, processes and Agentic harnesses to help them tangibly"
   What was wrong: generic consulting copy, nothing concrete from his methods. Root cause: the method library was skimmed, not used.
5. 17:28 - "Again, you're getting too into the weeds, you need to understand the why, don't open with the how. They don't care that it's a Google drive or a harness. You need to actually figure out how to talk about this to a prospective client, and use the five pass framework in Spanish"
   What was wrong: tools visible, why missing, wrong language. Root cause: no reader-language pass; the five passes had not run on a Spanish version.
6. 17:32 - "What's the point of all the superfluous design elements? Didn't you use impeccable?"
   What was wrong: eyebrows, stickers, stripes and boxed cards, against both Impeccable and his own copy rules. Root cause: design gate skipped.
7. 18:03 - "Don't you wanna include interactive elements, graphics, or any way to actually show what the approach would be and how it would benefit the business?"
   What was wrong: the page described the approach instead of showing it. Root cause: show-don't-tell was in the skill as guidance, not as a gate.
8. 18:34 - "Use compound engineering, find what's missing, I feel like you're just skimming the surface, and you haven't even mentioned the perks of my systems, approaches, the attention framework, or anything that's tangibly mine"
   What was wrong: the pitch could have come from any consultant; nothing distinctively his. Root cause: no ownership pass and no gap pass before publishing.
9. 18:42 - "There's English terms, and overly technical ones. Use the five pass again"
   What was wrong: English method labels and technical vocabulary inside the Spanish page. Root cause: the five passes were not re-run after the rebuild; terminology was not localized.

## Root causes, grouped

1. The gates existed but did not block. Six of the nine corrections repeated rules already written into the skill after that morning's explainer page. Prose rules do not stop a bad publish; an ordered checklist the runner must execute and report evidence for does. Fix: the nine-gate pre-publish checklist in `skills/pitch-website/SKILL.md` v0.2.0.
2. Deployment surface was not part of orientation. Fix: gate 0.
3. No reader-language pass. Fix: gate 1, and the five passes run on the final language version.
4. No ownership pass: what is tangibly his was absent. Fix: gate 5.
5. No compound gap pass: "find what's missing" had to be requested. Fix: gate 8, findings recorded before first publish.
6. Show-don't-tell treated as optional decoration guidance. Fix: gate 6.

## What the accepted result did well

- Opens with the reader's why: what a class could become for the business. Tools stay invisible.
- Teaches the real method, not a description of it: the five depth stages walked on one clearly illustrative post-class example, all seven parts of the work visible at each stage, the rule that the weakest part caps the depth, and the two-manual-runs requirement before any scripted repetition.
- Makes the perks tangible: written reusable methods, an evidence trail, judgment staying with people, learning from corrections.
- Honest claims: the example is labeled as supposition, no invented ROI, no implied problems on the business's side, sources linked to their real pages.
- Design: calm editorial layout in the business's own palette, no eyebrows or decoration, one clear call to action.
- Plain Spanish throughout, including the method's stages and parts rendered as ordinary questions.

## Standing changes from this run

- `skills/pitch-website/SKILL.md` is now v0.2.0: the pre-publish check is a nine-gate blocking list with evidence reporting; ownership, reader-language, show-don't-tell, and the compound gap pass are new gates; deployment surface is confirmed at orientation.
- `routines/learnings.md`: new rules logged for deployment surface, reader language, ownership, gap pass, and show-don't-tell.
- The example is preserved twice: verbatim in the private Drive archive, anonymized under `skills/pitch-website/examples/2026-10-31-cafeteria/`.

## Evidence and limits

- Sources: the owner's WhatsApp messages of 2026-10-31 16:33-19:09 COT, quoted verbatim above; the accepted page; the earlier same-day record `knowledge/site/pitch-page-learnings-2026-10-31.md`.
- The page is an illustrative example of the approach, reviewed by the owner. It is not a deployed system, not a client result, and not evidence of business performance. The business has not been pitched beyond the owner's review.
- The research brief behind the page used labeled evidence and stayed out of the public page by design; the owner's visit photos were never used on the page.
