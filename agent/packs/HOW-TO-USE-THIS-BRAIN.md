# packs/HOW-TO-USE-THIS-BRAIN.md

Pointer file. The brain-level retrieval and trust rules are
`../HOW-TO-USE-THIS-BRAIN.md`. For this folder specifically:

1. Open `index.md` and find the task you have. If no pack fits, record the
   ask in `../decisions/open-loops.md` and ask - never pick the nearest
   pack by name.
2. Copy the pack folder into the agent that needs it. It is read-only
   there. Its files are hashed in `../MANIFEST.md` so drift shows.
3. Run the pack's eval on its fixtures before relying on it.
4. If the pack gets a correction, log it in `../routines/learnings.md`,
   not in the copy.
5. Never put client details in a pack. Run the push gate before pushing.

Replaced 2026-11-14 (decisions/log.md #34).
