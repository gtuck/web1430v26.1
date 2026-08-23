# Week 13 Overview: Framework Forms and Data Flow

## This week
- Theme: Framework Forms and Data Flow
- Lecture: Component Communication, Reactive Forms, and Derived State
- Lab: Lab 12 – Small Data Dashboard
- Studio: Dashboard Studio and Milestone Revision
- Deliverables: Assignment 6, Final Project Revised Wireframe and Data Plan, Vue and Workload Pulse Check

## Live sessions
- **Monday 9:30–10:45 AM:** Component communication, reactive forms, and derived state, demonstrated one workflow step at a time.
- **Wednesday 9:30–10:45 AM:** Lab 12 dashboard studio, an Assignment 6 build-order clinic, and a Milestone 2 revision workshop for the Final Project.
- Thanksgiving falls on Thursday, November 26, so both sessions this week meet as normal (Monday Nov 23 and Wednesday Nov 25). If you are travelling, watch the recordings and keep the Sunday deadline in view — this is one of the heaviest weeks of the term.
- Sessions meet in the [class Zoom room](https://weber.zoom.us/j/82982068432); recordings are posted to Canvas.

## Success plan
1. Before Monday: skim the module overview and read the chapter
2. Attend Monday's live session for the week's core concepts and demo
3. Start the lab and read the studio notes; bring blockers to Wednesday's session
4. Attend Wednesday's live session for guided lab work, code review, and Q&A
5. Finish the weekly assessment or milestone, then commit and deploy your work

## Resources
- [Lecture notes: Component Communication, Reactive Forms, and Derived State](../lectures/week-13-lecture.md)
- [Studio notes: Dashboard Studio and Milestone Revision](../lectures/week-13-studio.md)
- [Chapter 12: Introductory Component-Based Development](../textbook/chapters/chapter-12-introductory-component-based-development.md) (continued)
- [Chapter 13: Accessibility Synthesis](../textbook/chapters/chapter-13-accessibility-synthesis.md) — **finish the second half** (focus management, `prefers-reduced-motion`, and the 3-minute manual audit checklist); you read the WCAG and ARIA-pattern sections in Week 12
- [Vue Transition Guide](../course/vue-transition-guide.md) — Use the parent/child event checklist before debugging your entire app.
- [Assignment 6 brief](../assignments/assignment-6-reactive-form-workflow.md) — Follow the build-order section so the workflow works one step at a time instead of all at once.
- [Final Project brief](../projects/final-project-campus-or-community-tool.md) — Use your Milestone 1 feedback and planning starter to revise the wireframes and data plan after one core interaction or scaffold already exists.
- [Vue and Workload Pulse Check](../course/student-survey-week-13.md) — Complete the anonymous instructor-provided survey link so late-course pacing and Vue support can be adjusted during the live term.
- **Time estimate:** 10–12 hours (reading, lab, Assignment 6, Final Project Milestone 2 revision)

## What students usually struggle with
- This week combines validation, emits, derived state, focus management, and revision work. Do not solve all five at once. Get one step working, then repeat the pattern.
- Shared workflow state should stay in the parent. Let each step own only its temporary input state and emit upward when the user advances.
- Milestone 2 should feel like refinement, not a blank-page planning week. If you are still inventing the whole final project now, narrow the scope immediately.

## Checkpoint question
Where is the clean boundary between local step input state and the parent-controlled workflow state in your Assignment 6 app?
