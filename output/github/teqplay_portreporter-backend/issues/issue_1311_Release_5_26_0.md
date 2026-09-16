---
id: github:teqplay/portreporter-backend:issue:1311
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1311
title: Release/5.26.0
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1311
labels: []
explicit_links:
- jira:PRA-649
- jira:PRP-1830
- jira:PRP-1896
- jira:PRP-1986
- jira:PRP-2090
- jira:PRP-2092
- jira:PRP-1985
- jira:PRP-1929
- jira:PRP-1895
- jira:PRP-2133
- jira:PRP-2168
- jira:PRP-2167
- jira:PRP-2109
- jira:PRP-2150
- jira:PRP-2121
- jira:PRP-2061
---
# Issue #1311: Release/5.26.0

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1311  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [7f11c3071426...8e65ae521108](https://github.com/teqplay/portreporter-backend/compare/7f11c3071426...8e65ae521108)
**Merge commit:** [8e65ae521108](https://github.com/teqplay/portreporter-backend/commit/8e65ae521108)
**Author:** Joaquin Marquez Bugella
**Reviewers:** 
**Approvers:** 
**Source Branch:** [release/5.26.0](https://github.com/teqplay/portreporter-backend/tree/release/5.26.0)
**Destination Branch:** [master](https://github.com/teqplay/portreporter-backend/tree/master)
**Closed On:** 2023-07-11T11:38:04.472183+00:00
**Status:** MERGED

* Changed some messages.
* Updated messages.
* KTLint format
* Added unit test for the different smartfleet event notification messages.
* Fixed unit tests.
* New snapshot version 5.26.0-SNAPSHOT
* Merged in PRA-649-api-support \(pull request #651\)
    fix\(platform\): don't use / prefix, so the full url is used instead of just the base

    * fix\(platform\): don't use / prefix, so the full url is used instead of just the base
    * PR Feedback
    
    Approved-by: Shan Minh Nguyen

* Merged in feature/PRP-1830\_new\_config\_setting\_to\_start\_from\_minimum\_invoice\_number \(pull request #652\)
    Feature/PRP-1830 new config setting to start from minimum invoice number

    * Added new config setting to start from a minimum invoiceNumber instead of all the way from the start.
    * Set starting number for config property to 0.
    * Refactored code cleaner.
    
    Approved-by: Joaquin Marquez Bugella

* Changed accepted event types we get from smartfleet to also include the PortAtaAtdEvent
* Make sure the unlocode is 5 long and all uppercase
* Merged in feat/PRP-1896/use\_new\_vessel\_voyage\_endpoints \(pull request #654\)
    Feat/PRP-1896/use new vessel voyage endpoints

    * Merge branch 'develop' into feat/PRP-1896/use\_new\_vessel\_voyage\_endpoints
    * PRP-1986 : Take the new skeleton version and make logic leaner.
    * PRP-1896 : remove former capped result.
    * PRP-1896 : reformatting swagger operation annotation.
    * PRP-1896 : upgrade skeleton client to use the actual new VesselVoyageClient methods and add the converter for the VisitVoyage class.
    * PRP-1896 : Adding Swagger details and code comments.
    * PRP-1896 : Renaming the new vesselvoyage endpoint to avoid controller name conflict.
    * PRP-1896 : rename deprecated getTravel to avoid building signature conflicts.
    * PRP-1896 : Using and adapting the new endpoint to get leading visits and previous voyages, combined for the FrontEnd and marking as deprecated the future not used methods.
    
    Approved-by: Wouter Naloop

* Corrected a bug from changes where ADD/REMOVE ship events would not be notified due to not having any ports where this should still sent a notification.
* Removed unused code.
* Added a check on fleet settings if requested user can access the fleet and continue to subscribe to the fleet.
* Merged in feat/PRP-2090/endpoint\_to\_inject\_sf\_events \(pull request #656\)
    PRP-2090 : Enable new endpoint to schedule injected SmartFleet events.

    * PRP-2090 : Enable new endpoint to schedule injected SmartFleet events.
    
    Approved-by: Wouter Naloop

* Merged in feat/PRP-2092/if\_autoUpdateSettings\_autoUpdate\_is\_true\_and\_has\_perCategoryFilter\_is\_set\_it\_cannot\_be\_empty \(pull request #661\)
    PRP-2092 : restrict autoUpdateSettings.perCategoryFilter not empty if set and autoUpdate is true.

    * PRP-2092 : restrict autoUpdateSettings.perCategoryFilter not empty if set and autoUpdate is true.
    * PRP-2092 : Updating changelog.md
    * Merge branch 'develop' into feat/PRP-2092/if\_autoUpdateSettings\_autoUpdate\_is\_true\_and\_has\_perCategoryFilter\_is\_set\_it\_cannot\_be\_empty
    
    Approved-by: Maurice van Veen

* Removed some unnecessary comments
* Feedback from Joaquin implemented.
* Feedback from Joaquin implemented.
* Added some unit tests and fix a bug at same time for SmartFleetSubscriptionLogic.
* Added a unit test to test if an event containing multiple ports will send multiple notifications.
* PRP-2090 : consuming message instead of payload.
* Updating the changelog.
* Merged in fix/smartFleet\_ata\_berth\_events\_to\_get\_port\_matching\_berths\_by\_id \(pull request #663\)
    SmartFleetEvents - Berth events to get the port by berth matching by berth's id instead of berth's uniqueId

    * SmartFleetEvents - Berth events to get the port by berth matching by berth's id instead of berth's uniqueId
    
    Approved-by: Wouter Naloop

* Merged in fix/PRP-1985/PRP-1929/returning\_VesselVoyageVisits\_instead\_of\_VesselVoyage\_Visits \(pull request #662\)
    PRP-1895, PRP-1929 : Returning VesselVoyageVisits instead of VesselVoyage's Visits in two endpoints.

    * PRP-1895, PRP-1929 : Returning VesselVoyageVisits instead of VesselVoyage's Visits in two endpoints.
    * PRP-1895, PRP-1929 : Renaming controller method's name for consistency.
    * Merge branch 'develop' into fix/PRP-1985/PRP-1929/returning\_VesselVoyageVisits\_instead\_of\_VesselVoyage\_Visits
    
    Approved-by: Wouter Naloop

* Merged in feature/PRP-2133/extend\_vessel\_voyage\_endpoints\_with\_matching\_portcallId \(pull request #665\)
    PRP-2133 : Enrich VesselVoyageVisits with matching Portcalls \(when they exist\) and supply with the new endpoint /v1/vesselVoyage/visitsAroundPortcall.

    * PRP-2133 : Enrich VesselVoyageVisits with matching Portcalls \(when they exist\) and supply with the new endpoint /v1/vesselVoyage/visitsAroundPortcall.
    * Merge branch 'develop' into feature/PRP-2133/extend\_vessel\_voyage\_endpoints\_with\_matching\_portcallId
    * PRP-2133 : correcting typo.
    
    Approved-by: Wouter Naloop

* PRP-2168 : Add new endpoint to get a vesselvoyage's voyage by it's id. Also extend VesselVoyageVisit model with previousEntryId and nextEntryId.
* Revert "PRP-2168 : Add new endpoint to get a vesselvoyage's voyage by it's id. Also extend VesselVoyageVisit model with previousEntryId and nextEntryId." They were meant to be in a branch, not direct commit. This reverts commit 93a5f122260ebfd61a45f62d97919313b982dfde.
* Merged in feat/PRP-2168/add\_vesselvoyage\_endpoint\_to\_retrieve\_voyage\_by\_id \(pull request #669\)
    PRP-2168 : Add new endpoint to get a vesselvoyage's voyage by it's id. Also extend VesselVoyageVisit model with previousEntryId and nextEntryId.

    * PRP-2168 : Add new endpoint to get a vesselvoyage's voyage by it's id. Also extend VesselVoyageVisit model with previousEntryId and nextEntryId.
    * PRP-2168 : removing unneeded path variable in new endpoint.
    
    Approved-by: Shan Minh Nguyen

* Bugfix for updating user profile, checking id instead of e-mail now.
* Fixed the unit tests due to a line change.
* Updated tests with some consistency of usage of functions.
* Merged in feat/PRP-2167/endpoint\_to\_get\_most\_recent\_fleet\_still\_containing\_an\_imo \(pull request #672\)
    PRP-2167 : New endpoint to obtain the most recent fleet still containing a given imo.

    * PRP-2167 : New endpoint to obtain the most recent fleet still containing a given imo.
    * PRP-2167 : setting the fallback mechanism correctly.
    * PRP-2167 : Move fallback to controller, remove potential circular dependency and ease out the test.
    * PRP-2167 : Standarizing some naming.
    * PRP-2167 : setting a composed mongo index, renaming some stuff and splitting some functional chain into more understandable steps.
    
    Approved-by: Darius Wattimena

* Merged in fix/PRP-2109/fix\_impersonation\_in\_method\_getUserProfiles\_controller \(pull request #674\)
    Fix/PRP-2109/fix impersonation in method getUserProfiles controller

    * PRP-2109 : Fix impersonation in GET /v1/userProfile \(and add it to GET /v1/userProfile/current\).
    * PRP-2109 : allow Teqplay admins and SmartFleet admins to create fleets for them.
    * Merge branch 'develop' into fix/PRP-2109/fix\_impersonation\_in\_method\_getUserProfiles\_controller
    * PRP-2109 : rename a test method to be English-ish.
    
    Approved-by: Wouter Naloop

* Removing a merge conflict left-over.
* Merged in feat/PRP-2150/extend\_company\_model\_with\_support\_fields \(pull request #675\)
    PRP-2150 : extend Company model with nullable support field.

    * PRP-2150 : extend Company model with nullable support field.
    * Merge branch 'develop' into feat/PRP-2150/extend\_company\_model\_with\_support\_fields
    
    Approved-by: Gavin den Hollander

* Merged in feat/PRP-2121/set\_a\_flag\_to\_disable\_smartfleet\_notifications\_for\_a\_smartfleet\_company\_to\_develop \(pull request #676\)
    Cherry Pick - Merged in feat/PRP-2121/set\_a\_flag\_to\_disable\_smartfleet\_notifications\_for\_a\_smartfleet\_company \(pull request #666\)

    * Merged in feat/PRP-2121/set\_a\_flag\_to\_disable\_smartfleet\_notifications\_for\_a\_smartfleet\_company \(pull request #666\)
    
    PRP-2121 : Set a flag for SmartFleet companies to control SmartFleet events processing and notifications \(not subscription modifications\).

    * PRP-2121 : Set a flag for SmartFleet companies to control SmartFleet events processing and notifications \(not subscription modifications\).
    * Merge branch 'feature/SmartFleetEvents\_Part\_4' into feat/PRP-2121/set\_a\_flag\_to\_disable\_smartfleet\_notifications\_for\_a\_smartfleet\_company
    * PRP-2121 : renaming new fields to the agreed ones with the FE.
    * PRP-2121 : notificationsEnabled flag not updatable by non-admin users.
    * PRP-2121 : Applying feedback from PR: renaming methods and returning more efficient classes.
    
    Approved-by: Wouter Naloop

* When trying to reset invoices, it will now check for portcall aliases beforehand to get the right portcall id.
* Added unit tests and renamed function for clearer understanding and added changelog line.
* Merged in fix/PRP-2133/manage\_portcall\_aliases\_in\_endpoint\_requests\_with\_portcallIds \(pull request #678\)
    PRP-2133 : Manage portcall aliases in endpoint requests with portcallIds.

    * PRP-2133 : Manage portcall aliases in endpoint requests with portcallIds.
    * Merge branch 'develop' into fix/PRP-2133/manage\_portcall\_aliases\_in\_endpoint\_requests\_with\_portcallIds
    
    Approved-by: Shan Minh Nguyen

* Merged in feat/PRP-2061/endpoint\_to\_retrieve\_csi\_ship\_info\_in\_the\_shape\_of\_platform\_model \(pull request #673\)
    PRP-2061 : Replace logic of /v1/ship/search/query by quering csi for static info and platform for dynamic.

    * PRP-2061 : Replace logic of /v1/ship/search/query by quering csi for static info and platform for dynamic.
    * PRP-2061 : Improve csi-platform matching result.
    * Merge branch 'develop' into feat/PRP-2061/endpoint\_to\_retrieve\_csi\_ship\_info\_in\_the\_shape\_of\_platform\_model
    * Merge branch 'develop' into feat/PRP-2061/endpoint\_to\_retrieve\_csi\_ship\_info\_in\_the\_shape\_of\_platform\_model
    * Merge branch 'develop' into feat/PRP-2061/endpoint\_to\_retrieve\_csi\_ship\_info\_in\_the\_shape\_of\_platform\_model
    * PRP-2061 : not querying platform by imo to get the best eta.
    * Merge branch 'develop' into feat/PRP-2061/endpoint\_to\_retrieve\_csi\_ship\_info\_in\_the\_shape\_of\_platform\_model
    * Merge branch 'develop' into feat/PRP-2061/endpoint\_to\_retrieve\_csi\_ship\_info\_in\_the\_shape\_of\_platform\_model
    * PRP-2061 : Taking the feedback into account.
    
    Approved-by: Wouter Naloop


