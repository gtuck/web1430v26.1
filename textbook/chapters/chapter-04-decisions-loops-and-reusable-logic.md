# Chapter 4: Decisions, Loops, and Reusable Logic

Programs are not straight lines. They branch based on conditions, repeat actions over collections, and package behavior into reusable functions. This chapter builds the tools you need to write code that responds intelligently to data.

## What this chapter is really about

This chapter teaches you how to write code that makes choices, repeats work efficiently, and organizes behavior into named, reusable functions. These three ideas — conditionals, loops, and functions — are the building blocks of every interactive interface you will ever build. The emphasis is on writing logic that is readable, predictable, and testable.

## Key ideas

**Conditionals** run different code depending on whether a condition is true or false.

```js
if (score >= 90) {
  grade = 'A';
} else if (score >= 80) {
  grade = 'B';
} else {
  grade = 'C or below';
}
```

Use **early returns** to avoid deep nesting. Instead of wrapping the main logic in an `if`, return early when conditions fail:

```js
function getDiscount(member) {
  if (!member) return 0;          // guard clause
  if (member.type === 'premium') return 0.2;
  return 0.1;
}
```

**Truthy and falsy**: JavaScript treats some values as `false` in a boolean context even when they are not literally `false`. Falsy values: `false`, `0`, `''`, `null`, `undefined`, `NaN`. Everything else is truthy. This matters in conditions: `if (username)` is a common pattern that checks whether a string is non-empty.

**Loops** repeat a block of code. Use `for...of` when iterating over an array:

```js
const fruits = ['apple', 'banana', 'cherry'];
for (const fruit of fruits) {
  console.log(fruit);
}
```

Use a classic `for` loop when you need the index:

```js
for (let i = 0; i < fruits.length; i++) {
  console.log(`${i}: ${fruits[i]}`);
}
```

**Functions** name a reusable piece of logic. A function declaration is hoisted; a function expression is not.

```js
// Declaration (hoisted — can be called before it's defined)
function calculateTax(price, rate) {
  return price * rate;
}

// Arrow function expression (concise, not hoisted)
const formatPrice = (price) => `$${price.toFixed(2)}`;

Arrow functions are especially useful as short, anonymous callbacks passed to array methods (covered in the next chapter).
```

A function should do **one thing**. Give it a verb name that describes what it does: `calculateTotal`, `renderCard`, `isValidEmail`. If you can't name it in one verb phrase, it probably does too many things.

**Pure functions** return a value based solely on their inputs and have no side effects. They are easier to test, easier to reason about, and easier to reuse.

```js
// Pure: same input always gives same output, no side effects
function addTax(price, taxRate) {
  return price + price * taxRate;
}

// Impure: depends on and modifies external state
let total = 0;
function addToTotal(price) {
  total += price;   // side effect: changes external variable
}
```

## Mental model

Think of a function as a named recipe with ingredients (parameters) and a result (return value). You write the recipe once, name it clearly, and call it by name whenever you need the result. The function doesn't care what's happening outside it — it only cares about the ingredients it receives.

When you find yourself writing the same logic in two places, that is a signal to extract it into a named function.

## Working habits

- Name functions as verbs: `calculateTotal`, `filterByCategory`, `isValidEmail`, `renderProduct`.
- Keep functions short. If a function is longer than 15–20 lines, it probably has more than one responsibility.
- Return values instead of modifying outer variables. Pure functions are easier to debug.
- Test edge cases. What happens if the array is empty? If the number is negative? If the string is empty? Test these in the console before trusting the function.
- Use early returns (guard clauses) to eliminate nesting. Flat code reads better than nested code.

## Common mistakes

- **Deeply nested conditionals**: more than two levels of `if/else` nesting is a signal to refactor. Use early returns.
- **Not returning a value**: if a function should return something but doesn't have a `return` statement on all paths, it returns `undefined`. Using that result causes errors downstream.
- **Modifying global variables from inside functions**: this creates hidden dependencies and makes functions hard to test and reuse.
- **Anonymous functions for everything**: `function() { ... }` tells the reader nothing. Name your functions.
- **Confusing `=` (assignment) with `===` (comparison)** inside a conditional: `if (x = 5)` assigns 5 to x and always evaluates as true.
- **Off-by-one errors in loops**: remember that arrays are zero-indexed. The last item in an array of length `n` is at index `n - 1`.

## Accessibility and UX note

Conditional logic determines what users see. Make sure every branch of your logic produces valid, complete, accessible output — not just the happy path. If your function renders a product card, it should handle the case where the product has no image, no price, or no name without breaking the interface or producing empty labels that confuse screen readers.

## Practice prompt

Write a function called `describeTemperature(degrees)` that:
- Returns `'freezing'` if degrees is below 0
- Returns `'cold'` if degrees is 0–15
- Returns `'comfortable'` if degrees is 16–25
- Returns `'hot'` if degrees is above 25

Then write a function called `labelTemperatures(readings)` that accepts an array of numbers and returns a new array of strings (the descriptions). Use a loop or array method — do not repeat the `if/else` logic.

Test both functions in the console with at least six inputs, including the exact boundary values: -1, 0, 15, 16, 25, 26.

## Reflection

What happened at the boundary values (0, 15, 16, 25)? How did your conditional logic handle them, and did any edge case produce a result you didn't expect? When you extracted the repeated logic into `describeTemperature`, what did `labelTemperatures` become?

## Vocabulary

- **conditional** — a statement that runs different code depending on whether a condition is true or false
- **branch** — one path through a conditional
- **truthy / falsy** — values JavaScript treats as true or false in a boolean context even when they are not literally `true` or `false`
- **loop** — a statement that repeats a block of code
- **iteration** — one pass through a loop
- **function** — a named, reusable block of code with defined inputs and outputs
- **parameter** — a named placeholder in a function definition
- **argument** — the actual value passed to a function when it is called
- **return value** — the value a function produces when it finishes
- **scope** — the region of code where a variable is accessible
- **pure function** — a function that returns a value based only on its inputs and has no side effects
- **guard clause** — an early return at the top of a function that handles edge cases before the main logic

## Mini checklist

- I can write an `if/else if/else` conditional and explain what each branch does.
- I can write a `for...of` loop that iterates over an array.
- I can write a named function with parameters and a return value.
- I can explain the difference between a pure function and one with side effects.
- I can use a guard clause to avoid nested conditionals.
- I can test my functions at edge cases and fix unexpected results.
