---
id: confluence:651853832
source: confluence
type: page
space: TC
title: RouteScout Facility call
author: Richard van Klaveren
date: '2025-03-04'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/651853832
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/651853832
---
# RouteScout Facility call

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/651853832  

## Content

## Introduction

The following steps include everything needed to fully update routes in the route planner.

Summary of the steps:

* Indicate facility settings
* Activate prepared graphs
* Fix graph errors
* Test facility sandbox and switch to live

Note: as reference, the manual steps of the importing graphs process is shown [here](https://bitbucket.org/teqplay/teqplay-wiki/wiki/RouteScout%20Importing%20graphs%20process).

# Steps

## 1 Indicate facility settings

*Endpoint*

`/facility/initiate`

*Schema*

{
"setting": "FULL" | "CUSTOM" | "SAVED" | "MANUAL" | "WRITE", // where the process starts
"prepared": InputGraph | null, // optional: if not supplied defaults to `null`, schema shown below
"custom": InputGraph | null, // optional: if not supplied defaults to `null`, schema shown below
"manual": InputGraph | null // optional: if not supplied defaults to `null`, schema shown below
}

*Schema: InputGraph*

{
"active": [ // optional: if not supplied defaults to `null`, list of graph keys to be set active
"ownerId.generationId.speciesId" // key of a graph `ownerId.generationId.speciesId`
] | null,
"inactive": [ // optional: if not supplied defaults to `null`, list of graph keys to be set inactive
"ownerId.generationId.speciesId" // key of a graph `ownerId.generationId.speciesId`
] | null
}

After you've initiated the facility a message will be sent to Slack.

## 2 Activate prepared graphs

Wait for the facility to send the Slack message about activating prepared graphs.

Then look at all the prepared graphs, including the newly imported graphs, and activate or inactivate graphs. After you've done this you can release the hold on the facility to continue running it.

`/facility/hold/release?referenceId={referenceId}`

You will have to include the `referenceId` of the facility to release the hold.

## 3 Fix graph errors

If the facility sends a Slack message about the write stage having failed, then continue, else go to the next step.

If the write stage ends with any notification then it will fail. You have to fix these notifications and then re-run the facility with the following endpoint. If the write stage is fixed, the facility will continue where it stopped.

`/facility/run?referenceId={referenceId}`

You will have to include the `referenceId` of the facility to run it.

## 4 Test facility sandbox and switch to live

Wait for the facility to send the Slack message about testing the sandbox.

You can now test the sandbox.

### If you are not happy with the functioning of the test sandbox:

#### If you don't want the routes of the base sources or want to stop in general. You can stop the facility with the following endpoint:

`/facility/stop?referenceId={referenceId}`

You will have to include the `referenceId` of the facility to stop it.

You can now change the base sources if needed and then run a new facility with correct settings to retry.

#### If you want to edit manual routes, you have to manually perform the following steps

1. Update the manual routes to your liking.
2. Trigger the graph write step manually and ensure no notifications are returned and the graph is written.
3. Open or update the facility test sandbox.

   * Look for the pipeline of the facility.
   * Facility test sandbox does not exist / open sandbox

     + Use the graph info of `writeOutput` for the `ownerId`, `generationId` and `speciesId`
     + Use the graph info of `facilityTestSandbox` for the `targetOwnerId`, `targetGenerationId` and `targetSpeciesId`
   * Facility test sandbox already exists / update sandbox

     + Use the graph key of `facilityTestSandbox` to update the sandbox
4. Go back to step `4 Test facility sandbox and switch to live`

### If you are happy with the functioning of the test sandbox you can continue the facility with the following endpoint:

`/facility/hold/release?referenceId={referenceId}`

You will have to include the `referenceId` of the facility to release the hold.

After doing this the facility test sandbox will be closed, a new sandbox will be created and it will be switched to live.

---

**You are now done updating the route planner!**