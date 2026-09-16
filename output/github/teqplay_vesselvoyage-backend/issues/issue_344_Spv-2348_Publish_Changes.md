---
id: github:teqplay/vesselvoyage-backend:issue:344
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 344
title: Spv-2348 Publish Changes
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/344
labels: []
explicit_links:
- jira:SPV-2348
---
# Issue #344: Spv-2348 Publish Changes

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/344  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [a6d79b02dc60...293bf0c43c64](https://github.com/teqplay/vesselvoyage-backend/compare/a6d79b02dc60...293bf0c43c64)
**Merge commit:** [293bf0c43c64](https://github.com/teqplay/vesselvoyage-backend/commit/293bf0c43c64)
**Author:** Darius Wattimena
**Reviewers:** Michel Wilson, Leon Joosse, Gavin den Hollander
**Approvers:** Michel Wilson
**Source Branch:** [SPV-2348-publish-changes](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2348-publish-changes)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-09-23T13:48:25.226015+00:00
**Status:** MERGED

Adds publishing of the internal changes to an outgoing changes model which publishes:
* The API Visit model and PTO SOF model when an internal Visit or related ESoF changes
* The API Voyage model when an internal Voyage or related ESoF changes

What is being published is also configurable in multiple ways:
* With a toggle `event-publishing.enabled` to fully toggle on and off the publishing
* With a list of enabled publishers via `event-publishing.enabled-publishers` where you can disable PTO SOF or API Entries \(API Visits and Voyages\) publishing individually

I’ve added a bunch of test cases as well which should cover all the weird changes that can happen with event processing.

