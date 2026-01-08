# Personal System Project
## Asana Project Plan

---

## Project Overview

**Objective:** Create a friction-free experience layer where Ed always knows about the best options and can execute on them effortlessly.

**Key Outcomes:**
- Restaurant recommendations by category with source citations
- 2AM Principal experience library
- Book summaries and Rules for Living delivered regularly
- Availability checking (longer-term)

---

## Section: Phase 1 — Quick Wins

### Task: Deliver January Restaurant Recommendations
- **Description:** Compile and deliver January restaurant and experience recommendations
- **Subtasks:**
  - [ ] Review current restaurant list
  - [ ] Identify new openings / noteworthy spots
  - [ ] Categorize by dining category
  - [ ] Add source citations
  - [ ] Format for delivery
  - [ ] Send to Ed
- **Assignee:** TBD
- **Priority:** P0
- **Difficulty:** Easy

### Task: Deliver 2AM Principal NYC Experience Ideas
- **Description:** Research and compile 15-20 NYC experience ideas meeting "surprising, exhilarating, dangerous, satisfying" criteria
- **Subtasks:**
  - [ ] Research speakeasy/hidden bar options
  - [ ] Research late-night experiences
  - [ ] Research unique entertainment options
  - [ ] Research private/exclusive access experiences
  - [ ] Research adventure/thrill options (within reason)
  - [ ] Categorize by type and group size
  - [ ] Add logistical details
  - [ ] Format for delivery
- **Assignee:** TBD
- **Priority:** P0
- **Difficulty:** Easy

### Task: Identify Book Summary Sources
- **Description:** Research 10+ sources for discovering esoteric nonfiction books worth summarizing
- **Subtasks:**
  - [ ] Review The Browser recommendations
  - [ ] Review Five Books interviews
  - [ ] Identify academic/intellectual book review sources
  - [ ] Find science/complexity book sources
  - [ ] Document source quality and frequency
- **Assignee:** TBD
- **Priority:** P2
- **Difficulty:** Easy

### Task: Identify Rules for Living Sources
- **Description:** Research sources for business/life wisdom content
- **Subtasks:**
  - [ ] Review Farnam Street
  - [ ] Review Brain Pickings / The Marginalian
  - [ ] Identify philosophy/wisdom sources
  - [ ] Find business biography sources
  - [ ] Document quality and relevance
- **Assignee:** TBD
- **Priority:** P2
- **Difficulty:** Easy

### Task: Create Restaurant Visited/Unvisited Tracker
- **Description:** Simple spreadsheet to track Ed's restaurant history
- **Subtasks:**
  - [ ] Design tracking columns (name, category, date visited, rating, notes)
  - [ ] Pre-populate with known visited restaurants
  - [ ] Create "want to visit" section
  - [ ] Share with relevant team members
- **Assignee:** TBD
- **Priority:** P2
- **Difficulty:** Easy

---

## Section: Phase 2 — Foundation

### Task: Design Restaurant Database Schema
- **Description:** Create data structure for tracking restaurants by category, source, status, availability
- **Subtasks:**
  - [ ] Define entity attributes (name, location, category, sources, ratings, etc.)
  - [ ] Define relationship structure
  - [ ] Choose storage approach (spreadsheet vs. database)
  - [ ] Create initial data entry template
  - [ ] Document schema
- **Assignee:** TBD
- **Priority:** P1
- **Difficulty:** Medium

### Task: Build Restaurant Recommender Skill
- **Description:** Category-aware recommendation skill respecting non-substitution principle
- **Subtasks:**
  - [ ] Implement category filtering
  - [ ] Add location/distance awareness (UES proximity)
  - [ ] Include source citation requirement
  - [ ] Add "new/unknown" flagging
  - [ ] Handle wife constraints for date night
  - [ ] Test recommendations
- **Assignee:** TBD
- **Priority:** P1
- **Difficulty:** Medium
- **Dependencies:** Database design complete

### Task: Build Book Summary Generator Skill
- **Description:** Skill that produces 800-1000 word summaries of esoteric nonfiction
- **Subtasks:**
  - [ ] Define summary structure
  - [ ] Set quality standards
  - [ ] Test on sample books
  - [ ] Get Ed feedback on format
  - [ ] Refine based on feedback
- **Assignee:** TBD
- **Priority:** P2
- **Difficulty:** Medium
- **Dependencies:** Source list complete

### Task: Build Rules for Living Curator Skill
- **Description:** Skill that surfaces business/life wisdom from quality sources
- **Subtasks:**
  - [ ] Define curation criteria
  - [ ] Set up source monitoring
  - [ ] Design output format
  - [ ] Test curation quality
- **Assignee:** TBD
- **Priority:** P2
- **Difficulty:** Medium
- **Dependencies:** Source list complete

### Task: Build Event Horizon Scanner Skill
- **Description:** Monitors upcoming conferences, shows, events worth planning for
- **Subtasks:**
  - [ ] Identify event sources (economics conferences, NYC shows, etc.)
  - [ ] Define relevance criteria
  - [ ] Create monitoring schedule
  - [ ] Design calendar output format
- **Assignee:** TBD
- **Priority:** P2
- **Difficulty:** Medium

### Task: Build 2AM Principal Curator Skill
- **Description:** Ongoing curation of surprising NYC experiences
- **Subtasks:**
  - [ ] Systematize criteria from John Levy book
  - [ ] Identify monitoring sources
  - [ ] Create novelty detection (don't repeat)
  - [ ] Design recommendation format
- **Assignee:** TBD
- **Priority:** P2
- **Difficulty:** Medium
- **Dependencies:** Initial ideas document complete

### Task: Set Up Lifestyle Source Monitoring
- **Description:** Configure monitoring for key lifestyle sources
- **Subtasks:**
  - [ ] Set up RSS/email for Tier 1 sources
  - [ ] Create aggregation approach
  - [ ] Define review cadence
  - [ ] Test delivery
- **Assignee:** TBD
- **Priority:** P2
- **Difficulty:** Medium

---

## Section: Phase 3 — Automation

### Task: Build Availability Checking Automation
- **Description:** Real-time availability checking from Resy/OpenTable
- **Subtasks:**
  - [ ] Research Resy API access options
  - [ ] Research OpenTable API access options
  - [ ] Assess scraping feasibility and legality
  - [ ] Evaluate third-party services (Cita, etc.)
  - [ ] Choose implementation approach
  - [ ] Build availability checker
  - [ ] Test reliability
- **Assignee:** TBD
- **Priority:** P1
- **Difficulty:** Difficult

### Task: Build Last-Minute Alert System
- **Description:** Monitors for cancellations at hard-to-book restaurants
- **Subtasks:**
  - [ ] Define target restaurants to monitor
  - [ ] Set up monitoring frequency
  - [ ] Design alert delivery (SMS, email, etc.)
  - [ ] Handle false positives
  - [ ] Test response time
- **Assignee:** TBD
- **Priority:** P2
- **Difficulty:** Difficult
- **Dependencies:** Availability checking operational

### Task: Build Upgrade Hunting Automation
- **Description:** Continuously seeks better options for already-booked dates
- **Subtasks:**
  - [ ] Integrate with Ed's calendar
  - [ ] Define "upgrade" criteria by category
  - [ ] Set monitoring for booked dates
  - [ ] Design upgrade proposal format
  - [ ] Handle booking/cancellation workflow
- **Assignee:** TBD
- **Priority:** P2
- **Difficulty:** Difficult
- **Dependencies:** Calendar integration + availability checking

---

## Section: Phase 4 — Intelligence

### Task: Implement Preference Learning
- **Description:** System learns from Ed's feedback over time
- **Subtasks:**
  - [ ] Design feedback capture mechanism
  - [ ] Define preference dimensions
  - [ ] Build learning model
  - [ ] Test prediction accuracy
  - [ ] Integrate into recommendations
- **Assignee:** TBD
- **Priority:** P2
- **Difficulty:** Difficult

### Task: Build Predictive Suggestion Engine
- **Description:** Anticipates what Ed wants before he asks
- **Subtasks:**
  - [ ] Analyze historical patterns
  - [ ] Identify predictable preferences
  - [ ] Design proactive suggestion triggers
  - [ ] Test relevance
- **Assignee:** TBD
- **Priority:** P2
- **Difficulty:** Difficult

---

## Key Dependencies

```
January Deliverables → Immediate (no dependencies)
Source Lists → Summary/Curator Skills
Database Design → Restaurant Recommender Skill
2AM Ideas Doc → 2AM Curator Skill
Availability API Research → All Automation Tasks
Calendar Integration → Upgrade Hunting
```

---

## Dining Categories Reference

| Category | Use Case | Key Constraints |
|----------|----------|-----------------|
| Fine Dining / Destination | Special occasions | Worth traveling for |
| Scene / Going Out | Groups, Friday night | Buzzy atmosphere |
| Date Night | Intimate with wife | NOT pure sushi, NOT loud |
| Neighborhood Comfort (UES) | Nearby, reliable | High distance sensitivity |
| Quick / Casual | Lunch, weeknight | Walk-in friendly |
| Discovery / Unknown | New spots | Never visited flag |

---

## Source Trust Hierarchy Reference

| Tier | Sources |
|------|---------|
| **Tier 1 (Highest)** | Michelin, NYT (Pete Wells) |
| **Tier 2 (High)** | Infatuation, Eater editorial, WSJ, NY Mag, Time Out |
| **Excluded** | Yelp, Google reviews, sponsored content |

---

## Output Cadence Targets

| Output | Frequency | Status |
|--------|-----------|--------|
| Category Guides | Monthly | Not started |
| Weekly Digest | Weekly | Not started |
| Opportunity Alerts | As-needed | Not started |
| Event Horizon | Monthly | Not started |
| Book Summaries | Weekly | Not started |
| Rules for Living | Weekly | Not started |

---

*This project plan should be imported into Asana under the EWC System portfolio.*
