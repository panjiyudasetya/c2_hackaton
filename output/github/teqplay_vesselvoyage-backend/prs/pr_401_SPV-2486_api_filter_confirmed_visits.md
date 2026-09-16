---
id: github:teqplay/vesselvoyage-backend:pr:401
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 401
title: SPV-2486 api filter confirmed visits
author: Darius-Wattimena
state: closed
date: '2025-01-28'
merged_at: '2025-02-03'
base_branch: develop
head_branch: SPV-2486-api-filter-confirmed-visits
url: https://github.com/teqplay/vesselvoyage-backend/pull/401
labels: []
linked_issues: []
explicit_links: []
---
# PR #401: SPV-2486 api filter confirmed visits

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/401  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `SPV-2486-api-filter-confirmed-visits`  
**Created:** 2025-01-28  
**Merged:** 2025-02-03  

## Description

Adds support to filter using the `confirmed` flag on API endpoints where we return visits.

For example the `/v2/visit/byImo/{IMO}` where you can do now add the following:
1. confirmed=true to get only confirmed visits
2. confirmed=false to get only not confirmed visits
3. when no filter flag is provided you get all of them, meaning the old behaviour of the endpoint

## Commits

- `ec38da66` **Darius Wattimena** (2025-01-27): Added the confirmed param to filter for all endpoints where you can get visits
- `4954a3ba` **Darius Wattimena** (2025-01-27): Removed unused import
- `23ff0d0b` **Darius Wattimena** (2025-01-28): Merge branch 'refs/heads/develop' into SPV-2486-api-filter-confirmed-visits
- `7162bb1f` **Darius Wattimena** (2025-01-28): Removed the default value in the base service and added named arguments where needed
- `2b46cc91` **Darius Wattimena** (2025-01-28): Adjusted test cases to ensure the calls to get visits is being mocked correctly
- `d5b902b8` **Darius Wattimena** (2025-01-31): Reworked a bit of the code so it makes a bit more sense what we are trying to filter
- `a3fbb23a` **Darius Wattimena** (2025-01-31): Merge branch 'develop' into SPV-2486-api-filter-confirmed-visits

## Reviews

### TeqJoostD — CHANGES_REQUESTED (2025-01-29)

Some small changes

### leonjoosse — COMMENTED (2025-01-30)

_No comment._

### leonjoosse — APPROVED (2025-01-30)

_No comment._

### TeqJoostD — COMMENTED (2025-01-30)

_No comment._

### Darius-Wattimena — COMMENTED (2025-01-31)

_No comment._

### TeqJoostD — APPROVED (2025-02-03)

_No comment._

## Review Comments

### TeqJoostD — 2025-01-29 on `src/main/kotlin/nl/teqplay/vesselvoyage/datasource/NewEntryDataSource.kt`

Did you forget to add functionality for confirmed?

### TeqJoostD — 2025-01-29 on `src/main/kotlin/nl/teqplay/vesselvoyage/datasource/NewEntryDataSource.kt`

And maybe better to create a separate function for this

### TeqJoostD — 2025-01-29 on `src/main/kotlin/nl/teqplay/vesselvoyage/datasource/NewEntryDataSource.kt`

Ah I because its a voyage the confirmed doesn't matter

### TeqJoostD — 2025-01-29 on `src/main/kotlin/nl/teqplay/vesselvoyage/datasource/NewEntryDataSource.kt`

need comment!!!!

### TeqJoostD — 2025-01-29 on `src/main/kotlin/nl/teqplay/vesselvoyage/datasource/NewEntryDataSource.kt`

Ah so we have a super function that only does the finished filter applying. And then we override this in the visit data source with addition of confirmed parameter. while the voyage uses the regular additional query function.

Would be better to split up into separate functions and in the implementations themselves call the functions we need.

### TeqJoostD — 2025-01-29 on `src/main/kotlin/nl/teqplay/vesselvoyage/datasource/NewVisitDataSource.kt`

Same here this is a bit confusing especially without any comments

### TeqJoostD — 2025-01-29 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/StoryService.kt`

Should we make confirmed nullable by default in some cases? So we can only specify it when neede. Or do you not agree

### leonjoosse — 2025-01-30 on `src/main/kotlin/nl/teqplay/vesselvoyage/datasource/NewEntryDataSource.kt`

WE NEED MOAR COMMENTS

### TeqJoostD — 2025-01-30 on `src/main/kotlin/nl/teqplay/vesselvoyage/datasource/NewEntryDataSource.kt`

I agree, is this too much too ask darius??? we need more comments... and we need them NOW!

### Darius-Wattimena — 2025-01-31 on `src/main/kotlin/nl/teqplay/vesselvoyage/datasource/NewEntryDataSource.kt`

![](https://programmerhumor.io/wp-content/uploads/2023/04/programmerhumor-io-programming-memes-9409a76e8b6c85b.jpg)

## Comments

### GavinTeqplay — 2025-01-31


![image](https://github.com/user-attachments/assets/3a496ee9-0f7a-4883-bb32-49ca81fc68e5)

