# Assignment 3 – DOM Pattern Library

**Due:** End of Week 8 (Midterm Week)
**Weight:** One of six assignments (20% combined)
**Skills:** DOM selection, class toggling, event delegation, createElement, accessible interactive patterns

---

## Overview

You will build a small **in-browser pattern library** — a single page that demonstrates three reusable UI patterns, each implemented correctly in vanilla JavaScript with accessible markup. The page serves as both a working demo and a reference document: a developer (or your future self) should be able to open it, see each pattern in action, and understand how it was built.

---

## Scenario

Imagine you are a front-end developer joining a small team. Before starting a new project, you are asked to build a living reference of three interaction patterns the team will use across the site. Each pattern should be isolated (no pattern depends on another), documented inline, and keyboard-accessible.

---

## Patterns to implement

You must implement all three of the following patterns. Each pattern must be built independently (no shared state between them).

### Pattern 1: Accordion / FAQ

An accordion with at least **four** question-answer pairs. Rules:
- Only one answer can be open at a time (opening a new one closes the previous)
- Each trigger is a `<button>` inside an `<h3>` (or `<h2>`) — not a bare `<div>`
- `aria-expanded="true"/"false"` on the trigger button reflects open/closed state
- `aria-controls` on the button points to the answer panel's `id`
- The answer panel has `id` matching the `aria-controls` value

### Pattern 2: Tabbed interface

A tab component with at least **three** tabs. Rules:
- Tabs use correct ARIA roles: `role="tablist"` on the container, `role="tab"` on each button, `role="tabpanel"` on each panel
- `aria-selected="true"` on the active tab, `aria-selected="false"` on inactive tabs
- Each tab has `aria-controls` pointing to its panel's `id`; each panel has `aria-labelledby` pointing to its tab's `id`
- Arrow key navigation: Left/Right arrow keys move focus between tabs (keyboard users should not have to Tab through every tab to reach the content)
- The active tab is visually distinct from inactive tabs

### Pattern 3: Live filter

A list of at least **eight** items (cards, names, products — your choice) with a text input that filters visible items as the user types. Rules:
- Filtering updates the DOM without a full re-render (use CSS class `hidden` + `classList.toggle`)
- A count element below the input reads "Showing X of Y items" and updates on every keystroke
- The count element has `aria-live="polite"`
- Empty state: if no items match, display a "No results" message
- Input is labelled with a `<label>` (not just a placeholder)

---

## Page structure

The library page itself should have:
- A clear `<h1>` title
- A `<nav>` with anchor links to each of the three pattern sections
- Each pattern in its own `<section>` with an `<h2>` heading
- A brief (1–2 sentence) description of each pattern above its demo

---

## JavaScript requirements

- All three patterns in a single `patterns.js` file (or split into three files)
- Each pattern implemented as a named initialization function: `initAccordion()`, `initTabs()`, `initFilter()`
- All three called at the bottom of the file (or in `DOMContentLoaded`)
- No `innerHTML` for dynamic content — use `classList` for show/hide, `textContent` for count updates
- Event delegation where appropriate (accordion and filter)
- No `onclick` HTML attributes

---

## Constraints

- No JavaScript UI libraries (no jQuery, no Alpine.js)
- No CSS frameworks
- All three patterns must work with keyboard only (Tab, Enter, Space, arrow keys as appropriate)
- Validate HTML; fix all errors

---

## Above baseline (stretch)

Work in this section is reflected in the Excellent (4) column of the rubric.

- The accordion supports keyboard navigation: Down/Up arrow keys move focus between triggers
- The filter input debounces keystrokes (waits 150ms after the last keystroke before filtering, using `setTimeout`)
- Each pattern section includes a collapsed `<details>` element showing the relevant HTML snippet for that pattern

---

## Deliverable

In your course repository, create `assignments/assignment-3/`:
- `index.html`
- `patterns.js`
- `style.css`
- `rationale.md`

Deploy and submit live URL, repo URL, and rationale link to Canvas.

---

## Rationale (in rationale.md)

Write 4–6 sentences addressing:
- What was the most technically challenging of the three patterns and why?
- How did you implement keyboard accessibility for the tab component — what did you have to learn that wasn't obvious?
- Where did you use event delegation and why was it the right choice there?
- What would you refactor if you were extending this into a real project component library?

---

## Rubric

| Criterion | Excellent (4) | Proficient (3) | Developing (2) | Incomplete (1) |
|-----------|--------------|----------------|----------------|----------------|
| **Accordion** | One-open-at-a-time behavior; `aria-expanded` and `aria-controls` correct; trigger is `<button>` in heading | Functional; one ARIA attribute missing or incorrect | Functional; no ARIA | Non-functional |
| **Tabs** | Correct ARIA roles; `aria-selected` updates; arrow key navigation works; panels show/hide | Correct roles and selection; no arrow key nav | Functional tabs; no ARIA | Non-functional |
| **Live filter** | Filters on input; count updates; empty state shown; `aria-live` present; proper label | Filters and counts; missing empty state or `aria-live` | Filters; no count or accessibility | Non-functional |
| **Code structure** | Named init functions; no `innerHTML` for dynamic content; event delegation where appropriate | Named functions; one `innerHTML` for static content | Partial structure; mixed concerns | All logic inline or anonymous |
| **Keyboard accessibility** | All three patterns keyboard-operable; visible focus styles present | Two patterns keyboard-operable | One pattern keyboard-operable | No keyboard support |
| **Rationale** | Specific, honest, addresses all four prompts | Addresses three prompts | Vague or two prompts | Missing |
