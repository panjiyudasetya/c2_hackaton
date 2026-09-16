---
id: confluence:279805979
source: confluence
type: page
space: TC
title: Manual Changes
author: Joost Dambrink (Unlicensed)
date: '2024-02-27'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/279805979
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/279805979
---
# Manual Changes

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/279805979  

## Content

In RouteScout manual changes have to be made to correct errors in imported data and merge imported data together into one graph. These changes should work even when data from imported sources has changed. To achieve this Bounding Boxes are used which can be created by the user. They will fix new points and existing lines from imported sources together.

In this page the followings items will be discussed:

16falsedisclistfalsebrackets

## Bounding Boxes

Data from imported sources can change. e.g. Lines can shift, node locations can change and things can get removed. To make sure that manual changes still work bounding boxes can be used.

Bounding Boxes are polygons with a **bounding point** in the middle. Any lines (edges + nodes) coming into these boxes will be deleted. The cut off line(s) will then be connected to the bounding point in the middle. Connecting all of the lines that intersect the bounding box with the **bounding point**.

This connecting is done by deleting the nodes & edges from the bounding box for all the line(s). After this we take a look at the point where the line is **cutoff**. The last point on the loose end is taken and **connected** to the **bounding point**.

In the example above a new point is placed on the line (edge). This can be done when we want to for example add a bridge to an existing route. Another use case is when we need to connect 2 routes together.

## How to make manual changes

### Adding new routes

* Manual changes in terms of routes are reflected in (manual) graphs, which are also attached using the above bounding boxes method.
* Can be combined with a graph area filter to quickly remove any underlying other (non-manual) graphs.
* Recommended way of adding new routes:

  + All manual changes could (technically) be stored in the same manual graph, only keeping one version.
  + However, there also is a benefit in having manual graphs per area (one for some routes in Rotterdam versus Friesland for example). That way you can easily turn on/off different manual graphs independently.

### Updating routes from graph sources

* Edges can be updated based on their `routeId`. (Assuming that they are consistent)
* Any set properties will overwrite the properties on the edge. Only updating Cemt Class for example.

## Miscellaneous

* What should the use be for a `source=MANUAL` graph’s `version`? Should we keep multiple versions to be able to differentiate between them in the front-end? Should they be allowed to be mutable or not?
* A `GraphAreaFilter` should have an `active` flag, to allow turning on/off.

## How changes are stored

* Manual changes are stored as graphs with `source=MANUAL`.
* The `version` property on the graph *could* be used, but awaiting a requirement like having multiple versions of manual graphs. For now we allow manual graphs to be mutable. (Whereas non-manual graphs, like FIS, are immutable and rely on the `version` property.)
* The `infrastructure.bridges` and `infrastructure.locks` should always contain ALL bridges and locks, even if they are not used on a route. This allows you to add these bridges onto a manual graph, by referencing it using the `InfrastructureIdentifier`. (If after updating the bridge/lock can’t be found, that should result in a conflict.)
* A `description` field is present in the `PersistedGraph` object that can be used to describe the manual change.

## Conflicts

* `GraphAreaFilter`

  + `sources=[FIS] && mode=INCLUDE`, e.g. FIS should exist & active & only 1 version active

    - FIS doesn’t exist => make inactive
    - FIS not active => make graph active
    - FIS multiple versions active => make only one graph active
  + `sources=[FIS] && mode=EXCLUDE`, can be ignored, maybe a notification?

    - above fixes, or make inactive
  + no points are detected inside the polygon (maybe per source?)

    - move the polygon
    - or, make inactive
  + `sources=[]` (empty list)

    - should turn inactive to disable warning
    - move polygon/add sources/etc. (make it useful please)
  + if one `polygon` is The Netherlands and another filter has a `polygon` that’s inside another one, like Friesland (two `polygon` that overlap)

    - should that be solved by adding the inner `polygon`’s `sources` into the parent
    - or, use recursive/inner structure to model this in `GraphAreaFilter` itself
* `BoundingBox` / manual changes

  + no points/edges detected inside the polygon

    - move polygon
  + `expectedSources`, which graphs should be found inside the polygon, if not found throw error

    - move polygon
    - or, change `expectedSources`
  + if within the `polygon` (new) points/edges are changed, case=only distance markers/no junctions: always `node=DistanceMarker`

    - if no bridges/locks/infrastructure is attached, can simply change to `Junction`, or move polygon, or make inactive
    - if bridges/locks/infrastructure, can’t turn it into a `Junction`, either move polygon or make inactive
  + if within the `polygon` (new) points/edges are changed, case=any junctions: always `node=Junction`

    - can still stay as a `Junction`, but warn about it needing to be changed to a `DistanceMarker`
    - optionally also just remove the change or make inactive