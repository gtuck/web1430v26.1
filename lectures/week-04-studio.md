# Week 04 Studio Notes: Decision-Tree Studio and Build Order

## Session focus

Session 1 introduced conditionals, loops, and functions. Session 2 puts them to work on the Lab 04 decision trees and then plans Assignment 2's build order — deciding what to write first is most of the difficulty in building a calculator.

## Before class

- Sketch your Lab 04 decision tree on paper before you write any code. The bugs are almost always in the tree, not the syntax.
- Skim the Assignment 2 brief so the build-order discussion lands on something concrete.

## Studio plan

1. **Refactor live (15 min).** Take a block of repeated code from a volunteer and extract it into a function together. Name it well, add a guard clause, and see how much shorter the caller gets.
2. **Decision-tree studio (25 min).** Compare paper sketches, then translate them into `if`/`else if` chains or a `switch`. Watch for the ordering bug where a broad condition shadows a narrower one below it.
3. **Assignment 2 build order (20 min).** Pure calculation functions first, user interface second. Write one function and test it in the console before you add a single event listener.
4. **Live code review (15 min).** Two volunteer solutions read aloud, with the room suggesting better names, missing guard clauses, and where duplication still remains.

The virtual section runs this plan live, Wednesday 9:30–10:45 AM (75 minutes). The online section works the same sequence self-paced; where the plan says "the room" or "a volunteer," use the Help & Questions discussion board.

## Accessibility connection

Well-named functions make code more maintainable, and maintainable code is more likely to stay accessible over time. When functions handle one thing — like `validateEmailInput()` rather than a 50-line anonymous blob — future developers can update validation logic without accidentally breaking the ARIA attributes or error messages attached to that form field. Descriptive function names also serve as inline documentation that helps teams with diverse experience levels contribute to accessibility improvements.

## Practice prompt

Write a function called `shippingCost(weightLbs, expedited)` that returns a shipping price. Rules: under 1 lb is $3.99, 1–5 lbs is $6.99, over 5 lbs is $12.99. If `expedited` is `true`, add $5.00 to any tier. Use guard clauses to return `null` if `weightLbs` is not a positive number. Test it with at least five calls in the console.

## Bridge

The logic patterns from this week — conditionals, loops, and functions with return values — are exactly what you need for Lab 04's form decision tree. Assignment 2 will ask you to build a multi-step calculator, so practice writing functions that accept parameters and return values rather than hardcoding answers. As you work through the lab, keep your functions short and pure so they are easy to test piece by piece.
