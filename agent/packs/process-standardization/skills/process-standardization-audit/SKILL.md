---
name: process-standardization-audit
description: Inspects a process-standardization project folder, infers which pipeline stage it is currently at from folder structure alone, and recommends the next skill to invoke. Triggers on phrases like "audit this process project", "what stage is this project at", "diagnose process standardization folder", "next step for standardization project", "review project state", or "where am I in the methodology".
version: 0.1.0
---

# process-standardization-audit

## Purpose

Inspect a process-standardization project folder, identify which canonical pipeline stage it is currently at, and recommend the next skill to invoke. The audit is read-only: it never modifies the project folder, never reads SOP or playbook content to make stage calls, and never invokes downstream skills on its own. It returns a structured diagnosis the user can act on.

## When to trigger

Invoke this skill when:

- The user has an existing project folder created by `process-standardization-bootstrap` (or one that follows the same layout) and is unsure which stage of the methodology they are on.
- The user wants a sanity check before running the next skill in the pipeline.
- The user asks a question like "what stage is this at", "where am I in the methodology", "diagnose this folder", "review project state", or "what should I run next".
- A different skill needs to confirm the project is in the expected state before proceeding.

Do not trigger this skill to fix anything. It only diagnoses.

## Inputs

- **`project_path`** (required): absolute path to the project folder root. The folder is expected to follow the bootstrap layout, with subfolders such as `00_inputs/`, `01_working/`, `02_outputs/`, `03_playbook/`, and `04_prompts/`. If the layout is not recognizable, return `unknown` with an explanation.

The audit accepts any role-family taxonomy and any external reference framework that may live under `03_playbook/`. It does not assume a fixed list of role families or a specific framework name.

## Canonical pipeline stages

The audit recognizes exactly nine stages, in order. Use the first stage whose entry condition is satisfied; advance further only if the next stage's entry condition is also satisfied.

1. **bootstrapped** — folders exist, no transcripts dropped yet.
   - Recommend: drop transcripts into the inputs folder, then run `interview-extraction`.

2. **extracting** — at least one transcript is present, but the number of extractions is fewer than the number of transcripts.
   - Recommend: run `interview-extraction` for each transcript that does not yet have an extraction.

3. **extracted** — every transcript has a matching extraction, and no synthesis artifact is present.
   - Recommend: run `cross-interview-synthesis`.

4. **synthesized** — synthesis artifact is present, but no action manifest is present.
   - Recommend: run `action-manifest`.

5. **manifested** — action manifest, source map, and action families are all present, and no v1 SOPs exist yet.
   - Recommend: run `sop-drafter` in `internal` mode.

6. **v1-drafted** — v1 SOP files are present, and no v2 SOP files exist yet.
   - Recommend: run `sop-drafter` in `overlay` mode. Ask the user to specify the external reference framework to overlay.

7. **v2-drafted** — v2 SOP files are present, and review summaries have not all been returned/reconciled yet.
   - Recommend: run `interviewee-review-summary` once per interviewee on the authoritative roster, then collect responses and dispositions.

8. **reviewed** — a user/owner-provided review-completion record confirms that every required interviewee summary has been returned and all corrections are marked incorporated or deferred, and no final playbook is present.
   - Recommend: run `playbook-assembler`.
   - Filesystem presence/counts/timestamps alone cannot establish that a person returned a review or that corrections were reconciled. If the explicit review-completion record is absent, report the stage as `v2-drafted` with review completion unverified; do not infer `reviewed` from file presence.

9. **shipped** — final playbook is present.
   - No next pipeline step. Point the user to the maintenance section of the assembled playbook for ongoing upkeep.

If no stage condition is satisfied (for example the folder is empty, mis-shaped, or contains only unrelated files), return `unknown` and explain what was missing.

## Detection rules

Make stage calls from folder structure, file presence, file counts, timestamps, and an explicit user/owner-provided review-completion record for stage 8. Do not open or parse the contents of SOPs, the playbook, transcripts, extractions, synthesis, manifests, or review summaries to decide stage. Folder-level signals are sufficient for stages 1-7 and 9; stage 8 requires the explicit review-completion record described above.

Use signals like the following. Treat exact filenames as illustrative — match by location, role, and naming pattern rather than literal strings.

- **Transcripts**: files under `00_inputs/transcripts/` or an equivalent transcripts folder.
- **Extractions**: per-interviewee extraction markdown files under `00_inputs/` (or a clearly named extractions subfolder). Compare the count and base names against transcripts to detect partial coverage.
- **Synthesis**: a cross-interview synthesis markdown file under `00_inputs/` or `01_working/`.
- **Manifest, source map, families**: markdown or structured files under `01_working/` that play these roles. All three must be present to consider the project `manifested`.
- **v1 SOPs**: files under `02_outputs/sop_v1/` (or an equivalent v1 folder).
- **v2 SOPs**: files under `02_outputs/sop_v2/` (or an equivalent v2 folder).
- **Review summaries**: per-interviewee review summary files in `01_working/review_summaries/`, `02_outputs/review_summaries/`, or another clearly named review folder. Compare coverage to the authoritative planned-interviewee roster, not only inferred extraction names.
- **Final playbook**: a single assembled playbook file under `03_playbook/` or another clearly identified playbook output folder.

When checking counts, prefer matching by base name (interviewee identifier) rather than raw count, so the audit can flag specific gaps.

When using timestamps, treat them as supporting evidence (for example to note that v2 SOPs predate review summaries) rather than as the primary stage signal.

## Output format

Return a structured response with these fields:

- **Detected stage**: one of the nine canonical stages, or `unknown`.
- **Evidence**: the specific folders, files, counts, and (where useful) timestamps that supported the call. Prefer a short table.
- **Gaps and anomalies**: anything that would block clean progression to the next stage, such as:
  - Transcripts without matching extractions, or extractions without matching transcripts.
  - Partial v2 SOP coverage relative to v1.
  - Missing planned-interviewee roster or review-completion record, which prevents a completeness claim.
  - Review summaries missing for some interviewees.
  - Action families present without a manifest, or a manifest without a source map.
  - Files in unexpected locations.
- **Recommended next skill**: the exact skill name from the pipeline, plus the inputs the user must supply (for example: project path, mode flag, the name of the external reference framework, or the interviewee identifier list).
- **Out-of-pipeline detections**: if the folder contains v3 or v4 refactor outputs (for example `sop_v3/`, `sop_v4/`), patch-flow artifacts, or any patch-mode scratch areas, list them and tell the user that this plugin is out of scope for those flows. State explicitly that this plugin will not patch existing artifacts — it can only re-run pipeline stages.

Keep the response concise, structured, and operational. Prefer tables. Mark any uncertainty with a "Needs Human Review" note rather than guessing.

## Controller rules (restated inline)

The shared controller at `${CLAUDE_PLUGIN_ROOT}/CONTROLLER.md` is canonical. Restated here for convenience:

1. Read files before acting.
2. Preserve evidence traceability to source interviews.
3. Prefer best scalable practice, not best individual practice.
4. Mark ambiguity explicitly; do not invent source material.
5. Distinguish source-grounded fact from reasonable inference from recommendation.
6. Do not flatten useful role-specific differences.

If anything in this skill appears to conflict with `${CLAUDE_PLUGIN_ROOT}/CONTROLLER.md`, the controller wins.

## Idempotence

Running the audit must not modify the project folder. Do not create, rename, move, or delete files. Do not write scratch notes into the project. The only side effect permitted is the response returned to the user.

## Out of scope

- **Patching**: this plugin does not edit individual SOPs, the playbook, manifests, or review summaries in place. If the user wants to patch, tell them this plugin will only detect that state and recommend a re-run of the appropriate stage.
- **v3/v4 refactor flows**: detect their presence as out-of-pipeline and stop. Do not recommend a next skill that targets them.
- **Fixed taxonomies**: do not hardcode a specific role-family list or a specific external reference framework. Accept whatever the project contains.
