---
id: confluence:633012235
source: confluence
type: page
space: TC
title: Add GitHub Actions to a new project
author: Damon Asberg
date: '2025-02-17'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/633012235
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/633012235
---
# Add GitHub Actions to a new project

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/633012235  

## Content

Migrating an existing project? <https://teqplaybv.atlassian.net/wiki/x/AYCHHQ>

1. Make sure you add the `Frontend` team to your repository with `Admin` access level.

* Go to your repository Settings page
* Click collaborators and teams
* Click `Add teams`
* Type in `Frontend` and add them

2. Note down the following items:

   * What environments do you need to deploy to?

     + i.e. production, develop, staging
   * For each environment, note down the following:

     + S3 bucket name; e.g. `portreporterdev.teqplay.nl`
     + Cloudfront distribution ID; e.g. `E2P0EJILMIP0M5`)
   * Is there a different build folder other than `build`?
   * Any Slack channel you want deployment messages to post to? Find out its channel ID
3. Prepare your environments in GitHub

   * Go to your GitHub repository page → Settings → “Code and automation” → Environments
   * For each environment you want to add (example being CargoOptima staging):

     + Click the `New environment` button
     + Name it anything you want (as long as you remember it to write down in main.yml later…) and click save/Configure environment
     + Check the `Required reviewers` checkbox underneath Deployment protection rules.
     + Inside the search box, search for the `teqplay/frontend` team and add this
     + If you are using the `production` environment or any others where you want only certain branches to deploy to, make sure to limit the Deployment branches and tags.  
       This also supports wildcards like `feature/**`.

       Example for production environment
     + Underneath `Environment variables` add the following 2 variables (names are case insensitive, values are case sensitive):

       - `s3_bucket` with the S3 bucket of this environment (e.g. `cargooptimastaging.teqplay.com`)
       - `cloudfront_distribution_id` of this environment (e.g. `E3V7W5CA3M11YA`)

         * You can find this ID at: [console.aws.amazon.com/cloudfront/v4/home](http://console.aws.amazon.com/cloudfront/v4/home)
4. Add your Slack Channel id to post your deploy messages to

   * Go to your GitHub repository page → Click Settings → Underneath “Security” → “Secrets and variables” → Click on Actions
   * Click on the Variables tab

     + You should now also see all your environment variables successfully configured
   * Underneath Repository variables, click `New repository variable`
   * Name it `SLACK_CHANNEL_ID`
   * For the value, determine the Slack Channel id

     + Go into the Slack channel you want to post the message to
     + Click the name to go into the details screen (image below)
     + Copy the `Channel ID` at the bottom
     + Paste this copied value into GitHub as the value
     + Click save/Add variable

       At the bottom, the Channel ID is shown
5. Create a new branch in your GitHub repository to apply your changes to, for example `migration/gh-actions`. It can really be any name, just to make sure all your steps are not immediately on master…
6. Create a GitHub actions folder structure with a new file at `.github/workflow/main.yml`
7. Inside the file add the following code block:

   * Create a `string` array of environments, matching the GitHub environments you created in the previous main step. (i.e. production, develop, staging…)
   * Remember to replace `[true|false]` with either values depending on your preferences.
   * `pnpm_version` is optional, when removed it will fall back to using `npm`
   * Or change on what triggers the workflow

name: Web build and deploy
run-name: ${{ github.event.head\_commit.message }}
on:
push:
branches:
- master
- develop
- staging
pull\_request:
branches:
- master
- develop
- staging
jobs:
build-and-deploy:
name: Frontend build and deploy
uses: teqplay/actions/.github/workflows/frontend-standard.yml@master
secrets:
aws\_access\_key\_id: ${{ secrets.aws\_access\_key\_id }}
aws\_secret\_access\_key: ${{ secrets.aws\_secret\_access\_key }}
npm\_token: ${{ secrets.npm\_token }}
sentry\_auth\_token: ${{ secrets.sentry\_auth\_token }}
slack\_bot\_token: ${{ secrets.slack\_bot\_token }}
dt\_api\_key: ${{ secrets.dt\_api\_key }}
with:
environments: '["production", "develop", "your-environment-name-here"]'
# pnpm\_version is optional, when removed it will fall back to npm
pnpm\_version: 10

8. Commit and push your changes
9. Add the project on DependencyTrack

   1. Go to [dependencytrack.teqplay.nl](http://dependencytrack.teqplay.nl/) and login with credentials
   2. Click on projects in the left bar
   3. For each environment you are deploying (i.e. production / develop / staging):

      * Click create project
      * For the `Project Name`, fill in the **exact**  field the package.json `name` field has. This should also be aligned with your repository name.
      * For version, fill in the environment you are adding right now.
      * Fill in the Classifier as matching with the project structure.
      * Click `Create`.
   4. Now you can continue with your workflow.