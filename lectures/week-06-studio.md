# Week 06 Studio Notes: FAQ, Tabs, and Keyboard Testing Studio

## Session focus

Session 1 walked the DOM lifecycle: select, create, update, remove. Session 2 builds two composite widgets with it — an accessible FAQ and a tab set — which together are the core of the pattern library Assignment 3 asks for.

## Before class

- Read the Lab 06 brief.
- Re-read the roving tabindex section of the lecture notes. It is the part of this lab that is hard to invent on the spot.

## Studio plan

1. **Which method, and why (10 min).** A rapid sequence of small changes. For each one, call out `querySelector` versus `querySelectorAll`, `textContent` versus `innerHTML`, and `classList.toggle` versus rebuilding a class string by hand.
2. **FAQ disclosure studio (20 min).** Build the disclosure pattern with real `aria-expanded` state rather than a CSS class alone. The class controls the pixels; the attribute controls what a screen reader announces.
3. **Tabs and roving tabindex (25 min).** Implement `setActiveTab` and the arrow-key handler live, then test with the keyboard only. Mouse-only testing hides every bug this pattern has.
4. **Assignment 3 patterns (20 min).** Which of this week's patterns belongs in your library, and what a pattern entry has to document — markup, behavior, and keyboard contract — to be useful to someone else.

The virtual section runs this plan live, Wednesday 9:30–10:45 AM (75 minutes). The online section works the same sequence self-paced; where the plan says "the room" or "a volunteer," use the Help & Questions discussion board.

## Accessibility connection

`classList.toggle` is the right tool for show/hide patterns (accordions, modals, navigation menus), but toggling a CSS class is invisible to screen readers unless you also update ARIA state. When you toggle `is-open` on a nav, pair it with `setAttribute("aria-expanded", true/false)` on the button that controls it. Similarly, when you use `createElement` to render dynamic content, apply semantic elements (`<article>`, `<ul>`, `<button>`) rather than generic `<div>` tags — screen readers use those semantics to describe the page structure to non-visual users.

## Practice prompt

Build a page with a `<ul id="task-list"></ul>` and an `<input>`/`<button>` for adding tasks. Write an `addTask(text)` function that creates a `<li>` with the task text and a "Done" button. When "Done" is clicked, toggle a `.completed` CSS class on the `<li>` (style it with strikethrough in your CSS). Add a `data-created` attribute to each `<li>` storing the timestamp of when it was added (`Date.now()`). Log the timestamp to the console when the "Done" button is clicked.

## Bridge

Lab 06 asks you to build an interactive FAQ and tabs interface — both require `classList.toggle` for show/hide and `querySelector` for finding the right panel to reveal, and the tabs need the roving-tabindex pattern from the Session 1 notes. Assignment 3 grades that arrow-key behaviour directly, so get it working in the lab first. Assignment 3 will have you render a data array into the DOM, which is exactly the `renderProducts` pattern from the Session 1 demo. As you work, keep rendering and data logic in separate functions — that separation will make Assignment 3 much easier to debug and extend.
