---
id: confluence:296288270
source: confluence
type: page
space: TC
title: PortReporter new Keycloak flows
author: Shan Minh Nguyen (Unlicensed)
date: '2025-01-30'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/296288270
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/296288270
---
# PortReporter new Keycloak flows

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/296288270  

## Content

For the migration of PortReporter authenticator to Keycloak, we will have to change some existing workflows in PortReporter.  
Disable authentication of the old ways by Authenticator.  
  
Current login with Authenticator has to be modified to still verify and migrate existing users but still not authenticate these users as they may not have migrated their account to Keycloak yet.  
Once in the future all users have been migrated to Keycloak, we can deprecate this endpoint and remove this endpoint eventually.  
  
We can work with Keycloak either by a REST API endpoint or through the Java Objects provided by their documentation and save them by the provided Java methods.  
  
Currently we replace the tokens returned from Keycloak with a custom token. This cannot be used to Keycloak anymore, but the way it is setup now, this can easily be modified in the plugin to return the Keycloak token without updating PortReporter code.  
PortReporter will work as long as the authentication to Keycloak does not raise an error, thus however the tokens look like, will authenticate the user (based on what the token contains of the user profile).

# Login to PortReporter

With the new adjustments, we’ll always have to return an error with a message.  
As we cannot directly login the user to Keycloak, we’ll only create a user and send them a password link after which they need to login to the new LoginWithKeyCloak method.   
This can be done using an endpoint (POST) /admin/realms/{realm}/users (found here <https://www.keycloak.org/docs-api/24.0.1/rest-api/index.html#_users> ) with a M2M connection that has to be setup beforehand in the configuration or can be done without through the keycloak admin client java package to connect to the Keycloak backend server.  
  
Once the step with Login to PortReporter is done by the existing end users, we can continue with the next step Login with Keycloak assuming they updated their Keycloak admin client account with their password.

# Login with Keycloak

The new flow consists of users logging into Keycloak through the frontend where the result should be that the frontend will only pass Keycloak tokens (idToken & access token) to the FE which will be validated by the PortReporter backend to Keycloak exchanging a new token.  
The main purpose is to avoid sending any user credentials in the request directly to PortReporter.  
After the validation check has been completed, we can authenticate the user in PortReporter and store the access key in our database.  
With the refreshToken stored in the database we can get a new access token from Keycloak.

# Add user

Adding users should be done likewise the step Login to PortReporter.  
Using (POST) /admin/realms/{realm}/users we can add a user and send an e-mail to set the password.  
A password cannot be set as it as of this version 23.0.1 it currently requires Keycloak to sent a password reset link.

# Delete user

# Password reset

Contrary to the other steps, resetting a password has two flows for resetting a password of a user.

The above image shows the flow for any user wanting to login but forgot their password and triggering a password reset.  
The following shows the one as an Admin that wants to reset a password for another user in PortReporter.

The endpoint that can be requested for the above flow through the backend is   
PUT /admin/realms/{realm}/users/{user-id}/reset-password

# M2M tokens

I’ve also ensured that by using the normal login authentication that we’re able to also authenticate by machines.  
  
This is done by creating a custom client where in the mapper a hardcoded claim is made by overwriting the e-mail with a value mapping the e-mail to a user in portreporter.  
  
An example below for smartfleet M2M

This can be tested with the following details (lookup client\_id and client\_secret in keycloak environment)

The returning token can then be authenticated to the following endpoint

This should if the backend side has been configured properly to successfully authenticate a machine.