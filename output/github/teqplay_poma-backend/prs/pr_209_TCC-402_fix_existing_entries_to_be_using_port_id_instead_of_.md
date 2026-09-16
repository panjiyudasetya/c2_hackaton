---
id: github:teqplay/poma-backend:pr:209
source: github
type: pull_request
repo: teqplay/poma-backend
number: 209
title: TCC-402 fix existing entries to be using port id instead of unlocode
author: Jamie-de-Leest
state: closed
date: '2025-09-08'
merged_at: '2025-09-11'
base_branch: develop
head_branch: TCC-402-fix-existing-entries-to-be-using-port-id-instead-of-unlocode
url: https://github.com/teqplay/poma-backend/pull/209
labels: []
linked_issues: []
explicit_links:
- jira:TCC-402
---
# PR #209: TCC-402 fix existing entries to be using port id instead of unlocode

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/pull/209  
**State:** closed | **Author:** Jamie-de-Leest  
**Base ← Head:** `develop` ← `TCC-402-fix-existing-entries-to-be-using-port-id-instead-of-unlocode`  
**Created:** 2025-09-08  
**Merged:** 2025-09-11  

## Description

_No description._

## Commits

- `17d842ed` **Jamie de Leest** (2025-09-08): fix: add endpoint to replace main port unlocode with port id
- `c8b78644` **Jamie de Leest** (2025-09-08): chore: ktlint
- `ae5f89c4` **Jamie de Leest** (2025-09-08): fix: make a script to update main port to port ID instead of unlocode
- `f3442a4f` **Jamie de Leest** (2025-09-08): chore: ktlint

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-09-08)

## Pull Request Overview

This PR updates the port validation system to use port IDs instead of UNLOCODE (United Nations Location Code) for mainPort references. The change includes adding validation logic for mainPort fields across Terminal, Port, and Berth controllers, along with a migration function to convert existing UNLOCODE references to port IDs.

- Add mainPort validation to Terminal, Port, and Berth controllers
- Implement migration function to replace UNLOCODE with port IDs in existing data
- Add comprehensive test coverage for the new validation logic

### Reviewed Changes

Copilot reviewed 10 out of 10 changed files in this pull request and generated 8 comments.

<details>
<summary>Show a summary per file</summary>

| File | Description |

| ---- | ----------- |

| src/main/kotlin/nl/teqplay/poma/feature/infrastructure/port/PortService.kt | Adds migration function to replace UNLOCODE with port IDs |

| src/main/kotlin/nl/teqplay/poma/feature/infrastructure/port/PortController.kt | Adds mainPort validation and migration endpoint |

| src/main/kotlin/nl/teqplay/poma/feature/infrastructure/terminal/TerminalService.kt | Adds port validation using UNLOCODE lookup |

| src/main/kotlin/nl/teqplay/poma/feature/infrastructure/terminal/TerminalController.kt | Adds mainPort validation logic |

| src/main/kotlin/nl/teqplay/poma/feature/infrastructure/berth/BerthService.kt | Adds port validation using UNLOCODE lookup |

| src/main/kotlin/nl/teqplay/poma/feature/infrastructure/berth/BerthController.kt | Adds mainPort validation logic |

| src/test/kotlin/nl/teqplay/poma/feature/terminal/TerminalControllerTest.kt | Comprehensive test coverage for terminal validation |

| src/test/kotlin/nl/teqplay/poma/feature/port/PortControllerTest.kt | Comprehensive test coverage for port validation |

| src/test/kotlin/nl/teqplay/poma/feature/berth/BerthControllerTest.kt | Comprehensive test coverage for berth validation |

| helm/values.yaml | Reduces replica count from 2 to 1 |
</details>






---

<sub>**Tip:** Customize your code reviews with copilot-instructions.md. <a href="/teqplay/poma-backend/new/develop/.github?filename=copilot-instructions.md" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Create the file</a> or <a href="https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">learn how to get started</a>.</sub>

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-09-10)

## Pull Request Overview

This PR fixes existing port entries to use port IDs instead of UN LOCODEs for the mainPort field, addressing TCC-402.
- Adds a new service method to replace mainPort UN LOCODEs with corresponding port IDs
- Introduces an admin endpoint to trigger the main port link fixes
- Reduces replica count from 2 to 1 in the Helm configuration

### Reviewed Changes

Copilot reviewed 3 out of 3 changed files in this pull request and generated 2 comments.

| File | Description |
| ---- | ----------- |
| PortService.kt | Implements `replaceMainportUnlocodeWithId()` method to convert mainPort references from UN LOCODEs to port IDs |
| PortController.kt | Adds admin-secured endpoint `fixMainPortLinks()` to trigger the mainPort conversion process |
| helm/values.yaml | Updates replica count configuration from 2 to 1 |





---

<sub>**Tip:** Customize your code reviews with copilot-instructions.md. <a href="/teqplay/poma-backend/new/develop/.github?filename=copilot-instructions.md" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Create the file</a> or <a href="https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">learn how to get started</a>.</sub>

### Darius-Wattimena — APPROVED (2025-09-10)

_No comment._

## Review Comments

### Copilot — 2025-09-08 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/terminal/TerminalService.kt`

The validation logic is inconsistent with the PR's purpose of using port IDs instead of UNLOCODE. This function validates against UNLOCODE but should validate against port IDs since the PR is migrating from UNLOCODE to port ID usage.
```suggestion
        return portService.getById(mainPort) == null
```

### Copilot — 2025-09-08 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/berth/BerthService.kt`

The validation logic is inconsistent with the PR's purpose of using port IDs instead of UNLOCODE. This function validates against UNLOCODE but should validate against port IDs since the PR is migrating from UNLOCODE to port ID usage.
```suggestion
        return portService.getById(mainPort) == null
```

### Copilot — 2025-09-08 on `src/test/kotlin/nl/teqplay/poma/feature/terminal/TerminalControllerTest.kt`

Test setup is inconsistent. The controller validation uses `service.getByIds()` for port ID validation (line 109), but tests are mocking `service.validateMainPort()` (lines 35 and 48) which uses UNLOCODE validation. This mismatch will cause the tests to fail.

### Copilot — 2025-09-08 on `src/test/kotlin/nl/teqplay/poma/feature/terminal/TerminalControllerTest.kt`

Test setup is inconsistent. The controller validation uses `service.getByIds()` for port ID validation (line 109), but tests are mocking `service.validateMainPort()` (lines 35 and 48) which uses UNLOCODE validation. This mismatch will cause the tests to fail.

### Copilot — 2025-09-08 on `src/test/kotlin/nl/teqplay/poma/feature/terminal/TerminalControllerTest.kt`

Test setup is inconsistent. The controller validation uses `service.getByIds()` for port ID validation (line 109), but tests are mocking `service.validateMainPort()` (lines 35 and 48) which uses UNLOCODE validation. This mismatch will cause the tests to fail.

### Copilot — 2025-09-08 on `src/test/kotlin/nl/teqplay/poma/feature/berth/BerthControllerTest.kt`

Test setup is inconsistent with the actual controller implementation. The controller should use port ID validation, but tests are only mocking `service.validateMainPort()` which validates UNLOCODE. The test for 'all fields are valid' (line 109) should also mock the correct validation method.

### Copilot — 2025-09-08 on `src/test/kotlin/nl/teqplay/poma/feature/berth/BerthControllerTest.kt`

Test setup is inconsistent with the actual controller implementation. The controller should use port ID validation, but tests are only mocking `service.validateMainPort()` which validates UNLOCODE. The test for 'all fields are valid' (line 109) should also mock the correct validation method.

### Copilot — 2025-09-08 on `src/test/kotlin/nl/teqplay/poma/feature/berth/BerthControllerTest.kt`

Test setup is inconsistent with the actual controller implementation. The controller should use port ID validation, but tests are only mocking `service.validateMainPort()` which validates UNLOCODE. The test for 'all fields are valid' (line 109) should also mock the correct validation method.
```suggestion
        whenever(service.validatePortId("validPortId")).thenReturn(false)
```

### Copilot — 2025-09-10 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/port/PortService.kt`

The condition `port._id == port.mainPort` on line 476 compares a port ID with what should be a UN LOCODE (since this method is meant to replace UN LOCODEs with IDs). This condition will likely never be true and the logic appears incorrect.

### Copilot — 2025-09-10 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/port/PortService.kt`

The `else` branch that returns `null` is unreachable because the condition `mainPortId != port.mainPort` on line 478 should always be true when reaching this point (since we're converting from UN LOCODEs to IDs). Consider removing this unreachable code or clarifying the intended logic.
```suggestion

```
