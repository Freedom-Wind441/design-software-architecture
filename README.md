# 软件架构设计与渐进迁移

面向 AI 编程助手的 `design-software-architecture` Skill，用于新项目架构设计、现有工程的职责与依赖审计、数据流梳理、渐进重构和跨平台扩展。

根据项目规模选择适度架构，保护已有行为与数据；不强制五层，不因普通 UI 调整扩大为架构重写。架构判断需要源码、实际依赖和验证结果支持，不能仅靠目录名称或编译成功。

## 与 Reasoning Workflow 的关系

- **本 Skill**：补充软件架构专项规则，包括职责边界、依赖方向、状态所有权、迁移和验收。
- **[Reasoning Workflow](https://github.com/zy839971925-zyy/Agent--deep-research-Workflow-Skills)**：由第三方 `zy839971925-zyy` 独立维护，提供任务理解、证据、推理与执行控制。

两者可以配合使用。Reasoning Workflow 不可用时，本 Skill 仍完成架构专项工作，并明确未调用前者。本仓库不复制或打包 Reasoning Workflow，也不将其归为本项目作者的作品；其安装、版本与许可证以原仓库为准。

## 安装

### Codex

在支持 `$skill-installer` 的 Codex 中输入：

```text
$skill-installer install https://github.com/Freedom-Wind441/design-software-architecture/tree/main/skills/design-software-architecture
```

也可将整个 `skills/design-software-architecture/` 文件夹复制到：

- 项目内：`.agents/skills/design-software-architecture/`
- 用户级：`~/.agents/skills/design-software-architecture/`

保留文件夹名称和内部结构；不要只复制 `SKILL.md`。Codex 通常会自动发现，未显示时重启。安装器下载和客户端发现尚未在本次验证中实际执行。

### 其他支持 Agent Skills 的宿主

按宿主文档导入 `skills/design-software-architecture/` 文件夹。其他客户端尚未逐一实测，不能仅由结构兼容推断完整运行兼容。

需要配合 Reasoning Workflow 时，从[其原仓库安装说明](https://github.com/zy839971925-zyy/Agent--deep-research-Workflow-Skills/blob/main/README.zh-CN.md)单独安装。

## 使用示例

```text
使用 $design-software-architecture，为这个新项目选择适合规模的架构。
先明确主要用例、状态所有权和外部接入，再实现一条端到端用例及失败路径。
```

```text
使用 $design-software-architecture，检查当前工程的职责、依赖与状态写入路径。
在保留已有功能、UI 和数据兼容性的前提下，实施少量高价值的渐进迁移并验证。
```

```text
同时使用 $reasoning-workflow 和 $design-software-architecture，分析增加第二个数据源的影响。
本次只交付设计方案，不修改代码。
```

## 文件与依赖

可安装文件夹包含 `SKILL.md`、`agents/openai.yaml`、三份 `references/` 文档、`assets/icon.svg` 和 `LICENSE`。正文按需引用参考文件，所有本地引用保持在 Skill 内。

本 Skill 是指令与参考资料，无运行脚本、固定 MCP 服务、API Key 或额外软件包依赖。实际工程的构建与测试工具由项目决定；Reasoning Workflow 属于可选协作 Skill，不是自动安装的工具依赖。

## 已验证范围

截至 2026-10-12，已验证发布文件的 Agent Skills 基本结构、YAML 元数据、Codex 可选界面配置、相对路径、图标有效性、脱敏检查和核心规则保留。详情见 [VALIDATION.md](VALIDATION.md)。

验证依据：[Agent Skills 规范](https://agentskills.io/specification)、[OpenAI Skill 文档](https://learn.chatgpt.com/docs/build-skills)及[元数据校验说明](https://developers.openai.com/plugins/deploy/submission-errors)。本次验证属于静态文件与本地目录复制检查；未实测 Codex CLI/IDE 的加载、ChatGPT 导入、API 上传或 Windows/macOS 客户端运行。该仓库发布独立 Skill，尚未包含插件市场提交所需的插件清单。

## 许可证

采用 [MIT License](LICENSE)，版权署名为 `Copyright (c) 2026 Freedom-Wind441`。可安装文件夹也包含相同的许可证，单独安装时请保留。Reasoning Workflow 的许可独立适用，以其原仓库为准。
