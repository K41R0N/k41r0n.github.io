probe: ran
dataset: alpha
## Sources
- source: mail-api | reachable: no | role: canonical
- source: csv-export | reachable: no | role: fallback
## Values
- value: opens = 3900 | source: mail-api | as-of: 2026-11-01 | status: ok
## Refusals
## Verify
- verify: opens matches the dashboard
