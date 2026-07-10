Before importing, rebuild and validate the package from the source files:

```bash
python3 scripts/build_canvas_package.py build
python3 scripts/build_canvas_package.py validate
```

Then import `canvas/WEB1430-Canvas-Export.imscc` in Course Settings > Import Course Content with Content Type set to **Common Cartridge 1.x Package**.

Do **not** select "Canvas Course Export Package" — that converter expects a byte-faithful Canvas-native export and fails on every quiz and assignment in this generated package (verified July 2026). Leave "Convert content to New Quizzes" unchecked; the quizzes are authored as Classic Quiz QTI. If re-importing into a course that already received this package, run Reset Course Content (or use a fresh course shell) first so page links resolve to the new copies instead of duplicate `-2` page URLs.

After import, complete these instructor-side setup steps before the term starts:

1. Import the course learning outcomes into Canvas Outcomes:
   - Go to Course > Outcomes > Import and upload `instructor/canvas-outcomes.csv`.
   - This creates a "WEB 1430: Client-Side Web Development" group containing the 10 course outcomes from `course/learning_outcomes.md`, each with the course's four rubric levels (Excellent 4 / Proficient 3 / Developing 2 / Incomplete 1) and mastery set at Proficient.
   - The `.imscc` import does not carry outcomes, so this CSV step is required each time a fresh course shell is set up. If you edit `course/learning_outcomes.md`, update the CSV to match.
   - After importing, outcomes can be attached to assignment rubrics via Manage Rubrics to track mastery while grading.
2. Create the course rubrics in Canvas. The 24 rubrics (14 labs, 6 assignments, 3 projects, and the Final Project course reflection) are generated from the rubric tables in the course briefs into `instructor/canvas-rubrics.csv`.

   **Import:** go to Course > Rubrics > Import Rubrics and upload `instructor/canvas-rubrics.csv`. This creates all 24 rubrics as course-level rubrics.

   **Manual follow-up (Canvas's CSV import cannot do these):**

   a. Attach each assignment/project rubric to its Canvas assignment: open the assignment, click "+ Rubric" > Find a Rubric, and pick the rubric with the same title. Nine to attach: Assignments 1–6, Project 1, Project 2, and the Final Project.

   b. Add the learning outcome(s) to each rubric for mastery tracking: edit the rubric, click "Find Outcome", and add the mapped outcome(s) from the "WEB 1430: Client-Side Web Development" group. Recommended mapping (short outcome titles from `instructor/canvas-outcomes.csv`):

   | Rubric | Outcome(s) |
   |--------|-----------|
   | Lab 00 | Git & GitHub Workflow |
   | Lab 01 | DevTools & Debugging |
   | Lab 02 | Responsive Semantic Pages |
   | Lab 03 | Readable JavaScript, DevTools & Debugging |
   | Lab 04, Lab 05, Lab 10 | Readable JavaScript |
   | Lab 06 | DOM Interaction |
   | Lab 07 | Accessible Forms |
   | Lab 08 | APIs & Remote Data |
   | Lab 09 | Client-Side State |
   | Lab 11, Lab 12 | Component Thinking |
   | Lab 13 | Project Delivery |
   | Assignment 1 | Responsive Semantic Pages |
   | Assignment 2, Assignment 5 | Readable JavaScript |
   | Assignment 3 | DOM Interaction |
   | Assignment 4 | APIs & Remote Data |
   | Assignment 6 | Component Thinking, Accessible Forms |
   | Project 1 | Responsive Semantic Pages, DOM Interaction, Accessible Forms |
   | Project 2 | APIs & Remote Data, Client-Side State |
   | Final Project | Project Delivery, Git & GitHub Workflow |
   | Final Project – Course Reflection | Project Delivery |

   At minimum, add outcomes to the six assignment rubrics and three project rubrics — those are attached to graded assignments, so they feed the Learning Mastery gradebook directly. The lab-rubric outcomes matter only if labs later become rubric-graded assignments.

   **Notes:**
   - Rubric point totals (4 points per criterion) intentionally differ from assignment point values — the rubrics are grading guides and outcome-mastery instruments, not point calculators. Leave "Use this rubric for assignment grading" off unless you want rubric-driven scores.
   - If a brief's rubric table changes, regenerate the CSV with `python3 scripts/build_canvas_rubrics_csv.py`, delete the affected rubric in Canvas, and re-import.
3. Create actual anonymous response forms for:
   - Week 05 Mid-Course Check-In
   - Week 11 Late-Course Check-In
   - Week 13 Vue and Workload Pulse Check
4. Use the question banks in:
   - `course/student-survey-week-05.md`
   - `course/student-survey-week-11.md`
   - `course/student-survey-week-13.md`
5. Review `instructor/first-delivery-monitoring-guide.md` and set up the tracking sheet before students reach Week 11.
