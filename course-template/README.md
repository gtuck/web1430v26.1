# WEB 1430 – Course Repository

This is your personal repository for **WEB 1430: Client-Side Web Development** at Weber State University. Every lab, assignment, and project this semester is committed to this repository and pushed to GitHub — it is the record of your work for the course.

**Student:** *(your name — adding it here is part of your first commit in Lab 00)*

**Course goal:** *(one sentence about what you want to get out of this course)*

## Repository structure

```
labs/           one folder per lab (lab00 … lab13); starter files are already
                in place for the labs that have them
assignments/    one folder per assignment (see assignments/README.md)
projects/       one folder per project (see projects/README.md)
```

Do **not** rename or move these top-level folders — graders and course tooling rely on this layout.

## Working rhythm

Commit early and often, with messages that finish the sentence "This commit will…":

```bash
git add .
git commit -m "describe the change"
git push
```

Before starting new work, make sure your local copy and GitHub agree:

```bash
git status          # anything changed, staged, or clean?
git pull --ff-only  # safely pick up anything newer on GitHub
```

If a push is rejected or something feels off, run `git status` first and read it carefully — don't guess with random Git commands.

## Getting help

Post in the **Help & Questions** board in Canvas with what you tried, the exact command, and the exact error message (paste it, don't paraphrase).
