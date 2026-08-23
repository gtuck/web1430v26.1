# Week 13 Studio Notes: Dashboard Studio and Milestone Revision

## Session focus

Session 1 covered props down and events up, reactive forms, and derived state. Session 2 assembles those into the Lab 12 dashboard, works an Assignment 6 build-order clinic, and revises Final Project wireframes against their data plans. Both sessions meet as normal this week — Thanksgiving falls on the Thursday.

## Before class

- Have your Lab 12 data ready as a plain array of objects. Get the data right and the dashboard is mostly `computed()`.
- Bring your Milestone 1 wireframe, however rough.

## Studio plan

1. **Events up, live (10 min).** A child emits, a parent handles, and the data changes in exactly one place. Trace the round trip on screen until the direction is obvious.
2. **Lab 12 dashboard studio (25 min).** `computed()` for every derived number. If you find yourself recalculating a total in two places, that is not a style problem, that is the bug.
3. **Assignment 6 build order (15 min).** Form state first, validation second, submit handler last, and `nextTick` when focus has to land on something that does not exist yet.
4. **Milestone 2 revision workshop (25 min).** Swap wireframes with someone else. Mark every element the data plan cannot actually supply, then revise the plan rather than redrawing the picture.

The virtual section runs this plan live, Wednesday 9:30–10:45 AM (75 minutes). The online section works the same sequence self-paced; where the plan says "the room" or "a volunteer," use the Help & Questions discussion board.

## Accessibility connection

Form labels are not optional. Every `<input>` needs an associated `<label>` — either wrapping the input or connected via matching `for` and `id` attributes. `v-model` handles the binding of data but does nothing for label association. When you disable a submit button with `:disabled="!isValid"`, some screen readers will not announce why the button is disabled; consider adding a visible or visually-hidden explanation near the form. Focus management with `nextTick` is not just a convenience — it is essential for users navigating a multi-step form by keyboard, because they need focus to land in the right place after each step transition.

## Practice prompt

Build a `CommentForm.vue` component with `reactive()` fields for `author` and `body`. Use a `computed()` to determine form validity (both fields non-empty, body at least 10 characters). Display a live character count below the body field derived from `form.body.length`. Emit a `submit` event to the parent with the form data when the user submits. In the parent, push each submitted comment onto an array and render the list below the form.

## Bridge

Lab 12 — Small Data Dashboard has you build a filterable, sortable list with components communicating through props and events — the exact pattern from today's demo. Assignment 6 — Reactive Form Workflow applies the same pattern at a larger scale: a parent that owns the workflow state, three input steps that validate locally and emit upward, and a review step that receives everything as props. Before you write any of it, sketch which component owns which piece of state and what each step emits. That diagram takes five minutes and saves hours of debugging.
