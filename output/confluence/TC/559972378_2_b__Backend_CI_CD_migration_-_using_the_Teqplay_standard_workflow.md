---
id: confluence:559972378
source: confluence
type: page
space: TC
title: 2.b. Backend CI/CD migration - using the Teqplay standard workflow
author: Joaquin Marquez Bugella
date: '2024-12-26'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/559972378
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/559972378
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/559972378/2.b.+Backend+CI+CD+migration+-+using+the+Teqplay+standard+workflow#Publish-image-method
---
# 2.b. Backend CI/CD migration - using the Teqplay standard workflow

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/559972378  

## Content

#FFF0B3

**Work in progress:**

* Only containing unsorted notes.
* It requires changes to standardise the CI/CD flow across all projects.
none

# Introduction

This page shows how to reuse the standard backend workflow published in the [Github Teqplay’s actions repository](https://github.com/teqplay/actions) ([backend-standard.yml](https://github.com/teqplay/actions/blob/master/.github/workflows/backend-standard.yml))

Briefly, a Teqplay standard project complies with the following:

* `helm` folder with environment values files (`values.yaml`, `values.dev.yaml`, `values.prod.yaml`and `values.staging.yaml`)
* A **Kotlin** project, using a **Gradle wrapper**.
* Having 3 steps layers: **build&test**, **publish image** and **deploy** (in different environments).
* It publishes the docker image in our ECR.
* It uses the repo `chartmuseum.teqplay.nl`
* It deploys in our **Kubernetes** **production** (only master) and **develop** **clusters** (rest of branches)
* Repository name follows the pattern `teqplay/<projectName>-backend`
* Kubernetes releases follow the pattern `projectName` (without `teqplay/` prefix and `-backend` prefix)

If the project satisfy all these above, then you can proceed with the next steps.

# Steps

1. After moving the repository to github (following 1. Code-base git migration), clone your repository from GitHub and create and checkout into a migration branch, i.e. `migration/cicd-setup`.

   git branch migration/cicd-setup
   git checkout migration/cicd-setup
2. Create a workflow file in your repository: `.github/workflows/main.yml` and add this content (example here):

   name: Teqplay Standard Workflow
   run-name : ${{ github.event.head\_commit.message }}
   on: [push]
   jobs:
   external-main:
   name: Teqplay standard workflow
   uses: teqplay/actions/.github/workflows/backend-standard.yml@master
   secrets:
   aws\_access\_key\_id: ${{ secrets.AWS\_ACCESS\_KEY\_ID }}
   aws\_secret\_access\_key: ${{ secrets.AWS\_SECRET\_ACCESS\_KEY }}
   cm\_username: ${{ secrets.CM\_USERNAME }}
   cm\_password: ${{ secrets.CM\_PASSWORD }}
3. Grant access to the repository to the intended users group (by now, `Backend` is fine).

|  |
| --- |
|  |
| Granting access to users in Repository |

4. Create the **repository Environments** in Github ([example here](https://github.com/teqplay/scrapeshark-backend/settings/environments))

   * I.e. `production` , `develop` or/and `staging`. Also, `publish-image`
   * Set a reviewing rule by any of the users in `backend` group (see point 3).

|  |
| --- |
|  |
| Repository environments |

|  |
| --- |
|  |
| Environment Protection Rule - reviewers |

5. Create the **repository** variable `NAMESPACE` ([example here](https://github.com/teqplay/scrapeshark-backend/settings/variables/actions)).

|  |
| --- |
|  |
| Repository variables |

6. Adapt your `build.gradle` when needed in the following points:

   * **Gradle Versioning:** the gradle function to create the image version (probably `generateVersion()`) needs to be adapted to the new expected GH environment variables ([Complete example here](https://github.com/teqplay/scrapeshark-backend/commit/15f56bbf9b33726a74fdd9f0857815a3b83f8a90#diff-49a96e7eea8a94af862798a45174e6ac43eb4f8b4bd40759b5da63ba31ec3ef7R252)) :

     + `GH,` indicating that gradle is running in Github actions, not locally
     + `BRANCH,` indicating the branch for what the workflow is running gradle.
     + `GITHUB_RUN_NUMBER,` which the Github action provides as `${{ github.run_id }}.${{ github.run_number }}.${{ github.run_attempt }}`

       static def generateVersion() {
       if (System.getenv('GH') != null) {
       def branch = System.getenv('BRANCH').replace("/", "\_").toLowerCase()
       def buildNum = System.getenv('GITHUB\_RUN\_NUMBER')
       def formattedTimestamp = getTimestamp()
       return branch + "-" + formattedTimestamp + "-b" + buildNum
       } else {
       return 'local'
       }
       }
       static def getTimestamp() {
       def date = new Date()
       def formattedDate = date.format('yyyy-MM-dd')
       return formattedDate
       }
   * **Publish gradle plugin**: Make sure your project uses `bmuschko` **gradle plugin** to publish in our ECR.  
     In case the project uses `awssdk`’s `ecrClient`, please change it according to [the troubleshooting section **publish-image**.](https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/559972378/2.b.+Backend+CI+CD+migration+-+using+the+Teqplay+standard+workflow#Publish-image-method)  
      Complete [example here](https://github.com/teqplay/scrapeshark-backend/commit/fc0df50ce63697c8ca13dfb0afa4d1e5d38cf87c)
7. **Add, commit and push changes.**  This will trigger a workflow in your repository’s Actions tab ([see example here](https://github.com/teqplay/scrapeshark-backend/actions)).

|  |
| --- |
|  |
| Workflow triggered in GitHub Actions. |

9. If your project is aligned with the Teqplay backend standards (to be formally defined) everything should be fine.  
   Create a PR `migration/cicd-setup` → `master` and assign relevant people in the project.

# Validate CICD migration

After the PR is approved, it’s time to merge and validate (there’s no other way).

Reaching this point, you should be able to run the CICD workflow with no issues in all expected scenarios according to your project.

A standard backend project should have at least the look on previous point 8. Then, you should be able accomplish all steps in the workflow:

* Test & build
* Publish a docker image in ECR (<https://eu-west-1.console.aws.amazon.com/ecr/private-registry/repositories?region=eu-west-1>).
* Deploy image on develop and/or production (in our k8s clusters).

Note that **deploying on production** is protected and it's possible for master branches workflows.

# Clean up

* Disable CICD pipelines for this project by **stopping building** in the CircleCI project settings:

|  |
| --- |
|  |
| https://app.circleci.com/settings/project/bitbucket/teqplay/<repo\_name> |

* Remove `.circleci` folder in the Github repository (do it with a PR!)

# Troubleshooting:

## Gradle wrapper

Gradle step failed with a similar message to this:

… and in the specific job log:

...
✗ Found unknown Gradle Wrapper JAR files:
5c9b7c88dad7622cbc1eb09dbd71d7fec253d1cbd684ee848d84fded5cf43c86 gradle/wrapper/gradle-wrapper.jar
Error: Error: At least one Gradle Wrapper Jar failed validation!
...

**Possible reason:** your project is using a custom made gradle wrapper version, by any of us or the original OS where the project was set up.

**Possible solution:** reset gradle wrapper version to the official same one with this:

./gradlew wrapper --gradle-version <x.y.z>

This will probably make changes in the following files:

git status
On branch migration/branch
Changes not staged for commit:
(use "git add <file>..." to update what will be committed)
(use "git restore <file>..." to discard changes in working directory)
modified: gradle/wrapper/gradle-wrapper.jar
modified: gradle/wrapper/gradle-wrapper.properties
modified: gradlew
modified: gradlew.bat

## Publish-image method

In case your project uses the AWS ECR client (`import com.bmuschko.gradle.docker.tasks.image.DockerPushImage` at the top of your build.gradle, you’d have to replace it by the latest bmuschko’s gradle plugin `DockerPushImage`

Here are the changes ( complete [example here](https://github.com/teqplay/scrapeshark-backend/commit/fc0df50ce63697c8ca13dfb0afa4d1e5d38cf87c)):

1. Remove `EcrClient` import
2. Add import for DockerPushImage   
   `import com.bmuschko.gradle.docker.tasks.image.DockerPushImage`
3. Remove the following `dependencies` classpaths in the `buildscript` (if they are)

   * `software.amazon.awssdk:bom`
   * `software.amazon.awssdk:ecr"`
   * `software.amazon.awssdk:sts"`
4. Remove related unused Gradle variables (i.e. `aws_version`)
5. Add the following `plugins` in `buildscript`:

   * `id "com.bmuschko.docker-remote-api" version "$docker_api_version"`
   * `id "com.patdouble.awsecr" version "$ecr_version"` (required for bmuschko to publish to AWS ECR).
6. Add new Gradle variables for docker\_api\_version, ecr\_repo\_url, and ecr\_version

   * `docker_api_version = "9.4.0"` (latest according to <https://github.com/bmuschko/gradle-docker-plugin/tags> )
   * `ecr_repo_url = "050356841556.dkr.ecr.eu-west-1.amazonaws.com"`
   * `ecr_version = "0.7.0"`
7. Remove `ecrLogin` task
8. Define dockerImageName:  
   `def dockerImageName = "$ecr_repo_url/${project.name.replace("-backend", "")}:${project.version}"`
9. Remove `dependsOn` and `afterEvaluate` from `bootBuildImage`
10. Set `imageName` in `bootBuildImage`

    bootBuildImage {
    imageName = dockerImageName
    }
11. Add task dockerPushImage as following:

    task dockerPushImage(type: DockerPushImage) {
    images.add(dockerImageName)
    }

**Related links:**

1. [Gradle plugin for managing Docker images and containers (by Bmuschko)](https://github.com/bmuschko/gradle-docker-plugin)
2. [Gradle plugin to integrate with AWS ECR](https://plugins.gradle.org/plugin/com.patdouble.awsecr)
3. [Gradle Docker Plugin User Guide & Examples](https://bmuschko.github.io/gradle-docker-plugin/#examples_2)