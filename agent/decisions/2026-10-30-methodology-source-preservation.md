# 2026-10-30: Source-package preservation before processing

## Incident

A user-provided methodology archive was processed before an unchanged durable copy had been verified. Later recovery checks found a derived monolithic method file, but not the original package or its separate source documents. The user had to resend the ZIP before the original-file redaction work could continue.

## Rule

On arrival, first save an unchanged copy of any source package to the user's designated durable Drive account. Verify the uploaded copy against the received file (size and SHA-256 where available) before extracting, redacting, summarizing, or otherwise processing it. Keep the original intact. Work on separate copies, record source hashes and changes, and do not claim a derivative is the original. If the durable copy cannot be verified, stop processing and report the blocker.

## This incident's recovery

The resent archive was uploaded unchanged to the user's Kairon Drive before processing. Downloading it back produced a file with the same byte size and SHA-256 as the received archive. The per-file redaction work is being staged separately from that durable source.

## Provenance

- User's direct correction on October 30: “I don't want synthesis, I want redaction on the original files as they are so we don't lose out on the actual documents.”
- User's direct request after the recovery: “Let's log this learning.”
- Archive SHA-256: `6e3e125a36ee078ff23569a9e1e9bbb7d5560206eb3c4d9aab54679ba0033f64`.
- Drive original: private copy in the user's Kairon account. The durable link is reported in the handoff, not stored in this public repo.
