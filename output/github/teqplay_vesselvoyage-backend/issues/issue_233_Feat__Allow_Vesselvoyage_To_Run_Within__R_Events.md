---
id: github:teqplay/vesselvoyage-backend:issue:233
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 233
title: 'Feat: Allow Vesselvoyage To Run Within (R)Events'
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/233
labels: []
explicit_links: []
---
# Issue #233: Feat: Allow Vesselvoyage To Run Within (R)Events

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/233  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [aa51eb3e474b...9ecac8479b00](https://github.com/teqplay/vesselvoyage-backend/compare/aa51eb3e474b...9ecac8479b00)
**Merge commit:** [9ecac8479b00](https://github.com/teqplay/vesselvoyage-backend/commit/9ecac8479b00)
**Author:** Former user
**Reviewers:** Michel Wilson, Darius Wattimena
**Approvers:** Darius Wattimena
**Source Branch:** [SPV-2134-run-vesselvoyage-in-revents](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2134-run-vesselvoyage-in-revents)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-06-18T11:39:03.331434+00:00
**Status:** MERGED

This PR requires these changes to be published:  
[https://bitbucket.org/teqplay/ais-engine/pull-requests/1019](https://bitbucket.org/teqplay/ais-engine/pull-requests/1019) 
This PR adds support for running VesselVoyage within \(r\)events. Ensuring events that are received out-of-order are sorted before being processed, and sending a poison pill when processing has completed.

