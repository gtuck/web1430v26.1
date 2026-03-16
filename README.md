# WEB 1430: Client-Side Web Development

This repository contains a fully rebuilt, online-first **WEB 1430** course package designed for Canvas and a GitHub-based workflow.

## Included

- original textbook with 14 chapters
- weekly lecture notes and module overviews
- labs
- assignments
- projects
- quizzes and exams in Canvas-compatible QTI/Common Cartridge structure
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
```

The build now regenerates both learner-facing Canvas pages and assessment export files. Markdown is the source of truth for course pages, and `quizzes/*.json` is the source of truth for quizzes and exams.

Validate that the current Canvas package is synchronized with the source files:

```bash
python3 scripts/build_canvas_package.py validate
```

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
