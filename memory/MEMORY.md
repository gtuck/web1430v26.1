# WEB 1430 Project Memory

## Project Summary

WEB 1430 is a complete, online-first **Client-Side Web Development** course package for Weber State University. The repository contains the authored course source plus a generated Canvas export package.

## Current Source of Truth

- Markdown files drive learner-facing course pages, briefs, lectures, labs, and support guides.
- `quizzes/*.json` drives quizzes and exams.
- `scripts/build_canvas_package.py` regenerates the Canvas HTML, assessment XML/QTI, and the `.imscc` package.

## Current Course Shape

- 14 textbook chapters
- 16 weekly module overviews and lecture notes (`week-00` through `week-15`)
- 14 labs
- 6 assignments
- 3 projects
- 8 quizzes, 1 midterm, 1 final

## Important Current State

- The repo and Canvas package have already been synchronized after a broad content review.
- Week 5 and Week 11 student surveys are now published and surfaced in the weekly flow.
- Week 13 and Week 14 now explicitly show Final Project milestones in the schedule and module overviews.
- The accessibility primer and other support guides are now published into the Canvas package.
- Quiz/exam point totals are synchronized with question counts.
- Canvas pages for assignments/projects now come from the source briefs instead of summary stubs.
- Canvas assessment files are now generated from `quizzes/*.json`.
- Quiz 4, Quizzes 6-8, the Midterm, and the Final now include stronger code-reading/debugging stems.

## Key Files to Keep in Sync

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

## Remaining Limitations

- Validation is repo/package-level only; there is still no live Canvas import smoke test in the repo.
- Assessment quality is improved, but all exported items are still selected-response.
- The build script currently assumes the existing Canvas assessment resource structure; adding brand-new assessments may need script updates.
