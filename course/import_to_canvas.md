Before importing, rebuild and validate the package from the source files:

```bash
python3 scripts/build_canvas_package.py build
python3 scripts/build_canvas_package.py validate
```

Then import `canvas/WEB1430-Canvas-Export.imscc` in Course Settings > Import Course Content with Content Type set to **Common Cartridge 1.x Package**.

Do **not** select "Canvas Course Export Package" — that converter expects a byte-faithful Canvas-native export and fails on every quiz and assignment in this generated package (verified July 2026). Leave "Convert content to New Quizzes" unchecked; the quizzes are authored as Classic Quiz QTI. If re-importing into a course that already received this package, run Reset Course Content (or use a fresh course shell) first so page links resolve to the new copies instead of duplicate `-2` page URLs.

After import, complete these instructor-side setup steps before the term starts:

1. Import the course learning outcomes into Canvas Outcomes:
   - Go to Course > Outcomes > Import and upload `course/canvas-outcomes.csv`.
   - This creates a "WEB 1430: Client-Side Web Development" group containing the 10 course outcomes from `course/learning_outcomes.md`, each with the course's four rubric levels (Excellent 4 / Proficient 3 / Developing 2 / Incomplete 1) and mastery set at Proficient.
   - The `.imscc` import does not carry outcomes, so this CSV step is required each time a fresh course shell is set up. If you edit `course/learning_outcomes.md`, update the CSV to match.
   - After importing, outcomes can be attached to assignment rubrics via Manage Rubrics to track mastery while grading.
2. Create actual anonymous response forms for:
   - Week 05 Mid-Course Check-In
   - Week 11 Late-Course Check-In
   - Week 13 Vue and Workload Pulse Check
3. Use the question banks in:
   - `course/student-survey-week-05.md`
   - `course/student-survey-week-11.md`
   - `course/student-survey-week-13.md`
4. Review `course/first-delivery-monitoring-guide.md` and set up the tracking sheet before students reach Week 11.
