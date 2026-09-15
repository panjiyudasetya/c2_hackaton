---
id: confluence:177963009
source: confluence
type: page
space: TC
title: Frontend / testing approach
author: Damon Asberg
date: '2023-04-19'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/177963009
explicit_links: []
---
# Frontend / testing approach

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/177963009  

## Content

As defined in the meeting on Wednesday 19th April, we have defined the following testing approach / structure:

* Better define tasks with actual Definition of Done criteria before development
* During development of new features, the Q/A can already define certain testing scenarios which he can expect once the development is finish and follow them
* During development, the frontend developer should adhere to a list of best practices

  + “Business logic” and util functions should always have full unit testing coverage
  + Alongside usage of `class` inside JSX code, `id` attributes and `data-xxx` attributes should be set to help the Q/A in creating automated tests later.
  + To be added upon later during the frontend meeting
* Once the development has been completed, a pull request (PR) is created
* After this point, the Q/A can start testing the new feature manually
* Once the PR is approved by developers **and** the Q/A has manually tested and approved the feature, it can be merged.
* After merging the automated testing development can start and end