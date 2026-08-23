# Lab Starter Files

Each folder here contains starter files for the corresponding lab. These are the same files that come pre-loaded in your course repository (created for you in the `web1430-fall26` organization from the course template), so you normally do **not** need to copy anything — the starter for each lab is already at `labs/labXX/` in your repo. This folder is the reference copy: if you ever delete or break a starter file, restore it by copying from here into `labs/labXX/`.

| Lab | Starter files | Notes |
|-----|--------------|-------|
| `lab00/` | `index.html` | Minimal HTML shell for your first commit |
| `lab01/` | `notes-template.md` | Fill this in during your inspection |
| `lab02/` | `index.html`, `style.css` | Pre-filled HTML content + CSS skeleton with TODOs |
| `lab03/` | `index.html`, `lab03.js`, `debug.js` | Function stubs + intentionally broken code for Part 3 |
| `lab04/` | `index.html`, `lab04.js` | HTML structure + trails data + function stubs |
| `lab05/` | `index.html`, `data.js` | HTML structure + products array |
| `lab06/` | `index.html` | Accordion and tabs HTML structure with real content |
| `lab07/` | `index.html`, `lab07.js` | Full form HTML + validation stubs |
| `lab08/` | `index.html`, `lab08.js` | Search page HTML + async function stubs |
| `lab09/` | `index.html`, `lab09.js` | Preferences page HTML + storage stubs |
| `lab10/` | `index.html`, `bundle.js` | Monolithic script to refactor into modules |
| `lab11/` | *(none)* | Scaffold with `npm create vite@latest lab11 -- --template vue` |
| `lab12/` | *(none)* | Scaffold with `npm create vite@latest lab12 -- --template vue` |
| `lab13/` | *(none)* | Audit lab — use one of your deployed projects from Labs 05 or 08 |

## How to use a starter

1. Open `labs/labXX/` in your course repo — the starter files are already there (restore from this folder only if something is missing)
2. Read the lab instructions before opening any file
3. TODOs and stub comments mark the parts you need to implement
4. Do not modify provided data arrays or HTML structure unless the lab explicitly says to

## Scaffolding Labs 11 and 12 (Vite + Vue)

Labs 11 and 12 have no starter files — you scaffold the project yourself using Vite. Run these commands in your terminal from inside your course repository:

### Lab 11

```bash
npm create vite@latest lab11 -- --template vue
cd lab11
npm install
npm run dev
```

After scaffolding, clean up the default files:

1. Delete `src/components/HelloWorld.vue`
2. Replace the contents of `src/App.vue` with a minimal shell:
   ```vue
   <script setup></script>
   <template>
     <main>
       <h1>Lab 11</h1>
     </main>
   </template>
   ```
3. Add these lines to `.gitignore` if they aren't already there:
   ```
   node_modules/
   dist/
   ```
4. Open `http://localhost:5173` in your browser to confirm Vite is running.

### Lab 12

```bash
npm create vite@latest lab12 -- --template vue
cd lab12
npm install
npm run dev
```

Apply the same cleanup steps as Lab 11. Then read the Lab 12 instructions before writing any components.

### Common Vite troubleshooting

- **"command not found: npm"** — Node.js is not installed. Download the current LTS version (Node 22) from nodejs.org. Node 22.12 or higher is required; Vite will not run on older versions.
- **Port 5173 already in use** — Another Vite dev server is running. Stop it with Ctrl+C in the other terminal, or Vite will automatically pick the next available port.
- **Changes not showing in browser** — Vite's hot module replacement (HMR) updates automatically. If you don't see changes, check the terminal for errors.
- **`dist/` folder appears after `npm run build`** — This is the production build output. Do not commit it; it is already in `.gitignore`.
