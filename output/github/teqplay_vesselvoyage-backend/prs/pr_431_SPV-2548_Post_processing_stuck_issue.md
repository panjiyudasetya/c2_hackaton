---
id: github:teqplay/vesselvoyage-backend:pr:431
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 431
title: SPV-2548 Post processing stuck issue
author: Darius-Wattimena
state: closed
date: '2025-02-25'
merged_at: '2025-02-25'
base_branch: develop
head_branch: post-processing-stuck-issue
url: https://github.com/teqplay/vesselvoyage-backend/pull/431
labels: []
linked_issues: []
explicit_links: []
---
# PR #431: SPV-2548 Post processing stuck issue

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/431  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `post-processing-stuck-issue`  
**Created:** 2025-02-25  
**Merged:** 2025-02-25  

## Description

_No description._

## Commits

- `fd22e01b` **Darius Wattimena** (2025-02-25): Added a bunch of extra logging to see what is going on while post processing
- `ad290a97` **Darius Wattimena** (2025-02-25): Added a try catch so we know what goes wrong
- `a8705e3e` **Darius Wattimena** (2025-02-25): Fix an issue where we fully stop post processing a batch whemn one of them is not found or the end time is not set
- `cfeedb05` **Darius Wattimena** (2025-02-25): Move removing of the post processing task once we are actually done instead of when we schedule the runnable
- `c3ff1b0b` **Darius Wattimena** (2025-02-25): Removed extra thread pool as we want post processing to be blocking the scheduled thread
- `dc6a16ef` **Darius Wattimena** (2025-02-25): Remove unused imports

## Reviews

### leonjoosse — APPROVED (2025-02-25)

Good find!
