#!/usr/bin/env node
/**
 * update-activity.js — refresh content/projects/<slug>.activity.json from the
 * public GitHub API. Plain data only: dates, commit subjects, commit URLs.
 * No prose, no commentary. Pages render the section only when the file exists.
 *
 * Usage: node scripts/update-activity.js
 */
import fs   from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

const CONTENT = path.join(__dirname, '..', 'content', 'projects');

// project-page slug -> public GitHub repo (public repos only; private work
// never appears on the site unless Alejandro says otherwise)
const REPOS = {
  'meal-planner':                     'meal-planner',
  'threadbot':                        'threadbot',
  'notion-telegram-bot':              'Notion-Telegram-Bot',
  'rm-quickshare-bot':                'RM-quickshare-bot',
  'uh-vibe-checker':                  'UH-Vibe-Checker',
  'notion-as-cms':                    'Notion-as-CMS',
  'opensource-curriculum':            'opensource-curriculum',
  'interactive-quiz-maker':           'Interactive-Quiz-Maker',
};

const ENTRIES_PER_PROJECT = 5;
const FETCH_PER_PROJECT = 12; // fetch extra so filtering still yields 5

// Forward-looking filter (his rule 2026-10-29: describe what exists, never
// what is planned). Subjects matching this are dropped, never rewritten -
// rewriting his words would break the voice rule. Same standard as the
// site-wide sweep.
const FORWARD_LOOKING = /roadmap|coming soon|stay tuned|later work|in the works|upcoming|next release|planned feature|will be (available|added|launched|shipped)|work in progress|\bWIP\b/i;

function cleanSubject(message) {
  return (message || '').split('\n')[0].replace(/\s*\[skip ci\]\s*$/i, '').trim();
}

async function fetchCommits(repo) {
  const url = `https://api.github.com/repos/K41R0N/${repo}/commits?per_page=${FETCH_PER_PROJECT}`;
  const res = await fetch(url, { headers: { 'User-Agent': 'k41r0n-site-build', 'Accept': 'application/vnd.github+json' } });
  if (!res.ok) throw new Error(`${repo}: GitHub API ${res.status}`);
  const commits = await res.json();
  return commits.map(c => ({
    date:    (c.commit.committer.date || '').slice(0, 10),
    subject: cleanSubject(c.commit.message),
    url:     c.html_url,
  }))
  .filter(e => e.date && e.subject && e.url)
  .filter(e => !FORWARD_LOOKING.test(e.subject))
  .slice(0, ENTRIES_PER_PROJECT);
}

(async () => {
  const today = new Date().toISOString().slice(0, 10);
  for (const [slug, repo] of Object.entries(REPOS)) {
    try {
      const entries = await fetchCommits(repo);
      if (!entries.length) { console.log(`${slug}: no commits, skipped`); continue; }
      const file = path.join(CONTENT, `${slug}.activity.json`);
      fs.writeFileSync(file, JSON.stringify({ updated: today, entries }, null, 2) + '\n');
      console.log(`${slug}: ${entries.length} entries`);
    } catch (e) {
      console.log(`${slug}: ${e.message}, skipped`);
    }
  }
})();
