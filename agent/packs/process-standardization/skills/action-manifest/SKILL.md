---
name: action-manifest
description: Builds the canonical action manifest, source map, and action-family grouping from synthesis artifacts. Triggers when the user asks to "build the action manifest", "create action manifest", "generate source map", "group actions into families", or "build action taxonomy". Produces the single index that every downstream SOP is drafted against.
version: 0.1.0
---

# Action Manifest

## Purpose

Produce the canonical index of standardizable team actions. The manifest is the bridge between synthesis (what the team currently does) and SOP drafting (what the team will do). It names every action once, groups actions into families, classifies each action's standardization boundary, and proves each action is grounded in real interview evidence.

Three artifacts come out of this skill, in order:

1. An **action manifest** — one row per canonical action.
2. A **source map** — the verbatim evidence that grounds each row.
3. An **action families** grouping — manifest rows organized by the user-supplied family list.

Downstream skills (in particular `sop-drafter`) read these three artifacts and treat them as the source of truth.

## When to trigger

Trigger this skill only when:

- Synthesis artifacts already exist for the engagement (cross-interview SWOT, action comparison matrix, standardization boundary map).
- A set of role/team interview extractions is available for back-reference.
- The user has supplied a role-family list at bootstrap.
- No action manifest, source map, or action-families file has been produced yet for this engagement.

This is **build mode only**. If a manifest already exists, do not enter this skill — there is no patch flow here. See "Out of scope" below.

## Required inputs

Read all of these before writing anything. This restates controller rule 1.

- **Synthesis SWOT** — strengths, weaknesses, opportunities, threats across the team. Used to set priority and to identify which practices are worth standardizing vs. preserving.
- **Action comparison matrix** — the cross-interview comparison of how each role performs each recurring action. Used to detect the canonical action set and to compare implementations.
- **Standardization boundary map** — the synthesis call on which areas should be standardized strictly, templatized, or preserved as variants. Used to assign the boundary classification on each manifest row.
- **The N role/interview extractions** — the original per-person extractions. Used as the verbatim source for the source map and as the back-reference layer for any claim made in the manifest.
- **User-supplied role-family list** — the list of action families the user wants used as the top-level taxonomy for this engagement. Do not invent or hardcode this list. If the user has not supplied it, stop and ask.

If any of these inputs are missing or ambiguous, stop and ask the user. Do not proceed with a partial picture.

## Output 1: Action manifest

Produce one file: an action manifest with one row per canonical action. Each row must include:

- **id** — stable slug-style identifier (lowercase, hyphenated, short). Examples of the *form*: `daily-research`, `visual-request-lifecycle`, `weekly-kpi-reporting`. Once issued, an id is permanent. Downstream SOPs will reference it.
- **name** — short human-readable action name.
- **owning role-family** — the family this action belongs to, drawn from the user-supplied family list.
- **boundary classification** — one of `STANDARDIZE`, `TEMPLATIZE`, `PRESERVE-VARIANT`, taken directly from the standardization boundary map.
  - `STANDARDIZE` — the team performs this the same way across roles and clients.
  - `TEMPLATIZE` — there is a shared template, structure, or output format, but content/parameters vary by role or client.
  - `PRESERVE-VARIANT` — useful role-specific differences exist and should not be flattened.
- **one-line description** — what the action is, in plain language.
- **source extractions cited** — the list of extraction files that contain evidence for this action.

Deduplicate aggressively. If two interviews describe the same underlying action under different names, collapse them into one row and record both source extractions.

Where evidence is thin (only one extraction mentions the action) or where the synthesis flagged the action as ambiguous, mark it explicitly. Do not invent supporting material. This restates controller rule 4.

When two roles do the same action differently and the difference is a useful role-specific divergence, do **not** flatten them into a single `STANDARDIZE` row. Either keep them as a `PRESERVE-VARIANT` row with both variants noted, or, if the difference is large enough, split into two manifest rows with distinct ids. This restates controller rule 6.

When choosing what to standardize, prefer the most scalable, teachable, repeatable practice — not the highest-performing single individual's idiosyncratic workflow. This restates controller rule 3.

## Output 2: Source map

For each manifest row, produce a corresponding source-map entry. The source map exists to enforce evidence traceability (controller rule 2). For every claim a future SOP makes, the source map must let any reader trace that claim back to a specific interview passage.

Each source-map entry must contain:

- **manifest id** — the stable id of the action.
- **per-extraction quotes** — for each extraction cited on the manifest row, include the verbatim or near-verbatim quote(s) from that extraction that ground the action. If the original extraction is long, quote only the load-bearing sentence(s).
- **section/anchor reference** — which section, process card, or heading in the extraction the quote came from, so a reader can find the surrounding context.
- **inference markers** — when the manifest row makes a claim that is not directly stated in any extraction but is a reasonable inference from synthesis or recommendation, label it as such. Use a clear marker like `[INFERENCE]` or `[RECOMMENDATION]`. This restates controller rule 5: distinguish source-grounded fact from reasonable inference from recommendation.

If a manifest row has no quotable evidence in any extraction (it exists only as a synthesis recommendation), say so explicitly in the source-map entry. Mark the row in the manifest as a recommendation rather than as observed practice. Do not retrofit an extraction quote that does not actually support the row.

## Output 3: Action families

Produce a third artifact that groups manifest rows into families using the user-supplied role-family list. This is the navigation layer SOP-drafter uses to decide which SOPs to write and in what scope.

For each family, include:

- **family name** — exactly as the user supplied it.
- **action rows** — the list of manifest ids in this family, with name, priority hint, and boundary classification carried through.
- **family summary** — a short paragraph describing what the family covers and any cross-cutting prerequisites.
- **unfit actions** — if a manifest row does not fit cleanly into any family the user supplied, do not force it. Note it under an "Actions that do not fit cleanly" section with a one-line note on why. Surface this back to the user as ambiguity rather than silently classifying it.

Do not hardcode any specific taxonomy. One example is a six-family taxonomy that includes research, content production, visual production, reporting, community, and campaign templates. is **one example**. Domain-specific examples in source archives are illustrative only. Accept whatever family list the user supplies.

## Naming rules

- Ids are slug-style: lowercase, hyphenated, short, descriptive.
- Ids are stable. Once issued, an id never gets renamed. Downstream SOPs reference these ids; renaming breaks traceability.
- If an action's *display name* needs to change later, change the name field, not the id.
- If two actions get accidentally collapsed into one id and need to be split later, that is a re-run of the manifest, not an in-place rename. See "Out of scope".
- Family names follow the user's spelling and casing exactly.

## Controller rules (restated inline)

These six rules govern this skill. The canonical version lives at `${CLAUDE_PLUGIN_ROOT}/CONTROLLER.md` — defer to that file if there is any conflict.

1. **Read files before acting.** Read every input listed above before producing any output.
2. **Preserve evidence traceability to source interviews.** Every manifest claim must be traceable through the source map back to specific extraction passages.
3. **Prefer best scalable practice, not best individual practice.** Standardize on what is teachable and repeatable across roles, not on a single person's expert workflow.
4. **Mark ambiguity explicitly; do not invent source material.** If a row is thin or contested, say so. Never fabricate quotes or process detail to fill a gap.
5. **Distinguish source-grounded fact from reasonable inference from recommendation.** Use explicit markers in the source map. A future reader must be able to see at a glance which claims are observed vs. inferred vs. recommended.
6. **Do not flatten useful role-specific differences.** If a difference between roles is meaningful, keep it as a `PRESERVE-VARIANT` row or split into separate rows. Do not collapse for the sake of a tidy taxonomy.

## Out of scope

This skill is **build only**. It produces the manifest, the source map, and the families grouping once per engagement.

Explicitly **not** part of this skill:

- No patch mode. Do not include flows for editing the manifest after it has been produced.
- No re-run flow for new interviews arriving after the manifest is built.
- No re-run flow for mid-project staffing changes (someone joins, someone leaves, someone's role shifts).
- No re-run flow for re-extractions of existing interviews.
- No mid-flight reclassification of `STANDARDIZE` vs `TEMPLATIZE` vs `PRESERVE-VARIANT` after the manifest has been handed off.

If new evidence arrives after the manifest is built, the user should re-run the entire pipeline from synthesis forward, not patch the manifest in place. Patch flows that may exist elsewhere in the broader project are explicitly excluded from this skill.

## Hand-off

When all three outputs are written and the user has confirmed the family grouping is correct, hand off to `sop-drafter`. Pass:

- the action manifest file,
- the source map file,
- the action families file.

`sop-drafter` will draft one SOP per family (or per logical SOP scope inside a family) using these three artifacts as its only authoritative reference for what to standardize and which evidence supports each decision.
