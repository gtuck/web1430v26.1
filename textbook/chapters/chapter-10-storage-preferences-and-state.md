# Chapter 10: Storage, Preferences, and State

Not all state belongs on a server. User preferences, UI choices, and session context can live in the browser — surviving page reloads, informing the interface, and making the experience feel continuous rather than reset every visit.

## What this chapter is really about

This chapter distinguishes between ephemeral state (JavaScript variables that disappear on reload) and persisted state (values stored in `localStorage` or `sessionStorage` that survive). You will learn when to use each storage mechanism, how to serialize and deserialize complex data, how to read stored preferences at page load, and what never to store in the browser.

## Key ideas

**`localStorage`** stores key-value pairs that persist indefinitely — across page reloads, browser restarts, and even reboots — until explicitly cleared.

**`sessionStorage`** stores key-value pairs that survive page reloads within the same tab but are cleared when the tab is closed.

Both APIs share the same interface:

```js
// Write
localStorage.setItem('theme', 'dark');

// Read (returns null if the key doesn't exist)
const theme = localStorage.getItem('theme');

// Delete one key
localStorage.removeItem('theme');

// Delete everything in this origin's storage
localStorage.clear();
```

**Both storage APIs only store strings.** To store objects or arrays, serialize with `JSON.stringify` when writing and parse with `JSON.parse` when reading:

```js
// Storing an object
const preferences = { theme: 'dark', fontSize: 'large' };
localStorage.setItem('preferences', JSON.stringify(preferences));

// Reading it back
const raw = localStorage.getItem('preferences');
const prefs = raw ? JSON.parse(raw) : null;
```

**Always handle the case where storage is empty** (`getItem` returns `null` on first visit):

```js
function loadPreferences() {
  const raw = localStorage.getItem('preferences');
  if (!raw) return { theme: 'light', fontSize: 'medium' };  // defaults
  try {
    return JSON.parse(raw);
  } catch {
    return { theme: 'light', fontSize: 'medium' };           // corrupted data fallback
  }
}
```

**Apply stored preferences at page load**, before rendering the UI. This prevents a flash of incorrect styling:

```js
document.addEventListener('DOMContentLoaded', () => {
  const prefs = loadPreferences();
  applyTheme(prefs.theme);
  applyFontSize(prefs.fontSize);
  renderPreferencesPanel(prefs);
});
```

**When to use which storage**:

| Use case | localStorage | sessionStorage |
|----------|-------------|----------------|
| User theme preference | ✓ | |
| Font size setting | ✓ | |
| Shopping cart (current session only) | | ✓ |
| Last search query (session) | | ✓ |
| Draft form content (persist across reloads) | ✓ | |
| User authentication token | ✗ Never | ✗ Never |

**State** is any information your application needs to remember in order to behave correctly. Some state is **ephemeral** (lives only in JavaScript variables — a counter, an open/closed flag, a temporary filter). Some state is **persisted** (should survive a reload — a user preference, a saved draft). Knowing which is which is a design decision, not a technical one.

## Mental model

Think of state in three tiers:

1. **In-memory** — JavaScript variables. Fast, but gone on reload. Good for UI flags, current selections, temporary calculations.
2. **Session** — `sessionStorage`. Survives page reloads within the same tab. Good for multi-step flows, session-specific context.
3. **Persistent** — `localStorage`. Survives everything until explicitly cleared. Good for user preferences, saved settings, offline drafts.

Start with in-memory state. Promote to sessionStorage or localStorage only when you have a concrete reason to persist it.

## Working habits

- Wrap `JSON.parse` in `try/catch`. Stored data can be corrupted by browser extensions, old versions of your code, or manual edits in DevTools.
- Provide default values when `getItem` returns `null`. Every preference needs a sensible default for first-time visitors.
- Apply stored preferences synchronously in `DOMContentLoaded` before your first render to avoid a flash of unstyled or incorrectly-configured UI.
- Inspect storage in DevTools: Application → Local Storage / Session Storage.
- Clear storage in DevTools when testing first-visit behavior: Application → Clear Site Data.
- In course work, use fictional or demo data when a feature resembles an account, registration, or user profile. Browser storage is for preferences, lightweight drafts, and non-sensitive state, not real personal records.

## Common mistakes

- **Storing objects without `JSON.stringify`**: `localStorage.setItem('user', { name: 'Jordan' })` stores the string `"[object Object]"`. Always stringify.
- **Not handling `null` from `getItem`**: `JSON.parse(null)` returns `null` without throwing, but calling `.theme` on `null` throws a TypeError. Check for `null` first.
- **Storing sensitive data**: localStorage is accessible to any JavaScript running on the page — including third-party scripts and browser extensions. Never store passwords, authentication tokens, or personal information.
- **Using real personal data in class projects**: even if the feature is "just a demo," treat names, emails, IDs, and preference data as sensitive unless the assignment explicitly says otherwise. Use fictional/demo values when practicing browser storage patterns.
- **Hitting the 5MB storage limit**: storing large amounts of data (images encoded as strings, full API responses) will throw a `QuotaExceededError`. Store references (IDs) rather than full records.
- **Not clearing stale state**: if your data model changes between versions of your app, old stored data can break the new version. Consider versioning your stored keys or clearing old data on initialization.

## Accessibility and UX note

Remembered preferences are a meaningful accessibility feature. Dark mode reduces eye strain for users with photosensitivity. Larger font size benefits users with low vision. Reduced motion settings prevent vestibular discomfort. These are not cosmetic features — they are functional for real users.

Apply stored preferences before the page renders to avoid a flash of default styling. This is especially important for dark mode: a white flash before switching to dark mode is jarring and potentially painful for photosensitive users.

Communicate preference changes clearly. When a user toggles dark mode, they should receive visual confirmation that the change was saved — not just a visual change that might feel accidental.

## Practice prompt

Build a preferences panel with:
- A dark/light mode toggle (updates `<body>` class and saves to localStorage)
- A font size selector: Small / Medium / Large (updates a `data-font-size` attribute on `<body>`)

Requirements:
1. On page load, read preferences from localStorage and apply them before showing the UI.
2. Provide sensible defaults for first-time visitors.
3. Wrap `JSON.parse` in `try/catch`.
4. When preferences change, save the updated object to localStorage immediately.
5. Confirm the preferences survive a page reload and a browser restart.

Test the "first visit" experience by clearing localStorage in DevTools and reloading.

## Reflection

What happened when you stored an object without `JSON.stringify`? What did you see in DevTools → Application → Local Storage? What was the difference between closing and reopening the tab when using `localStorage` vs `sessionStorage`? How did you handle the case where no preferences were stored yet?

## Vocabulary

- **localStorage** — browser storage that persists indefinitely across sessions (until cleared)
- **sessionStorage** — browser storage that persists for the duration of the tab session
- **state** — information an application needs to remember to behave correctly
- **persistence** — storing data so it survives a page reload or browser restart
- **serialization** — converting a JavaScript value (object, array) into a string for storage
- **JSON.stringify** — converts a JavaScript value to a JSON string
- **JSON.parse** — converts a JSON string back to a JavaScript value
- **getItem / setItem** — methods for reading and writing values in web storage
- **ephemeral** — lasting only as long as the current JavaScript session (lost on reload)
- **session** — the period from opening a tab to closing it

## Mini checklist

- I can store a string and an object in `localStorage` and retrieve them correctly.
- I can use `JSON.stringify` and `JSON.parse` when storing objects.
- I can handle the case where `getItem` returns `null` (first visit) with a default value.
- I can wrap `JSON.parse` in `try/catch` to handle corrupted data.
- I can explain the difference between `localStorage` and `sessionStorage`.
- I can read and apply stored preferences in `DOMContentLoaded` to avoid a flash of incorrect styling.
- I can inspect and clear storage using the DevTools Application panel.
