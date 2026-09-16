---
id: github:teqplay/vesselvoyage-backend:pr:466
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 466
title: SPV-2580 fix terminal mooring jittering
author: Darius-Wattimena
state: closed
date: '2025-03-21'
merged_at: '2025-03-26'
base_branch: develop
head_branch: SPV-2580-fix-terminal-mooring-jittering
url: https://github.com/teqplay/vesselvoyage-backend/pull/466
labels: []
linked_issues: []
explicit_links: []
---
# PR #466: SPV-2580 fix terminal mooring jittering

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/466  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `SPV-2580-fix-terminal-mooring-jittering`  
**Created:** 2025-03-21  
**Merged:** 2025-03-26  

## Description

Not needed for the upcoming release. But for future cases this would be nice to have in as this fixes quite a lot of cases where we have jittering. Next to this to apply this to existing data we would need to require to do a recalculation, so having this in for the full recalc would be smart.

## Commits

- `deebca91` **Darius Wattimena** (2025-03-21): Added activity merging logic that can be enabled for specific area activities
- `e605af10` **Darius Wattimena** (2025-03-21): Adjusted the terminal mooring area activities to enable activity merging
- `a7dc7b84` **Darius Wattimena** (2025-03-21): Adjusted scenario test to the correct terminal mooring end time without the jittering

## Reviews

### TeqJoostD — APPROVED (2025-03-26)

_No comment._
