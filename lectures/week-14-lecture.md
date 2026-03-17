# Week 14 Lecture Notes: Quality Checks, Accessibility Audits, and Shipping to the Web

## Weekly focus
Running a Lighthouse audit, fixing the most common accessibility failures, and deploying a Vite project to GitHub Pages or Netlify.

## Why this matters
Shipping is not the last step — auditing before shipping is. A project with a Lighthouse accessibility score of 62 communicates to a reviewer that accessibility was not a priority. Knowing how to run a Lighthouse audit, interpret each category, and fix the most common failures in under an hour is a concrete, employable skill. Deployment is the step that turns a local project into something you can link on a resume.

## Learning targets
- Run a Lighthouse audit in Chrome DevTools and explain what each of the four score categories measures
- Identify and fix the five most common accessibility failures flagged by Lighthouse
- Manually verify keyboard navigation and check a page with a screen reader
- Build a Vite project with `npm run build` and understand what the `dist/` folder contains
- Deploy a project to GitHub Pages using the `gh-pages` branch approach or the `/docs` folder approach
- Deploy a project to Netlify using drag-and-drop or the Netlify CLI

## Core concepts

### What Lighthouse measures
Lighthouse is a built-in Chrome DevTools audit tool. Open it under the DevTools Lighthouse tab, select Desktop or Mobile, and click Analyze. It produces scores from 0–100 in four categories:

**Performance** — measures how fast the page loads and becomes interactive. Key metrics include Largest Contentful Paint (LCP, when the main content is visible), Total Blocking Time (TBT, how long the main thread is blocked by JavaScript), and Cumulative Layout Shift (CLS, whether elements jump around while loading). A Vite-built Vue app typically scores 90+ on performance by default because Vite tree-shakes unused code and minifies aggressively.

**Accessibility** — runs automated checks against WCAG guidelines. It checks for missing alt text, low color contrast, missing form labels, missing landmark regions, and more. This score is bounded: automated tools catch roughly 30–40% of real accessibility issues. A score of 100 does not mean the page is fully accessible.

**Best Practices** — checks for HTTPS, no deprecated APIs, correct image aspect ratios, and absence of browser console errors.

**SEO** — checks for a meta description, crawlable links, mobile viewport meta tag, and legible font sizes.

Run Lighthouse in an incognito window to avoid browser extensions skewing the results. Also run it on the production build (`dist/`), not the Vite dev server, for accurate performance numbers.

### Five common accessibility failures and how to fix them

**1. Images missing alt text.**
Every `<img>` must have an `alt` attribute. For informative images, write a meaningful description. For decorative images, use `alt=""` (empty string, not omitted). In Vue, bind it dynamically:

```vue
<img :src="product.imageUrl" :alt="product.name" />
```

Lighthouse flags both missing `alt` attributes and `alt="image"` placeholder text as failures.

**2. Low color contrast.**
Text must have a contrast ratio of at least 4.5:1 against its background for normal text (3:1 for large text, 18px+ bold or 24px+ regular). Lighthouse reports the failing ratio. Fix it by darkening the text color or lightening/darkening the background until the ratio passes. The WebAIM Contrast Checker at webaim.org/resources/contrastchecker/ lets you find a compliant value quickly.

**3. Form inputs without labels.**
Every `<input>`, `<select>`, and `<textarea>` needs a programmatic label. Use a `<label for="id">` paired with an `id` on the input, or wrap the input inside the label element. `placeholder` text is not a substitute — it disappears when the user types and is not reliably announced by screen readers.

```html
<label for="search">Search products</label>
<input id="search" type="text" v-model="query" />
```

**4. Missing landmark regions.**
Screen reader users navigate by jumping between landmark regions: `<header>`, `<nav>`, `<main>`, `<footer>`, `<aside>`. If your page uses only `<div>` containers, there are no landmarks to jump to. Wrap your primary content in `<main>`. Put your site navigation in `<nav>`. This is a structural fix in `App.vue` and takes less than two minutes.

**5. Interactive elements not reachable by keyboard.**
A button created with a `<div>` and a click handler is not focusable by default and has no keyboard activation. Use semantic HTML: `<button>`, `<a href>`, `<input>`. If you must use a custom element, add `tabindex="0"` and a `keydown` handler for Enter and Space. Test by pressing Tab to navigate your entire page without a mouse — every action must be reachable.

### Manual accessibility testing
Lighthouse is a starting point. Two manual checks you must do before calling a project complete:

**Keyboard navigation:** Press Tab to move forward through interactive elements, Shift+Tab to move backward. Every link, button, and input must be reachable and visually focused. Test that modal dialogs (if present) trap focus inside them and return focus to the trigger when closed.

**Screen reader:** On macOS, enable VoiceOver with Command+F5. On Windows, use NVDA (free download) or Narrator. Navigate to your page and listen. Does the page make sense when you cannot see it? Are images described? Do form errors get announced? You do not need to be a screen reader expert — even ten minutes of listening reveals major gaps.

### Building for production
The Vite dev server is not what you deploy. Run:

```bash
npm run build
```

This produces a `dist/` folder containing:
- `index.html` — the entry HTML with injected `<script>` and `<link>` tags
- `assets/` — hashed filenames for cache-busting (e.g., `index-BxYzK1a3.js`)

The `dist/` folder is self-contained. You can open `dist/index.html` directly in a browser (with some caveats around file:// paths) or serve it from any static file host.

### Deploying to GitHub Pages
GitHub Pages serves static files from a repository. Two approaches:

**Option 1 — `/docs` folder.** In `vite.config.js`, set `build.outDir: 'docs'`. Run `npm run build`. Commit the `docs/` folder. In the repository's Settings > Pages, set the source to the `main` branch, `/docs` folder.

**Option 2 — `gh-pages` branch.** Install the `gh-pages` package and add a deploy script:

```bash
npm install --save-dev gh-pages
```

In `package.json`:
```json
"scripts": {
  "deploy": "npm run build && gh-pages -d dist"
}
```

```bash
npm run deploy
```

This pushes the contents of `dist/` to a `gh-pages` branch. In Settings > Pages, set the source to the `gh-pages` branch. The site is live at `https://<username>.github.io/<repo-name>/`.

Important: if your Vite project is not at the root of a domain (e.g., it lives at `/repo-name/`), you must set `base` in `vite.config.js`:

```js
export default {
  base: '/repo-name/'
}
```

Without this, asset paths like `/assets/index.js` will 404.

### Deploying to Netlify
**Drag-and-drop:** Run `npm run build`, then drag the `dist/` folder onto the drop zone at app.netlify.com/drop. Netlify gives you a random URL immediately. You can rename it in site settings.

**Netlify CLI:**
```bash
npm install -g netlify-cli
netlify deploy --dir=dist --prod
```

Netlify automatically handles single-page app routing if you add a `_redirects` file to `dist/`:
```
/*  /index.html  200
```

For Vue Router apps, this prevents 404 errors when users navigate directly to a URL like `/about`.

### Custom domains
Both GitHub Pages and Netlify support custom domains. In GitHub Pages, add a `CNAME` file to the root of your deployment with your domain name. In Netlify, go to Domain settings and follow the DNS configuration steps. Free TLS certificates are provided automatically by both platforms.

### What goes in .gitignore
Never commit `node_modules/` or `dist/`. Both are generated and can be reproduced from `package.json` and source files. A standard Vite project's `.gitignore` includes both. If you are using the `/docs` folder for GitHub Pages deployment, you must commit `docs/` — that is the intentional exception.

## Common mistakes

1. **Auditing the Vite dev server instead of the production build.** The dev server includes unminified source files, hot-reload scripts, and no optimization. Always audit `npm run build` output served over a local static server or after deploying.

2. **Forgetting `base` in `vite.config.js` for GitHub Pages subdirectory deploys.** The app loads but all assets 404. Add `base: '/repo-name/'` to match your repository name.

3. **Using `placeholder` as a label substitute.** Placeholder text disappears on input, has insufficient contrast in most browsers by default, and is not reliably announced by screen readers. It is supplementary hint text, not a label.

4. **Treating a Lighthouse score of 100 as a guarantee of accessibility.** Automated tools check for detectable structural errors. They cannot tell whether alt text is meaningful, whether focus order makes logical sense, or whether a custom widget is usable with a screen reader. Manual testing is required.

5. **Committing `node_modules/` to the repository.** This is a common mistake on first deployments. It bloats the repository, slows clones, and can cause version conflicts. Verify `.gitignore` includes `node_modules/` before the first `git add`.

## Accessibility connection
Lighthouse accessibility scores measure automated rule compliance, not lived experience. The goal of this week's audit is not a number — it is building the habit of checking your work against the needs of real users. Keyboard-only navigation is used by people with motor disabilities, power users, and people with broken pointing devices. Screen readers are used by people who are blind or have low vision. Both groups are part of your audience on any public web project, and building with them in mind from the start is far less work than retrofitting accessibility at the end.

## Demo walkthrough
1. Open the completed Project 2 build (or the Week 12/13 card project) in Chrome.
2. Open DevTools > Lighthouse. Run an audit (Desktop mode, all categories).
3. Walk through each score. Click into the Accessibility section and expand the failing items.
4. Fix one failure live: find an image missing alt text in the source, add a meaningful `:alt` binding, rebuild, re-audit to show the score change.
5. Fix a second failure: find a form input missing a label, add `<label for="...">` and a matching `id`, re-audit.
6. Run `npm run build`. Show the `dist/` folder in the file system. Serve it locally: `npx serve dist`.
7. Add `gh-pages` to the project, add a `deploy` script, set `base` in `vite.config.js`, and run `npm run deploy`. Open the live URL.

## Practice prompt
Run a Lighthouse audit on your Project 2. Document every Accessibility failure in a short list. Fix at least three failures. Re-run Lighthouse and screenshot the before and after scores. Then deploy the fixed build to GitHub Pages or Netlify and submit the live URL alongside your fix list.

## Bridge
Lab 13 — Lighthouse, Accessibility, and Deployment walks you through this exact sequence: audit, fix, deploy, and document what changed. Quiz 8 is now a short readiness check on the core concepts behind that work: Lighthouse categories, common accessibility failures, and deployment verification steps. Project 2 final submission requires a live deployed URL, and Final Project Beta asks you to carry those same QA habits forward.
