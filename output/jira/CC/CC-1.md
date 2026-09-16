---
id: jira:CC-1
source: jira
type: issue
key: CC-1
project: CC
board: CC board
issuetype: Epic
priority: Medium
assignee: Unassigned
labels: []
components: []
title: Poma Syncing
author: Darius Wattimena
status: Done
date: '2024-07-18'
url: https://teqplaybv.atlassian.net/browse/CC-1
explicit_links: []
---
# [CC-1] Poma Syncing

**URL:** https://teqplaybv.atlassian.net/browse/CC-1  
**Type:** Epic | **Status:** Done | **Priority:** Medium  
**Reporter:** Darius Wattimena | **Assignee:** Unassigned  
**Created:** 2024-07-18 | **Updated:** 2024-11-05  
**Board:** CC board  

## Description

_No description._

## Comments

### Pim van den Toorn — 2024-09-09

[~accountid:5e37d9154512b80ca4319871] pls test

[~accountid:63e01252c2b1cb6b3472aad3] Richard asked if you could test this, so please do. If you need anything just message me on slack.



These are merged with the develop branch, so you can test from there.

These changes are running on dev and sandbox, but only sandbox currently has the credentials to acces dev and prod, so request sandbox to test.

Syncing per port is currently not possible from prod, as prod misses a necessary endpoint, so only test that with DEV as the source.



If you want to test it on your own machine, these are the preparations:

Add PROD, DEV and/or SANDBOX credentials to the properties and set enabled: true for those.

Go to PortService.convertToInfrastructureModel and remove the null check for timeZone, as PROD and DEV don’t have the tz yet and calling resolveTimeZone for each takes ages. Otherwise just sync from sandbox



SyncController endpoint at “/v1/sync”

[https://teqplaybv.atlassian.net/browse/CC-2|https://teqplaybv.atlassian.net/browse/CC-2|smart-link] : 

“/{source}” endpoint (PROD, DEV or SANDBOX)

Defaults to only return the differences, request param synchronize true to also synchronize

extra feature: “/{source}/{infrastructureType}” to only show or sync that infrastructure type



[https://teqplaybv.atlassian.net/browse/CC-3|https://teqplaybv.atlassian.net/browse/CC-3|smart-link] : 

“/{source}/ports” endpoint, specify the port or ports in the request params as “?ports=NLRTM,BEANR”.

Also defaults to only return differences.

Only call to SANDBOX, as dev and prod don’t have the getByPorts yet.



[https://teqplaybv.atlassian.net/browse/CC-4|https://teqplaybv.atlassian.net/browse/CC-4|smart-link] : 

Removed as it’s being deprecated, whitelisted now in the port model.



[https://teqplaybv.atlassian.net/browse/CC-5|https://teqplaybv.atlassian.net/browse/CC-5|smart-link] : 

Syncs are logged to the “sync_log” collection.



[https://teqplaybv.atlassian.net/browse/CC-6|https://teqplaybv.atlassian.net/browse/CC-6|smart-link] : 

Any of the CC-2 and CC-3 endpoints return the difference, whether actually syncing or not
