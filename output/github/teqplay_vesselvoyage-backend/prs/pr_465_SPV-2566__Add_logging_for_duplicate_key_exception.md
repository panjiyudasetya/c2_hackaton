---
id: github:teqplay/vesselvoyage-backend:pr:465
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 465
title: 'SPV-2566: Add logging for duplicate key exception '
author: leonjoosse
state: closed
date: '2025-03-21'
merged_at: '2025-03-21'
base_branch: develop
head_branch: SPV-2566-trace-insert-exception
url: https://github.com/teqplay/vesselvoyage-backend/pull/465
labels: []
linked_issues: []
explicit_links: []
---
# PR #465: SPV-2566: Add logging for duplicate key exception 

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/465  
**State:** closed | **Author:** leonjoosse  
**Base ← Head:** `develop` ← `SPV-2566-trace-insert-exception`  
**Created:** 2025-03-21  
**Merged:** 2025-03-21  

## Description

Trying to find out when the visit / voyage / trace gets inserted, but there is still an existing record. The log line also dumps the existing record, hopefully we can compare the data and see where it originates

## Commits

- `4a032b5a` **leonj** (2025-03-21): Add logging for duplicate key exception while writing visit/voyage changes
- `dc4e2c24` **leonj** (2025-03-21): Add logging for duplicate key exception while writing traces

## Reviews

### Darius-Wattimena — APPROVED (2025-03-21)

_No comment._
