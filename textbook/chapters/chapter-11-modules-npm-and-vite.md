# Chapter 11: Modules, NPM, and Vite

Modern front-end development is not a single HTML file with a script tag at the bottom. It is an organized collection of files with defined interfaces, managed dependencies, and a build process that prepares code for deployment. This chapter makes that infrastructure approachable.

## What this chapter is really about

This chapter gives you a working understanding of ES modules (how to split JavaScript across files with explicit imports and exports), NPM (how to install and manage third-party packages), and Vite (a development server and build tool that makes working with modules fast and simple). By the end, you will scaffold a Vite project, split code into modules, and produce a deployable build output.

## Key ideas

**ES module syntax** — each file is its own module with a private scope. Anything not exported is invisible to other files.

Named exports (a file can have many):
```js
// utils.js
export function formatPrice(amount) {
  return `$${amount.toFixed(2)}`;
}

export const TAX_RATE = 0.08;
```

Named imports:
```js
// main.js
import { formatPrice, TAX_RATE } from './utils.js';
```

Default exports (a file can have one):
```js
// ProductCard.js
export default function renderProductCard(product) {
  // ...
}
```

Default imports:
```js
import renderProductCard from './ProductCard.js';
```

**Import paths**:
- `'./utils.js'` — relative path, same directory
- `'../data/products.js'` — relative path, parent directory
- `'vue'` — an installed npm package (no `./`)

**NPM** (Node Package Manager) manages third-party packages. Key files and commands:

```bash
npm init vite@latest my-project   # scaffold a new Vite project
cd my-project
npm install                        # install all dependencies listed in package.json
npm run dev                        # start the Vite development server
npm run build                      # produce optimized output in the dist/ folder
```

**`package.json`** describes the project and its dependencies:

```json
{
  "name": "my-project",
  "scripts": {
    "dev": "vite",
    "build": "vite build"
  },
  "dependencies": {
    "vue": "^3.4.0"
  },
  "devDependencies": {
    "vite": "^5.0.0"
  }
}
```

`dependencies` — needed in production. `devDependencies` — only needed during development (build tools, linters).

**`.gitignore`** — always add these entries to avoid committing generated or large directories:

```
node_modules/
dist/
```

**Vite**'s dev server serves files from `src/`, watches for changes, and reloads the browser automatically. The `npm run build` command bundles and minifies everything into `dist/` for deployment.

**Why modules matter**: without modules, all JavaScript runs in a single global scope. Variables from one file can accidentally overwrite variables in another. With modules, each file has its own scope. Dependencies are explicit and traceable.

## Mental model

A module is a file with a defined interface: it declares what it shares (exports) and what it depends on (imports). This replaces the old pattern of loading 10 `<script>` tags in a specific order and hoping global variables don't collide.

Think of modules as LEGO bricks: each piece has a specific shape (its exports) and specific connection points (its imports). You compose the application by snapping pieces together, and each piece can be developed and tested independently.

The bundler (Vite) takes all your modules, resolves the imports, and produces a small number of optimized files that browsers can load efficiently. Your source code stays modular and readable; the deployed output is optimized for performance.

## Working habits

- `npm install` every time you clone a project or pull changes that modify `package.json`. Never commit `node_modules/`.
- Run `npm run dev` at the start of every session. Work against the live dev server, not by opening `index.html` directly in the browser (modules require a server to resolve relative imports).
- Add `node_modules/` and `dist/` to `.gitignore` before your first commit.
- Prefer named exports over default exports when a file exports more than one thing — named exports are easier to search for and rename.
- One file, one responsibility. If a file's purpose is hard to describe in one sentence, split it.
- Add a `README.md` for substantial projects. It should explain the audience/problem, setup steps, data source, and quality checks so another developer can run and understand the project without guessing.

## Common mistakes

- **Committing `node_modules/`**: it can contain tens of thousands of files and hundreds of megabytes. Always `.gitignore` it. Teammates install their own copy with `npm install`.
- **Circular imports** (A imports B, B imports A): causes initialization order problems and confusing errors. Restructure so dependencies flow one direction.
- **Exporting DOM references**: `export const button = document.querySelector('#btn')` fails because the DOM doesn't exist when modules are initialized. Export functions, not DOM elements.
- **Opening `index.html` directly in the browser** (with a `file://` URL): module imports don't work without a server. Always use `npm run dev`.
- **Confusing `dependencies` and `devDependencies`**: tools you only need to build the project (Vite, linters) go in `devDependencies`. Libraries your app uses at runtime (Vue, date-fns) go in `dependencies`.

## Accessibility and UX note

Build tooling doesn't change what users experience directly — but it does change what you can ship. A Vite build produces:
- Minified JavaScript (smaller files, faster load)
- Tree-shaken output (only the code you actually use is included)
- Hashed file names (allows browsers to cache files indefinitely and update automatically when files change)

For users on slow connections or low-powered devices, these optimizations meaningfully improve experience. The discipline of writing modular code also makes it easier to do performance work later — you can split large modules into smaller chunks that load on demand.

## Practice prompt

1. Scaffold a new Vite project: `npm create vite@latest` (choose Vanilla JavaScript, not a framework).
2. Add `node_modules/` and `dist/` to `.gitignore`.
3. Move your `formatPrice` function (or another utility from a previous chapter) into a file called `src/utils.js` and export it as a named export.
4. Import it in `src/main.js` and use it to format a price and log the result.
5. Move your book data array (from Chapter 5) into `src/data.js` and export it.
6. Import it in `main.js`, filter it, and render the results to the DOM.
7. Run `npm run dev` and verify it works. Run `npm run build` and inspect the `dist/` folder. What is different about the files there?
8. Add a short `README.md` that explains what the project does, how to run it, and which files matter most.

## Reflection

What changed about your workflow when you started using a dev server instead of opening a file directly? What does the `dist/` folder contain that `src/` does not? What happened when you forgot to run `npm install` before `npm run dev`?

## Vocabulary

- **module** — a JavaScript file with a private scope and explicit exports and imports
- **export** — making a value or function available to other modules
- **import** — bringing a value or function from another module into the current file
- **named export** — an export with a specific name that importers must use
- **default export** — an unnamed export; each file can have at most one
- **package.json** — a file that describes the project and lists its dependencies
- **npm** — Node Package Manager; the tool for installing and managing packages
- **node_modules** — the directory where npm installs packages (never committed to git)
- **bundler** — a tool that takes modular source files and combines them into optimized output
- **Vite** — a fast development server and bundler for modern JavaScript projects
- **dev server** — a local server that serves your files during development with hot reloading
- **build** — the process of producing optimized, deployable output from source files

## Mini checklist

- I can create a JavaScript module with named exports and import them in another file.
- I can scaffold a Vite project and understand the purpose of each generated file.
- I can run `npm run dev` to start the development server and `npm run build` to produce output.
- I can add `node_modules/` and `dist/` to `.gitignore` before committing.
- I can explain the difference between `dependencies` and `devDependencies`.
- I can explain why modules prevent naming collisions that occur with global script loading.
- I can write a short project `README.md` that helps another developer set up and understand my module-based project.
