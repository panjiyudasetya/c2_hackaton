---
id: github:teqplay/csi-backend:issue:27
source: github
type: issue
repo: teqplay/csi-backend
number: 27
title: 'Spv-177: Imo/Mmsi Mapping'
author: jbugella
state: closed
date: '2025-01-07'
url: https://github.com/teqplay/csi-backend/issues/27
labels: []
explicit_links: []
---
# Issue #27: Spv-177: Imo/Mmsi Mapping

**Repo:** teqplay/csi-backend  
**URL:** https://github.com/teqplay/csi-backend/issues/27  
**State:** closed | **Author:** jbugella  
**Created:** 2025-01-07  
**Closed:** 2025-01-07  

## Description

**Full diff:** [8dcfe7be06b3...e74fe6f6d5a1](https://github.com/teqplay/csi-backend/compare/8dcfe7be06b3...e74fe6f6d5a1)
**Merge commit:** [e74fe6f6d5a1](https://github.com/teqplay/csi-backend/commit/e74fe6f6d5a1)
**Author:** Former user
**Reviewers:** Jos de Jong
**Approvers:** Jos de Jong
**Source Branch:** [feature/SPV-177-build-solution-to-keep-this-live](https://github.com/teqplay/csi-backend/tree/feature/SPV-177-build-solution-to-keep-this-live)
**Destination Branch:** [develop](https://github.com/teqplay/csi-backend/tree/develop)
**Closed On:** 2024-08-26T07:49:38.902324+00:00
**Status:** MERGED

**Quite a big PR, overview of what is added:**
Listening to AIS updates:
* CSI listens to the AIS streaming ship updates and stores the usage of IMO\+MMSI pairs in buckets of one hour per IMO
* all changes are kept in-memory and are persisted in bulk per five minutes \(is also triggered on shutdown to ensure no data loss\)
Searching for MMSI changes:
* Every day in the morning, a process will start looking through the stored buckets
* A timeframe of a day will be selected starting from -2 days to -1 days of the current time \(so if it’s Wednesday today, then the timeframe will be Monday 0:00 < Tuesday 0:00\). This is to ensure we still get satellite messages even if they are late, and it also functions as a natural timer since it’s not really useful to detect changes of yesterday because you will not be able to verify if the change is correct as there will not much history at that point.
* Apart from the buckets of a day, we use a bit more “precision” of 1 hour around the timeframe. This way we can detect an MMSI change at any point during the day, even at the start of the timeframe, because of having that extra hour at the start and end.
* Messages for a given IMO must exceed a threshold of minimum messages
* If a ship for a given IMO has no MMSI set, then any registered MMSI for this IMO will trigger with a `hint` of `MMSI_GETS_SET`
* If a ship for a given IMO has a MMSI set, but no other MMSIs were detected then nothing happens
* If a ship for a given IMO has a MMSI set AND there are other MMSIs, then the usage of these MMSIs must exceed a minimum absolute threshold and a minimum relative threshold \(that means, if MMSI A is used 100 times, and the relative threshold is set to 0.1, then MMSI B must at least occur 10 times for it to be registered as a change\)
* a `hint` of `MULTIPLE_MMSI` or `MMSI_CHANGED` will be set \(`MMSI_CHANGED` will be accompied by a `suggestion` about which MMSI changed to which other MMSI and at what time\)
    do note that `MMSI_CHANGED_ALREADY` is also detected, but these changes are ignored \(they should already be captured by the automatic ticket creation based on AIS, so not duplicating the messages\)

Aggregating MMSI changes:
* when the user requests all open mapping inputs, all stored MMSI changes get requested per IMO
* we then determine which changes can be grouped, for example we detect on Monday that MMSI A\+B are used, same for Tuesday, Wednesday and Thursday. But on Saturday we detect the usage of MMSI A\+C. We want to group the usage of the same MMSIs, so we get two groups, one with MMSI A\+B between Monday-Thursday and one with MMSI A\+C on Saturday.
* we also ensure we don’t use observations/groups immediately, we wait another day. This way we can verify if a MMSI change actually occurred, a MMSI change is only valid if it’s detected on day 1, and day 2 doesn’t provide other MMSIs. Then we have an isolated event of a MMSI change, verified by another day of data not giving more insights. Or we know that the MMSI actually didn’t change and multiple MMSIs are being used for the same vessel.

Apart from this, some backwardscompatibility was required:
* when a user wants to create a ticket, it will not be allowed to do so if: a ticket already exists for this ship or if a mapping input exists \(this makes sure no conflicts arise\)
* when an automatically generated AIS ticket is accepted and the MMSI is changed, then this change is also applied to the ship mapping
* when a ship mapping has a `MMSI_CHANGED` state, then the resulting MMSI will be applied to the ship as well

One case that is not covered yet:
* When a user edits the MMSI of the ship, what to do now? We don’t know if this MMSI was correct all along, or if it started to be correct at a specific point… I don’t have an idea of how to do that at this moment

If you have any question, please ask away. This PR has quite some “magic” going on.

