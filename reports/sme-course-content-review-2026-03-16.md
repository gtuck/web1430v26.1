# SME Course Content Review Memo: WEB 1430 Client-Side Web Development

**Reviewer:** Codex  
**Date:** March 16, 2026  
**Review mode:** Content Review Mode  
**Scope reviewed:** `syllabus.md`, `course/syllabus.md`, `course/schedule.md`, representative module overviews, lectures, labs, assignments, projects, support docs, textbook chapters, and quiz source files  
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

A later alignment pass also strengthened the surrounding course ecosystem:

5. Week 12-15 pacing now shifts some Final Project planning earlier and treats Lab 13 as stronger applied QA evidence
6. Week 00 now teaches Git sync/recovery habits instead of stopping at the first push
7. API-driven briefs now require viability checks and major projects now require lightweight README documentation
8. textbook chapters now reflect those same API, storage/privacy, documentation, and QA expectations

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

### 5. Late-course scaffolding and QA evidence improved further

The course now shifts a small amount of Final Project planning earlier into Week 12, clarifies Week 13 as revision work rather than a cold-start planning week, and treats `Lab 13` as stronger applied QA evidence while reducing `Quiz 8` to a short readiness check.

Updated sources:

- `course/schedule.md`
- `modules/week-12-overview.md`
- `modules/week-13-overview.md`
- `modules/week-14-overview.md`
- `modules/week-15-overview.md`
- `projects/final-project-campus-or-community-tool.md`
- `labs/lab13-lighthouse-accessibility-and-deployment.md`
- `course/quiz-alignment.md`
- `quizzes/quiz-8-testing-performance-and-deployment.json`

### 6. Git workflow, documentation, and textbook alignment improved

The course now makes three expectations more explicit than before:

- Week 00 teaches `git status` and `git pull --ff-only` as baseline sync/recovery habits
- API-driven work requires students to think about CORS, rate limits, attribution, and data reliability before they build
- major project work requires lightweight `README.md` documentation, and the textbook now teaches that expectation instead of leaving it implicit

Updated sources:

- `labs/lab00-local-setup-and-github-workflow.md`
- `modules/week-00-overview.md`
- `lectures/week-00-lecture.md`
- `assignments/assignment-4-api-data-story.md`
- `projects/project-2-data-driven-micro-app.md`
- `projects/final-project-campus-or-community-tool.md`
- `textbook/chapters/chapter-08-design-systems-and-small-front-end-architecture.md`
- `textbook/chapters/chapter-09-fetch-json-and-remote-data.md`
- `textbook/chapters/chapter-10-storage-preferences-and-state.md`
- `textbook/chapters/chapter-11-modules-npm-and-vite.md`
- `textbook/chapters/chapter-14-performance-testing-and-deployment.md`

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
