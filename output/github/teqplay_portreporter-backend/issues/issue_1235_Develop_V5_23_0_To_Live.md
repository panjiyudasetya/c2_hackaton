---
id: github:teqplay/portreporter-backend:issue:1235
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1235
title: Develop V5.23.0 To Live
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1235
labels: []
explicit_links: []
---
# Issue #1235: Develop V5.23.0 To Live

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1235  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [4996bf160cd0...5915649ea5c9](https://github.com/teqplay/portreporter-backend/compare/4996bf160cd0...5915649ea5c9)
**Merge commit:** [5915649ea5c9](https://github.com/teqplay/portreporter-backend/commit/5915649ea5c9)
**Author:** Joaquin Marquez Bugella
**Reviewers:** 
**Approvers:** 
**Source Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Destination Branch:** [master](https://github.com/teqplay/portreporter-backend/tree/master)
**Closed On:** 2023-03-14T12:24:21.979169+00:00
**Status:** MERGED

* PRP-1658 : Forbidding deleting an agent, shipping Company or shipping line if there are invoices linked to them.  
  \(pull request #583\) Approved-by: Wouter Naloop
* Fix: change the default locale from from ENGLISH to UK to get european weeks \(starting on Monday\).  
  \(pull request #588\) Approved-by: Gavin den Hollander
* Feat/PRP-1552/invoice summarized search endpoint and Including sorting options.  
  \(pull request #589\) Approved-by: Michel Wilson
* Merged in temp/adding\_hashing\_for\_berth\_matching.  
  Added sha1 hashing to the matching method that matches berth events and berth visits together.  
  \(pull request #570\) Approved-by: Darius Wattimena
* Feature/PRP-1326 Return a 400 \(BAD\_REQUEST\) when requesting a subscriptionProfile of a company that doesnt' exist.  
  \(pull request #579\) Approved-by:  Wouter Naloop and Joaquin Marquez Bugella
* Feature/PRP-517 bugfix portcall search duplicates  
  \(pull request #590\) Approved-by: Wouter Naloop and Joaquin Marquez Bugella
* Feature/PRP-1531 bugfix password change request checks mail validity  
  \(pull request #581\) Approved-by: Wouter Naloop and Joaquin Marquez Bugella
* Feature/PRP-1532 bugfix userProfile fcm returned data  
  \(pull request #586\) Approved-by: Wouter Naloop and Joaquin Marquez Bugella
* Feature/PRP-1499 bugfix check for invalid email  
  \(pull request #587\) Approved-by: Wouter Naloop and Joaquin Marquez Bugella
* PRP-1636 : Fix the spreadsheet generation of kickback overviews for shippinglines and agencies: including the correct credit invoices in the given time period.  
  \(pull request #591\) Approved-by: Gavin den Hollander
* Feature/PRP-1524 bugfix: not returning valid terminal when terminal id doesnt' exist.  
  \(pull request #578\) Approved-by: Wouter Naloop and Joaquin Marquez Bugella
* PRP-1453 : Consider the timezone of the Spring Scheduled tasks in the calculation of week-shifting seconds.  
  \(pull request #594\) Approved-by: Michel Wilson

