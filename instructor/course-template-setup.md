# Course Template Repo Setup (web1430-fall26)

How to publish and maintain the starter repo that the WSU repo-creation system (next-crsapps) uses as the template for each student's course repository.

## What and where

- **Source of truth:** `course-template/` in this repo. It contains everything a student repo starts with: root `README.md`, `.gitignore`, `labs/lab00`–`lab13` (starter files pre-seeded for lab00–lab10, README notes for lab11–13), `assignments/`, and `projects/`.
- **Published template:** `https://github.com/web1430-fall26/CourseTemplate` — the name must match the `task=CourseTemplate` parameter in the student request URL.
- **Student request page:** `https://crsapps.netlify.app/gh?instructor=gt&course=WEB1430&task=CourseTemplate` (system source: `https://github.com/aalgahmi/next-crsapps-faculty`).

## First-time publish

Run from your own terminal (the automation sandbox has no GitHub credentials):

```bash
# Work from a copy so the template repo isn't nested inside web1430-26.1
cp -R ~/Documents/GitHub/web1430-26.1/course-template ~/Documents/GitHub/CourseTemplate
cd ~/Documents/GitHub/CourseTemplate

git init -b main
git add .
git commit -m "Initial course template: folder structure and lab starters"

# With GitHub CLI:
gh repo create web1430-fall26/CourseTemplate --private --source . --push
# ...or create an empty repo named CourseTemplate in the web1430-fall26 org on
# github.com, then:
#   git remote add origin https://github.com/web1430-fall26/CourseTemplate.git
#   git push -u origin main
```

Then check the next-crsapps-faculty docs for whether the repo must be flagged as a **Template repository** (repo Settings → check "Template repository") — flag it either way; it costs nothing and GitHub's repo-generation API requires it.

## Updating the template later

Edit the files under `course-template/` here (so the course repo stays the source of truth), then copy the changes to the published repo and push:

```bash
rsync -av --delete --exclude .git ~/Documents/GitHub/web1430-26.1/course-template/ ~/Documents/GitHub/CourseTemplate/
cd ~/Documents/GitHub/CourseTemplate
git add -A && git commit -m "Sync template from course repo" && git push
```

Template changes only affect repos created **after** the change — existing student repos are not updated.

## Keeping starters in sync

`course-template/labs/labXX/` was seeded from `starters/labXX/` (Aug 22, 2026). If a starter file changes in `starters/`, make the same change in `course-template/labs/` (and re-publish) so new repos and the reference copy agree.

## Student-facing instructions

The student flow (request page → username → passcode → Create Repo → accept invitation → clone) is documented in:

- `labs/lab00-local-setup-and-github-workflow.md` (Part 3)
- `lectures/week-00-lecture.md` and `virtual/lectures/week-00-lecture.md` ("Cloning the course starter repo")
- `assignments/github-repo-setup.md`

The passcode is deliberately NOT stored in this repo. It lives only in the **Course Repo Passcode** announcement in the Canvas shell (and in the crsapps faculty configuration). If the passcode changes, update that announcement — the repo docs only point to it, so they need no edit.
