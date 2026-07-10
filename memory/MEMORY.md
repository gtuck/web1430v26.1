# WEB 1430 Project Memory

Current as of July 10, 2026. `CONTEXT.md` carries the working rules; this file carries project state and history highlights.

## Project Summary

WEB 1430 is a complete, online-first **Client-Side Web Development** course package for Weber State University. The repository contains the authored course source plus a generated Canvas export package, verified through live Canvas imports in July 2026.

## Current Source of Truth

- Markdown files drive learner-facing course pages, briefs, lectures, labs, and support guides.
- `quizzes/*.json` drives quizzes and exams.
- `scripts/build_canvas_package.py` regenerates the Canvas HTML, assessment XML/QTI, and the `.imscc` package. Internal page links are emitted as `$WIKI_REFERENCE$/pages/<slug>` placeholders so Canvas resolves them on import.
- `scripts/build_canvas_rubrics_csv.py` regenerates `course/canvas-rubrics.csv` from the rubric tables in the briefs.
- Repo-maintenance and instructor-side files that do **not** feed the Canvas export: `reports/`, `memory/`, `CONTEXT.md`, `README.md`, `textbook/README.md`, `course/import_to_canvas.md`, `course/first-delivery-monitoring-guide.md`, `course/canvas-outcomes.csv`, `course/canvas-rubrics.csv`.

## Current Course Shape

- 14 textbook chapters (Chapter 8 is the Week 08 reading; every chapter is assigned to a week)
- 16 weekly module overviews and lecture notes (`week-00` through `week-15`)
- 14 labs, 6 assignments, 3 projects
- 8 quizzes, 1 midterm, 1 final — all selected-response, 1 point per item, points equal question counts

## Canvas Delivery Workflow (verified live, July 2026)

- Import `canvas/WEB1430-Canvas-Export.imscc` with Content Type **"Common Cartridge 1.x Package"** only. The "Canvas Course Export Package" option fails on every quiz and assignment. Leave "Convert content to New Quizzes" unchecked. Use a fresh course shell or Reset Course Content before re-importing.
- The institution has **no Canvas API access** (no tokens). All automation must use Canvas UI channels; never propose REST API tooling.
- Instructor-side setup after import (full checklist in `course/import_to_canvas.md`):
  1. Import `course/canvas-outcomes.csv` (Course > Outcomes > Import) — 10 outcomes in one group, ratings Excellent 4 / Proficient 3 / Developing 2 / Incomplete 1, mastery at Proficient.
  2. Import `course/canvas-rubrics.csv` (Course > Rubrics > Import Rubrics) — 24 rubrics from the briefs. Then manually attach the 9 assignment/project rubrics to their assignments and add outcome rows using the mapping table in the guide (CSV import cannot do either).
  3. Create the Week 05 / 11 / 13 anonymous survey forms and set up the monitoring workflow (`course/first-delivery-monitoring-guide.md`).

## Content State Highlights

- Content is aligned across source docs and the Canvas export; the export imports cleanly (pages, links, quizzes, assignments, groups).
- July 2026 accuracy pass: fixed textbook facts (CSS render-blocking vs parser-blocking; Lighthouse's four categories, PWA removed; Vue 3 named exports; JSON `null`), a Chapter 4 code-fence bug, the Week 08 lecture's midterm-format description (now matches the selected-response exam), and the Week 03 primitive-type count; added Chapter 8 to Week 08; added the DOM glue pattern to Labs 04–05 (used ahead of Week 06 by design); completed three rubric rows with empty Incomplete cells; added a GitHub Pages `base`-path note to Chapter 14; synced the course reflection prompt's rubric with the Final Project brief; corrected the Week 11 survey's Project 2 milestone reference (Milestone 2 build is due Week 12).
- Module overviews use week-specific checkpoint questions, time estimates, and harder-week struggle guidance. Surveys run Weeks 5, 11, and 13. Final Project milestones are visible in the schedule and late-course overviews, with a Week 12 planning starter and Week 13 revision milestone.
- Week 14 uses Lab 13 as applied QA evidence with Quiz 8 as a short readiness check. API briefs require a viability check; major projects require `README.md` documentation. Week 00 teaches `git status` / `git pull --ff-only`.
- The reports in `reports/` are current as of March 16, 2026 and predate the July 2026 pass.

## Key Files to Keep in Sync

- `course/schedule.md`, `modules/week-*-overview.md`, `assignments/*.md`, `projects/*.md`
- `syllabus.md` and `course/syllabus.md` (duplicated; must stay identical)
- `course/quiz-alignment.md` and `quizzes/*.json`
- `course/canvas-outcomes.csv` with `course/learning_outcomes.md`
- `course/canvas-rubrics.csv` with the briefs' rubric tables (regenerate via the script)
- generated Canvas outputs under `canvas/expanded_package/`

## Build / Verification Commands

```bash
python3 scripts/build_canvas_package.py build
python3 scripts/build_canvas_package.py build --check
python3 scripts/build_canvas_package.py validate
python3 scripts/build_canvas_rubrics_csv.py   # after any rubric-table change
```

## Working Assumptions

- Do not hand-edit generated Canvas HTML or assessment XML as the primary change path.
- If source content changes, rebuild the Canvas package before considering the repo synchronized.
- Keep both syllabus copies aligned; keep assignment/project `Due:` lines aligned with `course/schedule.md`; keep quiz JSON `points` equal to the sum of `questions[].points_possible`.
- Preserve the module-overview support pattern (time estimate, tailored checkpoint question, struggle guidance on hard weeks) and the four-level rubric format with every cell filled — the rubric tables are machine-parsed.
- If learner-facing support docs linked from modules or briefs change, rebuild the Canvas package.
- Already-imported Canvas courses do not update when the repo changes: either re-import into a fresh/reset shell or hand-edit the affected Canvas pages.

## Remaining Limitations

- Import verified manually, but no automated Canvas import smoke test exists; repo validation is package-level only.
- All exported assessment items are selected-response.
- No standalone early low-stakes checkpoints for DevTools or persistence (Week 14's Lab 13 is the main applied QA evidence).
- Survey forms and follow-up announcements require manual instructor execution.
- Rubric-to-assignment attachment and outcome rows are manual Canvas UI work after each fresh import (no API access).
- The build script assumes the existing Canvas assessment resource structure; brand-new assessments may need script updates.
- Main open instructional-design risk: late-term workload compression. Use first-delivery evidence before changing overlap or deadlines.
