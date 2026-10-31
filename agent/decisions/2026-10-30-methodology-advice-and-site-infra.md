# 2026-10-30: Methodology, advice packaging, and site infrastructure

## Decision and record

This entry preserves the methods and infrastructure facts established on October 30. The canonical Harness Standard and Attention Graduation Framework remain in their existing reference locations; this is a dated record, not a second copy of either document.

## Harness methodology

**Canonical source:** Harness Standard v0.3 and the Attention Graduation Framework are maintained in the private `Marketing-harness` repository under `docs/references/harness-standard-v0.3/`. The self-interview loop state File already keeps a snapshot of these documents. Do not create another copy here.

The Standard defines exactly three harness kinds: `operator-agent`, `brand-brain`, and `operator-profile`. Do not reconstruct the kinds from memory. Read the Standard before describing them.

The owner corrected two earlier advice-kit drafts on October 30: they invented harness kinds and missed the purpose of skills and the framework. His point was that deterministic scripts should take on routine inference and repetitive work, leaving the owner focused on what actually needs his judgment. Keep that purpose central in future explanations and examples.

## Advice-harness packaging, tested with an external recipient

The starter kit was shared on October 30 as a method-only package. Keep this pattern for future advice-harness on-ramps:

- Remove client material and infrastructure specifics. Use a beginner edition of the Attention Graduation Framework and label each adaptation at the top of the document.
- Write bounded claims. Check service pricing and compatibility against current sources or leave numbers out. Do not promise that corrections, integrations, or AI behavior will work permanently or without error.
- Include a hands-on demonstration so the reader can see the method in use.
- Before sending anything, inspect it for factual accuracy. That review caught unsupported pricing, compatibility, and permanence claims in both copies of the README; both were corrected before delivery.
- Keep the recipient’s identity and private details out of this public record. The open question is what goal they want the system to serve: market research, reaching an audience, engagement, or sales. Treat the exchange as an anonymized example of the advice-harness on-ramp, not as proof of a general result.

The package included a guide, a beginner framework, a starter template with a worked example, and interview/coaching methods. It was delivered through the approved private channel at about 6:59 PM. The interactive demonstration was temporary and had a claim option; its link is intentionally not stored here.

## Website deployment record

On October 30 the site moved its `www` host to Cloudflare Workers. Pushes to `main` now trigger Workers Builds; the build and deployment run automatically. The Worker serves the static site and forwards the first-party analytics ingest route. A comment-only smoke-test commit confirmed an automatic deploy; the mirror matched 51 of 51 files, with only build timestamps differing.

The Cloudflare static-mirror configuration and Workers Builds GitHub integration landed on `main` through a merged pull request on October 30. GitHub’s pull-request API later returned a stale closed/unmerged status, but the live PR page showed the merge into `main`, and the `main` commit history showed the merge and subsequent smoke-test commit.

Live check after cutover: `https://www.kairon.xyz/` returned HTTP 200 with `server: cloudflare` and a Cloudflare request-ray header; no Vercel response header was present. This supports that Cloudflare served the `www` host at the time of the check. Cloudflare dashboard settings were not independently inspected in this review.

Vercel remains intact for the bare-domain redirect and as the rollback path. To restore serving through Vercel, remove the Worker’s `www` custom-domain attachment and recreate the proxied `www` CNAME to Vercel. The email link behavior changed: it is now plain HTML because the prior edge obfuscation rewrite is not part of the Worker. The page content itself remained unchanged by the hosting cutover.

The Cloudflare API credential is kept in the vault, not in this repository. It expires around November 29, 2026; renew it before later infrastructure work. No account, zone, domain, token, or vault-entry identifiers belong in this record.

## Sources and confidence

- Harness kinds and canonical path: current Harness Standard v0.3 in the private reference repository.
- Owner’s methodology correction, packaging request, review, approval, delivery time, and open goals question: direct WhatsApp messages on October 30, 2026.
- Deployment and rollback sequence, smoke-test comparison, email-link behavior, and credential expiry: direct session report on October 30, 2026. The PR/API status discrepancy was independently checked against the live GitHub PR page and `main` commit history.
- Public serving evidence: live request to `https://www.kairon.xyz/` on October 30, 2026; HTTP 200, `server: cloudflare`, Cloudflare ray present, no `x-vercel-id`. This is a point-in-time check, not a guarantee of future routing.
