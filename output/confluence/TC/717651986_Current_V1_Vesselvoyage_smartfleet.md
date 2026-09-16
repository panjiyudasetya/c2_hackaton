---
id: confluence:717651986
source: confluence
type: page
space: TC
title: Current V1 Vesselvoyage/smartfleet
author: David Hansson
date: '2025-04-30'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/717651986
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/717651986
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/717651986/Current+V1+Vesselvoyage+smartfleet#Visit-page
---
# Current V1 Vesselvoyage/smartfleet

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/717651986  

## Content

# **Ship page**

`/v1/vesselvoyage/visits/imo`  
We are calling this when are on the **Port schedule** tab, we also pass the params like this:

1. start: 2025-03-29T15:52:31.253Z
   end: 2025-04-29T14:52:31.254Z
   imo: 9470973

We use the start and end filters to allow users to filter all visits within a specific time range.

**ADMIN FEATURE ONLY**   
`/v1/vesselvoyage/visitsAround/imo`  
We use this feature to retrieve the two most recent visits and display a simple trace on the map for admin users.  
  
`visit?.progress?.historicVoyage?.trace` and also:

  const historicVisits = visits.filter(v => v.ataPort)
  const plannedVisits = visits.filter(v => !v.ataPort)

Following this link take you to this page: <https://portreporterdev.teqplay.nl/ship/636093269>

---

# **Visit page**

`/v1/vesselvoyage/visit/id`  
This is currently a fallback on the visit page, usually we always prio the `/v1/smartfleet/${fleetId}/voyage/` endpoint to get the information and then fallback to vesselvoyage if we don’t find any visitID or by the visitPort in the smartfleet endpoint  
  
We are taking the information from the visitID and taking the data from .`esof` property which contains all the stops and encounters like this:

{
"encounters": [],
"stops": []
}

We also show relevant information on the map, including traces of recent visits, like the stops and encounters in the tabs

We also use the portschedule tab here:

We also use the here:  
`/v1/vesselvoyage/visits/${imo}/count`  
This function is designed to improve backend performance by minimizing unnecessary data fetching. It first queries the backend to determine the total number of visits If the number of items is less than or equal to the specified radius, the function skips re-fetching visit data, assuming that all relevant visits are already included  
  
 **ADMIN FEATURE ONLY (Red notes)**  
`/v1/vesselvoyage/visitsAround/imo` For the search around  
`/v1/vesselvoyage/visits/imo` + date query For the search Range  
`/v1/vesselvoyage/visits/${imo}/ids`  
This function optimizes the process of fetching visit data by first querying the backend for the total number of visits associated with a specific IMO.

<https://portreporterdev.teqplay.nl/visit/df512c66-2648-4bfc-b58f-d0c9010ede8c.VISIT> (Vesselvoyage endpoint without a fleet)

---

# **Portcall page**

`/v1/vesselvoyage/visitsAroundPortcall`  
  
We use this endpoint to get 2 pink containers, so the traces with some information on the map. And also the visits port (unlocode +port name),   
For the map we use:  
All the visits +  
`visit?.progress?.historicVoyage?.trace`  
`visit?.progress?.predictedVoyage?.trace`  
  
The port schedule is same logic as [Visit page (port schedule tab)](https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/717651986/Current+V1+Vesselvoyage+smartfleet#Visit-page) . And only Admins are able to filter on dates + view more historic visits

Following this link take you to this page: <https://portreporterdev.teqplay.nl/portcall/USCRP290255>

---

So basically we use:

* **Primary for visit page**

  + `/v1/smartfleet/${fleetId}/voyage`

    - Primary endpoint for retrieving voyage and visit information.
    - If no `visitId` or relevant port visit data is found here, fallback to `/v1/vesselvoyage/visit/id`
* **Fallback and Visit Details**

  + `/v1/vesselvoyage/visit/id`

    - Fallback for retrieving visit details when not found in SmartFleet.
    - Example: `/visit/df512c66-2648-4bfc-b58f-d0c9010ede8c.VISIT`
* **Port Schedule View**

  + `/v1/vesselvoyage/visits/imo`

    - Used for fetching visits for a ship (via IMO) for the **Port Schedule** tab.
    - Example: `/ship/636093269`
* **Ship Page (Around Visits)**

  + `/v1/vesselvoyage/visitsAround/imo`

    - Retrieves visits for the given ship (IMO).
    - Used in **map traces**, and **compact info cards**.
    - Only a **admin feature**
* **Port Call Page (Around Portcall)**

  + `/v1/vesselvoyage/visitsAroundPortcall`

    - Fetches visits for a given **port call ID**.
    - Used in the **port call page**, map, and small detail components.
    - Example: `/portcall/USCRP290255`
* **Visit Count Check**

  + `/v1/vesselvoyage/visits/${imo}/count`

    - Lightweight endpoint that returns only the **count of visits**.
    - Used to optimize performance: if the count is ≤ radius limit, visit data fetching is skipped.
* **Visit by IMO and ID**

  + `/v1/vesselvoyage/visits/${imo}/ids`

    - Only to retrive a list of visit ids, **only a admin feature**

This is how the current structure mainly look like:

export interface VesselVoyageVisit {
imo: string
port?: PomaPort // Normal poma port
ataPort?: string
ataLocation?: Location
atdPort?: string
atdLocation?: Location
esof?: ESOF
progress?: Progress
planned?: PlannedLocation
linkedPortcall?: string
id: string
previousEntryId?: string
nextEntryId?: string
}interface Progress {
historicVisitTrace?: string
historicVoyage?: Travel
predictedVoyage?: Travel
}interface Travel {
distanceInKm: number // double
trace?: string
}interface PlannedLocation {
unlocode: string
port?: PomaPort
}
export interface ESOF {
encounters: Encounter[]
stops: Stop[]
}