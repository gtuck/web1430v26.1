# Final Project – Campus or Community Tool

**Due:** End of Week 15 (five milestones across Weeks 12–15)
**Weight:** Largest single component of Projects (30% of course grade)
**Skills:** Full-stack front-end — semantic HTML, responsive CSS, vanilla JS or Vue, Fetch API, localStorage, ES modules, Vite, accessibility, deployment, presentation

---

## Overview

The final project is your capstone: a complete, deployed, portfolio-ready client-side web application built for a realistic audience. It synthesizes every skill from the course — design, structure, behavior, data, state, and accessibility — in a single coherent product.

The tool must solve a real (if small) problem for a defined audience. "Campus or community" is a prompt, not a constraint: your audience can be students, staff, club members, volunteers, local residents, or any group you can describe concretely. The requirement is that the tool is useful and the audience is real, not hypothetical.

## Start-ahead plan

The first graded Final Project milestone lands at the end of Week 12 and now includes a small planning starter, so you should not wait until Week 13 to start thinking.

During Week 12, spend 20 to 45 minutes doing these three things:

1. Choose one likely audience and one specific problem worth solving.
2. Test one API endpoint or local JSON source and confirm that the data is usable.
3. Write a rough feature list with 3 to 5 realistic interactions.

Milestone 1 asks you to capture that work in a small, low-overhead form. The goal is not finished planning in Week 12. The goal is to make Week 13 a revision week instead of a cold start.

## Suggested pacing across Weeks 12–15

- **Week 12:** choose the audience, test data, rule out ideas that are too large, and submit the pitch plus a small planning starter by Sunday.
- **Week 13:** scaffold the project, prove one core interaction is technically possible, and revise the starter into the full wireframes, data plan, and state map while the implementation is still small.
- **Week 14:** reach the beta with all major features present, then use Lab 13 and the audit guides to find weak spots and begin the rationale draft.
- **Week 15:** tighten deployment quality, finish the rationale while your decisions are still visible in the code, and complete the reflection before the final deadline window closes.

---

## Scope

Your project must include **all** of the following capability areas:

| Area | Minimum requirement |
|------|-------------------|
| **Structure** | Semantic, validated HTML; logical heading hierarchy; skip navigation link |
| **Presentation** | Mobile-first responsive layout; CSS custom properties for all design values; consistent visual language |
| **Behavior** | At least three distinct user interactions (not just page load and one click) |
| **Remote data** | At least one fetch from a public API or a local JSON file; full async error handling |
| **Persistence** | At least one `localStorage` feature (saved preference, saved list, or draft) |
| **Code organization** | ES modules via Vite; at minimum four files with clear single responsibilities |
| **Accessibility** | WCAG AA contrast; keyboard-operable; semantic roles; `aria-live` for dynamic content |
| **Deployment** | Live URL; production build via `npm run build` |

You may choose to use Vue for your front-end layer. If you use Vue, the requirement for ES module organization is satisfied by the Vue SFC structure, and you should demonstrate at least two components with props/emits communication.

---

## Milestone 1 — Pitch and Planning Starter

**Due:** End of Week 12 (Sunday)

Submit `projects/final-project/pitch.md` containing:

1. **One-sentence description:** What does it do and for whom?
2. **Problem statement (2–3 sentences):** What specific problem does this solve? Why does this audience need it?
3. **Feature list:** 3–5 bullet points describing what a user can do
4. **API or data source:** What data powers the app? Paste an example endpoint or a sample of the JSON
5. **Tech stack decisions:** Vanilla JS or Vue? Which API? Any other libraries?
6. **Starter sketch:** Paste or link one rough sketch of either the initial/empty state or the loaded state
7. **Data starter:** Draft one normalized object with 4–6 likely properties and add one sentence describing what you expect to store in `localStorage`
8. **API viability check:** In 4 bullets, document CORS/browser access, rate limits or auth requirements, attribution or terms-of-use expectations, and how current/reliable the data appears to be

Pitch feedback will be returned within 48 hours. If scope is too large or too small, you will be asked to adjust before proceeding. The planning starter exists to reduce Week 13 friction, not to make Week 12 feel like a finished design document.

---

## Milestone 2 — Revised Wireframe and Data Plan

**Due:** End of Week 13 (Sunday)

By this point you should already have a starter sketch and a draft normalized object from Milestone 1. Use Week 13 to revise those early ideas after you have scaffolded the project or proven that one core interaction is technically possible.

Submit in `projects/final-project/`:
- `wireframes/` — at minimum three sketches: initial/empty state, loaded state, and a detail or interaction state. Hand-drawn photos are acceptable.
- `data-plan.md` — describing:
  - The shape of one normalized data object (all properties, types, sources)
  - What is stored in `localStorage` (key name, value shape, when it is written/read)
  - Which UI states exist (loading, empty, error, success, detail, etc.)
  - Where each major piece of state lives (for example, UI state, fetched data, selected item, saved preferences)

Use fictional or demo data while planning and testing. Do not store passwords, government IDs, tokens, or other sensitive personal data in `localStorage` or `sessionStorage`.

---

## Milestone 3 — Beta Review

**Due:** End of Week 14

A substantially complete deployed version. At this stage:
- All major features present and functional (may have rough edges)
- Fetch, localStorage, and at least two interactions working
- Mobile layout functional
- Loading and error states implemented

Submit live URL and a brief self-assessment:
- What is working well?
- What is not yet done or not working correctly?
- What help do you need before final submission?
- Which 2–3 issues from your Lab 13 audit or personal QA pass are highest priority before Week 15?

Also start `rationale.md` this week. It does not need to be polished yet, but the file should exist with each required prompt and at least bullet notes under each heading so Week 15 writing becomes revision instead of first drafting.

---

## Milestone 4 — Final Submission

**Due:** End of Week 15 (Sunday)

Submit to Canvas:
- Live URL (deployed production build)
- GitHub repository URL (link to `projects/final-project/`)
- `README.md` link
- `rationale.md` link

The submitted live URL must load within 5 seconds on a standard connection. The deployed version is what is graded — not the source code alone.

Include `README.md` in `projects/final-project/` with:
- audience and problem statement
- setup and run steps
- data source and attribution notes
- accessibility and QA checks performed
- known limitations / future improvements

---

## Milestone 5 — Course Reflection

**Due:** End of Week 15 (same deadline as final submission)

Submit `projects/final-project/reflection.md` using the [Course Reflection Prompt](../course/course-reflection-prompt.md). The prompt contains all five questions and the rubric. Write 6–10 sentences total, with specific, honest answers — not generalizations.

This reflection is graded separately from the project itself (see rubric below).

---

## Technical requirements

### JavaScript / Vue
- All JavaScript in ES modules loaded via Vite
- Minimum four module files with clear single-responsibility comments
- `README.md` in the project root with setup, audience/problem, data source, and QA notes
- No `innerHTML` with user-supplied or API-sourced data
- No `var`; no anonymous functions for named responsibilities

### CSS
- All design values (colors, spacing, type sizes) as custom properties in `:root`
- Mobile-first: base styles work at 375px without a media query
- At least one responsive layout shift with `min-width` media query
- No CSS frameworks

### Accessibility
- `lang` attribute on `<html>`
- Skip navigation link before `<header>`
- All images have meaningful `alt` text (or `alt=""` if decorative)
- All interactive elements keyboard-operable with visible focus style
- `aria-live="polite"` on any region that updates dynamically
- Color contrast: WCAG AA for all text
- HTML validates with no errors at validator.w3.org
- Manual screen reader test completed and documented (see [Screen Reader Testing Guide](../course/screen-reader-testing-guide.md))

### Deployment
- Deployed via Netlify, Vercel, or GitHub Pages
- `npm run build` produces the `dist/` output that is deployed
- `node_modules/` and `dist/` absent from the repository

---

## Commit history requirements

Your repository must show a meaningful commit history:
- At least 10 commits across the project
- Commit messages describe what changed (not "update" or "fix stuff")
- Commits distributed across the build period (not all on the last day)

Committing all work in one or two commits suggests the project was not developed iteratively and will affect the Maintainability criterion.

---

## Constraints

- No full-stack server (Node, PHP, etc.) — client-side only
- No paid APIs or APIs that require payment info for a free tier
- If using Vue: Vue 3 with `<script setup>` only (no Options API)
- No UI component libraries (Bootstrap, Vuetify, etc.)
- If your project models user-entered or account-like information, use fictional/demo data only and never store sensitive personal data in Web Storage
- Original work — cite any code you did not write, including AI-assisted sections

---

## Above baseline (stretch)

- A Lighthouse score of 90+ in all four categories (Performance, Accessibility, Best Practices, SEO) — document your score with a screenshot
- Offline support: a service worker or `sessionStorage` fallback that lets the app function with cached data when the network is unavailable
- A shareable URL: the current view state (search query, filter selection, selected item) reflected in the URL hash so users can bookmark or share a specific state

---

## Rationale (rationale.md)

Write 6–8 sentences addressing:
- Who is this tool for and what specific problem does it solve for them?
- Describe one technical decision you made that improved the user experience
- How is your code organized, and what would a new developer need to understand to contribute?
- What Lighthouse scores did you achieve, and what did you do to reach them?

---

## Rubric

### Project (graded at Milestone 4)

| Criterion | Excellent (4) | Proficient (3) | Developing (2) | Incomplete (1) |
|-----------|--------------|----------------|----------------|----------------|
| **Functionality** | All stated features work correctly; three distinct interactions functional; no broken states | Most features work; one interaction has minor issues | Core feature works; secondary features incomplete or broken | Non-functional or only partially loads |
| **Remote data** | Fetch with `response.ok` check; `try/catch/finally`; loading, success, error, and empty states all handled distinctly | Three of four states handled; `response.ok` checked | Two states handled | No fetch or no error handling |
| **Persistence** | `localStorage` feature correctly reads on load, writes on change, and handles first-visit null case; `JSON.stringify/parse` used for objects | Feature works; first-visit case not handled | Feature present but broken on reload | No localStorage |
| **Code organization** | Four module files with responsibility comments; useful `README.md`; no circular dependencies; no `innerHTML` with external data; no `var` | Three files or README has minor gaps; one minor violation | Two files; weak or missing documentation; some mixing | Single file |
| **Responsive design** | Mobile-first; custom properties for all design values; layout functional at 375px, 768px, and 1280px | Responsive with minor gap at one size | Partially responsive; some custom properties | Not responsive |
| **Accessibility** | Validates; skip nav; alt text; keyboard-operable; `aria-live`; contrast passes; focus visible | Four of six criteria | Three criteria | Two or fewer |
| **Commit history** | 10+ meaningful commits distributed across the build period | 7–9 commits; most meaningful | 4–6 commits | 3 or fewer; or all on one day |

### Course Reflection (graded at Milestone 5)

| Criterion | Excellent (4) | Proficient (3) | Developing (2) | Incomplete (1) |
|-----------|--------------|----------------|----------------|----------------|
| **Depth and specificity** | All five prompts answered with specific, concrete details from the project; demonstrates genuine self-assessment | Four prompts answered specifically | Three prompts; answers somewhat vague | Two or fewer prompts; very vague |
| **Technical honesty** | Identifies real weaknesses and specific things to change; does not claim everything went perfectly | Identifies some weaknesses | Weaknesses mentioned but not specific | Claims no weaknesses or missing |
| **Growth evidence** | Reflection on accessibility prompt shows concrete shift in understanding from start to end of course | Some growth evident | Accessibility prompt answered generically | Not addressed |
