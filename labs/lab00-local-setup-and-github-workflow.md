# Lab 00 – Local Setup and GitHub Workflow

## Purpose

Before any code can be written, you need a working development environment. This lab walks you through installing the tools you will use every week, configuring Git, creating your course repository on GitHub, and making your first commit. Getting this right in Week 0 prevents the most common source of early-semester frustration.

## Skills practiced

- Installing and verifying VS Code and Node.js
- Configuring Git with your name and email
- Creating and cloning a GitHub repository
- Making commits with meaningful messages
- Pushing changes and verifying them on GitHub
- Checking repository status and safely syncing with GitHub

## What you're building

A course repository on GitHub that will hold all your labs, assignments, and projects this semester. By the end of this lab your repo will be live, your tools will be verified, and you will have made your first real commit.

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

## Part 3: Create your course GitHub repository

1. Log in to github.com. Create an account if you don't have one — use your school email.
2. Click **New repository** (the + icon, top right).
3. Name it `web1430-[yourname]` (e.g., `web1430-jordan-smith`). Make it public if your section uses public repos; otherwise a private or instructor-shared repo is acceptable as long as your instructor can access it.
4. Check **Add a README file**.
5. Click **Create repository**.

---

## Part 4: Clone the repository to your machine

On your repository page, click the green **Code** button and copy the HTTPS URL.

In your terminal, navigate to where you keep your projects (e.g., `~/Documents/GitHub`), then clone:

```bash
git clone https://github.com/YOUR-USERNAME/web1430-yourname.git
cd web1430-yourname
```

Open the folder in VS Code: `code .`

---

## Part 5: Set up your folder structure

Inside the cloned repository, create the following folders. You can do this in VS Code's Explorer panel or in the terminal:

```
web1430-yourname/
  labs/
    lab00/
  assignments/
  projects/
```

Inside `labs/lab00/`, create a file called `index.html` with the following starter content:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Lab 00 – Setup</title>
</head>
<body>
  <main>
    <h1>WEB 1430 – Lab 00</h1>
    <p>Tools installed. Environment ready.</p>
  </main>
</body>
</html>
```

Open it in Live Server (right-click the file → Open with Live Server) and verify you see the page in your browser.

---

## Part 6: Make your first commit and push

In the terminal (inside your repo folder):

```bash
git add labs/lab00/index.html
git commit -m "lab00: initial setup and folder structure"
git push
```

Visit your repository on GitHub and verify the file appears there.

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
- [ ] Your GitHub repository is visible at its URL and accessible to your instructor
- [ ] `labs/lab00/index.html` is committed and visible on GitHub
- [ ] The page opens correctly in Live Server
- [ ] `git status` shows a clean working tree after your first push
- [ ] `git pull --ff-only` runs successfully after your first push

---

## Troubleshooting

**"git: command not found" on Mac**: Run `xcode-select --install` in the terminal.

**"Permission denied" when pushing**: You may need to authenticate. GitHub now requires a Personal Access Token instead of a password. Go to GitHub → Settings → Developer Settings → Personal Access Tokens → Generate new token. Use that token as your password when Git prompts for credentials.

**"rejected — fetch first" or "Updates were rejected" when pushing**: Your GitHub copy changed and your local copy is behind. Run `git status`, then `git pull --ff-only`. If Git says you have local changes, commit them first. If you see conflict markers in a file, stop and fix them before your next push.

**Live Server shows a blank page**: Check that you saved the file (Cmd/Ctrl+S). Check that there are no errors in the VS Code terminal.

**npm install errors**: Make sure you installed the LTS version of Node.js, not the "Current" version.

---

## Deliverable

Submit to Canvas:
- The URL of your GitHub repository (e.g., `https://github.com/username/web1430-yourname`)
- A screenshot showing your terminal with `node --version`, `npm --version`, `git --version`, and `git status` output

## Process reflection

In 3–5 sentences: What took longer than expected? What error did you run into and how did you fix it? What does your commit history look like so far? If your local repo and GitHub ever differed, what command would you run first and why?

---

## Rubric

| Criterion | Excellent (4) | Proficient (3) | Developing (2) | Incomplete (1) |
|-----------|--------------|----------------|----------------|----------------|
| **Tools installed and verified** | All three tools verified in terminal with correct versions | Two of three verified | One verified, others attempted | No verification shown |
| **Repository setup** | Repo accessible to instructor, correct name, proper folder structure committed | Repo exists, some structure present | Repo exists but access/setup incomplete | No repo found |
| **First commit and push** | Meaningful commit message, file visible on GitHub | File on GitHub, generic message | Pushed but incomplete | Not pushed |
| **Smoke test** | All checklist items confirmed, including status and sync check | Most items confirmed | Some items confirmed | Few or none confirmed |
| **Reflection** | Specific, honest account of what worked and what broke | Addresses the prompts briefly | Vague or one sentence | Missing |
