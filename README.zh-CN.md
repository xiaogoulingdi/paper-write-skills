# Academic Research Skills for Claude Code

[![Version](https://img.shields.io/badge/version-v3.1-blue)](https://github.com/Imbad0202/academic-research-skills/releases/tag/v3.1)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/license-CC%20BY--NC%204.0-lightgrey)](https://creativecommons.org/licenses/by-nc/4.0/)
[![Sponsor](https://img.shields.io/badge/sponsor-Buy%20Me%20a%20Coffee-orange?logo=buy-me-a-coffee)](https://buymeacoffee.com/crucify020v)

[English](README.md) | [繁体中文版](README.zh-TW.md)

一套完整的学术研究 Claude Code 技能包，涵盖从研究到论文出版的全流程。

> **AI 是你的副驾驶，不是机长。** 这工具不会帮你写论文。它处理苦工 — 搜文献、排格式、验数据、查逻辑一致性 — 让你专注在真正需要你脑子的事：定义问题、选方法、诠释数据的意义、写出「我认为」后面那句话。
>
> 跟 humanizer 不同，这工具不是帮你隐藏用 AI 协作的事实，而是帮你把关文章品质。风格校准从你过去的文章学习你的声音，写作品质检查抓出让文字读起来像机器产的模式。目标是品质，不是遮掩。

---

## 使用指南与文章

- [学术写作不该是一个人的事：一套开源 AI 协作工具如何改变研究者的工作流](https://open.substack.com/pub/edwardwu223235/p/ai?r=4dczl&utm_medium=ios) — 完整使用指南（繁体中文）
- [Academic Writing Shouldn&#39;t Be a Solo Act](https://open.substack.com/pub/edwardwu223235/p/academic-writing-shouldnt-be-a-solo?r=4dczl&utm_medium=ios) — Full pipeline walkthrough (English)

---

## 功能特色

- **Deep Research** — 13 个 Agent 组成的研究团队，支援苏格拉底引导（含 SCR 反思机制）+ 系统性文献回顾 / PRISMA + **意图侦测** + **对话健康度监控** + **可选跨模型 DA** + **论证与推理认知框架**
- **Academic Paper** — 12 个 Agent 的论文撰写团队，含风格校准、写作品质检查、LaTeX 输出强化、视觉化、修订教练、引用格式转换、**写作判断力框架**
- **Academic Paper Reviewer** — 多视角同侪审查，0-100 品质量表（主编 + 3 位动态审查者 + 魔鬼代言人，含**让步门槛协议** + **攻击强度保持** + **可选跨模型审查**）+ **R&R 追溯矩阵** + **唯读约束** + **审查品质思维框架**
- **Academic Pipeline** — 10 阶段全流程调度器，含自适应 checkpoint、宣称验证、素材护照、**可选跨模型诚信验证**、**中途强化机制**、**自我检查问题**

### 完整 Pipeline

```
研究 → 撰写 → 诚信审查 → 审稿（5人）→ 苏格拉底指导
  → 修订 → 再审 → 再修订 → 最终诚信审查 → 定稿
```

**核心特点：**

1. 自适应 checkpoint（FULL / SLIM / MANDATORY）
2. 审稿前诚信验证 — 100% 引用、数据、宣称验证（Phase A-E）
3. 两阶段审查，含魔鬼代言人 + 0-100 品质量表
4. 审稿与修订之间的苏格拉底修订指导（含 SCR 表态-挑战-反思机制，可随时开关）
5. 出版前最终诚信验证
6. 输出格式：MD + DOCX + LaTeX（APA 7.0 `apa7` class / IEEE / Chicago）→ tectonic 编译 PDF
7. Pipeline 完成后自动产出协作品质评估（6 维度 1-100 分）
8. 素材护照（Material Passport）支援中途进入流程的来源追踪
9. 跨 skill 模式顾问（14 种情境 + 使用者典型）
10. 风格校准 — 从过去的论文学习作者写作风格（可选，intake Step 10）
11. 写作品质检查 — 侦测 AI 文字常见的高频词汇、标点模式、结构问题
12. **跨模型验证（可选）** — 用 GPT-5.4 Pro 或 Gemini 3.1 Pro 作为独立第二审查者，验证引用、挑战魔鬼代言人、审查论文

---

## v3.0 优化：我们发现了 AI 的哪些结构性限制

在使用 ARS 撰写一篇关于 AI 与高教的反思文章时，我们遇到了三个结构性问题：

1. **框架锁定**：AI 在给定框架内越来越精致，但无法质疑框架本身
2. **谄媚倾向**：每次挑战魔鬼代言人的攻击，它都让步得太快
3. **意图侦测错误**：苏格拉底模式在使用者仍在探索时就急着收束

### 改了什么

- **魔鬼代言人让步门槛**：反驳必须评分 1-5，≥4 才允许让步。不允许连续让步。框架锁定侦测。
- **苏格拉底意图侦测**：侦测使用者是「探索型」还是「目标型」。探索型模式停用自动收束。
- **对话健康度指标**：每 5 轮静默自检，侦测持续同意、回避冲突、过早收束。
- **跨模型验证**：设定 `ARS_CROSS_MODEL` 启用第二 AI 模型独立审查。见下方设定指南。
- **AI 自我反思报告**：Pipeline 结束后自动产出 AI 行为自评。

这些优化不能完全解决 AI 的结构性限制——它们让限制变得可见、可追踪、可被人类介入。

---

## 跨模型验证（可选）

ARS 使用 Claude Opus 4.6 即可完整运作。想要更高信心，可选择启用第二 AI 模型独立验证。

### 快速设定

```bash
# 设定 API key（择一或两者皆设）
export OPENAI_API_KEY="sk-your-key-here"        # GPT-5.4 Pro
export GOOGLE_AI_API_KEY="AIza-your-key-here"    # Gemini 3.1 Pro

# 选择跨验证模型
export ARS_CROSS_MODEL="gpt-5.4-pro"

# 照常启动 Claude Code
claude
```

### 启用后的差异

| 功能       | 未启用               | 启用后                                |
| ---------- | -------------------- | ------------------------------------- |
| 诚信验证   | 单模型 100% 检查     | + 30% 样本由第二模型独立验证          |
| 魔鬼代言人 | 单模型 DA            | + 跨模型独立 critique，新发现自动加入 |
| 同侪审查   | 5 位审稿人（同模型） | + 来自第二模型的独立 DA critique      |

没有设定 `ARS_CROSS_MODEL`？一切照旧运作，无任何额外开销。

---

## 实际产出展示

查看完整 10 阶段 pipeline 的实际产出 — 包含**同侪审查报告、诚信验证报告、完稿论文**：

**[浏览所有 pipeline 产出 →](examples/showcase/)**

| 产出物                                                                | 说明                                                         |
| --------------------------------------------------------------------- | ------------------------------------------------------------ |
| [完稿论文（英文）](examples/showcase/full_paper_apa7.pdf)                | APA 7.0 格式，LaTeX 编译                                     |
| [完稿论文（中文）](examples/showcase/full_paper_zh_apa7.pdf)             | 中文版，APA 7.0                                              |
| [诚信报告 — 审稿前](examples/showcase/integrity_report_stage2.5.pdf)    | Stage 2.5：抓出 15 个虚构引用 + 3 个统计错误                 |
| [诚信报告 — 最终](examples/showcase/integrity_report_stage4.5.pdf)      | Stage 4.5：确认零回归                                        |
| [同侪审查第一轮](examples/showcase/stage3_review_report.pdf)             | 主编 + 3 审查者 + 魔鬼代言人                                 |
| [复审](examples/showcase/stage3prime_rereview_report.pdf)                | 修订后验证审查                                               |
| [同侪审查第二轮](examples/showcase/stage3_review_report_r2.pdf)          | 追踪审查                                                     |
| [回复审查意见](examples/showcase/response_to_reviewers_r2.pdf)           | 逐点回复                                                     |
| [出版后稽核报告](examples/showcase/post_publication_audit_2026-03-09.md) | 独立全引用稽核：发现 21/68 篇问题，通过了 3 轮诚信审查仍漏网 |

---

## 效能说明

> **建议模型：Claude Opus 4.6**，搭配 **Max plan**（或同等的延伸思考设定）。
>
> 完整学术 pipeline（10 阶段）会消耗**大量 token** — 单次完整执行可能超过 200K 输入 + 100K 输出 token，视论文长度和修订轮数而定。请依预算斟酌使用。
>
> 单独使用个别 skill（如只用 `deep-research` 或 `academic-paper-reviewer`）的消耗明显较少。

### 各模式 Token 消耗估算

| Skill / 模式                        | 输入 Token       | 输出 Token       | 估算费用（Opus 4.6） |
| ----------------------------------- | ---------------- | ---------------- | -------------------- |
| `deep-research` socratic          | ~30K             | ~15K             | ~$0.60               |
| `deep-research` full              | ~60K             | ~30K             | ~$1.20               |
| `deep-research` systematic-review | ~100K            | ~50K             | ~$2.00               |
| `academic-paper` plan             | ~40K             | ~20K             | ~$0.80               |
| `academic-paper` full             | ~80K             | ~50K             | ~$1.80               |
| `academic-paper-reviewer` full    | ~50K             | ~30K             | ~$1.10               |
| `academic-paper-reviewer` quick   | ~15K             | ~8K              | ~$0.30               |
| **完整 pipeline（10 阶段）**  | **~200K+** | **~100K+** | **~$4-6**      |
| + 跨模型验证                        | +~10K（外部）    | +~5K（外部）     | +~$0.60-1.10         |

*以 ~15,000 字论文、~60 篇引用为基准估算。实际消耗随论文长度、修订轮数、对话深度而异。*

### 建议设定

为获得最佳使用体验，建议启用以下 Claude Code 功能：

| 设定                       | 功能说明                                                                        | 启用方式                                                    | 官方文件                                                                                                                                           |
| -------------------------- | ------------------------------------------------------------------------------- | ----------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Agent Team**       | 产生子代理（subagent）平行执行研究、撰写、审查 — 多 Agent pipeline 的核心机制  | 设定 `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`（研究预览） | 实验性功能 — 尚无稳定文件                                                                                                                         |
| **Ralph Loop**       | 在长时间 pipeline 阶段保持 session 持续运作，让 Claude 能自主执行而不会逾时中断 | 使用 `/ralph-loop` 启动                                   | 社群插件 — 实验性                                                                                                                                 |
| **Skip Permissions** | 跳过每次工具使用的确认提示，实现全 pipeline 不中断的自主执行                    | 启动时加上 `claude --dangerously-skip-permissions`        | [Permissions](https://docs.anthropic.com/en/docs/claude-code/cli-reference) · [Advanced Usage](https://docs.anthropic.com/en/docs/claude-code/advanced) |

> **⚠️ Skip Permissions 注意事项**：此旗标会停用所有工具使用的确认对话框。请自行斟酌使用 — 在可信任的长时间 pipeline 中非常方便，但会移除手动审核的安全机制。仅在你确定接受 Claude 自动执行档案读写、shell 指令等操作时才启用。

---

## 前置需求

### 安装 Claude Code

**建议：原生安装程式**（不需要 Node.js，自动更新）：

```bash
# macOS / Linux
curl -fsSL https://claude.ai/install.sh | bash

# Windows（PowerShell）
irm https://claude.ai/install.ps1 | iex
```

<details>
<summary>替代方案：npm 安装（已弃用）</summary>

需要 Node.js 18+。

```bash
npm install -g @anthropic-ai/claude-code
```

</details>

### 设定 API Key

你需要一个 Anthropic API key，请至 https://console.anthropic.com/ 取得。

```bash
# Claude Code 首次执行时会提示输入 API key
claude
```

或设定环境变数：

```bash
export ANTHROPIC_API_KEY=sk-ant-xxxxx
```

### LaTeX / PDF 输出（选用）

PDF 输出需要 [tectonic](https://tectonic-typesetting.github.io/) 和特定字型。**这是选用的** — MD 和 DOCX 输出不需要这些。

```bash
# macOS
brew install tectonic

# Linux (Debian/Ubuntu)
curl --proto '=https' --tlsv1.2 -fsSL https://drop-sh.fullyjustified.net | sh
```

**所需字型**（APA 7.0 中文输出）：

- **Times New Roman** — macOS/Windows 通常已内建；Linux 安装 `ttf-mscorefonts-installer`
- **思源宋体 VF**（Source Han Serif TC VF）— 从 [Google Fonts](https://fonts.google.com/specimen/Noto+Serif+TC) 或 [Adobe GitHub](https://github.com/adobe-fonts/source-han-serif) 下载
- **Courier New** — 通常已内建

> 如果只需要 MD/DOCX 输出，可完全跳过此步骤。Pipeline 会在尝试 LaTeX 编译前先询问。

---

## 安装方式

### 方法一：作为专案 Skills（推荐）

将此 repo clone 到专案的 `.claude/skills/` 目录：

```bash
# 切换到你的专案根目录
cd /path/to/your/project

# 建立 skills 目录（若不存在）
mkdir -p .claude/skills

# Clone skills
git clone https://github.com/Imbad0202/academic-research-skills.git .claude/skills/academic-research-skills
```

接着将 `.claude/CLAUDE.md` 的内容复制到你专案的 `.claude/CLAUDE.md`（若已有则合并）。

> **全域安装：** 若希望所有专案都能使用这些 skills，可安装到 `~/.claude/skills/`：
>
> ```bash
> mkdir -p ~/.claude/skills
> git clone https://github.com/Imbad0202/academic-research-skills.git ~/.claude/skills/academic-research-skills
> ```

### 方法二：作为独立专案

```bash
# Clone repo
git clone https://github.com/Imbad0202/academic-research-skills.git

# 进入专案
cd academic-research-skills

# 启动 Claude Code
claude
```

<details>
<summary><strong>没有安装 Git？</strong>直接下载 ZIP</summary>

1. 前往 https://github.com/Imbad0202/academic-research-skills
2. 点击绿色 **Code** 按钮 → **Download ZIP**
3. 解压缩到你想要的位置
4. 方法一：将解压后的资料夹移动到你专案内的 `.claude/skills/academic-research-skills`
5. 独立使用：在解压后的资料夹中开启终端机，执行 `claude`

</details>

### 方法三：Claude Cowork（桌面版）

在 [Claude Cowork](https://claude.com/product/cowork) 中使用这些 skills — Claude Desktop 的 AI 自主工作区。

**选项 A：资料夹存取（最快）**

1. 将此 repo clone 到本机：
   ```bash
   git clone https://github.com/Imbad0202/academic-research-skills.git ~/academic-research-skills
   ```
2. 开启 Claude Desktop → 点击上方 **Cowork** 分页
3. 选择 clone 下来的 `academic-research-skills` 资料夹作为工作目录
4. Claude 会自动从 `SKILL.md` 侦测并载入 skills

**选项 B：作为专案 Skills**

若你已有 Cowork 专案资料夹：

```bash
cd /path/to/your/project
mkdir -p .claude/skills
git clone https://github.com/Imbad0202/academic-research-skills.git .claude/skills/academic-research-skills
```

Skills 会在对话相关时自动载入 — 例如说「帮我写论文」会触发 `academic-paper`。

**需求：**

- Claude Desktop（最新版本）且已启用 Cowork
- 付费方案（Pro、Max、Team 或 Enterprise）

### 方法四：上传至 claude.ai

claude.ai 的 Project 功能可以载入这些 skills，不需要安装 Claude Code。

**步骤：**

1. 从这个 repo 下载所有 `SKILL.md` 档案（共 4 个）：

   - `deep-research/SKILL.md`
   - `academic-paper/SKILL.md`
   - `academic-paper-reviewer/SKILL.md`
   - `academic-pipeline/SKILL.md`
2. 登入 [claude.ai](https://claude.ai)
3. 建立新 Project：

   - 点击左侧栏 **Projects** → **Create Project**
   - 命名为「Academic Research」（或任意名称）
4. 上传 SKILL.md 档案：

   - 进入 Project → 点击 **Project Knowledge**（右侧面板）
   - 点击 **Add Content** → **Upload Files**
   - 上传 4 个 `SKILL.md` 档案
5. （选用）上传 reference 和 template 档案以获得更好效果：

   - `deep-research/references/` 下的档案（APA 指南、方法论模板等）
   - `academic-paper/references/` 下的档案（引用格式、写作风格等）
   - `academic-paper/templates/` 下的档案（论文结构模板）
6. 开始对话：在 Project 中开启新对话，直接说「引导我研究 X」或「帮我写论文」

**claude.ai 限制：**

- Project Knowledge 档案大小上限为每个档案 200KB
- SKILL.md 的 YAML frontmatter 中 `version` 和 `last_updated` 必须在 `metadata:` 下，否则上传会失败
- claude.ai 不支援多 agent 平行执行，效果不如 Claude Code 完整
- 建议至少上传 4 个 SKILL.md + 核心 references，以获得最佳效果

---

## 使用方式

### 快速开始

```
# 启动完整研究 pipeline
你: "我想做一篇关于 AI 对高教品保影响的研究论文"

# 苏格拉底引导模式
你: "引导我研究 AI 在教育评鉴中的应用"

# 引导式论文撰写
你: "引导我写一篇关于少子化影响的论文"

# 审查现有论文
你: "帮我审查这篇论文"（接着提供论文）

# 查看 pipeline 进度
你: "进度" 或 "status"
```

### 个别 Skill 使用

#### Deep Research（深度研究，7 种模式）

```
"研究 AI 对高等教育的影响"                    → full mode（完整研究）
"给我一份 X 的快速摘要"                       → quick mode（快速简报）
"帮我做 X 的系统性文献回顾，含 PRISMA"        → systematic-review mode（新增）
"引导我研究 X"                                → socratic mode（苏格拉底引导）
"帮我查核这些说法"                            → fact-check mode（事实查核）
"帮我做文献回顾"                              → lit-review mode（文献回顾）
"审查这篇论文的研究品质"                      → review mode（论文审查）
```

#### Academic Paper（学术论文撰写，9 种模式）

```
"帮我写一篇论文"                              → full mode（完整撰写）
"引导我写论文"                                → plan mode（引导规划）
"我有初稿，这是审稿意见"                      → revision mode（修订）
"帮我整理这些审稿意见成修订路线图"            → revision-coach mode（新增）
"转换成 LaTeX" / "引用格式转 IEEE"            → format-convert mode（格式转换）
"检查引用格式"                                → citation-check mode（引用检查）
"写一份中英双语摘要"                          → bilingual-abstract mode（双语摘要）
"润饰我的写作风格"                            → writing-polish mode（写作润饰）
"自动完成整篇论文"                            → full-auto mode（全自动撰写）
```

#### Academic Paper Reviewer（论文审查，5 种模式）

```
"审查这篇论文"                                → full mode（主编 + R1/R2/R3 + 魔鬼代言人）
"快速评估这篇论文"                            → quick mode（快速评估）
"引导我改进这篇论文"                          → guided mode（引导改进）
"检查研究方法"                                → methodology-focus mode（方法论聚焦）
"验收修订"                                    → re-review mode（再审验收）
```

#### Academic Pipeline（全流程调度器）

```
"我想做一篇完整的研究论文"                    → 从 Stage 1 开始完整 pipeline
"我已经有论文，帮我审查"                      → 从 Stage 2.5 进入（先做诚信审查）
"我收到审稿意见了"                            → 从 Stage 4 进入
```

> Pipeline 结束时自动产出 **Stage 6：过程纪录** — 含论文创建过程纪录与 6 维度协作品质评估（1–100 分）。

### 支援语言

- **繁体中文** — 使用者以中文对话时预设使用
- **English** — 使用者以英文对话时预设使用
- 学术论文自动产出双语摘要（中文 + English）

> **使用其他语言？** 苏格拉底模式（deep-research）和 Plan 模式（academic-paper）采用**意图匹配**启动 — 侦测你的请求含义，而非比对特定关键字。这代表它们**支援任何语言**，无需额外设定。
>
> 不过，一般的 `Trigger Keywords` 区块（决定 skill 是否被启动）仍以英文和繁体中文为主。如果你发现 skill 在你的语言下触发不稳定，可以在各 `SKILL.md` 的 `### Trigger Keywords` 区块中加入你的语言的关键字，提高匹配信心。

### 支援引用格式

- APA 7.0（预设，含中文引用规则）
- Chicago（Notes & Author-Date）
- MLA
- IEEE
- Vancouver

### 支援论文结构

- IMRaD（实证研究）
- 主题式文献回顾
- 理论分析
- 个案研究
- 政策简报
- 研讨会论文

---

## Skill 详细资讯

### Deep Research (v2.7)

13 个 Agent 的严谨学术研究 pipeline：

| Agent                     | 角色                                                        |
| ------------------------- | ----------------------------------------------------------- |
| Research Question Agent   | FINER 评分的研究问题制定                                    |
| Research Architect        | 研究方法设计                                                |
| Bibliography Agent        | 系统性文献搜寻                                              |
| Source Verification Agent | 证据分级、掠夺性期刊侦测                                    |
| Synthesis Agent           | 跨来源整合                                                  |
| Report Compiler           | APA 7.0 报告撰写 + 风格校准 + 写作品质检查（可选）          |
| Editor-in-Chief           | Q1 期刊主编审查                                             |
| Devil's Advocate          | 假设挑战（3 个检查点）                                      |
| Ethics Review Agent       | AI 揭露、引用诚信                                           |
| Socratic Mentor           | 苏格拉底引导式研究对话，含收敛准则 + SCR 反思机制（可开关） |
| Risk of Bias Agent        | RoB 2 + ROBINS-I 偏误风险评估                               |
| Meta-Analysis Agent       | 效果量、异质性、森林图、GRADE                               |
| Monitoring Agent          | Pipeline 完成后的文献监测警报                               |

**模式：** full、quick、paper-review、lit-review、fact-check、socratic、**systematic-review**（新增）

### Academic Paper (v2.8)

12 个 Agent 的学术论文撰写 pipeline：

| Agent                 | 角色                                                                                         |
| --------------------- | -------------------------------------------------------------------------------------------- |
| Intake Agent          | 组态访谈 + 上游衔接侦测 + 风格校准（可选）                                                   |
| Literature Strategist | 搜寻策略 + 注释书目                                                                          |
| Structure Architect   | 论文大纲 + 字数分配                                                                          |
| Argument Builder      | 论点 + 主张-证据链                                                                           |
| Draft Writer          | 逐章撰写 + 写作品质检查 + 风格校准套用                                                       |
| Citation Compliance   | 多格式引用审核 + APA↔Chicago↔MLA↔IEEE↔Vancouver 转换                                     |
| Abstract Bilingual    | 中英双语摘要                                                                                 |
| Peer Reviewer         | 5 维度审查（最多 2 轮）                                                                      |
| Formatter             | LaTeX/DOCX/PDF 输出 — 强制 `apa7` class、XeCJK 双语、`ragged2e` 对齐修正、tectonic 编译 |
| Socratic Mentor       | 逐章引导规划，含收敛准则 + SCR 反思机制（可开关）                                            |
| Visualization Agent   | 9 种图表类型、matplotlib/ggplot2、APA 7.0 标准                                               |
| Revision Coach Agent  | 解析非结构化审稿意见 → 修订路线图                                                           |

**模式：** full、plan、revision、citation-check、format-convert、bilingual-abstract、writing-polish、full-auto、**revision-coach**（新增）

### Academic Paper Reviewer (v1.7)

7 个 Agent 的多视角审查，搭配 **0-100 品质量表**：

| Agent                     | 角色                                     |
| ------------------------- | ---------------------------------------- |
| Field Analyst             | 辨识领域、配置审查者 persona             |
| Editor-in-Chief           | 期刊适配性、新颖性、重要性               |
| Methodology Reviewer      | 研究设计、统计、可重现性                 |
| Domain Reviewer           | 文献涵盖率、理论框架                     |
| Perspective Reviewer      | 跨领域观点、实务影响                     |
| Devil's Advocate Reviewer | 核心论点挑战、逻辑谬误侦测、最强反论     |
| Editorial Synthesizer     | 共识分析、修订路线图、**量表评分** |

**模式：** full、re-review（验收）、quick、methodology-focus、guided

**决策对照：** ≥80 接受、65-79 小修、50-64 大修、<50 退稿

### Academic Pipeline (v3.0)

10 阶段调度器，含诚信验证、两阶段审查、苏格拉底指导、协作品质评估：

| 阶段                        | Skill                                  | 目的                                                   |
| --------------------------- | -------------------------------------- | ------------------------------------------------------ |
| 1. 研究                     | deep-research                          | 厘清研究问题、搜寻文献                                 |
| 2. 撰写                     | academic-paper                         | 撰写论文初稿                                           |
| **2.5. 诚信审查**     | **integrity_verification_agent** | **100% 引用与数据验证（v2.0：反幻觉强制令）**    |
| 3. 审稿                     | academic-paper-reviewer                | 5 人审查（主编 + R1/R2/R3 + 魔鬼代言人）               |
| →                          | *苏格拉底修订指导*                   | *引导使用者理解审稿意见*                             |
| 4. 修订                     | academic-paper                         | 回应审稿意见                                           |
| 3'. 再审                    | academic-paper-reviewer                | 验收修订内容                                           |
| →                          | *苏格拉底残余指导*                   | *引导处理剩余问题（若为 Major）*                     |
| 4'. 再修订                  | academic-paper                         | 最终修订（若需要）                                     |
| **4.5. 最终诚信审查** | **integrity_verification_agent** | **100% 最终验证（零问题要求）**                  |
| 5. 定稿                     | academic-paper                         | 询问格式风格 → MD + DOCX + LaTeX → tectonic → PDF   |
| **6. 过程纪录**       | **pipeline**                     | **论文创建过程纪录 + 协作品质评估（1–100 分）** |

**Pipeline 保证：**

- 每个阶段都需使用者确认 checkpoint
- 诚信验证（Stage 2.5 + 4.5）不可跳过
- 可重现 — 标准化流程，含完整稽核轨迹
- Pipeline 完成后自动产出协作品质评估，含 6 维度诚实评分
- 每次 stage 转换注入中途强化（IRON RULE + Anti-Pattern 提醒）
- R&R 追溯矩阵（Schema 11）独立验证作者修订宣称

---

## 授权条款

本作品采用 [CC-BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) 授权。

**你可以自由：**

- 分享 — 复制及散布本作品
- 改作 — 重混、转换、以本作品为基础进行创作

**惟须遵守以下条件：**

- **姓名标示** — 你必须给予适当的标示
- **非商业性** — 你不得将本作品用于商业目的

**标示格式：**

```
Based on Academic Research Skills by Cheng-I Wu
https://github.com/Imbad0202/academic-research-skills
```

---

## 贡献者

**吴政宜** (Cheng-I Wu) — 作者与维护者

**[aspi6246](https://github.com/aspi6246)** — 贡献者。v3.1 优化灵感来自 [Claude-Code-Skills-for-Academics](https://github.com/aspi6246/Claude-Code-Skills-for-Academics)：唯读约束模式、Anti-Pattern 作为一等公民设计、认知框架方法（教「如何思考」而非只有步骤）、精简 skill 尺寸哲学。

---

## 更新纪录

### v3.1 (2026-04-06) — 抗 Context Rot + 认知框架 + 精简尺寸

灵感来自 [aspi6246/Claude-Code-Skills-for-Academics](https://github.com/aspi6246/Claude-Code-Skills-for-Academics)。

**Wave 1：抗 Context Rot 锚定**

- 4 个 skill 共 29 条 Anti-Patterns（每个 7-8 条，表格含「为何失败」+「正确行为」）
- 22 个 IRON RULE 标记，确保长对话中关键规则不被遗忘
- 审查者唯读约束（reviewer 不可修改论文原稿）

**Wave 2：追溯性 + 认知框架 + 中途强化**

- R&R 追溯矩阵（Schema 11）：Re-Review 新增「作者声称」+「已验证？」栏位，独立核实修订宣称
- 3 个认知框架 reference 档案，教 agent「如何思考」而非只是「做什么」：
  - 论证与推理框架（Toulmin 模型、Bradford Hill 因果推理、最佳解释推论、认知状态分类）
  - 审查品质思维框架（三镜头法、常见审查陷阱、校准问题）
  - 写作判断力框架（清晰度测试、读者旅程、学科语态、修订决策矩阵）
- 中途强化机制：每次 stage 转换注入对应 IRON RULE + Anti-Pattern 提醒
- FULL checkpoint 前的 5 题自我检查（引用完整性、谄媚让步、品质轨迹、范围纪律、完整性）

**Wave 3：精简 Skill 尺寸**

- SKILL.md 总大小从 142KB 降至 85KB（-40%），详细协议移至 `references/` 按需载入
- 新增 ~15 个 reference 档案（re-review protocol、guided mode、systematic review、process summary 等）
- 所有 IRON RULE 保留在 SKILL.md；详细内容按需载入
- 新版本：deep-research v2.7、academic-paper v2.8、academic-paper-reviewer v1.7、academic-pipeline v3.0

### v3.0 (2026-04-03) — 反谄媚 + 意图侦测 + 跨模型验证 + AI 自我反思

- **魔鬼代言人让步门槛**（deep-research + academic-paper-reviewer）：反驳必须评分 1-5。≥4 才允许让步。不允许连续让步。让步率追踪。框架锁定侦测。
- **攻击强度保持**（academic-paper-reviewer）：DA 不因被反驳而软化。反驳评估协议含偏移侦测。
- **意图侦测层**（deep-research socratic）：侦测探索型 vs. 目标型。探索模式停用自动收束，最大轮数提升至 60。每 5 轮重新评估。
- **对话健康度指标**（deep-research socratic）：每 5 轮静默自检，侦测持续同意、回避冲突、过早收束。侦测到模式时自动注入挑战性问题。
- **跨模型验证协议**（shared，可选）：用 GPT-5.4 Pro 或 Gemini 3.1 Pro 作为独立第二审查者。诚信验证 30% 抽样跨模型检查。DA 获得跨模型独立 critique。设定 `ARS_CROSS_MODEL` 环境变数启用——未设定时零开销。完整设定指南见 `shared/cross_model_verification.md`。
- **AI 自我反思报告**（academic-pipeline Stage 6）：Pipeline 结束后 AI 行为自评——DA 让步率、健康警报、谄媚风险评级（LOW/MEDIUM/HIGH）、框架锁定事件。
- 来源：四轮辩证实验中发现 DA 让步太快、苏格拉底模式过早收束、整个辩论锁定在人类设定的框架中。
- 版本：deep-research v2.5、academic-paper-reviewer v1.5、academic-pipeline v2.8

### v2.9.1 (2026-04-03) — Skill Metadata

- 为 4 个 SKILL.md 加入 `status: active` 和 `related_skills` 交叉引用
- 支援 skill 探索工具及跨技能导航

### v2.9 (2026-03-27) — 风格校准 + 写作品质检查

- **风格校准**（academic-paper intake Step 10，可选）：提供 3+ 篇过去论文，pipeline 会学习你的写作风格 — 句子节奏、词汇偏好、引用整合方式。写作时作为软性指引；学科规范永远优先。优先级系统：学科规范（硬性）> 期刊惯例（强）> 个人风格（软性）。见 `shared/style_calibration_protocol.md`
- **写作品质检查**（`academic-paper/references/writing_quality_check.md`）：写作品质 checklist，于初稿自我审查时套用。5 大类：AI 高频词汇警告（25 个词）、标点模式控制（em dash ≤3）、开头废话侦测、结构模式警告（三项列举强迫症、均匀段落、同义词循环）、句子长度变化检查。这是好写作规则 — 不是逃避侦测
- **Style Profile** 透过 academic-pipeline Material Passport 携带（`shared/handoff_schemas.md` Schema 10）
- **deep-research** report compiler 也可选地消费这两个功能
- 版本：academic-paper v2.5、deep-research v2.4、academic-pipeline v2.7

### v2.8 (2026-03-22) — SCR Loop Phase 1：State-Challenge-Reflect 反思机制

- **Socratic Mentor Agent**（deep-research + academic-paper）：整合 SCR（表态-挑战-反思）协议
  - **Commitment Gate**：在每个层级/章节转换前收集使用者预测，再呈现资料
  - **Certainty-Triggered Contradiction**：侦测高信心语句（「显然」「毫无疑问」），自动引入反面观点
  - **Adaptive Intensity**：追踪 commitment 准确率，动态调整挑战频率
  - **Self-Calibration Signal (S5)**：新收敛讯号，追踪使用者在对话中是否展现自我校准能力
  - **SCR Switch**：使用者可随时说「跳过预测」关闭 SCR，或「恢复预测」重新开启，苏格拉底式提问不受影响
- `deep-research/references/socratic_questioning_framework.md`：新增 SCR Overlay Protocol，对映 SCR 三阶段到苏格拉底功能
- 新增 `CHANGELOG.md`

### v2.7 (2026-03-09) — 诚信验证 v2.0：反幻觉全面改版

- **integrity_verification_agent v2.0**：Anti-Hallucination Mandate（禁止靠 AI 记忆验证）、消除灰色地带分类（仅 VERIFIED/NOT_FOUND/MISMATCH）、强制 WebSearch audit trail、Stage 4.5 独立全面验证、Gray-Zone Prevention Rule
- **已知引用幻觉 Pattern**：5 类分类法（TF/PAC/IH/PH/SH，来自 GPTZero × NeurIPS 2025 研究）、5 种复合欺骗模式、实战案例、文献统计
- **出版后稽核**：对全部 68 篇引用做 WebSearch 逐一验证，发现 21 篇有问题（31% 错误率），证明外部查证的必要性
- **论文修正**：移除 4 篇捏造引用、修正 6 篇作者错误、修正 7 篇书目细节、修正 2 篇格式问题

### v2.6.2 (2026-03-09) — 意图匹配模式启动

- **deep-research**：苏格拉底模式改为**意图匹配**启动，取代关键字比对。支援任何语言 — 侦测含义（如「使用者想要引导式思考」）而非比对特定字串。
- **academic-paper**：Plan 模式改为**意图匹配**启动。侦测意图信号如「使用者不确定如何开始」「使用者想要逐步引导」，不限语言。
- 两个模式新增**预设规则**：当意图模糊时，偏好 `socratic`/`plan` 而非 `full` — 先引导比较安全。
- 双层架构：Layer 1（skill 启动）用双语关键字提高匹配信心；Layer 2（mode 路由）用语言无关的意图信号。

### v2.6.1 (2026-03-09) — 双语触发关键字

- **deep-research**：新增繁体中文触发关键字，涵盖一般启动和苏格拉底模式。
- **academic-paper**：新增繁体中文触发关键字及 Plan Mode 触发区块。
- 两份 mode selection guide 加入双语范例及中文专属误选情境。

### v2.6 / v2.4 / v1.4 (2026-03-08) — 15+ 项改进

- **deep-research v2.3**：新增系统性文献回顾 / PRISMA 模式（第 7 模式）；3 个新 agent（risk_of_bias、meta_analysis、monitoring）；PRISMA 协议/报告模板；苏格拉底收敛准则（4 讯号 + 自动结束）；快速模式选择指南
- **academic-paper v2.4**：2 个新 agent（visualization、revision_coach）；修订追踪模板含 4 种状态；引用格式转换（APA↔Chicago↔MLA↔IEEE↔Vancouver）；统计视觉化标准；苏格拉底收敛准则；修订复原范例；**LaTeX 输出强化** — 强制 `apa7` document class、`ragged2e` + `etoolbox` 文字对齐修正、表格栏宽公式、双语摘要置中、标准字体集（Times New Roman + 思源宋体 VF + Courier New）、仅 tectonic 编译 PDF
- **academic-paper-reviewer v1.4**：0-100 品质量表含行为指标；决策对照（≥80 接受、65-79 小修、50-64 大修、<50 退稿）；快速模式选择指南
- **academic-pipeline v2.6**：自适应 checkpoint（FULL/SLIM/MANDATORY）；Phase E 宣称验证；素材护照（Material Passport）支援中途进入；跨 skill 模式顾问（14 情境）；团队协作协议；强化衔接 schema（9 个含验证规则）；诚信审查失败复原范例

### v2.4 / v1.3 (2026-03-08)

- **academic-pipeline v2.4**：新增 Stage 6 过程纪录 — 自动生成结构化论文创建过程纪录（MD → LaTeX → PDF，中英双语）；必含最后一章：**协作品质评估**，6 个维度各计 1–100 分（方向设定、智识贡献、品质把关、迭代纪律、委派效率、后设学习），含诚实回馈与改进建议；pipeline 从 9 阶段扩展为 10 阶段

### v2.3 / v1.3 (2026-03-08)

- **academic-pipeline v2.3**：Stage 5 定稿阶段现在会先询问格式风格（APA 7.0 / Chicago / IEEE）；PDF 必须从 LaTeX 经 `tectonic` 编译（禁止 HTML-to-PDF）；APA 7.0 使用 `apa7` document class（`man` 模式）+ XeCJK 支援中英双语；字体：Times New Roman + 思源宋体 VF + Courier New

### v2.2 / v1.3 (2025-03-05)

- **跨 Agent 品质对齐**：统一定义（同侪审查、时效规则、CRITICAL 严重度、来源分级）横跨所有 agent
- **deep-research v2.2**：synthesis 反模式、苏格拉底自动结束条件、DOI+WebSearch 验证、强化伦理诚信审查、模式转换矩阵
- **academic-paper v2.2**：4 级论证强度评分、抄袭筛查、2 个新失败路径（F11 退稿复活、F12 研讨会转期刊）、Plan→Full 模式转换
- **academic-paper-reviewer v1.3**：DA vs R3 角色边界、CRITICAL 判定标准、共识分类（4/3/SPLIT/DA-CRITICAL）、信心分数加权、亚洲与区域期刊参考
- **academic-pipeline v2.2**：checkpoint 确认语意、模式切换矩阵、技能失败降级策略、状态所有权协议、素材版本控制

### v2.0.1 (2026-03)

- **精简 4 个 SKILL.md**（-371 行, -16.5%）：移除跨 skill 重复、内嵌模板改为档案引用、冗余路由表、重复模式选择区块
- 修复 academic-paper 与 academic-pipeline 之间修订回圈上限的矛盾

### v2.0 (2026-02)

- **academic-pipeline v2.0**：5→9 阶段、强制诚信验证、两阶段审查、苏格拉底修订指导、可重现性保证
- **academic-paper-reviewer v1.1**：+魔鬼代言人审查者（第 7 agent）、+re-review 模式（验收）、+审后苏格拉底指导
- 新增 agent：`integrity_verification_agent` — 100% 引用/数据验证，含稽核轨迹
- 新增 agent：`devils_advocate_reviewer_agent` — 8 维度论点挑战
- 输出顺序：MD + DOCX → 询问 LaTeX → 确认 → PDF

### v1.0 (2026-02)

- 初版发布
- deep-research v2.0（10 agents、6 模式含 socratic）
- academic-paper v2.0（10 agents、8 模式含 plan）
- academic-paper-reviewer v1.0（6 agents、4 模式含 guided）
- academic-pipeline v1.0（调度器）
