#!/usr/bin/env node

/**
 * Kairon Portfolio — Build Script
 *
 * Layout language: editorial layout grammar.
 * Colour palette: Kairon crimson #bf150f.
 *
 * Outputs:
 *   dist/index.html                      — home  (ms-main, masthead, intro-flow, toc-ms)
 *   dist/thesis-NN-[slug].html           — thesis detail pages (chapter-page layout)
 *   dist/llms.txt · llms-full.txt        — AI agent guidance
 *   dist/api/content.json                — structured JSON API
 *   dist/sitemap.xml · feed.xml          — SEO
 *   dist/robots.txt                      — AI crawler allowances
 */

import fs   from 'fs';
import path from 'path';
import matter from 'gray-matter';
import { marked } from 'marked';

const ROOT    = process.cwd();
const DIST    = path.join(ROOT, 'dist');
const CONTENT = path.join(ROOT, 'content');
const SRC     = path.join(ROOT, 'src');
const ASSETS  = path.join(SRC, 'assets');

// Ensure SITE_URL always has a protocol — Vercel env vars are sometimes set without https://
const _rawSiteUrl = process.env.PUBLIC_SITE_URL || 'https://kairon.xyz';
const SITE_URL    = (_rawSiteUrl.startsWith('http') ? _rawSiteUrl : `https://${_rawSiteUrl}`).replace(/\/$/, '');
const GSC_VERIFICATION  = process.env.GOOGLE_SITE_VERIFICATION || '';
const GA4_ID            = process.env.GA4_MEASUREMENT_ID || 'G-4E1LTHSFX8';

// ============================================================================
// Utilities
// ============================================================================

function ensureDir(dir) {
  if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });
}

function copyDir(src, dest) {
  ensureDir(dest);
  for (const e of fs.readdirSync(src, { withFileTypes: true })) {
    const s = path.join(src, e.name), d = path.join(dest, e.name);
    e.isDirectory() ? copyDir(s, d) : fs.copyFileSync(s, d);
  }
}

function slugify(text) {
  return String(text).toLowerCase()
    .replace(/[^a-z0-9\s-]/g, '').replace(/\s+/g, '-')
    .replace(/-+/g, '-').replace(/^-|-$/g, '');
}

function escHtml(str) {
  return String(str)
    .replace(/&/g, '&amp;').replace(/</g, '&lt;')
    .replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}

function toRFC822(date) { return date.toUTCString(); }

function thesisUrl(thesis) {
  return `thesis-${String(thesis.order).padStart(2,'0')}-${thesis.slug}.html`;
}

function projectUrl(project) {
  return `project-${project.slug}.html`;
}

// ============================================================================
// Content Loading
// ============================================================================

function loadSettings() {
  const p = path.join(CONTENT, 'settings', 'site.json');
  if (!fs.existsSync(p)) { console.error('Missing content/settings/site.json'); process.exit(1); }
  return JSON.parse(fs.readFileSync(p, 'utf-8'));
}

function loadAbout() {
  const p = path.join(CONTENT, 'about.md');
  if (!fs.existsSync(p)) return { body: '' };
  const { data, content } = matter(fs.readFileSync(p, 'utf-8'));
  return { ...data, body: content.trim() };
}

function loadHome() {
  const p = path.join(CONTENT, 'home.json');
  if (!fs.existsSync(p)) return {};
  return JSON.parse(fs.readFileSync(p, 'utf-8'));
}

function loadWriting() {
  const p = path.join(CONTENT, 'writing.json');
  if (!fs.existsSync(p)) return { links: [] };
  return JSON.parse(fs.readFileSync(p, 'utf-8'));
}

function loadTheses() {
  const dir = path.join(CONTENT, 'theses');
  if (!fs.existsSync(dir)) return [];
  return fs.readdirSync(dir)
    .filter(f => f.endsWith('.md'))
    .map(f => {
      const { data, content } = matter(fs.readFileSync(path.join(dir, f), 'utf-8'));
      return { ...data, body: content.trim(), filename: f };
    })
    .sort((a, b) => (a.order || 99) - (b.order || 99));
}

function loadProjects() {
  const dir = path.join(CONTENT, 'projects');
  if (!fs.existsSync(dir)) return [];
  return fs.readdirSync(dir)
    .filter(f => f.endsWith('.md'))
    .map(f => {
      const { data, content } = matter(fs.readFileSync(path.join(dir, f), 'utf-8'));
      data.title = data.title || f.replace(/\.md$/, '');
      data.slug = data.slug || slugify(data.title);
      data.order = typeof data.order === 'number' ? data.order : 99;
      return { ...data, body: content.trim(), filename: f };
    })
    .sort((a, b) => a.order - b.order);
}

function loadAboutPage() {
  const p = path.join(CONTENT, 'pages', 'about.md');
  if (!fs.existsSync(p)) return null;
  const { data, content } = matter(fs.readFileSync(p, 'utf-8'));
  return { ...data, body: content.trim() };
}

function loadBlog() {
  const dir = path.join(CONTENT, 'blog');
  if (!fs.existsSync(dir)) return [];
  return fs.readdirSync(dir)
    .filter(f => f.endsWith('.md'))
    .map(f => {
      const { data, content } = matter(fs.readFileSync(path.join(dir, f), 'utf-8'));
      return { ...data, body: content.trim(), filename: f };
    })
    // Sort newest-first by date field; fall back to filename for stability
    .sort((a, b) => {
      const da = a.date ? new Date(a.date) : new Date(0);
      const db = b.date ? new Date(b.date) : new Date(0);
      return db - da;
    });
}

// ============================================================================
// Markdown Transformations
// ============================================================================

/**
 * Apply dropcap to the first paragraph of an HTML string.
 * Guard: only fires when the paragraph opens with 3+ consecutive letters.
 * This prevents ::first-letter from splitting contractions ("I'm") or
 * lone articles ("A ") into a giant floated character.
 */
function applyDropcap(html) {
  return html.replace(/<p>([A-Za-z]{3,})/, '<p class="dropcap">$1');
}

/**
 * Transform thesis body:
 *   > **Note:** ...  →  <aside class="margin-note"><p>…</p></aside>
 *   ---              →  <hr class="section-break">
 */
function transformBody(markdown) {
  let md = markdown;
  // Margin notes: any blockquote (single or multi-line) → <aside class="margin-note">
  md = md.replace(/^(> [^\n]+(?:\n> [^\n]+)*)/gm, (match) => {
    const content = match
      .split('\n')
      .map(line => line.replace(/^> /, ''))
      .join(' ')
      .trim();
    return `<aside class="margin-note">\n  <p>${content}</p>\n</aside>`;
  });
  // section breaks
  md = md.replace(/\n---\n/g, '\n<hr class="section-break">\n');
  // parse remaining markdown, then apply guarded dropcap
  let html = applyDropcap(marked.parse(md, { async: false }));

  // Post-process img tags:
  //   1. Add loading="lazy" to all body images (hero gets loading="eager" separately)
  //   2. Request smaller versions of Substack CDN images (w_1456 → w_800)
  //      Substack's CDN supports resize params in the URL — 800px is plenty for body images
  html = html.replace(/<img([^>]*?)>/g, (tag, attrs) => {
    // Add lazy loading if no loading attribute present
    if (!attrs.includes('loading=')) attrs += ' loading="lazy"';
    // Downsize Substack CDN images from 1456px to 800px
    attrs = attrs.replace(/w_1456,c_limit/g, 'w_800,c_limit');
    return `<img${attrs}>`;
  });

  return html;
}

// ============================================================================
// Shared <head>
// ============================================================================

// Root-relative paths so CSS loads correctly from any page depth (/, /blog/, etc.)
const CSS_LINKS = `
  <link rel="stylesheet" href="/css/fonts.css">
  <link rel="stylesheet" href="/css/tokens.css">
  <link rel="stylesheet" href="/css/base.css">
  <link rel="stylesheet" href="/css/components.css">
  <link rel="stylesheet" href="/css/layout.css">
  <link rel="stylesheet" href="/css/animations.css">
  <link rel="stylesheet" href="/css/overrides.css">`.trim();

function sharedHead({ title, description, url, type = 'website', settings }) {
  return `
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>${escHtml(title)}</title>
  <meta name="description" content="${escHtml(description)}">
  <meta name="author" content="${escHtml(settings.full_name)}">
  <meta name="theme-color" content="#F5F5F5">
  <link rel="canonical" href="${url}">
  <link rel="alternate" type="application/rss+xml" title="${escHtml(settings.title)}" href="${SITE_URL}/feed.xml">
  <link rel="me" href="${escHtml(settings.github)}">
  <link rel="me" href="${escHtml(settings.substack)}">
  <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><rect width='100' height='100' fill='%23F5F5F5'/><text x='50' y='74' text-anchor='middle' font-size='68' font-family='serif' fill='%23bf150f'>K</text></svg>">
  <!-- Open Graph -->
  <meta property="og:type" content="${type}">
  <meta property="og:title" content="${escHtml(title)}">
  <meta property="og:description" content="${escHtml(description)}">
  <meta property="og:url" content="${url}">
  <meta property="og:site_name" content="${escHtml(settings.title)}">
  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary">
  <meta name="twitter:title" content="${escHtml(title)}">
  <meta name="twitter:description" content="${escHtml(description)}">
  ${GSC_VERIFICATION ? `<meta name="google-site-verification" content="${GSC_VERIFICATION}">` : ''}
  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="preload" href="/assets/fonts/AT-Kyrios-Variable.woff2" as="font" type="font/woff2" crossorigin>
  ${CSS_LINKS}
  <noscript><style>body{opacity:1!important}</style></noscript>
  <!-- Google Analytics -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=${GA4_ID}"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', '${GA4_ID}');
  </script>`.trim();
}

// ============================================================================
// Structured Data
// ============================================================================

const PERSON_ID  = `${SITE_URL}/#person`;
const WEBSITE_ID = `${SITE_URL}/#website`;

function personEntity(settings) {
  return {
    '@type': 'Person', '@id': PERSON_ID,
    name: settings.full_name, alternateName: settings.author_handle,
    url: SITE_URL, email: settings.email,
    jobTitle: settings.tagline, description: settings.description,
    sameAs: [settings.github, settings.substack, settings.instagram].filter(Boolean),
    knowsAbout: ['Creative Technology', 'Martech', 'Digital Culture',
                 'Open Source', 'Storytelling', 'Digital Discovery']
  };
}

function websiteEntity(settings) {
  return {
    '@type': 'WebSite', '@id': WEBSITE_ID,
    name: settings.title, url: `${SITE_URL}/`,
    description: settings.description, inLanguage: 'en',
    author: { '@id': PERSON_ID }
  };
}

function jsonLd(graph) {
  return `<script type="application/ld+json">\n${JSON.stringify({'@context':'https://schema.org','@graph':graph},null,2)}\n</script>`;
}

function homeSchema(settings) {
  return jsonLd([
    websiteEntity(settings),
    { '@type': 'ProfilePage', '@id': `${SITE_URL}/#page`,
      url: `${SITE_URL}/`, name: `${settings.full_name} — ${settings.tagline}`,
      description: settings.description, isPartOf: {'@id': WEBSITE_ID},
      about: {'@id': PERSON_ID}, inLanguage: 'en' },
    personEntity(settings)
  ]);
}

function thesisSchema(thesis, settings) {
  const url = `${SITE_URL}/${thesisUrl(thesis)}`;
  return jsonLd([
    { '@type': 'Article', '@id': `${url}#article`,
      headline: `${String(thesis.order).padStart(2,'0')} · ${thesis.title}`,
      description: thesis.description, url,
      isPartOf: {'@id': WEBSITE_ID}, author: {'@id': PERSON_ID},
      inLanguage: 'en',
      speakable: { '@type': 'SpeakableSpecification', cssSelector: ['.dropcap','.article h1','.eyebrow'] }
    },
    { '@type': 'BreadcrumbList',
      itemListElement: [
        { '@type': 'ListItem', position: 1, name: settings.title, item: `${SITE_URL}/` },
        { '@type': 'ListItem', position: 2, name: thesis.title, item: url }
      ]
    },
    websiteEntity(settings),
    personEntity(settings)
  ]);
}

function projectSchema(project, settings) {
  const url = `${SITE_URL}/${projectUrl(project)}`;
  
  const projectEntity = {
    '@type': ['SoftwareSourceCode', 'SoftwareApplication'],
    '@id': `${url}#project`,
    name: project.title,
    description: project.description,
    url: url,
    applicationCategory: 'DeveloperApplication',
    operatingSystem: 'Any',
    author: { '@id': PERSON_ID },
    maintainer: { '@id': PERSON_ID },
    isPartOf: {'@id': WEBSITE_ID}
  };

  if (project.repository_url) projectEntity.codeRepository = project.repository_url;
  if (project.language) projectEntity.programmingLanguage = project.language;
  if (project.license) {
    if (project.license.startsWith('http')) {
      projectEntity.license = project.license;
    } else if (project.license.toUpperCase() === 'MIT') {
      projectEntity.license = 'https://opensource.org/licenses/MIT';
    } else {
      projectEntity.license = {
        '@type': 'CreativeWork',
        'name': project.license
      };
    }
  }
  if (project.version) projectEntity.softwareVersion = project.version;

  return jsonLd([
    projectEntity,
    { '@type': 'BreadcrumbList',
      itemListElement: [
        { '@type': 'ListItem', position: 1, name: settings.title, item: `${SITE_URL}/` },
        { '@type': 'ListItem', position: 2, name: project.title, item: url }
      ]
    },
    websiteEntity(settings),
    personEntity(settings)
  ]);
}

// ============================================================================
// Home Page
// ============================================================================

function renderHomePage(settings, about, theses, projects, home, writing) {
  const title       = `${settings.full_name} — ${settings.tagline}`;
  const year        = new Date().getFullYear();
  const thesisCount = String(theses.length).padStart(2, '0');

  // Masthead right panel — social links + blog link in the live-metrics grid.
  const instagramHandle = settings.instagram ? settings.instagram.split('/').filter(Boolean).pop() : '';
  const metricsHtml = `
    <div class="live-metrics" aria-label="Social links" style="grid-template-columns:repeat(4,1fr);">
      ${settings.instagram ? `<div>
        <div class="metric-label">Instagram</div>
        <div class="metric-value" style="font-size:var(--text-lg);"><a href="${escHtml(settings.instagram)}" target="_blank" rel="noopener">${escHtml(instagramHandle)}</a></div>
      </div>` : ''}
      ${settings.github ? `<div>
        <div class="metric-label">GitHub</div>
        <div class="metric-value" style="font-size:var(--text-lg);"><a href="${escHtml(settings.github)}" target="_blank" rel="noopener">${escHtml(settings.author_handle)}</a></div>
      </div>` : ''}
      ${settings.substack ? `<div>
        <div class="metric-label">Substack</div>
        <div class="metric-value" style="font-size:var(--text-lg);"><a href="${escHtml(settings.substack)}" target="_blank" rel="noopener">${escHtml(settings.substack.replace('https://', ''))}</a></div>
      </div>` : ''}
      <div>
        <div class="metric-label">Blog</div>
        <div class="metric-value" style="font-size:var(--text-lg);"><a href="/blog/">${escHtml(home.section_writing || 'Writing')} →</a></div>
      </div>
    </div>`;

  // About intro-flow — from content/about.md body, with guarded dropcap
  const aboutHtml = about.body
    ? applyDropcap(marked.parse(about.body, { async: false }))
    : `<p>${escHtml(settings.tagline)}</p>`;

  // Theses TOC — dot-leader list
  const tocItems = theses.map(t => {
    const url   = `/${thesisUrl(t)}`;
    const label = `${String(t.order).padStart(2,'0')} · ${t.title}`;
    const pg    = `th. ${String(t.order).padStart(2,'0')}`;
    return `      <li class="toc-group">
        <a class="group-title" href="${url}">${escHtml(label)}</a>
        <ul>
          <li><a class="toc-row" href="${url}"><span class="t">${escHtml(t.description)}</span><span class="dots"></span><span class="pg">${pg}</span></a></li>
        </ul>
      </li>`;
  }).join('\n');

  // Projects TOC
  const projectCount = String(projects.length).padStart(2, '0');
  const projectItems = projects.map(p => {
    const url   = `/${projectUrl(p)}`;
    const label = `${String(p.order).padStart(2,'0')} · ${p.title}`;
    const pg    = `pr. ${String(p.order).padStart(2,'0')}`;
    return `      <li class="toc-group">
        <a class="group-title" href="${url}">${escHtml(label)}</a>
        <ul>
          <li><a class="toc-row" href="${url}"><span class="t">${escHtml(p.description)}</span><span class="dots"></span><span class="pg">${pg}</span></a></li>
        </ul>
      </li>`;
  }).join('\n');

  // Writing links — from content/writing.json (curated, independently editable)
  const writingList = writing.links || [];
  const writingLinks = writingList.length
    ? `<ul>\n${writingList.map(l =>
        `<li><a href="${escHtml(l.url)}" target="_blank" rel="noopener">${escHtml(l.title)}</a> — <em>${escHtml(l.label)}</em></li>`
      ).join('\n')}\n</ul>`
    : '';

  // Social nav links
  const navLinks = [
    settings.instagram && `<li><a href="${escHtml(settings.instagram)}" target="_blank" rel="noopener" aria-label="Instagram (opens in new tab)">Instagram</a></li>`,
    settings.github    && `<li><a href="${escHtml(settings.github)}"    target="_blank" rel="noopener" aria-label="GitHub (opens in new tab)">GitHub</a></li>`,
    settings.substack  && `<li><a href="${escHtml(settings.substack)}"  target="_blank" rel="noopener" aria-label="Substack (opens in new tab)">Substack</a></li>`,
  ].filter(Boolean).join('\n      ');

  return `<!DOCTYPE html>
<html lang="en">
<head>
  ${sharedHead({ title, description: settings.description, url: `${SITE_URL}/`, type: 'profile', settings })}
  ${homeSchema(settings)}
</head>
<body>
  <main class="ms-main">

    <header class="masthead">
      <div>
        <h1 class="sr-only">${escHtml(settings.full_name)}</h1>
        <p class="wordmark" aria-hidden="true" style="margin:0;">${escHtml(settings.wordmark_line1 || settings.full_name.split(' ')[0])}<br>${escHtml(settings.wordmark_line2 || settings.full_name.split(' ')[1] || '')}</p>
      </div>
      <div>
        ${metricsHtml}
      </div>
    </header>

    <!-- Introduction -->
    <section class="intro-flow" style="margin-top:2.5rem;">
      ${aboutHtml}
    </section>

    <!-- Kairon logo mark -->
    <div style="text-align:center; margin:6rem 0 2rem;">
      ${home.logo_image ? `<img src="${escHtml(home.logo_image)}"
           alt="${escHtml(home.logo_alt || '')}"
           style="width:min(320px, 60%); height:auto; display:inline-block;">` : ''}
    </div>

    <!-- Theses index -->
    <div class="sec-head" id="theses" style="margin-top:2rem;">
      <h3>${escHtml(home.section_theses || 'Theses')}<sup>${thesisCount}</sup></h3>
      <div class="rule-solid"></div>
      <div class="sec-label">${escHtml(settings.author_handle)} · ${escHtml(home.section_theses_label || 'index')}</div>
    </div>

    <ol class="toc-ms">
${tocItems}
    </ol>

    ${projects.length ? `<!-- Projects index -->
    <div class="sec-head" id="projects" style="margin-top:4rem;">
      <h3>${escHtml(home.section_projects || 'Projects')}<sup>${projectCount}</sup></h3>
      <div class="rule-solid"></div>
      <div class="sec-label">${escHtml(settings.author_handle)} · ${escHtml(home.section_projects_label || 'tools')}</div>
    </div>

    <ol class="toc-ms">
${projectItems}
    </ol>` : ''}

    ${writingLinks ? `<!-- Writing links -->
    <div class="sec-head" id="writing" style="margin-top:4rem;">
      <h3>${escHtml(home.section_writing || 'Writing')}</h3>
      <div class="rule-solid"></div>
      <div class="sec-label">${escHtml(settings.author_handle)} · ${escHtml(home.section_writing_label || 'links')}</div>
    </div>
    <div class="intro-flow" style="margin-top:2rem;">${home.section_writing_intro ? `<p>${escHtml(home.section_writing_intro)}</p>` : ''}${writingLinks}
    <p style="margin-top:2rem;"><a href="/blog/">Read all articles →</a></p></div>` : ''}

    <!-- Newsletter -->
    <div class="sec-head" id="newsletter" style="margin-top:4rem;">
      <h3>${escHtml(home.section_newsletter || 'Newsletter')}</h3>
      <div class="rule-solid"></div>
      <div class="sec-label">${escHtml(settings.author_handle)} · ${escHtml(home.section_newsletter_label || 'subscribe')}</div>
    </div>
    <div class="intro-flow" style="margin-top:2rem;">
      <p>${escHtml(home.newsletter_body || '')}</p>
      <p><a href="${escHtml(settings.substack)}" target="_blank" rel="noopener">${escHtml(home.newsletter_cta || 'Subscribe →')}</a></p>
    </div>

    <footer class="footer-ms">
      <div class="stars">· · ·</div>
      <div class="credits">
        <p>${escHtml(settings.tagline)}</p>
        <p><a href="mailto:${escHtml(settings.email)}">${escHtml(settings.email)}</a></p>
        <p class="disclaimer">&copy; ${year} ${escHtml(settings.full_name)}</p>
      </div>
      <div class="band"></div>
    </footer>

  </main>
</body>
</html>`;
}

// ============================================================================
// Thesis Detail Page
// ============================================================================

function renderThesisPage(thesis, allTheses, settings) {
  const url     = `${SITE_URL}/${thesisUrl(thesis)}`;
  const title   = `${String(thesis.order).padStart(2,'0')} · ${thesis.title} — ${settings.title}`;
  const year    = new Date().getFullYear();
  const num     = String(thesis.order).padStart(2, '0');
  const next    = allTheses.find(t => t.order === thesis.order + 1);
  const shortTitle = thesis.title.split(' ').slice(0, 2).join(' ');

  // Chapter nav — all theses
  const chapterNav = allTheses.map(t => {
    const isCurrent = t.slug === thesis.slug;
    return `      <a href="/${thesisUrl(t)}"${isCurrent ? ' aria-current="true"' : ''}>${String(t.order).padStart(2,'0')} · ${escHtml(t.title)}</a>`;
  }).join('\n');

  // Body HTML with margin-note transform + dropcap
  const bodyHtml = transformBody(thesis.body || '');

  // Links as references section within the article
  const linksHtml = thesis.links && thesis.links.length
    ? `<div class="sec-head" style="margin-top:3rem;">
      <h3 style="font-size:var(--text-2xl);">${escHtml(settings.thesis_links_heading || 'Links')}</h3>
      <div class="rule-solid"></div>
      <div class="sec-label">th. ${num} · ${escHtml(settings.thesis_links_label || 'references')}</div>
    </div>
    <ul style="margin-top:1.5rem;">
      ${thesis.links.map(l =>
        `<li style="margin-bottom:.75rem;">
          <span class="eyebrow" style="display:inline;">${escHtml(l.label)}</span>
          <a href="${escHtml(l.url)}" target="_blank" rel="noopener">${escHtml(l.title)} →</a>
        </li>`
      ).join('\n      ')}
    </ul>` : '';

  // Next thesis link
  const nextLink = next
    ? `    <p class="mono" style="font-size:var(--text-sm);text-transform:uppercase;margin-top:3rem;"><a href="/${thesisUrl(next)}">${escHtml(settings.thesis_next_label || 'Next')}: ${String(next.order).padStart(2,'0')} · ${escHtml(next.title)} →</a></p>`
    : '';

  // CSS path prefix — thesis pages are in root, same as index
  const cssLinks = CSS_LINKS;

  return `<!DOCTYPE html>
<html lang="en">
<head>
  ${sharedHead({ title, description: thesis.description, url, type: 'article', settings })}
  ${thesisSchema(thesis, settings)}
</head>
<body>
  <div class="page chapter-page">

    <nav class="site-nav">
      <a href="/">← ${escHtml(settings.title)}</a>
      <span class="mono">${escHtml(settings.thesis_nav_label || 'Thesis')} ${num} / ${escHtml(thesis.title)}</span>
    </nav>

    <hr class="rule-dotted">

    <nav class="chapter-nav" aria-label="Theses">
${chapterNav}
    </nav>

    <article class="article" id="${escHtml(thesis.slug)}">
      <span class="margin-label">§${thesis.order} — ${escHtml(shortTitle)}</span>
      <p class="eyebrow">${escHtml(settings.thesis_nav_label || 'Thesis')} ${num} · §1</p>
      <h1>${escHtml(thesis.title)}</h1>
      ${bodyHtml}
      ${linksHtml}
      <hr class="section-break">
    </article>

${nextLink}

    <div class="chapter-marker" style="margin-top:4rem;"><span>${escHtml(settings.title)} · th. ${num}</span></div>

    <footer class="footer-ms">
      <div class="stars">· · ·</div>
      <div class="credits">
        <p>by <a href="${SITE_URL}">${escHtml(settings.author_handle)}</a></p>
        <p class="disclaimer">&copy; ${year} ${escHtml(settings.full_name)}</p>
      </div>
      <div class="band"></div>
    </footer>

  </div>
</body>
</html>`;
}

function renderProjectPage(project, allProjects, settings) {
  const url     = `${SITE_URL}/${projectUrl(project)}`;
  const title   = `Project ${String(project.order).padStart(2,'0')} · ${project.title} — ${settings.title}`;
  const year    = new Date().getFullYear();
  const num     = String(project.order).padStart(2, '0');
  const shortTitle = project.title.split(' ').slice(0, 2).join(' ');

  // Chapter nav — all projects
  const chapterNav = allProjects.map(p => {
    const isCurrent = p.slug === project.slug;
    return `      <a href="/${projectUrl(p)}"${isCurrent ? ' aria-current="true"' : ''}>${String(p.order).padStart(2,'0')} · ${escHtml(p.title)}</a>`;
  }).join('\n');

  // Body HTML
  const bodyHtml = transformBody(project.body || '');

  // Technical metadata block
  const metaHtml = `
      <dl style="margin-bottom: 2rem; display: grid; grid-template-columns: auto 1fr; gap: 0.5rem 1rem; align-items: baseline;">
        ${project.repository_url ? `<dt class="eyebrow" style="margin:0;">Repository</dt><dd class="mono" style="margin:0;"><a href="${escHtml(project.repository_url)}" target="_blank" rel="noopener">${escHtml(project.repository_url)}</a></dd>` : ''}
        ${project.language ? `<dt class="eyebrow" style="margin:0;">Language</dt><dd class="mono" style="margin:0;">${escHtml(project.language)}</dd>` : ''}
        ${project.license ? `<dt class="eyebrow" style="margin:0;">License</dt><dd class="mono" style="margin:0;">${escHtml(project.license)}</dd>` : ''}
        ${project.version ? `<dt class="eyebrow" style="margin:0;">Version</dt><dd class="mono" style="margin:0;">${escHtml(project.version)}</dd>` : ''}
      </dl>
  `;

  return `<!DOCTYPE html>
<html lang="en">
<head>
  ${sharedHead({ title, description: project.description, url, type: 'article', settings })}
  ${projectSchema(project, settings)}
</head>
<body>
  <div class="page chapter-page">

    <nav class="site-nav">
      <a href="/">← ${escHtml(settings.title)}</a>
      <span class="mono">Project ${num} / ${escHtml(project.title)}</span>
    </nav>

    <hr class="rule-dotted">

    <nav class="chapter-nav" aria-label="Projects">
${chapterNav}
    </nav>

    <article class="article" id="${escHtml(project.slug)}">
      <span class="margin-label">§${project.order} — ${escHtml(shortTitle)}</span>
      <p class="eyebrow">Project ${num}</p>
      <h1>${escHtml(project.title)}</h1>
      ${metaHtml}
      ${bodyHtml}
      <hr class="section-break">
    </article>

    <div class="chapter-marker" style="margin-top:4rem;"><span>${escHtml(settings.title)} · pr. ${num}</span></div>

    <footer class="footer-ms">
      <div class="stars">· · ·</div>
      <div class="credits">
        <p>by <a href="${SITE_URL}">${escHtml(settings.author_handle)}</a></p>
        <p class="disclaimer">&copy; ${year} ${escHtml(settings.full_name)}</p>
      </div>
      <div class="band"></div>
    </footer>

  </div>
</body>
</html>`;
}

// ============================================================================
// Blog Pages
// ============================================================================

function blogPostUrl(post) {
  return `blog/${post.slug}.html`;
}

function renderBlogListing(settings, posts, home, activeTag = null) {
  const title        = `Writing — ${settings.title}`;
  const year         = new Date().getFullYear();
  const heading      = home.section_writing || 'Writing';
  const headingLabel = home.section_writing_label || 'articles';
  const intro        = home.blog_intro || '';

  // Split: featured (most recent) + archive (the rest)
  const [featured, ...archive] = posts;

  // Collect unique tags across all posts (for filter nav)
  const allTags = [...new Set(posts.flatMap(p => p.tags || []).filter(Boolean))].sort();
  const tagFilterHtml = allTags.length ? `
    <nav class="blog-tag-nav" aria-label="Filter by topic">
      <a href="/blog/"${!activeTag ? ' aria-current="page"' : ''}>All</a>
      ${allTags.map(t => `<a href="/blog/tag/${slugify(t)}/"${activeTag === t ? ' aria-current="page"' : ''}>${escHtml(t)}</a>`).join('')}
    </nav>` : '';

  // Featured entry (most recent article, largest visual weight)
  function coverBlock(p, cls, size) {
    return p.cover_image
      ? `<div class="${cls}"><img src="${escHtml(p.cover_image)}" alt="" aria-hidden="true" loading="${size === 'eager' ? 'eager' : 'lazy'}"></div>`
      : `<div class="${cls}"><div class="blog-${cls.includes('featured') ? 'entry' : 'archive'}-placeholder" aria-hidden="true">K</div></div>`;
  }

  const featuredHtml = featured ? (() => {
    const url     = `/${blogPostUrl(featured)}`;
    const date    = featured.date ? new Date(featured.date).toLocaleDateString('en-GB', { day: 'numeric', month: 'short', year: 'numeric' }).toUpperCase() : '';
    const tag     = featured.tags?.[0] || '';
    const metaStr = [tag, date].filter(Boolean).join(' · ');
    const cover   = featured.cover_image
      ? `<div class="blog-featured-cover"><img src="${escHtml(featured.cover_image)}" alt="" aria-hidden="true" loading="eager"></div>`
      : `<div class="blog-featured-cover"><div class="blog-entry-placeholder" aria-hidden="true">K</div></div>`;
    return `
    <a class="blog-featured" href="${url}">
      ${cover}
      <div>
        <p class="blog-featured-flag">Latest</p>
        <p class="blog-featured-meta">${escHtml(metaStr)}</p>
        <h2 class="blog-featured-title">${escHtml(featured.title)}</h2>
        <p class="blog-featured-desc">${escHtml(featured.description)}</p>
      </div>
    </a>`;
  })() : '';

  // Archive entries — text always in the centre column, images pivot L/R by index.
  // Even index (0,2,4…) → image in LEFT slot. Odd index (1,3,5…) → image in RIGHT slot.
  const archiveHtml = archive.map((p, i) => {
    const url     = `/${blogPostUrl(p)}`;
    const date    = p.date ? new Date(p.date).toLocaleDateString('en-GB', { day: 'numeric', month: 'short', year: 'numeric' }).toUpperCase() : '';
    const tag     = p.tags?.[0] || '';
    const metaStr = [tag, date].filter(Boolean).join(' · ');

    const thumbInner = p.cover_image
      ? `<img src="${escHtml(p.cover_image)}" alt="" aria-hidden="true" loading="lazy">`
      : `<div class="blog-archive-placeholder" aria-hidden="true">K</div>`;
    const thumb = `<div class="blog-archive-slot has-image">${thumbInner}</div>`;
    const empty = `<div class="blog-archive-slot"></div>`;

    const leftSlot  = i % 2 === 0 ? thumb : empty;
    const rightSlot = i % 2 === 0 ? empty : thumb;

    return `
    <a class="blog-archive-entry" href="${url}">
      ${leftSlot}
      <div class="blog-archive-content">
        <p class="blog-archive-meta">${escHtml(metaStr)}</p>
        <h2 class="blog-archive-title">${escHtml(p.title)}</h2>
        <p class="blog-archive-desc">${escHtml(p.description)}</p>
      </div>
      ${rightSlot}
    </a>`;
  }).join('\n');

  const listingDesc = `Essays on digital culture, devices, and creative technology by ${settings.full_name}`;

  return `<!DOCTYPE html>
<html lang="en">
<head>
  ${sharedHead({ title, description: listingDesc, url: `${SITE_URL}/blog/`, type: 'website', settings })}
</head>
<body>
  <div class="page">

     <nav class="site-nav blog-listing-nav">
       <a href="/">← ${escHtml(settings.title)}</a>
       <div style="display:flex;gap:1.25rem;align-items:center;flex-wrap:wrap;justify-content:flex-end;">
         <a href="/about.html" class="mono" style="font-size:var(--text-xs);text-transform:uppercase;letter-spacing:.06em;color:var(--text-muted);text-decoration:none;">About</a>
         <span class="mono">${escHtml(settings.author_handle)} · ${escHtml(headingLabel)}</span>
       </div>
     </nav>

    <hr class="rule-dotted">

    <div class="sec-head" id="writing" style="margin-top:4rem;">
      <h3>${escHtml(heading)}<sup>${String(posts.length).padStart(2,'0')}</sup></h3>
      <div class="rule-solid"></div>
      <div class="sec-label">${escHtml(settings.author_handle)} · ${escHtml(headingLabel)}</div>
    </div>

    ${intro ? `
    <p class="blog-intro-text">${escHtml(intro)}</p>
    <p style="margin-top:.75rem;"><a href="/about.html" class="mono" style="font-size:var(--text-xs);text-transform:uppercase;letter-spacing:.06em;">About this publication →</a></p>` : ''}

    ${tagFilterHtml}

    ${featuredHtml}

    ${archive.length ? `<div class="blog-archive">${archiveHtml}</div>` : ''}

    <footer class="footer-ms" style="margin-top:4rem;">
      <div class="stars">· · ·</div>
      <div class="credits">
        <p>by <a href="${SITE_URL}">${escHtml(settings.author_handle)}</a></p>
        <p class="disclaimer">&copy; ${year} ${escHtml(settings.full_name)}</p>
      </div>
      <div class="band"></div>
    </footer>

  </div>
</body>
</html>`;
}

function estimateReadTime(markdown) {
  const words = (markdown || '').replace(/[#*_~`>\[\]()!+-]/g, ' ').split(/\s+/).filter(Boolean).length;
  return Math.max(1, Math.ceil(words / 220));
}

function renderBlogPost(post, settings) {
  const year       = new Date().getFullYear();
  const title      = `${post.title} — ${settings.title}`;
  const url        = `${SITE_URL}/${blogPostUrl(post)}`;
  const dateStr    = post.date
    ? new Date(post.date).toLocaleDateString('en-GB', { day: 'numeric', month: 'long', year: 'numeric' })
    : '';
  const dateShort  = post.date
    ? new Date(post.date).toLocaleDateString('en-GB', { month: 'short', year: 'numeric' }).toUpperCase()
    : '';
  const primaryTag = Array.isArray(post.tags) && post.tags.length ? post.tags[0] : null;
  const readTime   = estimateReadTime(post.body);
  const eyebrowStr = [primaryTag, dateStr, `${readTime} min read`].filter(Boolean).join(' · ');
  const navLabel   = [primaryTag, dateShort].filter(Boolean).join(' · ');

  const coverHtml = post.cover_image
    ? `<img class="blog-hero-cover" src="${escHtml(post.cover_image)}" alt="${escHtml(post.title)}" loading="eager">`
    : '';

  const bodyHtml = transformBody(post.body || '');

  // Article JSON-LD structured data
  const articleSchema = JSON.stringify({
    '@context': 'https://schema.org',
    '@type': 'BlogPosting',
    headline: post.title,
    description: post.description,
    url,
    datePublished: post.date || '',
    dateModified:  post.date || '',
    author: {
      '@type': 'Person',
      name: settings.full_name,
      url: SITE_URL
    },
    publisher: {
      '@type': 'Person',
      name: settings.full_name,
      url: SITE_URL
    },
    mainEntityOfPage: { '@type': 'WebPage', '@id': url },
    ...(post.cover_image ? { image: post.cover_image.startsWith('http') ? post.cover_image : `${SITE_URL}${post.cover_image}` } : {})
  }, null, 2);

  return `<!DOCTYPE html>
<html lang="en">
<head>
  ${sharedHead({ title, description: post.description, url, type: 'article', settings })}
  <meta property="article:published_time" content="${post.date || ''}">
  <meta property="article:author" content="${escHtml(settings.full_name)}">
  ${post.tags?.length ? `<meta property="article:tag" content="${escHtml(post.tags.join(', '))}">` : ''}
  ${post.cover_image ? `<meta property="og:image" content="${post.cover_image.startsWith('http') ? escHtml(post.cover_image) : `${SITE_URL}${escHtml(post.cover_image)}`}">
  <meta property="og:image:alt" content="${escHtml(post.title)}">
  <meta name="twitter:image" content="${post.cover_image.startsWith('http') ? escHtml(post.cover_image) : `${SITE_URL}${escHtml(post.cover_image)}`}">
  <meta name="twitter:card" content="summary_large_image">` : ''}
  <script type="application/ld+json">${articleSchema}</script>
</head>
<body>

  <!-- Scroll progress bar — fixed at viewport bottom, fills as reader scrolls -->
  <div class="scroll-progress" id="scroll-progress" aria-hidden="true"></div>

  <section class="blog-hero" aria-labelledby="post-title">
    ${coverHtml}
    <h1 class="blog-hero-title" id="post-title">${escHtml(post.title)}</h1>
    ${post.description ? `<p class="blog-hero-subtitle">${escHtml(post.description)}</p>` : ''}
  </section>

  <div class="page chapter-page">

    <nav class="site-nav">
      <a href="/blog/">← Writing</a>
      <span class="mono">${escHtml(navLabel || post.title)}</span>
    </nav>

    <hr class="rule-dotted">

    <article class="article" id="${escHtml(post.slug)}">
      <span class="margin-label">${escHtml(dateShort)}</span>
      <p class="eyebrow">${escHtml(eyebrowStr)}</p>
      ${bodyHtml}
      <hr class="section-break">
    </article>

    <div class="chapter-marker" style="margin-top:4rem;">
      <span>${escHtml(settings.title)} · ${escHtml(dateShort)}</span>
    </div>

    <footer class="footer-ms">
      <div class="stars">· · ·</div>
      <div class="credits">
        <p>by <a href="${SITE_URL}">${escHtml(settings.author_handle)}</a></p>
        <p class="disclaimer">&copy; ${year} ${escHtml(settings.full_name)}</p>
      </div>
      <div class="band"></div>
    </footer>

  </div>

  <script>
    (function() {
      var bar = document.getElementById('scroll-progress');
      if (!bar) return;
      function update() {
        var h = document.documentElement;
        var scrolled = h.scrollTop || document.body.scrollTop;
        var total = h.scrollHeight - h.clientHeight;
        bar.style.width = (total > 0 ? Math.min(100, (scrolled / total) * 100) : 0) + '%';
      }
      window.addEventListener('scroll', update, { passive: true });
      update();
    })();
  </script>

</body>
</html>`;
}

// ============================================================================
// About Page
// ============================================================================

function renderAboutPage(page, settings) {
  const year  = new Date().getFullYear();
  const title = `${page.title} — ${settings.title}`;
  const url   = `${SITE_URL}/about.html`;
  const bodyHtml = transformBody(page.body || '');

  return `<!DOCTYPE html>
<html lang="en">
<head>
  ${sharedHead({ title, description: page.description, url, type: 'website', settings })}
</head>
<body>
  <div class="page chapter-page">

    <nav class="site-nav">
      <a href="/blog/">← Writing</a>
      <span class="mono">${escHtml(settings.author_handle)} · about</span>
    </nav>

    <hr class="rule-dotted">

    <article class="article" id="about">
      <span class="margin-label">About</span>
      <p class="eyebrow">${escHtml(settings.author_handle)} · device economies</p>
      ${bodyHtml}
      <hr class="section-break">
    </article>

    <div class="chapter-marker" style="margin-top:4rem;">
      <span>${escHtml(settings.title)} · about</span>
    </div>

    <footer class="footer-ms">
      <div class="stars">· · ·</div>
      <div class="credits">
        <p>by <a href="${SITE_URL}">${escHtml(settings.author_handle)}</a></p>
        <p class="disclaimer">&copy; ${year} ${escHtml(settings.full_name)}</p>
      </div>
      <div class="band"></div>
    </footer>

  </div>
</body>
</html>`;
}

// ============================================================================
// LLM + SEO Endpoints
// ============================================================================

function generateLlmsTxt(settings, theses, posts, projects) {
  const thesisList  = theses.map(t => `- **[${t.title}](/${thesisUrl(t)})** — ${t.description}`).join('\n');
  const writingList = posts.length
    ? posts.map(p => `- **[${p.title}](/${blogPostUrl(p)})** (${p.date || 'n/d'}) — ${p.description}`).join('\n')
    : '(no articles yet)';
  const projectList = projects.length
    ? projects.map(p => `- **[${p.title}](/${projectUrl(p)})** (${p.language || 'n/d'}) — ${p.description}\n  Repository: ${p.repository_url || 'n/a'}`).join('\n')
    : '(no projects yet)';

  return `# ${settings.full_name}

> ${settings.description}

## About

${settings.full_name} is a Creative Technologist and Martech Daylighter. Alias: ${settings.author_handle}.

## Theses

${thesisList}

## Projects

${projectList}

## Writing

${writingList}

## Machine-Readable Endpoints

- **Full content**: /llms-full.txt
- **Structured JSON**: /api/content.json
- **RSS feed**: /feed.xml
- **Sitemap**: /sitemap.xml

## Contact

- Email: ${settings.email}
- GitHub: ${settings.github}
- Substack: ${settings.substack}

## Usage Guidelines

Content is freely indexable, summarizable, and citable.
Voice: direct, thoughtful, anti-buzzword.
`;
}

function generateLlmsFullTxt(settings, theses, posts, projects) {
  let out = `# ${settings.full_name}\n\n> ${settings.description}\n\nGenerated: ${new Date().toISOString()}\n\n---\n\n`;
  for (const t of theses) {
    out += `## Thesis ${String(t.order).padStart(2,'0')}: [${t.title}](/${thesisUrl(t)})\n\n${t.description}\n\n`;
    if (t.body) out += `${t.body}\n\n`;
    if (t.links?.length) {
      out += `### Links\n\n${t.links.map(l => `- [${l.label}] ${l.title}: ${l.url}`).join('\n')}\n\n`;
    }
    out += `---\n\n`;
  }
  if (projects.length) {
    out += `## Projects\n\n`;
    for (const p of projects) {
      out += `### Project ${String(p.order).padStart(2,'0')}: [${p.title}](/${projectUrl(p)})\n\n`;
      out += `Repository: ${p.repository_url || 'n/a'}\nLanguage: ${p.language || 'n/a'}\nLicense: ${p.license || 'n/a'}\nVersion: ${p.version || 'n/a'}\n\n`;
      out += `${p.description}\n\n`;
      if (p.body) out += `${p.body}\n\n`;
      out += `---\n\n`;
    }
  }
  if (posts.length) {
    out += `## Writing\n\n`;
    for (const p of posts) {
      out += `### [${p.title}](/${blogPostUrl(p)}) (${p.date || 'n/d'})\n\n${p.description}\n\n`;
      if (p.body) out += `${p.body}\n\n`;
      out += `---\n\n`;
    }
  }
  return out;
}

function generateContentJson(settings, theses, posts, projects) {
  return {
    version: '1.0',
    generated: new Date().toISOString(),
    site: {
      name: settings.title, url: SITE_URL, description: settings.description,
      author: { name: settings.full_name, handle: settings.author_handle, email: settings.email, github: settings.github, substack: settings.substack }
    },
    theses: theses.map(t => ({
      title: t.title, slug: t.slug, order: t.order,
      description: t.description, url: `/${thesisUrl(t)}`,
      links: t.links || []
    })),
    projects: projects.map(p => ({
      title: p.title, slug: p.slug, order: p.order,
      description: p.description, url: `/${projectUrl(p)}`,
      repository_url: p.repository_url, language: p.language,
      license: p.license, version: p.version
    })),
    posts: posts.map(p => ({
      title: p.title, slug: p.slug, date: p.date,
      description: p.description, tags: p.tags || [],
      url: `/${blogPostUrl(p)}`
    }))
  };
}

function generateSitemap(theses, posts, projects) {
  const today = new Date().toISOString().split('T')[0];
  const urls  = [
    { loc: `${SITE_URL}/`,           priority: '1.0', changefreq: 'monthly', lastmod: today },
    { loc: `${SITE_URL}/blog/`,      priority: '0.9', changefreq: 'weekly',  lastmod: today },
    { loc: `${SITE_URL}/about.html`, priority: '0.7', changefreq: 'monthly', lastmod: today },
    ...theses.map(t => ({ loc: `${SITE_URL}/${thesisUrl(t)}`, priority: '0.8', changefreq: 'monthly', lastmod: today })),
    ...projects.map(p => ({ loc: `${SITE_URL}/${projectUrl(p)}`, priority: '0.8', changefreq: 'monthly', lastmod: today })),
    ...posts.map(p  => ({ loc: `${SITE_URL}/${blogPostUrl(p)}`, priority: '0.8', changefreq: 'monthly', lastmod: p.date || today }))
  ];
  return `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${
    urls.map(u => `  <url>\n    <loc>${u.loc}</loc>\n    <lastmod>${u.lastmod}</lastmod>\n    <changefreq>${u.changefreq}</changefreq>\n    <priority>${u.priority}</priority>\n  </url>`).join('\n')
  }\n</urlset>`;
}

function generateFeed(settings, posts) {
  // posts = blog posts only, sorted newest-first
  // theses are portfolio pieces, not articles — excluded from the syndication feed
  const now = posts.length && posts[0].date ? new Date(posts[0].date) : new Date();

  let rss = `<?xml version="1.0" encoding="UTF-8"?>\n`;
  rss += `<rss version="2.0" xmlns:content="http://purl.org/rss/1.0/modules/content/" xmlns:atom="http://www.w3.org/2005/Atom">\n`;
  rss += `  <channel>\n`;
  rss += `    <title>${escHtml(settings.full_name)}</title>\n`;
  rss += `    <link>${SITE_URL}</link>\n`;
  rss += `    <description>${escHtml(settings.description)}</description>\n`;
  rss += `    <language>en</language>\n`;
  rss += `    <lastBuildDate>${toRFC822(new Date())}</lastBuildDate>\n`;
  rss += `    <atom:link href="${SITE_URL}/feed.xml" rel="self" type="application/rss+xml"/>\n`;

  for (const p of posts) {
    const link    = `${SITE_URL}/${blogPostUrl(p)}`;
    const pubDate = p.date ? toRFC822(new Date(p.date)) : toRFC822(new Date());
    // Strip empty anchors left by Substack's cover-image export format (<a href="..."></a>)
    const bodyHtml = p.body
      ? marked.parse(p.body, { async: false }).replace(/<a[^>]+><\/a>/g, '')
      : '';

    rss += `    <item>\n`;
    rss += `      <title>${escHtml(p.title)}</title>\n`;
    rss += `      <link>${link}</link>\n`;
    rss += `      <guid isPermaLink="true">${link}</guid>\n`;
    rss += `      <description>${escHtml(p.description)}</description>\n`;
    rss += `      <pubDate>${pubDate}</pubDate>\n`;
    if (p.tags?.length) {
      rss += p.tags.map(tag => `      <category>${escHtml(tag)}</category>\n`).join('');
    }
    if (bodyHtml) {
      rss += `      <content:encoded><![CDATA[${bodyHtml}]]></content:encoded>\n`;
    }
    rss += `    </item>\n`;
  }

  return rss + `  </channel>\n</rss>`;
}

function generateRobotsTxt() {
  return `User-agent: *\nAllow: /\n\n# AI crawlers — explicitly allowed for indexing and citation\nUser-agent: GPTBot\nAllow: /\n\nUser-agent: Google-Extended\nAllow: /\n\nUser-agent: PerplexityBot\nAllow: /\n\nUser-agent: ClaudeBot\nAllow: /\n\nUser-agent: Amazonbot\nAllow: /\n\nUser-agent: Applebot-Extended\nAllow: /\n\nUser-agent: CCBot\nAllow: /\n\nUser-agent: Bytespider\nAllow: /\n\nSitemap: ${SITE_URL}/sitemap.xml\n`;
}

// ============================================================================
// Main
// ============================================================================

function main() {
  console.log('Building Kairon portfolio...\n');

  if (fs.existsSync(DIST)) fs.rmSync(DIST, { recursive: true });
  ensureDir(DIST);

  const settings  = loadSettings();
  const about     = loadAbout();
  const theses    = loadTheses();
  const projects  = loadProjects();
  const home      = loadHome();
  const writing   = loadWriting();
  const posts     = loadBlog();
  const aboutPage = loadAboutPage();

  console.log(`  Loaded ${theses.length} theses, ${projects.length} projects, ${posts.length} blog posts, ${(writing.links||[]).length} writing links`);

  // Home page
  fs.writeFileSync(path.join(DIST, 'index.html'), renderHomePage(settings, about, theses, projects, home, writing));
  console.log('  index.html');

  // Thesis detail pages
  for (const thesis of theses) {
    const filename = thesisUrl(thesis);
    fs.writeFileSync(path.join(DIST, filename), renderThesisPage(thesis, theses, settings));
    console.log(`  ${filename}`);
  }

  // Project detail pages
  for (const project of projects) {
    const filename = projectUrl(project);
    fs.writeFileSync(path.join(DIST, filename), renderProjectPage(project, projects, settings));
    console.log(`  ${filename}`);
  }

  // About page
  if (aboutPage) {
    fs.writeFileSync(path.join(DIST, 'about.html'), renderAboutPage(aboutPage, settings));
    console.log('  about.html');
  }

  // Blog listing + post pages
  if (posts.length) {
    ensureDir(path.join(DIST, 'blog'));
    fs.writeFileSync(path.join(DIST, 'blog', 'index.html'), renderBlogListing(settings, posts, home));
    console.log('  blog/index.html');
    for (const post of posts) {
      fs.writeFileSync(path.join(DIST, 'blog', `${post.slug}.html`), renderBlogPost(post, settings));
      console.log(`  blog/${post.slug}.html`);
    }
  }

  // LLM + SEO endpoints
  console.log('\nGenerating LLM + SEO endpoints...');
  fs.writeFileSync(path.join(DIST, 'llms.txt'),      generateLlmsTxt(settings, theses, posts, projects));     console.log('  llms.txt');
  fs.writeFileSync(path.join(DIST, 'llms-full.txt'), generateLlmsFullTxt(settings, theses, posts, projects)); console.log('  llms-full.txt');
  ensureDir(path.join(DIST, 'api'));
  fs.writeFileSync(path.join(DIST, 'api', 'content.json'), JSON.stringify(generateContentJson(settings, theses, posts, projects), null, 2));
  console.log('  api/content.json');
  fs.writeFileSync(path.join(DIST, 'sitemap.xml'), generateSitemap(theses, posts, projects)); console.log('  sitemap.xml');
  fs.writeFileSync(path.join(DIST, 'feed.xml'),    generateFeed(settings, posts));  console.log('  feed.xml');
  fs.writeFileSync(path.join(DIST, 'robots.txt'),  generateRobotsTxt());            console.log('  robots.txt');

  // Static assets
  console.log('\nCopying static assets...');
  copyDir(path.join(SRC, 'css'), path.join(DIST, 'css'));   console.log('  css/');
  copyDir(ASSETS, path.join(DIST, 'assets'));                console.log('  assets/');

  // Admin
  const adminSrc = path.join(ROOT, 'admin');
  if (fs.existsSync(adminSrc)) {
    ensureDir(path.join(DIST, 'admin'));
    fs.copyFileSync(path.join(adminSrc, 'index.html'), path.join(DIST, 'admin', 'index.html'));
    const cfg = path.join(adminSrc, 'config.yml');
    if (fs.existsSync(cfg)) fs.copyFileSync(cfg, path.join(DIST, 'admin', 'config.yml'));
    console.log('  admin/');
  }

  console.log('\nBuild complete → dist/');
}

main();
