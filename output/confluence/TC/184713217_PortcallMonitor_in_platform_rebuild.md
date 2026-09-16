---
id: confluence:184713217
source: confluence
type: page
space: TC
title: PortcallMonitor in platform rebuild
author: Richard van Klaveren
date: '2023-05-22'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/184713217
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/184713217
---
# PortcallMonitor in platform rebuild

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/184713217  

## Content

During the platform rebuild, one of the subjects to be rebuild is the way platform handles portcalls. In this section we will discuss:

1. Original platform architecture
2. Intended Platform rebuild architecture
3. Intermediate step in between original and intended architecture

## 1. Original platform architecture

Traditionally all external Port Community System (PCS) connections were monitored directly from platform. It was realized at connection number, this was not a sustainable approach. It was expected to make many external connection, and also the mix internal in platform between PCS knowledge and derived knowledge was not ideal. Therefore a new component ‘portcall+’ was started, with the mere purpose to interface to all different external portcall information providers. Platform interfaced to portcall+, requesting it once per minute if new updates are available. It would get the portcalls that were updated, detect the changes and send the relevant update events internally on the bus. Such changes were applied in the portcallsubsystem to the portcall database, available for all other monitors.

PortReporterMonitor would listen to the internal bus, convert all internal events (both the ones detected itself via AIS (blue) and the external PCS events (green) and convert them into the portcallEvent format to bring them to PortReporter. Additionally, a portcall End monitor was running in the platform, checking all open portcalls if the vessel already left the port, if so it would close the portcall after x hours (to allow pilot / anchor events outbound to be attributed to the portcall), firing also an event about that to notify PortReporter.

PortReporter in itself keeps a store on all planned visits (visits and their order, all based on external PCS events), Estimated visits (for which an ETA was received) and actual visits (as detected by platform or PCS).

## 2. Intended Platform Rebuild Architecture

In order to rebuild the platform, the intention is to reduce the dependencies on the platform, and limit the amount of places where portcall information is stored. Also, applying more strictness on having all PCS systems monitored by the same component is the target. This leads to the following architecture:

In this architecture, all external PCS components are directly interfaced by Portcall+. Portcall+ itself does detect the changed immediately and converts them into Teqplay Events (or maybe this could be immediately portcall Events) being distributed over the NATS event stream as external events. The NATS event stream also holds the Teqplay events detected by the various monitors. Those 2 types of events are being received by the PortReporterMonitor, which executes 2 steps:

1. Conversion of the data into the portcall model, deriving for example out of a pilot vessel alongside or the departure from a pilot area the ‘pilotOnBoard’ event, or actually the ‘PilotDisembarked’ event.
2. Applying the relevant portcall identifier to the event to indicate to which portcall the event belongs. Even so, it adds the Smartfleet identifier to indicate to which smartfleets this portcall events belongs.

The resulting information is forwarded to PortReporter, which makes sure the relevant parties are being notified and relevant SOFs are being updated

EventHistory receives all three types of events, and stores all of them in the eventStore, for later retrieval.

## 3. Intermediate step in between original and intended architecture

To make sure the main platform dependency are being addressed as quickly as possible, a intermediate step is envisioned, preventing:

1. Rewriting of Hamis and IRIS interfacing from platform into portcall+. This would be a serious investment, whereas the future is unclear on both IRIS and Hamis, it might be that actually soon all information on NLRTM and NLAMS comes via PortBase, which is already integrated in Portcall+
2. Postponing the integration of PortReporter into NATS instead of RabbitMQ (more as a consequence than as a target).

Therefore the following architecture is envisioned as an intermediate step:

In this architecture, the interfacing of Hamis and IRIS is still being done via a platform instance, and the resulting events are put on the rabbitMQ. This does not block the decommissioning of backendPronto, since this connection to Hamis and IRIS is already running in the ‘backend’ platform instance as well, and could be easily switched there as well.