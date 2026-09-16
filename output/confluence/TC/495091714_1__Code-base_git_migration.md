---
id: confluence:495091714
source: confluence
type: page
space: TC
title: 1. Code-base git migration
author: Damon Asberg
date: '2025-02-24'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/495091714
explicit_links:
- jira:DEV-552
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/495091714
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/495091714/1.+Code-base+git+migration#Large-files-in-the-repository
---
# 1. Code-base git migration

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/495091714  

## Content

# Introduction and aims

none

This page attempts illustrate the steps and relevant remarks for migrating the codebase of any project, whether front-end or backend.

In contrast, this document **is NOT aimed to describe ALL** possibilities and scenarios, **but to focus on our own needs** and context.

# Overview

The steps of the code migration will be:

1. Migrate code-base
2. Migrate pull requests

# Preparations

Before any race, we must know where do we hit the road, the check points and the finish line!  
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

| **Resource** | **Value** | **Comments** |
| --- | --- | --- |
| Bitbucket **repository url** | `fill this gap` | e.g. `https://bitbucket.org/teqplay/cargooptima-backend/`. |
| GitHub **repository url** | `fill this gap` | e.g. `https://github.com/teqplay/cargooptima-backend/`. |
| Bitbucket and Github **organization** | `teqplay` | Both are always `teqplay`. |
| Bitbucket and Github **repo name** | `fill this gap` | e.g. `cargooptima-backend` (  They must be the same). |
| Bitbucket **repository** token | `fill this gap` | [Go here to see the](https://bitbucket.org/teqplay/cargooptima-backend/admin/access-tokens) `cargooptima-backend` [**example**](https://bitbucket.org/teqplay/cargooptima-backend/admin/access-tokens). |
| GitHub **classic** PAT | `fill this gap` | [Go here to create one](https://github.com/settings/tokens). |
| Public SSH key in Bitbucket | `fill this gap` | [Set it here in Bitbucket](https://bitbucket.org/account/settings/ssh-keys/). |
| Public SSH key used in GitHub | `fill this gap` | [Set it here in GitHub](https://github.com/settings/keys). |

# Repository migration

According to the document [*Planning your migration to GitHub*](https://docs.github.com/en/migrations/overview/planning-your-migration-to-github) and given our migration origin (Bitbucket), we shall take the [*Bitbucket Cloud (Bitbucket.org) to GitHub.com*](https://docs.github.com/en/migrations/overview/migration-paths-to-github#bitbucket-cloud-bitbucketorg-to-githubcom) migration path.

Among the options we have, the most suitable to us (technically skillful) would be a [**bare migration**](https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/importing-an-external-git-repository-using-the-command-line)**.**  
It is quick, low in complexity and it includes the commits and existing branches – pull-requests, commit comments and other git-provider specifics can only be migrated if migrating from Bitbucket server on premise.

## Bare migration (command-line)

### Prerequisites

You will need:

* Reading access rights to Bitbucket repository.
* Writing access rights to GitHub repository/organization.

It’s highly recommended satisfy them with SSH keys (which you probably already use for Bitbucket):

1. Use or create a SSH key and set it locally – specially your private one – in the right folder `~/.ssh`.

   ssh-keygen -t rsa -b 2048 -f myKey
2. Set your [public SSH key in Bitbucket](https://bitbucket.org/account/settings/ssh-keys/) (if not already)
3. Set your [public SSH key in GitHub](https://github.com/settings/keys) (if not already)

### Steps

We will use CargoOptima as an example to follow instructions from [here in GitHub (importing an external Git repo...)](https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/importing-an-external-git-repository-using-the-command-line):

1. If possible, **coordinate with the development team so no commits are pushed during the migration** on the repository to migrate.  
   You can, as a safety measure, block any commits in Bitbucket, just in case! ([portlocaltime-backend example here](https://bitbucket.org/teqplay/portlocaltime-backend/admin/branch-restrictions)).

|  |
| --- |
|  |
| Blocking commits in Bitbucket |

2. Create a [new repository in GitHub](https://github.com/organizations/teqplay/repositories/new).

|  |
| --- |
|  |
| Creation of repository in GitHub. |

If your repository contains files [larger than 100MB](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github#file-size-limits) AND git LFS was enabled in the Bitbucket repository, you need to enable the Git LFS option in Github (**see image below**).

|  |
| --- |
|  |
| Repository Settings / Archives |

**However**, if the Bitbucket repository didn’t have git LFS enabled **before** and already had files > 100MB, the migration will be impaired. See Troubleshooting section [Large files in the repository](https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/495091714/1.+Code-base+git+migration#Large-files-in-the-repository).

3. Locally, bare-clone the Bitbucket repository:

   git clone --bare git@bitbucket.org:teqplay/[REPO-NAME].git [REPO-NAME]-bare
4. Change your current directory (in the terminal) and push with the option `mirror`:

   cd [REPO-NAME]-bare
   git push --mirror git@github.com:teqplay/[REPO-NAME].git
5. Remove the local bare repository, as it’s no use for it anymore.

   cd ..
   rm -rf [REPO-NAME]-bare

If no issues found, your repository, including branches and commits shall been in happily hosted in GitHub.

|  |
| --- |
|  |
| Repository migrated |

You’d be ready to clone it from GitHub and work!

## Troubleshooting

### Large files in the repository

We face a medium-size problem, discovered when migrating [routescout](https://github.com/teqplay/routescout-backend) (see [DEV-552](https://teqplaybv.atlassian.net/browse/DEV-552)).

The Bitbucket repository had files larger than the GitHub maximum file size, 100Mb. So, it will refuse to push these files. See [https://docs.github.com/...about-large-files-on-github#file-size-limits](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github#file-size-limits).

We will follow an approach based on [BFG repo cleaner](https://rtyley.github.io/bfg-repo-cleaner/).

##### Important remarks:

* It is highly likely that some large files will be lost (Github has a strong restriction on that).
* The solution goes through removing the large files from the git history, meaning that it’ll rewrite the commit history. New commits will be written that won’t match the ones in bitbucket.

##### Steps

The recommended approach to follow is:

1. Mirror-clone the repository:

   git clone --mirror git@bitbucket.org:teqplay/repository.git bb-mirror-repository
2. download bfg from <https://rtyley.github.io/bfg-repo-cleaner/> and make a soft link of the downloaded version for simple command convenience (or rename it! Either way!).

   ln ./bfg-1.14.0.jar bfg.jar

   **On macOS you can use brew to install:**

   brew install bfg
3. Run **bfg**, that removes files bigger than Github limit (`100Mb`):

   java -jar bfg.jar --strip-blobs-bigger-than 100M bb-mirror-repository

   **On macOS:**

   bfg --strip-blobs-bigger-than 100M bb-mirror-repository
4. Change directory in and clean up unwanted but still existent unlinked large files from the repo:

   cd bb-mirror-repository
   git reflog expire --expire=now --all && git gc --prune=now --aggressive
5. Git-push mirror to github:

   git push --mirror git@github.com:teqplay/repository.git

If any errors beyond this point, it’s unexplored land!  
The ball is all yours.  
Put on Indiana Jones' hat , run away from the rolling boulder  and document everything  .

# Bitbucket pull requests conversion to GitHub Issues

As stated before, the migrated git repository doesn’t contain the merged pull requests.

For tracking and traceability purposes, we’d like to maintain the them. However, none of the available migration methods offered by GitHub include them.

After balancing the options, including own research in GitHub documentation, external technical forums and direct communication with a Github executive account manager, we end up customizing our own migration script ([**Teqplay's bitbucket pull request migration**](https://github.com/teqplay/bitbucket-pull-request-migration)) based on [mashayev](https://github.com/mashayev/bitbucket-pull-request-migration)’s.

Note that as pull-requests require both branches (source and destination) to exist, together with the fact that we commonly delete the source branch once they are merged. It’s not possible to hold record of the merged pull requests in GitHub.  
 Therefore, we will use **GitHub Issues** for keeping track of our former merged pull requests in Bitbucket.

## Prerequisites

* Docker v3.7 must be installed locally.
* GitHub **classic** PAT token with rights to create Issues (rights to `repo`) in the target repository. [Go here to create one](https://github.com/settings/tokens)
* Bitbucket **repository** token with rights to read pull requests in the source repository. [Go here to see the](https://bitbucket.org/teqplay/cargooptima-backend/admin/access-tokens) `cargooptima-backend` [**example**](https://bitbucket.org/teqplay/cargooptima-backend/admin/access-tokens)

## Using the migration script

The migration’s [README.md](https://github.com/teqplay/bitbucket-pull-request-migration) how to proceed, however, here you have a brief summary.

1. Clone repository [Teqplay's bitbucket pull request migration](https://github.com/teqplay/bitbucket-pull-request-migration).
2. Run the `checkRequirements.sh` and satisfy them if any is missing

   1. here is where you will need the Bitbucket and Github tokens.
3. Run the script `run.sh` (with no arguments) to convert all merged Bitbucket pull requests into GitHub issues.  
    Note that you might need to run it **as root**, depending on your local environment.

Note that only the MERGED pull requests will be migrated. This is how a migrated pull request will look as GitHub issue would look:

|  |
| --- |
|  |
| A GitHub issue representing a migrated Bitbucket pull request. |

## Helpful links:

Bitbucket cloud Rest API: <https://developer.atlassian.com/cloud/bitbucket/rest/>

PyGitHub Documentation: <https://pygithub.readthedocs.io/en/stable/github_objects/Repository.html>