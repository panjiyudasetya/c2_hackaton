---
id: confluence:596738049
source: confluence
type: page
space: TC
title: How can we reduce (new) Security Vulnerabilities in our products?
author: Richard van Klaveren
date: '2025-01-16'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/596738049
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/596738049
---
# How can we reduce (new) Security Vulnerabilities in our products?

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/596738049  

## Content

In an initial exploratory discussion the topic of reducing security vulnerabilities in general, and the introduction of new security vulnerabilities was discussed. This section gives a short summary:

## Insight and removing historical debt on vulnerabilities

There was a common agreement that it should be the very first step to have an overview in a tool of what vulnerabilities have been detected, but also which vulnerabilities apply is important. Current process is that on a weekly basis all current vulnerabilities are being detected and reported.

Untriaged vulnerabilities are being maintained [in a spreadsheet](https://teqplaybv.atlassian.net/wiki/pages/resumedraft.action?draftId=596738049&draftShareId=a32e081d-d996-4bc8-91e5-66e9cd671e3b), and for the more operational tools also a separate spreadsheet exists ([portreporter example](https://docs.google.com/spreadsheets/d/1Z-EhqGmdykOY8SqdXxOcUMKG4Q02V5nG9HKkDA3rAXE)) where the triage is being documented on a regular basis. Currently there is no way to get a full overview on all triaged vulnerability in one view. Agreement has been reached such overview should be obtained in a dedicated tool, which supports both the triaging process and visualizing them in a resulting overview. This will make awareness in the team. It should provide insight in 2 main Key Performance Indicators:

* #untriaged vulnerabilities / oldest untriaged vulnerability
* #triaged as 'has to be fixed'

## Keeping newly introduced vulnerabilities low

When the backlog of untriaged and unaddressed vulnerabilities has been addressed, it becomes relevant to see what can be done to reduce new vulnerabilities being introduced developer, and keep the backlog as small as possible. For picking up new found vulnerabilities on existing dependencies, we see a difference between product being developed actively and having a team assigned, and products that are actually not having active development:

* On an active product: At least triage (and plan to fix) them on a weekly basis, and address the found applicable vulnerabilities as part of the product development prioritized by the product owner.
* On a dorming product:  There should be resources allocated ( on rotating basis) from a secops perspective on a monthly basis to triage and address the issues based on priority.

Next to maintaining the backlogs, it should be considered to use tools that will provide hints during development time or when assessing the PR that will provide hints on which vulnerabilities have been detected in the used library version and how to address the vulnerability (which version have they been addressed).

Other ideas to make sure the vulnerabilities can be addressed effectively

* use micro Front-ends to 'fix the issue once' and apply everywhere
* When upgrading a major library (React / Spring) in one project, and in Front-end/backend team, then discuss about applying this broadly (via MT) and even consider upgrading ALL libraries when you make such step to prevent snowballing effects.

## Dependency Management

A very closely related topic to vulnerability management is of course dependency management in general. Using latest version of libraries will not only make maintenance and development faster, but also as a side-effect will keep vulnerabilities low. The following tools have been mentioned to use for implementing dependency management:

* [Renovate docs](https://docs.renovatebot.com/)
* [Dependabot](https://docs.github.com/en/code-security/dependabot/working-with-dependabot)

## Concluding

Concluding, all of such efforts will only be executed if they get priority and time assigned from both the team and the Management. When the financial situation allows, it could be even considered to have a dedicated team addressing such SecOps items.