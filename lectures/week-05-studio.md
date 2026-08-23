# Week 05 Studio Notes: Data Explorer Studio and Proposal Workshop

## Session focus

Session 1 was about data shape. Session 2 turns shapes into working code in the Lab 05 studio, then applies the same skill to your own Project 1 idea — a proposal that names its data is a proposal you can actually build.

## Before class

- Draft the `products` array for Lab 05 before the session. Six objects is enough.
- Bring one Project 1 idea you can state in a single sentence.

## Studio plan

1. **Reading chained methods (10 min).** Read `products.filter(...).map(...)` chains aloud and predict each intermediate array. Quiz 3 asks you to do exactly this on paper.
2. **Lab 05 data-explorer studio (25 min).** Build the data layer first and log it. Only once the array transformations are right do you touch the display code — that separation is the whole lesson of the week.
3. **Project 1 proposal workshop (25 min).** Pitch your idea in one sentence, then sketch its data as an array of objects. The room stress-tests scope: too big usually shows up as too many properties.
4. **Milestone and survey logistics (15 min).** What Milestone 1 asks for, how it is graded, and the Mid-Course Check-In Survey. Complete the survey after the session while the week is fresh.

The virtual section runs this plan live, Wednesday 9:30–10:45 AM (75 minutes). The online section works the same sequence self-paced; where the plan says "the room" or "a volunteer," use the Help & Questions discussion board.

## Accessibility connection

Structuring data as arrays of objects — rather than scraping values directly out of the DOM — keeps your accessible markup clean and authoritative. When you build the DOM from a data array, every element is created deliberately: you can ensure that `alt` text, `aria-label` values, and semantic roles are set from the data rather than inferred or forgotten. It also makes it straightforward to regenerate or update the page without inadvertently stripping ARIA attributes that were added by hand.

## Practice prompt

Create a `students` array with at least five objects. Each object should have `name`, `grade` (a number 0–100), and `enrolled` (boolean) properties. Then write three things: (1) use `.filter()` to get only enrolled students, (2) use `.map()` to produce an array of strings in the format `"Alice: B"` using a helper function that converts the grade number to a letter, and (3) use `.find()` to locate a student by name. Log all three results to the console.

## Bridge

The data structures you build this week are exactly what Lab 05's Product Data Explorer will render to the page. For Quiz 3, you should be able to trace through a chain like `products.filter(...).map(...)` and predict its output. Your Project 1 Proposal should include a rough data sketch — an array of objects showing what properties your project's main data will have. That sketch will save you significant time when you start building in Week 06.
