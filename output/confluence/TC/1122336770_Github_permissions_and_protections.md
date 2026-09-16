---
id: confluence:1122336770
source: confluence
type: page
space: TC
title: Github permissions and protections
author: Michel Wilson
date: '2026-02-10'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1122336770
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1122336770
---
# Github permissions and protections

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1122336770  

## Content

# Permissions

* **Organisation owner:** at most 2-3 people
* **Repository admin:** project lead
* **Repository maintainer:** some senior team members, to allow limited repository settings changes, if needed.
* **Read access:** all developers (with possible exceptions for confidential projects)
* **Write access**

  + Option 1: every developer has write and merge access to the repositories.
  + Option 2: project members have write and merge access. Non-project members can create and push to a branch and create pull requests, but they can’t merge them.  
    Given the organisation size, we currently opt for the less complicated first option.

# Branch protection rules

The following protection rules are to be applied to master and develop branches:

* Always require pull requests to merge: no pushes against master and develop
* Review required: at least one positive review is required to be able to merge
* Dismiss stale reviews: if a PR is updated after review, the reviews are dismissed

If possible, we also want to have:

* Status checks required. This means that a succesful build has to be completed, including tests, before merging is possible. To be done: investigate whether this is possible in combination with our use of Github actions and approvals

We currently choose not to have:

* Block force push. In some cases a rebase or commit amendment is useful to have.
* Require conversation resolution. This is not a feature we use actively.
* Linear history. We experimented with this earlier and it was decided that we prefer the approach using merge commits.