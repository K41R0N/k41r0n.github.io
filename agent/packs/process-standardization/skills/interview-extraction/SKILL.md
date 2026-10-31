---
name: interview-extraction
description: Converts a single interview transcript into a lossless, structured extraction that downstream synthesis can rely on. Triggers when the user says "extract this transcript", "process an interview", "structured extraction from transcript", "lossless interview extraction", or "convert transcript to extraction". Operates on one interviewee at a time and emits a normalized markdown artifact with traceable evidence, per-action process cards, and SWOT-relevant signals captured but not yet synthesized.
version: 0.1.0
---

# Interview Extraction

## Purpose

Turn one raw interview transcript into a single, structured, lossless extraction document. The extraction is the canonical record of what one interviewee said and how they work. Every downstream step in this plugin (action manifest building, cross-interview synthesis, SOP drafting, SWOT analysis) reads extractions, never raw transcripts. The extraction must therefore preserve the interviewee's evidence with enough fidelity that no future step needs to re-open the transcript.

This skill produces the extraction. It does not compare interviewees, propose standards, or recommend changes.

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

These rules apply to every step of this skill. The canonical version lives at `${CLAUDE_PLUGIN_ROOT}/CONTROLLER.md`; treat that file as the source of truth if the two ever drift.

1. **Read files before acting.** Open the transcript and any referenced inputs in full before writing the extraction.
2. **Preserve evidence traceability to source interviews.** Every claim points back to a quote, timestamp, or section marker.
3. **Prefer best scalable practice, not best individual practice.** When tagging standardization candidates, consider whether the practice generalizes — not just whether this person does it well.
4. **Mark ambiguity explicitly; do not invent source material.** Use "Not stated" liberally. Never fabricate quotes, metrics, tool names, or process steps.
5. **Distinguish source-grounded fact from reasonable inference from recommendation.** Section 10 splits fact from inference. This skill never produces recommendations — those belong to later skills.
6. **Do not flatten useful role-specific differences.** If two interviewees do "the same" thing differently and the difference matters, that difference belongs in their respective extractions exactly as stated.

## Output location and naming

Write the extraction as a single markdown file. Use a stable, predictable filename so downstream skills can find it: `<interviewee-label>-extraction.md`, all lowercase, hyphenated. Place it alongside the project's other extractions (the user supplies the directory).

Confirm the path with the user once before writing if more than one plausible location exists.

## Hand-off to the next skill

After writing this extraction, check whether extractions now exist for ALL planned interviewees on this project.

- If YES: invoke `cross-interview-synthesis` to begin comparing across people. Pass the directory containing the full set of extractions.
- If NO: report which interviewees still need extractions and stop. Do not begin synthesis with a partial set.

Do not attempt to synthesize, draft SOPs, or build the action manifest from inside this skill. Those are downstream and depend on the full extraction set.
