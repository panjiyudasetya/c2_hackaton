---
id: github:teqplay/portreporter-backend:issue:1108
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1108
title: Feat/Alongside Events Unfinished
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1108
labels: []
explicit_links: []
---
# Issue #1108: Feat/Alongside Events Unfinished

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1108  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [e464fdedb66b...7ca9eb26cbc1](https://github.com/teqplay/portreporter-backend/compare/e464fdedb66b...7ca9eb26cbc1)
**Merge commit:** [7ca9eb26cbc1](https://github.com/teqplay/portreporter-backend/commit/7ca9eb26cbc1)
**Author:** Wouter Naloop
**Reviewers:** Joaquin Marquez Bugella
**Approvers:** Joaquin Marquez Bugella
**Source Branch:** [feat/alongside_events_unfinished](https://github.com/teqplay/portreporter-backend/tree/feat/alongside_events_unfinished)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2022-07-13T10:29:21.364517+00:00
**Status:** MERGED

We found out that for singapore for example we had alot of unfinished Alongside events 

With unfinished i mean 


We detected that a bunker ship came alongside, but never detected that it left. 
Or the other way around.


We found out that it had to do with the ais points we have available. 
When detecting events we compare the last ais points we have of each ship. Sometimes that can be up to 3 hours of no ais when only receiving sattelite data. 

In that case we give the event a lower probability. And in platform we say that if the probability is too low we don't send the event to portreporter. 

This means that at the cutoff point of too low probability or just enough we could have one being sent and the other one not. In that case we have a incomplete overview in Portreporter and we decided that if the ship leaves the port we would clean up all incomplete alongside events. 

Clean up means in this case remove from the statusevents, this makes it so that it does not show up anymore in any dashboard or SOF

