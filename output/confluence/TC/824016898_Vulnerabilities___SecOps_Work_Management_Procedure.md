---
id: confluence:824016898
source: confluence
type: page
space: TC
title: Vulnerabilities & SecOps Work Management Procedure
author: Michel Wilson
date: '2025-08-11'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/824016898
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/824016898
---
# Vulnerabilities & SecOps Work Management Procedure

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/824016898  

## Content

## Overview

This document describes the procedure for managing vulnerabilities and SecOps-driven work within our products. It aims to ensure that security-related tasks are identified, prioritized, tracked, and completed in a timely and transparent manner, with clear responsibilities for both product teams and the SecOps function.

## 1. Problem Statement

* New vulnerabilities appear from time to time in our products.
* SecOps requires certain security-related changes, updates, or implementations across various products.
* SecOps is not embedded within product development teams.

**Challenge:**  
How do we effectively plan, manage, and ensure completion of SecOps-driven work?

## 2. SecOps Work Management Process

### 2.1. General Approach

* All SecOps-related work is tracked as Jira issues, labeled with `SecOps`.
* SecOps uses an overview board to visualize and manage all labeled cards.
* Weekly meetings are held between SecOps and each team lead to review the status and priorities.
* Teams are responsible for triaging, scheduling, and delivering SecOps work.

## 3. Procedure Steps

### 3.1. Identifying and Labeling Work

* **Vulnerabilities:**

  + Detected via Dependency Track.
  + Each finding is logged as a Jira card and labeled `SecOps`.
  + Projects in Dependency Track are labeled with the responsible team to facilitate filtering.
* **Non-Vulnerability SecOps Work:**

  + Examples: encryption at rest, changes to authentication flow, certification policies.
  + Added collaboratively by SecOps and the team lead to the product backlog, always with the `SecOps` label.

### 3.2. Visibility & Tracking

* SecOps maintains an overview board aggregating all `SecOps`-labeled cards.
* Weekly status/prioritization meetings ensure alignment and follow-up.
* Teams regularly check Dependency Track (or receive Slack alerts, future enhancement) for new issues.

### 3.3. Prioritization & Scheduling

* **Critical Vulnerabilities:**

  + Must be addressed within **15 days** (may require scope adjustment of current sprint or prioritized at the start of next sprint).
* **High Vulnerabilities:**

  + Must be addressed within **30 days** (added to next sprint, ideally).
* **Other Vulnerabilities:**

  + Target completion within **45 days** (next or following sprint).

### 3.4. Team Responsibilities

* Monitor for new SecOps-labeled Jira issues and new vulnerabilities (Dependency Track).
* Schedule work within required timeframes according to severity.
* Proactively add and triage security work.
* Participate in weekly meetings with SecOps to review status and priorities.

### 3.5. SecOps Responsibilities

* Ensure all relevant work is correctly labeled and visible.
* Monitor Jira and Dependency Track to confirm issues are addressed on schedule.
* If ~50% of the allowed time has passed without progress, nudge the team lead for action.
* Collaborate with team leads to add non-vulnerability work items to the backlog.
* Facilitate and lead weekly overview meetings.