# Assignment 1 – Responsive Content Page

**Due:** End of Week 2
**Weight:** One of six assignments (20% combined)
**Skills:** Semantic HTML, mobile-first CSS, CSS layout, accessibility fundamentals

---

## Overview

You will build a multi-section content page for a fictional organization of your choice — a campus club, a local nonprofit, a small business, or a community event. The page must be meaningful, well-structured, and fully responsive without any JavaScript.

This assignment is intentionally HTML and CSS only. JavaScript is introduced in Week 3. Any submitted JavaScript will be ignored in grading.

---

## Scenario

You have been asked to build the public-facing landing page for your chosen organization. The page needs to work on any screen size (a visitor might view it on a phone, tablet, or desktop monitor) and must be readable and navigable without a mouse.

---

## What to build

A single HTML page with all of the following:

### Required sections
- A `<header>` with the organization name and a `<nav>` containing at least three anchor links
- A `<main>` with at least **three** `<section>` or `<article>` elements, each with a heading
- A `<footer>` with contact information or copyright notice

### Required HTML elements
- At least one `<figure>` with `<figcaption>` (image or illustration with a caption)
- At least one `<ul>` or `<ol>` used for genuinely list-like content
- At least one `<form>` with two or more fields (e.g., a contact or newsletter sign-up form) — the form does not need to submit anywhere, but labels must be properly connected to inputs

### Required CSS
- All colors, spacing, and font sizes defined as **CSS custom properties** in `:root`
- **Mobile-first** layout: base styles work at 375px; at least one `min-width` media query adds layout for wider viewports
- At least one use of **Flexbox or CSS Grid** for layout
- No `!important`; no inline `style` attributes

### Accessibility requirements
- `lang` attribute on `<html>`
- Every `<img>` has a descriptive `alt` attribute (or `alt=""` if decorative)
- Color contrast: all text must pass WCAG AA (4.5:1 for normal text, 3:1 for large text)
- Form labels connected to inputs with matching `for` / `id` pairs
- Heading hierarchy is logical (`<h1>` once, headings do not skip levels)

---

## Constraints

- No JavaScript of any kind
- No CSS frameworks (Bootstrap, Tailwind, etc.) — write your own CSS
- No `<table>` for layout purposes
- Validate your HTML at **validator.w3.org** and fix all errors before submitting

---

## Above baseline (stretch)

To demonstrate work beyond minimum requirements, consider:
- A skip-navigation link (`<a href="#main-content">Skip to main content</a>`) before the header
- A `:focus-visible` style that makes keyboard focus clearly visible
- A CSS-only dark/light mode using `@media (prefers-color-scheme: dark)`
- Print styles via `@media print`

These are not required for full marks, but the rubric's Excellent column reflects this level of care.

---

## Deliverable

In your course GitHub repository, create `assignments/assignment-1/`:
- `index.html`
- `style.css` (or organized into multiple CSS files imported from `style.css`)
- `rationale.md`

Deploy to GitHub Pages, Netlify, or Vercel.

**Submit to Canvas:**
- Live URL
- GitHub repository URL (direct link to `assignments/assignment-1/`)
- Link to `rationale.md`

---

## Rationale (in rationale.md)

Write 4–6 sentences addressing:
- Who is the intended audience for this page?
- What element-choice decisions did you make and why (e.g., why `<article>` instead of `<section>` somewhere)?
- What was the most challenging CSS decision and how did you resolve it?
- What would you improve if you had more time?

---

## Rubric

| Criterion | Excellent (4) | Proficient (3) | Developing (2) | Incomplete (1) |
|-----------|--------------|----------------|----------------|----------------|
| **Semantic HTML** | All required elements present; element choices reflect meaning, not appearance; no presentational markup | Most required elements present; minor misuse (e.g., one `<div>` where semantic element would work) | Some required elements present; several semantic errors | Missing major elements; heavy `<div>` use throughout |
| **Mobile-first CSS** | Base styles correct at 375px; `min-width` query adds meaningful layout; custom properties used for all design values | Responsive at most sizes; custom properties used; minor mobile issue | Some responsiveness; few custom properties; starts desktop-first | Not responsive; no custom properties |
| **Layout technique** | Flexbox or Grid used correctly for at least one layout; layout does not break at intermediate sizes | Flexbox or Grid used; minor layout issue at some size | Layout technique attempted but inconsistent | No Flexbox or Grid |
| **Accessibility** | `lang`, `alt`, contrast, label/id pairs, heading hierarchy all correct; HTML validates with no errors | Three of five criteria met; validator shows minor warnings | Two criteria met; some validation errors | One criterion met; significant accessibility issues |
| **Rationale** | Specific, honest, addresses all four prompts; demonstrates design thinking | Addresses three prompts; some specificity | Addresses two prompts; vague | Missing or one sentence |
