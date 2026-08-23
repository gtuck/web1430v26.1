# Week 12 Overview: Component Thinking with Vue

## This week
- Theme: Component Thinking with Vue
- Lecture: Props, State, Templates, and Simple Components
- Lab: Lab 11 – Vue UI Card System
- Deliverables: Quiz 7, Project 2 Build, Final Project Pitch and Planning Starter

## Live sessions
- **Monday 9:30–10:45 AM:** Props, state, templates, and simple components: building a first parent/child Vue pair live.
- **Wednesday 9:30–10:45 AM:** Lab 11 card-system studio, Project 2 build check-ins, and a Final Project pitch workshop — leave with a real audience and a draft data model.
- Sessions meet in the [class Zoom room](https://weber.zoom.us/j/82982068432); recordings are posted to Canvas.

## Success plan
1. Before Monday: skim the module overview and read the chapter
2. Attend Monday's live session for the week's core concepts and demo
3. Start the lab or studio activity; bring blockers to Wednesday's session
4. Attend Wednesday's live session for guided lab work, code review, and Q&A
5. Finish the weekly assessment or milestone, then commit and deploy your work

## Resources
- [Lecture notes: Props, State, Templates, and Simple Components](../lectures/week-12-lecture.md)
- [Chapter 12: Introductory Component-Based Development](../textbook/chapters/chapter-12-introductory-component-based-development.md)
- [Chapter 13: Accessibility Synthesis](../textbook/chapters/chapter-13-accessibility-synthesis.md) — **read the first half this week** (through the ARIA patterns and keyboard-contract sections). It is the longest chapter in the book and Week 13 is the heaviest week of the term; splitting it here keeps that week manageable.
- [Vue Transition Guide](../course/vue-transition-guide.md) — Use this if the switch from DOM code to components feels abrupt; it breaks the week into one working Vue pattern at a time.
- [Final Project brief](../projects/final-project-campus-or-community-tool.md) — Read the start-ahead plan and Milestone 1 section now; the goal is to leave Week 12 with a real audience, a starter sketch, and a draft data model so Week 13 is revision work instead of a cold start.
- **Time estimate:** 11–13 hours (reading, lab, quiz, Project 2 Build checkpoint, Final Project Pitch and Planning Starter)

## What students usually struggle with
- The biggest mistake this week is trying to build a full app before one parent component and one child component can already exchange data clearly.
- If multiple components need the same data, the data probably belongs in the parent. Let children receive props and emit events instead of silently changing shared state.
- If the final project is still only a vague idea by the weekend, Week 13 becomes much harder. Use the planning starter to leave behind one rough sketch and one draft normalized object before the week ends.

## Checkpoint question
Which piece of data belongs in the parent this week, and what should the child receive as a prop instead of owning itself?
