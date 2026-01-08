# Professional System Project
## Asana Project Plan

---

## Project Overview

**Objective:** Transform the Macro Roundup consumption engine into a content production pipeline that generates OpEds in Ed's voice with minimal friction.

**Key Outcomes:**
- OpEd drafts that require minimal Ed editing
- Zingers accessible via slash command
- Special Edition candidates automatically identified
- Broader content sources integrated

---

## Section: Phase 1 — Quick Wins

### Task: Convert Zinger CLI to Slash Command
- **Description:** Wrap existing `zinger_cli.py` functionality as Claude Code slash command `/zinger`
- **Subtasks:**
  - [ ] Review current CLI implementation
  - [ ] Create skill wrapper
  - [ ] Test with sample queries
  - [ ] Document usage
- **Assignee:** TBD
- **Priority:** P1
- **Difficulty:** Easy

### Task: Compile OpEd Voice Examples Document
- **Description:** Select 5-10 published Ed OpEds and annotate them for AI training: tone, structure, certainty levels, counterargument handling
- **Subtasks:**
  - [ ] Select representative OpEds from different topics
  - [ ] Annotate tone markers
  - [ ] Annotate argument structure patterns
  - [ ] Annotate counterargument handling
  - [ ] Document "too aggressive" vs. appropriate examples
- **Assignee:** TBD
- **Priority:** P1
- **Difficulty:** Easy

### Task: Compile Content Source Expansion List
- **Description:** Research 20+ think tanks and publications for Macro Roundup content expansion
- **Subtasks:**
  - [ ] List current sources being used
  - [ ] Research AEI, Brookings, Heritage, Cato, etc.
  - [ ] Find newsletter signup URLs
  - [ ] Categorize by content focus
  - [ ] Prioritize for trial
- **Assignee:** TBD
- **Priority:** P2
- **Difficulty:** Easy

### Task: Export Zingers to Reference Spreadsheet
- **Description:** Create easily browsable spreadsheet of all 2,434 zingers by argument category
- **Subtasks:**
  - [ ] Query Neo4j for all zingers
  - [ ] Format with argument, score, source, date
  - [ ] Create pivot views by argument
  - [ ] Share with team
- **Assignee:** TBD
- **Priority:** P2
- **Difficulty:** Easy

### Task: Create Special Edition Candidate List
- **Description:** Manual analysis of database to identify 10-15 potential special edition themes
- **Subtasks:**
  - [ ] Review "Growth" tag entries for subthemes
  - [ ] Document AI/investment crowding theme
  - [ ] Document Europe comparison theme
  - [ ] Document Germany problems theme
  - [ ] Document debt crisis theme
  - [ ] Document electricity/AI bottleneck theme
  - [ ] Assess article depth for each theme
- **Assignee:** TBD
- **Priority:** P2
- **Difficulty:** Easy

---

## Section: Phase 2 — Foundation

### Task: Build OpEd Drafter Skill v1
- **Description:** Create first version of OpEd generation skill using voice guidelines
- **Subtasks:**
  - [ ] Design skill prompt structure
  - [ ] Incorporate voice examples
  - [ ] Include zinger integration logic
  - [ ] Add counterargument section
  - [ ] Test on 3 sample topics
  - [ ] Get Ed feedback on drafts
  - [ ] Document calibration needs
- **Assignee:** TBD
- **Priority:** P0
- **Difficulty:** Medium
- **Dependencies:** Voice examples document complete

### Task: Build Counterargument Mapper Skill
- **Description:** Skill that maps common objections to Ed's 10 arguments with suggested rebuttals
- **Subtasks:**
  - [ ] Document typical objections for each argument
  - [ ] Source rebuttals from Ed's published work
  - [ ] Create query interface
  - [ ] Test retrieval accuracy
- **Assignee:** TBD
- **Priority:** P1
- **Difficulty:** Medium

### Task: Build Special Edition Scout Skill
- **Description:** Analyzes Neo4j database to identify emerging themes worthy of special edition treatment
- **Subtasks:**
  - [ ] Design theme detection queries
  - [ ] Set article count thresholds
  - [ ] Add recency weighting
  - [ ] Create output format
  - [ ] Test against known good themes
- **Assignee:** TBD
- **Priority:** P1
- **Difficulty:** Medium

### Task: Build Content Expansion Scout Skill
- **Description:** Identifies new contributors and think tank sources for Macro Roundup diversification
- **Subtasks:**
  - [ ] Define evaluation criteria
  - [ ] Create source monitoring list
  - [ ] Build sample content retrieval
  - [ ] Design recommendation format
- **Assignee:** TBD
- **Priority:** P2
- **Difficulty:** Medium
- **Dependencies:** Content source list complete

### Task: Initiate Tag Refinement Project
- **Description:** Work with Steve to improve broad tags like "Growth" with meaningful subtags
- **Subtasks:**
  - [ ] Review "Growth" tag issues with Steve
  - [ ] Identify other problematic tags
  - [ ] Propose subtag structure
  - [ ] Create tagging guidelines
  - [ ] Implement in Neo4j
- **Assignee:** TBD (requires Steve)
- **Priority:** P2
- **Difficulty:** Medium

### Task: Surface Human-AI Overlap Analysis to Ed
- **Description:** Create presentation of existing overlap analysis for Ed's review
- **Subtasks:**
  - [ ] Compile current overlap metrics
  - [ ] Create visual presentation
  - [ ] Prepare interpretation guide
  - [ ] Schedule review with Ed
- **Assignee:** TBD (requires Anthony)
- **Priority:** P2
- **Difficulty:** Medium

---

## Section: Phase 3 — Automation

### Task: Implement Tag-Level AI View (Centroid Embeddings)
- **Description:** Compute and expose tag-level semantic views using embedding centroids
- **Subtasks:**
  - [ ] Design centroid computation approach
  - [ ] Implement for all 15 categories
  - [ ] Create query interface
  - [ ] Test semantic similarity
  - [ ] Document for team use
- **Assignee:** TBD (requires Anthony)
- **Priority:** P1
- **Difficulty:** Difficult

### Task: Build Special Edition Auto-Identification
- **Description:** System that proactively identifies special edition candidates without human prompting
- **Subtasks:**
  - [ ] Define detection algorithms
  - [ ] Set alert thresholds
  - [ ] Create notification system
  - [ ] Test against historical editions
  - [ ] Tune for precision
- **Assignee:** TBD
- **Priority:** P2
- **Difficulty:** Difficult
- **Dependencies:** Scout skill complete

### Task: Build Market Demand Monitoring Agent
- **Description:** Agent that scans publications for topics where Ed's perspective would be timely
- **Subtasks:**
  - [ ] Identify publications to monitor (WSJ, NYT, etc.)
  - [ ] Define relevance scoring
  - [ ] Create monitoring schedule
  - [ ] Design opportunity alerts
  - [ ] Test accuracy
- **Assignee:** TBD
- **Priority:** P2
- **Difficulty:** Difficult

---

## Section: Phase 4 — Intelligence

### Task: Build OpEd Drafter Skill v2 (Calibrated)
- **Description:** Refined version that produces drafts requiring minimal Ed editing
- **Subtasks:**
  - [ ] Analyze Ed's edits on v1 drafts
  - [ ] Identify systematic corrections
  - [ ] Update prompt engineering
  - [ ] Re-test on multiple topics
  - [ ] Iterate until quality threshold met
- **Assignee:** TBD
- **Priority:** P0
- **Difficulty:** Difficult
- **Dependencies:** v1 + Ed feedback cycles

### Task: Develop Voice Model Refinement Process
- **Description:** Systematic approach to improving AI match to Ed's rhetorical style
- **Subtasks:**
  - [ ] Create feedback capture mechanism
  - [ ] Define quality metrics
  - [ ] Establish refinement cadence
  - [ ] Document learnings
- **Assignee:** TBD
- **Priority:** P1
- **Difficulty:** Difficult

### Task: Address AI Article Selection Challenge
- **Description:** Explore whether AI can articulate "principles and exceptions" for article curation
- **Subtasks:**
  - [ ] Document current human selection criteria
  - [ ] Attempt AI codification
  - [ ] Test against Steve's selections
  - [ ] Assess feasibility
  - [ ] Document conclusions
- **Assignee:** TBD
- **Priority:** P2
- **Difficulty:** Difficult (may be unsolvable)

---

## Key Dependencies

```
Voice Examples Doc → OpEd Drafter v1 → Ed Feedback → OpEd Drafter v2
Content Source List → Content Expansion Scout
Steve Coordination → Tag Refinement
Anthony Coordination → Tag-Level AI View, Overlap Surface
```

---

## Success Metrics

| Metric | Target |
|--------|--------|
| OpEd drafts produced per month | 4+ |
| Ed editing time per draft | < 1 hour |
| Zinger searches per week | 10+ |
| Special edition candidates surfaced | 2+ per quarter |

---

*This project plan should be imported into Asana under the EWC System portfolio.*
