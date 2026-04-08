---
name: project-init
description: "Initialize project profile for easy-paper. Generates USER_RESEARCH_PROFILE.md and aligns deep-research, academic-paper, and academic-paper-reviewer to one domain boundary. Triggers: initialize project, setup thesis profile, create research profile, initialize paper workspace, 初始化课题, 初始化配置, 创建课题配置."
metadata:
  version: "1.0"
  last_updated: "2026-04-08"
  status: active
  related_skills:
    - deep-research
    - academic-paper
    - academic-paper-reviewer
---

# Project Init

`project-init` is the workspace bootstrap skill for Easy Paper Toolkit.

It creates a single source of truth file at workspace root:

- `USER_RESEARCH_PROFILE.md`

Once this file exists, downstream skills load it before running their own agents.

## Why This Skill Exists

Without a profile file, writing and review agents may drift across domains, use inconsistent terms, or over-generalize. `project-init` avoids that by freezing domain boundaries up front.

## Included Assets

- `agents/profile_builder_agent.md`
  Role: collects user context and writes profile content using template.
- `templates/USER_RESEARCH_PROFILE_TEMPLATE.md`
  Role: canonical schema for profile fields.

## Integration Logic With Other Modules

1. `project-init` runs first (recommended) and writes `USER_RESEARCH_PROFILE.md`.
2. `deep-research` reads this profile and constrains:
   - search keywords
   - inclusion/exclusion scope
   - terminology in synthesis reports
3. `academic-paper` reads this profile and constrains:
   - outline and section focus
   - writing register and terminology
   - abstract keyword consistency
4. `academic-paper-reviewer` reads this profile and constrains:
   - review criteria
   - methodology challenge style
   - terminology checks against glossary

## Trigger Conditions

### Trigger Keywords

English: initialize project, initialize thesis, setup profile, create research profile, setup paper workspace, bootstrap writing project

Simplified Chinese: 初始化课题, 初始化配置, 创建课题配置, 创建研究画像, 论文项目初始化

### Should Trigger

- User starts a new thesis/paper project.
- User says current outputs are drifting and asks for domain alignment.
- User requests a reusable profile for multi-agent writing/review workflow.

### Should NOT Trigger

- User asks directly for literature search results: use `deep-research`.
- User asks to draft sections now: use `academic-paper`.
- User asks for critique of existing text: use `academic-paper-reviewer`.

## Invocation Examples

- "Initialize my thesis profile. Topic: graph contrastive learning for few-shot NIDS."
- "帮我初始化课题配置：题目是基于图对比学习的小样本网络入侵检测方法研究。"

## Execution Workflow

1. Intake: collect topic, domain, paper type, methods, constraints.
2. Normalize: resolve abbreviations and define canonical glossary.
3. Generate: write `USER_RESEARCH_PROFILE.md` from template.
4. Confirm: summarize what was set and suggest next command for target module.
