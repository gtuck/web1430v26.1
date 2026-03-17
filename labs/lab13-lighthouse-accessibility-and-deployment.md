# Lab 13 – Lighthouse, Accessibility, and Deployment

## Purpose

Code that runs locally but is never deployed is unfinished. Code that deploys but scores poorly on performance and accessibility is incomplete. This lab closes the loop: you will audit a previous project with Lighthouse, identify and fix issues, verify improvements, and deploy a production-ready build.

This lab is also the main applied quality-assurance evidence for Week 14, so your notes should directly inform Project 2, your Final Project beta, or both.

## Skills practiced

- Running a Lighthouse audit in Chrome DevTools
- Reading and interpreting Lighthouse scores (Performance, Accessibility, Best Practices, SEO)
- Identifying and fixing common accessibility failures (missing labels, low contrast, missing alt text)
- Identifying and fixing common performance issues (missing meta viewport, large images, render-blocking resources)
- Deploying a Vite project to Netlify or GitHub Pages
- Verifying deployment with a second Lighthouse audit

## What you're auditing

Choose **one** project you can still improve this week. Strongly recommended: **Project 2** or your **Final Project beta**. Those are the artifacts most likely to benefit immediately from a real QA pass.

If neither current project is ready enough to audit, use Lab 08 or Lab 05 as a fallback. The goal is still to practice a QA workflow you can carry into the current week's graded work.

---

## Part 1: Run the initial Lighthouse audit

1. Open your deployed page in **Chrome** (Lighthouse works best in Chrome).
2. Open DevTools → **Lighthouse** tab (or right-click → Inspect → Lighthouse).
3. Configure:
   - Categories: Performance, Accessibility, Best Practices, SEO
   - Device: Mobile
4. Click **Analyze page load**.
5. Wait for the audit to complete (30–60 seconds).
6. Take a **full-page screenshot** of the results panel showing all four scores.

Record your baseline scores in `labs/lab13/notes.md`:

```
## Baseline scores (mobile)
- Performance: XX
- Accessibility: XX
- Best Practices: XX
- SEO: XX
```

---

## Part 2: Read and understand the audit

Expand each failed or warning-level audit item. For each issue, Lighthouse shows:
- What failed and why
- How many elements are affected
- A link to documentation

In your `notes.md`, document at least **six issues** Lighthouse flagged, organized by category. Write the notes clearly enough that they function like a short QA memo, not just a checklist:

```
## Issues found

### Accessibility
1. [Issue name] — [what it means in plain language] — [which element(s) affected]
2. ...

### Performance
3. ...

### Best Practices / SEO
5. ...
```

---

## Part 3: Fix the issues

Fix at least **five** of the issues you documented. For each fix, record:
- What you changed
- The file and line number
- Why the fix addresses the issue

Prioritize fixes you can actually carry into this week's submission. The best version of this lab improves a real project, not only a disconnected practice page.

### Common accessibility fixes

**Missing form labels:**
```html
<!-- Before -->
<input type="text" placeholder="Search...">

<!-- After -->
<label for="search-input">Search</label>
<input type="text" id="search-input" placeholder="Search...">
```

**Images without alt text:**
```html
<!-- Before -->
<img src="cover.jpg">

<!-- After -->
<img src="cover.jpg" alt="Book cover: Dune by Frank Herbert">
```

**Insufficient color contrast:**
Change the color values in your CSS custom properties so the contrast ratio is at least 4.5:1 for normal text. Use the WebAIM Contrast Checker (webaim.org/resources/contrastchecker/) to verify.

**Missing `lang` attribute:**
```html
<html lang="en">
```

**Links with no discernible text** (e.g., icon-only links):
```html
<!-- Before -->
<a href="..."><img src="github-icon.svg"></a>

<!-- After -->
<a href="..." aria-label="View project on GitHub"><img src="github-icon.svg" alt=""></a>
```

### Common performance fixes

**Missing meta viewport** (already in lab templates, but check):
```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

**Render-blocking scripts:** Move `<script>` tags to end of `<body>` or add `defer`.

**Missing `<title>` element:**
```html
<title>Open Library Book Search – WEB 1430 Lab 08</title>
```

**Images without explicit width/height** (causes layout shift):
```html
<img src="cover.jpg" alt="..." width="200" height="300">
```

### Common SEO fixes

**Missing meta description:**
```html
<meta name="description" content="Search books by title using the Open Library API.">
```

---

## Part 4: Run the audit again

After fixing at least five issues:
1. Rebuild if it's a Vite project (`npm run build`) and redeploy
2. Clear the browser cache (DevTools → Application → Clear Site Data, or open in Incognito)
3. Run Lighthouse again with the same settings
4. Take a screenshot of the new results

Record your final scores:

```
## Final scores (mobile)
- Performance: XX (+/- from baseline)
- Accessibility: XX (+/- from baseline)
- Best Practices: XX
- SEO: XX
```

**Target:** Accessibility score of 90 or above. Performance and SEO scores of 70 or above.

---

## Part 5: Deployment verification

If you deployed a Vite project, verify the deployment was built correctly:

1. The deployed URL loads without a blank screen
2. All assets (CSS, JS, images) load — check the Network tab for 404 errors
3. The page functions the same as on the dev server
4. Run Lighthouse on the deployed URL (not localhost)

Common deployment issues:
- **Blank screen on Netlify**: Check that the publish directory is set to `dist/`
- **404 on GitHub Pages**: Ensure you're deploying from the correct branch and folder
- **Assets not loading**: Check that all import paths are relative, not absolute

---

## Part 6: Final accessibility walkthrough

Do a manual accessibility check before submitting:

- [ ] Tab through the entire page — every interactive element is reachable
- [ ] Focus ring is visible on all focused elements
- [ ] No keyboard traps (you can tab into and out of all components)
- [ ] Test with VoiceOver (Mac: Cmd+F5) or NVDA (Windows: free download) — navigate to the main heading and through at least three interactive elements. See the [Screen Reader Testing Guide](../course/screen-reader-testing-guide.md) for step-by-step instructions.
- [ ] Color is not the only indicator for any state (error, active, selected)

---

## Deliverable

In `labs/lab13/`:
- `notes.md` — baseline scores, six documented issues, five fixes documented, final scores; treat this like a short QA memo you can reuse
- `screenshot-baseline.png` — initial Lighthouse report
- `screenshot-final.png` — final Lighthouse report
- A link to the deployed, audited project

Submit to Canvas: your deployed project URL, GitHub repo URL, and the link to `labs/lab13/notes.md`.

If you audited Project 2 or the Final Project beta, use the same issue list when writing that project's self-assessment or revision plan.

---

## Process reflection (in notes.md)

Answer in 4–6 sentences:
- Which Lighthouse issue surprised you most and why?
- Which fix had the biggest impact on your scores?
- What is one accessibility issue that Lighthouse cannot detect automatically, and how would you test for it?

---

## Rubric

| Criterion | Excellent (4) | Proficient (3) | Developing (2) | Incomplete (1) |
|-----------|--------------|----------------|----------------|----------------|
| **Baseline audit** | Lighthouse run on deployed site; all four scores documented; screenshot provided | Three scores documented; screenshot present | Scores documented; no screenshot | No audit |
| **Issue documentation** | Six issues documented with plain-language explanation and affected elements | Four or five issues | Two or three issues | Fewer than two |
| **Fixes** | Five issues fixed; each fix documented with file, line, and explanation | Four fixes documented | Two or three fixes | One or zero |
| **Final audit** | Re-audit run; final scores documented; Accessibility ≥ 90 achieved | Accessibility 75–89 | Accessibility 60–74 | No re-audit |
| **Manual walkthrough** | All six checklist items verified; screen reader test documented | Four items verified | Two items | Not completed |
| **Reflection** | Specific; all three prompts addressed | Two prompts | Vague | Missing |
