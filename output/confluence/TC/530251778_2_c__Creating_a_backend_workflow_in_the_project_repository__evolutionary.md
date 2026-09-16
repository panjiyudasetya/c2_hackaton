---
id: confluence:530251778
source: confluence
type: page
space: TC
title: 2.c. Creating a backend workflow in the project repository (evolutionary)
author: Joaquin Marquez Bugella
date: '2024-12-03'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/530251778
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/530251778
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/edit-v2/495091714#Deploy-job-hold-%26-approval
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/edit-v2/495091714#Deploy
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/530251778/2.c.+Creating+a+backend+workflow+in+the+project+repository+evolutionary#Gradle-Wrapper-Jar-failed-validation
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/495091714/General+backend+project+migration+steps#Branch-deployment-protection
---
# 2.c. Creating a backend workflow in the project repository (evolutionary)

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/530251778  

## Content

#FFF0B3

**Work in progress:**

* Currently it only replicates the current CI/CD pipeline.
* It requires changes to standardise the CI/CD flow across all projects.
none#FFF0B3

Work in progress

# Introduction and aims

This document focuses on the second part of the **git migration (see parent page)**.

It should attempts to illustrate the general steps for a **Teqplay backend** project’s **CI/CD pipeline**.

In contrast, this document **is NOT aimed to describe ALL** CI/CD possibilities, **but to focus on our own needs** and context.

As a **prerequisite**, the git repository should have been migrated before starting this guide, or, at the very least, a working version of it (in case it was not possible at some extend).

# Preparations

Before any race, we must know where do we hit the road, the check points and the !  
So let’s know where we stand and answer yourself the following:

* **Where** is your project? (the starting point).

  + obviously Bitbucket, but let’s get detailed!
* **Where** will it be placed? (the end point).

  + obviously GitHub, but let’s get detailed!
* **What** your git artifacts that you want to migrate? (the load)

  + commits, branches, pull-requests, users or groups, etc…
* **How** is your CI/CD workflow? (the checkpoints).

  + Identify the **CircleCI** script and get familiar with it (typically in the `.CircleCI` folder) : jobs and steps to migrate.
* Collect needed credentials and access rights (the needs).

  + Can you access the project Bitbucket repository?
  + Do you have a GitHub user with the correct access rights?
  + Any project-dependent blockers and/or special needs?

Here’s a template table that might help you that you can use as a quick reference and track progress (copy and paste it in the specific Jira issue).

7
7
incomplete
 Next table TBC throughout the process.

| **Resource** | **Value** | **Comments** |
| --- | --- | --- |
| Bitbucket repo url |  |  |
| GitHub repo url |  |  |
| Credentials |  | Bitbucket and GitHub users. |
| access rights |  | Bitbucket and GitHub users access. |
| Environments |  |  |
| Gradle authentication method |  | How Gradle authenticates to access Teqplay maven repositories. |
| *TBC throughout the process* | *TBC throughout the process* | *TBC throughout the process* |
| … |  |  |

# Current CircleCI scenario

Until 2024-November, most Teqplay backend projects have their CI/CD pipelines managed by CircleCI.

This step describes the steps and considerations to migrate the CI/CD from **CircleCI** to **GitHub actions**.

This pipeline workflow and steps are set in the file `.circleci/config.yml` and requires some environment variables defined in **CircleCI** context (see them [**here**](https://app.circleci.com/settings/organization/bitbucket/teqplay/contexts/3447aa56-16a8-4fdf-bc67-8c0068711ff9?return-to=https%3A%2F%2Fapp.circleci.com%2Fpipelines%2Fbitbucket%2Fteqplay)).

A standard Teqplay pipeline in CircleCI currently has the following jobs:

|  |
| --- |
|  |
| A typical CircleCI pipeline |

Consisting of:

1. **Building**

   1. Including the gradle tasks

      1. run unit tests.
      2. build the application.
      3. publish a docker image to [ECR repository](https://eu-west-1.console.aws.amazon.com/ecr/private-registry/repositories?region=eu-west-1) (specified in your `build.gradle` file).
2. **Split flows by environment remained in Holding**

   1. A simple manual approval job that allows us to decide where to deploy.
3. **Environment deploy**

   1. Indicate Kubernetes cluster.
   2. Configure Helm: add Teqplay repo ( it needs the AWS access credentials) and update it.
   3. Deploy image (published in step 1.a.iii)

# GitHub actions script set

These pipeline actions need to be replicated in what’s called a ***workflow*** in GitHub Actions, which is structured in ***jobs*** and ***steps***.

|  |
| --- |
|  |
| Example of analogous version of CircleCI pipeline to achieve in GitHub Actions. |

Notice that not only the *look&feel* is different, but also the CI/CD capabilities. The CircleCI job (Point 2) that splits and approves each environment deployment independently, is managed differently.  
It requires the definition of several environments, where a selected group of developers can approve the associated GitHub actions job.  
This will be explained in the [**Deploy job hold & approval** section](https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/edit-v2/495091714#Deploy-job-hold-%26-approval).

Similarly to CircleCI, GitHub Actions scripts should be located in the project root folder `.github`

## Main workflow

It’s recommended to create an initial workflow in `./.github/workflows/main.yml` that contains the main jobs

It’s highly recommended to *modularized* each step (for readability) in **local** ***reusable workflows*** and/or ***composite actions***.  
Both are fairly the same (let’s call them ***reusable blocks*** of code), but with different capabilities ([see more details here](https://docs.github.com/en/actions/sharing-automations/avoiding-duplication#key-differences-between-reusable-workflows-and-composite-actions)).

Worth to mention that if you need to use conditional logic to run a ***reusable block***, you must choose between reusable workflows or composite actions, depending on whether you’re using it as a step in a job and as an entire job replacement (I’ll relate to this later in this guide, I promise  ).

Here is the (broad) documentation for workflow syntax: <https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions>

### Jobs flow and environment split

Jobs in a workflow can be chained one after another, by defining the job’s `need` (as opposed to the `requires` of CircleCI).

Basically, we would like **build first** and **deploy after** it in **each environment**.

* Build

  + → Deploy in Production
  + → Deploy in Develop
  + → Deploy in Staging

Let’s not talk yet about holding the deploy.

Here is an example of a basic shallow (only *echoes*) workflow representing a generic pipeline:

|  |
| --- |
| name: Main workflow run-name : ${{ github.event.head\_commit.message }} on: [push] jobs: test-build-publish-image: name: Test, build, and publish image run: echo "Test, buld and publish image to ECR." deploy-on-production: needs: test-build-publish-image name: Deploying on Production run: echo "Deploying on Production" deploy-on-develop: needs: test-build-publish-image name: Deploying on develop run: echo "Deploying on develop" deploy-on-staging: needs: test-build-publish-image name: Deploying on staging run: echo "Deploying on Staging" |
| File `./.github/workflows/main.yml` |

Which will produce the result in GitHub Actions:

|  |
| --- |
|  |
| Basic workflow produced by `main.yml` |

### **Deploy job hold & approval**

In **CircleCI**, to hold onto a step for manual confirmation, it was enough to use a job of the type `approval`. See line **line 6** in the next CircleCI snippet:

|  |
| --- |
| ... - build: context: common-builds-context - hold-develop: type: approval requires: - build ... |
| **CircleCI** approval job |

**However, GitHub provides a different way**, focused on actions over an **environment** by a **group of reviewers** – which on the other hand it loses the simplicity of “just set a manual release”.  
In GitHub, an approval job is linked to environment protection measures and it needs the following artifacts:

1. An **environment,** that presumably the job actions will be subjected (i.e. deployed).
2. A **reviewers list** of people and/or group (of people) who can approve (release) the job after reviewing.
3. A job **environment indication** to the job to be approved on that environment, where the job steps will be (probably) executed.

#### The **environment**

The **environment** needs to be defined in the repository settings (in GitHub itself).

|  |
| --- |
|  |
| [Environment list in Github.com](https://github.com/teqplay/cargooptima-backend/settings/environments) |

#### The **reviewers list**

The **reviewers list**, which is related to that environment. Only these reviewers could approve the held job – hence, release the workflow job chain.  
Note that there are more advance options, but let them aside.

|  |
| --- |
|  |
| [Environment setup in Github.com](https://github.com/teqplay/cargooptima-backend/settings/environments/4385344234/edit) |

#### The job **environment indication**

After that, let’s indicate which job requires to be approved (**lines 13, 19 and 25**):

|  |
| --- |
| name: Main workflow run-name : ${{ github.event.head\_commit.message }} on: [push] jobs: test-build-publish-image: name: Test, build, and publish image run: echo "Test, buld and publish image to ECR." deploy-on-production: needs: test-build-publish-image name: Deploying on Production environment: production run: echo "Deploying on Production" deploy-on-develop: needs: test-build-publish-image name: Deploying on Develop environment: develop run: echo "Deploying on Develop" deploy-on-staging: needs: test-build-publish-image name: Deploying on staging environment: staging run: echo "Deploying on Staging" |
| Shallow basic jobs workflow. |

**Notice** the lines 13, 19 and 25 indicate that each job would require manual confirmation on the specified environment ( we’ll see further use of that ***environment*** later).

### Environment deployment protection – 1st half

For the last part, **we can’t (or shouldn’t!)** deploy on production any image not coming from master branch!  
And it’d be desirable not to deploy a master branch image on anywhere else.

Therefore, we should apply measures to ensure this protection.

GitHub allows a workflow to be executed for specific branches. See this example that defines the related workflow to be available only for pushing on the master branch:

on:
push:
branches:
- master
...

Or this one that is available only for any branch except master:

on:
push:
branches:
- '\*'
- '!master'

**However**, if we use this syntax, we’d have to define two very similar deploy workflows: one for deploying **only master images only on production** and another for the rest of cases.

**Let’s not do that**, for the sake of avoiding code duplication.

**Instead, let’s parametrized a reusable workflow** `deploy.yml`, valid for all environments. We’ll see it more in deep in the [Deploy section](https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/edit-v2/495091714#Deploy) ( remember the  promise? here’s part of it, there’ll be more at the end of the deploy section).

**For now** (and for the sake of satisfaction), since the `deploy.yml` is yet neither presented nor *explained*, let’s apply a conditional execution in the `main.yml` **deploy-on-*****environment*** jobs (**lines 11, 19 and 25**):

|  |
| --- |
| name: Main workflow run-name : ${{ github.event.head\_commit.message }} on: [push] jobs: test-build-publish-image: name: Test, build, and publish image run: echo "Test, buld and publish image to ECR." deploy-on-production: if: github.ref\_name == 'master' needs: test-build-publish-image name: Deploying on Production environment: production run: echo "Deploying on Production" deploy-on-develop: if: github.ref\_name != 'master' needs: test-build-publish-image name: Deploying on Develop environment: develop run: echo "Deploying on Develop" deploy-on-staging: if: github.ref\_name != 'master' needs: test-build-publish-image name: Deploying on staging environment: staging run: echo "Deploying on Staging" |
| Shallow basic jobs workflow. |

### Result (environments, reviewers and job all together)

All the combination of these three points will produce the following pipeline.

About ***Branch deployment protection***, notice the icon  in the Deploy on Production job and the icon  in the other ***Deploy*** jobs. This is because the screenshot is about a non-master branch.

|  |
| --- |
|  |
| Result in [github.com](http://Github.com) of the `main.yml` file mentioned above. |

## Test, build and publish an image

This job will contain the basics to produce an deployable image.

As stated before, it basically consist of:

> …
>
> 1. **Building**
>
>    1. Including the gradle tasks
>
>       1. run unit tests.
>       2. build the application.
>       3. build a docker image of your application.
>       4. publish the image to ECR repository.
> 2. …

We will use a *reusable workflow* named `test-build-publish-image` to modularize this job (for readability). Here it’ll be a first version:

|  |
| --- |
| name: test-build-publish-image on: workflow\_call: jobs: test-build-publish-image: name: ' ' runs-on: ubuntu-latest steps: - name: Run unitTest step run: | ./gradlew test - name: Building the image run: | ./gradlew build - name: Building docker image run: | ./gradlew bootBuildImage - name: Publish docker image to ECR repository run: | ./gradlew dockerPushImage |
| Initial steps in the job `test-build-publish-image` ( still incomplete!) |

**However,** this basic steps won’t work straight forward. You will probably need to set up your job runner (the virtual machine – shell – where your actions run), for running the Gradle tasks:

1. **Initialize the AWS context,** required for the next step so gradle can:

   1. pull libraries from Teqplay maven repositories,
   2. push the docker docker image to the ECR repository.
2. **Initialize the Gradle**

   1. to be able to run the Gradle tasks.

Both will be reused as **job steps**, so they will be written as **composite actions**, due to the following needs:

1. to be used as job’s steps ( this is a strong constraint to use a composite action)
2. the need of reusing the runner context (setting the environment variables and files).

A local action needs a special syntax and folder structure ([see here the specific GitHub documentation section](https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions#example-using-an-action-in-the-same-repository-as-the-workflow)).  
Notice the `./.github/actions` folder and the subfolder in it `hello-world-action` which will be the composite local action name and, in it, the `action.yml` file that contains the action script:

|  |
| --- |
| |-- hello-world (repository) | |\_\_ .github | └── workflows | └── my-first-workflow.yml | └── actions | |\_\_ hello-world-action | └── action.yml |
| Folder structure of local actions (lines 5-7) |

### init-aws

Let’s start with the `init-aws` local action (which will be reused for the Deploy job, we’ll see it later  ).

It will consist of a the filepath `./.github/actions/init-aws/action.yml`

Note the lines:

* **Line 3**: aws credentials, which are defined as organizational secrets, can’t be accessed in a local (composite) actions ([see it here](https://docs.github.com/en/actions/sharing-automations/avoiding-duplication#key-differences-between-reusable-workflows-and-composite-actions)), so we’d have to define them as input parameters (we will see later how to pass them as arguments).
* **Line 12**: specifically `using: composite`.
* **Line 17**: In this example, Gradle uses this method `AwsImAuthentication` to authenticate in AWS, requiring the file `/.aws/credentials`.  
   May you use a different method (i.e. `AwsCredentials`), then you’ll probably have to set the environment variables`s3_access_key` and `s3_secret_key`) instead (or also).

|  |
| --- |
| name: init-aws inputs: aws\_access\_key\_id: required: true description: "The aws\_access\_key\_id used to authenticate with AWS" aws\_secret\_access\_key: required: true description: "The aws\_secret\_access\_key used to authenticate with AWS" runs: using: "composite" steps: - name: Setup AWS credentials shell: bash run: | FILE=~/.aws/credentials mkdir -p `dirname $FILE` echo "[default]" > $FILE echo "aws\_access\_key\_id = ${{ inputs.aws\_access\_key\_id }}" >> $FILE echo "aws\_secret\_access\_key = ${{ inputs.aws\_secret\_access\_key }}" >> $FILE |
| **init-aws** action script (`./.github/actions/init-aws/action.yml`) |

### init-gradle

Now, init-gradle will take care of setting up:

**1st job step:** The gradle properties file `.gradle/gradle.properties`

**2nd job step:** The required environment variables that your `build.gradle` file uses.  
 **Warning** ahead! Some adaptations on that file are recommended .  
Please, notice that your `build.gradle` script will probably use `CI`, `CIRCLE_BRANCH` and `BUILD_NUM`.  
 Let’s replace them there by `GH`, `BRANCH` and `GITHUB_RUN_NUMBER`.  
Of course, you can still use the former environmental variable names, but they refer to CircleCI  .

**3rd job step:** The Java environment installation to run `gradlew` jar  (version according your needs).

**4th job step:** Gradle installation itself!

**Regarding 2nd step**, the changes in build.gradle refer to the generateVersion gradle function, which is likely to be similar to this (notice **lines 3~5** below):

|  |
| --- |
| ... static def generateVersion() { if (System.getenv("CI") != null) { def branch = System.getenv("CIRCLE\_BRANCH").replace("/", "\_").toLowerCase() def buildNum = System.getenv("BUILD\_NUM") return branch + "-b" + buildNum } else { return "local" } } ... |
| **init-gradle** action script (`./build.gradle`) |

**Now, regarding** `init-gradle/actions.yml`

Note the that in the AWS credentials are available as secrets, but they aren’t accessible directly, so they have to be passed as parameters (**lines 4~9**).

And related to Gradle `generateVersion()`'s environment variables, we will need the `branch` and `version` for for it. They are available in the `github` context, but not reachable from the local composite action .  
So they should be passed as parameters (**lines 10~15**).  
We’ll see later how to provide the arguments.

|  |
| --- |
| name: init-gradle inputs: aws\_access\_key\_id: required: true description: "The aws\_access\_key\_id used to authenticate with AWS" aws\_secret\_access\_key: required: true description: "The aws\_secret\_access\_key used to authenticate with AWS" branch: required: true description: "The branch to work on" version: required: true description: "The version to build and publish" runs: using: "composite" steps: - name: Set up S3 credentials for gradle shell: bash run: | PROPFILE=~/.gradle/gradle.properties mkdir -p `dirname $PROPFILE` [ -e $PROPFILE ] || touch $PROPFILE grep -q s3\_access\_key $PROPFILE || echo "s3\_access\_key=${{ inputs.aws\_access\_key\_id }}" >> $PROPFILE grep -q s3\_secret\_key $PROPFILE || echo "s3\_secret\_key=${{ inputs.aws\_secret\_access\_key }}" >> $PROPFILE - name: Set up gradle build environment. shell: bash run: | echo "export GH=Github environment" >> build.env echo "export BRANCH=${{ inputs.branch }}" >> build.env echo "export GITHUB\_RUN\_NUMBER=${{ inputs.version }}" >> build.env - name: Setup Java uses: actions/setup-java@v4 with: distribution: 'corretto' java-version: 17 - name: Setup Gradle uses: gradle/actions/setup-gradle@v4 |
| **init-gradle** action script (`./.github/actions/init-gradle/action.yml`) |

### **Result**

**There’s a warning at the end of this section! It might be easy to overlook it, PLEASE DON’T!**

Once you have declared both local composite actions (see image below). You can use them in your workflow `test-build-publish-image` (see code below image).

|  |
| --- |
|  |
| Your `.github` folder content at the moment. |

In order to use the local composite actions in a workflow, you are required to add a previous `checkout` step (see **lines 17~18**).  
Then you can add `init-aws` and `init-gradle` steps (**lines 20~24** and **26~32**, respectively).  
Please, note how the required parameters for `init-aws` and `init-gradle` are passed as arguments (**lines 23~24** and **lines 29~32** respectively).

Note as well that a reusable workflows, requires to define the secrets to use (as if input parameters would be), probably to protect from wrong access to sensitive data. Therefore, we’d have to define the them under `workflow_call:` (**lines 5~9**). Later, in the main workflow, they should be provided as such (secrets).

So far, your `test-build-publish-image` should look like this:

|  |
| --- |
| name: test-build-publish-image on: workflow\_call: secrets: aws\_access\_key\_id: required: true aws\_secret\_access\_key: required: true jobs: test-build-publish-image: name: ' ' runs-on: ubuntu-latest steps: # This step is needed only to be able to invoke the local git actions (in the next 2 steps). - name: Check out repository code uses: actions/checkout@v4 - name: Setting AWS uses: ./.github/actions/init-aws with: aws\_access\_key\_id: ${{ secrets.aws\_access\_key\_id }} aws\_secret\_access\_key: ${{ secrets.aws\_secret\_access\_key }} - name: Setting Gradle uses: ./.github/actions/init-gradle with: aws\_access\_key\_id: ${{ secrets.aws\_access\_key\_id }} aws\_secret\_access\_key: ${{ secrets.aws\_secret\_access\_key }} branch: ${{ github.ref\_name }} version: ${{ github.run\_id }}.${{ github.run\_number }}.${{ github.run\_attempt }} - name: Run unitTest step run: | ./gradlew test - name: Building the image run: | source build.env ./gradlew build - name: Building docker image run: | source build.env ./gradlew bootBuildImage - name: Publish docker image to ECR repository run: | source build.env ./gradlew dockerPushImage |
| Current state of `./.github/workflows/test-build-publish-image.yml` ( **still in progress!**). |

And to finalize this the `test-build-publish-image` section, let’s use it in the `main.yml` workflow.  
Note the changes in the 1st job in `main.yml` (**lines 6~11**): the clause `run:` has been replaced by the `uses:` of the `test-build-publish-image` reusable workflow:

|  |
| --- |
| name: Main workflow run-name : ${{ github.event.head\_commit.message }} on: [push] jobs: test-build-publish-image: name: Test, build, and publish image uses: ./.github/workflows/test-build-publish-image.yml secrets: aws\_access\_key\_id: ${{ secrets.AWS\_ACCESS\_KEY\_ID }} aws\_secret\_access\_key: ${{ secrets.AWS\_SECRET\_ACCESS\_KEY }} deploy-on-production: if: github.ref\_name == 'master' needs: test-build-publish-image name: Deploying on Master environment: production run: echo "Deploying on Master" deploy-on-develop: if: github.ref\_name != 'master' needs: test-build-publish-image name: Deploying on Develop environment: develop run: echo "Deploying on Develop" deploy-on-staging: if: github.ref\_name != 'master' needs: test-build-publish-image name: Deploying on staging environment: staging run: echo "Deploying on Staging" |
| Current state of `./.github/workflows/main.yml` |

**At this point, when running your the workflow, it might fail due to due to a using a custom Gradle wrapper.**  
GitHub Actions checks the detect that its signature doesn’t match to the **public checksum** of the Gradle wrapper version it’s declared in your `gradle/wrapper/gradle-wrapper.properties` file and won’t let you continue.  
Please, see the troubleshooting section [Gradle Wrapper JAR failed validation](https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/530251778/2.c.+Creating+a+backend+workflow+in+the+project+repository+evolutionary#Gradle-Wrapper-Jar-failed-validation).

## Deploy (job)

As stated before, this steps needs the job `test-build-publish-image` to finish successfully  .

This job consists of:

> 2. …
> 3. **Environment deploy**
>
>    1. Indicate Kubernetes cluster.
>    2. Configure Helm: add Teqplay repo and update it ( it needs the AWS access credentials).
>    3. Deploy image (published in step 1.a.iii)

**This job is rather complex to understand as a whole**, because for different reasons we’d have to modify it to achieve the whole aim functionality.  
**So, we’ll go step-by-step** (please excuse the redundancy) through it.

### Shallow job steps:

**First,** let’s create `deploy` job with simple **shallow steps** in the file `./github/workflows/deploy.yml`:

|  |
| --- |
| name: eks-deployment on: workflow\_call: env: NAMESPACE: voyage jobs: deploy: name: ' ' runs-on: ubuntu-latest steps: - name: Init kubeconfig run: echo 'Init kubeconfig' - name: Set helm-charts repo run: echo help repo add and update step - name: Deploy run: echo Deploying image on environment |
| Shallow deploy reusable workflow in the file `./github/workflows/deploy.yml` |

### Init kubeconfig

Now, let’s fill the `Init kubeconfig` step, which will indicate helm in which cluster (`CLUSTER_NAME` in **lines 33-38**) to deploy and the AWS region (using the [Github **organization action variable**](https://github.com/organizations/teqplay/settings/variables/actions) `${{ vars.AWS_REGION }}` in **line 39)**.

For this, we’ll need the **eks cluster**, which we decide on the spot based on the `environment` (**line 19~24**).  
Therefore, we’ll need to provide the `environment` where to deploy as a workflow input parameter (**lines 6~8**).  
This will be provided as argument in the `main.yml`. We’ll see it later.

However, as we are using the `aws` command, again we need the AWS credentials.  
So let’s use the reusable local composite action `init-aws` (**lines 25~29**), for which we need to provide the AWS credentials (**lines 28~29**), which should be available as workflow secrets (**lines 9~13**) (*pheeeew* ).

Let’s not forget that, in order to invoke a local composite action, we’d need to call `checkout` as a previous step (**lines 22~23**).

|  |
| --- |
| name: eks-deployment on: workflow\_call: inputs: environment: required: true type: string secrets: aws\_access\_key\_id: required: true aws\_secret\_access\_key: required: true env: NAMESPACE: voyage jobs: deploy: name: ' ' runs-on: ubuntu-latest steps: - name: Check out repository code uses: actions/checkout@v4 - name: Setting AWS uses: ./.github/actions/init-aws with: aws\_access\_key\_id: ${{ secrets.aws\_access\_key\_id }} aws\_secret\_access\_key: ${{ secrets.aws\_secret\_access\_key }} - name: Init kubeconfig run: | case ${{ inputs.environment }} in production) CLUSTER\_NAME="production" ;; develop) CLUSTER\_NAME="develop" ;; staging) CLUSTER\_NAME="develop" ;; \*) CLUSTER\_NAME="" esac aws eks update-kubeconfig --name $CLUSTER\_NAME --alias $CLUSTER\_NAME --region ${{ vars.AWS\_REGION }} - name: Set helm-charts repo run: echo help repo add and update step - name: Deploy run: echo Deploying image on environment |
| `Init kubeconfig` step complete! |

If the previous invocation to `init-aws` was fine (in the `test-build-publish-image` job), there’s no reason credentials are invalid. If you have any issue in this step, it might be because the secrets were not correctly passed as arguments.

### Set helm charts repo

Now, let’s go to the next step of **adding Teqplay’s chartmuseum to the helm repositories**.

Please, notice that our chartmuseum (`https://chartmuseum.teqplay.nl`) is password protected. Thus, we’ll require the credentials (defined as [organization secrets in GitHub.com](https://github.com/organizations/teqplay/settings/secrets/actions)) in the process. Added to the workflow’s secrets section (**lines 14-17**) and used in the first helm command (**line 47**).  
Let’s not forget they have to be passed when using the `deploy` workflow in `main.yml`.

|  |
| --- |
| name: eks-deployment on: workflow\_call: inputs: environment: required: true type: string secrets: aws\_access\_key\_id: required: true aws\_secret\_access\_key: required: true cm\_username: required: true cm\_password: required: true env: NAMESPACE: voyage jobs: deploy: name: ' ' runs-on: ubuntu-latest steps: - name: Check out repository code uses: actions/checkout@v4 - name: Setting AWS uses: ./.github/actions/init-aws with: aws\_access\_key\_id: ${{ secrets.aws\_access\_key\_id }} aws\_secret\_access\_key: ${{ secrets.aws\_secret\_access\_key }} - name: Init kubeconfig run: | case ${{ inputs.environment }} in production) CLUSTER\_NAME="production" ;; develop) CLUSTER\_NAME="develop" ;; staging) CLUSTER\_NAME="develop" ;; \*) CLUSTER\_NAME="" esac aws eks update-kubeconfig --name $CLUSTER\_NAME --alias $CLUSTER\_NAME --region ${{ vars.AWS\_REGION }} - name: Set helm-charts repo run: | helm repo add teqplay https://chartmuseum.teqplay.nl --username ${{ secrets.cm\_username }} --password ${{ secrets.cm\_password }} helm repo update - name: Deploy run: echo Deploying image on environment |
| `Set helm-charts repo` complete. |

If the *ChartMuseum*’s credentials are valid, their secrets are well set in Github and there’s no misuse in the workflow `*.yml` files, everything should be fine!

### Actual deploy step!

And for the last step, the actual deploy! This is a bit more complex. Our step’s target is to invoke:

helm upgrade $RELEASE teqplay/skeleton-mongo-app -n $NAMESPACE -f ./helm/values.yaml -f $HELM\_VALUES --set image.tag=${{ inputs.image\_tag }} -i

For that, we have to use or decide:

1. The `RELEASE` where to deploy, based on the ***naked*** repository name:

   1. stripped folder’s prefix and of `-backend` suffix (**line 60**)
   2. and *lowercased* (**line 62**).
   3. appended the environment suffix (**lines 64~79**) when needed.
2. The `namespace` (well, that’s not a decision, but a project specific fix value) of the release (**line 22**).
3. The (`HELM_VALUES`) file, which is environment’s specific (**lines 64~79**).
4. The **image** to deploy (that was produced in the `test-build-publish-image`, so it’d require:

   1. to be declared as a workflow input parameter (**lines 9~11**)!
   2. to be declared as output and a return it in `test-build-publish-image` ( see line changes later **in the second code snippet** `test-build-publish-image.yml` )
   3. to pipe `test-build-publish-image`’s output with `deploy`’s input in the `main.yml` ( see line changes later **in the third** `main.yml` **snippet**).  
      If you want to know more about passing values between jobs and steps in GitHub, read this<https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/passing-information-between-jobs>

**For a last change in** `deploy.yml`, as we intend to use it as a job replacement in `main.yml`, we’re forced to move the environment approval control (`environment:` statement) inside the deploy (**see line 27**).

Here’s the `deploy.yml` state so far:

|  |
| --- |
| name: eks-deployment on: workflow\_call: inputs: environment: required: true type: string image\_tag: required: true type: string secrets: aws\_access\_key\_id: required: true aws\_secret\_access\_key: required: true cm\_username: required: true cm\_password: required: true env: NAMESPACE: voyage jobs: deploy: name: ' ' environment: ${{ inputs.environment }} runs-on: ubuntu-latest steps: - name: Check out repository code uses: actions/checkout@v4 - name: Setting AWS uses: ./.github/actions/init-aws with: aws\_access\_key\_id: ${{ secrets.aws\_access\_key\_id }} aws\_secret\_access\_key: ${{ secrets.aws\_secret\_access\_key }} - name: Init kubeconfig run: | case ${{ inputs.environment }} in production) CLUSTER\_NAME="production" ;; develop) CLUSTER\_NAME="develop" ;; staging) CLUSTER\_NAME="develop" ;; \*) CLUSTER\_NAME="" esac aws eks update-kubeconfig --name $CLUSTER\_NAME --alias $CLUSTER\_NAME --region ${{ vars.AWS\_REGION }} - name: Set helm-charts repo run: | helm repo add teqplay https://chartmuseum.teqplay.nl --username ${{ secrets.cm\_username }} --password ${{ secrets.cm\_password }} helm repo update - name: Deploy run: | # Let's do it in steps so it's more readable # FULL\_REPO\_NAME follows the pattern 'teqplay/repositoryName-backend' in the case of backends. FULL\_REPO\_NAME=${{ github.repository }} # Next step removes any folder type prefix and removes the prefix -backend. REPO\_NAME=$(basename $FULL\_REPO\_NAME -backend ) # Now, let's lowercase it. REPO\_NAME\_LOWERCASE="${REPO\_NAME,,}" # Set HELM\_VALUES and RELEASE depending on the environment. case ${{ inputs.environment }} in production) HELM\_VALUES="./helm/values.prod.yaml" RELEASE=$REPO\_NAME\_LOWERCASE ;; develop) HELM\_VALUES="./helm/values.dev.yaml" RELEASE=$REPO\_NAME\_LOWERCASE-dev ;; staging) HELM\_VALUES="./helm/values.staging.yaml" RELEASE=$REPO\_NAME\_LOWERCASE-staging ;; \*) echo "Wrong environment value ${{ inputs.environment }} (valid values production, develop and staging)." exit -1 esac echo Deploying image '${{ inputs.image\_tag }}'. helm upgrade $RELEASE teqplay/skeleton-mongo-app -n $NAMESPACE -f ./helm/values.yaml -f $HELM\_VALUES --set image.tag=${{ inputs.image\_tag }} -i |
| `Set helm-charts repo` complete. |

Again, notice the changes in `test-build-publish-image.yml`:

* declaration of the `test-build-publish-image`’s output `image_tag` (**lines 10~13**)
* workflow’s jobs output declaration in lines 19~20

  + note we have set the step id where it’s produced `building_step_id` (see also **line 45**).
* set the actual output in the step `Building the image` (**lines 51~53**)

|  |
| --- |
| name: test-build-publish-image on: workflow\_call: secrets: aws\_access\_key\_id: required: true aws\_secret\_access\_key: required: true outputs: image\_tag: description: "Produced and published image tag" value: ${{ jobs.test-build-publish-image.outputs.image\_tag }} jobs: test-build-publish-image: name: ' ' runs-on: ubuntu-latest outputs: image\_tag: ${{ steps.building\_step\_id.outputs.image\_tag }} steps: # This step is needed only to be able to invoke the local git actions (in the next 2 steps). - name: Check out repository code uses: actions/checkout@v4 - name: Setting AWS uses: ./.github/actions/init-aws with: aws\_access\_key\_id: ${{ secrets.aws\_access\_key\_id }} aws\_secret\_access\_key: ${{ secrets.aws\_secret\_access\_key }} - name: Setting Gradle uses: ./.github/actions/init-gradle with: aws\_access\_key\_id: ${{ secrets.aws\_access\_key\_id }} aws\_secret\_access\_key: ${{ secrets.aws\_secret\_access\_key }} branch: ${{ github.ref\_name }} version: ${{ github.run\_id }}.${{ github.run\_number }}.${{ github.run\_attempt }} - name: Run unitTest step run: | ./gradlew test - name: Building the image id: building\_step\_id run: | source build.env ./gradlew build # For readability: # - produce IMAGE\_TAG: IMAGE\_TAG=$(./gradlew -q getVersion | tail -n 1) # - and now make sure it's piped to the job step's job output: echo "image\_tag=$IMAGE\_TAG" >> "$GITHUB\_OUTPUT" - name: Building docker image run: | source build.env ./gradlew bootBuildImage - name: Publish docker image to ECR repository run: | source build.env ./gradlew dockerPushImage |
| Updated `test-build-publish-image.yml` |

Once more, remember changes in `main.yml`:

* using the new `deploy.yml` reusable workflow for jobs with their respective inputs and secrets:

  + `deploy-on-production` (**lines 16~24**)
  + `deploy-on-develop` (**lines 29~37**)
  + `deploy-on-staging` (**lines 24~50**)
* *piping* `test-buld-publish-image` job’s output to each `deploy` job’s input (**lines 19, 32 and 45**)  
   Note the use of `${{ needs.test-build-publish-image.outputs.image_tag }}`

|  |
| --- |
| name: Main workflow run-name : ${{ github.event.head\_commit.message }} on: [push] jobs: test-build-publish-image: name: Test, build, and publish image uses: ./.github/workflows/test-build-publish-image.yml secrets: aws\_access\_key\_id: ${{ secrets.AWS\_ACCESS\_KEY\_ID }} aws\_secret\_access\_key: ${{ secrets.AWS\_SECRET\_ACCESS\_KEY }} deploy-on-production: if: github.ref\_name == 'master' needs: test-build-publish-image name: Deploying on Master uses: ./.github/workflows/deploy.yml with: environment: production image\_tag: ${{ needs.test-build-publish-image.outputs.image\_tag }} secrets: aws\_access\_key\_id: ${{ secrets.AWS\_ACCESS\_KEY\_ID }} aws\_secret\_access\_key: ${{ secrets.AWS\_SECRET\_ACCESS\_KEY }} cm\_username: ${{ secrets.CM\_USERNAME }} cm\_password: ${{ secrets.CM\_PASSWORD }} deploy-on-develop: if: github.ref\_name != 'master' needs: test-build-publish-image name: Deploying on Develop uses: ./.github/workflows/deploy.yml with: environment: develop image\_tag: ${{ needs.test-build-publish-image.outputs.image\_tag }} secrets: aws\_access\_key\_id: ${{ secrets.AWS\_ACCESS\_KEY\_ID }} aws\_secret\_access\_key: ${{ secrets.AWS\_SECRET\_ACCESS\_KEY }} cm\_username: ${{ secrets.CM\_USERNAME }} cm\_password: ${{ secrets.CM\_PASSWORD }} deploy-on-staging: if: github.ref\_name != 'master' needs: test-build-publish-image name: Deploying on Staging uses: ./.github/workflows/deploy.yml with: environment: staging image\_tag: ${{ needs.test-build-publish-image.outputs.image\_tag }} secrets: aws\_access\_key\_id: ${{ secrets.AWS\_ACCESS\_KEY\_ID }} aws\_secret\_access\_key: ${{ secrets.AWS\_SECRET\_ACCESS\_KEY }} cm\_username: ${{ secrets.CM\_USERNAME }} cm\_password: ${{ secrets.CM\_PASSWORD }} |
| Updated `main.yml` |

However this is still unfinished!  
All changes until now together will fail in GitHub Actions **due to lines 14, 28 and 42**.  
**The reason** is that when replacing a job by a reusable workflow, `if:` statements are not allowed in the *outer* job declaration (blame GitHub.com).

### **Environment deployment protection – 2nd half**

For closure of the the `deploy` job, and as promised in the section [Environment deployment protection – 1st part](https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/495091714/General+backend+project+migration+steps#Branch-deployment-protection) (it was too early back then to address this), **we should protect the environment deployment of the right images!**

Continuing the last statement at the end of the previous sub-section, we can’t use the conditional statements in `main.yml`.  
Therefore, **we have to move it inside** of the `deploy.yml` to maintain the **protection**.

**Not all are bad news: there’s an implicit benefit** of including the conditional statement in the `deploy.yml` workflow: `deploy.yml` can’t be misused to deploy an image not intended for a given environment (so everything will be deploy in the allowed places by definition).

Thus, changes are:

1. In `main.yml`:

   1. **Lines 13, 26 and 39**: let’s remove the if statements in **deploy-on-*****environment*** jobs.
2. In `deploy.yml`:

   1. **Line 26**: add an *all-rounded* `if:` statement allowing the workflow execution only in cases:

      1. **branch** is `master` AND **environment** is `production`
      2. **branch** IS NOT `master` AND **environment** IS NOT `production`

|  |
| --- |
| name: Main workflow run-name : ${{ github.event.head\_commit.message }} on: [push] jobs: test-build-publish-image: name: Test, build, and publish image uses: ./.github/workflows/test-build-publish-image.yml secrets: aws\_access\_key\_id: ${{ secrets.AWS\_ACCESS\_KEY\_ID }} aws\_secret\_access\_key: ${{ secrets.AWS\_SECRET\_ACCESS\_KEY }} deploy-on-production: needs: test-build-publish-image name: Deploying on Master uses: ./.github/workflows/deploy.yml with: environment: production image\_tag: ${{ needs.test-build-publish-image.outputs.image\_tag }} secrets: aws\_access\_key\_id: ${{ secrets.AWS\_ACCESS\_KEY\_ID }} aws\_secret\_access\_key: ${{ secrets.AWS\_SECRET\_ACCESS\_KEY }} cm\_username: ${{ secrets.CM\_USERNAME }} cm\_password: ${{ secrets.CM\_PASSWORD }} deploy-on-develop: needs: test-build-publish-image name: Deploying on Develop uses: ./.github/workflows/deploy.yml with: environment: develop image\_tag: ${{ needs.test-build-publish-image.outputs.image\_tag }} secrets: aws\_access\_key\_id: ${{ secrets.AWS\_ACCESS\_KEY\_ID }} aws\_secret\_access\_key: ${{ secrets.AWS\_SECRET\_ACCESS\_KEY }} cm\_username: ${{ secrets.CM\_USERNAME }} cm\_password: ${{ secrets.CM\_PASSWORD }} deploy-on-staging: needs: test-build-publish-image name: Deploying on Staging uses: ./.github/workflows/deploy.yml with: environment: staging image\_tag: ${{ needs.test-build-publish-image.outputs.image\_tag }} secrets: aws\_access\_key\_id: ${{ secrets.AWS\_ACCESS\_KEY\_ID }} aws\_secret\_access\_key: ${{ secrets.AWS\_SECRET\_ACCESS\_KEY }} cm\_username: ${{ secrets.CM\_USERNAME }} cm\_password: ${{ secrets.CM\_PASSWORD }} |
| Updated `main.yml` |

Again:

> 1. …
> 2. In `deploy.yml`:
>
>    1. **Line 26**: add an *all-rounded* `if:` statement allowing the workflow execution only in cases:
>
>       1. **branch** is `master` AND **environment** is `production`
>       2. **branch** IS NOT `master` AND **environment** IS NOT `production`

|  |
| --- |
| name: eks-deployment on: workflow\_call: inputs: environment: required: true type: string image\_tag: required: true type: string secrets: aws\_access\_key\_id: required: true aws\_secret\_access\_key: required: true cm\_username: required: true cm\_password: required: true env: NAMESPACE: voyage jobs: deploy: if: ${{ (github.ref\_name == 'master' && inputs.environment == 'production') || (github.ref\_name != 'master' && inputs.environment != 'production') }} name: ' ' environment: ${{ inputs.environment }} runs-on: ubuntu-latest steps: - name: Check out repository code uses: actions/checkout@v4 - name: Setting AWS uses: ./.github/actions/init-aws with: aws\_access\_key\_id: ${{ secrets.aws\_access\_key\_id }} aws\_secret\_access\_key: ${{ secrets.aws\_secret\_access\_key }} - name: Init kubeconfig run: | case ${{ inputs.environment }} in production) CLUSTER\_NAME="production" ;; develop) CLUSTER\_NAME="develop" ;; staging) CLUSTER\_NAME="develop" ;; \*) CLUSTER\_NAME="" esac aws eks update-kubeconfig --name $CLUSTER\_NAME --alias $CLUSTER\_NAME --region ${{ vars.AWS\_REGION }} - name: Set helm-charts repo run: | helm repo add teqplay https://chartmuseum.teqplay.nl --username ${{ secrets.cm\_username }} --password ${{ secrets.cm\_password }} helm repo update - name: Deploy run: | # Let's do it in steps so it's more readable # FULL\_REPO\_NAME follows the pattern 'teqplay/repositoryName-backend' in the case of backends. FULL\_REPO\_NAME=${{ github.repository }} # Next step removes any folder type prefix and removes the prefix -backend. REPO\_NAME=$(basename $FULL\_REPO\_NAME -backend ) # Now, let's lowercase it. REPO\_NAME\_LOWERCASE="${REPO\_NAME,,}" # Set HELM\_VALUES and RELEASE depending on the environment. case ${{ inputs.environment }} in production) HELM\_VALUES="./helm/values.prod.yaml" RELEASE=$REPO\_NAME\_LOWERCASE ;; develop) HELM\_VALUES="./helm/values.dev.yaml" RELEASE=$REPO\_NAME\_LOWERCASE-dev ;; staging) HELM\_VALUES="./helm/values.staging.yaml" RELEASE=$REPO\_NAME\_LOWERCASE-staging ;; \*) echo "Wrong environment value ${{ inputs.environment }} (valid values production, develop and staging)." exit -1 esac echo Deploying image '${{ inputs.image\_tag }}'. helm upgrade $RELEASE teqplay/skeleton-mongo-app -n $NAMESPACE -f ./helm/values.yaml -f $HELM\_VALUES --set image.tag=${{ inputs.image\_tag }} -i |
| Updated `deploy.yml` |

Warning ahead!  
The result in GitHub is uglier than in CircleCI, but it has the benefit of only allow a selected group of actors to act/deploy in each environment.

When clicking on any of these (green squares):

You are presented with this:

And, when clicking on “Review pending deployments”, you presented with:

Where you finally can approve (at once) a selection of the presented environments.

### All together

Forgive me if I don’t bring up all files until here (I’ve already written a lot of snippets). But I think if you have followed the guide and fought your particular project particularities, your version is better  and more robust  than this guide’s.

But I can show you how the new `deploy.yml` file, together with the changes in `main.yml`, `test-build-publish-image.yml` (covered in the **Deploy** section), would look like in GitHub:

|  |
| --- |
|  |
| GitHub result of our new steps. No big changes, though, but that’s good! |

When approving a deploy step, you’d see the progress and, eventually, a green icon on it!

### Scripts wrap-up: folders and scripts

As a working example, you can go to GitHub cargooptima's repo and see the PR ( to add a link when is migrated).

Here it’s the final `.github` folder content:

|  |
| --- |
|  |
| Expected folder content of `./.github` in your repository. |

Hopefully, if no particular errors, your GitHub Actions should be in shape!

## Troubleshooting

### Enable debug logging in GitHub actions

When a GitHub workflow fails, you can re-run it enabling ***debug logging***. See screenshot below.

Then you will see your workflow steps as such (see purple lines):

### Sudden stop of workflow progress

If your workflow stops displaying step progress (i.e. empty steps), it might be because you are using a non existing [**Organization** variable](https://github.com/organizations/teqplay/settings/secrets/actions) (did you forget to declare it? or was it deleted?).

### Gradle Wrapper Jar failed validation

Gradle step failed with a similar message to this:

...
✗ Found unknown Gradle Wrapper JAR files:
5c9b7c88dad7622cbc1eb09dbd71d7fec253d1cbd684ee848d84fded5cf43c86 gradle/wrapper/gradle-wrapper.jar
Error: Error: At least one Gradle Wrapper Jar failed validation!
...

1. **Possible reason:** your project is using a custom made gradle wrapper version, by any of us or the original OS where the project was set up.
2. **Possible solution:** reset gradle wrapper version to the official same one with this

   ~$ ./gradlew wrapper --gradle-version 7.5.1

   This will probably make changes in the following files:

   ~$ git status
   On branch migration/branch
   Changes not staged for commit:
   (use "git add <file>..." to update what will be committed)
   (use "git restore <file>..." to discard changes in working directory)
   modified: gradle/wrapper/gradle-wrapper.jar
   modified: gradle/wrapper/gradle-wrapper.properties
   modified: gradlew
   modified: gradlew.bat

### Error resolving Teqplay libraries

Gradle build failed fetching Teqplay skeleton libraries:

...
FAILURE: Build failed with an exception.
\* What went wrong:
Execution failed for task ':compileKotlin'.
> Could not resolve all files for configuration ':compileClasspath'.
> Could not resolve nl.teqplay.skeleton:common:1.7.0.
Required by:
project :
> Could not resolve nl.teqplay.skeleton:common:1.7.0.
> Could not get resource 's3://repo.teqplay.nl/release/nl/teqplay/skeleton/common/1.7.0/common-1.7.0.pom'.
> Access Denied (Service: Amazon S3; Status Code: 403; Error Code: AccessDenied; Request ID: BQ330C31FX0BSG...
...

1. **Possible reason**: Problem with AWS credentials. The [**Organization** secrets](https://github.com/organizations/teqplay/settings/secrets/actions) `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` should be set, used and valid so the GitHub script can access.  
    The associated IAM user (initially ***GitHub-ci***) should have access to the resources set in the user group ***ci-deployments***.
2. **Possible solution:** Verify the AWS credentials are set, used and correct. If they are wrong, ask **tech support** to provide you the correct credentials.

### Other problems

Please, create Confluence comments to this page and name me  here to update this sections with the special case problems you find in your CI/CD migration.

## Considerations

### Context variables and secrets

Your GitHub actions script-set will probably use a bunch of secrets and variables in order to make it configurable and avoid unnecessary commits.  
Thus, in example, in case of needing to rotate or reset some specific credentials, it’d be sufficient to change the associated secrets and variables.

A set of secrets and variables have been set in the [**Organization** variables and secrets](https://github.com/organizations/teqplay/settings/secrets/actions) section (which has been mentioned more than a couple of times in this guide).

In case you need project specific ones, please use the [**Repository** variables and secrets](https://github.com/teqplay/cargo-optima-backend-sandbox/settings/secrets/actions). If you create a *Repository secret,* please, add them to **BitWarden** for future reference, as they will be encrypted and not visible in GitHub.

### Unclassified notes:

1. In case you need to customize your scripts to suit your project, here it is the GitHub Workflow syntax: <https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions>
2. Triggers: <https://docs.github.com/en/actions/about-github-actions/understanding-github-actions#events>
3. project **JDK** **distribution** and version: [https://GitHub.com/actions/setup-java/blob/83a06ff9d9aa70f76a8d73278e646c20b2bf1ae5/README.md#supported-version-syntax](https://github.com/actions/setup-java/blob/83a06ff9d9aa70f76a8d73278e646c20b2bf1ae5/README.md#supported-version-syntax)
4. If you want to enjoy the dependencies cache between gradle executions, you must upgrade gradle to 8.6 or newer (see <https://github.com/gradle/actions/blob/main/docs/setup-gradle.md#saving-configuration-cache-data>).  
   It is recommended to set up gradle so to use an encryption key for the cache (as the gradle cache stores sensitive data in the runner’s filesystem, so available during the runner lifetime) and run gradle commands with the option `--configuration-cache`.

    - uses: gradle/actions/setup-gradle@v4
   with:
   gradle-version: 8.6
   cache-encryption-key: ${{ secrets.GradleEncryptionKey }}
   - run: gradle build --configuration-cache
5. More about cache dependencies [https://docs.GitHub.com/en/actions/use-cases-and-examples/building-and-testing/building-and-testing-java-with-gradle#caching-dependencies](https://docs.github.com/en/actions/use-cases-and-examples/building-and-testing/building-and-testing-java-with-gradle#caching-dependencies)
6. Runner selection. Each job in GitHub Actions has its own independent runner, not shared with any other jobs. Hence, any specific environment setup (shell variables, files, etc, will not be available for other jobs in the job chain). Keep this in mind!  
   Read more here: <https://docs.github.com/en/actions/writing-workflows/choosing-where-your-workflow-runs/choosing-the-runner-for-a-job#standard-github-hosted-runners-for--private-repositories>
7. Different context accessibility by scope, *contextual information* in your scripts is not consistent, but in depends on the scope you use it.  
   I.e. secrets are not accessible in a reusable workflow. So if you need them, you’d have to find a way out, like using the workflow `inputs`.  
    It’d be a try-error process.  
   Read more [here about "Accessing contextual information about workflow runs"](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/accessing-contextual-information-about-workflow-runs#context-availability)
8. Clarify that the Gradle summary table displayed in the workflow’s GitHub Actions (just below the workflow illustration) is not under our control.  
   It’s an automatic report of all gradle commands run, thanks toour `init-gradle` composite action that makes use of the public `gradle/actions/setup-gradle@v4` (the final responsible!).