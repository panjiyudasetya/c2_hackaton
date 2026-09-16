---
id: github:teqplay/portreporter-backend:issue:1301
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1301
title: Prp-2169 Bugfix For Updating User Profile, Checking Id Instead Of E-Mail Now.
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1301
labels: []
explicit_links: []
---
# Issue #1301: Prp-2169 Bugfix For Updating User Profile, Checking Id Instead Of E-Mail Now.

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1301  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [fd72ac0b2215...4b852e8fc45f](https://github.com/teqplay/portreporter-backend/compare/fd72ac0b2215...4b852e8fc45f)
**Merge commit:** [4b852e8fc45f](https://github.com/teqplay/portreporter-backend/commit/4b852e8fc45f)
**Author:** Shan Minh Nguyen
**Reviewers:** Joaquin Marquez Bugella
**Approvers:** Joaquin Marquez Bugella
**Source Branch:** [feature/PRP-2169_updating_user_profile_by_id_instead_of_email](https://github.com/teqplay/portreporter-backend/tree/feature/PRP-2169_updating_user_profile_by_id_instead_of_email)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2023-07-05T07:48:53.492748+00:00
**Status:** MERGED

Tested this with a payload of wrong e-mail and it will catch the error with a Forbidden error.

