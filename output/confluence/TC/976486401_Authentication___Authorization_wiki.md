---
id: confluence:976486401
source: confluence
type: page
space: TC
title: Authentication / Authorization wiki
author: Joost Laurman
date: '2026-03-26'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/976486401
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/976486401
---
# Authentication / Authorization wiki

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/976486401  

## Content

Work in progress document

16falsenonelisttrue

### Platform (backend/backenddev)

* Create user in Gatekeeper ([https://gatekeeper.teqplay.nl](#)) with the right authorization groups (`ALL_RIGHTS` group) in there
* Edit user in database, set `isAdmin` to `true`
* Restart platform (bug, since it’s caching userProfiles)

### Internal API /v0 endpoint (to platform)

* Create user in `platform` realm
* Create user in Gatekeeper ([https://gatekeeper.teqplay.nl](#)) with the right authorization groups (`ALL_RIGHTS` group) in there
* Backend creates own Service to talk to internal-api with that username and password

Look at **terminalplanner** for implementation

### Internal API /v1 endpoints

* Create client in `dev` or `prod` realm
* Add `clientId` to specific applications you want to get data from (e.g., ship-history, csi, poma). This is done in the `keycloak_s2s_connections` collection

### Giving developer access to certain namespace

* Go to Keycloak DEV or PROD
* Go to `kubeapps` realm
* Create `User` if the developer has none yet
* Open this user and go to `Groups`
* Add user to the required namespace by clicking `Join group` and selecting the namespace, e.g. `brokers`

### Giving access to Keycloak itself

* Go to Keycloak DEV or PROD
* Go in the `master` realm
* Create user by email address
* Assign right `Role Mapping` → assign Realm role → e.g. `admin`

### Giving access to Grafana

* Go to Keycloak DEV or PROD
* Go in the `kubeapps` realm
* Create user by email address and set temporary password

### Giving user access to certain application

* Go to Keycloak DEV or PROD
* Go in the `dev` or `prod` realm
* Go the the `Users` page
* See if there is already an user with this username.

  + If so, you are all set
  + If not, create a user
* So the desired application’s database
* Go the `users`and add a user with either `ROLE_ADMIN` or `ROLE_USER`. For example:

  json{
  "username": "developer\_name@teqplay.com",
  "roles": ["ROLE\_ADMIN"]
  }

### Giving M2M access the generic way

The most recent applications have a common way of giving M2M access. This applies to basically everything but Portreporter and PortcallPlus.

* Go to Keycloak DEV or PROD
* Go into the `dev` or `prod` realm
* Create a client for the application you want to give access to
* Create client

  + Client authentication: ON
  + Authorization: ON
  + Authentication flow:
* Go the tab ‘Client Scopes’

  + Now you grant here the client scopes that you want your application to have access to. For example `csi`
* Go to the desired application database, find a `keycloak_s2s_connections` table and add your application as an entry
* Make sure the `clientId` and `clientSecret` are correctly setup in the backend project

### Giving M2M access to PortReporter

* Go to Keycloak DEV or PROD
* Go in the `portreporter` realm
* Create client

  + Root URL: `https://portreporterdev.teqplay.nl`
  + Home URL: `/index.html`
  + Valid redirect URIs: `https://portreporterdev.teqplay.nl/*`
  + Valid post logout redirect URIs: `https://portreporterdev.teqplay.nl/*`
  + Web origins: `https://portreporterdev.teqplay.nl`
  + Admin URL: `https://portreporterdev.teqplay.nl`
  + Client Authentication: ON
  + Authorization: OFF
  + Authentication flow:

    - Standard flow
    - Direct access grants
    - Service account roles
* When created the client, go into client scopes

  + Add client scope `portreporter-dev-be-audience`
  + Now click on the `portreporter-dev-portcallreports-dedicated` (or something similair)
  + Add these predefined mappers:

    - client roles
    - realm roles
  + Create these ‘By configuration’ mappers:

    - Type: User Session Note  
      Name: Client ID  
      User Session note: `client_id`  
      Token claim name: `client_id`  
      Add to ID token: ON  
      Add to access token: ON  
      Add to token introspection: ON  
      Rest turned off
    - Type: User Attribute  
      Name: email  
      User Session note: `client_id`  
      User attribute: `portcallreports`  
      Token claim name: `email`  
      Claim JSON Type: `String`  
      Add to ID token: ON  
      Add to userinfo: ON  
      Add to token introspection: ON  
      Rest turned off
    - Type: Hardcoded claim  
      Name: email-overwrite  
      User Session note: `client_id`  
      Token claim name: `email`  
      Claim value: `portcallreports@teqplay.nl`  
      Claim JSON Type: `String`  
      Add to ID token: ON  
      Add to userinfo: ON  
      Add to token introspection: ON  
      Rest turned off

### Giving M2M access to Portcall Plus

* Go to Keycloak DEV or PROD
* Go in the `dev` realm
* Create client

  + Client authentication: ON
  + Authorization: ON
  + Authentication flow:
* Go the tab ‘Client Scopes’

  + Add client scope → add `api`
  + Add client scope → add `portcallplus`
* Make sure the clientId and clientSecret are correctly setup in the backend project

### **Setting up a new project in Keycloak**

This covers adding a new project as a client in an existing realm in DEV or PROD.

**Create the client**

* Go to Keycloak DEV or PROD
* Go into the dev or prod realm
* Go to Clients → Create client
* Set a descriptive Client ID, e.g. `my-new-project`

  + Client authentication: ON
  + Authorization: ON
  + Authentication flow:

    - Standard flow
    - Direct access grants
    - Service account roles
  + Set Root URL, Valid redirect URIs, and Web origins to the project's URL

**Grant client scopes**

* Go to the tab Client Scopes
* Add the relevant scopes your project needs access to, e.g. `csi`, `portcallplus`

**User (human) access**

* Go to the Users page in the dev or prod realm
* Check if the user already exists

  + If so, you are all set
  + If not, create a user
* Go to the project's database and add the user to the users collection with the appropriate role:

jsonwide760{
"username": "developer\_name@teqplay.com",
"roles": ["ROLE\_ADMIN"]
}

**M2M / Service account access**

* After creating the client (see above), go to the project's database and find the `keycloak_s2s_connections` collection
* Add an entry for your new client, making sure the `clientId` and `clientSecret` match what was generated in Keycloak
* Make sure the `clientId` and `clientSecret` are correctly configured in the backend project

**Repeat for PROD**

* Repeat all of the above steps in the PROD environment, using production URLs and credentials