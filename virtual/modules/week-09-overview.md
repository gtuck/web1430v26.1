# Week 09 Overview: Async JavaScript and APIs

## This week
- Theme: Async JavaScript and APIs
- Lecture: Promises, Fetch, Async/Await, and Failure States
- Lab: Lab 08 – Build an API-Powered Viewer
- Deliverables: Quiz 5, Assignment 4

## Live sessions
- **Monday 9:30–10:45 AM:** Promises, fetch, async/await, and failure states, with a live API request demo covering loading, error, empty, and success states.
- **Wednesday 9:30–10:45 AM:** Lab 08 API-viewer studio and a response-shape debugging clinic; run your Assignment 4 API viability check live if you're unsure.
- Sessions meet in the [class Zoom room](https://weber.zoom.us/j/82982068432); recordings are posted to Canvas.

## Success plan
1. Before Monday: skim the module overview and read the chapter
2. Attend Monday's live session for the week's core concepts and demo
3. Start the lab or studio activity; bring blockers to Wednesday's session
4. Attend Wednesday's live session for guided lab work, code review, and Q&A
5. Finish the weekly assessment or milestone, then commit and deploy your work

## Resources
- [Lecture notes: Promises, Fetch, Async/Await, and Failure States](../lectures/week-09-lecture.md)
- [Chapter 9: Fetch, JSON, and Remote Data](../textbook/chapters/chapter-09-fetch-json-and-remote-data.md)
- [API Troubleshooting Guide](../course/api-troubleshooting-guide.md) — Use this if your API response shape, null values, or rate limits slow down Assignment 4.
- **Time estimate:** 10–12 hours (reading, lab, quiz, Assignment 4)

## What students usually struggle with
- It is tempting to jump straight from `fetch()` to rendering cards. First confirm the response shape and decide how loading, error, empty, and success states should differ.
- Many API bugs are data-shape bugs, not syntax bugs. Log one real response and normalize it before you build more UI.

## Checkpoint question
Can you describe exactly what the page should show in loading, success, empty, and error states before you write the full fetch flow?
