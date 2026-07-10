#!/usr/bin/env python3
"""Generate instructor/canvas-rubrics.csv for Canvas's Import Rubrics feature.

Parses every rubric table in labs/, assignments/, and projects/ and writes a
CSV matching the template Canvas provides under Course > Rubrics > Import
Rubrics: one row per criterion, grouped by rubric name, with repeating
(Rating Name, Rating Description, Rating Points) column triplets in
descending point order (Excellent 4 / Proficient 3 / Developing 2 /
Incomplete 1).

Canvas's CSV import creates course-level rubrics only. Attaching rubrics to
assignments and adding learning-outcome rows are manual steps in the Canvas
UI — see instructor/import_to_canvas.md for the checklist.

Usage:
    python3 scripts/build_canvas_rubrics_csv.py            # writes instructor/canvas-rubrics.csv
    python3 scripts/build_canvas_rubrics_csv.py out.csv    # writes elsewhere

Re-run whenever a rubric table in a brief changes, then delete the affected
rubric in Canvas and re-import the CSV.
"""

from __future__ import annotations

import csv
import re
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_OUTPUT = ROOT / "instructor" / "canvas-rubrics.csv"

RATING_LEVELS = [
    (4, "Excellent"),
    (3, "Proficient"),
    (2, "Developing"),
    (1, "Incomplete"),
]


@dataclass
class Criterion:
    name: str
    ratings: list[tuple[int, str, str]]  # (points, level label, description)


@dataclass
class Rubric:
    title: str
    criteria: list[Criterion]


def strip_markdown(cell: str) -> str:
    cell = re.sub(r"`([^`]*)`", r"\1", cell)
    cell = cell.replace("**", "").replace("\\|", "|")
    return re.sub(r"\s+", " ", cell).strip()


def split_row(line: str) -> list[str]:
    parts = re.split(r"(?<!\\)\|", line.strip())
    return [strip_markdown(p) for p in parts[1:-1]]


def parse_rubric_tables(path: Path) -> list[list[Criterion]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    tables: list[list[Criterion]] = []
    i = 0
    while i < len(lines):
        cells = split_row(lines[i]) if lines[i].strip().startswith("|") else []
        if cells and cells[0] == "Criterion" and any("Excellent" in c for c in cells):
            i += 2  # skip header and separator rows
            criteria: list[Criterion] = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                row = split_row(lines[i])
                if len(row) >= 5 and row[0]:
                    ratings = [
                        (points, label, row[idx + 1] or f"{label} work")
                        for idx, (points, label) in enumerate(RATING_LEVELS)
                    ]
                    criteria.append(Criterion(name=row[0], ratings=ratings))
                i += 1
            if criteria:
                tables.append(criteria)
        else:
            i += 1
    return tables


def heading_text(path: Path) -> str:
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("#"):
            return re.sub(r"^#+\s*", "", line).strip()
    raise ValueError(f"{path} has no H1 heading")


def build_rubrics() -> list[Rubric]:
    rubrics: list[Rubric] = []
    for folder in ("labs", "assignments", "projects"):
        for path in sorted((ROOT / folder).glob("*.md")):
            tables = parse_rubric_tables(path)
            title = heading_text(path) if tables else ""
            for index, criteria in enumerate(tables):
                # The final project brief holds two rubric tables: the project
                # rubric and the course-reflection rubric.
                rubric_title = title if index == 0 else "Final Project – Course Reflection"
                rubrics.append(Rubric(title=rubric_title, criteria=criteria))
    return rubrics


def write_csv(rubrics: list[Rubric], path: Path) -> None:
    header = ["Rubric Name", "Criteria Name", "Criteria Description", "Criteria Enable Range"]
    for _ in RATING_LEVELS:
        header += ["Rating Name", "Rating Description", "Rating Points"]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(header)
        for rubric in rubrics:
            for criterion in rubric.criteria:
                row = [rubric.title, criterion.name, "", "false"]
                for points, label, text in criterion.ratings:
                    row += [label, text, points]
                writer.writerow(row)


def main(argv: list[str]) -> int:
    output = Path(argv[0]) if argv else DEFAULT_OUTPUT
    rubrics = build_rubrics()
    write_csv(rubrics, output)
    criteria_count = sum(len(r.criteria) for r in rubrics)
    print(f"Wrote {len(rubrics)} rubrics ({criteria_count} criteria) to {output}")
    print("Upload via Course > Rubrics > Import Rubrics, then follow the manual "
          "attach/outcome checklist in instructor/import_to_canvas.md.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
