# Assignment 4 – API Data Story

**Due:** End of Week 10
**Weight:** One of six assignments (20% combined)
**Skills:** Fetch API, async/await, error handling, loading states, data normalization, DOM rendering from remote data

---

## Overview

You will choose a public JSON API, pull real data into a browser interface, and present that data as a coherent, interactive **data story** — a page that gives users a way to explore the dataset and understand something meaningful from it. The page must handle three async states (loading, success, error) and be accessible to screen reader users.

---

## Scenario

You are building a public-facing data explorer. Your audience may not know the underlying API or data format — they just want to find and understand relevant information quickly. Your job is to make the data clear, interactive, and resilient: it should work gracefully whether the API responds in 200ms or fails entirely.

---

## Choose an API

Select **one** public API that:
- Returns JSON
- Does not require authentication (or has free-tier key access that does not require payment)
- Has consistent enough data that you can normalize it reliably

**Suggested options** (no API key required):
- Open Library Search API — `https://openlibrary.org/search.json`
- JSONPlaceholder — `https://jsonplaceholder.typicode.com`
- REST Countries — `https://restcountries.com/v3.1`
- The Dog API — `https://dog.ceo/api`
- Open-Meteo (weather) — `https://open-meteo.com`
- NASA APOD — `https://api.nasa.gov` (free key)

If you use a different API, confirm it supports browser cross-origin requests (no CORS block) before committing to it.

---

## What to build

### Required features

**1. Initial load view**
When the page opens, automatically fetch a meaningful starting dataset and render it. Do not require the user to take an action before seeing any data.

**2. Search or filter control**
A form input (search field, dropdown, or set of filter buttons) that lets users narrow, sort, or explore the dataset. This control must trigger a new fetch or filter the already-loaded data — at minimum one of the two.

**3. Detail view** (one of the following)
- Clicking a result card reveals additional details about that item (expand in place, or render to a dedicated panel)
- A second fetch triggered by clicking an item retrieves and displays additional data for that specific item

**4. Three async UI states**
Every fetch must handle all three:
- **Loading** — a visible loading indicator while the request is in flight
- **Success** — the data rendered
- **Error** — a visible, descriptive error message (not just a console log)

### Required JavaScript structure

In a file named `app.js` (or organized into modules if you prefer):

```
fetchData(query)        — async, checks response.ok, throws on failure
normalizeData(rawDocs)  — transforms raw API fields into clean, consistent objects
showLoading()           — clears the results region, shows loading message
showError(message)      — clears the results region, shows error
showEmpty()             — clears the results region, shows "no results" message
renderResults(items)    — renders an array of normalized objects to the DOM
```

The normalization function must provide default values for any API fields that may be absent (e.g., `author: doc.author_name?.[0] ?? 'Unknown'`).

### Accessibility requirements
- Results container has `aria-live="polite"` so screen readers announce updates
- Loading, error, and empty messages are text-based (not spinner-only)
- Each result card uses a semantic element (`<article>` or `<li>`)
- If the detail view changes what is visible, move keyboard focus to the new content

---

## Error handling requirements

Your `try/catch` must handle:
- Network failure (tested by disabling Wi-Fi before submitting)
- HTTP error status (test by temporarily using a bad URL — verify `response.ok` check fires)
- Empty results (test with a query that returns zero results)

Each error condition must produce a different, human-readable message in the UI.

---

## Constraints

- No front-end frameworks (Vue, React, etc.) — vanilla JavaScript only
- No jQuery
- No CSS frameworks
- `innerHTML` may be used only for static structural markup you fully control — never for any value derived from API data
- Validate HTML; fix all errors

---

## Above baseline (stretch)

- Cache the most recent successful result in `sessionStorage` and restore it on page reload so users don't see a blank page on refresh
- Add pagination or a "load more" button that fetches the next page of results
- Implement an `AbortController` to cancel in-flight requests when a new search is submitted before the previous one completes

---

## Deliverable

In your course repository, create `assignments/assignment-4/`:
- `index.html`
- `app.js`
- `style.css`
- `rationale.md`

Deploy and submit live URL, repo URL, and rationale link to Canvas.

---

## Rationale (in rationale.md)

Write 4–6 sentences addressing:
- What API did you choose and what data story does your page tell?
- How does your normalization function protect your rendering code from inconsistent API responses?
- Walk through one error path: what happens in the UI when the request fails?
- What would you add or change if you were building this for a real audience?

---

## Rubric

| Criterion | Excellent (4) | Proficient (3) | Developing (2) | Incomplete (1) |
|-----------|--------------|----------------|----------------|----------------|
| **Async handling** | `response.ok` checked; `try/catch/finally` used; all three states (loading, success, error) produce distinct, appropriate UI | Two states handled; `response.ok` checked | One state handled; no `response.ok` check | No error handling |
| **Data normalization** | Normalization function covers all rendered fields; default values for missing data; rendering code uses only normalized objects | Two of three fields normalized; some raw API fields in renderer | No normalization; raw API data passed directly to renderer | |
| **Search / filter** | User control triggers data update; empty results handled | Control works; empty results not handled | Control partially functional | No interactive control |
| **Accessible async** | `aria-live` on results region; loading/error messages are text-based and descriptive; focus managed on detail view | `aria-live` present; text messages present; focus not managed | Partially accessible | No accessible state management |
| **Code structure** | Named functions for fetch, normalize, and each UI state; no `innerHTML` with API data | Named functions; one minor `innerHTML` issue | Partial function separation | All logic inline |
| **Rationale** | Specific, honest, addresses all four prompts | Addresses three prompts | Vague or two prompts | Missing |
