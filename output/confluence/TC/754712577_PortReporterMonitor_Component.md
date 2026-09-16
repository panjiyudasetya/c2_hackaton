---
id: confluence:754712577
source: confluence
type: page
space: TC
title: PortReporterMonitor Component
author: Richard van Klaveren
date: '2025-06-05'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/754712577
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/754712577
---
# PortReporterMonitor Component

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/754712577  

## Content

The PortReporterMonitor Component in Ais Engine is built to do the following 2 functionalities:

* Interpret the Teqplay Events to put them into the context of a portcall. So, for example, a relevant pilot encounter event can become a ‘Pilot on board’ event
* Assign Events related to a portcall or to a Smartfleet. For tools using these events it is important these events have the right meta-data, so the portcallId or the fleetId of the relevant portcalls / smartfleets will be added
* Convert the data in the portcall event model (based on PCO Working Group standard for communication about a Portcall) instead of the internal Teqplay event model.

The following relevant resources are available to grasp a better understanding on the PortReporterMonitor:

* Youtube explanation: <https://www.youtube.com/watch?v=q3dO-ktnIMQ>
* [Functional description of event conversions](https://docs.google.com/document/d/1-ZIiOxSEfYchBYs3hO-2F8LQGeFYtoMBWlZE220u8TM) in PortReporterMonitor
* Overall [Teqplay Architecture picture](https://app.diagrams.net/#G1klTRtqqRzvMzmf8PFNU8ikvKEPHaSOmw#{"pageId"%3A"rDCxWZ16RrHVMkRNnX7i"})
* Specific architecture on PortReporterMonitor, past, target and now.
* Explanation on internal PortReporterMonitor design / flow.
* PortReporterMonitor design description.
* Teqplay [Event Mapping to Portcall events](https://docs.google.com/spreadsheets/d/1FfGqcxzpHZ2S7T8tXrIc0aXJs_B4ZcFtMibV_O9H4W8/edit?gid=0#gid=0)