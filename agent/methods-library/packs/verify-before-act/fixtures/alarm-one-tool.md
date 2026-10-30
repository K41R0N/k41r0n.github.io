mode: change
## Claims
- claim: disk has 5 GB free | check: df on the host | result: confirmed
## Signals
- signal: one warning line at boot | classified: expected
## Findings
- finding: service is down | independent-confirmation: no
## Change
- change: restart the service
## Verify
- verify: service answers on its port
