---
id: github:teqplay/portreporter-backend:issue:765
source: github
type: issue
repo: teqplay/portreporter-backend
number: 765
title: Refacotring/Replace Static Dependencies
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/765
labels: []
explicit_links: []
---
# Issue #765: Refacotring/Replace Static Dependencies

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/765  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [1b7ed4e4157b...02f4eb467a9b](https://github.com/teqplay/portreporter-backend/compare/1b7ed4e4157b...02f4eb467a9b)
**Merge commit:** [02f4eb467a9b](https://github.com/teqplay/portreporter-backend/commit/02f4eb467a9b)
**Author:** Vasyl Pidlisniak
**Reviewers:** Shravan Shetty, Wouter Naloop
**Approvers:** Shravan Shetty
**Source Branch:** [refacotring/replace-static-dependencies](https://github.com/teqplay/portreporter-backend/tree/refacotring/replace-static-dependencies)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2020-05-01T10:11:15.747061+00:00
**Status:** MERGED

* replace static references with dependency injection
* break circular dependencies

Tests are failing and being updated





The idea of this pull request is to replace calling static methods with calling methods on objects. You’d see some ugly constructors, that’s because classes are doing a lot and concerns aren’t clearly separated - this would be fixed separately.

