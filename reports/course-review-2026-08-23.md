# WEB 1430 — Course Review and Change Record

**Course:** WEB 1430 Client-Side Web Development, Fall 2026 virtual section (Canvas course 631246)
**Reviewed and revised:** August 23, 2026 — the day before the term opened
**Landed as:** `d583022` (first batch) and `332e22f` "Course review updates" (the rest). Working tree clean.

---

## What this is

A full audit of the course package — every module overview, lecture, lab, brief, quiz, textbook chapter, the course spine, both modality overrides, the generated Canvas packages, and the instructor setup guides — followed by the repair work, all completed the day before the term opened.

Thirty findings were raised. All thirty are resolved in the repo, and the live Canvas course was synced to match. This document records what changed, why, and what remains a judgement call.

**The audit's verdict on the course itself was, and remains, positive.** The spine is coherent, the lecture → lab → assignment chain is deliberate, accessibility is structural rather than decorative, and the build tooling keeps the sources honest. Nothing here required rethinking the course. The problems were places where two documents disagreed, one structural gap in Canvas, a handful of code examples that didn't run as described, and a systematic weakness in how quiz items were built.

---

## Where things stand

| | State |
|---|---|
| Repo | Both batches committed; working tree clean |
| Lint, both builds, both validations | Passing |
| Live course 631246 | Synced — now 96 pages and 44 assignments, all verified against the repo |
| Live quizzes | 78 multiple-choice + 14 true/false, all matching the repo |
| Assignment group totals | Repo and live identical |
| Still open | Week 15 exam dates; support-page placement |

---

## Decisions taken

Four choices shaped the repair work. Each had a defensible alternative.

**Milestones are graded, with points carved out of the parent project.** The alternative — ungraded checkpoints — costs nothing to set up, but ungraded milestones are the ones students skip, which is precisely the failure the late-term pacing design exists to prevent. Carving points from the parent keeps the Projects group weight unchanged, so the grading scheme students read in the syllabus still holds.

**Arrow-key tab navigation is taught in Week 06** rather than demoted to stretch work. Demoting it would have been faster, but Lab 06 would have kept teaching a tab widget that announces itself as a tablist and doesn't behave like one — worse than plain buttons, because the user's expectations are then wrong too.

**Grading weights were fixed by changing the points, not the syllabus.** Students already had the syllabus, and the promises in it were reasonable. The points were what had drifted.

**Quiz fixes were applied to both the repo and the live New Quizzes.** The repo is the source of truth for future terms, but this term's students sit the live quizzes, and repo edits do not reach them — the quizzes were hand-migrated to New Quizzes.

---

## What changed

### Course structure: eight deliverables that had nowhere to go

The schedule and module overviews promised eight weekly deliverables — both project proposals, both build checkpoints, three Final Project milestones, and the course reflection — and **none of them existed as a Canvas assignment**. The briefs actively instructed submission ("Submit the live URL and repo URL to Canvas with a brief note"). There was no submission point, no due date, no gradebook row.

All eight now exist, published, dated on the normal Sunday 11:59 PM window, and placed in the correct module:

| Week | Milestone | Points |
|---|---|---|
| 05 | Project 1 Proposal | 20 |
| 07 | Project 1 Build | 25 |
| 10 | Project 2 Proposal | 25 |
| 12 | Project 2 Build | 30 |
| 12 | Final Project Pitch and Planning Starter | 20 |
| 13 | Final Project Revised Wireframe and Data Plan | 20 |
| 14 | Final Project Beta Review | 25 |
| 15 | Course Reflection | 24 |

Points are carved from the parent, so the Projects group weight is untouched: Project 1 = 20 + 25 + 96, Project 2 = 25 + 30 + 120, Final Project = 20 + 20 + 25 + 24 + 140.

The Course Reflection now has its own assignment with the **Final Project – Course Reflection** rubric attached. That rubric already existed and had nowhere to attach — the setup guide described it as "used within the Final Project." All twenty-four rubrics now have a home.

### Weekly rhythm: one lecture became two sessions

The virtual section meets twice a week — Monday and Wednesday, 9:30–10:45 — but the course shipped one lecture document per week. The module overviews already promised a split (Monday: concepts and a live demo; Wednesday: guided studio work, code review, Q&A) that the reading material did not reflect. A student preparing for Wednesday had no idea which part of a 10 KB lecture file was Wednesday's.

Each week is now two session-sized units:

- **Session 1 stays at `lectures/week-NN-lecture.md`** — same filename, same H1, same Canvas slug, so every existing live page and cross-link keeps resolving. It keeps Weekly focus, Why this matters, Learning targets, Core concepts, Common mistakes, and the Demo walkthrough, and closes with a new `Session 2: the studio` pointer.
- **Session 2 is a new `lectures/week-NN-studio.md`** — `Week NN Studio Notes: <subtitle>`. It opens with a Session focus paragraph, a *Before class* list, and a timed Studio plan totalling 75 minutes, then carries the Accessibility connection, Practice prompt, and Bridge sections that moved out of the lecture file.

The studio plans are authored per week from what the virtual overviews already promised: Week 00 is a setup clinic that ends with a verified first push; Week 02 absorbs the Labor Day Monday with a condensed demo plus reading Q&A before the layout studio; Week 08 is a Project 1 polish studio and the last midterm review; Week 15 is the Final Studio, 45 minutes of demos.

Both pages publish to both modalities. The studio notes close with a line telling online students to work the plan self-paced and to use the Help & Questions board wherever the plan says "the room" — so the same page serves an asynchronous section without a second copy to maintain. The one exception is the Week 00 studio, which has a virtual override for the Zoom screen-sharing instructions, mirroring the Week 00 lecture override that already existed.

Module overviews and both schedules gained a `- Studio:` line and a studio-notes link under Resources; the base success plan now reads "Complete the lab, then work the Session 2 studio plan."

### Assessment integrity: the quiz bank

The bank was technically clean — every item had exactly one correct answer, points matched counts, lint passed — but two measurable properties made items answerable without knowing the content.

| Measure | Before | After | Chance |
|---|---|---|---|
| Correct answer in position 1 / 2 / 3 / 4 | 37 / 34 / 7 / **0** | 20 / 20 / 19 / 19 | even |
| Correct answer is the single longest option | 69% | 38% | ~25% |

The correct answer was **never** in position four across all 78 multiple-choice items. A student who noticed that could raise their score without learning anything.

The length signal came from a two-tier bank: newer code-reading items carried an explanatory clause in the correct answer ("— finally runs whether the request succeeds or fails, ensuring…") while every distractor was a short assertion. Those clauses were moved out, so all four options now read as comparable claims.

Roughly 65 items were rewritten with plausible near-misses in place of distractors that could be eliminated without any course knowledge — "Network routing", "GPU memory", "Configure Wi-Fi", "The postal location of a user", "A network cable". The replacements are the mistakes students actually make: `event.currentTarget` as a foil for `event.target`, a `Response` object against a `Promise`, graceful degradation against progressive enhancement, a JavaScript object in memory against JSON text.

Three true/false items in the final exam had been encoded as multiple-choice with True/False options; they are now properly typed. Quiz 8's Lighthouse item now includes SEO — it previously named three of the four categories while the lecture, Chapter 8, and Chapter 14 all correctly said four. Answer shuffling is enabled on all 78 live multiple-choice items as a second defence against position bias.

### Grading model: points now equal rubrics

Three things disagreed with the syllabus, and one made grading unreliable.

The syllabus promised the Final Exam roughly two-thirds of the exam credit. The points gave it 17 against the midterm's 15 — a 53/47 split. Final Exam items are now 2 points each: **34 against 15, a 69/31 split**.

Every assignment brief read "One of six assignments (20% combined)," implying equal sixths. The actual points ran 50 / 60 / 75 / 80 / 70 / 80 — Assignment 1 carried 12% of the assignment grade while Assignments 4 and 6 carried 19.3% each. All six are now **24 points**. Assignment 1 gained a sixth rubric row, "Constraints and validation," splitting validation and the no-JS/no-framework constraints out of the accessibility row — a genuine improvement as well as the mechanism for equalising.

Most importantly, there was **no documented way to turn a rubric score into gradebook points**. Labs matched their rubric maximum exactly; assignments and projects did not (Assignment 3's rubric maxed at 24 against 75 points; the Final Project's at 40 against 220), and rubrics were attached with `use_for_grading` off. The grader was left multiplying by 3.125 in their head, inconsistently, across a semester.

Now every lab and assignment is worth exactly its rubric maximum, and each project's final artifact is a clean multiple of its rubric — Project 1 ×4, Project 2 ×5, Final Project ×5, Course Reflection ×2. The conversion table is in `import_to_canvas.md`.

Resulting group totals, identical in repo and live: Orientation 23, Labs 312, Assignments 144, Projects 545, Quizzes 52, Exams 49.

### Teaching content

**Arrow-key tabs.** Assignment 3 (Week 06) and Project 1 both graded arrow-key tab navigation, and it was taught only in Chapter 13 — seven weeks later. Worse, Lab 06 taught the anti-pattern Chapter 13 warns against: `role="tab"` buttons all left in the natural tab order. Assignment 3's rationale prompt asked "what did you have to learn that wasn't obvious?" — and the honest answer was "nothing in this course taught me."

The Week 06 lecture now has a roving-tabindex section: why an ARIA role is a promise about behaviour, the `tabIndex = 0 / -1` mechanism, Arrow/Home/End handling, `preventDefault()`, and why accordions must *not* use the pattern. Lab 06 teaches and tests it — five new checklist items, updated keyboard and ARIA rubric rows, `tabindex` in the starter markup. Project 1's modal option now points at Chapter 13 for focus trapping, the one technique the weekly lectures still don't cover.

**Five code examples that didn't do what they claimed.** Each was verified by execution:

- `formatDate("2025-03-15")` was documented as printing "March 15, 2025". In Mountain Time — this course's own timezone — it prints **March 14**, because a bare date string parses as midnight UTC. The example now uses `T12:00:00` and carries a note explaining the trap.
- The Week 11 Vite scaffold tree showed `main.js` at the project root; the actual scaffold puts it in `src/`, as Lab 10 correctly said. The lecture and its own lab disagreed.
- The Week 04 function-forms example declared `const greet` three times in one code fence — pasting it whole throws.
- Lab 04's stated expected output named the wrong trail. `findTrail` returns the *first* match, which is Lakeside Loop, not Ridgeline Path. Students who got it right would have thought they got it wrong.
- The Week 09 empty-state branch was unreachable: a parsed JSON object is always truthy. The four-state model is that lecture's centrepiece, and the empty state was demonstrated with dead code. The example moved to a search endpoint that can genuinely return nothing.

### Consistency

Twelve places where two documents disagreed, all cleared. The ones with real consequences:

- **Assignment 5** listed `constants.js` and `ARCHITECTURE.md` as required *and* as stretch work. A student reading top-down and one reading bottom-up built different projects.
- **Project 2's** Milestone 2 checkpoint asked "What two features remain for Week 12?" — in a milestone due at the end of Week 12.
- **Two lecture Bridges described the wrong assignment.** Week 13 told students Assignment 6 asked them to document Project 2's component data flow; it doesn't. Week 15 described a reflection prompt that doesn't exist and sent students to a Final Studio discussion that didn't either.
- **Lab 12** listed `defineEmits` under Skills practiced and never used it — in the same week the lecture teaches emits. It now has a real props-down/events-up round trip: `GradeTable` emits `clear-filters` from its empty state and the parent resets.
- **Lab 10 and Assignment 5** used `innerHTML = ''` while Labs 04, 05, and 08 grade "no `innerHTML`" and the Week 06 lecture teaches `textContent = ""` as the clearing idiom. Both now use `replaceChildren()`.
- **All 32 module overviews** told students to "read the chapter" in Weeks 00 and 15, where the same page says "No textbook chapter this week."

Also fixed: both empty Milestone 3 headings, Lab 13's checklist that listed five items against a rubric demanding six, Assignment 6's component count, the Final Project's "Full-stack front-end" against its own "no full-stack server" constraint, and Lab 13's GitHub Pages advice that omitted the `base:` fix its own week teaches and Quiz 8 tests.

### Calendar and workload

The course mentioned **no holiday anywhere**, in either modality. Verified against the registrar's calendar: Labor Day **Mon Sep 7**, Fall Break **Fri Oct 9**, Thanksgiving **Thu Nov 26 – Fri Nov 27**.

Only Labor Day hits a class session — and it landed on the Week 02 Monday, where the virtual overview scheduled a live demo. Week 02 now states there is no Monday session and points students at the lecture notes, with Wednesday opening on a condensed version of the demo. Week 13 states plainly that both its sessions *do* meet, since Thanksgiving falls Thursday and students will assume otherwise. A Semester calendar section is in both schedules and both syllabi.

On workload: the module time estimates sum to **~163 hours** against the ~135-hour federal standard for three credits — about 20% over, honestly self-reported. The compression is worst in Weeks 12–14, where the two longest chapters land in the two heaviest weeks. Chapter 13 alone is 4,172 words against a ~1,200-word typical chapter. It is now split across Weeks 12 and 13, which is the cheapest available relief. The deeper question — whether late-term milestone overlap should change — is left for first-delivery evidence, as `CONTEXT.md` recommends.

### Canvas setup

**The Help & Questions board did not exist.** Six student-facing documents routed students to it, and "Post in the Help & Questions board with what you tried and the exact error message" was the keyed correct answer to Question 7 of the Canvas Orientation Quiz. The package contained zero discussion topics and the setup guide never said to create one. It now exists — published, pinned, threaded, ungraded — placed in Module 0 immediately *before* the Orientation Quiz so students meet it before the quiz asks about it.

**Modules and Discussions were hidden from student navigation.** This surfaced while placing the board, and it was the more serious problem: it would have made both the new board and the Modules page unreachable, while Orientation Quiz Q1 keys "Modules" as the authoritative weekly list. Both are now visible. Student navigation reads: Home, Announcements, Modules, Zoom, Discussions, Syllabus, Assignments, Quizzes, Grades. Pages and Files remain hidden, which is fine — every page students need is linked from a module.

**Lab 00 asked for a screenshot the submission type couldn't accept.** Every generated assignment is URL + text entry, no file upload. The deliverable now routes through the repo as `labs/lab00/setup-check.png`, matching how Labs 01, 02, and 13 already handled screenshots — and reinforcing the repo workflow Lab 00 exists to teach.

**Node 18 would have failed in Week 11.** Lab 00 accepted v18; the current Vite release requires `^20.19.0 || >=22.12.0`. A student installing Node 18 in Week 0 would sail through eight weeks and hit an engine error the moment they ran `npm create vite@latest` in Lab 10. Lab 00 now requires Node 22 with an explicit warning and a troubleshooting entry for an old Node shadowed by a version manager.

---

## Tooling changes

Three changes to the build and lint scripts that a future maintainer needs to know about.

**`milestones/` is a new source directory** that generates Canvas *assignments only* — no wiki pages — because the authoritative requirements stay in the parent brief in `projects/`. Milestone briefs carry only a summary, submission mechanics, and a point breakdown, so there is one place to change a requirement rather than two. Registered in `MILESTONE_ASSIGNMENTS` in the build script.

**`assignment_body_specs()` needed a fix.** It built its source lookup only from `publishable_wiki_specs()`, so any generated assignment whose source is not *also* a wiki page rendered an empty description. Milestone descriptions came out blank until `generated_assignment_specs()` sources were merged into the lookup. Anything added later that follows the assignment-only pattern depends on this.

**Studio pages wire themselves in.** `publishable_wiki_specs()` already globs `lectures/*.md`, so each `week-NN-studio.md` becomes a Canvas page with no registration step. Placement is the only thing that needed code: a `studio_module_items` list in `create_expected_file_outputs()` inserts a studio module item directly after the `Week NN Lecture Notes` item in all 16 modules, in both `module_meta.xml` and the manifest organization, reusing the existing `GeneratedModuleItem` / `insert_assignment_module_items()` machinery.

**Lint rule 4 was relaxed** from `points == sum == question count` to `points == sum`, plus a check that every item carries positive points. The count equality was an artifact of the one-point-per-question convention and blocked the Final Exam's 2-point items. Lint and `validate_module_alignment` were also extended to cover `milestones/`.

---

## Operational notes

Things discovered while syncing the live course that will matter next time.

**The live syllabus has diverged from the repo.** Canvas `syllabus_body` carries an "Instructor information" block — name, department, office, Zoom link, office hours — that does not exist in `virtual/course/syllabus.md`. Every syllabus edit in this pass was made surgically for that reason. A course reset or re-import would lose it. Worth adding to the repo source.

**The New Quizzes API works with browser session auth**: `GET`/`PATCH` on `/api/quiz/v1/courses/:course/quizzes/:assignmentId/items`. Items match repo questions by `entry.title` against the JSON `name` field. Choice items take `interaction_data.choices` plus `scoring_data.value` set to the correct choice's id.

**An in-place interaction-type change returns 422.** Converting a choice item to true/false is not permitted; the item must be deleted and a replacement posted at the same position. That is how the three final-exam items were retyped.

**Canvas normalises whitespace inside assignment descriptions** — inserting a newline after `<li>` or `<td>` when the content starts with an inline tag — but leaves page bodies alone. It also adds `data-api-endpoint` and `data-api-returntype` attributes to internal links on import. Targeted live edits need whitespace-tolerant patterns, or they silently match nothing.

**Do not re-import over course 631246.** It would duplicate pages as `-2` URLs and clobber manual state. Sync individual objects instead.

---

## Verification

Every claim in the original audit was checked rather than asserted, and every repair was read back:

- Vite's engines field confirmed against `vite@8.2.2`; the vanilla and Vue scaffolds generated and inspected.
- `new Date("2025-03-15")` executed under `America/Denver`.
- Lab 04's `findTrail` run against its own dataset.
- Answer-position and answer-length distributions computed across all 11 assessment sources, before and after.
- Canvas manifest resource counts and assignment point values read directly from the generated package.
- Fall 2026 holidays and the final-exam grid read from the registrar's published calendar.
- After the session split: 16 studio pages created live and read back byte-identical to the built package, 16 lecture pages re-verified for section order and the studio link, 16 overviews checked for the Studio line, the Resources link, and the revised success plan, and all 16 module items confirmed to sit directly after their lecture item and published.
- After the sync: all 80 live pages and 44 live assignments swept for stale strings from every finding — none remain. Live quizzes read back as 78 multiple-choice and 14 true/false with positions 20/20/19/19, shuffle enabled, exactly one correct answer per item.

---

## Still open

**The Week 15 exam and final-project dates.** The registrar's Fall 2026 grid assigns a Monday/Wednesday 9:30 class to **Monday, December 7, 9:30–11:20 a.m.** Finals run December 7–10; **December 11 is graduation**. The live placeholder is still Friday December 11, 11:59 PM — after the exam period closes. How to set the Final Exam window, and whether the Final Project and Reflection stay on the 11th, are pedagogical calls rather than lookups.

**Support-page placement.** The accessibility primer, API troubleshooting guide, screen reader guide, Vue transition guide, reflection prompt, and three surveys exist as Canvas pages but sit in no module — reachable only through inline links in the weekly overviews. Defensible as a design choice; worth a decision rather than an accident.

**Late-term workload.** Splitting Chapter 13 helps Week 13, but Weeks 12–14 still carry four deliverables each. `CONTEXT.md` is right that this wants first-delivery evidence before deadlines move. The Week 5, 11, and 13 surveys are the instrument; the milestones are now graded, so submission timing will show the compression directly.

---

## Findings index

Thirty findings, with disposition.

| # | Finding | Disposition |
|---|---|---|
| 1 | Help & Questions board did not exist | Created, pinned, in Module 0 |
| 2 | Lab 00 accepted Node 18; Vite needs 20.19+/22.12+ | Now requires Node 22 |
| 3 | Lab 00 screenshot vs URL-only submission | Routed through the repo |
| 4 | Week 15 final-exam slot unconfirmed | Slot identified; dates **still open** |
| 5 | Eight milestones with no Canvas assignment | All eight created and graded |
| 6 | Arrow-key tabs graded Week 06, taught Week 13 | Taught in Week 06 |
| 7 | Focus trapping graded but never taught | Project 1 points at Chapter 13 |
| 8 | Exam split 53/47 vs syllabus's 2:1 | Final Exam 2 pts/item → 69/31 |
| 9 | "One of six assignments" but unequal points | All six at 24 points |
| 10 | No rubric-to-points conversion documented | Points = rubric max or clean multiple |
| 11 | Correct answer never in position 4 | Positions now 20/20/19/19 |
| 12 | Correct answer longest in 69% of items | Down to 38% |
| 13 | Implausible distractors in older items | ~65 items rewritten |
| 14 | Three T/F items typed as multiple-choice | Retyped |
| 15 | Quiz 8 named three of four Lighthouse categories | SEO added |
| 16 | `formatDate` printed the wrong date locally | Fixed with a UTC-parsing note |
| 17 | Vite scaffold tree omitted `src/` | Corrected |
| 18 | `const greet` declared three times in one fence | Renamed |
| 19 | Lab 04 named the wrong expected trail | Corrected |
| 20 | Week 09 empty-state branch unreachable | Example moved to a list endpoint |
| 21 | Assignment 5: required *and* stretch | Required only |
| 22 | Project 2 checkpoint asked about its own week | Weeks 13–14 |
| 23 | Week 13 Bridge described the wrong assignment | Rewritten |
| 24 | Week 15 Bridge described a nonexistent prompt and discussion | Rewritten |
| 25 | Lab 12 promised `defineEmits`, never used it | Real emit added |
| 26 | Lab 10 / Assignment 5 contradicted the `innerHTML` rule | `replaceChildren()` |
| 27 | Weeks 00/15 told to read a nonexistent chapter | Reworded in all four files |
| 28 | Empty Milestone 3 headings; Lab 13 five-vs-six; A6 count; "Full-stack front-end" | All corrected |
| 29 | No holidays mentioned anywhere | Calendar added; Week 02 and 13 resolved |
| 30 | Chapter 13 (4,172 words) landed in the heaviest week | Split across Weeks 12–13 |

Two items surfaced during the repair rather than the audit: **Modules and Discussions hidden from student navigation** (fixed), and **the live syllabus diverging from the repo** (documented, not fixed).
