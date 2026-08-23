# Week 15 Lecture Notes: Project Storytelling, Portfolio Readiness, and Next Steps

## Weekly focus
How to present your project work, what makes a portfolio visible to employers, and where to go from here.

## Why this matters
Technical skill without communication is invisible. Employers reviewing front-end portfolios spend less than two minutes on each project before deciding whether to read further. A clear README, a coherent commit history, and the ability to explain your technical decisions out loud are what separate candidates who get interviews from candidates who do not. This week is about translating the work you have already done into evidence of capability.

## Learning targets
- Articulate what problem a project solves, what technical decisions were made, and what trade-offs were accepted
- Write a project README that communicates purpose, setup instructions, and design decisions to a technical reader
- Evaluate a GitHub repository's commit history as a professional signal and identify what makes it strong or weak
- Identify at least two realistic next steps for continuing front-end development after this course
- Describe what front-end employers look at when reviewing a portfolio

## Core concepts

### Presenting a project: the three questions
When a recruiter, hiring manager, or senior developer looks at your project, they are trying to answer three questions. Practice answering all three out loud before any interview:

**1. What problem does this solve?**
"A card-based UI for browsing and filtering a product catalog" is a problem statement. "A Vue 3 app with components" is a technology description. Start with the user need, not the implementation. Even small class projects have a problem they address — name it.

**2. What technical decisions did you make, and why?**
This is where you demonstrate judgment, not just execution. Why Vite instead of a CDN script? Because module bundling and hot reload made development faster and the build output is optimized. Why `reactive()` for the form instead of individual `ref()` calls? Because the fields belong together and destructuring is not needed. You do not need to defend every choice — pick two or three meaningful ones and explain the trade-off.

**3. What would you do differently?**
This is the question that separates a learner from a professional. Nobody's first version is their best version. Saying "I would extract the data fetching into a composable so the component only handles display logic" shows that you understand the code you wrote and can identify its limitations. Saying "nothing, it's fine" signals the opposite.

### Writing a project README
A README is the cover letter for a repository. It lives at the root of the project as `README.md` and is rendered automatically on GitHub. A strong README for a course project includes:

```
# Project Name

One or two sentences describing what the project does and who it is for.

## Live Demo
[Link to deployed site]

## Features
- What the project does (user-facing, not technical)
- Feature 2
- Feature 3

## Technical decisions
Brief explanation of framework/tool choices and why they were made.

## Setup
Steps to run the project locally:

    git clone https://github.com/username/repo-name
    cd repo-name
    npm install
    npm run dev

## Known limitations / future work
What you would improve with more time.

## Accessibility
Note any accessibility features you implemented or known gaps.
```

Keep it factual and specific. Avoid filler phrases like "This is a simple project that demonstrates..." — get to the point. The setup section is not optional; another developer must be able to clone and run your project without asking you questions.

### Git commit history as a professional signal
A recruiter with a GitHub link can see your entire commit history. What they are looking for:

**Strong signals:**
- Commits are small and focused: "Add filter input to SearchBar component" rather than "stuff"
- Commits happen throughout the project timeline, not in one batch the night before the deadline
- Commit messages describe what changed and why, not what file was touched
- Branch names are descriptive if branches were used

**Weak signals:**
- One or two massive commits with hundreds of changed files
- Messages like "final", "fixed it", "asdfgh", or "changes"
- A commit history that starts the day a project is due
- Committing `node_modules/` or `.DS_Store` files

You cannot retroactively fix a commit history before submitting this semester's work, but you can start building good habits on every project from now on. Employers reviewing entry-level portfolios do look at commit frequency and message quality.

### What employers look for in front-end portfolios
Based on what front-end hiring managers describe when asked about entry-level portfolios:

**Deployed, working projects.** A GitHub link that 404s or a project that throws a console error on load immediately lowers confidence. Every project in your portfolio should have a live URL and should work without errors.

**Evidence of decisions, not just output.** A to-do list app built in plain JavaScript and a to-do list app built in Vue tell different stories if the portfolio explains *why* the choice was made. The explanation is what shows thinking.

**Accessibility awareness.** More employers are asking about WCAG compliance in interviews. Even one sentence in your README like "All interactive elements are keyboard accessible and color contrast meets WCAG AA requirements" demonstrates that you know accessibility exists and acted on it.

**Readable source code.** Not perfect code — readable code. Consistent indentation, meaningful variable names, and short focused functions signal that you can work in a team codebase.

**Breadth over depth is usually fine at the entry level.** Three solid projects that show HTML/CSS, JavaScript, and a framework are enough to get interviews. You do not need ten projects.

### Paths forward: what comes after this course

**Vue Router and Pinia** — the natural next steps inside the Vue ecosystem. Vue Router adds client-side routing (multiple "pages" in a single-page app). Pinia is Vue's official state management library for sharing state between components that are not in a parent-child relationship.

**React** — the most common framework in U.S. job postings. If you understand Vue's Composition API, React's hooks (`useState`, `useEffect`, `useRef`) will feel familiar. The mental model is the same; the syntax is different.

**Svelte** — a framework that compiles to vanilla JavaScript with no runtime. Smaller bundles, simpler reactivity syntax. Worth learning as a second framework.

**Node.js and Express** — if you want to build APIs and work full-stack. Node lets you run JavaScript on the server. Express is a minimal web framework. You already know JavaScript — the backend is more accessible than it looks.

**TypeScript** — adds static types to JavaScript. Most professional Vue and React codebases use TypeScript. It catches errors before they reach the browser and makes large codebases easier to navigate.

**Design systems** — Figma, design tokens, and component libraries like Vuetify, Radix, or shadcn/ui. Understanding how design systems work makes you a better collaborator with designers and makes your own projects more consistent.

**Accessibility specialist track** — WCAG 2.2, ARIA patterns, axe-core, and formal accessibility testing. A specialist in accessibility is consistently in demand and the supply of qualified developers is low.

### How to keep learning after the course ends
The web platform changes continuously. Some practices that stay relevant:

- **Build projects, not tutorials.** Following a tutorial produces a project that looks like the tutorial. Building something you want to exist — even if it is small — teaches problem-solving.
- **Read the official documentation.** Vue's docs at vuejs.org, MDN Web Docs for browser APIs. Both are written for developers, not academics, and are the most reliable source.
- **Review other people's code.** Contributing to open source projects, even just reading issues and PRs, exposes you to codebases and conventions you would not otherwise see.
- **Write about what you build.** A short post on a personal site or dev.to explaining how you solved one problem forces you to understand it well enough to explain it. It also creates a public record of your learning.

## Common mistakes

1. **Building a portfolio of tutorial clones.** If you followed a tutorial step-by-step, the project belongs in a practice folder, not your portfolio. Employers can identify tutorial projects. Add one meaningful change or build something adjacent that is genuinely yours.

2. **Not writing a README.** A repository with only source files and no README asks the reviewer to clone and run the project before they know if it is worth their time. Most will not.

3. **Describing technology instead of outcomes in project descriptions.** "Built with Vue 3 Composition API, Vite, and CSS Grid" is a list of tools. "A searchable product catalog that filters in real time as you type, built with Vue 3" tells a story. Lead with the outcome.

4. **Treating the final project as done when it is submitted.** The final project is a starting point for a portfolio piece, not a finished artifact. After the semester ends, spend a few hours improving it: add keyboard navigation, fix the one known bug, improve the mobile layout.

5. **Waiting until you feel "ready" to apply or share work.** Entry-level portfolios are not expected to look like senior work. Apply early, share work in progress, and treat rejections as data rather than verdicts.

## Accessibility connection
Accessibility is not a feature you add to a project before you ship it — it is a lens you apply throughout. If your portfolio itself is inaccessible (low contrast, missing alt text on project screenshots, no keyboard navigation), it undercuts any claim that you value accessible development. Audit your portfolio site with Lighthouse and fix the failures. It takes less than an hour and sends a clear signal to any employer who notices.

## Demo walkthrough
This week's demo is a portfolio review exercise rather than a code demonstration. Walk through the following:

1. Open a student project (with permission) or a sample repository on GitHub.
2. Read the README aloud as if you were a reviewer seeing it for the first time. What questions does it leave unanswered?
3. Look at the commit history. Count how many commits there are. Read the five most recent messages. What story do they tell?
4. Open the live deployed URL. Tab through the page without touching the mouse. What happens?
5. Run Lighthouse on the live URL. Look at the Accessibility score. Click into the failures.
6. Write a two-sentence project description that leads with the problem, not the technology.

## Practice prompt
Write a README for your Final Project using the template structure from this week's notes. Include a live URL, a feature list written from the user's perspective, a brief explanation of two technical decisions you made and why, and one thing you would do differently with more time. Bring the README to the Final Studio session for peer feedback, or post it in **Help & Questions** if you would like written comments before the deadline.

## Bridge
The Final Studio session is unstructured work time — bring your project, your README draft, and specific questions. The Final Exam covers concepts from the full semester; review the learning targets from each week's lecture notes. The Course Reflection asks five questions: what you built, the hardest technical problem you solved, what you would do differently, what "accessible" means to you now that it didn't in Week 1, and what you are most proud of. Connecting each answer to specific decisions and specific code is what separates a strong reflection from a generic one.
