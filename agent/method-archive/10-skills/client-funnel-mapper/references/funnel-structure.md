# Funnel structure

## Contents
1. Colour code
2. Always-on funnel: stages and node patterns
3. Campaign funnel: stages and node patterns
4. Rows under the flow
5. Wording rules
6. Layout coordinates

---

## 1. Colour code

Use one fill per meaning so the board reads at a glance. Put a legend of chips at the top of every funnel frame.

| Meaning | Fill | Stroke | Text | Notes |
|---|---|---|---|---|
| Agency runs / owns | #FFE86D | #A28E26 | #574900 | e.g. "Owned by the client product" |
| Client runs / owns | #9CE6FF | #2C97BB | #1C4657 | e.g. "Owned by [client]" |
| Not confirmed | #DDDDD8 | #8A8A7E, dashed 5,5 | #434339 | anything you couldn't verify |
| Where people drop off | #FD9AE7 | #D756BA | #511341 | evidence-based leaks only |
| Fix needed / proposed | #B3E65F | #6E9A24 | #2F440B | recommendations, new steps |

Arrow colour follows the owner of the step it leaves. Dashed arrows mean unconfirmed or optional paths.

## 2. Always-on funnel: stages and node patterns

Column order (rename to fit the client):

1. **Channels.** One node per channel. Examples: brand X, brand Instagram, founder's channels, YouTube and podcasts, Reddit, affiliates and creators, Discord or community, paid media.
2. **How we move people.** One or more mechanism nodes per channel, stacked in that channel's lane. Examples: CTA in posts, keyword-reply auto DM, profile banner offering a report, link in bio, comment-to-DM automation, posts pointing to an AI tool. A channel with no mechanism gets a pink "No signup link today" node.
3. **Where we send them.** Destinations: the current campaign page (generic, linked to the campaign funnel), lead magnets (reports, AI tools, calculators), the logged-out homepage, and green fix nodes (e.g. "Signup link in channel and video descriptions, on-screen CTA and QR code").
4. **Sign up.** The signup page, with the URL and sign-in options.
5. **Account.** "Free account created". Only add rewards here if they really are granted at signup.
6. **Activate.** The onboarding steps, then a decision diamond ("All 5 done within 72 hours?") with a Yes path onwards and a No path to a grey "Follow-up not known" node if nothing is known to happen.
7. **Nurture.** Emails split by audience ("Free member emails" listing each stream and its cadence), a grey "Other emails, to confirm" node below, and a link to the email audit doc.
8. **Convert.** Paywall or pricing page, then "Paid member". If conversion is held for a date, say so.
9. **Retain.** Paid member emails, community (e.g. Discord, paid only), renewal.

Arrow labels worth using: "direct CTA", "link in bio", "campaign posts", "sign up to read", "about N%", "about N a day", "Yes, activated", "No", "clicks a paid link", "joins the community", "reason to renew", "amplify".

## 3. Campaign funnel: stages and node patterns

1. **Channels** for this campaign (confirm with the user). Amplifiers labelled "amplify".
2. **The offer.** One node listing the hooks (prizes, the challenge, weekly rewards, no-cost entry, dates).
3. **Campaign page.** Rules, prizes, how to enter.
4. **Get eligible.** Decision diamond ("Has an account?") splitting into: no account → signup → activation steps; free member → activation steps; paid member → enters directly.
5. **Enter.** "Eligible to enter", then the participation action (e.g. "Publish up to 3 ideas, 2 needed to count").
6. **Compete / engage.** The recurring moment (e.g. "Weekly results, Mondays"), with an arrow down to "Results become content, feeds step 1".
7. **Convert.** Close and winners, then the conversion offer.

Also add:
- **Teaser lane (green, proposed)** from the offer: teaser → "sign up and finish activation early" → "ready list: reminder when entry opens" → arrow up into "Eligible to enter".
- **Watcher path**: campaign page → "Follows the campaign" → dashed arrow to the conversion offer ("still gets the offer").

## 4. Rows under the flow

Place these under the relevant columns, aligned to the step they refer to, with a bold label at the left:

- **Where people drop off** (pink). One fact each, with the number if you have it: "Login drops UTMs, about 30% of source data lost."
- **[Agency] audit** on the always-on funnel (yellow = take over, green = recommend changes, green "Hold until [date]", grey "After [date]").
- **What [agency] adds** on campaign funnels (yellow): the concrete things the agency will do at that step.

## 5. Wording rules

- Node titles in bold, then one or two short lines. Max about 12 words per line.
- Say who, what and when. "Daily Vision, Tue, Wed, Fri, about 1:17pm ET" beats "Regular newsletter".
- Label anything unverified "to confirm" or turn it into a question.
- No em dashes, no exclamation marks, sentence case. Use "to" for ranges ("Oct 15 to 16").
- Frame title states the journey ("from stranger to free member, then paid at Black Friday"), and the subtitle states the goal and how to read the map.

## 6. Layout coordinates

Frame-relative, left to right. These worked well; adjust if you add or drop columns.

- Frame padding 64. Title baseline y=97 (33px bold). Subtitle textArea y=120 (22px). Legend chips y=180, 280x50, 20px gap.
- Stage labels y=320 (33px bold).
- Flow starts y=360. Column x positions with 160px gaps: 64 (w320), 544 (w400), 1104 (w400), 1664 (w380), 2204, 2744, 3284 (diamond w300), 3744, 4284, 4824, 5364 (all w380). Frame width 5808.
- Channel lanes: each mechanism node 110 tall with 20px gaps; the channel node spans its mechanisms; 48px between lanes.
- Main chain centred around y≈1000, nodes 160 tall.
- Drop-off row about 200px below the lowest flow node; audit or "adds" row 240px below that; campaign lanes below those.
- Leave at least 160px between frames, and check what's already on the board before placing a new frame.
