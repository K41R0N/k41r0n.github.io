# 2026-10-30: Methodology, advice packaging, and site infrastructure

## Decision and record

This entry preserves the methods and infrastructure facts established on October 30. The canonical Harness Standard and Attention Graduation Framework remain in their existing reference locations; this is a dated record, not a second copy of either document.

## Harness methodology

**Canonical source:** Harness Standard v0.3 and the Attention Graduation Framework are maintained in the private `Marketing-harness` repository under `docs/references/harness-standard-v0.3/`. A snapshot of these documents is also kept with the self-interview loop state File so the working loop can find them. The user had repeatedly found the source documents missing from the loop; the fix is to check the canonical path and keep the snapshot available, not make another public copy.

The Standard defines exactly three harness kinds: `operator-agent`, `brand-brain`, and `operator-profile`. Do not reconstruct the kinds from memory. Read the Standard before describing them.

Two early advice drafts failed in different ways: the first invented harness kinds; the next still missed the point of skills and the framework, and did not make the business application concrete. The user's correction was that deterministic scripts should take on routine inference and repetitive work, leaving attention for what needs the owner's judgment. Keep that purpose central, show how it could help the business, and explain what decisions and data the owner would need to consider.

## Advice-harness packaging, tested with a founder in the owner's network

The starter kit was shared on October 30 as a method-only package. Keep this pattern for future advice-harness on-ramps:

- Remove client material and infrastructure specifics. Use a beginner edition of the Attention Graduation Framework and label each adaptation at the top of the document.
- Write bounded claims. Check service pricing and compatibility against current sources or leave numbers out. Do not promise that corrections, integrations, or AI behavior will work permanently or without error.
- Include a hands-on demonstration so the reader can see the method in use.
- Before sending anything, inspect it for factual accuracy. That review caught unsupported pricing, compatibility, and permanence claims in the README copies; they were corrected before delivery.
- Keep the recipient’s identity and private details out of this public record. The open question is what goal they want the system to serve: market research, reaching an audience, engagement, or sales. Treat the exchange as an anonymized example of the advice-harness on-ramp, not as proof of a general result.

The owner's platform guidance was goal-dependent: first consider an email platform and a way to monitor the audience; Grokbot had worked well for insights into the owner's ICP. For someone setting up a harness, his advice was that GitHub plus an inference provider is enough, and a harness kept in GitHub can move between providers. This is his reported experience, not a promise that every setup migrates without changes.

The package included a guide, a beginner framework, a starter template with a worked example, and interview/coaching methods. It was delivered through the approved private channel at about 6:59 PM. The interactive demonstration was hosted anonymously on here.now, was expected to expire after about 24 hours, and had a separate claim link to keep it. Neither link is stored in this public record.

## Website deployment record

On October 30 the site moved its `www` host to Cloudflare Workers. Pushes to `main` now trigger Workers Builds; the build and deployment run automatically. The Worker serves the static site and forwards the first-party analytics ingest route. A comment-only smoke-test commit confirmed an automatic deploy; the mirror matched 51 of 51 files, with only build timestamps differing.

PR #18 merged the Cloudflare static-mirror configuration into `main` (merge commit `0bdedef`). The Workers Builds GitHub integration was set up separately; it was not what PR #18 merged. The pull-request API returned a stale closed/unmerged status, while the live PR page showed the merge and the `main` history contained the merge commit and later smoke-test commit. Verify the live PR and branch history when API status conflicts with them.

Live check after cutover: `https://www.kairon.xyz/` returned HTTP 200 with `server: cloudflare` and a Cloudflare request-ray header; no Vercel response header was present. This supports that Cloudflare served the `www` host at the time of the check. Cloudflare dashboard settings were not independently inspected in this review.

Vercel remains intact for the bare-domain redirect and as the rollback path. To restore serving through Vercel, remove the Worker’s `www` custom-domain attachment and recreate the proxied `www` CNAME to Vercel. The email link behavior changed: it is now plain HTML because the prior edge obfuscation rewrite is not part of the Worker. The page content itself remained unchanged by the hosting cutover.

The Cloudflare API credential is kept in the vault, not in this repository. It expires around November 29, 2026; renew it before later infrastructure work. No account, zone, domain, token, or vault-entry identifiers belong in this record.

## Sources and confidence

- Harness kinds and canonical path: current Harness Standard v0.3 in the private reference repository. The loop snapshot and prior document-finding problem are recorded in the October 30 conversation.
- Owner’s methodology correction, packaging request, platform guidance, review, approval, delivery time, and open goals question: direct WhatsApp messages on October 30, 2026.
- Deployment and rollback sequence, smoke-test comparison, email-link behavior, and credential expiry: direct session report on October 30, 2026. The PR/API status discrepancy was independently checked against the live GitHub PR page and `main` commit history.
- Public serving evidence: live request to `https://www.kairon.xyz/` on October 30, 2026; HTTP 200, `server: cloudflare`, Cloudflare ray present, no `x-vercel-id`. This is a point-in-time check, not a guarantee of future routing.
