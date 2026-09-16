---
id: github:teqplay/vesselvoyage-backend:pr:400
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 400
title: SPV-2474 api model json type
author: Darius-Wattimena
state: closed
date: '2025-01-24'
merged_at: '2025-01-28'
base_branch: develop
head_branch: SPV-2474-api-mode-json-type
url: https://github.com/teqplay/vesselvoyage-backend/pull/400
labels: []
linked_issues: []
explicit_links: []
---
# PR #400: SPV-2474 api model json type

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/400  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `SPV-2474-api-mode-json-type`  
**Created:** 2025-01-24  
**Merged:** 2025-01-28  

## Description

Adds a `_type` field. Otherwise you can't get any of the api models when trying to retrieve `Entry`

I wasn't really sure on how to create a test for this. But any suggestions would be nice.

## Commits

- `b8386152` **Darius Wattimena** (2025-01-24): Added a type field to the entry interface so they can be consumed by other backends

## Reviews

### leonjoosse — APPROVED (2025-01-27)

_No comment._
