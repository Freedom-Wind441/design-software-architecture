# 发布验证

[English](./VALIDATION.md) · **简体中文** · [首页](./README.zh-CN.md)

发布版本：**0.2.0** · 检查日期：**2026-10-15**

## 来源与范围

上一轮公开基线为 [`4a80bc1`](https://github.com/Freedom-Wind441/design-software-architecture/commit/4a80bc19e60f6f6ce481a8249d2f5bb19cc77123)。本次同步作者当前已安装的架构 Skill，包含新增适配参考和当前图标；不修改原始安装文件。

入口正文、四份参考及图标与本机最新来源逐字节一致。已有三份参考也与公开基线一致。仅发布副本的显示名称、简介和起始提示切换为英文；保留隐式调用策略。发布图标路径继续使用 `./assets/`，不重新引入不受支持的产品枚举元数据。

Reasoning Workflow 仅引用上游仓库，未包含其副本、压缩包、运行代码或许可证。

## 可复现检查

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate.py
```

可安装内容共有八个 UTF-8 文件。准确的 SHA-256 指纹保存在 [`docs/skill-manifest.json`](./docs/skill-manifest.json)。

| 检查 | 结果与边界 |
| --- | --- |
| 文件清单与入口 | 八个普通文件，无符号链接或其他 Skill；名称、描述有效，入口少于 500 行 |
| 按需参考 | 四份参考都可从 `SKILL.md` 直接到达 |
| Codex 显示元数据 | YAML 有效，默认英文，起始提示保留显式调用，隐式策略及图标路径有效 |
| 许可证与 SVG | 两份 MIT 许可证相同，SVG XML 可解析 |
| 文档 | 中英切换、本地文件链接及标题锚点有效；README、更新记录、指纹清单与 `VERSION` 的版本一致 |
| 有界脱敏模式检查 | 安装文件中未匹配到本机路径、邮箱、常见凭据模式或应用专属标识 |
| 完整性与安装布局 | 所有文件指纹匹配；复制到干净临时 `.agents/skills/` 目录后逐字节一致 |
| 额外校验器 | OpenAI 随附 Skill Creator 的 `quick_validate.py` 接受此安装内容 |
| 校验器反例 | 隔离副本中的断开引用、改变调用策略和篡改文件指纹均被拒绝 |

仓库校验器是有界的发布检查，不是完整 Markdown 解析器、通用凭据扫描器或行为评测器。在线网址可用性与本地链接分开检查。仓库开发使用 Python 与 PyYAML，可安装 Skill 不依赖这些软件包。

## 兼容限制

结构依据 [Agent Skills 规范](https://agentskills.io/specification)检查；本地发现路径和可选元数据依据 [OpenAI 文档](https://learn.chatgpt.com/docs/build-skills)及随附 Skill Creator 的元数据说明检查。

本轮未执行 Codex CLI/IDE 实际加载、ChatGPT 导入、API 上传、Windows/macOS 客户端运行或真实工程行为评测。复制到文档规定的目录不等于证明客户端已发现。跨平台开发指导不意味着所有宿主或操作系统均已实测。本仓库发布直接安装的 Skill 文件夹，未包含插件市场清单。

GitHub Actions 运行相同的仓库校验器；实时状态由 README 徽章显示。本记录描述本地发布检查，不预先声明 CI 成功。

## 历史记录

[2026-10-12 验证记录](./docs/archive/validation-2026-10-12.zh-CN.md)原样保留。其中的指纹和文件数量仅对应更早的发布基线。
