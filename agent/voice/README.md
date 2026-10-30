# agent/voice
Alejandro Arango's voice and copy engine. Start with HARNESS.md.

Run measurement and checks (Python 3, stdlib only):
    python3 tools/build_spec.py corpus > tools/spec_v0.json
    python3 tools/gen_spec_md.py > canon/voice-spec.md
    python3 tools/checks.py drafts/<draft>/draft.md
    python3 tools/verify.py <optional controls dir>   # writes reports/verification.md
