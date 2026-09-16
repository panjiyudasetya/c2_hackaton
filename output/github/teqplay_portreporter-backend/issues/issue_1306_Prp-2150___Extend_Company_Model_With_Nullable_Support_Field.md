---
id: github:teqplay/portreporter-backend:issue:1306
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1306
title: 'Prp-2150 : Extend Company Model With Nullable Support Field.'
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1306
labels: []
explicit_links: []
---
# Issue #1306: Prp-2150 : Extend Company Model With Nullable Support Field.

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1306  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [10a9eb284805...fd72ac0b2215](https://github.com/teqplay/portreporter-backend/compare/10a9eb284805...fd72ac0b2215)
**Merge commit:** [fd72ac0b2215](https://github.com/teqplay/portreporter-backend/commit/fd72ac0b2215)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Joost Laurman, Gavin den Hollander, Shan Minh Nguyen
**Approvers:** Gavin den Hollander
**Source Branch:** [feat/PRP-2150/extend_company_model_with_support_fields](https://github.com/teqplay/portreporter-backend/tree/feat/PRP-2150/extend_company_model_with_support_fields)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2023-07-05T07:22:03.642267+00:00
**Status:** MERGED

Simple extension of the company model.
Note: because of the inheritance of models, I kept using `var` for the new field. Otherwise I should have to be extending constructors unnecessarily.

