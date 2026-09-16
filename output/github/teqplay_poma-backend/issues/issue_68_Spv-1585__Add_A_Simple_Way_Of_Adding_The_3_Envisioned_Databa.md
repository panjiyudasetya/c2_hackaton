---
id: github:teqplay/poma-backend:issue:68
source: github
type: issue
repo: teqplay/poma-backend
number: 68
title: 'Spv-1585: Add A Simple Way Of Adding The 3 Envisioned Databases (Original,
  Merged And External) For The World Of Ports Data.'
author: jbugella
state: closed
date: '2025-01-13'
url: https://github.com/teqplay/poma-backend/issues/68
labels: []
explicit_links: []
---
# Issue #68: Spv-1585: Add A Simple Way Of Adding The 3 Envisioned Databases (Original, Merged And External) For The World Of Ports Data.

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/issues/68  
**State:** closed | **Author:** jbugella  
**Created:** 2025-01-13  
**Closed:** 2025-01-13  

## Description

**Full diff:** [898ee50f17d9...c930e6dfc005](https://github.com/teqplay/poma-backend/compare/898ee50f17d9...c930e6dfc005)
**Merge commit:** [c930e6dfc005](https://github.com/teqplay/poma-backend/commit/c930e6dfc005)
**Author:** Wouter Naloop
**Reviewers:** Joost Laurman, Leon Joosse, Darius Wattimena
**Approvers:** Darius Wattimena, Leon Joosse
**Source Branch:** [SPV-1585/multiple_databases](https://github.com/teqplay/poma-backend/tree/SPV-1585/multiple_databases)
**Destination Branch:** [develop](https://github.com/teqplay/poma-backend/tree/develop)
**Closed On:** 2023-08-25T08:48:36.036366+00:00
**Status:** MERGED

Helloooo,   
  
This PR is the copy heavy but reasonable simple but flexible approach to adding 2 extra databases to poma.  
  
So we want is to have 3 versions of the poma data   
- External sources their data \( for legal reasons has to be seperate\)  
- The original Teqplay poma   
- A merged view of both the external sources and the teqplay data  
  
This External database thingie will be filled with bought data and then later a merge strategy will be added to fill the merged db.   
  
All requesting the API should go to the merged Database except for persons that are accessing the FE.  
  
For that i made Roles that are linked to the databases. Each Role always goes to 1 database, later admins should be able to choose or something.

