---
id: confluence:222560259
source: confluence
type: page
space: TC
title: Chorus usage queries
author: Leon Joosse (Unlicensed)
date: '2023-10-30'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/222560259
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/222560259
---
# Chorus usage queries

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/222560259  

## Content

This is a list of queries used earlier for requests of Shell, to get some usage stats from Chorus.

## Nominations initiated by vendors and customers

Outputs the amount of nominations created by vendors and customers. And specifies the amount of nominations with status completed. In case of a delegation, only the left nomination is counted.

Example output, from 30-oct-2023:

Counting nominations created by Shell and customers (this may take a while)
Querying for all eventIds of all nominations
-> in case of delegation, only the left nomination is included in the result
-> other event types are skipped
Found 1700 nominations
Initiated by Shell: Count(count=630, withStatusCompleted=465, withStatusOther=165)
Not initiated by Shell: Count(count=1070, withStatusCompleted=848, withStatusOther=222)

This is quite a complex query, so it is written in code. Please see the following standalone script in the back-end repository. Don’t forget to set the MongoDB environment variables when running it, see the comments in the script which env vars are needed.

[QueryUsage.kt](https://bitbucket.org/teqplay/chorus-backend/src/master/src/main/kotlin/nl/teqplay/bunkerplanner/QueryUsage.kt)

## Number of eBDNs

There is always 0 or 1 eBDN entry in the collection per nomination. Creating a new eBDN for a nomination always overrides the previous one.

Count:

db.EBDN.countDocuments()

Count of signed eBDNs:

db.document.find({type: "EBDN", signingStatus: "SIGNED"})

## Number of NORs

A Notice Of Readiness (NOR) is either for the receiving ship or bunker ship.

Count for receiving ships:

db.document.countDocuments({type: "NOR\_RECEIVINGSHIP"})

Count for bunker ships:

db.document.countDocuments({type: "NOR\_BUNKERSHIP"})

## Number of MRF

A Master Requisition Form (MRF)

Count:

db.mastersRequisitionForm.countDocuments()

## Number of delegated nominations

Note `latest: true`, this ignores earlier proposals of the same nomination (they are all stored in the same db collection)

db.prompt.find({delegatedNominationEventId: { $ne: null }, latest: true})