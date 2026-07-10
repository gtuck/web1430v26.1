# Lab 08 – Build an API-Powered Viewer

## Purpose

Client-side applications rarely work with hardcoded data. This lab connects your JavaScript to a real public API, handles the asynchronous lifecycle of a network request, and manages the three states every async interface must communicate: loading, success, and error.

## Skills practiced

- Writing `async` functions and using `await`
- Checking `response.ok` before parsing JSON
- Wrapping fetch in `try/catch` with a `finally` block
- Displaying loading, success, and error states in the UI
- Using `aria-live` for accessible async updates
- Building a search or filter interface on top of remote data

## What you're building

An **Open Library Book Search** — a browser tool that lets users search for books by title using the Open Library Search API. Results display as cards showing the book title, author, and publication year. A loading message appears during the request, an error message appears if the request fails, and an empty state message appears when no results are found.

**API endpoint:** `https://openlibrary.org/search.json?title=[query]&limit=12`

No API key required. The API is free and publicly accessible from the browser.

---

## Part 1: HTML structure

Create `labs/lab08/index.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Book Search</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <main>
    <h1>Open Library Book Search</h1>

    <form id="search-form">
      <label for="search-input">Search by title</label>
      <input type="search" id="search-input" placeholder="e.g. Dune" autocomplete="off">
      <button type="submit">Search</button>
    </form>

    <div id="results-region" aria-live="polite" aria-label="Search results">
      <!-- Status messages and results are injected here -->
    </div>
  </main>
  <script src="lab08.js" defer></script>
</body>
</html>
```

Key: the `aria-live="polite"` attribute on `#results-region` means screen readers will announce its content when it changes.

---

## Part 2: API and data functions

In `labs/lab08/lab08.js`:

### `fetchBooks(query)`

An `async` function that:
1. Fetches `https://openlibrary.org/search.json?title=${encodeURIComponent(query)}&limit=12`
2. Checks `response.ok` — if `false`, throws `new Error(\`Request failed: ${response.status}\`)`
3. Parses and returns the JSON

The response shape is:
```json
{
  "numFound": 123,
  "docs": [
    {
      "title": "Dune",
      "author_name": ["Frank Herbert"],
      "first_publish_year": 1965
    }
  ]
}
```

### `normalizeBooks(docs)`

Accepts the `docs` array from the API response. Returns a new array of plain objects with clean, guaranteed properties:

```js
function normalizeBooks(docs) {
  return docs.map(doc => ({
    title: doc.title || 'Unknown Title',
    author: doc.author_name ? doc.author_name[0] : 'Unknown Author',
    year: doc.first_publish_year || 'Unknown Year',
  }));
}
```

This normalizer protects your rendering code from missing or inconsistent API fields.

---

## Part 3: UI state functions

Write four functions that control what is displayed in `#results-region`. All must update the region's content using `createElement` and `textContent`.

```js
function showLoading() { /* ... */ }
function showError(message) { /* ... */ }
function showEmpty() { /* ... */ }
function renderBooks(books) { /* ... */ }
```

### `showLoading()`
Clears the results region and appends a `<p>` with class `status-loading` reading "Searching for books…"

### `showError(message)`
Clears the results region and appends a `<p>` with class `status-error` containing the provided message.

### `showEmpty()`
Clears the results region and appends a `<p>` with class `status-empty` reading "No books found. Try a different search."

### `renderBooks(books)`
Clears the results region. For each book in the array, creates a `<article>` with class `book-card` containing:
- Title in an `<h2>`
- Author in a `<p>` with class `book-author`
- Publication year in a `<p>` with class `book-year`

Appends all cards to the results region.

---

## Part 4: Search handler

```js
const form = document.getElementById('search-form');
const input = document.getElementById('search-input');
const resultsRegion = document.getElementById('results-region');

form.addEventListener('submit', async (event) => {
  event.preventDefault();
  const query = input.value.trim();

  if (!query) {
    showError('Please enter a search term.');
    return;
  }

  showLoading();

  try {
    const data = await fetchBooks(query);
    const books = normalizeBooks(data.docs);

    if (books.length === 0) {
      showEmpty();
    } else {
      renderBooks(books);
    }
  } catch (error) {
    showError('Unable to load results. Please check your connection and try again.');
    console.error(error);
  }
});
```

---

## Part 5: CSS

In `labs/lab08/style.css`:
- Book cards display in a responsive grid (one column mobile, two or three columns desktop)
- `.status-loading`, `.status-error`, and `.status-empty` are visually distinct from each other and from card content
- The search form is accessible at all viewport sizes
- Cards have a consistent height/structure even when author or year is missing

---

## Testing requirements

Test each scenario manually before submitting:

- [ ] Search "Dune" → 12 cards appear with titles, authors, and years
- [ ] Search with an empty field → error message appears
- [ ] Search "asdkjhaskdjhaskdjh" (no results) → empty state message appears
- [ ] Disconnect Wi-Fi, search anything → network error message appears (not a blank screen)
- [ ] Watch the Network tab in DevTools while a search runs — confirm the request fires and the response shape
- [ ] Confirm `#results-region` has `aria-live="polite"` in the Elements panel

---

## Deliverable

In `labs/lab08/`:
- `index.html`
- `lab08.js`
- `style.css`
- `notes.md`

Commit at least three times (after HTML, after fetch functions, after full wiring). Push and deploy.

Submit to Canvas: live URL, repo URL, notes.md link.

---

## Process reflection (in notes.md)

Answer in 4–6 sentences:
- What does `response.ok` tell you that the `catch` block does not?
- What happened when you removed an `await` — which one caused the most confusing error?
- How did you make the loading and error states accessible to a screen reader, not just visually?

---

## Rubric

| Criterion | Excellent (4) | Proficient (3) | Developing (2) | Incomplete (1) |
|-----------|--------------|----------------|----------------|----------------|
| **Fetch and error handling** | `response.ok` checked; `try/catch/finally` used; all three states (loading, success, error) handled | Two states handled; response.ok checked | One state handled | No error handling |
| **Data normalization** | `normalizeBooks` protects against missing fields; all three properties normalized | Two properties normalized | One property normalized | No normalization |
| **Rendering** | Cards render all three fields; empty state shown; `createElement` used; no `innerHTML` | Cards render; one issue | Partial render | Not functional |
| **Accessible async** | `aria-live` on results region; loading and error messages text-based and readable | `aria-live` present | Partially accessible | No accessible state management |
| **CSS** | Responsive grid; three status states visually distinct | Responsive; two states distinct | Single column; minimal distinction | No meaningful CSS |
| **Reflection** | Specific; all three prompts addressed | Two prompts | Vague | Missing |
