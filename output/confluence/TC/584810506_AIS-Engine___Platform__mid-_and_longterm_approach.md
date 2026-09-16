---
id: confluence:584810506
source: confluence
type: page
space: TC
title: AIS-Engine & Platform, mid- and longterm approach
author: Richard van Klaveren
date: '2025-01-03'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/584810506
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/584810506
---
# AIS-Engine & Platform, mid- and longterm approach

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/584810506  

## Content

## PortcallAdapters

HamisPortcallAdapter  
IrisPortcallNLAMSAdapter  
IrisPortcallNLRTMAdapter

PortcallPlusMonitor  
--> plan with mid-term and long-term approach.

* Mid-term:  
   (- Keep running on backend and expose events to RabbitMQ / NATS + portcall+ )

  + should send out events itself with updates on portcalls
* long-term: move them all to portcall+

## LockAdapters

Focus: lock eta/etd events

* NlamsLockAdapter (Ijmuiden)
* RwsLockScraper (Terneuzen, Ghent)

Question: are these events still relevant in PortReporter?  
 mid-term: keep them running in platform, and forward event via new portreporter monitor  
 long-term: Aim for discontinuation

## Port infra monitors

PilotAvailabilityAdapter (BEANR)  
PINMessageAdapter (NLRTM)

* mid-term: not via PortReporterMonitor, let platform post this directly on RabbitMQ (to portReporter)
* long-term: Rebuild separate from platform rebuild / Ais-Engine

## Predictions

PortcallETAMonitor --> ETA predictions

* USHOU
* BEANR
* NLRTM
* NLAMS
* FIHEL
* FIVSS
* SGSIN

### BerthEtaPredictionMonitor

Issue: Antwerp when running this in platform, since portcalls are generated in portcall+ (so platform should not generate events)

* Berth-level: discontinue.
* Berth-level Rotterdam / Amsterdam: could do..... --> check if berth eta is really relevant, focus on discontinue.
* Mid-Term: ETA predictor will do 1 hop ETA predictons for all vessels with a true destination set (portcall/smartfleet stamp via portreporter monitor).
* Long-term: ETA predictor will do 1 hop ETA predictons for all vessels with a true destination set (portcall/smartfleet stamp via portreporter monitor).

### ShipRolesMonitor

* Mid-term: develop shiprole mechanism to keep things up-to-date
* Long-term: develop shiprole mechanism to keep things up-to-date

### PortcallMonitor

* End a portcall whenever

  + the vessel left the port + X hours
  + the vessel starttime in the port 30 days ago
* mid-term: close portcalls in portcall+ (for portcall+ portcalls, backend for NLRTM/NLAMS)
* long-term: close portcalls in portcall+

Portcall+ receiving Port ATA/ATD events

* mid-term: make sure portreportermonitor will send port ata/atd events to portcall+
* long-term: make sure portreportermonitor will send port ata/atd events to portcall+

### ExternalTeqplayEventInjectAdapter

* injecting events from Ais Engine, current use, no change foreseen

### AisSignalMonitor

* Lost / recovered: decided to discontinue

### OeverfrontNummerAdapter

* not used anymore

### NavisMonitor

* not used anymore

### BanyanVopakMonitor

* not used anymore, brrrr

### BrazilMrnPilotMonitor

* not used anymore