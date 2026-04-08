# Easy Paper Toolkit Router

This workspace is a modular toolkit for research, writing, and review. It is designed to be context-efficient: load only the required skill and required agent for the current user intent.

## Skill Map

| Skill | Primary Use | Typical Output |
|-------|-------------|----------------|
| `project-init` | Create or update project-specific research profile | `USER_RESEARCH_PROFILE.md` |
| `deep-research` | Research question shaping, literature search, verification, synthesis | Research brief/report |
| `academic-paper` | Outline, drafting, abstract, citation and format support | Paper draft and formatted sections |
| `academic-paper-reviewer` | Structured critique, methodology checks, revision roadmap | Review report and revision plan |

## Routing Rules

1. **Initialization first**: If user asks to initialize a thesis/project profile, route to `project-init`.
2. **Research tasks**: If user asks for evidence gathering, source search, fact-checking, systematic review, or uncertain RQ clarification, route to `deep-research`.
3. **Writing tasks**: If user asks to generate outline/sections/abstracts, improve style, or format manuscript, route to `academic-paper`.
4. **Review tasks**: If user asks to critique or challenge existing text, route to `academic-paper-reviewer`.
5. **Do not load all skills**: Never read all `SKILL.md` files by default. Read only the selected skill plus required assets for the current task.

## Global Profile Rule (Critical)

If `USER_RESEARCH_PROFILE.md` or `课题配置.md` exists in workspace root, every selected skill must silently read it before invoking any agent. All output must respect that profile:

- domain boundaries
- terminology constraints
- paper type constraints
- style and evaluation criteria

If profile does not exist and the user starts with writing/review tasks, recommend running `project-init` first.

## Trigger Examples

- "Initialize my thesis profile" -> `project-init`
- "Help me search recent papers on graph contrastive learning IDS" -> `deep-research`
- "Write section 3.2 based on this outline" -> `academic-paper`
- "Act as a strict reviewer and find logic flaws in section 4" -> `academic-paper-reviewer`

## Default Policies

- Default output language: follow user language; if unspecified in this workspace, prefer Simplified Chinese.
- Citation integrity: do not fabricate references; if external evidence is needed, ask for source metadata or provide explicit uncertainty.
- Anti-sycophancy: maintain critical reasoning in review modes.
