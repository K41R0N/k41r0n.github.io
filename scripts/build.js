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
  // margin notes
  md = md.replace(/^> \*\*Note:\*\*\s*(.*?)(?=\n\n|\n>|\n#|$)/gms, (_, content) =>
    `<aside class="margin-note">\n  <p>${content.trim()}</p>\n</aside>`
  );
  // section breaks
  md = md.replace(/\n---\n/g, '\n<hr class="section-break">\n');
  // parse remaining markdown, then apply guarded dropcap
  return applyDropcap(marked.parse(md, { async: false }));
}

// ============================================================================
// Shared <head>
// ============================================================================

const CSS_LINKS = `
  <link rel="stylesheet" href="css/fonts.css">
  <link rel="stylesheet" href="css/tokens.css">
  <link rel="stylesheet" href="css/base.css">
  <link rel="stylesheet" href="css/components.css">
  <link rel="stylesheet" href="css/layout.css">
  <link rel="stylesheet" href="css/animations.css">
  <link rel="stylesheet" href="css/overrides.css">`.trim();

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
  <link rel="preload" href="assets/fonts/AT-Kyrios-Variable.woff2" as="font" type="font/woff2" crossorigin>
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

// ============================================================================
// Home Page
// ============================================================================

function renderHomePage(settings, about, theses) {
  const title       = `${settings.full_name} — ${settings.tagline}`;
  const year        = new Date().getFullYear();
  const thesisCount = String(theses.length).padStart(2, '0');

  // Masthead right panel — social links in the live-metrics grid.
  // Platform name as label, handle/link as value. Clean and scannable.
  const instagramHandle = settings.instagram ? settings.instagram.split('/').filter(Boolean).pop() : '';
  const metricsHtml = `
    <div class="live-metrics" aria-label="Social links">
      ${settings.instagram ? `<div>
        <div class="metric-label">Instagram</div>
        <div class="metric-value" style="font-size:var(--text-xl);"><a href="${escHtml(settings.instagram)}" target="_blank" rel="noopener">${escHtml(instagramHandle)}</a></div>
      </div>` : ''}
      ${settings.github ? `<div>
        <div class="metric-label">GitHub</div>
        <div class="metric-value" style="font-size:var(--text-xl);"><a href="${escHtml(settings.github)}" target="_blank" rel="noopener">${escHtml(settings.author_handle)}</a></div>
      </div>` : ''}
      ${settings.substack ? `<div>
        <div class="metric-label">Substack</div>
        <div class="metric-value" style="font-size:var(--text-xl);"><a href="${escHtml(settings.substack)}" target="_blank" rel="noopener">${escHtml(settings.substack.replace('https://', ''))}</a></div>
      </div>` : ''}
    </div>`;

  // About intro-flow — from content/about.md body, with guarded dropcap
  const aboutHtml = about.body
    ? applyDropcap(marked.parse(about.body, { async: false }))
    : `<p>${escHtml(settings.tagline)}</p>`;

  // Theses TOC — dot-leader list
  const tocItems = theses.map(t => {
    const url   = thesisUrl(t);
    const label = `${String(t.order).padStart(2,'0')} · ${t.title}`;
    const pg    = `th. ${String(t.order).padStart(2,'0')}`;
    return `      <li class="toc-group">
        <a class="group-title" href="${url}">${escHtml(label)}</a>
        <ul>
          <li><a class="toc-row" href="${url}"><span class="t">${escHtml(t.description)}</span><span class="dots"></span><span class="pg">${pg}</span></a></li>
        </ul>
      </li>`;
  }).join('\n');

  // Writing links — all links labelled "Article" / "Podcast" / "Tool" across all theses
  const allLinks = theses.flatMap(t => (t.links || []).map(l => ({ ...l, thesis: t.title })));
  const writingLinks = allLinks.length
    ? `<ul>\n${allLinks.map(l =>
        `<li><a href="${escHtml(l.url)}" target="_blank" rel="noopener">${escHtml(l.title)}</a> — <em>${escHtml(l.label)}</em> · from <em>${escHtml(l.thesis)}</em></li>`
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
      <img src="assets/img/kairon-logo.svg"
           alt="Kairon"
           style="width:min(320px, 60%); height:auto; display:inline-block;">
    </div>

    <!-- Theses index -->
    <div class="sec-head" id="theses" style="margin-top:2rem;">
      <h3>${escHtml(settings.section_theses || 'Theses')}<sup>${thesisCount}</sup></h3>
      <div class="rule-solid"></div>
      <div class="sec-label">${escHtml(settings.author_handle)} · index</div>
    </div>

    <ol class="toc-ms">
${tocItems}
    </ol>

    ${writingLinks ? `<!-- Writing links -->
    <div class="sec-head" id="writing" style="margin-top:4rem;">
      <h3>${escHtml(settings.section_writing || 'Writing')}</h3>
      <div class="rule-solid"></div>
      <div class="sec-label">${escHtml(settings.author_handle)} · links</div>
    </div>
    <div class="intro-flow" style="margin-top:2rem;">${writingLinks}</div>` : ''}

    <!-- Newsletter -->
    <div class="sec-head" id="newsletter" style="margin-top:4rem;">
      <h3>${escHtml(settings.section_newsletter || 'Newsletter')}</h3>
      <div class="rule-solid"></div>
      <div class="sec-label">${escHtml(settings.author_handle)} · subscribe</div>
    </div>
    <div class="intro-flow" style="margin-top:2rem;">
      <p>${escHtml(settings.newsletter_body || '')}</p>
      <p><a href="${escHtml(settings.substack)}" target="_blank" rel="noopener">${escHtml(settings.newsletter_cta || 'Subscribe →')}</a></p>
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
    return `      <a href="${thesisUrl(t)}"${isCurrent ? ' aria-current="true"' : ''}>${String(t.order).padStart(2,'0')} · ${escHtml(t.title)}</a>`;
  }).join('\n');

  // Body HTML with margin-note transform + dropcap
  const bodyHtml = transformBody(thesis.body || '');

  // Links as references section within the article
  const linksHtml = thesis.links && thesis.links.length
    ? `<div class="sec-head" style="margin-top:3rem;">
      <h3 style="font-size:var(--text-2xl);">Links</h3>
      <div class="rule-solid"></div>
      <div class="sec-label">th. ${num} · references</div>
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
    ? `    <p class="mono" style="font-size:var(--text-sm);text-transform:uppercase;margin-top:3rem;"><a href="${thesisUrl(next)}">Next: ${String(next.order).padStart(2,'0')} · ${escHtml(next.title)} →</a></p>`
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
      <a href="index.html">← ${escHtml(settings.title)}</a>
      <span class="mono">Thesis ${num} / ${escHtml(thesis.title)}</span>
    </nav>

    <hr class="rule-dotted">

    <nav class="chapter-nav" aria-label="Theses">
${chapterNav}
    </nav>

    <article class="article" id="${escHtml(thesis.slug)}">
      <span class="margin-label">§${thesis.order} — ${escHtml(shortTitle)}</span>
      <p class="eyebrow">Thesis ${num} · §1</p>
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

// ============================================================================
// LLM + SEO Endpoints
// ============================================================================

function generateLlmsTxt(settings, theses) {
  const list = theses.map(t => `- **${t.title}** — ${t.description}`).join('\n');
  return `# ${settings.full_name}

> ${settings.description}

## About

${settings.full_name} is a Creative Technologist and Martech Daylighter. Alias: ${settings.author_handle}.

## Theses

${list}

## Machine-Readable Endpoints

- **Full content**: /llms-full.txt
- **Structured JSON**: /api/content.json
- **Sitemap**: /sitemap.xml
- **RSS feed**: /feed.xml

## Contact

- Email: ${settings.email}
- GitHub: ${settings.github}
- Substack: ${settings.substack}

## Usage Guidelines

Content is freely indexable, summarizable, and citable.
Voice: direct, thoughtful, anti-buzzword.
`;
}

function generateLlmsFullTxt(settings, theses) {
  let out = `# ${settings.full_name}\n\n> ${settings.description}\n\nGenerated: ${new Date().toISOString()}\n\n---\n\n`;
  for (const t of theses) {
    out += `## Thesis ${String(t.order).padStart(2,'0')}: ${t.title}\n\n${t.description}\n\n`;
    if (t.body) out += `${t.body}\n\n`;
    if (t.links?.length) {
      out += `### Links\n\n${t.links.map(l => `- [${l.label}] ${l.title}: ${l.url}`).join('\n')}\n\n`;
    }
    out += `---\n\n`;
  }
  return out;
}

function generateContentJson(settings, theses) {
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
    }))
  };
}

function generateSitemap(theses) {
  const today = new Date().toISOString().split('T')[0];
  const urls  = [
    { loc: `${SITE_URL}/`, priority: '1.0', changefreq: 'monthly' },
    ...theses.map(t => ({ loc: `${SITE_URL}/${thesisUrl(t)}`, priority: '0.8', changefreq: 'monthly' }))
  ];
  return `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${
    urls.map(u => `  <url>\n    <loc>${u.loc}</loc>\n    <lastmod>${today}</lastmod>\n    <changefreq>${u.changefreq}</changefreq>\n    <priority>${u.priority}</priority>\n  </url>`).join('\n')
  }\n</urlset>`;
}

function generateFeed(settings, theses) {
  const now = new Date();
  let rss = `<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0">\n  <channel>\n`;
  rss += `    <title>${escHtml(settings.full_name)}</title>\n    <link>${SITE_URL}</link>\n`;
  rss += `    <description>${escHtml(settings.description)}</description>\n    <lastBuildDate>${toRFC822(now)}</lastBuildDate>\n`;
  for (const t of theses) {
    const link = `${SITE_URL}/${thesisUrl(t)}`;
    rss += `    <item>\n      <title>${escHtml(t.title)}</title>\n      <link>${link}</link>\n`;
    rss += `      <guid isPermaLink="true">${link}</guid>\n      <description>${escHtml(t.description)}</description>\n`;
    rss += `      <pubDate>${toRFC822(now)}</pubDate>\n    </item>\n`;
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

  const settings = loadSettings();
  const about    = loadAbout();
  const theses   = loadTheses();

  console.log(`  Loaded ${theses.length} theses`);

  // Home page
  fs.writeFileSync(path.join(DIST, 'index.html'), renderHomePage(settings, about, theses));
  console.log('  index.html');

  // Thesis detail pages
  for (const thesis of theses) {
    const filename = thesisUrl(thesis);
    fs.writeFileSync(path.join(DIST, filename), renderThesisPage(thesis, theses, settings));
    console.log(`  ${filename}`);
  }

  // LLM + SEO endpoints
  console.log('\nGenerating LLM + SEO endpoints...');
  fs.writeFileSync(path.join(DIST, 'llms.txt'),      generateLlmsTxt(settings, theses));     console.log('  llms.txt');
  fs.writeFileSync(path.join(DIST, 'llms-full.txt'), generateLlmsFullTxt(settings, theses)); console.log('  llms-full.txt');
  ensureDir(path.join(DIST, 'api'));
  fs.writeFileSync(path.join(DIST, 'api', 'content.json'), JSON.stringify(generateContentJson(settings, theses), null, 2));
  console.log('  api/content.json');
  fs.writeFileSync(path.join(DIST, 'sitemap.xml'), generateSitemap(theses)); console.log('  sitemap.xml');
  fs.writeFileSync(path.join(DIST, 'feed.xml'),    generateFeed(settings, theses));    console.log('  feed.xml');
  fs.writeFileSync(path.join(DIST, 'robots.txt'),  generateRobotsTxt());               console.log('  robots.txt');

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
