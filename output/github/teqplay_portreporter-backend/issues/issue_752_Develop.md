---
id: github:teqplay/portreporter-backend:issue:752
source: github
type: issue
repo: teqplay/portreporter-backend
number: 752
title: Develop
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/752
labels: []
explicit_links: []
---
# Issue #752: Develop

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/752  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [5006f5d7e9fb...ccfdd447cfec](https://github.com/teqplay/portreporter-backend/compare/5006f5d7e9fb...ccfdd447cfec)
**Merge commit:** [ccfdd447cfec](https://github.com/teqplay/portreporter-backend/commit/ccfdd447cfec)
**Author:** Shravan Shetty
**Reviewers:** 
**Approvers:** 
**Source Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Destination Branch:** [master](https://github.com/teqplay/portreporter-backend/tree/master)
**Closed On:** 2020-03-25T15:45:37.396808+00:00
**Status:** MERGED

* made first steps to move all logic centrally for portcalleventtype
* added logic to portcallEventType
* code clean up
* review feedback from wouter
* create empty subscriptions for shipping companies too
* only reduce pilot event time if it is a fallback event
* create test for the pilot events fallback or no fallback
* made portcall structuring logic generic and easier to read
* code clean up
* moved some more eventType logic to Enum class. Improved readability
* moved tests to more correct json test resources and fetch it only once to make tests efficient
* add berthVisitIndex to context info
* fix singleton issue with AuthConnection
* Added formatting and content for pilot ladder messages
* added a lock in processing a portcall event
* bumped version to 1.40.3
* review feedback
* deprecate `isDirectBilling` in ShippingCompany. Moved it to InvoiceOptions
* Added option to add a note to each subscription. This is currently only used in email notification
* added mongo script to copy directBilling from shippingCompany to invoiceOptions
* added breaking changelog
* append fromSea to a portcall if found in the event
* review feedback. added test for shippingCompany with direct and indirect billing for different port
* added some spaces for readability
* Added check if note is empty and added unit test
* Change null check to nullOrBlank
* Make note bold and orange in mail
* Added check if portcall has been cancelled before invoicing


