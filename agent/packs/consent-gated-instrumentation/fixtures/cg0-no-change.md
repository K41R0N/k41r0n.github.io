## Scopes
- vendor: replayco | scope: session-replay | state: granted
- vendor: funnellens | scope: product-analytics | state: missing
## Decisions
- decision: enabled | side-effect: replayco session recording | basis: granted
- decision: blocked | side-effect: funnellens event capture | basis: missing
## Migration
- record: legacy-replay-consents | review: reviewed | carried: yes
