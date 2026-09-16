---
id: github:teqplay/poma-backend:pr:235
source: github
type: pull_request
repo: teqplay/poma-backend
number: 235
title: Feedback from david, search functionality and addition of location an…
author: TeqJoostD
state: closed
date: '2026-02-17'
merged_at: '2026-02-17'
base_branch: develop
head_branch: poma-feedback
url: https://github.com/teqplay/poma-backend/pull/235
labels: []
linked_issues: []
explicit_links: []
---
# PR #235: Feedback from david, search functionality and addition of location an…

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/pull/235  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `poma-feedback`  
**Created:** 2026-02-17  
**Merged:** 2026-02-17  

## Description

…d area

## Commits

- `5ccdf931` **TeqJoostD** (2026-02-17): Feedback from david, search functionality and addition of location and area

## Reviews

### github-actions[bot] — COMMENTED (2026-02-17)

Review completed. The changes look good overall - the search functionality is properly integrated and the type constraint change from `InfrastructureModel` to `AreaInfrastructureModel` is safe since all entity types (Port, Terminal, Berth, Anchorage, PilotBoardingPlace) implement `AreaInfrastructureModel`.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### copilot-pull-request-reviewer[bot] — COMMENTED (2026-02-17)

## Pull request overview

This PR updates the mapping endpoints to support searching ports by a text pattern and enriches entity-overview responses with `location` and `area` data to support UI needs around location/area display.

**Changes:**
- Add an optional `searchPattern` query parameter to `/v1/mapping/port/status` and pass it through to `PortService.getAll`.
- Extend `EntityOverview` to include `location` and `area`, and populate these fields from the underlying infrastructure entities.
- Tighten `createEntityOverview`’s input type from `InfrastructureModel` to `AreaInfrastructureModel` to access `area`.

### Reviewed changes

Copilot reviewed 3 out of 3 changed files in this pull request and generated 3 comments.

| File | Description |
| ---- | ----------- |
| `src/main/kotlin/nl/teqplay/poma/feature/mapping/MappingService.kt` | Plumbs `searchPattern` into port retrieval; adds `location`/`area` into `EntityOverview` creation. |
| `src/main/kotlin/nl/teqplay/poma/feature/mapping/MappingController.kt` | Exposes `searchPattern` as a request param on the mapping status endpoint. |
| `api/src/main/kotlin/nl/teqplay/poma/api/v1/EntityOverview.kt` | Adds `location` and `area` fields to the public API model. |


<details>
<summary>Comments suppressed due to low confidence (1)</summary>

**src/main/kotlin/nl/teqplay/poma/feature/mapping/MappingService.kt:60**
* New `searchPattern` behavior in `getPortMappingStatus` isn’t covered by tests in `MappingServiceTest` (there are tests for other MappingService endpoints, but none asserting search filtering or pagination totals). Adding tests for filtering and for the `totalCount` value when a searchPattern is used would help prevent regressions.
```
    fun getPortMappingStatus(
        searchPattern: String?,
        page: Int,
        limit: Int,
        countryCode: String?,
        expectedMappingStatus: String?,
    ): PaginatedResponse<PortMappingStatus> {
```
</details>



---

💡 <a href="/teqplay/poma-backend/new/develop/.github/instructions?filename=*.instructions.md" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Add Copilot custom instructions</a> for smarter, more guided reviews. <a href="https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Learn how to get started</a>.

### Darius-Wattimena — APPROVED (2026-02-17)

_No comment._

## Review Comments

### Copilot — 2026-02-17 on `src/main/kotlin/nl/teqplay/poma/feature/mapping/MappingService.kt`

Pagination metadata can become incorrect when `searchPattern` is provided: `ports` is filtered via `portService.getAll(searchPattern = ...)`, but `totalCount` is computed via `portService.getCount(...)` which does not include the `searchPattern` filter. This will produce an inflated total and inconsistent page counts. Consider extending the count query to apply the same filters as `getAll` (including searchPattern), or adding a datasource method to count filtered results.

### Copilot — 2026-02-17 on `api/src/main/kotlin/nl/teqplay/poma/api/v1/EntityOverview.kt`

The KDoc for `EntityOverview` is now out of sync with the data class: `location`/`area` were added as required properties but the `@property` list still describes `id` as the third property and the new descriptions are grammatically incorrect (e.g., "area area of the Entity"). Please update the KDoc to match the current fields and use consistent capitalization/wording.

### Copilot — 2026-02-17 on `src/main/kotlin/nl/teqplay/poma/feature/mapping/MappingController.kt`

The `searchPattern` parameter description is a bit vague compared to what the backend actually searches (currently `_id`, `name`, `unlocode`, `countryCode` in `AbstractPortDatasource.extraFilters`). Consider updating the description to list the supported fields so API consumers know what to expect.
```suggestion
        @Parameter(
            description =
                "Search pattern to filter ports by ID, name, UN/LOCODE, or ISO country code " +
                    "(_id, name, unlocode, countryCode)",
        )
```
