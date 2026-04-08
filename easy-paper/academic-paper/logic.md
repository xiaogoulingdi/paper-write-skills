# Academic Paper 工作流解析 (Logic Review)

本文件是对 `easy-paper/academic-paper/` 目录下所有组件的梳理与说明。这个目录是论文写作的核心枢纽，包含了从构思、撰写、文献引用到最终排版定稿的完整工具链。

## 1. 智能体目录 (`agents/`)

`agents` 包含了多个不同职责的 AI 智能体“人设”。在写作的不同阶段，系统会调用对应专长的智能体。

*   **`abstract_bilingual_agent.md`**: 中英双语摘要生成专家。擅长根据正文提炼核心摘要。
*   **`argument_builder_agent.md`**: 论点构建专家。负责帮助梳理论点逻辑和文章说理过程。
*   **`citation_compliance_agent.md`**: 引用合规审查员。专门检查论文中的交叉引用以及参考文献格式是否规范。
*   **`draft_writer_agent.md`**: 草稿撰写核心代笔。用于长文本段落输出，将零散思路扩展成有血有肉的学术正文。
*   **`formatter_agent.md`**: 格式排版整理员。负责根据指定模板（如 Markdown 或 LaTeX）输出成最终展示格式。
*   **`intake_agent.md`**: 需求接收引导员。用于最初接收用户的写作指令并进行任务拆解与指派。
*   **`literature_strategist_agent.md`**: 文献策略专家。分析参考文献，指导你在当前段落该如何安插、组合这些引文以加强论点。
*   **`peer_reviewer_agent.md`**: 初级同行评审员。在写完后充当第一道审稿关卡，提供基本反馈。
*   **`revision_coach_agent.md`**: 修改教练。根据反馈意见指导并修改已写好的草稿。
*   **`socratic_mentor_agent.md`**: 苏格拉底导师。不直接给你答案，而是通过提问引导你优化论文核心逻辑（破除卡壳）。
*   **`structure_architect_agent.md`**: 结构架构师。专门负责把控论文大纲，帮你拆解出合理的一、二、三级目录。
*   **`visualization_agent.md`**: 可视化专家。协助整理数据图表的描述与图注，或提供绘图思路。

## 2. 范例目录 (`examples/`)

`examples` 目录提供了各种写作模式下，AI 和用户一问一答、高质量工作的极佳实战范例（Prompt 参考）。

*   **`chinese_paper_example.md`**: 中文论文产出的参考案例。
*   **`imrad_hei_example.md`**: 基于 IMRAD（引言、方法、结果、讨论）结构和高等教育类 (HEI) 领域的案例。
*   **`literature_review_example.md`**: 文献综述类型的写作范例。
*   **`plan_mode_guided_writing.md`**: “计划模式”下的引导式写作范例（分步骤一步步写大纲再写正文）。
*   **`revision_mode_example.md`**: 教你如何根据审稿意见进行修改的范例。
*   **`revision_recovery_example.md`**: 论文大修/被拒后重建论点进行补救的案例。

## 3. 参考知识库 (`references/`)

`references` 相当于各位 Agent 的“参考教科书”。AI 工作时会随时调取此处的学术规章制度。

*   **指南与建议**: `abstract_writing_guide.md` (摘要指南)、`academic_writing_style.md` (学术语调风格)。
*   **格式与引用规范**: `apa7_chinese_citation_guide.md` (APA 第七版中文规范)、`apa7_extended_guide.md` (APA 扩展)、`citation_format_switcher.md` (格式切换对照)。
*   **流程与模式规划**: `mode_selection_guide.md` (模式选择指南)、`plan_mode_protocol.md` (步骤分解协定)、`workflow_phase_details.md` (管线阶段定义)。
*   **出版与作者申明**: `credit_authorship_guide.md` (作者署名规范)、`funding_statement_guide.md` (资金说明指南)、`journal_submission_guide.md` (期刊投稿指南)。
*   **排版与评审标准**: `paper_structure_patterns.md` (文章模板分析)、`writing_judgment_framework.md` (写作评判框架)、`writing_quality_check.md` (质量检测)。
*   **其它**: `failure_paths.md` (记录可能出现的失败和防范)、`hei_domain_glossary.md` (高教领域术语表)、`latex_template_reference.md` (LaTeX 基础语法参考)、`statistical_visualization_standards.md` (统计学和图表可视化标准)。

## 4. 模板目录 (`templates/`)

`templates` 是预先搭好的框架骨骼，AI 生成内容后可直接灌入这些骨架。

*   **论文体裁模板**: `case_study_template.md` (案例研究)、`conference_paper_template.md` (会议论文)、`imrad_template.md` (IMRAD 实证论文)、`literature_review_template.md` (文献综述)、`policy_brief_template.md` (政策简报)、`theoretical_paper_template.md` (理论论文)。
*   **模块化模板**: `bilingual_abstract_template.md` (双语摘要)、`credit_statement_template.md` (CRediT 作者贡献说明)、`funding_statement_template.md` (资金声明)、`revision_tracking_template.md` (审稿意见追溯修改表)。
*   **导出格式模板**: `latex_article_template.tex` (标准的 LaTeX 文稿模板文件)。

---
*注：该文档旨在帮助使用者快速了解学术写作流 (`academic-paper`) 中各组件的位置与用途，无需逐一打开阅读便可掌握其内部协作逻辑。*