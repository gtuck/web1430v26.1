# WEB 1430 — First Delivery Monitoring Guide

**Purpose:** This guide operationalizes the "monitor during first delivery" recommendations from the instructional design review. It is instructor-facing. Use it to gather concrete evidence about the late-course workload, the Vue transition, and the overlap between `Project 2` and the `Final Project`.

---

## Monitoring Goals

Track three questions during the first live run of the course:

1. Are Weeks 13–15 producing unusual time pressure or late/incomplete work?
2. Does the Vue transition in Weeks 12–13 correlate with a quality drop in late-course submissions?
3. Does the overlap between `Project 2` and `Final Project` work reduce quality in either artifact?

---

## Data Sources

Use all four of these, not just one:

- **Student surveys:** `course/student-survey-week-11.md` and `course/student-survey-week-13.md`
- **Submission timing:** on-time, late, extension-request, and missing-work counts
- **Rubric performance:** especially `Assignment 6`, `Project 2`, `Final Project Beta`, and `Final Project`
- **Instructor observation log:** repeated bugs, repeated conceptual confusions, and what support interventions were posted

---

## Before the Term Starts

1. Create actual anonymous survey forms for:
   - Week 05 Mid-Course Check-In
   - Week 11 Late-Course Check-In
   - Week 13 Vue and Workload Pulse Check
2. Use the markdown files in `course/` as the canonical question banks.
3. Decide where survey data will live:
   - Canvas survey export
   - Microsoft Forms / Google Forms export
   - private spreadsheet
4. Add announcement reminders for:
   - Week 05 survey opening
   - Week 11 survey opening
   - Week 13 pulse-check opening
5. Create a simple tracking sheet with the table in this guide.

---

## Monitoring Calendar

### Week 11: Baseline before Vue

Review:

- Week 11 survey responses
- `Project 2 Build` checkpoint completion
- any extension requests or unusual late submissions in Weeks 9–11

Watch for these warning signs:

- More than **25%** of respondents choose `Not very confident` or `Not at all confident` about Vue readiness
- More than **25%** of respondents report being `Slightly behind` or `Significantly behind` on `Project 2`
- More than **20%** of respondents say the remaining workload feels `Concerning` or `Not realistic`

Suggested response if triggered:

- Post a "what matters most in Weeks 12–13" announcement
- publish one extra worked Vue example or debugging walkthrough
- restate which `Project 2` milestone requirements are most important

### Week 12: Early framework transition check

Review:

- `Quiz 7` completion rate
- `Lab 11` or `Project 2 Build` bug patterns
- office-hour / email questions related to props, refs, emits, or file setup

Watch for these warning signs:

- many students can complete the quiz but cannot begin component work independently
- repeated confusion around `.value`, prop mutation, or event flow

Suggested response:

- post a short debugging note with one small working example
- emphasize "smallest working Vue example" before students scale up

### Week 13: Workload and overlap pulse check

Review:

- Week 13 pulse-check responses
- on-time completion for `Assignment 6`
- on-time completion for Final Project Milestones 1 and 2
- extension requests

Watch for these warning signs:

- More than **30%** of respondents choose `Somewhat confused` or `Very confused` about Vue
- More than **30%** report `13–16 hours` or `More than 16 hours`
- More than **25%** say completing `Project 2` and `Final Project` work without sacrificing quality is `Probably not realistic` or `Not realistic`
- more than **15%** of the class misses `Assignment 6` or a Final Project milestone

Suggested response:

- post a priority-order announcement for Week 14
- narrow the focus of any optional stretch work
- add a short video or note showing one complete parent/child Vue pattern

### Week 14: Artifact comparison week

Review:

- `Project 2` submission quality
- Final Project Beta quality
- late/missing counts
- repeated support requests

Compare these questions:

- Are students submitting a stronger `Project 2` and a weak beta?
- Are students submitting a strong beta but a rushed `Project 2`?
- Are both artifacts slipping in the same criteria: async states, persistence, accessibility, structure, or deployment?

Suggested response:

- if `Project 2` is broadly weaker, the overlap is likely competing with capstone focus
- if betas are broadly weaker, students may be triaging toward the immediately graded project and deferring capstone quality

### Week 15: Final outcome check

Review:

- Final Project completion rate
- Final Exam completion rate
- Course Reflection themes
- final rubric distribution

Ask:

- Did students recover after Beta feedback?
- Did Vue-related issues still appear in final submissions?
- Did end-of-term timing depress polish, accessibility, or deployment quality?

---

## Core Tracking Table

Use one row per week.

| Week | Key artifacts | On-time % | Late % | Missing % | Avg hours signal | Main confusion | Intervention posted? | Notes |
|------|---------------|-----------|--------|-----------|------------------|----------------|----------------------|-------|
| 11 | Survey, Project 2 Build | | | | | | | |
| 12 | Quiz 7, Lab 11 / Project 2 Build | | | | | | | |
| 13 | Assignment 6, FP Milestones 1–2, pulse check | | | | | | | |
| 14 | Quiz 8, Project 2, FP Beta | | | | | | | |
| 15 | Final Exam, Final Project, Reflection | | | | | | | |

---

## Comparison Rubric Focus

When reviewing late-course artifacts, focus on these criteria across multiple assignments/projects:

- `Functionality`
- `Code organization`
- `Persistence`
- `Accessibility`
- `Deployment / polish`

If the same criteria fall in both `Project 2` and the `Final Project`, the issue is probably time pressure or insufficient integration support rather than one weak assignment.

---

## Instructor Response Pattern

After each survey window, post a short announcement in this format:

### You said

- 2–3 short findings from survey or submission data

### I changed

- one concrete action taken this week

### I am watching

- one thing still being monitored

This keeps the feedback loop visible and improves survey participation.

---

## End-of-Term Decision Questions

At the end of first delivery, answer these before changing the structure:

1. Was the main problem **time pressure**, **framework confusion**, or **project overlap**?
2. Did students struggle more with **Vue concepts** or with **managing simultaneous deliverables**?
3. If one change is made first, should it be:
   - reducing overlap between `Project 2` and `Final Project`
   - expanding Vue scaffolding
   - adding another low-stakes checkpoint before Week 13

Do not make all three structural changes at once. Use the first-delivery evidence to choose the smallest justified revision.
