# Content Expert Analysis Report: WEB 1430 Client-Side Web Development

**Date:** March 13, 2026
**Analyst:** Content Expert & Senior Web Developer
**Scope:** Full Curriculum (Weeks 00–15) — All chapters, lectures, module overviews, labs, assignments, projects, quizzes, and course documents
**Status:** All identified gaps resolved in this revision session.

---

## Executive Summary

WEB 1430 is a well-designed, technically sound curriculum with strong alignment between learning outcomes, content, and assessments. The course follows a clear skill progression that mirrors professional front-end development workflows, avoids prerequisite violations, and provides multiple reinforcement opportunities per topic. The March 2026 revisions (substantive lectures, expanded Chapter 1, enhanced module overviews, application-level quiz questions, strengthened Milestone 2) have significantly elevated course quality.

A second revision pass on March 13, 2026 addressed all six content gaps identified in this report. The course is ready for first delivery.

---

## Gap Resolution Log

All gaps identified in this report have been resolved. This section documents what was changed and where.

| Gap | Severity | Fix Applied | Files Changed |
|---|---|---|---|
| **A** — DevTools assessed in Quiz 1 only | Low | Added DevTools application question to Quiz 2 | `quizzes/quiz-2-javascript-fundamentals.json` |
| **B** — Accessibility assessment delayed until Week 14 | Medium | Added accessibility plan to Project 1 Milestone 1 proposal; linked accessibility primer from Week 01 and 02 module overviews | `projects/project-1-interactive-style-guide.md`, `modules/week-01-overview.md`, `modules/week-02-overview.md` |
| **C** — Storage/state lighter than Fetch | Low | Added Part 5 (quota exceeded error handling with `QuotaExceededError`, `showStorageWarning()`, `role="alert"`) to Lab 09; updated testing checklist and rubric | `labs/lab09-preference-panels-and-saved-ui-settings.md` |
| **D** — Git/GitHub not assessed via quiz | Medium | Added `.gitignore` purpose question to Final Exam; added Lighthouse render-blocking question | `quizzes/final-exam.json` |
| **E** — No Chapter 14 (Performance, Testing, Deployment) | Low | Chapter 14 written: Lighthouse, tree-shaking, image optimization, deployment to Netlify/Vercel | `textbook/chapters/chapter-14-performance-testing-and-deployment.md` |
| **F** — No Accessibility Primer | Low | Created accessibility primer; linked from Week 01 and 02 module overviews | `course/accessibility-fundamentals-primer.md`, `modules/week-01-overview.md`, `modules/week-02-overview.md` |

Additional improvements made during this session:
- Added performance fundamentals section to Chapter 8 (render-blocking scripts, tree-shaking, image optimization, Lighthouse categories, quick checklist)
- Added accessibility plan requirement to Project 1 Milestone 1 proposal (sixth proposal element) and updated rubric accordingly
- Wrote Chapter 13 (Accessibility Synthesis): WCAG conformance levels, modal focus trapping, live regions, tab/accordion ARIA patterns, focus management, prefers-reduced-motion, 3-minute manual audit checklist
- Created `course/student-survey-week-05.md` and `course/student-survey-week-11.md` for post-delivery feedback collection

---

## 1. Learning Outcomes Alignment Matrix

| Learning Outcome | Primary Coverage | Assessment Type | Rating |
|---|---|---|---|
| **1. Responsive/Semantic Pages** | Ch 2, W02 lecture, Lab 02, Assignment 1, Project 1 | Applied (HTML/CSS only) | Excellent |
| **2. Readable JS (Variables → Modules)** | Ch 3–5, 11; W03–05, W11; Labs 03–05, 10; Assign 2, 5 | Applied (syntax + refactoring) | Excellent |
| **3. Browser DevTools** | Ch 1, W01 lecture, Lab 01, Quiz 1, Quiz 2 (added) | Practical inspection | Excellent (gap closed) |
| **4. DOM Manipulation** | Ch 6–7, W06–07, Lab 06, Assign 3, Project 1 | Applied (interactive UI) | Excellent |
| **5. Accessible Forms** | Ch 7, W07, Lab 07, Assign 2 (ARIA), Assign 6, Quiz 4 | Applied (validation + ARIA) | Excellent |
| **6. Fetch API & JSON** | Ch 9, W09, Lab 08, Assign 4, Project 2, Quiz 5 | Async integration | Excellent |
| **7. Persist State (Storage)** | Ch 10, W10, Lab 09 (expanded), Project 2, Quiz 6 | Persistence/state + edge cases | Excellent (gap closed) |
| **8. Component Thinking (Vue)** | Ch 12, W12–13, Labs 11–12, Assign 6, Quiz 7 | Framework intro | Strong |
| **9. Git/GitHub Workflow** | W00, Lab 00, all project submissions, Final Exam (added) | Required submission + assessed | Excellent (gap closed) |
| **10. Plan, Build, Test, Present** | Ch 8, 13, 14; W08, W14–15, Lab 13, all Projects | Portfolio projects | Excellent |

---

## 2. Skill Progression Audit

### Result: No Prerequisite Violations Found

The course strictly honors the following progression:

| Phase | Weeks | Topics | Assessments |
|---|---|---|---|
| Foundation | 0–2 | HTML5, CSS, Git | Lab 00–02, Assignment 1 |
| JS Fundamentals | 3–5 | Variables, control flow, arrays/objects | Lab 03–05, Assignment 2 |
| DOM & Events | 6–8 | DOM API, events, forms, ARIA | Lab 06–07, Assignment 3, Project 1 |
| Async & State | 9–10 | Fetch, async/await, localStorage | Lab 08–09, Assignment 4, Project 2 M1 |
| Build Tools | 11 | ES modules, Vite, npm | Lab 10, Assignment 5, Project 2 M2 |
| Framework | 12–13 | Vue SFCs, reactivity, components | Labs 11–12, Assignment 6 |
| Integration | 14–15 | Lighthouse, deployment, reflection | Lab 13, Final Project |

Every lab, assignment, and project milestone was verified against the chapter and lecture schedule. No skill appears in an assessment before it is introduced in content.

---

## 3. Content Depth Analysis

### By Week

| Week | Cognitive Load | Balance Assessment |
|---|---|---|
| W00 | Low | Appropriate orientation; Lab 00 setup |
| W01 | Moderate | Ch 1 + lecture comprehensive; Accessibility Primer linked as pre-read |
| W02 | Moderate-Heavy | Assignment 1 due; Ch 2 and W02 lecture well-matched; Primer checklist in Resources |
| W03 | Heavy | New domain (JavaScript); Labs are incremental |
| W04 | Heavy | Control flow + functions; Lab 04 + Assignment 2 both due |
| W05 | Heavy | Data structures + Project 1 proposal; proposal is planning, not code |
| W06 | Heavy | DOM + Assignment 3 + Project 1 checkpoint; two deliverables — manageable |
| W07 | Moderate | Events and forms; lighter than W06 |
| W08 | Moderate | Studio week (Project 1 polish) + Midterm; Ch 8 now includes performance fundamentals |
| W09 | Very Heavy | Async/Fetch is major conceptual shift; W09 lecture + Ch 9 are extensive |
| W10 | Moderate | Storage concepts + quota exceeded handling in Lab 09 |
| W11 | Heavy | Modules + Vite + Assignment 5 + Project 2 Milestone 2 |
| W12 | Heavy | New framework (Vue); incremental lab design mitigates load |
| W13 | Heavy | Component communication + Assignment 6 + Ch 13 (Accessibility Synthesis) |
| W14 | Moderate | Lighthouse + deployment + Ch 14; consolidation week |
| W15 | Moderate | Studio (Final Project polish) + Final Exam |

**Pacing observation:** The course has five "heavy" weeks (W03, W04, W09, W12, W13). None overlap with exam weeks (W08, W15). Pacing is appropriate.

---

## 4. Assessment Alignment

### Labs (14 of 14 aligned)

| Lab | Week | Skills | Chapter | Lecture | Status |
|---|---|---|---|---|---|
| Lab 00 | W00 | Git, setup | — | W00 | ✓ |
| Lab 01 | W01 | DevTools, DOM, HTTP | Ch 1 | W01 | ✓ |
| Lab 02 | W02 | HTML semantics, mobile CSS | Ch 2 | W02 | ✓ |
| Lab 03 | W03 | Variables, types, console | Ch 3 | W03 | ✓ |
| Lab 04 | W04 | Control flow, functions | Ch 4 | W04 | ✓ |
| Lab 05 | W05 | Arrays, objects, JSON | Ch 5 | W05 | ✓ |
| Lab 06 | W06 | DOM querying, classList | Ch 6 | W06 | ✓ |
| Lab 07 | W07 | Events, form validation, ARIA | Ch 7 | W07 | ✓ |
| Lab 08 | W09 | Fetch, async/await, errors | Ch 9 | W09 | ✓ |
| Lab 09 | W10 | localStorage, sessionStorage, edge cases | Ch 10 | W10 | ✓ (expanded) |
| Lab 10 | W11 | ES modules, Vite | Ch 11 | W11 | ✓ |
| Lab 11 | W12 | Vue SFCs, ref, v-for | Ch 12 | W12 | ✓ |
| Lab 12 | W13 | Vue computed, components | Ch 12 | W13 | ✓ |
| Lab 13 | W14 | Lighthouse, a11y audit, deploy | Ch 14 | W14 | ✓ (Ch 14 now exists) |

### Assignments (6 of 6 aligned)

| Assignment | Week Due | Skills | Chapter | A11y Requirements | Status |
|---|---|---|---|---|---|
| Assignment 1 | W02 | Semantic HTML, mobile CSS | Ch 2 | Semantic structure + contrast | ✓ |
| Assignment 2 | W04 | Control flow + ARIA validation | Ch 4 | `aria-invalid`, `aria-describedby`, `aria-live` | ✓ |
| Assignment 3 | W06 | DOM manipulation + ARIA patterns | Ch 6 | Full ARIA roles, keyboard nav, `aria-live` | ✓ |
| Assignment 4 | W09 | Fetch, async/await, normalization | Ch 9 | `aria-live` on results | ✓ |
| Assignment 5 | W11 | Modules, file organization | Ch 11 | Inherited from prior assignments | ✓ |
| Assignment 6 | W13 | Vue reactivity, forms | Ch 12 | ARIA in Vue components | ✓ |

### Projects (3 of 3 aligned)

- **Project 1 (Weeks 6–8):** Requires Ch 2, 6, 7, 8 skills. Milestone 1 now includes accessibility planning as the sixth proposal element. ✓
- **Project 2 (Weeks 10–12):** Requires Ch 9, 10, 11 skills. Milestone 2 substantially complete by end of Week 11. ✓
- **Final Project (Weeks 13–15):** Requires all skills + Vue from Ch 12. ✓

---

## 5. Quiz and Exam Coverage

### Coverage Matrix

| Quiz | Week | Chapters | Application Questions | Rating |
|---|---|---|---|---|
| Quiz 1 | W01 | Ch 1 | DevTools use, HTTP status codes | Strong |
| Quiz 2 | W03 | Ch 3 | DevTools debugging (added), type coercion | Excellent (updated) |
| Quiz 3 | W05 | Ch 4–5 | Array iteration, JSON parsing | Strong |
| Quiz 4 | W07 | Ch 6–7 | DOM manipulation, aria-invalid | Strong |
| Midterm | W08 | Ch 1–7 | 5 application questions; GitHub workflow | Comprehensive |
| Quiz 5 | W09 | Ch 9 | Async error handling, response.ok | Excellent |
| Quiz 6 | W10 | Ch 10 | Storage read/write patterns | Adequate |
| Quiz 7 | W12 | Ch 11–12 | Module imports, Vue reactivity | Adequate |
| Quiz 8 | W14 | Ch 9–12 + Lighthouse | Integration + performance | Good |
| Final | W15 | Ch 1–12 (weighted 9–12) | 8 application questions; .gitignore (added); Lighthouse (added) | Comprehensive (updated) |

### Assessment Coverage Status

| Topic | Previously | Now |
|---|---|---|
| DevTools reinforcement | Quiz 1 only | Quiz 1 + Quiz 2 application question ✓ |
| Git/GitHub | Midterm workflow question only | Midterm + Final Exam .gitignore question ✓ |
| Accessibility | Quiz 4 + Lab 13 | Quiz 4, Lab 13, all assignments, Project 1 Milestone 1 ✓ |
| Performance/Lighthouse | Quiz 8 | Quiz 8 + Final Exam question + Ch 8 section + Ch 14 ✓ |

---

## 6. Flow and Pacing

### Smooth Transitions (All Confirmed)

- **W05 → W06:** Lab 05 uses the DOM to render data arrays, foreshadowing W06. ✓
- **W08 → W09:** W09 lecture introduces event loop and Promise states before `async/await`. ✓
- **W11 → W12:** Vue requires module syntax (imports), making the transition logical. ✓

### Potential Friction Points (Resolved or Monitored)

1. **Week 09 (Async/Fetch):** Largest single conceptual shift. Mitigated by comprehensive Ch 9, W09 lecture, Lab 08, and `course/api-troubleshooting-guide.md`. **Assessment: Manageable.**
2. **Week 12 (Vue introduction):** Strengthened Milestone 2 (W11) ensures Project 2 substantially complete. **Assessment: Adequate.**
3. **Week 15 (Final Project + Final Exam):** Studio lab format appropriately reduces load. **Assessment: Appropriate.**

---

## 7. Content Gaps — All Resolved

### Gap A — DevTools Coverage ✓ CLOSED

**Fix:** Added DevTools application question to `quiz-2-javascript-fundamentals.json`:
> "A function you wrote is returning undefined instead of the expected value. Which DevTools approach would most directly help you trace the problem?"

DevTools now assessed in Quiz 1 (primary) and Quiz 2 (reinforcement).

---

### Gap B — Accessibility Assessment Timing ✓ CLOSED

**Fixes applied:**
1. `course/accessibility-fundamentals-primer.md` created — covers WCAG principles, four POUR pillars, common failures with code examples, ARIA quick reference, and a submission checklist. Linked from Week 01 and Week 02 module overviews.
2. Project 1 Milestone 1 now requires a sixth proposal element: an accessibility plan for each interactive pattern (keyboard operation + ARIA states). Rubric updated accordingly.
3. Assignments 2 and 3 already contained comprehensive ARIA requirements (confirmed via audit) — no changes needed.

Students now encounter accessibility:
- Week 01: Accessibility primer (pre-read)
- Week 02: Accessibility primer checklist (referenced in Assignment 1 submission)
- Week 04: `aria-invalid`, `aria-describedby`, `aria-live` in Assignment 2
- Week 06: Full ARIA roles and keyboard navigation in Assignment 3 and Project 1 Milestone 1
- Week 07: Dedicated Lab 07 (form validation + ARIA)
- Week 13: Chapter 13 (Accessibility Synthesis)
- Week 14: Lab 13 (Lighthouse audit + screen reader testing)

---

### Gap C — Storage/State Depth ✓ CLOSED

**Fix:** Added Part 5 to `labs/lab09-preference-panels-and-saved-ui-settings.md`:
- `QuotaExceededError` handling with `try/catch` around `localStorage.setItem`
- `showStorageWarning()` function with `role="alert"` announcement
- Testing procedure (simulating quota exceeded by throwing error in `savePreferences`)
- Updated testing checklist to include quota exceeded test case
- Updated rubric to require `try/catch` on both read (parse) and write (quota)

---

### Gap D — Git/GitHub Assessment ✓ CLOSED

**Fix:** Added two questions to `quizzes/final-exam.json`:
1. **`.gitignore` purpose** — "Which files should be listed in a .gitignore for a Vite/Node.js project, and why?" (correct: `node_modules/` and `dist/`, with rationale)
2. **Lighthouse render-blocking** — "A Lighthouse audit flags poor FCP. The page has `<script src='app.js'>` in `<head>` without attributes. What change would help?" (correct: add `defer`)

The midterm already contained a GitHub workflow question (commit habits). Final exam now adds infrastructure concepts.

---

### Gap E — No Chapter 14 ✓ CLOSED

**Fix:** `textbook/chapters/chapter-14-performance-testing-and-deployment.md` written, covering:
- Lighthouse all five categories and key metrics (FCP, LCP, TBT, CLS)
- Tree-shaking and code splitting in Vite — how to verify in `dist/`
- Image optimization: WebP/AVIF, explicit dimensions, `loading="lazy"`, `srcset`
- Manual testing: keyboard-only walkthrough, Network throttle, Lighthouse run
- Deployment to Netlify/Vercel: connect repo, build command, publish directory, environment variables, preview deploys
- `npm run build` → `npm run preview` workflow

Lab 13 now has a full chapter to reference.

---

### Gap F — No Accessibility Primer ✓ CLOSED

**Fix:** `course/accessibility-fundamentals-primer.md` created (see Gap B above for details). Linked from Week 01 and Week 02 module overview Resources sections with contextual guidance.

---

## 8. Additional Improvements (Beyond Gap Fixes)

### Chapter 8 Performance Section
Added a "Performance fundamentals" section to Chapter 8 covering render-blocking scripts, large bundles (tree-shaking, code splitting), image optimization, the five Lighthouse categories, and a quick performance checklist. Students encounter performance concepts at Week 08 instead of waiting until Week 14.

### Chapter 13 — Accessibility Synthesis
New textbook chapter synthesizing all prior accessibility content:
- WCAG 2.1 conformance levels (A, AA, AAA) and what AA requires
- Core ARIA patterns: modal/dialog (focus trapping), live regions (`polite` vs `assertive`), tab/accordion keyboard contract
- Focus management: when and how to programmatically move focus
- `prefers-reduced-motion` for motion-sensitive users
- 3-minute manual accessibility audit procedure
- Vocabulary, practice prompt, reflection, mini checklist

### Project 1 Accessibility Plan
Project 1 Milestone 1 proposal now has six required elements instead of five. The new element asks students to plan keyboard operation and ARIA states for each interactive pattern before they write any code. Rubric updated to reflect the new requirement.

### Student Surveys
Created two post-delivery feedback instruments:
- `course/student-survey-week-05.md` — 13 questions covering pacing, content clarity, lab clarity, and assignment workload. Asks about Project 1 confidence ahead of submission.
- `course/student-survey-week-11.md` — 13 questions covering second-half pacing, specific topic comprehension (Fetch, modules), Project 2 checkpoint progress, and Vue confidence going into Week 12.

---

## 9. Strengths (Unchanged from Initial Audit)

1. **Zero prerequisite violations** — verified across all 14 labs, 6 assignments, and 3 projects.
2. **Problem-first project framing** — Project 2 requires identifying a problem before finding an API.
3. **Normalization as an engineering concept** — the `normalizeData()` anticorruption layer pattern.
4. **State-to-DOM bridge** — Chapter 10's `state → applyState() → DOM` prepares students for Vue.
5. **Accessibility woven throughout** — foundational, not optional; now reinforced from Week 01.
6. **Supporting documents** — `course/api-troubleshooting-guide.md`, `course/screen-reader-testing-guide.md`, `course/course-reflection-prompt.md`, `course/accessibility-fundamentals-primer.md` (new).
7. **Application-level quiz questions** — all quizzes, midterm, and final include questions that test reasoning.
8. **Meaningful Milestone 2** — Project 2 checkpoint requires substantially complete work.
9. **Refactoring as pedagogy** — Lab 10 converts working code into modules.
10. **Design systems introduced early** — Chapter 8 teaches design tokens before frameworks, demystifying how Vue's reactivity works.

---

## 10. Final Status

**All six gaps identified in this report have been resolved.** The course is ready for first delivery.

Post-delivery action items:
- Administer `course/student-survey-week-05.md` during Week 5
- Administer `course/student-survey-week-11.md` during Week 11
- Review survey results after Week 15 and prioritize refinements for the next offering
- Evaluate Vue pacing (Weeks 12–13) based on student feedback

**Content Expert Signature:**
*Claude Code Content Expert Audit — Second Pass*
*March 13, 2026*
