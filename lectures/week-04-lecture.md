# Week 04 Lecture Notes: Conditionals, Loops, Functions, Scope, and Parameters

## Weekly focus

Writing reusable logic: making decisions with conditionals, repeating work with loops, and packaging behavior into functions.

## Why this matters

Every interactive feature on the web — a form that validates input, a button that changes state, a list that filters results — is built on conditionals and functions. Without this layer of logic, JavaScript can only run top-to-bottom once; it cannot respond, repeat, or adapt. Mastering functions now also sets the foundation for every remaining week in this course.

## Learning targets

- Write `if/else` and `switch` statements that branch based on a value or condition
- Use `for` and `while` loops to repeat an operation without copy-pasting code
- Distinguish between function declarations, function expressions, and arrow functions
- Define parameters and use `return` to send a value back to the caller
- Explain the difference between block scope, function scope, and global scope
- Identify and refactor a guard clause to exit a function early on bad input

## Core concepts

### Conditionals: if/else and switch

An `if` statement runs a block of code only when a condition is truthy. The optional `else if` and `else` branches handle other cases. Use `switch` when you are comparing one value against many fixed options — it keeps the code readable.

```js
function describeScore(score) {
  if (score >= 90) {
    return "A";
  } else if (score >= 80) {
    return "B";
  } else if (score >= 70) {
    return "C";
  } else {
    return "F";
  }
}

console.log(describeScore(85)); // "B"
```

```js
function dayLabel(num) {
  switch (num) {
    case 1: return "Monday";
    case 2: return "Tuesday";
    case 3: return "Wednesday";
    default: return "Unknown";
  }
}
```

Prefer `if/else` when you are testing ranges or complex expressions. Use `switch` when one variable maps to a set of known string or number values.

### Loops: for and while

A `for` loop is best when you know in advance how many times to repeat. A `while` loop is best when you repeat until a condition changes.

```js
// Count from 1 to 5
for (let i = 1; i <= 5; i++) {
  console.log(i);
}

// Repeat until the user has valid input (conceptual example)
let attempts = 0;
while (attempts < 3) {
  console.log("Attempt:", attempts + 1);
  attempts++;
}
```

Off-by-one errors are the most common loop bug. Before you write the loop, ask: "Does my condition use `<` or `<=`? Does my counter start at 0 or 1?"

### Function declarations vs expressions vs arrow functions

All three create reusable blocks of code. They differ in syntax and in how they handle `this` (important later).

```js
// Declaration — hoisted, can be called before the line it appears on
function greet(name) {
  return `Hello, ${name}!`;
}

// Expression — stored in a variable, not hoisted
const greet = function(name) {
  return `Hello, ${name}!`;
};

// Arrow function — concise, preferred in modern code
const greet = (name) => `Hello, ${name}!`;
```

For beginners, start with declarations while learning. Move to arrow functions once you are comfortable, because you will see them everywhere in modern JavaScript.

### Parameters and return values

Parameters are placeholders defined in the function signature. Arguments are the actual values passed when the function is called. `return` sends a value back — without it, a function returns `undefined`.

```js
function calculateTax(price, rate) {
  return price * rate;
}

const tax = calculateTax(100, 0.07); // 7
console.log(tax);                    // 7
```

A function should do one thing and return a result. Avoid functions that both compute a value and directly update the page — that mixing makes code harder to test and reuse.

### Scope: block, function, and global

`const` and `let` are block-scoped: they exist only inside the `{}` where they are declared. Variables declared with `var` are function-scoped (legacy behavior — avoid `var`). Variables declared outside any function are global and visible everywhere, which makes them risky.

```js
let total = 0; // global — visible everywhere below

function addItem(price) {
  const tax = price * 0.07; // block-scoped to this function
  total += price + tax;     // reads the global total
}

addItem(10);
console.log(total); // 10.7
// console.log(tax); // ReferenceError — tax is not visible here
```

As a rule of thumb: keep variables as local as possible. If you find yourself reaching for a global variable, consider passing the value as a parameter instead.

### Pure functions and guard clauses

A pure function always returns the same output for the same input and does not modify anything outside itself. Pure functions are predictable and easy to test.

A guard clause is an early `return` that exits the function when input is invalid. It avoids deeply nested `if` blocks.

```js
// Without guard clause — hard to read
function getDiscount(price) {
  if (typeof price === "number") {
    if (price > 0) {
      return price * 0.1;
    }
  }
  return 0;
}

// With guard clauses — easier to read
function getDiscount(price) {
  if (typeof price !== "number") return 0;
  if (price <= 0) return 0;
  return price * 0.1;
}
```

## Common mistakes

1. **Using `=` instead of `===` in a condition.** `if (x = 5)` assigns 5 to `x` and always evaluates to truthy. Always use `===` for comparison.
2. **Forgetting `return`.** A function that calculates a value but never `return`s it gives back `undefined`. Check the console: if you see `undefined` where you expected a number, look for a missing `return`.
3. **Infinite loops.** A `while` loop whose condition never becomes false freezes the browser tab. Always verify your counter variable is being updated inside the loop body.
4. **Scope confusion with `var`.** `var` leaks out of `if` blocks and `for` loops. Use `const` or `let` exclusively and never declare the same variable twice with `let` in the same scope.
5. **Writing one giant function that does too much.** If a function is longer than about 15 lines, it is probably doing more than one job. Break it into smaller, named functions — your future self will thank you.

## Accessibility connection

Well-named functions make code more maintainable, and maintainable code is more likely to stay accessible over time. When functions handle one thing — like `validateEmailInput()` rather than a 50-line anonymous blob — future developers can update validation logic without accidentally breaking the ARIA attributes or error messages attached to that form field. Descriptive function names also serve as inline documentation that helps teams with diverse experience levels contribute to accessibility improvements.

## Demo walkthrough

**Demo: Grade Classifier with Guard Clauses**

1. Open a new `demo-04.js` file and link it to a minimal HTML file with a `<p id="output"></p>`.
2. Write `classifyGrade(score)` using guard clauses: return `"Invalid"` if score is not a number or is outside 0–100, then use `if/else if` to return letter grades.
3. Write a `for` loop that iterates over an array `[55, 73, 88, 95, 101, -5]`, calls `classifyGrade()` for each, and logs the result.
4. In the browser console, call `classifyGrade(88)` directly to show how testing a pure function is trivial.
5. Update `document.getElementById("output").textContent` with the result of one call to show the connection to the DOM (a preview of Week 06).
6. Introduce a deliberate bug — change `===` to `=` in a condition — and show how the console reveals the problem.

## Practice prompt

Write a function called `shippingCost(weightLbs, expedited)` that returns a shipping price. Rules: under 1 lb is $3.99, 1–5 lbs is $6.99, over 5 lbs is $12.99. If `expedited` is `true`, add $5.00 to any tier. Use guard clauses to return `null` if `weightLbs` is not a positive number. Test it with at least five calls in the console.

## Bridge

The logic patterns from this lecture — conditionals, loops, and functions with return values — are exactly what you need for Lab 04's form decision tree. Assignment 2 will ask you to build a multi-step calculator, so practice writing functions that accept parameters and return values rather than hardcoding answers. As you work through the lab, keep your functions short and pure so they are easy to test piece by piece.
