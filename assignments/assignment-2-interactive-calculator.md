# Assignment 2 – Interactive Calculator

**Due:** End of Week 5
**Weight:** One of six assignments (20% combined)
**Skills:** JavaScript variables, conditionals, functions, form input, DOM output, defensive input handling

---

## Overview

You will build a focused, single-purpose browser calculator that solves a real (if small) problem. This is not a four-function arithmetic calculator — it is a **domain-specific tool** that does one kind of calculation well, with clear inputs, validated data, and readable output.

---

## Scenario

Choose **one** of the following calculator types, or propose your own with instructor approval:

- **Tip and bill splitter** — takes a meal total, tip percentage, and number of people; outputs each person's share
- **Unit converter** — converts between two or more related units (temperature, distance, weight, cooking measurements)
- **GPA estimator** — takes up to five courses with credits and letter grades; outputs estimated semester GPA
- **Loan payment estimator** — takes principal, interest rate, and loan term; outputs estimated monthly payment
- **BMI or calorie estimator** — takes relevant health measurements; outputs a calculated result with context

All calculators must follow the same technical requirements regardless of topic.

---

## What to build

### HTML requirements
- A `<form>` with appropriately typed inputs (`<input type="number">`, `<select>`, etc.)
- Labels connected to every input with `for` / `id` pairs
- A trigger button (`<button type="button">`, not a submit button)
- A results area (`<div>` or `<section>`) where output is rendered
- An error display area linked to invalid inputs via `aria-describedby`

### JavaScript requirements

All JavaScript in a separate `.js` file linked with `<script defer>`.

**Required functions — each must be named and in its own `const` or `function` declaration:**

1. A **pure calculation function** that accepts inputs as arguments and returns the computed result — no DOM access inside this function
2. A **validation function** that checks inputs and returns either `null` (valid) or an error message string
3. A **render function** that accepts the result and updates the DOM — no calculation logic inside this function
4. A **click handler** that orchestrates: read inputs → validate → calculate → render (or show error)

No anonymous functions for named responsibilities. No logic inside event handlers beyond orchestration.

### Output requirements
- Display the result in a human-readable format (not raw numbers — format prices as `$12.50`, temperatures as `72°F`, etc.)
- Show at least two calculated values (e.g., total and per-person share; converted value and original value for reference)
- Clear previous results before rendering new ones

### Accessibility requirements
- Error messages use `aria-describedby` to associate with their input
- Set `aria-invalid="true"` on inputs that fail validation; remove it when corrected
- Results area uses `aria-live="polite"` so screen readers announce new output

---

## Validation requirements

Your validation function must catch and report all of the following:
- Empty or non-numeric inputs where a number is required
- Values outside a valid range (e.g., tip percentage above 100%, negative distances)
- Division-by-zero conditions (e.g., 0 people splitting a bill)

Each error message must name the specific field and the problem: "Number of people must be at least 1" not "Invalid input."

---

## Constraints

- No CSS frameworks
- No external calculation libraries
- Calculation logic must be in your own functions, not delegated to `eval()`
- Validate your HTML; fix all errors

---

## Above baseline (stretch)

- Store the last calculation result in `sessionStorage` and restore it on page reload
- Add a "calculation history" list showing the last three results
- Support keyboard submission (pressing Enter in any input field triggers the calculation)

---

## Deliverable

In your course repository, create `assignments/assignment-2/`:
- `index.html`
- `calculator.js`
- `style.css`
- `rationale.md`

Deploy and submit live URL, repo URL, and rationale link to Canvas.

---

## Rationale (in rationale.md)

Write 4–6 sentences addressing:
- What calculator did you build and who is it for?
- How did you separate calculation logic from rendering logic, and why does that separation matter?
- What edge cases did your validation catch, and did you discover any you hadn't anticipated?
- What would you add if you extended this tool?

---

## Rubric

| Criterion | Excellent (4) | Proficient (3) | Developing (2) | Incomplete (1) |
|-----------|--------------|----------------|----------------|----------------|
| **Calculation correctness** | Correct results for all valid inputs including edge cases; output formatted meaningfully | Correct for typical inputs; one edge case fails or formatting missing | Calculation works for basic case; multiple edge cases fail | Calculation incorrect or non-functional |
| **Function separation** | Pure calculation function, validation function, and render function each in separate named declarations; handler only orchestrates | Two of three separated; minor mixing | Logic partially separated | All logic in one handler or anonymous function |
| **Validation** | All required error conditions caught; specific, field-named messages; `aria-invalid` and `aria-describedby` used | Most conditions caught; messages vague or not linked to fields | Some validation; no ARIA | No validation |
| **Accessible output** | `aria-live` on results; `aria-describedby` on error spans; `aria-invalid` set/removed correctly | Two of three ARIA requirements met | One requirement met | No accessible output |
| **Code quality** | Named functions, `const` throughout, no `var`, descriptive variable names, no `eval()` | Named functions; minor style issues | Some named functions; `var` used | Anonymous functions throughout; unclear names |
| **Rationale** | Specific, honest, addresses all four prompts | Addresses three prompts | Vague or two prompts | Missing |
