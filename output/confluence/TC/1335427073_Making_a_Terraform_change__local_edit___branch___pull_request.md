---
id: confluence:1335427073
source: confluence
type: page
space: TC
title: 'Making a Terraform change: local edit → branch → pull request'
author: Jamie de Leest
date: '2026-08-28'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1335427073
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1335427073
---
# Making a Terraform change: local edit → branch → pull request

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1335427073  

## Content

Audience: anyone making a change in this repo, whether it's your first time or your tenth and you want a checklist. Covers everything from "I need to change something" up to "the PR is open and CI is running." What happens after merge (deploy approvals, drift checks) is summarized at the end but is owned by whoever holds the environment approval role — see for the full pipeline design.

## 1. One-time setup

You need:

* **Git**, and push access to `teqplay/teqplay-terraform`.
* **OpenTofu 1.12.2** and **Terragrunt 1.1.2** — these exact versions, pinned in [.github/actions/setup-terragrunt/action.yml](file:///C:/Users/jamie/IdeaProjects/teqplay-terraform/.github/actions/setup-terragrunt/action.yml) because they match what generated this repo's `.terraform.lock.hcl` files. A newer local version can plan differently or fail to read the lock file.
* **AWS CLI** with named SSO profiles `dev` and `prod` configured (`aws configure sso --profile dev`, same for `prod`). `root.hcl` reads the profile name from each environment's `env.hcl` ([live/dev/env.hcl](file:///C:/Users/jamie/IdeaProjects/teqplay-terraform/live/dev/env.hcl), [live/prod/env.hcl](file:///C:/Users/jamie/IdeaProjects/teqplay-terraform/live/prod/env.hcl)) — you do not set it yourself, but the profile names must exist in your `~/.aws/config` and must be logged in (`aws sso login --profile dev`) before Terragrunt can read state or plan.

Clone the repo if you haven't already:

wide760truegit clone git@github.com:teqplay/teqplay-terraform.git

## 2. Branch

Branch off `master`:

wide760truegit checkout master
git pull
git checkout -b <short-description-of-change>

There's no enforced naming convention, but a short imperative name (e.g. `bump-eks-node-size`, `add-dev-sns-topic`) makes the PR list easier to scan.

## 3. Make the change

Every component lives at `live/<env>/<component>/terragrunt.hcl` (occasionally one level deeper, e.g. `live/prod/rds/keycloak`). It includes `root.hcl` and points at a module under `modules/`. Two common cases:

* **Change an existing component's inputs** — edit the `inputs = { ... }` block in its `terragrunt.hcl`.
* **Add a new component** — see [README.md § Adding a component to an environment](file:///C:/Users/jamie/IdeaProjects/teqplay-terraform/README.md#adding-a-component-to-an-environment) for the minimal `terragrunt.hcl` template.

If the change is in shared module code (`modules/<name>/*.tf`), remember it will affect **every environment's component that uses that module** — dev and prod both, not just the one you're thinking about.

## 4. Check it locally before pushing

From inside the component's directory:

wide760truecd live/<env>/<component>
terragrunt init # only needed the first time, or after a source/provider change
terragrunt hcl fmt # auto-formats the .hcl you just edited
terragrunt plan

Read the plan output. Confirm it only touches what you intended — especially watch for anything unexpected being destroyed. If the component depends on another (e.g. `eks` depends on `vpc`), Terragrunt resolves that automatically via its `dependency` blocks; you don't need to plan those separately unless you changed them too.

If you touched files under `modules/`, also run from the repo root:

wide760truetofu fmt -check -recursive modules/

This is the same check CI runs repo-wide; fixing it locally avoids a failed required check later.

## 5. Commit and push

wide760truegit add live/<env>/<component>/terragrunt.hcl # or whatever you changed
git commit -m "short description of why, not just what"
git push -u origin <branch-name>

Only stage the files you meant to change — a stray `.terraform/` or `.terragrunt-cache/` directory should never be committed (they're local working directories, not something to review).

## 6. Open the pull request

wide760truegh pr create --base master --title "..." --body "..."

or open it from the GitHub UI after pushing. Target `master`.

## 7. What happens automatically on the PR

`terraform-pr.yml` runs as soon as the PR is opened (and again on every push to it):

1. **Format check** — `tofu fmt` (modules/) and `terragrunt hcl fmt` (live/, root.hcl), repo-wide.
2. **Affected-component detection** — figures out every component your change touches, including ones you didn't edit directly (dependents of a changed module, or of a changed dependency like `vpc`).
3. **Plan** — runs a real `terragrunt plan` for each affected component, using a **read-only** role in that component's own AWS account (dev changes plan with the dev role, prod changes with the prod role). No apply credentials are ever used here.
4. **PR comments** — one index comment listing every affected component with its add/change/destroy counts (plus a warning banner if anything would be destroyed), and a separate comment per component that actually has changes to show. A component whose plan comes back clean doesn't get its own comment — just a line in the index.

   * For `live/*/secrets-manager` and `live/*/lambda` components, the actual plan output is deliberately withheld from both the comment and the CI log (it can contain plaintext secret values). That component's comment will tell you to plan it locally instead if you need to see the detail.
5. **Required check** — a single `terraform-pr` gate job needs to pass before the PR can merge. It reflects the worst outcome of the jobs above; on a docs-only PR (nothing under `live/`/`modules/`) it passes trivially since there's nothing to plan.

If a job fails, click through to its log from the PR checks tab — the PR comment only carries plan output, not fmt/validate errors.

## 8. Review and merge

A reviewer reads the PR comment(s), particularly the add/change/destroy counts and any destroy warning, then approves normally through GitHub. Push more commits to the same branch if changes are requested — the PR comments update in place rather than piling up.

Once approved and the `terraform-pr` check is green, merge to `master` (standard GitHub merge — no special merge process here).

## 9. After merge

Merging to `master` triggers `terraform-deploy.yml`, which is a separate, approval-gated process — not something opening the PR drives directly:

1. A fresh plan runs for every affected `live/dev/*` component, then waits for a required reviewer to approve the `dev` GitHub Environment before applying.
2. If any `live/prod/*` components are affected, the same fresh-plan → approval → apply sequence runs against `production`, independent of the dev stage's outcome.
3. A deployment summary posts to the `terraform-deployment` Slack channel (success/failure, resources changed, commit, link to the run).

If you need something applied and don't hold either environment's approval role, ask whoever does to approve the pending deployment run in GitHub Actions — merging the PR does not apply anything by itself.

## Quick reference

wide760truegit checkout master && git pull
git checkout -b my-change
# edit live/<env>/<component>/terragrunt.hcl
cd live/<env>/<component>
terragrunt hcl fmt
terragrunt plan
cd -
git add -A
git commit -m "..."
git push -u origin my-change
gh pr create --base master