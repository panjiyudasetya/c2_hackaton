---
id: github:teqplay/portreporter-backend:issue:1067
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1067
title: 'Spv-802: Bugfix, Assign Future Visits To Inbound Portcalls Only'
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1067
labels: []
explicit_links:
- jira:SPV-802
---
# Issue #1067: Spv-802: Bugfix, Assign Future Visits To Inbound Portcalls Only

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1067  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [e579df1a6104...38f6335b77df](https://github.com/teqplay/portreporter-backend/compare/e579df1a6104...38f6335b77df)
**Merge commit:** [38f6335b77df](https://github.com/teqplay/portreporter-backend/commit/38f6335b77df)
**Author:** Former user
**Reviewers:** Joaquin Marquez Bugella
**Approvers:** Joaquin Marquez Bugella
**Source Branch:** [SPV-802-future-visits-are-assigned-to-ou](https://github.com/teqplay/portreporter-backend/tree/SPV-802-future-visits-are-assigned-to-ou)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2022-04-13T13:14:37.471531+00:00
**Status:** MERGED

Small fix, if two portcalls are close enough to the same visit, it will always pick the closest. But the closest visit might have an outbound status, which shouldn’t happen for a future visit, those should only be inbound.

