# Lab 00 – Local Setup and GitHub Workflow

## Purpose

Before any code can be written, you need a working development environment. This lab walks you through installing the tools you will use every week, configuring Git, requesting your course repository, and making your first commit. Getting this right in Week 0 prevents the most common source of early-semester frustration.

## Skills practiced

- Installing and verifying VS Code and Node.js
- Configuring Git with your name and email
- Requesting and cloning your course GitHub repository
- Making commits with meaningful messages
- Pushing changes and verifying them on GitHub
- Checking repository status and safely syncing with GitHub

## What you're building

A course repository on GitHub that will hold all your labs, assignments, and projects this semester. The repository is created for you in the course's `web1430-fall26` GitHub organization, pre-loaded with the semester's folder structure and starter files. By the end of this lab your repo will be live, your tools will be verified, and you will have made your first real commit.

---

## Part 1: Install tools

### 1.1 Visual Studio Code

Download and install VS Code from code.visualstudio.com. After installing, open it and install the following extensions (Extensions panel, left sidebar):

- **Prettier – Code Formatter** (esbenp.prettier-vscode)
- **ESLint** (dbaeumer.vscode-eslint)
- **Live Server** (ritwickdey.LiveServer)

### 1.2 Node.js

Download and install the **LTS** version of Node.js from nodejs.org. After installing, open a terminal (VS Code → Terminal → New Terminal) and verify:

```bash
node --version    # should print v18.x.x or higher
npm --version     # should print 9.x.x or higher
```

If either command returns "command not found," restart your terminal and try again. If the problem persists, reinstall Node.js.

### 1.3 Git

**Mac**: Git is installed with Xcode Command Line Tools. Run `git --version` in the terminal. If it's not installed, macOS will prompt you to install it.

**Windows**: Download from git-scm.com. During installation, select "Use Git from the command line and also from 3rd-party software."

Verify: `git --version` should print a version number.

---

## Part 2: Configure Git

Run both of these commands in your terminal, replacing the placeholder values with your own name and the email address you use for GitHub:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

Verify: `git config --list` should show your name and email.

---

## Part 3: Request your course GitHub repository

Your course repository is created for you — with the starter files already in it — through the course repo request page:

1. Don't have a GitHub account? Create one first at `https://github.com/join` using your `@mail.weber.edu` email address — you'll use the same username in the next step.
2. Go to <https://crsapps.netlify.app/gh?instructor=gt&course=WEB1430&task=CourseTemplate>
3. Enter your GitHub username exactly as it appears on GitHub (typos will block submission).
4. Enter this passcode: `MrC0der2shoe$`
5. Click **Create Repo**. You'll get an invitation link — accept it (sign in to GitHub first), and your repository is ready to clone from the `web1430-fall26` organization.

---

## Part 4: Clone the repository to your machine

Open your new repository in the `web1430-fall26` organization (the invitation you accepted takes you there), click the green **Code** button, and copy the HTTPS URL.

In your terminal, navigate to where you keep your projects (e.g., `~/Documents/GitHub`), then clone:

```bash
git clone https://github.com/web1430-fall26/YOUR-REPO-NAME.git
cd YOUR-REPO-NAME
```

Open the folder in VS Code: `code .`

---

## Part 5: Explore the folder structure

Your repository comes pre-built with the folder structure and starter files for the whole semester:

```
your-repo/
  labs/
    lab00/ … lab13/    # starter files already included where a lab has them
  assignments/
  projects/
```

Every lab, assignment, and project you submit this semester lives in one of these folders. Do not rename or move them.

Open `labs/lab00/index.html` in Live Server (right-click the file → Open with Live Server) and verify you see the Lab 00 page in your browser.

---

## Part 6: Make your first commit and push

Open `README.md` at the root of your repository and personalize it: add your name and one short sentence about what you want to get out of this course.

In the terminal (inside your repo folder):

```bash
git add README.md
git commit -m "lab00: add name and course goal to README"
git push
```

Visit your repository on GitHub and verify your change appears there.

---

## Part 7: Sync and recovery check

After your first push, run these commands:

```bash
git status
git pull --ff-only
```

You should see a clean working tree and an "Already up to date" message.

Why this matters:
- `git status` tells you whether you have local changes that are not committed yet.
- `git pull --ff-only` is the safest first sync command when you just want to update your local repo without creating a surprise merge commit.

If `git pull --ff-only` fails because you have local edits, do **not** panic. Run `git status`, commit the work you want to keep, and try again. If Git shows conflict markers like `<<<<<<<`, save the file, ask for help if needed, and do not keep coding until the markers are removed and the file is committed again.

---

## Part 8: Smoke test checklist

Before submitting, confirm every item below:

- [ ] `node --version` prints v18 or higher
- [ ] `npm --version` prints a version number
- [ ] `git --version` prints a version number
- [ ] `git config user.name` and `git config user.email` show your details
- [ ] Your GitHub repository exists in the `web1430-fall26` organization and you accepted the invitation
- [ ] Your personalized `README.md` is committed and visible on GitHub, and `labs/lab00/index.html` opens in Live Server
- [ ] The page opens correctly in Live Server
- [ ] `git status` shows a clean working tree after your first push
- [ ] `git pull --ff-only` runs successfully after your first push

---

## Troubleshooting

**No invitation, or a 404 when opening your repository**: Make sure you accepted the invitation link shown after clicking **Create Repo** (an email invitation also goes to the address on your GitHub account, so check there). If the link expired or you entered the wrong username, post in the Help & Questions board with your exact GitHub username so the repo can be re-issued.

**"git: command not found" on Mac**: Run `xcode-select --install` in the terminal.

**"Permission denied" when pushing**: You may need to authenticate. GitHub now requires a Personal Access Token instead of a password. Go to GitHub → Settings → Developer Settings → Personal Access Tokens → Generate new token. Use that token as your password when Git prompts for credentials.

**"rejected — fetch first" or "Updates were rejected" when pushing**: Your GitHub copy changed and your local copy is behind. Run `git status`, then `git pull --ff-only`. If Git says you have local changes, commit them first. If you see conflict markers in a file, stop and fix them before your next push.

**Live Server shows a blank page**: Check that you saved the file (Cmd/Ctrl+S). Check that there are no errors in the VS Code terminal.

**npm install errors**: Make sure you installed the LTS version of Node.js, not the "Current" version.

---

## Deliverable

Submit to Canvas:
- The URL of your GitHub repository (it will look like `https://github.com/web1430-fall26/your-repo-name`)
- A screenshot showing your terminal with `node --version`, `npm --version`, `git --version`, and `git status` output

## Process reflection

In 3–5 sentences: What took longer than expected? What error did you run into and how did you fix it? What does your commit history look like so far? If your local repo and GitHub ever differed, what command would you run first and why?

---

## Rubric

| Criterion | Excellent (4) | Proficient (3) | Developing (2) | Incomplete (1) |
|-----------|--------------|----------------|----------------|----------------|
| **Tools installed and verified** | All three tools verified in terminal with correct versions | Two of three verified | One verified, others attempted | No verification shown |
| **Repository setup** | Repo created in the course organization, invitation accepted, starter structure intact | Repo exists, some structure present | Repo exists but access/setup incomplete | No repo found |
| **First commit and push** | Meaningful commit message, file visible on GitHub | File on GitHub, generic message | Pushed but incomplete | Not pushed |
| **Smoke test** | All checklist items confirmed, including status and sync check | Most items confirmed | Some items confirmed | Few or none confirmed |
| **Reflection** | Specific, honest account of what worked and what broke | Addresses the prompts briefly | Vague or one sentence | Missing |
