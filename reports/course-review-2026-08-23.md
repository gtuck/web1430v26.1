# WEB 1430 — Full Course Review

**Reviewed:** August 23, 2026 (one day before term start, Aug 24)
**Scope:** all 16 module overviews, 16 lecture note sets, 14 labs, 8 assignment/orientation briefs, 3 project briefs, 11 quiz/exam JSON sources, 14 textbook chapters, the course spine (syllabus, schedule, outcomes, quiz alignment), both virtual overrides, the generated Canvas packages, and the instructor setup guides.
**Method:** mechanical checks (lint, `build --check`, `validate` — all pass in both modalities), plus manual cross-reading and executable verification of code examples, quiz keys, point arithmetic, and toolchain claims.

---

## Update — August 23, all ten sections resolved

Every section of this report has been fixed in the repo, and the live Canvas course (631246) has been synced to match. **Repo changes are made but not committed** — they need a push from your terminal. Lint, both package builds, and both validations pass.

### Decisions taken
Milestones are **graded, with points carved out of the parent project**. Arrow-key tab navigation is **taught in Week 06** rather than demoted to stretch. Grading weights were fixed **by changing the points**, leaving the syllabus wording as students already have it. Quiz fixes were applied to **both the repo and the live New Quizzes**.

### §1 Blocking — done
Help & Questions board created (published, pinned, threaded, ungraded), placed in Module 0 immediately before the Orientation Quiz. Lab 00 now requires Node 22 (v22.12.0+) with a "this breaks in Week 11 otherwise" warning and an nvm troubleshooting entry. The screenshot deliverable routes through the repo as `labs/lab00/setup-check.png`.

**Final exam slot — answered, not set.** The registrar's Fall 2026 grid assigns a MW 9:30 class to **Monday, December 7, 9:30–11:20 a.m.**; finals run Dec 7–10 and Dec 11 is graduation. The live placeholder is still Fri Dec 11 — your call.

### §2 Eight milestones — done
A new `milestones/` source directory generates Canvas **assignments only** (no wiki pages; the authoritative requirements stay in the parent brief). All eight are live, published, dated on the normal Sunday 11:59 PM window, and placed in the correct module. Points are carved from the parent so the Projects group weight is unchanged: Project 1 = 20 + 25 + 96, Project 2 = 25 + 30 + 120, Final Project = 20 + 20 + 25 + 24 + 140. The Course Reflection now has its own assignment with the existing **Final Project – Course Reflection** rubric attached — the 24th rubric, which previously had nowhere to go.

Wiring this required a build-script fix: `assignment_body_specs()` only looked up sources from wiki pages, so milestone descriptions rendered empty until non-page sources were added to the lookup.

### §3 Arrow-key tabs — done
The Week 06 lecture gains a **roving tabindex** section: why `role="tab"` is a promise about behaviour, the `tabIndex = 0 / -1` mechanism, Arrow/Home/End handling, `preventDefault()`, and why accordions must *not* use the pattern. Lab 06 now teaches and tests it (five new checklist items, updated keyboard and ARIA rubric rows, `tabindex` in the starter markup). Project 1's modal option now points at Chapter 13 for focus trapping.

### §4 Grading weights — done
Final Exam items are now 2 points each (34 vs the midterm's 15) — a **69% / 31%** split, matching the syllabus's stated two-thirds. All six assignments are 24 points; Assignment 1 gained a sixth rubric row ("Constraints and validation") so the set is genuinely equal. Every lab and assignment is now worth exactly its rubric maximum, and each project final is a clean multiple of its rubric (×4, ×5, ×5, ×2), so a rubric score converts with one multiplication. The conversion table is in `import_to_canvas.md`. Live group totals now match the repo exactly.

### §5 Quiz bank — done, repo and live
Correct-answer positions went from **37/34/7/0 (never slot 4)** to **20/20/19/19**. "Correct answer is the single longest option" dropped from **69% to 38%** (chance is ~25%). Roughly 65 items were rewritten with plausible near-miss distractors — `event.currentTarget` as a foil for `event.target`, a `Response` object against a `Promise`, graceful degradation against progressive enhancement — replacing "Network routing", "GPU memory" and "A network cable". Three final-exam true/false items were retyped (they had to be deleted and recreated; New Quizzes refuses an in-place type change). Quiz 8 Q1 now includes SEO. Answer shuffling is enabled on all 78 multiple-choice items as a second defence.

### §6 Code defects — done
`formatDate` now uses `T12:00:00` with a note explaining the UTC-parsing trap. The Vite scaffold tree shows `src/`. The Week 04 example is `greetExpr` / `greetArrow` so it can be pasted whole. Lab 04 expects Lakeside Loop. The Week 09 empty-state branch is reachable — the example moved to a search endpoint that can genuinely return nothing.

### §7 Contradictions — done
All twelve: Assignment 5's required-vs-stretch collision, Project 2's checkpoint asking about its own week, both empty Milestone 3 headings, the two wrong lecture Bridges, Lab 12 now genuinely using `defineEmits` (GradeTable emits `clear-filters`), Lab 10 and Assignment 5 on `replaceChildren()`, Weeks 00/15 no longer told to read a chapter that does not exist, Lab 13's sixth checklist item and the `base:` GitHub Pages fix, Assignment 6's component count, and the Final Project's "End-to-end front-end".

### §8 Calendar — done
Verified against the registrar's calendar image: Labor Day **Mon Sep 7**, Fall Break **Fri Oct 9**, Thanksgiving **Thu Nov 26 – Fri Nov 27**. Only Labor Day hits a session. Week 02 now states no Monday session; Week 13 states both sessions do meet. A Semester calendar section is in both schedules and both syllabi.

### §9/§10 Workload and small items — done
Chapter 13 is split across Weeks 12–13 in all four module overviews. Weeks 05/07/10 now link their project briefs. Fixed: the `typeof null` age, the 304 cache wording, the `requireField` hardcoded message, Chapter 13's forward reference to Lighthouse, the reflection length-versus-depth mismatch, and Lab 03's ambiguous third bug.

### Two things that surfaced along the way
1. **Modules and Discussions were hidden from student navigation** on the live course — which would have made both the new help board and the Modules page unreachable, while Orientation Quiz Q1 keys "Modules" as the authoritative weekly list. Both are now visible.
2. **The live syllabus has diverged from the repo** — it carries an "Instructor information" block the sources do not have. All syllabus edits were made surgically. A course reset or re-import would lose that block; worth adding to the repo source.

### Verification
A sweep of all 80 live pages and 44 live assignments found **no remaining stale strings** from any finding in this report. Live quizzes read back as 78 multiple-choice + 14 true/false, positions 20/20/19/19, shuffle on, every item with exactly one correct answer. Live assignment-group totals match the repo: Orientation 23, Labs 312, Assignments 144, Projects 545, Quizzes 52, Exams 49.

### Still open
The Week 15 exam and final-project dates, and the decision about whether support pages should be placed in modules rather than reached only through inline links.

---

## Verdict

This is a genuinely strong course. The spine is coherent, the lecture-to-lab-to-assignment chain is deliberate, accessibility is woven through rather than bolted on, and the build tooling keeps the sources honest. Lint, both package builds, and both validations pass.

The problems are not conceptual. They are **twelve places where two documents disagree with each other**, **one structural gap in Canvas** (eight promised deliverables have nowhere to be submitted), **three code examples that produce different output than the notes claim**, and **a systematic test-validity weakness in the quiz bank**. Nothing here requires rethinking the course. Most items are 5-minute edits.

Findings below are ordered by when they will bite.

---

## 1. Blocking — fix before Week 0 opens  ✅ all four resolved

### 1.1 The "Help & Questions" board does not exist

Six student-facing documents send students to a Canvas discussion board called **Help & Questions**, and it is the keyed correct answer on the Canvas Orientation Quiz (Q7: *"Post in the Help & Questions board with what you tried and the exact error message"*).

The Canvas package contains **zero discussion topics** (no `imsdt` resources in either manifest), and `instructor/import_to_canvas.md` never says to create one. A Week 0 student who follows the instructions — or answers the quiz correctly — is pointed at something that isn't there.

- Referenced in: `labs/lab00`, `assignments/github-repo-setup.md`, `assignments/welcome-survey.md`, `lectures/week-00-lecture.md` (+ virtual override), `course-template/README.md`
- `instructor/virtual-delivery-guide.md:49` says the board "remains," which assumes it already exists.

**Fix:** create the discussion in Canvas, pin it in Module 0, and add the step to `import_to_canvas.md`.

### 1.2 Node 18 will fail at Week 11

`labs/lab00:37` tells students `node --version` "should print v18.x.x or higher," and the smoke-test checklist (line 150) accepts v18. But the current Vite release requires **Node `^20.19.0 || >=22.12.0`** (verified: `vite@8.2.2` engines field). A student who installs Node 18 in Week 0 sails through eight weeks and then hits an engine error the moment they run `npm create vite@latest` in Lab 10 — mid-semester, when a Node reinstall is the last thing they want.

**Fix:** change Lab 00 to "Node 22 LTS (v22.12 or higher)" in both the install step and the checklist. One-line edit, saves a week of support tickets.

### 1.3 Lab 00 asks for a screenshot the submission type can't accept

Lab 00's deliverable asks for "a screenshot showing your terminal." Every generated Canvas assignment uses `online_url,online_text_entry` — **no file upload**. Labs 01, 02, and 13 handle this correctly by telling students to commit screenshots into the repo and link them; Lab 00 does not.

**Fix:** either add `online_upload` to the orientation submission types in the build, or tell students to commit the screenshot to the repo and paste the link.

### 1.4 Confirm the Week 15 final-exam slot

Memory records the Week 15 Final Exam and Final Project as a **placeholder** due Fri Dec 11, 11:59 PM. Weber State's registration page lists Fall 2026 finals as **Dec 7–10**; the academic calendar PDF reads Dec 7–11. Confirm the university-assigned slot for this section and set the real date before students see it.

---

## 2. Structural — eight deliverables with nowhere to submit  ✅ resolved

The schedule and module overviews promise these as weekly deliverables. **None of them exists as a Canvas assignment.** The package contains exactly 25 assignments: 14 labs, 2 orientation items, 6 assignments, and one each for Project 1, Project 2, and the Final Project.

| Week | Promised deliverable | Canvas item |
|---|---|---|
| 05 | Project 1 Proposal (Milestone 1) | — none |
| 07 | Project 1 Build (Milestone 2) | — none |
| 10 | Project 2 Proposal (Milestone 1) | — none |
| 12 | Project 2 Build (Milestone 2) | — none |
| 12 | Final Project Pitch and Planning Starter (M1) | — none |
| 13 | Final Project Revised Wireframe and Data Plan (M2) | — none |
| 14 | Final Project Beta Review (M3) | — none |
| 15 | Course Reflection (M5) | — none (graded inside the Final Project rubric) |

The briefs actively instruct submission: Project 1 M2 says *"Submit the live URL and repo URL to Canvas with a brief note on what is remaining."* Project 2 M1 says the proposal *"will be reviewed against the problem statement first... returned for revision before you build."* Neither has a submission point, a due date, or a gradebook row.

This matters beyond bookkeeping. The whole late-term pacing strategy — which the briefs argue for at length — depends on milestones being real, graded checkpoints. Ungraded milestones get skipped, and Weeks 12–14 collapse into exactly the compression the course design is trying to prevent.

**Fix:** add eight zero-or-low-point assignments (or ungraded "not graded" submissions) via the build's `GENERATED_ASSESSMENTS`-style mapping, and add them to `import_to_canvas.md`. Also add the three surveys as module items — they exist as pages but sit in no module.

---

## 3. Sequencing — content required before it's taught  ✅ resolved

**Arrow-key tab navigation.** Assignment 3 (Week 06) requires it as a graded rubric row:

> `assignments/assignment-3:40` — "Arrow key navigation: Left/Right arrow keys move focus between tabs"
> `assignments/assignment-3:121` rubric — Excellent requires "arrow key navigation works"; Proficient is capped at "no arrow key nav"

Project 1 Option B (Weeks 5–8) requires it too (`projects/project-1:112`).

It is taught **only in Chapter 13** (`chapter-13:278–299`), assigned in Week 13 — seven weeks later. Lab 06, the tab lab in the same week as Assignment 3, teaches tabs *without* it and its checklist says only "All tabs are keyboard-reachable." The accessibility primer covers ARIA attributes but no keyboard interaction patterns.

Worse, Lab 06's pattern is the anti-pattern Chapter 13 warns against: `role="tab"` buttons all left in the natural tab order, where Chapter 13 line 299 specifies `tabindex="-1"` on inactive tabs so one Tab reaches the tablist and arrows navigate within it. A student who follows Lab 06 builds a widget that announces itself as a tablist but doesn't behave like one — measurably *less* usable than plain buttons.

Assignment 3's rationale prompt makes the gap explicit: *"How did you implement keyboard accessibility for the tab component — what did you have to learn that wasn't obvious?"* The honest answer is "nothing in this course taught me."

**Fix (pick one):**
- Add a short roving-tabindex section to the Week 06 lecture and Lab 06 (~30 lines, and it makes Lab 06 correct), **or**
- Move arrow-key navigation to the "Above baseline (stretch)" list in Assignment 3 and Project 1 until Chapter 13.

Related: **focus trapping** is required by Project 1 Option C (modal) and taught only in Chapter 13 (Week 13). Same fix applies.

---

## 4. Grading weights that contradict the syllabus  ✅ resolved

Canvas computes group grades by total points. Three places where the points don't produce the promised weighting:

**Exams.** The syllabus states: *"The Final Exam counts for approximately two-thirds of the 15% exam credit; the Midterm counts for one-third."* Actual points: Midterm 15, Final 17 → **47% / 53%**, essentially a 1:1 split. To hit 2:1 the Final needs ~30 points to the Midterm's 15.

**Assignments.** Every brief says *"Weight: One of six assignments (20% combined),"* implying equal sixths. Actual Canvas points:

| A1 | A2 | A3 | A4 | A5 | A6 | total |
|---|---|---|---|---|---|---|
| 50 | 60 | 75 | 80 | 70 | 80 | 415 |

Assignment 1 is 12.0% of the assignment grade; Assignments 4 and 6 are 19.3% each — **60% more weight**. Either equalize the points or change the briefs to state the real weights.

**Rubric-to-points conversion.** Labs use points equal to their rubric maximum (20 or 24), so grading is direct. Assignments and projects don't: Assignment 3's rubric maxes at 24 but the assignment is worth 75; Project 2's rubric maxes at 24 against 180 points; the Final Project's 40 against 220. With `use_for_grading` off (as `import_to_canvas.md` specifies), there is no documented conversion — the grader is left multiplying by 3.125 in their head, inconsistently, across a semester.

**Fix:** either set assignment/project points to their rubric maxima (matching the lab convention), or document the conversion factor per assignment in `import_to_canvas.md`.

---

## 5. Quiz bank — a real test-validity problem  ✅ resolved

The quiz sources are technically clean (lint passes; every item has exactly one 100-weight answer; points match counts). The design has two measurable weaknesses across all 78 non-true/false multiple-choice items:

**Position bias.** The correct answer is never in position 4. Ever.

| Position | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| Correct answers | 37 | 34 | 7 | **0** |

91% of correct answers sit in the first two positions. A student who has noticed this can raise their score without knowing content.

**Length as a tell.** The correct answer is the single longest option in **54 of 78 items (69%)**. The newer code-reading items make this near-deterministic — their correct answers carry an explanatory clause ("— finally runs whether the request succeeds or fails, ensuring...") while all three distractors are short assertions. Final Exam Q13–Q17 and Midterm Q13–Q15 are all this shape.

**Distractor quality is two-tiered.** The newer scenario items are well built. The older items lean on joke distractors — "Network routing," "DNS," "GPU memory," "Configure Wi-Fi," "Generate PDFs," "The postal location of a user," "A network cable," "A random folder." These are answerable without any course knowledge, so they measure nothing.

**Also:** Final Exam Q1, Q5, and Q12 are true/false items encoded as `multiple_choice_question` with True/False answer pairs, while the midterm uses `true_false_question` for the same shape. Q1 lists False first. Cosmetic, but inconsistent.

**Fix (a 60–90 minute pass, not a rewrite):**
1. Shuffle answer positions so correct answers distribute across all four slots — or enable Canvas's per-attempt answer shuffling.
2. Move the explanatory clause out of the correct answer into the item's feedback field, so all four options are the same shape.
3. Replace the joke distractors with plausible near-misses (for "What is HTML responsible for?": "Structure and meaning" vs "Structure and styling" vs "Content and behavior" vs "Layout and spacing").
4. Retype the three final-exam items as `true_false_question`.

**Coverage note:** Quiz 4 (DOM, events, forms — arguably the course's highest-value skills, two chapters) is only **5 items**, and Quiz 8 covers the two longest chapters in **4 items**. Quiz 2 gets 8 items for one chapter. Worth rebalancing when you next touch the bank.

---

## 6. Code examples that don't produce the stated output  ✅ resolved

**`lectures/week-11-lecture.md:51`** — verified wrong for this course's own timezone:

```js
console.log(formatDate("2025-03-15"));   // claims "March 15, 2025"
```

`new Date("2025-03-15")` parses as UTC midnight; `toLocaleDateString` renders it in local time. In America/Denver this prints **"March 14, 2025."** (Confirmed by execution.) This is the single most common date bug in JavaScript, and the lecture reproduces it while claiming the wrong output. Either fix the comment and use it as a teaching moment, or change the input to `"2025-03-15T12:00:00"`.

**`lectures/week-11-lecture.md:127`** — the "What this creates" tree for `npm create vite@latest --template vanilla` shows `main.js` and `style.css` at the project root. The actual scaffold (verified against the current template) puts them in **`src/`**. Lab 10 correctly says `src/main.js`, so the lecture and its own lab disagree.

**`lectures/week-04-lecture.md`** — the function-forms example declares `const greet` twice inside one code fence (declaration, expression, arrow). Copy-pasting it throws `SyntaxError: Identifier 'greet' has already been declared`. Rename to `greetExpr` / `greetArrow`, or split into three fences.

**`labs/lab04:156`** — the stated test expectation is wrong:

> "Experience: beginner, distance: 10, time: 5 → should find 'Ridgeline Path' or similar"

`findTrail` is specified to return the **first** match. With the provided data that is **Lakeside Loop** (beginner, 2.5 mi, 1.5 h). Verified by execution. The hedge "or similar" papers over a spec the lab itself defines precisely — students who get it right will think they got it wrong.

**`lectures/week-09-lecture.md`** — in `searchPokemon`, the `if (!pokemon) showEmpty()` branch is unreachable: a parsed JSON object is always truthy. The four-state model is the lecture's centerpiece, and the empty state is demonstrated with dead code.

---

## 7. Cross-document contradictions  ✅ resolved

**Assignment 5 — the same items are both required and optional.** `constants.js` and `ARCHITECTURE.md` appear under "Required output structure" ("You must also include:"), in the verification checklist, and in the rubric's Excellent column — *and* as the first two bullets under **"Above baseline (stretch)"** (`assignment-5:154`). A student reading top-down and a student reading bottom-up build different projects.

**Project 2 — a checkpoint that asks about its own week.** Milestone 2 is due end of Week 12, and its `checkpoint.md` prompt asks *"What two features remain for Week 12?"* (`project-2:86`). Should be Weeks 13–14.

**Week 13 lecture misdescribes Assignment 6.** `week-13-lecture.md:208`: *"Assignment 6 asks you to document the data flow of your Project 2 components."* Assignment 6 is a multi-step Vue form workflow with no such requirement and no connection to Project 2.

**Week 15 lecture misdescribes the reflection.** `week-15-lecture.md:149`: *"The Course Reflection asks you to identify the moment in the semester when something clicked."* The actual prompt has five questions, none of which is that. Line 146 also tells students to *"share the README in the Final Studio discussion"* — a discussion that does not exist (see §1.1).

**Lab 12 promises `defineEmits` and never uses it.** `lab12:11` lists "Component communication with `defineProps` and `defineEmits`" under Skills practiced. Both child components are props-only; no emit appears anywhere in the lab. It's the same week the Week 13 lecture teaches emits, so the gap is visible to students.

**Lab 10 contradicts the course's own `innerHTML` rule.** Labs 04, 05, and 08 grade "no `innerHTML`" and mark `innerHTML` for dynamic content as *Developing*. Lab 10's starter and refactored code use `grid.innerHTML = ''` (lines 63, 168) to clear a container, and Assignment 5's starter does the same (line 43). Week 06's lecture explicitly teaches `textContent = ""` as the clearing idiom. `innerHTML = ''` is safe, but the mixed message undermines a rule the course grades on. Use `replaceChildren()` or `textContent = ''`.

**All 32 module overviews tell Weeks 00 and 15 to read a chapter that doesn't exist.** The five-step Success plan is byte-identical in all 16 base and all 16 virtual modules — step 1 is "Read the module overview and chapter" (virtual: "Before Monday: skim the module overview and read the chapter"). Weeks 00 and 15 both state in Resources: "No textbook chapter this week." Four documents contradict themselves.

The identical boilerplate is a broader quality issue: the rest of each module overview is thoughtfully week-specific (real time estimates, tailored checkpoint questions, targeted struggle notes), which makes the generic five steps read as filler. Weeks 02, 04, 06, and 07 are all 10–12-hour assignment weeks with no "What students usually struggle with" section, while Weeks 00, 09, and 12–15 have one.

**Milestone 3 headings are empty.** In both Project 1 and Project 2, `## Milestone 3 — Final Submission` is followed by a due date, a horizontal rule, and then a different H2. The requirements that follow are implicitly M3's, but the heading itself has no body.

**Lab 13 off-by-one.** Part 6's manual walkthrough lists **five** checklist items; the rubric (`lab13:230`) requires "All six checklist items verified."

**Project 1 Milestone 2 mentions `node_modules/` and `dist/`.** Project 1 is vanilla HTML/CSS/JS at Week 7 — Vite isn't introduced until Week 11. The requirement is inert and confusing there.

**Lab 13's GitHub Pages advice omits the fix its own week teaches.** "Common deployment issues → Assets not loading: check that all import paths are relative." The Week 14 lecture (line 140) and Chapter 14 (line 131) both name the real fix — `base: '/repo-name/'` in `vite.config.js` — and Quiz 8 Q4 tests exactly that. Lab 13 should point at it.

**Assignment 6 component count.** The structure lists seven files; the rubric says "All five component types present." Defensible if "types" means categories, but a student counting components will disagree with their grader.

**"Full-stack front-end."** The Final Project's Skills line reads "Full-stack front-end" while its Constraints say "No full-stack server." Confusing phrase; "end-to-end front-end" reads better.

---

## 8. Calendar — no holidays anywhere  ✅ resolved

There is **not one mention** of Labor Day, Fall Break, or Thanksgiving in any module, schedule, syllabus, or lecture, in either modality. For Fall 2026:

- **Labor Day, Monday September 7** = **Week 02 Monday.** The virtual section's Week 02 overview schedules a live Monday 9:30 session ("Semantic HTML, CSS architecture, and a live mobile-first layout demo") on a university holiday.
- **Thanksgiving, Thursday November 26** falls in **Week 13** (Nov 23–29). The virtual Week 13 schedules a Wednesday Nov 25 session — the day before Thanksgiving, when attendance and travel are a real factor. Week 13 is also the course's heaviest week (Assignment 6 + Lab 12 + Final Project Milestone 2 + the pulse-check survey).
- The virtual schedule's "August 24 – December 4, 2026" matches the university's last day of classes. Good.

**Fix:** add a holiday line to `course/schedule.md` and `virtual/course/schedule.md`, and adjust the Week 02 and Week 13 live-session plans (async makeup, recorded demo, or shifted content).

---

## 9. Workload  ✅ resolved

Summing the module time estimates gives **~163 hours** across 16 weeks. The federal credit-hour standard for a 3-credit course is ~135 hours. The course is honestly self-reporting about **20% over** — and the estimates look realistic, not padded.

Twelve of sixteen weeks are estimated at 10–13 hours. The compression is worst exactly where the course already knows it is:

| Week | Load | Contents |
|---|---|---|
| 12 | 11–13 h | Quiz 7 + Lab 11 (first Vue) + Project 2 Build M2 + Final Project Pitch M1 |
| 13 | 10–12 h | Assignment 6 (called "the most complex individual assignment") + Lab 12 + Final Project M2 + survey + **Chapter 13 (4,162 words — 3× the average chapter)** |
| 14 | 10–12 h | Quiz 8 + Lab 13 QA report + Project 2 final + Final Project Beta M3 + **Chapter 14 (3,439 words)** |

The two longest chapters in the book land in the two most compressed weeks. Chapter 13 alone is longer than Chapters 2 and 3 combined.

The mitigations already in place are good — the Vue transition guide, Assignment 6's build order and "minimum viable path," Project 2's pacing block, the Final Project start-ahead plan. `CONTEXT.md` correctly names late-term compression as the open question and says to wait for first-delivery evidence. That's the right call; this review just quantifies the size of it. One cheap lever available now: split Chapter 13 across Weeks 12–13 rather than dropping all 4,000 words into Week 13.

---

## 10. Smaller items  ✅ resolved

- `lectures/week-03-lecture.md:54` — "a 25-year-old bug." JavaScript shipped in 1995; it's ~31 years old in 2026. Say "a bug from the language's first version."
- `lectures/week-01-lecture.md` — "served from cache (status 304)." A 304 is a revalidation response; true cache hits show "(from disk cache)" with no status.
- `lectures/week-08-lecture.md` — the extracted `requireField(inputId, errorId)` hardcodes "Name is required." for any field, and the call sites use bare `return` at top level. The refactoring lesson would land better with the message as a parameter.
- **Quiz 8 Q1** — "Lighthouse helps evaluate: Performance, accessibility, and best practices" omits SEO, while the Week 14 lecture, Chapter 8, and Chapter 14 all correctly say four categories. Add SEO to the keyed answer.
- **Chapter 13** opens with "You have been applying... Lighthouse audits" — Lighthouse is taught in Week 14, one week *after* Chapter 13 is assigned.
- **Module resource links.** Weeks 12–15 link the relevant project briefs in Resources; Weeks 05, 07, and 10 list project milestones as deliverables but link no brief.
- **Support pages are unplaced.** The accessibility primer, API troubleshooting guide, screen reader guide, Vue transition guide, reflection prompt, and three surveys all exist as Canvas pages but appear in no module — reachable only through inline links in overviews.
- **Reflection length vs depth.** The reflection prompt asks for "6–10 sentences total" across five prompts (~1.5 sentences each) while the rubric demands "specific, concrete details" on all five. The Final Project rationale has the same tension (6–8 sentences, four prompts).
- **`import_to_canvas.md`** says "Rubric point totals intentionally differ from assignment point values" — true for assignments and projects, but labs match exactly. Worth stating the distinction.
- **Lab 03 debug exercise** — bug 3 is `if (userAge == 28)` logging "Age matched with strict equality." Fixing it to `===` makes the branch false and the message disappear. The lab says "do not rewrite the logic," but doesn't say what the corrected output should be. Students will reasonably disagree about the right fix.
- **Lab 03 Part 3** tells students to "open `debug.js` in a browser" without saying to link it from an HTML file.

---

## What's working — don't touch it

Worth naming, because a defect list distorts the picture:

- **The lecture → lab → assignment chain is deliberate.** Every lecture's Bridge section names the specific lab and quiz it feeds, and (with the two exceptions in §7) does it accurately. This is rarer than it should be.
- **Accessibility is structural, not decorative.** The primer lands in Week 01 and explicitly maps which ARIA attribute is needed for which assignment. Every lab and project rubric has a keyboard/ARIA row. The Week 07 lecture cites specific WCAG success criteria (3.3.1, 2.4.3). The Week 14 lecture states plainly that automated tools catch only 30–40% of issues.
- **The four-state async model** (loading / success / error / empty) is introduced in Week 09 and then reinforced identically in Lab 08, Assignment 4, Project 2, and the Final Project. That consistency is why students will actually internalize it.
- **Data-first design** is taught in Week 05 and carried through Lab 05, Week 06's render pattern, Lab 08's normalizer, and Project 2's normalize module.
- **The API viability check** (CORS, rate limits, attribution, reliability) appears in Assignment 4, Project 2, and the Final Project with identical four-bullet framing. Rare in an intro course and genuinely professional.
- **The build/lint tooling works.** Lint, `build --check`, and `validate` pass in both modalities. The lint catches real classes of drift — links, fences, rubric shape, quiz points, due weeks, CSV freshness, virtual-override consistency.
- **The virtual overrides are done right** — attendance policy, recording policy, per-week live-session plans, and a session-aware success plan, without duplicating anything that should stay shared.
- **The pacing scaffolds in the late-term briefs** — Assignment 6's build order, its "minimum viable path," Project 2's week-by-week pacing, the Final Project's start-ahead plan — are the work of someone who has watched students hit this wall before.

---

## Suggested order of work

**Today (before Week 0 opens)** — §1.1 create the Help & Questions board, §1.2 Node version, §1.3 Lab 00 screenshot, §1.4 confirm the final-exam slot, §8 Labor Day (Week 02 is only two weeks out).

**This week** — §2 add the eight milestone assignments (they start mattering in Week 05, and adding them now means due dates get set in one pass).

**Before Week 04** — §6 the Lab 04 expected-output fix and the Week 04 `const greet` fence.

**Before Week 06** — §3 the arrow-key tabs decision. This is the one that changes what students build.

**Before grading Assignment 1 (Week 02)** — §4 the rubric-to-points conversion, at minimum documented.

**Before Week 11** — §6 the Week 11 lecture's date output and Vite scaffold tree.

**When convenient** — §5 the quiz-bank pass (the highest-value item for assessment quality, but nothing breaks if it waits for the between-terms window), §7 the contradiction cleanup, §9 the Chapter 13 split.
