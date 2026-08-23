# Week 02 Studio Notes: Layout Studio and Assignment 1 Kickoff

## Session focus

There is no Session 1 meeting this week — Labor Day, Monday September 7, is a university holiday, and the Week 02 lecture notes stand in for it. This session therefore does double duty: a condensed live version of the mobile-first demo and Q&A on the reading, then the Lab 02 layout studio and the Assignment 1 kickoff.

## Before class

- Read the Week 02 lecture notes end to end. They cover everything the first session would have covered.
- Write down the two things that were least clear. The condensed demo is built around what you bring.
- Have the Lab 02 starter files open.

## Studio plan

1. **Reading Q&A (15 min).** Work the questions you brought from the lecture notes. Semantic element choice and `min-width` breakpoint direction are the two that usually need a second pass.
2. **Condensed mobile-first demo (20 min).** Build the layout from the notes live: custom properties first, single-column base second, then one `min-width` breakpoint. Watch where Flexbox is the right tool and where Grid is.
3. **Lab 02 layout studio (25 min).** Rebuild with support available. Check contrast as you go rather than at the end — retrofitting a palette is far more work than choosing one.
4. **Assignment 1 kickoff (15 min).** Requirements walkthrough, the rubric read aloud, and the accessibility quick-reference checklist you will use on every assignment from here on.

The virtual section runs this plan live, Wednesday 9:30–10:45 AM (75 minutes). The online section works the same sequence self-paced; where the plan says "the room" or "a volunteer," use the Help & Questions discussion board.

## Accessibility connection

The HTML5 landmark elements — `<header>`, `<nav>`, `<main>`, `<footer>` — expose implicit ARIA landmark roles to the browser's accessibility tree. Screen reader users can navigate directly to any landmark by pressing a shortcut key (e.g., pressing `M` in NVDA jumps to `<main>`). A page built entirely from `<div>` elements forces screen reader users to read linearly through every element to find the content they want. Using semantic elements is therefore a significant navigational aid, not just a stylistic choice.

## Practice prompt

Build a single HTML page for a fictional blog post. The page must include: a `<header>` with a site name and `<nav>`, a `<main>` containing one `<article>` with at least two paragraphs and one `<figure>` with `alt` text and a `<figcaption>`, and a `<footer>` with a copyright line. Style it with at least four CSS custom properties defined at `:root`. Add one `min-width` media query that changes the layout in a meaningful way. Verify your heading color passes WCAG AA contrast using DevTools or WebAIM.

## Bridge

Assignment 1 asks you to rebuild a provided design comp as a responsive, semantic HTML/CSS page — you will apply everything from this week's notes directly. Pay particular attention to the landmark structure and the mobile-first breakpoint; both are explicitly checked in the rubric. The Chapter 2 reading covers progressive enhancement in more depth, which gives the conceptual grounding behind the mobile-first rule. Read it before starting the assignment so the "why" is clear.
