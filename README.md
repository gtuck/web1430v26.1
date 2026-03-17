# WEB 1430: Client-Side Web Development

This repository contains a fully rebuilt, online-first **WEB 1430** course package designed for Canvas and a GitHub-based workflow.

Recent alignment work also updated:

- Week 00 Git/GitHub materials to teach `git status` and `git pull --ff-only` as baseline sync/recovery habits
- API-driven assignments and projects to require an API viability check (CORS, rate limits/auth, attribution/terms, data reliability)
- major project briefs and syllabus docs to require lightweight `README.md` documentation
- Week 14 quality-assurance materials so Lab 13 functions as applied QA evidence alongside a shorter Quiz 8 readiness check
- textbook chapters 8, 9, 10, 11, and 14 so the textbook matches current assignment, project, and QA expectations

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
- `textbook/` – original textbook chapters
- `lectures/` – weekly lecture notes
- `modules/` – weekly overview pages
- `labs/` – lab handouts
- `assignments/` – assignment briefs
- `projects/` – project briefs
- `quizzes/` – source JSON for quiz content
- `canvas/` – exploded package and importable IMSCC
- `scripts/` – Canvas build and validation tools

## Canvas build workflow

Regenerate the exploded Canvas package and the importable `.imscc` from the source files:

```bash
python3 scripts/build_canvas_package.py build
python3 scripts/build_canvas_package.py build --check
python3 scripts/build_canvas_package.py validate
```

The build now regenerates both learner-facing Canvas pages and assessment export files. Markdown is the source of truth for course pages, and `quizzes/*.json` is the source of truth for quizzes and exams.

## Suggested GitHub publishing steps

```bash
git init
git branch -M main
git remote add origin git@github.com:gtuck/web1430v261.git
git add .
git commit -m "Initial WEB1430 course build"
git push -u origin main
```

## Canvas import

In Canvas, go to **Settings → Import Course Content** and import the file in `canvas/WEB1430-Canvas-Export.imscc`.

Before the term starts, also complete the instructor-side setup documented in `course/import_to_canvas.md`:

- create the Week 05, Week 11, and Week 13 anonymous check-in forms
- review `course/first-delivery-monitoring-guide.md`
- set up the tracking workflow before students reach Week 11
