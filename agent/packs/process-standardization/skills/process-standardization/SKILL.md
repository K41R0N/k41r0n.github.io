---
name: process-standardization
description: Runs the full evidence-traceable process-standardization method from project setup and interview extraction through SOPs, review, playbook assembly, or read-only project audit.
argument-hint: "[project inputs or project path]"
version: 0.1.0
metadata:
  harness:
    lane: L3
    surfaces: [any]
    requires: { modules: [], contracts: [], secrets: [] }
    attention: { depth: D3, mode: E4, slots: [strategize, suspect, anticipate, act, react, recognize, calculate] }
    owner: K41R0N
---
# Process standardization

Use this pack for end-to-end operations-process standardization. It preserves the complete stage procedures and their schemas, templates, quality rules, and handoffs. Existing packs can serve individual adjacent tasks; do not replace this workflow with a duplicate or thin restatement. Route to the existing relevant pack when the user asks only for that separate method.

## Shared Controller Rules

1. Read files before acting.
2. Preserve evidence traceability to source interviews.
3. Prefer best scalable practice, not best individual practice.
4. Mark ambiguity explicitly; do not invent source material.
5. Distinguish source-grounded fact from reasonable inference from recommendation.
6. Do not flatten useful role-specific differences.

The detailed canonical rules immediately below this section govern where the full meaning and examples are needed.


---

## Module: Shared controller rules

# Controller Rules

Shared rules every skill in this method package must follow. Each skill SKILL.md restates these rules so they stay in context, and may reference this file for the canonical text.

## Six Rules

1. **Read files before acting.** Always inspect the actual contents of inputs (transcripts, prior outputs, prompts) before generating anything. Do not act on filenames or summaries alone.

2. **Preserve evidence traceability to source interviews.** Every claim, action, SWOT item, or recommendation must carry an attribution back to the interview(s) it came from (interviewee label + transcript section or quote where possible).

3. **Prefer best scalable practice, not best individual practice.** When team members do similar work differently, the standard is the version that scales across the team — not the most senior person's version, the fastest version, or the most polished version.

4. **Mark ambiguity explicitly; do not invent source material.** When evidence is missing, contradictory, or unclear, flag it (e.g., `[AMBIGUOUS — see review]`, `[NOT IN SOURCE]`). Never fabricate quotes, decisions, tools, or process steps.

5. **Distinguish source-grounded fact from reasonable inference from recommendation.** Use consistent labels in outputs: `FACT` (verbatim or near-verbatim from source), `INFERENCE` (synthesized from multiple sources), `RECOMMENDATION` (best-practice guidance not present in source). Never blur the three.

6. **Do not flatten useful role-specific differences.** When two roles legitimately need different versions of an action (e.g., research vs. content), keep both. Standardization is not homogenization.

## Out of Scope

Patch-mode and mid-stream refactor flows (re-running synthesis after late-arriving interviews, regenerating manifests after staffing changes) are explicitly **out of scope** for this method package. The pipeline assumes a clean run: extract → synthesize → manifest → v1 SOPs → v2 overlay → review summaries → final playbook.

---

## Module: Pipeline overview and operating guide

# process-standardization

A method package that packages an end-to-end methodology for standardizing how an operations team works. Drop in interview transcripts, follow the pipeline, ship a rollout playbook.

## Pipeline

```
extract → synthesize → manifest → v1 SOPs → v2 overlay → review summaries → final playbook
```

The method package assumes a clean run. Patch-mode flows (re-running synthesis after late interviews, mid-project staffing fixes, later major-version refactors) are intentionally out of scope. If new evidence arrives after the manifest is built, re-run the pipeline rather than patching.

## Skills

| Skill | When to use |
|---|---|
| `process-standardization-bootstrap` | Scaffold a new project — folder layout, controller rules, master prompt. Run first. |
| `interview-extraction` | One transcript in, one lossless structured extraction out. Run once per interviewee. |
| `cross-interview-synthesis` | N extractions in. Produces SWOT, action comparison matrix, standardization boundary map. |
| `action-manifest` | Builds the canonical action manifest, source map, and action families. Build only — no patch mode. |
| `sop-drafter` | Two modes: `internal` (v1 from team practice) and `overlay` (v2 layered on a user-supplied external reference framework). |
| `interviewee-review-summary` | Two-page verification doc back to each interviewee before the playbook is finalized. |
| `playbook-assembler` | Assembles the final 12-section rollout playbook from manifest, families, v2 SOPs, and incorporated review feedback. |
| `process-standardization-audit` | Inspects an existing project folder, identifies which pipeline stage it is at, recommends the next skill. Read-only. |

## Shared rules

Every skill restates and enforces the six controller rules. The canonical text lives at `CONTROLLER.md` (referenced from each skill as `the Six Rules section near the start of this skill`):

1. Read files before acting.
2. Preserve evidence traceability to source interviews.
3. Prefer best scalable practice, not best individual practice.
4. Mark ambiguity explicitly; do not invent source material.
5. Distinguish source-grounded fact from reasonable inference from recommendation.
6. Do not flatten useful role-specific differences.

## Parameters every skill accepts

The methodology generalizes — none of these are hardcoded:

- **Role-family taxonomy** — any list. The team supplies its own role-family list at bootstrap.
- **External reference framework** — any methodology, book, industry standard, or third-party playbook the team wants to overlay in v2. The framework is supplied by the team when needed.

## Setup

Load this pack, then start a session in the directory you want to scaffold and invoke the bootstrap skill (for example, "set up a process standardization project for my team").

---

## Module: Project bootstrap

# Bootstrap

# process-standardization-bootstrap

## Purpose

Scaffold a new project that turns interview transcripts from an operations team into rollout-ready SOPs and a final process playbook. This stage creates only the folder layout, controller rules, master project prompt, and inputs README. It does not run extractions, draft SOPs, or assemble the playbook — those are downstream skills.

The output of this skill is a clean, empty project directory that:

- Tells the user exactly where to drop interview transcripts and reference material.
- Carries the six controller rules into every downstream step.
- Stages the master project prompt so any later working session inherits the same operating mode.
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

1. **Team name** — short label used in the project root and in headings (e.g. "team-a", "team-b", "service-team").
2. **Project root path** — absolute project root consistent with the user's workspace. If unspecified, propose a path and confirm it before creating files.
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

The canonical controller rules for every downstream skill. Restate the six controller rules below verbatim. Also include a one-line note pointing at `the Six Rules section near the start of this skill` as the canonical version any downstream skill should defer to if it ships with the method package.

### 3. `04_prompts/15_master_project_prompt.md`

A master prompt that any future assistant session can paste in to operate on the project holistically. It must:

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

These rules apply to every skill in the pipeline, not just bootstrap. Write them into `04_prompts/00_controller.md` exactly as listed below, and reference `the Six Rules section near the start of this skill` as the canonical shared copy.

1. Read files before acting.
2. Preserve evidence traceability to source interviews.
3. Prefer best scalable practice, not best individual practice.
4. Mark ambiguity explicitly; do not invent source material.
5. Distinguish source-grounded fact from reasonable inference from recommendation.
6. Do not flatten useful role-specific differences.

## Pipeline this bootstrap prepares for

The scaffolded project is designed to flow through these stages, in order. Each stage corresponds to a downstream skill in the same method package.

1. **Extract** — `interview-extraction` parses each transcript in `00_inputs/transcripts/` into a structured extraction in `01_working/extractions/`.
2. **Synthesize** — `cross-interview-synthesis` rolls the extractions up into a single synthesis document in `01_working/synthesis/`.
3. **Manifest** — `action-manifest` produces the action manifest, source map, and action-family grouping in `01_working/manifest/`.
4. **SOP v1** — `sop-drafter` produces SOP v1 files in `02_outputs/sop_v1/`, grounded only in internal team practice from the extractions.
5. **SOP v2 overlay** — `sop-drafter` (v2 mode) produces SOP v2 files in `02_outputs/sop_v2/` by selectively overlaying the reference framework.
6. **Review summaries** — `interviewee-review-summary` produces per-person review summaries in `01_working/review_summaries/` so each interviewee can validate their input.
7. **Final playbook** — `playbook-assembler` produces `03_playbook/final-team-process-playbook.md`.

Out of scope for this skill and the broader bootstrap flow: patch-mode flows on partial transcripts, later major-version refactor passes, and mid-project re-extraction. If the user asks for those, stop and route them to a manual conversation rather than scaffolding around them.

## Hand-off

After bootstrap completes:

1. List every file and folder created, by absolute path.
2. Tell the user the next action: drop interview transcripts into `00_inputs/transcripts/` (one file per interviewee, named `<role-family>__<person>.md`), and optional reference material into `00_inputs/reference/`.
3. Tell the user the next skill to invoke is `interview-extraction`, run once per transcript.
4. Do not start the extraction in this skill, even if transcripts are already present. Bootstrap ends at hand-off.

---

## Module: Interview extraction

# Interview Extraction

## Purpose

Turn one raw interview transcript into a single, structured, lossless extraction document. The extraction is the canonical record of what one interviewee said and how they work. Every downstream step in this method package (action manifest building, cross-interview synthesis, SOP drafting, SWOT analysis) reads extractions, never raw transcripts. The extraction must therefore preserve the interviewee's evidence with enough fidelity that no future step needs to re-open the transcript.

This stage produces the extraction. It does not compare interviewees, propose standards, or recommend changes.

## When to trigger

Invoke this skill when ALL of the following are true:

- A single interview transcript is in hand (file, pasted text, or path).
- No extraction has been produced yet for this interviewee, or the existing extraction is being replaced wholesale.
- The user asks for "an extraction", "to process the interview", or any of the trigger phrases in the frontmatter.

Do NOT invoke this skill to update an existing extraction in place, to compare interviewees, or to draft an SOP. Those are separate skills.

If two or more transcripts are provided at once, run this skill once per transcript and produce one extraction per interviewee.

## Required inputs

Collect the following before writing the extraction. If any are missing, ask the user explicitly rather than guessing.

- **Transcript path or text**: absolute path to the transcript file, or the full transcript pasted inline.
- **Interviewee name** (or stable label if anonymized).
- **Role / job title** as the interviewee describes it.
- **Role-family**: the higher-level grouping this role belongs to in the project's role taxonomy (whatever role-family list the project is using; do not assume a fixed list). If the project has not defined one, mark "Not stated" and continue.
- **Team / business context** (optional): one or two sentences on the team this person sits in, the client(s) or product(s) they support, and the timeframe of the interview.

If the transcript includes timestamps, section markers, or speaker labels, preserve those exactly when quoting.

## Output schema

Write the extraction as a single markdown file. The downstream contract is the section structure below — keep section headings stable so other skills can parse them.

### 1. Interviewee Profile

- Name / label
- Role / function
- Role-family (as supplied by the user)
- Team / business context
- Core ownership areas
- Main collaborators / dependencies (named individuals plus their function)
- Scope boundaries (owns vs supports vs depends on others for)
- Tenure / time in role on this work, if stated

### 2. Main Actions / Responsibilities

A compact table listing each recurring action this person performs. For each row capture:

- Action name
- Purpose
- Frequency / cadence
- Whether the action is strategic, executional, or both

This is the index. The detail lives in the Process Cards.

### 3. Process Cards (one per recurring action)

Use the per-action capture format defined below. Produce one Process Card for every action in the table, in the same order.

### 4. Handoffs

For each action that crosses a person or team boundary, record:

- Handoffs IN: who delivers what to this person, in what form, on what trigger.
- Handoffs OUT: who this person delivers what to, in what form, on what trigger.
- Approval / review path, if any.

If a process is fully self-contained, record that explicitly.

### 5. Pain Points

For each pain point:

- Pain point statement
- Root cause if stated or strongly implied (mark which)
- Operational impact
- Evidence / quote

### 6. Ambiguities Flagged by the Interviewee

Anything the interviewee said they were unsure about, did not know, or said was undefined (missing KPIs, unclear ownership, undocumented steps, conflicting guidance). Capture each with the verbatim phrasing or a tight paraphrase plus its source location. Do not resolve these here.

### 7. Verbatim Quotes

A bank of direct quotes preserved verbatim, each tagged with timestamp or section marker when the transcript provides one (e.g., `[00:14:22]`, `[Q3 — Tools]`, or line range). Include any quote that:

- Captures a decision rule, judgment criterion, or workaround in the interviewee's own words.
- Reveals attitude, friction, or workaround that a paraphrase would dilute.
- Will plausibly be cited by downstream synthesis.

When in doubt, keep the quote. Lossless beats tidy.

### 8. Tools and Systems Mentioned

A flat list of every concrete tool, platform, dashboard, template, framework, content format, file, channel, and metric named in the transcript. One bullet per item. Include short context (what the interviewee uses it for) but do not editorialize.

### 9. SWOT-Relevant Signals (captured, not synthesized)

Capture signals into four buckets without comparing across interviewees and without recommending action:

- Strengths: things the interviewee or transcript indicates they do well.
- Weaknesses: friction, gaps, or under-developed practices.
- Opportunities: improvements explicitly named or strongly implied by the interviewee.
- Threats: risks, failure modes, dependencies, or fragilities.

Each signal is one line plus an evidence pointer (quote ID, timestamp, or paraphrase tag). Synthesis happens later in `cross-interview-synthesis`.

### 10. Explicit vs Inferred

Two short lists:

- **Explicitly stated**: facts the interviewee said outright.
- **Reasonably inferred**: conclusions tightly grounded in what was said. Each inference must be followed by the evidence it rests on.

If you cannot point to evidence, do not include the inference.

### 11. Analyst Notes for Later Comparison

Plain-English notes for the synthesis step: candidate standout strengths, candidate inconsistency points, candidate best-practice patterns to test against other interviewees. Do not compare yet. Do not recommend.

## Lossless rule

Every claim in the extraction must trace back to a verbatim quote or to a paraphrase tagged with the source location (timestamp, section marker, or line range). If a claim cannot be traced, either find the evidence, mark it "Not stated", or remove the claim. Do not invent material. Do not smooth over contradictions — record both sides and flag the conflict in section 6.

When the interviewee describes multiple workflows that look similar, separate them. Do not collapse useful distinctions for the sake of brevity.

## Per-action capture format (Process Card)

Use this exact structure for each Process Card in section 3. Fields that are absent from the transcript get "Not stated" — never a guess.

```
## Process Card: [Action Name]
- Purpose:
- Trigger:
- Inputs:
- Step-by-step current workflow:
  1.
  2.
  3.
- Tools / systems used:
- Templates / frameworks used:
- Decision rules / judgment criteria:
- Approvals / review path:
- Handoffs / collaborators:
- Outputs / deliverables:
- Timing / SLA / cadence:
- Success metrics mentioned:
- Pain points / friction:
- Risks / threats:
- What works especially well:
- Notable workarounds / hacks:
- Standardization candidate:
  - Yes / No / Conditional
  - Why:
- Evidence / quotes:
  - Quote 1 (with source tag)
  - Quote 2 (with source tag)
```

The downstream `action-manifest` skill expects these exact field names. Do not rename them.

The "Standardization candidate" field is a structural marker, not a recommendation. Tag Yes / No / Conditional based on whether the action looks transferable in principle. The actual standard is decided later in synthesis.

## Six controller rules (restated inline)

These rules apply to every step of this skill. The canonical version lives at `the Six Rules section near the start of this skill`; treat that file as the source of truth if the two ever drift.

1. **Read files before acting.** Open the transcript and any referenced inputs in full before writing the extraction.
2. **Preserve evidence traceability to source interviews.** Every claim points back to a quote, timestamp, or section marker.
3. **Prefer best scalable practice, not best individual practice.** When tagging standardization candidates, consider whether the practice generalizes — not just whether this person does it well.
4. **Mark ambiguity explicitly; do not invent source material.** Use "Not stated" liberally. Never fabricate quotes, metrics, tool names, or process steps.
5. **Distinguish source-grounded fact from reasonable inference from recommendation.** Section 10 splits fact from inference. This stage never produces recommendations — those belong to later skills.
6. **Do not flatten useful role-specific differences.** If two interviewees do "the same" thing differently and the difference matters, that difference belongs in their respective extractions exactly as stated.

## Output location and naming

Write the extraction as a single markdown file. Use a stable, predictable filename so downstream skills can find it: `<interviewee-label>-extraction.md`, all lowercase, hyphenated. Place it alongside the project's other extractions (the user supplies the directory).

Confirm the path with the user once before writing if more than one plausible location exists.

## Hand-off to the next skill

After writing this extraction, check whether extractions now exist for ALL planned interviewees on this project.

- If YES: invoke `cross-interview-synthesis` to begin comparing across people. Pass the directory containing the full set of extractions.
- If NO: report which interviewees still need extractions and stop. Do not begin synthesis with a partial set.

Do not attempt to synthesize, draft SOPs, or build the action manifest from inside this skill. Those are downstream and depend on the full extraction set.

---

## Module: Cross-interview synthesis

# Cross-Interview Synthesis

## Purpose

Take every completed interview extraction for a single operations team and produce three artifacts: a team-level SWOT grounded in interviewee evidence, an action comparison matrix that lines up recurring actions across role-families, and a standardization boundary map that classifies each action as STANDARDIZE, TEMPLATIZE, or PRESERVE-VARIANT. These three artifacts are the inputs the `action-manifest` skill needs to decide what to standardize next.

## When to trigger

Trigger this skill when:

- An interview extraction exists for every planned interviewee on the team.
- No action manifest, SOP set, or playbook has been drafted yet for this team.
- The user asks to compare, synthesize, or roll up the interviews into team-level findings.

Do not trigger this skill when extractions are still missing, when the synthesis already exists and the user is asking for a downstream artifact, or when the request is to patch an existing synthesis after a late interview. Patch-mode synthesis is out of scope.

## Required inputs

Before running, confirm the following with the user:

1. **Folder containing N extractions.** A directory holding one extraction file per interviewee. Read every file in that folder. If the folder is unclear, ask.
2. **Role-family list.** The set of role-families to compare across. The taxonomy is whatever the team uses. A role-family taxonomy is a project input, not a fixed schema. Accept any list, with fewer or more families and different labels.
3. **Team identifier.** A short label for the team being synthesized so the output title is unambiguous.

If any input is ambiguous, stop and ask before reading. Do not invent a role-family list.

## Outputs

Produce one synthesis document containing the three required artifacts in this order.

### a. Team-level SWOT (evidence-grounded)

Four sections: **Strengths**, **Weaknesses**, **Opportunities**, **Threats**.

For every bullet, include:

- A short description of the pattern.
- The interviewee(s) that show it — by name or pseudonym, matching how they appear in the extractions.
- A direct evidence reference: a quote, a paraphrased observation tagged to the source, or both.
- The operational implication for the team.

A SWOT bullet without a named source is not allowed. If a pattern is supported by inference rather than a direct quote, mark it as inference and say which extraction(s) the inference is drawn from.

### b. Action comparison matrix

Rows are recurring actions (the things people on the team actually do). Columns are role-families, or individual interviewees when the team is small enough that role-family is just one person per family.

Each cell describes how that role-family performs the action: shared steps, tools, decision rules, handoffs, pain points. For every row also call out:

- Where the role-families converge (the shared spine of the action).
- Where they diverge (the role-specific variations).
- Whether the divergence appears intentional and useful, or accidental and harmful.

If an action is only performed by one role-family, keep it in the matrix and mark the other cells as "not performed" rather than dropping it. The reader needs to see the gap.

### c. Standardization boundary map

For every action in the matrix, classify it as exactly one of:

- **STANDARDIZE** — converge on one shared way. Use when the variation is harmful inconsistency, the best scalable practice is clear, and there is no good reason for role-specific variants.
- **TEMPLATIZE** — shared skeleton plus role-specific overlay. Use when the action has a stable structure (template, format, cadence) but the content or inputs legitimately differ by role-family.
- **PRESERVE-VARIANT** — leave the role differences alone. Use when the variation reflects a real and useful specialization that would lose value if flattened (rule 6 below).

For each action, write one or two sentences explaining why it landed in that bucket, citing the matrix evidence.

## Method

1. **Read every extraction file in the folder before writing anything.** If the folder contains files outside the extraction format, ask before including them. Do not summarize from filenames.
2. **Inventory recurring actions.** Walk through every extraction and pull out the actions each person performs. Cluster actions across people that are the same operational thing under different names. Note disagreement on naming — terminology drift is itself a finding.
3. **Build the matrix first.** For each clustered action, fill the cells. The matrix is what the SWOT and boundary map both read from.
4. **Derive the SWOT from the matrix.** Strengths and weaknesses follow from the convergence/divergence pattern. Opportunities follow from cross-pollination candidates (one role-family does it well, others would benefit). Threats follow from key-person dependencies, single points of failure, and unmanaged risk surfaced in the matrix.
5. **Classify each action for the boundary map.** Apply rule 3: pick the best **scalable** practice, not the best **individual** practice. Some practitioners are world-class because of personal skill that does not transfer. The synthesis must distinguish "this works because it is well-designed" from "this works because of who is doing it."
6. **Sanity-check against the controller rules below before finalizing.**

## Anti-patterns

Do not:

- **Default to the senior person's version.** Seniority is not evidence. A strong individual may be doing it the hardest, least transferable way. Pick the version that the rest of the team can actually run.
- **Flatten role-specific differences that exist for a reason.** If a research role-family needs deep boolean filtering and a content role-family needs broad ideation, those are different jobs. Pretending they are the same job because the word "research" appears in both produces SOPs that nobody follows.
- **Score consistency without explaining cost.** "Low consistency" is a description, not a recommendation. The boundary map is where the recommendation lives.
- **Invent supporting quotes.** If you cannot find a direct evidence reference, mark the bullet as inference and name the extractions it is drawn from.
- **Drop solo actions.** An action performed by one person is still in the matrix — that is exactly where key-person risk lives.

## Controller rules (restated inline)

The canonical version lives at `the Six Rules section near the start of this skill`. Restated here for inline use:

1. **Read files before acting.** Read every extraction file in the input folder before producing any synthesis output. No summary may rely on filename inference.
2. **Preserve evidence traceability to source interviews.** Every SWOT bullet, matrix cell, and boundary classification must be traceable to one or more named interviewees.
3. **Prefer best scalable practice, not best individual practice.** When two practitioners diverge, ask which version a new hire could run on day 30 — not which version produces the best output today in the hands of the most skilled person.
4. **Mark ambiguity explicitly; do not invent source material.** If extractions disagree, say so. If evidence is thin, say so. Do not paper over gaps with confident prose.
5. **Distinguish source-grounded fact from reasonable inference from recommendation.** Tag each finding as `fact` (direct from extraction), `inference` (reasoned from extractions), or `recommendation` (synthesist's judgment). The reader should always know which is which.
6. **Do not flatten useful role-specific differences.** Variation that reflects real specialization is a feature. The boundary map's PRESERVE-VARIANT category exists for exactly this case. Use it.

## Hand-off

The synthesis output (SWOT + action comparison matrix + standardization boundary map) is the input to the `action-manifest` skill. After writing the synthesis, point the user at `action-manifest` as the next step. Do not draft SOPs, playbooks, or rollout plans inside this skill — those are downstream.

---

## Module: Action manifest

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

- **id** — stable slug-style identifier (lowercase, hyphenated, short). Examples of the *form*: `daily-research`, `vp-request-lifecycle`, `weekly-kpi-reporting`. Once issued, an id is permanent. Downstream SOPs will reference it.
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

Do not hardcode any specific taxonomy. Any taxonomy examples are illustrative only. Accept whatever family list the user supplies.

## Naming rules

- Ids are slug-style: lowercase, hyphenated, short, descriptive.
- Ids are stable. Once issued, an id never gets renamed. Downstream SOPs reference these ids; renaming breaks traceability.
- If an action's *display name* needs to change later, change the name field, not the id.
- If two actions get accidentally collapsed into one id and need to be split later, that is a re-run of the manifest, not an in-place rename. See "Out of scope".
- Family names follow the user's spelling and casing exactly.

## Controller rules (restated inline)

These six rules govern this skill. The canonical version lives at `the Six Rules section near the start of this skill` — defer to that file if there is any conflict.

1. **Read files before acting.** Read every input listed above before producing any output.
2. **Preserve evidence traceability to source interviews.** Every manifest claim must be traceable through the source map back to specific extraction passages.
3. **Prefer best scalable practice, not best individual practice.** Standardize on what is teachable and repeatable across roles, not on a single person's expert workflow.
4. **Mark ambiguity explicitly; do not invent source material.** If a row is thin or contested, say so. Never fabricate quotes or process detail to fill a gap.
5. **Distinguish source-grounded fact from reasonable inference from recommendation.** Use explicit markers in the source map. A future reader must be able to see at a glance which claims are observed vs. inferred vs. recommended.
6. **Do not flatten useful role-specific differences.** If a difference between roles is meaningful, keep it as a `PRESERVE-VARIANT` row or split into separate rows. Do not collapse for the sake of a tidy taxonomy.

## Out of scope

This stage is **build only**. It produces the manifest, the source map, and the families grouping once per engagement.

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

---

## Module: SOP drafting

# SOP drafting

# sop-drafter

## Purpose

Produce one Standard Operating Procedure per action in the action manifest, then optionally enrich each SOP by overlaying an external reference framework supplied by the user. The skill operates in two clearly separated modes so that team-grounded practice never gets silently mixed with outside guidance: every step is labeled, every claim is traceable, and the output is consistent enough to feed the downstream playbook assembler.

Reference the canonical controller at `the Six Rules section near the start of this skill` for shared rules. The six controller rules are restated inline at the bottom of this skill — apply them on every run.

## The Two Modes

This stage has exactly two modes. Decide which mode to run before reading any source material. If the user request is ambiguous, ask.

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

The skill must not assume any specific framework. Any particular reference framework is only an example, not a baked-in dependency. Treat whichever framework the user supplies as the reference, and do not bring in material from frameworks the user did not name.

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

Canonical authority: `the Six Rules section near the start of this skill`. If the canonical file disagrees with this restatement, the canonical file wins.

## Hand-off

After producing v2 SOPs, hand off in this order:

1. Invoke `interviewee-review-summary` once per interviewee. Each interviewee should receive a personalized summary of which of their practices are preserved, upgraded, or marked as known limitations across the v2 SOP set.
2. After review summaries are produced, invoke `playbook-assembler` to compile the SOPs and supporting artifacts into the final playbook.

After producing v1 SOPs (and not yet v2), hand off back to the orchestrator. Do not invoke `interviewee-review-summary` until v2 exists — review summaries should reflect the final state of each interviewee's contribution, not an intermediate one.

---

## Module: Interviewee review summary

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

Out of scope: patch flows, mid-project re-extraction, later major-version refactors. If corrections are major, the user re-runs the relevant pipeline stages — this skill does not orchestrate that.

## Required Inputs

Before generating the document, confirm access to:

1. The interviewee's extraction file (single source of truth for what they said).
2. The current action manifest (so each action they own or contributed to can be located).
3. The v1 SOPs and v2 SOPs that cite their extraction (so boundary classifications and SOP ids are knowable).
4. The role-family list in use on this project; adapt to the team’s own taxonomy.

If any of these are missing, stop and say which one.

## The Six Controller Rules (Restate Inline)

These rules govern every skill in this method package. The canonical version lives at `the Six Rules section near the start of this skill`. Restated here so this skill is self-contained:

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
- Major corrections (you missed an action, you mis-classified a STANDARDIZE as a PRESERVE-VARIANT, an entire workflow was wrong) are escalated. This stage does not invoke patch flows. The user re-runs the affected pipeline stage with the corrected input.

Once corrections are folded in (or escalated), this skill is done. The playbook assembler picks up from there.

---

## Module: Playbook assembly

# Playbook assembly

# Playbook Assembler

## Purpose

Produce the single canonical rollout playbook that an operations team will work from after process standardization is complete. The playbook is the executable artifact: every team member can be handed this document and told "this is how we work now." It consolidates the manifest of actions, the action-family taxonomy, the v2 SOPs (with review corrections incorporated), and the team's operating context into one structured document with twelve sections.

This stage produces a playbook. It does not produce SOPs (see sop-drafter), patches, or refactors. Revisions after rollout flow through Section 12 of the playbook itself, not through a separate patch skill.

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
   - Any external reference framework the team is mapping against (this is optional and team-specific; this is optional and team-specific).

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
3. Source-content hygiene: verify that no patch-mode artifacts have leaked through. The output is the canonical playbook. Do not include language that refers to internal version refactors or to interviewee-specific patch flows. Those belong to upstream skills, not to the rollout document.
4. Section completeness: every one of the twelve sections is present, in order, non-empty, and uses content from the required inputs.
5. Boundary visibility: the standardized-strictly versus standardized-with-flexibility versus left-role-specific classification is visible in Section 1 and reflected per item in Section 6.

## Controller Rules (Restated Inline)

The shared controller for this method package is canonical at `the Six Rules section near the start of this skill`. The six rules apply to this skill in full:

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

---

## Module: Process-standardization audit

# Process-standardization audit (read-only)

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

7. **v2-drafted** — v2 SOP files are present, and no interviewee review summaries exist yet.
   - Recommend: run `interviewee-review-summary` once per interviewee.

8. **reviewed** — review summaries have been returned and incorporated, and no final playbook is present.
   - Recommend: run `playbook-assembler`.

9. **shipped** — final playbook is present.
   - No next pipeline step. Point the user to the maintenance section of the assembled playbook for ongoing upkeep.

If no stage condition is satisfied (for example the folder is empty, mis-shaped, or contains only unrelated files), return `unknown` and explain what was missing.

## Detection rules

Make stage calls from folder structure, file presence, file counts, and timestamps. Do not open or parse the contents of SOPs, the playbook, transcripts, extractions, synthesis, manifests, or review summaries to decide stage. Folder-level signals are sufficient.

Use signals like the following. Treat exact filenames as illustrative — match by location, role, and naming pattern rather than literal strings.

- **Transcripts**: files under `00_inputs/transcripts/` or an equivalent transcripts folder.
- **Extractions**: per-interviewee extraction markdown files under `00_inputs/` (or a clearly named extractions subfolder). Compare the count and base names against transcripts to detect partial coverage.
- **Synthesis**: a cross-interview synthesis markdown file under `00_inputs/` or `01_working/`.
- **Manifest, source map, families**: markdown or structured files under `01_working/` that play these roles. All three must be present to consider the project `manifested`.
- **v1 SOPs**: files under `02_outputs/sop_v1/` (or an equivalent v1 folder).
- **v2 SOPs**: files under `02_outputs/sop_v2/` (or an equivalent v2 folder).
- **Review summaries**: per-interviewee review summary files in a clearly named reviews folder under `02_outputs/`. Compare count and names against the interviewee list inferred from extractions.
- **Final playbook**: a single assembled playbook file (for example `final-team-process-playbook.md`) under `02_outputs/`.

When checking counts, prefer matching by base name (interviewee identifier) rather than raw count, so the audit can flag specific gaps.

When using timestamps, treat them as supporting evidence (for example to note that v2 SOPs predate review summaries) rather than as the primary stage signal.

## Output format

Return a structured response with these fields:

- **Detected stage**: one of the nine canonical stages, or `unknown`.
- **Evidence**: the specific folders, files, counts, and (where useful) timestamps that supported the call. Prefer a short table.
- **Gaps and anomalies**: anything that would block clean progression to the next stage, such as:
  - Transcripts without matching extractions, or extractions without matching transcripts.
  - Partial v2 SOP coverage relative to v1.
  - Review summaries missing for some interviewees.
  - Action families present without a manifest, or a manifest without a source map.
  - Files in unexpected locations.
- **Recommended next skill**: the exact skill name from the pipeline, plus the inputs the user must supply (for example: project path, mode flag, the name of the external reference framework, or the interviewee identifier list).
- **Out-of-pipeline detections**: if the folder contains later major-version refactor outputs (for example `sop_vNext/`), patch-flow artifacts, or any patch-mode scratch areas, list them and tell the user that this method package is out of scope for those flows. State explicitly that this method package will not patch existing artifacts — it can only re-run pipeline stages.

Keep the response concise, structured, and operational. Prefer tables. Mark any uncertainty with a "Needs Human Review" note rather than guessing.

## Controller rules (restated inline)

The shared controller at `the Six Rules section near the start of this skill` is canonical. Restated here for convenience:

1. Read files before acting.
2. Preserve evidence traceability to source interviews.
3. Prefer best scalable practice, not best individual practice.
4. Mark ambiguity explicitly; do not invent source material.
5. Distinguish source-grounded fact from reasonable inference from recommendation.
6. Do not flatten useful role-specific differences.

If anything in this skill appears to conflict with `the Six Rules section near the start of this skill`, the controller wins.

## Idempotence

Running the audit must not modify the project folder. Do not create, rename, move, or delete files. Do not write scratch notes into the project. The only side effect permitted is the response returned to the user.

## Out of scope

- **Patching**: this method package does not edit individual SOPs, the playbook, manifests, or review summaries in place. If the user wants to patch, tell them this method package will only detect that state and recommend a re-run of the appropriate stage.
- **later major-version refactor flows**: detect their presence as out-of-pipeline and stop. Do not recommend a next skill that targets them.
- **Fixed taxonomies**: do not hardcode a specific role-family list or a specific external reference framework. Accept whatever the project contains.

## Provenance

Expanded from the user-provided process-standardization method package: its controller, README, bootstrap, interview extraction, cross-interview synthesis, action-manifest, SOP-drafting, interviewee review, playbook assembly, and process audit documents. Original procedure detail, output contracts, templates, and quality rules are retained; the source's named domain-framework and fixed-taxonomy examples are generalized. The archive's workflow implementation/delivery status has not been independently established.
