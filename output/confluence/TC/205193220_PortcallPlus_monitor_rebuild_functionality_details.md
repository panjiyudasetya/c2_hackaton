---
id: confluence:205193220
source: confluence
type: page
space: TC
title: PortcallPlus monitor rebuild functionality details
author: Darius Wattimena
date: '2023-12-05'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/205193220
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/205193220
---
# PortcallPlus monitor rebuild functionality details

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/205193220  

## Content

This document contains details on how the PortcallPlus monitor in Platform will be rebuilt. This document is separated into three different sections.

1. Current situation
2. Expected functionality
3. Proposed rebuild

This document will not focus on changes that need to be done for HAMIS and IRIS to move to PortcallPlus, as this step will be taken at a later time.

# 1. Current situation

## 1.1 Current Platform Implementation

All text written in red shouldn’t be relevant for the rebuild. The green text contains all changes needed to be done in the Platform implementation.

### The `PortcallPlusMonitor`

* Get portcall updates using `PortcallPlusService` from `/v1/portcall/updates` endpoint.
* Ignore all NLRTM updates. This is handled by Platform itself using HAMIS & IRIS.  
   (Will be extended with excluding NLAMS in Platform in PRA-7905c406517-69e9-3c5d-b831-d2bed7d442a4System JIRA )
* Events are generated for the updated portcalls using the `PortcallPlusSubSystem`.
* Events are handled and dispatched when allowed to be published.

  + Handle portcall events.

    - Decide if we process structure events.
    - Return the event as is if it is an ETA for an outbound portcall.
    - If not, handle the portcall event using `PortcallSubSystem`.
  + Publish events using `HamisIrisMessageProcessorImpl`.

### The `PortcallPlusSubSystem`.

The following logic is executed when we want to generate events for a provided list of updated portcalls.

* When this is a new portcall.

  + Don’t do anything when portAtaTime is set, meaning portcall is already finished.
  + Create events for the new portcall.

    - Create an ETA event when visits are empty.
    - Otherwise, generate ETA/ETD/ATA/ATD events for every visit.
* When this is an existing portcall.

  + On IMO changes:

    - Determine `PortcallShipChangedEvent` with IMO changes.
    - Always update giving portcall with portcall plus IMO.
  + Generate events for all visits.

    - Map `PortcallPlusVisit` to platform `PortcallVisit` resolving with berth mapping in `getBerthMapping` so we can match the provided external identifiers to internal ones.

      * Adds `terminalName`, or from visit when not known.
      * Adds `berthName`, or from visit when not known.
      * Adds `berthOwnerId`, when Vopak berth using `teqplayBerthOwnerId` or otherwise using the `berthName` when Teqplay berth.
    - Get the first matching `PortcallVisit` (currently known in Platform) that matches our internal `berthName` or internal `berthOwnerId`.
    - When no matching `PortcallVisit` generates ETA/ETD/ATA/ATD events using the `PortcallPlusVisit` when we have a `berthName` in this visit.
    - When matching a `PortcallVisit`:

      * Generate `EtaEvent` when `berthEta` is filled, and `berthEta` / `berthAta` are not matching the visit `startTime`.
      * Generate `AtaEvent` when `berthAta` is not matching visit `startTime`.
      * Generate `EtdEvent` when `berthEtd` is filled, and `berthEtd` / `berthAtd` are not matching the visit `startTime`.
      * Generate `AtdEvent` when `berthAtd` is not matching visit `startTime`.
  + On agent changes:

    - Create `AgentChangedEvent` when you already have a `vesselAgent` on the Platform `Portcall`, and there is a new agent.
  + Create update portcall:

    - Set `originUnlocode` from `PortcallPlusPortcall`.
    - Set `destinationUnlocode` from `PortcallPlusPortcall`.
    - Set `status` from `PortcallPlusPortcall`.
    - Set `vesselAgent` from `PortcallPlusPortcall`.
    - Determine and set `pilotBoardingPlaceType` on every visit for SGSIN.
    - Determine and set `startTime` based on the smallest `startTime` of known Vopak or Teqplay berth.
* Save the created or updated portcall.
* Add the `AgentChangedEvent` to the result list of events if created.
* Create and add all `DraughtChangedEvent`.
* Create and add all `PilotEvent` for all visits. Not used anymore, should be remade into a different kind of pilot event instead of an encounter in the future. (Like is done in HAMIS/IRIS)

  + Get the `pilotTiming` from a visit. This is the `pilotOutgoing` or `pilotIncoming` if null.
  + Check if we have already generated a pilot event for this portcall.

    - Don’t add anything if we already have a `PilotEvent`.
    - Create a `PilotEvent` without:

      * Create the `lastPilotTime` variable from the visit `pilotTiming.pilotOffBoardTime` or `pilotTiming.pilotOnBoardTime`.
      * On a start event, set the event time to the `lastPilotTime`, while leaving `otherMmsi` empty.
      * On an end event, set the event time to the `lastPilotTime + 5 minutes`, while leaving `otherMmsi` empty.

### The `PortcallSubSystem`

When we process the provided events, the following logic is executed to mutate the related portcall for the events:

* `VisitDeclarationEvent` updates the original unlocode to the previous port when different from the currently known.
* `VisitCancellationEvent` set the cancel flag to true on the portcall.
* `EtaEvent`

  + Update Platform portcall based on event.
  + Create derived structure events Add/Update/Cancel PortcallVisit.
* `EtdEvent`

  + Update Platform portcall based on event.
  + Create derived structure events Add/Update/Cancel PortcallVisit.
* `AtaEvent`

  + Update Platform portcall based on event.
  + Create derived structure events Add/Update/Cancel PortcallVisit.
* `AtdEvent`

  + Update Platform portcall based on event.
  + Create derived structure events Add/Update/Cancel PortcallVisit.
* `NauticalOrderEvent` update Platform portcall based on event.
* `AgentReportsTugsEvent` update Platform towing company portcall based on event.

The following event types are not relevant for this PortcallPlus monitor rewrite, so they can be ignored:

* `EtaRequestEvent` HAMIS/IRIS only
* `EtdRequestEvent` HAMIS/IRIS only
* `HamisPilotBoardingEtaEvent` HAMIS only

## 1.2 Current PortcallPlus Implementation

The PortcallPlus portcall is created and updated in the application itself. Platform gets the update portcalls in the `PortcallController` executing the `getUpdatedPortcalls` function, which will:

* Use the provided `from` or `now - 30 days`

  + Platform only allows to provide the `from`
* Use the provided `to` or `now`
* Use the provided `port` or find portcalls for all ports when null
* Find the updated portcalls via `portcallDataSource.getByUpdateTimes`

  + Parse the `from` and `to`, maxing the number of portcalls we can ask for to a max of 30 days
  + Get all portcalls by update time between the parsed `from` until `now` and filter on port if provided

---

# 2. Intended Functionality

PortcallPlus should maintain the portcall and create events from changes made in this portcall. The events should then be parsed by the PortReporterMonitor and converted into the model that works for PortReporter.

## 2.1 Structure events

Instead of providing Create/Update/Cancel events for every visit change, we want to publish a `PortcallVisitsUpdateEvent`, which contains the full picture of the created, updated or cancelled visits. This means we will not publish any `AddPortcallVisitEvent`, `UpdatePortcallVisitEvent` or `CancelPortcallVisitEvent`.

### 2.1.1 Special case for Rotterdam & Amsterdam

We want to add a toggle to ensure we don’t publish PortcallPlus events for NLRTM & NLAMS. We want to keep the old behaviour of using IRIS & HAMIS for NLRTM & NLAMS. While still having the exception of using PortcallPlus to get the PortBase portcall alias for invoicing.

## 2.2 Agent changed events

When the agent changes on the portcall, an `AgentChangedEvent` should be generated. The generated event should eventually be put onto the events queue.

## 2.3 Portcall IMO changed event

When the IMO is changed on the portcall, a `PortcallShipChangedEvent` should be generated. The generated event should eventually be put onto the events queue.

## 2.4 Berth ETA, ETD, ATA and ATD events

For every visit that has been changed, an `EtaEvent`, `EtdEvent`, `AtaEvent` and `AtdEvent` can be generated. The result of this should eventually be put onto the events queue.

---

# 3. Proposal

On every portcall create/update:

* We save the updated portcall, which is the current behaviour.
* Events are generated based on the previous version of the portcall and the current version of the portcall.
* Generated events are published to the NATS event stream. Which will result in the following extra functionality:

  + Events are consumed by the new PortReporterMonitor and converted into required PortReporter events.
  + Events are saved in the new EventHistory.

## 3.1 Proposed code changes

Currently, the `createOrUpdate` method on the `PortcallDataSource` is used by the `SourceService` to update the portcall. Here the `updatePortcall` should be extended with the new functionality.

Once this portcall is saved, we compare the old portcall with the updated portcall if any events should be generated. If this is the case, we generate the events in their AisEngine model and publish them to the events NATS stream.

## 3.2 Transition to the new events

The generated events should not be exposed to Platform. The new events should only be used in the new PortReporterMonitor as the `PortcallVisitsUpdateEvent` is only generated in the Platform PortReporterMonitor and is currently not saved in the EventHistory. By doing so, we keep the new behaviour exclusively to AisEngine.

We could alternatively add support for this event in the existing PortReporterMonitor. However, I would rather avoid having to make any changes to the existing codebase of Platform if possible.