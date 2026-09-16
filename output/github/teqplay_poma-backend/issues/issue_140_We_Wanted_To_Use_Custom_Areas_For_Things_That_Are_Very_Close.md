---
id: github:teqplay/poma-backend:issue:140
source: github
type: issue
repo: teqplay/poma-backend
number: 140
title: We Wanted To Use Custom Areas For Things That Are Very Close To Eachother For
  If We Don'T Know The Name Of An Area, But This Was Limited By The Generation Of
  The Id
author: jbugella
state: closed
date: '2025-01-13'
url: https://github.com/teqplay/poma-backend/issues/140
labels: []
explicit_links: []
---
# Issue #140: We Wanted To Use Custom Areas For Things That Are Very Close To Eachother For If We Don'T Know The Name Of An Area, But This Was Limited By The Generation Of The Id

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/issues/140  
**State:** closed | **Author:** jbugella  
**Created:** 2025-01-13  
**Closed:** 2025-01-13  

## Description

**Full diff:** [0e0c6b7eea9c...99a1a696f56e](https://github.com/teqplay/poma-backend/compare/0e0c6b7eea9c...99a1a696f56e)
**Merge commit:** [99a1a696f56e](https://github.com/teqplay/poma-backend/commit/99a1a696f56e)
**Author:** Wouter Naloop
**Reviewers:** Joost Dambrink, Joaquin Marquez Bugella
**Approvers:** Joost Dambrink
**Source Branch:** [feat/allow-custom-areas-close-to-eachother](https://github.com/teqplay/poma-backend/tree/feat/allow-custom-areas-close-to-eachother)
**Destination Branch:** [develop](https://github.com/teqplay/poma-backend/tree/develop)
**Closed On:** 2024-07-09T13:11:37.430021+00:00
**Status:** MERGED

This PR consists of 2 parts  
* Custom Area Service, changing the id generation to be 5 numbers precise
* Deletion of the terminal Entity 
    * Note this is not Terminals but an experiment done a while ago which did not turn out to be useful
    

