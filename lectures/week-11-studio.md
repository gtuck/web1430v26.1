# Week 11 Studio Notes: Modularization Studio and Vite Setup

## Session focus

Session 1 split a script into ES modules and introduced Vite. Session 2 performs that conversion on real code in the Lab 10 studio and checks in on Assignment 5, which is the same move at a larger scale.

## Before class

- Skim the Lab 10 starter and note which functions belong together. Grouping is the design decision; `export` is just the syntax.
- Run `npm create vite` once on your own machine so installation problems surface before the session, not during it.

## Studio plan

1. **Scaffold and run (10 min).** `npm create vite`, install, `npm run dev`. Confirm your Node version meets Vite's requirement first — a version error here looks nothing like a version error.
2. **Draw the module boundaries (15 min).** Group the starter's functions on screen before touching a file. Boundaries first, `export` statements second.
3. **Lab 10 conversion studio (30 min).** Move functions out, add named exports, fix imports until the console is clean. Expect the module-scope surprise: what used to be global is not any more, and that is the feature.
4. **Assignment 5 check-ins and survey (20 min).** Short reviews of in-progress refactors. Complete the Late-Course Check-In Survey afterwards — the responses shape how the last four weeks run.

The virtual section runs this plan live, Wednesday 9:30–10:45 AM (75 minutes). The online section works the same sequence self-paced; where the plan says "the room" or "a volunteer," use the Help & Questions discussion board.

## Accessibility connection

Module organization does not directly change what users experience, but it has real indirect accessibility benefits. When rendering logic is isolated in a dedicated module (like `card.js`), you can ensure that every rendered component includes proper semantic markup, ARIA attributes, and keyboard-accessible controls in one place — rather than replicating (and potentially forgetting) that work across many scattered locations. Build tooling also enables automated accessibility auditing as part of the build pipeline in more advanced setups.

## Practice prompt

Take the JavaScript from your Assignment 4 solution (the API viewer) and split it into at least three files:
- `api.js` — exports the fetch function (and nothing else)
- `render.js` — exports functions that build and insert DOM nodes
- `main.js` — imports from both and handles event listeners and app startup

Set up a Vite project, move your files in, run `npm run dev`, and verify everything still works. Then run `npm run build` and inspect the `dist/` folder.

## Bridge

Lab 10 has you do exactly this conversion on a provided single-file project — the practice prompt above is the same skill. Assignment 5 asks you to deliver your work as a Vite project with a proper module structure, so the `dist/` folder must build without errors before you submit. Starting in Week 12, you will build new features directly into modular projects rather than retrofitting them.
