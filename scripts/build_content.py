#!/usr/bin/env python3
"""Validate content/ and emit the static files the site fetches.

Outputs (all under site/public/content/, which is generated and gitignored):
  tree.json          navigation tree built from content/site
  problems.json      parsed problems from content/problems
  checker.py         copy of site/runner/checker.py
  site/**            copy of content/site (markdown)
  problems/**        copy of content/problems (markdown and check.py)

Also runs every check.py against its Reference block under CPython and fails
if any case fails. Standard library only.
"""
from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(ROOT, "content")
SITE_SRC = os.path.join(CONTENT, "site")
PROBLEMS_SRC = os.path.join(CONTENT, "problems")
CHECKER = os.path.join(ROOT, "site", "runner", "checker.py")
OUT = os.path.join(ROOT, "site", "public", "content")

DIRECTIVE = re.compile(r"^:::problem\s+([a-z0-9][a-z0-9-]*)\s*$", re.M)
LINK = re.compile(r"\]\(problem:([a-z0-9][a-z0-9-]*)\)")
FENCE = re.compile(r"^```[^\n]*\n(.*?)^```\s*$", re.M | re.S)
SECTION_NAMES = ["Starter", "Hints", "Approach", "Reference"]

errors: list[str] = []
warnings: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


def read(path: str) -> str:
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def title_of(markdown: str, fallback: str) -> str:
    m = re.search(r"^#\s+(.+?)\s*$", markdown, re.M)
    return m.group(1) if m else fallback


def display_name(folder: str) -> str:
    return re.sub(r"^\d+[-_ ]?", "", folder).replace("-", " ").capitalize() or folder


def sort_key(folder: str):
    m = re.match(r"^(\d+)", folder)
    return (0, int(m.group(1)), folder) if m else (1, 0, folder)


# ------------------------------------------------------------------ site tree

def build_tree(dirpath: str, rel: str) -> dict:
    readme = os.path.join(dirpath, "README.md")
    if not os.path.exists(readme):
        err(f"site page missing README.md: content/site/{rel or '.'}")
        md = ""
    else:
        md = read(readme)
    node = {
        "path": rel,
        "title": title_of(md, display_name(os.path.basename(dirpath)) if rel else "Home"),
        "problems": DIRECTIVE.findall(md),
        "links": LINK.findall(md),
        "children": [],
    }
    for child in sorted(os.listdir(dirpath), key=sort_key):
        full = os.path.join(dirpath, child)
        if os.path.isdir(full) and not child.startswith("."):
            node["children"].append(build_tree(full, f"{rel}/{child}" if rel else child))
    return node


def walk_tree(node: dict):
    yield node
    for c in node["children"]:
        yield from walk_tree(c)


# ------------------------------------------------------------------- problems

def split_sections(md: str) -> tuple[str, dict[str, str]]:
    """Return (statement, {section: body}) using the four level-2 headings."""
    pattern = re.compile(r"^##\s+(" + "|".join(SECTION_NAMES) + r")\s*$", re.M)
    matches = list(pattern.finditer(md))
    statement = md[: matches[0].start()] if matches else md
    sections: dict[str, str] = {}
    for i, m in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(md)
        sections[m.group(1)] = md[m.end():end]
    order = [m.group(1) for m in matches]
    return statement, sections, order


def single_fence(body: str, where: str) -> str | None:
    fences = FENCE.findall(body)
    if len(fences) != 1:
        err(f"{where}: expected exactly one code fence, found {len(fences)}")
        return None
    return fences[0].rstrip("\n")


def parse_hints(body: str) -> list[str]:
    hints: list[str] = []
    for line in body.splitlines():
        m = re.match(r"^\s*\d+\.\s+(.*)$", line)
        if m:
            hints.append(m.group(1).strip())
        elif hints and line.strip():
            hints[-1] += " " + line.strip()
    return hints


def parse_problem(pid: str, folder: str) -> dict | None:
    readme = os.path.join(folder, "README.md")
    check = os.path.join(folder, "check.py")
    where = f"content/problems/{pid}"
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", pid):
        err(f"{where}: id must be lowercase kebab-case")
    if not os.path.exists(readme):
        err(f"{where}: missing README.md")
        return None
    if not os.path.exists(check):
        err(f"{where}: missing check.py")
        return None
    md = read(readme)
    statement, sections, order = split_sections(md)
    for required in ("Starter", "Reference"):
        if required not in sections:
            err(f"{where}: missing '## {required}' section")
    expected_order = [s for s in SECTION_NAMES if s in sections]
    if order != expected_order:
        err(f"{where}: sections must be in order {expected_order}, found {order}")
    if errors and any(where in e for e in errors):
        return None
    starter = single_fence(sections["Starter"], f"{where} Starter")
    reference = single_fence(sections["Reference"], f"{where} Reference")
    return {
        "id": pid,
        "title": title_of(md, pid),
        "statement": statement.strip() + "\n",
        "starter": starter or "",
        "hints": parse_hints(sections.get("Hints", "")),
        "approach": sections.get("Approach", "").strip(),
        "reference": reference or "",
    }


def verify_reference(problem: dict, folder: str) -> None:
    """Run check.py against the Reference block in a separate interpreter."""
    with tempfile.TemporaryDirectory() as tmp:
        with open(os.path.join(tmp, "solution.py"), "w", encoding="utf-8") as fh:
            fh.write(problem["reference"] + "\n")
        code = (
            "import sys, json\n"
            f"sys.path[:0] = [{tmp!r}, {os.path.dirname(CHECKER)!r}]\n"
            "import checker\n"
            f"src = open({os.path.join(folder, 'check.py')!r}, encoding='utf-8').read()\n"
            "print(checker._run(src))\n"
        )
        proc = subprocess.run([sys.executable, "-I", "-c", code], capture_output=True, text=True, timeout=60)
    if proc.returncode != 0:
        err(f"content/problems/{problem['id']}: verification crashed:\n{proc.stderr.strip()}")
        return
    try:
        report = json.loads(proc.stdout.strip().splitlines()[-1])
    except (json.JSONDecodeError, IndexError):
        err(f"content/problems/{problem['id']}: verification produced no report:\n{proc.stdout}")
        return
    if report["status"] != "pass":
        failed = [c for c in report["cases"] if c["status"] != "pass"]
        detail = "; ".join(f"{c['name']}: expected {c.get('expected')} got {c.get('actual')}" for c in failed)
        err(f"content/problems/{problem['id']}: reference fails check.py ({report['status']}) {detail} {report.get('error') or ''}".strip())


# ----------------------------------------------------------------------- main

def main() -> int:
    if not os.path.isdir(SITE_SRC):
        err("content/site does not exist")
    if not os.path.isdir(PROBLEMS_SRC):
        err("content/problems does not exist")
    if not os.path.exists(CHECKER):
        err("site/runner/checker.py does not exist")
    if errors:
        for e in errors:
            print("error:", e, file=sys.stderr)
        return 1

    tree = build_tree(SITE_SRC, "")

    problems: dict[str, dict] = {}
    for pid in sorted(os.listdir(PROBLEMS_SRC)):
        folder = os.path.join(PROBLEMS_SRC, pid)
        if not os.path.isdir(folder) or pid.startswith("."):
            continue
        parsed = parse_problem(pid, folder)
        if parsed:
            problems[pid] = parsed

    referenced: set[str] = set()
    for node in walk_tree(tree):
        for pid in node["problems"] + node["links"]:
            referenced.add(pid)
            if pid not in problems:
                err(f"content/site/{node['path'] or '.'}: references unknown problem '{pid}'")
    for pid in problems:
        if pid not in referenced:
            warn(f"problem '{pid}' is not referenced from any page")

    for pid, problem in problems.items():
        verify_reference(problem, os.path.join(PROBLEMS_SRC, pid))

    for w in warnings:
        print("warning:", w, file=sys.stderr)
    if errors:
        for e in errors:
            print("error:", e, file=sys.stderr)
        print(f"\n{len(errors)} error(s); nothing written", file=sys.stderr)
        return 1

    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    shutil.copytree(SITE_SRC, os.path.join(OUT, "site"))
    shutil.copytree(PROBLEMS_SRC, os.path.join(OUT, "problems"))
    shutil.copy(CHECKER, os.path.join(OUT, "checker.py"))
    with open(os.path.join(OUT, "tree.json"), "w", encoding="utf-8") as fh:
        json.dump(tree, fh, indent=2)
    with open(os.path.join(OUT, "problems.json"), "w", encoding="utf-8") as fh:
        json.dump(problems, fh, indent=2)

    pages = sum(1 for _ in walk_tree(tree))
    print(f"ok: {pages} pages, {len(problems)} problems, {len(warnings)} warning(s) -> site/public/content/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
