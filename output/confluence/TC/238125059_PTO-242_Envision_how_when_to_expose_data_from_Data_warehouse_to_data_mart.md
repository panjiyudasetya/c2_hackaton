---
id: confluence:238125059
source: confluence
type: page
space: TC
title: PTO-242 Envision how/when to expose data from Data warehouse to data mart
author: Wouter Naloop (Unlicensed)
date: '2023-12-05'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/238125059
explicit_links:
- jira:PTO-242
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/238125059
---
# PTO-242 Envision how/when to expose data from Data warehouse to data mart

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/238125059  

## Content

### Goals

Think of a way to let the data flow to the Datamart without needing to recreate the entire datamart every time (Partial updates)

### Topics

* How up to date do we want the data to be?  
  Weekly
* Is it good to do it by port?  
  We can add a filter in the transformation tool to reduce the amount of ports we calculate when going for a push based approach. With the architecture in the image it should also be
* Can we find a way to reduce the need for validation

This is what we talked about the most, we think it should be possible to send data to the datawarehouse straight away if we have an automated validation mechanism that checks basic rules the data should conform to.   
An initial architecture sketch could be like the following image.

Key points about the image

* The Events and revents can both be used for the calculation.  
  Revents would be used to get older data or for redoing data that we deem not good enough
* Automatic validation.   
  In between the sources and events we have the transformation tool (ETL, currently kotlin) which transforms the data in valid input for the datawarehouse. This data will then be validated without a man in the middle.   
  This validation process will on success send the data to the database. On error it will be collected in a error bucket
* Error bucket  
  All the visits that have been incorrectly transformed need to be collected somewhere. It is not discussed what this exactly looks like. But it should be possible to redo those visits with revents at a later time once the issues are fixed.
* Triggers between Data warehouse and   
  To get the data from the datawarehouse into a more business focussed representation in the datamart we need a trigger. For datamarts that have the same or more fine granularity we can use the trigger   
  - When a port visit enters the   
    
  But for datamarts that span over multiple port visits we should introduce individual triggers