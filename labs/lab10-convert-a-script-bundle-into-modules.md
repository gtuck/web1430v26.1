# Lab 10 – Convert a Script Bundle into Modules

## Purpose

Modules are not just a syntax change — they are a different way of thinking about how code is organized and how files relate to each other. This lab starts with a provided single-file script and asks you to decompose it into a proper Vite module project with clear file responsibilities and explicit imports and exports.

## Skills practiced

- Scaffolding a Vite project with `npm create vite@latest`
- Using named `export` and `import` syntax
- Splitting code by responsibility (data, utilities, rendering, events)
- Understanding module scope (no accidental globals)
- Running the Vite dev server and build
- Ignoring `node_modules/` and `dist/` in git

## What you're starting with

The file below represents a common beginner pattern: all the code in one place, no organization, global variables shared across functions. Your job is to refactor it into a modular Vite project — without changing what the app does.

**Provided `bundle.js` (read-only reference — do not submit this file):**

```js
// All code in one file — globals everywhere

const products = [
  { id: 1, name: 'Notebook', price: 4.99, category: 'Stationery' },
  { id: 2, name: 'USB Hub', price: 29.99, category: 'Electronics' },
  { id: 3, name: 'Hoodie', price: 39.99, category: 'Apparel' },
  { id: 4, name: 'Keyboard', price: 89.99, category: 'Electronics' },
  { id: 5, name: 'Sticky Notes', price: 3.49, category: 'Stationery' },
];

let activeCategory = 'All';

function formatPrice(amount) {
  return '$' + amount.toFixed(2);
}

function getCategories() {
  const cats = products.map(p => p.category);
  return ['All', ...new Set(cats)];
}

function filterProducts(category) {
  if (category === 'All') return products;
  return products.filter(p => p.category === category);
}

function renderCard(product) {
  const article = document.createElement('article');
  const h2 = document.createElement('h2');
  h2.textContent = product.name;
  const price = document.createElement('p');
  price.textContent = formatPrice(product.price);
  const cat = document.createElement('p');
  cat.textContent = product.category;
  article.append(h2, price, cat);
  return article;
}

function renderAll() {
  const grid = document.getElementById('product-grid');
  grid.replaceChildren();
  const filtered = filterProducts(activeCategory);
  filtered.forEach(p => grid.append(renderCard(p)));
}

function buildFilter() {
  const bar = document.getElementById('filter-bar');
  getCategories().forEach(cat => {
    const btn = document.createElement('button');
    btn.textContent = cat;
    btn.addEventListener('click', () => {
      activeCategory = cat;
      renderAll();
    });
    bar.append(btn);
  });
}

document.addEventListener('DOMContentLoaded', () => {
  buildFilter();
  renderAll();
});
```

---

## Part 1: Scaffold the Vite project

In your terminal, navigate to `labs/` inside your course repo and run:

```bash
npm create vite@latest lab10 -- --template vanilla
cd lab10
npm install
```

Open the project in VS Code. Delete the boilerplate content from `src/main.js` and `src/style.css`. You will replace them.

Add a `.gitignore` file in `lab10/` (if not already present) with:
```
node_modules/
dist/
```

Verify the dev server works: `npm run dev`. You should see a blank page with no errors.

---

## Part 2: Plan your module structure

Before writing any code, plan the file layout. Create this structure inside `lab10/src/`:

```
src/
  data.js       — the products array (exported)
  utils.js      — formatPrice, getCategories, filterProducts (exported)
  render.js     — renderCard, renderAll (imports from utils and data)
  events.js     — buildFilter, DOMContentLoaded handler (imports from render and utils)
  main.js       — entry point: imports from events.js and initializes the app
  style.css     — styles (linked in index.html)
```

Write a one-sentence comment at the top of each file before adding any code.

---

## Part 3: Move code into modules

### `src/data.js`

```js
// Provides the static product dataset for the application.

export const products = [
  { id: 1, name: 'Notebook', price: 4.99, category: 'Stationery' },
  { id: 2, name: 'USB Hub', price: 29.99, category: 'Electronics' },
  { id: 3, name: 'Hoodie', price: 39.99, category: 'Apparel' },
  { id: 4, name: 'Keyboard', price: 89.99, category: 'Electronics' },
  { id: 5, name: 'Sticky Notes', price: 3.49, category: 'Stationery' },
];
```

### `src/utils.js`

Move `formatPrice`, `getCategories`, and `filterProducts` here. Each must be a named export. `getCategories` and `filterProducts` accept `productList` as a parameter — remove the reference to the global `products` variable.

```js
// Pure utility functions for formatting and filtering product data.

export function formatPrice(amount) { ... }
export function getCategories(productList) { ... }
export function filterProducts(productList, category) { ... }
```

### `src/render.js`

Move `renderCard` and `renderAll` here. Import `formatPrice` from `utils.js`. Accept `productList` and `container` as parameters instead of querying the DOM inside the function.

```js
// Renders product cards and the product grid.
import { formatPrice } from './utils.js';

export function renderCard(product) { ... }

export function renderGrid(productList, container) {
  container.replaceChildren();   // safe way to clear all children
  productList.forEach(p => container.append(renderCard(p)));
}
```

### `src/events.js`

Move `buildFilter` here. Import what it needs. Accept the products array, active category state, and DOM containers as parameters — don't reach for globals.

```js
// Sets up filter button event listeners.
import { getCategories, filterProducts } from './utils.js';
import { renderGrid } from './render.js';

export function buildFilter(products, filterContainer, gridContainer) {
  getCategories(products).forEach(cat => {
    const btn = document.createElement('button');
    btn.textContent = cat;
    btn.addEventListener('click', () => {
      const filtered = filterProducts(products, cat);
      renderGrid(filtered, gridContainer);
    });
    filterContainer.append(btn);
  });
}
```

### `src/main.js`

The entry point wires everything together:

```js
// Entry point: initializes the product explorer on DOMContentLoaded.
import { products } from './data.js';
import { renderGrid } from './render.js';
import { buildFilter } from './events.js';
import './style.css';

document.addEventListener('DOMContentLoaded', () => {
  const filterBar = document.getElementById('filter-bar');
  const productGrid = document.getElementById('product-grid');

  buildFilter(products, filterBar, productGrid);
  renderGrid(products, productGrid);
});
```

---

## Part 4: Update `index.html`

Vite's `index.html` should reference `src/main.js` as a module:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Lab 10 – Product Explorer</title>
</head>
<body>
  <main>
    <h1>Campus Store</h1>
    <div id="filter-bar"></div>
    <div id="product-grid"></div>
  </main>
  <script type="module" src="/src/main.js"></script>
</body>
</html>
```

---

## Part 5: Run, build, and verify

1. `npm run dev` — the app should function identically to the original bundle
2. Test the filter buttons: each category should filter correctly
3. `npm run build` — should complete without errors
4. Inspect the `dist/` folder: note that the JavaScript has been bundled and minified

---

## Testing requirements

- [ ] App works identically to the original bundle (filter buttons, all products displayed)
- [ ] No global variables — all data flows through function parameters or imports
- [ ] Each file has a one-sentence comment at the top
- [ ] `node_modules/` and `dist/` are in `.gitignore`
- [ ] `npm run build` completes without errors
- [ ] The `dist/` folder is not committed to git

---

## Deliverable

Commit the `labs/lab10/` Vite project (excluding `node_modules/` and `dist/`). Push to GitHub.

Submit to Canvas: GitHub repo URL with a direct link to `labs/lab10/src/`, and either a Netlify/Vercel deployed URL (deploy the `dist/` output) or a screenshot of the running dev server.

---

## Process reflection (in `labs/lab10/notes.md`)

Answer in 4–6 sentences:
- What global variables did the original bundle rely on, and how did you eliminate them?
- What happened when you forgot `export` on a function you were trying to import?
- What does the `dist/` folder contain that `src/` does not, and who is it for?

---

## Rubric

| Criterion | Excellent (4) | Proficient (3) | Developing (2) | Incomplete (1) |
|-----------|--------------|----------------|----------------|----------------|
| **Module structure** | All five files present with correct responsibilities; one-sentence comments in each | Four files; mostly correct | Three files; some responsibilities mixed | Single file |
| **Import/export** | Named exports on all public functions; no global variables; imports use correct relative paths | Exports present; one global remains | Partial imports/exports | No module syntax |
| **Functionality** | App works identically to the bundle; filter works for all categories | App works; one filter issue | App partially works | App broken |
| **Build** | `npm run build` completes; `dist/` excluded from git | Build completes; dist committed | Build attempted | Not built |
| **Reflection** | Specific; all three prompts addressed | Two prompts | Vague | Missing |
