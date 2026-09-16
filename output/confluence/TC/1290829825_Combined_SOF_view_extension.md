---
id: confluence:1290829825
source: confluence
type: page
space: TC
title: Combined SOF view extension
author: Darius Wattimena
date: '2026-07-20'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1290829825
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1290829825
---
# Combined SOF view extension

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1290829825  

## Content

Currently we have a VesselVoyage SOF with only AIS based information. Next to this we have portcall information which has all the PCS information.

For UAB online the need was created to have a merged SOF data view so they can have both VesselVoyage data and portcall information in one endpoint.

We imagined for now to have a solution in the Teqplay API itself, later on we want have a single component that resolves those two information sources for us returning a combined SOF.

## Envision

We decided the following during the envision:

* PortReporter information will not be exposed.
* Portcall+ will be the source to get all the PCS/Portcall information
* VesselVoyage will be only AIS based, no external information
* The solution needs to be made in the Teqplay API or at least receivable from the API.

Envision Richard and Darius did on  about this topic.

## Implementation Phase 1

Short term solution, done to give UAB all the needed information to make the decision on their side.

* A new component is made in the API itself, combining the VesselVoyage SOF output we have now and having the PCS information next to this.
* This will not combine any information yet, just having all the information available in 1 endpoint

Expected JSON output of API:

jsonwide760{
"sof": {
// existing VesselVoyage SOF info left as is
}
"pcs": {
"berthVisits": [
{
"location": "berth area id",
"berthEta": "ISO timestamp here",
"berthEtd": "ISO timestamp here",
// other info we have from the PCS
}
]
}
}

## Implementation Phase 2

Long term solution

* Moving this endpoint away from the API and having a separate component which combines the PCS information in the VesselVoyage SOF model, having an extended view for this.

Expected JSON output of API:

jsonwide760{
"sof": {
"berthVisits": [
{
// existing VesselVoyage info
// extension with PCS info
}
],
"anchorVisits": [
{
// existing VesselVoyage info
// extension with PCS info
}
],
...
}
}