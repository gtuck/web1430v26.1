# Week 11 Lecture Notes: File Organization, ES Modules, and Build Tooling

## Weekly focus
Split a single-file JavaScript project into modules with clear responsibilities, and use Vite to run a development server and produce an optimized build.

## Why this matters
A single JavaScript file works fine for small projects, but it does not scale — global variables from one section collide with variables from another, it becomes impossible to know what depends on what, and loading one large file is slower than loading only what a page needs. ES Modules give you a standard, browser-native way to split code into focused files with explicit imports and exports. Build tools like Vite remove the friction from that workflow and add capabilities (hot reload, bundling, minification) that are standard in professional development environments.

## Learning targets
- Explain what global scope pollution is and why it is a problem in large projects
- Write named exports and default exports in a module file
- Import named and default exports into another file using correct syntax
- Explain what Vite provides and how it differs from opening an HTML file directly
- Initialize a Vite project from the command line and identify the role of `package.json` and `node_modules`
- Explain why `node_modules` belongs in `.gitignore`

## Core concepts

### The problem: global scope pollution
When all JavaScript lives in one file (or in multiple files loaded with `<script>` tags in HTML), every `var`, `function`, and `const` at the top level becomes a global variable on `window`. In a small project, that is manageable. In a larger one:

- Two files both define `function formatDate()` — one silently overwrites the other
- A utility function named `state` collides with a different file's `state` variable
- You cannot tell which parts of the code depend on which other parts
- Loading order matters, and getting it wrong causes `ReferenceError` at runtime

Modules solve this by giving each file its own scope. Nothing is global unless you explicitly export it and explicitly import it.

### ES module syntax: named exports
Named exports let a file expose multiple specific values. Any `const`, `function`, or `class` can be exported.

```js
// utils/format.js
export function formatDate(dateString) {
  return new Date(dateString).toLocaleDateString("en-US", {
    year: "numeric",
    month: "long",
    day: "numeric",
  });
}

export function formatCurrency(cents) {
  return `$${(cents / 100).toFixed(2)}`;
}
```

```js
// main.js
import { formatDate, formatCurrency } from "./utils/format.js";

console.log(formatDate("2025-03-15"));   // "March 15, 2025"
console.log(formatCurrency(1999));        // "$19.99"
```

The `{ }` braces in the import match the exported names exactly. Importing a name that was not exported causes a `SyntaxError`.

### ES module syntax: default exports
A default export represents the primary thing a file provides. A file can have only one default export.

```js
// components/card.js
export default function renderCard(item) {
  const article = document.createElement("article");
  article.className = "card";
  article.innerHTML = `
    <h2>${item.title}</h2>
    <p>${item.description}</p>
  `;
  return article;
}
```

```js
// main.js
import renderCard from "./components/card.js";

const card = renderCard({ title: "Hello", description: "World" });
document.getElementById("grid").append(card);
```

The import does not use `{ }` for default exports, and you can name it anything you want at the import site — though using the same name is clearest.

### Mixing named and default exports
A file can have both, and you can import both in one statement:

```js
import renderCard, { cardStyles, CARD_LIMIT } from "./components/card.js";
```

### Module scope
Inside a module, `const`, `let`, and `function` declarations are scoped to that file. They do not appear on `window`. Two modules can each define a `const state = {}` without interfering.

You also cannot use `import` or `export` in a regular `<script>` tag. You must use `<script type="module">`:

```html
<script type="module" src="./main.js"></script>
```

Without `type="module"`, the browser treats the file as a classic script and `import` statements cause a `SyntaxError`.

### What Vite does
Opening an HTML file directly (`file://`) works for simple pages, but modules and many browser APIs require a real HTTP server. Vite provides:

- **Dev server** — serves your project over `http://localhost:5173` so modules, fetch, and other APIs work correctly
- **Hot Module Replacement (HMR)** — when you save a file, only that module is swapped in the browser without a full reload; your app state is preserved
- **Build step** — `npm run build` produces a `dist/` folder with bundled, minified files ready for deployment
- **Zero configuration for vanilla JS** — no webpack config file needed; it works out of the box

Vite is not required to use ES modules, but it makes the developer experience significantly smoother.

### Scaffolding a Vite project
```bash
npm create vite@latest my-project -- --template vanilla
cd my-project
npm install
npm run dev
```

What this creates:
```
my-project/
  index.html         # entry point — loads main.js as a module
  main.js            # your JavaScript entry point
  style.css
  package.json       # project metadata and script definitions
  node_modules/      # installed packages — never commit this
  .gitignore         # already excludes node_modules
```

The `package.json` file records your project name, version, and the `scripts` block that defines `npm run dev` and `npm run build`.

### npm and package.json
`npm` (Node Package Manager) manages third-party libraries. When you run `npm install`, npm reads `package.json` and downloads every listed dependency into `node_modules/`.

Key concepts:
- `npm install <package>` — downloads a package and adds it to `package.json`
- `node_modules/` — can contain thousands of files; do not commit it
- `package-lock.json` — records exact versions installed; do commit this

### Why node_modules goes in .gitignore
`node_modules/` can be hundreds of megabytes and is entirely reproducible from `package.json` by running `npm install`. Committing it makes your repository enormous and creates constant merge conflicts. Any developer who clones your repository runs `npm install` and gets an identical copy of all dependencies. Vite's `.gitignore` template already excludes it.

## Common mistakes

1. **Using `import` in a `<script>` without `type="module"`.** The browser will throw `SyntaxError: Cannot use import statement outside a module`. Always add `type="module"` to any script tag that uses `import`.

2. **Importing with `{ }` braces for a default export (or without them for a named export).** Default exports: no braces. Named exports: braces with the exact exported name. Mixing these up is the most common module syntax error.

3. **Omitting the `.js` extension in import paths when not using a bundler.** When importing directly in the browser, the path must include the `.js` extension: `"./utils/format.js"`, not `"./utils/format"`. Vite relaxes this, but it is good practice to be explicit.

4. **Committing `node_modules/`.** If you see `node_modules/` appearing in `git status`, check that `.gitignore` includes it. Run `git rm -r --cached node_modules` to remove it from tracking without deleting the files.

5. **Confusing the Vite dev server port with a deployed site.** `localhost:5173` only works on your machine while `npm run dev` is running. To share or deploy the project, run `npm run build` and use the `dist/` folder.

## Accessibility connection
Module organization does not directly change what users experience, but it has real indirect accessibility benefits. When rendering logic is isolated in a dedicated module (like `card.js`), you can ensure that every rendered component includes proper semantic markup, ARIA attributes, and keyboard-accessible controls in one place — rather than replicating (and potentially forgetting) that work across many scattered locations. Build tooling also enables automated accessibility auditing as part of the build pipeline in more advanced setups.

## Demo walkthrough
1. Start with a single `main.js` that has validation helpers, rendering functions, and event handlers all in one place — approximately 80 lines.
2. Identify three groups: formatting utilities, DOM rendering functions, and app logic.
3. Create `utils/format.js` and move the formatting functions there with `export`.
4. Create `components/card.js` and move the render function there as a default export.
5. Update `main.js` to import from both files.
6. Show the browser — same output, cleaner code.
7. Run `npm run build`, open `dist/`, point out the single bundled and minified `assets/index-[hash].js`.
8. Show the Network tab comparing the dev server (multiple small module requests) to the build (one request).

## Practice prompt
Take the JavaScript from your Assignment 4 solution (the API viewer) and split it into at least three files:
- `api.js` — exports the fetch function (and nothing else)
- `render.js` — exports functions that build and insert DOM nodes
- `main.js` — imports from both and handles event listeners and app startup

Set up a Vite project, move your files in, run `npm run dev`, and verify everything still works. Then run `npm run build` and inspect the `dist/` folder.

## Bridge
Lab 10 has you do exactly this conversion on a provided single-file project — the practice prompt above is the same skill. Assignment 5 asks you to deliver your work as a Vite project with a proper module structure, so the `dist/` folder must build without errors before you submit. Starting in Week 12, you will build new features directly into modular projects rather than retrofitting them.
