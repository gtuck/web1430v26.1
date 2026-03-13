# Week 01 Lecture Notes: How the Browser Parses, Paints, and Executes

## Weekly focus
Understanding the browser as a runtime environment, not just a display window.

## Why this matters
Most beginners think of the browser as something that "shows" a web page. In reality it is a complex program that fetches resources over a network, builds in-memory data structures, and runs JavaScript — all before anything appears on screen. Knowing this model helps you make intentional decisions: where to place scripts, why a layout shift happens, and how to measure what is actually slow. DevTools stops being a mystery and becomes your primary debugging instrument starting this week.

## Learning targets
- Describe the HTTP request/response cycle: what the browser sends, what the server returns, and what status codes mean
- Explain how the browser converts HTML bytes into a DOM tree and CSS bytes into a CSSOM tree
- Define the render tree and describe why elements hidden with `display: none` are excluded from it
- Explain what "render-blocking" means and correctly place scripts using `defer` or `async`
- Use the DevTools Elements tab to inspect and live-edit the DOM and computed styles
- Use the DevTools Network tab to identify resource sizes, load order, and HTTP status codes

## Core concepts

### The HTTP request/response cycle
When you type a URL and press Enter, the browser performs a DNS lookup to resolve the domain name to an IP address, then opens a TCP connection to the server and sends an HTTP request. The request looks roughly like this:

```
GET /index.html HTTP/1.1
Host: example.com
Accept: text/html
```

The server responds with a status code and a body:

```
HTTP/1.1 200 OK
Content-Type: text/html; charset=UTF-8

<!doctype html>
<html>...
```

Common status codes to know now: **200** (OK), **301/302** (redirect), **404** (not found), **500** (server error). You will see all of these in the Network tab this week.

### Parsing HTML into the DOM
The browser reads the HTML response as a byte stream and parses it top-to-bottom into nodes. Each HTML element becomes a node in the **Document Object Model (DOM)** — a tree structure in memory. The DOM is what JavaScript reads and modifies; it is not the HTML source file. If you write malformed HTML, the browser silently repairs it, so the DOM may differ from what you typed.

Key implication: when JavaScript runs and calls `document.querySelector('h1')`, it is querying the DOM tree, not the HTML text file.

### Parsing CSS into the CSSOM
In parallel with HTML parsing, when the browser encounters a `<link rel="stylesheet">` tag it fetches the CSS file and parses it into the **CSS Object Model (CSSOM)** — a separate tree of style rules. CSS parsing is render-blocking: the browser will not paint anything until it has a complete CSSOM, because any rule could affect any element.

### The render tree and painting
Once both the DOM and CSSOM are ready, the browser merges them into a **render tree** containing only the nodes that will actually be drawn. Nodes with `display: none` are excluded entirely. Nodes with `visibility: hidden` remain in the render tree (they occupy space) but are not painted.

After the render tree is built, the browser performs **layout** (computing the size and position of each box) and then **paint** (filling in pixels). Changes to layout properties like `width`, `height`, or `margin` trigger a full re-layout — an expensive operation called **reflow**.

### Why script placement matters: defer and async
A `<script>` tag without attributes is render-blocking: the HTML parser stops, the script is fetched and executed, then parsing resumes. This is why scripts placed in `<head>` without `defer` or `async` can make a page appear blank for a noticeable time.

```html
<!-- Blocks parsing — avoid in <head> -->
<script src="app.js"></script>

<!-- Fetches in parallel, executes after HTML is fully parsed — preferred -->
<script src="app.js" defer></script>

<!-- Fetches in parallel, executes immediately when downloaded — use for independent scripts -->
<script src="analytics.js" async></script>
```

Use `defer` for any script that needs to access the DOM. Use `async` only for scripts that are completely independent (e.g., analytics). The safest fallback is placing a plain `<script>` tag just before `</body>`, but `defer` in `<head>` is the modern standard because the fetch starts earlier.

### DevTools: Elements tab
Open DevTools with `F12` or `Cmd+Option+I`. The **Elements** tab shows a live, editable view of the DOM — not the HTML source. You can:
- Click any element to highlight it in the viewport
- Double-click text to edit it in-place (changes are temporary, in-memory only)
- View **Computed** styles on the right panel to see which CSS rules are actually applied after inheritance and specificity resolution

The Elements tab is the fastest way to answer: "Why is this element positioned there?" and "Which CSS rule is overriding my style?"

### DevTools: Network tab
The **Network** tab records every resource the browser requests: HTML, CSS, JS, images, fonts. Reload the page with the tab open to see the waterfall. Key things to notice:
- The order resources are requested
- Which resources block rendering (shown with a long initial bar)
- File sizes and whether responses are served from cache (status 304)
- Response headers, including `Content-Type` and caching directives

Filter by type (JS, CSS, Img) to reduce noise. Click any row to see the full request and response headers.

### DevTools: Console tab
The **Console** is a live JavaScript REPL. You can type any JavaScript expression and see the result immediately:

```javascript
document.title                   // returns the page title
document.querySelectorAll('p').length  // counts paragraph elements
```

Errors from your scripts appear here in red with a file name and line number. This is your first stop when something does not work.

## Common mistakes
1. **Thinking DevTools shows the HTML file.** The Elements tab shows the live DOM. If the browser repaired malformed HTML, or if JavaScript modified the page, the Elements view will differ from the source. Use `View Page Source` (`Ctrl+U`) to see the actual HTML that was delivered.
2. **Placing scripts in `<head>` without `defer`.** This blocks rendering. Students often wonder why their page is slow to appear — the Network tab will show the script request completing before any painting occurs.
3. **Confusing `async` and `defer`.** Using `async` on a script that manipulates the DOM can cause "cannot read properties of null" errors because the DOM may not be ready when the script executes.
4. **Ignoring the Console.** Many students open DevTools to inspect elements but never look at the Console. Any JavaScript error — including errors from browser extensions — appears there. Clear it before debugging your own code.
5. **Conflating HTTP status 200 with "the page works."** A 200 response means the server returned something — but it could be an error page served as HTML. Always read the response body in the Network tab, not just the status code.

## Accessibility connection
The DOM tree that the browser builds from your HTML is the same structure that screen readers traverse to announce page content to users who cannot see the screen. If your HTML is not semantic — for example, if you build a navigation list out of `<div>` tags instead of `<nav>` and `<ul>` — the DOM still exists but carries no meaning for assistive technologies. Understanding the DOM as a tree (not just a visual layout) is the foundation for writing accessible markup starting next week.

## Demo walkthrough
**Goal:** Use DevTools to watch a page load and trace exactly what happens.

1. Open a browser and navigate to `https://example.com` (a simple, fast page).
2. Open DevTools (`F12`) and click the **Network** tab. Check "Disable cache" in the toolbar.
3. Reload the page. Watch the waterfall appear. Identify the initial HTML document request (status 200) and any subsequent CSS or image requests.
4. Click the HTML row. Show the **Headers** tab: point out the `GET` request and the `200 OK` response. Show the **Response** tab to see the raw HTML.
5. Switch to the **Elements** tab. Expand the DOM tree. Click the `<h1>` element — the viewport highlights it.
6. In the right panel, switch to **Computed** and scroll to `display`. Show that it reads `block`.
7. Double-click the text inside `<h1>` in the Elements panel and change it. Show that the page updates but refreshing reverts it ("this is DOM editing, not file editing").
8. Open a new tab, navigate to any page with a `<script>` tag in `<head>`. View page source (`Ctrl+U`) and find the script tag. Return to DevTools, Network tab, and show the script request in the waterfall — point out if it appears before CSS finishes loading.

## Practice prompt
Pick any public website you visit regularly. Open DevTools and go to the Network tab. Reload the page. Answer these questions in writing (a text file or Canvas journal entry):
- How many total requests were made?
- What was the size of the initial HTML document?
- Did any requests return a non-200 status code? If so, what were they?
- Can you find a `<script>` tag in the Elements panel? Does it have `defer` or `async`?

## Bridge
Lab 01 – Inspecting the Web asks you to use the Network and Elements tabs to document the load behavior of an assigned page — exactly the skills practiced in the demo and practice prompt above. Quiz 1 covers the request/response cycle, render-blocking, and the difference between `defer` and `async`; re-read the script placement section before taking it. Bring any DevTools questions to the Help board before the Sunday deadline.
