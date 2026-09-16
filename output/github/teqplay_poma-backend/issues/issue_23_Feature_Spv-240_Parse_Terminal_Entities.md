---
id: github:teqplay/poma-backend:issue:23
source: github
type: issue
repo: teqplay/poma-backend
number: 23
title: Feature/Spv-240 Parse Terminal Entities
author: jbugella
state: closed
date: '2025-01-13'
url: https://github.com/teqplay/poma-backend/issues/23
labels: []
explicit_links: []
---
# Issue #23: Feature/Spv-240 Parse Terminal Entities

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/issues/23  
**State:** closed | **Author:** jbugella  
**Created:** 2025-01-13  
**Closed:** 2025-01-13  

## Description

**Full diff:** [e6d7c7a49ee0...fe65895005a7](https://github.com/teqplay/poma-backend/compare/e6d7c7a49ee0...fe65895005a7)
**Merge commit:** [fe65895005a7](https://github.com/teqplay/poma-backend/commit/fe65895005a7)
**Author:** Darius Wattimena
**Reviewers:** Wouter Naloop
**Approvers:** Wouter Naloop
**Source Branch:** [feature/SPV-240_parse-terminal-entities](https://github.com/teqplay/poma-backend/tree/feature/SPV-240_parse-terminal-entities)
**Destination Branch:** [develop](https://github.com/teqplay/poma-backend/tree/develop)
**Closed On:** 2021-11-16T15:15:52.887769+00:00
**Status:** MERGED

* Started implementing parsing of the terminal entities from gisis
* Corrected location coordinates
* Renamed decimal degrees converter function
* Made last changes to import to be able to import the new terminals
* Removed the master/develop filter on the circleci script to allow deploying feature branches
* Moved the terminal entities to their own feature package, saving them in a separate collection for now
* Removed unneeded import


