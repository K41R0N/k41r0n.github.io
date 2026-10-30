// Phase 1 mirror: only the /ingest reverse proxy runs in the Worker (parity with
// the vercel.json rewrite /ingest/:path* -> https://eu.i.posthog.com/:path*).
// Everything else is served from static assets (dist/).
export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (url.pathname === '/ingest' || url.pathname.startsWith('/ingest/')) {
      const target = 'https://eu.i.posthog.com' + url.pathname.slice('/ingest'.length) + url.search;
      return fetch(new Request(target, request));
    }
    return env.ASSETS.fetch(request);
  }
};
