# Changelog

All notable changes to this package are documented in this file.

This project follows a simplified Keep a Changelog style.

## [0.1.0] - 2026-04-08

### Added
- Added `project-init` skill module for profile-first initialization.
- Added `project-init/agents/profile_builder_agent.md`.
- Added `project-init/templates/USER_RESEARCH_PROFILE_TEMPLATE.md`.
- Added `project-init/examples/trigger_examples.md`.
- Added `project-init/references/integration_contract.md`.
- Added module-level architecture guides:
  - `project-init/logic.md`
  - `deep-research/logic.md`
  - `academic-paper/logic.md`
  - `academic-paper-reviewer/logic.md`
  - `shared/logic.md`
- Added `LICENSE` file under `easy-paper/` (copied from upstream, unchanged).

### Changed
- Reorganized routing approach from full heavy pipeline narrative to on-demand module flow.
- Updated README and README.zh-CN with:
  - explicit upstream attribution
  - non-official adaptation notice
  - embedding-only integration instructions for Claude Code
  - initialization checklists

### Removed
- Removed nested `.claude/` from skill package to avoid dual-router conflicts in embedding mode.

## Notes
- Upstream project: https://github.com/Imbad0202/academic-research-skills
- Upstream license: CC BY-NC 4.0
