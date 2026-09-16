---
id: confluence:226590721
source: confluence
type: page
space: TC
title: RouteScout Refactor Proposal
author: Former user (Deleted)
date: '2023-11-20'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/226590721
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/226590721
---
# RouteScout Refactor Proposal

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/226590721  

## Content

On this page, we will be showing the plan for the RouteScout refactor. Our main goal with this refactor is to enhance manageability and user accessibility, even for users without any prior knowledge of the subject.

**Key Features and Enhancements:**

1. **Simplified Data Management:** One of the main priorities is to allow users, regardless of their prior experience with the project, to update nodes/edges and manage graphs. This process will be made possible using a front-end which shows the user all of the information needed to make changes.
2. **Graph Maintenance:** The new design is focused on making it a lot easier to maintain graphs. New incoming updates are first automatically handled. When this process fails, users without any technical experience should be guided through all of the conflicts where they are able to fix them.
3. **Transition to an Edge-Based System:** We will be moving from a node-based to a edge-based system. Information will be stored on edges instead of nodes.
4. **Enhanced Edge Information:** The application will incorporate additional data on edges, such as NOGO areas, maximum speed limits, and other relevant parameters.
5. **Authentication:** All of the endpoints will contain authentication in the new refactor.

### **1. Simplified Data Management**

**Ease of Updating Nodes/Edges/Graphs:** The current version of RouteScout presents challenges in updating nodes, edges, and graphs, requiring manual database entries and re-initiation of the entire graph creation process. This not only is time-consuming but also inefficient, particularly when verifying if updates are successful. In the new RouteScout system, users will have the ability to interact directly with the graph in a front end. The application will show the current state of the graph, allowing users to plan routes and gain an understanding of the graph's layout and data. Users will be able to click on any edge within the graph to view the information attached to it. Also, the process of adding, removing, or editing nodes and edges will be significantly simplified. Users should be able to make these changes without having to touch the database layer at all.

**Deployment from DEV to LIVE:** The RouteScout refactor will still have one environment on which we can manage LIVE and DEV active graphs. Modifications made in the DEV graph can be deployed seamlessly to the LIVE graph through the front-end interface. This approach ensures that changes are tested and reviewed in the DEV graph before affecting the LIVE graph. And will also keep the DEV and LIVE graphs in sync as much as possible.

**Inline Editing Feature:** Another one of the upgrades is the introduction of inline editing. This feature eliminates the need to recreate the entire graph for minor modifications, thus saving a lot of time and making the updating process a lot faster.

### **2. Graph Maintenance**

**Faster and more efficient Graph Maintenance:** One of the key objectives with the new RouteScout system is to significantly speed up and streamline the graph maintenance process. We aim for a system that can allow people with no prior knowledge to maintain the graphs of RouteScout.

Currently, updates from data sources like FIS or FRYSLAN can be challenging due to manual changes that have been applied to the old data from previous updates. This often leads to conflicts that hinder the automatic update process.

**Two Layered Graph:** To address this, the new version of RouteScout will only contain a two-layered graph:

1. **The Manual Layer:** This layer will contain all the manual changes and edits made to the graph.
2. **The Import Layer:** This layer will consist of data imported from external sources such as FIS or FRYSLAN.

**Bounding Boxes:** One approach is to automatically reconnect these manual changes to new imported data is by using bounding boxes. How these works is briefly explained further into this page.

**Graph Creation with Conflicts:** Another addition in the new application will be the ability to create and visualize the graph even when there are unresolved conflicts. This feature is not available in the current system and will be an improvement, as it allows the visualization of the conflicts making them easier to solve.

**User-friendly conflict resolving:** When conflicts still arise after automatic resolving failed, the new RouteScout front end will even enable users with no prior knowledge to resolve them effectively. The system will first **notify** the users and then guide them through each conflict, providing assistance in identifying and solving issues. Users will be presented with both the old and new situations around each conflict. This comparative view allows for a better understanding of the changes and helps in making decisions to resolve the issue. Users can then add, remove, or move nodes and edges on the map to resolve the conflicts.

**Deployment:** After resolving conflicts, users will have the option to deploy these changes to either the DEV or LIVE environment directly through the front-end.

### **3. Edge based system**

In the current RouteScout system all graphs are primarily based on nodes having information. Nodes hold the information like dimensions, CEMT class, etc. Edges only connect two nodes together.

Since RouteScout was a node-based it system it would mean that:

* If a route has an invalid CEMT class, and the route consists of 10 nodes, then you have to update all 10 nodes individually for the information to correctly be updated
* If you want to delete a route, you need to delete nodes attached to that route. If the route only consists of two nodes, you are out of luck. You’ll need to delete one of those two nodes, and then redo all the edges that will be removed due to the removal.

In the new RouteScout the application will be edge-based, meaning:

* If information on a route is incorrect, you can update the information in one go.
* If the route should be removed, you can simply select the edge and delete it in one go.

Making the system edge-based immediately makes it easier for a user to edit the graph through the front-end. The only “downside” of making the system edge-based is that edges are not inferred based on the connections between the nodes. Previously, if you wanted to add an edge you just draw a new line and attach it to a pre-existing node, which takes care of creating the right edges. Since the nodes will not be leading anymore, you’ll need an option to split edges. How this could work is described later on.

Apart from making the editing of the graph easier, it also means that the graph itself can be stored in a smaller format. The duplication of lots of data because the same data exists multiple times on multiple nodes will not be an issue anymore. Graphs could be purely made up of edges. Containing the junction points, the detailed route in-between, and the information like dimensions and CEMT class. This also matches better with other systems that expose or route through graphs, which also reason more in terms of edges.

### **4. Enhanced Edge Information**

**Incorporating Essential Route Dimensions:** Like the old RouteScout, the new RouteScout application will maintain route dimensions such as width, height, allowed draught, CEMT classes, and permissible recreational classes, along with elements like bridges and locks.

**Visibility of Missing Information:** Another improvement in the new version is the visibility of missing information on certain routes. The front-end design will indicate when specific data points, such as dimensions or restrictions, are absent or incomplete for a certain route. This feature ensures that users are immediately aware of potential information gaps. It will be easy for users to add this missing data to the graphs using the new front-end.

**Additional Route Information:** The new RouteScout will also incorporate additional data to its routes:

1. Maximum Allowed Speed
2. Temporary Route Unavailability/Bridge Operations
3. Designated NO GO Areas (If a user wants to avoid the Suez canal for example)
4. Specifics for Sea or Inland Routes

**Prioritization of Data Relevance:** While all these features add value, we need to prioritize data like maximum speeds and NO GO areas because they will likely receive more usage, especially for sea routes. Information such as bridge waiting times, while useful, might be less prioritized due to its lower relevance for inland routes.

### 5 Authentication

**Authentication for All Endpoints:** In the new RouteScout version, every endpoint will require user authentication.

**Access for Users:**

* **Route Planning:** Available to all authenticated users, allowing everyone to plan routes effectively.
* **Graph Management:** Restricted to selected internal users, ensuring that only authorized personnel can manage and update the graph.

## **Main requirements**

* maintenance  
  Apart from the main developers of RouteScout, people should be able to make informed changes to the graph.
* sailable lines / polygons  
  There’s a possibility of getting weird routes, depending on how the rounded lines are drawn. Sailing from one port to the next, first taking a detour, then getting back on track.  
  See also: RouteScout refactor

## **Requirements**

| **Prio** | **Requirement** |
| --- | --- |
| **M** | All endpoints require authentication. |
| **M** | Only internal users are allowed to manage the graph. |
| **M** | The user is notified of any automated updates to the sources. |
| **M** | The user is taken through a guide to solve the issues, as detected during the automated updates. |
| **M** | The user can detect issues themselves and solve these by being taken through a guide. |
| **M** | The user has to approve the made changes before they are applied. |
| **M** | The user has the option to make these approved changes be propagated to the DEV/LIVE environment used for route requests. |
| **M** | All routes must have information like: allowed dimensions, CEMT class, recreational class. The user has a way to be made aware of anything missing information. |
| **S** | Route information like maximum speeds and “NO GO” areas should be able to be added and/or supplied by the requesting user. |
| **C** | Route information like bridge waiting times and information about operations could be added. But are mostly relevant to inland skippers. |

## **Conflicts that can occur when automatically updating data**

| **Issue description** | **Solution / possible actions** |
| --- | --- |
| Route is missing, can be attached to end of an edge/node. | User draws a route and attaches it to the pre-existing edge/node from an existing route. |
| Route is missing, but needs to be added in the middle of an edge. | Be able to split a route into two edges and continue drawing a route from there.  *Backend should be edge-based, not node-based. So splitting an edge is made possible.* |
| Bridge needs to be removed. | User is able to edit the information on a node to make sure it doesn’t incorporate the bridge information anymore.  User also has the option to delete the node if the route is not valid anymore after changes in data (Bridge cannot open anymore). |
| Bridge needs to be added. | The user can add a bridge to the edge, and indicate where it’s located along that edge.  *In the frontend, click on the edge to add a node where the bridge is located. Then this (dynamic) bridge information is stored along the edge, but the existence and location of the bridge is stored on the node.* |
| Route is incorrect, needs to be removed. | The user can delete a route/edge in one go, by selecting the edge and deleting it. |
| Route dimensions/CEMT is incorrect, needs to be updated. | The user can select the edge, see the information stored on that edge (like the dimensions and CEMT), and is able to edit this in one place for the whole edge.  An edge could be part of a larger route. The user should be able to see all edges as part of a route. Nice to have; would this user then also be able to edit these edges?  *Backend should be edge-based, not node-based. So information is attached to the edge and can be updated all at once, instead of needing to update all individual nodes.* |
| Route is incorrect, shape needs to be adjusted. | The user can select the edge, and change the shape of the route by dragging on the nodes along the lines. (Just like polygons in POMA)  *How should the backend be able to automatically update these?* *=> see examples below* |

### Bounding Boxes

For a given route, you indicate an area where you’d like to make a “cut” in the edge.

At that area you specify which location should be used for any line crossing that area.

The example below shows the addition of a bridge and a specific location for that bridge. Where the white line intersects with the green area, the edge is cut in two parts. The edge is then reconnected by adding the intermediate green point.

This would allow for the line of the other source to shift. As long as there is still a line intersecting the box, there will be no conflicts and no manual fixes needed.

How would this work if multiple lines are meant to intersect with the box? When connecting two different graph sources for example: the sea connection between FIS and Cofano, or the Friesland connection between the FIS and Fryslan sources.

Maybe the following example, where the area is used as “glue” between two sources. Where the lines within the area should be removed, and the connection between the two lines is automatically made within this circle.

## **Meeting notes from Requirement Session**

### Authentication

All endpoints must require being authenticated.

All users must be able to plan routes, but only select (internal) users are allowed to manage the graph.

### Management via the frontend

The user must be able to see the current (knowledge of the) graph, and be able to plan routes on it.

The user receives a notification that a source like FIS/Fryslan has been updated, and gets informed about what potential issues need to be resolved.

To solve these issues the user is, for every issue, taken through a guide which displays:

* The old situation.
* The new situation.
* Options/actions to take to de-conflict this.
* Approve the changes.

After fixing and approving all changes, the user has the ability to bring these changes to the DEV/LIVE environment.

The user must also be able to initiate this process themselves, for example when informed of issues by customer support. The user is then taken through a guide to:

* See the current situation.
* Identify the issue(s).
* Apply certain actions to fix this.
* Approve the changes.

### Information on the routes

The routes must have information related to:

* maximum dimensions, such as width, height, allowed draught
* allowed CEMT classes
* allowed recreational classes
* items on the route, like bridges and locks

The user must be made aware if this information is not available on certain routes. And the user must be able to add or correct any missing/wrong information.

In relation to the ETA, other information could also be included, like:

* maximum allowed speed
* routes that are temporarily not available / bridges that aren’t operated

Other context information that could be included, like:

* bridge waiting times
* “NO GO” areas, indicating you don’t want to sail into the Suez Canal for example
* not sailing either sea or inland specific routes

This information, although useful, might not be implemented due to less relevance for inland routes (mostly looking at bridge waiting times). We’ll be more likely to focus on maximum speeds and “NO GO” areas, since they are (more) applicable to sea routes.

## **Timeline**

* **Plan an envision meeting with Joost D & Maurice, to brainstorm about:**

  + How the scenarios, like solving issues, actually will work. How will the user be guided through the process, what will they see, what will they need to do, how to accomplish this from a backend perspective?
  + required backend features to make this possible
  + write a proposal based on this, and let it be reviewed (or meet again with Richard)
* **Work this out in a more detailed plan that results in Jira issues being created, containing at least:**

  + think about the data model

    - what is the request model?
    - what is the graph model? (what is the primary perspective, node or edge based?)
    - how will a new graph be communicated with the DEV/LIVE environment?
  + make designs for frontend
  + start implementing the backend
* (longer term, but soon-ish) **Phasing out current RouteScout v1, using the new RouteScout v2 instances. Ensuring backward compatibility.**