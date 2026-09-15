---
id: confluence:163315722
source: confluence
type: page
space: TC
title: FlexCTS initial description (functional and technical) - Gavin den Hollander
author: Daan Spikker (Unlicensed)
date: '2023-01-23'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/163315722
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/163315722
---
# FlexCTS initial description (functional and technical) - Gavin den Hollander

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/163315722  

## Content

22 januari 2023

writers: 1st:

**Functional overview** DNV requests functionality bypassing the regular eBDN flow existing in Fuelboss. This is required to help onboard customers that have their own digital eBDN implementation. The currently chosen external system for the implementation is FlexCTS, although it would be beneficial to have a generic implementation with other systems in mind. DNV expects that there might be more integrations with other companies in the future. For simplicity sake we’d refer to FlexCTS when referring to an external eBDN document.Assumptions

* The flow should bypass the (manual) eBDN flow as-is.
* An external system (e.g. FlexCTS) will provide data and a PDF.
* eBDN Signing through Signrequest not applicable; assumes provided documents are completed and signed.

**Functional Requirements:**

* In case there is a FlexCTS document this will be shown in FB. No Manual eBDN is available anymore for this nomination.
* Adding of FlexCTS to nomination is done automatically when available, user not needed to manually add this. (TBD)
* eBDN Signing status nomination is set to completed when FlexCTS document is attached to nomination.

Optional:

1. Data from FlexCTS document should be available for BI Export usage. (TBD)
2. Updating of nomination actuals is happening based on FlexCTS data. (TBD)

**Technical proposal**The following technical overview is a proposal made after hearing the idea for an externally provided eBDN. Since external systems do not have the same unique identifiers as our system we have to match the incoming data to a nomination.

**User experience**

The user will follow the normal nomination flow in fuelboss. When eBDN data is supplied by an external source. the regular eBDN flow will not be shown. The current selector for a template will say “External eBDN source” and only the last stap (currently signing step) will be shown with a list of signed eBDN(s). No additional data nor tables with eBDN data will be shown in the frontend. ***Alternative:*** *Instead of just replacing the eBDN, the user will see a dropdown, just like the eBDN revamp to import from the flexCTS integration. This has as a benefit that the matching doesn't have to be as strict.*

**Expected data flow**The data from the flexCTS will be shared with DNV by “containers' ', every company owns their own “container” on servers owned by DNV. DNV will share the information to Teqplay’s backend through an API call.

**Flow Fuelboss backend Teqplay**

**Required data Teqplay**as a minimum Teqplay will need the following data:

* signed eBDN PDF
* Company Id of the company owning the eBDN (supplier nomination)
* Bunker asset Id could be a pipeline id or a bunkership IMO.
* Receiving ship IMO
* A time unit preferably bunkering start and stop time.

Additional information would be preferred like quantity delivered or location.Please note: Teqplay does not need any additional eBDN information since the PDF replaces the normal eBDN. Any data required for analytics or statistics should be communicated and supplied by DNV explicitly. Meaning, extracting data from within PDF is out-of-scope, due to high-level of complexity and error proneness.

**Models**

Teqplay will need data from DNV, the model used will be as following: { File: Blob bunkerVessel: string? pipelineId: string?

supplierCompanyId: string, receivingShipImo: string, bunkeringStart: date, bunkeringStop: date, eBDN:  {// additional data required by DNV or data available }

}

The Fuelboss backend will need an additional field on the eBDN. “externalProvidedEbdn: bool” and will be false by default. this field can be set to true to allow the frontend to change views.

**Estimated time required: 7 - 12 man days**