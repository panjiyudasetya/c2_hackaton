---
id: github:teqplay/poma-backend:issue:77
source: github
type: issue
repo: teqplay/poma-backend
number: 77
title: 'Feat(Terminal): Add Mooring Area'
author: jbugella
state: closed
date: '2025-01-13'
url: https://github.com/teqplay/poma-backend/issues/77
labels: []
explicit_links: []
---
# Issue #77: Feat(Terminal): Add Mooring Area

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/issues/77  
**State:** closed | **Author:** jbugella  
**Created:** 2025-01-13  
**Closed:** 2025-01-13  

## Description

**Full diff:** [7451ff0fb978...2339c17a5531](https://github.com/teqplay/poma-backend/compare/7451ff0fb978...2339c17a5531)
**Merge commit:** [2339c17a5531](https://github.com/teqplay/poma-backend/commit/2339c17a5531)
**Author:** Former user
**Reviewers:** Michel Wilson, Wouter Naloop, Darius Wattimena
**Approvers:** Wouter Naloop
**Source Branch:** [SPV-1498-terminal-mooring-area](https://github.com/teqplay/poma-backend/tree/SPV-1498-terminal-mooring-area)
**Destination Branch:** [develop](https://github.com/teqplay/poma-backend/tree/develop)
**Closed On:** 2023-08-21T08:37:10.269988+00:00
**Status:** MERGED

This PR adds support for terminal mooring areas, which are automatically generated areas based on the terminal’s berths including a default margin \(if not overwritten manually\).
**Example:**
* green = berths
* teal = convex hull
* white = convex hull \+ margin
![](https://bitbucket.org/repo/7zbd4Ep/images/4014999392-image.png)

