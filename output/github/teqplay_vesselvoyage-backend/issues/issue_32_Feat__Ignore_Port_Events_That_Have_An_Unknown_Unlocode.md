---
id: github:teqplay/vesselvoyage-backend:issue:32
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 32
title: 'Feat: Ignore Port Events That Have An Unknown Unlocode'
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/32
labels: []
explicit_links: []
---
# Issue #32: Feat: Ignore Port Events That Have An Unknown Unlocode

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/32  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [95af082344c1...641fff366137](https://github.com/teqplay/vesselvoyage-backend/compare/95af082344c1...641fff366137)
**Merge commit:** [641fff366137](https://github.com/teqplay/vesselvoyage-backend/commit/641fff366137)
**Author:** Jos de Jong
**Reviewers:** 
**Approvers:** Former user
**Source Branch:** [fix/SPV-305_filter_events_with_invalid_port](https://github.com/teqplay/vesselvoyage-backend/tree/fix/SPV-305_filter_events_with_invalid_port)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2021-12-09T07:40:15.229057+00:00
**Status:** MERGED

There are some historic area events which have a wrong unlocode. Here is one example \(only on the live server not on dev\):

[https://vesselvoyage.teqplay.nl/#/ships/8913447/story](https://vesselvoyage.teqplay.nl/#/ships/8913447/story)

In this case there are events for a wrong unlocode DEBRVR at 2021-09-20. This results in an ugly story of the vessel. 

This PR will make sure these wrong historic events are ignored. Since the application is now more strict about this, I had to fix some unit tests that where working with non existing ports :grin: .

