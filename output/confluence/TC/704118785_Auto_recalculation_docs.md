---
id: confluence:704118785
source: confluence
type: page
space: TC
title: Auto recalculation docs
author: Darius Wattimena
date: '2025-04-18'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/704118785
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/704118785
---
# Auto recalculation docs

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/704118785  

## Content

## Configuration

The current auto recalculation process can be configured with the following:

automatic-recalculation.enabled=false
automatic-recalculation.event-history-pre-recalculation-enabled=false
automatic-recalculation.batch-size=100
automatic-recalculation.cron=0 0 \* \* \* \*
automatic-recalculation.ready-offset=PT48H
automatic-recalculation.ship-refresh-interval=PT15M

* `enabled`Need to be set to `true` if you want to do any recalculations.
* `event-history-pre-recalculation-enabled` When enabled, first run a recalculation using the real-time events from event history.
* `batch-size` The amounts of ships that will be recalculated.
* `cron` The interval we want to trigger a batch.
* `ready-offset` How long ago we needed a started Voyage. This is set to 2 days because of a technical limitation with revents where it can only use AIS data from S3.
* `ship-refresh-interval` How often we refresh the ships that are “ready“ for recalculation.

## Auto recalculation status

There are 5 different statuses a ship can be:

* `RUNNING` The ship is currently being recalculated, the revents scenario is still running.
* `READY` The ship is ready to be recalculated. A ship is moved to this status when we have a Voyage for this ship 2 days ago.
* `NOT_READY` The ship is NOT ready for recalculation. This means we are either still in the first ever Visit or the ship is not active, meaning we haven’t received any AIS.
* `FINISHED` The ship is automatic recalculated.
* `ERROR` A ship can go to the ERROR status when something went wrong while merging back the result or when the full scenario crashed.

## Grafana

In grafana there are multiple dashboards that can aid us in checking the status of our running recalculations.

The VesselVoyage dashboard can be used to find counters of all 5 states a ship can be in the auto-recalculation process. Dashboard can be found here → <https://grafana.teqplay.nl/d/NdlJ2Zn4z/vesselvoyage?orgId=1>

Next to the VesselVoyage dashboard we also have the Revents dashboard which can show some insight in the CPU thread stability of the Orchestrator. Dashboard can be found here → <https://grafana.teqplay.nl/d/aeiw7zbrzlv5sf/revents?orgId=1>

## Process of checking if all is running stable

### Check if the newly created scenarios are running

Go to <https://vesselvoyagev2.teqplay.nl/#/scenarios> and check if any scenario is stuck at `Queued`.

Possible issues that can happen:

1. Scenarios get stuck at `Queued` status because the Orchestrator crashed. You have to restart the orchestrator, because it will stay stuck forever.
2. Scenarios get stuck at `Queued` status because Jobs are stuck and we reached the max of 32 jobs. Apparently their are Jobs stuck, or the ships are taking too long.

   1. For stuck jobs following the `Check if the currently running jobs haven’t crashed` steps.
   2. For ships taking too long, this would mean we can’t recalculate with our given speed. We most likely have to change the cron.

### Check if the currently running jobs haven’t crashed

Steps to take:

1. Go to lens, go to the `revents-jobs` namespace, pods.
2. Click each Pod and check if the CPU is still using a lot, expected CPU is ~4.0
3. Open the logs of the `revents-engine` container inside each pod to see if new AIS messages are still being scheduled for all monitors, and the events are being consumed by VesselVoyage.

Possible scenarios that can happen:

1. If you think a pod is stuck, check in the Orchestrator if the scenario of said job is not writing their results to the database. Around 15~ minutes it still takes after all AIS and events are processed the orchestrator saves the results to the Revents API database. At that time only the NATS server inside the job is being used, but all other containers are basically idle.
2. If it is actually stuck, we need to find out what is wrong, but also kill the Pod. You can either remove the Pod on Kubernetes level or restart the Orchestrator.

   1. Downside of removing the Pod is that it will result in exceptions being spammed in the Orchestrator.
   2. Downside of restarting the Orchestrator is that it will cancel all other jobs currently running.

### Check if the Revents database is not growing too fast

Because the result of the scenarios are all being saved in the database it can happen that the revents database grows out of its disk size. While it is expected that we have Grafana alerts on this, it is still a good practice to check once a week or so that the disk isn’t growing too rapidly.

If the disk is reaching any limits then we have to resize it. This can be done by updating the mongo database size of the Revents API.

## Extra info

When ships stay stuck on status `RUNNING` while you for example restarted the orchestrator, run the following mongo query to reset the state of those ships:

db.automaticRecalculations.updateMany({state: "RUNNING"}, {$set: {state: "READY"}, $unset: {scenarioId: "" }})

Don’t do this when one of the ships is actually running a scenario. Because this can result in ships having a scenario running 2 times when scheduled again.

When you want to trigger an auto recalculation by hand. This can be done by using the following endpoint in the API of the processing unit (backend of the VesselVoyage frontend):

Endpoint = `/v2/recalculate/automatic/batch`  
Server = <https://backendvesselvoyage-processing.teqplay.nl>