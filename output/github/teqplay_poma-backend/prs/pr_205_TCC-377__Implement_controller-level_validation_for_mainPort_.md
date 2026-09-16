---
id: github:teqplay/poma-backend:pr:205
source: github
type: pull_request
repo: teqplay/poma-backend
number: 205
title: 'TCC-377: Implement controller-level validation for mainPort in Berth, Port,
  and Terminal controllers'
author: Jamie-de-Leest
state: closed
date: '2025-09-03'
merged_at: '2025-09-10'
base_branch: develop
head_branch: TCC-377-implement-controller-level-validation-for-main-port
url: https://github.com/teqplay/poma-backend/pull/205
labels: []
linked_issues: []
explicit_links: []
---
# PR #205: TCC-377: Implement controller-level validation for mainPort in Berth, Port, and Terminal controllers

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/pull/205  
**State:** closed | **Author:** Jamie-de-Leest  
**Base ← Head:** `develop` ← `TCC-377-implement-controller-level-validation-for-main-port`  
**Created:** 2025-09-03  
**Merged:** 2025-09-10  

## Description

_No description._

## Commits

- `68e55ec9` **Jamie de Leest** (2025-09-03): Feat: Implement controller-level validation for mainPort in Berth, Port, and Terminal controllers
- `21053716` **Jamie de Leest** (2025-09-03): Fix: replaced non-null assertion with a safe call and null check
- `dea71bb2` **Jamie de Leest** (2025-09-03): Test: Add unit tests for controller-level validation in Berth, Port, and Terminal controllers
- `224abb11` **Jamie de Leest** (2025-09-03): chore: ktlint
- `0b47f940` **Jamie de Leest** (2025-09-08): Merge branch 'develop' into TCC-377-implement-controller-level-validation-for-main-port
- `a59eb457` **Jamie de Leest** (2025-09-08): fix: update main port validation logic in Berth and Terminal services

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-09-03)

## Pull Request Overview

This PR implements controller-level validation for mainPort fields across Berth, Port, and Terminal controllers to ensure mainPort references are valid and not empty.

- Adds mainPort validation logic to check for empty/blank values and validate port existence
- Implements validateMainPort helper methods in BerthService and TerminalService
- Adds consistent validation patterns across all three infrastructure controllers

### Reviewed Changes

Copilot reviewed 5 out of 5 changed files in this pull request and generated 2 comments.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| BerthController.kt | Adds mainPort validation to check for blank values and valid port references |
| BerthService.kt | Implements validateMainPort helper method for port existence validation |
| PortController.kt | Adds mainPort validation with direct port existence check |
| TerminalController.kt | Adds mainPort validation to check for blank values and valid port references |
| TerminalService.kt | Implements validateMainPort helper method for port existence validation |
</details>






---

<sub>**Tip:** Customize your code reviews with copilot-instructions.md. <a href="/teqplay/poma-backend/new/develop/.github?filename=copilot-instructions.md" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Create the file</a> or <a href="https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">learn how to get started</a>.</sub>

### michel-teqplay — APPROVED (2025-09-03)

_No comment._

### Jamie-de-Leest — COMMENTED (2025-09-04)

_No comment._

### TeqJoostD — APPROVED (2025-09-09)

_No comment._

## Review Comments

### Copilot — 2025-09-03 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/port/PortController.kt`

The use of non-null assertion operator (!!) is risky here. Consider using safe call operator and explicit null check instead, or ensure the null check on line 166 covers all cases where mainPort could be null.
```suggestion
        if (model.mainPort == null) {
            throw BadRequestException("mainPort is required")
        }
        if (service.getByIds(listOf(model.mainPort)).isEmpty()) {
```

### Copilot — 2025-09-03 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/berth/BerthService.kt`

This validation logic is duplicated in TerminalService. Consider extracting this common validation to a shared utility class or service to avoid code duplication.
```suggestion
        return portService.isPortMissing(mainPort)
```

### michel-teqplay — 2025-09-03 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/berth/BerthController.kt`

I would prefer `mainPort.isNullOrBlank()` here.

### Jamie-de-Leest — 2025-09-04 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/berth/BerthController.kt`

mainPort is allowed to be null it cant be a blank/empty string
