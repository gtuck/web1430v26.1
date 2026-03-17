# Quiz Alignment Document

This document maps the current assessment source files in `quizzes/` to the week they are administered, the chapter range they cover, the learning outcomes they assess, and the number of questions currently present in each JSON file.

All current assessment source files use **1 point per question**, so each assessment's `points` value now matches its question count.
The Canvas assessment package is now regenerated directly from these JSON sources, so the quiz files are the assessment source of truth.

---

## Summary Table

| Assessment | Week | Chapter(s) | Questions / Points | Primary Topics |
|-----------|------|-----------|--------------------|----------------|
| Quiz 1 | 01 | Ch 1 | 7 / 7 | Browser layers, progressive enhancement, DevTools, render-blocking scripts |
| Quiz 2 | 03 | Ch 3 | 8 / 8 | Variables, equality, template literals, coercion, debugging |
| Quiz 3 | 05 | Ch 4–5 | 7 / 7 | Objects, JSON, array methods, property access, `map()` / `filter()` |
| Quiz 4 | 07 | Ch 6–7 | 5 / 5 | DOM selection, event listeners, preventDefault, accessible feedback |
| Midterm Exam | 08 | Ch 1–7 | 15 / 15 | HTML/CSS foundations, JS fundamentals, DOM, events, validation, Git workflow |
| Quiz 5 | 09 | Ch 9 | 7 / 7 | `fetch()`, `.json()`, `async/await`, loading states, `response.ok` |
| Quiz 6 | 10 | Ch 10 | 7 / 7 | `localStorage`, `sessionStorage`, serialization, persistence gotchas |
| Quiz 7 | 12 | Ch 11–12 | 7 / 7 | ES modules, Vite, Vue components, props, refs, imports |
| Quiz 8 | 14 | Ch 13–14 | 4 / 4 | Lighthouse categories, accessibility failures, production verification, GitHub Pages base path |
| Final Exam | 15 | Ch 1–14 | 17 / 17 | Cumulative; stronger emphasis on async/state, modules/Vue, accessibility, deployment |

---

## Quiz 1 — Week 01

**Covers:** Chapter 1 – Thinking in the Browser  
**Administered:** End of Week 01  
**Current format:** 7 selected-response questions, 7 points

**Learning outcomes addressed:**
- Use browser developer tools to inspect, debug, and improve client-side code
- Build a correct mental model of HTML, CSS, JavaScript, and DOM behavior in the browser

**Topic checklist:**
- [ ] HTML structure vs CSS presentation
- [ ] Progressive enhancement
- [ ] DOM generation from HTML
- [ ] DevTools for live inspection
- [ ] Render-blocking script placement
- [ ] Elements panel vs source view

---

## Quiz 2 — Week 03

**Covers:** Chapter 3 – JavaScript Syntax, Values, and Expressions  
**Administered:** End of Week 03  
**Current format:** 8 selected-response questions, 8 points

**Learning outcomes addressed:**
- Write readable JavaScript using variables, expressions, and basic debugging techniques
- Use browser developer tools to inspect values while code runs

**Topic checklist:**
- [ ] `const`
- [ ] Strict equality
- [ ] Template literals
- [ ] Array indexing
- [ ] `console.log()`
- [ ] Type coercion
- [ ] Loose-equality risk
- [ ] DevTools-based debugging

---

## Quiz 3 — Week 05

**Covers:** Chapters 4–5 – Decisions, Loops, and Reusable Logic; Modeling Information in JavaScript  
**Administered:** End of Week 05  
**Current format:** 7 selected-response questions, 7 points

**Learning outcomes addressed:**
- Write readable JavaScript using control flow, arrays, objects, and JSON

**Topic checklist:**
- [ ] Object purpose
- [ ] JSON as a data format
- [ ] Array methods
- [ ] Mutation vs non-mutation
- [ ] Property access
- [ ] `map()` vs `filter()`
- [ ] Empty array results

---

## Quiz 4 — Week 07

**Covers:** Chapters 6–7 – The Document Object Model; Event-Driven Interfaces and Forms  
**Administered:** End of Week 07  
**Current format:** 5 selected-response questions, 5 points, including code-reading/debug stems

**Learning outcomes addressed:**
- Manipulate the DOM to create interactive interfaces that respond to user events
- Design and validate accessible forms that provide clear feedback and error recovery

**Topic checklist:**
- [ ] Element selection
- [ ] Event listeners
- [ ] Accessible feedback patterns
- [ ] `event.preventDefault()`
- [ ] UI state as the source of rendered behavior

---

## Midterm Exam — Week 08

**Covers:** Chapters 1–7 (cumulative through Week 07)  
**Administered:** Week 08  
**Current format:** 15 selected-response questions, 15 points, including several scenario/debug items  
**Time limit:** 60 minutes

**Learning outcomes addressed:**
- Browser DevTools and render-pipeline fundamentals
- Responsive semantic markup foundations
- JavaScript syntax, control flow, functions, arrays, and objects
- DOM manipulation, events, validation, and interface safety
- Git/GitHub workflow habits

**Topic checklist:**
- [ ] Semantic HTML
- [ ] Mobile-first thinking
- [ ] Function reuse
- [ ] Truthy/falsy values
- [ ] Objects and JSON
- [ ] Safe DOM updates
- [ ] Event targeting
- [ ] Validation patterns
- [ ] Scope
- [ ] Commit-message workflow
- [ ] `defer`
- [ ] `innerHTML` / XSS risk
- [ ] Array method output tracing

---

## Quiz 5 — Week 09

**Covers:** Chapter 9 – Fetch, JSON, and Remote Data  
**Administered:** End of Week 09  
**Current format:** 7 selected-response questions, 7 points, including code-reading/debug stems

**Learning outcomes addressed:**
- Exchange data with external services using JSON and the Fetch API

**Topic checklist:**
- [ ] `fetch()` return value
- [ ] `response.json()`
- [ ] `async/await`
- [ ] Error handling
- [ ] Loading states
- [ ] `response.ok`
- [ ] Why 404 responses do not automatically reject

---

## Quiz 6 — Week 10

**Covers:** Chapter 10 – Storage, Preferences, and State  
**Administered:** End of Week 10  
**Current format:** 7 selected-response questions, 7 points, including code-reading/debug stems

**Learning outcomes addressed:**
- Persist client-side state with local storage and session storage when appropriate

**Topic checklist:**
- [ ] `localStorage`
- [ ] Persistence after browser close
- [ ] `sessionStorage`
- [ ] State as a UI model
- [ ] Serialization for stored objects
- [ ] Boolean-string gotcha
- [ ] Persistence scope

---

## Quiz 7 — Week 12

**Covers:** Chapters 11–12 – Modules, npm, and Vite; Introductory Component-Based Development  
**Administered:** End of Week 12  
**Current format:** 7 selected-response questions, 7 points, including code-reading/debug stems

**Learning outcomes addressed:**
- Write readable JavaScript using modules
- Apply introductory component-based thinking with a modern JavaScript framework

**Topic checklist:**
- [ ] ES module purpose
- [ ] Vite role
- [ ] Vue component model
- [ ] Reactive state
- [ ] Props
- [ ] `ref().value`
- [ ] Named export imports

---

## Quiz 8 — Week 14

**Covers:** Chapters 13–14 – Accessibility Synthesis; Performance, Testing, and Deployment  
**Administered:** End of Week 14  
**Current format:** 4 selected-response questions, 4 points, used as a short readiness check before the applied QA evidence in Lab 13

**Learning outcomes addressed:**
- Design and validate accessible interfaces
- Plan, test, and deploy polished client-side work

**Topic checklist:**
- [ ] Lighthouse categories
- [ ] Production vs local verification
- [ ] Common Lighthouse accessibility failures
- [ ] Vite base-path configuration for GitHub Pages

---

## Final Exam — Week 15

**Covers:** Chapters 1–14 (cumulative), with stronger emphasis on later-course integration topics  
**Administered:** Week 15  
**Current format:** 17 selected-response questions, 17 points  
**Time limit:** 90 minutes

**Learning outcomes addressed:** All 10 course learning outcomes.

**Topic checklist:**
- [ ] Front-end architecture and progressive enhancement
- [ ] Form UX
- [ ] Async state models
- [ ] Robust API rendering
- [ ] Storage choice
- [ ] Modules and dependency direction
- [ ] Components, props, and data flow
- [ ] Accessibility fundamentals
- [ ] Performance habits
- [ ] Deployment verification
- [ ] `.gitignore` purpose
- [ ] Render-blocking and Lighthouse

---

## Coverage Snapshot

| Learning Outcome | Direct Assessment Coverage | Notes |
|-----------------|----------------------------|-------|
| Browser DevTools / debugging | Quiz 1, Quiz 2, Midterm | Also practiced in Lab 01 and Lab 03 |
| Responsive semantic HTML | Quiz 1, Midterm, Final | Assignment 1 remains the primary applied measure |
| Readable JavaScript | Quizzes 2–3, Midterm, Final | Strong concept coverage plus applied work |
| DOM manipulation | Quiz 4, Midterm, Final | Reinforced in Lab 06 and Assignment 3 |
| Accessible form design | Quiz 4, Quiz 8, Final | Stronger direct performance evidence in labs, assignments, and Lab 13 |
| Fetch / JSON / APIs | Quiz 5, Final | Applied heavily in Assignment 4 and Project 2 |
| localStorage / state | Quiz 6, Final | Reinforced in Lab 09 and Project 2 |
| Component-based thinking | Quiz 7, Final | Assignment 6 provides applied evidence |
| Git / GitHub workflow | Midterm, Final | Also enforced through repo-based submissions |
| Plan, build, test, present | Quiz 8, Lab 13, Final | Lab 13 now provides the primary applied QA evidence for Week 14 |

## Note on Item Types

The current source files still store all quiz and exam items as selected-response questions. Scenario-based, code-reading, and debugging prompts are embedded as multiple-choice items rather than separated into a distinct free-response question type.
