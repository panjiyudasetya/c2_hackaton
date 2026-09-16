---
id: confluence:214532102
source: confluence
type: page
space: TC
title: New PortReporter monitor in production
author: Darius Wattimena
date: '2023-09-26'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/214532102
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/214532102
---
# New PortReporter monitor in production

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/214532102  

## Content

As decided before with item 3 from PortcallMonitor in platform rebuild, the portcalls of NLRTM and NLAMS will still be handled by Platform, as the data comes from HAMIS/IRIS.

## 1. Steps to get the new PortReporterMonitor LIVE

* The `PortcallPlusSubSystem` will be turned off on the side of Platform.
* PortcallPlus will create the events, already provided with a portcall ID.

  + This will result in the new PortReporterMonitor handling the events, but it will not go back to PortcallPlus to get the portcall ID, as the events already contain this ID.
* The Lock ETA/ETD monitor will be disabled for NLTNZ and BEGNE.

These ETA / ETD events are currently not being actively used, and since our lock monitors (NLAMS + NLTNZ/BEGNE) are monitoring ports where the authoritative source for the portcallId is respectively Platform (Backend) or PortcallPlus, it makes it easier to choose a house for the lock monitor. With this approach it stays (for now) in Platform.

* The PortcallEtaMonitors will be disabled for BEANR, SGSIN, FIHEL and FIVSS. Since the source for these eta predictors for portcalls is in PortcallPlus.

These ETA’s are currently not actively used.

* TeqplayEvents will no longer be handled by the old PortReporterMonitor.

  + This means when TeqplayEvents of NLRTM and NLAMS request a portcall ID from PortcallPlus, the question is forwarded to Platform.

This means that no Lock ETA/ETD events will be generated for NLTNZ and BEGNE. This also means that there will be no ETA’s generated for BEANR, SGSIN, FIHEL and FIVSS.

## 2. Not affected by the change

* The PIN messages will stay in Platform.
* The VTS Scheldt messages made by the PilotAvailablityAdapter are not portcall related, so they can stay in Platform.
* The LockMonitor for NLAMS lock can stay in Platform.

## 3. Long term steps

* Website scrapers will be moved to their own component outside of Platform.

  + The PIN website scraper.
  + The lock ETA/ETD scrapers for NLAMS, NLTNZ and BEGNE.
* Port ETA prediction for portcalls will be moved to their own component.
* The source for portcalls for NLRTM and NLAMS will need to be moved to PortcallPlus.