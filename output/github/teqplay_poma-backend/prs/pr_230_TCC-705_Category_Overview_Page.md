---
id: github:teqplay/poma-backend:pr:230
source: github
type: pull_request
repo: teqplay/poma-backend
number: 230
title: TCC-705 Category Overview Page
author: TeqJoostD
state: closed
date: '2026-02-13'
merged_at: '2026-02-16'
base_branch: TCC-703
head_branch: TCC-705
url: https://github.com/teqplay/poma-backend/pull/230
labels: []
linked_issues: []
explicit_links:
- jira:TCC-705
- jira:TCC-703
---
# PR #230: TCC-705 Category Overview Page

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/pull/230  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `TCC-703` ← `TCC-705`  
**Created:** 2026-02-13  
**Merged:** 2026-02-16  

## Description

_No description._

## Commits

- `6e5ef07e` **TeqJoostD** (2026-02-13): Add support for category overview page
- `060cbf41` **TeqJoostD** (2026-02-13): Merge branch 'TCC-703' into TCC-705
- `710845ba` **TeqJoostD** (2026-02-16): remove false documentation
- `31e7dff8` **TeqJoostD** (2026-02-16): Merge branch 'TCC-703' into TCC-705
- `d9f03148` **TeqJoostD** (2026-02-16): Merge branch 'TCC-703' into TCC-705
- `3ff1c268` **TeqJoostD** (2026-02-16): Feedback
- `9f17d1ae` **TeqJoostD** (2026-02-16): Merge branch 'TCC-703' into TCC-705
  # Conflicts:
  #	src/main/kotlin/nl/teqplay/poma/feature/mapping/MappingService.kt

## Reviews

### github-actions[bot] — COMMENTED (2026-02-13)

Review completed. No suggestions at this time.

### github-actions[bot] — COMMENTED (2026-02-13)

Review completed. The implementation looks solid overall with proper use of Kotlin idioms and good test coverage. I found one minor documentation inconsistency that should be corrected.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### github-actions[bot] — COMMENTED (2026-02-16)

Review completed. The implementation looks solid overall with good test coverage and proper error handling. I found one potential issue with the reflection-based field extraction that could include non-Validity fields in the processing.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### github-actions[bot] — COMMENTED (2026-02-16)

Review completed. The implementation looks solid overall with good test coverage. I identified one potential edge case issue with list size mismatches that could silently hide bugs.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### github-actions[bot] — COMMENTED (2026-02-16)

Review completed. Found one potential issue with the zip operation that could silently drop data.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### Darius-Wattimena — CHANGES_REQUESTED (2026-02-16)

_No comment._

### Darius-Wattimena — APPROVED (2026-02-16)

_No comment._

### github-actions[bot] — COMMENTED (2026-02-16)

Review completed. Found one potential bug related to list synchronization.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

## Review Comments

### Darius-Wattimena — 2026-02-16 on `src/main/kotlin/nl/teqplay/poma/feature/mapping/MappingService.kt`

Should we not thrown an exception instead of having this `else` branch return an empty string?

### Darius-Wattimena — 2026-02-16 on `src/main/kotlin/nl/teqplay/poma/feature/mapping/MappingService.kt`

Feels to me that this should be written a bit better here.

Right now you basically have the same switch for each field, while you already know if it is a port/terminal/etc after we've checked the first field?

Also, I'm sure you can maybe even use any of the interfaces which Poma provides to make your life easier, and just do smart casting of the `entity` variable?

### Darius-Wattimena — 2026-02-16 on `src/main/kotlin/nl/teqplay/poma/feature/mapping/MappingService.kt`

Some common type would be better here? This way you could improve bunch of the code below if possible.
