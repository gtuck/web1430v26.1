# Lab 03 – Console Exercises and Small Programs

## Purpose

JavaScript syntax becomes fluent through repetition. This lab is a series of short, focused exercises that build comfort with variables, types, operators, and string methods — first in the browser Console, then in a script file. It also introduces your first debugging exercise: reading an error message and fixing intentionally broken code.

## Skills practiced

- Declaring variables with `const` and `let`
- Identifying and working with primitive types
- Using comparison operators correctly (`===` vs `==`)
- Writing and using template literals
- Calling common string methods (`.trim()`, `.includes()`, `.toUpperCase()`, `.replace()`)
- Reading and interpreting error messages in the Console
- Fixing broken code by reading the error

## What you're building

A script file (`lab03.js`) that completes a series of exercises, plus a linked HTML page that runs it. Each exercise is a self-contained function. You will also complete a set of Console-only experiments and record your findings in `notes.md`.

---

## Part 1: Console experiments (no file needed)

Open a browser tab to any page and open the Console (F12 → Console). Run each experiment below, record the result, and write a one-sentence explanation of why you got that result.

**Type coercion:**
```
'5' + 3
'5' - 3
'5' == 5
'5' === 5
0 == false
0 === false
null == undefined
null === undefined
```

**Types:**
```
typeof 'hello'
typeof 42
typeof true
typeof undefined
typeof null
typeof []
typeof {}
```

Note: `typeof null` returns `'object'` — this is a well-known JavaScript quirk, not a feature.

**Strings:**
```
'  hello world  '.trim()
'hello world'.includes('world')
'hello world'.toUpperCase()
'hello world'.replace('world', 'JavaScript')
'hello'.length
```

Record all results in `labs/lab03/notes.md` under a "Console experiments" section.

---

## Part 2: Script exercises

Create `labs/lab03/index.html` and `labs/lab03/lab03.js`. Link the script with `<script src="lab03.js" defer></script>`.

Implement each function below. After each function, call it with test inputs and log the result. Do not delete your test calls — your grader will read your console output.

### Exercise 1: Greeting

```js
function greet(name) {
  // Returns: "Hello, [name]! Welcome to WEB 1430."
  // If name is empty or only whitespace, return: "Hello, stranger!"
}

console.log(greet('Jordan'));       // "Hello, Jordan! Welcome to WEB 1430."
console.log(greet('  '));           // "Hello, stranger!"
console.log(greet(''));             // "Hello, stranger!"
```

### Exercise 2: Celsius to Fahrenheit

```js
function toFahrenheit(celsius) {
  // Formula: (celsius * 9/5) + 32
  // Return a string formatted to one decimal place: "72.5°F"
}

console.log(toFahrenheit(0));       // "32.0°F"
console.log(toFahrenheit(100));     // "212.0°F"
console.log(toFahrenheit(-40));     // "-40.0°F"
```

Hint: `number.toFixed(1)` returns a string with one decimal place.

### Exercise 3: Password strength

```js
function checkPassword(password) {
  // Return "strong" if password.length >= 12
  // Return "medium" if length is 8–11
  // Return "weak" if length is less than 8
  // Return "invalid" if password is not a string or is empty
}

console.log(checkPassword('abc'));               // "weak"
console.log(checkPassword('MyPass123'));         // "medium"
console.log(checkPassword('MyLongP@ssword!'));   // "strong"
console.log(checkPassword(''));                  // "invalid"
console.log(checkPassword(12345));               // "invalid"
```

### Exercise 4: Initials

```js
function getInitials(fullName) {
  // Accept a full name string, return the initials in uppercase.
  // "Jordan Alex Smith" → "J.A.S."
  // Handle extra spaces gracefully.
}

console.log(getInitials('Jordan Smith'));         // "J.S."
console.log(getInitials('Maria Elena Vargas'));   // "M.E.V."
console.log(getInitials('  Sam   Lee  '));        // "S.L."
```

Hint: `.trim().split(' ')` — but you may get empty strings from double spaces. Filter them out.

---

## Part 3: Debugging exercise

The following code contains **three bugs**: two typos that throw, and one comparison whose comment does not match what the code actually does. Copy it into a new file `labs/lab03/debug.js`, add `<script src="debug.js" defer></script>` to a small `labs/lab03/debug.html` page (or temporarily swap the `src` in your `index.html`), open it in a browser, read the errors in the Console, and fix all three. Do not restructure the code — find and fix only the bugs.

```js
const userName = 'Casey';
const userAge = '28';

function buildWelcome(name, age) {
  const numericAge = parseInt(age);
  const nextYear = numericAge + 1
  return `Hi ${name}! You are ${numericAge} years old. Next year you will be ${nextYeer} years old.`;
}

const message = buildWelcome(userName, userAge)
console.log(mesage);

if (userAge == 28) {
  console.log('Age matched with strict equality');
}
```

Two of the three bugs throw an error that names the problem. The third does not throw at all: read the comparison and the message it prints, decide what the code was *meant* to do, and make the code and the comment agree. Either fixing the comparison or correcting the claim in the message is acceptable — but say which you chose and why.

In `notes.md`, under a "Debugging" section:
1. List each bug you found (line number and what was wrong)
2. Show the fixed code
3. Explain what the error message said and how it pointed you to the problem — and for the third bug, which fix you chose and why

---

## Deliverable

In `labs/lab03/`:
- `index.html`
- `lab03.js` (all four exercises with test calls)
- `debug.js` (fixed version)
- `notes.md` (Console experiments + debugging notes)

Commit with at least two progress commits. Push to GitHub. Deploy and verify the Console output looks correct in the deployed version.

Submit to Canvas: live URL, repo URL, and a link to `notes.md`.

---

## Process reflection (in notes.md)

Answer in 3–5 sentences:
- Which type coercion result surprised you most, and why?
- What was the hardest bug to find in Part 3, and what clue in the error message led you to it?

---

## Rubric

| Criterion | Excellent (4) | Proficient (3) | Developing (2) | Incomplete (1) |
|-----------|--------------|----------------|----------------|----------------|
| **Console experiments** | All expressions run, all results recorded, each explained in one sentence | All results recorded, no explanations | Results partially recorded | Missing |
| **Exercise correctness** | All four functions return correct output for all provided test cases including edge cases | Three functions correct | Two functions correct | One or zero |
| **Code quality** | `const` used correctly; `===` used throughout; functions named clearly; no `var` | Minor style issues | `var` used or `==` present | Significant issues |
| **Debugging** | All three bugs found and fixed; error message quoted and explained for each | Two bugs fixed with explanation | One bug fixed | Not attempted |
| **Reflection** | Specific and honest; references actual results | Addresses both prompts | Vague | Missing |
