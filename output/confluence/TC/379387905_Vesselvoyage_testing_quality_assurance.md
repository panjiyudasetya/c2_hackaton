---
id: confluence:379387905
source: confluence
type: page
space: TC
title: Vesselvoyage testing/quality assurance
author: Michel Wilson
date: '2024-06-17'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/379387905
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/379387905
---
# Vesselvoyage testing/quality assurance

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/379387905  

## Content

Some notes based on a discussion between Darius and Michel:

### Unit test level

Test coverage is currently at a high level. To safeguard this, it is recommended to setup codecov for this project as well, to keep track of the coverage level, to ensure it stays at a high level, and to be able to evaluate pull requests wrt the code coverage.

### Integration tests

The plan is to use integration tests to capture "scenario tests": tests describing a sequence of input events together with the various REST responses, which should lead to a specific timeline/statement of facts/list of visits for a vessel. Ideally, some effort is spent in ensuring that creating, reading and updating scenarios is as easy as possible, for example by making good use of the Kotlin DSL functionality.

### Monitoring

As a third safeguard, the operational performance should be monitored. We want to use Prometheus/Grafana for that, and the idea is to start with collecting a bunch of key statistics per port, on the number of "things" happening there. The things we would like to track are:

* number of visits
* number of pilot events
* number of tug events?
* number of anchor events

These will be tracked using counters, and Grafana will be used to determine daily/weekly event rates, and to trigger alerts if the rates fall below a threshold. Initially we will use regular hard-coded thresholds, but in the future it would be good to find a way to automatically determine a trend for these rates, and to trigger an alert if the trend is broken. This can be used to also account for weekday/weekend variation, for example.