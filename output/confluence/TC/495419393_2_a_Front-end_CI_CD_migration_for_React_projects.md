---
id: confluence:495419393
source: confluence
type: page
space: TC
title: 2.a Front-end CI/CD migration for React projects
author: Damon Asberg
date: '2025-02-17'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/495419393
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/495419393
---
# 2.a Front-end CI/CD migration for React projects

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/495419393  

## Content

Adding it to a new project? <https://teqplaybv.atlassian.net/wiki/x/CwC7JQ>

# Introduction

This will cover the full extent of replacing the CircleCI instance of your frontend project with new GitHub Actions workflows.

Before continuing, make sure you have followed all steps inside 1. Code-base git migration and have a repository in GitHub ready to go.

16falsenonelisttrue

## Summary: Main differences between CircleCI and GitHub Actions

There are some key difference in how both handle workflows, steps, (environment) variables and secrets.

All will be handled in the detailed steps, but this is a summary:

* Your CircleCI `config.yml` contains every single step of the workflow that needs to happen.

  + For GitHub Actions, you will use a reusable workflow which is already set up for you - simplifying the process and allowing for other projects to
* In CircleCI you have environment variables passed as `context` like `common-builds-context`, or as project environment variables. They are always kept secret and cannot be read afterwards.

  + GitHub Actions makes a distinction between secrets and variables, where variables can still be read after you have entered them.
  + GitHub Actions has different levels where both secrets and variables can come from:

    - Organisation (such as a `NPM_TOKEN`)
    - Repository (such as `GA_TOKEN` - Google Analytics)
    - Environment (such as a unique `S3_BUCKET` for dev / live) (explained in next bullet)
* CircleCI has no immediate distinction of environments such as `production`, `develop`, `staging` - only at a different job level.

  + GitHub Actions introduces `environments`, which can have their own secrets, variables and deploy permissions at branch level.
  + GitHub Actions environments can have deployment protection rules, where only certain user groups are allowed to deploy instances.
* CircleCI has `approval` job types, where you can hold a certain job.

  + GitHub Actions does not have this, in order to get the same effect you need to set up `Deployment protection rules > Required reviewers`. This will hold deploy steps until they can proceed.

# Migration for build-deploy

### 1. Preparation

0. Ensure you have followed all steps inside 1. Code-base git migration
1. Make sure you add the `Frontend` team to your repository with `Admin` access level.

   * Go to your repository Settings page
   * Click collaborators and teams
   * Click `Add teams`
   * Type in `Frontend` and add them
2. Determine the following for your project by looking at the CircleCI `.circleci/config.yml` file. What does your project contain?

   * Is this a React based project? If not (such as react-native), this guide is not suited for that project and you need your own workflow. Make sure to create it inside the teqplay/actions repository.
   * NodeJS version used to build the project
   * What kind of environments are present? `production`, `develop`, `staging`, others?

     + For each project, write down:
     + S3 bucket (e.g. `cargooptimadev.teqplay.nl`)
     + CloudFront distribution id (e.g. `E2P0EJILMIP0M5`)
   * Is the build folder any other than `build`? If it is `www` for example for Cordova projects, make sure to remember this output folder.
   * Does it post Slack deployment status messages to a channel? To what channel? Make sure you remember this for a later step.
   * Any extra steps other than build, run unit tests and deploy? **If this is the case**, you might need to branch off this guide at some point and create your own unique reusable steps or workflow tailored to your project.
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
4. (Optional, recommended) Add your Slack Channel id to post your deploy messages to

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

### 2. Create the yml file

1. Create a new branch in your GitHub repository to apply your changes to, for example `migration/gh-actions`. It can really be any name, just to make sure all your steps are not immediately on master…
2. Create a GitHub actions folder structure with a new file at `.github/workflow/main.yml`
3. Inside the file add the following code block:

   * Create a `string` array of environments, matching the GitHub environments you created in the previous main step. (i.e. production, develop, staging…)
   * Remember to replace `[true|false]` with either values depending on your preferences.
   * `pnpm_version` is optional, when removed it will fall back to using `npm`
   * Or change on what triggers the workflow

yamlname: Web build and deploy
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

3. Commit and push your changes

### 3. Prepare DependencyTrack

To increase our insights in how many vulnerabilities we have across all our projects, we have started using DependencyTrack to upload SBOM (Software Bill of Materials) files to it.

Luckily this is already mostly automated inside the workflow, but we still need to add the project to it.

1. Go to [dependencytrack.teqplay.nl](http://dependencytrack.teqplay.nl) and login with credentials
2. Click on projects in the left bar
3. For each environment you are deploying (i.e. production / develop / staging):

   * Click create project
   * For the `Project Name`, fill in the **exact**  field the package.json `name` field has. This should also be aligned with your repository name.
   * For version, fill in the environment you are adding right now.
   * Fill in the Classifier as matching with the project structure.
   * Click `Create`.
4. Now you can continue with your workflow.

### 4. View and deploy using your new workflow

This should be everything you have to do in order to get things going. To confirm that it is working:

1. Go to your repository page
2. Click Actions
3. Your latest commit should appear inside the workflow list, click its name

It should look something like this:

Example of the CargoOptima repository of a successful build step with pending deployments.

If your build passes, you are able to deploy!  As we have enabled Required reviewers for deployments, we need to approve the deployment.

1. Click the `Review deployments` button
2. Select which environment you want to deploy:
3. Leave a comment (or not)
4. Click Approve and deploy

# Migration for Fastlane applications

This guide is for Cordova specific projects… hopefully no more new ones

## 1. Preparation

0. Ensure you have followed all steps inside 1. Code-base git migration
1. Determine the following for your project by looking at the CircleCI `.circleci/config.yml` file. What does your project contain?

   * Is this a React based project? If not (such as react-native), this guide is not suited for that project and you need your own workflow.
   * NodeJS version used to build the project
   * What kind of environments are present? `production`, `develop`, `staging`, others?

     + For each project, write down:
     + S3 bucket (e.g. `cargooptimadev.teqplay.nl`)
     + CloudFront distribution id (e.g. `E2P0EJILMIP0M5`)
   * Put `www` as a build\_folder input inside the yml file in the next step
   * Does it post Slack deployment status messages to a channel? To what channel? Make sure you remember this for a later step.
   * Any extra steps other than build, run unit tests and deploy? **If this is the case**, you might need to branch off this guide at some point and create your own unique reusable steps or workflow tailored to your project
2. Prepare your environments in GitHub

   * Go to your GitHub repository page → Settings → “Code and automation” → Environments
   * For each environment you want to add (example being CargoOptima staging):

     + Click the `New environment` button
     + Name it any of `production` or `develop` or `staging` and click save/Configure environment
     + Check the `Required reviewers` checkbox underneath Deployment protection rules.
     + Inside the search box, search for the `teqplay/frontend` team and add this
     + Underneath `Environment variables` add the following 2 variables (names are case insensitive, values are case sensitive):

       - `s3_bucket` with the S3 bucket of this environment (e.g. `cargooptimastaging.teqplay.com`)
       - `cloudfront_distribution_id` of this environment (e.g. `E3V7W5CA3M11YA`)

         * You can find this ID at: [console.aws.amazon.com/cloudfront/v4/home](http://console.aws.amazon.com/cloudfront/v4/home)
3. As this is a Fastlane project, you will also need to setup the Android and iOS environments

   * Go to your GitHub repository page → Settings → “Code and automation” → Environments
   * Create an environment called `android`

     + Check the `Required reviewers` checkbox underneath Deployment protection rules.
     + Inside the search box, search for the `teqplay/frontend` team and add this
     + There are no secrets/variables required to put, all are on the organisational level
   * Create an environment called `ios` and follow the same substeps as for the previous step
4. (Optional) Add Slack message to the project

   * See migration guide for non-fastlane based projects

### 2. Create the yml file

1. Create a new branch in your GitHub repository to apply your changes to, for example `migration/gh-actions`. It can really be any name, just to make sure all your steps are not immediately on master...
2. Create a GitHub actions folder structure with a new file at `.github/workflow/main.yml`
3. Inside the file add the following:

   * Remember to replace `[true|false]` with either values depending on your preferences.

yamlname: Build and deploy
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
build-cordova:
name: Cordova workflow
uses: teqplay/actions/.github/workflows/frontend-cordova.yml@master
secrets:
android\_api\_json: ${{ secrets.android\_api\_json }}
fastlane\_android\_keystore: ${{ secrets.fastlane\_android\_keystore }}
fastlane\_android\_keystore\_alias: ${{ secrets.fastlane\_android\_keystore\_alias }}
fastlane\_android\_keystore\_password: ${{ secrets.fastlane\_android\_keystore\_password }}
aws\_access\_key\_id: ${{ secrets.aws\_access\_key\_id }}
aws\_secret\_access\_key: ${{ secrets.aws\_secret\_access\_key }}
npm\_token: ${{ secrets.npm\_token }}
sentry\_auth\_token: ${{ secrets.sentry\_auth\_token }}
slack\_bot\_token: ${{ secrets.slack\_bot\_token }}
fastlane\_ios\_cert\_issuer\_id: ${{ secrets.fastlane\_ios\_cert\_issuer\_id }}
fastlane\_ios\_cert\_key\_id: ${{ secrets.fastlane\_ios\_cert\_key\_id }}
fastlane\_ios\_cert\_pkey: ${{ secrets.fastlane\_ios\_cert\_pkey }}
match\_password: ${{ secrets.match\_password }}
dt\_api\_key: ${{ secrets.dt\_api\_key }}
with:
environments: '["production", "develop", "temp"]'
build\_folder: 'www'
android\_success\_url: '' # URL inside Slack message you can click to view
ios\_success\_url: '' # URL inside Slack message you can click to view

3. Commit and push your changes

### 3. View and deploy using your new workflow

This should be everything you have to do in order to get things going. To confirm that it is working:

1. Go to your repository page
2. Click Actions
3. Your latest commit should appear inside the workflow list, click its name

It should look something like this:

If your build passes, you are able to deploy!  As we have enabled Required reviewers for deployments, we need to approve the deployment.

1. Click the `Review deployments` button
2. Select which environment you want to deploy:

3. Leave a comment (or not)
4. Click Approve and deploy