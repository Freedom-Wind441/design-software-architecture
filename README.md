<div align="center">

<img src="./skills/design-software-architecture/assets/icon.svg" width="88" height="88" alt="Software Architecture" />

# Software Architecture

### Design boundaries that fit the project. Migrate without losing behavior.

An Agent Skill for architecture design, dependency and state audits, incremental refactoring, and cross-platform adaptation.

**English** · [简体中文](./README.zh-CN.md)

[![Version](https://img.shields.io/badge/version-0.2.0-2563eb)](./CHANGELOG.md)
[![License: MIT](https://img.shields.io/badge/license-MIT-475569)](./LICENSE)
[![Validation](https://github.com/Freedom-Wind441/design-software-architecture/actions/workflows/validate.yml/badge.svg)](https://github.com/Freedom-Wind441/design-software-architecture/actions/workflows/validate.yml)

[Quick start](#quick-start) · [Capabilities](#capabilities) · [Examples](#examples) · [Validation](#validation-and-compatibility) · [Changes](./CHANGELOG.md)

**[Browse the Skill](./skills/design-software-architecture/)** · [Read the rules](./skills/design-software-architecture/SKILL.md)

</div>

---

## Quick start

In Codex with `$skill-installer`, ask:

```text
$skill-installer install https://github.com/Freedom-Wind441/design-software-architecture/tree/main/skills/design-software-architecture
```

Then use:

```text
Use $design-software-architecture to inspect this project, choose boundaries
that fit its scale, implement the necessary changes, and verify behavior
and dependency direction. Preserve existing UI, data, and update compatibility.
```

For a reproducible version, replace `main` in the install URL with `v0.2.0`.

<details>
<summary>Manual installation and other hosts</summary>

Copy the entire [`skills/design-software-architecture/`](./skills/design-software-architecture/) folder into a location documented by your host. Codex documents these locations:

| Scope | Destination |
| --- | --- |
| Project | `.agents/skills/design-software-architecture/` |
| User | `~/.agents/skills/design-software-architecture/` |

Keep `SKILL.md`, `agents/`, `references/`, `assets/`, and `LICENSE` together. Do not copy only the entrypoint. If Codex does not discover an update, restart it. Other Agent Skills hosts may use different locations; check their documentation.

</details>

The Skill has no runtime scripts, API keys, fixed MCP services, or package dependencies. Repository validation uses Python and PyYAML separately. Project build and test tools depend on the project being changed.

## Capabilities

| Task | What the Skill guides |
| --- | --- |
| Start a project | Choose a proportionate structure; implement one end-to-end use case and its failure path first. |
| Audit an existing project | Trace actual dependencies, data flow, state ownership, and write paths from current source. |
| Refactor gradually | Select valuable migration slices while protecting behavior, UI, stored data, and installation identity. |
| Add platforms or data sources | Separate stable contracts from provider, scheduling, credential, lifecycle, and rendering adapters. |
| Combine automatic adaptation and customization | Preserve user intent; resolve effective settings from capabilities; isolate optional publication failures. |
| Accept a change | Check structure and behavior separately; report exactly what was tested and what remains unknown. |

Use simple functions or modules when they suffice. The Skill does not mandate five physical layers or turn ordinary UI edits into architecture rewrites. It guides an agent; it does not enforce dependency boundaries by itself.

## Relationship to Reasoning Workflow

| Skill | Responsibility | Maintainer |
| --- | --- | --- |
| **Software Architecture** | Architecture boundaries, dependency direction, state ownership, migration, and acceptance evidence | Freedom-Wind441 |
| **[Reasoning Workflow](https://github.com/zy839971925-zyy/Agent--deep-research-Workflow-Skills)** | General task understanding, reasoning, evidence, and execution control | Independent third party: zy839971925-zyy |

They can be composed. Install Reasoning Workflow separately using [its upstream instructions](https://github.com/zy839971925-zyy/Agent--deep-research-Workflow-Skills#start-in-30-seconds). If it is unavailable, this Skill still performs architecture work and must not claim to have invoked it.

Reasoning Workflow is not copied, bundled, auto-installed, or claimed as this author's work. Its releases and license are governed by its own repository.

## Examples

### Design a new project

```text
Use $design-software-architecture to design this new desktop application.
Identify the main use cases, state owners, persistence needs, and external
adapters. Implement one end-to-end path and its failure case before expanding.
```

### Improve an existing project

```text
Use $design-software-architecture to audit responsibilities, dependencies,
and state writes in the current source. Implement a small set of valuable
migrations. Preserve existing behavior, UI, and stored data; verify the result.
```

### Plan adaptation without changing code

```text
Use $reasoning-workflow and $design-software-architecture to evaluate adding
a second platform. Explain what can be reused, what needs an adapter, and how
automatic capability detection can coexist with explicit user preferences.
Deliver a design only; do not modify code.
```

## Repository map

| Location | Purpose |
| --- | --- |
| [`skills/design-software-architecture/SKILL.md`](./skills/design-software-architecture/SKILL.md) | Installable entrypoint and core rules |
| [`references/`](./skills/design-software-architecture/references/) | Four focused references, loaded as needed |
| [`agents/openai.yaml`](./skills/design-software-architecture/agents/openai.yaml) | English display metadata and invocation policy |
| [`CHANGELOG.md`](./CHANGELOG.md) / [中文](./CHANGELOG.zh-CN.md) | Version history; current version is in [`VERSION`](./VERSION) |
| [`VALIDATION.md`](./VALIDATION.md) / [中文](./VALIDATION.zh-CN.md) | Checks, provenance, and compatibility limits |
| [`docs/design-references.md`](./docs/design-references.md) | Presentation references and the choices adopted |
| [`scripts/validate.py`](./scripts/validate.py) | Repository checks; excluded from the installable Skill |

**Language:** repository documentation is available in English and Simplified Chinese. English is the default landing page and display metadata. The execution rules and four technical references remain in their original Chinese to preserve their wording; this release is not a full English translation of the Skill.

## Validation and compatibility

The release is checked against the [Agent Skills specification](https://agentskills.io/specification) and [OpenAI's Skill documentation](https://learn.chatgpt.com/docs/build-skills). See [the validation record](./VALIDATION.md) for reproducible checks and fingerprints.

Static structure, metadata, local links, icon XML, license consistency, version consistency, and clean installation-layout copying are checked. These checks do not establish successful loading or behavior in every host. Codex CLI/IDE loading, ChatGPT import, API upload, and Windows/macOS clients have not been tested in this release. No plugin marketplace manifest is included.

To run repository checks:

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate.py
```

## License

[MIT](./LICENSE) · Copyright (c) 2026 Freedom-Wind441. The installable folder includes the same license. Reasoning Workflow remains independently licensed upstream.
