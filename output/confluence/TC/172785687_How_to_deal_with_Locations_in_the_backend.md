---
id: confluence:172785687
source: confluence
type: page
space: TC
title: How to deal with Locations in the backend
author: Wouter Naloop (Unlicensed)
date: '2023-03-08'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/172785687
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/172785687
---
# How to deal with Locations in the backend

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/172785687  

## Content

In February 2023 we have had a discussion in the Backend meeting on the model of the Locations.   
  
At this moment in time there are 3 versions used in different projects   
- { lat, lon }  
- { latitude, longitude }  
- { [float, float] } where the first number is longitude and the second is the latitude  
  
The lat lon is preferred for database entries, because it results in less overhead for storing the keys.   
  
After a discussion we decided to use { lat, lon } internally in all backend projects for the following reasons  
- We prefer to use 1 model for all backends   
- There was no preference for one or the other syntax wise  
- A project with a high volume of data already uses this model ( Api Engine’s Ship history)

This requires a change in several projects that are currently using another format, the following rules will apply for those projects:

* We prefer not to make a migration of the database mandatory, but the application interfacing with the database that has old models will have to do a conversion in the layer between the database and the business logic.
* We should preserve all traffic to the frontend to remain as it is currently. This means that we should also return the model we always used to return to the frontend.   
  Example: Portreporter now returns {latitude, longitude} So we expect the frontend to still get that after the change
* Skeleton plugins should contain the Location model for { lat, lon }  
  This so that projects use the exact same class in their api’s