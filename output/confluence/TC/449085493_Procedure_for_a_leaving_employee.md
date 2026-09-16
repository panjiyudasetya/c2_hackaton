---
id: confluence:449085493
source: confluence
type: page
space: TC
title: Procedure for a leaving employee
author: Damon Asberg
date: '2024-12-05'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/449085493
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/449085493
---
# Procedure for a leaving employee

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/449085493  

## Content

# Procedures for Leaving Employee

When employees leave the following actions need to be taken care of to protect Teqplay:

## OutBriefing:

1. Make sure hour sheets are properly filled in, printed and signed
2. Make sure code hand-over has taken place
3. Hand-over access pass for the office and send the guards a mail to remove physical access
4. Hand-over laptop (has to be wiped by employee itself) and/or other Teqplay properties

## Digital access:

1. Vaultwarden: Remove employee from sharing list in lastpass
2. AWS:

   * Remove employee access from AWS (IAM user & IAM Identity Center User)
   * Remove access keys for S3
   * Remove SSH keys from the access list
3. Remove E-mail address and Google Drive access
4. Remove user from Trello Team and each board separately
5. Remove user from Jira
6. Remove user from BitBucket

   * If a user has created a repository, they will have separate Admin permissions for this repository even when removed. To remove this user completely, go to the [User directory](https://bitbucket.org/teqplay/workspace/settings/user-directory), for the user you want to remove click the … → Actions → Remove.
7. Remove user from GitHub organisation
8. Remove user from Slack channels
9. Remove user accounts/credentials from backend servers through Gatekeeper (e.g. [backend.teqplay.nl](http://backend.teqplay.nl))
10. Remove user accounts/credentials on non-platform based projects (e.g. Port Reporter LIVE/DEV, any projects with Auth0)
11. Remove user accounts from Keycloak projects (as a User + check M2M Connections)
12. Remove user accounts from Keycloak Admin portal
13. Remove user from Grafana
14. Remove user from Apple App Store Connect
15. Remove user accounts from Apple TestFlight app testers (App Store Connect => App => TestFlight => All testers, for each app)
16. Remove user from NPM
17. Remove user from Google Play Console
18. Remove user from <http://Teqplay.com> Wordpress
19. [Remove user, phone number from contact list inside Freshcaller](https://teqplay.freshdesk.com/a/contacts/filters/all)
20. Remove VPN access, see the [OpenVPN](https://bitbucket.org/teqplay/teqplay-wiki/wiki/OpenVPN) wiki page
21. Remove user from Figma
22. Remove user from Miro
23. Remove user from Microsoft Office portal

## Administrative closure:

1. Inform Insurances (verzekeringsinzicht / conceptarbo)
2. Inform de Cijferkamer / Saldad
3. In case of IND, make sure the employee has been signed of(/afgemeld)
4. In case of Lease-a-bike - end the lease before the 20th of the month
5. Communicate end date of employment to pension scheme Aegon
6. Disable user in Hrvey