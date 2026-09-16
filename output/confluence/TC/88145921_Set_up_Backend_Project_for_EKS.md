---
id: confluence:88145921
source: confluence
type: page
space: TC
title: Set up Backend Project for EKS
author: Former user (Deleted)
date: '2022-09-27'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/88145921
explicit_links:
- github:npryce/konfig:issue:36
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/88145921
---
# Set up Backend Project for EKS

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/88145921  

## Content

## Prerequisites

* installed commands: `aws` and `helm` (optionally `docker` if you want to run any images locally)
* access to AWS console (& `skeleton-plugins` repo)

## Update your project

In your `build.gradle`:

* Update your `skeleton-plugins` version to `20220617-b634` (or later)

  + if you are going to upgrade past `20220805-b686`, then also review required migrations  
    Migrating skeleton-plugins past `20220805-b686`
* Update your `spring_boot_version` to `2.6.6` (or later, which `skeleton-plugins` also uses)
* `Springfox` is deprecated in favour of `Springdoc`, which requires you to update your annotations for Swagger to the Open API 3 specification (<https://springdoc.org/migrating-from-springfox.html> )

  + also, remove any dependencies for `springfox` and/or `swagger 2` if you have them, the `skeleton-plugins:swagger` contains all you need

This update adds a `bootBuildImage` Gradle task to your project, with which you can easily create an optimized container image for your app!

## Add `common-kubernetes` dependency

If you upgraded skeleton-plugins past `20220725-b662`, you should have followed the migration guide, in which this dependency was removed. If so, please skip this step.

You only need to add a `bootstrap.properties` in the `resources` folder containing `spring.cloud.kubernetes.enabled=false` to disable Kubernetes ConfigMaps for local development. This file must be committed as well.

Add the `common-kubernetes` dependency of the `skeleton-plugins` to your `build.gradle`. This will ensure that we can detect ConfigMaps in Kubernetes and provides a way of overwriting the Konfig configuration.

Now make sure to add an overwrite for this ConfigMap inside your Konfig configuration (and add the appropriate bean):

kotlin// bean
val kubernetesConfigMap: KubernetesConfigMap
// config override
kubernetesConfigMap.properties() overriding

Your configuration will then look something like:

@Configuration
open class KonfigConfiguration(
private val kubernetesConfigMap: KubernetesConfigMap
) {
@Bean
open fun configuration(): KonfigConfiguration {
return systemProperties() overriding
EnvironmentVariables() overriding
kubernetesConfigMap.properties() overriding
ConfigurationProperties.fromOptionalFile(pathToFile("version.properties")) overriding
ConfigurationProperties.fromOptionalFile(pathToFile("application.properties"))
}
// path hack: https://github.com/npryce/konfig/issues/36
private fun pathToFile(path: String) =
File(KonfigConfiguration::class.java.classLoader.getResource(path)?.file ?: "")
}

**Important**, the `common-kubernetes` package adds a client that will try to discover if it’s running within Kubernetes. You need to add a `bootstrap.properties` in the `resources` folder containing `spring.cloud.kubernetes.enabled=false` to disable this for local development. This file must be committed as well.

## Set up DEGRADED status for health checks

If you are dependent on other backends/services, you should check if a service is healthy and change to a DEGRADED status. That way, the following should hold true for your service:

| **Status** | **Description** |
| --- | --- |
| UP | fully operational, no issues |
| DEGRADED | degraded performance, but still operational  this service can continue to function |
| DOWN | this service can’t function, not operational  (must not be accessible to users) |

The skeleton-plugins modules that expose a `RestTemplate` for auth calls, health checks and normal requests support this DEGRADED status out of the box. Some examples:

* `platform-auth`
* `portcallplus-auth`
* `portreporter-auth`
* …

If a service like platform, portcall+, portreporter, etc. have a DOWN status, our service will get a DEGRADED status indicating we are impacted but still operational. If our credentials used for authentication are invalid, this status will transition to DOWN instead, to indicate we aren’t operational and need to make a fix.

You might wonder; “Why is all of this important? We only reported UP and DOWN before, why does this need to change?”. Within Kubernetes applications are health checked, to ensure only healthy applications serve users. If your application reports DOWN, even if it’s still operational, Kubernetes will in turn try to restart your application until it goes UP again. Let’s say you are dependent on platform and platform gets restarted, deployed or has an outage; your application’s status will transition to DOWN and Kubernetes will try to restart your application to resolve the issue. Obviously.. until the issue is fixed at the platform-end we will not go UP this way. This would be even worse if we would have two services that are dependent on each other. If one of the two would go DOWN the other would also go DOWN, Kubernetes would try to restart both of them, and both applications will stay in this restarting loop indefinitely… Yikes! So, it’s pretty important to differentiate between an “I’m DOWN and can’t function normally” versus a “I have decreased performance, but can still function (and serve users)”.

**Ensuring the DEGRADED status works**

* validate that you are using skeleton-plugins modules that support the DEGRADED status
* inspect your code for any manually exposed `HealthIndicator` beans

  + if you have none, you are free to continue
  + if you have one or more, you need to do the following:

    - Add the `common` and `actuator` skeleton-plugins modules to your `build.gradle`
    - Don’t use the standard `RestTemplate` as that doesn’t use correct timeouts, create a custom `RestTemplate` with low timeouts by running:  
      `val restTemplate = configureRestTemplateForLowTimeouts(restTemplateBuilder, rootUri)`
    - In the `doHealthCheck` method, wrap the `restTemplate` that’s checking the other service with `builder.degradedOnRestClientError`, like so:

      builder.degradedOnRestClientError {
      if (restTemplate.getForEntity<String>("/actuator/health").statusCode.is2xxSuccessful) {
      builder.up()
      } else {
      builder.degraded()
      }
      }

      This ensures that all failure cases will turn into a DEGRADED status, unless it’s a 401 Unauthorized (which will turn into a DOWN status).
    - Ensure that you use this `RestTemplate` with low timeouts for both auth and normal calls.
    - If you are using the `KeyCloakS2SClientWrapper` (or `Auth0S2SClientWrapper`), you have used the `create` method to get a `RestTemplate`, swap this with a `createForLowTimeouts` to be used for these health checks.
    - Combining these will ensure your health checks don’t time out and also don’t propagate a DOWN status, but a DEGRADED status instead.

Up to this point we made the assumption that you want a DEGRADED status when an upstream service goes DOWN. However, it could be that you have a requirement that your service should go DOWN as well if a certain upstream service goes down or isn’t available. If so:

* You should expose a custom bean that overwrites the `HealthIndicator` bean exposed by a skeleton-plugins module, use the `builder.down()` to get a DOWN status in that specific scenario.
* Expose your own bean that doesn’t use the DEGRADED logic, but instead uses DOWN.

Both of these should be a very concious decision though! This will mean the performance/availability of your service is more likely to be DOWN. In practice you should only do this if you are, for example, processing data and there is no point of running if an upstream service is not providing data. In no case should your service be accessible by users if you go this route though. If you serve users and need to request an upstream service that is DOWN, you should fail those requests gracefully and keep running to keep serving requests to users. Otherwise you could cripple the experience of a user, or worse cripple/bring down the architecture as a whole.

## Set up ECR

Navigate to the ECR (Elastic Container Registry) in the Amazon Console, and press `Create repository`.

Set the visibility to private and set the repository name to the project’s name in lowercase. ***Tag immutability***, ***Scan on push*** and ***KMS encryption*** can stay **DISABLED**. Then create the repository.

This is the location where your container images will be pushed to, you can view them here later.

### Set up lifecycle policy

After opening your newly created repository, go to the `Lifecycle Policy` tab. Go to the `Actions` menu and press `Edit JSON`. A popup will appear, copy-paste the JSON below, and press `Save`.

json{
"rules": [
{
"description": "prune production images (main)", "rulePriority": 1,
"action": { "type": "expire" },
"selection": {
"countType": "imageCountMoreThan", "countNumber": 20,
"tagStatus": "tagged",
"tagPrefixList": [ "main-" ]
}
},
{
"description": "prune production images (master)", "rulePriority": 2,
"action": { "type": "expire" },
"selection": {
"countType": "imageCountMoreThan", "countNumber": 20,
"tagStatus": "tagged",
"tagPrefixList": [ "master-" ]
}
},
{
"description": "prune develop images", "rulePriority": 3,
"action": { "type": "expire" },
"selection": {
"countType": "imageCountMoreThan", "countNumber": 20,
"tagStatus": "tagged",
"tagPrefixList": [ "develop-" ]
}
},
{
"description": "prune untagged images", "rulePriority": 4,
"action": { "type": "expire" },
"selection": {
"tagStatus": "untagged",
"countType": "sinceImagePushed", "countNumber": 1, "countUnit": "days"
}
},
{
"description": "prune other/old images", "rulePriority": 5,
"action": { "type": "expire" },
"selection": {
"tagStatus": "any",
"countType": "sinceImagePushed", "countNumber": 60, "countUnit": "days"
}
}
]
}

This will make sure that old container images are automatically pruned for you, and we’ll not be storing all created images over the lifetime of a project.

**Breakdown of stored images:**

* 20 most recent production/develop images are stored
* untagged images are removed after a day
* any other image (feature branch, etc.) are stored for 60 days

**Important**, since any other images than production/develop are pruned after 60 days; make sure you don’t deploy these images for a longer period, as those images will not exist anymore after that point. Please merge and deploy your changes in a timely fashion.

## Set up Helm & Kubernetes settings

Add a helm repository, the needed password can be found on LastPass:

helm repo add teqplay https://chartmuseum.teqplay.nl --username charts --password <\*\*\*>

This ensures that we have access to all Helm charts that are available within Teqplay. Like the `teqplay/skeleton-mongo-app` Helm chart, that we’ll be using later.

In your project root, create a directory called `helm`, this is where we will keep the configuration values for the skeleton helm chart. To this directory, we will be adding the default `values.yaml` with common options, and `values.dev.yaml` and `values.prod.yaml` with develop- and production-specific settings.

In `values.yaml` put the following content:

yamlglobal:
storageClass: "gp2"
namespaceOverride: "teqplay-app"
image:
repository: 050356841556.dkr.ecr.eu-west-1.amazonaws.com/<project name>
resources:
requests:
cpu: 100m
memory: 2048Mi
limits:
cpu: 1000m
memory: 2048Mi

Append one of these options to the same `values.yaml` file:

* if you don’t need a database OR if you are using a pre-existing database

  yamlmongodb:
  enabled: false
* otherwise, add the following content so a MongoDB container is created for your application

  yamlmongodb:
  auth:
  # The MongoDB container initializes a database with this name, and creates a
  # user with auto-generated password automatically
  enabled: true
  database: <database name>
  username: "application"
  persistence:
  # Optionally, set the disk size for the database. This can be enlarged later.
  size: 4Gi
  resources:
  # Optionally, by default it uses 0.1 vCPU and 512Mi request, 0.2 vCPU and 1024Mi limit
  requests:
  cpu: 0.1
  memory: 2Gi
  limits:
  cpu: 0.4
  memory: 4Gi

In the `resources` section, set the CPU and memory requirements to the right values for your application:

* Change `resources.requests` to the minimum your app needs (this will be used by Kubernetes to check which nodes contain enough resources for your app to run)
* Change `resources.limits` to the maximum allowed resources your app should use. (the JVM memory settings will automatically be calculated for you as we use the `bootBuildImage` task)

In `values.dev.yaml` only the hostname is set:

yamlhostname: <dev backend hostname>

Likewise, `values.prod.yaml` sets the hostname for the production environment:

yamlhostname: <prod backend hostname>
ingress:
group: "eks-prod"

### `replicaCount`, `deployStrategy` and making your app Highly Available

The default settings are `replicaCount: 1` and `deployStrategy: Recreate`, this reflects what you are already used to when running your app locally or on one instance. We only run one replica of our app, and we fully destroy and re-run our app when we want to restart or deploy. This is fine for apps that don’t need to be Highly Available, but be aware that your app will have some downtime when making a deployment, as it will destroy and recreate your app.

There are quite some other deployment strategies that could be employed, like: rolling update, blue/green, canary, etc. You can research the different deployment strategies yourself, as we’ll focuss on the rolling update which requires the least amount of additional setup.

First, change the `replicaCount` to the amount of replicas you’d need, it’s best practice to have a minimum of 2 to have a highly available service (this could be set higher if this is required by the amount of traffic or load your app is on).

Then, change the `deployStrategy: RollingUpdate`. We are essentially telling Kubernetes to deploy our app one-by-one. This means that during a deployment, you will experience no downtime, however be aware that two versions of your app will be running side-by-side until the deployment finishes.

**Important:** setting up a Highly Available app doesn’t come for free! There is no notion of sticky sessions by default, so you must expect your first request to hit replica X and the next request to either hit replica X again, or replica Y, Z, etc. You MUST thoroughly inspect your app before going the Highly Available route. Any in-memory cache should be inspected, for example: in CSI a user can make changes to a ship in the form of tickets, if the ticket is completed any changes to the ship are persisted to the database and reflected in-memory (say a MMSI changes). This will mean that only one replica of CSI will know about this change in-memory, and in replica X we can find the ship with another MMSI than in replica Y and Z!! So, be aware of this and inspect your app before making the move, to ensure you won’t encounter weird differences/issues between replicas.

### If you use `@PreDestroy`, or require graceful termination

When the pod, that your project is running is, is being terminated. Kubernetes will send a `SIGTERM` so your app can gracefully shut down. This will also make sure the `@PreDestroy` is being triggered. If you don’t shut down within 30 seconds, Kubernetes will send a `SIGKILL` to forcefully kill your application.

Please make sure your app gracefully shuts down within the default 30 seconds. If it doesn’t, please try to improve your shut down performance, as this can lead to major issues mostly in the form of downtime or added instability when using low or no replication.

If however, you are sure you need an extended period of time to gracefully shut down; you can set the `terminationGracePeriodSeconds` to any amount in seconds, as required by your application. Use this setting with caution though, there is a reason for it being a reasonable grace period already.

To learn more about how Kubernetes handles (graceful) termination, take a look at <https://cloud.google.com/blog/products/containers-kubernetes/kubernetes-best-practices-terminating-with-grace>

## Set up Circle CI

We are adding support for building container images and pushing them to AWS ECR.

**Additions to your** `build.gradle`

First, add support to the `build.gradle`, small snippets about what needs to be added are listed below, for a full `build.gradle` you can reference CSI for example.

groovyimport com.bmuschko.gradle.docker.tasks.image.DockerPushImage
buildscript {
ext {
...
ecr\_repo\_url = '050356841556.dkr.ecr.eu-west-1.amazonaws.com'
docker\_remote\_api\_version = '7.4.0'
aws\_ecr\_version = '0.7.0'
}
...
}
plugins {
...
id 'com.bmuschko.docker-remote-api' version "$docker\_remote\_api\_version"
id 'com.patdouble.awsecr' version "$aws\_ecr\_version"
}
...
version = generateVersion()
...
docker {
registryCredentials {
url.set(ecr\_repo\_url)
}
}
def dockerImageName = "$ecr\_repo\_url/${project.name.replace("-backend", "")}:${project.version}"
bootBuildImage {
imageName = dockerImageName
}
task dockerPushImage(type: DockerPushImage) {
images.add(dockerImageName)
}
task getVersion {
doLast {
println project.version
}
}
...
static def generateVersion() {
if (System.getenv('CI') != null) {
def branch = System.getenv('CIRCLE\_BRANCH').replace("/", "\_").toLowerCase()
def buildNum = System.getenv('BUILD\_NUM')
return branch + '-b' + buildNum
} else {
return 'local'
}
}

**Additions to your** `.circleci/config.yml`

We’ll be fully rewriting our `config.yml` to utilize re-usable commands and make our CircleCI configs look consistent in the process. Feel free to make additions yourself as well.

Important things that have changed/been added:

* using a custom `docker.image` for running in CircleCI, namely `050356841556.dkr.ecr.eu-west-1.amazonaws.com/cci-jdk11-aws-ecr-helm`, which contains JDK11 and the required commands
* set `version` to `2.1`
* using re-usable commands to clean up the `jobs`
* persisting the build number of the `build` job and tag for the Docker image into a `build.env` file, which we’ll use for the version numbers for S3, ECR and deploying
* using `setup_remote_docker` to gain access to the `docker` commands and Daemon
* building the container image itself
* add jobs for deploying to Kubernetes

Do note that this CircleCI config also contains `jobs` and `commands` for deploying to Beanstalk. Feel free to remove these if they are (or become) irrelevant.

yamldefaults: &defaults
working\_directory: ~/repo
docker:
- image: 050356841556.dkr.ecr.eu-west-1.amazonaws.com/cci-jdk11-aws-ecr-helm:2.0
aws\_auth:
aws\_access\_key\_id: $AWS\_ACCESS\_KEY
aws\_secret\_access\_key: $AWS\_SECRET\_KEY
version: 2.1
jobs:
build:
<<: \*defaults
steps:
- checkout\_and\_restore\_cache
- add\_credentials
- update\_cache
- test\_and\_build
- setup\_remote\_docker
- publish\_container\_image
- persist\_to\_workspace:
root: ~/repo
paths:
- build
- ./\*/build
- out
- version.properties
- build.env
publish-models:
<<: \*defaults
steps:
- checkout\_and\_restore\_cache
- attach\_workspace:
at: ~/repo
- add\_credentials
- publish\_models
beanstalk-deploy:
<<: \*defaults
steps:
- checkout\_and\_restore\_cache
- attach\_workspace:
at: ~/repo
- add\_credentials
- deploy\_to\_beanstalk
deploy:
<<: \*defaults
parameters:
cluster-name:
description: Name of the EKS cluster
type: string
develop:
description: If it's about a develop release
type: boolean
steps:
- checkout
- add\_credentials
- attach\_workspace:
at: ~/repo
- deploy\_to\_kubernetes:
cluster-name: << parameters.cluster-name >>
develop: << parameters.develop >>
workflows:
version: 2
build-approve-deploy:
jobs:
- build:
context: common-builds-context
- publish-models:
requires:
- build
filters:
branches:
only:
- master
- main
- develop
context: common-builds-context
- beanstalk-hold:
type: approval
requires:
- build
- beanstalk-deploy:
requires:
- beanstalk-hold
context: common-builds-context
- hold-develop:
type: approval
requires:
- build
- deploy:
name: deploy-develop
cluster-name: develop
develop: true
requires:
- hold-develop
context: common-builds-context
- hold-production:
type: approval
requires:
- build
filters:
branches:
only:
- master
- main
- deploy:
name: deploy-production
cluster-name: production
develop: false
requires:
- hold-production
context: common-builds-context
commands:
checkout\_and\_restore\_cache:
steps:
- checkout
- restore\_cache:
keys:
- v1-dependencies-{{ checksum "build.gradle" }}
# fallback to using the latest cache if no exact match is found
- v1-dependencies-
update\_cache:
steps:
- run: ./gradlew dependencies
- save\_cache:
paths:
- ~/.gradle
key: v1-dependencies-{{ checksum "build.gradle" }}
test\_and\_build:
steps:
- run:
name: Test and build
command: |
echo "export BUILD\_NUM=$CIRCLE\_BUILD\_NUM" >> build.env
source build.env
./gradlew test build
echo "export TAG=$(./gradlew -q getVersion | tail -n 1)" >> build.env
- run:
name: Save test results
command: |
mkdir -p ~/tests/junit
find . -type f -regex ".\*/build/test-results/.\*xml" -exec cp {} ~/tests/junit/ \;
when: always
- store\_test\_results:
path: ~/tests
add\_credentials:
steps:
- run:
name: Add S3 credentials
command: |
PROPFILE=~/.gradle/gradle.properties
mkdir -p `dirname $PROPFILE`
[ -e $PROPFILE ] || touch $PROPFILE
grep -q s3\_access\_key $PROPFILE || echo "s3\_access\_key = $AWS\_ACCESS\_KEY" >> $PROPFILE
grep -q s3\_secret\_key $PROPFILE || echo "s3\_secret\_key = $AWS\_SECRET\_KEY" >> $PROPFILE
- run:
name: Add AWS credentials
command: |
FILE=~/.aws/credentials
mkdir -p `dirname $FILE`
echo "[default]" > $FILE
echo "aws\_access\_key\_id = $AWS\_ACCESS\_KEY" >> $FILE
echo "aws\_secret\_access\_key = $AWS\_SECRET\_KEY" >> $FILE
deploy\_to\_beanstalk:
steps:
- run:
name: Deploy to Elastic Beanstalk
command: |
if [ "${CIRCLE\_BRANCH}" == "master" ]; then
./gradlew deployProduction
else
./gradlew deployStaging
fi
publish\_models:
steps:
- run:
name: Publish to S3 repository
command: |
source build.env
./gradlew publish
publish\_container\_image:
steps:
- run:
name: Build docker image
command: |
source build.env
./gradlew bootBuildImage
- run:
name: Publish docker image to ECR repository
command: |
source build.env
./gradlew dockerPushImage
deploy\_to\_kubernetes:
parameters:
cluster-name:
description: Name of the EKS cluster
type: string
develop:
description: If it's about a develop release
type: boolean
steps:
- run:
name: Init kubeconfig
command: |
aws eks update-kubeconfig --name << parameters.cluster-name >> --alias << parameters.cluster-name >> --region $AWS\_REGION
- run:
name: Init helm-charts repo
command: |
helm repo add teqplay https://chartmuseum.teqplay.nl --username $CM\_USERNAME --password $CM\_PASSWORD
helm repo update
- run:
command: |
source build.env
REPONAME=$(basename $CIRCLE\_PROJECT\_REPONAME -backend)
ENV="${REPONAME,,}"
if << parameters.develop >>; then
ENV=${ENV}-dev
fi
echo "$ENV > $TAG"
helm upgrade $ENV teqplay/skeleton-mongo-app -n teqplay-app --set image.tag=$TAG --reuse-values

After committing and pushing you’ll see the following in CircleCI:

As part of the `build` step, a container image of your application will be built and uploaded to ECR, which you have set up previously.

## Creating a ConfigMap

You can create a ConfigMap from the command line or by using Lens, the following will describe using Lens.

A ConfigMap is not required per se, if your app doesn’t require changes to the config, feel free to not set it up now and only do so when necessary.

* go to the `Configuration > ConfigMaps` section (make sure to select the `teqplay-app` namespace), here all ConfigMaps for the different apps reside
* press the `+` button at the bottom left near the console window, and press `Create resource`
* press the `Select Template ...` dropdown, and select `ConfigMap`
* set the `metadata.name` to your app’s name
* set the `metadata.namespace` to `teqplay-app`
* specify your values within the `data` section.  
  If your application has a considerable number of config variables in the environment, consider the following procedure:

  1. **Save your application environment**:

     1. Go to **Elastic Beanstalk** console > **Environments**
     2. **Select the environment** and select the ***Action > Save configuration*** (providing a name)
  2. **Download the saved configuration** from the Elastic Beanstalk S3 bucket

     1. Go to **Amazon S3 > Buckets**
     2. Access the **Elastic Beanstalk bucket** (search by *elasticbeanstalk*)
     3. Access the path **/resources/templates/<environment>/**, where the previously saved configuration has been placed.
  3. Get all config variables as plain text under the section “***aws:elasticbeanstalk:application:environment:**”*.
* create/save the ConfigMap
* the `my-app-name` ConfigMap should now be visible in the list

apiVersion: v1
kind: ConfigMap
metadata:
name: my-app-name
namespace: teqplay-app
data:
value1: 'true'
value2: Hello, World!
value3: '1'

**Important**, quotes aren’t required when specifying strings, they are required however when specifying booleans, ints, etc.

## The first deployment

Update your local helm repos. This is important to do before every first deployment to ensure you have the latest version of our `teqplay/skeleton-mongo-app` chart.

helm repo update

Execute the deploy command:

helm install <app-name> <helm-chart>
-n teqplay-app
--values ./helm/values.yaml
--values <prod/dev values>
--set image.tag=<container image tag>
--kube-context <context>

In order to make a first deployment you’ll need:

* `app-name` => for an app like CSI this would be, `csi-dev` for dev, and just `csi` for production
* the namespace where the app will be installed, set to `teqplay-app` with `-n` (short for `--namespace`)
* `helm-chart` => the Helm chart you’re using, for example `teqplay/skeleton-mongo-app`
* `values` => `./helm/values.dev.yaml` for dev, and `./helm/values.prod.yaml` for production (and default values set in `./helm/values.yaml`
* `container image tag` => the initial container image version/tag you want to deploy
* `kube-context` => the name of the kubecontext you want to use, either `develop` or `production`

**Important**, make sure you run these commands at the root of your project

Deploying the first version to dev (for CSI) looks like:

helm install csi-dev teqplay/skeleton-mongo-app -n teqplay-app --values ./helm/values.yaml --values ./helm/values.dev.yaml --set image.tag=develop-b42 --kube-context develop

Deploying the first version to production (for CSI) looks like:

helm install csi teqplay/skeleton-mongo-app -n teqplay-app --values ./helm/values.yaml --values ./helm/values.prod.yaml --set image.tag=master-b42 --kube-context production

After this step you’ll be able to deploy via CircleCI. CircleCI runs the `helm upgrade` command, which will update the `image.tag` to the container image version that was just built and re-use the values that were previously supplied. To be able to execute `helm upgrade` we must install the app first, hence using the `helm install` manually and supplying the initial image and required values.

## Logging

Everything that your application prints to `stdout` and `stderr` will be captured by EKS. You can use Lens to view the log output of your application, and to view older data use Cloudwatch. A log group is created for every pod in your application, they are named `/eks/{develop|production}/{namespace}/{podname}`, for example `/eks/develop/teqplay-app/portcallinator-dev` for your new and awesome Portcallinator app.

If you want to log multiple separate streams (files), this is possible by applying the sidecar container pattern. This basically spins up a very lightweight extra pod that only contains a `tail -f` on your additional log file. The `skeleton-mongo-app` helm chart supports this out of the box, if you have a separate `/var/log/requests.log` for example, you can add this to your `values.yaml` to expose this log file in both Lens as well as Cloudwatch Logs:

yamllogs:
- name: audit-log
file: /var/log/audit.log
- name: foo-log
file: /var/log/foo.log 

This will create two additional pods called `audit-log` and `foo-log` which are used to stream your new log files.

Note that you *must* do log rotation for this additional log files, because otherwise the disk of your pod *will* fill up!

## Running container images locally

You can run any available image on ECR locally as well, for example if you want to replicate the exact same environment and test something, or if you’d just like to go back in time and try out a previous version.

By using the `docker run` command, you can pull images from ECR and run them.

As container images are isolated by default, we need to specifically tell docker which ports to “bridge” between the container and our host machine. We can specify `--network host` so it will use the network of our host machine, meaning the standard `8080` port it uses (and other ports it might require, like for making a database connection) don’t need to be specified manually and we can access our running app on `localhost:8080` like we are used to.

By using the `-e` argument, we can pass custom environment variables into our container, like secrets, credentials, and/or general config values we’d like to set/overwrite.

At the end we specify what exact image we’d like to run, by combining:

* where our image is hosted = `050356841556.dkr.ecr.eu-west-1.amazonaws.com`
* which repo/project we’d like to run = `csi` (in this example)
* which tag/version we’d like to use = `local` (in this example, can be any other tag that’s available in ECR within the desired project)

docker run --network host -e "AUTH\_CREDENTIALS\_SECRET=secret" 050356841556.dkr.ecr.eu-west-1.amazonaws.com/csi:local

If the image exists locally it will use it directly. Otherwise it will contact ECR to download the requested image.

When you get an authentication error, like:

Unable to find image '050356841556.dkr.ecr.eu-west-1.amazonaws.com/...:...' locally
docker: Error response from daemon: pull access denied for 050356841556.dkr.ecr.eu-west-1.amazonaws.com/..., repository does not exist or may require 'docker login': denied: Your authorization token has expired. Reauthenticate and try again.
See 'docker run --help'.

You first have to login by executing the following AWS and Docker command:

aws ecr get-login-password --region eu-west-1 | docker login --username AWS --password-stdin 050356841556.dkr.ecr.eu-west-1.amazonaws.com

* see AWS docs about this command (<https://docs.aws.amazon.com/AmazonECR/latest/userguide/getting-started-cli.html> )

Now try the `docker run` command again. It will automatically start pulling the image for you.