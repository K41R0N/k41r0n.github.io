change: enable session replay and funnel tracking
## Scopes
- vendor: replayco | scope: session-replay | state: granted
- vendor: funnellens | scope: product-analytics | state: missing
## Decisions
- decision: enabled | side-effect: replayco session recording | basis: granted
- decision: enabled | side-effect: funnellens event capture | basis: missing
## Migration
