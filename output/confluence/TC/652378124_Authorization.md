---
id: confluence:652378124
source: confluence
type: page
space: TC
title: Authorization
author: Richard van Klaveren
date: '2025-03-04'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652378124
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652378124
---
# Authorization

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652378124  

## Content

Addressing authorization within the Teqplay platform has been postponed deliberately till a moment where authorization both is required and a more clear view is available on what kind of authorization is required.

In order to address authorization the following model of relevant entities has been made:

* Users – The users of the applications, represented by UserProfiles in the platform
* Apps – The apps users can use
* Authorization groups – A functional grouping of one or more relevant resource calls in the API
* Resource Calls – The endpoints a user can call in the API of the platform

The basic thought is:

* All authorization will happen at the API, no content based authorization is envisioned
* For each user we want to control the resource calls he / she has access to. However, listing all resource calls for each user will be quite a hassle from maintenance perspective, therefore functional ‘Authorization groups’ have been defined.
* Authorization should have minimum impact on latency, since executed for each call. Therefore for each user a list of allowed resource calls will be made available, and a simple match will suffice.

In order to define a maintainable approach, 2 levels of indirection have been introduced:

* **The Authorization group level** holding a group of endpoint calls that functionally belong together, for example all calls related to retrieving current vessel status, or all calls related to retrieving historical events. This information is stored in a userProfile as well, and used as leading information for the authorization.
* **The app-level** describing which authorization groups are involved per app. This mapping will be maintained in the database, and will be stored per user-profile. However, for authorization this is not the leading entity. The apps a user has access to will be used only in case of a recalculation of the ‘authorization group’s a user has access to in case the mapping between apps and authorization groups change.

In short, changes for this process that are required are:

1. Document the approach (this wiki)
2. Definition of authorization groups in the backend and database (first proposal on functional decomposition is provided below)
3. Definition an implementation of mapping of which authorization groups are required per app
4. Implementation of Authorization mechanism itself as part of a ContainerRequestFilter or Interceptor.
5. Definition of a tool that allows the definition of users to apps and/or authorization groups
6. Conversion of existing users to allow only relevant calls.

The following apps currently are supported by the specified Authorization Groups:

* **AIS Buddy** – CurrentShipRead, Communication
* **Riverguide** – CurrentShipRead, InfrastructureRead, RoutePlanner
* **Koerswijzer** - CurrentShipRead, InfrastructureRead, hydroMeteoRead
* **Timeline** – CurrentShipRead, HistoricShipRead, AISEncounterEvents, InfraEncounterEvents, Context Events, InfraRead, subscription
* **NEI** - PortcallStatsRead
* **BinnenvaartTimeline** – CurrentShipRead, HistoricShipRead, AISEncounterEvents, InfraEncounterEvents, Context Events, HydroMeteo, InfraRead
* **BargeSchedules** - schedules
* **BridgeMonitor** – HistoricShipRead, CurrentShipRead, BridgeMonitor, InfraEncounterEvents
* **AreaMonitor** – CurrentShipRead, HistoricShipRead, AreaRead, AreaEvents
* **SluisMonitor** - AreaRead, AreaEvents, CurrentShipRead
* **BerthMonitor** – InfraRead, BerthMonitor
* **IRIS** - HydroMeteo
* **AcousticEventEngine** – HistoricShipRead, CurrentShipRead, IOT, InfraEncounterEvents
* **Movable Asset Monitor** - IOT
* **Trailerdashboard** - IOT
* **Kraandashboard** - IOT
* **IOT-Analyse** - IOT
* **Demonstrators** - Demonstrator

Following authorization groups have been identified. Next to access to the specific calls, also access to the login, logout and change password calls in the /auth/ resource are provided to ALL authorization groups via de 'Public' authorization group.

| **Group** | **Function** | **Resource** calls |
| --- | --- | --- |
| **CurrentShipRead** | Allows reading all current AIS data | GET /ship/\* (excluding history) |
| **CurrentShipRead** | Allows reading all current AIS data | POST /ship/mmsiListPOST /ship/polygon |
| **HistoricShipRead** | Allows reading of all historical AIS data per vessel | GET &POST /ship/history/\* |
| **AreaRead** | Allows reading of all areamonitor events, and areamonitor bounding boxes | GET /area/\* |
| **PortcallStatsRead** | All NEI related calls to read portcall information in the NEI | GET {NEI}/\*GET & POST /portcall/\* |
| **HydroMeteo** | All HydroMeteo calls to retrieve hydro and meteo data | GET /weather/\*GET {IRIS}/\* |
| **AISEncounterEvents** | All Encounter events, both AIS based | GET /proximity/\*GET & POST /event/\* (filter on ship-ship) |
| **InfraEncounterEvents** | All Encounter events AIS with Infrastructure based | GET& POST /event/\* (filter on infra) |
| **AreaEvents** | All area related AIS Events | GET & POST /event/\* (filter on area) |
| **Context events** | All events triggered based on context, e.g. strong wind or PIN events | GET & POST /event/\* (filter on context) |
| **BerthMonitor** | All berthEvents retrieval and BertVisits retrieval | GET & POST /berthVisits/\* (filter on terminal)GET bertVisit/\* |
| **InfraRead** | Allows reading of all infrastructure information (berths, buoys, …) in the system | GET /static/\* |
| **InfraUpdate** | Allows updating of infrastructure information, like updating bridges, berths etc. | GET & POST & PUT & DELETE /static/\* |
| **BridgeMonitor** | BridgeMovement reads | GET bridgeMovement/\* |
| **Communication** | All communication calls | GET & POST /communication/\*ALL /areachat/\* |
| **IOT** | Allow all IOT related calls | GET /sensor/\*GET /acoustic/\* |
| **Demonstrator** | Allows logging in only, no calls are allowed | <none> |
| **Administrator** | All admin functions like updating, deleting users etc. | <ALL> |
| **SubScription** | Subscribe for all notifications | GET/POST/DELETE /subscription/\* |
| **RoutePlanner** | Plan a route from a to b | GET & POST /route/\* |
| **Schedules** | Retrieve all information related to schedules | GET /schedules/\*GET /deepSeaSchedule/\* |
| **Public** | All calls available without login | POST /auth/login |

### App login facility

These authorization groups will control individual access to each of the end-point calls. However, each app (as depicted above) will require possibly multiple authorization groups to successfully operate. Therefore the intention is to add an additional login parameter, telling which app is logging in. The result of the login call will provide feed-back based on the provided authorization whether all required calls for this app will be authorized or not.

This page describes the technical implementation of authorization in the backend.

## TeqplayPlatform

In the TeqplayPlatform.java the AuthorisationFeature is added to the RegisterResources method. Also, at the end of the RegisterResources method there is call to the AuthorisationInterceptor to create a mapping of all the registered resources.

## AuthorisationFeature

The AuthorisationFeaure is used to register the AuthorisationInterceptor in the context.

## AuthorisationInterceptor

This is where all the magic happens. Most important variables and methods:

**resourceAuthorisation** This is a mapping of resource calls for authorisation. They key contains the HTTPMethoud and resource path, e.g. POST/auth/login. The value contains an ResourceAuthorisation object with regex-pattern and groups for this resource call.

**filter method** This is the actual filter of the call. This authorises of unauthorises people when they are trying to do calls to the platform.

1. It checks if security is used
2. It checks if there is a logged in user and if that user is admin
3. It checks if resource call has authorisation defined
4. It checks if resource call has the PUBLIC as group
5. It checks if a logged in user does the call
6. It checks if logged in user has the group of the resource call
7. Then it will return if user is authorized of abortWith specific errorCodes

##Using authorisation in resources## To use the authorisation in resources there is special annotation developed. This annotation is called `@Auth` and only contains a group parameter.

For example, to give a resource call access to the INFRA\_READ group, you add this annotation:

#!java
@GET
@Path("/vhf/kml")
@Auth(group = Auth.Group.INFRA\_READ)
@ManagedAsync
@ApiOperation(value = "Retrieve the VhfSector overview in the specified bounding box", response = VhfSector.class, responseContainer = "List")
@ApiResponses(value = { @ApiResponse(code = 404, message = "No notifications found") })
public void allVhfSectorsInBoundingboxAsKml(#!java
@Auth(group = Auth.Group.INFRA\_READ)

You can also assign multiple authorisation groups to a resource call. Add brackets to do this.

#!java
@Auth(group = {Auth.Group.INFRA\_READ,Auth.Group.INFRA\_UPDATE})

If you do NOT add the auth annotation to a resource call, the resource call will not be available and you will receive an 1504 errorcode, Authorization failed: Resource has no authorization defined.

##Creating new authorisation groups## To create a new authorisation group open the Auth model in `model/auth`. Here you will find an enum Group with all groups that are available for the auth annotation.