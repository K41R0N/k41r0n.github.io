---
name: process-standardization-bootstrap
description: Scaffolds a new process-standardization project for an operations team — creates the folder structure, controller rules, master project prompt, and inputs README so the team can drop in interview transcripts and run the full extraction-to-playbook pipeline. Triggers when the user says "set up a process standardization project", "scaffold a process project", "start a new team standardization", "bootstrap the methodology", "kick off a team interview project", or otherwise asks to initialize the methodology for a specific team and set of role-families.
version: 0.1.0
---

# process-standardization-bootstrap

## Purpose

Scaffold a new project that turns interview transcripts from an operations team into rollout-ready SOPs and a final process playbook. This skill creates only the folder layout, controller rules, master project prompt, and inputs README. It does not run extractions, draft SOPs, or assemble the playbook — those are downstream skills.

The output of this skill is a clean, empty project directory that:

- Tells the user exactly where to drop interview transcripts and reference material.
- Carries the six controller rules into every downstream step.
- Stages the master project prompt so any later Claude session inherits the same operating mode.
- Names the role-families to be standardized so downstream skills can fan out per family.

## When to trigger

Trigger this skill when the user asks to:

- Set up a new process-standardization project for a specific team.
- Scaffold the folder structure before interviews are loaded.
- Bootstrap the methodology in a fresh repo or directory.
- Kick off a team interview project where transcripts will be added later.
- Start a new team standardization for any operations function (content, research, design, support, ops, marketing, sales operations, community, etc.).

Do not trigger this skill if the project folders already exist with populated inputs. In that case route to `process-standardization-audit` or the next pipeline skill.

## Inputs the user must supply

Before writing any files, collect these from the user. Ask explicitly if any are missing — do not invent defaults.

1. **Team name** — short label used in the project root and in headings (e.g. "platform-ops", "growth-marketing", "client-services").
2. **Project root path** — absolute path under `~/Projects/...` consistent with the workspace policy. If unspecified, propose `~/Projects/products/<team-name>-process-standardization` and confirm.
3. **List of role-families to standardize** — any number of families, named by the user. Examples only: research, content, visual production, reporting, community, campaigns. Accept whatever the user provides; do not force the example taxonomy.
4. **List of interviewees** — names and role-family for each person whose transcript will be processed. One person may map to one or more families.
5. **Optional external reference framework** — a playbook, framework, or strategy doc that will be used as a v2 overlay (e.g. an internal best-practices guide). Optional. If supplied, capture title and source path.

State assumptions back to the user before scaffolding. If the user is vague about role-families or interviewees, stop and ask.

## Folder layout to create

Create the following structure under the chosen project root. Top-level folders are numbered so they sort in pipeline order. Do not create empty leaf files unless listed below — keep the tree minimal.

```
<project-root>/
├── 00_inputs/
│   ├── README.md                     # what to drop where
│   ├── transcripts/                  # raw interview transcripts (one file per interviewee)
│   └── reference/                    # optional external framework, SOWs, OKRs, prior docs
├── 01_working/
│   ├── extractions/                  # per-interview structured extractions
│   ├── synthesis/                    # cross-interview synthesis output
│   ├── manifest/                     # action manifest, source map, action families
│   └── review_summaries/             # per-interviewee review summaries
├── 02_outputs/
│   ├── sop_v1/                       # SOPs grounded only in internal team practice
│   └── sop_v2/                       # SOPs after selective overlay of the reference framework
├── 03_playbook/
│   └── final-team-process-playbook.md  # placeholder; assembled at the end
└── 04_prompts/
    ├── 00_controller.md              # the six controller rules
    └── 15_master_project_prompt.md   # operating-mode prompt for any future session
```

If the user did not supply a reference framework, still create `00_inputs/reference/` but note in the inputs README that it is optional.

If the user supplied N role-families, do not pre-create per-family subfolders inside `sop_v1/` and `sop_v2/`. Those are created by `sop-drafter` once the manifest is built — pre-creating them risks flattening the families before evidence is reviewed.

## Files to write

Write exactly four files during bootstrap. Do not pre-populate working files, SOPs, or the playbook.

### 1. `00_inputs/README.md`

A short, operator-facing file. Cover:

- Project name and team.
- One-paragraph goal: turn transcripts into SOP v1 → SOP v2 → final team process playbook.
- Where to put transcripts (`00_inputs/transcripts/`, one file per interviewee, name format `<role-family>__<person>.md` or `.txt`).
- Where to put reference material (`00_inputs/reference/`).
- The list of role-families captured from the user.
- The list of interviewees and their assigned family.
- The five project-level rules, restated plainly:
  - Preserve traceability to source interviews.
  - Prefer best scalable practice, not just best individual practice.
  - Do not flatten useful role-specific differences.
  - Do not apply the reference framework until SOP v1 exists.
  - Mark ambiguity explicitly rather than inventing details.

### 2. `04_prompts/00_controller.md`

The canonical controller rules for every downstream skill. Restate the six controller rules below verbatim. Also include a one-line note pointing at `${CLAUDE_PLUGIN_ROOT}/CONTROLLER.md` as the canonical version any downstream skill should defer to if it ships with the plugin.

### 3. `04_prompts/15_master_project_prompt.md`

A master prompt that any future Claude Code session can paste in to operate on the project holistically. It must:

- Identify the project root and team.
- Reference the six controller rules in `00_controller.md`.
- Describe the pipeline (extract → synthesize → manifest → v1 SOPs → v2 overlay → review summaries → final playbook).
- Tell the model to inspect folder state before recommending action.
- Tell the model to prefer surgical edits over reruns.
- Tell the model to push back on standardizing role-specific behavior.
- Keep the tone of a pragmatic staff operations consultant.

Generalize: remove any references to a specific industry, vertical, or example team. The prompt must read cleanly for any operations team.

### 4. `02_outputs/.gitkeep` and `03_playbook/.gitkeep`

Empty placeholders so the output folders are tracked before any artifact lands. Optional — skip if the project is not under version control.

## The six controller rules (restate inline)

These rules apply to every skill in the pipeline, not just bootstrap. Write them into `04_prompts/00_controller.md` exactly as listed below, and reference `${CLAUDE_PLUGIN_ROOT}/CONTROLLER.md` as the canonical shared copy.

1. Read files before acting.
2. Preserve evidence traceability to source interviews.
3. Prefer best scalable practice, not best individual practice.
4. Mark ambiguity explicitly; do not invent source material.
5. Distinguish source-grounded fact from reasonable inference from recommendation.
6. Do not flatten useful role-specific differences.

## Pipeline this bootstrap prepares for

The scaffolded project is designed to flow through these stages, in order. Each stage corresponds to a downstream skill in the same plugin.

1. **Extract** — `interview-extraction` parses each transcript in `00_inputs/transcripts/` into a structured extraction in `01_working/extractions/`.
2. **Synthesize** — `cross-interview-synthesis` rolls the extractions up into a single synthesis document in `01_working/synthesis/`.
3. **Manifest** — `action-manifest` produces the action manifest, source map, and action-family grouping in `01_working/manifest/`.
4. **SOP v1** — `sop-drafter` produces SOP v1 files in `02_outputs/sop_v1/`, grounded only in internal team practice from the extractions.
5. **SOP v2 overlay** — `sop-drafter` (v2 mode) produces SOP v2 files in `02_outputs/sop_v2/` by selectively overlaying the reference framework.
6. **Review summaries** — `interviewee-review-summary` produces per-person review summaries in `01_working/review_summaries/` so each interviewee can validate their input.
7. **Final playbook** — `playbook-assembler` produces `03_playbook/final-team-process-playbook.md`.

Out of scope for this skill and the broader bootstrap flow: patch-mode flows on partial transcripts, v3 or v4 refactor passes, and mid-project re-extraction. If the user asks for those, stop and route them to a manual conversation rather than scaffolding around them.

## Hand-off

After bootstrap completes:

1. List every file and folder created, by absolute path.
2. Tell the user the next action: drop interview transcripts into `00_inputs/transcripts/` (one file per interviewee, named `<role-family>__<person>.md`), and optional reference material into `00_inputs/reference/`.
3. Tell the user the next skill to invoke is `interview-extraction`, run once per transcript.
4. Do not start the extraction in this skill, even if transcripts are already present. Bootstrap ends at hand-off.
