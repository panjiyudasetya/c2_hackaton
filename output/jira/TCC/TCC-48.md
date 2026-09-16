---
id: jira:TCC-48
source: jira
type: issue
key: TCC-48
project: TCC
board: TCC board
issuetype: Story
priority: Medium
assignee: Unassigned
labels: []
components: []
title: Re-implement functionality in PortMatcher to handle ships that travel the same
  route and don't change their destination
author: Darius Wattimena
status: To Do
date: '2024-11-11'
url: https://teqplaybv.atlassian.net/browse/TCC-48
explicit_links:
- jira:CC-71
---
# [TCC-48] Re-implement functionality in PortMatcher to handle ships that travel the same route and don't change their destination

**URL:** https://teqplaybv.atlassian.net/browse/TCC-48  
**Type:** Story | **Status:** To Do | **Priority:** Medium  
**Reporter:** Darius Wattimena | **Assignee:** Unassigned  
**Created:** 2024-11-11 | **Updated:** 2025-05-22  
**Board:** TCC board  

## Description

In PortMatcher we want to handle cases like {{NLRTM <-> NLAMS}}. Here we want to get the last port ATD event of either {{NLRTM}} or {{NLAMS}} and based on that provide a true destination of the other port. Meaning if we got a port ATD of {{NLRTM}}, then our true destination will be {{NLAMS}} and visa versa.

Next to that something smart needs to be made to keep this true destination up-to-date, as right now we will not update the true destination anymore as it is only determined when the AIS destination is adjusted (which doesn’t happen for ships that have this case).

With the old decision of using VesselVoyage V1 we also had a limitation that only ships with IMO were tracked, meaning all ships with only an MMSI were ignored.

----

Out of the envision we decided on this kind of flow:

# On resolving a case with {{<->}} search the last port ATD of either of the ports on both sides.
# Get the last 7 days of port ATD’s of the MMSI from EventHistory.
# In some way track that we have a case of a ship with no destination changes and listen to all port ATD for those vessels.
# Once the ship enters the new port, update the true destination and trigger a TrueDestinationEvent for this ship.

The tracking part might need some more thinking through…

## Linked issues

- relates to: [CC-71] Re-evaluate if the VesselVoyage functionality in PortMatcher is something we need and re-introduce with V2 if needed
