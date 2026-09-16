---
id: github:teqplay/vesselvoyage-backend:pr:544
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 544
title: Fix traces batch call endpoint
author: Darius-Wattimena
state: closed
date: '2025-06-27'
merged_at: '2025-06-27'
base_branch: develop
head_branch: fix-api-endpoint
url: https://github.com/teqplay/vesselvoyage-backend/pull/544
labels: []
linked_issues: []
explicit_links: []
---
# PR #544: Fix traces batch call endpoint

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/544  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `fix-api-endpoint`  
**Created:** 2025-06-27  
**Merged:** 2025-06-27  

## Description

Client expected `/v2/traces/ids` as a post call instead of `/v2/traces` which it is now.
As nobody uses the batch call, aligning with the client

## Commits

- `eb901f49` **Darius Wattimena** (2025-06-27): Fix an issue where the batch call for traces wasn't correctly mapped to how the client would expect it

## Reviews

### leonjoosse — APPROVED (2025-06-27)

_No comment._
