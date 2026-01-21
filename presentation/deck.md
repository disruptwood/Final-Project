# Final Project: Verified Connections for Relocators (B2C)
**Problem #12**: People struggle to build and maintain social connections after moving cities or life stages.

---

## Slide 1: Title and One-Liner
**Project**: Verified Connections  
**One-liner**: A trust- and structure-first way for relocators to build reliable social circles.  
**Team**: [Names]

---

## Slide 2: Problem Statement (Evidence First)
**Problem statement**: After relocation, adults do not lack events. They lack emotional safety and a reliable structure to show up and return.

**Evidence (survey N=45)**:
- 53% go alone when they have no partner; 36% give up or skip the activity.
- 40% rate "going alone" as hard/very hard (avg 3.27/5).

**User voice (AI-simulated interview)**:
- "It feels like an audition. I have to go in alone and perform." (Noa)

**Visual**: `presentation/assets/survey_no_partner_behavior.png`  
**Source**: `research/surveys/survey1_summary.md`, `research/interviews/interview_noa.md`

---

## Slide 3: Research Question (Evolution)
**Initial RQ**: Why do relocators fail to form new social ties even when apps and events exist?  
**Early signals**: People avoid going alone and fear awkwardness more than logistics.  
**Refined RQ**: Which mechanisms reduce emotional risk and "go-alone" friction to increase show-up and repeat meetings?  
**Success metrics**: show-up rate, repeat attendance (3-4 meetings), at least 1 meaningful connection.

---

## Slide 4: Research Plan (Goals, Questions, Methods)
**Goals**
- Identify the core barriers to forming connections after relocation.
- Map the competitive landscape and trust mechanisms.
- Test willingness to verify and pay for reliability.

**Research questions**
- What stops people from attending social activities alone?
- Which trust signals make meeting strangers feel safe?
- What structures increase repeat attendance?
- What level of verification and payment is acceptable?

**Target audience**
- B2C: relocators and life-stage shifters (20s-30s) in large cities.

**Methods**
- Survey 1 (N=45) on behavior and barriers.
- Survey 2 (N=42) concept validation (verification + WTP).
- AI-simulated interview (Noa); thematic coding draft for early insights.
- Desk research: market and competitor scan.

**Limitations**
- Self-selected samples; not representative.
- AI-simulated interview used for hypothesis generation only.

**Timeline**
- Week 1: market + competitors.
- Week 2: surveys + interviews + synthesis.

**Sources**: `research/surveys/survey1_summary.md`, `research/surveys/survey2_summary.md`, `research/interviews/interview_noa.md`, `research/competitors/competitor_matrix.md`

---

## Slide 5: Market Context (Why Now)
**Relocation scale**
- 281M global migrants (UN, 2020).
- 12.1% of US population moves annually (Census, 2023).

**People pay for curated social experiences**
- Timeleft dinner: $16 per ticket.
- Soho Friends membership: $130 per year.

**Trend: loneliness is high**
- 57% of 18-35 in Europe report moderate to severe loneliness (Bertelsmann, 2024).

**Implication**: Mobility creates demand, and curated social products prove willingness to pay.

**Sources**: `research/data/key_metrics_wtp_proxies.csv`, `research/data/competitor_pricing.csv`, `research/sources.md`

---

---

## Slide 6: Market Sizing (Proxy)
**TAM (global)**: 281M international migrants (UN, 2020)  
**SAM (annual movers, US proxy)**: 12.1% of population moves each year (Census, 2023)  
**SOM (city pilot proxy)**: Berlin annual inflow 187,971 (2023)

**Interpretation**: The addressable audience is large; we start with a single-city SOM and expand by city once repeat attendance is validated.

**Sources**: `research/data/key_metrics_wtp_proxies.csv`

---

## Slide 7: Competitive Landscape (B2C)
**Status quo**
- Open matching: Bumble For Friends.
- Open events: Meetup.
- Curated events: Timeleft.
- Premium clubs: Soho House.

**Gap**: Few solutions combine trust signals with a repeatable structure that lowers the "go-alone" risk.

**Visual**: `presentation/assets/competitor_matrix.png`  
**Sources**: `research/competitors/competitor_matrix.md`, `research/data/competitor_pricing.csv`

---

## Slide 8: Survey Insights (Behavior + WTP)
**Behavior**
- When no partner: 53% go alone; 36% give up or skip the activity.
- 40% rate going alone as hard/very hard.

**Trust signals (open responses)**
- Video/phone call, real profile, mutual friends.

**Concept validation (N=42, high-intent)**
- 68% willing to link LinkedIn for verification.
- 22% would pay $5/month for "no flakes" + verified profiles.

**Sources**: `research/surveys/survey1_summary.md`, `research/surveys/survey2_summary.md`

---

## Slide 9: Interview/Thematic Insights (Early)
**Theme 1: Emotional safety is the core barrier**
- "Apps feel unsafe emotionally, not physically." (Noa)

**Theme 2: Structure beats spontaneity**
- People avoid unstructured mingling; activity-based contexts reduce pressure.

**Theme 3: Repeatability builds trust**
- Connections form after several shared meetings.

**Theme 4: Micro-recognition matters**
- One meaningful interaction beats many shallow ones.

**Sources**: `research/interviews/interview_noa.md`, `research/Thematic coding.md`

---

## Slide 10: Persona and Journey (Synthesized)
**Persona**: Omer, 32, relocated tech professional.  
**Pain**: High time cost and social risk; avoids open events and swipe apps.  
**Need**: Reliable peers and a repeatable structure that makes showing up worth it.

**Journey pattern**
- Week 1: tries open events or groups, feels awkward and drops off.
- Months 3-6: "quiet loneliness" sets in and effort declines.

**Sources**: `research/synthetic/synthetic_interviews.md`, `research/Thematic coding.md`

---

## Slide 11: Synthesis -> Product Requirements and Concept
**If the product works, it must:**
- Reduce the emotional risk of showing up alone.
- Provide a structured activity as a social bridge.
- Create repeatable circles where faces become familiar.
- Use light verification to set baseline trust.

**Verified Connections (B2C)**: verified profiles + reliability signals that reduce flakiness and make first meetings safe.

**Core loop**
1. Complete light verification (identity + context).
2. Match with a reliable peer or small group based on shared context.
3. Attend a first meeting with clear expectations.
4. Re-match based on reliability score and repeat attendance.

**Key feature**: "Digital host" to pair newcomers before the first event.

---

## Slide 12: MVP, Metrics, Risks
**MVP**
- One city, verified onboarding (LinkedIn + photo).
- Reliability signals (commitment score / no-show friction).
- First-meet flow with clear expectations and follow-up.

**Success metrics**
- Show-up rate.
- Repeat attendance (3-4 meetings).
- 1 meaningful connection per user (self-report).

**Risks**
- Cold start density.
- Privacy concerns.
- Commitment drop-off.

---

## Slide 13: Business Model (Primary B2C, Optional B2B2C)
**Primary**: B2C paid events -> recurring membership once density is proven.  
**Pricing anchors**: Timeleft ($16 ticket), Soho Friends ($130/year).

**Optional recommendation**: B2B2C as a distribution layer after B2C traction (HR value in months 3-6 relocation gap).  
**Note**: This is secondary and does not change the B2C scope of the project.

**Sources**: `research/data/competitor_pricing.csv`, `research/Thematic coding.md`

---

## Slide 14: Conclusion
- The main barrier is emotional safety and "go-alone" risk, not a lack of events.
- Survey data shows clear avoidance behavior and trust signal needs.
- The solution is a trust-first, repeatable structure that makes people show up and return.
- Next step: run a small-city pilot and measure show-up + repeat.
