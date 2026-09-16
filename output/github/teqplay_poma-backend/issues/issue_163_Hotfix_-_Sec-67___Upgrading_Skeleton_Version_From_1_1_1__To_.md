---
id: github:teqplay/poma-backend:issue:163
source: github
type: issue
repo: teqplay/poma-backend
number: 163
title: 'Hotfix - Sec-67 : Upgrading Skeleton Version From 1.1.1. To 1.8.1.'
author: jbugella
state: closed
date: '2025-01-13'
url: https://github.com/teqplay/poma-backend/issues/163
labels: []
explicit_links: []
---
# Issue #163: Hotfix - Sec-67 : Upgrading Skeleton Version From 1.1.1. To 1.8.1.

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/issues/163  
**State:** closed | **Author:** jbugella  
**Created:** 2025-01-13  
**Closed:** 2025-01-13  

## Description

**Full diff:** [18b131e56a8e...3366526f6878](https://github.com/teqplay/poma-backend/compare/18b131e56a8e...3366526f6878)
**Merge commit:** [3366526f6878](https://github.com/teqplay/poma-backend/commit/3366526f6878)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Joost Dambrink
**Approvers:** 
**Source Branch:** [hotfix/SEC-67/removing_sensitive_credential_logs](https://github.com/teqplay/poma-backend/tree/hotfix/SEC-67/removing_sensitive_credential_logs)
**Destination Branch:** [master](https://github.com/teqplay/poma-backend/tree/master)
**Closed On:** 2024-10-11T10:58:33.102617+00:00
**Status:** MERGED

Adding @{5f4cda8d3e9e2e004d5edf39} to be aware of it.
The _motiv_ is to stop writing in logs sensitive auth information \(such as the accessToken\).
The fix is also applied on develop \(see [https://github.com/teqplay/poma-backend/issues/163](https://github.com/teqplay/poma-backend/issues/163) \)

