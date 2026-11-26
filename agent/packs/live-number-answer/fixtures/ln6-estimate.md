probe: ran
dataset: alpha
## Sources
- source: mail-api | reachable: yes | role: canonical
- source: csv-export | reachable: yes | role: fallback
## Values
- value: opens = ~4120 | source: mail-api | as-of: 2026-11-13 | status: ok | final: yes
## Refusals
## Verify
- verify: opens matches the dashboard the human sees today
