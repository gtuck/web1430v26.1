# Lab 09 – Preference Panels and Saved UI Settings

## Purpose

localStorage lets you give users a continuous experience across sessions. This lab focuses entirely on the read-write-apply cycle: reading preferences at page load, applying them to the UI, saving them when the user makes a change, and surviving edge cases like missing data, corrupted JSON, and first-time visitors.

## Skills practiced

- Reading and writing `localStorage` with `getItem` / `setItem`
- Serializing objects with `JSON.stringify` and `JSON.parse`
- Handling `null` from `getItem` (first-visit defaults)
- Wrapping `JSON.parse` in `try/catch`
- Applying preferences synchronously in `DOMContentLoaded` before rendering
- Distinguishing `localStorage` from `sessionStorage`

## What you're building

A **Reading Preferences Panel** for a fictional long-form article page. The panel allows users to choose:
- **Color theme**: Light, Dark, or Sepia
- **Font size**: Small (14px), Medium (16px), or Large (20px)
- **Line spacing**: Compact (1.4), Normal (1.7), or Relaxed (2.0)

All preferences persist in localStorage. When the page reloads, the saved preferences are applied immediately — before any rendering — so there is no visible flash of default styling.

---

## Part 1: HTML structure

Create `labs/lab09/index.html`. The page has two main parts:

**Article area** (the content that preferences affect):
```html
<main id="article" class="theme-light font-medium spacing-normal">
  <article>
    <h1>The Long Road to Readable Text</h1>
    <p>Typography on the web has a long history...</p>
    <!-- At least 4 paragraphs of real or placeholder text -->
  </article>
</main>
```

**Preferences panel** (sidebar or overlay):
```html
<aside id="preferences-panel">
  <h2>Reading Preferences</h2>

  <fieldset>
    <legend>Color Theme</legend>
    <label><input type="radio" name="theme" value="light"> Light</label>
    <label><input type="radio" name="theme" value="dark"> Dark</label>
    <label><input type="radio" name="theme" value="sepia"> Sepia</label>
  </fieldset>

  <fieldset>
    <legend>Font Size</legend>
    <label><input type="radio" name="font-size" value="small"> Small</label>
    <label><input type="radio" name="font-size" value="medium"> Medium</label>
    <label><input type="radio" name="font-size" value="large"> Large</label>
  </fieldset>

  <fieldset>
    <legend>Line Spacing</legend>
    <label><input type="radio" name="spacing" value="compact"> Compact</label>
    <label><input type="radio" name="spacing" value="normal"> Normal</label>
    <label><input type="radio" name="spacing" value="relaxed"> Relaxed</label>
  </fieldset>

  <button id="reset-btn" type="button">Reset to Defaults</button>
</aside>
```

---

## Part 2: CSS

In `labs/lab09/style.css`, define the visual effect of each preference via classes on `<main id="article">`:

```css
/* Themes */
.theme-light  { background: #ffffff; color: #1a1a1a; }
.theme-dark   { background: #1a1a1a; color: #e8e8e8; }
.theme-sepia  { background: #f4ecd8; color: #3b2f2f; }

/* Font sizes */
.font-small  { font-size: 14px; }
.font-medium { font-size: 16px; }
.font-large  { font-size: 20px; }

/* Line spacing */
.spacing-compact  { line-height: 1.4; }
.spacing-normal   { line-height: 1.7; }
.spacing-relaxed  { line-height: 2.0; }
```

JavaScript will apply preferences by swapping these classes — it never sets inline styles.

---

## Part 3: Preferences module

In `labs/lab09/lab09.js`:

### Default preferences constant

```js
const DEFAULTS = {
  theme: 'light',
  fontSize: 'medium',
  spacing: 'normal',
};
const STORAGE_KEY = 'reading-prefs';
```

### `loadPreferences()`

Reads from localStorage. Returns the stored preferences, or `DEFAULTS` if nothing is stored or parsing fails:

```js
function loadPreferences() {
  const raw = localStorage.getItem(STORAGE_KEY);
  if (!raw) return { ...DEFAULTS };
  try {
    return JSON.parse(raw);
  } catch {
    return { ...DEFAULTS };
  }
}
```

### `savePreferences(prefs)`

```js
function savePreferences(prefs) {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(prefs));
}
```

### `applyPreferences(prefs, articleEl)`

Applies the preference object to the article element by swapping classes:

```js
function applyPreferences(prefs, articleEl) {
  // Remove all theme, font, and spacing classes first
  articleEl.className = articleEl.className
    .split(' ')
    .filter(cls => !cls.startsWith('theme-') && !cls.startsWith('font-') && !cls.startsWith('spacing-'))
    .join(' ');

  articleEl.classList.add(`theme-${prefs.theme}`);
  articleEl.classList.add(`font-${prefs.fontSize}`);
  articleEl.classList.add(`spacing-${prefs.spacing}`);
}
```

### `syncRadioButtons(prefs)`

After loading prefs, this function sets the correct radio button to checked:

```js
function syncRadioButtons(prefs) {
  document.querySelector(`[name="theme"][value="${prefs.theme}"]`).checked = true;
  document.querySelector(`[name="font-size"][value="${prefs.fontSize}"]`).checked = true;
  document.querySelector(`[name="spacing"][value="${prefs.spacing}"]`).checked = true;
}
```

---

## Part 4: Initialize and wire up

```js
document.addEventListener('DOMContentLoaded', () => {
  const article = document.getElementById('article');
  const prefs = loadPreferences();

  // Apply preferences immediately — before anything else renders
  applyPreferences(prefs, article);
  syncRadioButtons(prefs);

  // Listen for changes to any radio button group
  document.querySelector('#preferences-panel').addEventListener('change', (event) => {
    const updated = loadPreferences();

    if (event.target.name === 'theme') updated.theme = event.target.value;
    if (event.target.name === 'font-size') updated.fontSize = event.target.value;
    if (event.target.name === 'spacing') updated.spacing = event.target.value;

    savePreferences(updated);
    applyPreferences(updated, article);
  });

  // Reset button
  document.getElementById('reset-btn').addEventListener('click', () => {
    savePreferences({ ...DEFAULTS });
    applyPreferences(DEFAULTS, article);
    syncRadioButtons(DEFAULTS);
  });
});
```

---

## Part 5: Handling quota exceeded errors

`localStorage` has a storage limit (typically 5–10 MB per origin). In most preference-panel scenarios you will never hit it, but robust code handles the possibility. Wrap `setItem` in a `try/catch` so a full storage quota does not silently break saving.

Update `savePreferences` to catch `QuotaExceededError`:

```js
function savePreferences(prefs) {
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(prefs));
  } catch (err) {
    if (err.name === 'QuotaExceededError') {
      // Storage is full — preferences will not persist this session.
      // Show a non-intrusive warning rather than crashing.
      console.warn('localStorage quota exceeded. Preferences will not be saved this session.');
      showStorageWarning(); // implement below
    }
  }
}
```

Add `showStorageWarning()` to your JS and a matching element to your HTML:

```html
<!-- In index.html, inside #preferences-panel -->
<p id="storage-warning" role="alert" hidden>
  Preferences could not be saved (storage full). Your choices will reset on the next visit.
</p>
```

```js
function showStorageWarning() {
  const warning = document.getElementById('storage-warning');
  if (warning) warning.hidden = false;
}
```

**Why `role="alert"`?** Alert regions are announced immediately by screen readers — appropriate for error conditions that affect the user's experience even if they did not trigger an explicit action.

**Testing quota exceeded:**
You cannot easily fill storage in a lab setting, but you can verify your code handles the path correctly by temporarily replacing `localStorage.setItem(...)` with `throw Object.assign(new Error(), { name: 'QuotaExceededError' })` inside `savePreferences`, reloading, and confirming the warning appears without a JavaScript crash.

---

## Part 6: DevTools verification

Before submitting, use DevTools → Application → Local Storage to verify:

1. Open the page fresh (no stored preferences). Open DevTools → Application → Local Storage. The key should not exist yet.
2. Change a preference. The key `reading-prefs` should appear with a JSON string value.
3. Reload the page. The correct preferences should be applied immediately.
4. Click "Reset to Defaults". The stored JSON should return to the default values.
5. In DevTools, manually corrupt the stored value to an invalid string (e.g., `{bad json`). Reload. Your `try/catch` should recover gracefully and show defaults.

---

## Testing requirements

- [ ] First visit: page loads with light theme, medium font, normal spacing
- [ ] Change theme to dark: article updates immediately, preference saved
- [ ] Reload page: dark theme is applied before content is visible
- [ ] Reset: all preferences return to defaults, radio buttons update
- [ ] Corrupted localStorage value: page loads with defaults, no error thrown
- [ ] Quota exceeded (simulated): `showStorageWarning()` fires, no uncaught exception
- [ ] Keyboard: all radio buttons reachable by Tab and operable with arrow keys

---

## Deliverable

In `labs/lab09/`:
- `index.html`
- `lab09.js`
- `style.css`
- `notes.md`

Commit at least three times. Push and deploy.

Submit to Canvas: live URL, repo URL, notes.md link.

---

## Process reflection (in notes.md)

Answer in 4–6 sentences:
- What happened when you tried to store a preferences object directly without `JSON.stringify`?
- How did you test the "first visit" experience after preferences were already stored?
- What is the difference between `localStorage` and `sessionStorage`, and would `sessionStorage` be appropriate for reading preferences? Why or why not?

---

## Rubric

| Criterion | Excellent (4) | Proficient (3) | Developing (2) | Incomplete (1) |
|-----------|--------------|----------------|----------------|----------------|
| **localStorage read/write** | `setItem`/`getItem` with `JSON.stringify`/`JSON.parse`; null handled; `try/catch` on both read (parse) and write (quota exceeded); storage warning shown | Read/write works; one edge case (null or quota) not handled | Write works; read partially works | Not functional |
| **Preference application** | Classes swapped correctly for all three categories; no inline styles | Two categories work | One category works | Not functional |
| **Page load behavior** | Preferences applied in `DOMContentLoaded` before render; no visible flash | Applied at load but with minor flash | Applied after a delay | Not applied at load |
| **Reset** | Resets all three preferences in storage, DOM, and radio buttons | Resets two of three | Partially resets | Not implemented |
| **DevTools verification** | All five DevTools checks completed and documented in notes | Three checks documented | One check documented | Not documented |
| **Reflection** | Specific; all three prompts addressed | Two prompts | Vague | Missing |
