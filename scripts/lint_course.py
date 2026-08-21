#!/usr/bin/env python3
"""Course-source lint: mechanical checks for the synchronization rules.

Encodes the cross-file consistency rules from CONTEXT.md as automated checks:

 1. Relative markdown links resolve to real files
 2. Code fences are balanced in every source file
 3. Rubric tables use the exact four-level header and every cell is filled
 4. Quiz JSON integrity: points == sum of question points == question count,
    and every question has exactly one correct answer
 5. course/quiz-alignment.md question counts match the quiz JSON
 6. Assignment/project Due weeks match course/schedule.md deliverables
 7. instructor/canvas-outcomes.csv matches course/learning_outcomes.md
 8. instructor/canvas-rubrics.csv is up to date with the briefs' rubric tables
 9. Module overviews contain the required sections
10. The retired root syllabus.md has not been reintroduced (course/syllabus.md
    is the single canonical syllabus)
11. Virtual-modality overrides in virtual/ are consistent: every override has a
    base counterpart, keeps the base H1 title (Canvas slug stability), resolves
    links, balances fences, keeps overview deliverables and schedule deliverables
    identical to the base, and virtual module overviews include the Live sessions
    section

Usage:
    python3 scripts/lint_course.py

Exits non-zero if any check fails. Run alongside build --check and validate
before committing course content changes.
"""

from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_canvas_rubrics_csv as rubrics_gen

ROOT = Path(__file__).resolve().parent.parent
VIRTUAL_ROOT = ROOT / "virtual"

SOURCE_DIRS = ("course", "instructor", "textbook", "lectures", "modules",
               "labs", "assignments", "projects")
ROOT_SOURCES = ("home.md", "README.md", "CONTEXT.md", "textbook-table-of-contents.md")

RUBRIC_HEADER = ["Criterion", "Excellent (4)", "Proficient (3)", "Developing (2)", "Incomplete (1)"]

QUIZ_ALIGNMENT_FILES = {
    "Canvas Orientation Quiz": "quiz-0-canvas-orientation.json",
    "Quiz 1": "quiz-1-browser-foundations.json",
    "Quiz 2": "quiz-2-javascript-fundamentals.json",
    "Quiz 3": "quiz-3-arrays-objects-and-json.json",
    "Quiz 4": "quiz-4-dom-events-and-forms.json",
    "Quiz 5": "quiz-5-fetch-and-apis.json",
    "Quiz 6": "quiz-6-storage-and-state.json",
    "Quiz 7": "quiz-7-modules-and-vue-basics.json",
    "Quiz 8": "quiz-8-testing-performance-and-deployment.json",
    "Midterm Exam": "midterm-exam.json",
    "Final Exam": "final-exam.json",
}

MODULE_REQUIRED_SECTIONS = ("## This week", "## Success plan", "## Resources",
                            "**Time estimate:**", "## Checkpoint question")

errors: list[str] = []


def fail(message: str) -> None:
    errors.append(message)


def source_markdown_files() -> list[Path]:
    files = [ROOT / name for name in ROOT_SOURCES if (ROOT / name).exists()]
    for folder in SOURCE_DIRS:
        files.extend(sorted((ROOT / folder).rglob("*.md")))
    return files


def split_row(line: str) -> list[str]:
    parts = re.split(r"(?<!\\)\|", line.strip())
    return [p.strip() for p in parts[1:-1]]


def check_links_and_fences() -> None:
    for path in source_markdown_files():
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT)

        fence_count = sum(1 for line in text.splitlines() if line.strip().startswith("```"))
        if fence_count % 2:
            fail(f"{rel}: unbalanced code fences ({fence_count} fence lines)")

        for match in re.finditer(r"\[([^\]]*)\]\(([^)]+)\)", text):
            href = match.group(2).split("#")[0].strip()
            if not href or href.startswith(("http://", "https://", "mailto:")):
                continue
            target = (path.parent / href).resolve()
            if not target.exists():
                fail(f"{rel}: broken link [{match.group(1)}]({match.group(2)})")


def check_rubric_tables() -> None:
    for folder in ("labs", "assignments", "projects"):
        for path in sorted((ROOT / folder).glob("*.md")):
            rel = path.relative_to(ROOT)
            lines = path.read_text(encoding="utf-8").splitlines()
            for i, line in enumerate(lines):
                if not line.strip().startswith("|"):
                    continue
                cells = split_row(line)
                if cells and cells[0] == "Criterion":
                    if cells != RUBRIC_HEADER:
                        fail(f"{rel}:{i + 1}: rubric header differs from the required "
                             f"four-level format: {cells}")
                    j = i + 2
                    while j < len(lines) and lines[j].strip().startswith("|"):
                        row = split_row(lines[j])
                        if len(row) != 5 or any(not cell for cell in row):
                            fail(f"{rel}:{j + 1}: rubric row has missing or empty cells")
                        j += 1


def check_quiz_json() -> None:
    for path in sorted((ROOT / "quizzes").glob("*.json")):
        rel = path.relative_to(ROOT)
        data = json.loads(path.read_text(encoding="utf-8"))
        questions = data.get("questions", [])
        points = data.get("points")
        total = sum(q.get("points_possible", 0) for q in questions)
        if not (points == total == len(questions)):
            fail(f"{rel}: points={points}, sum={total}, questions={len(questions)} "
                 f"— all three must be equal")
        for idx, question in enumerate(questions, 1):
            correct = [a for a in question.get("answers", []) if a.get("weight", 0) > 0]
            if len(correct) != 1:
                fail(f"{rel}: question {idx} has {len(correct)} correct answers (expected 1)")


def check_quiz_alignment() -> None:
    alignment = (ROOT / "course" / "quiz-alignment.md").read_text(encoding="utf-8")
    for name, filename in QUIZ_ALIGNMENT_FILES.items():
        match = re.search(rf"^\| {re.escape(name)} \|[^|]*\|[^|]*\| (\d+) / (\d+) \|",
                          alignment, re.MULTILINE)
        if not match:
            fail(f"course/quiz-alignment.md: no summary-table row found for {name}")
            continue
        stated = int(match.group(1))
        data = json.loads((ROOT / "quizzes" / filename).read_text(encoding="utf-8"))
        actual = len(data.get("questions", []))
        if stated != actual:
            fail(f"course/quiz-alignment.md: {name} lists {stated} questions "
                 f"but {filename} has {actual}")


def check_due_weeks() -> None:
    schedule = (ROOT / "course" / "schedule.md").read_text(encoding="utf-8")
    week_deliverables: dict[int, str] = {}
    for match in re.finditer(r"^## Week (\d+):.*?(?=^## Week |\Z)", schedule,
                             re.MULTILINE | re.DOTALL):
        block = match.group(0)
        deliverables = re.search(r"^- Deliverables: (.+)$", block, re.MULTILINE)
        week_deliverables[int(match.group(1))] = deliverables.group(1) if deliverables else ""

    for folder in ("assignments", "projects"):
        for path in sorted((ROOT / folder).glob("*.md")):
            rel = path.relative_to(ROOT)
            text = path.read_text(encoding="utf-8")
            title = re.match(r"# (.+)", text)
            due = re.search(r"\*\*Due:\*\* End of Week (\d+)", text)
            if not title or not due:
                fail(f"{rel}: missing H1 title or '**Due:** End of Week N' line")
                continue
            artifact = title.group(1).split(" – ")[0].strip()
            week = int(due.group(1))
            deliverables = week_deliverables.get(week)
            if deliverables is None:
                fail(f"{rel}: due week {week} not present in course/schedule.md")
            elif artifact not in deliverables:
                fail(f"{rel}: '{artifact}' is due Week {week} but is not in that week's "
                     f"schedule deliverables ({deliverables})")


def check_outcomes_csv() -> None:
    outcomes_md = (ROOT / "course" / "learning_outcomes.md").read_text(encoding="utf-8")
    statements = [line[2:].strip() for line in outcomes_md.splitlines()
                  if line.startswith("- ")]
    csv_path = ROOT / "instructor" / "canvas-outcomes.csv"
    with csv_path.open(encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    outcome_rows = [r for r in rows if r.get("object_type") == "outcome"]
    csv_descriptions = [r.get("description", "").strip() for r in outcome_rows]
    if len(outcome_rows) != len(statements):
        fail(f"instructor/canvas-outcomes.csv has {len(outcome_rows)} outcomes but "
             f"course/learning_outcomes.md lists {len(statements)}")
    for statement in statements:
        if statement not in csv_descriptions:
            fail(f"instructor/canvas-outcomes.csv: outcome not found for statement: "
                 f"{statement[:70]}...")


def check_rubrics_csv_fresh() -> None:
    csv_path = ROOT / "instructor" / "canvas-rubrics.csv"
    import io
    expected = io.StringIO()
    writer = csv.writer(expected)
    header = ["Rubric Name", "Criteria Name", "Criteria Description", "Criteria Enable Range"]
    for _ in rubrics_gen.RATING_LEVELS:
        header += ["Rating Name", "Rating Description", "Rating Points"]
    writer.writerow(header)
    for rubric in rubrics_gen.build_rubrics():
        for criterion in rubric.criteria:
            row = [rubric.title, criterion.name, "", "false"]
            for points, label, text in criterion.ratings:
                row += [label, text, points]
            writer.writerow(row)
    if csv_path.read_text(encoding="utf-8").replace("\r\n", "\n") != \
            expected.getvalue().replace("\r\n", "\n"):
        fail("instructor/canvas-rubrics.csv is stale — regenerate with "
             "'python3 scripts/build_canvas_rubrics_csv.py'")


def check_module_overviews() -> None:
    for path in sorted((ROOT / "modules").glob("week-*-overview.md")):
        rel = path.relative_to(ROOT)
        text = path.read_text(encoding="utf-8")
        for section in MODULE_REQUIRED_SECTIONS:
            if section not in text:
                fail(f"{rel}: missing required section '{section}'")


def first_heading(text: str) -> str | None:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return None


def deliverable_lines(text: str) -> list[str]:
    return [line.strip() for line in text.splitlines()
            if line.strip().startswith("- Deliverables:")]


def check_virtual_overrides() -> None:
    if not VIRTUAL_ROOT.exists():
        return
    for path in sorted(VIRTUAL_ROOT.rglob("*.md")):
        rel = path.relative_to(ROOT)
        base_rel = path.relative_to(VIRTUAL_ROOT)
        base = ROOT / base_rel
        text = path.read_text(encoding="utf-8")

        # 1. Every override must shadow a real base source file.
        if not base.exists():
            fail(f"{rel}: orphan override — no base file at {base_rel}")
            continue

        # 2. H1 must match the base so Canvas page slugs and module item titles
        #    stay identical across modalities.
        base_text = base.read_text(encoding="utf-8")
        if first_heading(text) != first_heading(base_text):
            fail(f"{rel}: H1 differs from base {base_rel} — page titles must match "
                 f"across modalities (Canvas slug stability)")

        # 3. Fences balanced; relative links resolve as if the file sat at its
        #    base location (the build resolves override links against the base path).
        fence_count = sum(1 for line in text.splitlines() if line.strip().startswith("```"))
        if fence_count % 2:
            fail(f"{rel}: unbalanced code fences ({fence_count} fence lines)")
        for match in re.finditer(r"\[([^\]]*)\]\(([^)]+)\)", text):
            href = match.group(2).split("#")[0].strip()
            if not href or href.startswith(("http://", "https://", "mailto:")):
                continue
            if not (base.parent / href).resolve().exists():
                fail(f"{rel}: broken link [{match.group(1)}]({match.group(2)}) "
                     f"(resolved from the base location {base_rel})")

        # 4. Deliverables must not drift between modalities.
        if deliverable_lines(text) != deliverable_lines(base_text):
            fail(f"{rel}: '- Deliverables:' lines differ from base {base_rel} — "
                 f"both modalities share due dates")

    # 5. Virtual module overviews keep the required format plus Live sessions.
    virtual_modules = VIRTUAL_ROOT / "modules"
    if virtual_modules.exists():
        for path in sorted(virtual_modules.glob("week-*-overview.md")):
            rel = path.relative_to(ROOT)
            text = path.read_text(encoding="utf-8")
            for section in MODULE_REQUIRED_SECTIONS + ("## Live sessions",):
                if section not in text:
                    fail(f"{rel}: missing required section '{section}'")


def check_single_syllabus() -> None:
    if (ROOT / "syllabus.md").exists():
        fail("root syllabus.md exists — course/syllabus.md is the single canonical "
             "syllabus; delete the root copy")
    if not (ROOT / "course" / "syllabus.md").exists():
        fail("course/syllabus.md is missing")


def main() -> int:
    checks = [
        check_links_and_fences,
        check_rubric_tables,
        check_quiz_json,
        check_quiz_alignment,
        check_due_weeks,
        check_outcomes_csv,
        check_rubrics_csv_fresh,
        check_module_overviews,
        check_single_syllabus,
        check_virtual_overrides,
    ]
    for check in checks:
        check()
    if errors:
        print(f"LINT FAILED — {len(errors)} problem(s):\n")
        for error in errors:
            print(f"  ✗ {error}")
        return 1
    print("Lint passed: links, fences, rubrics, quizzes, alignment, due weeks, "
          "outcomes CSV, rubrics CSV, module format, syllabus, virtual overrides.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
