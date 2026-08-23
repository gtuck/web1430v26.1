# Week 08 Lecture Notes: Refactoring, Reuse, and Midterm Review

## Weekly focus

Consolidate Weeks 01–07 by improving existing code quality through refactoring, then prepare for the Midterm Exam and finalize Project 1.

## Why this matters

Every professional codebase is maintained and improved over time — rarely rewritten from scratch. Refactoring teaches you to read code critically, spot duplication, and make structural improvements without breaking what already works. The habits you build this week (extracting functions, naming things well, removing copy-paste) are what separate code that is easy to maintain from code that becomes a liability.

## Learning targets

- Define refactoring and explain why it does not change observable behavior
- Extract repeated logic into a named function and call it from multiple places
- Choose function names that describe what the function does, not how it does it
- Identify at least three categories of code that benefit most from refactoring
- Recall the major topics from Weeks 01–07 and explain how they connect
- Describe the Midterm Exam format and apply a preparation strategy

## Core concepts

### What refactoring means
Refactoring is the process of restructuring existing code without changing what it does from the user's perspective. The browser output stays identical. The tests (if any) still pass. What changes is the internal structure: it becomes easier to read, easier to change, and less prone to bugs introduced by duplication.

A useful test: if you can describe a refactor entirely in terms of code structure ("I extracted this block into a function") rather than behavior ("now it does X differently"), it is a refactor. If behavior changes, that is a bug fix or a feature — valuable, but not the same thing.

### The most common refactoring: extracting a function
The single most useful refactoring move is pulling a block of code out into a named function. This applies whenever you see the same logic in two or more places, or when a single block of code is doing too many things at once.

**Before — duplicated validation logic inline:**
```js
// Validate form A
const nameA = document.getElementById("name-a").value.trim();
if (nameA === "") {
  document.getElementById("error-a").textContent = "Name is required.";
  return;
}

// Validate form B (same logic, copied)
const nameB = document.getElementById("name-b").value.trim();
if (nameB === "") {
  document.getElementById("error-b").textContent = "Name is required.";
  return;
}
```

**After — one function, called twice:**
```js
function requireField(inputId, errorId, label) {
  const value = document.getElementById(inputId).value.trim();
  if (value === "") {
    document.getElementById(errorId).textContent = `${label} is required.`;
    return false;
  }
  return true;
}

// inside the submit handler
if (!requireField("name-a", "error-a", "Name")) return;
if (!requireField("name-b", "error-b", "Name")) return;
```

Note the third parameter. The first version of this refactor hardcoded `"Name is required."`, which works until the second caller is an email field. If an extracted function still contains a value that only makes sense for one of its callers, it is not finished — pass that value in.

The behavior is identical. But now the rule "what makes a field invalid" lives in one place. If you need to change it — say, add a minimum length — you change one function instead of hunting for every copy.

### Naming functions well
A function name should answer: "what does this do?" not "how does it do it?"

| Weak name | Stronger name |
|---|---|
| `doStuff()` | `resetForm()` |
| `handleIt()` | `displaySearchResults()` |
| `loop()` | `renderCardList(cards)` |
| `check()` | `isValidEmail(value)` |

Predicates (functions that return true/false) should start with `is`, `has`, or `can`. Functions that perform an action should use a verb: `render`, `display`, `fetch`, `save`, `clear`, `validate`.

### Removing duplication beyond functions
Duplication appears in more than just logic. Watch for:

- **Repeated DOM queries**: if you call `document.getElementById("status")` five times in one function, query it once at the top and store the reference.
- **Magic values**: if `"#ff6600"` appears in four places, assign it to a `const BRAND_COLOR` at the top of the file.
- **Parallel `if/else` chains**: if you find yourself writing the same branching structure twice for two similar things, consider whether a loop or a data-driven approach would work.

### Midterm Exam format and scope
The Midterm covers Weeks 01–07. It is 15 multiple-choice and true/false questions in Canvas, timed at 60 minutes, open notes. Expect:
- Concept questions on HTML semantics, CSS layout, and JS fundamentals
- Reading and tracing short code samples to determine output
- Identifying the bug or the fix in short code scenarios
- Questions about the Git/GitHub workflow habits used in this course

**High-priority topics to review:**
- Semantic HTML elements and when to use them
- CSS box model, flexbox, and responsive units
- `const` vs `let`; primitive vs reference types
- Array methods: `forEach`, `map`, `filter`, `find`
- Object dot notation and bracket notation
- `querySelector`, `addEventListener`, `textContent`, `innerHTML`
- Form `submit` event, `preventDefault()`, and field validation patterns

### Project 1 polish checklist
Before submitting, verify:
1. All form inputs have associated `<label>` elements (not just placeholder text)
2. Error messages are in the DOM (not just `alert()`), associated with their field
3. No `console.log` statements left in production code
4. Variable and function names are descriptive
5. Repeated blocks have been extracted into functions
6. The page is usable without a mouse (tab through all interactive elements)

## Common mistakes

1. **Thinking refactoring means adding features.** Refactoring is strictly structural. If your refactor also changes what the code does, you have mixed two things together. Keep them separate.

2. **Over-extracting too early.** Extracting a one-line expression into a named function adds overhead without benefit. Extract when the logic is complex enough to deserve a name, or when it appears in more than one place.

3. **Renaming without updating every call site.** When you rename a function, search the entire file (and any linked files) for the old name. Missing one call causes a `ReferenceError` that only appears at runtime.

4. **Confusing refactoring with cleaning up style.** Adding comments, reformatting indentation, and deleting dead code are worthwhile, but they are not refactoring. Refactoring changes the structure of the logic itself.

5. **Not testing after each small change.** Refactor in tiny increments and reload the browser after each one. Trying to do five refactors at once makes it impossible to tell which one introduced a bug.

## Demo walkthrough

1. Open a working Project 1 submission (or a prepared example) with obvious duplication — three nearly identical event listener callbacks.
2. Identify what is shared: all three read a value, validate it, and display a result.
3. Extract the validation into `validateField(value)` returning `{ valid: boolean, message: string }`.
4. Extract the display into `showResult(containerId, message, isError)`.
5. Rewrite each callback to call those two functions.
6. Reload the browser and verify behavior is unchanged.
7. Point out: the three callbacks are now each 3–4 lines instead of 12–15 lines, and a change to validation logic only needs to happen in one place.

## Session 2: the studio

The rest of this week's material lives in the studio notes — Wednesday's live session for the virtual section, and the second half of the week's work for the online section: [Week 08 Studio Notes: Project 1 Polish Studio and Midterm Review](week-08-studio.md).

Read the *Before class* list there before you start, and bring what it asks for.
