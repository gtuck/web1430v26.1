# WEB 1430 Project Memory

Current as of July 13, 2026. `CONTEXT.md` carries the working rules; this file carries project state and history highlights.

## Project Summary

WEB 1430 is a complete **Client-Side Web Development** course package for Weber State University, buildable in two delivery modalities from the same sources: the original **online** (asynchronous) section and a **virtual** (synchronous, Zoom-based) section added July 2026. The repository contains the authored course source plus generated Canvas export packages; both exports were verified through live Canvas imports in July 2026.

## Virtual Modality (added July 13, 2026)

- Fall 2026 virtual section: live sessions Mon/Wed 9:30–10:45 AM MT, Aug 24 – Dec 4, 2026; Zoom room https://weber.zoom.us/j/8013088825; office hours Mon/Wed 8:00–9:00 AM and 12:30–2:00 PM by appointment (https://calendar.app.google/5iHL7QJQDYRb2jeb8).
- Overrides live at `virtual/<same relative path>`: `home.md`, `course/syllabus.md`, `course/schedule.md`, `lectures/week-00-lecture.md`, and all 16 module overviews (which add a `## Live sessions` Mon/Wed agenda section and a session-oriented success plan). Everything else — textbook, labs, assignments, projects, quizzes, starters, support guides, surveys, outcomes/rubrics CSVs — is shared.
- Build with `--modality virtual` → `canvas/WEB1430-Virtual-Canvas-Export.imscc` + `canvas/virtual/expanded_package/` (seeded from the online package on first build). Online commands and outputs are unchanged.
- Lint enforces override consistency: no orphan overrides, base H1 titles preserved (Canvas slug stability), identical `- Deliverables:` lines (due dates shared — deliverables stay in the Sunday window in both modalities), links resolved from the base location, and the Live sessions section present.
- Weekly pattern: Monday session = concepts + live demo (lecture notes remain as shared reference reading); Wednesday session = guided lab/studio, code review, Q&A. Exams stay in Canvas windows, not session time. Instructor logistics: `instructor/virtual-delivery-guide.md`.
- The virtual `.imscc` was verified through a live Canvas import on July 13, 2026, with no issues (same import settings as the online package).

## Current Source of Truth

- Markdown files drive learner-facing course pages, briefs, lectures, labs, and support guides.
- `quizzes/*.json` drives quizzes and exams.
- `scripts/build_canvas_package.py` regenerates the Canvas HTML, assessment XML/QTI, and the `.imscc` package. Internal page links are emitted as `$WIKI_REFERENCE$/pages/<slug>` placeholders so Canvas resolves them on import.
- `scripts/build_canvas_rubrics_csv.py` regenerates `instructor/canvas-rubrics.csv` from the rubric tables in the briefs.
- `scripts/lint_course.py` mechanically enforces the cross-file consistency rules (links, fences, rubric tables, quiz points/alignment, due weeks, CSV freshness, module format, single syllabus, virtual-override consistency).
- Not part of the Canvas export: `reports/`, `memory/`, `instructor/` (import/setup guide, monitoring guide, Outcomes/Rubrics CSVs), `starters/` (student lab starter files, distributed via GitHub), `CONTEXT.md`, `README.md`, `textbook/README.md`.

## Current Course Shape

- 14 textbook chapters (Chapter 8 is the Week 08 reading; every chapter is assigned to a week)
- 16 weekly module overviews and lecture notes (`week-00` through `week-15`)
- 14 labs, 6 assignments, 3 projects, plus 2 Week 00 orientation briefs (Welcome Survey 5 pts, GitHub Repo Setup 10 pts)
- 8 quizzes, 1 midterm, 1 final — all selected-response, 1 point per item, points equal question counts
- Labs and orientation items are generated Canvas assignments (added July 13, 2026, after the Labs assignment group imported empty): labs carry 4 × rubric-criteria points (20–24), URL+text submission, placed after their handout page in each module. Generation is driven by `generated_assignment_specs()` in the build script; module items are keyed by `identifierref` so same-titled handout pages and assignments coexist. The Week 00 Canvas Orientation Quiz was authored August 21, 2026 as `quizzes/quiz-0-canvas-orientation.json` (8 modality-neutral selected-response items on Canvas navigation, the weekly rhythm, Git vs GitHub, `git status`, and the help workflow): the build's `GENERATED_ASSESSMENTS` mapping creates its manifest resources with stable ids, places it in the Orientation group (position 3), and inserts its `Quizzes::Quiz` module item after GitHub Repo Setup in Week 00. It is covered by lint's alignment check and appears in `course/quiz-alignment.md`.

## Canvas Delivery Workflow (verified live, July 2026)

- Import `canvas/WEB1430-Canvas-Export.imscc` with Content Type **"Common Cartridge 1.x Package"** only. The "Canvas Course Export Package" option fails on every quiz and assignment. Leave "Convert content to New Quizzes" unchecked. Use a fresh course shell or Reset Course Content before re-importing.
- The institution has **no Canvas API access** (no tokens). All automation must use Canvas UI channels; never propose REST API tooling.
- Instructor-side setup after import (full checklist in `instructor/import_to_canvas.md`):
  1. Import `instructor/canvas-outcomes.csv` (Course > Outcomes > Import) — 10 outcomes in one group, ratings Excellent 4 / Proficient 3 / Developing 2 / Incomplete 1, mastery at Proficient.
  2. Import `instructor/canvas-rubrics.csv` (Course > Rubrics > Import Rubrics) — 24 rubrics from the briefs. Then manually attach 23 rubrics to their assignments (Labs 00–13, Assignments 1–6, Projects 1–2, Final Project) and add outcome rows using the mapping table in the guide (CSV import cannot do either).
  3. Create the Week 05 / 11 / 13 anonymous survey forms and set up the monitoring workflow (`instructor/first-delivery-monitoring-guide.md`).

## Content State Highlights

- Content is aligned across source docs and the Canvas export; the export imports cleanly (pages, links, quizzes, assignments, groups).
- July 2026 accuracy pass: fixed textbook facts (CSS render-blocking vs parser-blocking; Lighthouse's four categories, PWA removed; Vue 3 named exports; JSON `null`), a Chapter 4 code-fence bug, the Week 08 lecture's midterm-format description (now matches the selected-response exam), and the Week 03 primitive-type count; added Chapter 8 to Week 08; added the DOM glue pattern to Labs 04–05 (used ahead of Week 06 by design); completed three rubric rows with empty Incomplete cells; added a GitHub Pages `base`-path note to Chapter 14; synced the course reflection prompt's rubric with the Final Project brief; corrected the Week 11 survey's Project 2 milestone reference (Milestone 2 build is due Week 12).
- Module overviews use week-specific checkpoint questions, time estimates, and harder-week struggle guidance. Surveys run Weeks 5, 11, and 13. Final Project milestones are visible in the schedule and late-course overviews, with a Week 12 planning starter and Week 13 revision milestone.
- Week 14 uses Lab 13 as applied QA evidence with Quiz 8 as a short readiness check. API briefs require a viability check; major projects require `README.md` documentation. Week 00 teaches `git status` / `git pull --ff-only`.
- The reports in `reports/` are current as of March 16, 2026 and predate the July 2026 pass.

## Key Files to Keep in Sync

- `course/schedule.md`, `modules/week-*-overview.md`, `assignments/*.md`, `projects/*.md`
- `course/syllabus.md` (the single canonical syllabus; the duplicated root copy was retired July 2026)
- `course/quiz-alignment.md` and `quizzes/*.json`
- `instructor/canvas-outcomes.csv` with `course/learning_outcomes.md`
- `instructor/canvas-rubrics.csv` with the briefs' rubric tables (regenerate via the script)
- generated Canvas outputs under `canvas/expanded_package/`

## Build / Verification Commands

```bash
python3 scripts/build_canvas_package.py build
python3 scripts/build_canvas_package.py build --check
python3 scripts/build_canvas_package.py validate
python3 scripts/lint_course.py                # cross-file consistency checks
python3 scripts/build_canvas_rubrics_csv.py   # after any rubric-table change
```

## Working Assumptions

- Do not hand-edit generated Canvas HTML or assessment XML as the primary change path.
- If source content changes, rebuild the Canvas package before considering the repo synchronized.
- Keep assignment/project `Due:` lines aligned with `course/schedule.md` and quiz JSON `points` equal to the sum of `questions[].points_possible` — `scripts/lint_course.py` enforces both.
- Preserve the module-overview support pattern (time estimate, tailored checkpoint question, struggle guidance on hard weeks) and the four-level rubric format with every cell filled — the rubric tables are machine-parsed.
- If learner-facing support docs linked from modules or briefs change, rebuild the Canvas package.
- Already-imported Canvas courses do not update when the repo changes: either re-import into a fresh/reset shell or hand-edit the affected Canvas pages.

## Remaining Limitations

- Import verified manually, but no automated Canvas import smoke test exists; repo verification is package-level (`validate`) plus source-level (`lint_course.py`).
- All exported assessment items are selected-response.
- No standalone early low-stakes checkpoints for DevTools or persistence (Week 14's Lab 13 is the main applied QA evidence).
- Survey forms and follow-up announcements require manual instructor execution.
- Rubric-to-assignment attachment and outcome rows are manual Canvas UI work after each fresh import (no API access).
- Brand-new assessments must be registered in the build script's `GENERATED_ASSESSMENTS` mapping so the build can generate their manifest resources (the Canvas Orientation Quiz is the first example).
- Main open instructional-design risk: late-term workload compression. Use first-delivery evidence before changing overlap or deadlines.
