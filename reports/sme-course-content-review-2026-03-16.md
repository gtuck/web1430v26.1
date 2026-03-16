# SME Course Content Review Memo: WEB 1430 Client-Side Web Development

**Reviewer:** Codex  
**Date:** March 16, 2026  
**Review mode:** Content Review Mode  
**Scope reviewed:** `syllabus.md`, `course/syllabus.md`, `course/schedule.md`, representative module overviews, lectures, labs, assignments, projects, and quiz source files  
**Update status:** Revised after source-level corrections, Canvas package rebuild, and successful validation

---

## Assumed context

- Lower-division university course
- 4-credit, fully online, asynchronous delivery
- Introductory client-side web development with GitHub- and deployment-based workflow
- Source-of-truth review performed from repository markdown/JSON, not from generated Canvas HTML alone

---

## Summary

WEB 1430 is a strong, delivery-ready client-side web development course. The content arc is technically sound, the skills build in a fair order, accessibility is treated as a built-in expectation rather than an add-on, and the applied work asks students to build artifacts that resemble real front-end practice.

I did not find major topic omissions relative to the stated learning outcomes in the original review, and the four priority issues identified in that pass have now been corrected in the source materials:

1. the Final Project pitch now follows the course's Sunday deadline rhythm
2. the two syllabus files are synchronized and both reflect the Week 13 pulse check
3. the Week 09 async lecture now describes rejected Promises accurately
4. the form/persistence briefs now restate the Web Storage privacy guardrail

The course remains strong, and the current state is cleaner and more internally consistent than the initial review snapshot.

---

## Strengths

### 1. Strong technical sequence

The course still moves through the right conceptual order:

- browser mental model before DOM manipulation
- semantic HTML and responsive CSS before JavaScript-heavy work
- JavaScript fundamentals before events and form behavior
- async/state before larger data-driven projects
- modules before Vue
- testing, accessibility audit, and deployment before final submission

That sequence is defensible for the stated audience and supports progressive skill building well.

### 2. Accessibility is embedded across the course

Accessibility is not isolated to one week. It appears in semantic structure, forms, dynamic updates, component work, testing, and final project expectations. Labs and projects repeatedly ask students to connect labels, manage focus, use `aria-live`, validate contrast, and test keyboard behavior. That is a real curricular strength.

### 3. Applied work is authentic and job-relevant

The labs, assignments, and projects require students to:

- use Git/GitHub as part of normal workflow
- deploy real work
- explain technical decisions in writing
- work with API data and persistence
- build interfaces that must function under real constraints

This helps the course prepare students for actual front-end practice rather than topic-by-topic classroom completion only.

### 4. Late-course scaffolding is noticeably better than a typical intro course

The Vue transition guide, build-order language in `Assignment 6`, pacing language in `Project 2`, and milestone structure in the Final Project all show a course team thinking about where students stall. That is appropriate for an asynchronous introductory audience.

---

## Corrections Applied

### 1. Weekly cadence aligned for the Final Project

The Final Project pitch was moved from Monday of Week 13 to Sunday of Week 12. The related pacing language and weekly course documents were updated to match.

Updated sources:

- `projects/final-project-campus-or-community-tool.md`
- `course/schedule.md`
- `modules/week-12-overview.md`
- `modules/week-13-overview.md`

This resolves the earlier cadence mismatch and slightly reduces Week 13 compression by shifting a small but meaningful planning deliverable into the preceding week.

### 2. Syllabus drift corrected

`syllabus.md` and `course/syllabus.md` now match. Both files include:

- the lecture-delivery section
- the exam-policy section
- the Week 13 Vue/workload pulse-check language in the weekly rhythm

Updated sources:

- `syllabus.md`
- `course/syllabus.md`

This resolves the active policy drift identified in the first pass. The duplicate-file maintenance risk still exists structurally, but the learner-facing content is now synchronized.

### 3. Async error explanation corrected

The Week 09 lecture no longer says that errors are "silently swallowed" when an async function is called without `await`. It now explains that the call returns a Promise immediately and that failures may surface as rejected Promises or unhandled rejections if the Promise is never handled.

Updated source:

- `lectures/week-09-lecture.md`

This brings the technical explanation back in line with the actual Promise model students need for debugging and reasoning.

### 4. Privacy/storage guardrails restated in the relevant briefs

The course already taught this rule in Week 10. It is now repeated in the two places where students are most likely to apply persistence to form-like or user-entered data.

Updated sources:

- `assignments/assignment-6-reactive-form-workflow.md`
- `projects/final-project-campus-or-community-tool.md`

Both briefs now explicitly require fictional/demo data where appropriate and prohibit storing sensitive personal data in `localStorage` or `sessionStorage`.

---

## Learning Outcome Check

The stated learning outcomes remain well covered.

- Responsive semantic HTML/CSS: clearly supported by Week 02, Assignment 1, Project 1, and the Final Project
- JavaScript foundations: supported by Weeks 03-05, labs, and assignments before larger interactive work begins
- DOM/events/forms: supported by Weeks 06-07 and applied in Project 1 and Assignment 3
- Fetch/API/state: supported by Weeks 09-10, Lab 08, Lab 09, Assignment 4, and Project 2
- Component thinking: supported by Weeks 12-13, Lab 11, Lab 12, and Assignment 6
- Accessibility: reinforced across structure, forms, dynamic updates, testing, and final deliverables
- Git/GitHub/deployment workflow: embedded from Week 00 through all major submissions

The main limitations are not outcome coverage gaps. After the corrective pass, the remaining concern is ordinary maintenance discipline rather than substantive content weakness.

---

## Final SME Verdict

WEB 1430 is content-strong, current enough to be credible, and appropriate for the stated audience. It teaches durable front-end concepts through realistic practice and does a better-than-average job integrating accessibility, deployment, and maintainability.

My judgment remains that the course is ready for delivery. After the corrections above, there are no major content issues remaining from this review pass. The only continuing low-level maintenance caution is that both syllabus files still exist, so future edits must keep them synchronized.

The corrective pass is complete, and the Canvas package has been rebuilt and validated against the updated sources.
