---
id: github:teqplay/portreporter-backend:issue:1174
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1174
title: Fix That The Getactiveportcalls Gives Cancelled Portcalls From The Past, And
  Make Sure That We Can Limit The Starttime Of The Portcall To 6 Days In The Future
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1174
labels: []
explicit_links: []
---
# Issue #1174: Fix That The Getactiveportcalls Gives Cancelled Portcalls From The Past, And Make Sure That We Can Limit The Starttime Of The Portcall To 6 Days In The Future

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1174  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [4ec9821d9c64...fbcd71783122](https://github.com/teqplay/portreporter-backend/compare/4ec9821d9c64...fbcd71783122)
**Merge commit:** [fbcd71783122](https://github.com/teqplay/portreporter-backend/commit/fbcd71783122)
**Author:** Wouter Naloop
**Reviewers:** Joaquin Marquez Bugella
**Approvers:** Joaquin Marquez Bugella, Wouter Naloop
**Source Branch:** [feat/isps_active_portcalls](https://github.com/teqplay/portreporter-backend/tree/feat/isps_active_portcalls)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2022-10-27T14:01:21.773226+00:00
**Status:** MERGED

Michel received all kinds of portcalls from 2019 and 2020, which he didn’t like when asking for active portcalls.  
And he had a special request for receiving portcalls up to 6 days in the future.   
  
He is the only user of the endpoint so i made the change directly in the controller with the default value

