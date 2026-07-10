Before importing, rebuild and validate the package from the source files:

```bash
python3 scripts/build_canvas_package.py build
python3 scripts/build_canvas_package.py validate
```

Then import `canvas/WEB1430-Canvas-Export.imscc` in Course Settings > Import Course Content with Content Type set to **Common Cartridge 1.x Package**.

Do **not** select "Canvas Course Export Package" — that converter expects a byte-faithful Canvas-native export and fails on every quiz and assignment in this generated package (verified July 2026). Leave "Convert content to New Quizzes" unchecked; the quizzes are authored as Classic Quiz QTI. If re-importing into a course that already received this package, run Reset Course Content (or use a fresh course shell) first so page links resolve to the new copies instead of duplicate `-2` page URLs.

After import, complete these instructor-side setup steps before the term starts:

1. Create actual anonymous response forms for:
   - Week 05 Mid-Course Check-In
   - Week 11 Late-Course Check-In
   - Week 13 Vue and Workload Pulse Check
2. Use the question banks in:
   - `course/student-survey-week-05.md`
   - `course/student-survey-week-11.md`
   - `course/student-survey-week-13.md`
3. Review `course/first-delivery-monitoring-guide.md` and set up the tracking sheet before students reach Week 11.
