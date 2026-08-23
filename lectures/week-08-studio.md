# Week 08 Studio Notes: Project 1 Polish Studio and Midterm Review

## Session focus

Session 1 reviewed Weeks 01–07 and the refactoring patterns that hold a larger project together. Session 2 is a polish studio for Project 1 plus the last structured midterm review. The exam itself is taken in Canvas inside the Week 08 window, not during a class meeting.

## Before class

- Run the Project 1 polish checklist from the lecture notes and note what fails.
- List the three midterm topics you are least sure of. The review is built from what the room brings.

## Studio plan

1. **Extract-a-function round (15 min).** A volunteer's longest function, refactored live: better names, a guard clause at the top, and one job per function.
2. **Project 1 polish studio (30 min).** Work the checklist — contrast, keyboard order, console errors, README, deployed link. These are cheap to fix and they are rubric line items, which is an unusually good combination.
3. **Midterm review (25 min).** Question by question on the topics you brought. Scope, format, timing, and what an "explain the difference" question actually expects you to write.
4. **Exam logistics (5 min).** Where the exam lives, how long the window is open, and what to do if something goes wrong mid-attempt.

The virtual section runs this plan live, Wednesday 9:30–10:45 AM (75 minutes). The online section works the same sequence self-paced; where the plan says "the room" or "a volunteer," use the Help & Questions discussion board.

## Accessibility connection

Refactoring is an ideal time to fix accessibility issues you rushed past earlier. When you extract a function that renders a card or a list item, you can ensure the markup it generates includes proper roles, labels, and keyboard-accessible controls once — rather than patching each copy individually. Consistent structure also makes it easier for screen reader users, since repeated components behave predictably.

## Practice prompt

Take any JavaScript file from your Project 1 and apply two refactors:
1. Extract at least one repeated block into a named function.
2. Replace at least one magic string or number with a named `const`.

After each change, reload the page and confirm everything still works. Write a two-sentence comment at the top of the file describing what you changed and why.

## Bridge

The Midterm Exam opens at the start of Week 08 and covers all material through Week 07 — review the high-priority topic list in the Session 1 notes and use your own past assignments as study material. This week's chapter reading, Chapter 8 (Design Systems and Small Front-End Architecture), goes deeper on this week's refactoring themes: design tokens, naming conventions, and file organization — apply its patterns during Project 1 polish. Project 1 is also due this week; use the polish checklist to run a final quality pass before submitting. Starting in Week 09, the course shifts to new territory — asynchronous JavaScript — so a clean mental slate after the midterm will help.
