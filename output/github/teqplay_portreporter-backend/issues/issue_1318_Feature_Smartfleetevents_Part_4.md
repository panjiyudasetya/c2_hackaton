---
id: github:teqplay/portreporter-backend:issue:1318
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1318
title: Feature/Smartfleetevents Part 4
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1318
labels: []
explicit_links: []
---
# Issue #1318: Feature/Smartfleetevents Part 4

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1318  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [ea9a31472c60...8347eac0ae4d](https://github.com/teqplay/portreporter-backend/compare/ea9a31472c60...8347eac0ae4d)
**Merge commit:** [8347eac0ae4d](https://github.com/teqplay/portreporter-backend/commit/8347eac0ae4d)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Wouter Naloop, Shan Minh Nguyen
**Approvers:** 
**Source Branch:** [feature/SmartFleetEvents_Part_4](https://github.com/teqplay/portreporter-backend/tree/feature/SmartFleetEvents_Part_4)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2023-07-24T15:39:26.243450+00:00
**Status:** MERGED

Summary:

* PRP-1993: Smartfleet subscription profiles
* PRP-1996: overwrite users fleet subscriptions based on subscriptionProfile
* PRP-1933 : Implementing first version of SmartFleet event Pilot Boarding Place
* PRP-2042: cleanup fleets and subscriptions when user or company is deleted

---

Automatic merge commit diff summary:

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
* Merged in feat/PRP-1993/extend\_smartfleet\_subscription\_profile\_controller\_with\_endpoint\_by\_companyId \(pull request #681\)

    PRP-1993 : Replace 'get subscriptionProfiles by user' by 'get subscriptionProfiles by companyId'. Replace Patch by Put endpoint. Enforce unitTests and improve existing SmartFleetSubscriptionProfileLogic.



    * PRP-1993 : Replace 'get subscriptionProfiles by user' by 'get subscriptionProfiles by companyId'. Replace Patch by Put endpoint. Enforce unitTests and improve existing SmartFleetSubscriptionProfileLogic.
    * Merge branch 'feature/SmartFleetEvents\_Part\_4' into feat/PRP-1993/extend\_smartfleet\_subscription\_profile\_controller\_with\_endpoint\_by\_companyId
    * Merged in feature/PRP-1993\_bugfix\_fleet\_not\_deleted\_alongside\_user \(pull request #683\)
    

    Bugfix where user fleets were not deleted alongside user when trying to delete a user.



    * Bugfix where user fleets were not deleted alongside user when trying to delete a user.
    

    Approved-by: Joaquin Marquez Bugella



    Approved-by: Shan Minh Nguyen




