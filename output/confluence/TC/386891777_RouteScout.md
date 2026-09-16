---
id: confluence:386891777
source: confluence
type: page
space: TC
title: RouteScout
author: lucas (Unlicensed)
date: '2024-07-01'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/386891777
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/386891777
---
# RouteScout

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/386891777  

## Content

## Design

<https://www.figma.com/design/5fLFnUEt43ESOP7D4GZ3JL/RouteScout-UI-Exploration?node-id=0-1&t=gtMUTvbkbHCA7uLa-1>

## Resources

* <https://vitejs.dev/>
* <https://reactrouter.com/en/main>
* <https://github.com/mapbox/mapbox-gl-draw>
* <https://github.com/visgl/react-map-gl/tree/7.1-release>

---

# Specification

## Environment

### Application Modes

The application will have two modes; the graph manager and route planning mode. The default mode will be the route planning mode. Users who have authorization to do so can switch to the graph manager mode by clicking on a switch in the header.  
  
**Graph Manager**  
The graph manager mode is used to make changes to the graphs and add new elements such as bounding boxes or area filters. This mode will only be available to authorized users.  
  
**Route Planner**  
The route planner features will consist of the ability to mark points on a map and create a route between them. The route will be shown visually on the map and detailed information will be shown in the primary panel in the UI. Additionally users can select segments of a route to view their information.

### Assistance

To assist users in using the application, tooltips will be provided when hovering on elements such as toolbar tools or buttons.

---

## Authentication & Authorization

### Users

The route planning functionality of the application will be available to every user. Making changes for graphs through the graph manager mode will be available to users with a specific role.

---

## Core Elements

### Manual Graphs

Manual graphs are graphs created by the user. These graphs consist of routes drawn manually as opposed to those that were imported. There can be multiple manual graphs which can be interacted with through the layers and properties panel. Manually drawn routes belong to one manual graph. Visibility of graphs can be toggled through the layers panel.

| **Method** | **Endpoint** | **Description** |
| --- | --- | --- |
| `POST` | `/v1/graph/manual` | Create/update manual graph. |
| `GET` | `/v1/graph` | List available graphs and their versions. |
| `GET` | `/v1/graph/{id}` | Get graph content by ID. |

### Source Graphs

Graphs containing routes can come from external sources, these are called source graphs. These graphs only contain route data which are stored as edges. The sources can be hidden to remove them from the view of the map or disabled to exclude them completely.

| **Method** | **Endpoint** | **Description** |
| --- | --- | --- |
| `GET` | `/v1/graph/source/check/update` | Check if an update is available for a source. |
| `POST` | `/v1/graph/source/{source}/update` | Update graph for a specified source. Where `source=FIS/FRYSLAN/etc.` |
| `GET` | `/v1/graph` | List available graphs and their versions. |
| `GET` | `/v1/graph/{id}` | Get graph content by ID. |

### Bounding Boxes

Bounding boxes are elements that are stored separately and can be used to resolve conflicts with graphs or add new functionality. The bounding box is essentially a polygon with any amount of sides that defines an area. Pre-defined shapes such as rectangles, circles and hexagons are provided. The bounding box can be used to connect routes that have been manually created in a manual graph to a different graph.  
  
The bounding box has two use cases:

* **Connecting graphs/routes together:** routes from separate graphs can be connected using a bounding box. Any edges intersecting with the polygon will be connected with each other in a new point. To determine this point, the user can create a bounding point marker which will define the location where the intersecting edges should connect.
* **Adding bridges or locks:** bridges can be added onto a route by creating a bounding box on the location of the bridge. A bounding point is used again to determine the exact location of a bridge.

| **Method** | **Endpoint** | **Description** |
| --- | --- | --- |
| `GET` | `/v1/bounding-box` | List all. |
| `GET` | `/v1/bounding-box/{id}` | Get by ID. |
| `POST` | `/v1/bounding-box` | Create or update. |
| `DELETE` | `/v1/bounding-box/{id}` | Delete. |

### Area Filters

An area filter is a polygon area defined by the user where imported graph sources can be included or excluded. Area filters can be easily disabled through a toggle in the properties panel. Additionally, they can be given a name which will be displayed on the map to make them more easily identifiable.

| **Method** | **Endpoint** | **Description** |
| --- | --- | --- |
| `GET` | `/v1/area-filter` | List all. |
| `GET` | `/v1/area-filter/{id}` | Get by ID. |
| `POST` | `/v1/area-filter` | Create or update. |
| `DELETE` | `/v1/area-filter/{id}` | Delete. |

### Environments

Data for the graphs can be stored in three different environments; Preview, Development & Production. Updates are always done on the preview environment but can be easily synced to the development or production environment. The preview environment is the one you will be viewing through the interface

| **Method** | **Endpoint** | **Description** |
| --- | --- | --- |
|  |  |  |

### NO-GO Zones

A no-go zone is a polygon area defined by the user that has a function based on the current mode in the application. When the user is in the route planning mode, the zone prevents edges within the polygon from being used in the generated route. In the graph manager mode, the zone contains metadata about obstacles which may influence the route.

---

## Viewport

### Map Elements

The elements that show up and the way they are displayed are dependent on the zoom of the map. The more zoomed out, the less detail you will see. The more you zoom in, the more elements will start showing up in their concrete shapes. The colors of various elements will be distinct from each other to enhance visibility.

### Layers

Graph data will be supplied in various chunks and layers. Users can interact with these layers to hide or disable them and view their detailed information. The detailed information can be triggered using a info icon which will open a detail popover below the icon, showing the information. (i.e. graph creation date, update date)  
  
**Layers:**

* Manual graphs
* Source graphs
* Area filters
* Bounding boxes
* Bridges
* Locks

---

## Making manual changes

### Graph Tools

To make changes to graphs, users can select graph tools from a toolbar. This toolbar includes tools for selection map elements or creating things like bounding boxes and area filters.

### Auditing

Changes that are made by the user are stored and persisted in the back-end. A list of these changes is shown in the front-end. Changes could contain an action to easily undo the change. When a user is satisfied with the changes, they can apply the batch of changes on the preview environment. This will remove them from the active changes list that is displayed in the primary panel.

### Properties

Properties for routes, bounding boxes, graph area filters etc. can be added or changed through the properties panel. The data displayed in this panel will be dynamic based on the selected element on the map. An alert will be shown in the panel to indicate if a selected element contains any missing information.  
  
(T.B.D) Changing properties for routes that are not manually inserted. Discussed with Joost: Property override polygons?

### Updating routes from imported sources

Making manual changes to the locations of route nodes and edges will not be supported as of now.

### Applying changes

Changes that have been made can be applied through in batches to the preview environment. An apply button will be visible in the top right which will open up a detailed dialog with a button to apply the changes. This dialog will show a list of changes that were made and include indicators for invalid changes that need to be fixed before they can be applied.  
  
There may be active conflicts when applying a change but this should not prevent the user from applying their manual changes.

### Syncing changes to environments

Changes are always applied to the preview environment. When the preview environment is out of sync with the development or production environment, this will be displayed to the user. The user can then choose to simply sync to one of the environments. This will be a simple dialog with one action, a list of changes will not be shown.

### Changes with issues

When changes contain critical issues or warnings, this will be clearly indicated using icons and distinct colors. The change will be blocked from being applied if it has a critical issue. Issues with warnings may be ignored by the user.

### List of issues

| **Target** | **Tone** | **Issue** | **Solutions** |
| --- | --- | --- | --- |
| Bounding Box | 🛑 | There are no points or edges inside the polygon | Move or remove the bounding box |
|  |  |  |  |

---

## Conflict resolution

### Notifying users of conflict

When a user with access to the graph manager launches the application, a notification will be shown if there are any unresolved conflicts. These conflicts can also be found in the conflicts tab of the primary panel. If changes contain a target object with a specified location, users can click a button to center the map on this location from the primary panel tab. If conflicts have a specific target and/or location, this will also be highlighted on the map using specific markers.

### Source updates

Users will be notified that updates for a graph source are available through a notification badge in the header. A dialog will open from which the user can manually choose to update a source to the newest version. The date and version of the source will be displayed.

### Data structure

Conflicts can be divided into two types, critical and warning. The conflicts will contain a title, description and possible solutions or actions to take to resolve the issue. Optionally it can include a target so the front-end will be able to visually display where the conflict resides.

### Examples of conflicts solutions

Some conflicts might have visual examples of how to resolve them. When this is the case, a examples button will be present in the conflict which is displayed in the list. This button opens a dialog which shows before and after situations of resolved conflicts. Multiple examples may be given.

### Resolving conflicts

Conflicts need to be resolved by users through making manual changes. When the user thinks a change has resolved a conflict, the conflict can be marked as resolved through the conflict card in the primary panel. Conflicts coming from the back-end can contain metadata such as steps to resolve the conflict, the target of the conflict, or possible solutions for the conflict.

### (T.B.D) Side by side

If a user would benefit from seeing the before and after situation of a conflict, this will be shown by splitting the map viewport into two vertical panels.

### List of conflicts

| **Target** | **Conflict** | **Solutions** |
| --- | --- | --- |
|  |  |  |
|  |  |  |

---

## Route Planning

### Defining a route

Routes can be defined by using the route tool in the route planning mode and clicking on the map to create route nodes. When the user is satisfied with the route, they can click a button in the secondary section of the toolbar to generate the route. A list of possible routes is then shown which can be selected from the primary panel. When a route is selected, it will be highlighted on the map and the primary panel will show details of the route such as bridges and locks that you will encounter.

### Configuring route settings

Settings for the route such as width, height and CEMT class can be configured through the primary panel. To apply the settings, the routes will need to be calculated again by clicking on the button in the secondary section of the toolbar

---

## Non-functional requirements

* **Responsive design:** the application will only support desktop devices. Mobile might be considered in the future for the route planning feature.
* **Multi-language:** the application will only include the English language.