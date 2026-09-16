---
id: github:teqplay/vesselvoyage-backend:issue:107
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 107
title: Stop Improvements
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/107
labels: []
explicit_links: []
---
# Issue #107: Stop Improvements

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/107  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [b261d6afa63e...8af7d2d74f45](https://github.com/teqplay/vesselvoyage-backend/compare/b261d6afa63e...8af7d2d74f45)
**Merge commit:** [8af7d2d74f45](https://github.com/teqplay/vesselvoyage-backend/commit/8af7d2d74f45)
**Author:** Darius Wattimena
**Reviewers:** Wouter Naloop
**Approvers:** Wouter Naloop
**Source Branch:** [stop_improvements](https://github.com/teqplay/vesselvoyage-backend/tree/stop_improvements)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2022-12-19T16:23:43.301138+00:00
**Status:** MERGED

* changed some log levels to reduce log spamming
* Fixed in V2 stops that the actual location is based on the trace of all combining stops. Fixed in V3 that the actual location is now also based on the duration of the stop.
* Added an extra check on V3 stops to combine when the distance between them is small, being basically on top of each other without taking into account the time in between
* Changed the logic a bit more to only combine close overlapping stops when the ship is "big"
* Changed unit tests to reflect the new way of combining

