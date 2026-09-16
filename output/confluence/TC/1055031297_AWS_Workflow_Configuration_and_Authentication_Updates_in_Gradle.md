---
id: confluence:1055031297
source: confluence
type: page
space: TC
title: AWS Workflow Configuration and Authentication Updates in Gradle
author: Jamie de Leest
date: '2025-12-18'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1055031297
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1055031297
---
# AWS Workflow Configuration and Authentication Updates in Gradle

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1055031297  

## Content

workflow file

this is only applicable if your application uses the backend-standard workflow

for the inputs under `with:`

make sure that `enable_develop` is not set to false  
the default value is true so if it is you can remove it or set it to true

make sure to remove `enable_new_develop`

---

this is applicable for all workflows

in the secrets replace

wide760aws\_access\_key\_id: ${{ secrets.AWS\_ACCESS\_KEY\_ID }}
aws\_secret\_access\_key: ${{ secrets.AWS\_SECRET\_ACCESS\_KEY }}
aws\_access\_key\_id\_develop: ${{ secrets.AWS\_ACCESS\_KEY\_ID\_NEW\_CLUSTER }}
aws\_secret\_access\_key\_develop: ${{ secrets.AWS\_SECRET\_ACCESS\_KEY\_NEW\_CLUSTER }}

with

wide760aws\_account\_id: ${{ secrets.AWS\_ACCOUNT\_ID }}
aws\_account\_id\_dev: ${{ secrets.AWS\_ACCOUNT\_ID\_DEV }}

---

in gradle make sure that you use aws cli for authentication to s3 and not gradle properties

groovy gradle

replace

wide760credentials(AwsCredentials) {
accessKey "$s3\_access\_key"
secretKey "$s3\_secret\_key"
}

with

wide760authentication {
awsIm(AwsImAuthentication)
}

gradle.kt

replace

wide760credentials(AwsCredentials::class) {
accessKey = s3\_access\_key
secretKey = s3\_secret\_key
}

with

wide760authentication {
create<AwsImAuthentication>("awsIm")
}