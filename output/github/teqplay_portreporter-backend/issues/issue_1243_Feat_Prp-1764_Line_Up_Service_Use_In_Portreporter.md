---
id: github:teqplay/portreporter-backend:issue:1243
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1243
title: Feat/Prp-1764 Line Up Service Use In Portreporter
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1243
labels: []
explicit_links:
- jira:PRP-1764
---
# Issue #1243: Feat/Prp-1764 Line Up Service Use In Portreporter

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1243  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [c92230c41ecd...2ee92cca8fb1](https://github.com/teqplay/portreporter-backend/compare/c92230c41ecd...2ee92cca8fb1)
**Merge commit:** [2ee92cca8fb1](https://github.com/teqplay/portreporter-backend/commit/2ee92cca8fb1)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Michel Wilson, Wouter Naloop, Darius Wattimena, Gavin den Hollander
**Approvers:** Michel Wilson
**Source Branch:** [feat/PRP-1764](https://github.com/teqplay/portreporter-backend/tree/feat/PRP-1764)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2023-04-11T15:34:07.618114+00:00
**Status:** MERGED

* First commit: Include a logic intermediate layer between controller and service.
* Second commit:
    * Adapt to the new the LineUp service.
    * Set a flag to enable automatic updates upon PortcallEvents processing.
    * Enable automatic update for multiple line-up companyOwners upon PortcallEvents processing.
    * Add new static\(v2\) endpoint to get terminals by port.
    
* Third commit: I made a _bobo_ when setting some config: forgot to set the object `externalConnection.lineUp` as `PropertyGroup` .

