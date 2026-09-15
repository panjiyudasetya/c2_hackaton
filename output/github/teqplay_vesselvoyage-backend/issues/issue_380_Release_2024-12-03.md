---
id: github:teqplay/vesselvoyage-backend:issue:380
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 380
title: Release 2024-12-03
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/380
labels: []
explicit_links: []
---
# Issue #380: Release 2024-12-03

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/380  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [1593baef6a1c...e9c831f6e7ad](https://github.com/teqplay/vesselvoyage-backend/compare/1593baef6a1c...e9c831f6e7ad)
**Merge commit:** [e9c831f6e7ad](https://github.com/teqplay/vesselvoyage-backend/commit/e9c831f6e7ad)
**Author:** Darius Wattimena
**Reviewers:** 
**Approvers:** 
**Source Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Destination Branch:** [master](https://github.com/teqplay/vesselvoyage-backend/tree/master)
**Closed On:** 2024-12-03T13:31:16.484150+00:00
**Status:** MERGED

* Added a new test case that test overlapping eosps similar to the schelde river
* Adjusted tests to correctly mock so we can have multiple ports to confirm visits
* Fix an issue where the EOSP start times would go in the past when having overlapping EOSPs
* Revert back change as it doesn't seem to work
* Changed at what time the buffer tests look at as they picked the wrong visit start and end times
* Removed unused helper function
* Add distance calculation to traces
* Cleanup
* Fix name
* Added a gauge to also track the ships that ended up in the error state
* Added more test cases of departure tugs that were not taking into account
* Adjusted code so it allow more cases of departure tugs
* Added missing ingress group
* Added missing permissions for revent role used when merging back
* Add generic TraceStatistic class for recording a NewTrace draught
* Add draught to TraceItem, populate it from AIS static messages
* Add calculator for trace statistic. Include it in the trace service
* Fix formula, add tests
* Reworked how the collection is initialized
* Adjusted visit and voyage data source aligning on indexes are made
* Added some logic to automatically cleanup scenarios that were stuck on restart of the backend
* Fix test name
* Add API model for NewTrace
* Fix controller test
* Expose port times to api
* Adjusted tests to also support the newly added port times
* Adjusted tests to also support the newly added port times
* Move trace distance top level functions instead of class based injection
* Move trace draught to top level functions instead of class based injection
* Made trace generation when requesting a ship story optional
* Added a new test case where multiple anchor stops should be merged when having a drifting like pattern in the same anchorage
* Adjusted how the anchor merging tactic works to group together anchor moments when they are close enough and of the same anchorage
* Changed comment why we use a more aggressive max distance
* ktlint
* Remove unused function appendTraceStatistic and test. Remove unnecessary TODO
* Add method docs
* Added persist changes service to decouple the persistchange function from the entry processing service.
* Created separate slow moving service \(former post processing service\)
* Renamed from post processing service
* Added properties class for post-processing service.
* Refactored Post-processing service to decouple from slow moving service
* Added total threads property for post-processing service
* Added post-processing and refactored persistChange function
* Added mocks for new services
* Removed unused import
* Removed status is null check
* Refactored createSpeedOfTrace to createSpeedOfTracItemsOrNull
* Added logging, clean up post processing and added a toggle to disable post processing
* Extend ShipDetails model with dwt \(deadWeightTonnage\)
* Add endpoint for front-end ports page, to combine all calls in one
* Moved some of the tests and did some code cleanup
* fix: create recursive retry mechanism instead of throwing exception for rabbitmq send
* Added a test to ensure the post processing service is called when we expect it
* Fixed the issue where the post processing service wouldn't be called when finishing a visit
* Added 2 extra test cases for the post processing service
* Adjusted logic to support 0-second voyages
* Changed the check to ensure only with 0-second voyages the logic is triggered
* ktlint
* Corrected test
* Added some all possible cases where we should or shouldn't run the post-processing
* Adjusted the code so we can also trigger post-processing for voyages
* Made the threadpool not lazy anymore as the bean only gets created now when enabled anyhow
* ktlint
* Made logging debug level for all the post-processing things
* Changed pilot outbound expected results to match the new desired behaviour
* Update logic so always the last pilot after the last berth is selected
* Corrected documentation
* Make sure to catch errors thrown by the drift predictor
* Removed logging of full exception
* Adjusted scenarios to the new behaviour for resumable visits
* Made it so we resume a previously finished visit when going back to the same EOSP but never entering a port
* code cleanup
* Added a scenario test where the visit is resumed after leaving the EOSP and re-entering it
* Adjusted mongo indexes so they are more stable
* Removed unneeded imo index
* Instead use the time field as otherwise the index doesn't make any sense
* Added back needed index
* Changed how we trigger and run the post-processing of Visits and Voyages
* Fixed an edge case where we would call the drift predictor when we would not have any AIS data to provide it
* Reworked loading of the esof to be done in one go instead of one by one
* ktlint
* feat: add handling of corrupt revents scenarios
* fix: test failed
* fix: add health indicator for rabbitmq
* fix: add bean
* fix: ktlint
* feat: override rabbitmq health endpoint
* fix: logs
* Made it so we can publish V2 changes on RabbitMQ and merged configuration of V1 and V2 in the shared event-publishing property group
* ktlint
* split the V1 and V2 exchange so they are fully split
* Attempt to fix an issue where the wrong data is returned when loading in the sailing towards and just left data
* Adjusted how we load in ports and ships when starting the backend
* Actually fix sailing towards and just left
* Remove sparse index that doesn't work
* ktlint

