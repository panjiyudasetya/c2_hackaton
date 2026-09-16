---
id: confluence:802291713
source: confluence
type: page
space: TC
title: Version control and deployment with Power BI
author: Yaren Aslan
date: '2025-08-19'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/802291713
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/802291713
---
# Version control and deployment with Power BI

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/802291713  

## Content

# Version Control Standards

Power BI reports and datasets must be maintained in the centralized GitHub repository. We use **Power BI Project files (PBIP)** for developing new content whenever possible, instead of traditional PBIX files. This stems from the following reasons:

* We use Git integration and not OneDrive refresh to publish or deploy content.
* We use source control to track and manage changes.
* Multiple content creators will collaborate together on a models or reports.
* We automate parts of the development, testing, or deployment process.

We use GitHub for version control. Make sure to

* Request and receive access to Teqplay GitHub organization
* Create an account in GitHub
* [Download GitHub Desktop](https://desktop.github.com/download/)

# Branching Strategy

We adopt a **feature branch workflow** (also called Git Flow) with a protected main branch:

* Developers create **feature branches** from the `dev` (development). Each feature or bug fix should be isolated in its own branch. Consider using Create branch function in Jira for traceability.

* The `dev` **branch** (development branch) corresponds to the *Development* workspace content. Feature branches are merged into `dev` via pull requests after peer review. This ensures that all changes integrated in `dev` branch have been reviewed and tested by the team.
* The `main` **branch** is considered the **production branch** and always reflects the content that is ready to deploy to Production. The main branch is protected: no direct commits are allowed; all changes must come via pull request merges that have passed review and testing. We keep the main branch in a **deployable state at all times**, meaning it contains only tested, quality-checked content that can be released.

We follow an approach similar to the figure below. In summary, the content creator

* has a branch where they can work on a feature (a branch from dev)
* uses their own local environment to develop
* whenever needed, uses their private workspace to validate their reports on Power BI service
* commits and pushes changes to their feature branch
* creates a pull request and merge it to dev, communicates with others in

  + reviewing other pull requests
  + merging from dev to main

| **Item** | **Description** |
| --- | --- |
|  | Each content creator develops content in their own local environment. |
|  | When ready, content creators commit and push their changes to a remote repository, such as an Azure Repos Git repository. |
|  | In the remote Git repository, content creators track and manage content changes by using source control, and branch and merge content to facilitate collaboration. |
|  | Content creators sync a branch of the remote repository with a private workspace. After syncing, the latest changes that a creator commits and pushes to the branch are visible in that private workspace. Different content creators work on their own, separate branches as they make changes. |
|  | In the private workspaces, content creators can develop content by using web authoring, and validate their own changes. Changes to content made by web authoring can sync with the branch in the Git repository when the content creator commits and pushes these changes from the workspace. Different content creators work in their own, separate private workspaces. |
|  | When ready, content creators perform a pull request to merge their changes into the main branch of the solution. |
|  | After merging changes, the main branch syncs with the development workspace. |
|  | In the development workspace, content creators can develop content that isn't supported by Fabric Git integration, such as dashboards. Content creators also validate the integrated solution that contains all of the latest changes. |
|  | When ready, content creators deploy content to a test workspace. In the test workspace, users perform user acceptance testing of content. |
|  | When ready, content creators deploy content to a production workspace. In the production workspace, content creators distribute content by publishing a Power BI app or sharing content from the workspace. |

# Git integration in Power BI Service

The **Development workspace** is connected to the **main branch** of our GitHub repository. Following steps are taken to ensure this connection.

* Create an access token in GitHub that grants permissions for the repo
* Provide this token to create a connection to GitHub. This can be done under Workspace settings> Git integration

  + From this point on, this connection appears under Manage Connections and Gateways page. It can be edited here if needed (in case of regenerated access token, for instance).
  + Make sure that the list of users cover all users that should be able to sync GitHub repository with Power BI Service. If a user experiences the warning “Sign in to GitHub”, go to “Manage users” in Connections, and add the user.
* Under Workspace settings> Git integration, provide the repository URL and the branch

Whenever needed, the workspace can be synced with the recent developments in the repo, using the Source Control button. Changes and updates can be reviewed before syncing.

The PTO Deployment pipeline is used to ensure that these developments are brought up further to the other two workspaces (Testing and Production). The pipeline is discussed in the following section.

# Deployment Pipeline

We use **Power BI Deployment Pipelines** in the Power BI Service to manage content promotion across **Development**, **Test**, and **Production** workspaces. Each pipeline consists of three linked workspaces (one per stage) and allows us to deploy content forward with consistency and automated comparison.

When deploying from one stage to the next, the pipeline will **compare** the content in source vs. target. We use the pipeline’s **“Compare Changes”** feature to review differences (added reports, modified datasets, etc.) before actually deploying.

After each deployment to Test or Prod, the BI team verifies that:

* All reports load without errors.
* Datasets in the new stage are refreshing or accessible (credentials have been applied).
* Any differences flagged by the pipeline’s comparison are intended. The pipeline does not automatically carry over permissions or certain settings (e.g., dataset security roles, refresh schedules)[learn.microsoft.com](https://learn.microsoft.com/en-us/fabric/cicd/deployment-pipelines/understand-the-deployment-process#:~:text=The%20following%20item%20properties%20aren%27t,copied%20during%20deployment)[learn.microsoft.com](https://learn.microsoft.com/en-us/fabric/cicd/deployment-pipelines/understand-the-deployment-process#:~:text=The%20following%20semantic%20model%20properties,also%20not%20copied%20during%20deployment), so those are checked manually at least on first deployment.

Different environments require different data connections or parameters. To handle these differences in a controlled way, we use **Deployment Rules** in Power BI and standard data source management practices. Following rules are in place:

* For the Testing workspace

  + connection\_string = “dsn=NewMARTProd“
  + vesselvoyage\_link = “<https://vesselvoyagev2.teqplay.nl>”
* For Production workspace

  + connection\_string = “dsn=NEW-ETL-CM-MART“
  + vesselvoyage\_link = ”[https://vesselvoyagedata.teqplay.nl](https://vesselvoyagev2.teqplay.nl)”

# Sources

[Power BI implementation planning: Develop content and manage changes - Power BI | Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/guidance/powerbi-implementation-planning-content-lifecycle-management-develop-manage)

[Expert Guide: GitHub Integration for Microsoft Fabric](https://www.youtube.com/watch?v=iLYIx3QS508)

[Proper Version Control in Power BI using Power BI Projects and GitHub](https://www.youtube.com/watch?v=PDI3k4G4Dpk)