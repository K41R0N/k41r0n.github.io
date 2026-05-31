# agent/ — Contributor Brain for the Kairon Portfolio

This folder is the **entry point for any AI agent** (primarily the Device
Economies **Research agent**) that contributes to this repository. It teaches an
agent how the site is built, what is safe to touch, what will break the CMS, and
how to lay down live components later without regressing the publishing pipeline.

If you are an agent reading this for the first time, **read `ORIENTATION.md`
next**, then consult the routing table below for the specific task in front of
you. Do not edit files outside `content/` until you have read
`protocols/PORTFOLIO-WRITE-GUARD-01.md`.

---

## Lookup Order (mirrors the research brain's memory hierarchy)

1. **This folder first** — `agent/` is authoritative for *how to contribute*.
   Use the routing table below to find the right file.
2. **Repo root docs second** — `AGENTS.md`, `CONTENT_ARCHITECTURE.md`,
   `docs/solutions/` hold deeper reference material.
3. **Ask Alejandro third** — if neither has the answer, report what you found
   and ask. Do not improvise on guarded paths.

---

## Routing Table

| If you need to… | Read |
|---|---|
| Understand how the whole site works | `ORIENTATION.md` |
| Know exactly what you may and may not edit | `protocols/PORTFOLIO-WRITE-GUARD-01.md` |
| Make any content edit safely, end-to-end | `protocols/PORTFOLIO-CONTENT-EDIT-01.md` |
| Publish a new blog post / essay | `skills/add-blog-post.md` |
| Add or edit a thesis | `skills/add-thesis.md` |
| Change site-wide settings (name, links, SEO) | `skills/edit-site-settings.md` |
| Change home-page section headings / newsletter copy | `skills/edit-home-sections.md` |
| Expose a NEW field to the CMS without breaking it | `skills/add-configurable-field.md` |
| Build the site and verify nothing broke | `skills/build-and-verify.md` |
| Understand the content→build→deploy architecture | `guidelines/repo-architecture.md` |
| Understand CMS invariants (do not break Sveltia) | `guidelines/cms-safety.md` |
| Look up a frontmatter / settings schema | `guidelines/content-schemas.md` |
| Know how to branch, commit, and ship | `guidelines/contribution-workflow.md` |
| Plan future "live component" automation | `automation/live-components-foundations.md` |

---

## The One Rule That Prevents Most Breakage

**Content is the source of truth. You edit `content/`, you run `npm run build`,
you verify, you ship. You never hand-edit `dist/` or `admin/config.yml` — those
are generated.** Everything else in this folder is an elaboration of that rule.

---

## Scope

- **Primary audience:** the Research agent, contributing edits via git and,
  later, via automation flows that add live components to the site.
- **Boundary:** this folder governs contributions to *this repository only*. It
  does not grant any agent permission to write to the research brain, Qdrant,
  or any other agent's workspace. Those are governed by the agent's own
  boot files and `SHARED-INFRA-WRITE-GUARD-01`.
- **Voice boundary still applies:** the Research agent supports writing; it does
  not ghostwrite Alejandro's essays. Publishing prose is a human decision. See
  `guidelines/contribution-workflow.md`.
