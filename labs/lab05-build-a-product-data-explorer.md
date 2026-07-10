# Lab 05 – Build a Product Data Explorer

## Purpose

Data modeling and DOM rendering are most useful when they work together. This lab asks you to define a structured dataset, write functions to filter and transform it, and render the results to the page — all without touching the data directly in your rendering code.

## Skills practiced

- Designing an array of objects with consistent structure
- Using `.filter()`, `.map()`, and `.find()` without mutating the source array
- Separating data, logic, and rendering into distinct functions
- Dynamically rendering a list of cards from a dataset
- Updating the DOM in response to a filter control

## What you're building

A **Campus Store Product Explorer** — a simple browser-based product browser that displays a list of products as cards and allows the user to filter by category. All data is hardcoded in a JavaScript file. No network requests are needed.

---

## Part 1: Data file

Create `labs/lab05/data.js`. Define and export (or just declare — use what you know) the following array. You may adjust product names and prices, but keep the structure exactly as shown:

```js
const products = [
  { id: 1, name: 'WEB 1430 Textbook', category: 'Books', price: 54.99, inStock: true },
  { id: 2, name: 'Campus Hoodie', category: 'Apparel', price: 39.99, inStock: true },
  { id: 3, name: 'Mechanical Keyboard', category: 'Electronics', price: 89.99, inStock: false },
  { id: 4, name: 'Introduction to Python', category: 'Books', price: 49.99, inStock: true },
  { id: 5, name: 'USB-C Hub', category: 'Electronics', price: 29.99, inStock: true },
  { id: 6, name: 'Campus Cap', category: 'Apparel', price: 24.99, inStock: true },
  { id: 7, name: 'Wireless Mouse', category: 'Electronics', price: 34.99, inStock: false },
  { id: 8, name: 'Data Structures Handbook', category: 'Books', price: 62.99, inStock: true },
  { id: 9, name: 'Laptop Sleeve', category: 'Accessories', price: 19.99, inStock: true },
  { id: 10, name: 'HDMI Cable', category: 'Accessories', price: 12.99, inStock: true },
];
```

---

## Part 2: Logic functions

In `labs/lab05/lab05.js`, write the following functions. Each must be a **pure function** — it should not modify `products` or any global state.

### `filterByCategory(productList, category)`

Returns a new array containing only products where `product.category === category`. If `category` is `'All'`, returns the full list unchanged.

### `getCategories(productList)`

Returns an array of unique category strings derived from the product list. The result should include `'All'` as the first element.

Example: `['All', 'Books', 'Apparel', 'Electronics', 'Accessories']`

Hint: use a `Set` to deduplicate: `[...new Set(productList.map(p => p.category))]`

### `formatPrice(amount)`

Returns a formatted price string: `49.99` → `'$49.99'`.

### `sortByPrice(productList, direction)`

Returns a new sorted array. `direction` is `'asc'` (lowest first) or `'desc'` (highest first). Do not mutate the original array — use `.slice()` before sorting.

---

## Part 3: Rendering functions

Write the following DOM functions. Use `createElement` and `textContent` — **no `innerHTML`**. (The DOM gets full coverage in Week 06; for now, reuse the "DOM preview" glue pattern from the top of Lab 04's Part 3 — select an element, create elements, set `textContent`, and `append`.)

### `renderProductCard(product)`

Creates and returns an `<article>` element with class `product-card` containing:
- Product name in an `<h2>`
- Category in a `<p>` with class `product-category`
- Formatted price in a `<p>` with class `product-price`
- A stock status indicator: a `<span>` reading "In Stock" or "Out of Stock", with class `in-stock` or `out-of-stock` accordingly
- A `<button>` reading "Add to Cart" that is `disabled` when `inStock` is `false`

### `renderProductList(productList, container)`

Clears `container` and appends a `renderProductCard(product)` for each product in the list. If the list is empty, display a `<p>` reading "No products found."

### `renderCategoryFilter(categories, container)`

Renders a `<select>` element into `container` with one `<option>` per category. The `value` of each option should equal the category string.

---

## Part 4: Wire it together

In `labs/lab05/index.html`, create a page with:
- A `<div id="filter-bar">` for the category filter select
- A `<select id="sort-order">` with options "Price: Low to High" and "Price: High to Low"
- A `<div id="product-grid">` for the product cards

In `labs/lab05/lab05.js`, on `DOMContentLoaded`:
1. Call `renderCategoryFilter(getCategories(products), filterBar)` to populate the filter
2. Call `renderProductList(products, productGrid)` to show all products initially
3. Add a `change` listener to the category filter: when it changes, filter the products and re-render the list
4. Add a `change` listener to the sort select: when it changes, apply the sort and re-render (preserving any active category filter)

---

## CSS requirements

In `labs/lab05/style.css`:
- Product cards display in a responsive grid (one column on mobile, three columns on desktop)
- Out-of-stock cards have a visually distinct appearance (e.g., reduced opacity, a strikethrough price, or a muted color scheme)
- The "Add to Cart" button looks disabled when the product is out of stock

---

## Deliverable

In `labs/lab05/`:
- `index.html`
- `lab05.js`
- `style.css`
- `notes.md`

Commit at least three times (after data + functions, after rendering, after wiring). Push and deploy.

Submit to Canvas: live URL, repo URL, notes.md link.

---

## Process reflection (in notes.md)

Answer in 4–6 sentences:
- What did your `getCategories` function look like before you used `Set`, and how did the approach change?
- What happened when you tried to sort the array in place with `.sort()` without `.slice()` first?
- How did you keep the active category filter applied when the sort order changed?

---

## Rubric

| Criterion | Excellent (4) | Proficient (3) | Developing (2) | Incomplete (1) |
|-----------|--------------|----------------|----------------|----------------|
| **Data functions** | All four functions correct and pure; source array never mutated | Three functions correct | Two correct | One or zero |
| **Rendering functions** | Cards render all fields correctly; empty state handled; no `innerHTML` | Cards render; one field missing or `innerHTML` used | Cards render but incomplete | Not functional |
| **Filter and sort** | Both controls work independently and together; active filter persists across sort changes | Both controls work separately | One control works | Neither works |
| **CSS layout** | Responsive grid; out-of-stock styling distinct; disabled button styled | Responsive grid; no out-of-stock styling | Single-column layout | No meaningful CSS |
| **Reflection** | Specific; addresses all three prompts | Two prompts addressed | Vague | Missing |
