---
id: confluence:257359875
source: confluence
type: page
space: TC
title: Using Auth0 in local development environment
author: Joost Laurman
date: '2024-01-18'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/257359875
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/257359875
---
# Using Auth0 in local development environment

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/257359875  

## Content

Prerequisites:

* Insomnia REST client
* [Global Headers extension](https://insomnia.rest/plugins/insomnia-plugin-global-headers)
* Auth0 application is setup (aka working dev environment)

## Setup the Authentication request

* Setup a new request, pointing towards the login call of your application

  + Setup OAuth 2.0 auth type
  + Grant type: `Implicit`
  + Authorization url: `https://teqplay.eu.auth0.com/authorize`
  + Client ID: `Copy client id from Auth0 console`
  + Redirect url: `http://localhost:3000` or something that has been already added to Auth0 allowed callback urls
  + Response type: `ID and Access Token`
  + Scope: `openid email`
  + Audience: `<<backend url>>`

* Now test out if the OAuth 2.0 connection works with the `Fetch Token` button. Login with your Auth0 credentials and you will retrieve a `Identity Token` and an `Access Token`.
* Setup JSON body inside this request with Oauth 2.0 response as parameters

* Do the call and you should be able to retrieve your actual token to use within your application!

## Setup Global Headers extension

To re-use the token in all requests that we have, we use the Global Headers extension (as mentioned in the prerequisites. Setup your `Base Environment` as the picture below:

You are using the response from the authentication request to fetch the token. You can also make sure this way to refresh the token automatically when it’s invalid.

In each folder in your Insomnia project you can say to use the `Global Headers`.

Now each request in the `voyages` folder will use the token automatically.

All ready and set to go!