# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

A complete course package for **WEB 1430: Client-Side Web Development** at Weber State University — a 4-credit, fully online, asynchronous course. All content is authored in Markdown and exported to Canvas LMS via an IMSCC package.

## Canvas export

The pre-built Canvas package is at `canvas/WEB1430-Canvas-Export.imscc`. Import it into Canvas via Course Settings → Import Course Content → Common Cartridge 1.x Package. The `scripts/build_canvas_package.py` stub is a placeholder; the IMSCC was generated externally and is not rebuilt from source in this repo.

## Repository structure

| Directory | Contents |
|-----------|----------|
| `course/` | Syllabus, week-by-week schedule, learning outcomes, Canvas import instructions |
| `textbook/chapters/` | 12 Markdown chapters (chapter-01 through chapter-12) |
| `lectures/` | 16 weekly lecture notes (week-00 through week-15) |
| `modules/` | 16 weekly module overview pages (week-00 through week-15) |
| `labs/` | 14 lab handouts (lab00 through lab13) — each has a 4-level rubric |
| `assignments/` | 6 assignment briefs with rubrics |
| `projects/` | 3 project briefs (Project 1, Project 2, Final Project) with milestones and rubrics |
| `quizzes/` | 8 weekly quizzes + midterm + final exam in Canvas-compatible format |
| `starters/` | Starter files students copy before beginning each lab (lab00–lab10) |
| `reports/` | Instructional design audit reports |

## Curriculum sequence and dependencies

The course follows a strict skill progression — later content depends on earlier content:

- **Weeks 0–2**: HTML5, CSS, Git workflow (no JavaScript)
- **Weeks 3–5**: JavaScript syntax, arrays, DOM basics
- **Weeks 6–8**: Event handling, accessible UI patterns, Project 1
- **Weeks 9–11**: Fetch API, async/await, localStorage, Project 2
- **Weeks 12–14**: ES modules, Vite, Vue 3 Composition API
- **Week 15**: Lighthouse audit, deployment, Final Project

**Key constraint**: When writing or editing assignment/lab requirements, never require a skill before it is introduced in the chapter sequence. Assignment 1 is HTML/CSS only; JavaScript is introduced in Week 3.

## Content conventions

### Lab format
Each lab file contains: Purpose → Skills practiced → What you're building → Parts (Part 1, 2, 3…) → CSS requirements → Deliverables → Process reflection → Rubric (4 levels: Excellent / Proficient / Developing / Incomplete).

### Starter file philosophy
Starters in `starters/labXX/` provide: HTML structure, data arrays, and pre-written "infrastructure" functions (error display, storage helpers, etc.). Students implement the learning-critical functions themselves. Do not pre-write the functions students are meant to practice.

### Module overview format
Each `modules/week-NN-overview.md` contains: theme, lecture reference, lab reference, deliverables list, 5-step success plan, and one checkpoint question. They intentionally omit resource links and time estimates (a known gap — these can be added).

### Rubric levels
All rubrics use exactly four levels: **Excellent** / **Proficient** / **Developing** / **Incomplete**. Do not use other level names.

## Grading weights (syllabus)
Orientation 5% · Labs 20% · Assignments 20% · Projects 30% · Quizzes 10% · Exams 15%

## Known gaps (from `reports/claude-id-report.md`)
- Lecture files (`lectures/`) are structural templates — substantive lecture content is the largest remaining gap
- Chapter 1 is underdeveloped (~68 lines) compared to later chapters
- Module overviews lack resource links and time estimates
- Quizzes are recall-only; no application-level questions yet
- Final exam format is not described in the syllabus
- `course/quiz-alignment.md` does not exist yet (needs to map each quiz to chapter and learning outcomes)
