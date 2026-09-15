---
id: confluence:147357697
source: confluence
type: page
space: TC
title: Portcall Structure Refactor
author: Richard van Klaveren
date: '2022-10-23'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/147357697
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/147357697
---
# Portcall Structure Refactor

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/147357697  

## Content

With the restructure of the platform, also the system of maintaining the portcalls up-to-date and detecting all portcall events will need to change. Below diagram highlights those elements responsible for the current situation, keeping the portcalls up-to-date:

11473904681Portcall creation.drawio11z6DqJ0ff0gZnOFyywDlNvLKXnH73DLF9https://teqplaybv.atlassian.net/wikiPortcall creation.drawio1GDrive6F58XeLFBTWS3TrmdDKf 17631autotop371

System responsibilities in this diagram (related to portcalls)

* **Portcall+**: Keeping an up-to-date representation of all portcall information retrieved from outside authoritative sources like Terminal Operating systems, Agency Systems, Port Community Systems and Port Authority systems. Portcalls are always receiving a unique portcallId in Portcall+. When portcalls are being reported by multiple sources, we keep a portcall alias per source, so that we can always find back the information related to the source. Portcall data itself is merged.
* **Platform**: Match detected events against the relevant portcall, put those event in the right context (pilot-on-board / pilot-off-board) and send out portcall events based on that assessment. For this purpose it tries to keep a local (persistent) ‘cache’ of these portcalls and their state, mixing local detections with planned info received from portcall+. Also, it need to be noted that some legacy information (NLRTM, NLAMS Hamis / IRIS) still is retrieved via platform, rebuild of those adapters in portcall+ has not been done yet.
* **PortReporter**: Keeping an accurate and up-to-date picture of all portcalls, keeping a separate log of all planning events (as collected from external sources), estimated events (e.g. from predictors), and actual events (both external and internal detected) and merging them every time again to the most relevant representation of the reality.

In order to refactor the platform into separate components (scalable where needed), multiple situations will need to be addressed:

1. Currently portcall+ events are retrieved via a request-response mechanism, where the requested keeps a record of the last time data was retrieved. In this case platform retrieves the data, and converts it into events and dispatches them into an (internal and external) Teqplay events bus. Would be ideal if that part (detection of events and dissemination) would be moved to portcall+
2. Some interfaces (big ones, but also very important ones) to existing systems have never been migrated to portcall+, and are still located in platform. These will need to move out towards portcall+
3. The PortReporterMonitor currently runs as part of the platform. It will need to run as a standalone component, as part of the EKS cluster and infrastructure.
4. Portcalls are currently stored in 3 places, portcall+ for the total authoritative view, platform as a cache required for PortReporterMonitor and PortReporter as a Merged view for the rest of the applications, so to say the authoritative location for all portcall information. Would be great if we can reduce here the platform version.

Taking those thoughts as a starting point, the following architecture has been discussed as a proposal:

11473577171Portcall creation.drawio11z6DqJ0ff0gZnOFyywDlNvLKXnH73DLF9https://teqplaybv.atlassian.net/wikiPortcall creation.drawio0GDrive2\_2\_MO2IA5tMbiHW0MQu 17611autotop428

As can be seen, the portcall+ updates here are converted into events, being put on a bus (NATS / RabbitMQ) in order to be read by a portcalls. Hamis and IRIS connections are read by portcall+ and the PortReporterMonitor is still the central place to go when something needs to be known on portcalls. However, it exposes the portcalls in a central node (mostly a KeyValue store, maybe some minor API’s around) to make there portcalls available for reading by all other nodes.

Remaining challenges foreseen with this proposed architecture are:

1. PortReporterMonitor does the assignment of an event to a portcall. When updates come from portcall+, there might be a bunch of updates coming all at once. There is no guarantee they will be processed by the central Portcall KeyValue store before the knowledge is required by PortReporterMonitor. Originally there was only an update foreseen by PortReporter, but since PortReporter is always updated after PortReporterMonitor, this might not work in all situations. Therefore the portcall changes are also received by a central Portcalls Node (so this might mean the KeyValue store cannot be a stand-alone node).
2. Within the old architecture, there is a small monitor running in platform, closing portcalls X hours (configurable per port) after the vessel has sailed (port.atd), which makes these portcalls less eligible for matching events against. This monitor has to be rebuild somewhere, it looks like the PortReporter is the right place to do so as the main source for all merged portcall information.