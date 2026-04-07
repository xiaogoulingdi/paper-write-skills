# 项目架构概述 (Project Structure Review)

本项目 (Academic Research Skills) 是一个为 Claude Code 设计的综合学术研究技能包。其核心目标是自动化并辅助学术研究的各个阶段，从文献检索、草稿撰写、同行评审到最终论文定稿。

项目采用模块化的结构，将不同的功能划分为独立的「技能 (Skills)」，每个技能又由多个专门的子智能体 (Agents) 组成。

## 目录结构 (Directory Structure)

```text
.
├── academic-paper/           # 论文写作技能流
├── academic-paper-reviewer/  # 论文评审技能流
├── academic-pipeline/        # 完整学术工作流编排器
├── deep-research/            # 深度研究与文献分析技能流
├── shared/                   # 跨技能的共享协议与配置
├── examples/                 # 高级别的演示与用例展示
├── QUICKSTART.md             # 快速启动指南
└── README.md                 # 项目主说明文档
```

## 核心组件说明

### 1. 四大核心技能 (Core Skills)

项目将任务拆分为四个主要阶段/技能，每个目录下都包含一个 `SKILL.md` 作为该技能入口与规则定义：

- **`deep-research/` (深度研究)**
  - 职责：作为上游的研究引擎，负责调研、信息搜集、提取与文献审查。可以协助提炼研究问题（Socratic 模式）。
- **`academic-paper/` (论文写作)**
  - 职责：核心的论文生产引擎。包含构建论点、大纲规划、段落撰写、双语摘要等。可以通过提供大纲逐步撰写（Plan 模式）。
- **`academic-paper-reviewer/` (论文同行评审)**
  - 职责：多视角的自动化评审。包含模拟领域专家、方法学专家甚至「魔鬼代言人」(Devil's Advocate) 进行严格审稿。
- **`academic-pipeline/` (学术管线编排)**
  - 职责：全流程统筹者，将上述所有的单一环节连接成一条完整的流水线。

### 2. 技能内部结构 (Internal Structure of a Skill)

每个技能模块（如 `academic-paper/`）内部基本遵循统一的目录设计模式：

- **`SKILL.md`**: 定义该技能的用途、工作模式、路由规则和触发条件等核心元数据信息。
- **`agents/`**: 存放所有专注特定任务的 Prompt 脚本文件（例如 `socratic_mentor_agent.md`、`peer_reviewer_agent.md`）。每个 Agent 代表一个拥有特定人设与校验规则的 AI。
- **`templates/`**: 各种标准化输出的排版模板，如 Markdown 论文模板、LaTeX 模板 (如 `latex_article_template.tex`) 或资金声明模板。
- **`references/`**: 参考指南与标准说明文件。供 Agent 读取作为外部知识补充，比如 APA 引用格式指南、论文图表标准等。
- **`examples/`**: 此技能相关的最佳实践范例。

### 3. shared/ (共享区域)

负责处理各流程与 Agent 的交叉与协作，包含：
- `cross_model_verification.md`：跨模型双重验证协议。
- `handoff_schemas.md`：定义不同流程节点（如 deep-research 到 academic-paper）之间交接材料的标准数据格式。
- `style_calibration_protocol.md`：学术写作风格校准协议，用于保持输出统一的学术语调。

## 工作流协同机制 (Workflow Synergy)

典型的处理顺序通常由 `academic-pipeline` 调度，按如下步骤执行（详见根目录 `.claude/CLAUDE.md` 设定的 Pipeline）：

1. **研究发想 (deep-research)** 
2. **打样撰写 (academic-paper)**
3. **初评定稿 (academic-paper-reviewer)**
4. **修改跟进 (academic-paper revision mode + paper-reviewer loops)**
5. **格式校定与导出 (academic-paper format-convert)**
