# Week 06 Lecture Notes: Selecting, Creating, Updating, and Removing Elements

## Weekly focus

Taking a data array from Week 05 and rendering it into the live DOM — safely, cleanly, and dynamically.

## Why this matters

The DOM (Document Object Model) is the bridge between your JavaScript data and what the user actually sees. Without DOM manipulation, JavaScript has no way to update the page after it loads — no dynamic lists, no toggling panels, no live search results. Every framework (React, Vue, Svelte) is ultimately doing this same work under the hood; understanding the raw DOM API makes you a better framework user and a more capable debugger.

## Learning targets

- Select one or multiple elements using `querySelector` and `querySelectorAll`
- Create new elements with `createElement` and insert them using `append` and `prepend`
- Set element content safely using `textContent`, and understand when and why to avoid `innerHTML`
- Manipulate CSS classes with `classList.add`, `.remove`, `.toggle`, and `.contains`
- Read and write `data-*` attributes using the `dataset` API
- Navigate the DOM tree using `parentElement`, `children`, and `nextElementSibling`

## Core concepts

### querySelector and querySelectorAll

`document.querySelector(selector)` returns the first matching element, or `null` if none is found. `document.querySelectorAll(selector)` returns a static `NodeList` of all matching elements. Both accept any valid CSS selector string.

```js
const title = document.querySelector("h1");
const allCards = document.querySelectorAll(".product-card");

// querySelectorAll returns a NodeList, not an array
// Convert with Array.from to use .map(), .filter(), etc.
const cards = Array.from(allCards);
cards.forEach(card => console.log(card.textContent));
```

If `querySelector` returns `null` and you immediately try to access a property on it, you get a TypeError. Always check that the element exists, or make sure your script runs after the DOM is ready.

### createElement and inserting elements

`document.createElement(tagName)` creates a new element that is not yet attached to the page. Build it completely, then insert it. This is more efficient than inserting HTML strings and then selecting the result.

```js
function createProductCard(product) {
  const article = document.createElement("article");
  article.classList.add("product-card");

  const heading = document.createElement("h2");
  heading.textContent = product.name;

  const price = document.createElement("p");
  price.textContent = `$${product.price.toFixed(2)}`;

  article.append(heading, price);
  return article;
}

const container = document.querySelector("#product-list");
products.forEach(p => container.append(createProductCard(p)));
```

`append` adds a child at the end. `prepend` adds it at the beginning. Both accept multiple arguments.

### textContent vs innerHTML — and the XSS risk

`textContent` sets or reads the plain text content of an element. It treats the value as raw text, so angle brackets are displayed literally and never interpreted as HTML. Use it whenever you are inserting user-supplied or data-sourced content.

`innerHTML` sets or reads content as an HTML string. The browser parses it and creates real elements. This is powerful but dangerous: if the string contains user input, an attacker can inject a `<script>` tag or an event handler attribute. This is called a cross-site scripting (XSS) attack.

```js
const el = document.querySelector("#message");

// Safe — displayed as literal text, even if input contains <script>
el.textContent = userInput;

// Dangerous if userInput is not fully controlled
el.innerHTML = userInput; // never do this with untrusted data
```

If you must render HTML strings from a controlled source (your own data, not user input), `innerHTML` is acceptable. For anything typed by a user, always use `textContent`.

### Removing elements

Call `.remove()` directly on the element you want to delete. To clear all children from a container, set `textContent = ""` — that is the shortest safe approach.

```js
const card = document.querySelector(".product-card");
card.remove(); // removes the element from the DOM entirely

// Clear a list before re-rendering
const list = document.querySelector("#product-list");
list.textContent = "";
products.forEach(p => list.append(createProductCard(p)));
```

### classList: add, remove, toggle, contains

Rather than building CSS class strings by hand, use the `classList` API. Each method is atomic — it changes exactly one class without affecting others.

```js
const btn = document.querySelector("#menu-btn");
const nav = document.querySelector("#main-nav");

btn.addEventListener("click", () => {
  nav.classList.toggle("is-open");           // adds if absent, removes if present
  btn.classList.toggle("btn--active");

  const isOpen = nav.classList.contains("is-open");
  btn.setAttribute("aria-expanded", isOpen); // keep ARIA in sync
});
```

### dataset attributes

`data-*` attributes let you embed custom data directly in HTML elements. The `dataset` property on a DOM node exposes them as a plain object. Camel-case in JavaScript maps to hyphenated HTML: `dataset.productId` corresponds to `data-product-id`.

```js
// HTML: <button data-product-id="42" data-category="footwear">View</button>
const btn = document.querySelector("button");

console.log(btn.dataset.productId);  // "42" (always a string)
console.log(btn.dataset.category);   // "footwear"

// Use the id to look up the item in your data array
const id = Number(btn.dataset.productId);
const product = products.find(p => p.id === id);
```

`dataset` values are always strings. Convert to a number with `Number()` or `parseInt()` before comparing with `===` to a numeric id.

### DOM traversal

Sometimes you need to move from a known element to a related one without running another `querySelector`. These properties navigate the live DOM tree:

```js
const item = document.querySelector(".active-item");

const parent = item.parentElement;          // one level up
const siblings = parent.children;          // HTMLCollection of all children
const next = item.nextElementSibling;      // next sibling element
const prev = item.previousElementSibling; // previous sibling element
```

Traversal is useful inside event handlers when `event.target` gives you a child element and you need to reach the containing card or list item.

## Common mistakes

1. **Calling `querySelector` before the DOM is loaded.** If your `<script>` tag is in `<head>` without `defer`, the element does not exist yet and you get `null`. Add `defer` to your script tag or move it just before `</body>`.
2. **Using `innerHTML` with form input values.** Students often write `el.innerHTML = inputField.value` — this is the textbook XSS bug. Always use `textContent` for user-supplied content.
3. **Forgetting that `querySelectorAll` returns a NodeList, not an array.** `NodeList` has `.forEach` but not `.map` or `.filter`. Use `Array.from(nodeList)` to get a real array.
4. **Re-rendering without clearing the container first.** If you call a render function twice (e.g., on filter change), you get duplicate cards unless you clear the container with `list.textContent = ""` before appending.
5. **Reading `dataset` values as numbers without converting.** `dataset.productId === 42` is always `false` because `dataset` returns strings. Always convert: `Number(btn.dataset.productId) === 42`.

## Accessibility connection

`classList.toggle` is the right tool for show/hide patterns (accordions, modals, navigation menus), but toggling a CSS class is invisible to screen readers unless you also update ARIA state. When you toggle `is-open` on a nav, pair it with `setAttribute("aria-expanded", true/false)` on the button that controls it. Similarly, when you use `createElement` to render dynamic content, apply semantic elements (`<article>`, `<ul>`, `<button>`) rather than generic `<div>` tags — screen readers use those semantics to describe the page structure to non-visual users.

## Demo walkthrough

**Demo: Render and Filter a Product List**

1. Start with an HTML file containing `<div id="product-list"></div>` and `<button id="filter-btn">Show In-Stock Only</button>`.
2. In `demo-06.js`, define a `products` array of five objects (reuse the Week 05 data shape).
3. Write a `renderProducts(list)` function that clears `#product-list` and appends a card for each item. Each card is an `<article>` with an `<h2>` (name), `<p>` (price), and a `data-product-id` attribute.
4. Call `renderProducts(products)` on load to show all items.
5. Add a click listener to `#filter-btn`: on click, toggle between showing all products and in-stock only. Use a boolean variable `showingAll` to track state. Update the button's `textContent` to reflect the current action.
6. In DevTools, show the Elements panel updating live as the filter runs. Point out the `data-product-id` attributes.
7. Deliberately set `el.innerHTML = "<img src=x onerror=alert('XSS')>"` in the console to demonstrate why `textContent` is safer.

## Practice prompt

Build a page with a `<ul id="task-list"></ul>` and an `<input>`/`<button>` for adding tasks. Write an `addTask(text)` function that creates a `<li>` with the task text and a "Done" button. When "Done" is clicked, toggle a `.completed` CSS class on the `<li>` (style it with strikethrough in your CSS). Add a `data-created` attribute to each `<li>` storing the timestamp of when it was added (`Date.now()`). Log the timestamp to the console when the "Done" button is clicked.

## Bridge

Lab 06 asks you to build an interactive FAQ and tabs interface — both require `classList.toggle` for show/hide and `querySelector` for finding the right panel to reveal. Assignment 3 will have you render a data array into the DOM, which is exactly the `renderProducts` pattern from the demo. As you work, keep rendering and data logic in separate functions — that separation will make Assignment 3 much easier to debug and extend.
