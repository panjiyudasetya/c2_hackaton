---
id: github:teqplay/poma-backend:issue:166
source: github
type: issue
repo: teqplay/poma-backend
number: 166
title: Displayname Minor Fix Endpoint Change
author: jbugella
state: closed
date: '2025-01-13'
url: https://github.com/teqplay/poma-backend/issues/166
labels: []
explicit_links: []
---
# Issue #166: Displayname Minor Fix Endpoint Change

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/issues/166  
**State:** closed | **Author:** jbugella  
**Created:** 2025-01-13  
**Closed:** 2025-01-13  

## Description

**Full diff:** [ca61c00bebd0...d503e78cc644](https://github.com/teqplay/poma-backend/compare/ca61c00bebd0...d503e78cc644)
**Merge commit:** [d503e78cc644](https://github.com/teqplay/poma-backend/commit/d503e78cc644)
**Author:** Pim van den Toorn
**Reviewers:** Joaquin Marquez Bugella
**Approvers:** Joaquin Marquez Bugella
**Source Branch:** [CC-58-sync-issue](https://github.com/teqplay/poma-backend/tree/CC-58-sync-issue)
**Destination Branch:** [develop](https://github.com/teqplay/poma-backend/tree/develop)
**Closed On:** 2024-11-05T09:07:30.189205+00:00
**Status:** MERGED

Just heard from Darius that maybe displayName should explicitly not be nullable, but I can’t check the prod db. Maybe not do this and just run a script over all the databases that fixes all the absent ones
>> Now just minor changes on displayName fix

