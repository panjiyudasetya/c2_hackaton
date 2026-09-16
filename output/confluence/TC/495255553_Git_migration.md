---
id: confluence:495255553
source: confluence
type: page
space: TC
title: Git migration
author: Joaquin Marquez Bugella
date: '2024-11-11'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/495255553
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/495255553
---
# Git migration

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/495255553  

## Content

none

# Introduction

This page set encompasses migration of our codebase and CI/CD artifactories.

It will serve, not only for the migration itself, but as the basis to understand our CI/CD policy for current or new projects.  
Thus, the how-to guides follow a pedagogic and evolutive step-by-step approach from a basic to detailed scripts set, so the reader could understand the details and reasons for each decision taken (now and in the future).  
 Beware that this will produce a document length longer than just plainly display the final scripts.

# Migration motivation

**CircleCI service disruptions** have increased in number since it was adopted.

**Centralization** of CI/CD and codebase repositories, which are tightly connected, but currently split in separated providers (CircleCI and Bitbucket respectively).

**Newer features in our git repository provider** so we enjoy more agile means to be more productive.

# Confluence page set

true

# Plan overview and steps

In a first glance, the steps will be commanded **by their dependencies**: migrating in the first place the codebase, followed by the CI/CD pipeline artifactory.

An inventory of projects will be made, including an action plan by project, with a candidates list to carry out the migrations.

Note that the Front-end and Back-end migration don’t pose any dependency, but it’d be desirable both are migrated at the same time (for a good peace of mind).