---
id: github:teqplay/portreporter-backend:issue:1328
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1328
title: Live Release V5.27.0 2023-09-05
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1328
labels: []
explicit_links:
- jira:PRP-1993
- jira:PRP-1996
- jira:PRP-1933
- jira:PRP-2121
- jira:PRP-2042
- jira:PRP-1536
---
# Issue #1328: Live Release V5.27.0 2023-09-05

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1328  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [f3edf4a4542e...55e8fcec2e15](https://github.com/teqplay/portreporter-backend/compare/f3edf4a4542e...55e8fcec2e15)
**Merge commit:** [55e8fcec2e15](https://github.com/teqplay/portreporter-backend/commit/55e8fcec2e15)
**Author:** Joaquin Marquez Bugella
**Reviewers:** 
**Approvers:** 
**Source Branch:** [release/5.27.0](https://github.com/teqplay/portreporter-backend/tree/release/5.27.0)
**Destination Branch:** [master](https://github.com/teqplay/portreporter-backend/tree/master)
**Closed On:** 2023-09-05T09:55:51.011556+00:00
**Status:** MERGED

* Add Changelog header.
* Merged in feat/PRP-1993/new\_basic\_setup\_for\_smartfleet\_subscription\_profiles \(pull request #649\)
    Feat/PRP-1993/new basic setup for smartfleet subscription profiles

    * PRP-1993 : Create basic set-up \(datasource, logic and controller\) \+ unitTests to handle SmartFleetSubscriptionProfiles.
    * PRP-1993 : Add Changelog line.
    * PRP-1993 : Correct roles allowed for delete subscriptionProfile.
    
    Approved-by: Shan Minh Nguyen

* Merged in feat/PRP-1996/overwrite\_users\_fleet\_subscriptions\_based\_on\_subscriptionProfile \(pull request #659\)
    PRP-1996 : overwrite users fleet subscriptions based on subscriptionProfile.

    * PRP-1996 : overwrite users fleet subscriptions based on subscriptionProfile.
    
    Approved-by: Shan Minh Nguyen

* Merged in feat/PRP-1933/implement\_eta\_pilot\_boarding\_place \(pull request #657\)
    PRP-1933 : Implementing first version of SmartFleet event Pilot Boarding Place.

    * PRP-1933 : Implementing first version of SmartFleet event Pilot Boarding Place.
    * PRP-1933 : forgotten severe log message.
    * Merge branch 'feature/SmartFleetEvents\_Part\_4' into feat/PRP-1933/implement\_eta\_pilot\_boarding\_place
    
    Approved-by: Wouter Naloop

* Correcting changelog.md
* Merged in feat/PRP-2121/set\_a\_flag\_to\_disable\_smartfleet\_notifications\_for\_a\_smartfleet\_company \(pull request #666\)
    PRP-2121 : Set a flag for SmartFleet companies to control SmartFleet events processing and notifications \(not subscription modifications\).

    * PRP-2121 : Set a flag for SmartFleet companies to control SmartFleet events processing and notifications \(not subscription modifications\).
    * Merge branch 'feature/SmartFleetEvents\_Part\_4' into feat/PRP-2121/set\_a\_flag\_to\_disable\_smartfleet\_notifications\_for\_a\_smartfleet\_company
    * PRP-2121 : renaming new fields to the agreed ones with the FE.
    * PRP-2121 : notificationsEnabled flag not updatable by non-admin users.
    * PRP-2121 : Applying feedback from PR: renaming methods and returning more efficient classes.
    
    Approved-by: Wouter Naloop

* New snapshot version 5.27.0-SNAPSHOT
* Merged in feature/PRP-2042\_cleanup\_fleets\_and\_subscriptions\_when\_user\_or\_company\_is\_deleted \(pull request #671\)
    Feature/PRP-2042 cleanup fleets and subscriptions when user or company is deleted

    * Some fixes from feedback Joaquin.
    * Fix conflicts.
    * Commit of shame. KTLint.
    * PRP-2042 : Additional changes to consider deleting in cascade.
    * Merged SF part 4 with branche and setup baseline to continue implementing deleting company subscription profiles as a last result.
    * KTLint.
    * Merged SF part 4 branche and fixed conflicts.
    * Added deletion of sfSubscriptionProfile when deleting a company.
    * Merged SF part 4 branch and fixed conflicts.
    * KTLint commit of shame.
    
    Approved-by: Wouter Naloop

* Removed lines of deleting users linked to company when deleting a company.
* Added timezone to userProfile and updated corresponding functions to make sure endpoints take the timezone into account and updated unitTests.
* Removed unused variable but somehow KTLint didn't pick it up.
* Merged in feat/PRP-1993/extend\_smartfleet\_subscription\_profile\_controller\_with\_endpoint\_by\_companyId \(pull request #681\)
    PRP-1993 : Replace 'get subscriptionProfiles by user' by 'get subscriptionProfiles by companyId'. Replace Patch by Put endpoint. Enforce unitTests and improve existing SmartFleetSubscriptionProfileLogic.

    * PRP-1993 : Replace 'get subscriptionProfiles by user' by 'get subscriptionProfiles by companyId'. Replace Patch by Put endpoint. Enforce unitTests and improve existing SmartFleetSubscriptionProfileLogic.
    * Merge branch 'feature/SmartFleetEvents\_Part\_4' into feat/PRP-1993/extend\_smartfleet\_subscription\_profile\_controller\_with\_endpoint\_by\_companyId
    * Merged in feature/PRP-1993\_bugfix\_fleet\_not\_deleted\_alongside\_user \(pull request #683\)
    
    Bugfix where user fleets were not deleted alongside user when trying to delete a user.

    * Bugfix where user fleets were not deleted alongside user when trying to delete a user.
    
    Approved-by: Joaquin Marquez Bugella

    Approved-by: Shan Minh Nguyen

* Added note to multiple subscriptions when subscribing
* KTLint
* Some extra quick unit tests to check if the quick bugfix is working and the correct arguments are supplied.
* KTLint commit of shame.
* Refactored some platform ship info objects in SF endpoints to retrieve CSI static ship info as a base with platform for dynamic info.
* Reworked some functions, leaving some fallbacks to easily revert the endpoint changes.
* CHANGELOG.md
* PRP-1536 : Making userProfile.admin field read-only and set the value according to the roles.
* PRP-1536 : Adding unitTests and adapting existing ones.
* Reworked code to fetch by csi imo first then filter by platform mmsi and combining info together like suggested.
* Including shipLogic in PortcalLogic.
* Making logic call for altering subscriptions synchronized.
* Some extra bugfixes to return the best possible results.
* Merged in feat/PRP-1993/inforce\_companyId\_not\_to\_be\_empty\_for\_SmartFleetSubscriptionProfile\_creation \(pull request #689\)
    PRP-1993 : inforce companyId not to be empty for SmartFleetSubscriptionProfile creation.

    * PRP-1993 : inforce companyId not to be empty for SmartFleetSubscriptionProfile creation.
    * Merged develop into feat/PRP-1993/inforce\_companyId\_not\_to\_be\_empty\_for\_SmartFleetSubscriptionProfile\_creation
    
    Approved-by: Shan Minh Nguyen

* Forgot to add a distinct for consistency.
* Fixes from feedback for synchronization.
* Updated usages of the alterSubscriptions to go with the synchronization method.
* Added a unit test with coroutines.
* KTLint commit of shame.
* Replaced synchronized lock with XSync implementation.
* Fixed feedback from Joaquin and updated test with better asynchronization test.
* Set filename with dates for invoices export.
* KTLint commit of shame.
* Added boolean export to csv option to allow for non csv export in plain text.
* Removed some code.
* Removed some unused
* Using util function for date to string conversion in invoices/csv.
* Reformatted code.
* Refactored some code and removed unused code.
* Added a flag to a smartfleet company to determine a custom zooming behaviour for a user.
* Updating Changelog.md
* Updating the changelog.md.
* Live release v5.27.0 2023-09-05 \(version number changes\)

