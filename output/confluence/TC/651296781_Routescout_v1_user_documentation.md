---
id: confluence:651296781
source: confluence
type: page
space: TC
title: Routescout v1 user documentation
author: Richard van Klaveren
date: '2025-03-04'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/651296781
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/651296781
---
# Routescout v1 user documentation

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/651296781  

## Content

## Components

### Routes

Call: `/routes`  
Cofano call: `/getpolyline` (mimics the results of Cofano)

Returns the used `origin`, `via` and `destination` locations as well as the `routes` in a `List<List<Route>>`. When using via points (A,B,C) the first entry is the routes between A to B and the second entry is the routes between B to C.

### Trigger Events

Call: `/trigger/graph/{event}`

Types:

* `prepare` => tries to fetch new versions of graphs, for instance the FIS of RWS.
* `save` => combines `prepare` and `custom` graphs
* `write` => combines `save` and `manual` graphs, also generates a simplified graph with detailed information and routes

**Hint**: after the `write` step => when the graph is written you can already see the changes in the frontend before updating the sandbox. This way you can visually check the graph before updating the sandbox to enable routing.

### Notifications

`/notification/list` => Lists all notifications sorted from newest to oldest  
`/notification/find` => List all notifications by a `referenceId`  
`/notification/delete` => Deletes all notifications with a `referenceId`

Notifications are created when there are new versions of graphs available (`prepare` step) or if there are errors while generating a graph. These notifications have descriptions how to fix the errors in the graph.

There are multiple types of notifications:

* `GRAPH_FETCH`
* `GRAPH_BUILD`

There are multiple specifications for notifications:

* `NEW_GRAPH_VERSION_AVAILABLE`
* `MODIFY_CONNECTIONS__<specification>`

These notifications indicate new graph versions or indicate problems with manual modifications to connections and information of the graph.

There are multiple priority levels for notifications:

* `INFO`
* `WARNING`
* `ERROR`

Notifications store the following information:

* `referenceId` => notifications with the same `referenceId` are encountered on the same run.
* `priority`
* `type`
* `specification`
* `manualNodeId` => optional `nodeId` of the manual node to more easily check an error on a manual node
* `message` => describes the notification
* `suggestionMessage` => suggests a certain action to take
* `createdTime` => when the notification was created

`WARNING` notifications indicate errors that aren't destructive to the quality of a graph for instance, or just act as warnings for certain conditions. `ERROR` means an error was encountered when building the graph for instance, these errors must always be fixed.

**Note**: you can ignore all warning notifications, even though they should be fixed. Whenever an error notification is given, the graph isn't written, you must fix the issues in the graph.

### Sandbox

Call: `/sandbox/...`

Graphs are put into a sandbox to be able to plan routes with those graphs.

A sandbox contains:

* Simplified graph, used for routing
* Graph info of the targetted graph
* Graph info of the sandbox itself (also stores the sandbox key)
* Graph info of the saved graph (to know which saved graph has been used in the sandbox)
* Objects used to be able to plan routes

Different resources or graphs can be viewed and tested by opening, updating and closing different sandboxes and referencing the correct sandbox key. This makes testing routing on new graphs possible by opening a new sandbox to test it in.

#### Sandbox default usage

Call: `/sandbox/live`

This call returns the sandbox that's currently used live for routing. This sandbox is used as default or as fallback when a sandbox key is used.

**IMPORTANT**: whenever a graph, node or edge is being imported a sandbox key should be given to ensure that it's connected to the correct sandbox and underlying graph. When not using a sandbox key, be sure that the made changes are applied to the current live sandbox, meaning the live sandbox should not be switched between fetching, changing and/or importing the data.

#### Opening, updating and closing sandboxes

##### Opening

`/sandbox/list` => View which graphs are available to be sandboxed  
`/sandbox/available` => View which graphs are already available

`/sandbox/list/open` => Opens a sandbox with the specified graph.

**Note**: you are able to have multiple sandboxes of the same graph. The `speciesId` of the generated graphs always are `null`. By changing the `speciesId` when opening a sandbox and keeping the `ownerId` and `generationId` the same, basically opens a new version of the same graph in another sandbox.

##### Updating

`/sandbox/available/update` => Update the sandbox with the `sandboxKey`, if a new version of a graph has been generated.

##### Closing

`/sandbox/available/close` => Closes a sandbox with the specified `sandboxKey`

**IMPORTANT**: you are not able to close a live sandbox. Switch the live version to another sandbox and then close the desired sandbox.

#### Switching live sandboxes

`/sandbox/live/switchTo` => Instantly switch the live sandbox to a sandbox with the given `sandboxKey`.

#### Sandbox graph caching

`/sandbox/available/cacheAllow` => Allow simplified graph caching on a sandbox  
`/sandbox/available/cacheDisable` => Disable cache on sandbox

By allowing cache the saved graph is saved into memory to be able to generate graphs faster. Then the saved graph doesn't have to be loaded and only the manual sources need to be applied.

**Note**: when allowing cache the cache for the sandbox will be made when first updating the sandbox. When disabling the cache, the cache will be removed immediately.

**WARNING**: watch out for updating the cached save graph, because the cache will not be updated when doing this. So be sure to disable and re-enable cache when doing so.

#### Sandbox quality

`/sandbox/quality/detectDecoupledLines` => Detects decoupled lines/graphs from the simplified graph in the sandbox. It returns a list of items with polylines to indicate where it's disconnected from the main/largest graph.

### Graph

#### Graph Manage

Call: `/graph/manage/...`

Managing graph is one of the most important steps of properly combining graphs to be used in a sandbox. You can activate and disable graphs to be used when writing the graph and manage all the graphs available within RouteScout.

You are able to:

* List graph management information (and filter on `ownerId`, `generationId` and `speciesId`)
* Update graph management information
* Delete graphs => also removes the associated nodes and edges
* Add `custom` graphs

**IMPORTANT**: when graphs are added or generated they are put on inactive by default, whenever a graph with the same version already exists and it was set to active, then this setting will also apply to the created graph.

**IMPORTANT**: when updating graph management information or deleting graphs, please make sure that you really want to do this as NO backups are made of these graphs.

#### Graph Node

Call: `/graph/node/...`

Here you can fully manage all the nodes available in RouteScout. You can view all nodes from all tables, search for closest nodes with a sandbox and manage manual nodes.

You are able to:

* View all nodes in all tables
* Find closest nodes in the current live sandbox or one defined with a `sandboxKey`
* Add, update and delete manual nodes (when deleting a manual node the edges to which it's connected will also be removed)

When adding manual nodes you have the option to either input coordinates and let the rest be generated for you, or to fully customize the manual node before submitting it.

**Hint**: you can decide to write a fully specified manual node beforehand, but maybe a faster way can be to just create a manual node with the desired coordinates and then updating the manual node with the given template.

**WARNING**: make sure you don't create nodes with the same `nodeId`, when generating the graph only one node may have one `nodeId`. Make sure you correctly add/update your manual nodes! If however there are two nodes with the same `nodeId` within the same source, you have to delete either all nodes with that same `nodeId` or remove the whole graph management information and the coupled nodes and edges. You can easily circumvent this by checking if a combination of a `ownerId`, `generationId` and `speciesId` already exists. If it already exists: don't use it! If not, you can just use it and you will never run into this problem.

#### Graph Edge

Call: `/graph/edge/...`

Here you can fully manage all the edges available in RouteScout. You can view edges from all tables, search for closest edges with a sandbox and manage manual edges.

You are able to:

* View all edges in all tables
* Find closest edges in the current live sandbox or one defined with a `sandboxKey`
* Add and delete manual edges (when deleting a manual edge it's connected manual nodes will NOT be removed)

When adding manual edges you have the following options:

* Create by node => define an edge by listing `from`, `to` and `between` nodes by referencing their `nodeId`
* Create by location => define an edge by listing `from`, `to` and `between`locations
* Create by coordinates => define an edge by listing a list of coordinates

**Hint**: by creating an edge by location or coordinates: you can also add information to this edge, for every location a node will be generated with the supplied information. You can use this to easily create edges and also generate nodes for it on the fly.

#### Graph Modify

Call: `/graph/modify/...`

Node modifications are modifications added to a manual node that indicate changes to be made in the combined `saved` graph.

There are three node modification types:

* `Delete` => deletes both the manual node and all referenced coupled nodes
* `Overlay` => indicates the manual node being overlaid on top of a referenced node, this moves and merges the manual node to node on the desired location
* `Overwrite` => overwrites the referenced nodes, the manual node is just placed onto the graph

There are two node modification settings:

* `useEdges` => whether the edges connected to the referenced node should be used or deleted (is only applicable with `overwrite`)
* `useInfo` => whether the referenced node's information will be combined with the manual node

**Note**: these settings only apply when using `overlay` or `overwrite`

There are two node settings:

* `active` => whether the node modification is applied or not
* `removeManualNode`

**Hint**: these node settings are useful for testing, then you don't have to fully disable the graph information and all it's connected components. Then you are able to test this manual node in isolation.

This really is for ease-of-use, you can either choose to update manual nodes directly or add node modifications with these endpoints. This simplifies adding node modifications to an existing node, just supply the associated manual node information and fill in the node modification options.

You are able to:

* Directly add node modifications
* Add node modifications to a manual node in a sandbox: this simplifies coupling a manual node to other nodes by just supplying locations of nodes in the sandbox, the rest will be generated for you.

#### Graph Routes

Call: `/graph/routes/...`

**Note**: these routes are not used for routing itself, the simplified graph is used for this!

After the `write` step, besides the generated simplified graph, routes are also generated for being returned and displayed visually.

You are able to:

* Get all routes in the current live sandbox or one defined with a `sandboxKey`
* Get the closest route/edge in the current live sandbox or one defined with a `sandboxKey`
* Get all the routes in an optimized format (and filter on source owner)

## Use Cases

### Initially setting up the graphs

RouteScout should be setup so it can properly generate the graphs initially.

You can run the `GraphUpdater` within the IDE to generate the graphs fully without interruption or by calling trigger events `prepare`, `save` and `write` in that order.

### Fetching new graph versions

To fetch new versions of graphs, for instance the FIS of RWS, you can call `prepare`

Make sure to update the `active` attribute if you want to activate it as well.

### Adding a 'dynamic' graph (like FIS of RWS)

Specify and add to the code how the graph should be created when the `prepare` step is run. Then run the `prepare` step to load the desired new graph.

**IMPORTANT**: for this to work you must be able to give every 'dynamic' graph a version number to specify if it should be generated or if it already exists. If no version number exists, try generating a code that simplifies the whole graph either to a number or a unique id/text.

### Adding a custom graph

A custom graph can be added via it's graph management endpoint. The graph management information, nodes and edges will be generated accordingly.

### Updating a saved graph

Make sure the correct graphs are set to active in `prepare` and `custom` sources, then run the `save` step.

Make sure to update the `active` attribute if you want to activate it as well.

### Updating a version/final graph

Make sure the correct graphs are set to active in `save` and `manual` sources, then run the `write` step.

The following will be generated:

* Detailed graph
* Simplified graph
* Simplified graph with detailed edges and notes
* Routes
* Notifications (if applicable)

**IMPORTANT**: you can only use 1 `save` graph and multiple `manual` graphs. If you want to include other `prepare` or `custom` graphs, you have to include these graphs in the prior steps.  
**IMPORTANT**: you shouldn't get any error notifications, you can simply ignore warning notifications but you should still fix these.  
**IMPORTANT**: you can not yet route over this graph, you have to either open or update a sandbox to do this. You can however visually request the routes of the generated graph.

### Sandboxing a version/final graph

You can sandbox all available graphs to make sure routing works correctly. Open, update and close sandboxes to manage which graphs are available to get routes for.

**Hint**: you can test a graph in different sandboxes

### Manual nodes and edges

When adding manual nodes and edges they aren't active by default, so make sure to activate the appropriate graph management information to include it in the version/final graph.

#### Creating manual routes

You can draw routes and save them via the frontend or input nodes and/or edges directly.

#### Updating manual routes

You can update manual routes by updating manual nodes directly. You can fully change a manual node to update all of it's information.

**Hint**: when a route is too long or a route isn't connected properly you can consider removing the manual nodes and edges and redo those when you don't want to update manual nodes separately.

#### Coupling manual to existing routes

When setting the location of a 'to be created' manual node exactly on an existing node within a sandbox, it will automatically get a `overlay` node modification and will be coupled to that node when writing the graph.

You can add a short edge of a few manual nodes to couple together existing routes.

**Hint**: you can choose to disable the information of a coupled node by setting `useInfo` in the node modification to `false`. This is useful for easily coupling a manual node to a certain location, but overwriting it's information.

#### Updating existing routes

You can update existing routes by adding manual nodes and setting their node modification to `overwrite`, then you can choose to:

* use or remove edges
* use or remove info

This way you can update existing routes and manipulate their information and connected edges.

#### Removing existing routes

You can remove existing routes by adding manual nodes and setting their node modification to `delete`. This will delete both the manual node and all referenced nodes.

**Hint**: you can remove multiple nodes by just creating one manual node and referencing/connecting multiple existing nodes to it, so you don't have to create manual nodes for every existing node.

### Fixing notifications

When running the `write` step, notifications can be returned when errors are encountered. These errors can either be of `WARNING` or `ERROR` priority.

Action:  
Read the notification `message` and `suggestionMessage`, it describes what went wrong and what you can do to fix it.

Manual node errors can be fixed with the following steps:

1. Search for the `manualNodeId` with the `/graph/node/manual?nodeId=<manualNodeId>` call
2. Copy the result of the found manual node information into the `/graph/node/manual/update` call
3. Fix the issue described in the notification. To visually check the issue you can use the frontend
4. Supply the `nodeId`, `ownerId`, `generationId` and `speciesId` of the manual node
5. Try re-building the graph

### Client

#### No routes are returned

Technical steps:

1. Does RouteScout return 404?

-- Yes => the query parameters are probably incorrect  
-- No => continue

2. RouteScout returns an empty list

-- This should only happen if the starting point is located in an edge that is not connected to any edges leading to the ending point. You can fix this issue by checking the `sandbox quality` with `detect decoupled lines`.

#### Not being able to cross graph 'borders'

Technical step:  
Check if there is a connection between the graphs  
-- Yes => go to [not being able to use a desired route](https://bitbucket.org/teqplay/teqplay-wiki/wiki/RouteScout%20User%20Documentation#not-being-able-to-use-a-desired-route)  
-- No => connect the graphs with a short manual edge

#### A route is returned that's invalid or not acceptable for the specified ship

Technical steps:

1. In the frontend; find where the given route is located
2. Find out if it's from a manual source

-- Yes => go to `manual update`  
-- No => go to `manual overwrite`

Manual update  
Steps:

1. Check if the route is easy to redo, you might want to just delete the line and re-add it if it's easier.
2. Find all the manual nodes with incorrect information or location and update or delete it.

Manual overwrite  
Options:

1. If the information is incorrect you can create manual nodes with the proper information, `overlay` them on the incorrect nodes and set `useInfo` to `false` and `useEdges` to `true` to overwrite the information.
2. If the location is incorrect you can create manual nodes with the proper locations, `overwrite` the incorrect nodes and set `useInfo` and `useEdges` to `true`
3. If both the information and the location is incorrect you can create manual nodes with the proper information and locations, `overwrite` the incorrect nodes and set `useInfo` to `false` and `useEdges` to `true`
4. If the route is incorrect you can do the following:  
   -- Check which locations are incorrect, `overwrite` these locations with manual nodes  
   -- Create the appropriate edges between the added manual nodes
5. If the route is incorrect and is missing some points in between you can do the following:  
   -- For all the locations except the start and the end, `overwrite` these locations with manual nodes  
   -- For all the locations you want to add in between, `overlay` these locations with manual nodes  
   -- The start and end should also have an `overlay` with manual nodes  
   -- Properly create an edge with these manual nodes, the route then is correctly changed. Make sure to set the `overwrite` manual node's modification setting of `useEdges` to `false`, you can decide whether or not to `useInfo`.

#### Not being able to use a desired route

Context steps:

* `cemtClass` and `dimensions` of the ship may disable parts of the route => check the information on the nodes and update if needed
* `maximumResults` has been set too low so that the route just isn't able to be returned
* incorrect sandbox (`sandboxKey`) may be used
* `ignoreWithErrors` automatically removes routes with errors
* `optimizeCEMTErrors` if not set, removes errors with cemt class errors, if `ignoreWithErrors` is set

Technical steps:

1. Check if the route is returned within RouteScout when routing between the given locations

-- No => continue  
-- Is the route passed to the platform? Yes => there might be a filter (bridge, lock, etc.) removing it there  
-- Else => go to `context` steps

2. Visually (in the frontend) check if the desired route is connected

-- No => continue  
-- Yes => go to `context` steps

3. Check if the `context` steps are the problem

-- No => Continue

4. Create or connect the needed routes and add or update the wanted information