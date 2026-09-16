---
id: confluence:199983140
source: confluence
type: page
space: TC
title: Stage environment set-up
author: Joaquin Marquez Bugella
date: '2023-09-04'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/199983140
explicit_links: []
---
# Stage environment set-up

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/199983140  

## Content

For the purpose of envisioning the required steps to create a reliable and not impactful Stage environment, I create this page.

Points to consider:

* Backend & DB hosting

  + Same or different EKS cluster?
* URLs
* Data synchronization: scheduled daily and by-request sync?

Here it is a list of external (to PortReporter) services to consider:

| **Service** | **Connection Type** | **Data direction** | **Purpose (if not obvious)** | **Comment & considerations** | **Actions** |
| --- | --- | --- | --- | --- | --- |
| SmartFleet | REST api | In/Out | Smartfleet CRUD operations.  SF events are driven by the SF queue. | After some envisioning sessions and talks, we will use live, using a different domain. The details will be described after finishing the card in ***actions***. | Jira issue PRP-22375c406517-69e9-3c5d-b831-d2bed7d442a4System JIRA |
| Communication - email, voice & push service | Library | Out | To notify portcall & SFEvents and send custom emails. | No need to configure the external services, but the flags to prevent their use (see actions).  Mail templates should be the live ones. | To enable `notification`’s `email`, `sms`, `phone` & `push`  To set `newUserRegistrationTemplateId` & `subscriptionEmailTemplateId` the same as live  To set `notification.debugPrefix: '[STAGING]'`  To set `notification.alertEmails: developer+staging@teqplay.nl` |
| Exact | REST api | In/Out | Keep track of exact invoice accounting. | It seems not relevant for staging unless attempting to test the ExactLogic. | Disabling it by now.  Check again when getting |
| SmartFleet queue | Queue consuming | In | To consume SF events. | New queue `SmartFleet-Notifications-Staging` created in live rabbitmq server that will be bound to exchange `SmartFleet-Notifications` | added to configmap  Bind queue to exchange when ready |
| AIS queue | Queue consuming | In | To consume Portcall events. | New queue `PORTREPORTING_STAGING` created in live rabbitmq server that will be bound to exchange `PORTREPORTING_LIVE` | added to configmap  Bind queue to exchange when ready |
| Vopak queue | Queue consuming | In | Receive additional agent information for Vopak (Wilhelmsem) | rabbitmq.vopakConsume: 'true' rabbitmq.vopakQueuename: teqplay\_out\_staging | added to configmap  Bind queue to exchange when ready |
| Portcall Nominations queue | Queue consuming | In |  | New queue `Scrapeshark-Nominations-Staging` created in live rabbitmq server that will be bound to exchange `Scrapeshark` | added to configmap  Bind queue to exchange when ready |
| NxtPort | REST api | Out | Send a subset of incoming portcallEvents (using the alias) to NxtPort following some logic (ports, alias sources, even types…) | **Disabled**. | added to configmap |
| Platform Authenticator | REST api | In/Out | Authenticate CRUD operations. | Access to live would imply the risk of a bug corrupting or deleting users.  Unrelated: Admin credentials are in the properties! | Pointing to **DEV** in the configmap.  **Todo:**  However we should prevent write access (in case of an undiscovered potentially harmful bugs, i.e. password resetting the wrong user/s or even deleting in live). |
| CSI | Skeleton library | In | Static Ship information | To Live | pointing to live in the configmap. |
| POMA | Skeleton library | In | Static Port Infrastructure information | To Live | pointing to live in the configmap. |
| VesselVoyage | Skeleton library | In | Historical voyage information. | To Live | pointing to live in the configmap. |
| Portcall+ | REST api | In/Out | * Enrich portcall information (when retrieving data). * Creating or nominating portcalls | This makes it complicated to address Live Portcall+ Out methods:  PortcallLogic:1213: `portcallPlusConnection.getOrCreatePortcall(request)`  `(endpoint /v2/portcalls/getOrCreate)`  PortcallLogic:1263: `portcallPlusConnection.nominatePortcall(request)`  (endpoint `/v2/portcalls/nomination`) | currently pointing to dev in the configmap.  **Todo:**  Put in place a mechanism to prevent staging actions to create Portcall+ portcalls or nominate portcalls. PRP-22325c406517-69e9-3c5d-b831-d2bed7d442a4System JIRA  We need to decouple the credentials as they’re shared with the **Platform** service, preventing us from addressing different environments. PRP-22335c406517-69e9-3c5d-b831-d2bed7d442a4System JIRA  point to live when portcallplus is merged to live. |
| Portbase | REST api | Out | To push portcall orders to portbase | Called on endpoint request.  Not relevant for stage environment, hence, **it should point to dev as there’s no enabling flag.**  `externalConnection.portbaseUrl: https://api.kt.portbase.com/` | added to configmap, but with a dev url |
| Platform | REST api | In |  | Linked to Portcall+ service as credentials are shared. | Same as second point of Portcall+ |
| Vopak sync | REST api | Out |  | **Disabled**. | added to configmap |
| Lineup service | REST api | In/Out | Unused? |  | check if it should be set up |
| Simply5 | - | - | - | I seems not used anymore. | - |
| TMA | - | - | - | I seems not used anymore. | - |

## Additional settings:

### Spring scheduled tasks

Need to check which tasks should be enabled or not, such as alias updater or invoicing cycle (todo: make a list)

### Invoice settings

Special email accounts to be notified set to  email:

invoice.defaultEmails: francisco@teqplay.nl
invoice.financialAdministrationEmails: francisco@teqplay.nl
invoice.vopakEdiEmailAmsterdam: francisco@teqplay.nl
invoice.vopakEdiEmailAntwerp: francisco@teqplay.nl
invoice.vopakEdiEmailRotterdam: francisco@teqplay.nl
invoice.vopakEdiEmailTerneuzen: francisco@teqplay.nl
invoice.vopakEdiEmailVlissingen: francisco@teqplay.nl
invoice.vopakEdiBccEmails: francisco@teqplay.nl
invoice.wilhelmsenEdiEmailAmsterdam: francisco@teqplay.nl
invoice.wilhelmsenEdiEmailAntwerp: francisco@teqplay.nl
invoice.wilhelmsenEdiEmailRotterdam: francisco@teqplay.nl
invoice.wilhelmsenEdiEmailTerneuzen: francisco@teqplay.nl
invoice.wilhelmsenEdiEmailVlissingen: francisco@teqplay.nl
invoice.wilhelmsenEdiBccEmails: francisco@teqplay.nl
trial.adminEmails: francisco@teqplay.nl

invoicing cycle

 invoice.financialAdministrationEmails: developer+staging@teqplay.nl
invoice.nominationBased: 'true'

Watch out with the companies invoice mails, they can’t be sent to the actual companies!

Daily exported reports

### They are sent by email

check their scope (users will receive the reports when registered in the collection `shipReportSubscription`

### AWS settings for the changelog feature

`aws` fields & `changelog.aws.folder`

### portreporter urls

 internalConnection.backendBaseUrl: https://backendportreporter.teqplay.nl
internalConnection.baseUrl: https://portreporter.teqplay.nl

### Slack webhooks

They should be duplicated

### Unclassified settings

`notification.debugPrefix` set to `staging`