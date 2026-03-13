# Chapter 8: Design Systems and Small Front-End Architecture

As projects grow, undisciplined code accumulates technical debt: magic numbers, duplicated styles, and 400-line scripts that no one wants to touch. This chapter introduces the naming conventions, file organization, and design decisions that keep a front-end project readable and maintainable.

## What this chapter is really about

A design system is not a luxury for large teams — it is the decision to make choices intentionally and once, rather than accidentally and repeatedly. This chapter shows you how to use CSS custom properties as design tokens, how to name things consistently, and how to organize JavaScript files so that each file has a clear, single responsibility.

## Key ideas

**CSS custom properties** (CSS variables) let you define a value once and reference it everywhere:

```css
:root {
  --color-brand: #2563eb;
  --color-text: #1a1a1a;
  --color-background: #ffffff;
  --space-sm: 0.5rem;
  --space-md: 1rem;
  --space-lg: 2rem;
  --font-size-base: 1rem;
  --border-radius: 0.375rem;
}

.button {
  background-color: var(--color-brand);
  padding: var(--space-sm) var(--space-md);
  border-radius: var(--border-radius);
}
```

Custom properties are **design tokens** — named decisions. Name them for what they *mean*, not what they look like. `--color-brand` is better than `--blue`. `--space-md` is better than `--16px`.

**A simple CSS file organization**:

```
base.css         → reset, typography, :root custom properties
layout.css       → page-level layout (grid, flex containers)
components.css   → reusable UI pieces (card, button, nav)
utilities.css    → single-purpose helper classes (.sr-only, .hidden)
```

Importing in a main CSS file:

```css
@import './base.css';
@import './layout.css';
@import './components.css';
@import './utilities.css';
```

**JavaScript file organization** — each file should have one responsibility:

```
data.js          → constants, raw data, data-fetching functions
state.js         → current application state and state-mutating functions
render.js        → functions that read state and update the DOM
events.js        → event listener setup
utils.js         → pure helper functions (formatting, validation)
main.js          → entry point: imports and initializes everything
```

Write a one-sentence comment at the top of each file stating its purpose. This is documentation you give your future self.

**Naming conventions** — consistent names reduce cognitive load:

- **CSS classes**: lowercase, hyphen-separated: `.nav-bar`, `.product-card`, `.btn-primary`
- **JavaScript variables and functions**: camelCase: `productCard`, `renderNavBar`, `handleSubmit`
- **Constants** (module-level, unchanging): SCREAMING_SNAKE_CASE: `MAX_RESULTS`, `API_BASE_URL`
- **Files**: lowercase, hyphen-separated: `product-card.js`, `nav-bar.css`

**Component thinking in plain JavaScript** — a "component" is a function that produces a piece of UI:

```js
function renderProductCard(product) {
  const card = document.createElement('article');
  card.classList.add('product-card');

  const name = document.createElement('h2');
  name.textContent = product.name;

  const price = document.createElement('p');
  price.textContent = formatPrice(product.price);

  card.append(name, price);
  return card;
}
```

Call `renderProductCard(product)` wherever you need a card. This is reusable, testable, and readable.

## Mental model

A design system is a set of decisions made once and referenced everywhere. Instead of choosing `#2563eb` in 12 places, you define `--color-brand` once and reference it everywhere. When the brand color changes, you change one line.

Architecture is about **where things live** and **who is responsible for what**. When you open a file named `render.js`, you should find rendering code. When you open `events.js`, you should find event listeners. A project where every file might contain anything is a project where you spend all your time searching.

## Working habits

- Define all colors, font sizes, and spacing values as custom properties in `:root`. Never use magic numbers in CSS.
- Name custom properties semantically (what they mean, not what they look like).
- Start each JavaScript file with a one-sentence comment: `// Handles all DOM rendering for the product list.`
- Keep rendering functions pure: they receive data and return (or append) DOM elements. They do not fetch data. They do not set global state.
- Store class name strings as constants if used in more than one place:

```js
const HIDDEN_CLASS = 'hidden';
const ACTIVE_CLASS = 'active';
```

## Common mistakes

- **Magic numbers in CSS**: `padding: 13px` with no explanation. Where did 13 come from? Will it be consistent with other spacing? Use a custom property.
- **One massive JavaScript file**: a 600-line `app.js` that mixes data fetching, DOM manipulation, validation, and event handling. Split by responsibility.
- **Inconsistent naming**: some classes use camelCase, some use hyphen-separated, some use underscores. Pick one convention and stick to it.
- **Putting class names in many places**: if you rename a CSS class, you have to find every place it appears in JavaScript. Store class names as constants at the top.
- **Mixing rendering and fetching**: a function called `renderProducts` should not also fetch data. Separate those concerns.

## Accessibility and UX note

Design decisions have direct accessibility consequences:

- **Color contrast**: choose custom property values that meet WCAG contrast ratios (4.5:1 for normal text). Verify with a tool like WebAIM's Contrast Checker. A beautiful brand color fails if it cannot be read.
- **Spacing and touch targets**: interactive elements should be at least 44×44px touch target size. Use your spacing tokens to ensure consistent sizing.
- **Consistent design** builds user trust and reduces cognitive load for all users, including those with cognitive disabilities. A page that looks intentional is easier to navigate than one that feels random.

## Performance fundamentals

Good architecture does not just make code readable — it directly affects how fast a page loads and how quickly users see content. You do not need to be a performance expert, but you should understand the most common bottlenecks and how to identify them.

**What makes a page slow?**

The browser renders a page in a sequence of steps: download HTML → parse HTML → download CSS and JavaScript (possibly blocking) → render the page → run JavaScript → paint pixels. Each step can stall the one after it.

The three most common culprits:

1. **Render-blocking scripts:** A `<script src="app.js">` in `<head>` without `defer` or `async` pauses HTML parsing until the script downloads and runs. Add `defer` (or move scripts to the end of `<body>`) so HTML parsing continues unblocked.

   ```html
   <!-- Blocks rendering -->
   <script src="app.js"></script>

   <!-- Doesn't block — browser downloads script in parallel -->
   <script defer src="app.js"></script>
   ```

2. **Large JavaScript bundles:** Sending 1 MB of JavaScript to the browser is slow even on fast connections. Build tools like Vite automatically split code into smaller chunks (**tree-shaking** removes code you never use; **code splitting** breaks a large bundle into smaller files loaded on demand).

3. **Unoptimized images:** Images are usually the heaviest assets on a page. Use modern formats (WebP, AVIF), set explicit `width` and `height` attributes to prevent layout shifts, and use `loading="lazy"` on images below the fold.

**How to measure: Lighthouse**

Lighthouse is built into Chrome DevTools (DevTools → Lighthouse tab). Run it on any page to get scores in five categories:

| Category | What it measures |
|---|---|
| **Performance** | How fast the page loads and becomes interactive (FCP, LCP, TBT, CLS) |
| **Accessibility** | Whether the page meets WCAG guidelines |
| **Best Practices** | Security and code quality signals |
| **SEO** | Search engine crawlability |
| **PWA** | Progressive Web App compliance |

Each finding includes a description of the problem and a link to documentation explaining how to fix it. You will run a full Lighthouse audit in Lab 13 (Week 14) and on every project before final submission.

**Quick performance checklist for this course:**

- [ ] All `<script>` tags in `<head>` use `defer`
- [ ] Images have explicit `width` and `height` attributes
- [ ] Images below the fold use `loading="lazy"`
- [ ] No unused CSS or JavaScript imported
- [ ] Vite build (`npm run build`) runs without warnings

---

## Practice prompt

Refactor the CSS from one of your previous labs:

1. Extract every color, spacing, and font-size value into CSS custom properties in `:root`. Name them semantically.
2. Organize your CSS into at least two separate files (e.g., `base.css` and `components.css`) and import them.
3. Refactor your JavaScript into at least two files: one for data/utilities and one for rendering/DOM operations. Add a one-sentence comment at the top of each.
4. Write a `renderCard(item)` function that accepts an object and returns a DOM element. Use it in a loop to render a list of items.

Check your brand color's contrast ratio against its background using a contrast checker tool.

## Reflection

What felt redundant in your CSS before you moved to custom properties? When you split your JavaScript into files, what dependencies did you find — which file needed to know about which other file? What changed about how you read and modified the code?

## Vocabulary

- **design system** — a set of reusable design decisions (colors, spacing, typography) defined once and referenced consistently
- **design token** — a named design decision stored as a CSS custom property or variable
- **CSS custom property** — a user-defined CSS variable declared with `--name` and accessed with `var(--name)`
- **component** — a self-contained, reusable piece of UI with its own markup, styles, and behavior
- **naming convention** — an agreed-upon pattern for naming files, classes, and variables
- **separation of concerns** — organizing code so each piece is responsible for one distinct thing
- **architecture** — the structure of files, modules, and their relationships
- **magic number** — a literal value in code that has no obvious meaning or origin

## Mini checklist

- I can define design tokens as CSS custom properties in `:root` and reference them with `var()`.
- I can name custom properties semantically (what they mean, not their visual value).
- I can organize CSS into multiple files with clear responsibilities.
- I can split JavaScript into files by responsibility, with a one-sentence comment at the top of each.
- I can write a rendering function that accepts data and returns a DOM element.
- I can check color contrast and verify it meets WCAG minimum ratios.
