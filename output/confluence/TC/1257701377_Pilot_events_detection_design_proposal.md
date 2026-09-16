---
id: confluence:1257701377
source: confluence
type: page
space: TC
title: Pilot events detection design proposal
author: Joaquin Marquez Bugella
date: '2026-07-13'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1257701377
explicit_links:
- jira:PROJ-824
- jira:PROJ-825
- jira:PROJ-826
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1257701377
---
# Pilot events detection design proposal

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1257701377  

## Content

none

# Events flow:

`PortCallPlus` → `PortReporterMonitor` → `PortReporter`

# PortCallPlus

Due to VesselVoyage needs to include pilot events in their ESOF, the Portcall and PortcallVisit models should contain the pilot information.

|  |
| --- |
|  |
| Visual representation of the pilot information in PortCall+ models |

Thus, the class PilotBoard should be defined as:

wide760data class PilotBoard(
val estimatedTime: Instant?
val actualTime: Instant?
val ship: PilotShipInfo?
)wide760data class PilotShipInfo(
val mmsi: String?,
val imo: String?,
val name: String?
)

So, the `Portcall` model should include the fields:

* `inboundOnboard: PilotBoard`
* `outboundOffboard: PilotBoard`

And the `PortcallVisit` model should:

* include the fields:

  + `outboundOffboard: PilotBoard`

    - related to the visit arriving event
  + `inboundOnboard: PilotBoard`

    - related to the visit departure event
* convert its berth-dedicated fields into a visitFields by

  + marking the original berth field as deprecated
  + creating a visit-dedicated field, which value shall be adapted for regressive values.

Once the portcall is updated accordingly (in each `TaskService.updatePortcall(...)`, the new pilot events should be identified and published together and after the existing ones.

Note that deciding whether they have relevant changes between similar ones (same portcall-locations) should be decided in the eventual consumer (PortReporter).

# PortReporter Monitor (within AisEngine project).

* To define PortCallPlus events (initial proposed kotlin models are in this [PROJ-824’s comment](https://teqplaybv.atlassian.net/browse/PROJ-824?focusedCommentId=56626)) and json examples in this [PROJ-825’s comment](https://teqplaybv.atlassian.net/browse/PROJ-825?focusedCommentId=56625):

  + `PortcallPlusEstimatedTimePilotOnBoardEvent`
  + `PortcallPlusActualTimePilotOnBoardEvent`
  + `PortcallPlusEstimatedTimePilotOffBoardEvent`
  + `PortcallPlusActualTimePilotOffBoardEvent`
* To enrich events published by PortCallPlus and publish them to PortReporter’s AIS queue (already done, just mentioning in case of need of adding an unforeseen use-case.

# PortReporter

* To receive *Pilot* and *PortcallVisitsUpdate* events
* To keep berth visit coherence

  + With the PortcallVisitsUpdate (currently done, but check if it needs a review).
* To extend `PortCallEventType` enum with new event types corresponding to the new PilotEvents.
* To implement the subscription-based notification for new events:

  + To implement pilot event subscriptions based on location (from/to depending on type of event). This means that the pilot subscriptions should include a location field.
  + To decide when a pilot event processing should send a notification based on portcallVisits and event details (event time & visit coherence)  
    Initially keep a simple logic. Then, extend it with event time and visit coherence.
* To modify if needed the existing logic in case it’s needed ([listed in this PROJ-826’s comment](https://teqplaybv.atlassian.net/browse/PROJ-826?focusedCommentId=56726))

---

# Useful scenarios

## **Scenario 1:**

### **Description:**

* Progressive building of Portcall information (visits and portcalls) with no visit reordering.
* Estimated visits detected before-hand.

### **Time events:**

1. 1st time PC+ receives Sea to BerthA information (without pilot info).

   1. Visits start to build up (not entirely) (Sea to BerthA) → publish `PortcallPlusVisitsUpdateEvent`
   2. No Pilot event identified!
2. Information about movement BerthA to BerthB (without pilot info).

   1. Visits start to build up (not entirely) (BerthA to BerthB) → publish `PortcallPlusVisitsUpdateEvent`
3. Information about movement BerthB to Sea (without pilot info)

   1. Visits start to build up (not entirely) (BerthB to Sea) → publish `PortcallPlusVisitsUpdateEvent`

---

4. Information **about pilot onboard estimated time** from Sea.

   1. Publish `PortcallPlusEstimatedTimePilotOnBoardEvent` (location **Sea**).
5. Information about pilot onboard actual time from Sea.

   1. Publish `PortcallPlusActualTimePilotOnBoardEvent` (location **Sea**).
6. Information **about pilot offboard actual time** In BerthA.

   1. Publish `PortcallPlusActualTimePilotOffBoardEvent` (location **BerthA**).

---

7. Information **about pilot onboard estimated time** from BerthA.

   1. Publish `PortcallPlusEstimatedTimePilotOnBoardEvent` (location **BerthA**).
8. Information about pilot offboard estimated time from BerthB.

   1. Publish `PortcallPlusEstimatedTimePilotOffBoardEvent` (location **BerthB**).
9. Information about pilot onboard actual time from BerthA

   1. Publish `PortcallPlusActualTimePilotOnBoardEvent` (location **BerthA**).
10. Information about pilot offboard actual time from BerthB.

    1. Publish `PortcallPlusActualTimePilotOffBoardEvent` (location **BerthB**).

---

11. Information **about pilot onboard estimated time** from BerthB.

    1. Publish `PortcallPlusEstimatedTimePilotOnBoardEvent` (location **BerthB**).
12. Information about pilot offboard estimated time from Sea.

    1. Publish `PortcallPlusEstimatedTimePilotOffBoardEvent` (location **Sea**).
13. Information about pilot onboard actual time from BerthB

    1. Publish `PortcallPlusActualTimePilotOnBoardEvent` (location **BerthB**).
14. Information about pilot offboard actual time from BerthB.

    1. Publish `PortcallPlusActualTimePilotOffBoardEvent` (location **Sea**).

## **Scenario 2:**

### **Description:**

* Progressive building of Portcall information (visits and portcalls) **with visit reordering** (estimation information differs from actual visit order).
* Estimated visits detected before-hand, but they will change throughout the time.

### **Time events:**

1. 1st time PC+ receives Sea to BerthA information (without pilot info).

   1. Visits start to build up (not entirely) (Sea to BerthA) → publish `PortcallPlusVisitsUpdateEvent` `(BerthA)`
   2. No Pilot event identified!
2. Information about movement BerthA to BerthB (without pilot info).

   1. Visits start to build up (not entirely) (BerthA to BerthB) → publish `PortcallPlusVisitsUpdateEvent` `(BerthA, BerthB)`
3. Information about movement BerthB to BerthC (without pilot info)

   1. Visits start to build up (not entirely) (BerthB to BerthC) → publish `PortcallPlusVisitsUpdateEvent` `(BerthA, BerthB, BerthC)`

---

4. Information **about pilot onboard estimated time** from Sea.

   1. Publish `PortcallPlusEstimatedTimePilotOnBoardEvent` (location **Sea**).
5. Information about pilot onboard actual time from Sea.

   1. Publish `PortcallPlusActualTimePilotOnBoardEvent` (location **Sea**).
6. Information **about pilot offboard estimated time** to BerthA.

   1. Publish `PortcallPlusEstimatedTimePilotOffBoardEvent` (location **BerthA**).
7. Information **about pilot offboard actual time** to BerthA.

   1. Publish `PortcallPlusActualTimePilotOffBoardEvent` (location **BerthA**).

---

8. Information **about pilot onboard estimated time** from BerthA.

   1. Publish `PortcallPlusEstimatedTimePilotOnBoardEvent` (location **BerthA**).
9. Information about pilot offboard estimated time from **BerthC**

   1. Publish `PortcallPlusVisitsUpdateEvent (BerthA, BerthC)`
   2. Publish `PortcallPlusEstimatedTimePilotOffBoardEvent` (location **BerthC**).
10. Information about pilot onboard actual time from BerthA

    1. Publish `PortcallPlusActualTimePilotOnBoardEvent` (location **BerthA**).
11. Information about pilot offboard actual time from BerthC.

    1. Publish `PortcallPlusActualTimePilotOffBoardEvent` (location **BerthC**).

---

12. Information **about pilot onboard estimated time** from BerthC.

    1. Publish `PortcallPlusEstimatedTimePilotOnBoardEvent` (location **BerthC**).
13. Information about pilot offboard estimated time from BerthB.

    1. Publish `PortcallPlusVisitsUpdateEvent (BerthA, BerthC, BerthB)`
    2. Publish `PortcallPlusEstimatedTimePilotOffBoardEvent` (location **BerthB**).
14. Information about pilot onboard actual time from BerthC

    1. Publish `PortcallPlusActualTimePilotOnBoardEvent` (location **BerthC**).
15. Information about pilot offboard actual time from BerthB.

    1. Publish `PortcallPlusActualTimePilotOffBoardEvent` (location **BerthB**).

---

16. Information **about pilot onboard estimated time** from BerthB.

    1. Publish `PortcallPlusEstimatedTimePilotOnBoardEvent` (location **BerthB**).
17. Information about pilot offboard estimated time from Sea.

    1. Publish `PortcallPlusEstimatedTimePilotOffBoardEvent` (location **Sea**).
18. Information about pilot onboard actual time from BerthC

    1. Publish `PortcallPlusActualTimePilotOnBoardEvent` (location **BerthB**).
19. Information about pilot offboard actual time from Sea.

    1. Publish `PortcallPlusActualTimePilotOffnBoardEvent` (location Sea).

## Scenarios notes:

PortReporter Monitor will receive and enrich the events in a timely order.  
Same wise, PortReporter will receive them triggering any notification for any subscription and keeping the visits information up to date.

Worth noticing that, in between point 3 and 4, if a PortReporter user subscribes to, i.e. BerthB estimated and actual pilot offboard, they will get notified by points 13.a or 15.a, respectively. Which is expected, unless the subscription intention is not about BerthB, but the second berth visit. Then, this case isn’t covered, but I undertand it’s not the feature intention.