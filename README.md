# WEB 1430: Client-Side Web Development

This repository contains a fully rebuilt, online-first **WEB 1430** course package designed for Canvas and a GitHub-based workflow.

Recent alignment work also updated:

- Week 00 Git/GitHub materials to teach `git status` and `git pull --ff-only` as baseline sync/recovery habits
- API-driven assignments and projects to require an API viability check (CORS, rate limits/auth, attribution/terms, data reliability)
- major project briefs and syllabus docs to require lightweight `README.md` documentation
- Week 14 quality-assurance materials so Lab 13 functions as applied QA evidence alongside a shorter Quiz 8 readiness check
- textbook chapters 8, 9, 10, 11, and 14 so the textbook matches current assignment, project, and QA expectations
- a July 2026 accuracy pass (see `memory/MEMORY.md` for the itemized list): textbook fact corrections, Chapter 8 assigned to Week 08, exam-format alignment in the Week 08 lecture, DOM starter patterns in Labs 04–05, rubric-table completions, Canvas-resolvable wiki links in the export, and instructor-side Canvas Outcomes/Rubrics import files

## Included

- original textbook with 14 chapters
- weekly lecture notes and module overviews
- labs
- assignments
- projects
- quizzes and exams in Canvas-compatible QTI/Common Cartridge structure
- published learner-support guides and student survey question banks
- first-delivery monitoring and Canvas import/setup documentation
- Canvas course export package (`canvas/WEB1430-Canvas-Export.imscc`)
- expanded Canvas package snapshot (`canvas/expanded_package/`)

## Repository structure

- `course/` – syllabus, schedule, outcomes, grading
  - includes support guides, survey question banks, and first-delivery monitoring docs
  - includes `canvas-outcomes.csv` and `canvas-rubrics.csv` for Canvas's Outcomes and Rubrics import features
- `textbook/` – original textbook chapters
- `lectures/` – weekly lecture notes
- `modules/` – weekly overview pages
- `labs/` – lab handouts
- `assignments/` – assignment briefs
- `projects/` – project briefs
- `quizzes/` – source JSON for quiz content
- `canvas/` – exploded package and importable IMSCC
- `scripts/` – Canvas build and validation tools, plus `build_canvas_rubrics_csv.py`, which regenerates `course/canvas-rubrics.csv` from the rubric tables in the briefs

## Safe to edit without affecting Canvas

These repo-maintenance files and folders are **not** included in the Canvas export package, so editing them will not change the generated learner-facing Canvas content:

- `reports/`
- `memory/`
- `CONTEXT.md`
- `README.md`
- `textbook/README.md`
- `course/first-delivery-monitoring-guide.md`
- `course/import_to_canvas.md`
- `course/canvas-outcomes.csv` and `course/canvas-rubrics.csv` (instructor-side Canvas imports, uploaded separately from the `.imscc`)

If you edit `home.md`, `course/syllabus.md`, `textbook-table-of-contents.md`, anything in `textbook/chapters/`, `lectures/`, `modules/`, `labs/`, `assignments/`, `projects/`, or the published learner-support guides in `course/`, those changes **do** affect the Canvas export.

## Canvas build workflow

Regenerate the exploded Canvas package and the importable `.imscc` from the source files:

```bash
python3 scripts/build_canvas_package.py build
python3 scripts/build_canvas_package.py build --check
python3 scripts/build_canvas_package.py validate
```

The build now regenerates both learner-facing Canvas pages and assessment export files. Markdown is the source of truth for course pages, and `quizzes/*.json` is the source of truth for quizzes and exams.

## Canvas import

In Canvas, go to **Settings → Import Course Content** and import `canvas/WEB1430-Canvas-Export.imscc` with Content Type set to **Common Cartridge 1.x Package**. Do not choose "Canvas Course Export Package" — that converter fails on every quiz and assignment in this generated package. Use a fresh course shell (or Reset Course Content) so page links resolve cleanly.

Before the term starts, also complete the instructor-side setup documented in `course/import_to_canvas.md`:

- import the learning outcomes (`course/canvas-outcomes.csv` via Course → Outcomes → Import)
- import the rubrics (`course/canvas-rubrics.csv` via Course → Rubrics → Import Rubrics), then attach the nine assignment/project rubrics and add outcome rows using the mapping table in the guide
- create the Week 05, Week 11, and Week 13 anonymous check-in forms
- review `course/first-delivery-monitoring-guide.md`
- set up the tracking workflow before students reach Week 11
