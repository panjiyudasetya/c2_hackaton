---
id: github:teqplay/portreporter-backend:issue:942
source: github
type: issue
repo: teqplay/portreporter-backend
number: 942
title: First Draft Of The Internal Portcall Alias Storing Mechanism
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/942
labels: []
explicit_links: []
---
# Issue #942: First Draft Of The Internal Portcall Alias Storing Mechanism

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/942  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [09e46d7c7076...4f13fb81c43c](https://github.com/teqplay/portreporter-backend/compare/09e46d7c7076...4f13fb81c43c)
**Merge commit:** [4f13fb81c43c](https://github.com/teqplay/portreporter-backend/commit/4f13fb81c43c)
**Author:** Wouter Naloop
**Reviewers:** Richard van Klaveren, Joost Laurman, Joaquin Marquez Bugella
**Approvers:** Joaquin Marquez Bugella
**Source Branch:** [feat/internal_portcall_alias](https://github.com/teqplay/portreporter-backend/tree/feat/internal_portcall_alias)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2021-09-23T08:06:48.327292+00:00
**Status:** MERGED

In this PR we want to replace the constant quering to portcallplus with doing that once every 5 min for all updated portcalls. And storing that in the database. This so that portreporter can still do its thing whenever portcallplus is down  
  
For this i rewrote the existing portcall alias fetch mechanisms because they had some gaps.   
also deprecated the portcallAlias field in the portcallMetadata class and added a new one where we give all aliasses they are allowed to see.   
  
Important to note is that i tried to make it explicit if we are requesting a teqplayId this id is the id that is in portcalls stored as portcallId.   
In all cases where the non explicit function is used we are either not sure if it is an alias/teqplayId or we know we have an alias and want to search on that.  
  
A choice has been made that when searching for single portcalls we expect to be able to search on partial portcallids, and when requesting multiple portcallids at the same time we expect full/exact portcallIds

