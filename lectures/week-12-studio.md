# Week 12 Studio Notes: Card System Studio and Pitch Workshop

## Session focus

Session 1 built a first parent and child Vue pair. Session 2 builds the Lab 11 card system, checks in on Project 2 builds, and workshops Final Project pitches — you should leave with a real audience in mind and a draft data model.

## Before class

- Have the Lab 11 starter running with `npm run dev`.
- Write one sentence naming who your Final Project is for. Not "students" — a specific person with a specific problem.

## Studio plan

1. **Props flowing down (10 min).** One component, three different prop sets, rendered side by side. `defineProps` is the entire contract between parent and child; read it as documentation.
2. **Lab 11 card studio (25 min).** `v-for` a data array into card components, keyed correctly, with `computed()` doing the formatting rather than the template.
3. **Project 2 build check-ins (15 min).** Short reviews of running builds. Deployed or `localhost` is fine; screenshots are not.
4. **Final Project pitch workshop (25 min).** Pitch in one sentence: who it is for, what they can do with it, what data it needs. The room asks the questions the rubric will ask later, while there is still time to answer them.

The virtual section runs this plan live, Wednesday 9:30–10:45 AM (75 minutes). The online section works the same sequence self-paced; where the plan says "the room" or "a volunteer," use the Help & Questions discussion board.

## Accessibility connection

The `<style scoped>` feature does not affect the semantic structure of your HTML. A card component that uses a `<div>` for its container is still a `<div>` after scoping. Choose semantic elements — `<article>`, `<section>`, `<h2>` — inside each component, because the compiled output is what assistive technology reads. When using `v-for` to render images, the `:alt` binding must be dynamic so each image gets a meaningful, unique description rather than a repeated empty or placeholder value.

## Practice prompt

Create a `TagBadge.vue` component that accepts a `label` prop (String) and a `color` prop (String, default `'blue'`). In `App.vue`, declare an array of five tag objects and render them with `v-for`. Add a button that appends a new tag to the array and confirm that Vue re-renders the list without a page reload.

## Bridge

Lab 11 — Vue UI Card System asks you to build a card display driven by a data array, which is exactly the `v-for` + component pattern from today. Quiz 7 covers `ref()`, `computed()`, `v-for`, and `defineProps`. Project 2 Build begins this week; the card system you build in the lab is a direct starting point for the project's component layer.
