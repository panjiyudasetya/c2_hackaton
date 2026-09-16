---
id: confluence:1213988865
source: confluence
type: page
space: TC
title: Vault Usage guide
author: Jamie de Leest
date: '2026-06-16'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1213988865
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1213988865
---
# Vault Usage guide

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1213988865  

## Content

Vault DEV URL: <https://secretsvault.dev.teqplay.dev/>

Vault PROD URL: <https://secretsvault.teqplay.dev/>

# Login

To login to vault with keycloak you need to select OIDC under method and leave Role Blank and then continue with signing in

Figure 1.1: Select Login Method

Figure 1.2: Login screen

# Getting Mongo Credentials

Vault Separates its secrets via Secrets engines for our purposes We split the core-components and projects Mongodb credentials in separate secret engines, there are multiple ways to get access to these credentials.

Because we decided to grant access at the MongoDB instance level rather than per database, you need to authenticate against the admin database. Unless its specified that its the role is only on database level.

## Via the secrets engine

On the landing page you will see a section with all the secret engines you have access to which you can click view on to get access to it

Figure 2.1: Vault landing page

When viewing a secret engine you will be greeted by this screen here you have to paths to get credentials you can use the Get Credentials to select a role and get generated credentials for that role.

Figure 2.1: Secret engine page

Figure 2.1.1: Select Role

Figure 2.1.2: Get credentials

Figure 2.1.3: Credentials

You can also go to the Roles page and view the roles here then by clicking on a role you can then request the credentials.

Figure 2.2.1: Roles page

Figure 2.2.2: Role page

Figure 2.2.3: Credentials

## Quick actions

In the landing page of vault you also have the option to use Quick actions here you can access secret without having to go to the respective secret engine page

Start by selecting the secret engine you want to retrieve a secret from then select a action you want to execute. lastly select the role you want to execute this action for

Figure 3.1: Landing Page

Figure 3.2: Select Secret Engine

Figure 3.3: Select Action

Figure 3.4: Select Role

Figure 3.5: Generate credentials

Figure 3.6: Credentials

# Managing secrets

Vault automatically syncs secrets with kubernetes, to make changes to secrets this needs to be done in vault.

Secrets are stored in KV secret engines each team has there own KV

Figure 4.1: KV secrets engines

the secrets engine themself are are structured based on namespace/application

Figure 4.2: KV namespace folders

Figure 4.3: KV applications

In the applications KV you can find and manage all the secrets for that application by clicking on SECRET

By clicking on “Create new version” you can edit the secrets and add or change values