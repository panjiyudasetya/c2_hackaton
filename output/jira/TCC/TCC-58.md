---
id: jira:TCC-58
source: jira
type: issue
key: TCC-58
project: TCC
board: TCC board
issuetype: Story
priority: Medium
assignee: Unassigned
labels: []
components: []
title: Improve the response you get when requesting an URL in the internal & external
  API when the endpoint doesn't exist
author: Darius Wattimena
status: To Do
date: '2025-03-06'
url: https://teqplaybv.atlassian.net/browse/TCC-58
explicit_links: []
---
# [TCC-58] Improve the response you get when requesting an URL in the internal & external API when the endpoint doesn't exist

**URL:** https://teqplaybv.atlassian.net/browse/TCC-58  
**Type:** Story | **Status:** To Do | **Priority:** Medium  
**Reporter:** Darius Wattimena | **Assignee:** Unassigned  
**Created:** 2025-03-06 | **Updated:** 2025-05-22  
**Board:** TCC board  

## Description

Damon switched to the external API to get VesselVoyage information. Because the URL was different on the side of the external API compared to the VesselVoyage API directly it resulted in calls failing with CORS errors.

The CORS error now given on unknown URLS:

{noformat}Access to fetch at 'https://apidev.teqplay.nl/v2/visit/byImo' from origin 'http://localhost:3000' has been blocked by CORS policy: Response to preflight request doesn't pass access control check: No 'Access-Control-Allow-Origin' header is present on the requested resource. If an opaque response serves your needs, set the request's mode to 'no-cors' to fetch the resource with CORS disabled.{noformat}


The related log line in the backend providing confusing information:

{noformat}2025-03-06 15:45:19,591 INFO  [parallel-4] n.t.a.s.RequestLoggerService: [41b92b1d]  method: OPTIONS, user: null, routeId: null, status: 403 FORBIDDEN, https://apidev.teqplay.nl/v2/visit/byImo <== null (2 ms){noformat}



Instead of giving a 403 on the backend and CORS on the frontend it should provided a 404 both in the backend and frontend.

## Comments

### Damon Asberg — 2025-03-06

yes
