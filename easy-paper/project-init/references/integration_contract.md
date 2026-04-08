# Integration Contract: project-init -> other skills

## Contract Objective

Define exactly how downstream modules consume `USER_RESEARCH_PROFILE.md`.

## Required Consumption Rules

Every downstream skill must read profile file before agent invocation:

1. `deep-research`
- use Topic, Domain, In Scope, Out of Scope for query design
- use Terminology Contract for report wording
- use Red Lines to avoid unsupported claims

2. `academic-paper`
- use Paper Type and Writing Constraints for section style
- use Core Methodology and Key Metrics for argument structure
- use Citation Policy and Terminology Contract in drafting

3. `academic-paper-reviewer`
- use Review Criteria and Red Lines as evaluation checklist
- use Terminology Contract to flag wording inconsistency
- use Scope fields to detect off-topic content

## Failure Handling

If profile file is missing:

- warn once
- suggest running `project-init`
- continue only if user explicitly asks to proceed without profile

If profile fields are incomplete:

- ask only for missing required fields
- avoid broad generic defaults when user intent is domain-specific
