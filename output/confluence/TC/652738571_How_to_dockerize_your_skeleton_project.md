---
id: confluence:652738571
source: confluence
type: page
space: TC
title: How to dockerize your skeleton project
author: Richard van Klaveren
date: '2025-03-04'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652738571
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652738571
---
# How to dockerize your skeleton project

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652738571  

## Content

This guide will describe how you can modify your skeleton project to use Docker containers for deployment.

## Preparing your system

Ensure that you have installed Docker, including the CLI, on your system, and that your user account is in the `docker` group. Otherwise you won't be able to interact with Docker on your system. On a Ubuntu/Debian system, `sudo aptitude install docker-ce` should do the trick. To add your user to the `docker` group, use `sudo usermod -a -G docker username`.

To be able to access the Amazon ECR (Elastic Container Registry), it is super helpful to install the [ECR credential helper](https://github.com/awslabs/amazon-ecr-credential-helper). The linked page should have everything you need.

## Preparing your project

By far the easiest way to build a Docker image out of your Spring Boot project is to use the integrated support for this. Unfortunately, this is only available as of Spring 2.3.0.M1, which is a newer version than what is currently used in the skeleton project. I went straight to version 2.4.0, which comes with some additional challenges:

* A too-new version of the Mongo Java driver dependency
* Spring Validation is no longer included in the dependencies

To make it all work despite of this, change your `build.gradle` in the following way:

* In the `buildscript.ext` block, up `spring_boot_version` to `2.4.0`
* In the `buildscript` block, add `ext['mongodb.version'] = ext.mongodb_version`. Skeleton unfortunately uses a property called `mongodb_version` to set the MongoDB dependency versions, whereas the Spring BOM uses `mongodb.version`. This trick aligns the two.
* To your `dependencies` block, add the following two lines:

  implementation "javax.validation:validation-api:2.0.1.Final"
  implementation "org.hibernate.validator:hibernate-validator:6.1.6.Final"

  This makes `ValidationConfiguration` in `skeleton-common` work (this dependency is no longer part of `spring-boot-starter-web`)
* Finally, add a block to set the name of the Docker image you're going to build:

  bootBuildImage {
  imageName = "teqplay/project-name"
  }

Also, your project might need to use a more recent version of Gradle. To upgrade your Gradle wrapper, do a `./gradlew wrapper --gradle-version 6.7.1`.

## Building an image, and testing it

Now things are going to be pretty simple. First, build your image:

./gradlew bootBuildImage

Use `docker image ls` to verify that your image was indeed built. Then, you can run your image locally, as follows:

docker run -p 8080:8080 teqplay/project-name

This will bind your local port 8080 to port 8080 on the Docker container. If your local port 8080 is already in use, feel free to use a different port. Use CTRL-C to stop the container.

To allow you to set environment variables controlling the various settings of your application, the easiest option is to use an env file. Create a file called, for example, `project-name-local.env` with each environment variable assignment on a single line, for example:

MONGODB\_HOST=dbpronto-dev.teqplay
MONGODB\_USERNAME=henk
MONGODB\_PASSWORD=secret-squirrel

Then, start your image as follows:

docker run -p 8080:8080 --env-file project-name-local.env teqplay/project-name

## Upload your image to Amazon ECR

To upload your image to ECR, you first need to create a repository for it. Each project needs a separate repository for the various image versions you want to store. Go to the [ECR website](https://eu-west-1.console.aws.amazon.com/ecr/repositories?region=eu-west-1#), and use the 'Create repository' button to create a new repository. I opted to prefix them with `develop` to separate develop and production builds, but that could maybe just as well be achieved by proper use of version tags.

After you created the repository, make note of the URI (of the form `050356841556.dkr.ecr.eu-west-1.amazonaws.com/develop/project-name`) and use it to tag your new image locally, and then push it to ECR:

docker image tag 050356841556.dkr.ecr.eu-west-1.amazonaws.com/develop/project-name teqplay/project-name:latest
docker push 050356841556.dkr.ecr.eu-west-1.amazonaws.com/develop/project-name

## Fire up a container in Amazon ECS

To prepare the container definition, create a .env file with the settings you want to use, and upload this to an S3 bucket, for example [this one](https://s3.console.aws.amazon.com/s3/buckets/docker-env.teqplay.nl?region=eu-west-1&tab=objects).

Go to the [ECS website](https://eu-west-1.console.aws.amazon.com/ecs/home) and create a new Task Definition. For now, you want to select FARGATE launch type (this is required by the type of cluster we use currently). In the next page, give the task a suitable name, allocate memory and vCPU, and add a container definition using your image. In the container definition, ensure that you add port 8080 to the port mappings (there's no way to remap ports). Also add the environment file you uploaded, by copy-pasting the S3 ARN into a new item under "Environment Files". Then create the new task definition.

Next, go to the cluster, and create a new Service. Select the FARGATE launch definition, your new task definition, and set the platform version to the latest version (1.4.0), *not* to be confused with the option LATEST, which ... does not work. Set the number of tasks to 1, and go to the next step. Here, select the Teqplay VPC (172.31.0.0/16) and add *all three* subnets. Edit the newly created security group and open up port 8080 to accept traffic from `172.31.0.0/16`.

Under Load Balancing, select "Application Load Balancer", and select "docker-develop". The "Container to load balance" should be the only container you have added. Note that you *do* still have to click "Add to load balancer". Select 443 as the listener port, and https as protocol. Add an evaluation order to the path pattern (this is needed, but will be changed later). Give the target group a reasonable name, and set the health check pattern to `/v1/version`.

The rest of the settings can be left at their defaults, and now you can create the service.

Next, we have to fix the Elastic Load Balancer settings, via the [Load Balancers](https://eu-west-1.console.aws.amazon.com/ec2/home?region=eu-west-1#LoadBalancers:sort=loadBalancerName) section of the EC2 console. Open the "Listeners" tab, and click the "View/edit rules" link of the HTTPS listener. Click the little pencil in the top row, then click the pencil of the row corresponding to your new target group. Delete the "Path is ..." condition, add a "Host header" condition, and enter the host name that you want to use for your new service, for example `backendproject-name.teqplay.nl`.

Lastly, we need to fix the Target Group settings, via the [Target Groups](https://eu-west-1.console.aws.amazon.com/ec2/home?region=eu-west-1#TargetGroups:) page. Open your new target group, click "Edit" on the "Health check settings" panel, open the "Advanced health check settings" page, and set the "Success codes" to `401`.

This is the final step, and your new container should now be reachable! The default settings include logging to CloudWatch, and you can also find useful diagnostic information in the "Events" tab of the ECS Service you have created.