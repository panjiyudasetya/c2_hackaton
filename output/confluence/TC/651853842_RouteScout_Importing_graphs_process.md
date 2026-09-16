---
id: confluence:651853842
source: confluence
type: page
space: TC
title: RouteScout Importing graphs process
author: Richard van Klaveren
date: '2025-03-04'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/651853842
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/651853842
---
# RouteScout Importing graphs process

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/651853842  

## Content

## Introduction

Contained on this page are the manual instructions for the importing graphs process. This process has been made easier by the facility call. Instead of doing these steps manually you can just run the facility call. [See here](https://bitbucket.org/teqplay/teqplay-wiki/wiki/RouteScout%20Facility%20call)

The following steps include everything needed to fully update routes in the route planner.

Summary of the steps:

* Import graphs
* Add custom graphs
* Combine imported (prepared) and custom graphs (to saved)
* Combine saved graph with manual graphs
* Fixing graph error/warning notifications
* Opening/updating a sandbox
* Switching sandbox to live
* Closing old sandbox

# Steps

## 1 Define scope

Check if you need new versions of the base sources:

* RWS FIS
* Fryslan
* Cofano

Or you need to make changes to custom graphs.

If not, you probably only want to update manual graphs. If so, you can skip the following steps and start at step 8. Note that before doing this, you should have set the manual graphs to their correct active/inactive states.

If you want to add/update custom graphs you can start at step 4.

Else you can just continue with the following step.

## 2 Import base sources

Import new versions of graphs with the following endpoint:

`/trigger/graph/prepare`

This will fetch new versions of the base sources.

**NOTE**: if you already have the newest version of a graph but want to fetch it again, you have to first delete this graph and then run the trigger endpoint. Delete a graph with the following endpoint: `/graph/manage/{table}/delete`

## 3 Activate prepared graphs

You now have to set the correct `prepared` graphs to active. List all prepared graphs with this endpoint:

`/graph/manage/prepared`

You will then get a list of all available prepared graphs, both active and inactive.

You need to set the graphs either active or inactive according to your liking, with the following endpoint:

`/graph/manage/prepared/{ownerId}/{generationId}/{speciesId}/update?active={active}`

You will have to include the `ownerId`, `generationId` and `speciesId` of the graph you want to update. Also supply the active setting with either `true` or `false` to determine if it's active or inactive.

## 4 Add/update custom graphs

**README**: If you want to import custom graphs continue with this step, if you just want to change if a custom graph is active go to step 5, else go to step 6.

List all custom graphs with this endpoint:

`/graph/manage/custom`

If your desired custom graph is not available you have to add it with the following endpoint and schema:

*Endpoint*

`/graph/manage/custom/add`

*Schema*

{
"graphInfo": {
"ownerId": "string", // which owner, like 'RWS'
"generationId": "string", // which generation, like 'FIS'
"speciesId": "string", // which species, like '1182'
"area": "string" | null, // optional note regarding which area this graph is from
"description": "string" | null, // optional description
"createdTime": 0, // time in millis, optional: if not supplied it will default to current time
"lastUpdatedTime": 0 // time in millis, optional: if not supplied will equal `createdTime`
},
"graphSettings": { // optional: if not supplied it will be defaulted to the following
"active": false,
"routeIdMerge": false,
"cannotMergeNodes": false,
"managePolygon": null
},
"nodes": [
{
"id": "string", // id of the node
"location": {
"type": "Point",
"coordinates": [
4.0, 52.0 // coordinates of the node in `lon`, `lat` form
]
}
}
],
"edges": [
{
"id": "string", // id of the edge
"from": "string", // id of the node from
"to": "string", // id of the node to
"between": {
"type": "LineString",
"coordinates": [
[
4.0, 52.0 // coordinates in `lon`, `lat` form
],
[
4.0, 52.0
],
...
]
},
"routeId": -1, // optional: if not supplied defaults, `routeId` is only used for a routeIdMerge
"info": { // optional: if not supplied defaults to `null`. details/information of an edge, indicating `cemtClass`, `width`, ...
"cemtClass": "5.2",
"width": "50.0",
...
}
}
]
}

**IMPORTANT**: once you have created this graph, you still have to connect this graph with another one by supplying a manually made route. If you don't do this you won't be able to route between these two graphs, so no routes can be returned.

## 5 Activate custom graphs

You now have to set the correct `custom` graphs to active. List all custom graphs with this endpoint:

`/graph/manage/custom`

You will then get a list of all available custom graphs, both active and inactive.

You need to set the graphs either active or inactive according to your liking, with the following endpoint:

`/graph/manage/custom/{ownerId}/{generationId}/{speciesId}/update?active={active}`

You will have to include the `ownerId`, `generationId` and `speciesId` of the graph you want to update. Also supply the active setting with either `true` or `false` to determine if it's active or inactive.

## 6 Write saved graph

Import new versions of graphs with the following endpoint:

`/trigger/graph/save`

This will combine all active `prepared` and `custom` graphs to one `saved` graph. A unique ID will be generated for these graphs combined.

**NOTE**: if you want to combine the graphs again, but haven't changed active states on underlying graphs, you have to first delete this graph and then run the trigger endpoint. Delete a graph with the following endpoint: `/graph/manage/{table}/delete`

## 7 Activate saved graph

You now have to set the correct `saved` graphs to active. List all saved graphs with this endpoint:

`/graph/manage/saved`

You will then get a list of all available saved graphs, both active and inactive.

You need to set the graphs either active or inactive according to your liking, with the following endpoint:

`/graph/manage/saved/{ownerId}/{generationId}/{speciesId}/update?active={active}`

You will have to include the `ownerId`, `generationId` and `speciesId` of the graph you want to update. Also supply the active setting with either `true` or `false` to determine if it's active or inactive.

**IMPORTANT**: there can only be 1 active saved graph, so make sure this is the case before continuing with the next steps.

## 8 Write final graph

Finally run the building of the graph with the following endpoint:

`/trigger/graph/write`

This will combine 1 saved graph and all manual graphs into one graph suited for route planning.

**IMPORTANT**: this will always **overwrite** a graph which has the same `ownerId`, `generationId` and `speciesId`.

## 9 Define final graph status

If everything went correctly while merging the saved and manual graphs you will get a result which contains the `ownerId`, `generationId` and `speciesId` needed to open a sandbox.

If instead you got errors, you have to fix these. These notifications come in three types: INFO, WARNING and ERROR. If any notification has a priority of ERROR, then the graph isn't written because it would be 'corrupt' if it did. If you only have notifications with type WARNING, then you can use this graph for testing, but before switching it to live you should have fixed all notifications (both warnings and errors).

## 10 Open/update a sandbox

Now you can open the sandbox! Open a sandbox with the following endpoint:

`/sandbox/list/open?generationId={generationId}&ownerId={ownerId}&speciesId={speciesId}`

You will have to include the `ownerId`, `generationId` and `speciesId` from the details of the `write` trigger.

**NOTE**: if a sandbox with the same details already exist, you have to update the sandbox with: `/sandbox/available/update?sandboxKey={sandboxKey}` Where `sandboxKey` is the key of the sandbox.

## 11 Test the sandbox

You can now test if the graph works for routing in the frontend.

To ensure the good functioning of a graph, try to at least plan one route.

**IMPORTANT**: if you added either a new custom graph or added/updated manual graphs, you must test the well functioning of these routes before continuing.

## 12 Switch the sandbox to live

You are now almost done! You imported all the needed graphs, set the correct ones to active, supplied manual graphs to correctly connect graphs, fixed potential errors while merging and opened/updated a sandbox for routing.

You can now switch this sandbox to live! When doing this the route planner will instantly switch from the old live sandbox to your selected new live sandbox. Users will not notice you changing the sandbox, only the routes that will be generated will change as you've changed the underlying graphs.

Switch your sandbox to live:

`/sandbox/live/switchTo?sandboxKey={sandboxKey}`

Supply your `sandboxKey` of your opened/updated sandbox.

**NOTE**: you should now ensure that the new live sandbox still works and produces correct routes. (just for your own confidence for the next steps)

You can now close the old sandbox by running:

`/sandbox/available/close?sandboxKey={sandboxKey}`

Supply the `sandboxKey` of the old/to-be-closed sandbox.

Please note that you can't close a live sandbox, so don't worry about messing up something. As long as the underlying graph works correctly, the live sandbox can never fail or be closed without switching first.

---

**You are now done updating the route planner!**