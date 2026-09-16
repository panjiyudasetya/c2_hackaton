---
id: confluence:452165635
source: confluence
type: page
space: TC
title: Keycloack add a S2S connection to internalApi
author: Richard van Klaveren
date: '2024-09-03'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/452165635
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/452165635
---
# Keycloack add a S2S connection to internalApi

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/452165635  

## Content

In this short manual, we will provide an overview on what steps are required to add a Server 2 server connection via Keycloak to access (via the internalAPI) the internal components like Poma, CSI and VesselVoyage.

1. Go to the [keycloak admin console](https://keycloak.teqplay.nl/auth/admin/master/console/) and login as an administrator
2. Select ‘prod’ as the realm and select ‘clients’ to show the existing S2S connections.

3. Click ‘Create client’ to create a new client and fill-in a client-id (no spaces, camelcase please) and optionally a name and description.

4. Select Next and enable ‘Client Authentication’ and ‘Authorization’

5. Click Next, no values need to be changed in the Login settings. So, click ‘Save'

6. Now access needs to be provided, so select the just created client and select ‘client scopes’ tab.

7. Click ‘add client scope’ and select the client scopes you want to add by selecting ‘poma’, ‘csi', ‘vesselvoyage’ and ‘api’ for access via the internal api). Finalize with clicking on ‘Add’

8. Now the user is created in keycloak, the ‘ClientId’ and ‘Client Secret’ are displayed when you select ‘credentials’. Make sure they are added in the relevant place in BitWarden

9. Do not forget to also add the ‘authorization’ to the relevant applications via Mongo in the relevant databases using the ‘keycloak\_s2s\_connections’ collection.

10. You’re all set now!