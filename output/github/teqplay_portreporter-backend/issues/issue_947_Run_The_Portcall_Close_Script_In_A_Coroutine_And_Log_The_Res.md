---
id: github:teqplay/portreporter-backend:issue:947
source: github
type: issue
repo: teqplay/portreporter-backend
number: 947
title: Run The Portcall Close Script In A Coroutine And Log The Results
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/947
labels: []
explicit_links: []
---
# Issue #947: Run The Portcall Close Script In A Coroutine And Log The Results

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/947  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [916b28d106ad...3d9c370c4d82](https://github.com/teqplay/portreporter-backend/compare/916b28d106ad...3d9c370c4d82)
**Merge commit:** [3d9c370c4d82](https://github.com/teqplay/portreporter-backend/commit/3d9c370c4d82)
**Author:** Wouter Naloop
**Reviewers:** Joost Laurman, Joaquin Marquez Bugella
**Approvers:** Joost Laurman
**Source Branch:** [feat/rewrite_close_portcalls](https://github.com/teqplay/portreporter-backend/tree/feat/rewrite_close_portcalls)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2021-09-09T15:31:27.900909+00:00
**Status:** MERGED

I have done 2 things here, 

1 make the IO coroutine bit a function and write docs around why its there. 

2 launch a coroutine to perform the closing of portcalls and log that, as the timeout was too low to execute this script from postman otherwise

