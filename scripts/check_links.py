#!/usr/bin/env python3
"""Check that every internal Markdown link in the repository resolves.

Three kinds of target are checked.

- A file link (``FILE.md``, ``schema/x.json``) must exist on disk.
- A fragment (``#anchor``, ``FILE.md#anchor``) must match a heading anchor or an
  explicit ``<a name="...">`` anchor in the target file.
- A case id mentioned in prose (``LC-A-001``) must exist in ``cases.json``, either
  as a case of its own or as a variant id folded under one.

GitHub's heading anchor rules are reproduced here: lowercase, drop anything that
is not a word character, a space or a hyphen, then spaces become hyphens.
Duplicate anchors in one file get ``-1``, ``-2`` and so on.

Exit 0 when every link resolves, 1 otherwise.
"""

import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LINK_RE = re.compile(r"\[(?:[^\]\\]|\\.)*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
EXPLICIT_ANCHOR_RE = re.compile(r"<a\s+(?:name|id)=\"([^\"]+)\"", re.IGNORECASE)
CASE_ID_RE = re.compile(r"\bLC-[A-Z]-\d{3}\b")
FENCE_RE = re.compile(r"^\s*(```|~~~)")


def strip_code(text):
    """Blank out fenced code blocks so their contents are not read as links."""
    out, in_fence = [], False
    for line in text.split("\n"):
        if FENCE_RE.match(line):
            in_fence = not in_fence
            out.append("")
            continue
        out.append("" if in_fence else line)
    return "\n".join(out)


def slug(text):
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"!?\[((?:[^\]\\]|\\.)*)\]\([^)]*\)", r"\1", text)
    text = text.replace("`", "")
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE)
    return re.sub(r"\s", "-", text.strip())


def anchors_for(path, text):
    """Every fragment that resolves inside one file."""
    found, seen = set(), {}
    body = strip_code(text)
    for line in body.split("\n"):
        m = HEADING_RE.match(line)
        if not m:
            continue
        base = slug(m.group(2))
        if not base:
            continue
        n = seen.get(base, 0)
        seen[base] = n + 1
        found.add(base if n == 0 else f"{base}-{n}")
    for m in EXPLICIT_ANCHOR_RE.finditer(text):
        found.add(m.group(1))
    return found


def markdown_files():
    out = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in (".git", "__pycache__")]
        for name in sorted(filenames):
            if name.endswith(".md"):
                out.append(os.path.join(dirpath, name))
    return sorted(out)


def main():
    files = markdown_files()
    texts = {p: open(p, encoding="utf-8").read() for p in files}
    anchors = {p: anchors_for(p, t) for p, t in texts.items()}

    with open(os.path.join(ROOT, "cases.json"), encoding="utf-8") as fh:
        cases = json.load(fh)
    case_ids = {c["id"] for c in cases}
    variant_ids = {v["id"] for c in cases for v in c.get("variants") or []}
    known_ids = case_ids | variant_ids

    problems = []
    checked = {"file": 0, "fragment": 0, "case_id": 0}

    for path in files:
        rel = os.path.relpath(path, ROOT)
        body = strip_code(texts[path])
        for lineno, line in enumerate(body.split("\n"), 1):
            for m in LINK_RE.finditer(line):
                target = m.group(1)
                if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("//"):
                    continue  # external, out of scope for this check
                filepart, _, frag = target.partition("#")
                if filepart:
                    resolved = os.path.normpath(
                        os.path.join(os.path.dirname(path), filepart))
                    checked["file"] += 1
                    if not os.path.exists(resolved):
                        problems.append(
                            f"{rel}:{lineno}: missing file: {filepart}")
                        continue
                else:
                    resolved = path
                if frag:
                    checked["fragment"] += 1
                    if resolved not in anchors:
                        if resolved.endswith(".md"):
                            problems.append(
                                f"{rel}:{lineno}: fragment into unread file: {target}")
                        continue
                    if frag not in anchors[resolved]:
                        problems.append(
                            f"{rel}:{lineno}: unresolved anchor: {target}")

        for lineno, line in enumerate(body.split("\n"), 1):
            for m in CASE_ID_RE.finditer(line):
                checked["case_id"] += 1
                if m.group(0) not in known_ids:
                    problems.append(
                        f"{rel}:{lineno}: case id not in cases.json: {m.group(0)}")

    print(f"markdown files: {len(files)}")
    print(f"known ids: {len(case_ids)} cases, {len(variant_ids)} folded variants")
    print("checked: {file} file links, {fragment} fragments, "
          "{case_id} case id mentions".format(**checked))
    if problems:
        print(f"\nFAILED: {len(problems)} unresolved")
        for p in problems:
            print("  " + p)
        return 1
    print("\nPASSED: every internal link resolves")
    return 0


if __name__ == "__main__":
    sys.exit(main())
