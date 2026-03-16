Before importing, rebuild and validate the package from the source files:

```bash
python3 scripts/build_canvas_package.py build
python3 scripts/build_canvas_package.py validate
```

Then import `canvas/WEB1430-Canvas-Export.imscc` into Canvas using either **Canvas Course Export Package** or **Common Cartridge 1.x Package** in Course Settings > Import Course Content.

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
