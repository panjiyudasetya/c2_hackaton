---
id: github:teqplay/vesselvoyage-backend:issue:357
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 357
title: Release 24-10-2024
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/357
labels: []
explicit_links: []
---
# Issue #357: Release 24-10-2024

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/357  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [90512025e451...1593baef6a1c](https://github.com/teqplay/vesselvoyage-backend/compare/90512025e451...1593baef6a1c)
**Merge commit:** [1593baef6a1c](https://github.com/teqplay/vesselvoyage-backend/commit/1593baef6a1c)
**Author:** Darius Wattimena
**Reviewers:** 
**Approvers:** 
**Source Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Destination Branch:** [master](https://github.com/teqplay/vesselvoyage-backend/tree/master)
**Closed On:** 2024-10-24T09:18:33.868429+00:00
**Status:** MERGED

* Add ship details to PTO SOF
* Add test for ship not in ship cache
* Add lock stops to PTO SOF
* Create separate generator for PortStatementOfFactsView
* Move generate port statement of facts view to esofv2service, moving logic out of the controller
* Remove Port statement of facts view
* Fix merge conflicts. Remove PortStatementOfFactsView and TerminalStatementOfFactsView again
* Added drift segment data class \(from drift predictor\)
* Added drift segment prediction item data class \(from drift predictor\)
* Added drift segment response body data class \(from drift predictor\)
* Added rest template configuration for drift predictor api
* Added drift predictor client
* Created post-processing service for determining slow moving segments
* Added Speed calculation for slow moving period
* Added test to validate slow moving period calculated by the PostProcessingService
* Changed expression label
* Added test for no slow moving period case & cleared up timestamps
* Refactored speed functions into separate util functions.
* Refactored service to make use of speed util functions.
* Refactored service to make use of speed util functions.
* Fixed ktlint error
* Added processing profile to service
* added info logging to see what is going wrong
* Fix compile issue
* Added slow moving periods to dry run
* Added properties class for drift-predictor api
* Added url for drift-predictor api
* Added drift-predictor properties class
* Refactored DriftSegmentPredictionItem to contain separate properties for each feature instead of an array containing all features
* Added some logging & incorporated DriftSegmentPredictionItem changes
* Added PostProcessingService as mock
* Refactored determineSlowMovingSegments function to be more clear and concise
* Added drift predictor url to test application.properties
* Started with merging of stops to fix jitter issues
* Rename createSpeedOfTrace method, so we can distinct between old and new implementation
* Added stop merging for anchorages
* Fix an issue where revents couldn't be loaded anymore
* Added a spring profile test that covers how revents jobs are run
* ktlint
* wip
* Create an esof when we never had one to use for the slow moving periods
* Added outgoing request logger so we see what calls are done to the drift predictor
* ktlint
* wip
* Moved the merging logic to their own components so they can be loaded using spring where needed
* Updated test to match expected outcome
* ktlint
* WIP
* Add approach areas
* Add test
* Move existing event sender to new package
* Added logic to publish the api entry and statement of facts
* Changed when and how things are published to nats
* Added nats publishing as the last thing for event processing if there are any changes
* Code cleanup
* Made some of the constants public so they can be reused when doing unit tests
* Adjusted existing tests to work with the new change publisher
* Added default configuration for the new changes publisher
* Added test cases to ensure changes are published as expected
* Added more test cases with all current possible usecases
* Fixed a bunch of issues where publishing wouldn't work as expected
* Code cleanup
* Adjusted mongo port to ensure we never connect to mongo locally
* Moved configuration to the ApplicationTestConfig and instead reuse that one for my publisher service test
* Updated comment to actual local mongo port
* Add weightedAverage and tests
* Lowered the total amount of activities one field can have
* Adjusted test cases to reflect the expected max of 50
* Make sure to use the same constant for all places where we limit
* feat: add support for ship cache without IMO but with MMSI fix: fix old READ.ME
* Added a toggle to disable real time V1 processing for events
* Added a toggle to disable real time V1 processing for traces
* Adjusted existing test cases to include the new parameters
* Added some extra logging to see what processing is enabled and which is slow
* Added test cases to ensure permissions are set correctly
* Added a new revents role that only has access to the events controller
* Commented out actual change
* Moved models of events to the internal model package instead
* Add test cases that cover the V2 event controllers as well
* Code cleanup
* Fix weighted average function
* Add 'finished' property to SOF api request
* Add finished state enum for querying finished, ongoing or both states. This is used internally in services and data layers, API controllers use a nullable boolean
* Extend new entry database queries with 'finishedState' flag
* Extend V2 NewEntry services with 'finished' flag
* Extend V2 NewEntry controllers with 'finished' flag
* Add documentation for NewEntryFinishedFilter and rename to reflect its meaning
* Add case to weightedAverage\(\) when both weights are 0. Fix tests, there was a fault in the generation code
* Fix tests
* Added an endpoint to expose the full trace object
* Added controller tests to ensure the trace object is returned as expected
* feat: add metadata fields to revent scenarios
* fix: make nullable
* Enhance documentation / comments, inline unnecessary variable, remove log statements intended for development
* Fix ProcessingV2TraceControllerTest, it was using a different object mapper. Now magically have the correct one?
* Make the finished state filter optional by setting default param.
* Remove index changes, not really needed.
* Adjusted URLs so the processing backend has a new URL and the API backend gets the old url
* fix: fix tests
* Added a test case of a ship state where the vessel would go out of order when having a zero-second voyage
* Fixed an issue where with a zero-second voyage you would always load in the ship state incorrectly resulting in creating of multiple visit
* Fix test compile issue

