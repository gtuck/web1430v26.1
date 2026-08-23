# Week 01 Studio Notes: DevTools Inspection Studio

## Session focus

Session 1 traced the path from a typed URL to painted pixels. Session 2 opens that same pipeline in DevTools on real pages and reads what the browser actually did — then turns those observations into Quiz 1 preparation.

## Before class

- Complete at least the first two Lab 01 inspection tasks so you have findings to compare against everyone else's.
- Pick one public page you use often. You will inspect it live.

## Studio plan

1. **Findings round-robin (15 min).** Share one thing in the Elements tab that surprised you. Surprises that repeat across the room usually mark a shared misconception worth naming out loud.
2. **Reading the network waterfall (20 min).** Load a page with the Network tab open and read the waterfall together: which requests block rendering, which are deferred, what the bar segments mean, and where the `defer` and `async` difference actually shows up.
3. **Inspection studio (25 min).** Work your own Lab 01 pages with help available. Bring anything that does not match what the lecture notes predicted — those are the interesting cases.
4. **Quiz 1 readiness (15 min).** Predict-the-output on script placement, then a pass over the vocabulary Quiz 1 uses: DOM, CSSOM, render tree, paint, request, response.

The virtual section runs this plan live, Wednesday 9:30–10:45 AM (75 minutes). The online section works the same sequence self-paced; where the plan says "the room" or "a volunteer," use the Help & Questions discussion board.

## Accessibility connection

The DOM tree that the browser builds from your HTML is the same structure that screen readers traverse to announce page content to users who cannot see the screen. If your HTML is not semantic — for example, if you build a navigation list out of `<div>` tags instead of `<nav>` and `<ul>` — the DOM still exists but carries no meaning for assistive technologies. Understanding the DOM as a tree (not just a visual layout) is the foundation for writing accessible markup starting next week.

## Practice prompt

Pick any public website you visit regularly. Open DevTools and go to the Network tab. Reload the page. Answer these questions in writing (a text file or Canvas journal entry):
- How many total requests were made?
- What was the size of the initial HTML document?
- Did any requests return a non-200 status code? If so, what were they?
- Can you find a `<script>` tag in the Elements panel? Does it have `defer` or `async`?

## Bridge

Lab 01 – Inspecting the Web asks you to use the Network and Elements tabs to document the load behavior of an assigned page — exactly the skills practiced in the Session 1 demo and the practice prompt above. Quiz 1 covers the request/response cycle, render-blocking, and the difference between `defer` and `async`; re-read the script placement section before taking it. Bring any DevTools questions to the Help board before the Sunday deadline.
