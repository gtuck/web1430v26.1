# Project 1 – Interactive Style Guide

**Due:** End of Week 8 (three milestones across Weeks 6–8)
**Weight:** Part of Projects (30% of course grade)
**Skills:** CSS custom properties, design tokens, semantic HTML, DOM manipulation, accessible interactive patterns, file organization

---

## Overview

A style guide is the source of truth for a design system: it defines the visual language (colors, typography, spacing) and documents the interactive patterns (buttons, cards, navigation, accordions, tabs) that a project will use consistently. You will build a **living style guide** — a deployed web page that both documents and demonstrates every element of your design system.

This project brings together everything from the first half of the course: semantic HTML, mobile-first CSS, JavaScript-driven interaction, and accessibility. It is larger in scope than any individual lab or assignment, and requires planning before building.

---

## Scenario

You have been hired to build the front-end foundation for a fictional product, organization, or publication of your choice. Before any feature work begins, the team needs a shared visual language and a set of reusable, tested UI components. Your deliverable is a style guide page that a developer could open and immediately understand what CSS variables are available, what each component looks like, and how each interactive pattern behaves.

---

## Milestone 1 — Proposal

**Due:** End of Week 6

Submit a `proposal.md` file in `projects/project-1/` containing:

1. **Project context:** What is the fictional product or organization? Who is the audience?
2. **Color palette:** At minimum four named colors (brand, text, background, accent). Include hex values and confirm contrast ratios using WebAIM Contrast Checker.
3. **Typography plan:** Font family choices (Google Fonts or system fonts), scale (at minimum body, small, large, heading sizes in rem).
4. **Component list:** The five components you will document (from the required list below).
5. **Rough sketch:** A hand-drawn or digital wireframe showing how the style guide page will be organized.

Proposal does not need to be code — it is a planning document.

---

## Milestone 2 — Build Checkpoint

**Due:** End of Week 7

A deployed, in-progress version with:
- All CSS custom properties defined in `:root`
- The typography section and color swatch section complete
- At least two interactive components functional (even if not polished)
- `node_modules/` and `dist/` absent from the repo

Submit the live URL and repo URL to Canvas with a brief note on what is remaining.

---

## Milestone 3 — Final Submission

**Due:** End of Week 8

---

## Required sections

Your style guide page must include all of the following sections, each with an `<h2>` heading and an anchor in the page navigation.

### 1. Design tokens

A visual reference of every CSS custom property defined in `:root`:
- **Colors:** Each color displayed as a swatch (a `<div>` with `background-color` set to the variable) with its variable name and hex value labeled
- **Spacing:** Each spacing token shown as a colored bar whose width or height equals the token value, labeled with the variable name and computed value
- **Typography:** Each font-size token shown as sample text at that size

### 2. Typography

Live examples of:
- All heading levels (`<h1>` through `<h4>`) using your type scale
- Body text paragraph with proper line height and measure (45–75 characters per line)
- A `<blockquote>` with attribution
- An `<ol>` and a `<ul>` in body context
- `<code>` inline and a `<pre><code>` block

### 3. Buttons

At minimum four button variants, each shown in default, hover, focus, and disabled states:
- Primary button
- Secondary button
- Destructive/danger button
- Icon button (button with an icon and a visible or visually-hidden label)

All buttons must be `<button>` elements. Hover and focus states must be visible. Disabled buttons must use the `disabled` attribute (not just a class).

### 4. Cards

A reusable card component shown in at minimum two configurations:
- A basic card (image, title, body text, action)
- A horizontal card (image beside text)

Cards must be built with `createElement` in a `renderCard(data)` function. Demonstrate rendering at least three cards from a hardcoded data array.

### 5. Navigation

A responsive `<nav>` with:
- A logo/brand link
- At least four nav links
- A mobile-friendly state: at narrow viewport, links collapse (can be CSS-only or JavaScript-toggled)
- If JavaScript-toggled: `aria-expanded` on the toggle button, keyboard-accessible open/close

### 6. Interactive patterns (choose two of three)

**Option A – Accordion**
At least four items. One-open-at-a-time behavior. `aria-expanded` and `aria-controls` on triggers.

**Option B – Tabs**
At least three tabs. Correct ARIA roles (`tablist`, `tab`, `tabpanel`). Arrow key navigation between tabs.

**Option C – Modal/Dialog**
A trigger button that opens a dialog overlay. Focus trapped inside the modal while open. Closed by Escape key, a close button, or clicking the backdrop. `role="dialog"` and `aria-labelledby` referencing the dialog title.

---

## Technical requirements

- All design values as CSS custom properties in `:root` — no magic numbers anywhere in the CSS
- CSS organized into at minimum: `base.css` (reset + tokens), `components.css`, imported into a main stylesheet
- JavaScript organized into at minimum two files: one for rendering utilities, one for interactive pattern initialization
- Each JS file has a one-sentence comment at the top stating its responsibility
- No CSS frameworks; no JS UI libraries
- HTML validates with no errors at validator.w3.org
- Deployed and accessible at a live URL

---

## Accessibility requirements

- Every interactive element keyboard-reachable and operable
- All ARIA attributes used correctly (no `aria-label` on elements that already have visible text)
- Color contrast meets WCAG AA for all text/background combinations
- Focus visible on all interactive elements (`:focus-visible` style defined)
- Images (if any) have descriptive `alt` text

---

## Above baseline (stretch)

- A CSS-only dark mode via `@media (prefers-color-scheme: dark)` that swaps custom property values
- A "copy to clipboard" button next to each CSS custom property name
- A `print.css` stylesheet that removes interactive elements and renders only the design token reference

---

## Deliverable

`projects/project-1/` in your repository containing:
- `index.html`
- `css/` folder with organized stylesheets
- `js/` folder with organized scripts
- `proposal.md`
- `rationale.md`

Deploy to GitHub Pages, Netlify, or Vercel.

**Submit to Canvas (Milestone 3):** Live URL, repo URL, rationale link.

---

## Rationale (rationale.md)

Write 6–8 sentences addressing:
- What organization or product did you design for, and what drove your color and typography choices?
- How did you decide what counts as a "component" vs. a one-off element?
- What was the hardest interactive pattern to implement accessibly and what did you learn?
- What would a developer need to know to use your style guide on a real project?

---

## Rubric

| Criterion | Excellent (4) | Proficient (3) | Developing (2) | Incomplete (1) |
|-----------|--------------|----------------|----------------|----------------|
| **Design tokens** | All colors, spacing, and type tokens defined as custom properties; swatch/bar visualizations present and labeled; no magic numbers in CSS | Most tokens defined; visualizations present; 1–2 magic numbers | Tokens partially defined; no visualization | No custom properties |
| **Component completeness** | All six sections present and functional; cards rendered from data array; buttons show all four states | Five sections present; cards hardcoded; three button states | Four sections present; significant gaps | Three or fewer sections |
| **Interactive patterns** | Both chosen patterns functional, keyboard-accessible, and ARIA-correct | Both functional; one ARIA attribute missing | One pattern functional | Neither pattern functional |
| **Code organization** | CSS in separate files by responsibility; JS in separate files with responsibility comments; no mixed concerns | Two files each; minor mixing | One CSS file; one JS file | Single monolithic file |
| **Accessibility** | All interactive elements keyboard-operable; contrast passes; ARIA used correctly; focus visible | Three of four criteria | Two criteria | One or none |
| **Proposal and rationale** | Proposal submitted on time with all five elements; rationale addresses all four prompts specifically | Proposal complete; rationale addresses three prompts | Proposal partially complete; rationale vague | Proposal missing or rationale missing |
