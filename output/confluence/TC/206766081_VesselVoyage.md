---
id: confluence:206766081
source: confluence
type: page
space: TC
title: VesselVoyage
author: Richard van Klaveren
date: '2024-10-25'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/206766081
explicit_links: []
---
# VesselVoyage

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/206766081  

## Content

This paragraph defines the considerations to move VesselVoyage from a successful experiment towards a productized core component

**Subpages**

true

---

The [main scope of VesselVoyage v2](https://docs.google.com/presentation/d/1gUaAwm1AQdbDIi-n-z7NRBZbw3-tDaN4d51icbV5g4Y) is to be the single source of truth on worked-up information for all port visits and voyages for cargo transporting sea-vessels.

VesselVoyage is required to have stability and quality information, the afterwards quality information should be great, the real-time quality information should be acceptable. In addition VesselVoyage will include a predictive part (ETA + destination).

The data within VesselVoyage should stay unclassified, which means that no customer specific data is stored inside vessel voyage. With new contextual information (updated berths, new pilot vessels recognized), we want to be able to re-evaluate / recalculate the VesselVoyage voyages (incl. port visits)

Port Visits staying only at anchorage should be included. All SOF calculations (unclassified) should be done in VesselVoyage to Reduce the duplication of other components to nihil (ongoing traces). Vesselvoyage should be input for an ETL street calculating port statistics in DWH

**Summary of our meeting 23-08-2023**

VesselVoyage is built with a more experimental approach, not knowing how good the results would be. This approach resulted in the VesselVoyage as we know it right now, having visits/voyages extended with a bunch of extra functionality such as Traces, the eSOF and improvement of data afterwards.

As VesselVoyage is getting much more critical for Teqplay, taking the following steps to get VesselVoyage to the next level is essentially for making the component more reliable, robust, enhancable and correct.

## 1. Code Quality

The code quality in VesselVoyage is quite subpar, as it didn't have a clear focus and was initially set up as an experiment.

A plan will be made to get the code base up to the standard we expect it to have. Here, the following topics will be covered:

* Regrouping/cancelling of Visits and Voyages.
* Improving the overall structure by making more use of Spring.
* Documenting the functional choices being made. (Not per see related to the code base)

## 2. Splitting of the processing and API

VesselVoyage is quite entangled, having the processing and API together in 1 big application. This results in the downtime of the API for around 5 minutes when we do a deployment. As VesselVoyage will be used in the future by many more applications and is already one of the more used components, having this split is vital to improve reliability.

## 3. Real-time vs. post-fixing

Currently, VesselVoyage has two different aspects:

* Real-time, where we have the events and AIS data processing
* Post-fixing, where we try to improve the visit/voyage data once they have happened.

While VesselVoyage was initially envisioned as a component to not focus on real-time at all, it has been grown towards a component more focused on being real-time up-to-date then focused on being more accurate afterwards. It has been decided to keep focusing on this part as many projects rely on the real-time view provided by VesselVoyage.

However, the Post-fixing perspective needs proper attention as well. We decided that there will be certain trigger moments defined (like ending a visit, or ending a voyage) where data from the past will be reconsidered and enhanced to expose higher quality information for the users. For example, when real-time detections were done resulting into 3 anchor visits, it can be much easier afterwards to judge whether this really were 3 anchor visits or maybe only 1 with some jitter in the middle due to communication / sensor behaviour.

We also want to change how traces are saved once the visits or voyages are finished. We now keep the location + time for each data point and have a simplified view once the visit/voyage finishes or when the trace becomes too big. Currently the majority of the database consists of traces, whereas except for doing calculations on ending visits etc there is no need to store the timestamp on each and every location. Instead, saving the trace as a polyline would be much more performant and save a lot of storage space, as the added value of having the time isn't used at all.

## 4. Recalculation

When doing a recalculation, you currently get all or nothing. We want to improve this process so there will be the possibility to recalculate any timeframe of the ship's story. For example, we are only recalculating 2022 for all vessels. We also want to improve the performance of recalculating by applying parallelization. Right now, we are limited by the performance of BackendGlobal. This is not the case with the new ShipHistory.

We might want to reconsider the trigger for recalculating the Visits and Voyages. Will this be entangled with revents, or will the revented events be saved in the new EventHistory so we can later decide when we want to do our recalculation process on the side of VesselVoyage? When the processing part is separated from the API (see also point 2), this should be in the back of our minds.

## 5. Real-time stop events

VesselVoyage has a built-in implementation to determine stops. This mechanism is currently based on movement events. With an improvement in the data once a Visit or Voyage is finished. This requires getting the ship traces to calculate the most accurate stop location.

This mechanism should instead be replaced with a new event that is not dependent on the movement events. A quick win would be that we can quickly expand this by creating a new event, parsing it in VesselVoyage, putting it in the related ongoing Visit or Voyage and once finished, we can make any enhancements.