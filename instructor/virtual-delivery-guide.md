# Virtual Section Delivery Guide

Instructor-side guide for running WEB 1430 as a **virtual (synchronous)** section. Not part of the Canvas export.

## Section facts

- **Semester:** August 24 – December 4, 2026; final exam and presentations in the Week 15 finals window
- **Live sessions:** Monday and Wednesday, 9:30–10:45 AM (Mountain Time)
- **Class Zoom room:** https://weber.zoom.us/j/82982068432
- **Virtual office (office hours):** https://weber.zoom.us/j/8013088825
- **Virtual office hours:** Monday and Wednesday, 8:00–9:00 AM and 12:30–2:00 PM, appointment required via https://calendar.app.google/5iHL7QJQDYRb2jeb8

## How the virtual variant works in this repo

Virtual overrides live in `virtual/<same relative path as the base file>`. Any source without an override is shared between modalities. Current overrides: `virtual/home.md`, `virtual/course/syllabus.md`, `virtual/course/schedule.md`, `virtual/lectures/week-00-lecture.md`, and all 16 `virtual/modules/week-*-overview.md` files.

Build and verify:

```bash
python3 scripts/build_canvas_package.py build --modality virtual
python3 scripts/build_canvas_package.py validate --modality virtual
python3 scripts/lint_course.py
```

This produces `canvas/WEB1430-Virtual-Canvas-Export.imscc` (import it exactly like the online package: Common Cartridge 1.x, no New Quizzes conversion, fresh/reset shell). The Outcomes and Rubrics CSVs are shared — the post-import setup in `import_to_canvas.md` applies unchanged to virtual sections.

Editing rules: a shared-file edit requires rebuilding **both** packages; an override edit requires rebuilding only the virtual package. Lint enforces that overrides keep the base H1 title and identical `- Deliverables:` lines, so the two modalities cannot drift on page identity or due dates.

## Weekly session pattern

Each week's module overview contains that week's Monday/Wednesday agendas (the `## Live sessions` section). The standing pattern:

- **Monday — concepts.** Teach the week's lecture topic live with a demo. The written lecture notes cover the same ground; students use them as the post-session reference. Close with the module's checkpoint question as a quick poll or cold-call.
- **Wednesday — studio.** Guided lab work, code review of volunteer solutions, and Q&A. This is where the harder-week "What students usually struggle with" items should be surfaced proactively.

Session prep that pays off: have the week's starter repo cloned and the demo half-built before class; live-code the second half. Keep the last ten minutes of Wednesday for deliverable logistics (what's due Sunday and where).

## Zoom logistics

- Enable waiting-room bypass for authenticated Weber State accounts; require sign-in to join.
- Record every session to the cloud and post the link in that week's Canvas module promptly — the syllabus promises recordings, and the attendance policy leans on them as the recovery path.
- Enable live captions. Encourage chat participation as an equal channel to voice.
- For lab debugging, have students share their screen; for shy students, offer breakout-room 1:1s during studio time.

## Adjustments from the online section

- **Surveys (Weeks 5, 11, 13):** still run as anonymous forms, but announce them at the end of the relevant Wednesday session for better response rates.
- **Exams:** still taken in Canvas within the exam window, not during session time. Week 8's Monday session is the structured midterm review; Week 15 follows the university final-exam schedule for the exam and Final Studio presentations.
- **Help channels:** the Canvas Help & Questions board remains, but expect most support demand to shift to Wednesday studios and office-hour appointments. The monitoring workflow in `first-delivery-monitoring-guide.md` still applies; session attendance becomes an additional early-warning signal alongside submission data.
- **Week 15:** the Final Studio runs as live presentations during session time. Plan roughly 5–7 minutes per student; if enrollment exceeds the two sessions, collect recorded demos and use class time for a curated subset.

## First-week checklist

1. Build/import the virtual `.imscc`; complete the shared post-import setup (`import_to_canvas.md`).
2. Verify the Zoom room link and the office-hours booking link work from a student account.
3. Configure cloud recording and captions before the first session.
4. Post a welcome announcement naming the first session date/time (Monday, August 24, 9:30 AM MT).
5. Run the Week 00 Wednesday setup clinic with extra time — Git setup issues surface live in the virtual section instead of asynchronously on the board.
