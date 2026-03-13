# Chapter 13: Accessibility Synthesis

You have been applying accessibility practices throughout this course — semantic HTML, ARIA attributes, screen reader testing, Lighthouse audits. This chapter pulls those threads together into a unified reference for building interfaces that work for everyone.

## What this chapter is really about

Accessibility is not a checklist you run at the end of a project. It is a design constraint you apply continuously, the same way you apply performance or security constraints. Every decision — which HTML element to use, how to show an error message, what happens when a modal opens — has an accessibility consequence. The goal of this chapter is to give you a mental framework for making those decisions correctly the first time, and a testing habit that catches failures before submission.

At this point in the course, you have the full toolkit: semantic HTML, ARIA attributes, async JavaScript, and component-based architecture. The patterns here are advanced — modals with focus trapping, accessible tab widgets, keyboard contracts for custom controls — but they follow from principles you already know. If you understand why `aria-live` works, you can apply it to any situation where dynamic content needs to be announced. If you understand the keyboard contract for a dialog, you can implement it in vanilla JavaScript today and in a Vue component tomorrow.

## Key ideas

### WCAG 2.1 conformance levels

The Web Content Accessibility Guidelines (WCAG) define three conformance levels:

- **Level A** — the minimum. Failures at this level block access entirely for some users (e.g., an image with no `alt` attribute, a video with no alternative). Every page must meet Level A.
- **Level AA** — the professional and legal standard. This is what courts, employers, and government contracts require. WCAG 2.1 AA adds requirements like color contrast ratios, resizable text, and consistent navigation. This course targets AA.
- **Level AAA** — the enhanced level. Some criteria are impossible to meet for all content (WCAG acknowledges this), so AAA is a goal for specific pages or features rather than an entire site requirement.

What AA means in day-to-day practice: every page you build should have sufficient color contrast (4.5:1 for body text), keyboard-accessible controls, text alternatives for non-text content, error identification and correction guidance, and no content that relies on sensory characteristics (color, shape, location, sound) alone to convey meaning.

### The keyboard navigation contract

Every interactive element in a web page has an implicit **keyboard contract** — a set of expected behaviors users have learned from years of using software. Violating the contract breaks assistive technology and frustrates power users.

**Tab order** — pressing Tab moves focus forward through focusable elements (links, buttons, inputs, elements with `tabindex="0"`). Focus order must match the visual reading order. Elements that appear first in the layout should appear first in the tab sequence.

```js
// Making a custom element focusable — only do this when a native element cannot work
el.setAttribute('tabindex', '0');

// Never use tabindex > 0 — it creates an unnatural tab order that confuses users
// Bad:
el.setAttribute('tabindex', '3');
```

**Widget keyboard patterns** — custom widgets have their own expected keyboard behavior:

| Widget | Keys users expect |
|--------|------------------|
| Tabs | Tab to reach the tab list, Arrow keys to move between tabs, Enter/Space to activate |
| Accordion | Tab to reach each header, Enter/Space to expand/collapse |
| Dialog/Modal | Tab and Shift+Tab cycle through focusable elements inside, Escape closes |
| Dropdown menu | Enter/Space to open, Arrow keys to navigate items, Escape to close |
| Listbox | Arrow keys to navigate options, Space to select, Enter to confirm |

The keyboard contract means: once you build a custom widget, you own its keyboard behavior. A `<div role="tablist">` does nothing without JavaScript implementing the arrow-key navigation.

**Focus trapping in modals** — when a dialog is open, Tab must cycle only through elements inside the dialog. If focus can escape to the page behind the modal, keyboard users lose their place and screen reader users hear content that is visually hidden.

```js
function trapFocus(dialogEl) {
  const focusable = dialogEl.querySelectorAll(
    'a[href], button:not([disabled]), input:not([disabled]), ' +
    'select:not([disabled]), textarea:not([disabled]), [tabindex="0"]'
  );
  const first = focusable[0];
  const last = focusable[focusable.length - 1];

  dialogEl.addEventListener('keydown', (event) => {
    if (event.key !== 'Tab') return;

    if (event.shiftKey) {
      // Shift+Tab from first element → wrap to last
      if (document.activeElement === first) {
        event.preventDefault();
        last.focus();
      }
    } else {
      // Tab from last element → wrap to first
      if (document.activeElement === last) {
        event.preventDefault();
        first.focus();
      }
    }
  });
}
```

### Focus management

**Programmatic focus** — moving focus with `.focus()` — is necessary in four situations:

1. **Modal opens**: move focus to the first focusable element inside the dialog (or the dialog container itself if it has `tabindex="-1"`).
2. **Modal closes**: return focus to the trigger that opened it, so the user's position in the page is restored.
3. **Async content loads**: after a fetch completes and new content renders, move focus to a heading or the results container so screen reader users know something changed.
4. **Route changes** (in single-page apps): move focus to the page's main heading so users are not left at the bottom of the previous page's content.

```js
// Pattern 1: Opening a modal
function openModal(triggerEl) {
  const modal = document.querySelector('#modal');
  modal.removeAttribute('hidden');
  modal.setAttribute('aria-modal', 'true');

  // Move focus into the dialog
  const firstFocusable = modal.querySelector('button, [href], input, [tabindex="0"]');
  firstFocusable?.focus();

  // Remember who opened it so we can restore focus on close
  modal._opener = triggerEl;
  trapFocus(modal);

  // Close on Escape
  modal.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') closeModal();
  });
}

// Pattern 2: Closing a modal — return focus to the trigger
function closeModal() {
  const modal = document.querySelector('#modal');
  const opener = modal._opener;
  modal.setAttribute('hidden', '');
  opener?.focus();
}
```

```js
// Pattern 3: Focus after async content loads
async function loadResults(query) {
  showLoading();
  try {
    const data = await fetchResults(query);
    renderResults(data);

    // Move focus to the results heading so screen reader users are oriented
    const heading = document.querySelector('#results-heading');
    heading.setAttribute('tabindex', '-1');
    heading.focus();
  } catch (error) {
    showError(error.message);
  } finally {
    hideLoading();
  }
}
```

`tabindex="-1"` on a non-interactive element makes it programmatically focusable without adding it to the natural tab order.

### Modal / dialog pattern

A fully accessible dialog requires the right HTML roles and ARIA attributes, focus management, and keyboard handling.

```html
<!-- Trigger button -->
<button type="button" id="open-btn" aria-controls="confirm-dialog">
  Delete item
</button>

<!-- Dialog — hidden by default -->
<div
  id="confirm-dialog"
  role="dialog"
  aria-modal="true"
  aria-labelledby="dialog-title"
  aria-describedby="dialog-desc"
  hidden
>
  <h2 id="dialog-title">Confirm deletion</h2>
  <p id="dialog-desc">
    This will permanently delete the item. This action cannot be undone.
  </p>
  <button type="button" id="confirm-btn">Delete</button>
  <button type="button" id="cancel-btn">Cancel</button>
</div>
```

```js
const openBtn = document.querySelector('#open-btn');
const dialog = document.querySelector('#confirm-dialog');
const confirmBtn = dialog.querySelector('#confirm-btn');
const cancelBtn = dialog.querySelector('#cancel-btn');

openBtn.addEventListener('click', () => openModal(openBtn));
cancelBtn.addEventListener('click', closeModal);
confirmBtn.addEventListener('click', () => {
  deleteItem();
  closeModal();
});

function openModal(trigger) {
  dialog.removeAttribute('hidden');
  dialog._opener = trigger;
  confirmBtn.focus();
  trapFocus(dialog);
  dialog.addEventListener('keydown', handleDialogKey);
}

function closeModal() {
  dialog.setAttribute('hidden', '');
  dialog._opener?.focus();
  dialog.removeEventListener('keydown', handleDialogKey);
}

function handleDialogKey(event) {
  if (event.key === 'Escape') closeModal();
}
```

What `role="dialog"` does: tells screen readers this is a dialog region. Screen readers announce "dialog" when focus enters, and many restrict their virtual cursor to the dialog content.

What `aria-modal="true"` does: tells screen readers to treat the rest of the page as inert. Some screen readers honor this; some do not — which is why you must also implement focus trapping in JavaScript.

### Live regions

`aria-live` tells screen readers to watch a region and announce changes without the user explicitly navigating there. Use it for status messages, error notifications, search results, and loading announcements.

```html
<!-- Polite: waits for the user to finish what they are doing before announcing -->
<div aria-live="polite" id="status-msg"></div>

<!-- Assertive: interrupts immediately — use for time-sensitive errors only -->
<div aria-live="assertive" role="alert" id="error-msg"></div>
```

```js
// Polite announcement — use for: search results count, save confirmation, progress
function announceStatus(message) {
  const status = document.querySelector('#status-msg');
  // Clear first, then set — ensures re-announcement if the message is the same text
  status.textContent = '';
  requestAnimationFrame(() => {
    status.textContent = message;
  });
}

// Assertive announcement — use for: session timeout, critical form errors, destructive action confirmations
function announceError(message) {
  const errorEl = document.querySelector('#error-msg');
  errorEl.textContent = message;
}
```

**`aria-live="polite"`** is almost always the right choice. It waits for the user to finish speaking before announcing the update. Use `aria-live="assertive"` only when the message is genuinely urgent and interrupting is appropriate — not for every error message.

**`role="alert"`** is a shorthand for `aria-live="assertive"` with some additional implied semantics. Use it for critical errors. For routine status messages (e.g., "3 results found"), use `aria-live="polite"` on a plain `div`.

**The empty-then-fill trick** — the `requestAnimationFrame` pattern above forces a DOM update cycle between clearing and setting the text. Without it, if you set the same text twice in a row, some screen readers do not re-announce because the DOM did not change.

The live region container must be in the DOM when the page loads — not inserted dynamically. Screen readers register live regions on page load and watch for changes. If you inject the container later, the watching never starts.

### Tab and accordion patterns

**Tabs** display one panel at a time. The accessible pattern requires `role="tablist"`, `role="tab"`, and `role="tabpanel"` with coordinated ARIA states.

```html
<div role="tablist" aria-label="Product details">
  <button role="tab" aria-selected="true"  aria-controls="panel-desc" id="tab-desc">Description</button>
  <button role="tab" aria-selected="false" aria-controls="panel-specs" id="tab-specs" tabindex="-1">Specifications</button>
  <button role="tab" aria-selected="false" aria-controls="panel-reviews" id="tab-reviews" tabindex="-1">Reviews</button>
</div>

<div id="panel-desc"    role="tabpanel" aria-labelledby="tab-desc">   <!-- visible --> </div>
<div id="panel-specs"   role="tabpanel" aria-labelledby="tab-specs"   hidden> </div>
<div id="panel-reviews" role="tabpanel" aria-labelledby="tab-reviews" hidden> </div>
```

```js
const tabs = document.querySelectorAll('[role="tab"]');

function activateTab(tab) {
  // Deactivate all tabs
  tabs.forEach(t => {
    t.setAttribute('aria-selected', 'false');
    t.setAttribute('tabindex', '-1');
    document.querySelector(`#${t.getAttribute('aria-controls')}`).hidden = true;
  });

  // Activate selected tab
  tab.setAttribute('aria-selected', 'true');
  tab.removeAttribute('tabindex');
  document.querySelector(`#${tab.getAttribute('aria-controls')}`).hidden = false;
  tab.focus();
}

// Arrow keys move between tabs — Tab moves out of the tablist entirely
document.querySelector('[role="tablist"]').addEventListener('keydown', (event) => {
  const current = document.activeElement;
  const tabsArray = [...tabs];
  const index = tabsArray.indexOf(current);

  if (event.key === 'ArrowRight') {
    event.preventDefault();
    activateTab(tabsArray[(index + 1) % tabsArray.length]);
  } else if (event.key === 'ArrowLeft') {
    event.preventDefault();
    activateTab(tabsArray[(index - 1 + tabsArray.length) % tabsArray.length]);
  }
});

tabs.forEach(tab => {
  tab.addEventListener('click', () => activateTab(tab));
});
```

Key details in this pattern:
- Only the active tab is in the natural tab order (`tabindex="-1"` on inactive tabs). This means one Tab keystroke reaches the tablist; arrow keys navigate within it.
- `aria-selected="true"` is on the active tab; `aria-selected="false"` is on all others.
- Each tab panel has `aria-labelledby` pointing to its tab, so screen readers announce the panel's name when focus enters.

**Accordions** use a similar pattern with `aria-expanded` instead of `aria-selected`, since each section can exist independently without mutual exclusion.

```html
<button
  type="button"
  aria-expanded="false"
  aria-controls="section-1-panel"
  id="section-1-btn"
>
  Shipping information
</button>
<div id="section-1-panel" aria-labelledby="section-1-btn" hidden>
  <p>Ships within 3–5 business days...</p>
</div>
```

```js
document.querySelectorAll('.accordion-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    const expanded = btn.getAttribute('aria-expanded') === 'true';
    const panel = document.querySelector(`#${btn.getAttribute('aria-controls')}`);

    btn.setAttribute('aria-expanded', String(!expanded));
    panel.hidden = expanded;
  });
});
```

### Form error patterns

Accessible form errors require three simultaneous changes: visual feedback, ARIA state on the input, and a live announcement.

```html
<label for="email">Email address</label>
<input
  type="email"
  id="email"
  name="email"
  aria-describedby="email-hint email-error"
  autocomplete="email"
>
<span id="email-hint" class="hint">We will not share your email.</span>
<span id="email-error" class="error-msg" aria-live="polite"></span>
```

```js
function showFieldError(inputEl, message) {
  const errorId = `${inputEl.id}-error`;
  const errorEl = document.querySelector(`#${errorId}`);

  inputEl.setAttribute('aria-invalid', 'true');
  errorEl.textContent = message;
  inputEl.classList.add('input--error');
}

function clearFieldError(inputEl) {
  const errorId = `${inputEl.id}-error`;
  const errorEl = document.querySelector(`#${errorId}`);

  inputEl.removeAttribute('aria-invalid');
  errorEl.textContent = '';
  inputEl.classList.remove('input--error');
}
```

`aria-describedby` accepts a space-separated list of IDs. The browser concatenates the text content of all referenced elements and delivers them to the screen reader when the input is focused. This means the hint text and the error message are both read — in order.

**After form submission with errors**, move focus to the first invalid field or to a summary heading at the top of the form:

```js
function handleSubmit(event) {
  event.preventDefault();
  const errors = validateForm(event.target);

  if (errors.length > 0) {
    errors.forEach(({ input, message }) => showFieldError(input, message));

    // Move focus to the first error so keyboard users know where to correct
    errors[0].input.focus();
  } else {
    submitForm(event.target);
  }
}
```

### Contrast and visual accessibility

**Color contrast** — the 4.5:1 ratio for body text is the floor, not the target. Aim higher (7:1 or more) for text on colored backgrounds, small print, and text over images.

For UI components (button borders, focus rings, form field borders), the required ratio is 3:1 against adjacent colors. This applies to non-text elements that convey information.

**Do not rely on color alone** to convey meaning. An error field shown only with a red border fails users with color blindness. Always pair color with a second indicator: an icon, a text label, a pattern, or a shape change.

```css
/* Bad: color is the only indicator of an error */
.input--error {
  border-color: red;
}

/* Good: color + icon-equivalent through text label + border style change */
.input--error {
  border-color: #c00;
  border-width: 2px;
}
/* The visible error message text is the second indicator — not just color */
```

**Motion sensitivity** — the `prefers-reduced-motion` media query lets users opt out of animations. Some users experience nausea, vertigo, or seizures from motion. Always check this query before running transitions or animations.

```css
/* Default: animation enabled */
.modal-overlay {
  animation: fade-in 200ms ease;
}

/* Respect the user's preference */
@media (prefers-reduced-motion: reduce) {
  .modal-overlay {
    animation: none;
  }

  /* Or: replace with an instant state change instead of removing entirely */
  .modal-overlay {
    transition: none;
  }
}
```

In JavaScript, you can read the preference before launching animations:

```js
const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

function openModalWithAnimation(modal) {
  if (prefersReduced) {
    modal.removeAttribute('hidden');
  } else {
    modal.classList.add('modal--entering');
    modal.removeAttribute('hidden');
    modal.addEventListener('animationend', () => {
      modal.classList.remove('modal--entering');
    }, { once: true });
  }
}
```

**Text resizing** — users may increase their browser's default font size to 200% or more. Use relative units (`rem`, `em`, `%`) instead of `px` for font sizes. Ensure layouts do not break at larger text sizes: test by setting your browser's default font size to 20px or 24px and checking for overflow or obscured content.

**Focus visibility** — every focusable element must show a visible focus indicator. The CSS `outline: none` reset without a replacement is a WCAG 2.1 AA failure. Use `:focus-visible` to show focus only during keyboard navigation, so mouse users are not distracted by outlines they do not need:

```css
/* Never just remove the focus outline */
/* button:focus { outline: none; } — do not do this */

/* Correct pattern: visible ring on keyboard focus, hidden on click */
button:focus-visible {
  outline: 3px solid var(--color-brand);
  outline-offset: 3px;
}
```

### Testing strategy: the 3-minute audit

Run this audit before submitting any lab, assignment, or project. It catches the most common failures without requiring a full automated scan.

**Step 1 — Tab through the page (60 seconds).** Starting from the browser address bar, press Tab repeatedly until you have reached every interactive element. Verify: every element is reachable, focus is visible at each stop, the order matches the visual layout, and nothing traps focus unexpectedly outside a modal.

**Step 2 — Test with a screen reader (60 seconds).** Enable VoiceOver (Cmd+F5) or NVDA (Ctrl+Alt+N). Navigate by headings (VoiceOver: VO+Cmd+H; NVDA: H). Verify: there is a logical heading structure, form labels are announced when inputs are focused, buttons announce their purpose, and error messages are read when triggered.

**Step 3 — Run Lighthouse (30 seconds).** Open DevTools → Lighthouse → check Accessibility → Generate report. Aim for 95 or higher. Read each flagged item — Lighthouse flags are specific and actionable.

**Step 4 — Check contrast (30 seconds).** Use the WebAIM Contrast Checker or the DevTools color picker's built-in contrast ratio to verify your primary text, secondary text, and any colored UI components.

The audit does not replace thorough testing — it is a minimum bar before submission. Real user testing with people who use assistive technology is the gold standard.

## Mental model

Think of accessibility as a contract between your code and the browser's accessibility tree. The accessibility tree is a parallel representation of the DOM that assistive technologies read instead of the visual page. Every semantic HTML element you use, every ARIA attribute you set, every label you connect — all of it populates that tree. When the tree accurately reflects the page's structure, state, and relationships, assistive technologies can convey it faithfully to their users.

Your job is to keep three things synchronized: the **visual state** (what sighted users see), the **DOM state** (the HTML), and the **accessibility tree state** (what assistive technologies read). When a modal opens visually, the DOM must change (remove `hidden`), and the ARIA state must change (`aria-expanded`, `aria-modal`). When a field has an error, the visual style changes, the DOM content changes (error text), and the ARIA state changes (`aria-invalid`). All three must move together, every time.

## Working habits

- Write semantic HTML first. `<button>`, `<nav>`, `<main>`, `<fieldset>`, `<label>` — these give you accessibility for free. Reach for ARIA only when a native element cannot express the pattern you need.
- Place `aria-live` regions in the HTML at page load — not in JavaScript. The browser registers live regions on load; dynamically inserted containers are not watched.
- Test keyboard behavior as you build a feature, not after. Adding keyboard support retroactively is harder than building it in from the start.
- Every programmatic `focus()` call should have a paired return — if you move focus somewhere, plan where it goes when the user is done there.
- Use the Accessibility tab in DevTools (or the full accessibility tree view in Chrome's Elements panel) to inspect computed roles, names, and states as you work.
- Respect system preferences: `prefers-reduced-motion`, `prefers-color-scheme`. These are user choices, not hints.
- Write error messages that explain the problem and the fix: "Email address is required" is better than "Invalid input." "Password must be at least 8 characters" is better than "Password too short."

## Common mistakes

- **Removing focus styles without replacement**: `button:focus { outline: none; }` is a WCAG failure. Always provide a `:focus-visible` replacement.
- **Using `aria-live` on dynamically injected containers**: the container must be in the DOM at page load. Inserting `<div aria-live="polite">` via JavaScript and then populating it does not work reliably.
- **Setting `aria-hidden="true"` on a focused element**: if a user focuses an element and you then hide it from the accessibility tree with `aria-hidden`, screen readers receive contradictory information. Never `aria-hidden` an element that can receive focus.
- **Forgetting to return focus when a modal closes**: after closing a dialog, focus is lost to the document body. The user has to Tab from the beginning. Always return focus to `modal._opener`.
- **Using `tabindex` values greater than 0**: positive `tabindex` values override the natural document order and create a confusing tab sequence. Only use `tabindex="0"` (add to natural order) or `tabindex="-1"` (programmatically focusable only).
- **Relying on `aria-label` to fix non-semantic markup**: if you have `<div class="btn" aria-label="Submit">Submit</div>`, the right fix is `<button type="button">Submit</button>` — not adding more ARIA to a non-interactive element. ARIA cannot add keyboard behavior or native form association.
- **Assertive live regions for routine updates**: `aria-live="assertive"` interrupts whatever the screen reader is currently saying. Using it for search results, status updates, or loading messages is disruptive. Reserve it for genuinely urgent announcements.
- **Missing `aria-selected` on inactive tabs**: both the active tab (`aria-selected="true"`) and inactive tabs (`aria-selected="false"`) must have the attribute. Omitting it from inactive tabs leaves screen reader users uncertain about the current state.
- **Animating without checking `prefers-reduced-motion`**: animations that play regardless of user settings can cause physical symptoms for some users. Always include a `prefers-reduced-motion: reduce` override in your CSS.

## Practice prompt

Build a small accessible product detail page with three interactive components: a tab widget, a modal confirmation dialog, and a contact form with validation.

1. Create the tab widget with three panels ("Description", "Specifications", "Reviews"). Implement `role="tablist"`, `role="tab"`, `role="tabpanel"`, `aria-selected`, and arrow-key navigation. Verify that Tab enters the tablist, arrow keys move between tabs, and Tab again moves focus out of the tablist into the first panel.
2. Add a "Request a quote" button that opens a modal dialog. The modal must have `role="dialog"`, `aria-modal="true"`, `aria-labelledby` pointing to the dialog heading, and an Escape key listener that closes it. Implement focus trapping so Tab and Shift+Tab cycle only inside the dialog. When the modal closes, return focus to the trigger button.
3. Add a contact form with Name, Email, and Message fields. Each field must have a `<label>`, an `aria-describedby` pointing to an error `<span>`. Validate on submit: show errors via `showFieldError()`, set `aria-invalid="true"`, and move focus to the first invalid field. On success, display a confirmation message in an `aria-live="polite"` container.
4. Add a `prefers-reduced-motion` CSS block that disables all transitions and animations.
5. Run the 3-minute audit: tab through the page, test a heading and form with VoiceOver or NVDA, run Lighthouse, and check contrast on your primary text color.

## Reflection

When you implemented focus trapping, what did you discover about the tab order of elements inside your dialog? Were there any elements you expected to be focusable that were not, or vice versa? What happened in the screen reader when you triggered a form validation error — was the error announced immediately, or did you have to navigate to it? What changed in the Lighthouse score between your first implementation and after you added all the ARIA attributes and labels?

## Vocabulary

- **WCAG** — Web Content Accessibility Guidelines; the international standard for web accessibility, organized around the four principles: Perceivable, Operable, Understandable, Robust
- **conformance level** — a tier of WCAG requirements: A (minimum), AA (professional standard), AAA (enhanced)
- **accessibility tree** — the browser's parallel representation of the DOM that assistive technologies read; populated by semantic HTML and ARIA attributes
- **focus management** — the practice of programmatically moving keyboard focus to the correct element when UI state changes (modal opens, content loads, route changes)
- **focus trap** — a keyboard behavior that constrains Tab navigation to a defined region (required inside open modals)
- **tabindex** — an HTML attribute controlling whether and how an element participates in keyboard focus: `0` adds it to the natural order; `-1` makes it programmatically focusable only; positive values should never be used
- **aria-live** — an ARIA attribute that causes a region's content changes to be announced by screen readers; `"polite"` waits for the user to finish; `"assertive"` interrupts immediately
- **role="dialog"** — an ARIA role that identifies an element as a dialog region; paired with `aria-modal`, `aria-labelledby`, and focus management
- **aria-modal** — an ARIA attribute that tells assistive technologies to treat the rest of the page as inert while the dialog is open
- **aria-selected** — an ARIA attribute indicating which option in a selection widget (tabs, listbox) is currently active
- **aria-expanded** — an ARIA attribute indicating whether a collapsible region (accordion, dropdown, disclosure) is currently open
- **aria-invalid** — an ARIA attribute indicating that an input's current value does not pass validation
- **aria-describedby** — an ARIA attribute that points to one or more elements whose text content describes the current element (used to connect inputs to their hint text and error messages)
- **role="tablist" / role="tab" / role="tabpanel"** — the ARIA role triad for a tab widget; establishes the semantic relationship between the tab navigation and the associated content panels
- **prefers-reduced-motion** — a CSS media query that reflects the user's operating system preference to minimize motion; use it to disable or simplify animations
- **contrast ratio** — a numeric measure of luminance difference between a foreground color and its background; WCAG AA requires 4.5:1 for normal text and 3:1 for large text and UI components

## Mini checklist

- I can explain the difference between WCAG conformance levels A, AA, and AAA and describe what AA requires in practice.
- I can implement a focus trap in JavaScript that constrains Tab and Shift+Tab navigation to the contents of an open modal dialog.
- I can open and close a modal dialog with correct focus management: focus moves into the dialog on open and returns to the trigger on close.
- I can build an accessible tab widget using `role="tablist"`, `role="tab"`, `role="tabpanel"`, `aria-selected`, and arrow-key keyboard navigation.
- I can build an accessible accordion using `aria-expanded`, `aria-controls`, and `hidden` panel toggling.
- I can implement accessible form error patterns with `aria-invalid`, `aria-describedby`, and `aria-live` so errors are announced to screen readers.
- I can explain the difference between `aria-live="polite"` and `aria-live="assertive"` and choose the correct one for a given situation.
- I can write a `prefers-reduced-motion` media query that disables animations for users who have requested reduced motion.
- I can perform a 3-minute manual accessibility audit: keyboard tab test, basic screen reader test, Lighthouse scan, and contrast check.
- I can explain why positive `tabindex` values, `aria-hidden` on focused elements, and dynamically injected live regions are accessibility anti-patterns.
