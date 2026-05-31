# PORTFOLIO-WRITE-GUARD-01

**Status:** Active
**Applies to:** Any agent contributing to `K41R0N/k41r0n.github.io`
**Pattern source:** Modeled on `SHARED-INFRA-WRITE-GUARD-01` from the research
brain. If you already obey that guard, this is the same forcing function applied
to this repository's break-the-CMS paths.

---

## Why this exists

This repo has a generated CMS config and a build pipeline that *fails closed*. A
careless write to the wrong file does one of three things: makes the `/admin`
editor unusable for Alejandro, silently deletes content on the next CMS save, or
breaks the Vercel deploy. None of these surface as an obvious error at the moment
you make them — they surface later, to Alejandro. That delay is exactly why a
forcing function is needed.

The trap is the same "clarity-as-permission" error named in
`SHARED-INFRA-WRITE-GUARD-01`: understanding *what* should change feels like
permission to change it. It is not. On guarded paths, understanding is the moment
you are most likely to act without approval, not least.

---

## The three tiers

### Tier 0 — Never write (generated; your change is destroyed on next build)

- `dist/**` — wiped and regenerated every build.
- `admin/config.yml` — regenerated from the template every build.

If you believe one of these is wrong, the cause is upstream. Fix the **source**
(a `content/` file, the template, or `build.js`) — never the artifact. Writing
here is not "guarded," it is simply pointless; flag it and stop.

### Tier 1 — Guarded (requires the forcing function below before writing)

These can break the CMS, the build, or the deploy. Propose first, wait for
explicit approval, then write.

**CMS schema & entry**
- `admin/config.template.yml` — the Sveltia schema. Changing field names,
  removing fields, or changing `file:`/`folder:` paths breaks the editor or
  causes silent content loss.
- `admin/index.html` — the CMS entry point.

**Build pipeline**
- `scripts/build.js`
- `scripts/generate-cms-config.js`
- `scripts/validate-content.js`

**Deploy & dependency config**
- `vercel.json`
- `package.json`, `package-lock.json`
- `server.py`

**Design token contract**
- `src/css/tokens.css` — you may change token *values*; you may **not** rename or
  remove token variables (the rest of the CSS references them by name). A rename
  is a Tier 1 write.

**Identity-critical settings**
- The `backend`, `base_url`, and `repo` lines in `admin/config.template.yml`
  (the GitHub repo and the Cloudflare auth worker). Breaking these logs Alejandro
  out of his own CMS.

If you are unsure whether a path is Tier 1, **treat it as Tier 1.**

### Tier 2 — Free to edit (no forcing function; build + verify is enough)

Content. This is where contribution normally happens.

- `content/settings/site.json` — edit values (keep all validator-required keys).
- `content/about.md` — body only, **no frontmatter**.
- `content/home.json`, `content/writing.json`
- `content/theses/*.md`
- `content/blog/*.md`
- `content/pages/about.md`
- `src/assets/images/**` — new media.
- Anything inside `agent/`, `docs/` — documentation.

Tier 2 still requires: valid schema (see `guidelines/content-schemas.md`),
a successful `npm run build`, and verification (see `skills/build-and-verify.md`).

---

## The forcing function (Tier 1 writes)

Before writing to any Tier 1 path, emit this **exact line** as the next line of
your response, then stop and wait for explicit approval in the next turn:

```
PROPOSING PORTFOLIO WRITE: <path> | reason: <one sentence> | blast radius: <CMS / build / deploy / design> | awaiting approval.
```

Approval is valid only when Alejandro replies in the next turn and explicitly
approves the specific path you named. A generic "yes," a remembered past
approval, or approval for a different path does not count. If conditions are not
met, ask again. If you start to emit the line and then continue with the write in
the same turn, you have violated this guard.

## Investigation / write split

If you are asked to *investigate* ("why is the CMS broken?", "what controls the
footer?", "check the build"), your response is a **report**: read-only operations
only (`Read`, `grep`, `git log/diff/status`, `npm run build` to a clean tree to
reproduce, `cat dist/...` to inspect output). If you spot a fix on a Tier 1 path,
**surface it as a `PROPOSING PORTFOLIO WRITE` line at the end of the report** —
do not execute it in the same turn.

---

## Self-test (answer before any Tier 1 work)

1. What exact line must you emit before editing `admin/config.template.yml`?
2. The home page footer shows the wrong name. Is editing `dist/index.html` ever
   the right fix? (No — fix `content/settings/site.json`, rebuild.)
3. You want to remove an unused field from the CMS schema. Tier? (Tier 1 — a
   field present in a content file but absent from the schema is stripped on the
   next CMS save. Propose first.)
4. You are adding a blog post. Tier? (Tier 2 — edit `content/blog/`, build,
   verify, ship.)
5. Approval was given yesterday to edit `scripts/build.js`. Valid for editing it
   today? (No — approval is per-path, per-turn.)
