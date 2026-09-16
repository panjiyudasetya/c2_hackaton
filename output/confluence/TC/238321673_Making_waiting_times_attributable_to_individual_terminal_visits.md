---
id: confluence:238321673
source: confluence
type: page
space: TC
title: Making waiting times attributable to individual terminal visits
author: Richard van Klaveren
date: '2024-02-01'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/238321673
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/238321673
---
# Making waiting times attributable to individual terminal visits

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/238321673  

## Content

In the initial data model for PTO, waiting times are measured into different categories including:

* **Waiting at anchor:** When a vessel waits while at an anchorage before entering the port
* **Waiting at layby:** When a vessel waits at a berth, which is not a berth where it can do it’s cargo operations. This includes waiting e.g. at a dry-bulk berth for a container vessel.
* **Waiting other:** When a vessel is either slow steaming outside the port or laying still at any place not characterized as an anchorage or berth.

Please note that slow sailing in port will be included in sailing time, not in waiting time. Those waiting times currently are associated at port level only. The goal is to make any waiting time attributable to an individual terminal visit. A terminal visit in this case is characterized as all consecutive berth visit belonging to the same cargo-terminal without intermediate waiting or other stops.

The idea is to attribute all waiting periods before a terminal visit to that terminal visit, excluding the waiting during the voyage (for now) since it is less clear whether that is attributable to the specific terminal visit. In practice that would mean in the above scenario:

* The waiting time for `Terminal Visit A` at `Terminal 1` would be the summatory of time waiting at stop1, stop2, stop3 and stop4.
* The waiting time for `Terminal Visit B` at `Terminal 2` consists of the waiting time at stop 6
* The waiting time for `Terminal visit C` at `Terminal 1` consist of stop 8

In order to not loose the knowledge on what type of waiting, we will maintain the 3 waiting categories (anchor, layby and other).

### Data warehouse storage

Currently the Data Warehouse model consists of 2 layers:

1. **Port Visit level**, with one entry per port visit
2. **Berth visit level** with one entry per berth visit.

At the data warehouse at berth level, each Berth item will be extended with 4 items:

1. In port Waiting Duration Anchor
2. In port Waiting Duration Layby
3. In port Waiting Duration Other
4. In port Waiting Duration Total

When multiple consecutive berth visits exist for the same terminal without other terminal visits or waiting time in between (e.g. since the vessel had to shift during cargo ops), those waiting times are only populated for the first berth visit in that terminal visit. At berth level those times are only populated with the waiting times after entering the port, waiting times before entering the port are stored only for the first berth visit of the first terminal visit in the following fields:

1. Outside Waiting Duration Anchor
2. Outside Waiting Duration Layby
3. Outside Waiting Duration Other
4. Outside Waiting Duration Total

### Data Mart Storage

In the data mart currently there are 3 layers:

1. **Port Visit level**, with one entry per port visit (temporary reintroduced till all dashboards are updated to use the terminal grouping level instead)
2. **Terminal Grouping level\***, with one entry per terminal visited (one terminal visited multiple times is just one entry).
3. **Berth visit level** with one entry per berth visit.

At the Data Mart at berth level, each Berth item will be extended with 4 items:

1. In port Waiting Duration Anchor
2. In port Waiting Duration Layby
3. In port Waiting Duration Other
4. In port Waiting Duration Total

The population of these berth items will follow the same rules as for the data warehouse. Similarly to the data ware house level, also items will be added to populate the Outside waiting time:

1. Outside Waiting Duration Anchor
2. Outside Waiting Duration Layby
3. Outside Waiting Duration Other
4. Outside Waiting Duration Total

Same items will be available at Terminal Grouping level, providing the summatory of these items per terminal grouping and at port visit level summarizing these at port visit level.

\*In the future it was agreed that `terminal grouping level` will be replaced with a `terminal visit level`, representing all stops to the same terminal without other stops in the middle. In that case the example above would result in 3 terminal visits (whereas there are 2 terminal groupings).

# Travel times

In the same way as we are planning to attribute waiting times, we also will apply travel times. There are functionally 2 different travel time categories:

* Steaming in / out the port
* Sailing between terminals.

Also here applies that at the berth level of the data warehouse and data mart, all travel times will be attributed to the next terminal visit. That means in an example of 3 terminal visits like above:

* Visit 1: will have the Steaming in being set, and no sailing in between terminals
* Visit 2: will have NO steaming-in being set, but travel time (also including the travel to and from stop 6) will be in the ‘sailing between terminals’
* Visit 3: will have:

  + travel time between visit B and visit C (including traveling to and from stop 8 ) in ‘sailing between berths'
  + steaming-out being set to the travel from terminal visit C to pilot disembarked.

It has been agreed that travelling time between 2 stops at the same terminal can be neglected for now from a functional perspective. It is not expected to add relevant time to the functional picture. From a technical perspective, not registering this time would be removing the possibility to validate if the pilot-to-pilot time is the sum of all parts, therefore this value will be registered in a separate field (Wouter / Yaren to propose a name).