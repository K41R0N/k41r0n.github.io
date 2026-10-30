# agent/voice
Alejandro Arango's voice and copy engine. Start with HARNESS.md.

Run measurement and checks (Python 3, stdlib only):
    python3 scripts/local/voice/build_spec.py assets/voice-corpus > scripts/local/voice/spec_v0.json
    python3 scripts/local/voice/gen_spec_md.py > knowledge/voice/voice-spec.md
    python3 scripts/local/voice/checks.py assets/voice-drafts/<draft>/draft.md
    python3 scripts/local/voice/verify.py <optional controls dir>   # writes ingestion/reports/voice/verification.md
