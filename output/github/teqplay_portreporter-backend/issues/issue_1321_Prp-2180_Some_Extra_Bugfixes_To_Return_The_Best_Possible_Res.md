---
id: github:teqplay/portreporter-backend:issue:1321
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1321
title: Prp-2180 Some Extra Bugfixes To Return The Best Possible Results.
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1321
labels: []
explicit_links: []
---
# Issue #1321: Prp-2180 Some Extra Bugfixes To Return The Best Possible Results.

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1321  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [5e066a120447...87661459ecd8](https://github.com/teqplay/portreporter-backend/compare/5e066a120447...87661459ecd8)
**Merge commit:** [87661459ecd8](https://github.com/teqplay/portreporter-backend/commit/87661459ecd8)
**Author:** Shan Minh Nguyen
**Reviewers:** Wouter Naloop, Joaquin Marquez Bugella
**Approvers:** Joaquin Marquez Bugella
**Source Branch:** [feature/PRP-2180_additional_bugfixes_for_csi_to_platform_info](https://github.com/teqplay/portreporter-backend/tree/feature/PRP-2180_additional_bugfixes_for_csi_to_platform_info)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2023-08-07T08:21:48.145750+00:00
**Status:** MERGED

Found out after testing on develop that the previous PR did not give the exact results I expected \(almost exacty\).  
Needed this extra bug fix to get it right.  
Not sure if I need to add unit tests as it’s more dependent on the external connection results \(CSI/Platform\).

