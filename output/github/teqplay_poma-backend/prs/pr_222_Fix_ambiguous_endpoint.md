---
id: github:teqplay/poma-backend:pr:222
source: github
type: pull_request
repo: teqplay/poma-backend
number: 222
title: Fix ambiguous endpoint
author: michel-teqplay
state: closed
date: '2025-12-30'
merged_at: '2025-12-31'
base_branch: develop
head_branch: TCC-578-fix_ambiguity
url: https://github.com/teqplay/poma-backend/pull/222
labels: []
linked_issues: []
explicit_links: []
---
# PR #222: Fix ambiguous endpoint

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/pull/222  
**State:** closed | **Author:** michel-teqplay  
**Base ← Head:** `develop` ← `TCC-578-fix_ambiguity`  
**Created:** 2025-12-30  
**Merged:** 2025-12-31  

## Description

_No description._

## Commits

- `991bbd3b` **Michel Wilson** (2025-12-30): Fix ambiguous endpoint

## Reviews

### github-actions[bot] — COMMENTED (2025-12-30)

Review completed. The endpoint path change correctly resolves the ambiguity with the inherited `/{id}` endpoint and follows patterns used elsewhere in the codebase. No suggestions at this time.

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-12-30)

## Pull request overview

This PR resolves an ambiguous endpoint mapping in the CustomerAreaController by renaming the GET endpoint from `/{customerId}` to `/byCustomerId/{customerId}`. The ambiguity arose because the parent class `InfrastructureController` already defines a `/{id}` endpoint, which would conflict with the `/{customerId}` pattern in Spring's routing.

**Key Changes:**
- Modified the endpoint path from `@GetMapping("/{customerId}")` to `@GetMapping("/byCustomerId/{customerId}")` to disambiguate from the inherited `/{id}` endpoint


<details>
<summary>Comments suppressed due to low confidence (1)</summary>

**src/main/kotlin/nl/teqplay/poma/feature/infrastructure/customerarea/CustomerAreaController.kt:73**
* The 'getByCustomerId' function lacks test coverage. Similar infrastructure controllers in the codebase (BerthController, PortController, TerminalController) have corresponding test classes. Consider adding a CustomerAreaControllerTest to verify this endpoint's behavior.
```
    fun getByCustomerId(
        @PathVariable customerId: String,
    ): List<ApiModel> {
        val result = service.getByCustomerId(customerId)
        return service.convertToApiModels(result)
    }
```
</details>



---

💡 <a href="/teqplay/poma-backend/new/develop/.github/instructions?filename=*.instructions.md" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Add Copilot custom instructions</a> for smarter, more guided reviews. <a href="https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Learn how to get started</a>.

### abi-teqplay — APPROVED (2025-12-31)

_No comment._

## Review Comments

### Copilot — 2025-12-30 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/customerarea/CustomerAreaController.kt`

The endpoint path uses camelCase ('byCustomerId') which is inconsistent with the existing naming conventions in the codebase. Other endpoints use all lowercase without separators (e.g., '/unlocode', '/mergedatabases', '/currentUser'). Consider changing this to '/bycustomerid/{customerId}' to maintain consistency.
```suggestion
    @GetMapping("/bycustomerid/{customerId}")
```

### Copilot — 2025-12-30 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/customerarea/CustomerAreaController.kt`

This endpoint change is a breaking API change that will affect existing API consumers. The original endpoint '/v1/customerarea/{customerId}' is now changed to '/v1/customerarea/byCustomerId/{customerId}'. Ensure that API consumers are notified of this breaking change, and consider if API versioning or a deprecation period is needed.
```suggestion

    /**
     * Deprecated: use GET /v1/customerarea/byCustomerId/{customerId} instead.
     * This endpoint is kept for backward compatibility with existing API consumers.
     */
    @Deprecated("Use /v1/customerarea/byCustomerId/{customerId} instead")
    @GetMapping("/{customerId}")
    fun getByCustomerIdLegacy(
        @PathVariable customerId: String,
    ): List<ApiModel> {
        val result = service.getByCustomerId(customerId)
        return service.convertToApiModels(result)
    }
```

## Comments

### abi-teqplay — 2025-12-31

I believe there is a plan in place to make sure the change of the endpoint path since it is a breaking changes.
