# Chapter 9: Fetch, JSON, and Remote Data

The browser can request data from remote servers without navigating away from the page. Understanding how that request-response cycle works asynchronously — and how to handle every outcome, including failure — is one of the most practical skills in client-side development.

## What this chapter is really about

This chapter introduces asynchronous JavaScript by teaching the Fetch API: how to request remote data, how to parse the response, how to handle errors, and how to keep the interface responsive and informative while the user waits. The goal is to write async code that handles three states every time: loading, success, and error.

## Key ideas

**Fetch** initiates an HTTP request and returns a **Promise** — a placeholder for a value that will arrive in the future.

```js
fetch('https://api.example.com/products')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error(error));
```

**async/await** is a cleaner syntax for the same thing:

```js
async function loadProducts() {
  const response = await fetch('https://api.example.com/products');
  const data = await response.json();
  console.log(data);
}
```

`await` pauses the function until the Promise resolves. It can only be used inside an `async` function.

**The two-step response** — fetch resolves in two stages. The first `await` resolves when the HTTP response headers arrive (the network round trip is complete). The second `await response.json()` resolves when the response body is fully read and parsed.

**Always check `response.ok`** before parsing the body. A 404 or 500 status code does not throw — it resolves with `response.ok === false`:

```js
async function loadProducts() {
  const response = await fetch('https://api.example.com/products');

  if (!response.ok) {
    throw new Error(`Request failed: ${response.status}`);
  }

  const data = await response.json();
  return data;
}
```

**Always use try/catch** to handle network failures, bad JSON, and unexpected errors:

```js
async function loadAndRender() {
  showLoading();
  try {
    const data = await loadProducts();
    renderProducts(data);
  } catch (error) {
    showError('Unable to load products. Please try again.');
    console.error(error);
  } finally {
    hideLoading();
  }
}
```

**The three UI states** every async interface must handle:
1. **Loading** — show a loading indicator before the request starts
2. **Success** — render the data
3. **Error** — show a descriptive error message

Missing any of these leaves users confused.

**CORS (Cross-Origin Resource Sharing)** — browsers block requests to a different domain unless that server explicitly allows it via CORS headers. If you get a CORS error, it is a server configuration issue, not a bug in your JavaScript. Use APIs that explicitly support public access (like JSONPlaceholder, Open Library, or The Movie Database) while learning.

**API viability** — before you build your interface around an API, verify that it is actually usable for your project. Four checks matter most:

1. **Browser access** — does the API support cross-origin browser requests, or will CORS block you?
2. **Rate limits / auth** — how often can you request data, and do you need an API key?
3. **Attribution / terms** — does the provider require a link, logo, credit line, or any specific terms-of-use compliance?
4. **Reliability** — how stable and current is the data, and what happens in your UI when fields are missing or the service is unavailable?

Choosing an API is not just a technical question. It is a product decision. A flashy API that rate-limits aggressively, breaks in the browser, or forbids your intended use is a bad fit no matter how interesting the data looks.

## Mental model

Fetch is **non-blocking**. When you call `fetch()`, the browser sends the request and immediately moves on to the next line of code. The function does not pause and wait — it returns a Promise. When you use `await`, you are telling JavaScript: "pause *this function* here and continue other work until the Promise resolves."

Think of a Promise as a ticket at a deli counter. You order (call `fetch`), get your ticket (the Promise), and do other things. When your number is called (the Promise resolves), you come back and collect your result (the data).

Synchronous code runs top to bottom, one step at a time. Asynchronous code schedules work to happen later, in response to events or resolved Promises.

## Working habits

- Show a loading indicator *before* calling `fetch`. Remove it in `finally` so it disappears whether the request succeeded or failed.
- Always check `response.ok` — a 404 is a valid HTTP response, not a thrown error.
- Always wrap async code in `try/catch`. Network failures, CORS errors, and bad JSON all throw exceptions.
- Show descriptive error messages to users. "Something went wrong" is not helpful. "Could not load products — please check your connection and try again" is.
- Log the full error to the console for debugging while showing a user-friendly message in the UI.
- Read the Network tab in DevTools while your fetch runs. See the request, its status code, and the raw response body.
- Before you commit to an API for a project, document your API viability check: CORS support, rate limits, attribution requirements, and data reliability.

## Common mistakes

- **Forgetting `await` on `fetch()`**: you get a Promise object, not a response. Calling `.json()` on a Promise throws immediately.
- **Forgetting `await` on `response.json()`**: same problem — you get another Promise, not data.
- **Not checking `response.ok`**: a 404 does not throw. Without the check, you call `.json()` on a 404 response body (often an HTML error page) and get a JSON parse error — confusing and misleading.
- **No error handling**: if the server is down, `fetch` throws. Without `try/catch`, the error propagates silently or crashes your app.
- **No loading state**: users see a blank section and don't know whether to wait or assume something broke.
- **Using an API without CORS support**: the browser blocks the request and you see a CORS error in the Console. Check that your chosen API allows cross-origin requests.

## Accessibility and UX note

Loading states need to be communicated to assistive technology, not just shown visually. Use `aria-live="polite"` on the region that updates so screen readers announce changes:

```html
<div id="results" aria-live="polite">
  <!-- loading message, error, or results are injected here -->
</div>
```

Error messages must be visible (not just a console log), descriptive, and persistent — not a toast that disappears in 2 seconds. A user navigating slowly with a screen reader may miss a transient message entirely.

## Practice prompt

Write an async function called `loadPosts()` that:

1. Shows a "Loading…" message in a designated container before fetching.
2. Fetches `https://jsonplaceholder.typicode.com/posts?_limit=5`.
3. Checks `response.ok` — if false, throws an error with the status code.
4. Parses the JSON.
5. For each post, creates a `<article>` element using `createElement` with the post's `title` (in an `<h2>`) and `body` (in a `<p>`), and appends it to the container.
6. Wraps everything in `try/catch`. On error, clears the container and shows a descriptive error message.
7. Removes the "Loading…" message in a `finally` block.
8. Write four short bullets describing whether this API is viable for a student project: CORS support, rate limits, attribution requirements, and data reliability.

Add `aria-live="polite"` to the container. Test the error state by changing the URL to something invalid.

## Reflection

What happened when you removed an `await` — which one caused the most confusing error? What does the Network tab show while the request is in flight? How did you make the loading state and error message perceivable to a screen reader, not just visually?

## Vocabulary

- **fetch** — a browser API for making HTTP requests that returns a Promise
- **Promise** — an object representing a value that is not yet available but will resolve (or reject) in the future
- **async** — a keyword that marks a function as asynchronous; it always returns a Promise
- **await** — a keyword used inside async functions to pause execution until a Promise resolves
- **response** — the object returned by `fetch` when the HTTP headers arrive
- **JSON** — JavaScript Object Notation; a text format for structured data
- **endpoint** — a URL that serves data (e.g., `/api/products`)
- **status code** — a number in the HTTP response indicating success (200), not found (404), server error (500), etc.
- **CORS** — Cross-Origin Resource Sharing; a browser security mechanism that blocks requests to different domains unless explicitly permitted by the server
- **loading state** — the UI state while a request is in flight
- **try/catch** — a JavaScript construct that handles errors thrown in async (and synchronous) code

## Mini checklist

- I can write an async function that fetches data with `await` and parses the response with `await response.json()`.
- I can check `response.ok` and throw a meaningful error when it is false.
- I can wrap a fetch call in `try/catch` and show a user-facing error message in the catch block.
- I can show a loading state before the request and remove it in a `finally` block.
- I can handle three distinct UI states: loading, success, and error.
- I can use the Network tab in DevTools to inspect a request's status and response body.
- I can explain what a CORS error is and why the browser enforces it.
- I can evaluate whether an API is viable for browser-based project work before I build around it.
