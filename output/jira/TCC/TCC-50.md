---
id: jira:TCC-50
source: jira
type: issue
key: TCC-50
project: TCC
board: TCC board
issuetype: Story
priority: Medium
assignee: Unassigned
labels: []
components: []
title: 'Envision: Define a way how to deal with Pontoons being registered in CSI with
  an invalid IMO by PoR'
author: Richard van Klaveren
status: To Do
date: '2025-02-12'
url: https://teqplaybv.atlassian.net/browse/TCC-50
explicit_links: []
---
# [TCC-50] Envision: Define a way how to deal with Pontoons being registered in CSI with an invalid IMO by PoR

**URL:** https://teqplaybv.atlassian.net/browse/TCC-50  
**Type:** Story | **Status:** To Do | **Priority:** Medium  
**Reporter:** Richard van Klaveren | **Assignee:** Unassigned  
**Created:** 2025-02-12 | **Updated:** 2025-05-22  
**Board:** TCC board  

## Description

Some time ago Jamie has implemented a mechanism to not allow invalid MMSI nor IMO number during creation and updating of CSI ships. This has led to some challenges since IRIS is providing invalid IMOs on Pontoons which have a portcall in the port of Rotterdam. 
Before this was resulting into platform registering those vessels with an invalid IMO in CSI, and thus could portreporter lookup the vesseldetails as soon as the portcall with that IMO were received. Since now this registration of the vessel is rejected, PortReporter does not have any information on the portcall but a invalid IMO.

2 possible directions are foreseen:

# put the invalid imo in a dedicated ‘invalid_imo’ field (which will snowball quite quickly to changes everywhere on the shipmodel)
# put the invalid imo in the imo field, but mark it as invalid and only allow it to be set after explicit agreement of the setter that he wants this imo to be invalid. It is not clear where this approach is going to bite us in the future.

For now, current behaviour of portreporter is that it will check everytime the portcall is touched the imo with CSI, resulting into many records in the ‘#data-quality’ channel in slack
