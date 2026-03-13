# Week 02 Lecture Notes: Semantic HTML, CSS Architecture, and Mobile-First Layout

## Weekly focus
Writing HTML that means something and CSS that scales — starting from the smallest screen.

## Why this matters
Semantic HTML is the difference between a page that works for everyone and one that only works for sighted mouse users. When you use `<nav>`, `<main>`, and `<article>` instead of nested `<div>` tags, you give browsers, search engines, and assistive technologies the information they need to do their jobs. CSS custom properties and a mobile-first approach are not just best practices — they are how production teams keep stylesheets maintainable across large projects and diverse devices.

## Learning targets
- Identify and correctly apply the HTML5 landmark elements: `header`, `nav`, `main`, `section`, `article`, `aside`, `footer`, `figure`, and `figcaption`
- Declare and use CSS custom properties (design tokens) to centralize color, spacing, and typography values
- Write mobile-first media queries using `min-width` and explain why `min-width` is preferred over `max-width`
- Build a two-column layout using either Flexbox or CSS Grid and collapse it to a single column on small screens
- Verify WCAG AA color contrast using a browser extension or the DevTools color picker

## Core concepts

### Semantic HTML elements and why `<div>` is not enough
A `<div>` is a generic container with no inherent meaning. A screen reader encounters a `<div>` and announces nothing — the user has no idea what region of the page they are in. Semantic elements carry built-in meaning:

```html
<header>
  <nav aria-label="Main navigation">
    <ul>
      <li><a href="/">Home</a></li>
      <li><a href="/about">About</a></li>
    </ul>
  </nav>
</header>

<main>
  <article>
    <h1>Article Title</h1>
    <p>First paragraph of the article.</p>
    <figure>
      <img src="chart.png" alt="Bar chart showing sales increasing 40% in Q3">
      <figcaption>Figure 1: Q3 Sales Growth</figcaption>
    </figure>
  </article>

  <aside>
    <h2>Related Links</h2>
  </aside>
</main>

<footer>
  <p>&copy; 2026 My Site</p>
</footer>
```

Key rules:
- There should be **one `<main>` per page** — it identifies the primary content.
- `<section>` groups thematically related content and should almost always have a heading.
- `<article>` marks content that could stand alone and be syndicated (a blog post, a news story, a product card).
- `<aside>` is supplementary content tangentially related to the surrounding content (sidebars, pull quotes).

### CSS custom properties (design tokens)
Custom properties let you define a value once and reference it everywhere. They are declared on `:root` (the document element) and accessed with `var()`:

```css
:root {
  --color-primary: #1a56db;
  --color-text: #111827;
  --color-bg: #ffffff;
  --space-md: 1rem;
  --space-lg: 2rem;
  --font-body: 'Inter', sans-serif;
}

body {
  color: var(--color-text);
  background-color: var(--color-bg);
  font-family: var(--font-body);
  padding: var(--space-md);
}

a {
  color: var(--color-primary);
}
```

When your client changes the brand color, you update `--color-primary` in one place instead of hunting through hundreds of rules. Custom properties also cascade and inherit, so you can override them inside a component or for a dark-mode media query.

### Mobile-first with `min-width` media queries
Mobile-first means: write your base styles for the narrowest viewport, then add complexity as the viewport grows. The keyword is `min-width`:

```css
/* Base styles — apply to all screen sizes (phones first) */
.card-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: var(--space-md);
}

/* Tablet and up */
@media (min-width: 48rem) {
  .card-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

/* Desktop and up */
@media (min-width: 64rem) {
  .card-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}
```

Why `min-width` over `max-width`? When you write `max-width` queries, you start from a wide desktop layout and progressively shrink it — which tends to produce brittle overrides and forgotten edge cases. `min-width` means you are progressively *enhancing*, which aligns with the principle that base content should work everywhere.

Use `rem` units in media queries (not `px`) so they respect user browser font-size preferences.

### Flexbox fundamentals
Flexbox works on a single axis (row or column). Use it for navigation bars, card rows, centering a single item, and any one-dimensional distribution:

```css
.nav-list {
  display: flex;
  list-style: none;
  gap: 1.5rem;
  padding: 0;
  margin: 0;
}

/* Center a single element both axes */
.hero {
  display: flex;
  justify-content: center;  /* main axis (horizontal in row) */
  align-items: center;      /* cross axis (vertical in row) */
  min-height: 50vh;
}
```

`flex-wrap: wrap` allows flex items to wrap to a new row when they overflow — useful for responsive card layouts without media queries.

### CSS Grid fundamentals
Grid works on two axes simultaneously. Use it for page-level layout and any two-dimensional arrangement:

```css
.page-layout {
  display: grid;
  grid-template-columns: 1fr 3fr;  /* sidebar | main content */
  grid-template-rows: auto 1fr auto;
  min-height: 100vh;
}

/* Named areas make the intent explicit */
.page-layout {
  grid-template-areas:
    "header  header"
    "sidebar main"
    "footer  footer";
}

header  { grid-area: header; }
.sidebar { grid-area: sidebar; }
main    { grid-area: main; }
footer  { grid-area: footer; }
```

### WCAG AA color contrast
WCAG AA requires a **minimum contrast ratio of 4.5:1** for normal text and **3:1** for large text (18pt+). This is not optional for professional work.

Quick checks:
- DevTools: in the Elements panel, click a color swatch next to a `color` property. Chrome shows the contrast ratio in the color picker and marks it with a checkmark or warning.
- Browser extensions: **axe DevTools** or **Colour Contrast Analyser** check the whole page at once.
- Online tool: `webaim.org/resources/contrastchecker/`

A common mistake is designing on a bright monitor and assuming the contrast is fine. Always verify with a tool — do not eyeball it.

## Common mistakes
1. **Wrapping everything in `<section>` or `<div>`.** `<section>` is not a semantic replacement for `<div>` — it implies a distinct, titled region. If the content has no heading, use `<div>`.
2. **Forgetting `alt` text on `<img>` inside `<figure>`.** `<figure>` and `<figcaption>` do not substitute for `alt`. The `alt` attribute on `<img>` is required for screen reader users and for when the image fails to load.
3. **Writing `max-width` media queries when the design brief says "mobile-first."** These work, but they train you to think desktop-first. Force yourself to write base styles for small screens and layer up.
4. **Hardcoding hex colors instead of custom properties.** When colors repeat across a stylesheet without a variable, a brand update becomes a find-and-replace hazard. Define tokens at `:root` from the start.
5. **Using `<b>` and `<i>` for emphasis.** These are presentational. Use `<strong>` for strong importance and `<em>` for stress emphasis. Screen readers adjust their vocal tone for `<strong>` and `<em>`; they ignore `<b>` and `<i>`.

## Accessibility connection
The HTML5 landmark elements — `<header>`, `<nav>`, `<main>`, `<footer>` — expose implicit ARIA landmark roles to the browser's accessibility tree. Screen reader users can navigate directly to any landmark by pressing a shortcut key (e.g., pressing `M` in NVDA jumps to `<main>`). A page built entirely from `<div>` elements forces screen reader users to read linearly through every element to find the content they want. Using semantic elements is therefore a significant navigational aid, not just a stylistic choice.

## Demo walkthrough
**Goal:** Convert a `<div>`-based page layout to semantic HTML, add CSS custom properties, and make it responsive with a single media query.

1. Start with a provided `starter.html` file containing a layout built entirely from `<div class="header">`, `<div class="nav">`, `<div class="main">`, etc.
2. Replace each `<div>` with the appropriate semantic element. Show the before/after in the Elements panel — point out that `<nav>` now appears in the accessibility tree under "landmarks."
3. Open `styles.css`. Add a `:root` block declaring `--color-primary`, `--color-text`, and `--space-md`. Replace hardcoded color values throughout the file with `var()` references.
4. Show the existing layout (likely two columns on all screens). Remove the fixed column widths and replace with:
   ```css
   .content-area { display: grid; grid-template-columns: 1fr; gap: var(--space-md); }
   @media (min-width: 48rem) { .content-area { grid-template-columns: 1fr 3fr; } }
   ```
5. Resize the browser window. Show the layout collapsing to one column below 48rem.
6. Open DevTools, click on the main heading's color swatch. Show the contrast ratio. If it is below 4.5:1, adjust `--color-text` until it passes.

## Practice prompt
Build a single HTML page for a fictional blog post. The page must include: a `<header>` with a site name and `<nav>`, a `<main>` containing one `<article>` with at least two paragraphs and one `<figure>` with `alt` text and a `<figcaption>`, and a `<footer>` with a copyright line. Style it with at least four CSS custom properties defined at `:root`. Add one `min-width` media query that changes the layout in a meaningful way. Verify your heading color passes WCAG AA contrast using DevTools or WebAIM.

## Bridge
Assignment 1 asks you to rebuild a provided design comp as a responsive, semantic HTML/CSS page — you will apply everything in this lecture directly. Pay particular attention to the landmark structure and the mobile-first breakpoint; both are explicitly checked in the rubric. The Chapter 2 reading covers progressive enhancement in more depth, which gives the conceptual grounding behind the mobile-first rule. Read it before starting the assignment so the "why" is clear.
