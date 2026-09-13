#!/usr/bin/env python3
"""Dependency-free structural validation for Product Designer Skills OS."""

from __future__ import annotations

import re
import sys
from pathlib import Path


NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)
ALLOWED_KEYS = {"name", "description", "license", "allowed-tools", "metadata"}


def scalar(frontmatter: str, key: str) -> str:
    match = re.search(rf"(?m)^{re.escape(key)}:\s*(.+)$", frontmatter)
    return match.group(1).strip().strip('"') if match else ""


def validate_skill(folder: Path) -> list[str]:
    errors: list[str] = []
    skill_file = folder / "SKILL.md"
    metadata_file = folder / "agents" / "openai.yaml"

    if not skill_file.is_file():
        return ["missing SKILL.md"]

    content = skill_file.read_text(encoding="utf-8").replace("\r\n", "\n")
    match = FRONTMATTER_RE.match(content)
    if not match:
        return ["missing or malformed frontmatter"]

    frontmatter = match.group(1)
    keys = set(re.findall(r"(?m)^([A-Za-z0-9_-]+):", frontmatter))
    unexpected = sorted(keys - ALLOWED_KEYS)
    if unexpected:
        errors.append(f"unexpected frontmatter keys: {', '.join(unexpected)}")

    name = scalar(frontmatter, "name")
    description = scalar(frontmatter, "description")
    if name != folder.name:
        errors.append(f"folder/name mismatch: {name!r}")
    if not NAME_RE.fullmatch(name) or len(name) > 64:
        errors.append("invalid skill name")
    if not description or len(description) > 1024 or "<" in description or ">" in description:
        errors.append("invalid description")
    if re.search(r"(?m)^\s*\[TODO:", content):
        errors.append("unfinished TODO placeholder")

    for relative in re.findall(r"\]\((references/[^)]+)\)", content):
        if not (folder / relative).is_file():
            errors.append(f"missing reference: {relative}")

    if not metadata_file.is_file():
        errors.append("missing agents/openai.yaml")
    else:
        metadata = metadata_file.read_text(encoding="utf-8")
        if f"${name}" not in metadata:
            errors.append("default_prompt does not mention the skill")
        short = re.search(r'(?m)^\s*short_description:\s*"([^"]+)"', metadata)
        if not short or not 25 <= len(short.group(1)) <= 64:
            errors.append("short_description must be 25-64 characters")

    return errors


def main() -> int:
    repository = Path(__file__).resolve().parents[1]
    skills_root = repository / "skills"
    failed = False
    for folder in sorted(path for path in skills_root.iterdir() if path.is_dir()):
        errors = validate_skill(folder)
        status = "PASS" if not errors else "FAIL"
        print(f"{status} {folder.name}")
        for error in errors:
            print(f"  - {error}")
        failed = failed or bool(errors)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
