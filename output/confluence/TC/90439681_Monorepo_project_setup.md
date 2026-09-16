---
id: confluence:90439681
source: confluence
type: page
space: TC
title: Monorepo project setup
author: Former user (Deleted)
date: '2022-03-11'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/90439681
explicit_links: []
---
# Monorepo project setup

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/90439681  

## Content

## Project structure

**General structure**

none.circleci/
└── ...
api/
└── ...
app/
└── app1/
└── app2/
└── ...
lib/
└── lib1/
└── lib2/
└── ...

| **Folder** | **Usage** |
| --- | --- |
| .circleci/ | scripts for CI/CD (CircleCI) |
| api/ | all API models, either as a single API module, or separate subprojects if required  *models are uploaded to S3 repo* |
| app/ | subprojects for all deployable apps  *container images are uploaded to ECR* |
| lib/ | subprojects containing re-usable logic/libs  must not contain independently deployable apps, those should reside in `app/`  private/non-exposed models may reside in a `lib` subproject to be shared with other subprojects, if it needs exposing then it should be moved to `api` |

**Concrete example**

.circleci/
└── config.yml
api/
└── src/
└── build.gradle
app/
└── ais-stream/
└── src
└── build.gradle
└── area-monitor/
└── src
└── build.gradle
└── berth-monitor/
└── src
└── build.gradle
└── ship-change-monitor/
└── src
└── build.gradle
└── ship-history/
└── src
└── build.gradle
└── event-history/
└── src
└── build.gradle
lib/
└── common/
└── src/
└── build.gradle
└── common-monitor/
└── src/
└── build.gradle
build.gradle
settings.gradle

Notably, the root `build.gradle` should contain most (if not all) versioned dependencies, so the specified dependencies in a subproject’s `build.gradle` can import a dependency without a specific version.

If at any point the `app` folder grows too large, we can opt for grouping certain apps together. For example, all monitors can be grouped under `app/monitor/`.

app/
└── ais-stream/
└── src
└── build.gradle
└── ship-history/
└── src
└── build.gradle
└── event-history/
└── src
└── build.gradle
└── monitor/
└── area-monitor/
└── src
└── build.gradle
└── berth-monitor/
└── src
└── build.gradle
└── ship-change-monitor/
└── src
└── build.gradle

## Versioning

SemVer must be used for all different components within the monorepo.

For ongoing development; branches are created, those changes are approved and merged into the `develop` branch. Once features inside `develop` are ready for release, a merge between `master/main` and `develop` should be done, along with a correct SemVer update (for all changed subprojects).

Models and Container images will receive the following tag per branch:

| **Branch** | **Tag** |
| --- | --- |
| master/main | `master-x.y.z` (where `x.y.z` equal to SemVer) |
| develop | `develop-b42` (`develop-b<build_num>`) |
| other branches | `feature-b42` (`<branch_name>-b<build_num>`) |

All container images will be immutable, meaning that no image can be overwritten. This ensures that any version `x.y.z` will always consist of the same underlying source code. Also, as the models and container images use the same tag, you can be sure that those are compatible with each other. This makes things easier when upgrading API models, which might contain breaking changes.

## CI/CD

Upon pushing a commit, all code (for every subproject) will be built, and tests will run.

Container images for develop and other branches can always be uploaded, master/main images can only be uploaded on a new version.

### Next steps

Instead of building and testing all parts of the whole project. Only the changed subprojects could be built and tested, along with only uploading those container images that should be changed.

Some pointers to get that working with CircleCI:

* “simple” path-filtering to trigger only certain subprojects to be built   
  <https://circleci.com/developer/orbs/orb/circleci/path-filtering>   
  <https://circleci.com/docs/2.0/configuration-cookbook/?section=examples-and-guides#execute-specific-workflows-or-steps-based-on-which-files-are-modified>
* path-filtering + config splitting  
  <https://discuss.circleci.com/t/intro-to-dynamic-config-via-setup-workflows/39868>   
  <https://github.com/circle-makotom/circle-advanced-setup-workflow>

An ideal way would be to identify exactly what changed and only build/test/create models & container images for those changes, allowing for a fast and clean process.