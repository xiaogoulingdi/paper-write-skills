# 深度研究工作流解析 (Deep Research Logic)

本文件是对 `easy-paper/deep-research/` 目录下所有组件的梳理。这是整个体系的最上游“研究引擎”。
它不负责写论文正文，而是负责在你动笔之前：**确立方向、检索文献、核实数据、评估偏倚风险、提炼核心观点**。

## 1. 智能体目录 (`agents/`)

这是一个由 13 种专业研究人员组成的科研智囊团：

*   **前期梳理与架构**
    *   **`socratic_mentor_agent.md`**: 苏格拉底导师。当你思路卡壳、不知道该研究什么时，它通过连环提问引导你破局。
    *   **`research_question_agent.md`**: 选题专家。将你模糊且宽泛的想法，收敛成一个具有可操作性、科学性的精准学术问题 (Research Question)。
    *   **`research_architect_agent.md`**: 架构师。为你制定研究方法草图（定性还是定量？用哪种数据收集手段？）。
*   **文献与数据搜集**
    *   **`bibliography_agent.md`**: 图书管理员。负责设计检索词，执行系统的文献搜集，生成带有注释的参考文献目录。
    *   **`source_verification_agent.md`**: 来源核查员。专门查证信息的真实性与出处。
    *   **`monitoring_agent.md`**: 论文追踪员。
*   **分析与评估**
    *   **`synthesis_agent.md`**: 综合分析师。把几十篇文献的观点交叉融合，找出共识与矛盾点。
    *   **`risk_of_bias_agent.md`**: 偏倚风险评估员。对文献质量进行审查，看前人的研究是否存在水分。
    *   **`meta_analysis_agent.md`**: 元分析专家。处理多个定量研究的数据综合。
    *   **`ethics_review_agent.md`**: 伦理审查员。检查研究是否合乎学术伦理规范。
    *   **`devils_advocate_agent.md`**: 魔鬼代言人。在研究阶段内部质疑你的假设。
*   **输出产物**
    *   **`report_compiler_agent.md`**: 报告汇编员。把研究结果浓缩成一份立项报告。
    *   **`editor_in_chief_agent.md`**: 主编。把控整体研究报告的基调。

## 2. 范例目录 (`examples/`)

*   **`systematic_review.md`**: 系统性文献综述流水线案例。
*   **`socratic_guided_research.md`**: 苏格拉底式发问引导完成的一套探索性对话。
*   **`fact_check_mode.md`**: 事实核查模式案例。
*   **`handoff_to_paper.md`**: 展示如何将完成的“研究成果”移交给下游的“写论文模块 (`academic-paper`)”。

## 3. 参考知识库 (`references/`)

研究人员遵从的硬核科学依据：
*   **指南与协议**: `prisma_2020_checklist.md` (PRISMA 综述指南)、`rob2_robins-i_guide.md` (偏倚风险评估工具)、`equator_reporting_guidelines.md` (卫生研究报告准则)。
*   **防误区指南**: `logical_fallacies.md` (常见逻辑谬误清单)、`cognitive_biases_checklist.md` (认知偏差自检表)、`failure_paths.md` (研究失败路径及防范)。
*   **框架与逻辑**: `argumentation_reasoning_framework.md` (论证推理框架)、`methodology_patterns.md` (方法论范式)、`interdisciplinary_bridges.md` (跨学科桥梁建立指南)。
*   **伦理体系**: `ethics_checklist.md` (学术伦理检查单)、`irb_decision_tree.md` (伦理审查委员会决策树)、`preregistration_guide.md` (研究预注册指引)。

## 4. 模板目录 (`templates/`)

提取文献和输出研究框架的展示骨架：
*   `annotated_bibliography_template.md`: 带注释的文献列表模板。
*   `research_brief_template.md`: 简短的研究成果摘要。
*   `research_report_template.md`: 长篇研究报告。
*   `systematic_review_protocol.md`: 系统性综述的执行协议。
*   `meta_analysis_summary_template.md` 等。