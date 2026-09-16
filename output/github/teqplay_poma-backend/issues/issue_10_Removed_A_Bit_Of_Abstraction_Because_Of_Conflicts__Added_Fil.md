---
id: github:teqplay/poma-backend:issue:10
source: github
type: issue
repo: teqplay/poma-backend
number: 10
title: Removed A Bit Of Abstraction Because Of Conflicts, Added Filter On Port To
  The Get All Controllers
author: jbugella
state: closed
date: '2025-01-13'
url: https://github.com/teqplay/poma-backend/issues/10
labels: []
explicit_links: []
---
# Issue #10: Removed A Bit Of Abstraction Because Of Conflicts, Added Filter On Port To The Get All Controllers

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/issues/10  
**State:** closed | **Author:** jbugella  
**Created:** 2025-01-13  
**Closed:** 2025-01-13  

## Description

**Full diff:** [b8c27cc2b396...82f3d328f755](https://github.com/teqplay/poma-backend/compare/b8c27cc2b396...82f3d328f755)
**Merge commit:** [82f3d328f755](https://github.com/teqplay/poma-backend/commit/82f3d328f755)
**Author:** Wouter Naloop
**Reviewers:** Shravan Shetty, Leon Joosse, Vasyl Pidlisniak
**Approvers:** 
**Source Branch:** [feat/portfilter](https://github.com/teqplay/poma-backend/tree/feat/portfilter)
**Destination Branch:** [develop](https://github.com/teqplay/poma-backend/tree/develop)
**Closed On:** 2020-09-29T13:02:58.345782+00:00
**Status:** MERGED

Had a wrong abstraction so decided to remove the getAll from the abstract Infrastructure Controller. Adding more different types of abstraction didn’t seem like the right choice

