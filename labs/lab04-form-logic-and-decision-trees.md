# Lab 04 – Form Logic and Decision Trees

## Purpose

Conditionals, loops, and functions are most useful when they are connected to real user input. This lab combines form reading with control flow: you will read values from HTML inputs and use functions to compute and display results based on what the user entered.

## Skills practiced

- Reading values from HTML form inputs with `.value`
- Writing named functions with parameters and return values
- Using `if/else if/else` conditionals
- Using guard clauses (early returns) for invalid input
- Iterating with a loop
- Keeping validation logic separate from rendering logic

## What you're building

A **Trail Recommender** — a small web tool that takes a hiker's experience level, preferred distance, and available time, then recommends one of several trail options from a hardcoded list. A second panel shows a simple loop: a table of hiking distances converted from miles to kilometers.

---

## Part 1: HTML structure

Create `labs/lab04/index.html`.

Build a page with two sections:

**Section 1 – Trail Recommender**

A form with:
- A `<select>` for experience level: `beginner`, `intermediate`, `advanced`
- A number input for preferred distance in miles (1–20)
- A number input for available time in hours (1–8)
- A `<button type="button">` labeled "Find My Trail" (not a submit button)
- A `<div id="recommendation">` where the result will be displayed

**Section 2 – Distance Converter Table**

- A number input for "miles per entry" (default: 5)
- A number input for "number of rows" (default: 10, max: 20)
- A `<button type="button">` labeled "Generate Table"
- A `<div id="table-output">` where the table will be rendered

No form submission needed — both sections use buttons that trigger JavaScript functions.

---

## Part 2: Trail data

In `labs/lab04/lab04.js`, define the following data. Do not modify it — write functions that work with it as-is.

```js
const trails = [
  { name: 'Lakeside Loop', distance: 2.5, hours: 1.5, level: 'beginner' },
  { name: 'Ridgeline Path', distance: 5, hours: 3, level: 'beginner' },
  { name: 'Canyon Crossing', distance: 8, hours: 4.5, level: 'intermediate' },
  { name: 'Summit Approach', distance: 12, hours: 6, level: 'intermediate' },
  { name: 'Granite Peak', distance: 16, hours: 7, level: 'advanced' },
  { name: 'Wilderness Circuit', distance: 20, hours: 8, level: 'advanced' },
];
```

---

## Part 3: Trail recommender logic

> **DOM preview — the glue code you need this week.** The DOM and events get full coverage in Weeks 06–07; this lab only needs the small pattern below. Copy and adapt it — the logic inside your functions is what is being graded this week.
>
> ```js
> // Read a form value (always a string — convert numbers with Number())
> const distance = Number(document.querySelector('#distance').value);
>
> // Run a function when a button is clicked
> const button = document.querySelector('#find-trail-btn');
> button.addEventListener('click', () => {
>   // read inputs, call your functions, render the result
> });
>
> // Display a result safely (no innerHTML)
> const output = document.querySelector('#recommendation');
> output.textContent = '';                 // clear previous output
> const p = document.createElement('p');   // create an element
> p.textContent = 'Your trail: Lakeside Loop';
> output.append(p);                        // add it to the page
> ```

Write the following functions. Keep each function focused on one task.

### `findTrail(level, maxDistance, maxHours)`

Accepts three arguments (strings and numbers from the form). Returns the first trail in `trails` that:
- Matches the `level` exactly
- Has `distance` ≤ `maxDistance`
- Has `hours` ≤ `maxHours`

Returns `null` if no trail matches.

### `validateInputs(level, maxDistance, maxHours)`

Returns an error message string if any input is invalid:
- `level` must be `'beginner'`, `'intermediate'`, or `'advanced'`
- `maxDistance` must be a number between 1 and 20
- `maxHours` must be a number between 1 and 8

Returns `null` if all inputs are valid.

### `renderRecommendation(trail)`

Accepts a trail object (or `null`). Updates `#recommendation`:
- If `trail` is `null`: displays "No trail matches your criteria. Try adjusting your distance or time."
- If a trail is found: displays the trail name, distance, estimated time, and difficulty level

Use `createElement` and `textContent`. Do not use `innerHTML`.

### Button click handler

Wire the "Find My Trail" button to:
1. Read the three form values
2. Call `validateInputs` — if invalid, display the error message in `#recommendation` and stop
3. Call `findTrail` with the validated values
4. Call `renderRecommendation` with the result

---

## Part 4: Distance converter table

### `milesToKm(miles)`

Returns the kilometers equivalent (miles × 1.60934), rounded to two decimal places.

### `renderTable(increment, rows)`

Generates a conversion table. Each row shows a distance in miles and its km equivalent, starting at `increment` and increasing by `increment` each row.

Guard clauses required:
- If `rows` is less than 1 or greater than 20, display an error message and return early
- If `increment` is less than 0.1, display an error message and return early

Build the table using `createElement` (not `innerHTML`). Render it into `#table-output`.

Example output for increment=5, rows=4:

| Miles | Kilometers |
|-------|-----------|
| 5 | 8.05 |
| 10 | 16.09 |
| 15 | 24.14 |
| 20 | 32.19 |

---

## Testing requirements

Before submitting, test the following scenarios manually and confirm the correct output:

- Experience: beginner, distance: 10, time: 5 → should find "Ridgeline Path" or similar
- Experience: advanced, distance: 5, time: 2 → should display "No trail matches"
- Distance left blank → should display a validation error
- Table: increment 5, rows 10 → should render 10 rows correctly
- Table: rows 25 → should display an error message

---

## Deliverable

In `labs/lab04/`:
- `index.html`
- `lab04.js`
- `notes.md`

Commit at least three times (after HTML, after Part 3, after Part 4). Push and deploy.

Submit to Canvas: live URL, repo URL, notes.md link.

---

## Process reflection (in notes.md)

Answer in 4–6 sentences:
- Where did you use a guard clause, and what would have happened without it?
- What happened when you tested with missing or out-of-range inputs?
- What would need to change if you wanted to add a fourth trail difficulty level?

---

## Rubric

| Criterion | Excellent (4) | Proficient (3) | Developing (2) | Incomplete (1) |
|-----------|--------------|----------------|----------------|----------------|
| **Trail recommender** | Correctly filters by all three criteria; handles no-match case; validation catches all invalid inputs | Filters by two criteria; some validation | Basic filtering, no validation | Not functional |
| **Distance table** | Table renders correctly for valid inputs; guard clauses catch both invalid conditions | Table renders; one guard clause missing | Table renders but no validation | Not functional |
| **Function separation** | Logic, rendering, and validation in separate named functions; no anonymous handlers | Some separation | All logic in one handler | No named functions |
| **DOM safety** | `createElement` and `textContent` used throughout; no `innerHTML` | Mostly safe; one `innerHTML` for static content | `innerHTML` used for dynamic content | Significant `innerHTML` misuse |
| **Reflection** | Specific; addresses all three prompts | Addresses two prompts | Vague | Missing |
