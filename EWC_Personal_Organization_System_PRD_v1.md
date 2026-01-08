# EWC Personal Organization System
## Product Requirements Document

**Version:** 1.0
**Date:** January 3, 2026
**Author:** Consultant
**Status:** Draft for Review

---

## Executive Summary

This document defines a comprehensive personal organization system for Edward Conard—a unified platform designed to optimize his time, maximize his impact, and support the legacy he is building. The system spans both professional and personal domains, connected by shared principles but implemented with distinct architectures appropriate to each.

**The core proposition:** EWC's scarcest resource is not money but time and attention. This system is designed to protect high-leverage activities (content production), minimize low-leverage friction (supervision, logistics, discovery), and create a feeling of effortless abundance across all life domains.

---

## Table of Contents

1. [Client Context](#1-client-context)
2. [Utility Function](#2-utility-function)
3. [System Architecture Overview](#3-system-architecture-overview)
4. [Professional System](#4-professional-system)
5. [Personal System](#5-personal-system)
6. [Integration Layer](#6-integration-layer)
7. [Design Principles](#7-design-principles)
8. [Implementation Roadmap](#8-implementation-roadmap)
9. [Open Questions](#9-open-questions)
10. [Appendices](#10-appendices)

---

## 1. Client Context

### 1.1 Who Is Edward Conard

- **Background:** Former founding partner of Bain Capital; worked closely with Mitt Romney
- **Current Role:** Adjunct Fellow at American Enterprise Institute; author and public intellectual
- **Published Works:**
  - *Unintended Consequences: Why Everything You've Been Told About the Economy Is Wrong* (2012) — NYT Top 10 Bestseller
  - *The Upside of Inequality: How Good Intentions Undermine the Middle Class* (2016) — NYT Top 10 Bestseller, #1 NYT Business
  - Contributor to Oxford University Press's *United States Income, Wealth, Consumption, and Inequality* (2020)
- **Public Presence:** 250+ media appearances (CNN, ABC, CBS, Fox, CNBC, Bloomberg, BBC); debates with Krugman, Stiglitz; The Daily Show with Jon Stewart
- **Focus Areas:** Economics, inequality, innovation, trade deficits, growth in high-wage economies; challenging conventional economic thinking

### 1.2 Current Operations

- **Macro Roundup:** Daily curated summary of significant economic news, produced by staff and published at edwardconard.com
- **OpEd Production:** Regular commentary in WSJ, NYT, Washington Post, Foreign Affairs
- **Potential Future:** Additional books

### 1.3 Operating Team

| Role | Function |
|------|----------|
| **Principal (Ed)** | Strategic direction, content production, final decisions |
| **Consultant** | Chief of Staff functions, system design, complexity management |
| **Staff** | Macro Roundup production, research support, logistics |

---

## 2. Utility Function

### 2.1 Priority Hierarchy

| Rank | Value | Description |
|------|-------|-------------|
| 1 | **Time** | The scarcest resource; must be protected and allocated to highest-leverage activities |
| 2 | **Impact** | What is accomplished with that time; influence on economic policy discourse |
| 3 | **Legacy** | Long-term compounding of impact; books, ideas that persist |

### 2.2 Pain Points

| Pain Point | Description |
|------------|-------------|
| **People Management** | Managing complexity and supervising others drains time |
| **Supervision Overhead** | Time spent on check-ins and oversight feels wasteful |
| **Content Production Friction** | Needs to write more; the path from idea to published OpEd has friction |
| **Experience Optimization** | Not yet maximizing the full potential of life experiences |

### 2.3 Preferences

- **Delegation:** Comfortable delegating; wants clean handoffs with minimal supervision
- **Content:** Production and consumption are primary activities
- **Experience:** Values the chase/journey of discovering excellent experiences; willing to pay for quality; satisfaction is in the continuous stream, not an end state

---

## 3. System Architecture Overview

### 3.1 Two Engines, One System

```
┌─────────────────────────────────────────────────────────────────┐
│                    UNIFIED ORGANIZATION SYSTEM                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   ┌─────────────────────┐         ┌─────────────────────┐       │
│   │   PROFESSIONAL      │         │     PERSONAL        │       │
│   │      ENGINE         │         │      ENGINE         │       │
│   │                     │         │                     │       │
│   │  Neo4j Database     │         │  Category-Based     │       │
│   │  (Macro Roundup)    │         │  Structure          │       │
│   │        ↓            │         │        ↓            │       │
│   │  AI Content Agents  │         │  Discovery Engine   │       │
│   │        ↓            │         │        ↓            │       │
│   │  OpEd Pipeline      │         │  Execution Layer    │       │
│   │                     │         │                     │       │
│   └──────────┬──────────┘         └──────────┬──────────┘       │
│              │                               │                   │
│              └───────────┬───────────────────┘                   │
│                          │                                       │
│              ┌───────────▼───────────┐                          │
│              │   INTEGRATION LAYER   │                          │
│              │                       │                          │
│              │  - Unified Calendar   │                          │
│              │  - Time Protection    │                          │
│              │  - Decision Queue     │                          │
│              │  - Compressed View    │                          │
│              └───────────────────────┘                          │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### 3.2 Role-Based Views

| User | View | Purpose |
|------|------|---------|
| **Principal (Ed)** | Compressed | Only what needs his attention; decisions, content calendar, curated options |
| **Consultant** | Full Complexity | All moving pieces, delegated items, system health, pipeline status |

---

## 4. Professional System

### 4.1 Core Objective

Transform the Macro Roundup consumption engine into a content production pipeline that generates OpEds in Ed's voice with minimal friction, while monitoring the marketplace for strategic opportunities.

### 4.2 Existing Infrastructure

#### 4.2.1 Macro Roundup

- **What It Is:** Daily curated summary of significant economic news
- **Production:** Staff-produced, well-systematized and sophisticated
- **Publication:** edwardconard.com
- **Content:** Economic analysis, policy commentary, data, research

#### 4.2.2 Neo4j Database

- **Structure:** Graph database containing Macro Roundup content
- **Capability:** Claude Code-interrogable
- **Status:** Working and functional
- **Value:** Enables AI agents to query research, find connections, surface relevant material

### 4.3 Content Production Pipeline

#### 4.3.1 Current State

```
Macro Roundup → Published on Website → (disconnect) → Ed writes OpEds manually
```

#### 4.3.2 Target State

```
┌─────────────────────────────────────────────────────────────────────────┐
│                     CONTENT PRODUCTION PIPELINE                          │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ┌──────────────┐     ┌──────────────┐     ┌──────────────┐            │
│  │   INPUTS     │     │  PROCESSING  │     │   OUTPUTS    │            │
│  │              │     │              │     │              │            │
│  │ Macro        │────▶│ AI Agents    │────▶│ Draft OpEds  │            │
│  │ Roundup DB   │     │ (Ed's voice) │     │              │            │
│  │              │     │              │     │ Pitch        │            │
│  │ Market       │────▶│ Topic        │────▶│ Suggestions  │            │
│  │ Demand       │     │ Matching     │     │              │            │
│  │ Signals      │     │              │     │ Research     │            │
│  │              │     │              │     │ Packages     │            │
│  └──────────────┘     └──────────────┘     └──────────────┘            │
│                                                                          │
│                              ↓                                           │
│                                                                          │
│                    ┌──────────────────┐                                 │
│                    │   ED'S REVIEW    │                                 │
│                    │                  │                                 │
│                    │  Edit/Refine     │                                 │
│                    │  Approve/Reject  │                                 │
│                    │  Submit          │                                 │
│                    └──────────────────┘                                 │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

### 4.4 AI Agent Capabilities

#### 4.4.1 Content Generation Agent

| Function | Description |
|----------|-------------|
| **Voice Modeling** | Generates drafts in Ed's argumentative style and voice |
| **Research Integration** | Pulls relevant data, quotes, and analysis from Neo4j database |
| **Position Consistency** | Maintains consistency with Ed's established positions and prior publications |
| **Draft Production** | Produces OpEd drafts ready for Ed's review and refinement |

#### 4.4.2 Market Intelligence Agent

| Function | Description |
|----------|-------------|
| **Demand Monitoring** | Scans for topics where OpEd commentary is sought |
| **Publication Tracking** | Monitors WSJ, NYT, WaPo, Foreign Affairs for relevant debates |
| **Timing Optimization** | Identifies when Ed's contrarian perspective would be timely |
| **Opportunity Surfacing** | Proactively suggests topics before Ed asks |

### 4.5 OpEd Pipeline Stages

| Stage | Description | Owner |
|-------|-------------|-------|
| **Idea Capture** | Raw topic, triggered by MR content or market signal | System/Consultant |
| **Research Package** | Relevant data, sources, prior positions assembled | AI Agent |
| **Draft** | Full OpEd draft in Ed's voice | AI Agent |
| **Review** | Ed reviews, edits, refines | Principal |
| **Pitch/Submit** | Sent to publication | Consultant/Staff |
| **Published** | Live | — |
| **Archive** | Added to body of work | System |

### 4.6 Delegation Model

- **Consultant absorbs complexity:** Full visibility into all pipeline stages, handles logistics
- **Ed sees exceptions only:** Surfaced items are decisions, reviews, or opportunities requiring his input
- **Clear accountability:** Each delegated item has an owner and status; system tracks without requiring Ed's supervision

---

## 5. Personal System

### 5.1 Core Objective

Create a friction-free experience layer where Ed always knows about the best options (restaurants, shows, books, conferences, experiences, goods) and can execute on them effortlessly. The system learns his preferences over time and proactively surfaces opportunities.

### 5.2 Philosophical Foundation

> "Not yet maximizing the full potential of life experiences."

This is not about reaching a destination—it's about the continuous journey. The system should deliver:

- **Abundance:** A constant stream of excellent options
- **Serendipity:** Pleasant surprises and discoveries
- **Effortlessness:** When he says yes, it just happens
- **Learning:** The system gets better over time

### 5.3 Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        PERSONAL EXPERIENCE ENGINE                        │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ┌──────────────────────────────────────────────────────────────────┐   │
│  │                      DISCOVERY LAYER                              │   │
│  │                                                                   │   │
│  │   ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐            │   │
│  │   │Dining   │  │Shows/   │  │Travel/  │  │Goods/   │            │   │
│  │   │         │  │Events   │  │Conf     │  │Books    │            │   │
│  │   └─────────┘  └─────────┘  └─────────┘  └─────────┘            │   │
│  │                                                                   │   │
│  │   - Source monitoring (trusted sources only)                      │   │
│  │   - Category-based organization (no cross-category ranking)       │   │
│  │   - NEW/UNKNOWN tagging                                          │   │
│  │   - Preference learning                                          │   │
│  │                                                                   │   │
│  └──────────────────────────────────────────────────────────────────┘   │
│                              ↓                                           │
│  ┌──────────────────────────────────────────────────────────────────┐   │
│  │                      CURATION LAYER                               │   │
│  │                                                                   │   │
│  │   - Proactive recommendations (before he asks)                    │   │
│  │   - Availability as constraint (what's bookable?)                 │   │
│  │   - Upgrade hunting (monitor for better options)                  │   │
│  │   - Last-minute alerts (cancellations at aspirational spots)      │   │
│  │                                                                   │   │
│  └──────────────────────────────────────────────────────────────────┘   │
│                              ↓                                           │
│  ┌──────────────────────────────────────────────────────────────────┐   │
│  │                      EXECUTION LAYER                              │   │
│  │                                                                   │   │
│  │   - Frictionless booking (reservations, tickets, travel)         │   │
│  │   - Logistics handling (transportation, timing, details)          │   │
│  │   - Confirmation and calendar integration                         │   │
│  │   - Experience smoothing (anticipate needs)                       │   │
│  │                                                                   │   │
│  └──────────────────────────────────────────────────────────────────┘   │
│                              ↓                                           │
│  ┌──────────────────────────────────────────────────────────────────┐   │
│  │                      FEEDBACK LAYER                               │   │
│  │                                                                   │   │
│  │   - Track what he liked/didn't like                               │   │
│  │   - Refine preference model                                       │   │
│  │   - Improve future recommendations                                │   │
│  │                                                                   │   │
│  └──────────────────────────────────────────────────────────────────┘   │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

### 5.4 Experience Categories

Following "The List" pattern: categories are non-substitutable. A fine dining experience does not substitute for a neighborhood comfort meal.

#### 5.4.1 Dining (The List)

| Category | Use Case | Distance Sensitivity |
|----------|----------|---------------------|
| **Fine Dining / Destination** | Special occasions, tasting menus, Michelin-starred | Low — worth traveling |
| **Scene / Going Out** | Buzzy, groups, Friday night downtown | Medium |
| **Date Night** | Intimate, conversation-friendly (NOT pure sushi, NOT loud) | Medium |
| **Neighborhood Comfort (UES)** | Nearby, reliable, don't need to impress | High |
| **Quick / Casual** | Lunch, easy weeknight, walk-in friendly | Very high |
| **Discovery / Unknown** | New spots, under-radar, never visited | Variable |

#### 5.4.2 Entertainment & Culture

| Category | Examples |
|----------|----------|
| **Theater / Broadway** | Shows, openings, special performances |
| **Comedy** | Stand-up, clubs, special events |
| **Music / Concerts** | Performances worth attending |
| **Museums / Exhibits** | Current shows, limited-time exhibits |
| **Sports** | Knicks, Rangers, major events |

#### 5.4.3 Travel & Conferences

| Category | Examples |
|----------|----------|
| **Conferences** | Economic policy, AEI events, speaking opportunities |
| **Destination Travel** | Trips worth taking |
| **Event-Based Travel** | Trips organized around specific events |

#### 5.4.4 Consumption Goods

| Category | Examples |
|----------|----------|
| **Books** | Worth reading (professional and personal) |
| **Products** | High-quality goods in relevant categories |

### 5.5 Output Cadence

| Output | Frequency | Purpose |
|--------|-----------|---------|
| **Category Guides** | Monthly | Reference material, NEW additions highlighted |
| **Weekly Digest** | Weekly | What's available/bookable this week |
| **Opportunity Alerts** | As-needed | Time-sensitive opportunities (cancellations, limited availability) |
| **Event Horizon** | Monthly | Upcoming conferences, shows, events worth planning for |

### 5.6 Source Trust Hierarchy

All recommendations must show source attribution.

> "Most recommendations are for sale. You show up and the place sucks."

| Tier | Trust Level | Examples |
|------|-------------|----------|
| **Tier 1** | Highest | Michelin, NYT critics (Pete Wells) |
| **Tier 2** | High | Infatuation, Eater (editorial), WSJ, NY Mag, Time Out |
| **Excluded** | None | Yelp, Google reviews, sponsored content |

### 5.7 Wife Constraints (Where Applicable)

- Date nights: Avoid pure sushi, avoid loud scene-forward places
- Need: Intimate, conversation-friendly, quality food

### 5.8 Existing Projects to Integrate

#### 5.8.1 "The List" — Restaurant Scheduling System

- **Status:** V3 design complete, ~20 restaurants curated, HTML template built
- **Not Yet Built:** Database, automation, availability checking, calendar integration, SMS alerts
- **Integration:** Becomes the dining module of the Personal System

#### 5.8.2 NYC Trip Planning Pattern

- **Status:** Demonstrated with January 2026 trip
- **Pattern:** Category-based folders, consistent formatting, practical details, source citations
- **Integration:** Template for event-based experience planning

---

## 6. Integration Layer

### 6.1 Unified Calendar

Both professional and personal systems feed into a single calendar that:

- Protects content production time (sacred blocks for writing)
- Prevents double-booking across domains
- Shows Ed only what he needs to see (decisions, commitments)
- Shows Consultant the full picture (all items, statuses, logistics)

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
| **Unified at the top, distinct underneath** | One system, two engines; connected by calendar and decision queue |
| **Protect high-leverage time** | Content production is sacred; supervision is waste |
| **Proactive, not reactive** | Surface opportunities before he asks |
| **Exception-based** | Don't show what's working; show what needs attention |
| **Learning** | System improves over time based on feedback |

### 7.2 For the Professional System

| Principle | Description |
|-----------|-------------|
| **Consumption feeds production** | Macro Roundup is fuel for OpEds |
| **AI as first draft** | Ed refines, not writes from scratch |
| **Market awareness** | Know where demand exists for his perspective |
| **Voice consistency** | AI output must match Ed's established voice and positions |

### 7.3 For the Personal System

| Principle | Description |
|-----------|-------------|
| **Categories don't substitute** | Fine dining ≠ neighborhood comfort; never rank across |
| **Availability is the constraint** | He knows what's good; scheduling is the friction |
| **Source transparency** | Every recommendation shows where it came from |
| **The journey is the point** | Continuous stream of excellent options, not a destination |
| **Frictionless execution** | When he says yes, it just happens |

---

## 8. Implementation Roadmap

### Phase 1: Foundation

**Objective:** Establish core infrastructure for both systems

#### Professional
- [ ] Document Neo4j database schema and query patterns
- [ ] Define Ed's voice/style guide for AI content generation
- [ ] Build OpEd pipeline tracking (Idea → Draft → Review → Submit → Published)
- [ ] Create Consultant dashboard for pipeline visibility

#### Personal
- [ ] Extend "The List" restaurant database structure
- [ ] Build monthly category guide generator
- [ ] Establish source monitoring for each experience category
- [ ] Create decision queue interface

#### Integration
- [ ] Unified calendar with time protection blocks
- [ ] Exception-based alert system
- [ ] Role-based views (Ed vs. Consultant)

### Phase 2: Automation

**Objective:** Reduce manual effort through automation

#### Professional
- [ ] AI agent for draft OpEd generation
- [ ] Market demand monitoring agent
- [ ] Automated research package assembly from Neo4j

#### Personal
- [ ] Availability checking automation (Resy, OpenTable, Tock)
- [ ] Last-minute alert system
- [ ] Upgrade hunting automation
- [ ] Calendar integration for bookings

### Phase 3: Intelligence

**Objective:** System learns and improves

#### Professional
- [ ] Feedback loop on OpEd performance
- [ ] Refined voice model based on edits
- [ ] Topic success pattern recognition

#### Personal
- [ ] Preference learning from feedback
- [ ] Improved recommendation relevance
- [ ] Predictive suggestions based on patterns

### Phase 4: Expansion

**Objective:** Extend to full life coverage

- [ ] Expand personal categories (travel, conferences, goods, books)
- [ ] Cross-category experience planning (dinner + show itineraries)
- [ ] Long-term calendar (events worth planning for months ahead)
- [ ] Delegation tracking for non-content items

---

## 9. Open Questions

| Question | Domain | Impact |
|----------|--------|--------|
| What is Ed's preferred format for reviewing draft OpEds? | Professional | Workflow design |
| How should we track Ed's visited vs. unvisited restaurants? | Personal | Unknown detection |
| Which reservation resale services to integrate beyond Appointment Trader? | Personal | Upgrade hunting |
| Resy/OpenTable API access vs. scraping? | Personal | Automation approach |
| How much should AI agents generate vs. outline? | Professional | Content workflow |
| What conferences/events should be monitored proactively? | Personal | Calendar planning |
| How to handle wife's preferences in shared experience planning? | Personal | Recommendation logic |
| What is the handoff protocol when Consultant is unavailable? | Both | Continuity |

---

## 10. Appendices

### Appendix A: Key Quotes / Design Mantras

> "A 3-star Michelin is not a substitute for a ham & cheese sandwich."
> — On non-substitutable categories

> "Fill slots in my calendar with the best available option, then keep working to upgrade."
> — On availability-first scheduling

> "Most recommendations are for sale. You show up and the place sucks."
> — On source transparency

> "He's not trying to reach some end state of satisfaction. The continuous stream of excellent options is the point."
> — On the journey vs. destination

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
| **AI Agent Platform** | Claude Code | Operational |
| **Restaurant Database** | TBD | Not yet built |
| **Calendar Integration** | TBD | Not yet built |
| **Alert System** | TBD | Not yet built |

### Appendix D: Related Project Files

| Project | Location | Status |
|---------|----------|--------|
| The List — Restaurant System | `restaurant-recommender/` | V3 design complete |
| NYC Trip January 2026 | `NYC-Trip-Jan-2026/` | Research complete |
| Macro Roundup | edwardconard.com | Operational |

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | January 3, 2026 | Consultant | Initial draft |

---

*This document serves as the master PRD for the EWC Personal Organization System. It should be used as context for all related AI conversations and updated as the system evolves.*
