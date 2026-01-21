# Final Project: Verified Connections for Relocators (B2C)
**Problem #12**: People struggle to build and maintain social connections after moving cities or life stages.

---

## Slide 1: Title and One-Liner
**Project**: Verified Connections  
**One-liner**: Reduce first-meet risk and increase repeat meetings after relocation.  
**Team**: [Ilya, Nitzan, Ishay]

---

## Slide 2: The Problem (Primary Evidence)
**Problem statement**: After relocation, the main barrier is not “finding events” — it’s the risk of showing up alone and meeting strangers.

**Evidence (Survey 1, N=45)**
- 40% rate going alone as hard/very hard (avg 3.27/5).
- When there is no partner: 53% go alone; 36% give up or skip the activity.

**Visual**: `presentation/assets/survey_no_partner_behavior.png`  
**Sources**: `research/surveys/survey1_summary.md`, `research/surveys/survey_responses_raw.csv`

---

## Slide 3: Research Question (Evolution)
**Initial RQ**: Why do relocators fail to form new social ties even when apps and events exist?  
**After Survey 1**: The bottleneck looks like “go alone” + trust, not discovery.  
**Refined RQ**: Which mechanisms reduce first-meet risk and increase show-up + repeat meetings?

---

## Slide 4: Research Plan (What We Checked)
**Methods and checks**
- **Primary**: Survey 1 with raw export (N=45).
- **Secondary**: desk research (market context, competitors, pricing, academic framing).
- **Qual (mechanism exploration)**: 3 AI-simulated interviews + thematic coding (course AI interview methodology).

**Limitations (one line)**
- Only one non-synthetic primary dataset; interviews are AI personas used to generate hypotheses (not prevalence).

**Sources**: `research/flow - עד כה.md`, `research/sources.md`

---

## Slide 5: Target Audience + Personas (B2C)
**Target audience**: relocators / expats / life-stage shifters (20s–30s) in large cities.

**Persona A — Relocator (Struggling) — AI persona**
- Noa (29): fear of “walking in alone”, emotional safety barrier.

**Persona B — Relocator (What Works) — AI persona**
- Daniel (31): succeeds via structured frameworks and repeat attendance.

**Sources**: `from drive/ראיונות - רקע + תיעוד/ראיון עם נועה.docx`, `from drive/ראיונות - רקע + תיעוד/ראיון עם דניאל.docx`

---

## Slide 6: Market Research (Context + Sizing Proxy)
**Why now (context)**
- 281M global migrants (UN, 2020).
- 12.1% of US population moves annually (Census, 2023).
- 57% of 18–35 in Europe report moderate to severe loneliness (Bertelsmann, 2024).

**Sizing proxy (TAM/SAM/SOM)**
- TAM: 281M global migrants (stock).
- SAM: annual movers (US mobility proxy).
- SOM: Berlin inflow 187,971 (city pilot proxy).

**Sources**: `research/data/key_metrics_wtp_proxies.csv`, `research/sources.md`

---

## Slide 7: Competitive Analysis (Where the Gap Is)
**Landscape**
Goal: Show the main alternatives a relocator uses today, and the specific gap our product targets: reliability + emotional safety for the first meet + repeat.

Include these competitor types (pick 6–8 total):

Friend-matching apps: Bumble BFF, (optionally) Friender / Patook (if in your table)
Open event platforms: Meetup
Curated social dinners / paid events: Timeleft
Expat communities: InterNations
Local interest groups / chats: Facebook Groups / WhatsApp groups
Premium gated communities (WTP proof, not direct competitor): Soho House (optional)
Invite-only professional networks (optional, only if you keep as “premium gated” reference): Chief / YPO (appendix if needed)
Format (use a simple matrix, not a long table):
Columns = the barriers we measured + “real-world conversion”

Trust/Safety: identity checks, moderation, rules
Go-alone support: hosted entry / buddy / small-group default
Commitment: RSVP friction, penalties, reputation, membership
Repeatability: recurring cohorts / same faces / follow-up design
Offline conversion: designed to get people from online → meeting → repeat
Rows = competitors (from table of concurents from desk research.csv) + “Us”.

What to write (tight bullets under the matrix):

“Most options optimize discovery, not reliability: no-show and awkward first meet remain unsolved.”
“Curated communities prove people pay for safety/curation—but they’re expensive or not designed for relocators.”
“Opportunity: a B2C product that makes first meet safe + increases show-up + drives repeat.”

**Gap (our framing)**
- Few solutions combine trust/reliability signals with a repeatable first-meet structure that reduces “go-alone” friction.

**Visual**: `presentation/assets/competitor_matrix.png`  
**Sources**: `research/competitors/competitor_matrix.md`, `research/data/competitor_pricing.csv`

---

## Slide 8: Survey Insights (What “Safe Enough” Looks Like)
**Open answers (recurring patterns; not % claims)**
- Video/phone call
- Real/detailed profile
- Mutual friends

**Interpretation**
- Users look for concrete trust signals before meeting a stranger.

**Source**: `research/surveys/survey1_summary.md`

---

## Slide 9: Interviews + Thematic Coding (Mechanisms, Not Prevalence)
**What we did**
- 3 AI-simulated interviews (Noa, Daniel, Maya) + thematic coding.

**Mechanisms that explain the barrier**
- Emotional safety (“audition feeling”).
- Structure beats spontaneous mingling.
- Repeatability (3–4 meetings) converts strangers → familiar faces.
- Micro-recognition: one meaningful moment drives belonging.

**Sources**: `research/Thematic coding.md`, `from drive/ראיונות - רקע + תיעוד/Thematic coding.docx`, `from drive/ראיונות - רקע + תיעוד/ראיון עם מאיה.docx`

---

## Slide 10: Synthesis → Product Requirements
**Requirements derived from Survey + mechanisms + competitor scan**
- Reduce emotional risk of showing up alone.
- Provide a structured first-meet flow (so nobody walks in alone).
- Create reliability/commitment signals that reward repeat attendance.
- Support trust signals users already look for (real profile, pre-contact).

---

## Slide 11: Product Concept (B2C)
**Unique value proposition**: “Reliable people, not random people.”

**Concept**
- Verified onboarding (real-profile signals) + clear rules.
- Reliability signals (commitment score / no-show friction).
- Hosted first-meet experience + repeatable follow-ups.

**Core loop**
1. Verify (low-friction trust signals).
2. Get introduced (buddy/micro-group) before first meet.
3. Attend a structured first meet (clear expectations).
4. Repeat with higher reliability and familiar faces.

---

## Slide 12: MVP + Validation Plan (What We’d Do Next)
**MVP (one city)**
- Small recurring format + host flow.
- Light verification signals + clear rules.
- Reliability mechanism (deposit/refund or reputation).

**Success metrics**
- Show-up rate.
- Repeat attendance after 3–4 meetings.
- “1 meaningful connection” self-report.

---

## Slide 13: Final Conclusions (Honest + Defensible)
**What we can defend**
- In our survey sample, “go alone” and trust signals are central friction points after relocation.
- Competitors differ mainly by how they create trust and structure; the combined gap is “trust + repeatable first-meet structure”.

**Recommendation (B2C)**
- Build for first-meet de-risking and repeat attendance; validate via a small-city pilot with measurable show-up + repeat.

**Note**
- B2B2C appeared as a hypothesis in the AI HR interview, but the project remains B2C per course scope.
