---
id: github:teqplay/vesselvoyage-backend:pr:421
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 421
title: SPV-2526 Make VesselVoyage processing more stable
author: Darius-Wattimena
state: closed
date: '2025-02-14'
merged_at: '2025-02-17'
base_branch: develop
head_branch: memory-usage-fix-attempt
url: https://github.com/teqplay/vesselvoyage-backend/pull/421
labels: []
linked_issues: []
explicit_links: []
---
# PR #421: SPV-2526 Make VesselVoyage processing more stable

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/421  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `memory-usage-fix-attempt`  
**Created:** 2025-02-14  
**Merged:** 2025-02-17  

## Description

_No description._

## Commits

- `0decc958` **Darius Wattimena** (2025-02-11): Reduce size of V1 traces to reduce memory footprint
- `77e9cecc` **Darius Wattimena** (2025-02-11): Adjust default resources of the processing pod
- `9ffa5524` **Darius Wattimena** (2025-02-11): Reduce the amount of days of ongoing traces we keep in the database
- `796cf13f` **Darius Wattimena** (2025-02-11): Reduce max age even more, so we keep the ongoing traces collection very small
- `6262f0ab` **Darius Wattimena** (2025-02-12): Increase memory a bit more and reduce the amount of threads that are used to do post-processing
- `198293a3` **Darius Wattimena** (2025-02-12): Changed persisting of traces to be interval based to avoid running multiple delete queries at the same time
- `1a083910` **Darius Wattimena** (2025-02-12): Fix test config
- `21dab26d` **Darius Wattimena** (2025-02-12): Adjusted properties class to match new property name
- `d78d284a` **Darius Wattimena** (2025-02-14): Merge branch 'refs/heads/develop' into memory-usage-fix-attempt

## Reviews

### leonjoosse — APPROVED (2025-02-17)

LGTM, but not sure what the exact impact is, so please see this approval only as code changes looks good.

## Comments

### Darius-Wattimena — 2025-02-17

> LGTM, but not sure what the exact impact is, so please see this approval only as code changes looks good.

Yes I still want to wait with merging this, to ensure we can actually lower the memory to 6 GB before moving this to production. I also want to check if V1 traces still work as expected, as that is code which was made by Jos, so far before I started working on the project.
