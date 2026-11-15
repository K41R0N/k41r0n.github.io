probe: ran
dataset: alpha
## Sources
- source: mail-api | reachable: yes | role: canonical
## Values
- value: opens = 3900 | source: mail-api | as-of: 2026-10-20 | status: stale | final: yes
## Refusals
## Verify
- verify: opens matches the dashboard
