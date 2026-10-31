---
name: interviewee-review-summary
description: Generates a focused 2-page review document for a single interviewee that summarizes what they said and shows how each contribution shaped the v2 SOPs, so they can verify and correct before the playbook is finalized. Triggers on "generate review summary for", "interviewee review document", "send back to interviewee", "two-page review", "interviewee verification doc", and "feedback loop with interviewee".
version: 0.1.0
---

# Interviewee Review Summary

## Purpose

Produce one short, scannable document per interviewee that closes the loop between their interview and the standardized SOPs. The document has two jobs: (1) show the interviewee what was captured from their session, and (2) show how each captured item was classified and folded into the team standard. The interviewee returns corrections; minor corrections are folded in before final assembly.

This is a verification artifact, not a deliverable. It is not the playbook, not a coaching document, and not a recap.

## When To Trigger

Run this skill once per interviewee, after:

- The interviewee's extraction exists.
- The action manifest is stable.
- v1 SOPs have been drafted and v2 SOPs (cross-interview reconciled) have been produced.
- Before the final playbook assembler runs.

Do not run this skill earlier in the pipeline. The point is to show the interviewee what their input became, which requires v2 SOPs to exist.

Out of scope: patch flows, mid-project re-extraction, v3/v4 refactors. If corrections are major, the user re-runs the relevant pipeline stages — this skill does not orchestrate that.

## Required Inputs

Before generating the document, confirm access to:

1. The interviewee's extraction file (single source of truth for what they said).
2. The current action manifest (so each action they own or contributed to can be located).
3. The v1 SOPs and v2 SOPs that cite their extraction (so boundary classifications and SOP ids are knowable).
4. The role-family list in use on this project (the 6-family taxonomy used in the social-team example is one example only — adapt to whatever taxonomy this project uses).

If any of these are missing, stop and say which one.

## The Six Controller Rules (Restate Inline)

These rules govern every skill in this plugin. The canonical version lives at `${CLAUDE_PLUGIN_ROOT}/CONTROLLER.md`. Restated here so this skill is self-contained:

1. Read files before acting.
2. Preserve evidence traceability to source interviews.
3. Prefer best scalable practice, not best individual practice.
4. Mark ambiguity explicitly; do not invent source material.
5. Distinguish source-grounded fact from reasonable inference from recommendation.
6. Do not flatten useful role-specific differences.

Rules 2, 4, and 6 are the most load-bearing for this skill. The interviewee will be reading their own words — get the citations right, do not fabricate, and do not paper over places where their version was preserved as a variant.

## Two-Page Structure

Target ~700-1,000 words total across both pages. Plain prose, scannable, no internal jargon (no "manifest", no "boundary classification matrix", no "v2 SOP" — translate to plain language for the reader).

### Page 1 — "Here's what we heard from you"

A concise summary of what the interview captured. Do not exhaustively re-list everything — pick the load-bearing items. For each, cite the section heading or timestamp from their extraction so they can verify.

Include:

- **Role and scope** as captured: 2-3 sentences on what they own and who they work with.
- **Key actions** they perform: short list, each with a one-line description and the extraction citation.
- **Pain points** they raised: bulleted, one line each, with citation.
- **Ambiguities they flagged**: where they themselves said "I'm not sure" or "this varies." Mark these explicitly per rule 4.
- **Direct-quote highlights**: 2-4 short quotes that were especially load-bearing for the SOPs. Quote verbatim; cite the timestamp.

Frame it as "here is what we wrote down," not "here is what you do." The interviewee is the authority on their own work.

### Page 2 — "Here's how it shaped the standard"

For each manifest action they own or materially contributed to, give the reader four pieces of information in a short row or paragraph:

1. **Action name** (in plain language).
2. **Boundary classification**: STANDARDIZE, TEMPLATIZE, or PRESERVE-VARIANT. Explain the classification in one sentence of plain English — for example, "We made your version the standard for the whole team," "We turned your structure into a template each role fills in," or "We kept your version as a [role-family] specific variant because it differs from how others do it."
4. **Resulting SOP id** (or section reference) so they can find it in the playbook.
5. **One-line note** on whether their version became the standard, was templatized, or was preserved as a role-specific variant. Where preserved as a variant (rule 6), say so plainly — name the variant, name the role family, and do not paper over the difference.

Close Page 2 with an explicit prompt:

> **Please correct anything wrong here.** If we mis-summarized what you said, mis-classified your action, or merged two things that should stay separate, tell us. Minor corrections will be folded in before the final playbook. Major corrections will trigger a re-run of the affected stage.

## Tone

Respectful, peer-level. The interviewee is a contributor and a subject-matter expert, not an audience for a deliverable. Avoid:

- Performative gratitude ("amazing insights!", "incredible work!").
- Selling them on the standardization ("this will save the team hours!").
- Exhaustive recap of every line they said.
- Internal pipeline jargon.

Aim for: clear, factual, easy to scan, easy to correct.

## Anti-Flatten Reminder

When a contribution was preserved as a role-specific variant, say so directly. Do not soften the difference with phrases like "we incorporated your approach into the standard" when the truth is "we kept your version as the variant for [role family] because it diverges from how others do it." The interviewee needs to know whether their practice survived as the standard, as a template, or as a named variant — those are three different outcomes and they each matter.

If you find yourself reaching for hedging language to make the document feel smoother, stop. The interviewee can handle "your version was preserved as a variant." That is the honest answer and it is the answer they need to verify.

## Hand-Off

After the document is generated and reviewed by the interviewee:

- Collect all corrections in one place.
- Minor corrections (clarifying a quote, fixing a citation, renaming an action, adjusting a one-line note) are folded directly into the affected SOP/extraction before the playbook assembler runs.
- Major corrections (you missed an action, you mis-classified a STANDARDIZE as a PRESERVE-VARIANT, an entire workflow was wrong) are escalated. This skill does not invoke patch flows. The user re-runs the affected pipeline stage with the corrected input.

Once corrections are folded in (or escalated), this skill is done. The playbook assembler picks up from there.
