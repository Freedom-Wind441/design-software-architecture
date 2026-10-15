#!/usr/bin/env python3
"""Validate this repository's release contract; does not test host behavior."""

import argparse
import hashlib
import json
import re
import shutil
import tempfile
from pathlib import Path
from urllib.parse import unquote, urlsplit
from xml.etree import ElementTree

import yaml


class UniqueLoader(yaml.SafeLoader):
    pass


def unique_mapping(loader, node):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node)
        if key in result:
            raise ValueError(f"duplicate YAML key: {key}")
        result[key] = loader.construct_object(value_node)
    return result


UniqueLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping
)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def headings(text):
    # GitHub-style slugs for the simple headings used by this repository.
    result, counts = set(), {}
    for line in text.splitlines():
        match = re.match(r"^#{1,6}\s+(.+)$", line)
        if not match:
            continue
        slug = re.sub(r"[^\w\- ]", "", match[1].strip().lower()).replace(" ", "-")
        number = counts.get(slug, 0)
        counts[slug] = number + 1
        result.add(slug + (f"-{number}" if number else ""))
    return result


def check_links(path, root):
    text = path.read_text(encoding="utf-8")
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    links = re.findall(r"\]\(([^\s)]+)\)", text)
    links += re.findall(r'(?:src|href)="([^"]+)"', text)
    for link in links:
        url = urlsplit(link)
        if url.scheme or url.netloc:
            continue  # External availability is a separate, online check.
        target = (path.parent / unquote(url.path)).resolve() if url.path else path
        require(target.is_relative_to(root), f"link escapes repository: {path}: {link}")
        require(target.exists(), f"broken local link: {path}: {link}")
        if url.fragment and target.suffix == ".md":
            require(unquote(url.fragment) in headings(target.read_text(encoding="utf-8")),
                    f"broken heading link: {path}: {link}")


def validate(root):
    root = root.resolve()
    skill = root / "skills/design-software-architecture"
    expected = {
        "SKILL.md", "LICENSE", "agents/openai.yaml", "assets/icon.svg",
        "references/boundaries-and-state.md", "references/incremental-migration.md",
        "references/verification-and-delivery.md",
        "references/preferences-capabilities-and-adaptation.md",
    }
    for path in skill.rglob("*"):
        require(not path.is_symlink(), f"symlink in Skill: {path}")
    actual = {str(p.relative_to(skill)) for p in skill.rglob("*") if p.is_file()}
    require(actual == expected, f"unexpected/missing Skill files: {actual ^ expected}")
    require({p.name for p in (root / "skills").iterdir()} == {skill.name},
            "only the architecture Skill may be bundled")

    entry = (skill / "SKILL.md").read_text(encoding="utf-8")
    frontmatter = re.match(r"\A---\n(.*?)\n---\n", entry, re.S)
    require(frontmatter is not None, "missing frontmatter")
    metadata = yaml.load(frontmatter[1], Loader=UniqueLoader)
    require(set(metadata) == {"name", "description"}, "unexpected entrypoint fields")
    name = metadata["name"]
    require(isinstance(name, str) and name == skill.name and len(name) <= 64
            and re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name), "invalid Skill name")
    description = metadata["description"]
    require(isinstance(description, str) and 1 <= len(description) <= 1024,
            "invalid Skill description")
    require(len(entry.splitlines()) < 500, "entrypoint must remain under 500 lines")
    for ref in sorted((skill / "references").glob("*.md")):
        require(f"(references/{ref.name})" in entry, f"unreachable reference: {ref.name}")

    ui = yaml.load((skill / "agents/openai.yaml").read_text(encoding="utf-8"),
                   Loader=UniqueLoader)
    require(set(ui) == {"interface", "policy"}, "unexpected UI top-level fields")
    interface = ui["interface"]
    require(set(interface) == {"display_name", "short_description", "default_prompt",
                               "icon_small", "icon_large"}, "unexpected UI fields")
    require(all(isinstance(v, str) and v for v in interface.values()), "invalid UI strings")
    require(25 <= len(interface["short_description"]) <= 64, "UI blurb length")
    require("$design-software-architecture" in interface["default_prompt"], "prompt invocation")
    require(interface["display_name"] == "Software Architecture", "English display default")
    require(ui["policy"] == {"allow_implicit_invocation": True}, "invocation policy changed")
    for field in ("icon_small", "icon_large"):
        icon = (skill / interface[field]).resolve()
        require(interface[field].startswith("./assets/") and icon.is_relative_to(skill)
                and icon.is_file(), f"invalid {field}")
        require(ElementTree.parse(icon).getroot().tag == "{http://www.w3.org/2000/svg}svg",
                "invalid SVG root")
    require((root / "LICENSE").read_bytes() == (skill / "LICENSE").read_bytes(),
            "license copies differ")
    require("Copyright (c) 2026 Freedom-Wind441" in (skill / "LICENSE").read_text(),
            "license attribution")

    version = (root / "VERSION").read_text().strip()
    require(re.fullmatch(r"\d+\.\d+\.\d+", version), "invalid version")
    for suffix in ("", ".zh-CN"):
        readme = (root / f"README{suffix}.md").read_text(encoding="utf-8")
        other = "README.zh-CN.md" if not suffix else "README.md"
        require(f"(./{other})" in readme, "missing language switch")
        require(f"version-{version}-" in readme and f"v{version}" in readme,
                "README version mismatch")
        require(f"## {version} — " in (root / f"CHANGELOG{suffix}.md").read_text(),
                "changelog version mismatch")
        require((root / f"VALIDATION{suffix}.md").is_file(), "missing validation translation")

    for path in root.rglob("*.md"):
        if ".git" not in path.parts:
            check_links(path, root)

    forbidden = {
        "machine path": r"/(?:root|workspace|Users|home)/|[A-Za-z]:\\(?:Users|Windows)\\",
        "email": r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        "credential": r"-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----|gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|sk-[A-Za-z0-9]{20,}",
        "project-specific content": r"GPT-Quota-Glass|OnePlus|ColorOS|PLK110",
    }
    for rel in expected:
        content = (skill / rel).read_text(encoding="utf-8")
        for kind, pattern in forbidden.items():
            require(not re.search(pattern, content), f"potential {kind} in Skill: {rel}")

    manifest = json.loads((root / "docs/skill-manifest.json").read_text())
    require(manifest["version"] == version, "manifest version mismatch")
    require(set(manifest["sha256"]) == expected, "manifest file list mismatch")
    for rel, fingerprint in manifest["sha256"].items():
        require(digest(skill / rel) == fingerprint, f"fingerprint mismatch: {rel}")

    with tempfile.TemporaryDirectory() as temporary:
        destination = Path(temporary) / ".agents/skills" / skill.name
        shutil.copytree(skill, destination)
        copied = {str(p.relative_to(destination)): digest(p)
                  for p in destination.rglob("*") if p.is_file()}
        require(copied == manifest["sha256"], "installation-layout copy differs")
    print(f"PASS: v{version}; {len(expected)} Skill files; metadata, references, local links,")
    print("SVG, licenses, version, scoped privacy patterns, manifest and installation layout.")
    print("Static checks only; host loading and real project behavior are not tested.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    arguments = parser.parse_args()
    try:
        validate(arguments.root)
    except (ValueError, OSError, KeyError, TypeError, yaml.YAMLError,
            ElementTree.ParseError) as error:
        parser.exit(1, f"FAIL: {error}\n")
