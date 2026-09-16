---
id: confluence:652345345
source: confluence
type: page
space: TC
title: Global ETA Predictor
author: Richard van Klaveren
date: '2025-03-04'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652345345
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652345345
---
# Global ETA Predictor

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652345345  

## Content

# Requirements

* Calculate ETA from any position to any position

# Envisioned Solution

* One main entry point
* Run as a separate service
* split ETA problem in 2 parts

  + determine route
  + determine travel time
* Multiple predictors which are optimized for a specific case
* selector which chooses between multiple predictors

  + each predictor should be able to give an estimate on how good it is at calculating the ETA
  + Should be possible to select a specific one

# First Steps

* Start with something in the platform (keep in mind that it should be possible to move it outside of the platform)
* Selector which always selects RouteScout to determine route
* Use constant speed to calculate travel time / arrival time