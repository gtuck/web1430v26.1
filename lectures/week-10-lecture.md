# Week 10 Lecture Notes: localStorage, sessionStorage, and UI State

## Weekly focus
Persist user preferences and UI state across page loads using the Web Storage API, and build a centralized state pattern that keeps the DOM in sync with your data.

## Why this matters
Without client-side storage, every page reload wipes out everything the user has done — their preferences, their progress, their settings. The Web Storage API gives you a simple key-value store that lives in the browser with no server required. Learning to store and restore state is also the foundation for understanding how larger frameworks (React, Vue) think about data: the UI is a function of state, not a pile of direct DOM mutations.

## Learning targets
- Explain the difference between `localStorage` and `sessionStorage` in terms of persistence and scope
- Use `setItem`, `getItem`, `removeItem`, and `clear` correctly
- Serialize and deserialize a JavaScript object using `JSON.stringify` and `JSON.parse`
- Explain why all storage values are strings and what that means for reading them back
- Apply a centralized state object pattern where the DOM is derived from state, not mutated directly
- Identify appropriate use cases for each storage type

## Core concepts

### localStorage vs sessionStorage
Both APIs live on the `window` object and share the same four methods. The difference is lifetime and scope:

| | `localStorage` | `sessionStorage` |
|---|---|---|
| Persists after tab close | Yes | No |
| Persists after browser close | Yes | No |
| Shared across tabs (same origin) | Yes | No — each tab has its own |
| Cleared by user/JS | Manual | Automatic on tab close |
| Typical use | Preferences, saved settings | Form wizard state, one-session cart |

Both are **origin-scoped** — code on `https://example.com` cannot read storage from `https://other.com`.

### The four storage methods
```js
// Store a value
localStorage.setItem("theme", "dark");

// Read it back
const theme = localStorage.getItem("theme"); // "dark"

// Remove one key
localStorage.removeItem("theme");

// Wipe everything for this origin
localStorage.clear();
```

`getItem` returns `null` (not `undefined`) when the key does not exist. Always handle the `null` case:

```js
const theme = localStorage.getItem("theme") ?? "light"; // default to "light"
```

### All values are strings
This is the most important constraint: `localStorage` stores strings only. Numbers, booleans, and objects must be converted.

```js
// BAD — stores the string "[object Object]"
localStorage.setItem("user", { name: "Ana", score: 42 });

// GOOD — serialize first
localStorage.setItem("user", JSON.stringify({ name: "Ana", score: 42 }));

// Reading back — always parse
const raw = localStorage.getItem("user");
const user = raw ? JSON.parse(raw) : null;
console.log(user.name); // "Ana"
console.log(user.score); // 42 (number, not string)
```

The same applies to booleans:

```js
localStorage.setItem("notifications", true);
localStorage.getItem("notifications"); // "true" — a string!
localStorage.getItem("notifications") === true; // false — never works
localStorage.getItem("notifications") === "true"; // true — this is how you check it
```

### Storing and restoring user preferences
A common pattern: save a preference when it changes, restore it on page load.

```js
const toggle = document.getElementById("dark-mode-toggle");

// Restore on load
const saved = localStorage.getItem("darkMode");
if (saved === "true") {
  document.body.classList.add("dark");
  toggle.checked = true;
}

// Save on change
toggle.addEventListener("change", () => {
  const isDark = toggle.checked;
  document.body.classList.toggle("dark", isDark);
  localStorage.setItem("darkMode", isDark);
});
```

### Centralized state object
Once your app stores several pieces of UI state, managing them individually becomes error-prone. A better approach: keep all state in one object and write a `render` function that derives the DOM from that object.

```js
// Central state — single source of truth
let state = {
  theme: "light",
  fontSize: "medium",
  notifications: true,
};

// Apply state to the DOM
function applyState() {
  document.body.dataset.theme = state.theme;
  document.body.dataset.fontSize = state.fontSize;
  document.getElementById("notify-toggle").checked = state.notifications;
}

// Update state and persist in one place
function updateState(changes) {
  state = { ...state, ...changes };
  localStorage.setItem("appState", JSON.stringify(state));
  applyState();
}

// Load state on page start
function loadState() {
  const saved = localStorage.getItem("appState");
  if (saved) {
    state = { ...state, ...JSON.parse(saved) };
  }
  applyState();
}

loadState();
```

Now every part of the app calls `updateState({ theme: "dark" })` instead of touching the DOM directly. The DOM is always a reflection of `state`, never the source of truth.

### Storage limits and when to use each
Browsers typically allow 5–10 MB per origin for Web Storage. This is enough for preferences and small data structures — not for images, large datasets, or anything that should live on a server. Rules of thumb:

- Use `localStorage` for preferences that should survive across visits (theme, language, saved form drafts)
- Use `sessionStorage` for temporary state that only needs to last one session (current step in a multi-step form, scroll position)
- Use `IndexedDB` (beyond this course) for larger structured data
- Never store passwords, tokens, or sensitive data in Web Storage — it is accessible to any JavaScript on the page

## Common mistakes

1. **Reading a stored object without parsing it.** `JSON.stringify` on the way in, `JSON.parse` on the way out — every time. Forgetting `JSON.parse` gives you a string like `"[object Object]"` where you expected an object.

2. **Comparing a stored boolean to `true`.** Storage always gives back a string. `getItem("flag") === true` is always `false`. Compare to `"true"` or use `JSON.parse(getItem("flag"))`.

3. **Calling `clear()` when you only mean to remove one key.** `localStorage.clear()` removes everything for your origin, including keys set by other parts of your app. Use `removeItem("specificKey")` instead.

4. **Assuming storage is always available.** In private/incognito mode, some browsers throw a `SecurityError` when you call `setItem`. Wrap storage calls in a try/catch if you need resilience, or at minimum do not let a storage error crash your whole app.

5. **Updating the DOM directly instead of updating state.** When you mix "update DOM here, save to storage there" across multiple event handlers, the DOM and storage drift out of sync. Centralize updates through one function so the DOM and storage are always updated together.

## Accessibility connection
Persisting preferences like font size, contrast, and reduced motion settings has direct accessibility value. If a user increases the text size for readability, that setting should survive a page reload — forcing them to re-apply it every visit is a usability barrier. When restoring state on page load, apply it before the page renders visible content (or as early as possible) to avoid a visible "flash" from default to preferred settings.

## Demo walkthrough
1. Build a settings panel with a theme toggle (light/dark), a font size selector (small/medium/large), and a checkbox for showing hints.
2. Show the Application tab in Chrome DevTools > Local Storage — currently empty.
3. Wire up each control to call `updateState()` with the changed value.
4. Reload the page — settings are lost (storage not hooked up yet).
5. Add `localStorage.setItem` inside `updateState` and `localStorage.getItem` inside `loadState`.
6. Reload again — settings survive. Show the key/value pairs appearing in DevTools.
7. Open a new tab to the same page — settings are there (localStorage). Open a new tab to a different origin — storage is not shared.
8. Demonstrate `sessionStorage` by switching the calls and showing the value disappears when the tab closes.

## Practice prompt
Build a "reading preferences" panel with three controls:
- A `<select>` for font size (small, medium, large)
- A toggle for dark mode
- A toggle for hiding images

When any control changes, save the full preferences object to `localStorage` using `JSON.stringify`. On page load, read the saved preferences and apply them immediately. Write a `render(prefs)` function that takes the preferences object and applies all three settings to the page — do not reach into the DOM from individual event handlers.

## Bridge
Lab 09 builds a full preference panel using exactly this pattern — you will save and restore a preferences object across reloads. Project 2 Proposal is also due this week; the project will use both the Fetch API from Week 09 and storage from this week, so your proposal should describe what data you will fetch and what preferences or state you will persist. Quiz 6 will ask you to trace a JSON round-trip and identify what type `getItem` returns.
