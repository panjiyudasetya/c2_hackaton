---
id: github:teqplay/vesselvoyage-backend:pr:396
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 396
title: SPV-2431 fix broken events jackson & log clean-up
author: Darius-Wattimena
state: closed
date: '2025-01-21'
merged_at: '2025-01-23'
base_branch: develop
head_branch: SPV-2431-fix-broken-events-jackson
url: https://github.com/teqplay/vesselvoyage-backend/pull/396
labels: []
linked_issues: []
explicit_links: []
---
# PR #396: SPV-2431 fix broken events jackson & log clean-up

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/396  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `SPV-2431-fix-broken-events-jackson`  
**Created:** 2025-01-21  
**Merged:** 2025-01-23  

## Description

This does need a fix on the side of EventHistory to fully fix the issue.

Next to this I've did some minor clean-up of log lines that weren't very useful for us.

## Commits

- `8743a9a4` **Darius Wattimena** (2025-01-21): Set logging to debug for functionality only used for V1 code
- `ea696882` **Darius Wattimena** (2025-01-21): Update logging level of V1 processing which isn't very useful
- `48401318` **Darius Wattimena** (2025-01-21): Adjusted event history fetcher to only get back events we are using for VesselVoyage V2
- `9faeab76` **Darius Wattimena** (2025-01-23): Upped version of AisEngine models
- `d72d27f5` **Darius Wattimena** (2025-01-23): Comment out included events for now because of a bug in skeleton plugins

## Reviews

### TeqJoostD — APPROVED (2025-01-23)

_No comment._
