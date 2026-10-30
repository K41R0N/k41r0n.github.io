mode: change
## Claims
- claim: disk has 5 GB free | result: confirmed
## Signals
- signal: one warning line at boot | classified: expected
## Findings
- finding: service is down | independent-confirmation: yes, checked with a second tool
## Change
- change: restart the service
## Verify
- verify: service answers on its port
