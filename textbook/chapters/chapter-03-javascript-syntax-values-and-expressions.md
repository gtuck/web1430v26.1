# Chapter 3: JavaScript Syntax, Values, and Expressions

JavaScript is the language of browser behavior. Before you can make pages interactive, you need a clear mental model of how JavaScript represents information, evaluates expressions, and communicates results.

## What this chapter is really about

This chapter covers the everyday grammar of JavaScript: how to declare variables, what types of values exist, how operators work, and how to use the console to see what your code is doing at any moment. The emphasis is on building correct mental models rather than memorizing syntax — a developer who understands why `0 == false` is `true` will never be surprised by it.

## Key ideas

**Variables and constants** store values. Prefer `const` for values that will not be reassigned. Use `let` when reassignment is necessary. Never use `var` — it has function scope and hoisting behavior that produces confusing bugs.

```js
const siteName = 'Campus Events';   // will not change
let currentPage = 1;                // will be incremented later
```

**Primitive types** are the basic kinds of values JavaScript can hold:
- `string` — text, written with single quotes, double quotes, or backticks: `'hello'`, `"world"`, `` `template` ``
- `number` — integers and decimals: `42`, `3.14`, `-7`
- `boolean` — `true` or `false`
- `undefined` — a variable that has been declared but not assigned a value
- `null` — an intentional absence of a value (you set this on purpose)

Use `typeof` to check what type a value is: `typeof 'hello'` returns `'string'`, `typeof 42` returns `'number'`.

**Template literals** (backtick strings) allow you to embed variables and expressions directly into strings:

```js
const name = 'Jordan';
const unreadCount = 3;
const greeting = `Hello, ${name}! You have ${unreadCount + 2} messages.`;
// "Hello, Jordan! You have 5 messages."
```

**Comparison operators**: Always use `===` (strict equality) and `!==` (strict inequality). The `==` operator performs type coercion — it converts values to the same type before comparing, which produces results like `0 == false` being `true` and `'' == false` being `true`. Strict equality never coerces.

**Useful string methods**:
- `.length` — number of characters
- `.toUpperCase()` / `.toLowerCase()` — case conversion
- `.trim()` — removes leading and trailing whitespace
- `.includes(substring)` — returns `true` if the string contains the substring
- `.replace(old, new)` — returns a new string with replacements

## Mental model

JavaScript evaluates *expressions* to produce *values*. An expression is any piece of code that produces a value: `2 + 2`, `'hello'.toUpperCase()`, `name === 'Jordan'`, and `typeof undefined` are all expressions. A *statement* is a complete instruction: a variable declaration, a function call, a conditional.

The type of a value determines what you can do with it. You can call `.toUpperCase()` on a string but not on a number. You can multiply numbers but not strings (well — you can, but the result is `NaN`, which means "Not a Number" and is almost never what you want).

## Working habits

- Default to `const`. Only switch to `let` when you know you will reassign the variable. This eliminates an entire category of bugs where values change unexpectedly.
- Use `===` for all comparisons. Add a linter rule to forbid `==` if you can.
- Log early and often. `console.log(variableName)` is not a crutch — it is a professional tool. Log values at each step when debugging to find exactly where the value becomes wrong.
- Name variables for what they contain: `userName` not `x`, `productPrice` not `p`, `isLoggedIn` not `flag`.

## Common mistakes

- Using `var`. It is function-scoped and hoisted to the top of its function, making behavior hard to predict. Use `const` and `let`.
- Comparing with `==`. The type coercion rules are complex and counterintuitive. Always use `===`.
- Not accounting for `undefined`. If a variable is declared but not assigned, or if a function doesn't return a value, the result is `undefined`. Operating on `undefined` (e.g., calling `.length` on it) throws an error.
- Confusing `null` and `undefined`. `null` is a value you assign intentionally. `undefined` means something was never set. Both are falsy, but `null === undefined` is `false`.
- String-number confusion: `'5' + 3` produces `'53'` (string concatenation), not `8`. Use `Number('5')` or `parseInt('5', 10)` to convert first.

## Accessibility and UX note

JavaScript that produces visible text output — error messages, labels, counts, status updates — must be written with real users in mind. Avoid outputting raw data values like `undefined` or `[object Object]` to the page. Format values meaningfully. A message like "3 results found" is useful; a message like `data.length` rendered directly to the DOM is not.

## Practice prompt

Open the browser console (F12 → Console tab). Complete the following without writing any HTML:

1. Declare three `const` variables: one string (a name of your choice), one number (a year), one boolean.
2. Use `typeof` on each variable and log the results.
3. Write a template literal that combines all three into a readable sentence and log it.
4. Try `'5' == 5` and `'5' === 5` in the console. Note the results. Then try `null == undefined` and `null === undefined`. Explain in a comment what you observe.
5. Call `.toUpperCase()` on your name string and `.toString()` on your number. Log both results.

## Reflection

When did type coercion surprise you during the practice prompt? What is the practical difference between `null` and `undefined`, and when would you assign `null` on purpose? Why does defaulting to `const` reduce bugs?

## Vocabulary

- **variable** — a named container for a value, declared with `let` or `const`
- **constant** — a variable declared with `const` that cannot be reassigned
- **type** — the category of a value (string, number, boolean, undefined, null, object)
- **expression** — any code that evaluates to a value
- **operator** — a symbol that performs an operation on values (`+`, `-`, `===`, `!==`, etc.)
- **type coercion** — automatic conversion of a value from one type to another (why `==` is dangerous)
- **template literal** — a string written with backticks that can embed expressions with `${}`
- **undefined** — the value of a variable that has been declared but not assigned
- **null** — an intentional absence of a value, assigned explicitly
- **NaN** — "Not a Number"; the result of invalid numeric operations like `'hello' * 2`

## Mini checklist

- I can declare variables with `const` and `let` and explain when to use each.
- I can name the five primitive types and give an example of each.
- I can write a template literal that embeds at least one expression.
- I can explain why `===` should always be preferred over `==`.
- I can use `typeof` and `console.log` to inspect values while debugging.
- I can convert a string to a number and explain when that is necessary.
