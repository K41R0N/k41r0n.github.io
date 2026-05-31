# Narrative Auditor: Portfolio State Sync & Drift Analysis

## Overview

The Research Agent runs on the G14 and possesses deep knowledge of Alejandro's daily writing, Substack drafts, and Obsidian vault state. The portfolio site (`K41R0N/k41r0n.github.io`) represents the public-facing "narrative" and structure of his theses. 

Because the Research agent operates under strict `SOUL.md` read-only and no-execution boundaries regarding the portfolio, it cannot build the site or execute file modifications outside its workspace. 

This spec defines a **Narrative Auditor** workflow. It bridges the gap by allowing the Research agent to ingest the public portfolio state, run a "drift analysis" against the Obsidian vault, and propose non-destructive structural updates through a structured outbox.

## Workflow Mechanics

### 1. Ingesting Portfolio State
The portfolio automatically generates an `llms-full.txt` endpoint during `npm run build`. This document contains the entire public narrative, including thesis structures, project metadata, and published blog posts.

**Action:**
A cron job (or an openclaw `store_context.py` execution) will fetch `https://kairon.xyz/llms-full.txt` (or the local `dist/llms-full.txt`) and save it to the Research agent's brain:
`~/.openclaw/workspace-research/research-brain/pending/vault/portfolio-state.md`

When the Qdrant sync runs, this file is ingested into the `research` Qdrant collection, giving the agent real-time visibility into the public narrative.

### 2. Executing Drift Analysis
When Alejandro publishes a new essay or finishes a new tool, or on a recurring weekly schedule, the Research agent executes a Narrative Audit:

1. **Compare Vault vs. Portfolio:** It queries the `obsidian_vault` collection for recent themes and compares them against the `portfolio-state.md` in its brain.
2. **Detect Drift:** If Alejandro's recent essays indicate a shift in his thinking (e.g., from "Open Source" to "Agent-Native Manufacturing"), the agent flags this as narrative drift.
3. **Map New Artifacts:** If a new artifact (essay or project) exists, the agent determines which of the three existing portfolio theses it supports best.

### 3. Outbox Handover (The "No Execution" Boundary)
The Research agent **must not** modify the `content/` folder of the portfolio repository. It operates on an "advise and propose" model.

**Action:**
When the Research agent wants to propose a portfolio update (such as linking a new essay to a thesis or tweaking the wording in `about.md`), it generates a Markdown proposal and writes it to the shared outbox:
`~/.openclaw/shared/outbox/staged-research/portfolio-update-{date}.md`

#### Outbox Proposal Format

The proposal must follow this exact format so that Alejandro or a coding agent (OpenCode) can apply it frictionlessly:

```markdown
## Narrative Audit Proposal: [Date]

**Drift Detected:** [Brief explanation of why the portfolio needs an update based on recent Obsidian notes or published work.]

### Proposed Action 1: Add Link to Thesis

**Target Thesis Slug:** `devices-as-co-creations`

**YAML to append to `links[]`:**
\`\`\`yaml
  - label: "Article"
    title: "[Exact Title of New Essay]"
    url: "[Exact URL]"
\`\`\`

### Proposed Action 2: Update About Copy (If applicable)

**Target File:** `content/about.md`

**Proposed Body:**
\`\`\`markdown
I'm in tech.
I care about craftsmanship.
[New proposed line reflecting recent narrative drift].
I don't like buzzwords.
\`\`\`
```

## Implementation Roadmap (For Coding Agents)

1. **Configure the Sync:** Set up a lightweight bash script or n8n workflow to curl `llms-full.txt` and drop it into `~/.openclaw/workspace-research/research-brain/pending/vault/portfolio-state.md`.
2. **Load into Qdrant:** Ensure the `research_brain_sync.py` script picks up this new file during its regular cycle.
3. **Prompt the Agent:** Introduce this spec to the Research agent so it knows its new recurring task and exactly how to format the outbox proposals.