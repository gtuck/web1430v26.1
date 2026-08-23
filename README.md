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

- `course/` – syllabus (single canonical copy), schedule, outcomes, quiz alignment, published support guides, and survey question banks
- `instructor/` – instructor-only material: Canvas import/setup guide, first-delivery monitoring guide, and the `canvas-outcomes.csv` / `canvas-rubrics.csv` files for Canvas's Outcomes and Rubrics import features
- `starters/` – student-facing lab starter files (see its README for the lab-by-lab list)
- `virtual/` – virtual-modality (synchronous Zoom section) source overrides; mirrors the base layout, everything not overridden is shared
- `textbook/` – original textbook chapters
- `lectures/` – weekly session notes: `week-NN-lecture.md` (session 1, Monday) and `week-NN-studio.md` (session 2, Wednesday)
- `modules/` – weekly overview pages
- `labs/` – lab handouts
- `assignments/` – assignment briefs
- `projects/` – project briefs
- `quizzes/` – source JSON for quiz content
- `canvas/` – exploded package and importable IMSCC
- `scripts/` – Canvas build and validation tools, `build_canvas_rubrics_csv.py` (regenerates `instructor/canvas-rubrics.csv` from the rubric tables in the briefs), and `lint_course.py` (cross-file consistency checks)

## Safe to edit without affecting Canvas

These repo-maintenance files and folders are **not** included in the Canvas export package, so editing them will not change the generated learner-facing Canvas content:

- `reports/`
- `memory/`
- `instructor/` (the Canvas import/setup guide, monitoring guide, and the Outcomes/Rubrics CSVs, which are uploaded to Canvas separately from the `.imscc`)
- `starters/` (distributed to students through GitHub, not Canvas)
- `CONTEXT.md`
- `README.md`
- `textbook/README.md`

If you edit `home.md`, `course/syllabus.md`, `textbook-table-of-contents.md`, anything in `textbook/chapters/`, `lectures/`, `modules/`, `labs/`, `assignments/`, `projects/`, or the published learner-support guides in `course/`, those changes **do** affect the Canvas export.

## Canvas build workflow

Regenerate the exploded Canvas package and the importable `.imscc` from the source files:

```bash
python3 scripts/build_canvas_package.py build
python3 scripts/build_canvas_package.py build --check
python3 scripts/build_canvas_package.py validate
python3 scripts/lint_course.py
```

The course builds in two delivery modalities from the same sources. The commands above build the **online** (asynchronous) package. The **virtual** (synchronous, Zoom-based) package uses `--modality virtual` and reads overrides from `virtual/<same relative path>` — any source without an override is shared:

```bash
python3 scripts/build_canvas_package.py build --modality virtual
python3 scripts/build_canvas_package.py validate --modality virtual
```

This produces `canvas/WEB1430-Virtual-Canvas-Export.imscc` and `canvas/virtual/expanded_package/`. See `instructor/virtual-delivery-guide.md` for running the virtual section.

The build regenerates both learner-facing Canvas pages and assessment export files. Markdown is the source of truth for course pages, and `quizzes/*.json` is the source of truth for quizzes and exams.

`lint_course.py` mechanically enforces the cross-file consistency rules: link and code-fence integrity, rubric-table format, quiz points/alignment counts, assignment due weeks vs the schedule, Outcomes/Rubrics CSV freshness, module-overview format, and the single-syllabus rule. Run it before committing content changes.

## Editing workflow

Follow these steps for any content change, before committing:

1. **Edit the source files** (never the generated files under `canvas/`).
2. **Run the lint:** `python3 scripts/lint_course.py`
   - Each failure names the file (usually the line) and the problem. Common cases:
     - *rubric row has missing or empty cells* → fill the cell in that brief's rubric table
     - *'Assignment N' is due Week X but is not in that week's schedule deliverables* → fix whichever is wrong: the brief's `**Due:**` line or `course/schedule.md`
     - *instructor/canvas-rubrics.csv is stale* → run `python3 scripts/build_canvas_rubrics_csv.py`
     - *broken link* → fix the path in the named file
   - Re-run until it passes.
3. **Run the package check:** `python3 scripts/build_canvas_package.py build --check`
   - "Canvas package is already up to date" → your edits do not feed Canvas; skip to step 5.
   - A list of files → your edits feed the export; go to step 4.
4. **Rebuild and validate:**
   `python3 scripts/build_canvas_package.py build` then `python3 scripts/build_canvas_package.py validate`
   - If you changed a **shared** source file (anything outside `virtual/`), also rebuild the virtual package: `build --modality virtual` then `validate --modality virtual`.
   - If you changed only a `virtual/` override, rebuild only the virtual package.
5. **Commit everything together** (source edits plus any regenerated `canvas/` files and CSVs) so the repo stays in the "sources and package agree" state.

When to run what:

| You changed… | Run |
|---|---|
| Lectures, chapters, modules, labs, assignments, projects, `home.md`, published `course/` guides or surveys | lint → build --check → rebuild + validate |
| A rubric table in any brief | `build_canvas_rubrics_csv.py` first, then the row above |
| `course/learning_outcomes.md` | update `instructor/canvas-outcomes.csv` to match (lint verifies), then the row above |
| `course/schedule.md` or a `**Due:**` line | lint → build --check |
| `quizzes/*.json` | lint → rebuild + validate |
| A `virtual/` override | lint → rebuild + validate with `--modality virtual` only |
| Only `instructor/`, `reports/`, `memory/`, `README.md`, `CONTEXT.md` | lint alone (build --check will confirm "up to date") |

Shared-file changes feed **both** packages; run the rebuild + validate step for each modality.

**Note:** passing checks keeps the repo and `.imscc` correct — it does not update an already-imported Canvas course. To publish changes to Canvas, re-import the new `.imscc` into a fresh or reset course shell (as Common Cartridge 1.x, per `instructor/import_to_canvas.md`), or hand-edit the affected Canvas pages.

## Canvas import

In Canvas, go to **Settings → Import Course Content** and import `canvas/WEB1430-Canvas-Export.imscc` with Content Type set to **Common Cartridge 1.x Package**. Do not choose "Canvas Course Export Package" — that converter fails on every quiz and assignment in this generated package. Use a fresh course shell (or Reset Course Content) so page links resolve cleanly.

Before the term starts, also complete the instructor-side setup documented in `instructor/import_to_canvas.md`:

- import the learning outcomes (`instructor/canvas-outcomes.csv` via Course → Outcomes → Import)
- import the rubrics (`instructor/canvas-rubrics.csv` via Course → Rubrics → Import Rubrics), then attach the nine assignment/project rubrics and add outcome rows using the mapping table in the guide
- create the Week 05, Week 11, and Week 13 anonymous check-in forms
- review `instructor/first-delivery-monitoring-guide.md`
- set up the tracking workflow before students reach Week 11
