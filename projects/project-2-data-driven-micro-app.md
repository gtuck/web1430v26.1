# Project 2 – Data-Driven Micro-App

**Due:** End of Week 12 (three milestones across Weeks 10–12)
**Weight:** Part of Projects (30% of course grade)
**Skills:** Fetch API, async/await, error handling, localStorage, ES modules, Vite, file organization by responsibility

---

## Overview

A micro-app is a small, focused browser application that does one thing well. It loads real data from an external source, lets users interact with and filter that data, remembers user preferences across sessions, and handles every possible state — loading, success, error, empty — gracefully.

This project is the culmination of the async and state management half of the course. It requires you to combine the Fetch API, `localStorage`, and ES module organization into a deployed, production-ready application.

---

## Scenario

You are building a small public-facing tool for an audience you define. The tool must be genuinely useful for that audience — not just a tech demo. Think about what problem it solves, who it is for, and what they would need to do quickly.

**Examples of appropriate scope:**
- A book finder that searches Open Library and lets users save favorites
- A country explorer that loads country data and lets users filter by region or population
- A weather snapshot for a single location using Open-Meteo
- A NASA photo-of-the-day viewer with a saved history
- A dog breed explorer with a filtered gallery and saved preferences

Choose a public API that does not require payment information for access.

---

## Milestone 1 — Proposal and Data Plan

**Due:** End of Week 10

Submit `projects/project-2/proposal.md` containing:

1. **Problem statement:** Who is this for and what does it help them do?
2. **API:** Which API will you use? Paste the endpoint URL. Paste one example of the raw JSON response (or a relevant excerpt).
3. **Data model:** What does one normalized item look like as a JavaScript object? List each property, its type, and where it comes from in the raw API response.
4. **UI sketch:** A wireframe showing the layout of the loaded state, the loading state, and the error state.
5. **localStorage plan:** What preferences or data will you persist? What is the key name and what does the stored value look like?

---

## Milestone 2 — Build Checkpoint

**Due:** End of Week 11

A deployed, in-progress version with:
- Vite project scaffolded and running (`npm run dev` works)
- At least one successful fetch and render of real API data
- Loading and error states functional (not just placeholder text)
- Module file structure started (at minimum `api.js` and `render.js` exist with their content)

Submit live URL and repo URL. Include a brief note on what is still to be done.

---

## Milestone 3 — Final Submission

**Due:** End of Week 12

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
