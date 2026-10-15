# Presentation references / 界面参考

[English home](../README.md) · [中文首页](../README.zh-CN.md)

Reviewed on 2026-10-15. These are design references, not a ranking of overall repository quality. No third-party text, images, or Skill payloads were copied.

查阅日期为 2026-10-15。这里记录适合本仓库的呈现方式，不对仓库整体质量作绝对排名；未复制第三方正文、图片或 Skill 内容。

| Reference / 参考 | Adopted / 采纳 | Scope decision / 取舍 |
| --- | --- | --- |
| [Reasoning Workflow](https://github.com/zy839971925-zyy/Agent--deep-research-Workflow-Skills) | Visible language switch, quick-start navigation, direct access to the installable folder / 显眼语言入口、快速开始、直达安装目录 | Baseline for information structure; preserve independent attribution / 信息结构基准，保持独立署名 |
| [obra/superpowers](https://github.com/obra/superpowers) | Explain use and installation by task or host; make the workflow concrete / 按任务或宿主解释使用与安装，给出具体工作方式 | Do not import its runtime hooks, methodology, or compatibility claims / 不引入其运行钩子、方法体系或兼容性承诺 |
| [anthropics/skills](https://github.com/anthropics/skills) | Keep human documentation outside self-contained Skill folders; distinguish standards from host implementations / 人类说明与可安装内容分开，区分规范与宿主实现 | Do not add a marketplace manifest without an actual plugin release / 未发布插件时不虚增市场清单 |
| [eli64s/readme-ai](https://github.com/eli64s/readme-ai) | Centered identity, compact badges, scan-friendly tables, collapsible secondary install details / 居中标识、少量徽章、易扫读表格、折叠次要安装说明 | Keep the original project icon and a short header; omit decorative separators and badge walls / 沿用原图标与简短首屏，不堆装饰分隔与徽章 |

The result uses GitHub-native Markdown and minimal HTML; no JavaScript, custom CSS, external font, or separate website is required. English is `README.md`; Chinese is `README.zh-CN.md`. The language switch is explicit, not automatic browser-language detection.

结果采用 GitHub 原生 Markdown 与少量 HTML，无需 JavaScript、自定义 CSS、外部字体或独立网站。英文为 `README.md`，中文为 `README.zh-CN.md`，通过链接切换，不宣称能按浏览器语言自动切换。
