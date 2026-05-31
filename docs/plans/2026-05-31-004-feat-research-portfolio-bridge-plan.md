---
title: feat: Research Agent & Portfolio Bridge
type: feat
status: active
date: 2026-05-31
---

# Research Agent & Portfolio Bridge

## Overview

Bridge the gap between the Research agent's knowledge base (in `~/.openclaw/workspace-research/`) and the live Kairon portfolio. Since the Research agent operates under strict `SOUL.md` boundaries (no ghostwriting, no file modification outside its workspace, no package installs), it cannot maintain the portfolio directly. Instead, it must act as an auditor and structurer, using a cross-reference loop and an outbox handoff pattern.

## Problem Frame

The Research agent understands Alejandro's Substack essays and Obsidian vault but lacks awareness of how the portfolio presents his work. To properly suggest where new essays fit within the portfolio's "theses", the agent needs a safe, automated way to read the portfolio's state and propose structural updates without breaking its `SOUL.md` constraints or the portfolio's CMS.

## Requirements Trace

- R1. The Research agent must understand the portfolio's architecture, including its Sveltia CMS schemas and file structures.
- R2. The Research agent must be able to read the live portfolio's content state to perform gap analysis against the Obsidian vault.
- R3. The Research agent must be able to propose changes to the portfolio (like adding a link to a newly published essay) without directly running build scripts, editing the repo, or executing commands.

## Scope Boundaries

- The Research agent will NOT execute `npm run build`, `npm install`, or any terminal commands within the portfolio repository.
- The Research agent will NOT directly commit changes to the portfolio repository.

## Context & Research

### Relevant Code and Patterns

- `my-portfolio/CONTENT_ARCHITECTURE.md`: Defines the source of truth for the portfolio.
- `my-portfolio/agent/README.md`: Governs how agents interact with the portfolio.
- `~/.openclaw/workspace-research/SOUL.md`: Imposes hard restrictions on the Research agent's execution abilities.

## Key Technical Decisions

- **Outbox Handover:** The Research agent will not edit the portfolio directly. It will drop formatted YAML or Markdown proposals into `shared/outbox/staged-research/` for Alejandro or the coding agent (OpenCode) to apply.
- **`llms-full.txt` Ingestion:** The portfolio's build output (`llms-full.txt`) will be synced to the Research agent's brain (`pending/vault/portfolio-state.md`) to provide the live source of truth.

## Implementation Units

- [ ] **Unit 1: Ingest Portfolio Architecture into Research Brain**

**Goal:** Teach the Research agent how the portfolio works.

**Files:**
- Create: `~/.openclaw/workspace-research/research-brain/_ingest/portfolio-architecture.md`

**Approach:**
- Consolidate `AGENTS.md` and `CONTENT_ARCHITECTURE.md` into a single reference document.
- Place it in the Research agent's `_ingest/` folder.

**Test scenarios:**
- Test expectation: none -- pure knowledge ingestion setup.

- [ ] **Unit 2: Automate Portfolio State Sync**

**Goal:** Keep the Research agent aware of the live portfolio state.

**Files:**
- Create: `scripts/sync-portfolio-state.sh` (or integrate into an existing cron)

**Approach:**
- Fetch `https://kairon.xyz/llms-full.txt` (or copy from the local `dist/`) and write it to `~/.openclaw/workspace-research/research-brain/pending/vault/portfolio-state.md` so the Research agent's Qdrant sync picks it up.

**Test scenarios:**
- Test expectation: none -- scripting automation task.

- [ ] **Unit 3: Define Outbox Proposal Format**

**Goal:** Standardize how the Research agent requests portfolio updates.

**Files:**
- Modify: `~/.openclaw/workspace-research/research-brain/protocols/PORTFOLIO-MAINTENANCE.md`

**Approach:**
- Define a template for the Research agent to use when an essay is published. The template should include the target `slug`, the new `links[]` entry, and the rationale. This ensures handoffs to the coding agent are perfectly formatted.

**Test scenarios:**
- Test expectation: none -- documentation update.

## System-Wide Impact

- **Integration coverage:** Bridges the gap between the isolated Research agent environment and the deployment-ready portfolio environment via a safe `shared/outbox` integration.

## Documentation / Operational Notes

- `agent/README.md` and `AGENTS.md` in the portfolio have already been updated to clarify the Research agent's specific constraints and read-only / outbox role.