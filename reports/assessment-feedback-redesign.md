# Assessment and Feedback Redesign Draft

**Date:** March 13, 2026  
**Purpose:** Strengthen assessment quality, make weak-signal outcomes more visible, and operationalize course feedback loops for the next iteration of WEB 1430.

**Implementation status:** A first implementation pass is now complete. Quiz 4, Quizzes 6-8, the Midterm, and the Final include stronger code-reading/debug stems, and the Canvas assessment package is generated from the `quizzes/*.json` sources.

## Current limitations

1. **Selected-response dominance**
   All quizzes and both exams are currently multiple-choice / true-false. This is efficient, but it under-measures debugging, code reading, accessibility judgment, and architectural reasoning.

2. **Two learning outcomes rely mostly on labs**
   Browser DevTools and client-side persistence are taught well, but they are not reinforced through standalone graded checkpoints. Students can pass through those topics with only partial mastery until a larger project exposes the gap.

3. **Feedback instruments existed without a delivery path**
   The Week 5 and Week 11 surveys were present in the repo but not embedded in the weekly learner flow. That limited their practical value.

## Design goals

1. Measure reasoning, not just recognition.
2. Add low-stakes checkpoints for fragile skills before major projects depend on them.
3. Close the feedback loop while the course is still in motion, not only after it ends.

## Near-term redesign for next delivery

### 1. Keep quizzes short, but improve item quality

- Add at least one code-reading or debugging stem to Quizzes 4, 6, 7, and 8.
- Add two scenario/debug items to the Midterm and two to the Final.
- If Canvas item support remains selected-response only, use richer stems with short code snippets and error diagnoses.
- If short-answer becomes practical, convert one Midterm item and one Final item to short response.

### 2. Add two low-stakes graded checkpoints

- **DevTools checkpoint (Week 1 or 3):**
  Submit one screenshot from DevTools plus a 2-3 sentence explanation of what was inspected and what was learned.

- **Persistence checkpoint (Week 10):**
  Submit a short state trace showing `getItem`, parse/default handling, and one screenshot of the stored value in DevTools.

These should be lightweight completion- or rubric-based items, not full assignments.

### 3. Formalize the course feedback loop

- Keep the Week 5 and Week 11 surveys as published course artifacts.
- Surface them in the weekly schedule and module overviews.
- Add one instructor follow-up step:
  Post a short "You said / I changed / I am watching" note in the next weekly announcement.

This creates visible responsiveness without overcommitting to immediate redesign.

### 4. Use the Final Project beta as a structured feedback instrument

Require the Week 14 beta review to answer three prompts:

- What is currently strongest in your project?
- What is the biggest remaining risk before final submission?
- What specific kind of feedback do you want from the instructor or peers?

That makes the beta a meaningful diagnostic checkpoint rather than only a status report.

## Suggested assessment map changes

| Area | Current state | Proposed adjustment |
|------|---------------|--------------------|
| DevTools | Lab-heavy | Add low-stakes checkpoint |
| localStorage / sessionStorage | Lab + Project 2 | Add low-stakes checkpoint |
| Quizzes | Mostly recall/recognition | Add code-reading/debug stems |
| Midterm / Final | Selected-response only | Add scenario/debug emphasis; consider 1 short-answer item each |
| Course feedback | Repo docs only | Surface in Weeks 5 and 11 and respond in announcements |

## What not to change yet

- Do not replace the milestone structure for Projects 1, 2, or the Final Project. That structure is already one of the course's strengths.
- Do not make every quiz longer. The problem is item depth, not item count.
- Do not add a full new assignment until delivery data shows a real failure pattern.

## Success indicators to monitor next term

- Fewer students reporting that Week 12 feels like a blind transition into Vue.
- Better Project 2 persistence scores.
- Fewer final-project accessibility failures caught only in Week 14.
- Survey completion rates high enough to produce actionable Week 5 and Week 11 signals.
