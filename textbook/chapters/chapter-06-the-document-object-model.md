# Chapter 6: The Document Object Model

The DOM is the live, scriptable representation of your page. Every element is an object. JavaScript can read it, modify it, add to it, and remove from it — and any change is immediately reflected in the browser.

## What this chapter is really about

This chapter teaches you how to select elements, read and change their content, manipulate their classes, and create new elements dynamically. It also teaches you what *not* to do: avoid `innerHTML` with user data, avoid selecting inside loops, and avoid writing JavaScript that is tightly coupled to fragile HTML structure.

## Key ideas

**Selecting elements** — use `querySelector` and `querySelectorAll`:

```js
const heading = document.querySelector('h1');              // first match
const items = document.querySelectorAll('.list-item');     // all matches (NodeList)
const btn = document.querySelector('#submit-btn');         // by ID
```

`querySelectorAll` returns a `NodeList`, not an array. You can iterate it with `for...of`, but it doesn't have `.map()` or `.filter()`. Convert with `Array.from(items)` or the spread operator `[...items]` if you need those methods.

**Reading and setting content**:

```js
heading.textContent = 'New Heading';         // safe — treats value as text
heading.innerHTML = '<em>New</em> Heading';  // unsafe with user input — can run scripts
```

Prefer `textContent` for plain text. Use `innerHTML` only when you control the content entirely and need embedded HTML structure. If you absolutely must render HTML from an untrusted or remote source, use an HTML sanitization library like DOMPurify first.

**Manipulating classes**:

```js
element.classList.add('active');
element.classList.remove('hidden');
element.classList.toggle('expanded');
element.classList.contains('active');   // returns true or false
```

Let CSS do the visual work. Add and remove classes with JavaScript; define what those classes look like in CSS.

**Creating and adding elements**:

```js
const card = document.createElement('div');
card.classList.add('card');
card.textContent = 'Hello';

const list = document.querySelector('.card-list');
list.append(card);      // adds to the end
```

**Reading form input values**:

```js
const input = document.querySelector('#search-input');
const value = input.value.trim();
```

**Waiting for the DOM to load** — if your script is in `<head>`, use `DOMContentLoaded`:

```js
document.addEventListener('DOMContentLoaded', () => {
  // safe to query the DOM here
});
```

Or place your `<script>` tag at the bottom of `<body>`, just before `</body>`, so the DOM is already built when the script runs.

## Mental model

The DOM is a live mirror of the document. When you call `document.createElement()` and `append()`, the new element appears on the page immediately. When you remove an element with `.remove()`, it disappears immediately. The DOM is always synchronized with what the user sees.

Think of DOM manipulation as working in two stages: (1) **select** the elements you need (store them in `const` variables at the top of your script), then (2) **operate** on them inside event handlers or functions. Selecting inside a handler that runs repeatedly is wasteful — select once, use many times.

## Working habits

- Select elements once and store in `const` variables at the top of your script or function.
- Never set `innerHTML` with user-supplied data — this creates a cross-site scripting (XSS) vulnerability. Use `textContent` instead, or `createElement` for structured content.
- Add and remove CSS classes rather than setting `style` attributes directly. It keeps styling in CSS and logic in JavaScript.
- When building a list of items from an array, use `createElement` and `append` in a loop rather than building a giant `innerHTML` string.
- Verify element selection worked before calling methods on it. If `querySelector` finds nothing, it returns `null`, and calling `.classList` on `null` throws a TypeError.

## Common mistakes

- **Selecting before the DOM loads**: a `<script>` in `<head>` runs before the `<body>` is parsed. `querySelector` returns `null` for everything. Fix: move the script to the end of `<body>`, or use `DOMContentLoaded`.
- **Setting `innerHTML` with user data**: if a user types `<script>alert('xss')</script>` into a field and you insert it with `innerHTML`, the script runs. Always use `textContent` for user-supplied strings.
- **Selecting inside a loop**: `document.querySelector('.list')` inside a loop that runs 100 times queries the DOM 100 times. Select once before the loop.
- **Tight coupling to HTML structure**: if your JavaScript depends on `document.querySelector('.sidebar > nav > ul > li:first-child')`, a small HTML change breaks everything. Select by ID or semantic class name instead.
- **Forgetting that `querySelectorAll` returns a NodeList, not an array**: you can't call `.map()` on a NodeList directly.

## Accessibility and UX note

Dynamically added content must be accessible. Elements created with `createElement` are not automatically announced by screen readers unless they are added to an `aria-live` region or focus is moved to them. Interactive elements (buttons, links, form controls) must be keyboard-reachable — a `<div>` with a click handler is not, but a `<button>` is. When you add a new piece of content that represents the result of a user action (a confirmation message, a search result), consider where keyboard focus should go next.

## Practice prompt

Given a plain HTML page with an empty `<ul id="task-list">` and an `<input id="task-input">` and a `<button id="add-btn">`:

1. Store all three elements in `const` variables at the top of your script.
2. When the button is clicked, read the input value (trimmed). If it is non-empty, create a new `<li>` element using `createElement`, set its `textContent` to the input value, and `append` it to the list. Then clear the input.
3. If the input is empty, add a visible error message without using `innerHTML`.
4. Add a "Remove" `<button>` inside each `<li>` that removes that item when clicked.

Do not use `innerHTML` anywhere.

## Reflection

What happened when you tried to select an element before the DOM was ready? What is the difference between `textContent` and `innerHTML`, and what would happen if a user typed `<b>bold</b>` into the input with each approach? Why is it safer to add and remove CSS classes from JavaScript rather than directly setting `style.color` or `style.display`?

## Vocabulary

- **DOM** — Document Object Model; the live, scriptable tree of objects representing the page
- **node** — any object in the DOM tree (elements, text nodes, comment nodes)
- **element** — an HTML tag represented as a DOM node
- **selector** — a CSS-style string used to target elements (`'h1'`, `'#id'`, `'.class'`)
- **querySelector** — returns the first element matching a selector, or `null`
- **querySelectorAll** — returns a NodeList of all elements matching a selector
- **classList** — an interface for adding, removing, toggling, and checking CSS classes
- **textContent** — the plain text content of an element (safe for user data)
- **innerHTML** — the HTML markup inside an element (dangerous with user data)
- **createElement** — creates a new DOM element that can be appended to the document
- **append** — adds a node or string to the end of an element's children
- **DOMContentLoaded** — an event that fires when the HTML is fully parsed and the DOM is ready

## Mini checklist

- I can select elements with `querySelector` and `querySelectorAll` and store them in `const` variables.
- I can set element text content using `textContent` (not `innerHTML`) for user-supplied values.
- I can add, remove, and toggle CSS classes with `classList`.
- I can create new elements with `createElement`, set their content, and `append` them to the DOM.
- I can explain why `innerHTML` with user input is a security risk.
- I can ensure my script runs after the DOM is ready.
