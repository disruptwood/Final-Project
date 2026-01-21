# Final Project: Verified Connections for Relocators (B2C)
**Problem #12**: People struggle to build and maintain social connections after moving cities or life stages.

---

## Slide 1: Title and One-Liner
**Project**: Verified Connections  
**One-liner**: Verified onboarding + reliability signals that make first meetings safe and repeatable.  
**Team**: [Ilya, Nitzan, Ishay]

---

## Slide 2: Problem Statement + Topic Overview (What’s happening?)
**Topic**: Building new friendships after relocation / life-stage change.  
**Problem statement**: After relocation, adults do not lack events. They lack emotional safety and a reliable structure to show up and return.

**Evidence (Survey 1, N=45)**
- 53% go alone when they have no partner; 36% give up or skip the activity.
- 40% rate "going alone" as hard/very hard (avg 3.27/5).

**User voice (Interview 1: Noa)**
- "It feels like an audition. I have to go in alone and perform."

**Visual**: `presentation/assets/survey_no_partner_behavior.png`  
**Sources**: `research/surveys/survey1_summary.md`, `research/interviews/interview_noa.md`

---

## Slide 3: Research Question (Evolution)
**Initial RQ**: Why do relocators fail to form new social ties even when apps and events exist?  
**Early signals**: People avoid going alone and fear awkwardness more than logistics.  
**Refined RQ**: Which mechanisms reduce emotional risk and “go-alone” friction to increase show-up and repeat meetings?  
**Success metrics**: show-up rate, repeat attendance (3–4 meetings), at least 1 meaningful connection.

---

## Slide 4: Research Plan (Phases + Methods + Tools)
**Phases**
- Market research
- Competitive analysis
- Customer/user research

**Research goals**
- Identify the core barriers to forming connections after relocation.
- Map the competitive landscape and trust mechanisms.
- Test willingness to verify and pay for reliability.

**Research questions**
- What stops people from attending social activities alone?
- Which trust signals make meeting strangers feel safe?
- What structures increase repeat attendance?
- What level of verification and payment is acceptable?

**Target audience**
- B2C: relocators and life-stage shifters (20s–30s) in large cities.

**Methods executed**
- Survey
- 3 Interviews
- Thematic coding summary.
- Desk research: market + competitors.

**Tools**
- Google Forms export + CSV analysis: `research/surveys/survey_responses_raw.csv`
- Sources index: `research/sources.md`

---

## Slide 5: Target Audience + Personas (B2C)
**Target audience**: relocators / expats / life-stage shifters (20s–30s) in large cities.

**Persona A — Relocator (high intent)**
- Profile: Omer, 32, relocated tech professional.
- Pain: high time cost + fear of awkward first meetings.
- Behavior: avoids swipe apps; drops off after 1–2 failed attempts.
- Need: reliable peers + low-friction first-meet structure.

**Persona B — Time-poor life-stage shifter **
- Profile: new job switcher / new parent / post-military (choose 1, based on Interview #2 or #3).
- Pain: cannot afford no-shows; avoids “random” open events.
- Need: commitment signals + predictable structure.

**Sources (Persona A draft)**: `research/synthetic/synthetic_interviews.md`

---

## Slide 6: Market Research (Context + Trends + Sizing)
**Why now**
- 281M global migrants (UN, 2020).
- 12.1% of US population moves annually (Census, 2023).
- 57% of 18–35 in Europe report moderate to severe loneliness (Bertelsmann, 2024).

**Willingness-to-pay anchors (B2C)**
- Timeleft: $16 per ticket.
- Soho Friends: $130/year.

**Market sizing (proxy TAM/SAM/SOM)**
- **TAM (global)**: 281M international migrants (UN, 2020).
- **SAM (annual movers, US proxy)**: 12.1% of population moves each year (Census, 2023).
- **SOM (city pilot proxy)**: Berlin annual inflow 187,971 (2023).

**Interpretation**: Start with one-city SOM, prove repeat attendance, expand city-by-city.

**Sources**: `research/data/key_metrics_wtp_proxies.csv`, `research/data/competitor_pricing.csv`, `research/sources.md`

---

## Slide 7: Competitive Analysis (Direct + Indirect)
**Direct competitors (B2C)**
- Bumble For Friends (open matching).
- Meetup (open events).
- Timeleft (curated events).

**Indirect competitors**
- WhatsApp/FB interest groups (low barrier, noisy).
- Premium clubs (Soho House; high curation).

**Key gap**
- Few solutions combine verification/reliability signals with a repeatable first-meet structure that reduces “go-alone” friction.

**Visual**: `presentation/assets/competitor_matrix.png`  
**TODO (visual/framework)**: add a 2×2 positioning map (Open↔Curated vs One-off↔Recurring).  
**Sources**: `research/competitors/competitor_matrix.md`, `research/data/competitor_pricing.csv`, `research/competitors/competitiors_comp.md`

---

## Slide 8: Customer/User Research — Key Findings (Quant, Survey 1)
**What people do when they have no partner (N=45)**
- 53% go alone.
- 36% give up or skip the activity.

**How hard is it to go alone?**
- 40% hard/very hard (avg 3.27/5).

**What makes people feel safe enough to meet? (open answers)**
- Video/phone call, real profile, mutual friends.

**So what?**
- The barrier is not event discovery; it’s the risk of the first attempt.

**Source**: `research/surveys/survey1_summary.md`

---

## Slide 9: Customer/User Research — Key Findings (Quant, Survey 2)
**Verification willingness (N=42, high-intent segment)**
- 68% willing to link LinkedIn.

**WTP**
- 22% would pay $5/month for “no flakes” + verified profiles.

**So what?**
- Verification is acceptable when it buys reliability.
- There is a premium early adopter segment.

**Source**: `research/surveys/survey2_summary.md`

---

## Slide 10: Customer/User Research — Interviews + Thematic Coding
**Requirement (course)**: at least 3 interviews + thematic coding summary.

**Interviews (status)**
- Interview #1 (done): Noa — relocator (user). `research/interviews/interview_noa.md`
- Interview #2 (TODO): relocator/expat in target age (user). *(add file + 3–5 quotes)*
- Interview #3 (TODO): life-stage shifter (user) **or** expert (community organizer). *(add file + 3–5 quotes)*

**Thematic coding summary (current draft)**
- Emotional safety > physical safety.
- Structure beats spontaneous mingling.
- Repeatability (3–4 meetings) is required for real ties.
- Micro-recognition: one meaningful moment drives belonging.

**TODO (quotes)**: add 1–2 quotes per theme (max ~6 total in the deck).  
**Source**: `research/Thematic coding.md`

---

## Slide 11: Synthesis (Insights -> Requirements)
**Key insights**
- People avoid social attempts when the emotional downside is high (awkwardness, “audition” feeling).
- Reliability is a product feature (commitment signals + repeated presence), not just a user trait.
- Trust is created by costly signals + clear structure, not by more matching.

**Product requirements**
- Reduce emotional risk of showing up alone.
- Provide a structured “first-meet” flow (so nobody walks in alone).
- Reward/ensure reliability (reduce no-shows, increase repeat meetings).
- Use light verification to set baseline trust.

---

## Slide 12: Product Concept (UVP + Core Loop)
**Unique value proposition**: “Reliable people, not random people.”

**Concept (B2C)**
- Verified onboarding (LinkedIn/photo) + clear rules.
- Reliability signals (commitment score / no-show friction).
- First-meet experience that reduces “go-alone” friction.

**Core loop**
1. Complete light verification (identity + context).
2. Match with a reliable peer or small group based on shared context.
3. Attend a first meeting with clear expectations.
4. Re-match based on reliability score and repeat attendance.

---

## Slide 13: MVP + Metrics + Risks
**MVP (one city)**
- Verified onboarding (LinkedIn + photo).
- Reliability signals (commitment score / no-show friction).
- Hosted first-meet flow + follow-up.

**Success metrics**
- Show-up rate.
- Repeat attendance (3–4 meetings).
- 1 meaningful connection per user (self-report).

**Risks**
- Cold start density.
- Privacy concerns.
- Commitment drop-off.

---

## Slide 14: Conclusion + Recommendation (Product Strategy)
**Conclusion**
- The main barrier is emotional safety and “go-alone” risk, not a lack of events.
- Surveys show avoidance behavior and concrete trust signal needs.
- The opportunity is a reliability layer: verification + commitment + repeat meetings.

**Recommendation (B2C)**
- Start with paid events → membership once repeat attendance is proven.
- Pricing anchors: Timeleft ($16 ticket), Soho Friends ($130/year).

**Optional recommendation (not changing project scope)**: B2B2C as a future distribution layer after B2C traction (HR value in months 3–6 relocation gap).

**Next validation (pilot plan, TODO thresholds)**
- Run 2–3 hosted first-meet events and measure show-up + repeat.
- Smoke-test WTP via ticket or refundable deposit.
- Define success thresholds for show-up and repeat rates.
