# Chapter 1: Thinking in the Browser

The browser is a runtime environment, not a display engine. Understanding what it does — and in what order — changes how you write every line of HTML, CSS, and JavaScript.

## What this chapter is really about

Most beginners treat the browser as a magic box: put code in, get a web page out. This chapter opens the box. You will learn how a URL becomes a rendered page, why the order of your code matters, and how to use developer tools to see exactly what the browser is doing at any moment. The goal is not just to write working pages but to understand why they work.

## Key ideas

### The request-response cycle

When you type a URL and press Enter, the browser sends an **HTTP GET request** to a server. The server responds with an HTML document and a status code. A `200 OK` status means success. A `404 Not Found` means the resource doesn't exist. A `301` or `302` means the resource has moved. You can watch every one of these transactions happen in DevTools → Network tab.

```
GET /index.html HTTP/1.1
Host: example.com

HTTP/1.1 200 OK
Content-Type: text/html
```

The response body is the raw HTML text — not a rendered page, just characters. The browser's job is to interpret those characters.

### Parsing HTML into the DOM

The browser reads the HTML document top to bottom, one token at a time, building the **DOM** (Document Object Model) — a live tree of objects representing every element on the page. Consider this small document:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="style.css">
    <title>My Page</title>
  </head>
  <body>
    <h1>Hello</h1>
    <p>Welcome.</p>
    <script src="app.js"></script>
  </body>
</html>
```

Here is what the browser does, in order:

1. Reads `<!DOCTYPE html>` — signals HTML5 parsing mode.
2. Reads `<html>` — creates the root DOM node.
3. Reads `<head>` — enters the head section.
4. Reads `<link rel="stylesheet" href="style.css">` — starts fetching `style.css` in parallel while HTML parsing continues. CSS is **render-blocking**: nothing is painted to the screen until the stylesheet is downloaded and parsed into the CSSOM.
5. Reads `<title>` — sets the page title.
6. Reads `<body>` — begins the body.
7. Reads `<h1>Hello</h1>` and `<p>Welcome.</p>` — creates those DOM nodes.
8. Reads `<script src="app.js">` — **pauses HTML parsing**, fetches `app.js`, executes it completely, then resumes.

The order matters. JavaScript that runs at step 8 can access `<h1>` and `<p>` because they were added to the DOM at step 7. JavaScript in `<head>` (without `defer`) runs before the body exists, so it cannot find any body elements.

### The CSSOM and the render tree

While HTML is parsed into the DOM, CSS is parsed into the **CSSOM** (CSS Object Model). The browser must have both trees before it can display anything. Once both are ready, it combines them into a **render tree** — a version of the DOM that only includes elements that will actually be painted to the screen. Elements with `display: none` are excluded from the render tree entirely (unlike `visibility: hidden`, which keeps the space but makes the element invisible).

The render tree drives **layout** (calculating exact positions and sizes) and **paint** (drawing pixels). Anything that changes the render tree — adding a class, changing a style, removing an element — triggers a recalculation. Understanding this helps you avoid expensive operations inside animation loops or event handlers that fire hundreds of times per second.

### Why script placement matters: `defer` and `async`

A `<script>` tag in `<head>` without attributes blocks HTML parsing. The browser stops building the DOM, fetches the script, runs it, then continues. This delays the first visible content on screen and makes the page feel slow.

The solution is to control when scripts execute:

```html
<!-- Blocks parsing — avoid this -->
<head>
  <script src="app.js"></script>
</head>

<!-- Recommended: defer -->
<head>
  <script src="app.js" defer></script>
</head>

<!-- Use for independent scripts only: async -->
<head>
  <script src="analytics.js" async></script>
</head>
```

**`defer`** — The script is fetched in parallel while HTML continues parsing. Execution is delayed until the HTML is fully parsed. Multiple deferred scripts execute in the order they appear. Use `defer` for most application scripts.

**`async`** — The script is fetched in parallel and executed as soon as it downloads, potentially interrupting HTML parsing. Execution order is not guaranteed. Use `async` only for scripts that have no dependencies (analytics, third-party widgets).

**Bottom of `<body>`** — An older technique that works but is less explicit than `defer`. Placing scripts just before `</body>` ensures the DOM exists when the script runs. `defer` is preferred because it starts fetching earlier.

For this course, always use `defer` or place scripts at the bottom of `<body>`.

### The layered model

Good client-side code respects three distinct layers:

| Layer | Technology | Purpose |
|-------|-----------|---------|
| Content | HTML | Structure and meaning |
| Presentation | CSS | Visual form and layout |
| Behavior | JavaScript | Interactivity and dynamic updates |

Collapsing these layers — writing CSS in JavaScript, or putting behavior in HTML `onclick` attributes — creates code that is harder to debug, maintain, and make accessible. Throughout this course, you will practice keeping these layers separate.

## Mental model

Think of the browser as a document interpreter that also runs programs. HTML is not displayed — it is *parsed* into a tree. CSS is not read top to bottom — it is *calculated* by specificity and cascade rules. JavaScript does not run instantly — it waits for the parser to reach it, or for events to fire.

When something goes wrong, ask: which layer is responsible? Is this a structure problem (HTML), a presentation problem (CSS), or a behavior problem (JavaScript)?

## Working habits

Open DevTools before you write your first line of code for the day. Use the **Elements** panel to inspect the live DOM tree — remember this shows the *current* state of the DOM, which may differ from your HTML source if JavaScript has modified it. Use the **Console** to read errors and run quick experiments. Use the **Network** tab to watch requests fire and see response status codes. Treat DevTools as your primary working environment, not an afterthought.

Read error messages completely. The browser's error messages are usually accurate and include a file name and line number. Skipping them is the single biggest time-waster a beginner can fall into.

## Common mistakes

- Treating `<div>` as a neutral container for everything. Divs have no meaning; most things on a page have a more appropriate element (`<nav>`, `<main>`, `<section>`, `<button>`, etc.).
- Placing `<script>` tags in `<head>` without `defer`, causing JavaScript to block HTML parsing and making the page slower to display.
- Confusing the Elements panel in DevTools with the HTML source file. Elements shows the *live DOM*, which may have been modified by JavaScript. View Source (Ctrl+U) shows the original file.
- Using `document.write()` — it destroys the DOM and is never appropriate in modern code.
- Closing DevTools because it "gets in the way." Keep it open while you work.
- Ignoring the red errors in the Console.

## Accessibility and UX note

The DOM is not just a rendering mechanism — it is how assistive technologies navigate the page. Screen readers traverse the DOM tree, announcing headings, landmarks, and interactive elements. If your HTML structure is meaningful, a screen reader user can navigate your page efficiently. If it is a sea of unnamed `<div>` elements, they cannot.

This also means that JavaScript-modified DOM is immediately visible to assistive technologies. When you add an element to the DOM dynamically, a screen reader can encounter it. When you remove one, it disappears. The way you structure and modify HTML is the single most impactful accessibility decision you make throughout this course.

## Practice prompt

Open browser DevTools (F12 or Cmd+Option+I) on any live website you use regularly.

**Part 1 — DOM inspection:**
1. In the **Elements** panel, find three semantic HTML elements (not `<div>` or `<span>`). Name them and explain what each one communicates to the browser and to assistive technologies.
2. Right-click any element and choose "Edit as HTML." Change some visible text. What happens on screen? What does this tell you about the relationship between the source file and the live DOM?

**Part 2 — Network tab:**
1. Open the **Network** tab and reload the page. Find the very first request (it should be the HTML document). What is the status code? What type of file was returned?
2. Find the CSS file(s) in the list. Notice the "Initiator" column — what initiated these requests?
3. Look for any failed requests (shown in red). What status codes do you see?

**Part 3 — Script analysis:**
1. In the **Elements** panel, find the `<script>` tags on the page. Do any have `defer` or `async` attributes? Are any in the `<head>` without those attributes?
2. In the **Console**, type `document.querySelectorAll('script').length` and press Enter. How many scripts does the page use?

Write a short paragraph describing what the browser is doing to render this page, based on what you observed.

## Reflection

In what order does the browser process HTML, CSS, and JavaScript? What would happen to a page if the CSS file failed to load? If the JavaScript file failed to load? What does that tell you about progressive enhancement — the principle that a page should work at a basic level without CSS, and at a fully enhanced level with JavaScript?

## Vocabulary

- **DOM** — Document Object Model; a live tree of objects representing the page as the browser currently understands it
- **CSSOM** — CSS Object Model; the browser's parsed representation of all CSS rules
- **render tree** — the combined DOM + CSSOM used to calculate layout and paint; excludes hidden elements
- **HTTP request/response** — the protocol by which browsers ask for and receive web resources
- **parse** — to read and interpret a document, building an internal representation
- **render** — to calculate layout and paint the final visual result to the screen
- **runtime** — an environment that executes code (the browser is a JS runtime)
- **DevTools** — browser developer tools for inspecting and debugging pages
- **semantic** — HTML that describes the meaning of content, not just its appearance
- **defer** — a script attribute that delays execution until HTML parsing is complete
- **async** — a script attribute that fetches and executes the script independently of HTML parsing

## Mini checklist

- I can describe what happens between typing a URL and seeing a page, step by step.
- I can explain what `defer` does and why it is preferred over placing scripts in `<head>` without it.
- I can open DevTools and find an element in the DOM, an error in the Console, and a network request in the Network tab.
- I can name the three layers of client-side web development and explain what belongs in each.
- I can explain the difference between the live DOM (Elements panel) and the HTML source file (View Source).
- I can explain why semantic HTML matters for both sighted users and assistive technology users.
