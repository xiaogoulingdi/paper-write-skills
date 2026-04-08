# 同行评审工作流解析 (Reviewer Logic)

本文件是对 `easy-paper/academic-paper-reviewer/` 目录下所有组件的梳理。这个目录是一个模拟真实世界顶级学术期刊的多视角同行评审系统 (Peer Review System)。
在完成论文初稿后，你可以通过调用这个系统来为自己的论文进行严格的“找茬”和“挑刺”。

## 1. 智能体目录 (`agents/`)

该目录下的智能体组成了一个完整的“编委会”和“审稿人”团队。

*   **`eic_agent.md`**: 主编 (Editor-in-Chief)。负责整体把控，判断论文是否符合目标期刊方向，权衡各审稿人的意见并做出最终决定（接收、大修、小修、拒稿）。
*   **`editorial_synthesizer_agent.md`**: 编辑助理/合成员。负责将多位盲审专家的零散意见汇总排版，撰写成一封专业的决定信。
*   **`field_analyst_agent.md`**: 领域分析师。在最开始接收论文时，判断论文的具体学科领域，从而自动为其指派匹配的虚拟审稿人。
*   **`methodology_reviewer_agent.md`**: 方法学评审专家。专门死磕你的研究设计、数据采集方式、统计分析方法是否严谨，寻找方法论上的硬伤。
*   **`domain_reviewer_agent.md`**: 领域理论专家。负责审视文章的文献综述是否遗漏了重要前沿、理论框架是否合理。
*   **`perspective_reviewer_agent.md`**: 跨视角评审专家。从更宏观的跨学科角度，评估论文的广泛应用价值与潜在社会影响。
*   **`devils_advocate_reviewer_agent.md`**: 魔鬼代言人 (杠精评委)。本项目最严苛的审稿人，不看优点，专门负责寻找文章核心论点中的逻辑漏洞、偷换概念和隐藏的致命弱点。

## 2. 范例目录 (`examples/`)

*   **`hei_paper_review_example.md`**: 高等教育类论文被这套系统完整评审的实战案例。
*   **`interdisciplinary_review_example.md`**: 跨学科论文审查案例。

## 3. 参考知识库 (`references/`)

审稿人们用于评判你的论文是否达标的“量刑标准”：
*   评判机制：`writing_judgment_framework.md` (写作评判框架)、`writing_quality_check.md` (写作质量检测)。
*   标准清单：`statistical_reporting_standards.md` (定量统计数据的报告标准)、`statistical_visualization_standards.md` (图表合规标准)。
*   出版要求：`top_journals_by_field.md` (各领域的重点期刊列表，用于评估论文的层级)、`apa7_extended_guide.md` 等。

## 4. 模板目录 (`templates/`)

生成的各种审稿报告的装填模板：
*   **`review_report_template.md`**: 格式化的单份盲审专家评审意见表。
*   **`editorial_decision_letter.md`**: 主编最终发给作者的官方Decision Letter。
*   **`revision_roadmap.md`**: 为作者生成的“修改路线图”，指导作者如何一步步修复被指出的问题。