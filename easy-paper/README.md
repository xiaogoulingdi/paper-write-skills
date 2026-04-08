# Easy Paper Toolkit

[简体中文](README.zh-CN.md)
[Changelog](CHANGELOG.md)

## Acknowledgement

Special thanks to the original author and maintainers of the upstream project:

- Upstream repository: [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills)

This repository is an adaptation for a different usage style and is **not** an official upstream-maintained distribution.

## Reference

This project is based on and adapted from the open-source repository [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills), with a lightweight reorganization for practical Chinese academic writing workflows.

## Upstream Attribution and Compliance

If you reuse or publish this package, keep attribution explicit in your README:

- upstream project: `Imbad0202/academic-research-skills`
- upstream URL: https://github.com/Imbad0202/academic-research-skills
- adaptation statement: what you changed (routing, modules, localization)
- license notice: preserve upstream license terms and include local modifications note

Suggested attribution template:

```md
This project is adapted from [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills).

Changes made in this fork/repackage:
- modular routing redesign
- added `project-init` initialization skill
- Chinese workflow localization and documentation restructuring

Please also review and comply with the upstream license and attribution requirements.
```

Recommended compliance block for publication:

```md
## License and Attribution Notice

This repository is an adapted package derived from:
- Upstream: https://github.com/Imbad0202/academic-research-skills
- Upstream License: CC BY-NC 4.0 (Attribution-NonCommercial)
- The local `LICENSE` file is copied from upstream without license-term modifications

This package is intended for learning, research, and non-commercial academic writing assistance.
It is an adaptation, not an official upstream-maintained distribution.
```

Key adaptation points:

- **Routing redesign (from heavy end-to-end narrative to on-demand modules):** routing is constrained to `project-init -> deep-research -> academic-paper -> academic-paper-reviewer`, avoiding full-pipeline default loading.
- **New initialization module (`project-init`):** added `project-init/SKILL.md`, `project-init/agents/profile_builder_agent.md`, `project-init/templates/USER_RESEARCH_PROFILE_TEMPLATE.md`, `project-init/references/integration_contract.md`, `project-init/examples/trigger_examples.md`, and `project-init/logic.md`.
- **Unified global profile mechanism:** `USER_RESEARCH_PROFILE.md` is the single cross-module constraint source for terminology, paper type constraints, scope boundaries, and review red lines.
- **Readable architecture docs:** added module-level `logic.md` files to reduce onboarding friction.

---

## Current Package Structure

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

## How to Integrate with Claude Code (Embedding Mode Only)

Use this package by embedding it into an existing project.

Recommended layout:

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

Integration steps:

1. Copy this `easy-paper` folder to `your-project/.claude/skills/easy-paper/`.
2. Merge routing rules into `your-project/.claude/CLAUDE.md`.
3. Launch Claude Code from `your-project/` root.
4. Run `project-init` first to generate `your-project/USER_RESEARCH_PROFILE.md`.

One-time setup commands (PowerShell example):

```powershell
cd C:\path\to\your-project
New-Item -ItemType Directory -Force .claude\skills | Out-Null
Copy-Item -Recurse -Force C:\path\to\easy-paper .claude\skills\easy-paper
```

Then edit and merge routing in:

- `your-project/.claude/CLAUDE.md`

Then initialize profile in Claude chat:

```text
Initialize project profile. Topic: <your topic>. Paper type: <your type>.
```

Expected output after initialization:

- `your-project/USER_RESEARCH_PROFILE.md`

Pre-release initialization checklist:

1. `your-project/.claude/skills/easy-paper/` exists with all module folders.
2. `your-project/.claude/CLAUDE.md` includes merged routing rules.
3. `your-project/USER_RESEARCH_PROFILE.md` is generated successfully.
4. A sample writing command routes to `academic-paper`.
5. A sample critique command routes to `academic-paper-reviewer`.

Important:

- Keep routing only at project root: `your-project/.claude/CLAUDE.md`.
- Do not keep a second nested `.claude` router inside the skill package.

---

## What Each Module Does

### 1. project-init

Initialization module for building one unified project profile.

- generates or updates `USER_RESEARCH_PROFILE.md`
- defines terminology contract, scope, paper-type constraints, and review criteria
- should be executed first

### 2. deep-research

Upstream research engine.

- clarifies research questions
- supports retrieval strategy and source verification
- prepares structured evidence for writing

### 3. academic-paper

Writing engine.

- outline planning
- section drafting
- abstract and citation support

### 4. academic-paper-reviewer

Structured critique engine.

- methodology challenge
- logic stress test
- revision roadmap

### 5. shared

Cross-module protocol layer.

- handoff schema
- style calibration protocol
- optional verification protocol

---

## Quick Start

### Scenario A: New Project

1. Run `project-init` to create `USER_RESEARCH_PROFILE.md`.
2. Use `deep-research` for scoped evidence collection.
3. Use `academic-paper` for drafting.
4. Use `academic-paper-reviewer` for critique and revision loop.

### Scenario B: Partially Completed Project

1. Run `project-init` first, but fill it using your existing draft context.
2. Skip unnecessary research steps and continue drafting targeted sections.
3. Review existing chapters with `academic-paper-reviewer` and apply revision roadmap.

---

## Notes

- Default output language is Simplified Chinese unless explicitly overridden.
- For IEEE/arXiv/top-conference references, provide metadata or excerpts when possible to reduce citation hallucination.
