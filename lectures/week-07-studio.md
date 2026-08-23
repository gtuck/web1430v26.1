# Week 07 Studio Notes: Accessible Validation Studio and Build Check-Ins

## Session focus

Session 1 covered listeners, `preventDefault`, delegation, and the ARIA attributes that make validation perceivable. Session 2 builds an accessible validated form in the Lab 07 studio and gives quick live feedback on Project 1 builds in progress.

## Before class

- Have your Lab 07 form markup written. Markup first means the studio time goes to behavior.
- Push your current Project 1 build and bring the deployed URL.

## Studio plan

1. **Delegation versus per-element listeners (10 min).** The same list wired both ways. Add an item at runtime and watch which version keeps working.
2. **Lab 07 validation studio (25 min).** Constraint attributes first, custom messages second, then `aria-invalid` and `aria-describedby` wired to a real error element, and one `aria-live` region for the summary.
3. **Keyboard and screen-reader pass (15 min).** Tab through the form. Confirm the error is announced, not just displayed, and that focus lands somewhere the user can act on.
4. **Project 1 build check-ins (25 min).** Short live reviews of in-progress builds. Bring a URL, not a description — five minutes on a running page beats twenty on a summary.

The virtual section runs this plan live, Wednesday 9:30–10:45 AM (75 minutes). The online section works the same sequence self-paced; where the plan says "the room" or "a volunteer," use the Help & Questions discussion board.

## Accessibility connection

Event-driven validation is one of the highest-impact areas for accessibility in front-end development. WCAG Success Criterion 3.3.1 requires that input errors be identified and described to the user in text — `aria-live` regions and `aria-describedby` are the technical implementation of that requirement. Focus management after form submission or error display is required by 2.4.3 (Focus Order) so that keyboard users are not stranded at a submit button after errors appear. Getting these right in Week 07 means your Project 1 form will meet real accessibility standards, not just pass visual inspection.

## Practice prompt

Build a contact form with Name, Email, and Message fields. Requirements: (1) validate each field on `blur` and show a specific error message next to the field using `aria-describedby` and `aria-live="polite"`, (2) prevent submission if any field is invalid, (3) use event delegation on a button group (three preset subject buttons: "Question", "Feedback", "Bug Report") so only one listener handles all three, storing the selection in a `dataset` attribute, and (4) on successful submission, display a `<div role="alert">` confirmation message and move focus to it.

## Bridge

Lab 07 is Accessible Form Validation — it is a direct application of everything in this week's notes, so the `showError`/`clearError` pattern from the Session 1 demo is a strong starting point. Quiz 4 will ask you to trace through event delegation code and predict which element `event.target` refers to in different click scenarios. Project 1 Build begins this week: if your project includes any form or interactive UI, the patterns here — `addEventListener`, `event.preventDefault`, and live ARIA regions — are the core tools you will reach for throughout the build.
