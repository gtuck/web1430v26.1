# Chapter 14: Performance, Testing, and Deployment

Getting code to work on your laptop is only half the job. This chapter covers how to verify that your application is actually ready for real users — and how to put it in front of them.

## What this chapter is really about

Everything in the course has been building toward a moment: you push a button, your application is live on the internet, and a real person uses it. That moment requires three things to go right. First, the application must be fast enough that users do not leave before the page loads. Second, it must work correctly — keyboard navigation, screen readers, every interaction path — not just in your best-case scenario. Third, the deployed version must actually match what you built.

This chapter treats Lighthouse as your scorecard, manual testing as your quality gate, and Netlify or Vercel as your publishing platform. These are not exotic tools for specialists. They are the practical minimum for shipping something you can stand behind.

## Key ideas

**The Lighthouse audit** is built into Chrome DevTools (DevTools → Lighthouse tab, or use the Lighthouse panel in Edge). Run it on any page — local dev server, preview deploy, or live URL — and it returns scores in five categories:

| Category | What it measures |
|---|---|
| **Performance** | How fast the page loads and becomes interactive |
| **Accessibility** | Automated checks against WCAG guidelines |
| **Best Practices** | Security, modern APIs, and common code quality signals |
| **SEO** | Whether search engines can crawl and understand the page |
| **PWA** | Progressive Web App compliance (offline support, installability) |

For this course, Performance and Accessibility are the categories you act on most. Best Practices catches things like using deprecated APIs or loading scripts over HTTP instead of HTTPS. SEO and PWA are informational at this stage.

**Lighthouse performance metrics** — the Performance score is computed from several sub-metrics. The four you will see most:

| Metric | What it measures | Target |
|---|---|---|
| **FCP** (First Contentful Paint) | When the browser first renders any text or image | Under 1.8 s |
| **LCP** (Largest Contentful Paint) | When the largest visible element finishes rendering | Under 2.5 s |
| **TBT** (Total Blocking Time) | How long the main thread is blocked, delaying interactivity | Under 200 ms |
| **CLS** (Cumulative Layout Shift) | How much visible content shifts unexpectedly during load | Under 0.1 |

A high CLS score usually means images without explicit dimensions (the page jumps when images load) or content injected above existing content. A high TBT score usually means large or long-running JavaScript.

**How to read a Lighthouse report**: the scores (0–100) are useful as a compass, not a grade. A Performance score of 55 does not mean you failed; it means something specific is slow and the report will tell you what. Every flagged item shows a description, an estimated savings, and a link to documentation. Work the list top-to-bottom — the items with the largest estimated savings first.

**Tree-shaking** removes code that you import but never actually call. Vite does this automatically when you run `npm run build`. The mechanism works because ES module imports are static — the bundler can analyze exactly which exports are used and drop the rest.

```js
// utils.js — exports three functions
export function formatPrice(n) { /* ... */ }
export function formatDate(d) { /* ... */ }
export function slugify(s) { /* ... */ }

// main.js — only uses one
import { formatPrice } from './utils.js';
```

When you build, `formatDate` and `slugify` are not included in the output because nothing imports them. If you had used `import * as utils from './utils.js'`, tree-shaking would be defeated — Vite cannot know which properties of `utils` you will read at runtime.

**Code splitting** breaks your bundle into separate files that load on demand instead of all at once. Vite handles this automatically for dynamic imports:

```js
// Static import — always bundled into the main chunk
import { renderProductList } from './render.js';

// Dynamic import — loaded only when this code runs
async function loadAdminPanel() {
  const { AdminPanel } = await import('./admin.js');
  AdminPanel.init();
}
```

Dynamic imports are useful for large features that only a subset of users ever access — an admin panel, a data export tool, a complex chart library. Do not over-apply them; splitting too aggressively creates more network round-trips than it saves.

**Verifying tree-shaking and code splitting**: after running `npm run build`, inspect the `dist/` folder:

```
dist/
  index.html
  assets/
    index-BsX2k3lm.js       ← main bundle (hashed filename for cache-busting)
    index-DqW8pLzY.css
    admin-Tn9cRmKj.js        ← split chunk, only loaded when needed
```

The hashed filenames are intentional — browsers cache files by URL, and the hash changes whenever the file contents change. This means users automatically get the updated file without you having to manage cache headers.

**Image optimization** — images are typically the heaviest assets on a page. Three practices make the biggest difference:

Use modern formats. WebP and AVIF are significantly smaller than JPEG and PNG at equivalent quality. Most image editors and free tools (Squoosh, ImageMagick) convert to these formats. AVIF is slightly smaller than WebP but has slightly less browser support; WebP is safe for all modern browsers.

```html
<!-- Single WebP image -->
<img src="hero.webp" alt="A person working at a desk" width="800" height="450">

<!-- srcset: serve the right size for the device -->
<img
  src="hero-800.webp"
  srcset="hero-400.webp 400w, hero-800.webp 800w, hero-1200.webp 1200w"
  sizes="(max-width: 600px) 400px, (max-width: 1000px) 800px, 1200px"
  alt="A person working at a desk"
  width="800"
  height="450"
>
```

Always include explicit `width` and `height` attributes. Without them, the browser does not know how much space to reserve before the image loads, causing layout shifts that raise your CLS score.

Use `loading="lazy"` on images that are below the fold — below the visible viewport on initial load. The browser will not download them until the user scrolls near them, reducing the data needed to render the initial view.

```html
<!-- Hero image: load immediately (above the fold) -->
<img src="hero.webp" alt="..." width="1200" height="600">

<!-- Product images further down the page: lazy-load -->
<img src="product-1.webp" alt="..." width="400" height="400" loading="lazy">
```

Do not put `loading="lazy"` on images that appear above the fold. The browser would delay loading the most important image, which is the opposite of what you want.

**The `npm run build` → `npm run preview` workflow** — always run both commands before deploying:

```bash
npm run build     # produces the dist/ folder
npm run preview   # serves dist/ locally on a different port
```

`npm run dev` serves your source files from `src/` with Vite's development transforms. `npm run preview` serves the actual compiled output from `dist/`. These are not always identical. Issues that only appear in the built version — broken import paths, missing environment variables, tree-shaking that removes something you needed — will surface in preview and not in dev. Make the preview your final check.

**Deployment to Netlify or Vercel** follows the same three-step pattern on both platforms:

1. **Connect your repository.** Sign in with your GitHub account and select your repo. The platform watches for new commits and redeploys automatically.

2. **Set the build command.** For a Vite project, this is `npm run build`. The platform runs this command in their environment after cloning your repo.

3. **Set the publish directory.** For Vite, this is `dist`. This tells the platform which folder contains the files to serve.

On Netlify, these settings live in Site Configuration → Build & Deploy → Build settings. On Vercel they are auto-detected from your `package.json` in most cases, but you can override them in the project settings.

**Environment variables for API keys** — never commit secret keys to git. Both platforms have a UI for setting environment variables that are injected at build time:

In Vite, environment variables that start with `VITE_` are exposed to your client-side code:

```js
// In your source code — references the env variable
const apiKey = import.meta.env.VITE_WEATHER_API_KEY;
```

In the Netlify or Vercel UI, add a variable named `VITE_WEATHER_API_KEY` with the actual key value. It is available during `npm run build` but never stored in your source code.

A `.env.local` file (always in `.gitignore`) holds the variable for local development:

```
# .env.local — never commit this file
VITE_WEATHER_API_KEY=your_actual_key_here
```

```
# .gitignore — add this line if it is not already there
.env.local
```

**Preview deploys** — both Netlify and Vercel create a unique URL for every pull request or branch push. This lets you share a live, shareable link for review before merging to main. The pattern is: create a branch, push it, share the preview URL, review and approve, merge. The main branch URL then updates automatically.

**The 3-check method** — before submitting any lab, assignment, or project, run these three checks in order:

1. **Keyboard-only walkthrough**: unplug (or ignore) your mouse and navigate the entire application using only Tab, Shift+Tab, Enter, Space, and arrow keys. Every interactive element must be reachable and operable. If you get stuck, something is wrong.

2. **Network throttle test**: in DevTools → Network tab, set the throttle to "Fast 3G" (or "Slow 3G" for a harder test). Reload the page. Does the layout shift? Does anything look broken or incomplete before all assets load? This simulates a user on a mobile connection.

3. **Lighthouse run**: run Lighthouse on the deployed or previewed version (not the dev server). Aim for Performance ≥ 90, Accessibility ≥ 90. Read every flagged item, fix the ones you can, and be able to explain the ones you leave.

Run checks 1 and 2 during development. Run check 3 on the built version. Do not run Lighthouse on the dev server — the dev server is intentionally unoptimized and will produce misleadingly low Performance scores.

**A complete pre-submission checklist**:

```
Before submitting:
[ ] npm run build completes without errors or warnings
[ ] npm run preview shows the app working correctly
[ ] Keyboard-only walkthrough: all interactions reachable and operable
[ ] DevTools Network throttle (Fast 3G): no broken layout or unreadable state
[ ] Lighthouse on preview or deployed URL: Performance ≥ 90, Accessibility ≥ 90
[ ] No API keys or secrets in source code (use import.meta.env.VITE_*)
[ ] .env.local is in .gitignore
[ ] dist/ is in .gitignore
```

## Mental model

Think of the journey from source code to a user's screen as a pipeline with three stages: build, verify, deploy.

The **build** stage (Vite) takes your human-readable source files — modular, named, commented — and produces a compact, optimized package. Tree-shaking strips unused code. Minification shortens identifiers and removes whitespace. Code splitting creates separate chunks for separate routes or features. The output is not meant to be read; it is meant to be loaded fast.

The **verify** stage (manual testing + Lighthouse) answers the question: does the built output actually work, and does it work for everyone? The dev server is your workshop; `npm run preview` is your dress rehearsal. You would not skip the dress rehearsal before a performance, and you should not skip `npm run preview` before deploying.

The **deploy** stage (Netlify/Vercel) moves the built output from your machine to a server with a public URL, a CDN, and HTTPS. The platform handles infrastructure; you handle the code.

A project that is shipped, accessible, and fast is more valuable than a project that is only finished on your machine.

## Working habits

- Run `npm run build && npm run preview` as a pair, not separately. If build fails, fix it before deploying.
- Run Lighthouse on the preview URL, not the dev server. Dev server scores are not meaningful for Performance.
- Address Lighthouse Accessibility findings before Performance ones — accessibility failures affect real users immediately; performance scores are a continuous improvement target.
- Set all API keys as environment variables before you write code that uses them. Committing a key by accident is a security incident that requires rotating the key, not just deleting the commit.
- Convert images to WebP before adding them to the project, not as an afterthought. Set `width` and `height` attributes at the same time you write the `<img>` tag.
- Keep `dist/` and `.env.local` in `.gitignore` from your first commit. Adding them later is harder than adding them first.
- After a successful Netlify or Vercel deployment, run the keyboard walkthrough and Lighthouse audit on the live URL, not just the preview. The production CDN occasionally introduces subtle differences.

## Common mistakes

- **Running Lighthouse on the dev server**: the dev server produces bundles with development tooling included, no minification, and no tree-shaking. Lighthouse scores on the dev server are not representative. Always audit the built version.
- **Forgetting `npm run preview` before deploying**: the app works on dev but breaks in production because an import path assumed source-file resolution, a feature was dev-only, or an environment variable was missing. Preview catches this.
- **Committing `.env.local`**: if you commit a secret key, rotating the key is mandatory even after you delete it from the repo — the key exists in git history. Use a pre-commit hook or simply check `git status` before every commit.
- **`loading="lazy"` on the hero image**: the browser delays loading the most prominent image on the page, causing a visible blank area during load and a poor LCP score. Only lazy-load images that are genuinely below the fold.
- **No `width` and `height` on images**: every image without explicit dimensions is a potential layout shift. Lighthouse flags these; more importantly, they make the page feel unstable while loading.
- **Using `import *`**: wildcard imports defeat tree-shaking. Import only the named exports you use.
- **One giant chunk**: if you import every module in `main.js` at the top level, everything lands in one bundle. Use dynamic imports for large features that are not needed immediately.
- **Ignoring the keyboard walkthrough**: many keyboard failures are invisible to mouse users. Tab through the entire app at least once before every submission.

## Practice prompt

1. Open a Vite project from a previous lab or assignment (or create a fresh one from a prior project's code).
2. Run `npm run build`. Open the `dist/assets/` folder and note the filenames and file sizes. Then run `npm run preview` and verify the application works.
3. Run a Lighthouse audit on the preview URL (the `localhost:4173` address). Record your scores for Performance, Accessibility, and Best Practices.
4. Find one Lighthouse Performance finding and one Accessibility finding. Read the description for each. Implement the recommended fix for each finding and re-run Lighthouse. Did your scores improve?
5. Add one image to the project (any image). Set explicit `width` and `height` attributes. Convert it to WebP if it is not already in that format. Add `loading="lazy"` if it appears below the fold. Re-run Lighthouse and note the CLS score.
6. If you have an API key used in one of your projects, move it to `.env.local` using a `VITE_` prefix and reference it with `import.meta.env.VITE_YOUR_KEY_NAME`. Verify the application still works, then add `.env.local` to `.gitignore`.
7. Create a free Netlify or Vercel account, connect your repository, set the build command to `npm run build` and publish directory to `dist`, and deploy. Share the live URL and run a final Lighthouse audit on it.

## Reflection

What was different about the application when you ran `npm run preview` compared to `npm run dev`? Which Lighthouse findings surprised you — were there accessibility issues you would not have found by looking at the page visually? When you did the keyboard-only walkthrough, what did you discover about the interaction model that you had not noticed before?

## Vocabulary

- **Lighthouse** — a Chrome DevTools auditing tool that scores a page on Performance, Accessibility, Best Practices, SEO, and PWA criteria
- **FCP (First Contentful Paint)** — the time when the browser first renders any text or image to the screen
- **LCP (Largest Contentful Paint)** — the time when the largest visible element in the viewport finishes rendering; the primary user-perceived load speed metric
- **TBT (Total Blocking Time)** — the total time during page load when the main thread is blocked and cannot respond to user input
- **CLS (Cumulative Layout Shift)** — a measure of how much visible content moves unexpectedly during load; caused by images without dimensions or late-loading content
- **tree-shaking** — the process of removing exported code that is never imported or called anywhere in the application
- **code splitting** — dividing a JavaScript bundle into separate chunks that load on demand rather than all at once
- **dynamic import** — a syntax (`await import('./module.js')`) that loads a module at runtime instead of at bundle time, enabling code splitting
- **WebP** — a modern image format that is significantly smaller than JPEG or PNG at comparable quality, supported by all modern browsers
- **AVIF** — a newer image format with even better compression than WebP, with slightly less browser support
- **srcset** — an HTML attribute that specifies multiple image sources at different resolutions, letting the browser pick the most appropriate one for the device
- **loading="lazy"** — an HTML attribute that defers image loading until the image is near the viewport
- **`npm run preview`** — a Vite command that serves the compiled `dist/` folder locally, simulating the deployed version
- **environment variable** — a value set outside the source code (in the platform UI or a `.env.local` file) and injected at build time; used to keep secrets out of git
- **`import.meta.env`** — Vite's mechanism for accessing environment variables in client-side code; only variables prefixed with `VITE_` are exposed
- **preview deploy** — a unique, shareable URL generated automatically for every pull request or branch push on Netlify or Vercel
- **CDN (Content Delivery Network)** — a network of servers distributed geographically that serves static assets from the location closest to the user
- **cache-busting** — the practice of including a content hash in asset filenames so browsers automatically fetch new versions when files change

## Mini checklist

- I can run a Lighthouse audit on a built application and identify the highest-impact Performance and Accessibility findings.
- I can explain what FCP, LCP, TBT, and CLS measure and what causes each metric to be poor.
- I can explain what tree-shaking does and why using `import *` defeats it.
- I can use a dynamic import to split a large feature into a separate chunk.
- I can inspect the `dist/` folder after `npm run build` and identify the bundled output files.
- I can run `npm run preview` and explain why it is more representative than `npm run dev` for pre-deployment testing.
- I can add explicit `width`, `height`, and `loading="lazy"` attributes to images appropriately.
- I can convert or specify images in WebP format and use `srcset` for responsive images.
- I can move an API key to `.env.local` and reference it with `import.meta.env.VITE_*`.
- I can deploy a Vite project to Netlify or Vercel by connecting a repo, setting the build command, and setting the publish directory.
- I can perform the 3-check method (keyboard walkthrough, network throttle, Lighthouse audit) before submitting a project.
