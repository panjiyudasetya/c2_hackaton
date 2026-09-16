---
id: github:teqplay/vesselvoyage-backend:pr:414
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 414
title: SPV-2525 Make the area field optional
author: Darius-Wattimena
state: closed
date: '2025-02-11'
merged_at: '2025-02-11'
base_branch: develop
head_branch: SPV-2525-area-optional
url: https://github.com/teqplay/vesselvoyage-backend/pull/414
labels: []
linked_issues: []
explicit_links: []
---
# PR #414: SPV-2525 Make the area field optional

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/414  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `SPV-2525-area-optional`  
**Created:** 2025-02-11  
**Merged:** 2025-02-11  

## Description

As it turns out, some visits are from deleted ports. Meaning `area` needs to be optional so the backend doesn't start throwing 500 for NPE's.

Downside of this change is that the field is now optional.

For example https://vesselvoyagedev.teqplay.nl/#/ships/9576765/sof/8199fc25-7313-4315-9a40-c18e4979eb6f.VISIT?mode=period&months=1 will throw a 500 because 1 of the visits is broken.

## Commits

- `152cc14f` **Darius Wattimena** (2025-02-11): Make the area field optional

## Reviews

### leonjoosse — APPROVED (2025-02-11)

_No comment._
