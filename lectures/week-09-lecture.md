# Week 09 Lecture Notes: Promises, Fetch, Async/Await, and Failure States

## Weekly focus
Write JavaScript that requests data from a remote API, handles loading and error states, and updates the DOM without blocking the page.

## Why this matters
Every modern web application that displays live data — weather, search results, social feeds, maps — uses asynchronous code. Without async patterns, a single slow network request would freeze the browser tab entirely. Understanding how JavaScript handles time and waiting is what makes it possible to build UIs that stay responsive while work happens in the background. This is one of the most important conceptual shifts in the course.

## Learning targets
- Explain why JavaScript uses an asynchronous model and what the event loop does at a high level
- Describe the three states of a Promise: pending, fulfilled, and rejected
- Write a `fetch()` call using `async/await` that reads JSON from a public API
- Check `response.ok` before parsing and throw a meaningful error if the request failed
- Handle loading, success, error, and empty states in the DOM
- Use `aria-live` to announce async content changes to screen readers

## Core concepts

### Why async exists: JavaScript is single-threaded
JavaScript runs on a single thread. That means it can only do one thing at a time. If a network request took 3 seconds and JavaScript waited for it synchronously, your entire page — scrolling, clicks, animations — would be completely frozen for those 3 seconds.

The solution is asynchronous execution: start the request, register a callback for when it finishes, and let the rest of the page continue running. The **event loop** is the mechanism that makes this work. It watches a queue of completed tasks (like "the fetch response arrived") and runs the registered callbacks when the main thread is free.

You do not need to implement the event loop — you need a mental model: *JavaScript starts async work, moves on, and comes back to the result later.*

### Promises: pending, fulfilled, rejected
A `Promise` is an object that represents a value that is not available yet. It is always in one of three states:

- **Pending** — the operation has started but has not completed
- **Fulfilled** — the operation completed successfully; the value is available
- **Rejected** — the operation failed; an error is available

`fetch()` returns a Promise. You do not get the response immediately — you get a promise that the response *will* arrive.

### async/await syntax
`async/await` is syntactic sugar over Promises. It lets you write async code that reads like synchronous code, without losing the non-blocking behavior.

```js
async function loadUser(userId) {
  const response = await fetch(`https://jsonplaceholder.typicode.com/users/${userId}`);
  const data = await response.json();
  return data;
}
```

Rules:
- `await` can only be used inside a function marked `async`
- `await` pauses execution of that function until the Promise settles
- The function itself returns a Promise, so callers can `await` it too

### Checking response.ok and throwing errors
`fetch()` only rejects its Promise for network-level failures (no connection, DNS error). A `404 Not Found` or `500 Server Error` still resolves — it just has `response.ok === false`. You must check this manually.

```js
async function fetchBreed(breed) {
  const response = await fetch(`https://dog.ceo/api/breed/${breed}/images/random`);

  if (!response.ok) {
    throw new Error(`Request failed: ${response.status} ${response.statusText}`);
  }

  return await response.json();
}
```

By throwing an error explicitly, you allow the `catch` block up the call stack to handle it uniformly.

### try/catch/finally
Wrap `await` calls in `try/catch` to handle both network errors and the explicit errors you throw:

```js
async function loadBreedImage(breed) {
  try {
    const data = await fetchBreed(breed);
    displayImage(data.message);
  } catch (error) {
    displayError(error.message);
  } finally {
    hideLoadingSpinner();
  }
}
```

`finally` runs whether the request succeeded or failed — use it to clean up loading state.

### Modeling UI states
Every async operation can be in one of four states. Your UI should reflect all of them:

| State | When | What to show |
|---|---|---|
| Loading | After request starts, before it resolves | Spinner, "Loading..." text |
| Success | Response arrived and data is valid | Rendered content |
| Error | Network failure or bad status | Error message with instructions |
| Empty | Request succeeded but returned no results | "No results found" message |

A clean pattern that handles all four:

```js
async function searchPokemon(name) {
  showLoading();

  try {
    const response = await fetch(`https://pokeapi.co/api/v2/pokemon/${name.toLowerCase()}`);

    if (!response.ok) {
      throw new Error(`Pokemon not found (status ${response.status})`);
    }

    const pokemon = await response.json();

    if (!pokemon) {
      showEmpty();
      return;
    }

    renderPokemon(pokemon);
  } catch (error) {
    showError(error.message);
  } finally {
    hideLoading();
  }
}

function showLoading() {
  document.getElementById("status").textContent = "Loading...";
  document.getElementById("results").innerHTML = "";
}

function showError(message) {
  document.getElementById("status").textContent = "";
  document.getElementById("error").textContent = message;
}

function hideLoading() {
  document.getElementById("status").textContent = "";
}
```

### aria-live for async updates
When content changes dynamically — after a fetch completes — screen readers are not automatically notified. The `aria-live` attribute tells assistive technology to announce changes to a region when they happen.

```html
<div id="status" aria-live="polite" aria-atomic="true"></div>
<div id="results"></div>
```

- `aria-live="polite"` — announces the change after the user finishes what they are doing
- `aria-live="assertive"` — interrupts immediately (use sparingly, for critical errors)
- `aria-atomic="true"` — reads the entire region's content, not just the changed part

When you update `status.textContent` with "Loading..." or an error message, screen readers will read it aloud without any extra JavaScript.

## Common mistakes

1. **Forgetting `await` on `response.json()`.** `response.json()` also returns a Promise. Writing `const data = response.json()` gives you a Promise object, not the parsed data. Both `fetch()` and `.json()` need `await`.

2. **Treating a 404 as an error automatically.** As covered above, `fetch()` resolves on a 404. Students often expect it to throw. Always check `response.ok`.

3. **Putting the entire app inside one giant `try` block.** This makes it impossible to know which line failed. Keep `try/catch` scoped tightly around the async calls.

4. **Not showing any UI feedback during loading.** If the request takes 2 seconds and the page shows nothing, users assume it is broken. Always set a loading state before `await`.

5. **Using `async` on a function and then not `await`-ing it at the call site.** Calling `loadData()` without `await` starts it immediately and returns a Promise. If it fails later, the failure becomes a rejected Promise and may surface as an unhandled rejection. Either `await` the call or attach a `.catch()` handler.

## Accessibility connection
Asynchronous content updates are one of the most common accessibility failures in modern web apps. When a fetch completes and new content appears, sighted users see it instantly — but screen reader users receive no notification unless you explicitly mark regions with `aria-live`. Error messages are equally important: an error that appears visually but is never announced leaves keyboard-only and screen reader users unable to understand why their action failed.

## Demo walkthrough
1. Start with a static HTML page: a search input, a button, an empty `<div id="results">`, and a `<div id="status" aria-live="polite">`.
2. Write a bare `fetch()` call in the console, show the Promise object before it resolves.
3. Add `await` inside an `async` function — show the resolved response object.
4. Show `response.ok` and `response.status` in the console.
5. Add `.json()` with `await` — show the parsed object.
6. Wire up the button to call the async function; show the four UI states in sequence by temporarily adding `throw new Error()` lines.
7. Add `aria-live="polite"` to the status div; use a screen reader or accessibility tree to verify the announcement fires.

## Practice prompt
Using the [Dog CEO API](https://dog.ceo/api/breeds/image/random) or the [JSONPlaceholder API](https://jsonplaceholder.typicode.com/posts), build a small page with:
- A button that triggers a `fetch()` call
- A loading state displayed while the request is in flight
- The result rendered to the DOM on success
- An error message rendered to the DOM on failure (test it by mistyping the URL)
- An `aria-live` region that announces status changes

## Bridge
Lab 08 has you build a full API-powered viewer using the patterns from this lecture — you will need the four-state UI model and the `aria-live` region. Quiz 5 will test whether you can read async code and trace its execution order, and whether you know what happens when `response.ok` is false. Assignment 4 extends the lab into a more complete feature; the cleaner you keep your state-management functions, the easier that extension will be.
