---
id: github:teqplay/poma-backend:issue:50
source: github
type: issue
repo: teqplay/poma-backend
number: 50
title: Develop
author: jbugella
state: closed
date: '2025-01-13'
url: https://github.com/teqplay/poma-backend/issues/50
labels: []
explicit_links: []
---
# Issue #50: Develop

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/issues/50  
**State:** closed | **Author:** jbugella  
**Created:** 2025-01-13  
**Closed:** 2025-01-13  

## Description

**Full diff:** [1b8565c698db...f03e78753759](https://github.com/teqplay/poma-backend/compare/1b8565c698db...f03e78753759)
**Merge commit:** [f03e78753759](https://github.com/teqplay/poma-backend/commit/f03e78753759)
**Author:** Wouter Naloop
**Reviewers:** 
**Approvers:** 
**Source Branch:** [develop](https://github.com/teqplay/poma-backend/tree/develop)
**Destination Branch:** [master](https://github.com/teqplay/poma-backend/tree/master)
**Closed On:** 2023-01-30T16:33:40.387436+00:00
**Status:** MERGED

* SPV-1146: Add cargo category type and cargo type to terminals
* SPV-1146: Add scripts to recalculate the current data in the berths and terminals
* SPV-1114: Eos area
* SPV-1146: ktlint
* SPV-1144: add terminal groups and a way to create them
* SPV-1114: feedback processing
* SPV-1146: add early return when no terminalId and terminalName are given, use the Boundingbox constructor where we know all values are non null
* SPV-1146: small change on the getBoundingbox logic
* SPV-1146: ktlint pls
* Add the area size in square meters on the fly to the models
* SPV-1114: nullability and empty lists instead of arraylists, is slightly faster
* SPV-1146: nullability and empty sets
* circleci changes because of key rotation
* SPV-1146: resolve merge conflicts
* SPV-1114: ktlint, pls
* SPV-1114: add emptylists if in the database the areas are null
* SPV-1114: woops too much nullability
* SPV-1114: :'\(
* SPV-1114: fix outerArea take if bug, make the outerArea default to emptyList and not nullable
* SPV-1144: remove the datasource for terminal groups and recalculate it by all the entries in the terminals
* SPV-1144: remove the unused endpoints
* SPV-1144: default berth and terminal sets to accomodate for legacy database null values
* SPV-1144: only get a distinct list and filter empty strings out
* DEV-114: Updated resources used to have no CPU limit and memory request and limit be the same
* weird and random
* PRA-463: hash the uniqueId, remove the createOrUpdate method which had the possibilty to override \_id if it was given by the frontend
* PRA-463: removed uniqueId to uppercase, because that is not always the case for legacy reasons
* PRA-463: ktlint pls
* PRA-463: ktlint pls
* PRA-463: added test cases
* PRA-463: added more test cases
* PRA-463: simplify the getting of the uniqueId
* PRA-463: additional case to test if TestSpaces does not result into the same as Test Spaces
* PRA-463: if the endresult was prepended with a 0 the current algorithm got it wrong. got a new one and added the tests for the new algorithm, the new algorithm uppercases the results, and I liked it. also found out that the collection name of breakwaterarea was changed at some point accidently
* removed an unnecessary comment

