# Week 10 Studio Notes: Preference Panel Studio and Proposal Workshop

## Session focus

Session 1 covered `localStorage`, `sessionStorage`, and keeping UI state in one place. Session 2 builds a preference panel that survives a reload, then workshops Project 2 proposals with particular attention to where the data comes from.

## Before class

- Decide which two or three preferences Lab 09 will persist. Fewer, done properly, beats a long list half-wired.
- Bring a Project 2 idea and a candidate data source.

## Studio plan

1. **First visit versus returning visit (10 min).** The same page in a fresh browser profile and in a returning one. Everything you store has to have a sensible default for the visit where it is absent.
2. **Lab 09 preference studio (25 min).** One state object, `JSON.stringify` on save, `JSON.parse` with a fallback on load. Skip the fallback once on purpose and watch what a corrupted value does to the page.
3. **Project 2 proposal workshop (25 min).** Pitch, then name the data: where it comes from, what shape it arrives in, and what the interface does when it is unavailable.
4. **Scope check and milestone logistics (15 min).** What Milestone 1 asks for and how it is graded. A scope you can finish is worth more than a scope you can describe.

The virtual section runs this plan live, Wednesday 9:30–10:45 AM (75 minutes). The online section works the same sequence self-paced; where the plan says "the room" or "a volunteer," use the Help & Questions discussion board.

## Accessibility connection

Persisting preferences like font size, contrast, and reduced motion settings has direct accessibility value. If a user increases the text size for readability, that setting should survive a page reload — forcing them to re-apply it every visit is a usability barrier. When restoring state on page load, apply it before the page renders visible content (or as early as possible) to avoid a visible "flash" from default to preferred settings.

## Practice prompt

Build a "reading preferences" panel with three controls:
- A `<select>` for font size (small, medium, large)
- A toggle for dark mode
- A toggle for hiding images

When any control changes, save the full preferences object to `localStorage` using `JSON.stringify`. On page load, read the saved preferences and apply them immediately. Write a `render(prefs)` function that takes the preferences object and applies all three settings to the page — do not reach into the DOM from individual event handlers.

## Bridge

Lab 09 builds a full preference panel using exactly this pattern — you will save and restore a preferences object across reloads. Project 2 Proposal is also due this week; the project will use both the Fetch API from Week 09 and storage from this week, so your proposal should describe what data you will fetch and what preferences or state you will persist. Quiz 6 will ask you to trace a JSON round-trip and identify what type `getItem` returns.
