---
id: confluence:153747457
source: confluence
type: page
space: TC
title: Authentication
author: Leon Joosse (Unlicensed)
date: '2022-11-24'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/153747457
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/153747457
---
# Authentication

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/153747457  

## Content

Data Store allows users to login with username/password and several ‘social’ identity providers via Auth0.

# Login via socials

## Google

To be done

## LinkedIn

**The key + secret will expire after 2 months! Make sure to renew in time!**

1. Log in with a LinkedIn account to LinkedIn Developers: [https://developer.linkedin.com](https://developer.linkedin.com/)  
   (linking to Teqplay happens later on, so can be any account)
2. Go to My Apps
3. Create or use the datastore app
4. Use the Auth tab to retrieve the key + secret for Auth0:

   1. Key: use the ClientID
   2. Secret: use the Client Secret
5. Make sure to set the callback URL, that redirects the user after successful login to the datastore:

   1. Go to Auth > OAuth2 settings
   2. Set the 'Authorized redirect URLs' to `https://teqplay.eu.auth0.com/login/callback` (when Auth0 tenant is `teqplay`)

To let the app appear a part of Teqplay LinkedIn page, let the Teqplay Page admin allow it. See here for explanation: <https://www.linkedin.com/help/linkedin/answer/a548360>

### Microsoft

**The key + secret will expire after 2 years! Make sure to renew in time!**

Manage the app via [https://portal.azure.com/](https://portal.azure.com/#home), using d[eveloper@teqplay.n](mailto:developer@teqplay.nl)l:

* Go to <http://entra.microsoft.com>
* Login with [developer@teqplay.nl](mailto:developer@teqplay.nl)
* Menu on the left: go to App registrations
* You’ll find the ‘Teqplay Data Store’ there
* To get key + secret for Auth0:

  + Key: use the value of 'Application (client) ID, as seen in the App registration overview
  + Secret: In the app registration: go to Certificates & secrets. Use the value from the **Values** column!