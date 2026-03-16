# Week 13 Overview: Framework Forms and Data Flow

## This week
- Theme: Framework Forms and Data Flow
- Lecture: Component Communication, Reactive Forms, and Derived State
- Lab: Lab 12 – Small Data Dashboard
- Deliverables: Assignment 6, Final Project Pitch, Final Project Wireframe and Data Plan, Vue and Workload Pulse Check

## Success plan
1. Read the module overview and chapter
2. Work through lecture notes
3. Complete the lab or studio activity
4. Finish the weekly assessment or milestone
5. Commit and deploy your work

## Resources
- [Lecture notes: Component Communication, Reactive Forms, and Derived State](../lectures/week-13-lecture.md)
- [Chapter 12: Introductory Component-Based Development](../textbook/chapters/chapter-12-introductory-component-based-development.md) (continued)
- [Chapter 13: Accessibility Synthesis](../textbook/chapters/chapter-13-accessibility-synthesis.md) — WCAG conformance, ARIA patterns, focus management, prefers-reduced-motion, 3-minute manual audit checklist
- [Vue Transition Guide](../course/vue-transition-guide.md) — Use the parent/child event checklist before debugging your entire app.
- [Assignment 6 brief](../assignments/assignment-6-reactive-form-workflow.md) — Follow the build-order section so the workflow works one step at a time instead of all at once.
- [Final Project brief](../projects/final-project-campus-or-community-tool.md) — Milestone 1 pitch is due Monday; Milestone 2 wireframes and data plan are due Sunday.
- [Vue and Workload Pulse Check](../course/student-survey-week-13.md) — Complete the anonymous instructor-provided survey link so late-course pacing and Vue support can be adjusted during the live term.
- **Time estimate:** 12–14 hours (reading, lab, Assignment 6, Final Project Milestones 1–2)

## What students usually struggle with
- This week combines validation, emits, derived state, focus management, and planning work. Do not solve all five at once. Get one step working, then repeat the pattern.
- Shared workflow state should stay in the parent. Let each step own only its temporary input state and emit upward when the user advances.

## Checkpoint question
Where is the clean boundary between local step input state and the parent-controlled workflow state in your Assignment 6 app?
