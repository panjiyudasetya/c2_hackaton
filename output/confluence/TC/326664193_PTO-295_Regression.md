---
id: confluence:326664193
source: confluence
type: page
space: TC
title: PTO-295 Regression
author: Richard van Klaveren
date: '2024-04-10'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/326664193
explicit_links:
- jira:PTO-295
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/326664193
---
# PTO-295 Regression

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/326664193  

## Content

### Attendees of the envision

* Maryam
* Richard
* Wouter

### Purpose of the Envision

To make sure our pipelines are doing what we want. We need to ensure that what we made in the past keeps working as it was designed. We should be able to make a decision on a regression in quality, which can only be done if we know what the reggression is.

### Envision

In real-life there are 3 main reasons why data patterns start differentiating from previous data patterns:

1. **Context changes**: If context is newly added or updated, this will have an effect on the timestamps being determined based on these changes. Examples, making a Anchor area larger, mapping a ship as ‘pilot’ or changing the port border.
2. **Algorithm changes**: If the algorithms change (because a new situation that was not properly covered before was encountered) or even the definitions used as an input for these algorithms change, it will have impact on the detections.
3. **Operational changes**: if the customer decides (hopefully inspired by our tool) to change their behavior.

We want to get insights in operational changes in an experiment context with our customer, and to not pollute the results we should limit the context and algorithm changes,

There are a few things that we can test on that.

* The cause and effect of configuration/infrastructure changes.   
  This means that we would make a comparison between for example a Pilot Boarding Place definition change.
* The difference between features  
  A comparison between dev and live in the exact resulting lines
* Nightly runs of the same scenario
* A change in characteristics of the data  
  Taking averages of the dataset of one or multiple Reports, here we would be taking the same port with the same time frame to have a comparable result. And compare the averages/means of the data to see if before and after are comparable

One method does not exclude the other

For now we agreed to execute this at the batch level, but in the future there will be another element that will need to be discussed. And that is how do we guard against regression when doing push based processing of port visits.

We want to do nightly runs of a stable scenario that we validated.  
Where a stable scenario means that we always run the same parameters for Port, and timeframe

Here we want to use the method of storing all data versioned, and keep a human in the loop who will do the pruning of the database after validating on a regular basis.

This human in the loop can have a dedicated BI dashboard in which it should be easy to detect changes in 2 different runs.

By having the human in the loop and keeping versioned data, we want to have awareness of what our changes in code and infrastructure change in the resulting quality of the data. By doing it nightly we can keep the changes that occurred during runs minimal, therefore limiting the places we have to check if we find problems in the newer reports.

We noted we can do 2 different kind of approached to do the comparison:

* Keep all rows of the old and new scenario, and do the comparison row-by-row to detect the refression
* Keep the characteristics of each parameter (e.g. steaming in) like median, max, min and spread over the whole dataset and compare the characteristics of the new dataset against the characteristics of the old data set.

We opted for storing all rows of the stable scenario for now because that enables us to check which visits have changed more easily than the characteristics approach would allow us to do.