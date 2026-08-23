# Week 00 Lecture Notes: Online Learning, Canvas, GitHub, and the Course Toolchain

## Weekly focus

Getting every student to the same starting line: tools installed, accounts connected, and the weekly rhythm understood before a single line of code is written.

## Why this matters

In a fully online course, the toolchain *is* the classroom. If your editor, terminal, and GitHub account are not working together from day one, every subsequent lab becomes a debugging session about setup rather than about web development. This week removes that friction so the rest of the semester can move quickly. The habits you build now — committing early, reading Canvas announcements, checking due dates on Sunday — compound over 16 weeks.

## Learning targets

- Navigate Canvas to find weekly modules, the syllabus, assignment rubrics, and the discussion board
- Install and configure VS Code with the recommended extensions for this course
- Create a GitHub account and explain the difference between Git (local version control) and GitHub (remote hosting)
- Clone a repository to your machine, make a change, commit it, and push it back to GitHub
- Use `git status` and `git pull --ff-only` to check whether your local repository is in sync with GitHub
- Describe the weekly rhythm: when to read, when labs are due, and how to ask for help asynchronously
- Submit the Welcome Survey and the GitHub Repo Setup deliverable

## Core concepts

### How this course is structured
WEB 1430 runs on a Monday–Sunday weekly cycle. Each week opens Monday morning and contains:
- **Lecture notes** (this document and others like it) — read these first
- **Chapter reading** from the course textbook
- **A lab** due by Sunday at 11:59 PM
- Occasional **quizzes** or **assignments** due on the same Sunday

There are no live sessions. Instructor feedback comes via Canvas comments and GitHub pull-request reviews. Check Canvas at least three times per week: Monday to see what opened, midweek to track your progress, and Saturday to catch anything before the deadline.

### Canvas navigation
The left sidebar in Canvas has four links you will use every week:
1. **Modules** — the authoritative list of what to do and in what order
2. **Assignments** — where you submit work and see rubric scores
3. **Grades** — running total; check this after each submission
4. **Announcements** — where the instructor posts corrections, tips, and reminders

Do not rely on the Canvas dashboard tiles for due dates. Always go to **Modules** to confirm what is required this week.

### VS Code setup
Download VS Code from `code.visualstudio.com`. After installing, add these extensions from the Extensions panel (`Ctrl+Shift+X` / `Cmd+Shift+X`):

- **Prettier – Code formatter** (esbenp.prettier-vscode) — auto-formats on save
- **ESLint** (dbaeumer.vscode-eslint) — flags JavaScript errors as you type
- **Live Server** (ritwickdey.LiveServer) — launches a local dev server with auto-reload
- **GitLens** (eamodio.gitlens) — shows inline Git blame and history

Enable format-on-save: open Settings (`Ctrl+,`), search for `format on save`, and check the box. This keeps your code consistently formatted without manual effort.

### Git and GitHub — the conceptual model
Git is software installed on your computer that tracks changes to files. GitHub is a website that stores a copy of your repository so others (and you, from other machines) can access it.

The three-step local workflow you will repeat every week:
```bash
git add .                        # stage all changed files
git commit -m "describe the change"  # save a snapshot locally
git push                         # send the snapshot to GitHub
```

A commit message should finish the sentence "This commit will…". Write `"Add hero section HTML"`, not `"stuff"` or `"asdfgh"`.

### Staying in sync with GitHub
The first push is not the end of the workflow. You also need to know whether your local copy and GitHub still agree.

```bash
git status         # tells you whether files are changed, staged, or clean
git pull --ff-only # updates your local repo only when Git can do it safely without a merge commit
git push           # sends your committed work to GitHub
```

Use this order when something feels off:
1. Run `git status` and read it carefully.
2. If your work is committed and you just need updates from GitHub, run `git pull --ff-only`.
3. If `git push` is rejected because the remote changed, stop and sync before making more edits.

`git pull --ff-only` is a good Week 00 default because it keeps the sync behavior simple. It succeeds when GitHub is simply ahead of your local copy and stops when the situation is more complicated.

### Simple recovery example
Imagine this sequence:
- You pushed your Lab 00 file yesterday.
- Today you made a quick README edit on GitHub.com or from another machine.
- Now your laptop copy is behind GitHub, and `git push` says the remote contains work you do not have yet.

Start here:

```bash
git status
git pull --ff-only
```

If Git updates cleanly, you are done. If Git says you have local changes, commit them first. If Git stops and a file shows markers like this:

```txt
<<<<<<< HEAD
Local version
=======
GitHub version
>>>>>>> main
```

That is a merge conflict. Open the file, decide what content to keep, delete the marker lines, save, then run:

```bash
git add <file>
git commit -m "Resolve merge conflict in <file>"
git push
```

You are not expected to be fast at this in Week 00. You are expected to recognize the situation and stop before making it messier.

### Cloning the course starter repo
Your course repository is created for you — pre-loaded with the semester's folder structure (`labs/`, `assignments/`, `projects/`) and starter files — through the course repo request page:

1. Don't have a GitHub account? Create one first at `https://github.com/join` using your `@mail.weber.edu` email address — you'll use the same username in the next step.
2. Go to [https://crsapps.netlify.app/gh?instructor=gt&course=WEB1430&task=CourseTemplate](https://crsapps.netlify.app/gh?instructor=gt&course=WEB1430&task=CourseTemplate)
3. Enter your GitHub username exactly as it appears on GitHub (typos will block submission).
4. Enter the course passcode — it is posted in the **Course Repo Passcode** announcement in Canvas (Announcements → Course Repo Passcode).
5. Click **Create Repo**. You'll get an invitation link — accept it, and your repository is ready to clone from the `web1430-fall26` organization.

To get it onto your machine:

```bash
# Replace YOUR-REPO-NAME with the actual name shown on GitHub
git clone https://github.com/web1430-fall26/YOUR-REPO-NAME.git
cd YOUR-REPO-NAME
code .          # opens the folder in VS Code
```

After cloning, open the integrated terminal in VS Code (`Ctrl+`` ` ``/ `Cmd+`` ` ``) — you will run all Git commands there.

### The terminal basics you need right now
You do not need to be a command-line expert. You need four commands:

```bash
pwd        # print working directory — where am I?
ls         # list files in the current folder
cd folder  # change into a folder
cd ..      # go up one level
```

If a Git command fails, read the error message. Git errors are usually self-explanatory: "nothing to commit," "not a git repository," "rejected — fetch first." Google the exact error text when you are stuck.

### Asking for help online
This course has a **Help & Questions** discussion board in Canvas. Post there before emailing. Include:
- What you were trying to do
- The exact command or step that failed
- The exact error message (paste it, do not paraphrase)
- A screenshot if relevant

Other students can answer, which benefits everyone. The instructor checks the board at least once per business day.

## Common mistakes

1. **Skipping the Modules view.** Students who navigate Canvas by clicking dashboard tiles miss hidden links and submission instructions buried in module pages.
2. **Committing without a message.** Running `git commit` without `-m "..."` drops you into a terminal text editor (Vim). If this happens, type `:q!` and press Enter to exit, then re-run with the `-m` flag.
3. **Editing files directly on GitHub.com instead of locally.** This can create a diverged history. If it happens, stop, run `git status`, then `git pull --ff-only` before making more changes locally.
4. **Not installing Live Server before Lab 01.** Lab 01 requires a running local server. Install it now so you are not troubleshooting an extension during a lab deadline.
5. **Confusing the repo URL formats.** GitHub shows both HTTPS and SSH clone URLs. Use HTTPS unless you have set up an SSH key — the HTTPS URL starts with `https://github.com/`.
6. **Trying random Git commands after a rejected push.** In this course, your first recovery move should usually be `git status`, not guessing.

## Demo walkthrough

**Goal:** Clone the starter repo, make one small change, and push it back to GitHub — in under 10 minutes.

1. Request your repository through the course repo request page (see "Cloning the course starter repo" above) and accept the invitation. Note the URL of your new repository in the `web1430-fall26` organization.
2. Copy the HTTPS clone URL from the green "Code" button on GitHub.
3. Open a terminal on your machine and run `git clone <url>`. Verify the folder appears with `ls`.
4. `cd` into the folder and run `code .` to open it in VS Code.
5. Open `README.md`. Add one line at the bottom: `Student: Your Name`.
6. Save the file. In the VS Code integrated terminal:
   ```bash
   git add README.md
   git commit -m "Add student name to README"
   git push
   ```
7. Refresh your GitHub repository page. Confirm the README now shows your name.
8. Show the commit history on GitHub: click the clock icon ("N commits") above the file list to see every snapshot.
9. Back in the terminal, run:
   ```bash
   git status
   git pull --ff-only
   ```
   Confirm that the working tree is clean and your local repo is in sync with GitHub.

## Session 2: the studio

The rest of this week's material lives in the studio notes — Wednesday's live session for the virtual section, and the second half of the week's work for the online section: [Week 00 Studio Notes: Setup Clinic and First Push](week-00-studio.md).

Read the *Before class* list there before you start, and bring what it asks for.
