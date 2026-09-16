---
id: github:teqplay/vesselvoyage-backend:pr:426
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 426
title: SPV-2526 Attempt to find memory leak
author: Darius-Wattimena
state: closed
date: '2025-02-17'
merged_at: '2025-02-18'
base_branch: develop
head_branch: SPV-2526-find-memory-leak
url: https://github.com/teqplay/vesselvoyage-backend/pull/426
labels: []
linked_issues: []
explicit_links: []
---
# PR #426: SPV-2526 Attempt to find memory leak

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/426  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `SPV-2526-find-memory-leak`  
**Created:** 2025-02-17  
**Merged:** 2025-02-18  

## Description

Adds a bunch of logging to know easier what scheduled task is running, and figure out what it is doing.

I've also deleted some code that could "stop" processing. But it doesn't make sense to maintain that logic as this was mainly done to ensure we don't process anything when platform was degraded in any way to avoid not being able to calculate stops for V1. This is now being solved by the internal-api and ship-history being highly available, so it should ensure that they are always available.

## Commits

- `851feec1` **Darius Wattimena** (2025-02-17): Removed scheduled task to check if we need to keep processing
- `056e3508` **Darius Wattimena** (2025-02-17): Added extra logging to find out where the memory leak is
- `3def6df6` **Darius Wattimena** (2025-02-17): Clean up the revents code a bit more
- `28295368` **Darius Wattimena** (2025-02-17): Merge branch 'refs/heads/develop' into SPV-2526-find-memory-leak
- `d8cf2c68` **Darius Wattimena** (2025-02-17): ktlint
- `f8559bff` **Darius Wattimena** (2025-02-17): Update post processing interval to be every minute instead of every 5 seconds

## Reviews

### leonjoosse — APPROVED (2025-02-18)

_No comment._

### TeqJoostD — APPROVED (2025-02-18)

_No comment._
