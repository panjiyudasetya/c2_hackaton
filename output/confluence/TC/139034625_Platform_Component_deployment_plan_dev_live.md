---
id: confluence:139034625
source: confluence
type: page
space: TC
title: Platform Component deployment plan dev/live
author: Richard van Klaveren
date: '2022-10-04'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/139034625
explicit_links:
- jira:PRA-259
- jira:PRA-260
- jira:PRA-256
- jira:PRA-257
- jira:PRA-261
- jira:PRA-262
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/139034625
---
# Platform Component deployment plan dev/live

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/139034625  

## Content

It has been decided to move from the old monolith Teqplay Platform to the one based on functional smaller components that are designed to be scalable and prepared to be highly available. However, moving from the old architecture to the new one will require to address specific things that might be addressed differently in the old paradigm than in the new one. Therefore this document describes the relevant steps to be addressed, with the envisioned situations that need special care. It is a working document, where each step will be more and more detailed throughout the discussions.

1. AISData → AisStream Conversion

   1. Rest interface usage

      1. no blocker, only internal use, so redirect calls
   2. True destination being calculated in central component and reused in all others

      1. Move Portmatcher into architecture in the stream to calculate trueDestination and send out as separate event (no need for highly available) based on DestinationChangedEvent.

         1. No blocker since now calculated in backendpronto
   3. Corrected heading berth being calculated and communicated to other components as part of the ais information in the REST interface

      1. in berth event embedded
      2. stored in Ship history component for use by other components

         1. No blocker, now calculated in backendpronto
   4. Monitoring:

      1. [Availability of the node + nr of restarts in a short time via prometheus](https://teqplaybv.atlassian.net/browse/PRA-259)
      2. [Message rates per sub-source to be monitored via prometheus](https://teqplaybv.atlassian.net/browse/PRA-260)

         1. Relevant, blocking production, not dev
2. Start-Stop + Ship Info changed monitors: Please note that functionally all need to be tested before deployment to live

   1. [Conversion of events on new architecture to rabbitmq to old architecture](https://teqplaybv.atlassian.net/browse/PRA-256)

      1. available, to be tested?
   2. Event forwarding/conversion/filtering needs to be defined

      1. [Selection of events mechanism is required to prevent flooding of old architecture](https://teqplaybv.atlassian.net/browse/PRA-257)
   3. enable externalevents on global, disable all local adapters
3. Setup [AisEvent](https://teqplaybv.atlassian.net/browse/PRA-261) and [TeqplayEvent](https://teqplaybv.atlassian.net/browse/PRA-262) Storage and retrieval

   1. Which apps / data science scripts to reconfigure to point to the new systems

      1. Reconfigure to internal API → ship history service + event history service
   2. Which internal API endpoints are required to (Backward Compatible)?

      1. to be analysed
   3. Implement platform endpoints as a proxy towards internal API and warn on any use the devOps team
   4. Minimizing platform storage (only for 7 days or so?)
   5. Storage conversion from old platform instances to new components

---

1. Area Monitor + berth

   1. Which event is created where, and which one is require where?
   2. Role of POMA, can it be the always authoritative source on areas and monitors?
2. Encounter Monitor

   1. How to make sure we can guarantee / outperform quality
   2. CSI integration (role / isSeaVessel)
   3. PoMa integration (excl. zones)
3. Anchor Monitor
4. PortReporter Monitor portcall component

   1. IRIS / HAMIS in Portcall+