# Week 07 Lecture Notes: Event Listeners, Validation, and UX Feedback

## Weekly focus

Making pages respond to user actions through event listeners, and giving users clear, accessible feedback when form input is invalid.

## Why this matters

Static pages with hardcoded content represent only a fraction of the web. Everything that responds to a user — a search field that filters results as you type, a form that shows an error message before submission, a button that expands a section — is powered by event listeners. Form validation done in JavaScript, paired with ARIA live regions, is the difference between a form that silently rejects input and one that clearly explains what went wrong and where. That distinction is the foundation of usable, accessible interfaces.

## Learning targets

- Attach event listeners to elements using `addEventListener` for `click`, `submit`, `input`, `change`, `blur`, and `keydown` events
- Prevent the browser's default behavior with `event.preventDefault()` and explain when that is necessary
- Read the element that triggered an event using `event.target` and its properties
- Implement event delegation so a single listener handles events from many child elements
- Write client-side form validation with both HTML constraint attributes and custom JavaScript messages
- Use `aria-invalid`, `aria-describedby`, and `aria-live` to communicate validation state to screen readers

## Core concepts

### addEventListener

`addEventListener(type, handler)` attaches a function to an element that runs whenever the named event fires. It does not replace existing listeners the way the old `onclick` property does.

```js
const btn = document.querySelector("#submit-btn");

btn.addEventListener("click", function (event) {
  console.log("Clicked!", event.target);
});
```

Common event types and when to use them:

| Event | Fires when |
|-------|------------|
| `click` | User clicks or activates with Enter/Space |
| `submit` | Form is submitted (button click or Enter in a field) |
| `input` | Value of an input changes (every keystroke) |
| `change` | Value changes and the element loses focus |
| `blur` | Element loses focus (good for validate-on-leave) |
| `keydown` | Any key is pressed; check `event.key` for which one |

### event.preventDefault()

The browser has built-in default behaviors: clicking a submit button sends a form to a server (and reloads the page), clicking an anchor navigates to a URL. Call `event.preventDefault()` inside a `submit` listener to stop the reload so your JavaScript validation can run first.

```js
const form = document.querySelector("#signup-form");

form.addEventListener("submit", (event) => {
  event.preventDefault(); // stop the page reload

  const email = document.querySelector("#email").value.trim();
  if (!email.includes("@")) {
    showError("email", "Please enter a valid email address.");
    return;
  }

  // Only reach here if all validation passes
  console.log("Form is valid, ready to send:", email);
});
```

### event.target

`event.target` is the element that the event originated from. This is especially useful when one listener handles multiple elements, because `event.target` tells you exactly which one was interacted with.

```js
document.querySelector("#product-list").addEventListener("click", (event) => {
  const btn = event.target.closest("button[data-product-id]");
  if (!btn) return; // click was not on a product button

  const id = Number(btn.dataset.productId);
  console.log("Selected product id:", id);
});
```

`event.target` vs `event.currentTarget`: `event.target` is where the event started. `event.currentTarget` is the element the listener is attached to. When using delegation (see below), these are different elements.

### Event delegation

Attaching one listener to a parent element instead of many listeners to individual children is called event delegation. It works because events bubble up the DOM tree from the target to the root. Delegation is more efficient and handles dynamically added children automatically.

```js
// Without delegation — fragile, does not work for items added later
document.querySelectorAll(".delete-btn").forEach(btn => {
  btn.addEventListener("click", handleDelete);
});

// With delegation — one listener, works for any .delete-btn in the list
document.querySelector("#task-list").addEventListener("click", (event) => {
  if (event.target.matches(".delete-btn")) {
    const listItem = event.target.closest("li");
    listItem.remove();
  }
});
```

Use `.matches(selector)` to check if `event.target` is the element you care about. Use `.closest(selector)` to walk up the tree to the nearest ancestor matching a selector.

### Form validation: HTML constraints and custom messages

HTML provides built-in validation attributes: `required`, `type="email"`, `minlength`, `maxlength`, `min`, `max`, and `pattern`. These run automatically on submit and work without JavaScript, so always include them as a baseline.

For richer feedback — error messages that appear next to the field, not just a browser tooltip — add JavaScript validation on top. The Constraint Validation API gives you `input.validity` and `input.setCustomValidity()`.

```js
const passwordInput = document.querySelector("#password");

passwordInput.addEventListener("blur", () => {
  if (passwordInput.value.length < 8) {
    passwordInput.setCustomValidity("Password must be at least 8 characters.");
    showError("password", "Password must be at least 8 characters.");
  } else {
    passwordInput.setCustomValidity(""); // clear the error
    clearError("password");
  }
});
```

### aria-invalid, aria-describedby, and aria-live

HTML validation attributes alone do not communicate errors to screen reader users as clearly as they could. Three ARIA attributes bridge that gap.

`aria-invalid="true"` signals to screen readers that the field currently has an invalid value. Set it in JavaScript when you show an error, remove it when the error clears.

`aria-describedby` links a field to an element that describes it — typically the error message container. The screen reader reads the description after the label and role.

`aria-live="polite"` on a region tells the screen reader to announce changes to that region as they happen, without interrupting the current reading position. Use this for error message containers.

```js
function showError(fieldId, message) {
  const field = document.querySelector(`#${fieldId}`);
  const errorEl = document.querySelector(`#${fieldId}-error`);

  field.setAttribute("aria-invalid", "true");
  errorEl.textContent = message;
  // aria-live="polite" on the error element triggers announcement
}

function clearError(fieldId) {
  const field = document.querySelector(`#${fieldId}`);
  const errorEl = document.querySelector(`#${fieldId}-error`);

  field.removeAttribute("aria-invalid");
  errorEl.textContent = "";
}
```

The HTML structure that makes this work:

```html
<label for="email">Email address</label>
<input
  type="email"
  id="email"
  required
  aria-describedby="email-error"
/>
<p id="email-error" aria-live="polite" class="field-error"></p>
```

### Focus management

After a dynamic action — especially showing an error summary or opening a modal — move keyboard focus to the relevant element so keyboard and screen reader users are not left behind. Use `element.focus()` to do this.

```js
form.addEventListener("submit", (event) => {
  event.preventDefault();
  const errors = validate();

  if (errors.length > 0) {
    const summary = document.querySelector("#error-summary");
    summary.textContent = `${errors.length} error(s) found. Please correct them.`;
    summary.focus(); // move focus to the summary so it is announced
  }
});
```

For `focus()` to work, the element must be focusable. If it is not an interactive element (`<button>`, `<input>`, etc.), add `tabindex="-1"` to it in HTML.

## Common mistakes

1. **Forgetting `event.preventDefault()` on a form submit listener.** The page reloads before your validation runs. The fix is always the first line inside a submit handler.
2. **Attaching listeners inside a loop without delegation.** Students often do `querySelectorAll(".btn").forEach(btn => btn.addEventListener(...))` and then add new buttons dynamically. The new buttons have no listener. Use delegation instead.
3. **Checking `event.target` without a guard.** `event.target` is whatever was clicked inside the parent — possibly a `<span>` inside the `<button>`, not the button itself. Use `event.target.closest("button")` to safely walk up to the intended element.
4. **Setting `aria-invalid` without an associated error message.** Marking a field invalid without explaining why is worse than saying nothing. Always pair `aria-invalid="true"` with a visible, linked error message.
5. **Running validation only on submit.** If a user fills out ten fields and submits once, seeing ten errors at once is overwhelming. Add `blur` listeners to validate each field when the user leaves it so errors surface one at a time.

## Accessibility connection

Event-driven validation is one of the highest-impact areas for accessibility in front-end development. WCAG Success Criterion 3.3.1 requires that input errors be identified and described to the user in text — `aria-live` regions and `aria-describedby` are the technical implementation of that requirement. Focus management after form submission or error display is required by 2.4.3 (Focus Order) so that keyboard users are not stranded at a submit button after errors appear. Getting these right in Week 07 means your Project 1 form will meet real accessibility standards, not just pass visual inspection.

## Demo walkthrough

**Demo: Accessible Signup Form with Live Validation**

1. Build an HTML form with three fields: username (minlength 3), email (type email, required), and password (minlength 8). Each field has a `<p aria-live="polite">` error container below it linked via `aria-describedby`.
2. In `demo-07.js`, write `showError(fieldId, message)` and `clearError(fieldId)` helper functions that set/remove `aria-invalid` and update `textContent` of the error container.
3. Attach `blur` listeners to each field. On blur, validate the field's value and call `showError` or `clearError` accordingly.
4. Attach a `submit` listener to the form. Call `event.preventDefault()`. Run all three validations. If any fail, move focus to the first invalid field.
5. If all fields pass, hide the form, create a separate success `<div role="alert" tabindex="-1">`, set its `textContent`, append it next to the form, and move focus to that success message.
6. Use a screen reader (macOS VoiceOver: Cmd+F5) to demonstrate that the live region announces errors without the student having to navigate to them manually.

## Practice prompt

Build a contact form with Name, Email, and Message fields. Requirements: (1) validate each field on `blur` and show a specific error message next to the field using `aria-describedby` and `aria-live="polite"`, (2) prevent submission if any field is invalid, (3) use event delegation on a button group (three preset subject buttons: "Question", "Feedback", "Bug Report") so only one listener handles all three, storing the selection in a `dataset` attribute, and (4) on successful submission, display a `<div role="alert">` confirmation message and move focus to it.

## Bridge

Lab 07 is Accessible Form Validation — it is a direct application of everything in this lecture, so the `showError`/`clearError` pattern from the demo is a strong starting point. Quiz 4 will ask you to trace through event delegation code and predict which element `event.target` refers to in different click scenarios. Project 1 Build begins this week: if your project includes any form or interactive UI, the patterns here — `addEventListener`, `event.preventDefault`, and live ARIA regions — are the core tools you will reach for throughout the build.
