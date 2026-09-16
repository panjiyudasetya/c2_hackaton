---
id: github:teqplay/poma-backend:issue:97
source: github
type: issue
repo: teqplay/poma-backend
number: 97
title: 'Feat(Port): Add Manualoverriddeneosarea To Port'
author: jbugella
state: closed
date: '2025-01-13'
url: https://github.com/teqplay/poma-backend/issues/97
labels: []
explicit_links: []
---
# Issue #97: Feat(Port): Add Manualoverriddeneosarea To Port

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/issues/97  
**State:** closed | **Author:** jbugella  
**Created:** 2025-01-13  
**Closed:** 2025-01-13  

## Description

**Full diff:** [d1fe88db6272...fcf97f60acb7](https://github.com/teqplay/poma-backend/compare/d1fe88db6272...fcf97f60acb7)
**Merge commit:** [fcf97f60acb7](https://github.com/teqplay/poma-backend/commit/fcf97f60acb7)
**Author:** Former user
**Reviewers:** Wouter Naloop, Maryam Tavakoli
**Approvers:** Wouter Naloop
**Source Branch:** [SPV-1808-eos-area-overriden-flag](https://github.com/teqplay/poma-backend/tree/SPV-1808-eos-area-overriden-flag)
**Destination Branch:** [master](https://github.com/teqplay/poma-backend/tree/master)
**Closed On:** 2023-09-13T11:53:53.758131+00:00
**Status:** MERGED

This PR adds initial support for just the `manualOverriddenEosArea` field.
This can be merged “way” in advance of the subsequent automatic updating of the EOS:  
[https://teqplaybv.atlassian.net/browse/SPV-1807](https://teqplaybv.atlassian.net/browse/SPV-1807) 
This is important, since the database will need to be adjusted to set `manualOverridenEosArea=true` for all entries that already have this manually set right now.

