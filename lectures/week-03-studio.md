# Week 03 Studio Notes: Console Studio and Type-Coercion Clinic

## Session focus

Session 1 covered variables, types, operators, and the debugging loop. Session 2 lives in the console — the fastest feedback loop you will have all semester — working the Lab 03 exercises and hunting the type conversions that trip up everyone at least once.

## Before class

- Attempt Lab 03 exercises 1–3.
- Note any result you could not explain. Those are the raw material for the clinic.

## Studio plan

1. **Predict-the-output warm-up (10 min).** Five expressions on screen. Commit to an answer before we run them. Coercion rules stick much better after you have been wrong about one.
2. **Type-coercion clinic (20 min).** Collect the results nobody could explain and work them as a group. `"5" + 3`, `"5" - 3`, `null == undefined`, and `NaN === NaN` between them explain most of the confusion.
3. **Lab 03 studio (30 min).** Work the exercises with support. Volunteers share a screen so the room can watch a real debugging pass rather than a finished answer.
4. **Quiz 2 readiness (15 min).** `const` versus `let`, `===` versus `==`, `NaN`, template literals, and how to read an error message down to the line number.

The virtual section runs this plan live, Wednesday 9:30–10:45 AM (75 minutes). The online section works the same sequence self-paced; where the plan says "the room" or "a volunteer," use the Help & Questions discussion board.

## Accessibility connection

JavaScript that runs in the browser can add, remove, or modify DOM content dynamically. When your scripts change content without updating the accessibility tree — for example, toggling a section visible without updating an associated `aria-expanded` attribute — screen reader users may not know the change occurred. This week's debugging skills apply directly: use the Console to verify that JavaScript is executing and that the DOM changes you intend are actually happening before worrying about accessibility attributes. Correct behavior is a prerequisite for accessible behavior.

## Practice prompt

Open the browser Console and work through these exercises, logging each result and writing down whether it matches your prediction before you run it:
1. `typeof null` — predict, then check
2. `'3' * '4'` — predict the type and value
3. `null == undefined` vs `null === undefined`
4. `` `${2 + 2} is ${2 + 2 === 4 ? 'correct' : 'wrong'}` ``
5. Declare `const colors = ['red', 'green']` then run `colors.push('blue')` — does `const` prevent this?

Document your predictions and the actual results. Note which ones surprised you and why.

## Bridge

Lab 03 – Console Exercises and Small Programs consists of small JavaScript problems solved entirely in the browser Console and in a `.js` file — the same environment used in today's demo. Quiz 2 will include questions on `typeof` output, the result of specific coercion expressions, and when to use `const` vs `let`; review the type table and the `==` vs `===` examples before taking it. The Chapter 3 reading goes deeper on expressions and operator precedence, which will fill in the gaps between what was covered here and what you encounter in the lab.
