# Vue Transition Guide

**Purpose:** Use this guide in Weeks 12 and 13 if Vue feels like a sharp jump from vanilla JavaScript. The goal is to shrink the transition into a few repeatable patterns instead of treating Vue like a brand-new programming language.

---

## What stays the same from vanilla JavaScript

Vue changes the syntax around your UI, but it does not change the core reasoning you already know:

- data still lives somewhere and changes over time
- the interface still reflects the current state
- events still tell the app that the user did something
- smaller pieces are still easier to test than one giant file

If you already understand variables, functions, objects, DOM events, and state, you are not starting from zero. You are learning a new way to organize the same ideas.

---

## Minimum viable Vue ramp

Build in this order. Do not skip ahead.

1. **Render one component with hard-coded content.**
   Prove that the app runs and the template renders before you add state.
2. **Add one `ref()` value and show it in the template.**
   Change the value once and confirm the UI updates.
3. **Pass one prop from a parent to a child.**
   This is the first pattern to master before you build a larger interface.
4. **Emit one event from the child back to the parent.**
   Treat this like the Vue version of a controlled interaction.
5. **Only then add forms, validation, derived state, or multiple components.**
   If the first four steps are not clear yet, more complexity will not help.

---

## Parent or child? Use this rule

- If only one component needs the data temporarily, it can stay local to that component.
- If multiple components need the data, or if the parent decides what to show next, the data should live in the parent.
- Children should receive data through props and communicate changes upward with emits.

If you are unsure, ask: "Who needs to know this value?" The broadest owner usually holds the state.

---

## Common transition mistakes

- Building three components before one prop and one emit already work
- Mutating a prop directly instead of emitting an update request upward
- Forgetting that `ref` values use `.value` in script code
- Mixing display logic, validation logic, and layout changes into one debugging session
- Treating Vue as "magic" instead of checking the data flow one step at a time

---

## Debug in this order

1. Is the component rendering at all?
2. Is the parent holding the data you think it is holding?
3. Is the child receiving the expected prop value?
4. Is the child emitting the event you expect?
5. Is the parent handling that event and updating state?
6. After the state changes, does the template reflect the new state?

If you cannot answer one of these clearly, stop there and fix that step before moving on.

---

## Week 12 survival plan

- Finish one small parent/child example before you scale up your app.
- Keep `Project 2` moving forward; do not let Vue work erase the progress you already made.
- Spend 20 to 30 minutes previewing the Final Project:
  - choose one audience
  - test one API or local JSON source
  - write down 3 to 5 realistic features

That preview work makes Week 13 milestones feel like continuation instead of a cold start.

---

## Week 13 survival plan

- For `Assignment 6`, get Step 1 working before you build Steps 2 and 3.
- Make the parent manage workflow state; let each step own only its temporary inputs.
- Add focus management and `aria-live` only after the basic step transitions work.
- Treat stretch goals as optional. Baseline correctness and accessibility matter more than extra effects.

---

## If you are behind

Reduce the scope of your interface before you reduce the quality of the fundamentals.

Keep these first:

- one clear parent/child data flow
- correct validation on required fields
- accessible labels, errors, and focus movement
- a working review or summary step

Cut these first:

- extra styling flourishes
- animations
- optional persistence features
- extra component variations
