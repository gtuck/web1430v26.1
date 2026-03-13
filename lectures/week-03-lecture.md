# Week 03 Lecture Notes: Variables, Types, Operators, and Debugging

## Weekly focus
Building a reliable mental model of JavaScript values and how to inspect them when things go wrong.

## Why this matters
JavaScript's type system behaves differently from most languages beginners have encountered. Silent type coercion — where `"5" + 3` produces `"53"` instead of an error — is the source of bugs that are genuinely hard to find without a clear mental model of what types are and how operators work on them. Learning to read error messages and use `console.log` strategically this week will save you hours of confusion in every subsequent week of the course.

## Learning targets
- Declare variables with `const` and `let` and explain why `var` is avoided in modern JavaScript
- Identify and distinguish the six primitive types: `string`, `number`, `boolean`, `null`, `undefined`, `symbol` (and `bigint`)
- Use `typeof` to inspect a value's type and predict its output for edge cases like `null` and functions
- Write template literals and explain when they are preferable to string concatenation
- Apply `===` (strict equality) instead of `==` (loose equality) and describe one case where `==` produces a surprising result
- Follow a console-debugging workflow: reproduce, isolate, inspect with `console.log`, form a hypothesis, test

## Core concepts

### `const` vs `let` — never `var`
JavaScript has three variable declaration keywords. Two are used in modern code:

```javascript
const siteName = 'Weber State';   // cannot be reassigned
let visitCount = 0;               // can be reassigned
visitCount = visitCount + 1;      // fine

siteName = 'Utah State';          // TypeError: Assignment to constant variable.
```

**Rule:** Default to `const`. Only use `let` when you know the value will change (a counter, a flag, a value that gets updated in a loop). Never use `var` — it has function scope and hoisting behavior that makes code harder to reason about.

`const` does not mean *immutable*. An object or array declared with `const` can still have its contents changed; `const` only prevents reassigning the variable itself to a different value.

### The primitive types
JavaScript has seven primitive types. You will use these five constantly:

| Type | Example values | `typeof` returns |
|------|---------------|-----------------|
| `string` | `'hello'`, `"world"`, `` `template` `` | `"string"` |
| `number` | `42`, `3.14`, `NaN`, `Infinity` | `"number"` |
| `boolean` | `true`, `false` | `"boolean"` |
| `null` | `null` | `"object"` *(historic bug)* |
| `undefined` | `undefined` | `"undefined"` |

```javascript
typeof 'hello'      // "string"
typeof 42           // "number"
typeof true         // "boolean"
typeof null         // "object"  ← this is a known JavaScript bug, not your mistake
typeof undefined    // "undefined"
typeof someUndeclaredVariable  // "undefined" (does not throw)
```

The `null` / `typeof` result is a 25-year-old bug in the language. It cannot be fixed without breaking the web. To reliably check for `null`, use `=== null`.

### Type coercion gotchas
JavaScript automatically converts types in certain operations. This is called *implicit type coercion*, and it produces results that look like bugs:

```javascript
// The + operator with a string converts the number to a string
'5' + 3           // "53"   (concatenation, not addition)
'5' - 3           // 2      (subtraction has no string meaning, so JS converts)

// Falsy values: these all evaluate to false in a boolean context
0, '', null, undefined, NaN, false

// Truthy surprises
Boolean('0')      // true  — non-empty string, even if it is "0"
Boolean([])       // true  — empty array is truthy
Boolean(0)        // false

// == performs type coercion before comparing
0 == false        // true
'' == false       // true
null == undefined // true
null == 0         // false  — inconsistent!
```

This is why `===` exists: it compares value *and* type without any conversion. Use it by default.

### `===` vs `==` in practice
```javascript
// Loose equality — coerces types, produces surprises
console.log(1 == '1');   // true
console.log(0 == '');    // true
console.log(null == undefined);  // true

// Strict equality — no coercion
console.log(1 === '1');  // false
console.log(0 === '');   // false
console.log(null === undefined); // false
```

The practical rule: **always use `===` and `!==`**. If you find yourself reaching for `==`, ask what type coercion you are relying on — there is almost always a cleaner way to express the intent.

### Template literals
Template literals use backtick characters and `${}` to embed expressions directly in strings:

```javascript
const firstName = 'Jordan';
const score = 94;

// Old style (concatenation)
const msg1 = 'Hello, ' + firstName + '! Your score is ' + score + '.';

// Template literal — easier to read and write
const msg2 = `Hello, ${firstName}! Your score is ${score}.`;

// Multi-line strings (no \n needed)
const html = `
  <article>
    <h2>${firstName}'s Profile</h2>
    <p>Score: ${score}</p>
  </article>
`;
```

The expression inside `${}` can be any valid JavaScript: a variable, a function call, a ternary, arithmetic — anything that produces a value.

### `NaN` — the "not a number" value
`NaN` is technically of type `number` but represents an invalid numeric operation:

```javascript
parseInt('hello')     // NaN
10 / 'hello'          // NaN
NaN === NaN           // false  ← NaN is not equal to itself
Number.isNaN(NaN)     // true   ← use this to check for NaN
```

`NaN` propagates: any arithmetic involving `NaN` produces `NaN`. If you see unexpected `NaN` values cascading through your code, find the original bad conversion.

### Console debugging workflow
When your code does not do what you expect, work through these steps:

1. **Reproduce** — confirm you can make the bug happen consistently.
2. **Identify the last line that worked** — use `console.log` to print values at key points:
   ```javascript
   function calculateTotal(price, quantity) {
     console.log('price:', price, typeof price);
     console.log('quantity:', quantity, typeof quantity);
     const total = price * quantity;
     console.log('total:', total);
     return total;
   }
   ```
3. **Read the error message** — the Console tab shows the error text, the file name, and the line number. Click the line number to jump to the source.
4. **Form a hypothesis** — "I think `price` is a string, not a number, because the input value came from a form field."
5. **Test the hypothesis** — add a `typeof` check or log the raw value before processing.
6. **Fix, then remove debug logs** — do not leave `console.log` calls in production code.

Common error types you will see this week:
- `ReferenceError: x is not defined` — you used a variable before declaring it, or misspelled it
- `TypeError: Cannot read properties of undefined` — you tried to access a property on `undefined` (e.g., called a method before a DOM element existed)
- `SyntaxError: Unexpected token` — a typo in your code structure (missing bracket, mismatched quotes)

## Common mistakes
1. **Using `var` because old tutorials do.** Most JavaScript tutorials on the internet predate 2015 and use `var`. When you encounter it, mentally substitute `let`. Do not write new `var` declarations.
2. **Treating `null` and `undefined` as the same thing.** `null` is an intentional "no value" set by a programmer. `undefined` means a variable was declared but never assigned, or a property does not exist. They behave similarly in many contexts but come from different causes — distinguish them when debugging.
3. **Using `==` to compare form input values to numbers.** Form input `.value` is always a string. `inputEl.value == 5` might return `true` due to coercion, masking a type problem. Use `Number(inputEl.value) === 5` or `parseInt(inputEl.value, 10) === 5` to be explicit.
4. **Forgetting that `const` objects are still mutable.** `const user = { name: 'Alex' }` — you cannot reassign `user`, but `user.name = 'Sam'` works fine. Students sometimes expect `const` to freeze the object.
5. **Ignoring `typeof` output when debugging.** When a value behaves unexpectedly, the first question is always "what type is this?" Log `typeof` alongside the value to confirm your assumption.

## Accessibility connection
JavaScript that runs in the browser can add, remove, or modify DOM content dynamically. When your scripts change content without updating the accessibility tree — for example, toggling a section visible without updating an associated `aria-expanded` attribute — screen reader users may not know the change occurred. This week's debugging skills apply directly: use the Console to verify that JavaScript is executing and that the DOM changes you intend are actually happening before worrying about accessibility attributes. Correct behavior is a prerequisite for accessible behavior.

## Demo walkthrough
**Goal:** Demonstrate type coercion causing a real bug, then fix it using strict equality and explicit type conversion.

1. Open the browser Console (`F12`, Console tab).
2. Type `'10' + 5` and press Enter. Show the result `"105"`. Ask: "What did you expect?" Then show `10 + 5` returns `15`.
3. Declare a variable simulating a form input value: `const rawInput = '10';`
4. Show that `rawInput == 10` is `true` but `rawInput === 10` is `false`.
5. Create a simple function in the Console:
   ```javascript
   function doubleIt(value) {
     return value * 2;
   }
   doubleIt('5');   // returns 10 — but for the wrong reason
   doubleIt('abc'); // returns NaN
   ```
6. Add a `console.log(typeof value)` inside the function body. Re-run. Show the type being logged.
7. Add an explicit conversion and show the corrected version:
   ```javascript
   function doubleIt(value) {
     const n = Number(value);
     if (Number.isNaN(n)) { return 'Invalid input'; }
     return n * 2;
   }
   ```
8. Show a `ReferenceError` deliberately: type `console.log(undeclaredVar)`. Point to the file/line indicator in the Console and explain how to read it.

## Practice prompt
Open the browser Console and work through these exercises, logging each result and writing down whether it matches your prediction before you run it:
1. `typeof null` — predict, then check
2. `'3' * '4'` — predict the type and value
3. `null == undefined` vs `null === undefined`
4. `` `${2 + 2} is ${2 + 2 === 4 ? 'correct' : 'wrong'}` ``
5. Declare `const colors = ['red', 'green']` then run `colors.push('blue')` — does `const` prevent this?

Document your predictions and the actual results. Note which ones surprised you and why.

## Bridge
Lab 03 – Console Exercises and Small Programs consists of small JavaScript problems solved entirely in the browser Console and in a `.js` file — the same environment used in today's demo. Quiz 2 will include questions on `typeof` output, the result of specific coercion expressions, and when to use `const` vs `let`; review the type table and the `==` vs `===` examples before taking it. The Chapter 3 reading goes deeper on expressions and operator precedence, which will fill in the gaps between what was covered here and what you encounter in the lab.
