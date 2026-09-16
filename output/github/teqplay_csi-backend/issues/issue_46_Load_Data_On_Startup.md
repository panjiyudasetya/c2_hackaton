---
id: github:teqplay/csi-backend:issue:46
source: github
type: issue
repo: teqplay/csi-backend
number: 46
title: Load Data On Startup
author: jbugella
state: closed
date: '2025-01-07'
url: https://github.com/teqplay/csi-backend/issues/46
labels: []
explicit_links: []
---
# Issue #46: Load Data On Startup

**Repo:** teqplay/csi-backend  
**URL:** https://github.com/teqplay/csi-backend/issues/46  
**State:** closed | **Author:** jbugella  
**Created:** 2025-01-07  
**Closed:** 2025-01-07  

## Description

**Full diff:** [f52316f6b499...77065fedee22](https://github.com/teqplay/csi-backend/compare/f52316f6b499...77065fedee22)
**Merge commit:** [77065fedee22](https://github.com/teqplay/csi-backend/commit/77065fedee22)
**Author:** Former user
**Reviewers:** Michel Wilson, Darius Wattimena
**Approvers:** Michel Wilson
**Source Branch:** [PRA-284/init-data](https://github.com/teqplay/csi-backend/tree/PRA-284/init-data)
**Destination Branch:** [CSI-HA-pre-release](https://github.com/teqplay/csi-backend/tree/CSI-HA-pre-release)
**Closed On:** 2023-03-03T09:22:55.312619+00:00
**Status:** MERGED

This PR adds functionality to `:app:query` to load all data from Mongo into memory on startup.
A subsequent PR will implement the “keeping data up-to-date”-part.

