# Accessibility Fundamentals Primer

**Read this before Week 2.** Accessibility is a foundational professional practice in web development — not an optional add-on addressed at the end of a project. This primer establishes the vocabulary and mindset you will use throughout this course.

---

## Why accessibility matters

The web is used by people with a wide range of abilities:

- People who are blind or have low vision use **screen readers** (software that reads page content aloud and responds to keyboard navigation)
- People with motor disabilities may use a **keyboard only** and cannot use a mouse
- People with color blindness or low contrast sensitivity need sufficient **color contrast** to distinguish text from backgrounds
- People with cognitive disabilities benefit from clear, predictable **language and structure**

Approximately 15–20% of the global population has some form of disability. Beyond the moral and ethical case, there is a legal one: in the United States, the Americans with Disabilities Act (ADA) and Section 508 of the Rehabilitation Act apply to web content; similar legislation exists in the EU, Canada, and Australia. Inaccessible websites have resulted in successful lawsuits against major companies.

Making something accessible usually improves it for everyone. Clear labels help all users. Good keyboard support helps power users who prefer not to use a mouse. High color contrast helps anyone viewing a screen in bright sunlight.

---

## The four WCAG principles

The **Web Content Accessibility Guidelines (WCAG)** are the international standard for web accessibility. They organize requirements under four principles — a useful mental checklist for any feature you build:

| Principle | Question to ask yourself |
|---|---|
| **Perceivable** | Can every user perceive the content, regardless of their sensory abilities? (Images have alt text; videos have captions; color is not the only indicator of meaning) |
| **Operable** | Can every user operate all controls, regardless of input device? (Everything keyboard-reachable; no timed interactions that cannot be extended; no flashing content) |
| **Understandable** | Is the content and behavior predictable and clear? (Labels on forms; error messages that explain the problem; consistent navigation) |
| **Robust** | Does the content work with current and future assistive technologies? (Valid HTML; ARIA attributes used correctly; no assumptions about the user's device or software) |

WCAG defines three conformance levels: **A** (minimum), **AA** (the legal and professional standard), and **AAA** (enhanced). This course targets WCAG 2.1 Level AA.

---

## Common failures — and how to avoid them

These are the most frequently cited accessibility failures on the web. Every one of them can be avoided with small, intentional choices:

### 1. Missing or unhelpful image alt text

Every `<img>` must have an `alt` attribute. The value should describe what the image communicates, not just what it depicts:

```html
<!-- Bad: empty or generic -->
<img src="chart.png" alt="image">

<!-- Good: describes the content and meaning -->
<img src="chart.png" alt="Bar chart showing enrollment growth from 1,200 students in 2020 to 2,400 in 2025">

<!-- Decorative images: empty alt tells screen readers to skip it -->
<img src="divider.svg" alt="">
```

### 2. Unlabeled form inputs

Every input must have a visible `<label>` element connected via `for`/`id`. A placeholder is not a label — it disappears when the user starts typing.

```html
<!-- Bad: label missing -->
<input type="email" placeholder="Email">

<!-- Good: visible label, connected by for/id -->
<label for="email">Email address</label>
<input type="email" id="email" placeholder="you@example.com">
```

### 3. Insufficient color contrast

Text must have a contrast ratio of at least **4.5:1** against its background for normal text, and **3:1** for large text (18pt / 24px or bold 14pt / ~19px). Use the [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/) to verify.

```css
/* Brand blue on white — check this! */
/* #2563eb on #ffffff = 5.9:1 — passes AA */
color: #2563eb;
background-color: #ffffff;

/* Light grey on white — common failure */
/* #aaaaaa on #ffffff = 2.3:1 — fails AA */
color: #aaaaaa;
```

### 4. No keyboard access for interactive elements

Every control a mouse user can click, a keyboard user must be able to reach with **Tab** and activate with **Enter** or **Space**. Custom interactive elements (dropdowns, carousels, dialogs) require careful implementation. Use native HTML elements (`<button>`, `<a>`, `<input>`, `<select>`) wherever possible — they have keyboard support built in.

```html
<!-- Bad: div used as button — not keyboard-reachable -->
<div onclick="submit()">Submit</div>

<!-- Good: native button -->
<button type="button" onclick="submit()">Submit</button>
```

### 5. Missing focus styles

Keyboard users need to see which element is focused. Browsers provide a default outline, but many designs remove it with `outline: none` without providing an alternative. Always provide a visible `:focus-visible` style.

```css
/* Bad: removes focus without replacement */
button:focus { outline: none; }

/* Good: custom focus style that is visible */
button:focus-visible {
  outline: 3px solid var(--color-brand);
  outline-offset: 2px;
}
```

---

## ARIA: when and why

**ARIA (Accessible Rich Internet Applications)** is a set of HTML attributes that communicate widget roles, states, and properties to assistive technologies. ARIA fills the gap for patterns that have no native HTML equivalent.

**The first rule of ARIA:** If a native HTML element already conveys the meaning you need, use it. ARIA is for cases where you must build a custom widget.

Common ARIA attributes you will use in this course:

| Attribute | Purpose | Example |
|---|---|---|
| `aria-label` | Labels an element when no visible text label is possible | `<button aria-label="Close dialog">✕</button>` |
| `aria-expanded` | Indicates whether a collapsible element is open or closed | `<button aria-expanded="false">Menu</button>` |
| `aria-controls` | Points to the element controlled by a button | `<button aria-controls="menu-panel">` |
| `aria-live` | Makes a region announce updates to screen readers | `<div aria-live="polite" id="results">` |
| `aria-invalid` | Marks an input as having an invalid value | `<input aria-invalid="true">` |
| `aria-describedby` | Points to an element that describes the current element | `<input aria-describedby="email-error">` |

---

## Accessibility throughout this course

You will encounter accessibility requirements in every major assessment:

- **Labs 02–13:** Semantic HTML, form labels, ARIA states, keyboard navigation, screen reader announcements
- **Assignment 2:** `aria-invalid`, `aria-describedby`, `aria-live` on a form
- **Assignment 3:** Full ARIA roles on accordion, tabs, and live filter patterns
- **Lab 13:** Full Lighthouse accessibility audit and screen reader testing
- **All projects:** Rubric criteria for keyboard operability, ARIA correctness, and color contrast

The screen reader testing guide (`course/screen-reader-testing-guide.md`) gives step-by-step instructions for testing with VoiceOver (macOS) and NVDA (Windows).

---

## Quick reference checklist

Use this before submitting any lab or assignment:

- [ ] Every `<img>` has an `alt` attribute (empty `""` for decorative images)
- [ ] Every form input has a connected `<label>` element
- [ ] Color contrast is at least 4.5:1 for body text (verified with a checker)
- [ ] All interactive elements are reachable and operable by keyboard
- [ ] Focus styles are visible on all interactive elements
- [ ] No `<div>` or `<span>` used as a button or link
- [ ] Dynamic regions that update have `aria-live="polite"`
- [ ] Error messages are connected to their inputs with `aria-describedby`
