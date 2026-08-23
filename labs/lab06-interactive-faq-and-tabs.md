# Lab 06 – Interactive FAQ and Tabs

## Purpose

DOM manipulation is most visible when it controls what users can see. This lab focuses on two of the most common interface patterns — accordions and tabs — and asks you to implement them correctly using class toggling, event delegation, and accessible markup.

## Skills practiced

- Selecting elements with `querySelector` and `querySelectorAll`
- Toggling CSS classes with `classList.toggle`, `.add`, `.remove`
- Using event delegation on a parent element
- Reading `event.target` and traversing the DOM with `.closest()`
- Adding `aria-expanded` and `aria-controls` for accessible disclosure patterns
- Creating tab panels with correct ARIA roles
- Implementing roving tabindex and arrow-key navigation for a tablist

## What you're building

A **Campus Services** help page with two sections:
1. An **accordion FAQ** — clicking a question reveals the answer; clicking again collapses it; only one answer is open at a time
2. A **tabbed panel** — three tabs that switch between content panels; only the active panel is visible

---

## Part 1: Accordion FAQ

### HTML

Create `labs/lab06/index.html`. The FAQ section should follow this structure:

```html
<section class="faq">
  <h2>Frequently Asked Questions</h2>

  <div class="faq-item">
    <button class="faq-question" aria-expanded="false" aria-controls="faq-answer-1">
      How do I register for classes?
    </button>
    <div class="faq-answer" id="faq-answer-1" hidden>
      <p>Log in to the student portal and navigate to Registration...</p>
    </div>
  </div>

  <div class="faq-item">
    <button class="faq-question" aria-expanded="false" aria-controls="faq-answer-2">
      Where is the financial aid office?
    </button>
    <div class="faq-answer" id="faq-answer-2" hidden>
      <p>The financial aid office is located in the Shepherd Union...</p>
    </div>
  </div>

  <!-- Add at least 4 more FAQ items total (6 minimum) -->
</section>
```

Key attributes:
- `aria-expanded="false"` on the button — updated by JavaScript when opened
- `aria-controls` points to the `id` of the answer panel
- `hidden` attribute on answer panels — CSS will reveal them when the `hidden` attribute is removed

### CSS

```css
.faq-answer[hidden] {
  display: none;
}

.faq-question[aria-expanded="true"] {
  /* style the open state — e.g., different background, arrow rotation */
}
```

### JavaScript

Write a function `initFaq(faqContainer)` that:

1. Adds a single `click` listener to `faqContainer` (event delegation)
2. When a click is detected, checks if `event.target.matches('.faq-question')`
3. Finds all other open questions and closes them (removes the `hidden` attribute trick: toggle `hidden` on the answer div, set `aria-expanded` to the correct string)
4. Toggles the clicked question open or closed

Specifically, for the clicked button:
- Toggle `aria-expanded` between `"true"` and `"false"` (as strings — ARIA attributes are always strings)
- Toggle the `hidden` attribute on the associated answer panel (use `answerEl.hidden = !answerEl.hidden` or `toggleAttribute('hidden')`)

For all *other* questions: set `aria-expanded="false"` and `hidden = true` (only one answer open at a time).

---

## Part 2: Tabbed panel

### HTML

```html
<section class="tabs-section">
  <h2>Campus Resources</h2>

  <div class="tab-list" role="tablist" aria-label="Campus resources">
    <button role="tab" aria-selected="true"  aria-controls="panel-library" id="tab-library" tabindex="0">
      Library
    </button>
    <button role="tab" aria-selected="false" aria-controls="panel-gym" id="tab-gym" tabindex="-1">
      Recreation Center
    </button>
    <button role="tab" aria-selected="false" aria-controls="panel-dining" id="tab-dining" tabindex="-1">
      Dining
    </button>
  </div>

  <div role="tabpanel" id="panel-library" aria-labelledby="tab-library">
    <h3>Library Hours</h3>
    <p>Monday–Friday: 7am–10pm...</p>
  </div>

  <div role="tabpanel" id="panel-gym" aria-labelledby="tab-gym" hidden>
    <h3>Recreation Center</h3>
    <p>Open daily 6am–11pm...</p>
  </div>

  <div role="tabpanel" id="panel-dining" aria-labelledby="tab-dining" hidden>
    <h3>Dining Locations</h3>
    <p>Three dining halls on campus...</p>
  </div>
</section>
```

### JavaScript

Write a function `initTabs(tabListContainer)` that handles **both** mouse and keyboard.

**Click behaviour**

1. Add a `click` listener to `tabListContainer`
2. When a `[role="tab"]` button is clicked:
   - Set `aria-selected="false"` on all tab buttons
   - Hide all tab panels (set `hidden = true`)
   - Set `aria-selected="true"` on the clicked tab
   - Show the panel whose `id` matches `event.target.getAttribute('aria-controls')` (remove `hidden`)

**Keyboard behaviour — roving tabindex**

Because these buttons carry `role="tab"` inside a `role="tablist"`, they are one composite widget, not three separate buttons. Assistive technology users expect one Tab press to enter the tablist, arrow keys to move between tabs, and the next Tab press to leave. See the roving-tabindex section of the Week 06 lecture notes for the reasoning and the full pattern.

3. Keep exactly one tab in the tab order: the selected tab gets `tabIndex = 0`, every other tab gets `tabIndex = -1`. Update this every time the selection changes — including on click.
4. Add a `keydown` listener to `tabListContainer`. On `ArrowRight` / `ArrowLeft`, move the selection one tab forward or backward and wrap around at the ends. On `Home` / `End`, jump to the first or last tab.
5. Call `event.preventDefault()` when you handle an arrow key, so the page does not scroll.
6. Call `.focus()` on the newly selected tab, so focus and selection stay together.

Factor the shared work into one `selectTab(index)` helper and call it from both the click and the keydown paths — the two should not have separate copies of the logic.

**Do not apply roving tabindex to the accordion in Part 1.** Each accordion header is an independent toggle, so all of them stay in the natural tab order.

### CSS

```css
[role="tabpanel"][hidden] {
  display: none;
}

[role="tab"][aria-selected="true"] {
  /* active tab styling */
}
```

---

## Part 3: Call both initializers

At the bottom of your script (or in a `DOMContentLoaded` handler):

```js
initFaq(document.querySelector('.faq'));
initTabs(document.querySelector('.tab-list'));
```

---

## Testing requirements

Test each behavior manually:

**Accordion:**
- [ ] Clicking a question opens its answer
- [ ] Clicking the same question again closes it
- [ ] Opening a second question automatically closes the first
- [ ] `aria-expanded` reflects the correct state in the Elements panel
- [ ] All buttons are keyboard-reachable and activatable with Enter/Space

**Tabs:**
- [ ] Clicking each tab shows that panel and hides the others
- [ ] `aria-selected` updates correctly in the Elements panel
- [ ] One Tab press moves focus into the tablist; the next Tab press moves out of it entirely
- [ ] Left/Right arrow keys move between tabs and wrap around at both ends
- [ ] Home and End jump to the first and last tab
- [ ] Exactly one tab has `tabindex="0"` at any moment; the others are `-1` (check in the Elements panel)
- [ ] Arrow keys do not scroll the page while focus is in the tablist

---

## Deliverable

In `labs/lab06/`:
- `index.html`
- `lab06.js`
- `style.css`
- `notes.md`

Commit at least twice (after each component). Push and deploy.

Submit to Canvas: live URL, repo URL, notes.md link.

---

## Process reflection (in notes.md)

Answer in 4–6 sentences:
- Why is event delegation better than adding a click listener to each individual button?
- What does `aria-expanded` communicate, and to whom?
- What would break if you used `display: none` in JavaScript directly instead of toggling the `hidden` attribute and controlling visibility through CSS?
- Why does the tablist use roving tabindex while the accordion does not?

---

## Rubric

| Criterion | Excellent (4) | Proficient (3) | Developing (2) | Incomplete (1) |
|-----------|--------------|----------------|----------------|----------------|
| **Accordion behavior** | Open/close works; only one panel open at a time; `aria-expanded` accurate | Open/close works; multiple panels can open simultaneously | Open works; close doesn't | Not functional |
| **Tab behavior** | Tabs switch panels correctly; all three panels reachable; `aria-selected` accurate | Tabs switch; ARIA not updated | Partially working | Not functional |
| **ARIA attributes** | `aria-expanded`, `aria-controls`, `aria-selected`, `role="tab"`, `role="tabpanel"` all present and accurate, and `tabindex` reflects the selected tab | Most ARIA present | Some ARIA present | No ARIA |
| **Event delegation** | One listener per component on a parent; `event.target.matches()` or `.closest()` used | Two listeners per component | Individual listeners on each button | No event delegation |
| **Keyboard accessibility** | Accordion headers reachable by Tab and activatable by Enter/Space; tablist uses roving tabindex with working Left/Right (and Home/End) arrow navigation | Both components keyboard-operable; arrow navigation present but incomplete (no wrap, or no Home/End) | Everything reachable by Tab, but the tablist has no arrow-key navigation | Not tested |
| **Reflection** | Specific; addresses all three prompts | Two prompts addressed | Vague | Missing |
