#!/usr/bin/env python3
"""Build and validate the Canvas package from the markdown source files."""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import os
import re
import sys
import zipfile
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parent.parent
EXPANDED_PACKAGE = ROOT / "canvas" / "expanded_package"
IMSCC_PATH = ROOT / "canvas" / "WEB1430-Canvas-Export.imscc"
MANIFEST_PATH = EXPANDED_PACKAGE / "imsmanifest.xml"
MODULE_META_PATH = EXPANDED_PACKAGE / "course_settings" / "module_meta.xml"
COURSE_SYLLABUS_PATH = EXPANDED_PACKAGE / "course_settings" / "syllabus.html"

IMS_NS = "http://www.imsglobal.org/xsd/imsccv1p1/imscp_v1p1"
LOM_NS = "http://ltsc.ieee.org/xsd/imsccv1p1/LOM/manifest"
CANVAS_NS = "http://canvas.instructure.com/xsd/cccv1p0"
QTI_NS = "http://www.imsglobal.org/xsd/ims_qtiasiv1p2"
XSI_NS = "http://www.w3.org/2001/XMLSchema-instance"

ET.register_namespace("", IMS_NS)
ET.register_namespace("lomimscc", LOM_NS)
ET.register_namespace("xsi", XSI_NS)

NS = {"im": IMS_NS, "c": CANVAS_NS}

PUBLISHED_COURSE_GUIDES = (
    ROOT / "course" / "accessibility-fundamentals-primer.md",
    ROOT / "course" / "api-troubleshooting-guide.md",
    ROOT / "course" / "course-reflection-prompt.md",
    ROOT / "course" / "screen-reader-testing-guide.md",
    ROOT / "course" / "student-survey-week-05.md",
    ROOT / "course" / "student-survey-week-11.md",
    ROOT / "course" / "student-survey-week-13.md",
)

FIXED_ZIP_TIMESTAMP = (2026, 3, 13, 0, 0, 0)


def qname(namespace: str, tag: str) -> str:
    return f"{{{namespace}}}{tag}"


def stable_id(seed: str) -> str:
    return f"i{hashlib.md5(seed.encode('utf-8')).hexdigest()}"


def normalize_text(text: str) -> str:
    return text.replace("\r\n", "\n").replace("\r", "\n")


def write_text_if_changed(path: Path, content: str, dry_run: bool) -> bool:
    existing = path.read_text(encoding="utf-8") if path.exists() else None
    if existing == content:
        return False
    if not dry_run:
        path.write_text(content, encoding="utf-8")
    return True


def write_bytes_if_changed(path: Path, content: bytes, dry_run: bool) -> bool:
    existing = path.read_bytes() if path.exists() else None
    if existing == content:
        return False
    if not dry_run:
        path.write_bytes(content)
    return True


def heading_text(markdown_text: str) -> str:
    for line in markdown_text.splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            text = re.sub(r"^#+\s*", "", stripped)
            text = re.sub(r"`([^`]+)`", r"\1", text)
            text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
            text = text.replace("**", "").replace("*", "")
            return text.strip()
    raise ValueError("Markdown file is missing an H1 heading.")


@dataclass(frozen=True)
class WikiPageSpec:
    source: Path
    href: str
    include_in_manifest: bool = True
    front_page: bool = False


@dataclass(frozen=True)
class AssignmentBodySpec:
    source: Path
    output_path: Path


@dataclass(frozen=True)
class AssessmentSpec:
    source: Path
    title: str
    resource_id: str
    assignment_id: str
    assignment_group_id: str
    position: str


class MarkdownRenderer:
    def __init__(self, published_sources: dict[Path, Path]):
        self.published_sources = published_sources

    def render(self, markdown_text: str, source_path: Path, output_path: Path) -> str:
        lines = normalize_text(markdown_text).split("\n")
        blocks: list[str] = []
        i = 0
        while i < len(lines):
            line = lines[i]
            stripped = line.strip()

            if not stripped:
                i += 1
                continue

            if stripped.startswith("```"):
                block, i = self._render_code_block(lines, i)
                blocks.append(block)
                continue

            if self._looks_like_table(lines, i):
                block, i = self._render_table(lines, i, source_path, output_path)
                blocks.append(block)
                continue

            heading_match = re.match(r"^(#{1,6})\s+(.*)$", stripped)
            if heading_match:
                level = len(heading_match.group(1))
                content = self._render_inline(
                    heading_match.group(2), source_path, output_path
                )
                blocks.append(f"<h{level}>{content}</h{level}>")
                i += 1
                continue

            if re.match(r"^-{3,}\s*$", stripped):
                blocks.append("<hr />")
                i += 1
                continue

            if stripped.startswith(">"):
                block, i = self._render_blockquote(lines, i, source_path, output_path)
                blocks.append(block)
                continue

            if re.match(r"^\s*[-*]\s+", line):
                block, i = self._render_list(
                    lines, i, ordered=False, source_path=source_path, output_path=output_path
                )
                blocks.append(block)
                continue

            if re.match(r"^\s*\d+\.\s+", line):
                block, i = self._render_list(
                    lines, i, ordered=True, source_path=source_path, output_path=output_path
                )
                blocks.append(block)
                continue

            block, i = self._render_paragraph(lines, i, source_path, output_path)
            blocks.append(block)

        return "\n".join(blocks)

    def _render_code_block(self, lines: list[str], index: int) -> tuple[str, int]:
        opener = lines[index].strip()
        language = opener[3:].strip()
        code_lines: list[str] = []
        index += 1
        while index < len(lines) and not lines[index].strip().startswith("```"):
            code_lines.append(lines[index])
            index += 1
        if index < len(lines):
            index += 1
        class_attr = f' class="language-{html.escape(language, quote=True)}"' if language else ""
        code = html.escape("\n".join(code_lines))
        return f"<pre><code{class_attr}>{code}</code></pre>", index

    def _render_table(
        self, lines: list[str], index: int, source_path: Path, output_path: Path
    ) -> tuple[str, int]:
        header_cells = self._split_table_row(lines[index])
        index += 2  # skip separator row
        body_rows: list[list[str]] = []
        while index < len(lines):
            line = lines[index].strip()
            if not line or "|" not in line or self._is_table_separator(line):
                break
            body_rows.append(self._split_table_row(lines[index]))
            index += 1

        header_html = "".join(
            f"<th>{self._render_inline(cell, source_path, output_path)}</th>"
            for cell in header_cells
        )
        row_html: list[str] = []
        for row in body_rows:
            if len(row) < len(header_cells):
                row = row + [""] * (len(header_cells) - len(row))
            elif len(row) > len(header_cells):
                row = row[: len(header_cells)]
            cells = "".join(
                f"<td>{self._render_inline(cell, source_path, output_path)}</td>"
                for cell in row
            )
            row_html.append(f"<tr>{cells}</tr>")

        table_html = ["<table>", f"<thead><tr>{header_html}</tr></thead>"]
        if row_html:
            table_html.append("<tbody>")
            table_html.extend(row_html)
            table_html.append("</tbody>")
        table_html.append("</table>")
        return "\n".join(table_html), index

    def _render_blockquote(
        self, lines: list[str], index: int, source_path: Path, output_path: Path
    ) -> tuple[str, int]:
        quote_lines: list[str] = []
        while index < len(lines):
            stripped = lines[index].strip()
            if not stripped.startswith(">"):
                break
            quote_lines.append(re.sub(r"^>\s?", "", stripped))
            index += 1
        inner = self.render("\n".join(quote_lines), source_path, output_path)
        return f"<blockquote>\n{inner}\n</blockquote>", index

    def _render_list(
        self,
        lines: list[str],
        index: int,
        *,
        ordered: bool,
        source_path: Path,
        output_path: Path,
    ) -> tuple[str, int]:
        items: list[str] = []
        bullet_re = re.compile(r"^\s*[-*]\s+(.*)$")
        ordered_re = re.compile(r"^\s*\d+\.\s+(.*)$")
        matcher = ordered_re if ordered else bullet_re

        while index < len(lines):
            match = matcher.match(lines[index])
            if not match:
                break

            item_lines = [match.group(1).strip()]
            index += 1
            while index < len(lines):
                continuation = lines[index]
                if not continuation.strip():
                    break
                if bullet_re.match(continuation) or ordered_re.match(continuation):
                    break
                if re.match(r"^(#{1,6})\s+", continuation.strip()):
                    break
                if continuation.strip().startswith(">"):
                    break
                if self._looks_like_table(lines, index):
                    break
                if continuation.strip().startswith("```"):
                    break
                if re.match(r"^-{3,}\s*$", continuation.strip()):
                    break
                item_lines.append(continuation.strip())
                index += 1

            item_text = " ".join(part for part in item_lines if part).strip()
            items.append(
                f"<li>{self._render_inline(item_text, source_path, output_path)}</li>"
            )

            while index < len(lines) and not lines[index].strip():
                index += 1
                break

        tag = "ol" if ordered else "ul"
        return f"<{tag}>\n" + "\n".join(items) + f"\n</{tag}>", index

    def _render_paragraph(
        self, lines: list[str], index: int, source_path: Path, output_path: Path
    ) -> tuple[str, int]:
        parts: list[str] = []
        while index < len(lines):
            stripped = lines[index].strip()
            if not stripped:
                break
            if stripped.startswith("```"):
                break
            if stripped.startswith(">"):
                break
            if re.match(r"^(#{1,6})\s+", stripped):
                break
            if re.match(r"^\s*[-*]\s+", lines[index]) or re.match(
                r"^\s*\d+\.\s+", lines[index]
            ):
                break
            if self._looks_like_table(lines, index):
                break
            if re.match(r"^-{3,}\s*$", stripped):
                break
            parts.append(stripped)
            index += 1

        if len(parts) > 1 and all(part.startswith("**") for part in parts):
            rendered = "<br />\n".join(
                self._render_inline(part, source_path, output_path) for part in parts
            )
            return f"<p>{rendered}</p>", index

        paragraph = " ".join(parts)
        return f"<p>{self._render_inline(paragraph, source_path, output_path)}</p>", index

    def _render_inline(
        self,
        text: str,
        source_path: Path,
        output_path: Path,
        *,
        allow_links: bool = True,
    ) -> str:
        placeholders: list[str] = []

        def stash(fragment: str) -> str:
            token = f"@@PLACEHOLDER{len(placeholders)}@@"
            placeholders.append(fragment)
            return token

        text = re.sub(
            r"`([^`]+)`",
            lambda match: stash(f"<code>{html.escape(match.group(1))}</code>"),
            text,
        )

        if allow_links:
            link_pattern = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")

            def replace_link(match: re.Match[str]) -> str:
                label = self._render_inline(
                    match.group(1),
                    source_path,
                    output_path,
                    allow_links=False,
                )
                href = match.group(2).strip()
                link_html = self._build_link(label, href, source_path, output_path)
                return stash(link_html if link_html is not None else label)

            text = link_pattern.sub(replace_link, text)

        text = html.escape(text, quote=False)
        text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
        text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", text)

        for idx, fragment in enumerate(placeholders):
            text = text.replace(f"@@PLACEHOLDER{idx}@@", fragment)

        return text

    def _build_link(
        self, label_html: str, href: str, source_path: Path, output_path: Path
    ) -> str | None:
        if href.startswith(("http://", "https://", "mailto:", "#")):
            safe_href = html.escape(href, quote=True)
            return f'<a href="{safe_href}">{label_html}</a>'

        target, _hash, _fragment = href.partition("#")
        resolved = (source_path.parent / target).resolve()
        published = self.published_sources.get(resolved)
        if published is None:
            return None

        relative_href = os.path.relpath(published, output_path.parent).replace(os.sep, "/")
        safe_href = html.escape(relative_href, quote=True)
        return f'<a href="{safe_href}">{label_html}</a>'

    @staticmethod
    def _looks_like_table(lines: list[str], index: int) -> bool:
        if index + 1 >= len(lines):
            return False
        first = lines[index].strip()
        second = lines[index + 1].strip()
        return "|" in first and MarkdownRenderer._is_table_separator(second)

    @staticmethod
    def _is_table_separator(line: str) -> bool:
        return bool(re.match(r"^\|?[\s:-]+(\|[\s:-]+)+\|?$", line))

    @staticmethod
    def _split_table_row(line: str) -> list[str]:
        stripped = line.strip().strip("|")
        return [cell.strip() for cell in stripped.split("|")]


def wrap_html_page(
    title: str,
    body_html: str,
    *,
    identifier: str | None = None,
    front_page: bool = False,
    include_workflow_state: bool = True,
    assignment_title: bool = False,
) -> str:
    title_text = f"Assignment: {title}" if assignment_title else title
    head = [
        "<html>",
        "<head>",
        '<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>',
        f"<title>{html.escape(title_text)}</title>",
    ]
    if identifier is not None:
        head.append(f'<meta name="identifier" content="{html.escape(identifier)}"/>')
    if front_page:
        head.append('<meta name="front_page" content="true"/>')
    if include_workflow_state:
        head.append('<meta name="workflow_state" content="active"/>')
    head.extend(["</head>", "<body>", body_html, "</body>", "</html>"])
    return "\n".join(head) + "\n"


def xml_bytes(root: ET.Element, namespace: str | None = None) -> bytes:
    if namespace is not None:
        ET.register_namespace("", namespace)
        ET.register_namespace("xsi", XSI_NS)
    return ET.tostring(root, encoding="utf-8", xml_declaration=True)


def assessment_specs(manifest_root: ET.Element) -> list[AssessmentSpec]:
    resources = manifest_root.find("im:resources", NS)
    assert resources is not None

    existing_by_title: dict[str, AssessmentSpec] = {}
    for resource in resources.findall("im:resource", NS):
        href = resource.get("href", "")
        if not href.endswith("/assessment_meta.xml"):
            continue
        resource_id = Path(href).parts[0]
        meta_path = EXPANDED_PACKAGE / href
        meta_root = ET.parse(meta_path).getroot()
        title = meta_root.find("c:title", NS)
        assignment = meta_root.find("c:assignment", NS)
        if title is None or assignment is None:
            raise ValueError(f"Assessment metadata is incomplete for {href}")
        group_id = assignment.find("c:assignment_group_identifierref", NS)
        position = assignment.find("c:position", NS)
        if group_id is None or position is None or assignment.get("identifier") is None:
            raise ValueError(f"Assessment assignment metadata is incomplete for {href}")
        existing_by_title[title.text] = AssessmentSpec(
            source=Path(),
            title=title.text,
            resource_id=resource_id,
            assignment_id=assignment.get("identifier", ""),
            assignment_group_id=group_id.text or "",
            position=position.text or "1",
        )

    specs: list[AssessmentSpec] = []
    for source in sorted((ROOT / "quizzes").glob("*.json")):
        data = json.loads(source.read_text(encoding="utf-8"))
        title = data.get("title")
        if title not in existing_by_title:
            raise ValueError(f"Assessment resource missing for quiz source {source.relative_to(ROOT)}")
        existing = existing_by_title[title]
        specs.append(
            AssessmentSpec(
                source=source,
                title=existing.title,
                resource_id=existing.resource_id,
                assignment_id=existing.assignment_id,
                assignment_group_id=existing.assignment_group_id,
                position=existing.position,
            )
        )

    return specs


def qti_item_profile(question_type: str) -> str:
    if question_type == "multiple_choice_question":
        return "cc.multiple_choice.v0p1"
    if question_type == "true_false_question":
        return "cc.true_false.v0p1"
    raise ValueError(f"Unsupported question type: {question_type}")


def build_assessment_meta(spec: AssessmentSpec, data: dict) -> ET.Element:
    root = ET.Element(
        qname(CANVAS_NS, "quiz"),
        {
            "identifier": spec.resource_id,
            qname(XSI_NS, "schemaLocation"): (
                f"{CANVAS_NS} https://canvas.instructure.com/xsd/cccv1p0.xsd"
            ),
        },
    )
    ET.SubElement(root, qname(CANVAS_NS, "title")).text = data["title"]
    ET.SubElement(
        root, qname(CANVAS_NS, "description")
    ).text = f"This assessment checks understanding for {data['title']}."
    ET.SubElement(root, qname(CANVAS_NS, "shuffle_answers")).text = "false"
    ET.SubElement(root, qname(CANVAS_NS, "scoring_policy")).text = "keep_highest"
    ET.SubElement(root, qname(CANVAS_NS, "hide_results"))
    ET.SubElement(root, qname(CANVAS_NS, "quiz_type")).text = "assignment"
    ET.SubElement(root, qname(CANVAS_NS, "points_possible")).text = str(data["points"])
    ET.SubElement(root, qname(CANVAS_NS, "show_correct_answers")).text = "true"
    ET.SubElement(root, qname(CANVAS_NS, "allowed_attempts")).text = "1"
    ET.SubElement(root, qname(CANVAS_NS, "one_question_at_a_time")).text = "false"
    ET.SubElement(root, qname(CANVAS_NS, "cant_go_back")).text = "false"
    ET.SubElement(root, qname(CANVAS_NS, "available")).text = "false"
    ET.SubElement(root, qname(CANVAS_NS, "one_time_results")).text = "false"

    assignment = ET.SubElement(
        root, qname(CANVAS_NS, "assignment"), {"identifier": spec.assignment_id}
    )
    ET.SubElement(assignment, qname(CANVAS_NS, "title")).text = data["title"]
    ET.SubElement(
        assignment, qname(CANVAS_NS, "assignment_group_identifierref")
    ).text = spec.assignment_group_id
    ET.SubElement(assignment, qname(CANVAS_NS, "workflow_state")).text = "published"
    ET.SubElement(assignment, qname(CANVAS_NS, "points_possible")).text = str(data["points"])
    ET.SubElement(assignment, qname(CANVAS_NS, "grading_type")).text = "points"
    ET.SubElement(assignment, qname(CANVAS_NS, "submission_types")).text = "online_quiz"
    ET.SubElement(assignment, qname(CANVAS_NS, "position")).text = spec.position
    ET.SubElement(assignment, qname(CANVAS_NS, "only_visible_to_overrides")).text = "false"
    ET.SubElement(root, qname(CANVAS_NS, "assignment_group_identifierref")).text = (
        spec.assignment_group_id
    )
    return root


def qti_question_identifier(assessment_id: str, question: dict) -> str:
    return stable_id(
        f"{assessment_id}:{question['name']}:{question['question_text']}:{question.get('question_type')}"
    )


def build_assessment_qti(spec: AssessmentSpec, data: dict, *, non_cc: bool) -> ET.Element:
    schema_location = (
        "http://www.imsglobal.org/xsd/ims_qtiasiv1p2p1.xsd"
        if non_cc
        else "http://www.imsglobal.org/profile/cc/ccv1p1/ccv1p1_qtiasiv1p2p1_v1p0.xsd"
    )
    root = ET.Element(
        qname(QTI_NS, "questestinterop"),
        {qname(XSI_NS, "schemaLocation"): f"{QTI_NS} {schema_location}"},
    )
    assessment = ET.SubElement(
        root,
        qname(QTI_NS, "assessment"),
        {"ident": spec.resource_id, "title": data["title"]},
    )
    qti_metadata = ET.SubElement(assessment, qname(QTI_NS, "qtimetadata"))
    metadata_fields = (
        [("cc_maxattempts", "1")]
        if non_cc
        else [
            ("cc_profile", "cc.exam.v0p1"),
            ("qmd_assessmenttype", "Examination"),
            ("qmd_scoretype", "Percentage"),
            ("cc_maxattempts", "1"),
        ]
    )
    for label, value in metadata_fields:
        field = ET.SubElement(qti_metadata, qname(QTI_NS, "qtimetadatafield"))
        ET.SubElement(field, qname(QTI_NS, "fieldlabel")).text = label
        ET.SubElement(field, qname(QTI_NS, "fieldentry")).text = value

    section = ET.SubElement(assessment, qname(QTI_NS, "section"), {"ident": "root_section"})
    for question in data["questions"]:
        question_type = question.get("question_type")
        answers = question.get("answers", [])
        if question_type not in {"multiple_choice_question", "true_false_question"}:
            raise ValueError(
                f"Unsupported question type in {spec.source.relative_to(ROOT)}: {question_type}"
            )
        if not answers:
            raise ValueError(f"Question '{question['name']}' in {spec.source.relative_to(ROOT)} has no answers")
        correct_answers = [answer["id"] for answer in answers if answer.get("weight") == 100]
        if len(correct_answers) != 1:
            raise ValueError(
                f"Question '{question['name']}' in {spec.source.relative_to(ROOT)} must have exactly one correct answer"
            )

        item = ET.SubElement(
            section,
            qname(QTI_NS, "item"),
            {"ident": qti_question_identifier(spec.resource_id, question), "title": question["name"]},
        )
        item_metadata = ET.SubElement(item, qname(QTI_NS, "itemmetadata"))
        qti_item_metadata = ET.SubElement(item_metadata, qname(QTI_NS, "qtimetadata"))

        if non_cc:
            item_fields = [
                ("question_type", question_type),
                ("points_possible", str(question.get("points_possible", 0))),
                ("original_answer_ids", ",".join(answer["id"] for answer in answers)),
            ]
        else:
            item_fields = [("cc_profile", qti_item_profile(question_type))]

        for label, value in item_fields:
            field = ET.SubElement(qti_item_metadata, qname(QTI_NS, "qtimetadatafield"))
            ET.SubElement(field, qname(QTI_NS, "fieldlabel")).text = label
            ET.SubElement(field, qname(QTI_NS, "fieldentry")).text = value

        presentation = ET.SubElement(item, qname(QTI_NS, "presentation"))
        material = ET.SubElement(presentation, qname(QTI_NS, "material"))
        ET.SubElement(material, qname(QTI_NS, "mattext"), {"texttype": "text/html"}).text = question[
            "question_text"
        ]
        response = ET.SubElement(
            presentation, qname(QTI_NS, "response_lid"), {"ident": "response1", "rcardinality": "Single"}
        )
        render_choice = ET.SubElement(response, qname(QTI_NS, "render_choice"))
        for answer in answers:
            label = ET.SubElement(
                render_choice, qname(QTI_NS, "response_label"), {"ident": answer["id"]}
            )
            answer_material = ET.SubElement(label, qname(QTI_NS, "material"))
            ET.SubElement(
                answer_material, qname(QTI_NS, "mattext"), {"texttype": "text/html"}
            ).text = answer.get("html") or f"<p>{html.escape(answer['text'])}</p>"

        resprocessing = ET.SubElement(item, qname(QTI_NS, "resprocessing"))
        outcomes = ET.SubElement(resprocessing, qname(QTI_NS, "outcomes"))
        ET.SubElement(
            outcomes,
            qname(QTI_NS, "decvar"),
            {"maxvalue": "100", "minvalue": "0", "varname": "SCORE", "vartype": "Decimal"},
        )
        respcondition = ET.SubElement(
            resprocessing, qname(QTI_NS, "respcondition"), {"continue": "No"}
        )
        condition = ET.SubElement(respcondition, qname(QTI_NS, "conditionvar"))
        ET.SubElement(condition, qname(QTI_NS, "varequal"), {"respident": "response1"}).text = (
            correct_answers[0]
        )
        ET.SubElement(
            respcondition, qname(QTI_NS, "setvar"), {"action": "Set", "varname": "SCORE"}
        ).text = "100"

    return root


def publishable_wiki_specs() -> list[WikiPageSpec]:
    specs: list[WikiPageSpec] = [
        WikiPageSpec(ROOT / "home.md", "wiki_content/home.html", front_page=True),
        WikiPageSpec(ROOT / "course" / "syllabus.md", "wiki_content/syllabus.html"),
        WikiPageSpec(
            ROOT / "textbook-table-of-contents.md",
            "wiki_content/textbook-table-of-contents.html",
        ),
    ]
    for folder in (
        ROOT / "textbook" / "chapters",
        ROOT / "lectures",
        ROOT / "modules",
        ROOT / "labs",
        ROOT / "assignments",
        ROOT / "projects",
    ):
        for source in sorted(folder.glob("*.md")):
            specs.append(WikiPageSpec(source, f"wiki_content/{source.stem}.html"))
    for source in PUBLISHED_COURSE_GUIDES:
        specs.append(WikiPageSpec(source, f"wiki_content/{source.stem}.html"))
    return specs


def parse_manifest(manifest_path: Path) -> ET.ElementTree:
    return ET.parse(manifest_path)


def existing_manifest_resources(manifest_root: ET.Element) -> dict[str, ET.Element]:
    resources = manifest_root.find("im:resources", NS)
    assert resources is not None
    mapping: dict[str, ET.Element] = {}
    for resource in resources.findall("im:resource", NS):
        href = resource.get("href")
        if href:
            mapping[href] = resource
    return mapping


def assignment_body_specs(manifest_root: ET.Element) -> list[AssignmentBodySpec]:
    resources = manifest_root.find("im:resources", NS)
    assert resources is not None
    specs: list[AssignmentBodySpec] = []
    source_lookup = {spec.source.stem: spec.source for spec in publishable_wiki_specs()}

    for resource in resources.findall("im:resource", NS):
        href = resource.get("href", "")
        if not href.endswith(".html") or href.startswith("wiki_content/"):
            continue
        files = [element.get("href", "") for element in resource.findall("im:file", NS)]
        if not any(file_name.endswith("assignment_settings.xml") for file_name in files):
            continue
        basename = Path(href).stem
        source = source_lookup.get(basename)
        if source is None:
            continue
        specs.append(AssignmentBodySpec(source=source, output_path=EXPANDED_PACKAGE / href))

    return sorted(specs, key=lambda spec: spec.output_path.as_posix())


def ensure_wiki_resource(manifest_root: ET.Element, href: str) -> str:
    resources = manifest_root.find("im:resources", NS)
    assert resources is not None

    for resource in resources.findall("im:resource", NS):
        if resource.get("href") == href:
            identifier = resource.get("identifier")
            assert identifier is not None
            return identifier

    identifier = stable_id(f"resource:{href}")
    resource = ET.SubElement(
        resources,
        qname(IMS_NS, "resource"),
        {"identifier": identifier, "type": "webcontent", "href": href},
    )
    ET.SubElement(resource, qname(IMS_NS, "file"), {"href": href})
    return identifier


def build_published_source_map(manifest_root: ET.Element) -> tuple[list[WikiPageSpec], dict[Path, Path]]:
    specs = publishable_wiki_specs()
    published: dict[Path, Path] = {}
    for spec in specs:
        ensure_wiki_resource(manifest_root, spec.href)
        published[spec.source.resolve()] = EXPANDED_PACKAGE / spec.href
    return specs, published


def synchronize_module_item_order(
    manifest_root: ET.Element,
    module_meta_root: ET.Element,
    *,
    module_title: str,
    expected_items: list[tuple[str, str, str]],
) -> None:
    learning_modules = manifest_root.find(
        "im:organizations/im:organization/im:item[@identifier='LearningModules']",
        NS,
    )
    if learning_modules is None:
        raise ValueError("LearningModules container not found in imsmanifest.xml")

    manifest_module = None
    for child in learning_modules.findall("im:item", NS):
        title_el = child.find("im:title", NS)
        if title_el is not None and title_el.text == module_title:
            manifest_module = child
            break
    if manifest_module is None:
        raise ValueError(f"Module '{module_title}' not found in imsmanifest.xml")

    existing_org_items = {
        item.find("im:title", NS).text: item
        for item in manifest_module.findall("im:item", NS)
        if item.find("im:title", NS) is not None
    }
    title_el = manifest_module.find("im:title", NS)
    assert title_el is not None
    manifest_module[:] = [title_el]
    for content_type, title, identifierref in expected_items:
        existing = existing_org_items.get(title)
        identifier = (
            existing.get("identifier")
            if existing is not None and existing.get("identifier")
            else stable_id(f"org:{module_title}:{title}")
        )
        item = ET.Element(
            qname(IMS_NS, "item"),
            {"identifier": identifier, "identifierref": identifierref},
        )
        ET.SubElement(item, qname(IMS_NS, "title")).text = title
        manifest_module.append(item)

    module = None
    for candidate in module_meta_root.findall("c:module", NS):
        title_candidate = candidate.find("c:title", NS)
        if title_candidate is not None and title_candidate.text == module_title:
            module = candidate
            break
    if module is None:
        raise ValueError(f"Module '{module_title}' not found in module_meta.xml")

    items_el = module.find("c:items", NS)
    if items_el is None:
        raise ValueError(f"Module '{module_title}' is missing its items container")

    existing_canvas_items = {
        item.find("c:title", NS).text: item
        for item in items_el.findall("c:item", NS)
        if item.find("c:title", NS) is not None
    }
    items_el[:] = []
    for position, (content_type, title, identifierref) in enumerate(expected_items, start=1):
        existing = existing_canvas_items.get(title)
        identifier = (
            existing.get("identifier")
            if existing is not None and existing.get("identifier")
            else stable_id(f"module_meta:{module_title}:{title}")
        )
        item = ET.Element(qname(CANVAS_NS, "item"), {"identifier": identifier})
        ET.SubElement(item, qname(CANVAS_NS, "content_type")).text = content_type
        ET.SubElement(item, qname(CANVAS_NS, "title")).text = title
        ET.SubElement(item, qname(CANVAS_NS, "identifierref")).text = identifierref
        ET.SubElement(item, qname(CANVAS_NS, "position")).text = str(position)
        ET.SubElement(item, qname(CANVAS_NS, "new_tab")).text = "false"
        ET.SubElement(item, qname(CANVAS_NS, "indent")).text = "0"
        items_el.append(item)


def expected_module_item_data(
    resource_ids: dict[str, str],
) -> dict[str, list[tuple[str, str, str]]]:
    return {
        "Module 13 – Framework Forms and Data Flow": [
            ("WikiPage", "Week 13 Overview", resource_ids["wiki_content/week-13-overview.html"]),
            ("WikiPage", "Week 13 Lecture Notes", resource_ids["wiki_content/week-13-lecture.html"]),
            (
                "WikiPage",
                "Chapter 13 – Accessibility Synthesis",
                resource_ids["wiki_content/chapter-13-accessibility-synthesis.html"],
            ),
            (
                "WikiPage",
                "Lab 12 – Small Data Dashboard",
                resource_ids["wiki_content/lab12-small-data-dashboard.html"],
            ),
            (
                "Assignment",
                "Assignment 6 – Reactive Form Workflow",
                "ib6d40158db1c506caccd4fbc873fc6f1",
            ),
        ],
        "Module 14 – Testing, Performance, and Deployment": [
            ("WikiPage", "Week 14 Overview", resource_ids["wiki_content/week-14-overview.html"]),
            ("WikiPage", "Week 14 Lecture Notes", resource_ids["wiki_content/week-14-lecture.html"]),
            (
                "WikiPage",
                "Chapter 14 – Performance, Testing, and Deployment",
                resource_ids["wiki_content/chapter-14-performance-testing-and-deployment.html"],
            ),
            (
                "WikiPage",
                "Lab 13 – Lighthouse, Accessibility, and Deployment",
                resource_ids["wiki_content/lab13-lighthouse-accessibility-and-deployment.html"],
            ),
            (
                "Quizzes::Quiz",
                "Quiz 8 – Testing, Performance, and Deployment",
                "iedff68894b1bc54511d86aa7dcc61cbf",
            ),
            (
                "Assignment",
                "Project 2 – Data-Driven Micro-App",
                "iad35047f229caf4f166eaca9b5aceab3",
            ),
        ],
    }


def create_expected_file_outputs() -> tuple[dict[Path, str], dict[Path, bytes]]:
    manifest_tree = parse_manifest(MANIFEST_PATH)
    manifest_root = manifest_tree.getroot()

    wiki_specs, published_sources = build_published_source_map(manifest_root)
    assessment_source_specs = assessment_specs(manifest_root)
    resource_ids = {
        spec.href: existing_manifest_resources(manifest_root)[spec.href].get("identifier", "")
        for spec in wiki_specs
    }

    module_meta_tree = ET.parse(MODULE_META_PATH)
    module_meta_root = module_meta_tree.getroot()
    for module_title, items in expected_module_item_data(resource_ids).items():
        synchronize_module_item_order(
            manifest_root,
            module_meta_root,
            module_title=module_title,
            expected_items=items,
        )

    renderer = MarkdownRenderer(published_sources)
    expected_text_files: dict[Path, str] = {}
    expected_binary_files: dict[Path, bytes] = {}

    for spec in wiki_specs:
        source_text = spec.source.read_text(encoding="utf-8")
        title = heading_text(source_text)
        body = renderer.render(source_text, spec.source.resolve(), EXPANDED_PACKAGE / spec.href)
        html_page = wrap_html_page(
            title,
            body,
            identifier=resource_ids[spec.href],
            front_page=spec.front_page,
        )
        expected_text_files[EXPANDED_PACKAGE / spec.href] = html_page

    for spec in assignment_body_specs(manifest_root):
        source_text = spec.source.read_text(encoding="utf-8")
        title = heading_text(source_text)
        body = renderer.render(source_text, spec.source.resolve(), spec.output_path)
        html_page = wrap_html_page(
            title,
            body,
            include_workflow_state=False,
            assignment_title=True,
        )
        expected_text_files[spec.output_path] = html_page

    syllabus_source = ROOT / "course" / "syllabus.md"
    syllabus_text = syllabus_source.read_text(encoding="utf-8")
    syllabus_title = heading_text(syllabus_text)
    syllabus_body = renderer.render(syllabus_text, syllabus_source.resolve(), COURSE_SYLLABUS_PATH)
    expected_text_files[COURSE_SYLLABUS_PATH] = wrap_html_page(
        syllabus_title,
        syllabus_body,
        include_workflow_state=False,
    )

    for spec in assessment_source_specs:
        data = json.loads(spec.source.read_text(encoding="utf-8"))
        meta_root = build_assessment_meta(spec, data)
        expected_binary_files[EXPANDED_PACKAGE / spec.resource_id / "assessment_meta.xml"] = xml_bytes(
            meta_root, CANVAS_NS
        )
        resource_qti_root = build_assessment_qti(spec, data, non_cc=False)
        expected_binary_files[EXPANDED_PACKAGE / spec.resource_id / "assessment_qti.xml"] = xml_bytes(
            resource_qti_root, QTI_NS
        )
        non_cc_qti_root = build_assessment_qti(spec, data, non_cc=True)
        expected_binary_files[
            EXPANDED_PACKAGE / "non_cc_assessments" / f"{spec.resource_id}.xml.qti"
        ] = xml_bytes(non_cc_qti_root, QTI_NS)

    expected_binary_files[MANIFEST_PATH] = xml_bytes(manifest_root, IMS_NS)
    ET.register_namespace("", CANVAS_NS)
    ET.register_namespace("xsi", XSI_NS)
    expected_binary_files[MODULE_META_PATH] = xml_bytes(module_meta_root, CANVAS_NS)

    return expected_text_files, expected_binary_files


def build_imscc_bytes() -> bytes:
    from io import BytesIO

    buffer = BytesIO()
    with zipfile.ZipFile(buffer, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(EXPANDED_PACKAGE.rglob("*")):
            if not path.is_file():
                continue
            if path.name == ".DS_Store":
                continue
            rel = path.relative_to(EXPANDED_PACKAGE).as_posix()
            info = zipfile.ZipInfo(rel, date_time=FIXED_ZIP_TIMESTAMP)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, path.read_bytes())
    return buffer.getvalue()


def apply_build(dry_run: bool) -> list[str]:
    expected_text_files, expected_binary_files = create_expected_file_outputs()
    changes: list[str] = []

    for path, content in sorted(expected_text_files.items(), key=lambda item: item[0].as_posix()):
        if write_text_if_changed(path, content, dry_run):
            changes.append(str(path.relative_to(ROOT)))

    for path, content in sorted(expected_binary_files.items(), key=lambda item: item[0].as_posix()):
        if write_bytes_if_changed(path, content, dry_run):
            changes.append(str(path.relative_to(ROOT)))

    imscc_bytes = build_imscc_bytes()
    if write_bytes_if_changed(IMSCC_PATH, imscc_bytes, dry_run):
        changes.append(str(IMSCC_PATH.relative_to(ROOT)))

    return changes


def parse_schedule() -> dict[int, list[str]]:
    schedule = ROOT / "course" / "schedule.md"
    week = None
    deliverables: dict[int, list[str]] = {}
    for line in schedule.read_text(encoding="utf-8").splitlines():
        week_match = re.match(r"^## Week (\d+):", line)
        if week_match:
            week = int(week_match.group(1))
            continue
        if week is None:
            continue
        deliverable_match = re.match(r"^- Deliverables:\s*(.+)$", line)
        if deliverable_match:
            items = [part.strip() for part in deliverable_match.group(1).split(",")]
            deliverables[week] = items
    return deliverables


def validate_due_dates() -> list[str]:
    issues: list[str] = []
    schedule = parse_schedule()

    for overview in sorted((ROOT / "modules").glob("week-*-overview.md")):
        week_match = re.search(r"week-(\d+)-overview", overview.stem)
        if week_match is None:
            continue
        week = int(week_match.group(1))
        expected = schedule.get(week, [])
        actual = None
        for line in overview.read_text(encoding="utf-8").splitlines():
            match = re.match(r"^- Deliverables:\s*(.+)$", line)
            if match:
                actual = [part.strip() for part in match.group(1).split(",")]
                break
        if actual != expected:
            issues.append(
                f"Module overview mismatch for Week {week:02d}: expected {expected}, found {actual}"
            )

    for source in sorted((ROOT / "assignments").glob("*.md")) + sorted((ROOT / "projects").glob("*.md")):
        text = source.read_text(encoding="utf-8")
        title = heading_text(text)
        due_match = re.search(r"^\*\*Due:\*\*\s*End of Week (\d+)", text, re.MULTILINE)
        if due_match is None:
            issues.append(f"Missing top-level due line in {source.relative_to(ROOT)}")
            continue
        week = int(due_match.group(1))
        short_label_match = re.match(r"^(Assignment \d+|Project \d+|Final Project)", title)
        short_label = short_label_match.group(1) if short_label_match else title
        expected = schedule.get(week, [])
        if not any(item.startswith(short_label) for item in expected):
            issues.append(
                f"Schedule mismatch for {source.relative_to(ROOT)}: {short_label} is due Week {week:02d}, "
                f"but Week {week:02d} deliverables are {expected}"
            )

    return issues


def validate_quiz_points() -> list[str]:
    issues: list[str] = []
    for quiz_path in sorted((ROOT / "quizzes").glob("*.json")):
        data = json.loads(quiz_path.read_text(encoding="utf-8"))
        declared = data.get("points")
        actual = sum(question.get("points_possible", 0) for question in data.get("questions", []))
        if declared != actual:
            issues.append(
                f"Quiz points mismatch in {quiz_path.relative_to(ROOT)}: declared {declared}, actual {actual}"
            )
    return issues


def validate_outputs() -> list[str]:
    issues: list[str] = []
    expected_text_files, expected_binary_files = create_expected_file_outputs()

    for path, content in expected_text_files.items():
        existing = path.read_text(encoding="utf-8") if path.exists() else None
        if existing != content:
            issues.append(f"Out-of-sync file: {path.relative_to(ROOT)}")

    for path, content in expected_binary_files.items():
        existing = path.read_bytes() if path.exists() else None
        if existing != content:
            issues.append(f"Out-of-sync file: {path.relative_to(ROOT)}")

    if not IMSCC_PATH.exists():
        issues.append("Missing canvas/WEB1430-Canvas-Export.imscc")

    issues.extend(validate_due_dates())
    issues.extend(validate_quiz_points())
    return issues


def parse_args(argv: Iterable[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build and validate the Canvas export package from markdown sources."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    build_parser = subparsers.add_parser("build", help="Regenerate the expanded package and IMSCC.")
    build_parser.add_argument(
        "--check",
        action="store_true",
        help="Report which files would change without writing them.",
    )

    subparsers.add_parser("validate", help="Fail if the expanded package is out of sync.")
    return parser.parse_args(list(argv))


def main(argv: Iterable[str]) -> int:
    args = parse_args(argv)

    if args.command == "build":
        changes = apply_build(dry_run=args.check)
        if args.check:
            if changes:
                print("The following files would be updated:")
                for change in changes:
                    print(change)
                return 1
            print("Canvas package is already up to date.")
            return 0

        if changes:
            print("Updated files:")
            for change in changes:
                print(change)
        else:
            print("Canvas package was already up to date.")
        return 0

    issues = validate_outputs()
    if issues:
        print("Validation failed:")
        for issue in issues:
            print(f"- {issue}")
        return 1

    print("Validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
