---
id: github:teqplay/poma-backend:issue:142
source: github
type: issue
repo: teqplay/poma-backend
number: 142
title: Release 15-07-2024
author: jbugella
state: closed
date: '2025-01-13'
url: https://github.com/teqplay/poma-backend/issues/142
labels: []
explicit_links: []
---
# Issue #142: Release 15-07-2024

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/issues/142  
**State:** closed | **Author:** jbugella  
**Created:** 2025-01-13  
**Closed:** 2025-01-13  

## Description

**Full diff:** [96df31984413...df425a02b67c](https://github.com/teqplay/poma-backend/compare/96df31984413...df425a02b67c)
**Merge commit:** [df425a02b67c](https://github.com/teqplay/poma-backend/commit/df425a02b67c)
**Author:** Maryam Tavakoli
**Reviewers:** Wouter Naloop, Darius Wattimena
**Approvers:** Wouter Naloop
**Source Branch:** [develop](https://github.com/teqplay/poma-backend/tree/develop)
**Destination Branch:** [master](https://github.com/teqplay/poma-backend/tree/master)
**Closed On:** 2024-07-16T08:33:20.808859+00:00
**Status:** MERGED

* Added approach and break water areas to getEosArea\(\),
* Added multi approach and break water area search to multi-port search
* Updated tests
* stop using world of port data
* add try catch to retrieving timezones, because the timezone stuff uses poma. So when trying to add a poma port it tries to ask for that poma port and gives a 404
* We wanted to use custom areas for things that are very close to eachother for if we don't know the name of an area, but this was limited by the generation of the id
* including the deletion of the terminal entity

