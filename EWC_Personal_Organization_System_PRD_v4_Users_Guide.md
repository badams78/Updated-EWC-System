# EWC Personal Organization System
## The Users' Guide

**Version:** 4.0
**Date:** January 3, 2026
**Status:** Working Document

---

## Executive Summary

This document defines a comprehensive personal organization system for Edward Conard—a unified platform designed to optimize his time, maximize his impact, and support the legacy he is building. The system spans both professional and personal domains, connected by shared principles but implemented with distinct architectures appropriate to each.

**The core proposition:** EWC's scarcest resource is not money but time and attention. This system is designed to protect high-leverage activities (content production), minimize low-leverage friction (supervision, logistics, discovery), and create a feeling of effortless abundance across all life domains.

**Ed's Own Words (January 1, 2026):**
> "Every moment I spend acquiring input is a moment I don't spend producing output (or consuming the precious waning moments of my life). It seems impossible to strike a productive balance without reducing the amount of input."

> "I think we need to work backwards from desired output to highly constrained input. I feel enslaved to input and daily tasks that I shouldn't be the one to do."

---

## Table of Contents

1. [Utility Function](#1-utility-function)
2. [System Architecture Overview](#2-system-architecture-overview)
3. [Professional System](#3-professional-system)
4. [Content Marketing System](#4-content-marketing-system)
5. [Personal System](#5-personal-system)
6. [Integration Layer](#6-integration-layer)
7. [Design Principles](#7-design-principles)
8. [Ed's Voice & Style Guide](#8-eds-voice--style-guide)
9. [Implementation Status & Roadmap](#9-implementation-status--roadmap)
10. [Suggested Skills](#10-suggested-skills)
11. [Open Questions](#11-open-questions)
12. [Appendices](#12-appendices)

---

## 1. Utility Function

### 1.1 Priority Hierarchy

| Rank | Value | Description |
|------|-------|-------------|
| 1 | **Time** | The scarcest resource; must be protected and allocated to highest-leverage activities |
| 2 | **Impact** | What is accomplished with that time; influence on economic policy discourse |
| 3 | **Legacy** | Long-term compounding of impact; books, ideas that persist |

### 1.2 Pain Points

| Pain Point | Description | Ed's Words |
|------------|-------------|------------|
| **Input Overload** | Too much to read/consume relative to output | "I feel enslaved to input and daily tasks" |
| **Supervision Overhead** | Time spent on check-ins and oversight | Drains time from content production |
| **Content Production Friction** | Path from idea to published OpEd has friction | Needs AI assistance but current drafts are "too aggressive" |
| **Experience Optimization** | Not maximizing life experiences | "Not yet maximizing the full potential" |
| **Signal-to-Noise** | Valuable information buried in noise | "The internet has filled the world with valuable information but buried it under a sea of noise" |

### 1.3 Preferences

**On Delegation:**
- Comfortable delegating; wants clean handoffs with minimal supervision
- Concerned about work plan alignment: "I'm concerned about whether we are executing on a mutually agreed upon work plan and arrival destination(s)." (December 23, 2025)

**On Information Consumption:**
- Prefers ~750 character summaries (flexible if needed)
- "The key insight that you think I could use or incorporate into my work"
- Shannon principle: "Insight needs to be wrapped in enough redundancy to be understood, but there was much more redundancy than was necessary"

**On Analytics:**
- Enjoys deep-dives into marketing analytics
- "We have performance data, but we aren't learning anything from it. How do we learn something?" (October 12, 2025)

**On AI and Slop (December 15, 2025):**
> "I think it's mistaken to assume that anything created by AI is necessarily slop. What could make it not-slop is the curation of the books and the story that it tells."

> "I'm always trying to solve the same problem—curating extremely high signal-to-noise for the things that interest me."

> "Ideally, AI would understand what I want—i.e., why I want it, which I don't fully understand—and then find it for me."

---

## 2. System Architecture Overview

### 2.1 Three Engines, One System

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
│                         │  - Full View (Consultants,  │                     │
│                         │    Chief of Staff, Caroline)│                     │
│                         └─────────────────────────────┘                     │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 2.2 Role-Based Views

| User | View | Purpose |
|------|------|---------|
| **Principal (Ed)** | Compressed | Only what needs his attention; decisions, content calendar, curated options |
| **Staff** | Full Complexity | All moving pieces, delegated items, system health, pipeline status |

---

## 3. Professional System

### 3.1 Core Objective

Transform the Macro Roundup consumption engine into a content production pipeline that generates OpEds in Ed's voice with minimal friction, while monitoring the marketplace for strategic opportunities.

### 3.2 Macro Roundup

#### 3.2.1 Current State

| Attribute | Detail |
|-----------|--------|
| **Format** | Daily curated summary of economic news |
| **Distribution** | ~4,000 subscribers via HubSpot |
| **Weekly Edition** | Saturdays, best-of summary |
| **Special Editions** | Occasional thematic deep-dives |
| **Website** | edwardconard.com |

#### 3.2.2 Content Philosophy

**Ed's View (October 3, 2025):**
> "I often think we skew too much to finance and not enough to hardcore social policy and policy math... and that we are focused on too narrow a set of (financial) bloggers."

**Content Expansion Goals:**
- Less finance skew, more hardcore social policy and "policy math"
- More authors, greater diversity
- Systematically try to add 1-2 new contributors per week
- Scour every think tank's daily newsletters
- Ed asks: "Could AI write something like Jim Friedman's WSJ Best of the Web column?"

**What the Roundup Should Be About:**
> "One of the many reasons the Roundup was created was to find quotes that change one's view of the world and can win an argument with a single well-placed sentence." (December 5, 2025)

### 3.3 Neo4j Database

#### 3.3.1 Technical Specifications

| Component | Detail |
|-----------|--------|
| **Database** | Neo4j Graph Database |
| **Articles** | ~1,762 with PDFs |
| **Entries** | 6,157+ with embeddings |
| **Vector Embeddings** | 1,536-dimensional (OpenAI text-embedding-3-small) |
| **Relationships** | 44,885 manually tagged `:RELATED_TO` relationships |
| **Status** | Operational, Claude Code-interrogable |

#### 3.3.2 Taxonomy (15 Main Categories)

1. Macro & Growth
2. Inflation & Prices
3. Labor & Demographics
4. Productivity, Innovation & Technology
5. Financial Markets
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

### 3.4 Zingers System

#### 3.4.1 Concept

**Ed's Definition (December 5, 2025):**
> "Quotes that change one's view of the world and can win an argument with a single well-placed sentence."

**Examples:**
- "Onshore wind turbines in Germany produce around one-fifth of their total theoretical output. Solar panels in Germany and the U.K. use only around 10% of their total theoretical output."
- "The maximum Social Security benefit, which today approaches $100,000 per year for a high-income couple, is two to four times higher in dollar terms than is paid in these other countries."

#### 3.4.2 Current Implementation

| Metric | Value |
|--------|-------|
| **Total Zingers Extracted** | 2,434 |
| **PDFs Processed** | 1,762 |
| **Rate** | ~1.6 zingers per article |
| **Categorization** | By Ed's 10 core arguments |

#### 3.4.3 Scoring Criteria (20 points each)

| Criterion | What It Measures |
|-----------|------------------|
| **Brevity & Punch** | Short, quotable, one-breath delivery |
| **Specific Facts** | Concrete numbers, percentages, comparisons |
| **Surprise Factor** | "Wait, really?" — counterintuitive beats obvious |
| **Credibility** | Attribution to credible source |
| **Argument Support** | Directly supports Ed's position |

### 3.5 OpEd Pipeline

#### 3.5.1 Pipeline Stages

| Stage | Description | Owner | Status |
|-------|-------------|-------|--------|
| **Idea Capture** | Raw topic, triggered by MR content or market signal | System/Staff | Operational |
| **Research Package** | Relevant data, sources, prior positions, zingers assembled | AI Agent | In Development |
| **Draft** | Full OpEd draft in Ed's voice | AI Agent | Prototype |
| **Review** | Ed reviews, edits, refines | Principal | Manual |
| **Pitch/Submit** | Sent to publication | Staff | Manual |
| **Published** | Live | — | — |
| **Archive** | Added to body of work | System | — |

#### 3.5.2 AI Draft Quality Assessment

**Ed's Feedback (December 19, 2025):**
> "Wow. Surprisingly good, especially for a first cut... But too aggressive, overstates the arguments (like the popular press), it would take substantial of my time to make this publishable under my name."

**Calibration Needed:**
- Less aggressive tone
- More modulated certainty
- Deeper argument structure (not just surface-level)
- Must address and defeat typical counterarguments
- Integrate zingers naturally

### 3.6 Special Editions

Thematic, curated editions of the Macro Roundup around a coherent topic.

**Ed's Ambition (November 27, 2025):**
> "I can't help but wonder whether the distribution of our special editions shouldn't be much wider. The whole world should see this edition."

**Candidates Identified:**
- AI crowding out other investments
- Comparison to Europe
- Problems plaguing Germany
- Productivity growth (past vs future)
- US debt crisis building
- Electricity as bottleneck to AI usage

---

## 4. Content Marketing System

### 4.1 Distribution Channels

| Channel | Subscribers | Frequency | Status |
|---------|-------------|-----------|--------|
| **Daily Roundup** | ~4,000 | Daily | Operational |
| **Weekly Roundup** | ~4,000 | Saturdays | Operational |
| **Special Editions** | ~4,000 | Occasional | Operational |
| **Twitter/X** | @EdwardConard | Underutilized | Needs scheduled system |

### 4.2 Two Strategic Problems

| Problem | Current State | Priority |
|---------|---------------|----------|
| **Retention/Optimization** | Halfway reasonable | Maintain |
| **Growth/Acquisition** | Very poor — not adding new subscribers | **High priority, needs ideas** |

**Growth Ideas to Explore:**
- Purchasing targeted email lists (economics/policy interested audiences)
- Advertising with TLDR Tech newsletters (tldr.tech)
- Wider distribution of Special Editions
- Twitter engagement strategy

### 4.3 Marketing Segmentation Framework

#### 4.3.1 Primary: Profession/Role

| Segment | Treatment |
|---------|-----------|
| **Journalists** | PR-focused, newsworthy content |
| **Policymakers** | Policy briefs, legislative implications |
| **Economists** | Research-focused, data-heavy |
| **Investors** | Market implications, investment angles |
| **Other Influencers** | Thought leadership positioning |

#### 4.3.2 Secondary: Relationship Tier

| Tier | Description | Approach |
|------|-------------|----------|
| **Tier 1: Friends** | Personal relationship with Ed | Direct, personal outreach |
| **Tier 2: Aware** | Know who Ed is, have engaged | Warm outreach, reference past interaction |
| **Tier 3: Unknown** | No prior awareness | Cold outreach, establish credibility |

#### 4.3.3 Tertiary: Influence/Audience

| Level | Examples | Value |
|-------|----------|-------|
| **High Audience** | Major media byline, 50k+ Twitter followers | Very high — amplification potential |
| **Medium Audience** | Regional/trade media, think tank fellow | High — targeted impact |
| **Low/Consumer** | No public platform, junior positions | Standard — direct reader value |

### 4.4 Analytics System

**Ed's Frustration (October 12, 2025):**
> "We have performance data, but we aren't learning anything from it. How do we learn something?"

**Required Capabilities:**
- Email campaign performance analytics (HubSpot)
- Website analytics (edwardconard.com)
- User segmentation by engagement level
- AI-flagged high/low performing entries with explanations

---

## 5. Personal System

### 5.1 Core Objective

Create a friction-free experience layer where Ed always knows about the best options (restaurants, shows, books, conferences, experiences, goods) and can execute on them effortlessly. The system learns his preferences over time and proactively surfaces opportunities.

### 5.2 Philosophical Foundation

**Ed's Core Problem (December 15, 2025):**
> "I'm always trying to solve the same problem—curating extremely high signal-to-noise for the things that interest me. I have a very limited amount of time. So, when I do something (read, for example) I want it optimized relative to all the other ways that I could spend my time."

### 5.3 The List — Restaurant System

#### 5.3.1 Non-Substitution Principle

**Ed's Foundational Rule (December 4, 2025):**
> "Rather than summing up all the different ways to differentiate (e.g., score) something, it's overwhelmingly more valuable and insightful to leave the relevant criteria segmented."

> "A 3-star is not a substitute for a delicious grilled ham and cheese sandwich from EAT a block from my house on Saturday for lunch."

#### 5.3.2 Dining Categories

| Category | Use Case | Distance Sensitivity |
|----------|----------|---------------------|
| **Fine Dining / Destination** | Special occasions, tasting menus, Michelin-starred | Low — worth traveling |
| **Scene / Going Out** | Buzzy, groups, Friday night downtown | Medium |
| **Date Night** | Intimate, conversation-friendly (NOT pure sushi, NOT loud) | Medium |
| **Neighborhood Comfort (UES)** | Nearby, reliable, don't need to impress | High |
| **Quick / Casual** | Lunch, easy weeknight, walk-in friendly | Very high |
| **Discovery / Unknown** | New spots, under-radar, never visited | Variable |

#### 5.3.3 Booking Philosophy

**Ed's Position:** Optimal system should NOT involve canceling a lot of reservations.

**The Hardest Parts (per Ed):**
1. Getting hard-to-get reservations
2. Planning ahead
3. Knowing WHICH TYPE to book, especially last minute

### 5.4 Source Trust Hierarchy

**Ed's Rule (December 4, 2025):**
> "Who says a restaurant is good matters. Most recommendations are for sale. You show up and the place sucks."

| Tier | Trust Level | Examples |
|------|-------------|----------|
| **Tier 1** | Highest | Michelin, NYT critics (Pete Wells) |
| **Tier 2** | High | Infatuation, Eater (editorial), WSJ, NY Mag, Time Out |
| **Excluded** | None | Yelp, Google reviews, sponsored content |

### 5.5 "2 AM Principal" Experiences

**Concept (from John Levy book):**
> "A great night out on the town with friends should include the preplanned illusion of a spontaneous event that is surprising, exhilarating, dangerous, and satisfying."

**Status:** Project initiated, deliverables pending.

### 5.6 Expanded Personal System

**Ed's Additional Requests (December 15, 2025):**

| Category | Description | Status |
|----------|-------------|--------|
| **Lifestyle Websites** | Sources for "rich old male New Yorkers" including paywalls | Source list compiled |
| **Weekly Book Summaries** | 800-1000 words, esoteric nonfiction, high signal-to-noise | Not started |
| **"Rules for Living"** | Daily/weekly brilliant rules for business/personal life | Not started |
| **Sunday Edition** | Combining lifestyle content | Concept only |

### 5.7 Output Cadence

| Output | Frequency | Purpose |
|--------|-----------|---------|
| **Category Guides** | Monthly | Reference material, NEW additions highlighted |
| **Weekly Digest** | Weekly | What's available/bookable this week |
| **Opportunity Alerts** | As-needed | Time-sensitive (cancellations, limited availability) |
| **Event Horizon** | Monthly | Upcoming conferences, shows, events worth planning for |

---

## 6. Integration Layer

### 6.1 Unified Calendar

Both professional and personal systems feed into a single calendar that:
- Protects content production time (sacred blocks for writing)
- Prevents double-booking across domains
- Shows Ed only what he needs to see (decisions, commitments)
- Shows Staff the full picture (all items, statuses, logistics)

### 6.2 Decision Queue

A single stream of items requiring Ed's input:

| Type | Source | Example |
|------|--------|---------|
| **Content Decision** | Professional | "Review this OpEd draft" |
| **Experience Decision** | Personal | "Le Bernardin has an opening Saturday—book?" |
| **Strategic Decision** | Either | "Invitation to speak at X conference" |

### 6.3 Time Protection

| Block Type | Purpose | Protection Level |
|------------|---------|------------------|
| **Writing Time** | OpEd and book production | Highest — do not interrupt |
| **Review Time** | Content review, decision-making | High — batch decisions here |
| **Open Time** | Meetings, calls, flexible | Normal |
| **Personal Time** | Dining, experiences, rest | Respect boundaries |

### 6.4 Exception-Based Surfacing

**Default:** Ed does not see operational details

**Exception:** Surface only when:
- A decision is required
- Something is off-track and needs his input
- An opportunity is time-sensitive
- A commitment needs confirmation

---

## 7. Design Principles

### 7.1 For the System as a Whole

| Principle | Description |
|-----------|-------------|
| **Unified at the top, distinct underneath** | One system, three engines; connected by calendar and decision queue |
| **Protect high-leverage time** | Content production is sacred; supervision is waste |
| **Proactive, not reactive** | Surface opportunities before he asks |
| **Exception-based** | Don't show what's working; show what needs attention |
| **Learning** | System improves over time based on feedback |
| **Work plan transparency** | Clear deliverables and destinations visible to Ed |

### 7.2 For the Professional System

| Principle | Description |
|-----------|-------------|
| **Consumption feeds production** | Macro Roundup is fuel for OpEds |
| **AI as first draft** | Ed refines, not writes from scratch |
| **Market awareness** | Know where demand exists for his perspective |
| **Voice consistency** | AI output must match Ed's voice, not be "too aggressive" |
| **Argument depth** | AI must understand arguments deeply enough to defeat counterarguments |

### 7.3 For the Personal System

| Principle | Description |
|-----------|-------------|
| **Categories don't substitute** | Fine dining ≠ neighborhood comfort; never rank across |
| **Availability is the constraint** | He knows what's good; scheduling is the friction |
| **Source transparency** | Every recommendation shows where it came from |
| **The journey is the point** | Continuous stream of excellent options, not a destination |
| **Frictionless execution** | When he says yes, it just happens |

### 7.4 For Communication

| Principle | Ed's Words |
|-----------|------------|
| **Optimal summary length** | ~750 characters, flexible if needed |
| **Shannon principle** | "Edit out a large share of the unnecessary redundancy" |
| **Key insight focus** | "The key insight that you think I could use or incorporate into my work" |
| **Significant digits** | Round to meaningful precision (23.6% → 24%) |

---

## 8. Ed's Voice & Style Guide

### 8.1 For AI Content Generation

| Attribute | Guideline |
|-----------|-----------|
| **Tone** | Measured, not aggressive (current AI drafts are "too aggressive") |
| **Certainty** | Modulate appropriately; don't overstate |
| **Data** | Specific percentages, round to significant digits |
| **Counterfactuals** | Always reference what would otherwise be (Europe as glimpse) |
| **Ex ante focus** | Emphasize decisions before outcomes, not billionaires after |
| **Counterarguments** | Must anticipate and defeat typical objections |
| **Audience** | Primarily economists, not general public |

### 8.2 Rhetorical Philosophy

**Ed's Self-Description (December 23, 2025):**
> "My rhetorical style is driven by the substance of my arguments and the typical counter arguments—arguments I think are lame, but others, who haven't given it much thought, nevertheless find persuasive, and therefore must be defeated."

> "To view my arguments through the lens of my rhetorical style is to wag the dog by the tail. My style is driven by the (quality/strength) of my arguments... and the need to defeat common misperceptions."

### 8.3 Key Mantras

> "The purpose of thinking is to stop thinking."

> "Proof is absence of imagination."

> "The world is smeared in a thick coating of propaganda because when people find an argument that they mistakenly think justifies their desired conclusion, they stop thinking."

### 8.4 Number Presentation

> "I often say X and not about X because I try to first round numbers (to significant digits). 23.6% of GDP becomes 24%. My view is that people can't remember fractions and that fractions over-represent the true accuracy of numbers."

---

## 9. Implementation Status & Roadmap

### 9.1 Current Status (as of January 3, 2026)

#### Professional System

| Component | Status | Notes |
|-----------|--------|-------|
| Neo4j Database | **Operational** | 6,157+ articles, vector embeddings, Claude-interrogable |
| Zingers Extraction | **Complete** | 2,434 zingers, scored, categorized |
| Zinger CLI Tool | **Prototype** | Command-line search functional |
| AI OpEd Generation | **Prototype** | Works but needs voice calibration |
| Special Editions | **Manual** | No automated identification yet |

#### Content Marketing System

| Component | Status | Notes |
|-----------|--------|-------|
| HubSpot Integration | **Operational** | ~4,000 subscribers |
| Segmentation Framework | **Designed** | Awaiting relationship tier input |
| Analytics Dashboard | **Partial** | Basic metrics, not insight-generating |
| Twitter Scheduling | **Not Built** | Identified as gap |
| Growth Strategy | **Gap** | "Very poor" per assessment |

#### Personal System

| Component | Status | Notes |
|-----------|--------|-------|
| The List v3 | **Design Complete** | ~20 restaurants curated |
| Restaurant Database | **Not Built** | — |
| Availability Checking | **Not Built** | Resy/OpenTable integration pending |
| 2AM Principal | **Initiated** | Deliverables pending |
| Book Summaries | **Not Started** | — |

### 9.2 Phase Roadmap

#### Phase 1: Foundation (Current)

**Professional:**
- [x] Neo4j database operational
- [x] Zingers system complete
- [x] AI OpEd prototype
- [ ] OpEd voice calibration
- [ ] OpEd skill development

**Content Marketing:**
- [x] Segmentation framework designed
- [ ] Relationship tier input
- [ ] Twitter scheduling system
- [ ] Analytics insight generation

**Personal:**
- [x] The List v3 design
- [ ] 2AM Principal deliverables
- [ ] January recommendations
- [ ] Lifestyle source integration

#### Phase 2: Automation

- [ ] Tag-level AI view (centroid embeddings)
- [ ] Special Edition candidate identification
- [ ] Availability checking automation
- [ ] Last-minute alert system

#### Phase 3: Intelligence

- [ ] Feedback loop on OpEd performance
- [ ] Refined voice model based on edits
- [ ] Preference learning from feedback
- [ ] Predictive suggestions

---

## 10. Suggested Skills

The following skills are proposed for development. Each skill is a specialized AI capability that can be invoked to perform a specific task within the EWC system.

### 10.1 Professional Skills

| Skill Name | Description | Input | Output |
|------------|-------------|-------|--------|
| **OpEd Drafter** | Generates OpEd drafts in Ed's voice with proper argument structure, zingers, and counterargument handling | Topic + relevant context | Full draft OpEd |
| **Zinger Search** | Searches the zinger database by topic, argument, or keyword | Search query | Rank-ordered zingers with sources |
| **Article Summarizer** | Summarizes articles following Ed's 750-char Shannon principle | Article text or URL | Condensed summary with key insight |
| **Special Edition Scout** | Analyzes database to identify emerging themes worthy of special edition treatment | Category or time range | Candidate themes with supporting articles |
| **Content Expansion Scout** | Identifies new contributors and think tank sources for Macro Roundup diversification | Content area | Recommended sources with sample content |
| **Counterargument Mapper** | Maps common objections to Ed's positions and suggested rebuttals | Argument topic | Objection-rebuttal pairs |

### 10.2 Content Marketing Skills

| Skill Name | Description | Input | Output |
|------------|-------------|-------|--------|
| **Analytics Insight Generator** | Extracts learnable insights from HubSpot/website performance data | Performance data | Actionable insights with explanations |
| **Segmentation Analyzer** | Analyzes subscriber behavior and suggests segmentation strategies | Subscriber data | Segment definitions with engagement patterns |
| **Twitter Thread Generator** | Creates Twitter threads from Macro Roundup content or OpEds | Source content | Thread-formatted posts |

### 10.3 Personal Skills

| Skill Name | Description | Input | Output |
|------------|-------------|-------|--------|
| **Restaurant Recommender** | Category-aware restaurant suggestions respecting non-substitution principle | Category + constraints (date, location, occasion) | Ranked options with source citations |
| **2AM Principal Curator** | Sources and curates "surprising, exhilarating" NYC experiences | Occasion type + group size | Curated experience options |
| **Book Summary Generator** | Weekly esoteric nonfiction summaries at 800-1000 words | Book title or topic area | Structured summary with key takeaways |
| **Rules for Living Curator** | Surfaces brilliant rules for business/personal life from quality sources | Topic area | Curated rules with attribution |
| **Event Horizon Scanner** | Monitors upcoming conferences, shows, events worth planning for | Time horizon + interest areas | Calendar of opportunities |

### 10.4 Cross-Cutting Skills

| Skill Name | Description | Input | Output |
|------------|-------------|-------|--------|
| **Decision Queue Manager** | Formats and prioritizes items requiring Ed's attention | Multiple inputs | Prioritized decision list |
| **Weekly Status Compiler** | Compiles progress across all three engines for status updates | System state | Formatted status report |

---

## 11. Open Questions

### 11.1 Professional

| Question | Impact | Status |
|----------|--------|--------|
| How to calibrate AI voice to be less aggressive? | OpEd quality | In progress |
| How to identify Special Edition topics algorithmically? | Content discovery | Open |
| Tag-level AI view implementation? | Database usability | Open |

### 11.2 Content Marketing

| Question | Impact | Status |
|----------|--------|--------|
| Ed's classification of contacts (Friends/Aware/Unknown)? | Segmentation | Awaiting Ed input |
| Growth strategy for adding new subscribers? | List growth | Open, seeking ideas |
| Twitter scheduling tool selection? | Social presence | Not started |

### 11.3 Personal

| Question | Impact | Status |
|----------|--------|--------|
| How to track visited vs. unvisited restaurants? | Discovery detection | Open |
| Resy/OpenTable API access vs. scraping? | Automation approach | Legal/technical |
| 2AM Principal experience ideas? | Deliverable | Pending |

---

## 12. Appendices

### Appendix A: Key Quotes / Design Mantras

**On Non-Substitution:**
> "A 3-star Michelin is not a substitute for a ham & cheese sandwich." — Ed Conard, December 4, 2025

**On Availability:**
> "Fill slots in my calendar with the best available option, then keep working to upgrade." — Ed Conard

**On Sources:**
> "Most recommendations are for sale. You show up and the place sucks." — Ed Conard, December 4, 2025

**On Signal-to-Noise:**
> "The internet has filled the world with valuable information but buried it under a sea of noise. We need to find a way to use AI to make it better—to filter out the noise and get to the meat of the matter." — Ed Conard, December 15, 2025

**On Input vs. Output:**
> "Every moment I spend acquiring input is a moment I don't spend producing output (or consuming the precious waning moments of my life)." — Ed Conard, January 1, 2026

**On Thinking:**
> "The purpose of thinking is to stop thinking." — Ed Conard, December 23, 2025

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

### Appendix D: Lifestyle Source Inventory

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
