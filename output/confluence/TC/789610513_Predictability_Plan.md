---
id: confluence:789610513
source: confluence
type: page
space: TC
title: Predictability Plan
author: Kevin Kencana
date: '2025-07-07'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/789610513
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/789610513
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/705233041/3.+Backfilling+Teqplay+Data+Warehouse?atlOrigin=eyJpIjoiNWE5MWNkNTliYmM1NDNkYjk1MzZmZGIxMmVlZTRjYWQiLCJwIjoiYyJ9
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/708345857/4.+Backfilling+POMA+and+CSI+Data?atlOrigin=eyJpIjoiY2IwYTFmOGZiYzI3NGFlMWI5YWEwMDNjMTFiZGI4OGEiLCJwIjoiYyJ9
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/734396427/5.+Cleanup+and+Reload+Visits+on+Teqplay+Datamart?atlOrigin=eyJpIjoiOGI1Yzc5YWQ4NzI5NGI4ZDllOWUwYzZmYWNiYTA0N2QiLCJwIjoiYyJ9
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/769523719/DWH+SOF+completeness+checks?atlOrigin=eyJpIjoiMWI5MjIzNGI1YTlhNDMxZGE3ZDBiMTVjNTRmMTk5NzQiLCJwIjoiYyJ9
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/769523719/DWH+SOF+completeness+checks?atlOrigin=eyJpIjoiYjM0YmY1YzdiYmFiNDdlYmI5NTgyNGUyZGQ4ZDE4ZWQiLCJwIjoiYyJ9
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/folder/777682953?atlOrigin=eyJpIjoiMmYzODdkNGQ4NzFlNDdmNWJlYTViY2RhNWJhNTZmNzYiLCJwIjoiYyJ9
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/folder/774504499?atlOrigin=eyJpIjoiMTViMjY2YjMzMDQzNGRmOGIyMzUzZGNhOTA2YThhMTEiLCJwIjoiYyJ9
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/folder/779812880?atlOrigin=eyJpIjoiZWViYjBkOTMwMTE0NDIwMmE2MzViNzc4OTRhNDY2NGIiLCJwIjoiYyJ9
---
# Predictability Plan

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/789610513  

## Content

Context Mapping and Data Validation Team

This is a step-by-step guide when starting a new port mapping until the validation process in PowerBI.

# **Step 1: POMA Mapping (2 - 10 Hours)**

When mapping a new port, we often already have a pretty good starting point from external sources. Instead of making new mappings, we modify the external mapping based on port information that we can find on the internet.

Where do we usually check for port information? It’s usually:

* Official port information and map on their website

* Google Maps

We add terminals and berths and add their information. The most important ones are:

* Terminal/Berth Name
* Cargo Type
* Vessel Types Allowed

Here’s the completed mapping done by us.

After terminals and berths have been mapped, we add in Anchorages and Pilot Boarding Places. Most ports don’t have precise information on how large the areas are, so we look at past voyages and try to find any visits that had an anchor event and pilot encounter. We then map the areas to cover every instance of anchor and pilot event we found.

The context mapping is done! The time needed may vary a lot. Bigger ports like the one above takes about 8-10 hours. Smaller ports with less than 5 terminals will take about 2 hours.

---

# **Step 2: Run PTO Report (5-11 hours)**

To generate a PTO report for our newly mapped port, there are a few steps to be done in our new architecture.

1. **Recalculate VesselVoyage (1-1.5 hours)**

We normally validate a year’s worth of visits so here we select the date from Jan 1, 2024 - Jan 1, 2025. This usually takes an hour of waiting.

2. **Run Airflow (4-10 hours)**

After the recalculation’s done, we move to Airflow to extract SOF data as well as the mapping done by us in POMA and CSI and transform them into fact and dimension tables. Full details on what is done in Airflow can be viewed here:

* <https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/705233041/3.+Backfilling+Teqplay+Data+Warehouse?atlOrigin=eyJpIjoiNWE5MWNkNTliYmM1NDNkYjk1MzZmZGIxMmVlZTRjYWQiLCJwIjoiYyJ9>
* <https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/708345857/4.+Backfilling+POMA+and+CSI+Data?atlOrigin=eyJpIjoiY2IwYTFmOGZiYzI3NGFlMWI5YWEwMDNjMTFiZGI4OGEiLCJwIjoiYyJ9>
* <https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/734396427/5.+Cleanup+and+Reload+Visits+on+Teqplay+Datamart?atlOrigin=eyJpIjoiOGI1Yzc5YWQ4NzI5NGI4ZDllOWUwYzZmYWNiYTA0N2QiLCJwIjoiYyJ9>

The output at the end is that our data mart is filled in with visits of our selected port and is ready to be validated. The time may vary, but generally we wait for half a working day (~4 hours) to fill in the data mart. For big ports with lots of visit like GBLON, we’ve run it on Airflow and it took 10 hours to fill the data mart, so let’s put that as the upper threshold of our estimation.

---

# **Step 3: Data Validation in PowerBI (~6 hours)**

We’ve reached the longest process, data validation. Here we have our data validation dashboard that’s been well-optimized to detect outlier visits. We have a guideline to follow when doing the validation which we’ll go through.

**a. Missing Ship Information in CSI (~1 hour)**

We have a table of all ships that visited the port within the time period that has missing information in CSI. We go over them and add the missing information by looking for that information on the internet, most reliably on Marinetraffic. The time required varies wildly depending on how many ships have missing information, but on average it’s around an hour.

**b. Wrong Cargo Type for Berths (~10 minutes)**

We have the number of ships visiting each berth and group the count based on ship classification. That way we can easily identify any miscategorized berths and terminals. This step doesn’t take much time.

**c. Longest and Shortest Anchor Duration (~1 hour)**

We look the 10 longest and 10 shortest durations for anchor events as they’re the most likely to have issues. We’ve improved the dashboard to provide easier ways to detect anomalies, mainly visits with Waiting Outside Port > Anchor Duration. Those are usually either anchoring in an unmapped area or mapping slightly outside of a mapped anchor area. Checking it would take around 1 hour.

**d. Longest and Shortest Berth Stay Duration (~1 hour)**

Similar to the anchor duration check, we look at the 10 longest and shortest berth stay duration. Mistakes that are often found in this step are jittering, double berth visits (one visit is counted as two), and berths that need a length/width change. This also roughly takes about an hour.

**e. Highest Steaming In and Steaming Out (~1 hour)**

A recently added check we have in the dashboard. High steaming in or steaming out duration usually indicates a missing berth visit. We never agreed on the number of visits needed to be checked, but we also roughly limit the check to an hour as there might be too many visits with this problem.

**f. Shifting Check (~1 hour)**

We do some checks on voyages with multiple berth and/or terminal visits. Similarly to steaming in and out, we don’t have an agreed number of visits to check, but we do look at the ones with weirdly high shifting durations. We also limit it to around an hour of checking.

**g. Random Ship Checking (~1 hour)**

At the end, we do a random sample check of at least 10 ships. We’ve added a timeline bar at the bottom to make it easy and quick to do a simple duration check. If everything’s perfectly aligned/symmetric, that means it’s most likely correct. This also takes around an hour of checking.

---

# **Step 4: Validation loop (2 x (11-17) hours)**

After the first round of validation and fixing any context mapping related issues found, we need to do it two more times. This is because each check mainly focuses on one of the three main cargo types of vessels, which are Container, Wetbulk, and Drybulk. That means recalculating vesselvoyage, running a new PTO report, then doing the whole validation steps again twice.

---

# **Step 5: Cross-validation (~5 + 3 hours)**

Once one person has done the three validations, then the other person in the context mapping team will check their work. That means they’ll re-run another report after all the changes have been mad, quickly go over through the dashboard and see if there’re any unnoticed errors by them. Then, they’ll fill in this spreadsheet below with all the issues found by them and the original checker.  
 <https://docs.google.com/spreadsheets/d/1ol5ySXlJrFKRsuBCFduRxA-xsINbvp19cv82Q7isO7Y/edit?gid=743392294#gid=743392294>

---

# **Total Maximum Time Estimation: 40-65 hours.**

Disclaimer: This estimation is assuming we run the recalculation and PTO report all during working hours. We often run it before signing off so it would be done by the next morning. Since we do it a total of 4 times, the minimum time estimation becomes **20 - 30 hours.**

Predictability check per Step:

| **Step** | **Question** | **How to Measure** |
| --- | --- | --- |
| POMA Mapping | \*Time needed for future ports, is it within our predicted estimation?  (I’m just spewing what I’m thinking, to be refined later)  How much time does it take to map a port with X amount of berths and terminals? | Time spent on mapping a port. Count number of berths and terminals |
| VesselVoyage recalculation | What is the percentage of failure for a recalculation? Is it often? Are there some ports that the error occurs often on?  How long does it take for VV to recalculate a port with X amount of berths and terminals? | Success rate      Recalculation duration per port  Number of visits |
| PTO/Airflow | Success rate of DAGs? Are certain ports prone to more failure than other ports?    Are the fact and dimension tables always filled in properly? | Success rate?      Completeness %  <https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/769523719/DWH+SOF+completeness+checks?atlOrigin=eyJpIjoiMWI5MjIzNGI1YTlhNDMxZGE3ZDBiMTVjNTRmMTk5NzQiLCJwIjoiYyJ9> |
| Data Validation Loop | How long does it take for small ports, big ports? Are there any correlations or do every port take about 6 hours? | Time spent on validation per port |
| Cross Validation | Number of issues found before correlates to how long cross validating will take? | Time spent on validation per port |

Quality Checks per Step:

| **Step** | **Definition of Quality** | **How to Check** |
| --- | --- | --- |
| POMA Mapping | Correctly Mapped Berths, Terminals, Anchorage, Pilot Stations    Correct Berth/Terminal Cargo Type | A Port must have at least 1 terminal, berth, anchor area, and pilot boarding place    Percentage of visiting ship’s cargo type > *X*% (Done in Validation) |
| VesselVoyage recalc | Complete Visits        Valid Visits                  Consistency of Recalculation | Events must have start and end time  A voyage has all “mandatory” events    End time > Start time  Only 1 visit is happening at a time for one ship (No overlapping timestamps between visits)  Logical duration for each event? (Pilot encounter should not be more than 30 minutes, Berth stay should be over 2 hours at least, etc.)    Visit ID stays the same after a recalculation  No duplicate visits/data |
| PTO/Airflow | Complete Fact and Dimension Tables          Valid data | All fact and dim tables are created and filled  no empty fields  no data lost during ETL process    No negative durations  No duplicate rows |
| Data Validation Loop | Correct Anchor and Berth Stay Timestamps      Complete Vessel Information | Timestamps are within 6 minutes compared to manual check    Length, Beam, DWT, V2 category is not empty in CSI |
| Cross Validation | - |  |

<https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/769523719/DWH+SOF+completeness+checks?atlOrigin=eyJpIjoiYjM0YmY1YzdiYmFiNDdlYmI5NTgyNGUyZGQ4ZDE4ZWQiLCJwIjoiYyJ9>

<https://teqplaybv.atlassian.net/wiki/spaces/TC/folder/777682953?atlOrigin=eyJpIjoiMmYzODdkNGQ4NzFlNDdmNWJlYTViY2RhNWJhNTZmNzYiLCJwIjoiYyJ9>

<https://teqplaybv.atlassian.net/wiki/spaces/TC/folder/774504499?atlOrigin=eyJpIjoiMTViMjY2YjMzMDQzNGRmOGIyMzUzZGNhOTA2YThhMTEiLCJwIjoiYyJ9>

<https://teqplaybv.atlassian.net/wiki/spaces/TC/folder/779812880?atlOrigin=eyJpIjoiZWViYjBkOTMwMTE0NDIwMmE2MzViNzc4OTRhNDY2NGIiLCJwIjoiYyJ9>

<https://docs.google.com/spreadsheets/d/14lhCHbDNMcmBZKVCIpiyqnuLT4xhENncYOuw9bu1y-4/edit?gid=0#gid=0>