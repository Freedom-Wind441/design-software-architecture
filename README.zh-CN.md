<div align="center">

<img src="./skills/design-software-architecture/assets/icon.svg" width="88" height="88" alt="软件架构" />

# 软件架构设计与渐进迁移

### 按项目规模划分边界，在保护现有行为的前提下逐步迁移。

面向 AI 编程助手的 Agent Skill：架构设计、依赖与状态审计、渐进重构和跨平台适配。

[English](./README.md) · **简体中文**

[![版本](https://img.shields.io/badge/version-0.2.0-2563eb)](./CHANGELOG.zh-CN.md)
[![许可证：MIT](https://img.shields.io/badge/license-MIT-475569)](./LICENSE)
[![验证](https://github.com/Freedom-Wind441/design-software-architecture/actions/workflows/validate.yml/badge.svg)](https://github.com/Freedom-Wind441/design-software-architecture/actions/workflows/validate.yml)

[快速开始](#快速开始) · [能力范围](#能力范围) · [使用示例](#使用示例) · [验证范围](#验证与兼容范围) · [更新记录](./CHANGELOG.zh-CN.md)

**[浏览 Skill](./skills/design-software-architecture/)** · [阅读执行规则](./skills/design-software-architecture/SKILL.md)

</div>

---

## 快速开始

在支持 `$skill-installer` 的 Codex 中输入：

```text
$skill-installer install https://github.com/Freedom-Wind441/design-software-architecture/tree/main/skills/design-software-architecture
```

安装后使用：

```text
使用 $design-software-architecture 检查当前工程，选择适合规模的职责边界，
实施必要修改并验证行为和依赖方向。保留现有 UI、数据和升级兼容性。
```

需要固定版本时，将安装链接中的 `main` 替换为 `v0.2.0`。

<details>
<summary>手动安装与其他宿主</summary>

将整个 [`skills/design-software-architecture/`](./skills/design-software-architecture/) 文件夹复制到宿主文档规定的位置。Codex 文档列出的位置包括：

| 范围 | 目标位置 |
| --- | --- |
| 项目级 | `.agents/skills/design-software-architecture/` |
| 用户级 | `~/.agents/skills/design-software-architecture/` |

保持 `SKILL.md`、`agents/`、`references/`、`assets/` 和 `LICENSE` 一起安装，不要只复制入口文件。Codex 未发现更新时可重启。其他 Agent Skills 宿主的目录可能不同，以其文档为准。

</details>

Skill 本身没有运行脚本、API Key、固定 MCP 服务或软件包依赖。仓库验证单独使用 Python 与 PyYAML；实际工程的构建和测试工具由工程决定。

## 能力范围

| 任务 | Skill 提供的指导 |
| --- | --- |
| 从零建立项目 | 按实际规模选择结构，先完成一条端到端用例及其失败路径。 |
| 审计现有工程 | 从最新源码追踪实际依赖、数据流、状态所有权和写入路径。 |
| 渐进重构 | 选择高价值迁移切口，保护功能、UI、存量数据和安装身份。 |
| 增加平台或数据源 | 分开稳定契约与数据源、调度、凭据、生命周期和渲染适配。 |
| 自动适配与自定义共存 | 保留用户意图，按实际能力解析配置，隔离可选发布的失败。 |
| 验收修改 | 分别核对结构与行为，明确已验证内容和未知范围。 |

简单函数或模块足够时，不增加空壳层。不强制五个物理层，也不因普通 UI 微调扩大为架构重写。Skill 为助手提供指导，本身不强制执行依赖边界。

## 与 Reasoning Workflow 的关系

| Skill | 职责 | 维护者 |
| --- | --- | --- |
| **软件架构设计与渐进迁移** | 架构边界、依赖方向、状态所有权、迁移和验收证据 | Freedom-Wind441 |
| **[Reasoning Workflow](https://github.com/zy839971925-zyy/Agent--deep-research-Workflow-Skills)** | 通用任务理解、推理、证据与执行控制 | 独立第三方：zy839971925-zyy |

两者可以配合使用。需要时按[原仓库说明](https://github.com/zy839971925-zyy/Agent--deep-research-Workflow-Skills/blob/main/README.zh-CN.md)单独安装 Reasoning Workflow。后者不可用时，本 Skill 仍完成架构专项工作，不伪称已经调用。

本仓库不复制、打包或自动安装 Reasoning Workflow，也不将其归为本项目作者的作品。其版本与许可证以原仓库为准。

## 使用示例

### 新项目设计

```text
使用 $design-software-architecture 为这个新桌面应用选择架构。
先明确主要用例、状态所有者、持久化需求和外部适配，
完成一条端到端路径和失败场景，再扩展结构。
```

### 优化现有项目

```text
使用 $design-software-architecture 审计最新源码中的职责、依赖和状态写入。
选择少量高价值切口实施渐进迁移，保留现有行为、UI 与存量数据，并验证结果。
```

### 仅设计适配方案

```text
同时使用 $reasoning-workflow 和 $design-software-architecture 评估增加第二个平台。
说明哪些可以复用、哪些需要适配器，以及自动能力探测如何与显式用户偏好共存。
本次只交付设计方案，不修改代码。
```

## 仓库导航

| 位置 | 用途 |
| --- | --- |
| [`skills/design-software-architecture/SKILL.md`](./skills/design-software-architecture/SKILL.md) | 可安装入口与核心规则 |
| [`references/`](./skills/design-software-architecture/references/) | 四份按需加载的专项参考 |
| [`agents/openai.yaml`](./skills/design-software-architecture/agents/openai.yaml) | 英文显示元数据与调用策略 |
| [`CHANGELOG.zh-CN.md`](./CHANGELOG.zh-CN.md) / [English](./CHANGELOG.md) | 更新记录；当前版本见 [`VERSION`](./VERSION) |
| [`VALIDATION.zh-CN.md`](./VALIDATION.zh-CN.md) / [English](./VALIDATION.md) | 检查结果、来源与兼容限制 |
| [`docs/design-references.md`](./docs/design-references.md) | 界面参考与采纳理由 |
| [`scripts/validate.py`](./scripts/validate.py) | 仓库验证，不进入可安装 Skill |

**语言范围：**仓库说明提供英文和简体中文，英文是默认首页和显示元数据。执行规则与四份技术参考保留原始中文，避免翻译改变规则；本次没有将整个 Skill 翻译为英文。

## 验证与兼容范围

发布文件按 [Agent Skills 规范](https://agentskills.io/specification)和 [OpenAI Skill 文档](https://learn.chatgpt.com/docs/build-skills)检查。可复现检查和文件指纹见[验证记录](./VALIDATION.zh-CN.md)。

检查覆盖静态结构、元数据、本地链接、图标 XML、许可证一致性、版本一致性与干净目录安装布局复制。这些检查不能证明所有宿主均能加载或正确执行。本轮未实测 Codex CLI/IDE 加载、ChatGPT 导入、API 上传和 Windows/macOS 客户端。仓库未包含插件市场清单。

运行仓库检查：

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate.py
```

## 许可证

[MIT](./LICENSE) · Copyright (c) 2026 Freedom-Wind441。可安装文件夹保留相同许可证。Reasoning Workflow 继续独立适用原仓库的许可。
