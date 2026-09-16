---
id: github:teqplay/poma-backend:issue:95
source: github
type: issue
repo: teqplay/poma-backend
number: 95
title: 'Fix: Only Link Berths To Terminals With The Terminalid'
author: jbugella
state: closed
date: '2025-01-13'
url: https://github.com/teqplay/poma-backend/issues/95
labels: []
explicit_links: []
---
# Issue #95: Fix: Only Link Berths To Terminals With The Terminalid

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/issues/95  
**State:** closed | **Author:** jbugella  
**Created:** 2025-01-13  
**Closed:** 2025-01-13  

## Description

**Full diff:** [898ee50f17d9...d1fe88db6272](https://github.com/teqplay/poma-backend/compare/898ee50f17d9...d1fe88db6272)
**Merge commit:** [d1fe88db6272](https://github.com/teqplay/poma-backend/commit/d1fe88db6272)
**Author:** Former user
**Reviewers:** Wouter Naloop, Maryam Tavakoli
**Approvers:** Maryam Tavakoli
**Source Branch:** [SPV-1784-only-link-berths-to-terminals-with-the-terminal-id](https://github.com/teqplay/poma-backend/tree/SPV-1784-only-link-berths-to-terminals-with-the-terminal-id)
**Destination Branch:** [master](https://github.com/teqplay/poma-backend/tree/master)
**Closed On:** 2023-09-01T09:31:01.816478+00:00
**Status:** MERGED

The berths were linked to terminals by both the `terminalId` and `terminalName`. This led to issues, since the same name can be used multiple times in different parts of the world. And cause the following for the terminal mooring area:
![](https://bitbucket.org/repo/7zbd4Ep/images/887609923-image.png)
This PR makes it only link by the `terminalId`.

