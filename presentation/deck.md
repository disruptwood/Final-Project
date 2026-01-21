# Final Project (B2C): Verified Circles for Relocators
**Problem #12 (B2C): Adults struggle to build and maintain social connections after moving cities or changing life stages.**

## Slide 1: Title & One-Liner
**Project**: Verified Circles — “don’t-go-alone” meetups for people new in town  
**Target**: relocators / expats / life-stage shifters (20s–30s)  
**Promise**: lower the risk of showing up (trust + structure) so people actually attend.

---
### Speaker Notes (optional)
- We are not building “Tinder for friends”. We’re building a structured path from “I want to go” → “I actually go”.

## Slide 2: Evidence of the Core Barrier (Survey N=45)
From our real survey (`research/surveys/survey_responses_raw.csv`):
- **53%** go alone when they have no partner (24/45).  
- **36%** either give up or don’t do the activity at all (16/45).  
- **40%** rate “going alone to a social activity” as hard/very hard (4–5 on a 1–5 scale).  
- **98%** of respondents who answered say they **don’t** use dating apps just for social interaction (43/44).

**Visual**: `presentation/assets/survey_no_partner_behavior.png` (generated from the raw CSV)

**Sources / data**:
- Survey summary: `research/surveys/survey1_summary.md`

## Slide 3: Research Question & What We Did
**Research question**: What mechanisms reduce the “go alone” + “trust strangers” barrier for relocators, enough to make them show up?

**Methods**:
- **User survey (N=45)** + open responses (trust signals).
- **Competitor scan** using official pricing / help-center pages (Meetup, Timeleft, CitySocializer, Soho House, etc.).
- **Academic / public sources** to explain mechanisms (signaling, homophily) and contextualize the problem.

**Sources**:
- Source list: `research/sources.md`
- Competitor pricing table: `research/data/competitor_pricing.csv`

## Slide 4: Market Context (Size + Spend Signals)
We keep market sizing simple and traceable:
- **Large base of “newcomers”**: 12.1% of US population changed residence in 2023 (U.S. Census ACS).  
- **Large base of relocators internationally**: 281M international migrants (UN DESA, 2020 stock).  
- **People already pay for “social experiences”**: paid curated social formats exist (e.g., Timeleft ~$16 per ticket) and membership communities exist (see competitor pricing table).

**Sources / data**:
- `research/data/key_metrics_wtp_proxies.csv`
- `research/data/competitor_pricing.csv`

---
### Critical Reflection
- This is *context*, not a full TAM/SAM/SOM. We’ll do a bottom-up pilot estimate per city once interviews define the best segment + price point.

## Slide 5: Synthesis — The 3 Things Any B2C Solution Must Solve
Based on survey patterns + competitor scan:
1) **Don’t-go-alone barrier**: people avoid activities if they’d attend solo.  
2) **Trust / safety**: users need concrete reassurance signals before meeting.  
3) **Structure to follow through**: turning “maybe” into attendance requires lightweight commitment + facilitation.

*(Keep this as the “design requirements” slide — everything later maps to one of these.)*

## Slide 6: Why Existing Solutions Still Fail This Moment
**Open matching (Bumble BFF)**:
- Feels like dating mechanics; weak context + awkward for friendship.  

**Open groups/events (Facebook Groups, Meetup)**:
- You still arrive alone + high noise; trust is manual and effortful.  

**Curated event apps (e.g., Timeleft / facilitated events)**:
- Better structure, but limited personalization and not “circles” built around repeatable context.

**Visual**: `presentation/assets/competitor_matrix.png`

**Data**:
- `research/data/competitor_pricing.csv`
- `research/competitors/competitor_matrix.md`

## Slide 7: Target Persona (B2C)
**Omer, 30s, relocated for a new job**  
- Wants to do activities (sports / culture / learning) but doesn’t want to show up alone.  
- Needs quick trust signals (“is this person normal/safe?”) without “social stalking”.  
- Has limited time; hates wasted evenings.

*(Add 1 real quote from the survey or upcoming interviews later.)*

## Slide 8: Product Concept — Verified Circles (B2C)
**Core idea**: Circles are small, repeatable communities with built-in trust + structure.

How it works:
1) **Join a circle** (city + context like “new in Berlin”, “tech runners”, “young parents”).  
2) **Trust signals** (light verification options: LinkedIn / photo / short intro; clear code of conduct).  
3) **Don’t-go-alone meetups**: the product pairs you with a buddy or micro-group (6–10) for the first event.  
4) **Follow-through mechanics**: RSVP rules (e.g., small deposit / reliability score) + facilitation.

## Slide 9: Why This Should Work (1 slide, no over-claim)
- **Costly signaling** (Spence 1973): small “cost” actions can increase credibility.  
- **Homophily** (McPherson et al. 2001): shared context increases chance of bonding.

**Positioning**: not elitist “high-achievers”, but “high-intent newcomers who value safety and structure”.

## Slide 10: Monetization (B2C) — Keep It Simple
Observed willingness to pay in the market is often **for the event/experience**, not for “friends”.
- Examples of paid social formats: curated dinners / facilitated events / membership communities.

**Our starting bet**:
- Start with **paid events** (tickets) + optional membership later, once there is density.

**Data**:
- `research/data/competitor_pricing.csv`

## Slide 11: Interviews (Placeholder — you will fill quotes)
**Plan** (per course guidance):  
- **3+ interviews** (relocators / life-stage changers) + **thematic coding**.  
- **What we’ll extract**: real stories (time/place), emotional quotes, repeated patterns, and contradictions.

**Drop-in structure for the slide** (fill later):
- Interviewees: `[#] relocators`, `[#] new job`, `[#] new parents` (or your final set)
- 2 quotes (verbatim):
  - Quote A: “[…]”
  - Quote B: “[…]”
- Mini coding snapshot:

| Quote | Code | Theme | Insight (so what) |
| :--- | :--- | :--- | :--- |
| “[…]” | … | Trust / Don’t-go-alone / Structure | … |
| “[…]” | … | … | … |

## Slide 12: Validation Plan (What We Will Test Next)
1) **Interviews**: insert the completed slide above.  
2) **Behavioral test** (MVP-level): a landing page for a specific circle (city + topic) and measure:
   - willingness to join + provide a trust signal,
   - show-up rate for the first event (buddy vs no buddy; deposit vs no deposit).

## Slide 13: Conclusion
- **Core problem**: people don’t go because going alone + low trust feels risky.  
- **Gap**: current tools optimize for discovery or scale, not for “show-up with confidence”.  
- **Recommendation**: build a B2C “Verified Circles” MVP focused on relocators with a measurable show-up outcome.
