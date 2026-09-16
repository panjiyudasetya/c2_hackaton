---
id: github:teqplay/poma-backend:pr:228
source: github
type: pull_request
repo: teqplay/poma-backend
number: 228
title: TCC-700 Introduce support for global ports overview page
author: TeqJoostD
state: closed
date: '2026-02-11'
merged_at: '2026-02-12'
base_branch: develop
head_branch: TCC-700
url: https://github.com/teqplay/poma-backend/pull/228
labels: []
linked_issues: []
explicit_links: []
---
# PR #228: TCC-700 Introduce support for global ports overview page

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/pull/228  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `TCC-700`  
**Created:** 2026-02-11  
**Merged:** 2026-02-12  

## Description

_No description._

## Commits

- `1e15dfb3` **TeqJoostD** (2026-02-11): Introduce support for global ports overview page
- `fb6b14b5` **TeqJoostD** (2026-02-11): small feedback
- `9aa47882` **TeqJoostD** (2026-02-11): smallest change
- `b12aeef7` **TeqJoostD** (2026-02-11): micro change
- `5777d487` **TeqJoostD** (2026-02-12): darius epic feedback
- `97f67ae0` **TeqJoostD** (2026-02-12): feedback
- `3e5fa201` **TeqJoostD** (2026-02-12): fix

## Reviews

### github-actions[bot] — COMMENTED (2026-02-11)

Review completed. I've identified several potential bugs that should be addressed.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### TeqJoostD — COMMENTED (2026-02-11)

_No comment._

### copilot-pull-request-reviewer[bot] — COMMENTED (2026-02-11)

## Pull request overview

This PR adds backend support for a “global ports overview” / mapping overview page by introducing mapping-status aggregation, new mapping API endpoints, and a port+infrastructure validation report used to compute per-port completeness.

**Changes:**
- Add `/v1/mapping/overview` and `/v1/mapping/port/status` endpoints with new API response models (overview + paginated port status).
- Introduce a `PortModelValidatorService` and validation report model to compute valid/invalid entity counts and mapping completeness.
- Extend port querying to support filtering/counting by `expectedMappingStatus`, and add a Mongo aggregation to summarize counts by mapping status.

### Reviewed changes

Copilot reviewed 14 out of 14 changed files in this pull request and generated 8 comments.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| src/test/kotlin/nl/teqplay/poma/feature/infrastructure/port/validation/PortModelValidatorServiceTest.kt | Adds unit tests for the new port/infrastructure validation service. |
| src/main/kotlin/nl/teqplay/poma/model/aggregation/MappingStatusCount.kt | Adds an aggregation result DTO for mapping-status counts. |
| src/main/kotlin/nl/teqplay/poma/generics/DataSource.kt | Adds generic `getCount(query)` and a bounding-box+field lookup helper. |
| src/main/kotlin/nl/teqplay/poma/feature/mapping/MappingService.kt | Implements mapping overview + paginated per-port mapping status computation. |
| src/main/kotlin/nl/teqplay/poma/feature/mapping/MappingController.kt | Exposes mapping overview/status endpoints with OpenAPI annotations. |
| src/main/kotlin/nl/teqplay/poma/feature/infrastructure/port/validation/Validity.kt | Introduces `Validity` enum used across validation reports. |
| src/main/kotlin/nl/teqplay/poma/feature/infrastructure/port/validation/ValidationReports.kt | Adds structured validity report data classes and counters. |
| src/main/kotlin/nl/teqplay/poma/feature/infrastructure/port/validation/PortModelValidatorService.kt | Implements validation logic for ports and related infrastructure entities. |
| src/main/kotlin/nl/teqplay/poma/feature/infrastructure/port/PortService.kt | Adds expected-mapping-status filtering and a count endpoint for pagination. |
| src/main/kotlin/nl/teqplay/poma/feature/infrastructure/port/PortController.kt | Wires the new `expectedMappingStatus` query parameter through to the service. |
| src/main/kotlin/nl/teqplay/poma/feature/infrastructure/port/AbstractPortDatasource.kt | Adds an index for mapping status and an aggregation summary method. |
| api/src/main/kotlin/nl/teqplay/poma/api/v1/PortMappingStatus.kt | New API DTO for per-port mapping status results. |
| api/src/main/kotlin/nl/teqplay/poma/api/v1/PaginatedResponse.kt | New generic pagination wrapper DTO. |
| api/src/main/kotlin/nl/teqplay/poma/api/v1/MappingOverview.kt | New API DTO for mapping overview counts. |
</details>






---

💡 <a href="/teqplay/poma-backend/new/develop/.github/instructions?filename=*.instructions.md" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Add Copilot custom instructions</a> for smarter, more guided reviews. <a href="https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Learn how to get started</a>.

### TeqJoostD — COMMENTED (2026-02-11)

_No comment._

### TeqJoostD — COMMENTED (2026-02-11)

_No comment._

### github-actions[bot] — COMMENTED (2026-02-11)

Review completed. I've identified a critical bug in the validation logic that could cause incorrect validation results when ports have no infrastructure entities.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### github-actions[bot] — COMMENTED (2026-02-11)

Review completed. Found a few potential issues related to performance and edge case handling.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### github-actions[bot] — COMMENTED (2026-02-11)

Review completed. Found several potential issues related to edge case handling and N+1 query performance.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### Darius-Wattimena — CHANGES_REQUESTED (2026-02-11)

_No comment._

### TeqJoostD — COMMENTED (2026-02-12)

_No comment._

### TeqJoostD — COMMENTED (2026-02-12)

_No comment._

### TeqJoostD — COMMENTED (2026-02-12)

_No comment._

### TeqJoostD — COMMENTED (2026-02-12)

_No comment._

### TeqJoostD — COMMENTED (2026-02-12)

_No comment._

### TeqJoostD — COMMENTED (2026-02-12)

_No comment._

### TeqJoostD — COMMENTED (2026-02-12)

_No comment._

### TeqJoostD — COMMENTED (2026-02-12)

_No comment._

### github-actions[bot] — COMMENTED (2026-02-12)

Review completed. Found potential performance concern with N+1 query pattern in the mapping status endpoint.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### Darius-Wattimena — COMMENTED (2026-02-12)

_No comment._

### Darius-Wattimena — COMMENTED (2026-02-12)

_No comment._

### Darius-Wattimena — COMMENTED (2026-02-12)

_No comment._

### davidTeqplay — COMMENTED (2026-02-12)

_No comment._

### github-actions[bot] — COMMENTED (2026-02-12)

Review completed. Found critical bugs that need to be addressed.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### github-actions[bot] — COMMENTED (2026-02-12)

Review completed. Found potential performance concerns with N+1 queries in the mapping status endpoint.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### Darius-Wattimena — APPROVED (2026-02-12)

_No comment._

## Review Comments

### TeqJoostD — 2026-02-11 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/port/validation/PortModelValidatorService.kt`

Port can have 0 anchorages

### Copilot — 2026-02-11 on `src/test/kotlin/nl/teqplay/poma/feature/infrastructure/port/validation/PortModelValidatorServiceTest.kt`

Test name says the berth should be INVALID when `mooringType` is null, but the assertions expect `Validity.MISSING`. Rename the test (or adjust expectations) so the test description matches the actual validation semantics.

### Copilot — 2026-02-11 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/port/validation/PortModelValidatorService.kt`

`validInfrastructureAreas` is computed and used for the emptiness check, but `containsAllInfrastructure` flattens `allAreas` instead. Using `validInfrastructureAreas.flatten()` (or removing the intermediate variable) would avoid redundant work and make the intent clearer.
```suggestion
        val containsAllInfrastructure = validInfrastructureAreas.flatten().all { pointInArea(eosArea, it) }
```

### Copilot — 2026-02-11 on `src/main/kotlin/nl/teqplay/poma/feature/mapping/MappingController.kt`

The endpoint description mentions filtering by “BI status”, but the API only exposes `countryCode` and `mappingStatus` query params. Please remove “BI status” from the description or add the missing filter parameter so the OpenAPI docs match the actual behavior.
```suggestion
                "Supports filtering by country code and mapping status",
```

### Copilot — 2026-02-11 on `src/main/kotlin/nl/teqplay/poma/feature/mapping/MappingController.kt`

New `/v1/mapping/*` endpoints add non-trivial behavior (aggregation grouping + pagination + mappingStatus filter) but there are no corresponding tests. Consider adding controller/service tests (similar to existing `PortControllerTest`) covering: overview counts per status, pagination boundaries, and invalid `mappingStatus` input returning a 4xx instead of 500.

### Copilot — 2026-02-11 on `src/main/kotlin/nl/teqplay/poma/model/aggregation/MappingStatusCount.kt`

`getMappingStatusSummary()` groups by Mongo’s `_id` field, but this aggregate result class exposes the grouping key as `status`. Unless the aggregation layer is doing custom field mapping, `status` will deserialize as null and the overview counts will be wrong. Consider renaming `status` to `_id` (like `TerminalTagCountAggregateResult`) or annotating it with `@BsonId` / proper BSON mapping so the group key is populated.
```suggestion
import nl.teqplay.poma.model.basemodels.Port
import org.bson.codecs.pojo.annotations.BsonProperty

data class MappingStatusCount(
    @BsonProperty("_id")
```

### Copilot — 2026-02-11 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/port/PortService.kt`

`MappingStatus.valueOf(it)` will throw `IllegalArgumentException` for unknown/blank query values, turning a client input error into a 500. Parse defensively (e.g., `isNullOrBlank` check + `runCatching`/`BadRequestException`) or reuse the existing `getMappingStatus(...)` helper that already returns a 400 on invalid values.
```suggestion
            val mappingStatusEnum = getMappingStatus(expectedMappingStatus)
```

### Copilot — 2026-02-11 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/port/PortService.kt`

Same issue as above: `MappingStatus.valueOf(...)` can throw on invalid `expectedMappingStatus` and will surface as a 500. Please validate/normalize input (blank -> null) and throw a `BadRequestException` (or reuse `getMappingStatus(...)`) so clients get a 4xx for invalid filters.

### Copilot — 2026-02-11 on `src/test/kotlin/nl/teqplay/poma/feature/infrastructure/port/validation/PortModelValidatorServiceTest.kt`

Test name says the terminal should be INVALID when `cargoType` is empty, but the assertions expect `Validity.MISSING`. Rename the test to match the expected behavior (or adjust expectations) so the suite documents the rules consistently.

### TeqJoostD — 2026-02-11 on `src/main/kotlin/nl/teqplay/poma/feature/mapping/MappingService.kt`

bro...

### TeqJoostD — 2026-02-11 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/port/AbstractPortDatasource.kt`

will do data migration

### Darius-Wattimena — 2026-02-11 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/port/validation/PortModelValidatorService.kt`

Not needed to check this, as we are only interested into the inner area of a port

### Darius-Wattimena — 2026-02-11 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/port/validation/PortModelValidatorService.kt`

It can also happen that we have no pilot boarding places. I would maybe make a generic function which just checks the following:

```
            when {
                entitiesToValidate.isEmpty() -> Validity.MISSING
                entitiesToValidate.all { it.valid } -> Validity.VALID
                else -> Validity.INVALID
            }
```

Where `entitiesToValidate` would be `anchorages`, `pilotBoardingPlaces`, `terminals`, etc

### Darius-Wattimena — 2026-02-11 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/port/validation/PortModelValidatorService.kt`

same here, when we don't have any berths it should be `Validity.MISSING`

### Darius-Wattimena — 2026-02-11 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/port/validation/PortModelValidatorService.kt`

This is not always true, when we only expected basic port information on the port it would mean all those fields aren't needed?

### Darius-Wattimena — 2026-02-11 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/port/validation/PortModelValidatorService.kt`

? This check is basically do I have an unlocode? Shouldn't this already be checked when validating the `unlocode` field of a port?

### Darius-Wattimena — 2026-02-11 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/port/validation/PortModelValidatorService.kt`

Does this need to be a non-flatten list when providing it to this function?

### Darius-Wattimena — 2026-02-11 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/port/validation/ValidationReports.kt`

How is ktlint happy with this? Surely this is breaking code style guidelines?

Can't you just do something along the following:
```
fun countValid() {
  sumOf(
    terminals.count { it.valid }
    berths.count { it.valid }
    ...
  )
}
```

### Darius-Wattimena — 2026-02-11 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/port/validation/ValidationReports.kt`

Apply the same here but for the invalid things

### Darius-Wattimena — 2026-02-11 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/port/validation/ValidationReports.kt`

The port fields are missing in this count. (e.g. if we miss the port name then it should be counted towards the total invalid)

### Darius-Wattimena — 2026-02-11 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/port/PortService.kt`

Will this not break existing API users? As they never provide an `expectedMappingStatus`?

### TeqJoostD — 2026-02-12 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/port/validation/PortModelValidatorService.kt`

For only basic information we check the PortValidationReport, for the full mapping we check the (now renamed for clarity) PortMappingValidationReport. Which is a report of the full port and not only the port info.
```
/**
     * Retrieve the mapping status based on the [expectedStatus]
     *
     * When the expected mapping is not mapped always return true
     * When the expected mapping is basic, return true if the port is valid
     * When the expected mapping is fully, return true if the whole report is valid
     */
    fun getMappingStatus(
        expectedStatus: MappingStatus,
        report: PortMappingValidationReport,
    ): Boolean {
        return when (expectedStatus) {
            MappingStatus.NOT_MAPPED -> true
            MappingStatus.BASIC_MAPPED -> report.port.valid
            MappingStatus.FULLY_MAPPED -> report.valid
        }
    }
```

Not very clear, but the whole thing is a bit all the rules are a bit confusing to begin with imo

### TeqJoostD — 2026-02-12 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/port/validation/PortModelValidatorService.kt`

well if the parentUnlocode is null its not the berths fault as in its not invalid but its missing. So still good to check? Although this probably doesn't happen. Just very annoying that the unlocode field is nullable

### TeqJoostD — 2026-02-12 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/port/validation/PortModelValidatorService.kt`

Its not a flat list, its a list with areas.

### TeqJoostD — 2026-02-12 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/port/validation/PortModelValidatorService.kt`

Do you mean flatten the area before passing it? Would not really make sense to me since we need both the flattened list and the non-flattened list.

### TeqJoostD — 2026-02-12 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/port/validation/ValidationReports.kt`

nitpicky but okay

### TeqJoostD — 2026-02-12 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/port/validation/ValidationReports.kt`

Do we want to calculate individual fields or entitites here? I do not advise doing both since that makes it much more confusing.

### TeqJoostD — 2026-02-12 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/port/validation/ValidationReports.kt`

So either checking all port fields + all fields of all entities. (please no)
Or we count an invalid port as +1 invalid or +1 valid (not count the fields individually)

### TeqJoostD — 2026-02-12 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/port/PortService.kt`

If all is null it just won't get filtered so no

### Darius-Wattimena — 2026-02-12 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/port/validation/PortModelValidatorService.kt`

I suppose a good first start for now, let re-review this once things are more visable in the frontend

### Darius-Wattimena — 2026-02-12 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/port/validation/ValidationReports.kt`

I believe we initially wanted to include those fields in the total. @davidTeqplay what do you think we should do here?

### Darius-Wattimena — 2026-02-12 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/port/PortService.kt`

wait it does `!= null` not `== null` sorry I missread this

### davidTeqplay — 2026-02-12 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/port/validation/ValidationReports.kt`

I think we can count the port as 1 invalid...or if we skip it?

Example:
<img width="1623" height="50" alt="image" src="https://github.com/user-attachments/assets/e2e991bd-388c-49a8-b3ba-5ea54ef81c54" />


