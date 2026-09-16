---
id: confluence:206143489
source: confluence
type: page
space: TC
title: How to fix vesselvoyage if a port was not mapped (properly) before
author: Richard van Klaveren
date: '2023-08-20'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/206143489
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/206143489
---
# How to fix vesselvoyage if a port was not mapped (properly) before

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/206143489  

## Content

How to deal with ports that are made bigger or were unknown before, so no valid port arrival / departure has been detected, and the visit in vesselvoyage is not in-line with the current knowledge

**The problem:**  
In vesselvoyage the ports that were not correctly defined but are now, have the problem that they don't have  
visits or not all visits. This can happen due to that the port did not encompass all terminals. If they are later expanded, the area events which vesselvoyage uses as a base don't exist.

This results in PTO missing data on several ships that they have been to a terminal at all or partially

**Answer:** The area events can be filled in by using Revents.

The idea we came up with was that there would be revents running for the ports that are affected.  
Those revents would be inserted into a clone of vesselvoyage that is running with only the events coming  
out of revents.

That vesselvoyage clone can then be used for the PTO purposes or a mechanism could be developed to merge the new data into the original vesselvoyage.

The concept of being able to trigger this from another perspective than PTO was agreed, and also the concept of merging (by generating a revents based only version of vesselvoyage for the involved ships, and merge then only those timeframes in there related to the visit of that portcall. This way of merging could also be seen as an option of the revents themselves into the operation live events in EventHistory, in order to prevent extreme complex (and untraceable) merge operations