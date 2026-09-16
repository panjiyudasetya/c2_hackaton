---
id: confluence:652148826
source: confluence
type: page
space: TC
title: Add husky with commit and branch naming check
author: Richard van Klaveren
date: '2025-03-04'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652148826
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652148826
---
# Add husky with commit and branch naming check

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652148826  

## Content

# Adding the check for clear commit and branch naming

## 1. Install

First of all you need to install the latest version of husky and make sure the prepare script is set: <https://typicode.github.io/husky/#/?id=install>

## 2. Install the required libraries

We need the commitlint configs and the enforce-branch-name

$ npm install @commitlint/{cli,config-conventional} enforce-branch-name

## 3. Add the branch name script

"scripts": {
...
"branch-name-check": "enforce-branch-name '(hotfix|bugfix|feature)/.+' --ignore '(develop|master)'"
}

## 4. Add commitlint config

Create a file name `.commitlintrc.json`:

{ "extends": ["@commitlint/config-conventional"] }

## 5. Add the husky config

To make sure that husky actually check the commit message and the branch name, before committing we need to notify husky about these scripts:

$ npx husky add .husky/commit-msg 'npx commitlint --edit $1'
$ npx husky add .husky/pre-commit "npm run branch-name-check"