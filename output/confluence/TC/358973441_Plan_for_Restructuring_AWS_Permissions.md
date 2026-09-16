---
id: confluence:358973441
source: confluence
type: page
space: TC
title: Plan for Restructuring AWS Permissions
author: Minh Trang Nguyen (Unlicensed)
date: '2024-09-19'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/358973441
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/358973441
---
# Plan for Restructuring AWS Permissions

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/358973441  

## Content

status: concept

# Summary

**Advantages of AWS Organization Units (OUs):**

1. **Centralized Management**:

   * Manage multiple AWS accounts from a single central location.
   * Easily apply policies to multiple accounts simultaneously.
2. **Cost Management**:

   * Detailed insight into costs and usage per account.
   * Ability to set budgets and cost limits.
3. **Security and Compliance**:

   * Apply consistent security and compliance settings.
   * Use Service Control Policies (SCPs) to centralize access management.
4. **Scalability**:

   * Easily add and manage new accounts.
   * Flexibility to group accounts based on organizational structure or project needs.
5. **Delegated Administration**:

   * Delegate specific administrative tasks to different teams without giving full access.

**Disadvantages of AWS Organization Units:**

1. **Complexity**:

   * Managing multiple accounts can be complex, especially in large organizations.
   * Requires a good understanding of AWS security and access management.
2. **Costs**:

   * Potential additional costs for using certain AWS services within multiple accounts.
   * Managing multiple accounts can lead to higher operational costs.
3. **Limitations of SCPs**:

   * SCPs can be complex to configure and manage correctly.
   * Incorrect configuration of SCPs can lead to unintended access restrictions.
4. **Initial Setup Time**:

   * The initial configuration of an AWS organization can be time-consuming.
   * Requires planning and careful implementation to be effective.
5. **Training and Knowledge**:

   * Requires training and knowledge of AWS organization management for effective use.
   * Additional training may be needed for team members to become familiar with the tools and processes.
6. **Migration Can Cause Errors**:

   * Time-consuming and requires good planning.
   * Migration scripts needed to move applications and services.

# Current situation

As per AWS and other authoritative guidelines, it's highly recommended to limit the use of the AWS ROOT account. This account should primarily be utilized for establishing organizational structures and administrator accounts, which aids in structuring the company's infrastructure.

The current setup and organization are functional for the team, but there's room for enhancement to bolster its robustness.

At present, all users and infrastructure are unified within a single account, lacking a clear distinction between DEVELOPMENT and PRODUCTION environments. The following images provide a visual representation of the organization of all elements within this unified account.

This method presents both advantages and disadvantages, which are summarized below.

**Advantages**

Simplicity

Managing all resources within a single account can be simpler as you don't have to switch between accounts for different environments. This can make it easier to oversee all resources and operations.

Cost tracking

It can be easier to track costs as all charges are on a single bill. This can simplify accounting and cost analysis.

Resource Sharing

Resources like Elastic Block Store (EBS) snapshots, and Relational Database Service (RDS) snapshots can be easily shared between environments without the need for cross-account permissions.

**Disadvantages**

Security

Separating environments into different accounts can limit the blast radius if one environment is compromised. For example, if your DEVELOP environment is compromised, your PRODUCTION resources are still safe in a separate account.

Resource Isolation

Each account has its own resources, limits, and settings, which can prevent development activities from impacting production.

Granular Access Control

Utilizing separate accounts enables a more detailed control over resource access. As per AWS recommendations, this can be particularly beneficial in larger organizations where distinct teams or individuals manage different environments. However, it's also a prudent practice for smaller teams to adopt, as a single error can significantly impact a smaller company.

Billing Separation

While having a single bill can be simpler, having separate bills for each environment can make it easier to track costs associated with each environment. This can be useful for cost attribution and budgeting.

# Proposed solution enhancement

The existing setup is functional, yet it does not meet enterprise-grade security standards. This proposal aims to highlight critical aspects that need to be addressed to enhance the security, along with the management of users, roles, and permissions. This solution is focused on identifying the best possible approach for the organization, without taking into account the cost or time implications of migration.

The first step is to map out how to incorporate administrators into this proposed solution by defining what are administrators.

## Administrators

Administrators are individuals responsible for managing and maintaining the cloud resources. Their responsibilities typically include:

* Setting up and configuring AWS services according to best practices.
* Monitoring and managing AWS resources to ensure optimal performance, security, and cost-efficiency.
* Troubleshooting any issues that arise within the AWS environment.
* Implementing and managing security measures, including access controls and firewalls.
* Keeping up-to-date with AWS updates and new features, and implementing them as necessary.

In the revamped configuration, administrators won't be categorized under Identity and Access Management (IAM) users; instead, they'll be positioned outside the IAM segment. To utilize this feature, activation of the IAM Identity Center is required. Please note, only users with root or admin account privileges have the authority to enable the IAM Identity Center feature.

## Enable IAM Identity Center

The IAM Identity Center must be established in EU-West-1, which serves as the availability zone for all company resources. While it's possible to switch to a different zone, be aware that doing so will result in the **removal** of all accounts created within the IAM Identity Center.

Navigate to the IAM Identity Center and follow the guidelines provided on the webpage.

First, activate this service, then proceed to enable it.

In the IAM Identity Center setup there are four steps to follow.

1. Confirm your identity source
2. Manage Permissions for Multiple AWS accounts
3. Set up application user and Group assignments
4. Configure multi-factor authentication (MFA)
5. Register a delegated administrator

### Confirm your identity source

In this initial phase, our focus will be on managing all users via the Identity Center. While "Active Directory" and "External Identity Provider" are available options, they are not applicable to the company's current needs.

Additionally, modify the access portal URL to **"**[**https://teqplay.awsapps.com/start**](https://teqplay.awsapps.com/start)" to enhance its readability.

### Manage Permissions for Multiple AWS accounts

In this phase, our task is to incorporate the necessary permission sets for user roles within the IAM Identity Center. While AWS provides a set of predefined permissions, there's also the flexibility to craft custom permissions tailored to specific needs, but we don’t need them at this moment.

The company needs at least two groups, these are:

1. Administrators
2. Techsupport

#### Administrators

This group has been previously outlined in the preceding section. For this group select the permission set “AdministratorAccess”.

#### Techsupport

The company maintains a dedicated team that provides round-the-clock support to its clientele, distinguishing it as a unique group. Typically, this group is established within the IAM module. However, when segregating DEVELOP and PRODUCTION environments, it becomes necessary for users within this group to hold accounts across these two distinct environments. It's important to note that AWS does not facilitate the use of a single account across two different Organizational Units (OU). For this fundamental reason, it is more advantageous to establish the accounts of “Techsupport” users within the IAM Identity Center.

For this particular group, opt for the "PowerUserAccess" permission set. This set grants comprehensive access to all AWS services and resources, with the exception of IAM.

### Set up application user and Group assignments

This step is applicable only when incorporating applications that intend to utilize the Single Sign-On feature of AWS. Currently, Keycloak is used to authenticate users across various applications within the company. This step is not needed.

### Configure multi-factor authentication (MFA)

Enforce multi-factor authentication for all users by selecting the options depicted in the image below.

### Register a delegated administrator

In this step, you will establish an account that possesses administrative access to the IAM Identity Center. This differs from typical administrator users as it is exclusively applicable to other root users within the Organizational Units (OU's). However, this step is not mandatory.

## AWS Organizations

AWS Organizations is a service that allows you to manage multiple AWS accounts centrally. With AWS Organizations, you can create Organizational Units (OUs) to group accounts with similar needs, and apply policies to them for consistent control across accounts, without manual setup.

This is an optimal method for segregating resources for DEVELOP and PRODUCTION environments. The subsequent diagram illustrates the intended configuration. In this suggested approach, we utilize the fewest possible Organizational Units (OU's) to effectively differentiate between the various environments. In the future, adding additional Organizational Units such as "Finance" and "Audits" could be created with ease.

The diagram illustrates a root node, to which the root user is connected. This root user also serves as the management account. However, it's important to note that this account should not be utilized for managing AWS resources. Instead, it should be safeguarded with secure credentials and Multi-Factor Authentication (MFA) enabled. The usage of this account should be minimal.

The root account branches out to a node labeled "Teqplay", representing the company. Underneath "Teqplay", there are child nodes representing different departments. In this instance, only the "Software Development" department is depicted, but additional departments, such as "Finance", can be added in the future.

From the "Software Development" node, two separate Organizational Units (OUs) are branched out, namely "Develop" and "Production". Under these nodes, AWS accounts are added. While these accounts do not require login credentials, it is possible to log in using them. To retrieve the login credentials for these accounts, navigate to the root user's login page and select the "Forgot password" option to initiate a password reset. This process grants the AWS account access to the AWS Console. Usually these accounts have the pay method assigned to them.

We have established four groups: "admin-develop", “admin-production”, “techsupport-develop” and "techsupport-production". These groups are assigned to the users "develop@teqplay" and "production@teqplay" respectively. Any users added to either the "administrators" or "techsupport" groups will gain access to the "DEVELOP" or "PRODUCTION" OUs. The following list identifies the users designated for inclusion in either the "administrators" or "techsupport" groups. The directory of additional groups can be located in the subsequent sections of this document.

**The drawbacks of this configuration, when compared to the existing setup, include:**

The personal access tokens for users are not everlasting, unlike in the current situation. These tokens have a lifespan that does not exceed the session duration set for "administrators" or "techsupport" users.

To obtain the access tokens, please use the portal. Refer to the example provided below.

**Statement**

The question is whether administrators require continuous access keys for AWS resources. It also asks about the tasks that users are unable to perform within the AWS console.

One significant benefit of using these keys is their compatibility with Multi-Factor Authentication (MFA) when pushing Docker images to the Elastic Container Registry (ECR). Unlike the current situation where MFA-enabled users encounter difficulties, these keys ensure successful Docker image pushes to ECR, even with MFA enabled.

## Inactive users and access keys

The present circumstances necessitate the cleanup of inactive users and access keys. This task should be integrated into the offboarding process for users. Refer to the attached image for a list of users who are inactive, yet possess active access keys.

## Reducing IAM User Access Keys, Increasing IAM Role Usage

As of the current update, the company employs long-term credentials associated with IAM users for authentication with AWS services such as S3, EKS, among others. The objective is to minimize the use of Access Keys by leveraging the AWS Security Token Service (AWS STS).

The objective is to implement a robust authentication mechanism for all job operations within the company, such as uploading files to S3, deploying a Helm chart in an EKS cluster, or creating snapshots.

We have established trust relationships with various identity providers, including Keycloak, CircleCI, GitHub, and potentially others, within AWS. Essentially, we have informed AWS that these identity providers are trustworthy.

When a job initiates, it requests a token from one of the identity providers, depending on the specific use case. The identity provider responds with a signed JWT token containing all the necessary information for AWS STS to verify the identity.

This token, along with the assumed role, is then sent to AWS STS. An IAM Role, for instance, could be S3, which only has permissions to upload a file to S3. AWS executes the job, and the outcome, such as the successful upload of a file, becomes visible.

This approach enhances security as the token, depending on the AWS configuration, is only valid for a limited duration, typically one hour. This transient nature of the token reduces the risk of unauthorized access or misuse.

### Migrating IAM users to IAM roles

Certain IAM users have been pinpointed who could potentially transition to utilizing IAM roles.

|  |
| --- |
| airflow-workers |
| aisdata-log-upload |
| app-event-history-processor-dev |
| app-revents-engine |
| app-revents-engine-api |
| app-ship-history-dev |
| app-ship-history-migrator |
| app-ship-history-processor |
| app-ship-history-processor-dev |
| bitbucket-pipelines |
| bunkerplanner-data |
| bunkerplanner-eb-deploy |
| bunkerplannerdev-data |
| cargooptimadev-data |
| chartmuseum |
| circle-ci |
| circle-ci-students |
| datascience-s3-datastore |
| datascience-s3-datastore-dev |
| demo.student |
| demostuds |
| eks-dns-user |
| event-history |
| event-history-migrator |
| event-history-processor |
| fuelboss-data |
| fuelbossdev-data |
| github-ci |
| gitlab-ci |
| isps-data |
| isps-data-dev |
| keycloakthemes-user |
| mturk |
| platform-integration-tests |
| portreporter |
| portreporterdev |
| portreporterstaging |
| pto-s3 |
| repo-user |
| teqplay |
| thanos |
| velero |
| vesselcompliance-data |
| vesselcompliancedev-data |

Here are some resources for configuring this setup with CircleCI and GitHub Actions.

* <https://circleci.com/blog/openid-connect-identity-tokens/>
* <https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services>
* <https://kubedemy.io/aws-eks-part-13-setup-iam-roles-for-service-accounts-irsa>
* <https://github.com/seifrajhi/aws-eks-irsa>

## IAM user groups

The table below illustrates the existing configuration of groups.

|  |  |
| --- | --- |
| administrators | The members of this group possess unrestricted access to all AWS resources, including billing features. |
| ci-deployments | This group, currently responsible for deployments to EKS clusters, possesses comprehensive access to ElasticBeanstalk, CloudFront, EC2, and EKS. However, it is recommended to eliminate this group and utilize IAM Roles for these tasks instead. |
| ci-deployments-students | This group is exclusively granted access to ElasticBeanstalk and could potentially be eliminated. |
| developers | The members of this group are granted extensive permissions to EC2, MechanicalTurk, SageMaker, Lambda, EKS, IAM, and PowerUserAccess. However, it appears that such a wide range of permissions may not be necessary for the developers. |
| developers-without-cluster-access | This group possesses the same permissions as the developers' group, with the exception of access to the EKS clusters. |
| devops | This group is granted unrestricted access to ECR, EC2, and IAM. |
| frontend-developers | This group is endowed with unrestricted access to Mechanical Turk, in addition to possessing PowerUserAccess. |
| marketing | This group is granted limited access to S3 buckets. |
| platform-integration-tests | This has full access to S3. |
| students | This group has limited access to EKS, S3 and ECR. |
| textract-developper | This group is granted unrestricted access to Textract, Simple Notification Service, and Simple Queue Service. |
| user | This group is designed to mandate users to activate Multi-Factor Authentication (MFA). |

Administrators can be relocated from the group to the IAM Identity Center. This means that all users in the administration group must be re-invited and their accounts reconfigured.

The `ci-deployments` and `ci-deployments-students` must be transitioned to IAM roles, as outlined in the preceding section.

The `developers` group is currently defined too broadly, providing insufficient clarity on its function. Permissions should be organized based on specific requirements. In the forthcoming section, we will propose a solution that identifies and discusses various distinct groups.

The `devops` group should be granted access to various AWS services, including EC2, ECR, IAM, Route53, S3, Lambda, EKS, CodeArtifact, CloudWatch, and Certificate Manager. The services that the DevOps group may require access to in the future also factor into this consideration. Upon examining the required permissions for the DevOps group, it appears that they closely align with those of the TechSupport group..

The `frontend-developers` group should be restricted to accessing only S3 and CloudFront services.

The `platform-integration-tests` group possesses an access key intended for integration testing. While utilizing an IAM role is the preferred method if feasible, it's worth noting that the access key has remained unused for over 1600 days. Maybe this group can be removed.

The groups `marketing`, `students`, and `textract-developer` (corrected from `textract-developper`) are organized based on the type of service, which makes them appropriately categorized.

The user group should not be present as its functionalities need to be enabled at a global level.

### Proposed grouping users

All users should be transitioned to the IAM Identity Center, as AWS advises the use of IAM exclusively for particular scenarios.

**AWS advice**

“We recommend that you create IAM users only if you need to enable programmatic access through access keys, service-specific credentials for AWS CodeCommit or Amazon Keyspaces, or a backup credential for emergency account access.”

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **PermissionSets** | **Develop (OU) environment** | **Production (OU) environment** |
| administrators-develop | AdministratorAccess | x |  |
| administrators-production | AdministratorAccess |  | x |
| techsupport-develop | PowerUserAccess | x |  |
| techsupport-production | PowerUserAccess |  | x |
| backend-devs-develop | BackendDevsPermissionSet | x |  |
| backend-devs-production | BackendDevsPermissionSet |  | x |
| billing-develop | BillingAccess | x |  |
| billing-production | BillingAccess |  | x |
| storage-develop | StorageAccess | x |  |
| storage-production | StorageAccess |  | x |
| networking-develop | NetworkAdministrator | x |  |
| networking-production | NetworkAdministrator |  | x |
| frontend-develop | FrontendAccess | x |  |
| frontend-production | FrontendAccess |  | x |
| students-develop | StudentsAccess | x |  |
| students-production | StudentsAccess |  | x |
| textract-develop | TextractDeveloperAccess | x |  |
| textract-production | TextractDeveloperAccess |  | x |

To facilitate the segregation of groups across different environments, we will append suffixes such as `develop` and `production` to the group names. This approach significantly reduces the likelihood of users gaining access to both development and production environments simultaneously.

**administrators**

This group possesses access to all AWS resources, a privilege that should be exclusively granted to a specific, dedicated group.

**techsupport**

This group is powerful and requires access to all resources, with the exception of managing IAM users. They are capable of managing users within the IAM Identity Center. The DevOps group should utilize this group for the execution and management of DevOps-related tasks.

**backend-devs**

This group is designed for backend developers requiring access to S3, CodeArtifact, Elastic Container Registry, CloudWatch, Lambda and EC2.

**billing**

This group has limited access to billing information.

**storage**

The users within this group have access to both database and S3 services.

**networking**

The users within this group are granted access to all network-related AWS services, including but not limited to VPC, Route53, and CloudWatch.

The groups mentioned above are managed by AWS and adhere to AWS's standard permissions. Conversely, the groups listed below possess custom permissions.

**frontend**

This group is granted exclusive access to the S3 and CloudFront services, as per the tailored permissions.

**students**

This group should be granted the minimum necessary permissions. For now, we can utilize the permissions that have already been established.

**textract**

This group has permissions to the services Textract, Simple Notification Service and Simple Queue Service.

### Current Kubernetes cluster DEVELOP and PRODUCTION

The existing clusters, DEVELOP and PRODUCTION, reside within the root account, leading to distinct group names for each. Due to their placement in the same root account, segregation between them is unfeasible. Here are the group names associated with the root account:

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **PermissionSets** | **Develop ROOT environment** | **Production ROOT environment** |
| v1-administrators | AdministratorAccess | x | x |
| v1-techsupport | PowerUserAccess | x | x |
| v1-backend-devs | BackendDevsPermissionSet | x | x |
| v1-billing | BillingAccess | x | x |
| v1-storage | StorageAccess | x | x |
| v1-networking | NetworkAdministrator | x | x |
| v1-frontend | FrontendAccess | x | x |
| v1-students | StudentsAccess | x | x |
| v1-textract | TextractDeveloperAccess | x | x |

### PermissionSets

| **PermissionSets** | **AWS Magaged** | **Custom** | **Comment** |
| --- | --- | --- | --- |
| AdministratorAccess | x |  | Full access |
| PowerUserAccess | x |  | Full access minus IAM |
| BackendDevsPermissionSet |  | x | EC2, S3, Lambda, CodeArtifact |
| BillingAccess | x |  | Billing only |
| StorageAccess |  | x | S3, RDS |
| NetworkAdministrator | x |  | VPC |
| FrontendAccess |  | x | S3, CloudFront |
| StudentsAccess |  | x | beanstalk\_students, repo.teqplay.nl\_readonly, s3\_students, tnt\_s3\_students |
| TextractDeveloperAccess |  | x | AmazonSNSFullAccess, AmazonSQSFullAccess, AmazonTextractFullAccess |

## Kubernetes cluster access

Currently, user access is configured through the ConfigMap, which hardcodes the list of users allowed to access the cluster. A better practice is to use IAM access entries. This approach defines groups with specific permissions for cluster access. By applying the AmazonEKSAdminPolicy and AmazonEKSClusterAdminPolicy, it is unnecessary to explicitly define users with full access to the cluster. See the picture below where to configure this. The permissions granted may still be overly broad for specific tasks, such as deployments to the EKS cluster.

### aws-auth configmap

The current configuration specifies individual users in the configmap for EKS cluster access. However, AWS has deprecated this approach, and future Kubernetes versions will no longer support it.

### CI/CD deployments

Helm chart deployments, executed through GitHub Actions or CircleCI, can leverage the IAM Role and Assume Role for interfacing with the EKS cluster API. It's crucial to include the IAM role in the IAM access entries; otherwise, the CI/CD pipeline will be unable to access the cluster.

#### Github Actions example

Below is an example for creating an IAM role for Github Actions.

The following represents the most straightforward example of establishing communication with the cluster.

steps:
- uses: actions/checkout@v4
- name: configure aws credentials
uses: aws-actions/configure-aws-credentials@v4
with:
role-to-assume: <ARN IAM ROLE>
role-session-name: test-session
aws-region: ${{ env.AWS\_REGION }}
- name: install kubectl
run: |
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x kubectl
sudo mv ./kubectl /usr/local/bin/kubectl
- name: Set KUBECONFIG
run: echo "KUBECONFIG=$GITHUB\_WORKSPACE/.kube/config" >> $GITHUB\_ENV
- name: Configure kubectl
run: |
aws eks update-kubeconfig --region eu-west-1 --name production --alias aws-production
kubectl config set-credentials aws-user --exec-api-version=client.authentication.k8s.io/v1beta1 \
--exec-command=aws --exec-arg=eks --exec-arg=get-token --exec-arg=--region --exec-arg=${{ env.AWS\_REGION }} \
--exec-arg=--cluster-name --exec-arg=production
kubectl config set-context --current --user=aws-user
- name: List namespaces
run: kubectl get namespaces

#### Circle-Ci example

The process of creating the IAM role closely mirrors that of the GitHub action, with the primary distinction being a different Identity Provider.

See <https://circleci.com/blog/openid-connect-identity-tokens/> and <https://circleci.com/docs/openid-connect-tokens/> how to set this up.

Additional steps are required in CircleCI to achieve the same outcome.

version: 2.1
orbs:
aws-cli: circleci/aws-cli@3.1.5
jobs:
aws-example:
environment:
AWS\_REGION: us-west-1
docker:
- image: cimg/aws:2022.06
steps:
- checkout
# run the aws-cli/setup command from the orb
- aws-cli/setup:
role-arn: "arn:aws:iam::123456789012:role/OIDC-ROLE"
aws-region: AWS\_REGION
# optional parameters
profile-name: "OIDC-PROFILE"
role-session-name: "example-session"
session-duration: "1800"
- run:
name: Log-into-AWS-ECR
command: |
# must use same profile specified in the step above
aws ecr get-login-password --profile "OIDC-PROFILE"
workflows:
OIDC-with-AWS:
jobs:
- aws-example:
context: aws

## On- and offboarding new users

AWS should serve as the authoritative source for user accounts, necessitating the establishment of a connection with both Keycloak Development and Production. This approach eliminates the need for duplicate account management. The synchronization process can be effectively implemented using Lambda and the API Gateway.

When a user requires offboarding, it should be executed through the AWS Identity Center, with the synchronization process mirroring that of the onboarding procedure.

### Mapping table AWS groups and Keycloak groups

|  |  |  |
| --- | --- | --- |
| **AWS group** | **Keycloak Develop** | **Keycloak Production** |
| administrators-develop | devops |  |
| administrators-production |  | devops |
| techsupport-develop | techsupport |  |
| techsupport-production |  | techsupport |
|  |  |  |

## Development Process

The development team is presently utilizing Amazon S3 as a storage solution for private Maven dependencies, which are subsequently imported into various projects. Here's an illustrative example of this process:

repositories {
mavenCentral()
maven { url 'https://jitpack.io' }
maven {
url "$teqplay\_repo\_url/release"
credentials(AwsCredentials) {
accessKey "$s3\_access\_key"
secretKey "$s3\_secret\_key"
}
}
maven {
url "$teqplay\_repo\_url/snapshot"
credentials(AwsCredentials) {
accessKey "$s3\_access\_key"
secretKey "$s3\_secret\_key"
}
}
}

While the current process of importing private dependencies may not be the recommended approach, alternative solutions such as AWS CodeArtifact offer a more secure method. Specifically, AWS CodeArtifact utilizes tokens via the Security Token Service (STS), enhancing the safety of the process. Below is an illustration of how to retrieve an authorization token:

aws codeartifact get-authorization-token --domain example-login-app --domain-owner <AWS account> --region eu-west-1 --query authorizationToken --output text

Adopting AWS CodeArtifact necessitates modifications to the existing build process for importing dependencies, as well as alterations to the current policy framework. The policy should resemble the following example. However, permissions ought to be explicitly defined:

{
"Version": "2012-10-17",
"Statement": [
{
"Action": [
"codeartifact:\*"
],
"Effect": "Allow",
"Resource": "\*"
},
{
"Effect": "Allow",
"Action": "sts:GetServiceBearerToken",
"Resource": "\*",
"Condition": {
"StringEquals": {
"sts:AWSServiceName": "codeartifact.amazonaws.com"
}
}
}
]
}

Given the existing implementation of Maven packages on S3, it is advisable to continue utilizing AWS access tokens. However, upon transitioning to CodeArtifact, these tokens can be safely discarded.

## Impact new proposition

The segregation of Development and Production environments significantly influences the company's infrastructure. The existing environment is not transferable to these newly isolated environments, necessitating the formulation of a migration strategy for both Development and Production.

Consideration should be given to establishing a connection between the existing VPC and the new DEVELOP and PRODUCTION VPCs, with the transfer being facilitated through migration scripts. While this solution is beyond the scope of the current plan, it's important to note that it constitutes a significant operation.