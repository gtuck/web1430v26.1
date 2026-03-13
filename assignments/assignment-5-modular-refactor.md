# Assignment 5 – Modular Refactor

**Due:** End of Week 12
**Weight:** One of six assignments (20% combined)
**Skills:** ES modules, named exports/imports, Vite dev server and build, file organization by responsibility, dependency direction

---

## Overview

You will take a working single-file JavaScript application — either your Assignment 4 submission or the provided starter script — and refactor it into a proper **Vite-based module project** with clearly separated files, explicit imports and exports, and a deployable production build.

The goal is not to add features. The goal is to demonstrate that you understand how to organize code so that each file has a single, clear responsibility and every dependency is explicit.

---

## Starting point

Choose one:

**Option A:** Use your Assignment 4 (`app.js`) as the source. It must be functional before you refactor it.

**Option B:** Use the provided starter script below. Copy it into a new file and use it as your source.

```js
// starter.js — a single-file book search app
// Refactor this into a Vite module project

const API_BASE = 'https://openlibrary.org/search.json';
const resultsEl = document.getElementById('results');
const form = document.getElementById('search-form');
const input = document.getElementById('search-input');

form.addEventListener('submit', async (e) => {
  e.preventDefault();
  const q = input.value.trim();
  if (!q) { resultsEl.textContent = 'Enter a search term.'; return; }
  resultsEl.textContent = 'Loading…';
  try {
    const res = await fetch(`${API_BASE}?title=${encodeURIComponent(q)}&limit=10`);
    if (!res.ok) throw new Error(res.status);
    const data = await res.json();
    resultsEl.innerHTML = '';
    if (!data.docs.length) { resultsEl.textContent = 'No results.'; return; }
    data.docs.forEach(doc => {
      const el = document.createElement('article');
      el.textContent = `${doc.title} — ${doc.author_name?.[0] ?? 'Unknown'} (${doc.first_publish_year ?? '?'})`;
      resultsEl.append(el);
    });
  } catch (err) {
    resultsEl.textContent = 'Error: ' + err.message;
    console.error(err);
  }
});
```

---

## Required output structure

Your refactored project must follow this file layout exactly:

```
assignments/assignment-5/
  index.html
  package.json
  vite.config.js (optional — only if needed)
  .gitignore          ← must include node_modules/ and dist/
  src/
    main.js           ← entry point: imports and initializes everything
    api.js            ← fetch functions only
    normalize.js      ← data transformation functions
    render.js         ← DOM rendering functions
    events.js         ← event listener setup
    utils.js          ← pure helper functions (formatting, validation)
```

Files that have no content for your specific app may be omitted, but at minimum you must have `main.js`, `api.js`, `render.js`, and `events.js` with appropriate content.

---

## Module requirements

### `api.js`
- Named export: `fetchBooks(query)` (or equivalent for your API)
- Checks `response.ok`; throws a descriptive error if false
- No DOM access — no `document.getElementById`, no `querySelector`

### `normalize.js`
- Named export: `normalizeBooks(docs)` (or equivalent)
- Pure function: input in, output out, no side effects
- Provides defaults for all fields that may be absent

### `render.js`
- Named exports: `showLoading()`, `showError(msg)`, `showEmpty()`, `renderResults(items)`
- Each function receives data as an argument — no direct API calls
- DOM element references selected **inside** this file (not passed in from outside)

### `events.js`
- Named export: `initSearch()` (or equivalent)
- Attaches event listeners
- Calls functions from `api.js`, `normalize.js`, and `render.js` — no business logic of its own

### `main.js`
- Imports `initSearch` from `events.js` and calls it
- Entry point only — no logic besides initialization

---

## Vite workflow requirements

- Scaffold with `npm create vite@latest` (Vanilla JavaScript template)
- App runs correctly with `npm run dev`
- `npm run build` completes without errors
- `dist/` folder is **not** committed (verify with `.gitignore`)
- `node_modules/` is **not** committed

---

## Verification checklist

Before submitting, confirm:
- [ ] Running `npm install && npm run dev` from `assignments/assignment-5/` opens the app in the browser
- [ ] `npm run build` produces a `dist/` folder
- [ ] `dist/` and `node_modules/` are absent from your git commit
- [ ] Each `src/` file has a one-sentence comment at the top stating its responsibility
- [ ] No file imports from a file it should not depend on (e.g., `render.js` does not import from `events.js`)

---

## Constraints

- No TypeScript
- No Vue or other frameworks
- The refactored app must be functionally equivalent to the original — same behavior, reorganized code

---

## Above baseline (stretch)

- Add a `constants.js` file that exports `API_BASE_URL` and any other magic strings, and import them wherever needed
- Use `import.meta.env` to demonstrate environment-aware configuration (e.g., a different limit in development vs production)
- Write a brief `ARCHITECTURE.md` inside `assignments/assignment-5/` that diagrams which files import from which (a simple text diagram is fine)

---

## Deliverable

In your course repository: `assignments/assignment-5/` containing the full Vite project source (without `node_modules/` or `dist/`).

Deploy the `dist/` output to Netlify or GitHub Pages (Netlify drag-and-drop for the `dist/` folder works well).

Submit to Canvas: live URL, repo URL (link to `assignments/assignment-5/`), and rationale link.

---

## Rationale (in rationale.md)

Write 4–6 sentences addressing:
- What was the single hardest dependency to untangle when splitting the monolithic file?
- How did you decide which functions belonged in `api.js` vs `render.js` vs `utils.js`?
- What did the `dist/` folder contain that your `src/` folder does not, and what does that tell you about what Vite did?
- What would you organize differently if this project were going to grow to ten files?

---

## Rubric

| Criterion | Excellent (4) | Proficient (3) | Developing (2) | Incomplete (1) |
|-----------|--------------|----------------|----------------|----------------|
| **Module structure** | All four required files present with correct responsibilities; one-sentence comment at top of each | Three files with correct responsibilities | Two files; responsibilities mixed | Single file; no modules |
| **Export / import correctness** | All exports named; all imports explicit with correct relative paths; no accidental globals | Minor import issue (missing `.js` extension, incorrect path) | Imports partially working | Module syntax errors prevent running |
| **Dependency direction** | `api.js` and `normalize.js` have no DOM access; `render.js` does not call fetch; `main.js` only initializes | One minor violation | Two violations | No separation of concerns |
| **Vite workflow** | `npm run dev` works; `npm run build` succeeds; `node_modules/` and `dist/` in `.gitignore` | Dev works; build works; one gitignore omission | Dev works; build not attempted | `npm run dev` fails |
| **Functional equivalence** | Refactored app behaves identically to original; no features lost | One feature regressed | Significant functionality missing | App non-functional |
| **Rationale** | Specific, honest, addresses all four prompts | Addresses three prompts | Vague or two prompts | Missing |
