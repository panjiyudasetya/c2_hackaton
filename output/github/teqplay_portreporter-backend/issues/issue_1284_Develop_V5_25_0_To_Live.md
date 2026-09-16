---
id: github:teqplay/portreporter-backend:issue:1284
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1284
title: Develop V5.25.0 To Live
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1284
labels: []
explicit_links:
- jira:PRP-1830
- jira:PRP-1865
- jira:PRP-1881
- jira:PRP-1837
- jira:PRP-1838
- jira:PRP-1860
- jira:PRP-598
- jira:PRP-1876
- jira:PRP-1492
- jira:PRP-1902
- jira:PRP-1892
- jira:PRP-1891
- jira:PRP-1981
- jira:PRP-1983
- jira:PRP-1862
- jira:PRP-2001
- jira:PRP-1895
- jira:PRP-1898
- jira:PRP-1929
- jira:PRP-2017
- jira:PRP-2015
- jira:PRP-1932
- jira:PRP-2008
---
# Issue #1284: Develop V5.25.0 To Live

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1284  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [ec939ca2d406...cf485d1c42bb](https://github.com/teqplay/portreporter-backend/compare/ec939ca2d406...cf485d1c42bb)
**Merge commit:** [cf485d1c42bb](https://github.com/teqplay/portreporter-backend/commit/cf485d1c42bb)
**Author:** Joaquin Marquez Bugella
**Reviewers:** 
**Approvers:** 
**Source Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Destination Branch:** [master](https://github.com/teqplay/portreporter-backend/tree/master)
**Closed On:** 2023-06-07T12:14:38.019351+00:00
**Status:** MERGED

* Bugfix a cron for Exact where a cron is stopped when error occurs and extended cron with some other checks for more robustness.
* Updated CHANGELOG.
* New snapshot version 5.25.0-SNAPSHOT
* Feedback from code review processed.
* Changing log level to debug.
* Moved PRP-1830 entry in CHANGELOG to correct version.
* Merged in feat/PRP-1865/better\_control\_and\_logging\_in\_vopak\_portcall\_details\_processing \(pull request #615\)
    PRP-1865 : Enhance control and logging in vopak\_portcall\_details queue processing.

    * PRP-1865 : Enhance control and logging in vopak\_portcall\_details queue processing.
    * PRP-1865 : Moving ProcessResult class to a separate file.
    * ktlint
    * Merge branch 'develop' into feat/PRP-1865/better\_control\_and\_logging\_in\_vopak\_portcall\_details\_processing
    * Updating changelog.md
    * PRP-1865 : Efficiency and cosmetic feedback applied.
    
    Approved-by: Maurice van Veen

* Merged in fix/PRP-1881/handle\_visits\_with\_no\_port\_areas \(pull request #616\)
    PRP-1881 : when processing visits for Vessel Voyage's visit wheel for a portcall, handle visits with no port areas.

    * PRP-1881 : when processing visits for Vessel Voyage's visit wheel for a portcall, handle visits with no port areas.
    * PRP-1881 : Setting a fallback chain to obtaining port information \(name and times\) when processing Visits in a VesselVoyage's journey.
    * Merge branch 'develop' into fix/PRP-1881/handle\_visits\_with\_no\_port\_areas
    * PRP-1881 : required changes to use Spring cache internally in the same class.
    * PRP-1881 : using self properly.
    * PRP-1881 : not using cache for poma port internally because it introduces a circular dependency.
    * PRP-1881 : also removing it from the application.properties.
    
    Approved-by: Leon Joosse Approved-by: Shan Minh Nguyen

* Merged in feat/PRP-1837/port\_name\_in\_smartfleet\_notification\_message \(pull request #617\)
    Feat/PRP-1837/port name in smartfleet notification message

    * Merge branch 'develop' into feat/PRP-1837/port\_name\_in\_smartfleet\_notification\_message
    * PRP-1837 : Better formatting.
    * PRP-1837 : Raise logs from WARNING to SEVERE when port information is not available when it should.
    * PRP-1837 : Including port name \(display name\) and fallback cases in Smartfleet notifications.
    
    Approved-by: Maurice van Veen

* Merged in feat/PRP-1838/notifications\_endpoint\_to\_return\_search\_results\_with\_metadata \(pull request #618\)
    PRP-1838 : new endpoint to search notifications with metadata \(for SmartFleet notifications\).

    * PRP-1838 : new endpoint to search notifications with metadata \(for SmartFleet notifications\).
    * PRP-1838 : correct changelog.md
    * PRP-1838 : correcting typos and setting a set to list.
    * PRP-1838 : correcting typos.
    
    Approved-by: Maurice van Veen

* Merged in feat/PRP-1860/smartfleet\_add\_remove\_events\_adaptions \(pull request #619\)
    Feat/PRP-1860/smartfleet add remove events adaptions

    * PRP-1860 : Adapting for receiving add and remove events from the same message.
    * PRP-1860 : Additional fix and adapting UnitTests.
    * PRP-1860 : Adding unitTest for ADD to and REMOVE from fleet SmartFleet events.
    * PRP-1860 : just change the order of methods in SmartFleetEventLogic for peace of mind.
    
    Approved-by: Maurice van Veen

* PRP-1860 : direct fix for add/remove ship message format.
* PRP-1860 : mock inserts on smartFleetEventDataSource in SmartFleetEventLogicTest just to remove an irrelevant but ugly exception.
* Merged in feature/PRP-598\_refactor\_platform\_ship\_connection\_to\_csi \(pull request #612\)
    PRP-598 Setup changes for initial review.

    * PRP-598 : renaming objects for consistency.
    * PRP-598: Unify PortReporter's Ship constructor from CSI's ShipRegisterInfo.
    * PRP-598 : Remove forgotten commented constructor.
    * PRP-598 : Be consistent with mmsi as well in the ship controller.
    * PRP-598 : Ship.shipType from ShipRegisterInfo.administration.shipCat \(from Portcalllogic.kt\) and some clean up.
    * Merge branch 'develop' into feature/PRP-598\_refactor\_platform\_ship\_connection\_to\_csi
    * Changed platform version to target snapshop version to test push notifications.
    * Reverting platform version set.
    * Merge branch 'develop' into feature/PRP-598\_refactor\_platform\_ship\_connection\_to\_csi
    * Merge branch 'develop' into feature/PRP-598\_refactor\_platform\_ship\_connection\_to\_csi
    
    Approved-by: Maurice van Veen

* PRP-1860 : SmartFleetEvent.shouldIgnore\(\) had a flaw, but just for letting saving the message as not ignored. Processing worked fine.
* Merged in feat/PRP-1865/send\_slack\_message\_when\_something\_is\_wrong \(pull request #620\)
    PRP-1865 : Send slack message via logs when any vopakPortcallDetail don't process properly.

    * PRP-1865 : Send slack message via logs when any vopakPortcallDetail don't process properly.
    * Merged develop into feat/PRP-1865/send\_slack\_message\_when\_something\_is\_wrong
    * PRP-1865 : modify portcall's agent remark.
    * PRP-1860 - Applying feedback changes.
    
    Approved-by: Maurice van Veen

* Merged in feature/PRP-1830\_testing\_bugfixes\_for\_invoices \(pull request #623\)
    Testing some bugfix for Cron Exact.

    * added stacktrace
    * Testing some bugfix.
    
    Approved-by: Joaquin Marquez Bugella

* Merged in feat/PRP-1838/include\_fleetName\_in\_notification\_when\_SFEvent \(pull request #625\)
    PRP-1838 : Removing unneeded metadata endpoint. Including searchPattern in the new field for searching. Include the fleet field in the Notification model.

    * PRP-1838 : Removing unneeded metadata endpoint. Including searchPattern in the new field for searching. Include the fleet field in the Notification model.
    
    Approved-by: Joost Laurman

* Merged in feat/PRP-1876/extend\_SmartFleetSubscriptionDetails\_with\_filterByPorts \(pull request #624\)
    feat/PRP-1876/extend SmartFleetSubscriptionDetails with filterByPorts

    * Merge branch 'develop' into feat/PRP-1876/extend\_SmartFleetSubscriptionDetails\_with\_filterByPorts
    * Merge branch 'develop' into feat/PRP-1876/extend\_SmartFleetSubscriptionDetails\_with\_filterByPorts
    * PRP-1876 : Obtaining ports from Berth and Port's events with fallbacks \(in case of missing them\). Adding unitTests for port filtering scenarios. Fix a SmartFleetSubscritionDetails scenario \(not able to remove subscriptions when no mediums\).
    * WIP - missing obtaining the port from the event and adapting endpoints to manage the ports extension.
    
    Approved-by: Maurice van Veen

* Merged in feature/PRP-1492\_added\_timestamp\_check\_for\_pilotavailability\_events \(pull request #626\)
    Feature/PRP-1492 added timestamp check for pilotavailability events

    * Added a timestamp to the existing equals check when comparing PilotAvailabilityChange objects.
    * Fixed a unit test, filled in timestamp to make unit test work as intended.
    * Merge branch 'develop' into feature/PRP-1492\_added\_timestamp\_check\_for\_pilotavailability\_events
    
    Approved-by: Maurice van Veen

* Merged in fix/PRP-1902/restore\_ship\_in\_portcall\_notifications\_and\_include\_it\_in\_smartfleet\_ones \(pull request #627\)
    Fix/PRP-1902/restore ship in portcall notifications and include it in smartfleet ones

    * PRP-1902 : Including ship in notifications, adapt and extend unitTest.
    * PRP-1902 : some code cleaning to improve readability.
    * Merge branch 'develop' into fix/PRP-1902/restore\_ship\_in\_portcall\_notifications\_and\_include\_it\_in\_smartfleet\_ones
    
    Approved-by: Joost Laurman

* PRP-1838 : Copied Notification doesn't copy \_id.
* Reverted some changes and make exception for port NLRTM for pilotAvailability events.
* Added a test to check if non NLRTM port pilotAvailability events will be checked or not.
* Merged in fix/PRP-1892/get\_dashboard\_column\_configuration\_by\_fleetId \(pull request #630\)
    PRP-1892 : Getting the correct fallback for Dashboard Configuration when fleet is not provided or not found.

    * PRP-1892 : Getting the correct fallback for Dashboard Configuration when fleet is not provided or not found.
    
    Approved-by: Wouter Naloop

* Merged in feat/PRP-1891/enable\_endpoint\_to\_get\_berthMapped\_ports \(pull request #629\)
    PRP-1891 : Enabling endpoint in static v2 controller to get list of berth mapped ports.

    * PRP-1891 : Enabling endpoint in static v2 controller to get list of berth mapped ports.
    * Merge branch 'develop' into feat/PRP-1891/enable\_endpoint\_to\_get\_berthMapped\_ports
    * PRP-1891 : Improving the api operation information.
    * Merge branch 'develop' into feat/PRP-1891/enable\_endpoint\_to\_get\_berthMapped\_ports
    
    Approved-by: Wouter Naloop

* Merged in feat/PRP-1981/endpoint\_to\_get\_smartfleet\_fleet\_metadata \(pull request #631\)
    PRP-1981 : New endpoint to get smartfleet subscriptions by user \(with metadata\).

    * PRP-1981 : New endpoint to get smartfleet subscriptions by user \(with metadata\).
    * PRP-1981 : Updating constructor in UnitTest.
    * Merge branch 'develop' into feat/PRP-1981/endpoint\_to\_get\_smartfleet\_fleet\_metadata
    
    Approved-by: Wouter Naloop

* Merged in fix/PRP-1983/smartfleet\_subscription\_should\_subscribe\_for\_logged\_in\_user\_or\_impersonated \(pull request #633\)
    PRP-1983 : Getting a smartfleet subscription takes into account the requesting user \(logged-in or impersonated\).

    * PRP-1983 : Getting a smartfleet subscription takes into account the requesting user \(logged-in or impersonated\).
    * PRP-1983 : Some code adaptation.
    * Merge branch 'develop' into fix/PRP-1983/smartfleet\_subscription\_should\_subscribe\_for\_logged\_in\_user\_or\_impersonated
    
    Approved-by: Wouter Naloop

* Merged in feat/PRP-1862/update\_smartfleet\_api\_library\_version\_to\_get\_model\_updates \(pull request #634\)
    Feat/PRP-1862/update smartfleet api library version to get model updates

    * PRP-1862 : Update Smartfleet version to get newest data models and adapt unitTests.
    * PRP-1862 : Modify the SF-Foo classes, define converter and adapt unitTests.
    * PRP-1862 : Change SFBerthArea.convert's parameters format.
    
    Approved-by: Wouter Naloop Approved-by: Maurice van Veen

* Merged in feat/PRP-2001/SFEvents\_list\_to\_inform\_if\_they\_need\_port\_filtering \(pull request #637\)
    PRP-2001: Add and use of hasPortFiltering field in SmartFleetEventType.

    * PRP-2001: Add and use of hasPortFiltering field in SmartFleetEventType.
    * PRP-2001 : Remove forgotten commented code.
    
    Approved-by: Joost Laurman

* Setting snapshot prefix to versions on dev.
* Merged in feat/PRP-1895/PRP-1898/extend\_vessel\_voyage\_endpoints \(pull request #638\)
    PRP-1895 \+ PRP-1898 : Add VesselVoyage Endpoints to get Visit or Voyage by their Id. PortReporter mirrored classes for VesselVoyage.

    * PRP-1895 \+ PRP-1898 : Add VesselVoyage Endpoints to get Visit or Voyage by their Id. PortReporter mirrored classes for VesselVoyage.
    * Merge branch 'develop' into feat/PRP-1895/PRP-1898/extend\_vessel\_voyage\_endpoints
    * PRP-1895 \+ PRP-1898 : Removing forgotten comment, adding a forgotten log and being more specific with Exception case.
    * Merge branch 'develop' into feat/PRP-1895/PRP-1898/extend\_vessel\_voyage\_endpoints
    
    Approved-by: Joost Laurman

* Merged in feat/PRP-1929/vessel\_voyage\_visits\_history\_endpoint \(pull request #639\)
    PRP-1929 : Extend VesselVoyage endpoints with ship visits history by imo.

    * PRP-1929 : Extend VesselVoyage endpoints with ship visits history by imo.
    
    Approved-by: Maurice van Veen

* Merged in feat/PRP-2017/return\_smartfleet\_subscribableEventTypes\_categorized \(pull request #640\)
    PRP-2017 : Return subscribable SmartFleetEvents in categories.

    * PRP-2017 : Return subscribable SmartFleetEvents in categories.
    * PRP-2017 : SmartFleetCategorization's field 'categoryName' to 'category'.
    
    Approved-by: Maurice van Veen

* Merged in feat/PRP-2015/implement\_SF\_Notification\_for\_ATA\_80\_nautical\_mile \(pull request #641\)
    PRP-2015 : Implement SmartFleet 80NM event processing, subscription and notification.

    * PRP-2015 : Implement SmartFleet 80NM event processing, subscription and notification.
    * Merge branch 'develop' into feat/PRP-2015/implement\_SF\_Notification\_for\_ATA\_80\_nautical\_mile
    
    Approved-by: Maurice van Veen

* Merged in fix/PRP-1981/get\_fleets\_by\_user\_to\_use\_the\_correct\_endpoint\_upon\_user\_admin\_role \(pull request #644\)
    PRP-1981 : call the correct smartfleet endpoint to get the fleets depending on the user role \(admin or regular\).

    * PRP-1981 : call the correct smartfleet endpoint to get the fleets depending on the user role \(admin or regular\).
    
    Approved-by: Joost Laurman

* devfix: notification search should be accessible now by smartfleet users \(admin and regular users\).
* Merged in fix/PRP-1983/remove\_unused\_smartfleetsubscription\_endpoints \(pull request #635\)
    Fix/PRP-1983/remove unused smartfleetsubscription endpoints

    * PRP-1983 : removing unused endpoints and modifying the signature of some.
    * PRP-1983 : Replacing RequestMapping by the actual PostMapping and PutMapping.
    * Merge branch 'develop' into fix/PRP-1983/remove\_unused\_smartfleetsubscription\_endpoints
    * Merge branch 'develop' into fix/PRP-1983/remove\_unused\_smartfleetsubscription\_endpoints
    
    Approved-by: Wouter Naloop

* Merged in feature/PRP-1932\_added\_anchor\_events \(pull request #642\)
    Feature/PRP-1932 added anchor events

    * Added anchor events with message formats.
    * Removed testing code.
    * Removed more testing code.
    * Removed some comma's that somehow got added by IDE.
    * Fixed getPortSuffix function, had incorrect check.
    * Merge branch 'develop' into feature/PRP-1932\_added\_anchor\_events
    * PRP-1932 : adding new events in the subscribable categorized events.
    * PRP-1932 : Changelog update.
    
    Approved-by: Joaquin Marquez Bugella

* Merged in fix/PRP-2015/port\_obtention\_in\_notification\_message\_of\_80NM\_SFEvent \(pull request #645\)
    PRP-2015 : 80NM notification message failed to obtain the port.

    * PRP-2015 : 80NM notification message failed to obtain the port.
    * PRP-2015 : special treatment of rtm custom port.
    * Merge branch 'develop' into fix/PRP-2015/port\_obtention\_in\_notification\_message\_of\_80NM\_SFEvent
    * PRP-2015 : fix getPortSuffix\(unlocode\) private method.
    * Merge branch 'develop' into fix/PRP-2015/port\_obtention\_in\_notification\_message\_of\_80NM\_SFEvent
    
    Approved-by: Wouter Naloop

* Merged in feat/make\_SmartFleetMessageFormat\_leaner \(pull request #646\)
    SmartFleetEvents : Make the SmartFleetMessageFormat leaner around the event's port.

    * SmartFleetEvents : Make the SmartFleetMessageFormat leaner around the event's port.
    * SmartFleetEvents : Avoid calling poma.getPortsByUnlocode\(\) with empty unlocode list.
    
    Approved-by: Shan Minh Nguyen

* Made error logging for Exact better by having the iterations configurable.
* Reset limit back to previous.
* Merged in feat/PRP-2008/add\_optional\_flag\_to\_get\_only\_SFfleet\_settings \(pull request #648\)
    PRP-2008 : Add new Endpoint to get the fleet settings and internally rename getFleet to getFleetVoyages for consistency.

    * PRP-2008 : Add new Endpoint to get the fleet settings and internally rename getFleet to getFleetVoyages for consistency.
    * PRP-2008 : correcting endpoint v2 to v3.
    * PRP-2008 : correcting endpoint path
    
    Approved-by: Maurice van Veen

* Renamed variable for easier understanding.
* Removed some code.
* Updated log to reflect the correct config property name.

