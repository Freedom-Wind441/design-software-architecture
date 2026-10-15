# Changelog

**English** · [简体中文](./CHANGELOG.zh-CN.md) · [Home](./README.md)

## 0.2.0 — 2026-10-15

First explicitly versioned release; earlier commits were unversioned.

### Skill update

- Publish the latest local rules and the new `preferences-capabilities-and-adaptation.md` reference.
- Separate user preferences, device capabilities, and resolved configuration; keep temporary fallbacks from overwriting preferences.
- Clarify optional publication failure isolation, recovery state, generation-aware cleanup, and rendering degradation lifecycle.
- Synchronize the current local icon; preserve the existing three references, core architecture rules, implicit invocation policy, and MIT license.

### Repository and display

- Make English the default README and Skill display metadata; add a complete Chinese README and bilingual change/validation records.
- Add a compact project header, direct navigation, capability table, installation choices, and task examples.
- Add `VERSION` and reproducible repository validation with GitHub Actions. Keep development tools outside the installable Skill.
- Preserve the previous validation report under `docs/archive/`.

The execution rules remain in Chinese. Reasoning Workflow is referenced upstream only and is not included in this release.

## 2026-10-12 — Unversioned baseline

Published the Chinese README, architecture Skill, three references, icon, MIT license, and static validation record. Baseline commit: [`4a80bc1`](https://github.com/Freedom-Wind441/design-software-architecture/commit/4a80bc19e60f6f6ce481a8249d2f5bb19cc77123).
