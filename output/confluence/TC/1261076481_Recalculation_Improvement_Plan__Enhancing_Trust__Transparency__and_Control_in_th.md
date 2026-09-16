---
id: confluence:1261076481
source: confluence
type: page
space: TC
title: 'Recalculation Improvement Plan: Enhancing Trust, Transparency, and Control
  in the Process'
author: Darius Wattimena
date: '2026-06-29'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1261076481
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1261076481
---
# Recalculation Improvement Plan: Enhancing Trust, Transparency, and Control in the Process

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1261076481  

## Content

# Recalculation Improvement Plan

## Problem Statement

The Revents recalculation process is a core component of VesselVoyage, but today we have very little visibility and control over what happens while a recalculation is running.

This affects both the VesselVoyage development team and consumers of the recalculated data, making it difficult to confidently introduce changes or validate results.

The current process has four key shortcomings.

### 1. Limited trust in the recalculation process

When a recalculation completes, it is difficult to determine whether it executed correctly or produced the expected results.

Without sufficient observability and validation, both developers and users have limited confidence in the generated data.

### 2. Insufficient quality assurance

There is currently limited automated validation to ensure that changes to the recalculation pipeline do not introduce regressions.

As the platform evolves, maintaining a consistent level of quality becomes increasingly difficult.

### 3. No clear long-term direction

While improvements have been made over time, there is no shared vision of what a mature recalculation platform should look like.

This makes it difficult to prioritize improvements and build towards a common goal.

### 4. Limited insight into data changes

After a recalculation has finished, it is difficult to answer fundamental questions such as:

* What changed?
* Why did it change?
* Which ships were affected?
* Which ports were affected?

This significantly increases the effort required to validate algorithm improvements and investigate issues.

---

# Goals

This initiative aims to transform the recalculation process into one that is:

* **Trusted** – Developers and users have confidence in every recalculation.
* **Reliable** – Automated validation protects against regressions.
* **Observable** – Every recalculation can be monitored and controlled while it is running.
* **Transparent** – Every data change can be understood and explained.

By achieving this, we aim to accomplish two primary goals.

## Goal 1 – A Trusted Recalculation Process

Both developers and users should have confidence that recalculations are:

* Reliable
* Repeatable
* Recoverable
* Easy to monitor

Every recalculation should behave predictably and provide enough information to diagnose issues when something goes wrong.

## Goal 2 – Complete Transparency

Every recalculation should clearly answer the following questions without requiring manual investigation:

* What changed?
* Why did it change?
* Which ships were affected?
* Which ports were affected?
* What is the overall impact?

This enables easier validation of algorithm improvements and significantly reduces debugging effort.

---

# Initiatives

To achieve these goals, we propose three initiatives.

---

# Initiative 1 – Improve Process Visibility & Operational Control

## Objective

Provide complete visibility into every step of the recalculation process while giving operators full control over running scenarios.

### Improve Execution Visibility

Provide dashboards showing:

* Currently running recalculations
* Ships currently being recalculated
* Progress of every recalculation
* Active monitors
* Performance metrics for every monitor

  + Processing speed
  + Queue size
  + Throughput

This should make it possible to immediately understand the current state of the recalculation process.

### Improve Operational Control

Operators should be able to:

* Stop or cancel recalculations
* Estimate remaining runtime
* View the post-processing backlog
* Verify that post-processing has completed successfully

  + Drifting
  + Other derived calculations

### Improve Failure Handling

Failures should never become "silent failures".

Introduce:

* Retry mechanisms where merge-back operations can fail
* Clear failure reasons
* Actionable error messages
* Alerts when scenarios fail validation or behave unexpectedly

### Expected Outcome

* Every recalculation can be monitored from start to finish.
* Every failure has a clear explanation.
* Operators can safely intervene when necessary.

---

# Initiative 2 – Improve Reliability Through Automated Integration Testing

## Objective

Continuously validate that the recalculation pipeline behaves consistently across releases.

### Execution Strategy

Run integration tests:

* Daily
* Before every release
* On the Develop branch
* On the Master branch

### Revents Integration Tests

Execute a known job over a fixed time period and compare the generated output against expected results.

Validate:

#### Revents API / Orchestrator

* Job execution
* Scheduling
* Correct orchestration between services

#### VesselVoyage

* Stable processing
* Expected output generation

### Merge-back Integration Tests

Ensure merge-back behaviour remains deterministic.

Cover scenarios including:

* Simple merge
* Overlapping ports
* Deleted data
* Timestamp consistency
* Record count consistency
* Successful completion of post-processing

### Monitor Integration Tests

Modernize and expand monitor coverage.

Planned improvements:

* Rebuild NATS integration tests for RabbitMQ
* Create StopMonitor integration tests
* Expand scenario coverage for every monitor used by Revents

### Expected Outcome

* Regressions are detected automatically.
* Every release validates the complete recalculation pipeline.
* Confidence in future changes increases significantly.

---

# Initiative 3 – Improve Visibility into Data Changes

## Objective

Provide complete insight into exactly what changed after every recalculation.

### High-Level Comparison

Provide summary statistics comparing the previous dataset with the recalculated dataset.

Examples include:

* Number of visits
* Number of encounters
* Average visit duration

This provides an immediate overview of the impact of a recalculation.

### Ship-Level Comparison

Allow inspection of individual ship histories.

Display:

* Previous timeline
* Recalculated timeline
* Exact differences

This enables detailed validation of specific scenarios.

### Port-Level Comparison

Provide detailed insight into changes per port.

Include:

* Number of affected ships
* Which ships changed
* Time periods affected

For every stop or encounter type, show:

* Added
* Modified
* Removed

Coverage includes:

* Berth stops
* Anchor stops
* Lock stops
* Unclassified stops
* Encounters
* Encounter types
* Ship-to-ship encounters
* Drifting (slow-moving periods)
* Port passthroughs
* EOSP passthroughs
* Port ATA / ATD
* Pilot areas
* Anchor areas
* Terminal mooring areas
* Lock areas
* Approach areas

### Expected Outcome

Every recalculation can be compared against the previous version, making it immediately clear:

* What changed
* Why it changed
* Which ships were affected
* Which ports were affected

---

# Roadmap

| Phase | Focus | Deliverables |
| --- | --- | --- |
| **Phase 1** | Process Visibility | Live recalculation dashboard, progress tracking, monitor metrics, runtime estimates |
| **Phase 2** | Operational Control | Stop/retry capabilities, alerts, failure reporting, post-processing visibility |
| **Phase 3** | Automated Testing | Daily integration tests, release validation, merge-back testing, monitor coverage |
| **Phase 4** | Data Comparison | Summary comparison, ship comparison, port comparison, detailed change reporting |
| **Phase 5** | Continuous Improvement | Performance optimizations, additional metrics, expanded test coverage |

---

# Success Criteria

At the completion of these initiatives, we aim to achieve the following outcomes:

* Developers trust the recalculation process and can confidently introduce changes.
* Consumers trust the recalculated data and understand how it was produced.
* Every recalculation can be monitored, controlled and diagnosed while it is running.
* Every release is automatically validated through integration testing.
* Every recalculation clearly shows what changed and why.
* Investigating regressions or validating algorithm improvements becomes significantly faster.