---
id: confluence:652116018
source: confluence
type: page
space: TC
title: Setup m2m connection on KeyCloak
author: Richard van Klaveren
date: '2025-03-04'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652116018
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652116018
---
# Setup m2m connection on KeyCloak

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652116018  

## Content

# Setup m2m connection on KeyCloak

Go to <https://keycloakdev.teqplay.nl/auth/> and login on the **Administration Console**

With the following set up you can use 1 client id and secret to connect to all the Audience's you have specified in your Mappers

# Creating a new M2M client for a new server

1. Select the realm **dev**
2. Configure > Clients
3. Press the **Create** button in the top right to add a new client
4. Write in **Client ID** the name of the application in lowercase (keep everything else default)
5. Set **Access Type** to **confidential**
6. Enable **Authorization Enabled**
7. Set the **Valid Redirect URIs** to `http://localhost:8080/*` (we won't be using this, but it is required)
8. Save the changes

# Configure client-side

1. Select the client who is at the client-side
2. Open the **Mapper** tab
3. Press the **Create** button in the top right to add a new client
4. At **Mapper Type** select **Audience**
5. At **Included Client Audience** select the server you want to connect to
6. Give the mapper a proper name for example `Audience APPLICATION_NAME`

# Generate a secret for you client

1. Select the client you want to create a secret for
2. Go to the **Credentials** tab
3. In **Client Authenticator** make sure it is set to **Client Id and Secret**
4. In the **Secret** field you will find you **Secret**

NOTE: the Client ID is the one specified in the **Client ID** field on the **Settings** tab