---
type: Finding
title: SME draft v4 rejected by him - structural checks did not catch what his ear catches
date: 2026-10-28
source: "His WhatsApp message on 2026-10-28 at about 5:53 PM, id wamid.HBgLMzQ2NzYyNDU0MDkVAgASGCBBQzY0QjQ5OUFEN0E1QTI1ODc2NEM1RjZGRjYwNzA4MgA=. Quote: \"That's not at all my style, and it also uses a bunch of LLM-isms, it reads like slop\". Draft and checks: drafts/2026-10-28-harness-for-smes/ (local, not in this PR)."
status: Decided by him (rejected). Revision work waits for his marked lines.
---
# SME draft v4 rejected

## What happened
The first live voice test asked for a LinkedIn and X post on why his harness method helps small companies. The engine ran the five-pass routine against canon/voice-spec.md and tools/checks.py. He read draft v4 and rejected it: not his style, full of LLM-isms, reads like slop. Nothing was posted. No rewrite has been done yet.

## Key finding
The engine's checks did not predict his verdict. The draft landed inside his measured ranges and still failed his ear.
- Structural range check: 1 of 25 features outside his widened range (threshold to warn is 3). That one feature, lexical variety, is not meaningful at 282 words.
- Sentence mean 17.8 words (his 20.0). Over 25 words 25% (his 28%). One-sentence paragraphs 50% (his 36%, range 18 to 49%). Sentences starting with "But" 6.2% (his 6%). One spaced hyphen, no em dash.
- tools/checks.py: no FAIL from his own-voice rules. The two sentence-over-32-words FAILs are the client-brand cap, which does not describe him. One WARN on the word "harness", his own term. On the X cut, one FAIL for no sentence over 25 words, which does not apply at 46 words.
- Conclusion: the spec measures the half of voice that can be counted (length, punctuation, function-word habits). It does not capture word choice, phrasing patterns, or the tells he hears. Passing it is not evidence of voice. This matches HARNESS.md section 1, which says the spec covers only the measurable half. Now there is a test case.

## Engine hypotheses about why (NOT confirmed by him)
These are guesses, listed so he can confirm or reject each. They become negative examples only when he points at lines.
- Negative parallelism: "this isn't a pitch for X. It's a pitch for Y."
- A neat closing question that works as a call to action.
- Aphorism-style one-line paragraphs ("None of it ever beat doing the work myself.", "That lesson stuck.").
- "It sounds boring - and it is." as a staged concession before the point.
- Hedge phrases used as style: "my bet is", "I suspect".
- A tidy three-item list ("the message..., the automation..., or the tool...").
- Content with no concrete scene. Every first-person detail was lifted from his old essays, so the post has claims and no live example.
Of these, the 19 rules in tools/checks.py cover none, as far as the engine can tell from reading them (it has W05 wrapper phrases and W04 false-depth openers, which do not match these patterns).

## Next steps (not started)
1. He points at the worst lines. Each marked line is stored as a negative example with his reason, in refs/ (evidence), and the draft is kept for reference below.
2. Spec revision starts from those lines: new checks or lexicon entries only when he confirms the reason.
3. Do not rewrite the draft until he asks.
4. Open question the tool results raise: whether the engine should write for him at all. His 2025-07-29 essay says he has not used an LLM to help with his writing since the 2022 book. He has not answered this.

## Rejected artifact (for reference, not a model to imitate)
### LinkedIn draft v4
I spent fifteen years building automations as a marketer, consultant and founder, and I got good at flows inside flows, hundreds of thousands of users deep, with plenty of efficiency theater for the executives watching.

None of it ever beat doing the work myself.

That's the idea behind my harness, and it's the case I'd make to anyone running a small company: automate what you can explain, and keep the judgment for yourself.

In practice it's a short list of rules. Nothing runs before I've explained it and estimated what it will cost. Anything a client will see passes me first. A repeatable job only gets scripted after I've done it by hand twice, the same way both times, and judgment calls never get scripted at all.

It sounds boring - and it is. But my bet is that most small companies don't lose their money on the big mistakes; they lose it on rework, like the message that went out wrong, the automation nobody on the team understood, or the tool that was fast at exactly the wrong thing. I'd rather pay for a rule that stops a bad message before it leaves than for any fix after.

I suspect revenue works the same way, because people buy from a business that sounds like itself. In 2022 I wrote a whole book with GPT, and it came out hollow because it wasn't my voice. That lesson stuck.

So this isn't a pitch for doing more with less, which I stopped believing in a while ago. It's a pitch for knowing what your machines are doing, and why you let them.

What would you stop automating if you had to explain it first?

### X cut v4
Automate what you can explain, and keep the judgment for yourself.

Nothing runs before it's explained and estimated, client work passes me first, and scripts wait for two identical manual runs.

Sounds boring. But my bet is small companies lose money on rework, not big mistakes.
