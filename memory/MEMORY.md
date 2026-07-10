# WEB 1430 Project Memory

## Project Summary

WEB 1430 is a complete, online-first **Client-Side Web Development** course package for Weber State University. The repository contains the authored course source plus a generated Canvas export package.

## Current Source of Truth

- Markdown files drive learner-facing course pages, briefs, lectures, labs, and support guides.
- `quizzes/*.json` drives quizzes and exams.
- `scripts/build_canvas_package.py` regenerates the Canvas HTML, assessment XML/QTI, and the `.imscc` package.
- Repo-maintenance files such as `reports/`, `memory/`, `CONTEXT.md`, `README.md`, `textbook/README.md`, `course/import_to_canvas.md`, and `course/first-delivery-monitoring-guide.md` do not feed the Canvas export.

## Current Course Shape

- 14 textbook chapters
- 16 weekly module overviews and lecture notes (`week-00` through `week-15`)
- 14 labs
- 6 assignments
- 3 projects
- 8 quizzes, 1 midterm, 1 final

## Important Current State

- The repo and Canvas package have already been synchronized after a broad content review.
- Week 5, Week 11, and Week 13 student surveys are now published and surfaced in the weekly flow.
- Week 13 and Week 14 now explicitly show Final Project milestones in the schedule and module overviews.
- The Final Project now uses a Week 12 planning starter and a Week 13 revised wireframe/data-plan milestone to reduce blank-page planning pressure.
- The accessibility primer and other support guides are now published into the Canvas package.
- The Vue transition is now supported by `course/vue-transition-guide.md`.
- Module overviews now use week-specific checkpoint questions instead of one repeated generic prompt.
- Harder weeks now include `What students usually struggle with` guidance.
- `Assignment 6`, `Project 2`, and the `Final Project` now include pacing/build-order support intended to reduce late-course student overload.
- Week 14 now treats Lab 13 as the main applied QA evidence and uses a shorter Quiz 8 readiness check.
- API-driven assignment/project briefs now require an API viability check.
- Major project briefs and syllabus docs now require lightweight `README.md` documentation.
- Week 00 materials now teach `git status` and `git pull --ff-only` as baseline sync/recovery habits, and repo visibility language now supports public or instructor-shared workflows.
- Textbook chapters 8, 9, 10, 11, and 14 were updated to align with these newer API, documentation, storage/privacy, and QA expectations.
- The root `README.md` now explicitly records which repo-maintenance files are safe to edit without affecting Canvas.
- Quiz/exam point totals are synchronized with question counts.
- Canvas pages for assignments/projects now come from the source briefs instead of summary stubs.
- Canvas assessment files are now generated from `quizzes/*.json`.
- Quiz 4, Quizzes 6-8, the Midterm, and the Final now include stronger code-reading/debugging stems.
- Instructor-side delivery support now includes `course/import_to_canvas.md` and `course/first-delivery-monitoring-guide.md`.
- The 10 course learning outcomes are available for Canvas Outcomes as `course/canvas-outcomes.csv` (imported manually via Course > Outcomes > Import; not carried by the `.imscc`). Ratings use the course rubric levels with mastery at Proficient (3). Keep the CSV in sync with `course/learning_outcomes.md`.
- Canvas rubrics come from `scripts/build_canvas_rubrics_csv.py`, which parses the rubric tables in the labs/assignments/projects briefs into `course/canvas-rubrics.csv` (24 rubrics, uploaded via Canvas's Rubrics > Import Rubrics). The CSV import is course-level only: attaching rubrics to the 9 graded assignments and adding outcome rows are manual UI steps, documented with a full rubric-to-outcome mapping table in `course/import_to_canvas.md`. If a brief's rubric table changes, regenerate the CSV, delete the affected Canvas rubric, and re-import.
- The institution has no Canvas API access (no API tokens available), so instructor-side automation must use Canvas UI features (CSV imports, .imscc) — never propose Canvas REST API tooling.
- The `.imscc` must be imported with Content Type "Common Cartridge 1.x Package"; the "Canvas Course Export Package" option fails on every quiz and assignment (verified July 2026, documented in `course/import_to_canvas.md`).
- The reports in `reports/` were refreshed on March 16, 2026 and now reflect the additional alignment pass that updated textbook/course consistency and repo-level documentation.
- A July 10, 2026 accuracy pass fixed: the Chapter 1 CSS parser-blocking claim (CSS blocks rendering, not parsing), a Chapter 4 code-fence formatting bug, the outdated five-category Lighthouse descriptions in Chapters 8 and 14 (Lighthouse now has four categories; PWA was removed), the invalid `import Vue from 'vue'` example in Chapter 11, the Week 08 lecture's midterm-format description (now matches the selected-response exam), and the Week 03 lecture's primitive-type count. Chapter 8 (previously assigned to no week) is now Week 08's chapter reading. Chapter 14 gained a short GitHub Pages `base`-path note to back Quiz 8. Labs 04/05 now include the DOM glue pattern students need before the DOM is formally taught in Week 06. Three rubric rows with empty Incomplete cells (Assignment 4, Lab 08, Lab 12) were completed.

## Key Files to Keep in Sync

- `README.md` for repo-maintenance guidance about what does and does not affect Canvas
- `course/schedule.md`
- `modules/week-*-overview.md`
- `assignments/*.md`
- `projects/*.md`
- `syllabus.md`
- `course/syllabus.md`
- `course/quiz-alignment.md`
- `quizzes/*.json`
- generated Canvas outputs under `canvas/expanded_package/`

## Build / Verification Commands

```bash
python3 scripts/build_canvas_package.py build
python3 scripts/build_canvas_package.py build --check
python3 scripts/build_canvas_package.py validate
```

## Working Assumptions

- Do not hand-edit generated Canvas HTML or assessment XML as the primary change path.
- If source content changes, rebuild the Canvas package before considering the repo synchronized.
- Keep both syllabus copies aligned.
- Keep assignment/project `Due:` lines aligned with `course/schedule.md`.
- Keep quiz JSON `points` aligned with the sum of `questions[].points_possible`.
- If you change module overviews, preserve the current student-support pattern: time estimate, tailored checkpoint question, and harder-week struggle guidance where appropriate.
- If you change learner-facing support docs linked from modules or briefs, rebuild the Canvas package so published pages stay in sync.

## Remaining Limitations

- Validation is repo/package-level only; there is still no live Canvas import smoke test in the repo.
- Assessment quality is improved, but all exported items are still selected-response.
- Week 14 QA evidence is stronger now, but earlier low-stakes applied checkpoints still do not exist.
- Survey/feedback workflows are documented, but live forms and follow-up announcements still require manual instructor execution.
- The build script currently assumes the existing Canvas assessment resource structure; adding brand-new assessments may need script updates.
- The main open instructional-design risk is still late-term workload compression; use first-delivery evidence before changing overlap or deadlines.
