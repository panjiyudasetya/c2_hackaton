---
id: confluence:715587586
source: confluence
type: page
space: TC
title: VesselVoyage test plan
author: Francisco Jose Muros Muriano (Unlicensed)
date: '2025-07-07'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/715587586
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/715587586
---
# VesselVoyage test plan

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/715587586  

## Content

**Testing Plan for Vessel Voyage**  
Currently, In Vessel Voyage we have unit tests on the backend side and manual tests suite on front end side. These tests verify the front end of Vessel Voyage with various options, along with some specific event checks between Vessel Voyage and the timeline. However, these tests are limited to a small set of vessels, and they are performed manually. These tests do not cover all available events inside Vessel Voyage nor do they check a sufficient number of vessels. The goal is to add more manual and automated checks to increase the quality of Vessel Voyage.

### Objective of the Testing Plan

The primary objective of this testing plan is to enhance the quality, accuracy, and reliability of Vessel Voyage data by implementing comprehensive manual and automated validations that cover all critical aspects of visits and events. Specifically, the plan aims to:

1. **Verify Data Accuracy:**  
   Ensure that event timestamps in a visit align with the expected timestamps retrieved manually from Timeline, within a 6-minute tolerance.
2. **Ensure Completeness and Consistency:**  
   Confirm that all mandatory events are present, all visits and events are correctly classified and uniquely identified, with no duplicates or missing data.
3. **Validate Logical Integrity:**  
   Check the correctness of event sequences, visit durations, and timing constraints, such as no overlapping visits for the same vessel and correct ordering of events (e.g., pilot inbound happens before terminal ATA).
4. **Automate Regular Testing:**  
   Implement automated tests that run nightly, enabling early detection of issues and detailed reporting to support timely investigation and resolution.
5. **Support Manual Testing:**  
   Enable manual execution of test suites on demand to verify changes after deployments or data updates.

By achieving these objectives, the testing plan will ensure higher data quality, improved operational reliability, and greater confidence in Vessel Voyage’s event and visit management processes.

### Automated Testing Process Overview

This process outlines the key steps for automatically validating Vessel Voyage data. It includes retrieving vessel visits, verifying event presence and timestamps within a 6-minute tolerance, checking logical event sequences, ensuring visit consistency, and monitoring data timeliness. Test results are compiled into detailed reports in slack for continuous monitoring, with the tests scheduled to run nightly and available for manual execution when needed.

The following test cases will be automated to ensure continuous and efficient validation of Vessel Voyage data quality and consistency:

* **Single Active Visit Checks**  
  Verify that only visit can happen at the same time for a vessel.
* **Visit Time Validations**  
  Confirm visits contain valid start and end times. Check that all timestamps start before their corresponding end times.
* **Visit Duration Verification**  
  Ensure the duration of visits aligns with average expected times per port, based on historical data.
* **Pilot and Tug Event Detection**  
  Automatically detect pilot inbound and outbound events or fallback events. Verify tug encounter end times are present.
* **Stop Classification**  
  Ensure all stops within visits are classified with no unclassified stops remaining.
* **Uniqueness of Visits and Events**  
  Detect and flag duplicate visits or events. Confirm no overlapping visits occur simultaneously for the same vessel.
* **PTO SOF Timeliness**  
  Validate that PTO statements of facts are published to RabbitMQ within 5 minutes after post-processing.
* **Completeness Checks**  
  Verify all mandatory timestamps are present in visits and check visits contain drifting times where applicable.
* **Visit ID Consistency**  
  Confirm that visit IDs remain consistent between recalculations.
* **Berth Event Timing**  
  Verify berth end time does not occur before the last tug arrival.
* **Anchor Event Presence and Order**  
  Ensure anchor events are present in visits and event sequences follow logical ordering rules (e.g., anchor, pilot before berth / terminal ATA, terminal / berth ATD before Pilot Outbound).

**Manual Test Execution**

Certain tests require manual verification due to the complexity of data, dependencies on external data, or challenges in automating judgment-based checks. The manual testing focuses on validating event accuracy against external sources (Timeline) and verifying complex scenarios:

* **Timestamp Accuracy Verification**  
  Compare pilot onboard, Port ATA, and Port ATD timestamps against manual recorded times, ensuring event times fall within a 6-minute tolerance.
* **Tug Encounter Start Times**  
  Verify manually that tug encounters have accurate start times, especially for encounters not automatically detected.
* **Visit Completion and Context Alignment**  
  Confirm visits are properly completed and aligned with POMA context mapping, validating that the contextual data corresponds with the visit data.
* **No Missing or Duplicate Visits**  
  Manually check for missing visits or duplicates by cross-referencing visits with baseline data or external sources..
* **Handling Complex Scenarios**  
  Validate manually cases that are difficult to automate, such as visits with overlapping port areas, ambiguous visit start/end times, or non-standard event occurrences.
* **Berth Visit Jitter Validations**  
  Verify manually that berth visits that contains a jitter are properly finished

---

These manual steps complement automated tests and are essential for validating complex scenarios and ensuring overall data quality where automation has limitations. All test cases can be found here: <https://docs.google.com/spreadsheets/d/14lhCHbDNMcmBZKVCIpiyqnuLT4xhENncYOuw9bu1y-4/edit?gid=0#gid=0>