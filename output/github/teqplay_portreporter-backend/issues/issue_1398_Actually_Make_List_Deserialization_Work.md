---
id: github:teqplay/portreporter-backend:issue:1398
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1398
title: Actually Make List Deserialization Work
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1398
labels: []
explicit_links: []
---
# Issue #1398: Actually Make List Deserialization Work

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1398  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [db7cc49ad1c1...f4fb8aa14bb8](https://github.com/teqplay/portreporter-backend/compare/db7cc49ad1c1...f4fb8aa14bb8)
**Merge commit:** [f4fb8aa14bb8](https://github.com/teqplay/portreporter-backend/commit/f4fb8aa14bb8)
**Author:** Michel Wilson
**Reviewers:** Joaquin Marquez Bugella
**Approvers:** Joaquin Marquez Bugella
**Source Branch:** [fix-list-deserialization](https://github.com/teqplay/portreporter-backend/tree/fix-list-deserialization)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2024-10-14T14:07:51.208094+00:00
**Status:** MERGED

So it turns out that type erasure made this totally not work at all, this’ll fix it.

