---
id: github:teqplay/vesselvoyage-backend:pr:706
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 706
title: TCC-671 limited visits and voyages
author: Darius-Wattimena
state: closed
date: '2026-02-02'
merged_at: '2026-02-03'
base_branch: develop
head_branch: TCC-671-limited-visits
url: https://github.com/teqplay/vesselvoyage-backend/pull/706
labels: []
linked_issues: []
explicit_links: []
---
# PR #706: TCC-671 limited visits and voyages

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/706  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `TCC-671-limited-visits`  
**Created:** 2026-02-02  
**Merged:** 2026-02-03  

## Description

_No description._

## Commits

- `0d732748` **Darius Wattimena** (2026-01-27): add 'limited' property to visit models to indicate processing limits
- `37aaa6fe` **Darius Wattimena** (2026-02-02): Also add 'limited' property to voyage models to indicate processing limits
- `98f3c3bc` **Darius Wattimena** (2026-02-02): Add default value to visit model to keep the models backwards compatible
- `532fd5ce` **Darius Wattimena** (2026-02-03): Update fields to be consistent
- `c722c673` **Darius Wattimena** (2026-02-03): Removed docs so it just takes the detailed one from the entry interface

## Reviews

### github-actions[bot] — COMMENTED (2026-02-02)

Review completed. Found one critical inconsistency in the implementation.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### copilot-pull-request-reviewer[bot] — COMMENTED (2026-02-02)

## Pull request overview

This PR adds a `limited` boolean field to the Entry interface and all its implementations (ImoVisit, ImoVoyage, BargeVisit, and BargeVoyage) to indicate when an entry has been limited during processing due to having more than 50 activities of the same type. The field is properly mapped in the EntryV2Mapper and corresponding tests have been updated.

**Changes:**
- Added `limited: Boolean` field to the Entry interface with documentation explaining it indicates limitation when processing entries with more than 50 activities
- Implemented the field in all Entry subtypes (ImoVisit, ImoVoyage, BargeVisit, BargeVoyage) with default values
- Updated EntryV2Mapper to map the `limited` field from internal models to API models
- Updated test cases to include the new `limited` field

### Reviewed changes

Copilot reviewed 9 out of 9 changed files in this pull request and generated 3 comments.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/Entry.kt | Adds `limited` boolean field to Entry interface with comprehensive documentation |
| api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/Visit.kt | Adds `limited` field to ImoVisit with default value `false` and documentation |
| api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/Voyage.kt | Adds `limited` field to ImoVoyage with default value `false` |
| api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/BargeVisit.kt | Adds `limited` field to BargeVisit with documentation |
| api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/BargeVoyage.kt | Adds `limited` field to BargeVoyage with default value `false` |
| src/main/kotlin/nl/teqplay/vesselvoyage/mapper/EntryV2Mapper.kt | Adds mapping configuration for `limited` field in all entry type mappers |
| src/test/kotlin/nl/teqplay/vesselvoyage/mapper/EntryV2MapperTest.kt | Updates test assertions to include `limited = false` |
| src/test/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiVisitV2ControllerTest.kt | Updates test to map `limited` field from visit entity |
| client/src/test/kotlin/nl/teqplay/vesselvoyage/client/VesselVoyageClientTest.kt | Updates test data to include `limited = false` |
</details>

### michel-teqplay — CHANGES_REQUESTED (2026-02-03)

I think it makes sense to add a default value, like the AI review suggests

### github-actions[bot] — COMMENTED (2026-02-03)

Review completed. The implementation correctly adds the `limited` property to the Entry interface and all implementing classes. The mapper configuration and test updates are consistent. Found one minor documentation issue regarding the threshold description.

### michel-teqplay — APPROVED (2026-02-03)

_No comment._

### github-actions[bot] — COMMENTED (2026-02-03)

Review completed. No suggestions at this time.

## Review Comments

### Copilot — 2026-02-02 on `api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/BargeVisit.kt`

The `limited` field in `BargeVisit` is missing a default value, which is inconsistent with the other implementations. `ImoVisit` (line 42 of Visit.kt), `ImoVoyage` (line 60 of Voyage.kt), and `BargeVoyage` (line 59 of BargeVoyage.kt) all have `= false` as a default value. This inconsistency will cause compilation issues when constructing `BargeVisit` instances without explicitly providing the `limited` parameter, while other types can be constructed without it.
```suggestion
    override val limited: Boolean = false,
```

### Copilot — 2026-02-02 on `api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/Voyage.kt`

The `limited` field in `ImoVoyage` is missing a documentation comment. While `ImoVisit` (line 41-42 of Visit.kt) and `BargeVisit` (line 40-41 of BargeVisit.kt) have documentation comments explaining "Whether this visit was limited when processing", the `ImoVoyage` lacks this documentation. This is inconsistent with the documentation pattern established for the same field in other Entry implementations.
```suggestion

    /** Whether this voyage was limited when processing */
```

### Copilot — 2026-02-02 on `api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/BargeVoyage.kt`

The `limited` field in `BargeVoyage` is missing a documentation comment. While `ImoVisit` (line 41-42 of Visit.kt) and `BargeVisit` (line 40-41 of BargeVisit.kt) have documentation comments explaining "Whether this visit was limited when processing", the `BargeVoyage` lacks this documentation. This is inconsistent with the documentation pattern established for the same field in other Entry implementations.
```suggestion

    /** Whether this voyage was limited when processing */
```

## Comments
