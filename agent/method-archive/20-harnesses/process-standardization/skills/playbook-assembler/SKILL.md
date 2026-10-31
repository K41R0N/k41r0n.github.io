---
name: playbook-assembler
description: Assembles the final 12-section rollout playbook from v2 SOPs, the action manifest, action families, and incorporated review feedback. Triggers when the user asks to assemble the final playbook, build the rollout playbook, produce the 12-section playbook, generate the final team playbook, or produce the playbook document for a team that has completed SOP v2 drafting and review reconciliation.
version: 0.1.0
---

# Playbook Assembler

## Purpose

Produce the single canonical rollout playbook that an operations team will work from after process standardization is complete. The playbook is the executable artifact: every team member can be handed this document and told "this is how we work now." It consolidates the manifest of actions, the action-family taxonomy, the v2 SOPs (with review corrections incorporated), and the team's operating context into one structured document with twelve sections.

This skill produces a playbook. It does not produce SOPs (see sop-drafter), patches, or refactors. Revisions after rollout flow through Section 12 of the playbook itself, not through a separate patch skill.

## When to Trigger

Invoke this skill only when all of the following are true:

- The action manifest exists and is stable.
- The action-family grouping exists and is stable.
- A complete set of v2 SOPs has been drafted, one per action family.
- Interviewee review summaries have been returned and corrections have been incorporated into the v2 SOPs (or explicitly logged as deferred).
- The team is preparing for rollout, not still in interview or drafting cycles.

If any of those conditions are missing, stop and route the user to the upstream skill (interview-extraction, cross-interview-synthesis, action-manifest, sop-drafter, or interviewee-review-summary). Do not assemble a playbook on top of unfinished inputs.

## Required Inputs

Before assembling, confirm you have read:

1. The action manifest (canonical list of every team action).
2. The action-families document (the grouping taxonomy).
3. The full set of v2 SOPs, one file per action family.
4. The cross-interview synthesis (for evidence traceability and operating principles).
5. The interviewee review summaries plus a record of which corrections were incorporated and which were deferred.
6. User-supplied team metadata:
   - Team name.
   - Team mission statement (one to three sentences).
   - Role-family list (the actual families this team uses; do not assume six).
   - Any external reference framework the team is mapping against (this is optional and team-specific; one example is a domain-specific overlay such as a Web3 social playbook, but accept any).

If any required input is missing, ask for it before writing. Do not invent team metadata.

## The Twelve Sections

Assemble the playbook with these twelve sections in order. Generalize for any team and any role-family list. The role-family count is a parameter, not a fixed number.

### Section 1. Executive Summary

State why this playbook exists, who it is for, and what changes on rollout day. List the SOPs at a glance (one line each). Call out the highest-leverage immediate changes (typically two to four). Show a standardization-levels table: what is standardized strictly, what is standardized with flexibility, and what is intentionally left role-specific.

Inputs: cross-interview synthesis, action-families, manifest counts, user-supplied team metadata.

### Section 2. Team Mission and Scope

Restate the team's mission in the user-supplied form. Define what the team is responsible for and explicitly what it is not. Name the clients, accounts, products, or internal customers the team serves, in the form the user provided. Keep this section short and load-bearing — downstream sections reference it.

Inputs: user-supplied mission and scope; cross-interview synthesis for any team-described scope language.

### Section 3. Role-Family Map

Render the role-family list the user supplied. For each family, give one to three sentences on what that family owns and the names or seats currently filling it. Do not collapse two families into one to make the document shorter. Do not pad to a target count. If the team has three families, show three; if eleven, show eleven.

Inputs: user-supplied role-family list; cross-interview synthesis for who currently does what.

### Section 4. Operating Cadence

Document the rhythm: daily checkpoints, weekly reviews, monthly retrospectives, quarterly strategy reviews, and any client- or product-driven cadences. Tie each cadence item to which SOP enforces it. Show time-zone handoffs if the team has them.

Inputs: cross-interview synthesis, v2 SOPs (each SOP's trigger and review cadence).

### Section 5. Action Families Overview

One subsection per action family. For each family, state its purpose, its owner role, the actions it covers (from the manifest), and the SOP file it points to. This is the index a team member uses to find the right SOP fast.

Inputs: action-families, manifest, v2 SOP filenames.

### Section 6. Standard SOP Catalog

For each v2 SOP, render a uniform block:

- Purpose
- Owner
- Trigger
- Core workflow summary
- Key decision rules
- Mandatory standards
- Flexible elements
- QC checklist
- Main handoffs
- KPI signals
- Boundary classification visible per item, per the standardization-levels table in Section 1: standardized strictly, standardized with flexibility, or left role-specific. Do not hide which behaviors are mandatory versus discretionary.

Inputs: v2 SOPs (with review corrections already incorporated).

### Section 7. Cross-Family Handoffs and Interfaces

Document every place where one family hands off to another: who triggers the handoff, what artifact is passed, what fields it must contain, and how the receiving family confirms receipt. Include external interfaces (clients, account managers, leadership) at the same fidelity as internal ones.

Inputs: v2 SOPs (handoff sections), cross-interview synthesis (pain points around handoffs).

### Section 8. Tools and Systems

List the tools the team uses, grouped: required, recommended, optional. For each tool, name the SOPs that depend on it and the configuration standard (not the vendor). State the rule that the standard is the configuration, not the product — if the vendor changes, the configuration requirements still apply.

Inputs: v2 SOPs, cross-interview synthesis.

### Section 9. Definition of Done and Quality Bar

State what "done" means for each major action family. Pull QC checklists from each SOP and consolidate the team-wide quality bar: the minimum review tier, the minimum evidence required to publish or ship, and the explicit criteria for rejecting work back to the producer. If the team has a tiered review model (for example, self-review, peer review, management review, client review), document it once here and reference it from each SOP rather than restating.

Inputs: v2 SOPs (QC sections), cross-interview synthesis.

### Section 10. Escalation and Exception Handling

Document how the team handles things the SOPs do not cover: who decides, how fast, what gets logged, and how exceptions feed back into SOP revisions. Include the failure mode of the SOPs themselves — what to do if a step is impossible, blocked, or contested.

Inputs: cross-interview synthesis, v2 SOPs (any explicit exception language).

### Section 11. Onboarding Flow Against the Playbook

A new team member's first thirty days against this playbook: what they read in week one, what they shadow in week two, what they own in week three, and what they are signed off on by day thirty. Map each onboarding step to the SOP and the family it belongs to.

Inputs: action-families, v2 SOPs, role-family map.

### Section 12. Maintenance and Revision Policy

Define how the playbook itself gets updated. Owner of each SOP. Who can approve changes. Review cadence (recommended quarterly). Version-control approach. How interviewee or end-user feedback re-enters the document. Make explicit that revisions flow through this section, not through a separate patch process.

Inputs: governance language from cross-interview synthesis; user-supplied ownership decisions.

## Per-Section Assembly Rules

For every section:

- Only use content traceable to a source: the manifest, the action-families doc, a v2 SOP, the cross-interview synthesis, an interviewee review summary, or user-supplied team metadata. If none of those covers a claim, do not write it.
- Preserve evidence traceability (controller rule 2). At minimum, every SOP block in Section 6 should reference the SOP file it was drawn from. Operating principles in Sections 1–4 should reference the synthesis or the interview source where the principle originated.
- Distinguish FACT, INFERENCE, and RECOMMENDATION at the section level (controller rule 5). FACT is something a source said directly. INFERENCE is something derived by combining sources. RECOMMENDATION is a best-practice judgment the playbook is asking the team to adopt. Sections that mix these (Executive Summary, Operating Principles, Final Recommendations) should label paragraphs or bullets with the type when the type is not obvious from context.
- Mark ambiguity explicitly (controller rule 4). If the synthesis disagrees with itself or with an SOP, name the disagreement in-line and pick the version that aligns with best scalable practice (controller rule 3) — do not paper over it.

## Anti-Flatten Reminder

Do not flatten the role-family map (Section 3) or the SOP catalog (Section 6) to make the document shorter or more uniform. Each family has its own owner, scope, and standards. Each SOP has its own decision rules and QC checklist. If two SOPs look identical, that is a signal to re-check whether they should be merged at the action-families level — not to copy-paste their contents at the playbook level.

Controller rule 6 applies here directly: useful role-specific differences must survive into the playbook.

## Final QA Pass

Before declaring the playbook complete, run these checks:

1. Manifest coverage: every action in the manifest appears somewhere in the playbook (typically inside an SOP block in Section 6 or in the family overview in Section 5). List any manifest action that is not referenced and either add it or explicitly mark it deferred.
2. Contributor acknowledgement: every interviewee whose input shaped the synthesis or SOPs is named in a contributors block (commonly placed at the top of the document with the version and date, or in a dedicated acknowledgements section). Missing names are a process error, not a stylistic choice.
3. Source-content hygiene: verify that no patch-mode artifacts have leaked through. The output is the canonical playbook. Do not include language that refers to internal version refactors (v3, v4) or to interviewee-specific patch flows. Those belong to upstream skills, not to the rollout document.
4. Section completeness: every one of the twelve sections is present, in order, non-empty, and uses content from the required inputs.
5. Boundary visibility: the standardized-strictly versus standardized-with-flexibility versus left-role-specific classification is visible in Section 1 and reflected per item in Section 6.

## Controller Rules (Restated Inline)

The shared controller for this plugin is canonical at `${CLAUDE_PLUGIN_ROOT}/CONTROLLER.md`. The six rules apply to this skill in full:

1. Read files before acting. Read the manifest, action-families, every v2 SOP, the synthesis, and the review summaries before writing the playbook.
2. Preserve evidence traceability to source interviews. Every SOP block and every operating principle traces back to a source artifact.
3. Prefer best scalable practice, not best individual practice. When the synthesis surfaces one star performer's method, codify the scalable version, not the personal one.
4. Mark ambiguity explicitly; do not invent source material. If the inputs do not say it, the playbook does not say it.
5. Distinguish source-grounded fact from reasonable inference from recommendation. Use FACT, INFERENCE, RECOMMENDATION labels in mixed sections.
6. Do not flatten useful role-specific differences. The role-family map and the SOP catalog must keep per-family detail.

If a controller rule and a section-level instruction conflict, the controller rule wins.

## Hand-Off

Deliver the assembled file as the canonical team playbook for rollout. Tell the user:

- This is the document the team operates from on rollout day.
- Future revisions go through Section 12 (Maintenance and Revision Policy), not through a separate patch flow.
- If the team needs new SOPs, route back to sop-drafter and then re-run this assembler. Do not edit the playbook freehand to introduce new SOPs.
- If the team needs to re-interview or re-synthesize, route back upstream. Do not patch the playbook to compensate for missing source material.

The playbook is final. Treat it that way.
