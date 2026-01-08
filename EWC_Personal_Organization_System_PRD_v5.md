# EWC Personal Organization System
## The Users' Guide

**Version:** 5.0
**Date:** January 8, 2026
**Status:** Working Document

---

## Executive Summary

This document defines a comprehensive personal organization system for Edward Conard—a unified platform designed to optimize his time, maximize his impact, and support the legacy he is building. The system spans both professional and personal domains, connected by shared principles but implemented with distinct architectures appropriate to each.

**The core proposition:** EWC's scarcest resource is not money but time and attention. This system is designed to protect high-leverage activities (content production), minimize low-leverage friction (supervision, logistics, discovery), and create a feeling of effortless abundance across all life domains.

**What's New in v5:**
- Formalized restaurant data model (28 attributes) based on production code
- Guest Context / Dining Modes as first-class concept
- Life Domain Engine pattern for extensible personal organization
- Booking Intelligence Layer with difficulty ratings and timing
- Weekly Digest as formal output structure
- Trend awareness and freshness tracking
- EWC In NYC web application concept

**Ed's Own Words (January 1, 2026):**
> "Every moment I spend acquiring input is a moment I don't spend producing output (or consuming the precious waning moments of my life). It seems impossible to strike a productive balance without reducing the amount of input."

> "I think we need to work backwards from desired output to highly constrained input. I feel enslaved to input and daily tasks that I shouldn't be the one to do."

---

## Table of Contents

1. [Utility Function](#1-utility-function)
2. [System Architecture Overview](#2-system-architecture-overview)
3. [Professional System](#3-professional-system)
4. [Content Marketing System](#4-content-marketing-system)
5. [Life Domain Engine (Personal System)](#5-life-domain-engine-personal-system)
6. [EWC In NYC Web Application](#6-ewc-in-nyc-web-application)
7. [Integration Layer](#7-integration-layer)
8. [Design Principles](#8-design-principles)
9. [Ed's Voice & Style Guide](#9-eds-voice--style-guide)
10. [Implementation Status & Roadmap](#10-implementation-status--roadmap)
11. [Suggested Skills](#11-suggested-skills)
12. [Open Questions](#12-open-questions)
13. [Appendices](#13-appendices)

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

### 2.1 Four Engines, One System

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                       UNIFIED ORGANIZATION SYSTEM v5                             │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                  │
│   ┌─────────────────┐   ┌─────────────────┐   ┌─────────────────────────────┐  │
│   │  PROFESSIONAL   │   │CONTENT MARKETING│   │     LIFE DOMAIN ENGINE      │  │
│   │     ENGINE      │   │     ENGINE      │   │                             │  │
│   │                 │   │                 │   │  ┌─────────┐ ┌─────────┐   │  │
│   │  Neo4j Database │   │  HubSpot        │   │  │ DINING  │ │ TRAVEL  │   │  │
│   │  (Macro Roundup)│   │  Analytics      │   │  │(The List)│ │(Trips)  │   │  │
│   │       ↓         │   │  (4,000 subs)   │   │  └────┬────┘ └────┬────┘   │  │
│   │  Zingers System │   │       ↓         │   │       │           │         │  │
│   │       ↓         │   │  Segmentation   │   │  ┌────┴───────────┴────┐   │  │
│   │  OpEd Pipeline  │   │       ↓         │   │  │  SHARED TEMPLATE    │   │  │
│   │                 │   │  Growth Strategy│   │  │  - Categories       │   │  │
│   │                 │   │                 │   │  │  - Guest Contexts   │   │  │
│   │                 │   │                 │   │  │  - Source Trust     │   │  │
│   │                 │   │                 │   │  │  - Booking Layer    │   │  │
│   └────────┬────────┘   └────────┬────────┘   │  └─────────────────────┘   │  │
│            │                     │            └──────────────┬──────────────┘  │
│            │                     │                           │                  │
│            └─────────────────────┼───────────────────────────┘                  │
│                                  │                                              │
│                   ┌──────────────▼──────────────┐                               │
│                   │     INTEGRATION LAYER       │                               │
│                   │                             │                               │
│                   │  - Unified Calendar         │                               │
│                   │  - Time Protection          │                               │
│                   │  - Decision Queue           │                               │
│                   │  - Weekly Digest Output     │                               │
│                   │  - EWC In NYC Web App       │                               │
│                   └─────────────────────────────┘                               │
│                                                                                  │
└─────────────────────────────────────────────────────────────────────────────────┘
```

### 2.2 Role-Based Views

| User | View | Purpose |
|------|------|---------|
| **Principal (Ed)** | Compressed | Only what needs his attention; decisions, content calendar, curated options |
| **Staff** | Full Complexity | All moving pieces, delegated items, system health, pipeline status |
| **Web App** | Browsable | Category navigation, weekly digests, quick reference |

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

## 5. Life Domain Engine (Personal System)

### 5.1 Core Objective

Create a friction-free experience layer where Ed always knows about the best options (restaurants, shows, books, conferences, experiences, goods) and can execute on them effortlessly. The system learns his preferences over time and proactively surfaces opportunities.

**v5 Evolution:** The Personal System is now architected as a **Life Domain Engine** — a template-based approach that can be applied to any life category (dining, travel, entertainment, services) with consistent structure.

### 5.2 Philosophical Foundation

**Ed's Core Problem (December 15, 2025):**
> "I'm always trying to solve the same problem—curating extremely high signal-to-noise for the things that interest me. I have a very limited amount of time. So, when I do something (read, for example) I want it optimized relative to all the other ways that I could spend my time."

### 5.3 Life Domain Template

Every life domain follows a consistent structure:

```
┌─────────────────────────────────────────────────────────────────┐
│                    LIFE DOMAIN TEMPLATE                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────┐    ┌─────────────────┐                    │
│  │   CATEGORIES    │    │  GUEST CONTEXTS │                    │
│  │                 │    │                 │                    │
│  │  Non-substitut- │    │  Family         │                    │
│  │  able buckets   │    │  Friends        │                    │
│  │  within domain  │    │  Solo           │                    │
│  │                 │    │  Business       │                    │
│  │                 │    │  Special Guest  │                    │
│  └────────┬────────┘    └────────┬────────┘                    │
│           │                      │                              │
│           └──────────┬───────────┘                              │
│                      ▼                                          │
│           ┌─────────────────────┐                               │
│           │   ITEM DATABASE     │                               │
│           │                     │                               │
│           │  - Identity         │                               │
│           │  - Quality signals  │                               │
│           │  - Logistics        │                               │
│           │  - Booking info     │                               │
│           │  - Trend data       │                               │
│           │  - User metadata    │                               │
│           └──────────┬──────────┘                               │
│                      ▼                                          │
│           ┌─────────────────────┐                               │
│           │  SOURCE TRUST LAYER │                               │
│           │                     │                               │
│           │  Tier 1: Highest    │                               │
│           │  Tier 2: High       │                               │
│           │  Excluded: None     │                               │
│           └──────────┬──────────┘                               │
│                      ▼                                          │
│           ┌─────────────────────┐                               │
│           │   BOOKING LAYER     │                               │
│           │                     │                               │
│           │  - Difficulty       │                               │
│           │  - Platform         │                               │
│           │  - Timing windows   │                               │
│           │  - Execution        │                               │
│           └──────────┬──────────┘                               │
│                      ▼                                          │
│           ┌─────────────────────┐                               │
│           │   OUTPUT LAYER      │                               │
│           │                     │                               │
│           │  - Weekly Digest    │                               │
│           │  - Category Guides  │                               │
│           │  - Opportunity Alerts│                              │
│           │  - Web Interface    │                               │
│           └─────────────────────┘                               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 5.4 Domain: Dining (The List)

#### 5.4.1 Non-Substitution Principle

**Ed's Foundational Rule (December 4, 2025):**
> "Rather than summing up all the different ways to differentiate (e.g., score) something, it's overwhelmingly more valuable and insightful to leave the relevant criteria segmented."

> "A 3-star is not a substitute for a delicious grilled ham and cheese sandwich from EAT a block from my house on Saturday for lunch."

#### 5.4.2 Dining Categories

| Category | Use Case | Distance Sensitivity |
|----------|----------|---------------------|
| **Fine Dining / Destination** | Special occasions, tasting menus, Michelin-starred | Low — worth traveling |
| **Scene / Going Out** | Buzzy, groups, Friday night downtown | Medium |
| **Date Night** | Intimate, conversation-friendly (NOT pure sushi, NOT loud) | Medium |
| **Neighborhood Comfort (UES)** | Nearby, reliable, don't need to impress | High |
| **Quick / Casual** | Lunch, easy weeknight, walk-in friendly | Very high |
| **Discovery / Unknown** | New spots, under-radar, never visited | Variable |

#### 5.4.3 Guest Context / Dining Modes

**NEW in v5:** First-class support for dining companion context.

| Mode | Description | Optimization Priority |
|------|-------------|----------------------|
| **Family** | Parents, relatives visiting | Comfortable, accommodating, reliable, not too loud |
| **Friends** | Social dining, groups | Scene, energy, shareable plates, fun |
| **Solo** | Just Ed | Quick, efficient, bar seating OK |
| **Business** | Professional context | Quiet, impressive, convenient location |
| **Date Night** | Intimate evening | Conversation-friendly, romantic, good drinks |
| **Special Guest** | Customizable per person | Adapts to guest preferences |

#### 5.4.4 Restaurant Data Model (Formalized)

**NEW in v5:** Production-ready schema based on implemented code.

```python
@dataclass
class Restaurant:
    # Identity
    id: str
    name: str
    neighborhood: Neighborhood  # 21 NYC neighborhoods
    cuisine: Cuisine            # 21 cuisine types

    # Quality Signals (Multi-Dimensional, Non-Aggregated)
    google_rating: float                    # 0-5
    michelin_status: MichelinStatus         # 3-star, 2-star, 1-star, Bib, None
    infatuation_rating: Optional[float]     # 0-10
    eater_essential: bool
    nyt_reviewed: bool
    nyt_critic_pick: bool

    # Dimensional Scores (Keep Separate per Non-Substitution)
    scene_score: int           # 1-10: How buzzy/trendy
    food_quality_score: int    # 1-10: Pure food quality
    noise_level: int           # 1-10: 1=quiet, 10=very loud

    # Trend Tracking
    opening_date: Optional[date]
    currently_hot: bool
    recent_press: Optional[str]

    # Booking Intelligence
    booking_platform: BookingPlatform  # Resy, OpenTable, Tock, etc.
    booking_url: Optional[str]
    booking_window_days: int           # How far ahead reservations open
    release_time: Optional[time]       # When new reservations drop
    price_tier: int                    # 1-4 ($, $$, $$$, $$$$)
    difficulty_rating: DifficultyRating  # Easy, Moderate, Hard, Lottery

    # User Metadata
    tags: List[str]
    last_recommended: Optional[date]
    visited: bool
    pro_tips: Optional[str]
    notes: Optional[str]

    # Computed Properties
    def age_months(self) -> int
    def is_new(self) -> bool           # < 18 months old
    def is_in_convenience_zone(self) -> bool  # UES proximity
    def is_in_scene_zone(self) -> bool        # Downtown trendy areas
```

#### 5.4.5 Booking Intelligence Layer

**NEW in v5:** Systematic approach to reservation difficulty.

| Difficulty | Description | Strategy |
|------------|-------------|----------|
| **Easy** | Walk-in or same-day booking | No advance planning needed |
| **Moderate** | Book 3-7 days ahead | Plan early in week for weekend |
| **Hard** | Book 2-4 weeks ahead, competitive | Set calendar reminder when window opens |
| **Lottery** | Reservation releases sell out instantly | Use alerts, consider concierge services |

**Booking Platforms:**
- Resy
- OpenTable
- Tock
- SevenRooms
- Phone Only
- Walk-in Only
- Members Only

#### 5.4.6 Source Trust Hierarchy

**Ed's Rule (December 4, 2025):**
> "Who says a restaurant is good matters. Most recommendations are for sale. You show up and the place sucks."

| Tier | Trust Level | Examples |
|------|-------------|----------|
| **Tier 1** | Highest | Michelin, NYT critics (Pete Wells) |
| **Tier 2** | High | Infatuation, Eater (editorial), WSJ, NY Mag, Time Out |
| **Excluded** | None | Yelp, Google reviews, sponsored content |

### 5.5 Domain: Travel

**Template Application:** The NYC trip (Ed in NYC / Mom Visit) demonstrates this pattern.

#### 5.5.1 Travel Categories

| Category | Examples |
|----------|----------|
| **Theater** | Broadway, Off-Broadway |
| **Museums** | The Met, MoMA, Guggenheim |
| **Restaurants** | By neighborhood, cuisine, budget |
| **Comedy** | Clubs, improv venues |
| **Sports** | Knicks, Rangers, Nets |
| **Events** | Seasonal festivals, concerts |

#### 5.5.2 Travel Data Structure

Each category follows consistent format:
- **Identity:** Name, address, contact
- **Quality signals:** Trusted source citations
- **Logistics:** Hours, pricing, booking requirements
- **Context notes:** Guest-specific recommendations (e.g., "Mom recommendations")
- **Timing:** Exhibit end dates, event schedules, seasonal factors

### 5.6 Weekly Digest Output

**NEW in v5:** Formalized output structure.

```python
@dataclass
class WeeklyDigest:
    generated_date: date
    target_week_start: date

    # Context-Segmented Recommendations
    family_recommendations: List[Recommendation]
    friends_recommendations: List[Recommendation]
    solo_recommendations: List[Recommendation]

    # Time-Sensitive Alerts
    hard_to_book_windows: List[BookingAlert]
    expiring_opportunities: List[Opportunity]
    new_openings: List[Restaurant]

@dataclass
class Recommendation:
    restaurant: Restaurant
    dining_mode: DiningMode
    party_size: int
    score: float
    target_date: date
    booking_action: str      # "Book now", "Opens Tuesday 10am", etc.
    why_recommended: str     # Reasoning
```

### 5.7 "2 AM Principal" Experiences

**Concept (from John Levy book):**
> "A great night out on the town with friends should include the preplanned illusion of a spontaneous event that is surprising, exhilarating, dangerous, and satisfying."

**Status:** Project initiated, deliverables pending.

### 5.8 Expanded Life Domains

**Ed's Additional Requests (December 15, 2025):**

| Domain | Description | Status |
|--------|-------------|--------|
| **Lifestyle Websites** | Sources for "rich old male New Yorkers" including paywalls | Source list compiled |
| **Weekly Book Summaries** | 800-1000 words, esoteric nonfiction, high signal-to-noise | Not started |
| **"Rules for Living"** | Daily/weekly brilliant rules for business/personal life | Not started |
| **Sunday Edition** | Combining lifestyle content | Concept only |

### 5.9 Output Cadence

| Output | Frequency | Purpose | Delivery |
|--------|-----------|---------|----------|
| **Weekly Digest** | Weekly (Sundays) | What's available/bookable this week, by context | Email + Web App |
| **Category Guides** | Monthly | Reference material, NEW additions highlighted | Web App |
| **Opportunity Alerts** | As-needed | Time-sensitive (cancellations, limited availability) | Push/Email |
| **Event Horizon** | Monthly | Upcoming conferences, shows, events worth planning for | Email + Web App |

---

## 6. EWC In NYC Web Application

### 6.1 Concept

A dedicated web application providing a browsable, always-available interface to the Life Domain Engine. Hosted on Replit for rapid development and easy access.

**URL:** `ewc-in-nyc.replit.app` (proposed)

### 6.2 Core Features

#### 6.2.1 Home Dashboard

```
┌─────────────────────────────────────────────────────────────────┐
│  EWC In NYC                                    [Family ▼] [Ed] │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  THIS WEEK                                      Jan 8-14, 2026  │
│  ─────────────────────────────────────────────────────────────  │
│                                                                 │
│  🍽️ DINING PICKS                                               │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐               │
│  │ Carbone     │ │ EAT (UES)   │ │ Tatiana     │               │
│  │ Scene/Group │ │ Neighborhood│ │ New/Hot     │               │
│  │ Book by Wed │ │ Walk-in OK  │ │ Hard-Book   │               │
│  └─────────────┘ └─────────────┘ └─────────────┘               │
│                                                                 │
│  🎭 SHOWS & EVENTS                                              │
│  • Bug opens Jan 8 — Carrie Coon psychological thriller        │
│  • Winter Jazzfest Jan 8-13                                    │
│  • Knicks vs Celtics Jan 11 (MSG)                              │
│                                                                 │
│  ⏰ BOOKING WINDOWS OPENING                                     │
│  • Le Bernardin: Jan 10 @ 10am (for Feb dates)                 │
│  • Atomix: Jan 12 @ 12pm (lottery)                             │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

#### 6.2.2 Category Browser

| Section | Contents |
|---------|----------|
| **Dining** | Full restaurant database, filterable by category, cuisine, neighborhood, difficulty |
| **Theater** | Current Broadway/Off-Broadway shows with booking status |
| **Museums** | Current exhibits with end dates, free admission days |
| **Events** | Calendar of upcoming events, concerts, festivals |
| **Comedy** | Venue guide with booking info |
| **Sports** | Game schedule with ticket availability |

#### 6.2.3 Context Switcher

Toggle between dining contexts to see tailored recommendations:
- Family Mode
- Friends Mode
- Solo Mode
- Date Night Mode

#### 6.2.4 Quick Actions

- **"Book This"** — Direct links to Resy/OpenTable/etc.
- **"Add to Calendar"** — Export to Google/Apple Calendar
- **"Set Reminder"** — Alert when booking window opens
- **"Save for Later"** — Personal wishlist

### 6.3 Technical Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     EWC In NYC - Replit Stack                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  FRONTEND                                                       │
│  ├── Framework: Next.js or React                                │
│  ├── Styling: Tailwind CSS                                      │
│  └── Hosting: Replit                                            │
│                                                                 │
│  BACKEND                                                        │
│  ├── Runtime: Node.js or Python (Flask/FastAPI)                 │
│  ├── Database: SQLite or PostgreSQL (Replit DB)                 │
│  └── API: REST or GraphQL                                       │
│                                                                 │
│  DATA LAYER                                                     │
│  ├── Restaurant Database (from models.py schema)                │
│  ├── Events/Shows Database                                      │
│  ├── User Preferences                                           │
│  └── Booking Windows/Alerts                                     │
│                                                                 │
│  INTEGRATIONS                                                   │
│  ├── Calendar Export (ICS)                                      │
│  ├── Email Notifications (SendGrid/Resend)                      │
│  └── Future: Resy/OpenTable API (if available)                  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 6.4 Data Sources

| Data Type | Source | Update Frequency |
|-----------|--------|------------------|
| **Restaurant Database** | Curated from trusted sources | Weekly |
| **Current Shows** | Broadway.com, Playbill | Weekly |
| **Museum Exhibits** | Direct from museum sites | Monthly |
| **Events** | TimeOut, NYC tourism | Weekly |
| **Booking Windows** | Manual entry + scraping | As needed |

### 6.5 Access & Authentication

| User | Access Level |
|------|--------------|
| **Ed** | Full access, all contexts |
| **Staff/Caroline** | Full access, manage content |
| **Guests** | Read-only, limited to shared views |

### 6.6 Development Phases

#### Phase 1: Static Site
- Markdown/JSON data files
- Simple category navigation
- Mobile-responsive design
- No backend required

#### Phase 2: Dynamic Features
- Database backend
- Context switcher
- Search/filter functionality
- Admin panel for content updates

#### Phase 3: Smart Features
- Booking window alerts
- Calendar integration
- Weekly digest auto-generation
- Preference learning

### 6.7 Why Replit?

| Benefit | Description |
|---------|-------------|
| **Rapid Deployment** | Live in minutes, no DevOps overhead |
| **Always On** | Hosted and accessible 24/7 |
| **Easy Updates** | Edit and deploy from browser |
| **Collaboration** | Staff can contribute without git expertise |
| **Cost Effective** | Free tier sufficient for personal use |
| **Mobile Friendly** | Responsive by default |

---

## 7. Integration Layer

### 7.1 Unified Calendar

Both professional and personal systems feed into a single calendar that:
- Protects content production time (sacred blocks for writing)
- Prevents double-booking across domains
- Shows Ed only what he needs to see (decisions, commitments)
- Shows Staff the full picture (all items, statuses, logistics)

### 7.2 Decision Queue

A single stream of items requiring Ed's input:

| Type | Source | Example |
|------|--------|---------|
| **Content Decision** | Professional | "Review this OpEd draft" |
| **Experience Decision** | Personal | "Le Bernardin has an opening Saturday—book?" |
| **Strategic Decision** | Either | "Invitation to speak at X conference" |

### 7.3 Time Protection

| Block Type | Purpose | Protection Level |
|------------|---------|------------------|
| **Writing Time** | OpEd and book production | Highest — do not interrupt |
| **Review Time** | Content review, decision-making | High — batch decisions here |
| **Open Time** | Meetings, calls, flexible | Normal |
| **Personal Time** | Dining, experiences, rest | Respect boundaries |

### 7.4 Exception-Based Surfacing

**Default:** Ed does not see operational details

**Exception:** Surface only when:
- A decision is required
- Something is off-track and needs his input
- An opportunity is time-sensitive
- A commitment needs confirmation

---

## 8. Design Principles

### 8.1 For the System as a Whole

| Principle | Description |
|-----------|-------------|
| **Unified at the top, distinct underneath** | One system, multiple engines; connected by calendar and decision queue |
| **Protect high-leverage time** | Content production is sacred; supervision is waste |
| **Proactive, not reactive** | Surface opportunities before he asks |
| **Exception-based** | Don't show what's working; show what needs attention |
| **Learning** | System improves over time based on feedback |
| **Work plan transparency** | Clear deliverables and destinations visible to Ed |

### 8.2 For the Professional System

| Principle | Description |
|-----------|-------------|
| **Consumption feeds production** | Macro Roundup is fuel for OpEds |
| **AI as first draft** | Ed refines, not writes from scratch |
| **Market awareness** | Know where demand exists for his perspective |
| **Voice consistency** | AI output must match Ed's voice, not be "too aggressive" |
| **Argument depth** | AI must understand arguments deeply enough to defeat counterarguments |

### 8.3 For the Life Domain Engine

| Principle | Description |
|-----------|-------------|
| **Categories don't substitute** | Fine dining ≠ neighborhood comfort; never rank across |
| **Context matters** | Family dining ≠ friends dining; same restaurant, different recommendation |
| **Multi-dimensional scoring** | Keep scene, food, noise separate; don't collapse to single score |
| **Availability is the constraint** | He knows what's good; scheduling is the friction |
| **Source transparency** | Every recommendation shows where it came from |
| **The journey is the point** | Continuous stream of excellent options, not a destination |
| **Frictionless execution** | When he says yes, it just happens |
| **Template extensibility** | Same pattern applies to any life domain |

### 8.4 For Communication

| Principle | Ed's Words |
|-----------|------------|
| **Optimal summary length** | ~750 characters, flexible if needed |
| **Shannon principle** | "Edit out a large share of the unnecessary redundancy" |
| **Key insight focus** | "The key insight that you think I could use or incorporate into my work" |
| **Significant digits** | Round to meaningful precision (23.6% → 24%) |

---

## 9. Ed's Voice & Style Guide

### 9.1 For AI Content Generation

| Attribute | Guideline |
|-----------|-----------|
| **Tone** | Measured, not aggressive (current AI drafts are "too aggressive") |
| **Certainty** | Modulate appropriately; don't overstate |
| **Data** | Specific percentages, round to significant digits |
| **Counterfactuals** | Always reference what would otherwise be (Europe as glimpse) |
| **Ex ante focus** | Emphasize decisions before outcomes, not billionaires after |
| **Counterarguments** | Must anticipate and defeat typical objections |
| **Audience** | Primarily economists, not general public |

### 9.2 Rhetorical Philosophy

**Ed's Self-Description (December 23, 2025):**
> "My rhetorical style is driven by the substance of my arguments and the typical counter arguments—arguments I think are lame, but others, who haven't given it much thought, nevertheless find persuasive, and therefore must be defeated."

> "To view my arguments through the lens of my rhetorical style is to wag the dog by the tail. My style is driven by the (quality/strength) of my arguments... and the need to defeat common misperceptions."

### 9.3 Key Mantras

> "The purpose of thinking is to stop thinking."

> "Proof is absence of imagination."

> "The world is smeared in a thick coating of propaganda because when people find an argument that they mistakenly think justifies their desired conclusion, they stop thinking."

### 9.4 Number Presentation

> "I often say X and not about X because I try to first round numbers (to significant digits). 23.6% of GDP becomes 24%. My view is that people can't remember fractions and that fractions over-represent the true accuracy of numbers."

---

## 10. Implementation Status & Roadmap

### 10.1 Current Status (as of January 8, 2026)

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

#### Life Domain Engine

| Component | Status | Notes |
|-----------|--------|-------|
| Restaurant Data Model | **Designed** | 28-attribute schema defined |
| Restaurant Database | **Not Built** | Schema ready, needs population |
| Guest Context System | **Designed** | Family/Friends/Solo modes defined |
| NYC Trip Content | **Complete** | Mom visit fully documented |
| Weekly Digest System | **Designed** | Schema defined, needs automation |
| Booking Intelligence | **Designed** | Difficulty ratings, platforms mapped |
| EWC In NYC Web App | **Not Started** | Architecture defined |
| 2AM Principal | **Initiated** | Deliverables pending |
| Book Summaries | **Not Started** | — |

### 10.2 Phase Roadmap

#### Phase 1: Foundation (Current → Q1 2026)

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

**Life Domain Engine:**
- [x] Restaurant data model designed
- [x] Guest context modes defined
- [x] NYC trip content complete
- [ ] Restaurant database populated
- [ ] **EWC In NYC web app Phase 1** (static site)
- [ ] Weekly digest automation

#### Phase 2: Automation (Q2 2026)

**Professional:**
- [ ] Tag-level AI view (centroid embeddings)
- [ ] Special Edition candidate identification

**Life Domain Engine:**
- [ ] **EWC In NYC web app Phase 2** (dynamic features)
- [ ] Booking window alert system
- [ ] Calendar integration
- [ ] Availability checking automation

#### Phase 3: Intelligence (Q3 2026)

**Professional:**
- [ ] Feedback loop on OpEd performance
- [ ] Refined voice model based on edits

**Life Domain Engine:**
- [ ] **EWC In NYC web app Phase 3** (smart features)
- [ ] Preference learning from feedback
- [ ] Predictive suggestions
- [ ] Cross-domain recommendations

---

## 11. Suggested Skills

The following skills are proposed for development. Each skill is a specialized AI capability that can be invoked to perform a specific task within the EWC system.

### 11.1 Professional Skills

| Skill Name | Description | Input | Output |
|------------|-------------|-------|--------|
| **OpEd Drafter** | Generates OpEd drafts in Ed's voice with proper argument structure, zingers, and counterargument handling | Topic + relevant context | Full draft OpEd |
| **Zinger Search** | Searches the zinger database by topic, argument, or keyword | Search query | Rank-ordered zingers with sources |
| **Article Summarizer** | Summarizes articles following Ed's 750-char Shannon principle | Article text or URL | Condensed summary with key insight |
| **Special Edition Scout** | Analyzes database to identify emerging themes worthy of special edition treatment | Category or time range | Candidate themes with supporting articles |
| **Content Expansion Scout** | Identifies new contributors and think tank sources for Macro Roundup diversification | Content area | Recommended sources with sample content |
| **Counterargument Mapper** | Maps common objections to Ed's positions and suggested rebuttals | Argument topic | Objection-rebuttal pairs |

### 11.2 Content Marketing Skills

| Skill Name | Description | Input | Output |
|------------|-------------|-------|--------|
| **Analytics Insight Generator** | Extracts learnable insights from HubSpot/website performance data | Performance data | Actionable insights with explanations |
| **Segmentation Analyzer** | Analyzes subscriber behavior and suggests segmentation strategies | Subscriber data | Segment definitions with engagement patterns |
| **Twitter Thread Generator** | Creates Twitter threads from Macro Roundup content or OpEds | Source content | Thread-formatted posts |

### 11.3 Life Domain Skills

| Skill Name | Description | Input | Output |
|------------|-------------|-------|--------|
| **Restaurant Recommender** | Context-aware restaurant suggestions respecting non-substitution principle | Category + context (dining mode, date, location, occasion) | Ranked options with source citations |
| **Weekly Digest Generator** | Produces weekly digest of recommendations across all contexts | Current week + available data | Formatted digest for email/web |
| **Booking Window Monitor** | Tracks upcoming booking windows for hard-to-get reservations | Restaurant list | Alert schedule with booking actions |
| **2AM Principal Curator** | Sources and curates "surprising, exhilarating" NYC experiences | Occasion type + group size | Curated experience options |
| **Book Summary Generator** | Weekly esoteric nonfiction summaries at 800-1000 words | Book title or topic area | Structured summary with key takeaways |
| **Rules for Living Curator** | Surfaces brilliant rules for business/personal life from quality sources | Topic area | Curated rules with attribution |
| **Event Horizon Scanner** | Monitors upcoming conferences, shows, events worth planning for | Time horizon + interest areas | Calendar of opportunities |
| **Trip Planner** | Generates category-based trip research following NYC template | Destination + dates + guests | Structured trip folder with guides |

### 11.4 Cross-Cutting Skills

| Skill Name | Description | Input | Output |
|------------|-------------|-------|--------|
| **Decision Queue Manager** | Formats and prioritizes items requiring Ed's attention | Multiple inputs | Prioritized decision list |
| **Weekly Status Compiler** | Compiles progress across all engines for status updates | System state | Formatted status report |

---

## 12. Open Questions

### 12.1 Professional

| Question | Impact | Status |
|----------|--------|--------|
| How to calibrate AI voice to be less aggressive? | OpEd quality | In progress |
| How to identify Special Edition topics algorithmically? | Content discovery | Open |
| Tag-level AI view implementation? | Database usability | Open |

### 12.2 Content Marketing

| Question | Impact | Status |
|----------|--------|--------|
| Ed's classification of contacts (Friends/Aware/Unknown)? | Segmentation | Awaiting Ed input |
| Growth strategy for adding new subscribers? | List growth | Open, seeking ideas |
| Twitter scheduling tool selection? | Social presence | Not started |

### 12.3 Life Domain Engine

| Question | Impact | Status |
|----------|--------|--------|
| How to track visited vs. unvisited restaurants? | Discovery detection | Open |
| Resy/OpenTable API access vs. scraping? | Automation approach | Legal/technical |
| 2AM Principal experience ideas? | Deliverable | Pending |
| **EWC In NYC: Which Replit stack?** | Development speed | **Recommend: Next.js + SQLite** |
| **Initial restaurant database population?** | Web app launch | **Need to curate ~50-100 restaurants** |

---

## 13. Appendices

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
| **Restaurant Database** | TBD (SQLite recommended) | Schema designed |
| **Calendar Integration** | TBD | Not yet built |
| **EWC In NYC Web App** | Replit (Next.js + SQLite) | Architecture defined |

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

### Appendix E: Neighborhood Taxonomy

```python
class Neighborhood(Enum):
    # Manhattan - Upper
    UPPER_EAST_SIDE = "Upper East Side"
    UPPER_WEST_SIDE = "Upper West Side"
    HARLEM = "Harlem"

    # Manhattan - Midtown
    MIDTOWN_EAST = "Midtown East"
    MIDTOWN_WEST = "Midtown West"
    HELLS_KITCHEN = "Hell's Kitchen"

    # Manhattan - Downtown
    CHELSEA = "Chelsea"
    FLATIRON = "Flatiron"
    GRAMERCY = "Gramercy"
    GREENWICH_VILLAGE = "Greenwich Village"
    WEST_VILLAGE = "West Village"
    EAST_VILLAGE = "East Village"
    SOHO = "SoHo"
    NOHO = "NoHo"
    NOLITA = "Nolita"
    LOWER_EAST_SIDE = "Lower East Side"
    TRIBECA = "Tribeca"
    CHINATOWN = "Chinatown"
    FINANCIAL_DISTRICT = "Financial District"

    # Brooklyn
    WILLIAMSBURG = "Williamsburg"
    BROOKLYN_HEIGHTS = "Brooklyn Heights"
```

### Appendix F: Cuisine Taxonomy

```python
class Cuisine(Enum):
    ITALIAN = "Italian"
    FRENCH = "French"
    JAPANESE = "Japanese"
    JAPANESE_OMAKASE = "Japanese (Omakase)"
    JAPANESE_KAISEKI = "Japanese (Kaiseki)"
    CHINESE = "Chinese"
    KOREAN = "Korean"
    THAI = "Thai"
    VIETNAMESE = "Vietnamese"
    INDIAN = "Indian"
    MEXICAN = "Mexican"
    SPANISH = "Spanish"
    GREEK = "Greek"
    MEDITERRANEAN = "Mediterranean"
    MIDDLE_EASTERN = "Middle Eastern"
    AMERICAN = "American"
    NEW_AMERICAN = "New American"
    STEAKHOUSE = "Steakhouse"
    SEAFOOD = "Seafood"
    PIZZA = "Pizza"
    DELI = "Deli"
```

### Appendix G: v4 → v5 Change Summary

| Area | v4 State | v5 Change |
|------|----------|-----------|
| Personal System naming | "Personal System" | Renamed to "Life Domain Engine" |
| Restaurant data model | Conceptual description | Formal 28-attribute schema |
| Dining context | Implicit in categories | Explicit Guest Context / Dining Modes |
| Booking difficulty | Not addressed | 4-tier rating + booking windows + platforms |
| Life domains | Restaurants only | Template pattern extensible to any domain |
| Weekly output | Not specified | Formalized WeeklyDigest structure |
| Trend tracking | Not specified | Age, hotness, press flags on restaurants |
| Scoring approach | "Don't aggregate" principle | Multi-dimensional scores (scene, food, noise) |
| Web interface | Not mentioned | EWC In NYC Replit application |
| Travel template | Ad hoc | NYC trip as replicable Life Domain template |

---

*Document generated: January 8, 2026*
*Next review: January 15, 2026*
