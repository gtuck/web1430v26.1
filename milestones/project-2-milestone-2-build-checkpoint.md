# Project 2 Build – Milestone 2

**Due:** End of Week 12
**Points:** 30
**Category:** Projects (Milestone 2 of 3)

## Purpose

The heaviest checkpoint in the course, and deliberately so. [Project 2](../projects/project-2-data-driven-micro-app.md) states it plainly: Milestone 2 must represent a substantially complete application, because Weeks 13 and 14 are for polish, accessibility review, and deployment — not initial scaffolding. An incomplete Milestone 2 means an incomplete final submission.

## What to submit

A deployed version with **all** of the following:

- Vite project scaffolded, running, and deployed — `npm run dev` works and the live URL loads
- All five module files present (`api.js`, `normalize.js`, `render.js`, `state.js`, `events.js`), each with its one-sentence responsibility comment
- Fetch → normalize → render pipeline complete, with real API data passing through `normalizeData()` before any rendering function touches it
- Loading, success, and error states each producing distinct UI — not placeholder text
- At least **one** interaction type (search, filter, or sort) working end to end
- At least **one** `localStorage` feature reading and writing correctly, restoring on reload

Also commit `projects/project-2/checkpoint.md` with 3–5 sentences covering: which two features remain for Weeks 13–14, and any API quirks you hit during normalization and how you handled them.

**Submit to Canvas:** the live URL, your repository URL, and a link to `checkpoint.md`.

## How this is graded

- **All six requirements met (30)** — deployed, modular, one interaction and one persistence feature genuinely working
- **Five of six (25)**
- **Four of six (20)** — typically the persistence feature or the deployed URL is missing
- **Pipeline works locally but nothing is deployed (12)**
- **Scaffolding only (6)**
- **Not submitted (0)**

Before you submit, verify the four things the project brief lists: it works from the deployed URL and not only `npm run dev`; one interaction works end to end with real data; one persistence feature restores on reload; and your loading, error, and success states look visibly different.
