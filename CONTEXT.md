# CONTEXT.md

This file provides project context for Claude Code and similar coding agents working in this repository.

## What this repository is

A source-driven course package for **WEB 1430: Client-Side Web Development** at Weber State University. The course is 4-credit, fully online, and asynchronous.

The repository uses:

- Markdown as the source of truth for learner-facing course pages
- JSON in `quizzes/` as the source of truth for quizzes and exams
- `scripts/build_canvas_package.py` to regenerate the Canvas package and `.imscc`
- `scripts/build_canvas_rubrics_csv.py` to regenerate `course/canvas-rubrics.csv` from the rubric tables in the briefs

## Source of truth and build workflow

Do not hand-edit generated files under `canvas/expanded_package/` unless you are explicitly debugging the export format. The normal workflow is to edit source files and rebuild.

Primary commands:

```bash
python3 scripts/build_canvas_package.py build
python3 scripts/build_canvas_package.py build --check
python3 scripts/build_canvas_package.py validate
```

The build script regenerates:

- Canvas wiki HTML from Markdown sources (internal links are emitted as `$WIKI_REFERENCE$/pages/<slug>` placeholders, where the slug is the Canvas-style slugified page title — plain relative links break on import)
- assignment/project body HTML
- Canvas syllabus HTML
- module ordering metadata
- quiz/exam assessment metadata
- both QTI assessment variants in `canvas/expanded_package/`
- `canvas/WEB1430-Canvas-Export.imscc`

## Canvas import constraints (verified July 2026)

- The `.imscc` must be imported with Content Type **"Common Cartridge 1.x Package"**. The "Canvas Course Export Package" option invokes a different Canvas converter that fails on every quiz and assignment in this generated package.
- "Convert content to New Quizzes" must stay unchecked (quizzes are Classic Quiz QTI).
- Re-imports should target a fresh course shell or follow Reset Course Content, so page links resolve to the new copies rather than duplicate `-2` page URLs.
- The instructor has **no Canvas API access** (no tokens available at the institution). All Canvas automation must use UI channels: the `.imscc` import, the Outcomes CSV import, and the Rubrics CSV import. Never build Canvas REST API tooling.
- Instructor-side setup after import is documented in `course/import_to_canvas.md`: outcomes CSV, rubrics CSV plus manual rubric-to-assignment attachment and outcome rows (a full mapping table is in that guide), survey forms, and the monitoring workflow.

## Repository structure

| Directory | Contents |
|-----------|----------|
| `course/` | Syllabus, schedule, outcomes, Canvas import notes, published support guides, student surveys, and the Canvas Outcomes/Rubrics import CSVs |
| `textbook/chapters/` | 14 Markdown chapters |
| `lectures/` | Weekly lecture notes (`week-00` through `week-15`) |
| `modules/` | Weekly module overviews (`week-00` through `week-15`) |
| `labs/` | 14 lab handouts (`lab00` through `lab13`) |
| `assignments/` | 6 assignment briefs |
| `projects/` | Project 1, Project 2, and Final Project briefs |
| `quizzes/` | 8 quizzes plus midterm and final exam source JSON |
| `canvas/` | Expanded Canvas package and importable `.imscc` |
| `scripts/` | Canvas package build/validation tool and rubrics CSV generator |
| `reports/` | Analysis, review, and redesign reports |
| `memory/` | Project memory / current-state notes |

## Canvas export boundary

These files or folders are repo-maintenance or instructor-side content and are **not** included in the Canvas export:

- `reports/`
- `memory/`
- `CONTEXT.md`
- `README.md`
- `textbook/README.md`
- `course/import_to_canvas.md`
- `course/first-delivery-monitoring-guide.md`
- `course/canvas-outcomes.csv` and `course/canvas-rubrics.csv` (uploaded to Canvas separately, via the Outcomes and Rubrics import features)

These sources **do** feed the Canvas export:

- `home.md`
- `course/syllabus.md`
- `textbook-table-of-contents.md`
- everything in `textbook/chapters/`
- everything in `lectures/`
- everything in `modules/`
- everything in `labs/`
- everything in `assignments/`
- everything in `projects/`
- published learner-support pages in `course/` that are included by `PUBLISHED_COURSE_GUIDES` in `scripts/build_canvas_package.py`

## Current course state

- The course content is substantive and aligned across source docs and Canvas export, and the export has been verified through live Canvas imports (July 2026): pages, internal links, quizzes, assignments, and assignment groups all import cleanly under the Common Cartridge 1.x content type.
- A July 2026 accuracy pass corrected textbook facts (CSS is render-blocking rather than parser-blocking; Lighthouse has four categories, PWA removed; Vue 3 has no default export; JSON values include `null`), assigned previously-orphaned Chapter 8 as the Week 08 reading, aligned the Week 08 lecture's exam-format description with the selected-response midterm, added the DOM starter pattern Labs 04–05 need before the DOM is formally taught in Week 06, and completed three rubric rows that had empty Incomplete cells.
- Module overviews include resource links, time estimates, week-specific checkpoint questions, and harder-week `What students usually struggle with` guidance.
- Published support pages include the accessibility primer, API troubleshooting guide, screen reader testing guide, course reflection prompt, Week 5 / Week 11 / Week 13 surveys, and the Vue transition guide. The course reflection prompt's rubric matches the Final Project brief's reflection rubric verbatim.
- The weekly schedule and late-course module overviews surface Final Project milestones; `Assignment 6`, `Project 2`, and the `Final Project` include pacing/build-order guidance; the Final Project uses a Week 12 planning starter followed by Week 13 revision work.
- Week 14 assessment leans on Lab 13 as applied QA evidence, with Quiz 8 as a short readiness check.
- Quizzes and exams include code-reading and debugging stems, though all items are selected-response.
- API-driven assignments and projects require an API viability check (browser access, rate limits/auth, attribution/terms, data reliability); major project briefs and syllabus docs require lightweight `README.md` documentation.
- Week 00 materials teach `git status` and `git pull --ff-only` as baseline sync/recovery habits; repo policy supports public or instructor-shared workflows.
- The 10 course learning outcomes are packaged for Canvas as `course/canvas-outcomes.csv`; the 24 rubrics (from the briefs' rubric tables) are packaged as `course/canvas-rubrics.csv`, regenerable via `scripts/build_canvas_rubrics_csv.py`.
- The reports in `reports/` are current as of March 16, 2026 and predate the July 2026 accuracy/import pass; `memory/MEMORY.md` carries the newer state.

## Curriculum sequence and dependency rules

The course follows a strict skill progression:

- Weeks 0-2: orientation, HTML, CSS, browser foundations, Git/GitHub workflow
- Weeks 3-5: JavaScript syntax, functions, arrays, objects, JSON
- Weeks 6-8: DOM, events, accessible forms, Project 1, midterm
- Weeks 9-11: Fetch API, async/await, APIs, storage/state, Project 2 preparation
- Weeks 12-14: modules, Vite, Vue 3 basics, accessibility synthesis, testing/performance/deployment
- Week 15: final presentation and final exam

Do not require students to use a concept before the course introduces it. (Known accepted exception: Labs 04–05 and Assignment 2 use a minimal provided DOM/event glue pattern ahead of Week 06; the pattern is supplied in Lab 04.)

## Synchronization rules

When changing major course content, check these related files together:

- `course/schedule.md`
- `modules/week-*-overview.md`
- `assignments/*.md`
- `projects/*.md`
- `course/*.md` support docs when linked from modules or briefs
- `syllabus.md`
- `course/syllabus.md`
- `course/quiz-alignment.md`
- `quizzes/*.json`
- `course/canvas-outcomes.csv` when `course/learning_outcomes.md` changes
- `course/canvas-rubrics.csv` (regenerate with `scripts/build_canvas_rubrics_csv.py`) when any rubric table in a brief changes

If you change any source content that feeds Canvas, rebuild and validate the package before finishing.

## Content conventions

### Module overview format

Each `modules/week-NN-overview.md` should include:

- theme
- lecture reference
- lab reference when applicable
- deliverables list
- resources list
- time estimate
- five-step success plan
- checkpoint question tailored to the week's core concept

For the more difficult or higher-risk weeks, module overviews should also include a short `What students usually struggle with` section that names the most common failure point or prioritization mistake.

### Rubric levels

Rubrics use exactly four levels:

- `Excellent`
- `Proficient`
- `Developing`
- `Incomplete`

Every rubric row must have all four cells filled (4/3/2/1 points). These tables are parsed by `scripts/build_canvas_rubrics_csv.py`, so keep the `| Criterion | Excellent (4) | Proficient (3) | Developing (2) | Incomplete (1) |` header format.

### Assessment conventions

- `quizzes/*.json` is the assessment source of truth
- all current items are 1 point each
- the build expects supported selected-response question types
- applied reasoning is embedded through richer stems rather than separate free-response items

## Current known limitations

- Canvas import has been verified manually (July 2026), but there is still no automated import smoke test; repo validation is package-level only.
- Assessments are all selected-response.
- Week 14 has applied QA evidence via Lab 13, but there are no standalone earlier low-stakes checkpoints for DevTools or persistence.
- Survey/feedback workflows are documented, but the live forms and follow-up announcements require manual instructor setup and execution.
- `course/syllabus.md` drives the Canvas syllabus export, but `syllabus.md` also exists and must stay synchronized.
- The build script relies on the existing Canvas manifest/resource structure for the current assessment set; adding brand-new assessments may require extending that mapping.
- Rubric and outcome attachment in Canvas (rubrics to assignments, outcome rows on rubrics) is manual UI work after each fresh import — no API access exists to automate it.
- The main open instructional-design question is late-term workload compression; use first-delivery evidence before changing deadlines or milestone overlap.
