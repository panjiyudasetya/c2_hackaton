---
id: github:teqplay/vesselvoyage-backend:pr:728
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 728
title: Release 10 Mar 2026
author: Darius-Wattimena
state: closed
date: '2026-03-09'
merged_at: '2026-03-09'
base_branch: master
head_branch: develop
url: https://github.com/teqplay/vesselvoyage-backend/pull/728
labels: []
linked_issues: []
explicit_links: []
---
# PR #728: Release 10 Mar 2026

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/728  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `master` ← `develop`  
**Created:** 2026-03-09  
**Merged:** 2026-03-09  

## Description

_No description._

## Commits

- _… 37 earlier commits not shown_
- `3e75e886` **Darius Wattimena** (2026-03-04): Adjust data sources so they use findOneById to have faster performance when loading in data
- `bfa1bf62` **Joost Dambrink** (2026-03-05): Merge pull request #724 from teqplay/improve-finding-one-by-id
  TCC-675 Improve normalized find by id performance
- `1ea469c4` **Joost Dambrink** (2026-03-05): Merge branch 'develop' into TCC-720
- `5cec0c9c` **TeqJoostD** (2026-03-05): Add lane mechanism for better consumption
- `2997fb97` **TeqJoostD** (2026-03-05): Merge remote-tracking branch 'origin/TCC-720' into TCC-720
- `92a66ab3` **TeqJoostD** (2026-03-05): Improve speed
- `03aaa8b1` **TeqJoostD** (2026-03-05): Improve speed even more
- `d1d23c3a` **TeqJoostD** (2026-03-05): Fix dropping messages issue
- `e776d0ba` **Darius Wattimena** (2026-03-05): Improve encounter processing to ignore any duplicate start events
- `b13aecbb` **Darius Wattimena** (2026-03-05): Fix merging of encounters
- `d816b82a` **Darius Wattimena** (2026-03-05): Fix merging for other things for the esof as well
- `44e3519f` **Darius Wattimena** (2026-03-05): Fix duplicate event issue on shiptoship
- `3a030ed8` **Darius Wattimena** (2026-03-05): Correct stop merging
- `ee92613a` **Darius Wattimena** (2026-03-05): Code cleanup
- `a1f32917` **Darius Wattimena** (2026-03-05): Adjust order of checks
- `4d0c3bd1` **Darius Wattimena** (2026-03-05): Adjusted how we load in ship state so it is faster and does less calls to the database
- `63859264` **Darius Wattimena** (2026-03-05): Clean up tests and remove test case which isn't valid anymore
- `5688d1dc` **Darius Wattimena** (2026-03-05): Merge branch 'TCC-675-processing-fixes' into TCC-675-improve-startup-speed
- `4179dfc6` **TeqJoostD** (2026-03-06): Stop dropping messages
- `eeeb30e2` **Darius Wattimena** (2026-03-06): Remove unused parameter from the ship status services
- `abd52f0c` **Darius Wattimena** (2026-03-06): Add unit testing for processing ship status service
- `aadc34e7` **Darius Wattimena** (2026-03-06): Rework index creation
- `7ec8ae55` **Darius Wattimena** (2026-03-06): ktlint
- `bdb72f5e` **Darius Wattimena** (2026-03-06): Add index for looking up by ais destination
- `711ae652` **Darius Wattimena** (2026-03-06): Improve loading of visits voyages and esofs by doing them in parallel
- `a2a3db27` **Darius Wattimena** (2026-03-06): Merge pull request #723 from teqplay/TCC-720
  RabbitMQ AIS Diff
- `ed148092` **Darius Wattimena** (2026-03-06): Speed up trace processing to not need the current ship status but just the identifiers
- `1e5e6f37` **Darius Wattimena** (2026-03-06): Updated tests to work with new logic
- `a11769a1` **Darius Wattimena** (2026-03-06): Merge branch 'develop' into TCC-675-trace-processing-speed-up
- `94f33219` **Darius Wattimena** (2026-03-06): Apply changes to rabbitmq ais consumer as well
- `ba6dec29` **Darius Wattimena** (2026-03-06): Merge branch 'develop' into TCC-675-processing-fixes
- `330ee5ae` **Darius Wattimena** (2026-03-06): Merge branch 'TCC-675-processing-fixes' into TCC-675-trace-processing-speed-up
- `86bbc00a` **Darius Wattimena** (2026-03-06): Minor improvements to loading of ship identifiers to set the correct updated at timestamps
- `268277f8` **Darius Wattimena** (2026-03-06): Set default date of all identifiers to min epoch to keep start up time fast initially
- `9fd2d133` **Darius Wattimena** (2026-03-06): Adjusted tests so they work
- `9897eb36` **Darius Wattimena** (2026-03-06): Improve brute force loading to be faster
- `f4006b4f` **Darius Wattimena** (2026-03-06): Adjust tests to work with new brute force loading mechanism
- `ed20d454` **Darius Wattimena** (2026-03-06): ktlint
- `431f9dbe` **Darius Wattimena** (2026-03-06): Set a default updatedAt to ensure we can load in older document
- `f9fe3e7f` **Darius Wattimena** (2026-03-06): Adjusted last updated at to be using EPOCH instead of MIN
- `2393bd37` **Darius Wattimena** (2026-03-06): Adjust mongo queries to be chunked to avoid bson query exceptions
- `4d436da5` **Darius Wattimena** (2026-03-09): Adjusted indexes so we can do loading of ship state by only the index
- `6ad3158c` **Darius Wattimena** (2026-03-09): Removed unused indexes from new and old collections
- `a974b17a` **Darius Wattimena** (2026-03-09): Move index creation to the background thread for the old collections and added a new index needed for faster ship state loading
- `ca591644` **Darius Wattimena** (2026-03-09): Adjusted loading of ships to be in smaller batches and log progress
- `e1b8d174` **Darius Wattimena** (2026-03-09): ktlint cleanup
- `367bdc38` **Darius Wattimena** (2026-03-09): Added additional logging so we can see how long each collection takes to load in a batch
- `48eec71d` **Darius Wattimena** (2026-03-09): Merge pull request #725 from teqplay/TCC-675-processing-fixes
  TCC-675 processing fixes
- `7f9dc6c3` **Darius Wattimena** (2026-03-09): Merge branch 'develop' into TCC-675-trace-processing-speed-up
- `992a2f26` **Darius Wattimena** (2026-03-09): Merge pull request #727 from teqplay/TCC-675-trace-processing-speed-up
  TCC-675 Start up and trace processing improvements

## Reviews

### michel-teqplay — APPROVED (2026-03-09)

_No comment._

## Comments
