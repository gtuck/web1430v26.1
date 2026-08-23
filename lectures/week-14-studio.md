# Week 14 Studio Notes: QA Audit Studio and Fix Triage

## Session focus

Session 1 ran Lighthouse and shipped a build. Session 2 audits your own projects in the Lab 13 studio and then triages the findings — an audit that does not become a prioritized fix list is just a bad mood.

## Before class

- Deploy something, anything, so you have a live URL to audit.
- Run Lighthouse against it once and save the report. Reading your own numbers beats reading mine.

## Studio plan

1. **Reading a Lighthouse report together (10 min).** Which numbers matter, which are noise, and why the accessibility score is a floor rather than a grade — it cannot detect most of what actually breaks for a screen-reader user.
2. **Lab 13 audit studio (25 min).** Run the automated audit, then do the manual pass Lighthouse cannot: keyboard-only navigation, visible focus, and heading order.
3. **Fix triage workshop (25 min).** Sort your findings into three piles — breaks a user, fails the rubric, nice to have. Fix everything in the first pile before the session ends.
4. **Deployment troubleshooting and Quiz 8 readiness (15 min).** Blank GitHub Pages deploys, wrong base paths, forgotten build steps, and the vocabulary Quiz 8 uses.

The virtual section runs this plan live, Wednesday 9:30–10:45 AM (75 minutes). The online section works the same sequence self-paced; where the plan says "the room" or "a volunteer," use the Help & Questions discussion board.

## Accessibility connection

Lighthouse accessibility scores measure automated rule compliance, not lived experience. The goal of this week's audit is not a number — it is building the habit of checking your work against the needs of real users. Keyboard-only navigation is used by people with motor disabilities, power users, and people with broken pointing devices. Screen readers are used by people who are blind or have low vision. Both groups are part of your audience on any public web project, and building with them in mind from the start is far less work than retrofitting accessibility at the end.

## Practice prompt

Run a Lighthouse audit on your Project 2. Document every Accessibility failure in a short list. Fix at least three failures. Re-run Lighthouse and screenshot the before and after scores. Then deploy the fixed build to GitHub Pages or Netlify and submit the live URL alongside your fix list.

## Bridge

Lab 13 — Lighthouse, Accessibility, and Deployment walks you through this exact sequence: audit, fix, deploy, and document what changed. Quiz 8 is now a short readiness check on the core concepts behind that work: Lighthouse categories, common accessibility failures, and deployment verification steps. Project 2 final submission requires a live deployed URL, and Final Project Beta asks you to carry those same QA habits forward.
