# Assignment 6 – Reactive Form Workflow

**Due:** End of Week 13
**Weight:** One of six assignments (20% combined)
**Skills:** Vue 3 Composition API, `ref`, `computed`, `v-model`, `v-if`, component decomposition, reactive form validation, accessible state communication

---

## Overview

You will build a **multi-step form workflow** in Vue 3 that guides a user through a sequence of inputs, validates each step, previews the submitted data before final confirmation, and provides clear, accessible feedback throughout. No page navigation — all steps happen within a single Vue application.

This is the most complex individual assignment in the course. It requires you to coordinate reactive state across components, manage which step is visible, validate before advancing, and ensure that assistive technology users receive the same information as sighted users.

If Vue still feels new, use the [Vue Transition Guide](../course/vue-transition-guide.md) while you build. This assignment goes much better when you treat it as a repeatable parent/child pattern instead of one giant interface.

## Build order that keeps this manageable

Use this sequence. It is the fastest path to a working submission.

1. Build `App.vue`, `StepIndicator.vue`, and `Step1.vue` first. Hard-code `currentStep` if needed until Step 1 can render and advance.
2. Add one shared form-data object in `App.vue` and make Step 1 emit its data upward on "Next."
3. Create `ReviewStep.vue` early, even if it only shows two or three fields at first. Seeing data arrive in the review step makes the rest of the assignment easier to reason about.
4. Add `Step2.vue` and `Step3.vue` by repeating the same pattern: local inputs, validation, emit upward, parent changes the visible step.
5. Add focus management, `aria-live`, and the success/reset flow after the step transitions are stable.
6. Only after the baseline works should you consider stretch work such as `localStorage`, progress percentage, or transitions.

## Minimum viable path

If you start to feel overloaded, protect these requirements first:

- one parent component owns the workflow state
- each step validates before advancing
- the review step shows the collected data clearly
- focus moves when the step changes
- errors are linked to the correct fields

Do not spend your best time on animation or visual polish before these are working.

---

## Scenario

Choose **one** of the following multi-step form contexts, or propose your own with instructor approval:

- **Event registration** — attendee info → session selection → dietary/accessibility preferences → review and confirm
- **Campus club application** — personal info → skills/interests → availability → review and confirm
- **Volunteer sign-up** — contact info → opportunity selection → scheduling preferences → review and confirm
- **Course feedback survey** — course rating → instructor feedback → suggestions → review and submit

All workflows must have exactly **three input steps plus one review step** (four steps total).

---

## What to build

### Application structure

```
assignments/assignment-6/
  src/
    App.vue             ← manages step state and overall layout
    components/
      StepIndicator.vue ← shows current step (e.g., "Step 2 of 4")
      Step1.vue         ← first input step
      Step2.vue         ← second input step
      Step3.vue         ← third input step
      ReviewStep.vue    ← displays all collected data for confirmation
      SuccessView.vue   ← shown after final submission
```

### App.vue responsibilities
- Owns the `currentStep` ref (1–4, or a named state: `'step1' | 'step2' | 'step3' | 'review' | 'success'`)
- Owns the collected form data object (updated as each step emits its data)
- Conditionally renders the correct step component with `v-if` / `v-else-if`
- Passes collected data to `ReviewStep` as props

### Each input step (Step1, Step2, Step3)
- Has its own local form state managed with `v-model` bound to `ref()` values
- Validates its own fields before emitting
- Emits a `'next'` event with its data when the user advances (do not mutate props)
- Emits a `'back'` event when the user goes back (no data needed)
- Shows inline validation errors for required fields

### ReviewStep
- Receives all collected data as props
- Displays each field and its value in a readable summary (use a definition list `<dl>` or a structured table)
- Has a "Submit" button that emits a `'submit'` event to the parent

### SuccessView
- Displayed after final submission
- Thanks the user and summarizes what was submitted (at minimum their name or primary identifier)
- Includes a "Start over" button that resets `currentStep` to 1 and clears form data

### StepIndicator
- Receives `currentStep` and `totalSteps` as props
- Renders a visible step indicator ("Step 2 of 4" or a progress bar)
- Has `aria-label="Form progress"` and communicates current step to screen readers

---

## Validation requirements

Each step must validate before allowing the user to advance. Required validations:

**Step 1** (contact/personal information):
- Name field: non-empty
- Email field: contains `@` and `.`
- At minimum one other required field of your choosing

**Step 2** (selection step):
- At least one item must be selected (radio, checkbox group, or dropdown)

**Step 3** (preference/scheduling step):
- At minimum one required field validated

For each invalid field:
- Show an inline error message using `textContent` (or a `<span>` with the message bound via `{{ }}`
- Set `aria-invalid="true"` on the input (`:aria-invalid="fieldError ? 'true' : 'false'"`)
- Link the error to its input with `aria-describedby`

---

## Reactive requirements

- `v-model` used for all form inputs (no manual `@input` handlers reading `.value`)
- A `computed` property in at least one step that derives a value from the step's form data (e.g., a character count, a formatted preview, a validation summary)
- The review step renders data from props reactively — if the parent's data changes, the review updates automatically

---

## Accessibility requirements

- Step indicator communicates current step to screen readers (not just visually)
- When advancing to a new step, focus moves to the new step's heading (use Vue's `nextTick` with `el.focus()`)
- All form inputs have connected `<label>` elements
- Error messages are linked to their inputs via `aria-describedby`
- The "Submit" button on the review step has a clear label (not just "Submit" — e.g., "Confirm registration")
- `aria-live="polite"` on a region that announces step changes

---

## Constraints

- Vue 3 with `<script setup>` syntax (Composition API)
- No Options API
- No Vuex or Pinia (manage all state in App.vue with `ref`)
- No UI component libraries (Vuetify, PrimeVue, etc.)
- `node_modules/` and `dist/` in `.gitignore`

---

## Above baseline (stretch)

Work in this section is reflected in the Excellent (4) column of the rubric.

- Persist partially-completed form data to `localStorage` so a user who closes the tab mid-flow can resume where they left off
- Add a `computed` property in `App.vue` that tracks overall form completion percentage and display it in `StepIndicator`
- Animate step transitions using Vue's `<Transition>` component

---

## Deliverable

In your course repository: `assignments/assignment-6/` containing the full Vite + Vue project source (without `node_modules/` or `dist/`).

Deploy to Netlify or Vercel.

Submit to Canvas: live URL, repo URL, and rationale link.

---

## Rationale (in rationale.md)

Write 4–6 sentences addressing:
- How did you decide where to own the form data — in each step component or in App.vue — and why?
- Where did you use `computed()` and what would have been more work without it?
- How did you handle focus management between steps, and why does it matter for keyboard users?
- What is one thing about Vue's reactivity system that surprised you while building this?

---

## Rubric

| Criterion | Excellent (4) | Proficient (3) | Developing (2) | Incomplete (1) |
|-----------|--------------|----------------|----------------|----------------|
| **Component decomposition** | All five component types present with correct responsibilities; data flows down via props, events flow up via emits | Four components; one minor responsibility leak | Three components; some prop mutation | Single-component app |
| **Reactive form state** | `v-model` on all inputs; `computed` used for derived value; review reflects parent data via props | `v-model` used; no `computed` | Mixed `v-model` and manual handlers | Manual DOM reads |
| **Validation** | All three steps validate before advancing; error messages inline and linked via `aria-describedby`; `aria-invalid` set correctly | Two steps validate; error messages present | One step validates | No validation |
| **Step flow** | Advancing, going back, and submitting work correctly; review shows complete data; success view resets app | Advancing and submitting work; back navigation missing | Forward flow works; review incomplete | Flow non-functional |
| **Accessibility** | Focus managed on step change; `aria-live` on step region; all labels connected; step indicator readable by screen reader | Three of four criteria | Two criteria | One or none |
| **Rationale** | Specific, honest, addresses all four prompts | Addresses three prompts | Vague or two prompts | Missing |
