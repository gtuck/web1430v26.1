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

### Cloning the course starter repo
The instructor will share a GitHub Classroom link in the Week 00 module. Clicking it creates a personal copy of the starter repository under your GitHub account. To get it onto your machine:

```bash
# Replace YOUR-USERNAME and REPO-NAME with the actual values shown on GitHub
git clone https://github.com/YOUR-USERNAME/REPO-NAME.git
cd REPO-NAME
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
3. **Editing files directly on GitHub.com instead of locally.** This creates a diverged history. Always work locally and push.
4. **Not installing Live Server before Lab 01.** Lab 01 requires a running local server. Install it now so you are not troubleshooting an extension during a lab deadline.
5. **Confusing the repo URL formats.** GitHub shows both HTTPS and SSH clone URLs. Use HTTPS unless you have set up an SSH key — the HTTPS URL starts with `https://github.com/`.

## Accessibility connection
Accessible online course design starts with the instructor, but students benefit from understanding it too. Canvas pages use heading structure, alt text on images, and sufficient color contrast — pay attention to how well-structured documents help you navigate faster, because you will apply the same principles to your own HTML pages starting in Week 02. Screen reader users and keyboard-only users depend on that structure.

## Demo walkthrough
**Goal:** Clone the starter repo, make one small change, and push it back to GitHub — in under 10 minutes.

1. Open the GitHub Classroom link from the Week 00 Canvas module and accept the assignment. Note the URL of your new repository.
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

## Practice prompt
Open VS Code and create a new folder called `week-00-practice` on your Desktop. Inside it, create a file called `notes.txt` and type three things you want to learn in this course. Initialize a Git repository in that folder (`git init`), stage the file, commit it with a descriptive message, and inspect the log with `git log --oneline`. You do not need to push this one — the goal is to practice the local commit cycle without a remote repository.

## Bridge
Completing the GitHub Repo Setup deliverable this week is the prerequisite for every lab in the course — all labs are submitted as pushes to GitHub repositories created through GitHub Classroom. The Canvas Orientation Quiz checks that you can find key course resources; take it after you finish reading through the Modules page so the answers are fresh. If anything in your setup is broken, post in the Help board now, before Lab 01 opens Monday.
