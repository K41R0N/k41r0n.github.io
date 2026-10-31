---
name: sop-drafter
description: Drafts per-action Standard Operating Procedures in two modes — internal (v1, drawn purely from the team's own practice) and overlay (v2, v1 enriched against an external reference framework supplied by the user). Triggers when the user asks to "draft SOPs from manifest", "generate v1 SOPs", "create v2 overlay SOPs", "draft an SOP", "produce SOPs for each action", or "overlay external framework on SOPs".
version: 0.1.0
---

# sop-drafter

## Purpose

Produce one Standard Operating Procedure per action in the action manifest, then optionally enrich each SOP by overlaying an external reference framework supplied by the user. The skill operates in two clearly separated modes so that team-grounded practice never gets silently mixed with outside guidance: every step is labeled, every claim is traceable, and the output is consistent enough to feed the downstream playbook assembler.

Reference the canonical controller at `${CLAUDE_PLUGIN_ROOT}/CONTROLLER.md` for shared rules. The six controller rules are restated inline at the bottom of this skill — apply them on every run.

## The Two Modes

This skill has exactly two modes. Decide which mode to run before reading any source material. If the user request is ambiguous, ask.

### Mode 1 — `internal` (v1)

Produce one SOP per action, drawn ONLY from the team's existing practice as captured in extractions and the source map. No external reference framework is consulted in this mode.

Operating constraints for `internal` mode:

- Build every step from current team practice. Do not introduce material from any outside playbook, methodology, or framework.
- Choose the best scalable practice across the team — not the most sophisticated individual practice, and not the lowest-common-denominator practice. A step belongs in v1 only if it is effective, teachable, repeatable, and low-friction enough for team-wide adoption.
- Preserve useful flexibility. If different variants are appropriate for different platforms, clients, or roles, mark them as variants rather than collapsing them into one rigid path.
- Mark anything that is not directly evidenced in source material as `INFERENCE` and explain the basis. Do not invent steps to fill gaps — gaps go in `Known Limitations`.
- Every standardized step must cite at least one source extraction in the per-action evidence block.

### Mode 2 — `overlay` (v2)

Take an existing v1 SOP set and a user-supplied EXTERNAL REFERENCE FRAMEWORK. Produce a v2 SOP per action that layers framework guidance on top of v1, clearly distinguishing what came from team practice (FACT) from what came from the framework (RECOMMENDATION).

The external reference framework can be ANY external body of practice the user provides:

- A methodology book or published framework
- An industry standard or compliance regime
- Another company's playbook or operating manual
- A consultant's deliverable, internal handbook, or research report

The skill must not assume any specific framework. A third-party content playbook is one example — not a baked-in dependency. Treat whichever framework the user supplies as the reference, and do not bring in material from frameworks the user did not name.

Operating constraints for `overlay` mode:

- The framework is an optimization layer, not a rewrite mandate. Keep what already works in v1.
- Only change v1 where the framework clearly improves quality, consistency, speed, governance, experimentation, or risk control.
- Every change must cite a specific section or page of the framework as its rationale.
- Classify every change as one of: validated existing practice, upgraded practice, missing element added, or anti-pattern corrected.
- Do not flatten useful role-specific differences when adopting framework language. If the framework prescribes one path and v1 carries two valid variants, keep the variants and reconcile in the rationale.
- Preserve the v1 evidence block. Add a parallel framework citation block for every RECOMMENDATION.

## When To Trigger Each Mode

Run `internal` (v1) mode when:

- The action manifest has just been finalized and no SOPs exist yet.
- The user asks for "v1 SOPs", "team-only SOPs", "internal-only SOPs", or "draft SOPs from manifest".
- A new action has been added to the manifest and needs its first standardized version.

Run `overlay` (v2) mode when:

- A complete v1 SOP set exists for the relevant actions or families.
- The user has supplied (or can point to) an external reference framework.
- The user asks for "v2", "overlay SOPs", "playbook overlay", "optimized SOPs", or "overlay external framework on SOPs".

If the user requests v2 but no v1 exists, stop and run `internal` mode first. Do not skip v1.

## Required Inputs

### `internal` (v1) mode

- Action manifest (canonical list of actions to standardize, with stable action ids).
- Source map (which interview / extraction / artifact each action originated from).
- Per-interviewee extractions (process cards, quotes, strengths, opportunities).
- Optional: cross-interview synthesis, role-family taxonomy.

If any of these inputs is missing, stop and ask. Do not draft v1 without a source map — there will be no way to satisfy traceability.

### `overlay` (v2) mode

- The complete v1 SOP set produced by `internal` mode.
- The external reference framework: either a path the user provides, the contents the user pastes in, or an explicit pointer to files already in the repo.
- Optional: a framework-to-action mapping that tells the skill which framework sections are most relevant to which actions. If the user does not provide one, propose one and confirm before drafting.

If the user names a framework but does not provide its contents or a path, stop and ask.

## Output Structure

Write outputs to the directory the user specifies. If unspecified, default to `/02_outputs/sop_v1/` for `internal` and `/02_outputs/sop_v2/` for `overlay`.

File granularity: one file per action family, with one SOP section per action inside that file. If the manifest is flat (no families), produce one file per action.

Use the same SOP template for both modes. The template generalizes from the research-monitoring sample and works for any action family or external framework.

### SOP template

For each action, produce these sections in this order:

1. **Action id** — the stable id from the manifest.
2. **Action name** — the human-readable name.
3. **Owner role-family** — the role-family that owns this action (do not collapse multiple owners into one if the manifest preserves them).
4. **Trigger** — the event, cadence, or condition that starts this action.
5. **Inputs** — required and optional inputs, tools, systems, and reference docs.
6. **Step-by-step procedure** — numbered steps. For each step capture:
   - Step number and short name.
   - What must be done.
   - Why this step is included.
   - Source person(s) or framework section.
   - Step classification: Required / Recommended / Situational.
   - Step label: `FACT`, `INFERENCE`, or `RECOMMENDATION` (see Per-Step Labeling below).
7. **Outputs** — concrete deliverables produced by the action.
8. **Handoffs** — who receives the outputs, and in what form.
9. **Decision rules** — explicit rules and judgment criteria, including variant selection when role/platform/client context changes the right choice.
10. **Definition of done** — pre-completion checklist that, if satisfied, means the action is finished.
11. **Preserved team strengths** (mode `internal`) / **Elements preserved from team practice** (mode `overlay`) — strongest existing practices intentionally kept.
12. **Flexible areas** — where flexibility is retained and why.
13. **Known limitations** — open issues, ambiguities, weak evidence, items needing human review.
14. **Evidence citations** — see Per-Action Evidence List below.

In `overlay` mode, add these sections after the procedure:

- **Change log (v1 to v2)** — for each change: change type (Validate / Add / Modify / Remove), section affected, what changed, why, framework reference.
- **New controls, templates, or frameworks added** — items injected from the framework, with purpose and placement.
- **Anti-patterns or risk areas corrected** — what was corrected and why.
- **Adoption notes** — what is easy to adopt versus what requires coaching or change management.

At the end of each `internal` file include a `Gaps Requiring External Review` block listing where overlay is most likely to add value.

At the end of each `overlay` file include a `Cross-SOP Implementation Priorities` block ranking SOPs by ease of adoption, expected operational impact, and change-management need.

## Per-Step Labeling

Every step in every SOP carries exactly one label. This is a hard rule (controller rule 5).

- `FACT` — directly evidenced by team practice in source extractions or by the v1 SOP itself. Cite the source person, extraction file, or v1 section.
- `INFERENCE` — a reasonable extension of evidenced practice that is not directly stated. Cite the basis and explain the gap. Use sparingly; prefer to mark gaps as `Known limitations` instead of inventing inferred steps.
- `RECOMMENDATION` — sourced from the external reference framework (overlay mode only). Cite the specific framework section or page.

Never combine labels on a single step. If a step blends team practice with a framework upgrade, split it into two steps so each carries one label, or annotate the upgrade in `Change log` and keep the step as `FACT` with a clearly separated `RECOMMENDATION` follow-on.

## Per-Action Evidence List

Each SOP closes with an `Evidence citations` block that links every claim back to source extractions (and, in overlay mode, framework sections). Use a simple two-column table:

| Element | Source |
|---------|--------|
| [Step name, decision rule, or template] | [Extraction file + section, or framework section/page] |

Every step must appear at least once in this block, indexed by step name. Decision rules and templates that carry significant weight must also appear. If an element has no traceable source, it does not belong in the SOP — move it to `Known limitations`.

## The Six Controller Rules (restated inline)

1. **Read files before acting.** Read the manifest, source map, extractions, and (in overlay mode) the framework before drafting. Do not draft from memory of a prior run.
2. **Preserve evidence traceability to source interviews.** Every standardized step, decision rule, and template must trace back to a source extraction (or, in overlay mode, a framework section). The evidence block is not optional.
3. **Prefer best scalable practice, not best individual practice.** A step belongs in the SOP only if it is effective, teachable, repeatable, and low-friction enough for team-wide adoption. The most sophisticated individual practice may be preserved as an optional advanced layer, not as the default.
4. **Mark ambiguity explicitly; do not invent source material.** If evidence is weak, conflicting, or absent, say so under `Known limitations` and flag it for human review. Never fabricate a quote, extraction, or framework citation.
5. **Distinguish source-grounded fact from reasonable inference from recommendation.** Every step is labeled `FACT`, `INFERENCE`, or `RECOMMENDATION`. The labels are not decorative — downstream skills rely on them.
6. **Do not flatten useful role-specific differences.** If platform, client, or role context legitimately changes the right step, keep variants and document when each applies. Do not collapse them to make the SOP look cleaner.

Canonical authority: `${CLAUDE_PLUGIN_ROOT}/CONTROLLER.md`. If the canonical file disagrees with this restatement, the canonical file wins.

## Hand-off

After producing v2 SOPs, hand off in this order:

1. Invoke `interviewee-review-summary` once per interviewee. Each interviewee should receive a personalized summary of which of their practices are preserved, upgraded, or marked as known limitations across the v2 SOP set.
2. After review summaries are produced, invoke `playbook-assembler` to compile the SOPs and supporting artifacts into the final playbook.

After producing v1 SOPs (and not yet v2), hand off back to the orchestrator. Do not invoke `interviewee-review-summary` until v2 exists — review summaries should reflect the final state of each interviewee's contribution, not an intermediate one.
