# Email audit from an inbox

Use this when the user (or a teammate) signed up to the client's product and received their emails. It's the fastest way to see what a new subscriber actually gets, rather than what the client says they send.

## Steps

1. **Connect Gmail** if it isn't loaded (search the connector registry, suggest it, wait for the user).
2. **Find the sender.** Search `from:<client domain>`. Marketing mail often comes from a subdomain (e.g. `hello@email.clientdomain.com`), separate from product or support mail.
3. **Find the window.** The first email is usually the welcome on signup; the end is the upgrade confirmation (e.g. "Welcome to Pro") or today. Search `from:<sender> before:<date>` to list everything in that window. Tell the user the real length of the window if it differs from what they remembered.
4. **Group into streams** by sender name, send time and subject pattern: onboarding sequence (days 0, 1, 4, 7, 10...), recurring newsletter (fixed weekdays and time), weekly digest, product launches, upgrade asks.
5. **Pull the full copy** of each email with `get_message` (plain text). For long digest emails of the same format, pull one in full and list the rest by subject.
6. **Note the tooling** from the links: tracked-redirect domains and preference-centre links usually reveal the email platform (e.g. HubSpot). Tracked links hide the final destination, so say destinations need checking by clicking.

## The Google Doc

Create it with a Docs tool (e.g. the agency's `docs_create`). Structure:

- **What this is:** whose inbox, the window, the number of emails, times in the client's time zone, and the caveat that a test or comped account may not see everything a normal subscriber gets.
- **Summary table:** stream, sender name, cadence, count in the window.
- **What we noticed:** numbered findings with evidence. Look for:
  - lists reaching people they aren't meant for;
  - how many asks there are and when (upgrade, activation, referral);
  - whether emails mention the onboarding steps or rewards the product relies on;
  - where the sequence stops;
  - double sends on the same day;
  - newsletter slots used for product launches;
  - inconsistent sender names;
  - lines the client's compliance lead should review (e.g. anything that reads like a trade call or an unqualified superlative).
- **Questions for the client.**
- **Full copy, in the order received:** for each email, the subject, stream and position, sent date and time, sender, preheader, Gmail link, copy (footers removed), and a CTA line listing every link text and where it seems to go.

Then link the doc from the Nurture step on the board and update the funnel's email nodes with the real streams and cadence.
