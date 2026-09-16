---
id: github:teqplay/vesselvoyage-backend:issue:193
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 193
title: Spv-1985 New Definitions
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/193
labels: []
explicit_links: []
---
# Issue #193: Spv-1985 New Definitions

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/193  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [116d1a763a9c...af39e8621449](https://github.com/teqplay/vesselvoyage-backend/compare/116d1a763a9c...af39e8621449)
**Merge commit:** [af39e8621449](https://github.com/teqplay/vesselvoyage-backend/commit/af39e8621449)
**Author:** Darius Wattimena
**Reviewers:** 
**Approvers:** 
**Source Branch:** [SPV-1985-new-definitions](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-1985-new-definitions)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-03-29T13:53:31.947366+00:00
**Status:** MERGED

* Added new models for the new Visit/Voyage structure
* Deprecated old models
* Added new ESoF model and deprecated old models
* Added a comment on top of the new Speed model
* Adjusted other ship identifiers to integers
* Added data sources for the new Visit and Voyage models
* Added loading in the new visit/voyage state
* Updated ship state loading logic to also include the esof when available
* Adjusted event processing base classes to support the new ship status
* Adjust event processors to support the new event status
* Code cleanup
* Adjusted status changed event processor to support the new event status
* Changed existing tests so they can run
* Added test cases to ensure the ship state is loaded in correctly
* ktlint
* Added support for processing end of sea passage events to result in a basic Visit/Voyage structure
* Code cleanup
* Added support to create a Visit when having no state for the ship when receiving a end of sea passage start event
* Adjusted testing constants to be using strings of numbers for MMSIs and IMOs
* Added test cases to ensure all different flows are handled as expected
* Fixed an issue where a visit would not be added as a pass through of the voyage when exiting the end of sea passage
* Added implementation to add support for creating anchor area activities on a start event
* Moved some logic to the base class and make sure on voyage and initial status we ignore the event
* Moved the check if the event has a valid area id to the base processor
* Added implementation for th anchor end event
* Moved processing issue descriptions to consts
* Adjusted tests to be easier to extend
* Moved issue description to consts
* Added extra test cases to ensure anchor start and end events are not processed on voyage and initial status
* Added test cases to ensure anchor area activities are added correctly when in visit status
* Added extra test cases that should ignore the provided anchor event
* Code cleanup
* Added support for unique berth event processing
* Changed the anchor event processor to also use the ActivityEventProcessor
* Added test cases to ensure we don't do anything with the berth start and end event when in voyage or initial status
* Added unique berth event tests to ensure they work as expected
* ktlint
* Removed old code which has been moved to the ActivityEventProcessor
* Removed unused imports
* Updated names of the tests so they make more sense
* Added test cases to ensure port events are not processed when in voyage or initial status
* Added more tests cases for port events
* Implemented support to handle port event
* Removed unused commented out code
* Removed unused import
* Adjust the NewChange model to also include the updated esof
* Added a helper function to replace the first item with a replacement
* Added a start event id to the encounter model to match on
* Implemented the new encounter logic which adjusts the esof of the ongoing visit or voyage
* Added test case to ensure the encounter logic is working as intended
* Added test cases for events that are not used anymore by the new definition
* Ensure events are ignored when not used by the new definition
* Changed the replaceFirst so it only scans the list once
* Fix a compile issue after merging in latest develop

