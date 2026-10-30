#!/usr/bin/env node

/**
 * Kairon Portfolio — Content Validation
 * Validates content/settings/site.json and content/theses/*.md
 * before the main build runs.
 */

import fs from 'fs';
import path from 'path';
import matter from 'gray-matter';

const ROOT    = process.cwd();
const CONTENT = path.join(ROOT, 'content');

let errors = 0;

function fail(msg) {
  console.error(`  ✗ ${msg}`);
  errors++;
}

function ok(msg) {
  console.log(`  ✓ ${msg}`);
}

// ---- Settings ---------------------------------------------------------------
const settingsPath = path.join(CONTENT, 'settings', 'site.json');
if (!fs.existsSync(settingsPath)) {
  fail('content/settings/site.json not found');
} else {
  const s = JSON.parse(fs.readFileSync(settingsPath, 'utf-8'));
  for (const field of ['title', 'full_name', 'description', 'author', 'email', 'github', 'substack', 'site_url']) {
    if (!s[field]) fail(`settings.${field} is required`);
  }
  ok('site.json');
}

// ---- Theses -----------------------------------------------------------------
const thesesDir = path.join(CONTENT, 'theses');
if (!fs.existsSync(thesesDir)) {
  fail('content/theses/ directory not found');
} else {
  const files = fs.readdirSync(thesesDir).filter(f => f.endsWith('.md'));
  if (files.length === 0) fail('No thesis files found in content/theses/');

  const seenSlugs  = new Set();
  const seenOrders = new Set();

  for (const file of files) {
    const { data } = matter(fs.readFileSync(path.join(thesesDir, file), 'utf-8'));
    const id = file;

    if (!data.title)       fail(`${id}: missing required field "title"`);
    if (!data.slug)        fail(`${id}: missing required field "slug"`);
    if (!data.description) fail(`${id}: missing required field "description"`);
    if (data.order == null) fail(`${id}: missing required field "order"`);

    if (data.slug && !/^[a-z0-9-]+$/.test(data.slug))
      fail(`${id}: slug "${data.slug}" must match ^[a-z0-9-]+$`);

    if (data.slug && seenSlugs.has(data.slug))
      fail(`${id}: duplicate slug "${data.slug}"`);
    else if (data.slug) seenSlugs.add(data.slug);

    if (data.order != null && seenOrders.has(data.order))
      fail(`${id}: duplicate order ${data.order}`);
    else if (data.order != null) seenOrders.add(data.order);

    if (errors === 0) ok(file);
  }
}

// ---- Projects ---------------------------------------------------------------
const projectsDir = path.join(CONTENT, 'projects');
if (fs.existsSync(projectsDir)) {
  const files = fs.readdirSync(projectsDir).filter(f => f.endsWith('.md'));

  const seenSlugs  = new Set();
  const seenOrders = new Set();

  for (const file of files) {
    const { data } = matter(fs.readFileSync(path.join(projectsDir, file), 'utf-8'));
    const id = `projects/${file}`;

    const title = data.title || file.replace(/\.md$/, '');
    const slug = data.slug || String(title).toLowerCase().replace(/[^a-z0-9\s-]/g, '').replace(/\s+/g, '-').replace(/-+/g, '-').replace(/^-|-$/g, '');
    const order = data.order;

    if (!slug) fail(`${id}: resulting slug is empty`);
    if (!/^[a-z0-9-]+$/.test(slug)) fail(`${id}: slug "${slug}" must match ^[a-z0-9-]+$`);

    if (seenSlugs.has(slug)) fail(`${id}: duplicate slug "${slug}"`);
    else seenSlugs.add(slug);

    if (order === undefined || order === null || !Number.isFinite(order) || !Number.isInteger(order)) {
      fail(`${id}: order must be a numeric integer`);
    } else if (seenOrders.has(order)) {
      fail(`${id}: duplicate order "${order}"`);
    } else {
      seenOrders.add(order);
    }

    if (errors === 0) ok(file);
  }
}


// ---- Editor markers (no unreplaced placeholders in content) ------------------
// Fails the build if any content file carries an unreplaced editor marker:
// [ALEJANDRO: ...], [TODO], [TBD], [FIXME], [PLACEHOLDER], or any bracketed
// ALL-CAPS note. Notes to Alejandro belong in the PR description, never in
// rendered content. Added 2026-10-29 after a placeholder reached a preview.
const MARKER_PATTERNS = [
  /\[ALEJANDRO[^\]]*\]/i,
  /\[(TODO|TBD|FIXME|PLACEHOLDER)[^\]]*\]/i,
  /\[[A-Z][A-Z0-9 :_,.'-]{3,}\]/,
];
function scanForMarkers(dir) {
  if (!fs.existsSync(dir)) return;
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    const p = path.join(dir, e.name);
    if (e.isDirectory()) { scanForMarkers(p); continue; }
    if (!/\.(md|json)$/.test(e.name)) continue;
    const text = fs.readFileSync(p, 'utf-8');
    for (const re of MARKER_PATTERNS) {
      const m = text.match(re);
      if (m) fail(`${path.relative(CONTENT, p)}: unreplaced editor marker "${m[0].slice(0, 60)}" - notes to Alejandro belong in the PR description, not in content`);
    }
  }
}
scanForMarkers(CONTENT);
if (errors === 0) ok('editor markers');


// ---- Public-register check (no buzzwords in public-facing copy) --------------
// Standing rule (Alejandro, WhatsApp 2026-10-29): nothing public-facing carries
// meta commentary or buzzwords. List seeded from the documented voice work
// (agent/voice/tools/checks.py: BANNED_AI, SOFT, FALSE_DEPTH), NOT invented.
// 'harness' is deliberately excluded: it is his term of art for his core work.
// Scope: public copy files agents edit. His published prose (blog/, theses/)
// is excluded - it is owner-authored. The 8 legacy project pages predate this
// rule and are exempt BY NAME until rewritten; any new or renamed file is
// checked. Exempt list reviewed at every upkeep cycle.
const BUZZ_WORDS = ['seamless','seamlessly','robust','unlock','leverage','leveraging','utilize','utilise','empower','streamline','delve','tapestry','realm','pivotal','crucial','testament','landmark','foster','elevate','bolster','underscore','underscores','underscoring'];
const BUZZ_PHRASES = ['in essence','essentially',"it's worth noting","it’s worth noting",'at the end of the day',"it's important to note","it’s important to note","in today's fast-paced","in today’s fast-paced",'at its core','the real question is',"here's the thing","here’s the thing","let's dive in","let’s dive in"];
const BUZZ_EXEMPT = new Set([
  'projects/threadbot.md','projects/notion-as-cms.md','projects/uh-vibe-checker.md',
  'projects/rm-quickshare-bot.md','projects/notion-telegram-bot.md',
  'projects/opensource-curriculum.md','projects/interactive-quiz-maker.md',
  'projects/openclaw-personal-infrastructure.md',
]);
const BUZZ_SKIP_DIRS = new Set(['blog','theses']);
const buzzRe = new RegExp('\\b(' + BUZZ_WORDS.join('|') + ')\\b', 'i');
function scanForBuzz(dir) {
  if (!fs.existsSync(dir)) return;
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    const p = path.join(dir, e.name);
    if (e.isDirectory()) { if (!BUZZ_SKIP_DIRS.has(e.name)) scanForBuzz(p); continue; }
    if (!/\.(md|json)$/.test(e.name)) continue;
    const rel = path.relative(CONTENT, p);
    if (BUZZ_EXEMPT.has(rel)) continue;
    const text = fs.readFileSync(p, 'utf-8');
    const w = text.match(buzzRe);
    if (w) fail(`${rel}: buzzword-register word "${w[0]}" (standing rule 2026-10-29: no buzzwords in public-facing copy)`);
    const lower = text.toLowerCase();
    for (const ph of BUZZ_PHRASES) {
      if (lower.includes(ph)) fail(`${rel}: buzzword-register phrase "${ph}"`);
    }
  }
}
scanForBuzz(CONTENT);
if (errors === 0) ok('public register');

// ---- Result -----------------------------------------------------------------
if (errors > 0) {
  console.error(`\nValidation failed with ${errors} error(s).`);
  process.exit(1);
} else {
  console.log('\nContent validation passed.');
}
