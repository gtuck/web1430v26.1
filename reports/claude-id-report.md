# Instructional Design Review: WEB 1430 – Client Side Web Development

**Reviewer:** Claude (Instructional Design Analysis)
**Date:** March 2026 (Revised)
**Scope:** Full course review — textbook, labs, assignments, projects, quizzes, starters, schedule, learning outcomes, syllabus
**Previous report:** March 2026 (initial draft, written against earlier version of materials)

---

## Executive Summary

WEB 1430 is a substantially complete, professionally executed online learning experience built around a coherent 15-week curriculum. Since the initial review, the course has undergone significant development: all 12 textbook chapters have been written with fully differentiated content, all 14 labs have been specified with scenarios, tasks, and 4-level rubrics, all 6 assignments have been rewritten with calibrated requirements and specific scenarios, all 3 projects have been built out with milestone structures and performance-level rubrics, and a full set of lab starter files has been created.

The course is **ready for delivery** in its current form. Its primary strengths are a well-designed curriculum sequence, consistent accessibility emphasis, design-first project structures, and strong alignment between textbook chapters, labs, and assignments. The most significant remaining gap is the lecture layer: all 16 lecture files are structural templates without substantive content, which is acceptable only if lectures are delivered via video screencasts or live sessions. A secondary gap is the quiz assessment model, which currently assesses recall only and does not include application-level questions.

This report documents the current state, identifies remaining gaps in priority order, and provides specific, actionable recommendations for the next revision cycle.

---

## Section 1: Strengths

### 1.1 Coherent Course Narrative

The 15-week arc has a clear, defensible progression: browser fundamentals → semantic HTML/CSS → JavaScript syntax → control flow → data modeling → DOM → events/forms → design systems → async/Fetch → state persistence → modules → Vue → integration and deployment. Each layer builds on the previous one, and the placement of the midterm at Week 8 (after DOM and forms, before async) creates a natural integration checkpoint.

### 1.2 Textbook: Complete and Differentiated

All 12 chapters are written with topic-specific content throughout. Every chapter contains: a "What this chapter is really about" framing section, topic-specific key ideas with code examples, a concrete mental model, working habits, common mistakes, an accessibility note tied to the chapter's topic, a directed practice prompt, chapter-specific reflection questions, chapter-appropriate vocabulary (not generic boilerplate), and a topic-specific mini checklist.

This was the most critical gap in the original report. It has been fully addressed.

### 1.3 Labs: Concrete, Scaffolded, Accessible

All 14 labs have differentiated scenarios (Wildcat Hiking Club, Campus Services, Open Library Book Search, etc.), named skills, step-by-step tasks, manual testing checklists, and 4-level rubrics. Accessibility is embedded as a first-class requirement in every lab that involves interactivity — not as an afterthought but as part of the specification. Lab 07 is dedicated entirely to accessible form validation; Lab 13 closes the course with a full Lighthouse audit cycle.

Starter files (HTML shells, data arrays, function stubs) have been created for Labs 00–10 and documented in `starters/README.md`. Students have a concrete starting point for every lab.

### 1.4 Assignments: Calibrated and Differentiated

All 6 assignments now have distinct scenarios, requirements calibrated to their position in the course, specific function/component expectations, and rubrics with 4 performance levels and concrete descriptors. The JavaScript requirement has been removed from Assignment 1 (which is correctly HTML/CSS only at Week 2). The sequence from Assignment 1 (HTML/CSS structure) through Assignment 6 (Vue reactive form) traces a clear professional development arc.

### 1.5 Projects: Design-First, Milestone-Driven

All 3 projects include multi-milestone structures that prevent last-minute builds. Project 1 (Style Guide) requires a written proposal before any code. Project 2 (Data-Driven Micro-App) requires a full data plan documenting the API shape, normalized object structure, and localStorage plan. The Final Project requires a pitch, wireframes, a beta review, a final submission, and a course reflection — each graded separately. This is exemplary project management pedagogy for an introductory course.

### 1.6 Accessibility Thread

Accessibility is woven throughout the course rather than treated as a bolt-on topic. It appears in the stated learning outcomes, in the mini checklist of every textbook chapter, in the rubric criteria of every lab, assignment, and project, and in Lab 07 (dedicated form validation) and Lab 13 (Lighthouse audit). Every assignment rubric includes an accessibility criterion with 4 performance levels. WCAG AA compliance and keyboard operability are mandatory for all three projects.

### 1.7 Assessment Variety and Alignment

The course uses a well-varied assessment structure: weekly quizzes (knowledge recall), labs (skill practice in constrained contexts), assignments (individual skill demonstration with specified scenarios), projects (integrated complexity with milestones and design phases), and exams (breadth and retention check). This variety prevents any single assessment type from dominating the grade, and the weighting (Labs 20%, Assignments 20%, Projects 30%) correctly prioritizes application over recall.

### 1.8 Professional Practice Reinforcement

Git workflow (meaningful commits, public repositories, deployment links) is required on every submission. Separation of concerns is explicitly required in Assignments 2–5 and modeled in lab code. Named functions are required throughout. `innerHTML` with user-supplied data is prohibited and explained in Lab 06. These are professional standards presented as standards, not optional suggestions.

---

## Section 2: Remaining Critical Issues

These issues should be addressed before or during the first delivery.

### 2.1 Lectures Are Templates Without Content

**This is the most significant remaining gap.**

All 16 lecture files (Week 00 through Week 15) follow an identical structural template: a focus statement, a "why this matters" paragraph (generic across all weeks), a fixed six-step lecture flow (warm-up → demo → breakdown → bugs → practice → bridge), instructor notes (generic), and an exit ticket (generic format). No lecture file contains actual instructional material: no code examples for the week's topic, no explanation of concepts, no worked problems.

**This is acceptable only if lectures are delivered as video screencasts or live sessions**, in which case the template functions as a preparation outline for the instructor. It is not acceptable if students are expected to read lecture files as standalone learning content.

**Concrete consequence:** A student who opens `lectures/week-09-lecture.md` to read about async/Fetch will find no explanation of Promises, no code examples of `await`, no description of the two-step response pattern. The syllabus does not clarify how lectures are delivered.

**Recommendation:** Add one sentence to the syllabus clarifying the lecture delivery model: "Lectures are delivered as weekly video screencasts (linked from each module overview)" or "Lectures are live Zoom sessions (recorded and linked in Canvas)." Then link recordings from each module overview. If text-based lectures are desired, expand each file with actual content — approximately 500–800 words of topic-specific explanation and code examples.

### 2.2 Chapter 1 Is Underdeveloped

Chapter 1 (Thinking in the Browser) is 68 lines — the shortest chapter in the textbook — despite covering the most foundational concepts in the course: HTTP request/response, HTML parsing, DOM construction, CSSOM, the render tree, and JavaScript execution and blocking.

A student reading Chapter 1 will understand that these things exist but will lack the mental model to reason about execution order. The chapter names `defer` and `async` but does not explain them. It mentions the render tree but does not show how HTML and CSS combine to produce it.

**Recommendation:** Expand Chapter 1 to 150–200 lines. Add:
- A concrete example of parsing a small HTML document top to bottom, showing when each resource is fetched
- An explanation of `defer` vs. `async` with a before/after code example
- A more detailed description of what the render tree is and why it matters for JavaScript timing
- An expanded practice prompt that requires inspecting parsing behavior in DevTools, not just identifying elements

### 2.3 Module Overviews Lack Integration Links and Estimates

All 16 module overview files are brief (400–600 bytes each) and follow a generic structure: weekly focus, deliverables list, and a five-step "success plan" that is identical across all weeks. No overview links to the corresponding lecture file, textbook chapter, or lab document. Students must navigate to these resources independently.

**Recommendation:** Add three lines to each module overview:
1. A direct link to the week's lecture file
2. A direct link to the relevant textbook chapter(s)
3. A time estimate: "This module typically requires 8–10 hours including lab and assignment work"

This is a small change that significantly reduces friction for online, asynchronous students.

---

## Section 3: Moderate Issues

### 3.1 Quizzes Assess Recall Only

All 10 weekly quizzes and both exams use multiple-choice and true/false questions that assess knowledge recognition (Bloom's Levels 1–2). There are no application-level questions: no "given this code snippet, what does it output?", no "which of these is the correct way to handle a 404 response from fetch?", no "what is wrong with this validation function?".

This is partially acceptable because labs and assignments assess skill application at a much higher weight. However, students who score well on quizzes may have a distorted sense of their actual fluency. Recall of `typeof null === 'object'` does not indicate the ability to use it correctly.

**Recommendation:** Add 1–2 code-reading or scenario-based questions to each quiz. These can remain multiple-choice for Canvas compatibility. Example:

*"A developer writes `if (userAge == '28')` in their code. What is the potential problem with this comparison? (A) It always returns false. (B) It uses type coercion and may produce unexpected results. (C) The `if` statement is missing braces. (D) It will throw a SyntaxError."*

This is achievable within the current JSON/QTI format and requires no changes to how quizzes are scored.

### 3.2 No Quiz Alignment Document

The course includes 10 quizzes and 2 exams but no document mapping each quiz to the week, chapter, and specific learning outcomes it covers. This makes it difficult for instructors to verify assessment coverage, identify outcome gaps, or revise the course efficiently.

**Recommendation:** Create `course/quiz-alignment.md` with a table mapping each quiz to:
- The week it is administered
- The textbook chapter(s) it covers
- 2–3 specific learning outcomes it addresses
- The number of questions by type (MC, T/F, application)

### 3.3 No Screen Reader Testing Guide

Labs 07 and 13 and all three projects reference testing with a screen reader (VoiceOver on Mac, NVDA on Windows), but no course material explains how to use a screen reader or what to listen for. For most students, this will be their first interaction with assistive technology.

A student who has never used VoiceOver or NVDA will not know how to enable it, navigate with it, or interpret what they hear. Without this guidance, "test with a screen reader" is an empty instruction.

**Recommendation:** Create a short guide (1–2 pages) titled "Introduction to Screen Reader Testing" and link to it from Lab 13 and the Final Project brief. At minimum, include:
- How to enable VoiceOver on Mac (Cmd+F5) and navigate with arrow keys
- How to install and start NVDA on Windows
- What to check: heading navigation, form labels, error announcements, button names, live region announcements
- What "passing" looks like for each

### 3.4 Final Exam Format Not Described

The syllabus and schedule reference a Final Exam at Week 15 worth part of the 15% exam credit, but no course document describes its format, scope, duration, or how it differs from the midterm. Students need to know whether it is cumulative, identical in format to weekly quizzes, or a different kind of assessment.

**Recommendation:** Add a section to `course/` or the syllabus describing the final exam: format (same MC/T-F as quizzes, or different?), scope (cumulative from Week 1 or focused on Weeks 9–15?), duration (timed?), and weight relative to the midterm.

### 3.5 Assignment 5 and Lab 10 Are Closely Similar

Lab 10 (Convert a Script Bundle into Modules) and Assignment 5 (Modular Refactor) both ask students to take a monolithic JavaScript script and reorganize it into a Vite module project with the same file structure (`api.js`, `render.js`, `events.js`, `main.js`). The lab uses a provided script; the assignment uses the student's own Assignment 4 code (or a provided alternative).

This is intentional scaffolding — do it once in a low-stakes lab, then demonstrate mastery in a graded assignment — and it is pedagogically sound. However, students who submit nearly identical code for both may find the assignment feels redundant.

**Recommendation:** Add one or two requirements to Assignment 5 that go beyond what Lab 10 covers. For example: the assignment could require a `constants.js` file for all magic strings, or a `ARCHITECTURE.md` that diagrams the module dependency graph. This ensures the assignment tests mastery, not repetition.

---

## Section 4: Minor Issues and Suggestions

### 4.1 Starter Files for Labs 11–12 Not Provided

Labs 11 (Vue Card System) and 12 (Small Data Dashboard) require students to scaffold a Vite + Vue project with `npm create vite@latest`. The `starters/README.md` notes this with "*(none)*" but doesn't provide the exact command or what to do after scaffolding.

For students new to npm and Vite, this is a nontrivial step. The first 20 minutes of the lab should not be troubleshooting scaffolding.

**Recommendation:** Add the exact command and first-steps checklist to `starters/README.md` for Labs 11 and 12:
```bash
npm create vite@latest lab11 -- --template vue
cd lab11
npm install
npm run dev
```
Then: delete HelloWorld.vue, create components/MemberCard.vue, add node_modules/ and dist/ to .gitignore.

### 4.2 Project 2 API Selection Framing

Project 2 (Data-Driven Micro-App) provides a list of 7 suggested APIs (Open Library, JSONPlaceholder, REST Countries, etc.) and asks students to choose one. The current framing selects the API first, then finds a problem — which often leads to "yet another book finder" built because Open Library is familiar from Lab 08, not because the student had a genuine use case in mind.

**Recommendation:** Reframe the selection guidance: "Start by identifying a specific problem for a specific audience. Then find an API that provides the data needed to solve it." Keep the API list as suggestions, but place the problem statement before the API selection in the proposal template.

### 4.3 Chapter 1 and Chapter 13 Coverage Gap

There is no textbook chapter explicitly covering testing, performance, or the deployment pipeline. Lab 13 (Lighthouse) and the Final Project handle these topics in practice, but students encounter Lighthouse for the first time in Lab 13 without a conceptual framing.

**Recommendation (optional):** A 13th chapter covering performance, testing, and deployment would complete the arc: build (Ch 1–12) → ship (Ch 13). Topics could include: Lighthouse categories and what drives each score, image optimization basics, `defer`/`async` and render-blocking resources, what `npm run build` produces and why it matters, and HTTPS/deployment options (GitHub Pages, Netlify, Vercel). This would make Lab 13 more effective by providing context before the audit rather than discovering the context during it.

### 4.4 Course Reflection Prompt Is Excellent; Visibility Is Low

The Final Project brief includes one of the strongest reflection prompts in the course — 5 specific prompts about what was built, the hardest technical problem, what would be changed, how understanding of accessibility grew, and what the student is most proud of. This is genuinely valuable metacognitive practice.

However, it is buried at the bottom of a 200-line project brief. Students working quickly through deliverable requirements may not read it carefully.

**Recommendation:** Extract the course reflection prompt into its own document (`course/course-reflection-prompt.md`) and reference it from both the project brief and the Week 15 module overview. Its visibility should match its importance.

### 4.5 "Above Baseline" Stretch Items Inconsistently Formatted

All 6 assignments and all 3 projects include an "Above baseline (stretch)" section. Labs include stretch items under various headings. The rubrics for labs and assignments include an "Excellent (4)" column that describes work at this level, but the connection between the stretch items and the Excellent rubric column is not always explicit.

**Recommendation:** Add a sentence to each "Above baseline" section: "Work in this section is reflected in the Excellent (4) column of the rubric." This makes the relationship clear without changing either section.

---

## Section 5: Learning Outcome Alignment Audit (Updated)

| Learning Outcome | Chapter(s) | Lab(s) | Assignment(s) | Project(s) | Assessment Status |
|---|---|---|---|---|---|
| Responsive semantic HTML | 2 | 02 | 1 | P1, FP | Strong |
| Readable JavaScript | 3, 4, 5 | 03, 04, 05 | 2, 3 | P1 | Strong |
| Browser DevTools / debugging | 1 | 01, 03 | — | — | Moderate — no graded assignment |
| DOM manipulation | 6 | 06 | 3 | P1 | Strong |
| Accessible form design | 7 | 07 | 2, 3 | FP | Strong |
| Fetch / JSON / remote data | 9 | 08 | 4 | P2, FP | Strong |
| localStorage / state | 10 | 09 | — | P2, FP | Moderate — no dedicated assignment |
| Component-based thinking | 12 | 11, 12 | 6 | FP | Moderate — only one chapter |
| Git / GitHub workflow | 0 | 00 | All | All | Strong |
| Plan, build, test, present | All | All | Rationale | P1, P2, FP | Strong |

**Notable gaps:**
- **Browser DevTools** — Covered in Lab 01 and Lab 03 (debugging) but no dedicated graded assignment. Lab 13 (Lighthouse) partially addresses it. Weight is adequate for a supporting skill.
- **localStorage** — Covered well in Chapter 10, Lab 09, and both major projects, but no dedicated assignment. Students who struggle with this topic have only one practice lab before encountering it in Project 2.
- **Component-based thinking** — Only one textbook chapter and two labs before Assignment 6 (the most complex individual assignment) and the Final Project. The ramp from vanilla JS to Vue in two weeks is workable but tight.

---

## Section 6: Prioritized Recommendations

### Priority 1 — Before First Delivery

1. **Clarify lecture delivery model in the syllabus.** Add one sentence specifying whether lectures are video screencasts, live sessions, or text documents. If video/live, link recordings from module overviews.

2. **Expand Chapter 1** to 150–200 lines with a worked parsing example, `defer`/`async` explanation, and render tree description.

3. **Add resource links to each module overview.** Three lines per overview: link to lecture, link to chapter, time estimate.

4. **Describe the final exam format** in the syllabus or a course document (scope, format, duration, weight).

### Priority 2 — First Revision Cycle

5. **Create `course/quiz-alignment.md`** mapping each quiz to week, chapter, and learning outcomes.

6. **Add 1–2 application-level questions per quiz** (code-reading or scenario-based, still MC format).

7. **Write a screen reader testing guide** (1–2 pages) and link it from Lab 13 and the Final Project.

8. **Add setup instructions for Labs 11 and 12** to `starters/README.md`.

9. **Reframe Project 2 API selection** to start with problem/audience before API choice.

10. **Differentiate Assignment 5** from Lab 10 with one additional requirement beyond what the lab covers.

### Priority 3 — Continuous Improvement

11. **Add Chapter 13: Accessibility First** — a synthesis chapter covering WCAG, testing, ARIA patterns, screen reader usage, and contrast tools.

12. **Add Chapter 14: Performance, Testing, and Deployment** — covering Lighthouse categories, build output, image optimization, and deployment options.

13. **Add a `localStorage` assignment** (optional or replacing a lower-value deliverable) to give this outcome more direct assessment weight.

14. **Survey students at Weeks 5 and 11** on workload, clarity, and confidence. Adjust Vue pacing if Week 12 consistently produces the most distress.

15. **Evaluate Vue pacing after first delivery.** If students consistently struggle with Assignment 6, consider expanding Vue coverage to Weeks 11–13 and shifting modules slightly.

---

## Section 7: Overall Assessment (Updated)

| Dimension | Rating | Change from Initial | Notes |
|---|---|---|---|
| Learning outcome clarity | Strong | — | Outcomes are action-verb, measurable, well-scoped |
| Curriculum sequence | Strong | — | Logical; minor compression risk at Vue introduction |
| Textbook content | Strong | ↑↑ Was "Needs major work" | All 12 chapters fully written and differentiated |
| Lab specificity | Excellent | ↑↑ Was "Needs major work" | 14 labs with scenarios, tasks, rubrics, starters |
| Assignment differentiation | Excellent | ↑↑ Was "Needs major work" | 6 assignments fully rewritten, calibrated to course position |
| Rubric quality | Excellent | ↑↑ Was "Needs work" | 4-level rubrics with descriptors across all graded work |
| Project structure | Excellent | ↑↑ Not previously noted | 3 projects with milestones, design-first proposals, capstone reflection |
| Starter files | Strong | ↑↑ Not previously noted | Labs 00–10 have HTML shells, data files, and function stubs |
| Assessment alignment | Strong | ↑ Was "Adequate" | Most outcomes strongly covered; 3 have moderate weight |
| Lecture content | Needs work | — | Templates without substantive content; requires video/live delivery |
| Quiz quality | Adequate | — | Good concept alignment; recall-only format |
| Accessibility integration | Strong | — | Consistent throughout all materials |
| Module integration | Adequate | — | Structural but generic; no resource links or time estimates |
| Tech stack relevance | Strong | — | Appropriate for 2026 front-end development |
| Portfolio integration | Strong | — | Live URLs, GitHub, and deployments throughout |

**Overall course readiness: Ready for delivery.** The course structure is sound, the assessments are aligned, and the materials are sufficient for students to succeed. The lecture template issue is the primary delivery risk and should be resolved before Week 1 by confirming and communicating the delivery model.

---

*Report updated March 2026. Based on full review of all source Markdown files and JSON quiz files in the repository as of the current revision.*
