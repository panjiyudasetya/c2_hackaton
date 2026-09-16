---
id: confluence:586743809
source: confluence
type: page
space: TC
title: Extend Vesselvoyage to support Vessels without an IMO
author: Richard van Klaveren
date: '2025-01-07'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/586743809
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/586743809
---
# Extend Vesselvoyage to support Vessels without an IMO

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/586743809  

## Content

Originally when VesselVoyage was designed and developed, we limited the scope of Vesselvoyage to ‘Sea-going vessels only’. Decision was mostly driven by the focus of Teqplay, where we decided that the barges market is not scalable.

Now using VesselVoyage more and more as the corner stone in the Teqplay architecture, the question rises more and more often if VesselVoyage could also support ships that are not sea-going. Therefore this article will explore what is needed in order to extend the scope of VesselVoyage to also support non-sea-going ships.

VesselVoyage is fed by events coming from AIS Engine, and is a relevant source for PTO, Smartfleet and PortReporter. All of those components depend in CSI for ship information. CSI does support both Sea-Going ships and non-sea-going ships.

[VesselVoyage Dependencies overview](https://app.diagrams.net/#G1oVjtP4rWkhgA7IpYzFq73FdN08EqwGi8#%7B%22pageId%22%3A%22PIMOj2zxPlNbgqEUQZ_z%22%7D)

## VesselVoyage input

AIS Engine has as the main focus AIS data, and thus does use the MMSI as the main identifier for identifying ships. Therefore AIS Engine is producing similarly results for sea-going and non-sea-going vessels. The only area where a clear distinction is made is in the encounter monitor. Encounter monitor uses the ‘isSeaVessel’ flag set on each sea-going vessel to distinguish between sea-going and non-sea-going vessels.

So, on the input side of VesselVoyage nothing is expected to need any change, in order to support sea-going and non-sea-going vessels simultaneously.

## VesselVoyage data model

The current Vesselvoyage data-model focuses on sea-going vessels that sail from port to port. Therefore the model is per ship a sequence of `port-visit` - `voyage` - `port-visit` - `voyage`.

First question of course is if this model would fit equally for non-sea-going ships. The answer here is undecided, as in, for some (barges transporting goods) it typically does, for others (like service providers, tugs, etc) it typically does not. However, there is also not a typical model that fits all vessels properly. So, the proposal would be to maintain the same (current) model for all ships. Consequence will be though that the `port-visit` section of non-sea-going vessels might grow very large (as in the ship might stay in port for years and do all kind of activities). For this a clear action needs to be done, since current visit is stored in a mongo document, and thus limited to the maximum size a mongo document can hold. Therefore, currently we limit (for now) each `port-visit` entry to maximum 100 events. Therefore the storage of the `port-visit` will need to be setup more scalable for future anyhow, but definitely is needed for extension to non-sea-going vessels.

Additionally the main identifier for identifying a ship in VesselVoyage is the IMO. This will not fly to support also non-sea-going vessels, since those do not have an IMO. There are 2 options possible for this:

* Quick-and-Dirty: Reuse the IMO field to hold the unique identifier of the non-sea-going vessel, begin the MMSI in this case. Consequence is that this introduces technical debt, with a field called `imo` but holding sometimes and `imo` and sometimes a `mmsi`. Although, the 2 are quite distinguishable since the `mmsi` is composed of 9 digits and the `imo` always contains 7.
* Future oriented: Replace the `IMO` as main identifier with the `CSI identifier`. CSI has all information on identifiers (`imo`, `eni` and `mmsi`) listed underneath a CSI identifier.

When Executing this step as a future oriented step, we should also implement the future oriented approach and thus replace the `IMO` as main ship identifier in Vesselvoyage with the `CSI Identifier`.

## VesselVoyage output

The action to change the main ship identifier in VesselVoyage from an `IMO` to the `CSI idenitifier` will also need to be applied in other dependent applications in order to take advantage of it. This can be done and executed as a separate step as long as vesselvoyage keeps exposing a backward compatible format of the data, but sooner or later the following components need to be updated:

* Smartfleet: accepting and using itself the `CSI Identifier` instead of the `IMO` as the main identifier for each ship.
* PortReporter (Smartfleet part): Accepting and using itself the `CSI Identifier` instead of the `IMO` as the main identifier for each ship.
* PTO: internally already uses the CSI Ship identifier everywhere, only will need some minor modifications to call VesselVoyage using the `CSI identifier` instead of the `IMO`.

## Effort

A ROM estimate for the effort would be:

* Quick-and-dirty 10 man days

  + VesselVoyage (storage: 5d, accepting mmsi in imo: 2d ),
  + Smartfleet (1d), removing imo specific checks
  + portReporter (1d), removing imo specific checks
  + PTO (1d), updating all calls to Vesselvoyage to know `imo` field could also contain an `mmsi`
* Future oriented: 23 man days

  + VesselVoyage (storage: 5d, replacing main identifier: 7d)
  + Smartfleet (replacing main identifier: 5d)
  + PortReporter (replacing main identifier: (5d)
  + PTO (1d), updating all calls to Vesselvoyage to use the `CSI Identifier`.

Please note that no specific barge functionality has been planned in these ROM effort estimates, so it just allows to have the non-sea-going vessel data in vesselvoyage and expose it in the same way as sea-going vessel data in the tools.