---
id: confluence:649592846
source: confluence
type: page
space: TC
title: Dependency Management Policy
author: Richard van Klaveren
date: '2025-03-03'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/649592846
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/649592846
---
# Dependency Management Policy

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/649592846  

## Content

Effective dependency management is critical to maintaining a consistent, secure, and efficient software development lifecycle. After recent implementation of dependency track, we do see that dependency management has some place for improvement. This page outlines a proposal for standardizing and managing dependencies across projects, focusing on leveraging a Bill of Materials (BOM) approach.

## Current Challenges

The challenges in the current way of managing dependencies without having a centralized or coordinated approach is that:

* Different projects utilize varying versions of the same libraries.
* Lack of clarity on which library versions are in use across applications.
* Not all projects are using the latest versions of libraries, leading to potential security risks and inefficiencies.

Within the current way, dependencies are managed via the following 3 mechanisms, where each project has full freedom when and how to update libaries:

* Most projects import skeleton plugins, which already has selected for each version a set of specific import versions
* Projects can freely exclude and override based on this pre-set list of dependency versions
* Some dependencies are not covered in the skeleton plugins, leaving it a manual job to do it at project level, increasing the risk of human error.

## Proposed Solution Direction: Bill of Materials (BOM)

A BOM is a mechanism provided by frameworks like **Spring** that defines versions for a set of dependencies. So, Spring defines for each version of Spring a set of specific versions of the relevant dependencies in the BOM. By referencing a BOM, applications can avoid specifying individual versions, instead inheriting a consistent set of libraries and versions.

### Strategy

* Provide a central BOM that includes all required dependencies.
* Each application sets the version of the BOM to use, ensuring consistency across projects.

The latter step allows freedom for the application to only move to the new BOM whenever it is appropriate. Very actively developed applications will probably require a more up-to-date version, whereas sleeping projects might have a lower update frequency of the BOM.

### Implementation Steps

1. **Remove Overrides:** Eliminate any dependency overrides currently set in skeleton plugins or individual applications.
2. **Develop a Custom BOM:** Build a Teqplay-specific BOM based on Spring’s BOM with necessary adjustments.
3. **Automate Updates:** Implement a process to regularly update the BOM based on:

   * Detected security vulnerabilities.
   * Regular intervals (e.g., every X months for active projects, Y months for non-active projects).

## Initial Rollout Plan

Initially, the BOM updates for projects will be driven by detected vulnerabilities in dependencies. Later on, we will establish a routine to ensure dependencies are updated regularly, based on a X monthly review process. Still then we want to keep the possibility to differentiate between different kind of projects:

* **Active Development:** Dependencies must be updated within X months.
* **Non-Active Development:** Updates required within Y months.

## Pros and Cons of the BOM Approach

### 5.1. Pros

* **Increased Development Speed:** Simplified dependency management accelerates development.
* **Improved Security:** Consistent and timely updates reduce exposure to vulnerabilities.
* **In Control:** The amount of different versions of a library will be limited, allowing faster response on security incidents in specific and a more efficient vulnerability management process.

### 5.2. Cons

* **Increased Testing Needs:** More frequent updates may require additional (manual) regression and integration testing.
* **Testing Coverage:** Unit and integration tests must be comprehensive to detect issues from dependency changes, otherwise application stability might be impacted.

## 6. Conclusion

Adopting a BOM-based dependency management strategy will enhance consistency, security, and development efficiency. The proposed approach balances proactive vulnerability management with scheduled updates, ensuring a structured and maintainable process.