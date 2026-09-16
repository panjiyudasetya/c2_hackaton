---
id: confluence:435716097
source: confluence
type: page
space: TC
title: Context mapping
author: Richard van Klaveren
date: '2024-09-04'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/435716097
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/435716097
---
# Context mapping

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/435716097  

## Content

Context mapping is the process where relevant context is added to ports and vessels. For example, the adding / updating of terminals, berths, anchorages and pilot areas to a port.

Below a couple of sections on how to find certain context data.

## How to find where an anchorage is?

An anchorage is a place where vessels wait till they are allowed to get into the port and move to the terminal. Some sources are more relevant for finding anchorage information than others, so based on priority, the following steps can be followed:

1. Search if the port authority has a website or port handbook where they share where to anchor, multiple ports do have.
2. Validate if our 'IHS Ports and Terminals Guide' has for this port any relevant information on the anchorages
3. Use VesselVoyage and select the port you want to find the anchorage for. Select a couple of vessels that have just left the port and verify whether they have been waiting in the same area, if so, this most probably is an anchorage area
4. Use OnTheMap tool, and change the settings (settings → Map → OpenSeaMap overlay) to see the openseamap overlay. This might give some idea on where anchorages are. Also, when you have ‘automatic zoom filters’ in the filters section switched off, it is possible to detect anchorages based on vessels laying still (noted with a dot instead of a vessel line) → see picture below
5. Check if any unvalidated anchorages are detected by data science team (in pink on the map of POMA when you enable the anchorages overlay). This might give you some hinch where to look for anchorages.

In case of doubt, better to make an anchorage too big than too small.

## How to find where a pilot area is?

A pilot area is the place where a pilot goes on board a sea-vessel.

## How to find relevant information on a vessel to update CSI?

When validating or updating basic ship data into CSI, we always want to use an external validated source. In order of priority, that could be one of the following sources:

1. When the vessel is a tanker, use Q88 to resolve all values. Best way is to type into Google `Q88 [IMO Number]`
2. Harder to find, but quite often the owner of the vessel proudly presents its vessel on his/her website. So searching on `[vesselname] fleet` will probably bring you there
3. Lookup the vessel in a relevant environment like Marinetraffic (doing a validation of data instead of directly showing data based on AIS) or VesselFinder. Again googling on `IMO [IMO Number]` and selecting the marinetraffic or vesselfinder link, which do also expose GT and DWT mostly. Please note that in bitwarden there is a marinetraffic account that will expose you the dwt as part of the ‘vessel characteristics’ tab.
4. Get the data from any other data provider based on AIS, typically such data could be found in our onthemap or otherwise in Vesseltracker, myShipTracking, shipspotting etc. You will not likely be able to find any info on DWT or GT.

## How to find the role of a v essel ?