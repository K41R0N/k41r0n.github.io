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

// ---- Result -----------------------------------------------------------------
if (errors > 0) {
  console.error(`\nValidation failed with ${errors} error(s).`);
  process.exit(1);
} else {
  console.log('\nContent validation passed.');
}
