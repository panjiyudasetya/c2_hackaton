---
id: confluence:361005059
source: confluence
type: page
space: TC
title: World-wide (r)events generation
author: Former user (Deleted)
date: '2024-07-24'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/361005059
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/361005059
---
# World-wide (r)events generation

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/361005059  

## Content

**Goal of running (r)events world-wide:**

* not all context data for service vessels is correct / high-enough quality
* we want to have VesselVoyage V2 data available quickly, with at least 'current' quality of encounters
* data available for 2022 and onwards as a staring point; we only have world-wide + satellite data starting from ~aug 2021

**Tasks:**

* add area index for fast vessel lookups

  + backfill data into ship-history S3, containing data starting from 2022
  + adjust ship-history-processor to write area index files, along with history by mmsi/area
* run (r)events without encounters starting from 2022 and merge into VesselVoyage V2
* add current encounters from event-history into VesselVoyage V2 ESoF

  + creation of new ESoFs based on given encounters  
    <https://bitbucket.org/teqplay/vesselvoyage-backend/pull-requests/271>
  + request encounters from event-history & add API endpoint to trigger + store results  
    <https://bitbucket.org/teqplay/vesselvoyage-backend/pull-requests/272>
* do selective encounter regeneration

  + first regenerate all pilot events and add to ESoF
  + after updating service vessel roles, also regenerate those and add to ESoF
  + regenerating by PTO report remains available as well