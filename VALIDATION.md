# Release validation

**English** · [简体中文](./VALIDATION.zh-CN.md) · [Home](./README.md)

Release: **0.2.0** · Check date: **2026-10-15**

## Source and scope

The previous public baseline is [`4a80bc1`](https://github.com/Freedom-Wind441/design-software-architecture/commit/4a80bc19e60f6f6ce481a8249d2f5bb19cc77123). This release synchronizes the author's currently installed architecture Skill, including the new adaptation reference and current icon. The original installed files are left unchanged.

The entrypoint, all four references, and icon match the current local source byte for byte. The three pre-existing references are also unchanged from the public baseline. Only the published display name, short description, and starter prompt switch to English; the implicit invocation policy remains enabled. Published icon paths keep their `./assets/` form and unsupported product-enumeration metadata is not reintroduced.

Reasoning Workflow is referenced through its upstream repository only. No copy, archive, runtime, or license from that project is included.

## Reproducible checks

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate.py
```

The checked payload consists of eight UTF-8 files. Exact SHA-256 fingerprints are recorded in [`docs/skill-manifest.json`](./docs/skill-manifest.json).

| Check | Result and boundary |
| --- | --- |
| Skill inventory and entrypoint | Eight regular files, no symlinks or extra Skills; valid name/description; entrypoint under 500 lines |
| Progressive references | All four references are directly reachable from `SKILL.md` |
| Codex display metadata | Valid YAML, English display default, intact explicit starter invocation and implicit policy, valid icon paths |
| License and SVG | Identical MIT license copies; valid SVG XML |
| Documentation | English/Chinese switches, local file links and heading anchors resolve; version agrees across README, change records, manifest, and `VERSION` |
| Scoped privacy patterns | Installable files contain no matched machine paths, email addresses, common credential patterns, or application-specific identifiers |
| Integrity and installation layout | All payload hashes match; a clean temporary `.agents/skills/` copy preserves all bytes |
| Additional validator | OpenAI's bundled Skill Creator `quick_validate.py` accepts the payload |
| Validator rejection checks | Isolated copies with a broken reference, changed invocation policy, or modified payload fingerprint are rejected |

The repository checker is a deliberately bounded release check, not a complete Markdown parser, general secret scanner, or behavioral evaluator. Online URL availability is checked separately from local links. Repository development uses Python and PyYAML; the installable Skill has no package dependency.

## Compatibility limits

Structure is checked against the [Agent Skills specification](https://agentskills.io/specification); local discovery and optional metadata are checked against [OpenAI's documentation](https://learn.chatgpt.com/docs/build-skills) and the bundled Skill Creator's metadata guidance.

No Codex CLI/IDE live loading, ChatGPT import, API upload, Windows/macOS client execution, or real-project behavioral evaluation was performed for this release. Copying to the documented installation layout does not prove client discovery. Guidance for cross-platform development does not imply every host or operating system was tested. This is a direct Skill-folder release, without a marketplace plugin manifest.

GitHub Actions runs the same repository checker. Its live status is shown in the README badge; this record describes the local release checks and does not predict CI success.

## Historical record

The [2026-10-12 validation record](./docs/archive/validation-2026-10-12.zh-CN.md) is retained unchanged for the older baseline. Its fingerprints and file counts describe that earlier release only.
