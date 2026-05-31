# Multi-Channel Syndication Spec

**Task #301** | Generated 2026-05-31

## Objective

Define a repeatable system for publishing a single Device Economies essay across Substack, Paragraph, and Ghost CMS — with canonical content management, platform-appropriate formatting, and subscriber base preservation.

## Platforms in Scope

| Platform | Status | Subscribers | Role |
|----------|--------|-------------|------|
| **Substack** | Live (k41r0n.substack.com) | 4,000+ | Primary audience + discovery. Email-native, comments, Notes. |
| **Paragraph** | Live (paragraph.com/@kairon-2) | Unknown (smaller) | Archive continuity from Mirror era. Web-native, less engagement surface. |
| **Ghost CMS** | Not deployed | 0 | Future home. Self-hosted, full control, membership/subscriptions, API for automation. |

## Core Design Decisions

### 1. Canonical source of truth = Obsidian

All writing happens in Obsidian. The markdown file in `Device Economies/Articles/` is the single source. Formatting, footnotes, links, corrections all happen there. Each platform pulls a derivative.

### 2. One platform is the "primary" per essay

Each essay designates a primary platform — usually Substack for new essays, Paragraph for migrated Mirror-era pieces. The primary gets published first and receives corrections first. Others syndicate after.

Rationale: simultaneous cross-posting creates SEO confusion, broken comment threads, and no clear canonical URL.

### 3. Ghost is the eventual home — timing is the decision

Ghost architecture assumes it's the canonical hub with syndication outbound. That requires:
- Ghost instance deployed and configured
- Obsidian-to-Ghost publish pipeline (API or webhook)
- Ghost membership/subscriptions active
- RSS → Substack import for newsletter (or dual-list management)

Until Ghost is ready, Substack remains primary and Paragraph is an archive mirror.

## Proposed Architecture (Pre-Ghost)

```
Obsidian (canonical)
  ├─→ Substack (primary publication) — email, discovery, comments, Notes
  │     ├─ native editor paste from markdown
  │     └─ link back from Substack post → Paragraph version
  └─→ Paragraph (archive mirror) — Mirror-era continuity, SEO, permalink
        └─ manual paste or API
```

Post-Ghost:

```
Obsidian (canonical)
  └─→ Ghost (canonical publication) — membership, API, RSS
        ├─→ Substack (syndicate) — email list via RSS or import
        └─→ Paragraph (syndicate) — cross-post or embed
```

## Per-Platform Formatting Notes

| Feature | Substack | Paragraph | Ghost |
|---------|----------|-----------|-------|
| Footnotes | Inline or manual | Inline | Markdown footnotes |
| Images | Upload to CDN | Upload | Markdown + CDN |
| Blockquotes | Native | Native | Markdown |
| Embeds (tweet, video) | Native | Limited | Markdown + HTML |
| Code blocks | Triple backtick | Triple backtick | Triple backtick |
| Newsletter sync | Built-in | None native | API or Sendmail |
| Series/sections | Sections feature | Manual | Tags + nav |
| SEO metadata | Limited | Limited | Full control |

## Workflow Sketch

1. **Write** in Obsidian until final draft
2. **Format for Substack** — apply Substack-specific formatting (manual footnotes, embedded media, section breaks)
3. **Publish to Substack** — send to email list, enable comments/Notes
4. **After 24-48 hours** — syndicate to Paragraph with canonical link back
5. **Collect engagement** — top comments and Notes responses inform next essay
6. **Archive** — update Obsidian with published links, store Substack email metrics
7. **(Future) Ghost** — when deployed, Substack becomes syndicate target, Ghost becomes hub

## Open Questions

1. **Ghost deployment timeline** — self-hosted (docker/podman) or Ghost(Pro)? When does it make sense to invest the infra time vs. staying on Substack?
2. **Paragraph relationship** — does Paragraph offer an API? Or is syndication always manual paste? Worth investigating.
3. **RSS as syndication bridge** — Substack RSS feeds can be consumed by other platforms. Can Ghost import Substack RSS for archive purposes? Can Paragraph?
4. **Cross-post timing** — should there be a delay between platforms? SEO-first approach suggests primary gets 48h head start.
5. **Subscriber base migration** — when Ghost arrives, do Substack subscribers migrate or do we run both lists? Substack allows email export.

## Next Steps

1. Evaluate Ghost deployment effort (docker-compose on G14 vs Ghost(Pro) at ~$25/mo)
2. Investigate Paragraph API capabilities
3. Test Obsidian → Substack → Paragraph round trip with one existing essay
4. Decide on Ghost timing based on #1
5. Turn approved spec into checklist/protocol for repeatable syndication
