---
id: confluence:1213104129
source: confluence
type: page
space: TC
title: Setup New Mongo Instances with vault
author: Jamie de Leest
date: '2026-05-18'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1213104129
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1213104129
---
# Setup New Mongo Instances with vault

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1213104129  

## Content

When setting up a new mongo instances it will automatically be created a set of vault-admin credentials use this credentials with the setup-db.py in the kubernetes-scripts/hashicorp-vault

this script uses some environment variables that can be passed with a env file

wide760VAULT\_ADDR=https://secretsvault.dev.teqplay.dev/
VAULT\_TOKEN=
VAULT\_ADMIN\_PASSWORD= 

the setup-db.py has 3 arguments that need to be passed with it

wide760setup-db.py <secret-engine-path> <connection-name> <mongo-url> \
--env-file ".env" \
--vault-admin-username vault-admin