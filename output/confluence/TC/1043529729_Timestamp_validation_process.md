---
id: confluence:1043529729
source: confluence
type: page
space: TC
title: Timestamp validation process
author: Francisco Jose Muros Muriano (Unlicensed)
date: '2025-12-12'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1043529729
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1043529729
---
# Timestamp validation process

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1043529729  

## Content

In order to perform the bi-weekly process of the timestamp validation we have to do the following steps:

* Going to the Performance metrics print spreadsheet, and create a new tab with the actual date as a name of the tab

<https://docs.google.com/spreadsheets/d/1pkvPsI5dWVkdGrBLIy_aKGtbqWz_-NE0exwJwif4YFk/edit?gid=1666694039#gid=1666694039>

* Then we have to select 2 visit for each of the ports (NLRTM, SGSIN, USCRP, USHOU, BEANR). The visit should have been finish the same day of the check or the day earlier, but not more than 3 days and should contain meaningful data in order to compare with timeline. After the visits have been selected save the imo with the actual link for vessel voyage for each of the ships

* After the ships are selected, we have to load the visit in timeline in order to see the events and open the SOF of the visit in Vessel voyage to see the times of each event. An easy way to do this is by clicking the three dots icon in the visit and selecting Show in SOF and Show in Timeline directly from the visit page

In SOF we have to click the three dots icon again to open the Time Validator

Here we have to compare the times of the events shown in the time validator with the times present in timeline for the same event

Thing to take into account when comparing the times:

* Sometimes there are more events in timeline than the one shown in Vessel Voyage, in those case we have to click in Create new in order to create a new entry for it, that will result in a missing status.
* Timestamps can differ by 6 minutes over or lower the actual timestamp, if its bigger than that, the the result would be inaccurate and a Jira bug ticket should be created.
* In timeline we events shows their start and end times but we have to double check the ship location and movements to be sure the times for start and end are actually correct, for example, anchor events can be started some minutes before the actual start time by looking a the ship movement.
* There are two endpoints that are not covered by UI that works a a way to report all the entries and check which ones are still valid and which ones are not, with those endpoints we can check extra information for the visits with time validations added as total percentage of accuracy or a list of all visits and the actual status of their events  
    
  `/v2/timestampAccuracy/score`  
  <https://backendvesselvoyage-processing.dev.teqplay.com/swagger-ui/index.html#/processing-timestamp-accuracy-controller/getAccuracyScores>   
  and `/v2/timestampAccuracy/check`  
  <https://backendvesselvoyage-processing.dev.teqplay.com/swagger-ui/index.html#/processing-timestamp-accuracy-controller/checkAccuracyForAllVisits>