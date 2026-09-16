---
id: confluence:812417027
source: confluence
type: page
space: TC
title: Analysis performance VesselVoyage processing
author: Darius Wattimena
date: '2025-07-31'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/812417027
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/812417027
---
# Analysis performance VesselVoyage processing

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/812417027  

## Content

Date of analysis 2025-03-14.

Test done locally with 8 GB memory allocated

## Processing steps

The following section highlights what needs to be done when processing certain functionality of VesselVoyage.

| **Processing mode** | **Events** | **Stops** | **Traces** | **Post-processing** (Step after a visit/voyage is finished) |
| --- | --- | --- | --- | --- |
| V1 | NATS event stream | Calculated directly using real-time AIS | 1. In-memory map keeping all new AIS points 2. Background task writing all AIS points on an interval basis | 1. Clean-up trace with full AIS 2. Recalculate all stops with full AIS |
| V2 | NATS event stream | Events | Light-weight updating of polyline | Calculate drifting with real-time AIS trace |

## Observations

| **Observation time** | **V1 and V2 enabled** | **V2 enabled** |
| --- | --- | --- |
| After 5 mins | ~3 GB mem / 60% CPU | ~1.2 GB mem / 24% CPU |
| After 30 mins | ~3.8 GB mem / 74% CPU | ~1.8 GB mem / 26% CPU |
| After 4 hours | ~5.4 GB mem / 82% CPU | ~2.2 GB mem / 23% CPU |

While the memory goes up in a more linear way, CPU is very stable when only running V2, showing that the JVM is not spiking as aggressively to keep the Java heap cleaned.

Without V1 enabled you will have a lot less objects in the eden space given that those are all short term allocations. V1 does a lot of calls to retrieve AIS history for a short time on the following tasks:

* Real-time stop detection
* Clean-up trace
* After the fact stops recalculation

## Conclusion

When disabling V1, the CPU is a lot more stable. Because we need to do less steps when processing an event or an ais point the processing throughput will also increase and locking time on a ship will be reduced significantly.