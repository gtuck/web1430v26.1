# Week 09 Studio Notes: API Viewer Studio and Response-Shape Clinic

## Session focus

Session 1 covered promises, `async`/`await`, and the four states every network request puts an interface through. Session 2 builds against a real API in the Lab 08 studio and runs a clinic on what actually goes wrong: the response is not shaped the way you assumed it would be.

## Before class

- Pick the API you plan to use for Assignment 4 and fetch one response in the browser address bar.
- Skim that JSON. You do not need to understand all of it — you need to know how deep the data you want is buried.

## Studio plan

1. **Four states, drawn (10 min).** Loading, error, empty, success. Sketch what your interface shows in each one before writing the fetch. Code that starts from four states rarely forgets one.
2. **Lab 08 viewer studio (25 min).** `await fetch`, check `response.ok`, `try`/`catch`/`finally`, then render. In that order — the check before the render is what turns a blank page into a message.
3. **Response-shape clinic (25 min).** Bring a response you cannot get at. We log it, walk the nesting together, and find the path. Most "the API is broken" bugs are one array index deep.
4. **Assignment 4 viability check (15 min).** Run the check live: does it return JSON, does it work without a key or with one you can safely use, and does it carry enough data to tell a story?

The virtual section runs this plan live, Wednesday 9:30–10:45 AM (75 minutes). The online section works the same sequence self-paced; where the plan says "the room" or "a volunteer," use the Help & Questions discussion board.

## Accessibility connection

Asynchronous content updates are one of the most common accessibility failures in modern web apps. When a fetch completes and new content appears, sighted users see it instantly — but screen reader users receive no notification unless you explicitly mark regions with `aria-live`. Error messages are equally important: an error that appears visually but is never announced leaves keyboard-only and screen reader users unable to understand why their action failed.

## Practice prompt

Using the [Dog CEO API](https://dog.ceo/api/breeds/image/random) or the [JSONPlaceholder API](https://jsonplaceholder.typicode.com/posts), build a small page with:
- A button that triggers a `fetch()` call
- A loading state displayed while the request is in flight
- The result rendered to the DOM on success
- An error message rendered to the DOM on failure (test it by mistyping the URL)
- An `aria-live` region that announces status changes

## Bridge

Lab 08 has you build a full API-powered viewer using this week's patterns — you will need the four-state UI model and the `aria-live` region. Quiz 5 will test whether you can read async code and trace its execution order, and whether you know what happens when `response.ok` is false. Assignment 4 extends the lab into a more complete feature; the cleaner you keep your state-management functions, the easier that extension will be.
