# Project 2 – Data-Driven Micro-App

**Due:** End of Week 14 (three milestones across Weeks 10, 12, and 14)
**Weight:** Part of Projects (30% of course grade)
**Skills:** Fetch API, async/await, error handling, localStorage, ES modules, Vite, file organization by responsibility

---

## Overview

A micro-app is a small, focused browser application that does one thing well. It loads real data from an external source, lets users interact with and filter that data, remembers user preferences across sessions, and handles every possible state — loading, success, error, empty — gracefully.

This project is the culmination of the async and state management half of the course. It requires you to combine the Fetch API, `localStorage`, and ES module organization into a deployed, production-ready application.

## Recommended pacing

Use the milestone structure as a workload guardrail, not just as grading checkpoints.

- **Week 10:** choose the audience, test the API, and normalize one example object before you write much UI code.
- **Week 11:** scaffold the Vite project and get the fetch → normalize → render path working with real data.
- **Week 12:** reach the deployed build checkpoint with one interaction type and one persistence feature already working.
- **Week 13:** add the second interaction, improve accessibility, and remove fragile code before the final week gets crowded.
- **Week 14:** run `npm run build`, test keyboard flow, verify error and empty states, and submit the polished final version.

If you delay the build checkpoint work until Week 13, this project will compete directly with `Assignment 6` and the `Final Project`.

---

## Scenario

You are building a small public-facing tool for a specific audience. Start by identifying a problem worth solving — then find the data that solves it. A tool built backward from an API tends to feel like a tech demo; a tool built from a real need tends to feel like a product.

**Start here — three questions before you write any code:**
1. Who is this for? (a specific type of person, not "everyone")
2. What do they need to do, and why is it currently inconvenient?
3. What data would make that task faster or easier?

Once you can answer those three questions, find a public API that provides the data you need.

**Examples that start from the problem:**
- *College students planning meals on a budget* → a recipe finder filtered by ingredient and cost (using TheMealDB or Spoonacular free tier)
- *Someone curious about a country before traveling* → a country snapshot with population, currency, and time zone (using REST Countries)
- *A space enthusiast wanting a daily photo* → a NASA APOD viewer with a saved personal gallery (using NASA Open APIs)
- *A reader managing a reading list* → a book search with saved favorites (using Open Library)
- *A dog owner comparing breeds* → a filtered gallery with saved preferences (using Dog CEO API)

Notice that the problem comes first in every example. Choose a public API that does not require payment information for access.

> **Reference:** See `course/api-troubleshooting-guide.md` for help with deeply nested responses, fields that are sometimes null, inconsistent types, CORS errors, rate limiting, and a debugging checklist.

---

## Milestone 1 — Proposal and Data Plan

**Due:** End of Week 10

Submit `projects/project-2/proposal.md` containing these sections **in this order**:

1. **Problem statement:** Who specifically is this for? What task does the tool help them complete? Why is that task currently inconvenient without this tool?
2. **API:** Which API provides the data needed to solve that problem? Paste the endpoint URL you will use. Paste one example of the raw JSON response (or a relevant excerpt).
3. **Data model:** What does one normalized item look like as a JavaScript object? List each property, its type, and where it comes from in the raw API response.
4. **UI sketch:** A wireframe showing the layout of the loaded state, the loading state, and the error state.
5. **localStorage plan:** What preferences or data will you persist? What is the key name and what does the stored value look like?

The proposal will be reviewed against the problem statement first. If the problem statement is vague ("users can search for things"), the proposal will be returned for revision before you build.

---

## Milestone 2 — Build Checkpoint

**Due:** End of Week 12

Milestone 2 must represent a substantially complete application. Weeks 13 and 14 are for polish, accessibility review, deployment, and final quality checks — not initial scaffolding. An incomplete Milestone 2 means an incomplete final submission.

A deployed version with **all of the following**:

- Vite project scaffolded, running, and deployed (`npm run dev` works; live URL accessible)
- All five required module files exist (`api.js`, `normalize.js`, `render.js`, `state.js`, `events.js`), each with its one-sentence comment and correct single responsibility
- Fetch, normalization, and render pipeline complete — real API data flows through `normalizeData()` before any rendering function touches it
- Loading, success, and error states all produce distinct UI (not placeholder text)
- At least **one** user interaction type (search, filter, or sort) functional end-to-end
- At least **one** localStorage feature reading and writing correctly (preference restored on page reload)

Submit live URL and repo URL. Include a `checkpoint.md` note (3–5 sentences) covering:
- What two features remain for Week 12?
- Did you encounter any API quirks during normalization? How did you handle them?

Before leaving Milestone 2, verify these four things:

- the app works from a deployed URL, not only `npm run dev`
- one interaction works end-to-end with real data
- one persistence feature restores correctly on reload
- your loading, error, and success states are visibly different

---

## Milestone 3 — Final Submission

**Due:** End of Week 14

---

## Required features

### Data loading
- On initial page load, fetch and render a meaningful starting dataset automatically (do not require user action before seeing data)
- Show a loading indicator before the request; remove it in `finally`
- Check `response.ok`; throw a descriptive error if false
- Wrap in `try/catch`; show a user-facing error message in the catch block (not just a console log)

### User interaction
At least **two** of the following interaction types:
- **Search:** A text input that filters results by querying the API or filtering loaded data
- **Filter:** A dropdown, set of buttons, or checkboxes that narrows results by a data property (category, region, type, etc.)
- **Sort:** A control that reorders results by a property (name, date, popularity, etc.)
- **Pagination or load more:** A button that fetches the next page of results

### Persistence
At least **two** of the following persistence features:
- Save a user preference (theme, filter state, sort order) to `localStorage` and restore it on page load
- Save a list of favorited or bookmarked items to `localStorage`; display a count or a saved list
- Cache the most recent successful result in `sessionStorage` and restore it on reload

### Detail view
Clicking a result card must reveal additional information about that item — either:
- Expanded inline (toggle a detail panel within the card)
- Rendered to a dedicated detail section on the same page
- A second fetch that retrieves additional data for that specific item

### Empty and error states
- An empty state message when a search or filter returns no results
- A specific error message for each failure type (network error, HTTP error, empty results)

---

## Required module structure

```
projects/project-2/
  index.html
  package.json
  .gitignore          ← node_modules/ and dist/
  src/
    main.js           ← entry: imports and initializes
    api.js            ← fetch functions; no DOM access
    normalize.js      ← data transformation; pure functions
    render.js         ← DOM rendering functions; no fetch calls
    state.js          ← localStorage read/write functions
    events.js         ← event listener setup
```

Each file must have a one-sentence comment at the top. `node_modules/` and `dist/` must not be committed.

---

## Accessibility requirements

- Results container has `aria-live="polite"`
- Loading, error, and empty messages are descriptive text (not spinner-only)
- All interactive controls (search, filter, sort) have visible `<label>` elements
- Keyboard focus is managed when detail view opens (focus moves to the detail content)
- Color contrast meets WCAG AA

---

## Constraints

- Vanilla JavaScript only (no Vue, React, etc.)
- No jQuery
- No CSS frameworks
- `innerHTML` forbidden for any content derived from API data — use `createElement` / `textContent`
- HTML validates with no errors

---

## Above baseline (stretch)

- Implement `AbortController` to cancel in-flight requests when a new search fires before the previous completes
- Add offline detection: if `navigator.onLine` is false, show a specific "You appear to be offline" message and load from cached `sessionStorage` data if available
- Add keyboard shortcut: pressing `/` focuses the search input

---

## Deliverable

`projects/project-2/` in your repository (Vite project source, no `node_modules/` or `dist/`).

Deploy to Netlify or Vercel.

**Submit to Canvas (Milestone 3):** Live URL, repo URL, rationale link.

---

## Rationale (rationale.md)

Write 6–8 sentences addressing:
- Who is this app for, and what problem does it solve for them?
- Walk through one complete user flow from initial load to seeing a result — what happens at each step in the code?
- How does your normalization function protect the rest of the app from API inconsistency?
- What would you need to change to support a different API with the same UI?

---

## Rubric

| Criterion | Excellent (4) | Proficient (3) | Developing (2) | Incomplete (1) |
|-----------|--------------|----------------|----------------|----------------|
| **Async handling** | `response.ok` checked; `try/catch/finally` used; loading, success, error, and empty states all produce distinct, appropriate UI | Three states handled; `response.ok` checked | Two states handled; no `response.ok` check | No error handling |
| **User interaction** | Two interaction types functional; interactions work together (e.g., search + filter both active simultaneously) | Two types present; minor interaction conflict | One type functional | No user interaction beyond initial load |
| **Persistence** | Two persistence features implemented; preferences restored correctly on page load; `JSON.stringify/parse` used correctly | Two features present; one restoration issue | One feature implemented | No localStorage use |
| **Module structure** | All five required files present; each file has one responsibility and a comment; no circular imports | Four files with correct responsibilities | Three files; some mixing | Single file or no modules |
| **Accessibility** | `aria-live` on results; text-based state messages; labels on all controls; focus managed | Three of four criteria | Two criteria | One or none |
| **Proposal and rationale** | Proposal complete with all five elements; rationale walks through code flow specifically | Proposal complete; rationale addresses three prompts | Proposal partially complete | Missing |
