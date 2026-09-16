---
id: confluence:410255417
source: confluence
type: page
space: TC
title: Authorization Matix
author: Minh Trang Nguyen (Unlicensed)
date: '2024-08-08'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/410255417
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/410255417
---
# Authorization Matix

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/410255417  

## Content

| **User** | **Root environment** | **Develop (OU)** | **Production (OU)** |
| --- | --- | --- | --- |
| Richard van klaveren | v1-administrators | administrators-develop | administrators-production |
| Michel Wilson | v1-administrators | administrators-develop | administrators-production |
| Darius Wattimena | v1-administrators | administrators-develop | administrators-production |
| Leon Gommans | v1-administrators | administrators-develop | administrators-production |
| Minh Trang Nguyen | v1-administrators | administrators-develop | administrators-production |
| Damon Asberg | v1-backend-devs | backend-devs-develop | backend-devs-production |
| Francisco Muros | v1-backend-devs | backend-devs-develop |  |
| Jamie de Leest | v1-backend-devs | backend-devs-develop |  |
| Joaquin Marquez Bugella | v1-backend-devs | backend-devs-develop | backend-devs-production |
| Maryam Tavakoli | v1-backend-devs | backend-devs-develop |  |
| Pim van den Toorn | v1-backend-devs | backend-devs-develop |  |
| Rowdey Goos | v1-backend-devs | backend-devs-develop |  |
| Shan Nguyen | v1-backend-devs | backend-devs-develop | backend-devs-production |
| Joost Dambrink | v1-backend-devs, v1-textract | backend-devs-develop, textract-develop |  |
| David Hansson | v1-frontend | frontend-develop | frontend-production |
| Ojas Gulati | v1-frontend | frontend-develop |  |
| Kimberly Konings | v1-students | students-develop |  |
| Regiena Zimmerman | v1-students | tudents-develop |  |
| Leon Joosse | v1-techsupport | techsupport-develop | techsupport-production |
| Gavin den Hollander | v1-techsupport | techsupport-develop | techsupport-production |
| Joost Laurman | v1-techsupport | techsupport-develop | techsupport-production |
| Hanh Tran |  |  |  |

## Onboarding new user

To add a new user through the IAM Identity Center, please follow the instructions outlined below.

**Step 1: Add new user**

Navigate to the IAM Identity Center and select the "Add user" button. Complete the displayed form by entering the username, email address, and name. Select the option that allows AWS to email the user instructions for password reset and Multi-Factor Authentication (MFA) setup.

**Step 2: Choose group**

Select the appropriate group for your environment. Groups prefixed with "v1-" are designated for environments within the root account. Click the "Next" button, then confirm by selecting "Add user" on the following screen.