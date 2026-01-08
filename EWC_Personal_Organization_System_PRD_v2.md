# EWC Personal Organization System
## Product Requirements Document

**Version:** 2.0
**Date:** January 3, 2026
**Author:** Consultant (Brandon Adams)
**Status:** Updated with Email Context

---

## Executive Summary

This document defines a comprehensive personal organization system for Edward Conard—a unified platform designed to optimize his time, maximize his impact, and support the legacy he is building. The system spans both professional and personal domains, connected by shared principles but implemented with distinct architectures appropriate to each.

**The core proposition:** EWC's scarcest resource is not money but time and attention. This system is designed to protect high-leverage activities (content production), minimize low-leverage friction (supervision, logistics, discovery), and create a feeling of effortless abundance across all life domains.

**Ed's Own Words (January 1, 2026):**
> "Every moment I spend acquiring input is a moment I don't spend producing output (or consuming the precious waning moments of my life). It seems impossible to strike a productive balance without reducing the amount of input."

> "I think we need to work backwards from desired output to highly constrained input. I feel enslaved to input and daily tasks that I shouldn't be the one to do."

---

## Table of Contents

1. [Client Context](#1-client-context)
2. [Ed's Core Arguments](#2-eds-core-arguments)
3. [Utility Function](#3-utility-function)
4. [System Architecture Overview](#4-system-architecture-overview)
5. [Professional System](#5-professional-system)
6. [Content Marketing System](#6-content-marketing-system)
7. [Personal System](#7-personal-system)
8. [Integration Layer](#8-integration-layer)
9. [Design Principles](#9-design-principles)
10. [Ed's Voice & Style Guide](#10-eds-voice--style-guide)
11. [Implementation Status & Roadmap](#11-implementation-status--roadmap)
12. [Open Questions](#12-open-questions)
13. [Appendices](#13-appendices)

---

## 1. Client Context

### 1.1 Who Is Edward Conard

- **Background:** Former founding partner of Bain Capital; worked closely with Mitt Romney
- **Current Role:** Adjunct Fellow at American Enterprise Institute; author and public intellectual
- **Published Works:**
  - *Unintended Consequences: Why Everything You've Been Told About the Economy Is Wrong* (2012) — NYT Top 10 Bestseller
  - *The Upside of Inequality: How Good Intentions Undermine the Middle Class* (2016) — NYT Top 10 Bestseller, #1 NYT Business
  - Contributor to Oxford University Press's *United States Income, Wealth, Consumption, and Inequality* (2020)
- **Public Presence:** 250+ media appearances (CNN, ABC, CBS, Fox, CNBC, Bloomberg, BBC); debates with Krugman, Stiglitz, Furman; The Daily Show with Jon Stewart
- **Focus Areas:** Economics, inequality, innovation, trade deficits, growth in high-wage economies; challenging conventional economic thinking

### 1.2 Current Operations

| Operation | Description | Status |
|-----------|-------------|--------|
| **Macro Roundup** | Daily curated summary of significant economic news | Operational, ~4,000 subscribers |
| **Weekly Roundup** | Saturday best-of summary | Operational |
| **Special Editions** | Thematic deep-dives (e.g., Thanksgiving edition) | Occasional |
| **OpEd Production** | Commentary in WSJ, NYT, Washington Post, Foreign Affairs | Active |
| **Website** | edwardconard.com | Operational |
| **Twitter/X** | @EdwardConard | Underutilized |

### 1.3 Operating Team

| Role | Person | Function |
|------|--------|----------|
| **Principal** | Ed Conard | Strategic direction, content production, final decisions |
| **Chief of Staff** | Niki Stellings-Hertzberg | Chief of Staff, marketing, operations, logistics |
| **Consultant** | Brandon Adams | System design, complexity management, AI implementation |
| **Staff** | Steven Bogden | Macro Roundup production, research support, article selection |
| **Technical** | Anthony Shafto | Neo4j database, website infrastructure, technical implementation |
| **Admin** | Caroline Conceison | Executive assistant, scheduling, HubSpot SuperAdmin |

---

## 2. Ed's Core Arguments

The AI system has identified Ed's 10 foundational arguments from his body of work. These serve as the organizing framework for the Zingers system and must inform all AI-generated content.

### 2.1 The Ten Arguments

| # | Argument | Description |
|---|----------|-------------|
| **1** | **5-to-1 Value Creation Ratio** | Entrepreneurs and investors capture only ~$1 for every $5 of value they create for society. Most gains flow to consumers and workers. This is Ed's foundational defense of high incomes at the top. |
| **2** | **Equity Investment Drives Productivity** | Unlike debt-financed consumption, equity capital deployed into uncertain ventures is what moves productivity forward. The US has significantly more risk-tolerant capital than Europe or Japan. |
| **3** | **Talent is the Binding Constraint** | The limiting factor for growth is not capital but skilled workers who can commercialize innovation. Money alone cannot substitute for human capital. |
| **4** | **Trade Deficits Export Unemployment** | Chronic surplus countries (Germany, China, Japan) export their "paradox of thrift" to the US. Trade deficits represent foreign savings funding American consumption rather than productive investment. |
| **5** | **Financial Crisis = Savings Glut** | The 2008 crisis resulted from a global flood of risk-averse savings seeking "safe" assets. Government housing policy channeled this into subprime. Blaming banker greed misdiagnoses the cause. |
| **6** | **Inequality = Byproduct of Value Creation** | High incomes at the top mostly reflect genuine economic contribution, not rent-seeking. Redistribution diminishes incentives for risk-taking that drives broadly shared prosperity. |
| **7** | **Europe/Japan = Risk Aversion** | Slower growth stems from cultural/institutional unwillingness to deploy equity capital into uncertain ventures. They save adequately but allocate into debt, not equity. |
| **8** | **Short-Termism Overstated** | Markets reward long-term investment when it genuinely creates value. The critique that quarterly earnings pressure forces destructive short-term thinking is largely unfounded. |
| **9** | **High-Skilled Immigration Helps** | High-skilled immigrants create substantial value and don't compete with low-wage American workers. Low-skilled immigration hurts American workers. This is labor economics, not xenophobia. |
| **10** | **Stimulus vs. Austerity = Wrong Debate** | The real question is whether policies increase equity investment in risky, productivity-enhancing ventures. Aggregate demand management cannot solve structural capital allocation problems. |

### 2.2 Key Nuances Ed Emphasizes

**On Taxes and Risk-Taking (December 23, 2025):**
> "A key nuance in my argument about taxes is that they reduce the expected after-tax value of risk-taking **before** an investment or decision to take-risk is made and that the lower after-tax expected value, and not the taxes per se, reduces risk-taking."

**On the Counterfactual:**
> "All that matters is relative to a counterfactual that no one sees or considers (except me). I try to show Europe as a glimpse of the counterfactual where lower expected returns equal near-zero-risk-taking."

**Ex Ante vs. Ex Post (critical distinction):**
> "Optimal tax policy isn't designed to motivate post-hoc billionaires like Musk. The goal is to motivate talented young people ex-ante to take the risk to buy one-in-a-million lottery tickets—to motivate a large pool of failure from which a small amount of success arises."

---

## 3. Utility Function

### 3.1 Priority Hierarchy

| Rank | Value | Description |
|------|-------|-------------|
| 1 | **Time** | The scarcest resource; must be protected and allocated to highest-leverage activities |
| 2 | **Impact** | What is accomplished with that time; influence on economic policy discourse |
| 3 | **Legacy** | Long-term compounding of impact; books, ideas that persist |

### 3.2 Pain Points

| Pain Point | Description | Ed's Words |
|------------|-------------|------------|
| **Input Overload** | Too much to read/consume relative to output | "I feel enslaved to input and daily tasks" |
| **Supervision Overhead** | Time spent on check-ins and oversight | Drains time from content production |
| **Content Production Friction** | Path from idea to published OpEd has friction | Needs AI assistance but current drafts are "too aggressive" |
| **Experience Optimization** | Not maximizing life experiences | "Not yet maximizing the full potential" |
| **Signal-to-Noise** | Valuable information buried in noise | "The internet has filled the world with valuable information but buried it under a sea of noise" |

### 3.3 Preferences

**On Delegation:**
- Comfortable delegating; wants clean handoffs with minimal supervision
- Concerned about work plan alignment: "I'm concerned about whether we are executing on a mutually agreed upon work plan and arrival destination(s)." (December 23, 2025)

**On Information Consumption:**
- Prefers ~750 character summaries (flexible if needed)
- "The key insight that you think I could use or incorporate into my work"
- Shannon principle: "Insight needs to be wrapped in enough redundancy to be understood, but there was much more redundancy than was necessary"

**On Analytics:**
- Enjoys deep-dives into marketing analytics, even if not optimal time use
- "We have performance data, but we aren't learning anything from it. How do we learn something?" (October 12, 2025)

**On AI and Slop (December 15, 2025):**
> "I think it's mistaken to assume that anything created by AI is necessarily slop. What could make it not-slop is the curation of the books and the story that it tells."

> "I'm always trying to solve the same problem—curating extremely high signal-to-noise for the things that interest me."

> "Ideally, AI would understand what I want—i.e., why I want it, which I don't fully understand—and then find it for me."

---

## 4. System Architecture Overview

### 4.1 Three Engines, One System

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       UNIFIED ORGANIZATION SYSTEM                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   ┌─────────────────────┐   ┌─────────────────────┐   ┌─────────────────┐  │
│   │   PROFESSIONAL      │   │  CONTENT MARKETING  │   │    PERSONAL     │  │
│   │      ENGINE         │   │       ENGINE        │   │     ENGINE      │  │
│   │                     │   │                     │   │                 │  │
│   │  Neo4j Database     │   │  HubSpot Analytics  │   │  Category-Based │  │
│   │  (Macro Roundup)    │   │  (4,000 subs)       │   │  Structure      │  │
│   │        ↓            │   │        ↓            │   │        ↓        │  │
│   │  Zingers System     │   │  Segmentation       │   │  Discovery      │  │
│   │        ↓            │   │        ↓            │   │  Engine         │  │
│   │  OpEd Pipeline      │   │  Growth Strategy    │   │        ↓        │  │
│   │                     │   │                     │   │  Execution      │  │
│   └──────────┬──────────┘   └──────────┬──────────┘   └────────┬────────┘  │
│              │                         │                        │           │
│              └─────────────────────────┼────────────────────────┘           │
│                                        │                                     │
│                         ┌──────────────▼──────────────┐                     │
│                         │     INTEGRATION LAYER       │                     │
│                         │                             │                     │
│                         │  - Unified Calendar         │                     │
│                         │  - Time Protection          │                     │
│                         │  - Decision Queue           │                     │
│                         │  - Compressed View (Ed)     │                     │
│                         │  - Full View (Consultant)   │                     │
│                         └─────────────────────────────┘                     │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 4.2 Role-Based Views

| User | View | Purpose |
|------|------|---------|
| **Principal (Ed)** | Compressed | Only what needs his attention; decisions, content calendar, curated options |
| **Consultant (Brandon)** | Full Complexity | All moving pieces, delegated items, system health, pipeline status |

---

## 5. Professional System

### 5.1 Core Objective

Transform the Macro Roundup consumption engine into a content production pipeline that generates OpEds in Ed's voice with minimal friction, while monitoring the marketplace for strategic opportunities.

### 5.2 Macro Roundup

#### 5.2.1 Current State

| Attribute | Detail |
|-----------|--------|
| **Format** | Daily curated summary of economic news |
| **Distribution** | ~4,000 subscribers via HubSpot |
| **Weekly Edition** | Saturdays, best-of summary |
| **Special Editions** | Occasional thematic deep-dives |
| **Website** | edwardconard.com |

#### 5.2.2 Content Philosophy

**Ed's View (October 3, 2025):**
> "I often think we skew too much to finance and not enough to hardcore social policy and policy math... and that we are focused on too narrow a set of (financial) bloggers."

**Content Expansion Goals:**
- Less finance skew, more hardcore social policy and "policy math"
- Broaden beyond narrow set of financial bloggers
- More authors, greater diversity
- Systematically try 1-2 new contributors per week
- Scour every think tank's daily newsletters
- Ed asks: "Could AI write something like Jim Friedman's WSJ Best of the Web column?"

**What the Roundup Should Be About:**
> "One of the many reasons the Roundup was created was to find quotes that change one's view of the world and can win an argument with a single well-placed sentence." (December 5, 2025)

Example of what Ed values:
> "The maximum Social Security benefit, which today approaches $100,000 per year for a high-income couple, is two to four times higher in dollar terms than is paid in these other countries."

### 5.3 Neo4j Database

#### 5.3.1 Technical Specifications

| Component | Detail |
|-----------|--------|
| **Database** | Neo4j Graph Database |
| **Articles** | ~1,762 with PDFs |
| **Entries** | 6,157+ with embeddings |
| **Vector Embeddings** | 1,536-dimensional (OpenAI text-embedding-3-small) |
| **Relationships** | 44,885 manually tagged `:RELATED_TO` relationships |
| **Status** | Operational, Claude Code-interrogable |

#### 5.3.2 Existing AI Capabilities (Ed Not Yet Aware)

| Feature | Status | Description |
|---------|--------|-------------|
| **Human-AI Overlap Analysis** | Live | Shows where human curation and AI-discovered similarity agree/diverge |
| **AI-Discovered Similar Articles** | Live | Vector similarity search on every article |
| **Overlap Rate Metric** | Live | Bidirectional comparison metric |

**Interpretation of Overlap:**
- High overlap (70%+): Semantically tight topics, tag well-defined
- Low overlap (<30%): Human expertise finding contextual connections AI misses

#### 5.3.3 Taxonomy (15 Main Categories)

1. Macro & Growth
2. Inflation & Prices
3. Labor & Demographics
4. Productivity, Innovation & Technology
5. Financial Markets (deep granularity: Rates, Credit, Equities, FX, Commodities, Vol, Microstructure, Real Assets)
6. Banks, Intermediation & Financial Stability
7. Monetary Policy & Central Banking
8. Fiscal Policy & Public Finance
9. Trade, Globalization & Industrial Policy
10. Sectors & Real Economy
11. Energy, Environment & Climate
12. Health, Aging & Healthcare
13. Inequality, Poverty & Mobility
14. Politics, Institutions & Governance
15. Geopolitics & Security

**Cross-Cutting Facets:** Region, Time Period, Asset Class, Policy Lever, Evidence Type, Format, Data Source, Entity tags, Stance

#### 5.3.4 Tagging Challenges

**Ed's Observation (December 6, 2025):**
> "'Growth' is too broad of a tag or at least it is used too loosely. The first entry, for example, is not really about growth... It's a hodge podge of stuff—interesting but not coherent."

**Subtheme Discovery:**
> "As you look down the list of entries, you can start to see subthemes/sub tags/special editions (e.g., AI crowding out other investments, comparison to Europe, problems plaguing Germany, productivity growth, past vs future)."

**The Hard Problem (November 16, 2025):**
> "I don't see how AI can select articles without an (our/Steve's) understanding of that (micro) topic. That would presumably come from looking at the history of articles related to that micro topic."

> "Prompt engineering within a topic may be as complicated as identifying and writing down the very complex set of interconnected if-then rules we use to sort the signal from the noise."

### 5.4 Zingers System

#### 5.4.1 Concept

**Ed's Definition (December 5, 2025):**
> "Quotes that change one's view of the world and can win an argument with a single well-placed sentence."

**Examples:**
- "Onshore wind turbines in Germany produce around one-fifth of their total theoretical output. Solar panels in Germany and the U.K. use only around 10% of their total theoretical output."
- "The cost of the transition has never been admitted or recognized... There is a massive dishonesty involved." — Gordon Hughes

#### 5.4.2 Current Implementation

| Metric | Value |
|--------|-------|
| **Total Zingers Extracted** | 2,434 |
| **PDFs Processed** | 1,762 |
| **Rate** | ~1.6 zingers per article |
| **Categorization** | By Ed's 10 core arguments |

**Zingers by Argument:**
| Argument | Count |
|----------|-------|
| Equity Investment (#2) | 140 |
| Trade Deficits (#4) | 87 |
| Talent Constraint (#3) | 83 |
| Inequality (#6) | 80 |
| Europe/Japan (#7) | 62 |
| Stimulus/Austerity (#10) | 50 |
| Value Creation (#1) | 45 |
| Financial Crisis (#5) | 42 |
| Short-Termism (#8) | 22 |
| Immigration (#9) | 21 |

#### 5.4.3 Scoring Criteria (20 points each)

| Criterion | What It Measures |
|-----------|------------------|
| **Brevity & Punch** | Short, quotable, one-breath delivery |
| **Specific Facts** | Concrete numbers, percentages, comparisons |
| **Surprise Factor** | "Wait, really?" — counterintuitive beats obvious |
| **Credibility** | Attribution to credible source |
| **Argument Support** | Directly supports Ed's position, undermines progressive assumptions |

#### 5.4.4 Zinger CLI Tool

```
python zinger_cli.py search "immigration"
```
Returns rank-ordered zingers on any topic from entire database.

**Future State:** Slash command `/zinger renewables` or app interface.

### 5.5 OpEd Pipeline

#### 5.5.1 Pipeline Stages

| Stage | Description | Owner | Status |
|-------|-------------|-------|--------|
| **Idea Capture** | Raw topic, triggered by MR content or market signal | System/Consultant | Operational |
| **Research Package** | Relevant data, sources, prior positions, zingers assembled | AI Agent | In Development |
| **Draft** | Full OpEd draft in Ed's voice | AI Agent | Prototype |
| **Review** | Ed reviews, edits, refines | Principal | Manual |
| **Pitch/Submit** | Sent to publication | Consultant/Staff | Manual |
| **Published** | Live | — | — |
| **Archive** | Added to body of work | System | — |

#### 5.5.2 AI Draft Quality Assessment

**Ed's Feedback (December 19, 2025):**
> "Wow. Surprisingly good, especially for a first cut... But too aggressive, overstates the arguments (like the popular press), it would take substantial of my time to make this publishable under my name."

> "Perhaps we should create a pseudonym and blast the world!"

**Ed's Deeper Concern (December 23, 2025):**
> "I think it needs a deeper understanding of my arguments—both modularity and zingers (single sentence arguments). It makes arguments and they are related to my arguments but I don't think they would persuade a skeptic/close the holes in their counter arguments."

**Calibration Needed:**
- Less aggressive tone
- More modulated certainty
- Deeper argument structure (not just surface-level)
- Must address and defeat typical counterarguments
- Integrate zingers naturally

#### 5.5.3 Required: OpEd "Skill"

A dedicated OpEd generation skill needs development that:
- Understands Ed's 10 core arguments at deep level
- Pulls relevant zingers from database
- Matches Ed's voice and certainty modulation
- Anticipates and defeats counterarguments
- Produces drafts requiring minimal Ed revision

### 5.6 Special Editions

#### 5.6.1 Concept

Thematic, curated editions of the Macro Roundup around a coherent topic. Example: Thanksgiving "Reasons for Thankfulness" edition on US economic outperformance.

**Ed's Ambition (November 27, 2025):**
> "I can't help but wonder whether the distribution of our special editions shouldn't be much wider. The whole world should see this edition."

#### 5.6.2 Special Edition Candidates

Identified from database subthemes:
- AI crowding out other investments
- Comparison to Europe
- Problems plaguing Germany
- Productivity growth (past vs future)
- US debt crisis building
- Electricity as bottleneck to AI usage

#### 5.6.3 The Discovery Problem

**Ed's Question (October 30, 2025):**
> "I'm still scratching my head about how AI is going to find insightful tags that comprise worthy special editions such as 'we are at the start of a debt crisis,' or 'electricity is a bottleneck to AI usage,' without us supplying them."

---

## 6. Content Marketing System

### 6.1 Distribution Channels

| Channel | Subscribers | Frequency | Status |
|---------|-------------|-----------|--------|
| **Daily Roundup** | ~4,000 | Daily | Operational |
| **Weekly Roundup** | ~4,000 | Saturdays | Operational |
| **Special Editions** | ~4,000 | Occasional | Operational |
| **Twitter/X** | @EdwardConard | Underutilized | Needs scheduled system |

### 6.2 Two Strategic Problems

| Problem | Current State | Priority |
|---------|---------------|----------|
| **Retention/Optimization** | Halfway reasonable | Maintain |
| **Growth/Acquisition** | Very poor — not adding new subscribers | **High priority, needs ideas** |

**Growth Ideas to Explore:**
- Purchasing targeted email lists (economics/policy interested audiences)
- Advertising with TLDR Tech newsletters (tldr.tech)
- Wider distribution of Special Editions
- Twitter engagement strategy

### 6.3 Marketing Segmentation Framework

#### 6.3.1 Primary: Profession/Role

| Segment | Treatment |
|---------|-----------|
| **Journalists** | PR-focused, newsworthy content |
| **Policymakers** | Policy briefs, legislative implications |
| **Economists** | Research-focused, data-heavy |
| **Investors** | Market implications, investment angles |
| **Other Influencers** | Thought leadership positioning |

#### 6.3.2 Secondary: Relationship Tier

| Tier | Description | Approach |
|------|-------------|----------|
| **Tier 1: Friends** | Personal relationship with Ed | Direct, personal outreach |
| **Tier 2: Aware** | Know who Ed is, have engaged | Warm outreach, reference past interaction |
| **Tier 3: Unknown** | No prior awareness | Cold outreach, establish credibility |

**Requires Ed's Input:** Classification of contacts into Friends/Aware/Unknown

#### 6.3.3 Tertiary: Influence/Audience

| Level | Examples | Value |
|-------|----------|-------|
| **High Audience** | Major media byline, 50k+ Twitter followers, top-20 professor | Very high — amplification potential |
| **Medium Audience** | Regional/trade media, published author, think tank fellow | High — targeted impact |
| **Low/Consumer** | No public platform, junior positions | Standard — direct reader value |

#### 6.3.4 Accessibility Matrix

| Accessibility | Strategy |
|---------------|----------|
| **Easy** | Direct outreach |
| **Medium** | Warm intro, value proposition |
| **Difficult** | Long-term relationship building |

**Ed's Example (November 26, 2025):**
> "We are also going to need to differentiate people by not only their importance but also the difficulty of reaching (Paul Gigot will be much harder to reach than Larry Summers)."

### 6.4 Analytics System

**Ed's Frustration (October 12, 2025):**
> "We have performance data, but we aren't learning anything from it. How do we learn something?"

> "I long for the day when we can segment users by their level of engagement and see performance numbers by segment."

**Required Capabilities:**
- Email campaign performance analytics (HubSpot)
- Website analytics (edwardconard.com)
- Google Search Console integration
- User segmentation by engagement level
- AI-flagged high/low performing entries with explanations
- Differentiate Apple vs. non-Apple recipients (engagement signal differs)

**Note:** Ed enjoys analytics deep-dives even if not optimal time use. System should accommodate this preference.

---

## 7. Personal System

### 7.1 Core Objective

Create a friction-free experience layer where Ed always knows about the best options (restaurants, shows, books, conferences, experiences, goods) and can execute on them effortlessly. The system learns his preferences over time and proactively surfaces opportunities.

### 7.2 Philosophical Foundation

**Ed's Core Problem (December 15, 2025):**
> "I'm always trying to solve the same problem—curating extremely high signal-to-noise for the things that interest me. I have a very limited amount of time. So, when I do something (read, for example) I want it optimized relative to all the other ways that I could spend my time."

**The Journey, Not the Destination:**
> "He's not trying to reach some end state of satisfaction. The continuous stream of excellent options is the point."

### 7.3 The List — Restaurant System

#### 7.3.1 Non-Substitution Principle

**Ed's Foundational Rule (December 4, 2025):**
> "Rather than summing up all the different ways to differentiate (e.g., score) something, it's overwhelmingly more valuable and insightful to leave the relevant criteria segmented."

> "A 3-star is not a substitute for a delicious grilled ham and cheese sandwich from EAT a block from my house on Saturday for lunch."

#### 7.3.2 Dining Categories

| Category | Use Case | Distance Sensitivity |
|----------|----------|---------------------|
| **Fine Dining / Destination** | Special occasions, tasting menus, Michelin-starred | Low — worth traveling |
| **Scene / Going Out** | Buzzy, groups, Friday night downtown | Medium |
| **Date Night** | Intimate, conversation-friendly (NOT pure sushi, NOT loud) | Medium |
| **Neighborhood Comfort (UES)** | Nearby, reliable, don't need to impress | High |
| **Quick / Casual** | Lunch, easy weeknight, walk-in friendly | Very high |
| **Discovery / Unknown** | New spots, under-radar, never visited | Variable |

#### 7.3.3 What Ed Actually Needs

| Need | Current Gap |
|------|-------------|
| **New/Unknown vs. Known** | System shows only well-known places |
| **Bookable NOW vs. Advance Planning** | No availability layer |
| **Last-Minute Availability** | Missing entirely |
| **Distance Sensitivity by Context** | Aggregated into single score |
| **Friday vs. Saturday Differentiation** | Not distinguished |
| **Scheduling Criteria** | "The much harder part" |

**Ed's Framework:**
> "Ultimately what you want is a relevantly sorted list (not substitutable) with rank ordering within the list where new with noteworthy additions land near the top."

**The Hardest Parts (per Ed):**
1. Getting hard-to-get reservations
2. Planning ahead
3. Knowing WHICH TYPE to book, especially last minute

#### 7.3.4 Booking Philosophy

**Ed's Position:** Optimal system should NOT involve canceling a lot of reservations.

**Brandon's Counter-View:** At ~$500/person average spend, the high-value customer status likely trumps cancellation concerns.

**Design Decision:** Track cancellation frequency; favor rebooking at places where cancellations occurred less recently.

#### 7.3.5 Reservation Marketplace

| Service | Notes |
|---------|-------|
| **Jeanie Voltsinis / The Vault** | Concierge option (Rod uses) |
| **Cita** | Best for last-minute |
| **Appointment Trader** | Reservation resale |
| **Dorsia** | Last-minute, requires active usage |

**Legal Context:** NY Restaurant Reservation Anti-Piracy Law (Feb 2025) bans third-party reservation sales without restaurant contract.

#### 7.3.6 Wife Constraints

- Date nights: Avoid pure sushi, avoid loud scene-forward places
- Need: Intimate, conversation-friendly, quality food

### 7.4 Source Trust Hierarchy

**Ed's Rule (December 4, 2025):**
> "Who says a restaurant is good matters. Most recommendations are for sale. You show up and the place sucks."

| Tier | Trust Level | Examples |
|------|-------------|----------|
| **Tier 1** | Highest | Michelin, NYT critics (Pete Wells) |
| **Tier 2** | High | Infatuation, Eater (editorial), WSJ, NY Mag, Time Out |
| **Excluded** | None | Yelp, Google reviews, sponsored content |

### 7.5 "2 AM Principal" Experiences

**Concept (from John Levy book, December 14, 2025):**
> "A great night out on the town with friends should include the preplanned illusion of a spontaneous event that is surprising, exhilarating, dangerous, and satisfying."

**Ed's Observation:** The book develops criteria but never provides actual NYC ideas. Google AI suggestions were "lame."

**Status:** Project initiated, deliverables pending.

### 7.6 Expanded Personal System

**Ed's Additional Requests (December 15, 2025):**

| Category | Description | Status |
|----------|-------------|--------|
| **Lifestyle Websites** | Sources for "rich old male New Yorkers" including paywalls | Source list compiled (Appendix E) |
| **Weekly Book Summaries** | 800-1000 words, esoteric nonfiction, high signal-to-noise | Not started |
| **"Rules for Living"** | Daily/weekly brilliant rules for business/personal life | Not started |
| **Sunday Edition** | Combining lifestyle content | Concept only |
| **Complexity Textbook** | Fund undergraduate textbook on evolution of complexity | Requires author identification |

### 7.7 Output Cadence

| Output | Frequency | Purpose |
|--------|-----------|---------|
| **Category Guides** | Monthly | Reference material, NEW additions highlighted |
| **Weekly Digest** | Weekly | What's available/bookable this week |
| **Opportunity Alerts** | As-needed | Time-sensitive (cancellations, limited availability) |
| **Event Horizon** | Monthly | Upcoming conferences, shows, events worth planning for |

---

## 8. Integration Layer

### 8.1 Unified Calendar

Both professional and personal systems feed into a single calendar that:
- Protects content production time (sacred blocks for writing)
- Prevents double-booking across domains
- Shows Ed only what he needs to see (decisions, commitments)
- Shows Consultant the full picture (all items, statuses, logistics)

### 8.2 Decision Queue

A single stream of items requiring Ed's input:

| Type | Source | Example |
|------|--------|---------|
| **Content Decision** | Professional | "Review this OpEd draft" |
| **Experience Decision** | Personal | "Le Bernardin has an opening Saturday—book?" |
| **Strategic Decision** | Either | "Invitation to speak at X conference" |

### 8.3 Time Protection

| Block Type | Purpose | Protection Level |
|------------|---------|------------------|
| **Writing Time** | OpEd and book production | Highest — do not interrupt |
| **Review Time** | Content review, decision-making | High — batch decisions here |
| **Open Time** | Meetings, calls, flexible | Normal |
| **Personal Time** | Dining, experiences, rest | Respect boundaries |

### 8.4 Exception-Based Surfacing

**Default:** Ed does not see operational details

**Exception:** Surface only when:
- A decision is required
- Something is off-track and needs his input
- An opportunity is time-sensitive
- A commitment needs confirmation

---

## 9. Design Principles

### 9.1 For the System as a Whole

| Principle | Description |
|-----------|-------------|
| **Unified at the top, distinct underneath** | One system, three engines; connected by calendar and decision queue |
| **Protect high-leverage time** | Content production is sacred; supervision is waste |
| **Proactive, not reactive** | Surface opportunities before he asks |
| **Exception-based** | Don't show what's working; show what needs attention |
| **Learning** | System improves over time based on feedback |
| **Work plan transparency** | Clear deliverables and destinations visible to Ed |

### 9.2 For the Professional System

| Principle | Description |
|-----------|-------------|
| **Consumption feeds production** | Macro Roundup is fuel for OpEds |
| **AI as first draft** | Ed refines, not writes from scratch |
| **Market awareness** | Know where demand exists for his perspective |
| **Voice consistency** | AI output must match Ed's voice, not be "too aggressive" |
| **Argument depth** | AI must understand arguments deeply enough to defeat counterarguments |
| **Explainability** | AI must articulate reasoning in "principles and exceptions" |

### 9.3 For the Personal System

| Principle | Description |
|-----------|-------------|
| **Categories don't substitute** | Fine dining ≠ neighborhood comfort; never rank across |
| **Availability is the constraint** | He knows what's good; scheduling is the friction |
| **Source transparency** | Every recommendation shows where it came from |
| **The journey is the point** | Continuous stream of excellent options, not a destination |
| **Frictionless execution** | When he says yes, it just happens |

### 9.4 For Communication

| Principle | Ed's Words |
|-----------|------------|
| **Optimal summary length** | ~750 characters, flexible if needed |
| **Shannon principle** | "Edit out a large share of the unnecessary redundancy" |
| **Key insight focus** | "The key insight that you think I could use or incorporate into my work" |
| **Significant digits** | Round to meaningful precision (23.6% → 24%) |

---

## 10. Ed's Voice & Style Guide

### 10.1 For AI Content Generation

| Attribute | Guideline |
|-----------|-----------|
| **Tone** | Measured, not aggressive (current AI drafts are "too aggressive") |
| **Certainty** | Modulate appropriately; don't overstate |
| **Data** | Specific percentages, round to significant digits |
| **Counterfactuals** | Always reference what would otherwise be (Europe as glimpse) |
| **Ex ante focus** | Emphasize decisions before outcomes, not billionaires after |
| **Counterarguments** | Must anticipate and defeat typical objections |
| **Audience** | Primarily economists, not general public |

### 10.2 Rhetorical Philosophy

**Ed's Self-Description (December 23, 2025):**
> "My rhetorical style is driven by the substance of my arguments and the typical counter arguments—arguments I think are lame, but others, who haven't given it much thought, nevertheless find persuasive, and therefore must be defeated."

> "To view my arguments through the lens of my rhetorical style is to wag the dog by the tail. My style is driven by the (quality/strength) of my arguments... and the need to defeat common misperceptions."

### 10.3 Key Mantras

> "The purpose of thinking is to stop thinking."

> "Proof is absence of imagination."

> "The world is smeared in a thick coating of propaganda because when people find an argument that they mistakenly think justifies their desired conclusion, they stop thinking."

### 10.4 Number Presentation

> "I often say X and not about X because I try to first round numbers (to significant digits). 23.6% of GDP becomes 24%. My view is that people can't remember fractions and that fractions over-represent the true accuracy of numbers."

---

## 11. Implementation Status & Roadmap

### 11.1 Current Status (as of January 3, 2026)

#### Professional System

| Component | Status | Notes |
|-----------|--------|-------|
| Neo4j Database | **Operational** | 6,157+ articles, vector embeddings, Claude-interrogable |
| Zingers Extraction | **Complete** | 2,434 zingers, scored, categorized by 10 arguments |
| Zinger CLI Tool | **Prototype** | Command-line search functional |
| AI OpEd Generation | **Prototype** | Works but needs voice calibration |
| Human-AI Overlap Analysis | **Live** | Ed not yet aware |
| Taxonomy (15 categories) | **Defined** | Cross-cutting facets implemented |
| Special Editions | **Manual** | No automated identification yet |

#### Content Marketing System

| Component | Status | Notes |
|-----------|--------|-------|
| HubSpot Integration | **Operational** | ~4,000 subscribers |
| Segmentation Framework | **Designed** | Awaiting Ed's relationship tier input |
| Analytics Dashboard | **Partial** | Basic metrics, not insight-generating |
| Twitter Scheduling | **Not Built** | Identified as gap |
| Growth Strategy | **Gap** | "Very poor" per assessment |

#### Personal System

| Component | Status | Notes |
|-----------|--------|-------|
| The List v3 | **Design Complete** | ~20 restaurants curated, HTML template built |
| Restaurant Database | **Not Built** | — |
| Availability Checking | **Not Built** | Resy/OpenTable integration pending |
| 2AM Principal | **Initiated** | Deliverables pending |
| January Recommendations | **Pending** | Ed noted as missing (Dec 23) |
| Lifestyle Sources | **Compiled** | See Appendix E |
| Book Summaries | **Not Started** | — |

### 11.2 Immediate Priorities (Ed's Dec 23 Feedback)

1. **"2AM Surprises"** — Deliver NYC experience ideas
2. **January Recommendations** — Personal system output for January
3. **Database Insights** — AI to articulate dimensions/topics from Neo4j
4. **OpEd Voice Calibration** — Deeper argument understanding, not surface-level
5. **Work Plan Alignment** — Clear deliverables and destinations

### 11.3 Phase Roadmap

#### Phase 1: Foundation (Current)

**Professional:**
- [x] Neo4j database operational
- [x] Zingers system complete
- [x] AI OpEd prototype
- [ ] OpEd voice calibration
- [ ] OpEd "skill" development

**Content Marketing:**
- [x] Segmentation framework designed
- [ ] Ed's relationship tier input
- [ ] Twitter scheduling system
- [ ] Analytics insight generation

**Personal:**
- [x] The List v3 design
- [ ] 2AM Principal deliverables
- [ ] January recommendations
- [ ] Lifestyle source integration

#### Phase 2: Automation

**Professional:**
- [ ] Tag-level AI view (centroid embeddings)
- [ ] Special Edition candidate identification
- [ ] Market demand monitoring agent

**Content Marketing:**
- [ ] User segmentation by engagement
- [ ] AI-flagged performance explanations

**Personal:**
- [ ] Availability checking automation
- [ ] Last-minute alert system
- [ ] Upgrade hunting automation

#### Phase 3: Intelligence

**Professional:**
- [ ] Feedback loop on OpEd performance
- [ ] Refined voice model based on edits
- [ ] AI articulation of selection criteria ("principles and exceptions")

**Personal:**
- [ ] Preference learning from feedback
- [ ] Predictive suggestions

---

## 12. Open Questions

### 12.1 Professional

| Question | Impact | Status |
|----------|--------|--------|
| How to calibrate AI voice to be less aggressive? | OpEd quality | In progress |
| How can AI articulate selection criteria as "principles and exceptions"? | Explainability | Ed's requirement |
| How to identify Special Edition topics algorithmically? | Content discovery | Open |
| Tag-level AI view implementation? | Database usability | Awaiting Brandon-Anthony alignment |

### 12.2 Content Marketing

| Question | Impact | Status |
|----------|--------|--------|
| Ed's classification of contacts (Friends/Aware/Unknown)? | Segmentation | Awaiting Ed input |
| Growth strategy for adding new subscribers? | List growth | Open, seeking ideas |
| Twitter scheduling tool selection? | Social presence | Not started |

### 12.3 Personal

| Question | Impact | Status |
|----------|--------|--------|
| How to track visited vs. unvisited restaurants? | Discovery detection | Open |
| Resy/OpenTable API access vs. scraping? | Automation approach | Legal/technical |
| Paywall strategy for lifestyle sources? | Content access | Three options identified |
| 2AM Principal experience ideas? | Deliverable | Pending |

### 12.4 Technical

| Question | Impact | Status |
|----------|--------|--------|
| Tech/Claude budget for token-heavy operations? | Operations | Needed — can burn $300-400/day |
| Calendar integration approach? | Personal system | Not started |

---

## 13. Appendices

### Appendix A: Key Quotes / Design Mantras

**On Non-Substitution:**
> "A 3-star Michelin is not a substitute for a ham & cheese sandwich." — Ed Conard, December 4, 2025

**On Availability:**
> "Fill slots in my calendar with the best available option, then keep working to upgrade." — Ed Conard

**On Sources:**
> "Most recommendations are for sale. You show up and the place sucks." — Ed Conard, December 4, 2025

**On the Journey:**
> "He's not trying to reach some end state of satisfaction. The continuous stream of excellent options is the point."

**On Signal-to-Noise:**
> "The internet has filled the world with valuable information but buried it under a sea of noise. We need to find a way to use AI to make it better—to filter out the noise and get to the meat of the matter." — Ed Conard, December 15, 2025

**On Input vs. Output:**
> "Every moment I spend acquiring input is a moment I don't spend producing output (or consuming the precious waning moments of my life)." — Ed Conard, January 1, 2026

**On Thinking:**
> "The purpose of thinking is to stop thinking." — Ed Conard, December 23, 2025

**On Propaganda:**
> "The world is smeared in a thick coating of propaganda because when people find an argument that they mistakenly think justifies their desired conclusion, they stop thinking." — Ed Conard, December 23, 2025

### Appendix B: Location Context (NYC)

| Zone | Use |
|------|-----|
| **Home Base** | Upper East Side (E 80th & 2nd Ave) |
| **Office** | 87th & Lexington |
| **Convenience Zone** | Within 10 min of home or office |
| **Scene Zones** | SoHo, LES, West Village, NoHo, Tribeca |
| **Acceptable** | Midtown (select), Greenwich Village, NoMad, Flatiron |
| **Avoid** | Outer boroughs (mostly), Times Square, generic Midtown |

### Appendix C: Technical Infrastructure

| Component | Technology | Status |
|-----------|------------|--------|
| **Macro Roundup Database** | Neo4j | Operational |
| **Vector Embeddings** | OpenAI text-embedding-3-small (1,536-dim) | Operational |
| **AI Agent Platform** | Claude Code | Operational |
| **Email Distribution** | HubSpot | Operational |
| **Website** | edwardconard.com | Operational |
| **Restaurant Database** | TBD | Not yet built |
| **Calendar Integration** | TBD | Not yet built |
| **Alert System** | TBD | Not yet built |

### Appendix D: Related Project Files

| Project | Location | Status |
|---------|----------|--------|
| The List — Restaurant System | `restaurant-recommender/` | V3 design complete |
| NYC Trip January 2026 | `NYC-Trip-Jan-2026/` | Research complete |
| Zingers Spreadsheet | `CONARD_ZINGERS_FINAL.xlsx` | Complete |
| Macro Roundup | edwardconard.com | Operational |
| EWC System Folder | `/Users/brandonadams/Desktop/EWC System/` | Active |

### Appendix E: Lifestyle Source Inventory

*Compiled August 2022, to be updated*

**Luxury:**
- Barrons Penta, Bloomberg Pursuits, FT How to Spend It, Robb Report, Town + Country, Haute Living, Forbes Life

**NYC:**
- Timeout NYC, Thrillist NYC, Hidden New York, In the Know Experiences

**Food:**
- The Infatuation, NYT Pete Wells, Eater NY, Grub Street, Michelin Guide NY, Zagat, Resy

**Reading:**
- Longreads, The Browser, Five Books

**Newsletters:**
- The Browser, Tim Ferriss, Kottke, Morning Brew, 1440

**Paywalled (require subscription strategy):**
- FT How to Spend It, WSJ Magazine, NYT sections

### Appendix F: Email Exchange Index

| Date | Topic | Importance | Section Reference |
|------|-------|------------|-------------------|
| Oct 3, 2025 | Content expansion goals | Low | 5.2.2 |
| Oct 6, 2025 | Tagging and Neo4j | Medium | 5.3.4 |
| Oct 12, 2025 | METR time horizon | Low | 5.2 |
| Oct 12, 2025 | Analytics deep-dives | Low (preference insight) | 6.4 |
| Oct 30, 2025 | AI thoughts, Neo4j project | Very High | 5.3, 5.4 |
| Nov 13, 2025 | OpenTable cancellation concerns | Low | 7.3.4 |
| Nov 16-17, 2025 | Curation complexity, micro-topics | Medium-High | 5.3.4 |
| Nov 24-25, 2025 | Year of Slop, context windows | Medium-High | 5.3 |
| Nov 26-29, 2025 | Marketing segmentation framework | Very High | 6.3 |
| Nov 27, 2025 | Thanksgiving Special Edition | High | 5.6 |
| Dec 4, 2025 | Restaurant system feedback | High | 7.3 |
| Dec 5-19, 2025 | Brainy quotes / Zingers | Very High | 5.4 |
| Dec 6-9, 2025 | Weekly roundup, tagging issues | Very High | 5.3.4 |
| Dec 14-17, 2025 | 2AM Principal, lifestyle expansion | Medium | 7.5, 7.6 |
| Dec 23, 2025 | Work plan concerns, priorities | Moderate | 11.2 |
| Dec 23, 2025 | Tax arguments, rhetorical style | Moderate | 10 |
| Dec 31-Jan 2, 2026 | Summary protocol, Shannon | Moderate | 9.4 |

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | January 3, 2026 | Consultant | Initial draft |
| 2.0 | January 3, 2026 | Consultant | Comprehensive update with email context; added Content Marketing section; expanded Ed's arguments and voice guide; updated implementation status |

---

*This document serves as the master PRD for the EWC Personal Organization System. It should be used as context for all related AI conversations and updated as the system evolves.*
