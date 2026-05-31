---
title: "Ghost CMS evaluated and rejected — staying on Sveltia + Vercel"
date: 2026-05-31
category: docs/solutions/best-practices
module: cms-architecture
problem_type: best_practice
component: tooling
severity: low
applies_when:
  - Evaluating a CMS migration for this portfolio
  - Considering Ghost CMS for any agent-driven static site
tags:
  - ghost
  - cms
  - sveltia
  - decision-record
  - agent-native
  - do-not-revisit
---

# Ghost CMS evaluated and rejected — staying on Sveltia + Vercel

## Decision

**Ghost CMS will not be used for kairon.xyz. Sveltia + Vercel is the permanent CMS stack.**

Do not re-open this question without a materially different set of requirements.

## What Was Evaluated

Ghost OSS (v6.43.2) was evaluated as a replacement for Sveltia CMS. The evaluation included:
- Cloning and reading the Ghost monorepo (`/tmp/ghost-repo`)
- Cloning the Casper reference theme (`/tmp/casper-theme`)
- Researching Ghost hosting options (Railway, Render, VPS, Ghost Pro, G14 self-host)
- Researching Paragraph cross-posting and Substack syndication mechanics
- A full implementation plan (`docs/plans/2026-05-31-002-feat-ghost-migration-blog-syndication-plan.md`)

## Why Ghost Was Rejected

### 1. Wrong tool for an agent-driven site

The primary content updater is a Research agent running on the G14 via OpenClaw. Agents update content by writing markdown files and committing to Git — that is their natural tool set. Ghost's update path requires:
- Ghost Admin API calls with authentication
- Content formatted as Lexical JSON (Ghost's proprietary editor format, not markdown)
- Separate image upload API calls
- Session/token management

Sveltia is a Git-based CMS. The agent's natural workflow (write file → git push) *is* the CMS workflow. They are the same operation. Ghost would be 4× more complex with zero editorial benefit to the agent.

### 2. Infrastructure overhead with no return

Ghost requires a persistent Node.js server + database + file system for uploads. Every hosting option adds cost and complexity:
- **G14 self-host**: Site goes down during G14 maintenance, power blips, or kernel panics. Unacceptable for a lead-generation portfolio.
- **Railway / Render**: ~$5–15/month for a service Vercel already covers for free.
- **Ghost Pro**: $9–25/month for managed hosting of a tool that adds no value in this stack.

Vercel static hosting has effectively zero downtime. A home server or PaaS container does not.

### 3. Every Ghost feature is already covered

| Ghost feature | What we use instead |
|---|---|
| Writing editor | Sveltia + markdown (agents write markdown natively) |
| RSS feed | Already exists at `/feed.xml` |
| `post.published` webhook | n8n on G14 polls RSS for new entries |
| Newsletter | Substack — not moving |
| Membership/paywalls | Not in scope |
| Headless Content API | Agents read markdown files from Git directly |

### 4. The G14 is not a web server

The G14 is the always-on OpenClaw brain. Its services (Ollama, Qdrant, n8n, PostgreSQL) are inference and coordination infrastructure. Adding Ghost as a production web server introduces failure coupling: if Ghost crashes or needs a restart, it could interfere with inference availability. The G14's role is agent infrastructure, not website hosting.

## What We Use Instead

- **CMS**: Sveltia (Git-based, browser UI, commits to GitHub)
- **Hosting**: Vercel (static, CDN-backed, zero-downtime)
- **Blog**: `content/blog/*.md` collection in Sveltia, rendered by the existing build script
- **Paragraph syndication**: RSS import (set-and-forget, already supported by `/feed.xml`)
- **Substack notification**: n8n workflow on G14 polling RSS for new entries
- **Agent editing**: Research agent clones repo on G14, writes markdown, pushes via GitHub fine-grained PAT

## Related

- Superseded plan: `docs/plans/2026-05-31-002-feat-ghost-migration-blog-syndication-plan.md`
- Active plan: `docs/plans/2026-05-31-003-feat-blog-syndication-agent-native-plan.md`
- CMS schema patterns: `docs/solutions/best-practices/sveltia-cms-schema-completeness-2026-05-31.md`
