# Week 00 Studio Notes: Setup Clinic and First Push

## Session focus

Session 1 explained how the course runs and what the toolchain is for. Session 2 makes it run on your machine. Nobody should leave this session without a working editor, a working terminal, and a commit they can see on github.com.

## Before class

- Attempt Lab 00 steps 1–4 on your own first. Getting stuck is fine — getting stuck *before* the studio is what makes the clinic useful.
- Copy the exact text of any error you hit into a note. "It didn't work" cannot be debugged; an error message can.
- Have VS Code and a terminal open, and confirm you can share your screen in Zoom. Debugging someone's setup without seeing it is guesswork.

## Studio plan

1. **Version check (10 min).** Run `node -v`, `npm -v`, `git --version`, and confirm each meets the Lab 00 minimums. Comparing version strings across the room finds the outliers in two minutes instead of two days.
2. **Install triage (15 min).** Work the three failure clusters that account for most setup problems: Windows not finding `node` on the PATH, macOS prompting for the Xcode command line tools, and Git missing `user.name` or `user.email`.
3. **Clone and open (10 min).** Clone the course starter repository and open the folder in VS Code. Confirm your file tree matches everyone else's before going further.
4. **First push, verified (20 min).** Edit one file, then `git add`, `git commit -m`, `git push`. Reload your repository page on github.com and see the change. The verification step is the point: a commit you cannot see on the web has not been submitted.
5. **Recovery drill (10 min).** Deliberately create a "your branch is behind" state, read what `git status` says about it, and fix it with `git pull --ff-only`. You will hit this again; recognizing it costs a minute, guessing at it costs an evening.
6. **Submission walkthrough (10 min).** Where the Lab 00 screenshot goes, how the Welcome Survey and Canvas Orientation Quiz are submitted, and where the Help & Questions board lives.

This plan runs live in the [class Zoom room](https://weber.zoom.us/j/82982068432), Wednesday 9:30–10:45 AM (75 minutes). Screen sharing is how the triage rounds work, so test it before the session — Zoom setup is covered in the Week 00 lecture notes.

## Accessibility connection

Accessible online course design starts with the instructor, but students benefit from understanding it too. Canvas pages use heading structure, alt text on images, and sufficient color contrast — pay attention to how well-structured documents help you navigate faster, because you will apply the same principles to your own HTML pages starting in Week 02. Screen reader users and keyboard-only users depend on that structure.

## Practice prompt

Open VS Code and create a new folder called `week-00-practice` on your Desktop. Inside it, create a file called `notes.txt` and type three things you want to learn in this course. Initialize a Git repository in that folder (`git init`), stage the file, commit it with a descriptive message, and inspect the log with `git log --oneline`. You do not need to push this one — the goal is to practice the local commit cycle without a remote repository.

## Bridge

Completing the GitHub Repo Setup deliverable this week is the prerequisite for every lab in the course — all labs are submitted as pushes to the GitHub repository created for you through the course repo request page. The Canvas Orientation Quiz checks that you can find key course resources; take it after you finish reading through the Modules page so the answers are fresh. If anything in your setup is broken, bring it to Wednesday's setup clinic or post in the Help board now, before Week 01 begins.
