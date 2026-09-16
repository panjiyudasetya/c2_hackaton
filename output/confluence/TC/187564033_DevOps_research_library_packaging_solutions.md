---
id: confluence:187564033
source: confluence
type: page
space: TC
title: DevOps research library packaging solutions
author: Minh Trang Nguyen (Unlicensed)
date: '2023-06-06'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/187564033
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/187564033
---
# DevOps research library packaging solutions

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/187564033  

## Content

The goal was to do research to find the most effective library packaging solution to be used in the DTAP (Development Testing Accepting and Production) environment.

After shifting solutions the most interesting solutions were studied in more detail and this has resulted in the solutions Apache Archiva, SonaType Nexus3 and AWS CodeArtifact. One interesting solution was JFrog(<http://jfrog.com> ), but it was more focussed on large enterprise customers.

### Apache Archiva

url: <https://archiva.apache.org/>

* This project supports only the Maven2 format.
* Supports releases and snapshots.
* No encryption, the content of files were visible by browsing to the files on disk.
* User management is available.
* Repository files are accessible in the releases and snapshots directory.
* Backups need to be done manually.
* No database needed.
* Open source and free of licenses.
* Helm chart was old and not maintained anymore.
* No vulnerability scanning.
* Must do a lot of setup to get it working by creating a custom Helm chart.

### Sonatype Nexus3

url: <https://www.sonatype.com/products/sonatype-nexus-oss-download>

* Supports multiple packaging formats (Maven2, NPM, Python, Go, Docker, Helm charts and many more which are not used at Teqplay.
* Supports encryption.
* Support for clean up policies.
* Advanced user management.
* Repository files aren’t accessible on file storage.
* No vulnerability scanning included, needs extra licenses.
* To use the cloud version, one needs to pay a license fee. The Cloud (Pro) version cost USD 13 per user with a minimum of 50 users and billed annually. This would be a yearly amount of 7800 USD.
* It’s also possible to use a Helm chart, but that one required a Pro version license.
* To setup in AWS also a license was required (<https://github.com/sonatype/nxrm3-helm-repository/tree/main/nxrm-aws-resiliency>). By using a custom Helm chart it was possible to test the solution, but it missed some features.
* The use of the Sonatype solution is only viable when most of the available features are integrated into the CI/CD environment.

### AWS CodeArtifact

url: <https://eu-west-1.console.aws.amazon.com/codesuite/codeartifact/repositories>

* Supports multiple packaging formats (Maven2, NPM, Python and many more which are not used at Teqplay.
* Encryption.
* No clean up policies, needs to create your own custom clean up script.
* Accessible with existing AWS accounts.
* Repository files aren’t accessible.
* No vulnerability scanning.
* Pricing is 2GB free per month in the free tier, 0.50 USD per 100,000 requests and 0.50 USD per 10 GB storage.
* Not much work to implement into the current development workflow.

### Conclusion

For Teqplay only the Maven2 format is needed. The formats NPM, Docker and Helm charts are using other solutions in the CI/CD environment. It doesn’t add extra value to put all different formats into the same repository. Using AWS CodeArtifact is the easier tool to migrate the existing workflow from S3 buckets to a dedicated Maven repository.

To be able to use the AWS CodeArtifact, one need to do a request to fetch an access token.

Example:

aws codeartifact get-authorization-token \
--domain teqplay --domain-owner 050356841556 \
--region eu-west-1 \
--query authorizationToken --output text

This token can be used as the password in the current Gradle build of Teqplay backend applications. It’s better to keep the existing settings and add extra the settings for the new repository.

Example:

maven {
url 'https://teqplay-050356841556.d.codeartifact.eu-west-1.amazonaws.com/maven/snapshots/'
credentials {
username "aws"
password System.env.CODEARTIFACT\_AUTH\_TOKEN
}
}