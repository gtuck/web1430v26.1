# CLAUDE.md

This file provides project context for Claude Code and similar coding agents working in this repository.

## What this repository is

A source-driven course package for **WEB 1430: Client-Side Web Development** at Weber State University. The course is 4-credit, fully online, and asynchronous.

The repository now uses:

- Markdown as the source of truth for learner-facing course pages
- JSON in `quizzes/` as the source of truth for quizzes and exams
- `scripts/build_canvas_package.py` to regenerate the Canvas package and `.imscc`

## Source of truth and build workflow

Do not hand-edit generated files under `canvas/expanded_package/` unless you are explicitly debugging the export format. The normal workflow is to edit source files and rebuild.

Primary commands:

```bash
python3 scripts/build_canvas_package.py build
python3 scripts/build_canvas_package.py build --check
python3 scripts/build_canvas_package.py validate
```

The build script now regenerates:

- Canvas wiki HTML from Markdown sources
- assignment/project body HTML
- Canvas syllabus HTML
- module ordering metadata
- quiz/exam assessment metadata
- both QTI assessment variants in `canvas/expanded_package/`
- `canvas/WEB1430-Canvas-Export.imscc`

## Repository structure

| Directory | Contents |
|-----------|----------|
| `course/` | Syllabus, schedule, outcomes, Canvas import notes, published support guides, student surveys |
| `textbook/chapters/` | 14 Markdown chapters |
| `lectures/` | Weekly lecture notes (`week-00` through `week-15`) |
| `modules/` | Weekly module overviews (`week-00` through `week-15`) |
| `labs/` | 14 lab handouts (`lab00` through `lab13`) |
| `assignments/` | 6 assignment briefs |
| `projects/` | Project 1, Project 2, and Final Project briefs |
| `quizzes/` | 8 quizzes plus midterm and final exam source JSON |
| `canvas/` | Expanded Canvas package and importable `.imscc` |
| `reports/` | Analysis, review, and redesign reports |
| `memory/` | Project memory / current-state notes |

## Current course state

- The course content is substantive and aligned across source docs and Canvas export.
- Module overviews now include resource links and time estimates.
- Published support pages include the accessibility primer, API troubleshooting guide, screen reader testing guide, course reflection prompt, and Week 5 / Week 11 surveys.
- The weekly schedule and late-course module overviews now surface Final Project milestones instead of hiding that workload.
- Quizzes and exams now include stronger code-reading and debugging stems, although they still use selected-response item types.
- The Canvas assessment package is generated from `quizzes/*.json`, so quiz JSON is the canonical assessment source.

## Curriculum sequence and dependency rules

The course still follows a strict skill progression:

- Weeks 0-2: orientation, HTML, CSS, browser foundations, Git/GitHub workflow
- Weeks 3-5: JavaScript syntax, functions, arrays, objects, JSON
- Weeks 6-8: DOM, events, accessible forms, Project 1, midterm
- Weeks 9-11: Fetch API, async/await, APIs, storage/state, Project 2 preparation
- Weeks 12-14: modules, Vite, Vue 3 basics, accessibility synthesis, testing/performance/deployment
- Week 15: final presentation and final exam

Do not require students to use a concept before the course introduces it.

## Synchronization rules

When changing major course content, check these related files together:

- `course/schedule.md`
- `modules/week-*-overview.md`
- `assignments/*.md`
- `projects/*.md`
- `syllabus.md`
- `course/syllabus.md`
- `course/quiz-alignment.md`
- `quizzes/*.json`

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
- checkpoint question

### Rubric levels

Rubrics use exactly four levels:

- `Excellent`
- `Proficient`
- `Developing`
- `Incomplete`

### Assessment conventions

- `quizzes/*.json` is the assessment source of truth
- all current items are 1 point each
- the build expects supported selected-response question types
- applied reasoning is currently embedded through richer stems rather than separate free-response items

## Current known limitations

- No live Canvas import smoke test is performed from this repo; validation is package-level only.
- Assessments are stronger than before, but they are still selected-response only.
- `course/syllabus.md` drives the Canvas syllabus export, but `syllabus.md` also exists and must stay synchronized.
- The build script relies on the existing Canvas manifest/resource structure for the current assessment set; adding brand-new assessments may require extending that mapping.
