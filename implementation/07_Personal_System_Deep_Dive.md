# Personal System Deep Dive
## Two-Week Implementation Plan

---

## Executive Summary

This document provides a comprehensive design and implementation plan for the EWC Personal System, scoped to be completed within two weeks. The plan prioritizes delivering immediate value (January recommendations, 2AM Principal ideas) while building sustainable infrastructure (database, skills, output cadence) that will compound over time.

**End State After Two Weeks:**
- Ed receives January restaurant + experience recommendations (Day 2)
- Ed receives 2AM Principal NYC experience library (Day 4)
- Operational restaurant database with 75+ entries across all categories
- Working Restaurant Recommender skill
- Working Book Summary Generator skill
- First Monthly Category Guide delivered
- Source monitoring established for ongoing curation

---

## Part 1: Design Philosophy

### 1.1 The Core Problem

Ed articulated this clearly:

> "I'm always trying to solve the same problem—curating extremely high signal-to-noise for the things that interest me. I have a very limited amount of time. So, when I do something (read, for example) I want it optimized relative to all the other ways that I could spend my time."

The Personal System solves this by:
1. **Curating** — Filtering the world down to excellent options
2. **Categorizing** — Organizing so substitutes aren't confused with non-substitutes
3. **Surfacing** — Proactively showing what's relevant without being asked
4. **Executing** — When Ed says yes, making it happen frictionlessly

### 1.2 The Non-Substitution Principle

This is the architectural foundation:

> "A 3-star is not a substitute for a delicious grilled ham and cheese sandwich from EAT a block from my house on Saturday for lunch."

**Design Implication:** The system must NEVER rank across categories. A "top 10 restaurants" list is meaningless. Instead: "top 3 for date night," "top 3 for neighborhood comfort," etc.

### 1.3 Source Trust as Filter

> "Who says a restaurant is good matters. Most recommendations are for sale. You show up and the place sucks."

**Design Implication:** Every recommendation must carry source attribution. The system should weight Tier 1 sources heavily and exclude untrusted sources entirely.

| Tier | Sources | Weight |
|------|---------|--------|
| **Tier 1** | Michelin Guide, NYT (Pete Wells, other critics) | Highest |
| **Tier 2** | The Infatuation, Eater NY (editorial), WSJ, NY Mag, Time Out, Grub Street | High |
| **Excluded** | Yelp, Google Reviews, TripAdvisor, sponsored content, influencer posts | Zero |

### 1.4 The Journey Principle

> "He's not trying to reach some end state of satisfaction. The continuous stream of excellent options is the point."

**Design Implication:** The system must continuously refresh. "New" and "Unknown" flags are critical. Staleness is failure.

---

## Part 2: Data Architecture

### 2.1 Why Airtable (Not Spreadsheet, Not Neo4j)

For a two-week sprint with ongoing maintenance needs, Airtable is optimal:

| Option | Pros | Cons | Verdict |
|--------|------|------|---------|
| Google Sheets | Simple, familiar | Poor filtering, no relational data, clunky | No |
| Neo4j | Powerful queries, already used for MR | Overkill for ~200 restaurants, requires Anthony | No |
| Notion | Nice UI | Weak filtering, slow | No |
| **Airtable** | Relational, excellent filtering, views, forms, API | Small learning curve | **Yes** |

Airtable advantages for this use case:
- Multiple linked tables (Restaurants ↔ Sources ↔ Visits)
- Filtered views by category (one click to see all Date Night options)
- "New this month" filter trivial to create
- API access for skill integration
- Forms for easy data entry
- Mobile app for on-the-go additions

### 2.2 Database Schema

#### Table: Restaurants

| Field | Type | Description | Required |
|-------|------|-------------|----------|
| `name` | Text | Restaurant name | Yes |
| `category` | Multi-select | Primary category(ies) | Yes |
| `neighborhood` | Single-select | NYC neighborhood | Yes |
| `address` | Text | Full address | Yes |
| `distance_from_home` | Formula | Minutes from E 80th & 2nd | Auto |
| `distance_from_office` | Formula | Minutes from 87th & Lex | Auto |
| `cuisine` | Single-select | Cuisine type | Yes |
| `price_range` | Single-select | $, $$, $$$, $$$$ | Yes |
| `sources` | Linked (Sources) | Which sources recommend it | Yes |
| `highest_source_tier` | Rollup | Best source tier (1 or 2) | Auto |
| `michelin_stars` | Number | 0, 1, 2, or 3 | No |
| `visited` | Checkbox | Has Ed been? | Yes |
| `visit_date` | Date | Last visit | No |
| `ed_rating` | Rating (1-5) | Ed's personal rating | No |
| `ed_notes` | Long text | Ed's comments | No |
| `wife_friendly` | Checkbox | Good for date night with wife | No |
| `wife_notes` | Text | Specific wife considerations | No |
| `noise_level` | Single-select | Quiet, Moderate, Loud | No |
| `reservation_difficulty` | Single-select | Easy, Moderate, Hard, Very Hard | No |
| `booking_platform` | Multi-select | Resy, OpenTable, Tock, Phone | No |
| `best_for` | Multi-select | Special occasion, Groups, Solo, Business | No |
| `date_added` | Date | When added to database | Auto |
| `last_updated` | Date | Last modification | Auto |
| `status` | Single-select | Active, Closed, Temporarily Closed | Yes |
| `discovery_flag` | Checkbox | Is this a "discovery" / never-visited spot? | Auto |

**Category Options:**
- Fine Dining / Destination
- Scene / Going Out
- Date Night
- Neighborhood Comfort (UES)
- Quick / Casual
- Discovery / Unknown

**Neighborhood Options:**
- Upper East Side
- Upper West Side
- Midtown East
- Midtown West
- Flatiron / NoMad
- Greenwich Village
- West Village
- East Village
- NoHo
- SoHo
- Tribeca
- Lower East Side
- Chelsea
- Other Manhattan
- Brooklyn (specify)

#### Table: Sources

| Field | Type | Description |
|-------|------|-------------|
| `name` | Text | Source name (e.g., "Michelin Guide 2025") |
| `tier` | Single-select | Tier 1, Tier 2 |
| `type` | Single-select | Guide, Critic, Publication, List |
| `url` | URL | Link to source |
| `date` | Date | Publication/update date |
| `restaurants` | Linked (Restaurants) | Which restaurants it recommends |

#### Table: Visits

| Field | Type | Description |
|-------|------|-------------|
| `restaurant` | Linked (Restaurants) | Which restaurant |
| `date` | Date | Visit date |
| `occasion` | Single-select | Category used for |
| `companions` | Text | Who was there |
| `rating` | Rating (1-5) | Post-visit rating |
| `would_return` | Checkbox | Would go back? |
| `notes` | Long text | What was good/bad |

#### Table: Experiences (for 2AM Principal)

| Field | Type | Description |
|-------|------|-------------|
| `name` | Text | Experience name |
| `type` | Single-select | Speakeasy, Late Night, Adventure, Private, Entertainment |
| `description` | Long text | What it is |
| `why_surprising` | Text | What makes it "2AM Principal" worthy |
| `location` | Text | Where |
| `best_group_size` | Text | Ideal group size |
| `price_estimate` | Text | Approximate cost |
| `booking_required` | Checkbox | Need reservation? |
| `how_to_book` | Text | Booking instructions |
| `source` | Text | How we found it |
| `ed_tried` | Checkbox | Has Ed done this? |
| `ed_rating` | Rating (1-5) | If tried, how was it? |

### 2.3 Key Views to Create

#### Restaurant Views

| View Name | Filter | Sort | Purpose |
|-----------|--------|------|---------|
| **All Active** | Status = Active | Name A-Z | Master list |
| **Fine Dining** | Category contains "Fine Dining" | Highest source tier, then name | Category browse |
| **Date Night** | Category contains "Date Night" + Wife Friendly = Yes | Distance from home | Wife-compatible date options |
| **Date Night (All)** | Category contains "Date Night" | Distance from home | All date night options |
| **Neighborhood UES** | Category contains "Neighborhood Comfort" | Distance from home | Quick nearby options |
| **Scene** | Category contains "Scene" | Name | Going out options |
| **Quick Casual** | Category contains "Quick / Casual" | Distance from home | Easy options |
| **Discovery** | Visited = No | Date added (newest) | Places to try |
| **New This Month** | Date added >= 1st of month | Date added (newest) | Recent additions |
| **Tier 1 Only** | Highest source tier = 1 | Category, then name | Best of the best |
| **Hard to Book** | Reservation difficulty = Hard or Very Hard | Name | Plan ahead |
| **Ed's Favorites** | Ed rating >= 4 | Ed rating desc | Proven winners |

### 2.4 Distance Calculation

For the `distance_from_home` and `distance_from_office` fields, we have options:

**Option A: Manual Entry (Recommended for MVP)**
- Enter estimated minutes when adding restaurant
- Simple, no API needed
- Good enough for 75 restaurants

**Option B: Google Maps API (Future)**
- Calculate automatically from address
- Requires API key and small cost
- More accurate but adds complexity

**Recommendation:** Start with manual entry. Upgrade later if needed.

---

## Part 3: The Restaurant Recommender Skill

### 3.1 Skill Specification

**Name:** `/restaurant` or `Restaurant Recommender`

**Purpose:** Given a category and optional constraints, return the best restaurant recommendations with source citations.

**Input Parameters:**

| Parameter | Type | Required | Example |
|-----------|------|----------|---------|
| `category` | enum | Yes | "date_night", "fine_dining", "neighborhood", "scene", "quick", "discovery" |
| `date` | string | No | "Saturday night", "this Friday", "tonight" |
| `occasion` | string | No | "anniversary", "business dinner", "casual" |
| `group_size` | number | No | 2, 4, 6 |
| `wife_joining` | boolean | No | true/false (applies wife constraints if true) |
| `max_distance` | string | No | "walkable", "10 min", "anywhere" |
| `tried_before` | enum | No | "yes", "no", "either" |
| `price` | enum | No | "any", "$$$+", "$$" |

**Output Format:**

```markdown
## Date Night Recommendations

### Top Picks (Tier 1 Sources)

**1. Le Bernardin** ⭐⭐⭐
- Cuisine: French Seafood
- Location: Midtown West (15 min from home)
- Source: Michelin 3-star, NYT 4-star
- Reservation: Hard — book 2-3 weeks ahead via Resy
- Wife notes: Elegant, conversation-friendly, not too loud
- Ed's past rating: 5/5 (visited Oct 2024)

**2. Atomix** ⭐⭐
- Cuisine: Korean Tasting Menu
- Location: NoMad (20 min from home)
- Source: Michelin 2-star, NYT Critic's Pick
- Reservation: Very Hard — releases monthly
- Wife notes: Intimate, unique experience
- Status: Never visited ✨ DISCOVERY

### Strong Options (Tier 2 Sources)

**3. Via Carota**
- Cuisine: Italian
- Location: West Village (25 min from home)
- Source: Infatuation 9.1, Eater Essential
- Reservation: Moderate — book 1 week ahead
- Wife notes: Romantic, bustling but not deafening
- Ed's past rating: 4/5

---

*Showing 3 of 12 date night options. Say "more" for additional recommendations.*
```

### 3.2 Skill Logic

```
function recommend(params):

    # 1. Filter by category
    results = db.filter(category contains params.category)

    # 2. Apply wife constraints if applicable
    if params.wife_joining AND params.category == "date_night":
        results = results.filter(wife_friendly == true)
        results = results.filter(noise_level != "Loud")

    # 3. Apply distance constraints
    if params.max_distance:
        results = results.filter(distance_from_home <= parse_distance(params.max_distance))

    # 4. Apply tried-before filter
    if params.tried_before == "no":
        results = results.filter(visited == false)
    elif params.tried_before == "yes":
        results = results.filter(visited == true)

    # 5. Apply price filter
    if params.price:
        results = results.filter(price_range matches params.price)

    # 6. Sort by source tier, then by Ed's rating (if visited), then by date added
    results = results.sort(
        highest_source_tier ASC,  # Tier 1 first
        ed_rating DESC,           # Higher rated first
        date_added DESC           # Newer first
    )

    # 7. Format output with source citations
    return format_recommendations(results, limit=5)
```

### 3.3 Airtable API Integration

The skill will query Airtable via API:

```python
import requests

AIRTABLE_API_KEY = "..."
BASE_ID = "..."
TABLE_NAME = "Restaurants"

def get_restaurants(category, filters=None):
    url = f"https://api.airtable.com/v0/{BASE_ID}/{TABLE_NAME}"
    headers = {"Authorization": f"Bearer {AIRTABLE_API_KEY}"}

    # Build filter formula
    formula_parts = [f"FIND('{category}', {{category}})"]
    if filters:
        for key, value in filters.items():
            formula_parts.append(f"{{{key}}} = '{value}'")

    params = {
        "filterByFormula": f"AND({', '.join(formula_parts)})",
        "sort[0][field]": "highest_source_tier",
        "sort[0][direction]": "asc"
    }

    response = requests.get(url, headers=headers, params=params)
    return response.json()["records"]
```

---

## Part 4: The 2AM Principal System

### 4.1 What Makes a "2AM Principal" Experience?

From the John Levy book:
> "A great night out on the town with friends should include the preplanned illusion of a spontaneous event that is surprising, exhilarating, dangerous, and satisfying."

**The Four Criteria:**

| Criterion | Definition | Examples |
|-----------|------------|----------|
| **Surprising** | Unexpected, hidden, not obvious | Secret entrance, hidden room, unexpected venue |
| **Exhilarating** | Creates excitement, energy | Live performance, immersive experience, high stakes |
| **Dangerous** | Edge of transgression (perceived, not actual) | Speakeasy vibe, late-night, exclusive access |
| **Satisfying** | Delivers on the promise | Great drinks, memorable moment, story to tell |

### 4.2 Experience Categories

| Category | Description | Example Venues |
|----------|-------------|----------------|
| **Hidden Speakeasies** | Secret entrances, password required | Please Don't Tell (PDT), Attaboy, Employees Only |
| **Late Night** | Open past midnight, energy after hours | Paul's Casablanca, 169 Bar, Welcome to the Johnsons |
| **Immersive/Theatrical** | Performance, participation | Sleep No More, Then She Fell, Drunk Shakespeare |
| **Private Access** | Members-only, exclusive | Zero Bond, Casa Cipriani, The Ned |
| **Adventure/Unusual** | Unexpected activities | Axe throwing, escape rooms, midnight kayaking |
| **Rooftop/View** | Spectacular setting | Peak at Hudson Yards, The Roof at Park South |
| **Live Music/Jazz** | Intimate performance | Smalls Jazz Club, Blue Note, 55 Bar |
| **Comedy** | Surprise laughs | Comedy Cellar, The Stand, UCB |

### 4.3 Initial 2AM Principal Library (20 Ideas)

This will be delivered by Day 4:

**Hidden Speakeasies (5):**
1. Please Don't Tell (PDT) — Enter through phone booth in Crif Dogs
2. Attaboy — Unmarked door, no menu, bartender creates for you
3. Angel's Share — Hidden in Japanese restaurant, strict rules
4. The Back Room — Prohibition-era speakeasy, teacups for drinks
5. Raines Law Room — Velvet curtains, reservation-only booths

**Late Night Energy (4):**
6. Paul's Casablanca — Chaotic, late, old New York energy
7. Ray's — Cash only, cheap beer, real dive
8. Welcome to the Johnsons — 70s living room aesthetic
9. 169 Bar — East Village institution, open late

**Immersive Experiences (3):**
10. Sleep No More — Wander a hotel, follow the actors
11. Drunk Shakespeare — Actor drinks, performs, chaos ensues
12. The Ding Dong Lounge — Underground punk rock karaoke

**Private/Exclusive (3):**
13. Zero Bond — If Ed has access or knows a member
14. The Ned NoMad rooftop — Hotel rooftop, reservation possible
15. Casa Cipriani — Members club, spectacular setting

**Adventure (3):**
16. SPIN NYC — Ping pong club, surprisingly fun with groups
17. Escape rooms (The Escape Game) — 1 hour, team bonding
18. Brooklyn Boulders — Late night climbing (unusual flex)

**Surprise Endings (2):**
19. Hop on the Staten Island Ferry — Free, runs late, best view of Statue of Liberty
20. Katz's Deli at 1 AM — Legendary pastrami, 24/7, quintessential NY

### 4.4 2AM Principal Curator Skill

**Name:** `/2am` or `2AM Principal Curator`

**Purpose:** Suggest surprising NYC experiences based on group and occasion.

**Input:**
- Group size
- Energy level desired (chill, moderate, high)
- Budget flexibility
- Any constraints (must end by X, wheelchair accessible, etc.)

**Output:** 3-5 curated options with logistics and "why it qualifies" explanation.

---

## Part 5: Book Summary System

### 5.1 Specification

**Deliverable:** 800-1000 word summaries of esoteric nonfiction, delivered weekly.

**What "Esoteric Nonfiction" Means for Ed:**
- Complexity science, evolution of systems
- Economic history and theory (non-mainstream)
- Decision-making and judgment
- Science books that challenge assumptions
- Philosophy of knowledge and progress

**NOT:**
- Business books (too obvious)
- Self-help (too fluffy)
- Current affairs (gets via Macro Roundup)
- Fiction

### 5.2 Source Pipeline

| Source | Frequency | Quality | How to Monitor |
|--------|-----------|---------|----------------|
| **The Browser** | Daily | High | Email subscription |
| **Five Books** | Weekly | High | RSS feed |
| **Farnam Street** | Weekly | High | Email subscription |
| **Marginalian (Brain Pickings)** | 2-3x/week | Medium-High | RSS feed |
| **Edge.org** | Occasional | Very High | Manual check |
| **Santa Fe Institute** | Occasional | Very High | Email |
| **Longreads** | Daily | Medium | Email |
| **LitHub** | Daily | Medium | RSS |

### 5.3 Book Summary Generator Skill

**Name:** `/booksummary`

**Input:** Book title (and optionally: author, or "suggest one for me")

**Output Structure:**

```markdown
# [Book Title]
## By [Author] ([Year])

### Why This Book Matters (100 words)
[What makes this book significant and relevant to Ed's interests]

### The Core Argument (300 words)
[The main thesis and supporting structure]

### Key Insights (400 words)
1. **[Insight 1 headline]**
   [Explanation with specific example or data point]

2. **[Insight 2 headline]**
   [Explanation]

3. **[Insight 3 headline]**
   [Explanation]

### Zinger-Worthy Quotes (100 words)
> "[Direct quote that could win an argument]"

> "[Another memorable quote]"

### Connection to Ed's Arguments (100 words)
[How this relates to Ed's 10 core arguments, if applicable]

---
*Summary generated [date] | Source: [where we found this book]*
```

### 5.4 Weekly Book Summary Cadence

| Day | Activity |
|-----|----------|
| Monday | Review sources, select book for the week |
| Tuesday-Thursday | Generate summary (may require reading/skimming) |
| Friday | Deliver summary to Ed |
| Weekend | Ed reads at leisure |

---

## Part 6: Output Cadence Design

### 6.1 Defined Outputs

| Output | Frequency | Content | Delivery Day |
|--------|-----------|---------|--------------|
| **Monthly Category Guide** | 1st of month | Full restaurant list by category, new additions highlighted | 1st |
| **Weekly Digest** | Weekly | What's new, what's bookable, any alerts | Monday |
| **Book Summary** | Weekly | 800-1000 word summary | Friday |
| **2AM Update** | Monthly | New experience ideas added | 15th |

### 6.2 Monthly Category Guide Format

```markdown
# EWC Restaurant Guide
## January 2026

### Fine Dining / Destination (12 restaurants)

| Restaurant | Cuisine | Stars | Source | Status |
|------------|---------|-------|--------|--------|
| Le Bernardin | French Seafood | ⭐⭐⭐ | Michelin | ✓ Visited |
| Eleven Madison Park | American | ⭐⭐⭐ | Michelin | ✓ Visited |
| Atomix | Korean | ⭐⭐ | Michelin | ✨ NEW |
| ... | | | | |

**New This Month:** Atomix added (Michelin 2-star, received Dec 2025)

---

### Date Night (15 restaurants)

[Same format, filtered for wife-friendly]

---

### Neighborhood Comfort - UES (8 restaurants)

[Same format, sorted by distance]

---

[Continue for all categories]

---

*Guide updated January 1, 2026*
*75 total restaurants tracked | 12 new this month | 45 visited*
```

### 6.3 Weekly Digest Format

```markdown
# EWC Weekly Digest
## Week of January 6, 2026

### 🆕 New Additions
- **Tatiana** (Fine Dining) — New Lincoln Center spot from Kwame Onwuachi, NYT rave review
- **Thai Diner** (Quick/Casual) — NoHo, Infatuation 8.9

### 📅 Worth Booking This Week
- **Le Bernardin** has unusual availability Wednesday
- **Via Carota** released weekend slots

### 📖 This Week's Book Summary
*"The Beginning of Infinity" by David Deutsch*
[Link to full summary]

### 💡 One Rule for Living
*"The best time to plant a tree was 20 years ago. The second best time is now."*
— Chinese Proverb (via Farnam Street)

---
*Questions or requests? Reply to this digest.*
```

---

## Part 7: Two-Week Implementation Plan

### Week 1: Foundation + Quick Wins

#### Day 1 (Monday)
**Morning:**
- [ ] Set up Airtable account and base
- [ ] Create Restaurants table with all fields
- [ ] Create Sources table
- [ ] Create Experiences table
- [ ] Create key views (by category)

**Afternoon:**
- [ ] Begin restaurant data entry: Fine Dining (10 restaurants)
- [ ] Enter all Michelin-starred NYC restaurants

**Deliverable:** Database structure complete

---

#### Day 2 (Tuesday)
**Morning:**
- [ ] Continue data entry: Date Night (10 restaurants)
- [ ] Continue data entry: Neighborhood UES (8 restaurants)

**Afternoon:**
- [ ] **DELIVER: January Restaurant Recommendations to Ed**
- [ ] Format: Category-organized list with source citations
- [ ] Include "new/unknown" highlights

**Deliverable:** ✅ January Recommendations Delivered (P0)

---

#### Day 3 (Wednesday)
**All Day:**
- [ ] Research 2AM Principal experiences
- [ ] Document 20 ideas with full details
- [ ] Categorize by type
- [ ] Add booking logistics

**Deliverable:** 2AM Principal library drafted

---

#### Day 4 (Thursday)
**Morning:**
- [ ] Review and refine 2AM Principal library
- [ ] Add "why it qualifies" for each

**Afternoon:**
- [ ] **DELIVER: 2AM Principal NYC Experience Library to Ed**
- [ ] Format: Categorized with logistics and "surprise factor" explanation

**Deliverable:** ✅ 2AM Principal Ideas Delivered (P0)

---

#### Day 5 (Friday)
**All Day:**
- [ ] Continue restaurant data entry: Scene (10 restaurants)
- [ ] Continue restaurant data entry: Quick/Casual (10 restaurants)
- [ ] Begin entering Source records (link to restaurants)

**Deliverable:** 50+ restaurants in database

---

#### Day 6-7 (Weekend — Optional)
- [ ] Data entry: remaining restaurants to reach 75
- [ ] Quality check all entries
- [ ] Verify source citations

**End of Week 1 Status:**
- ✅ January Recommendations delivered
- ✅ 2AM Principal library delivered
- ✅ 75+ restaurants in database
- ✅ Database structure complete

---

### Week 2: Skills + Cadence

#### Day 8 (Monday)
**All Day:**
- [ ] Build Restaurant Recommender skill
- [ ] Implement Airtable API connection
- [ ] Test category filtering
- [ ] Test wife constraints logic
- [ ] Test output formatting

**Deliverable:** Restaurant Recommender skill v1 working

---

#### Day 9 (Tuesday)
**Morning:**
- [ ] Refine Restaurant Recommender based on testing
- [ ] Add distance filtering
- [ ] Add "discovery" flag highlighting

**Afternoon:**
- [ ] Set up source monitoring (RSS feeds, email subscriptions)
- [ ] The Browser, Five Books, Farnam Street, Edge.org
- [ ] Create source review workflow

**Deliverable:** Restaurant Recommender complete, source monitoring active

---

#### Day 10 (Wednesday)
**All Day:**
- [ ] Build Book Summary Generator skill
- [ ] Design prompt for 800-1000 word summaries
- [ ] Test on sample book
- [ ] Refine output format

**Deliverable:** Book Summary Generator skill v1 working

---

#### Day 11 (Thursday)
**Morning:**
- [ ] Select first book for summary (from source pipeline)
- [ ] Generate first book summary

**Afternoon:**
- [ ] Create Monthly Category Guide template
- [ ] Generate January Category Guide from database

**Deliverable:** First book summary drafted, Category Guide template ready

---

#### Day 12 (Friday)
**Morning:**
- [ ] **DELIVER: First Monthly Category Guide to Ed**
- [ ] **DELIVER: First Book Summary to Ed**

**Afternoon:**
- [ ] Build 2AM Principal Curator skill (simple version)
- [ ] Test with sample queries

**Deliverable:** ✅ Category Guide delivered, ✅ Book Summary delivered

---

#### Day 13-14 (Weekend — Wrap Up)
- [ ] Document all systems
- [ ] Create Weekly Digest template
- [ ] Plan ongoing maintenance cadence
- [ ] Identify Phase 2 priorities

---

## Part 8: Success Criteria

### End of Two Weeks Checklist

| Deliverable | Target | Status |
|-------------|--------|--------|
| January Restaurant Recommendations | Delivered Day 2 | ⬜ |
| 2AM Principal Library (20 ideas) | Delivered Day 4 | ⬜ |
| Restaurant Database | 75+ entries | ⬜ |
| Restaurant Recommender Skill | Operational | ⬜ |
| Book Summary Generator Skill | Operational | ⬜ |
| First Monthly Category Guide | Delivered Day 12 | ⬜ |
| First Book Summary | Delivered Day 12 | ⬜ |
| Source Monitoring | Active | ⬜ |
| Weekly Digest Template | Created | ⬜ |

### What's NOT In Scope (Phase 2)

- Availability checking automation (API complexity)
- Last-minute alert system
- Upgrade hunting
- Calendar integration
- Preference learning
- Rules for Living skill (can add Week 3)
- Event Horizon Scanner (can add Week 3)

---

## Part 9: Ongoing Maintenance

### Weekly Maintenance (30-60 min)

| Task | Time | Day |
|------|------|-----|
| Review source feeds for new restaurants | 15 min | Monday |
| Add any new restaurants to database | 15 min | Monday |
| Select book for weekly summary | 10 min | Monday |
| Generate and send Weekly Digest | 15 min | Monday |
| Generate and send Book Summary | 30 min | Friday |

### Monthly Maintenance (2 hours)

| Task | Time | Day |
|------|------|-----|
| Generate Monthly Category Guide | 30 min | 1st |
| Add new 2AM Principal ideas (2-3) | 30 min | 15th |
| Database cleanup / status updates | 30 min | End of month |
| Review what's working / not working | 30 min | End of month |

---

## Part 10: Risk Mitigation

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Airtable learning curve | Low | Medium | Simple schema; good documentation |
| Data entry takes longer than expected | Medium | Low | Prioritize high-value categories first |
| Ed doesn't find recommendations useful | Medium | High | Deliver early (Day 2), get feedback, adjust |
| Source monitoring overwhelming | Medium | Medium | Start with top 3 sources only |
| Book summary quality insufficient | Medium | Medium | Test on 2-3 books before delivering |

---

## Appendix: Restaurant Seed List (Starting Point)

### Fine Dining / Destination (Priority 1)
1. Le Bernardin (Michelin ⭐⭐⭐)
2. Eleven Madison Park (Michelin ⭐⭐⭐)
3. Chef's Table at Brooklyn Fare (Michelin ⭐⭐⭐)
4. Masa (Michelin ⭐⭐⭐)
5. Per Se (Michelin ⭐⭐⭐)
6. Atomix (Michelin ⭐⭐)
7. Aquavit (Michelin ⭐⭐)
8. Saga (Michelin ⭐⭐)
9. Tempura Matsui (Michelin ⭐⭐)
10. Daniel (Michelin ⭐)

### Date Night (Priority 2)
1. Via Carota (Infatuation 9.1)
2. I Sodi (Infatuation 9.0)
3. Don Angie (Infatuation 8.9, Michelin ⭐)
4. The Polo Bar (Reliable, scene)
5. Cafe Altro Paradiso (Infatuation 8.5)
6. Le Coucou (Michelin ⭐)
7. Gage & Tollner (Brooklyn, worth the trip)
8. Llama Inn (Unique, fun)
9. Lilia (Infatuation 9.2)
10. Al Coro (New, buzzy)

### Neighborhood Comfort - UES (Priority 3)
1. JG Melon (Classic)
2. Café d'Alsace (Reliable French)
3. EAT (Ed mentioned)
4. Sistina (Italian)
5. Sfoglia (Pasta)
6. The Penrose (Gastropub)
7. The Simone (French)
8. Flex Mussels (Seafood)

*Continue building from here...*

---

## Part 11: Source Discovery & Data Ingestion

### 11.1 The Core Problem

The Personal System is only as good as what flows into it. Most "best restaurant" lists recycle the same 50 places. The real value is in:

1. **New openings** — before they're overhyped
2. **Under-the-radar gems** — that critics haven't found yet
3. **Specific use-case fits** — quiet date night, not just "good"

Without a robust source pipeline, we have garbage in, garbage out. This section defines how to construct and maintain that pipeline.

### 11.2 The Tastemaker Layer

These are writers/curators who discover places 3-6 months before mainstream lists:

| Type | Examples | How to Find |
|------|----------|-------------|
| **Food Critics** | Pete Wells (NYT), Ryan Sutton (Eater), Adam Platt (NY Mag) | Already known |
| **Food Writers on Substack** | Alicia Kennedy, Alison Roman, Robert Sietsema | Search Substack; check who critics follow on Twitter |
| **NYC-Focused Newsletters** | The Infatuation's weekly email, Eater NY newsletter | Sign up for all, evaluate signal-to-noise |
| **Instagram Curators** | Food accounts that aren't sponsored-content farms | Harder to filter; look for <50k followers with taste |
| **Industry Insiders** | Restaurant PR people, hospitality reporters | Eater's "Opening Tracker" is the canonical source |

### 11.3 Source Discovery Process

#### Step 1: Systematic Substack/Newsletter Search

1. **Go to Substack.com → Explore → Food & Drink**
   - Filter for NYC-relevant content
   - Subscribe to top 10, evaluate for 2 weeks
   - Keep 3-5 that surface genuinely new info

2. **Search terms to try:**
   - "NYC restaurants"
   - "New York dining"
   - "Manhattan food"
   - "restaurant openings"
   - "New York food scene"

3. **Check recommendations within newsletters**
   - Good newsletters cite other good newsletters
   - Follow the chain of references

#### Step 2: Identify Who Tastemakers Follow

- Check Twitter/X follows of known food critics
- Look at who The Infatuation editors follow
- See which Substacks established food writers recommend
- Note recurring names across multiple sources

#### Step 3: Industry Source Mining

- **Eater's Opening Tracker** — Canonical source for "what just opened"
- **James Beard Foundation** — Award nominations surface rising talent
- **NY Times "Hungry City" archives** — Discovers neighborhood gems
- **Grub Street Diet column** — Where actual food people eat (not PR choices)

### 11.4 Source Evaluation Rubric

| Criterion | Weight | What to Look For |
|-----------|--------|------------------|
| **Signal-to-Noise** | High | How much is genuinely useful vs. filler/sponsored? |
| **Freshness** | High | Are they finding things BEFORE mainstream coverage? |
| **Specificity** | Medium | Do they explain WHY/WHEN a place works, not just "it's good"? |
| **Source Transparency** | Medium | Do they disclose how they discovered/paid for meals? |
| **Frequency** | Low | Weekly is ideal; daily might be noise |
| **NYC Focus** | High | Is NYC their primary beat or occasional coverage? |

**Scoring:**
- 5 = Exceptional (keep permanently)
- 4 = Strong (keep, review quarterly)
- 3 = Useful (keep for now, may drop)
- 2 = Marginal (unsubscribe)
- 1 = Poor (unsubscribe immediately)

### 11.5 Known Sources (Tier 1-2)

These are already validated and should be monitored:

#### Tier 1: Highest Trust

| Source | Type | Frequency | Best For |
|--------|------|-----------|----------|
| **NYT Restaurant Reviews** | Critic reviews | 1-2/week | Major openings, quality assessment |
| **Michelin Guide NYC** | Annual guide | Yearly + updates | Fine dining, starred restaurants |
| **Pete Wells (NYT)** | Critic | Weekly | Definitive reviews |

#### Tier 2: High Trust

| Source | Type | Frequency | Best For |
|--------|------|-----------|----------|
| **The Infatuation NYC** | Editorial | Weekly newsletter | Curated picks, reliable ratings |
| **Eater NY** | Editorial + tracker | Daily | Opening tracker, news, lists |
| **Grub Street (NY Mag)** | Editorial | Multiple/week | Scene coverage, Grub Street Diet |
| **Time Out NY** | Editorial | Weekly | Broad coverage, events |
| **New Yorker (Tables for Two)** | Critic | Occasional | Thoughtful reviews |

### 11.6 Sources to Investigate

These require evaluation before adding to the pipeline:

#### Newsletters/Substacks

| Name | URL | Why Interesting | Status |
|------|-----|-----------------|--------|
| **Eater NY Newsletter** | eater.com/nyc | Opening tracker is canonical | Evaluate |
| **The Infatuation Weekly** | theinfatuation.com | Curated, reliable | Evaluate |
| **Cooked (Alison Roman)** | alisonroman.substack.com | Tastemaker, NYC-based | Evaluate |
| **From the Desk of Alicia Kennedy** | aliciakennedy.substack.com | Food industry insider perspective | Evaluate |
| **Vittles** | vittles.substack.com | UK-focused but excellent curation model | Evaluate |
| **Taste (David Chang adjacent)** | tastecooking.com | Industry perspective | Evaluate |

#### Other Formats

| Name | Type | Why Interesting | Status |
|------|------|-----------------|--------|
| **The Dave Chang Show** | Podcast | Industry insider, surfaces spots | Evaluate |
| **Grub Street Diet** | Column | Where food people actually eat | Monitor |
| **James Beard Nominations** | Annual | Rising talent identification | Monitor |
| **NY Times "Hungry City"** | Column | Neighborhood gems | Monitor |

#### Instagram (Use Cautiously)

| Account Type | Signal Quality | How to Filter |
|--------------|---------------|---------------|
| Food critics' personal accounts | High | Follow known critics |
| <50k follower curators | Medium | Look for specificity, no #ad |
| Large influencer accounts | Low | Mostly sponsored, avoid |
| Restaurant industry accounts | Medium | Good for openings, biased on quality |

### 11.7 Source Pipeline Tracker Template

Create a spreadsheet or Airtable to track sources:

| Source | Type | URL | Frequency | Signal Score | Subscribed | Trial Start | Notes |
|--------|------|-----|-----------|--------------|------------|-------------|-------|
| Eater NY Opening Tracker | Web | eater.com | Rolling | 5 | Yes | — | Best for new openings |
| The Infatuation NYC | Email | theinfatuation.com | Weekly | 4 | Yes | — | Reliable, slightly mainstream |
| [Substack X] | Email | substack.com/... | Weekly | TBD | Trial | Jan 6 | Evaluating for 2 weeks |
| [Substack Y] | Email | substack.com/... | 2x/week | TBD | Trial | Jan 6 | Found via Alicia Kennedy rec |

### 11.8 Pre-Sprint Source Discovery Protocol

**Before starting the two-week sprint, invest 2-3 hours in source discovery:**

#### Hour 1: Newsletter Signup Blitz
- [ ] Subscribe to 10 food/restaurant newsletters
- [ ] Create dedicated email folder "Food Sources - Evaluation"
- [ ] Set up filters to route to folder
- [ ] Document all subscriptions in tracker

#### Hour 2: Substack Deep Dive
- [ ] Search Substack for NYC food content
- [ ] Subscribe to top 5-7 candidates
- [ ] Note how you found each (recommendation chain)
- [ ] Check "recommended by" sections for more leads

#### Hour 3: Social/Industry Mining
- [ ] Review Twitter follows of 3-4 known food critics
- [ ] Note any recurring newsletter/Substack mentions
- [ ] Check Eater's contributor list for individual voices
- [ ] Set up Google Alert for "new restaurant NYC"

### 11.9 Ongoing Source Maintenance

#### Weekly (5 minutes)
- Scan all source emails
- Flag anything worth adding to database
- Note source quality (mental score adjustment)

#### Monthly (30 minutes)
- Review source tracker
- Unsubscribe from low-signal sources (score <3)
- Search for 1-2 new sources to trial
- Update signal scores based on past month

#### Quarterly (1 hour)
- Full source audit
- Research new Substacks/newsletters
- Check if any sources have declined in quality
- Refresh Instagram follows if using

### 11.10 The Discovery Advantage

The goal is to be **6 months ahead of mainstream lists**:

```
Discovery Timeline:

Month 0:  Restaurant opens
Month 1:  Eater Opening Tracker mentions
Month 2:  Food Twitter buzzes
Month 3:  Infatuation reviews
Month 4:  NY Mag / Grub Street covers
Month 6:  NYT reviews
Month 12: "Best of" lists include it
Month 18: Everyone knows about it, hard to book

TARGET: Be aware at Month 1-2, not Month 12
```

Sources that help you discover at Month 1-2:
- Eater Opening Tracker (Month 1)
- Industry insiders on Twitter (Month 1-2)
- Food-focused Substacks (Month 2-3)
- Grub Street Diet mentions (Month 2-3)

Sources that confirm quality at Month 3-6:
- The Infatuation (Month 3-4)
- NY Mag / Time Out (Month 4-5)
- NYT Reviews (Month 6+)

**Strategy:** Use early sources for discovery, wait for Tier 1-2 confirmation before recommending to Ed (unless it's explicitly flagged as "Discovery/Unknown").

---

*This document serves as the comprehensive design and implementation plan for the EWC Personal System two-week sprint.*
