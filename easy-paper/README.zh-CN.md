# Easy Paper Toolkit（简体中文）

[English](README.md)
[变更日志](CHANGELOG.md)

## 致谢（Acknowledgement）

感谢上游项目作者与维护者提供的开源基础：

- 上游仓库：[Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills)

本仓库是基于上游能力进行的适配改造版本，**并非**上游官方维护分支。

## 来源说明（Reference）

本项目基于并参考了开源仓库 [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) 的技能体系设计，在其基础上按中文学术写作场景进行了轻量化重组与本地化适配。

## 归因与许可声明

本仓库为上游项目的改造版本：

- Upstream: https://github.com/Imbad0202/academic-research-skills
- Upstream License: CC BY-NC 4.0（署名-非商业）
- 本仓库 `LICENSE` 文件为上游许可证文本的原样复制，未做条款改写

使用与再分发时请注意：

- 需保留上游归因信息
- 需遵循非商业使用限制
- 本仓库与上游作者为“改造与继承关系”，并非官方维护分支

本仓库重点改造方向：

- **路由层重构（从全流程叙事改为按需调用）**：重写 `.claude/CLAUDE.md`，将默认路由收敛为 `project-init -> deep-research -> academic-paper -> academic-paper-reviewer` 四模块协作，不再把完整重型 pipeline 作为默认入口，减少一次性上下文加载。
- **新增初始化模块（project-init）**：新增 `project-init/SKILL.md`、`project-init/agents/profile_builder_agent.md`、`project-init/templates/USER_RESEARCH_PROFILE_TEMPLATE.md`、`project-init/references/integration_contract.md`、`project-init/examples/trigger_examples.md`、`project-init/logic.md`，用于先生成统一配置再进入写作流程。
- **统一全局配置机制**：将 `USER_RESEARCH_PROFILE.md` 设为跨模块唯一约束源，明确 deep-research / academic-paper / academic-paper-reviewer 在执行前先读取该文件，统一术语、体裁、评审标准与红线约束。
- **结构可读性增强**：为四个核心模块补充 `logic.md`（`deep-research/logic.md`、`academic-paper/logic.md`、`academic-paper-reviewer/logic.md`、`shared/logic.md`），降低上手成本，避免逐文件摸索。
- **中文场景本地化**：将使用说明改为中文学术写作可直接落地的流程，新增“新项目”和“已完成部分项目”的双场景起步指引，突出增量续写与定向审查。

---

## 你当前版本包含什么

```text
easy-paper/
├── project-init/
├── deep-research/
├── academic-paper/
├── academic-paper-reviewer/
├── shared/
├── CHANGELOG.md
├── README.md
└── README.zh-CN.md
```

---

## 如何接入 Claude Code（放在哪个目录）

为避免技能不生效，核心原则是：**你从哪个目录启动 Claude，就以哪个目录作为工作区根目录**。

### 方式 B：嵌入到你已有项目（推荐）

适用场景：你已有自己的代码/论文项目，想把 easy-paper 作为技能包接入。

建议目录结构：

```text
your-project/
├── .claude/
│   ├── CLAUDE.md
│   └── skills/
│       └── easy-paper/
│           ├── project-init/
│           ├── deep-research/
│           ├── academic-paper/
│           ├── academic-paper-reviewer/
│           └── shared/
```

接入步骤：

1. 将 `easy-paper` 目录复制到 `your-project/.claude/skills/easy-paper/`。
2. 将本仓库的路由规则合并到 `your-project/.claude/CLAUDE.md`。
3. 在 `your-project/` 根目录启动 Claude Code。
4. 首次建议先触发 `project-init` 生成 `your-project/USER_RESEARCH_PROFILE.md`。

初始化操作命令（PowerShell 示例）：

```powershell
cd C:\path\to\your-project
New-Item -ItemType Directory -Force .claude\skills | Out-Null
Copy-Item -Recurse -Force C:\path\to\easy-paper .claude\skills\easy-paper
```

随后请手动完成两步：

1. 合并路由到 `your-project/.claude/CLAUDE.md`
2. 在 Claude 对话中触发初始化：

```text
初始化课题配置：题目=<你的题目>；体裁=<你的体裁>；方法=<你的核心方法>
```

初始化完成后应看到：

- `your-project/USER_RESEARCH_PROFILE.md`

发布前初始化检查清单（建议）：

1. `your-project/.claude/skills/easy-paper/` 目录存在并包含 5 个模块目录。
2. `your-project/.claude/CLAUDE.md` 已合并路由规则。
3. `your-project/USER_RESEARCH_PROFILE.md` 已成功生成。
4. 抽样触发一个写作任务，确认能命中 `academic-paper`。
5. 抽样触发一个评审任务，确认能命中 `academic-paper-reviewer`。

关于本 skill 包内的 `.claude/`：

- 采用嵌入方式时，**建议删除** skill 包内部的 `.claude/`，避免与主项目 `.claude/CLAUDE.md` 出现双路由或路径歧义。
- 路由文件应只保留在主项目根目录：`your-project/.claude/CLAUDE.md`。
- skill 包应只保留技能目录本体：`project-init`、`deep-research`、`academic-paper`、`academic-paper-reviewer`、`shared`。

### 常见坑位

- 在父目录启动 Claude，却希望它自动读取子目录里的 `.claude/`，通常不会按预期生效。
- 主项目与 skill 包同时存在路由文件，容易出现路由冲突或加载歧义。
- 未先生成 `USER_RESEARCH_PROFILE.md` 就直接大规模写作，容易出现术语不一致和风格漂移。

---

## 新增模块：project-init（重点）

`project-init` 是本版本新增的初始化模块，用于在开始写作前先建立全局配置文件：

- 生成或更新 `USER_RESEARCH_PROFILE.md`
- 统一课题范围、术语表、写作体裁约束、评审标准
- 供 `deep-research`、`academic-paper`、`academic-paper-reviewer` 统一读取

这样做的目的：先锁定边界，再让多 Agent 协作，减少跑偏和术语混乱。

---

## 各模块职责

- `project-init`：初始化课题配置（建议第一步）
- `deep-research`：研究问题澄清、文献检索策略、来源核验
- `academic-paper`：大纲、正文、摘要、引用与格式处理
- `academic-paper-reviewer`：结构化挑刺、方法学审查、修订路线图
- `shared`：跨模块协议（交接、风格校准、验证规范）

---

## 快速开始

### 场景 A：全新项目（推荐流程）

1. 先触发 `project-init`：生成 `USER_RESEARCH_PROFILE.md`。
2. 用 `deep-research` 做定向检索与证据整理。
3. 用 `academic-paper` 按章节写作，再用 `academic-paper-reviewer` 做挑刺修订。

示例触发：
- 初始化课题配置：题目是基于图对比学习的小样本网络入侵检测方法研究。

### 场景 B：已完成部分内容的项目（增量流程）

1. 仍先运行 `project-init`，把你已有目录、摘要草稿、术语约束固化进配置。
2. 跳过不需要的研究步骤，直接用 `academic-paper` 续写指定章节。
3. 对已写章节直接调用 `academic-paper-reviewer` 生成问题清单和修订路线。

示例触发：
- 基于我现有第 1-3 章内容，补全 `USER_RESEARCH_PROFILE.md` 并继续写第 4 章。

---

## 使用建议

- 默认输出简体中文；若需英文摘要可单独指定。
- 涉及 IEEE、arXiv、顶会论文时，建议提供文献元数据或摘要片段，降低引用幻觉风险。
- 如果课题方向发生变化，重新运行 `project-init` 更新全局配置即可。
