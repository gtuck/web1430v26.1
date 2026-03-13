# API Troubleshooting Guide

This guide covers the most common problems students encounter when working with real-world public APIs. Bookmark it while working on Assignment 4 and Project 2.

---

## 1. Accessing Deeply Nested Data

Some APIs return objects many levels deep. A response that looks tidy in the docs may require several property accesses to reach the value you want.

**Example problem:** an API returns:

```json
{
  "result": {
    "items": [
      { "details": { "author": { "name": "Jane Austen" } } }
    ]
  }
}
```

**Fragile access:**

```js
const author = data.result.items[0].details.author.name; // throws if any level is missing
```

**Defensive access using optional chaining and nullish coalescing:**

```js
const author = data?.result?.items?.[0]?.details?.author?.name ?? 'Unknown';
```

**Best practice:** do this work once, inside your `normalizeData()` function. The rest of your code should only ever touch the clean, normalized object — never the raw response.

---

## 2. Fields That Are Sometimes Null or Missing

Many APIs omit fields entirely when the value is absent, or return `null`. If your code assumes a field is always present, it will throw when it is not.

**Example:**

```json
{ "title": "Dune", "cover_i": null }          // cover ID is null
{ "title": "Foundation" }                      // cover ID is missing entirely
```

**Handle both cases in normalization:**

```js
function normalizeBook(doc) {
  return {
    title: doc.title ?? 'Untitled',
    coverId: doc.cover_i ?? null,             // store null explicitly; render handles it
    author: doc.author_name?.[0] ?? 'Unknown',
    year: doc.first_publish_year ?? 'Year unknown',
  };
}
```

**In the render function**, check before using the optional value:

```js
const img = item.coverId
  ? `<img src="https://covers.openlibrary.org/b/id/${item.coverId}-M.jpg" alt="Cover of ${item.title}">`
  : `<div class="no-cover" aria-label="No cover available"></div>`;
```

---

## 3. Fields That Change Type

Some APIs return a value as a string in one response and as a number in another — or an array when there is more than one item and a plain string when there is only one.

**Example:**

```json
{ "author_name": ["George Orwell"] }     // array with one item
{ "author_name": "Isaac Asimov" }        // plain string (inconsistent API)
```

**Normalize to a consistent type:**

```js
const authorRaw = doc.author_name;
const author = Array.isArray(authorRaw)
  ? authorRaw[0] ?? 'Unknown'
  : authorRaw ?? 'Unknown';
```

---

## 4. Array Versus Object Wrapping

Some APIs wrap results in a property; others return a bare array. Check the actual response in the browser's Network tab before writing normalization code.

**Fetch and log the raw response before writing anything else:**

```js
const res = await fetch(url);
const data = await res.json();
console.log(data);                // inspect in DevTools — is it an array or an object?
```

Common patterns and how to extract the array:

| Response shape | How to get the array |
|---|---|
| `[{...}, {...}]` | `data` directly |
| `{ "docs": [{...}] }` | `data.docs` |
| `{ "results": [{...}] }` | `data.results` |
| `{ "message": { "breeds": [...] } }` | `data.message.breeds` |

Write a guard in `normalizeData()` so it always receives an array:

```js
function normalizeData(raw) {
  const items = Array.isArray(raw) ? raw : (raw.docs ?? raw.results ?? []);
  return items.map(normalizeItem);
}
```

---

## 5. CORS Errors

If the browser console shows a CORS error, the API does not allow browser requests from other origins. This is a server-side restriction — you cannot fix it from the browser.

**What to do:**
- Switch to an API that explicitly supports browser requests (most APIs in the Assignment 4 suggested list do).
- Check the API's documentation for a note about `Access-Control-Allow-Origin`.
- Test in the browser's Network tab: look for a preflight `OPTIONS` request that returns a 4xx status.

---

## 6. Rate Limiting (429 Too Many Requests)

Free-tier APIs often limit how many requests you can make per minute. If you see a `429` status in the Network tab:

- Slow down your requests — do not fire a new fetch on every keystroke. Debounce input with a short delay (300–500ms).
- Cache the last successful result in `sessionStorage` so reloads do not consume your rate limit.
- Read the API documentation for the specific rate limit and respect it.

**Simple debounce:**

```js
let debounceTimer;
searchInput.addEventListener('input', () => {
  clearTimeout(debounceTimer);
  debounceTimer = setTimeout(() => fetchData(searchInput.value), 400);
});
```

---

## 7. Debugging Checklist

When a fetch is not working:

1. Open DevTools → **Network** tab. Find the request. What is the status code?
2. Click the response — does the JSON match what you expected?
3. `console.log(data)` immediately after `await res.json()` — before any normalization.
4. Check the **Console** tab for red errors (CORS, JSON parse failure, undefined access).
5. Verify the URL is correct — paste it directly into the browser address bar.
6. Confirm your normalization function receives the array, not the wrapper object.
