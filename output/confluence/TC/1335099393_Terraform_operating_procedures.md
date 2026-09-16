---
id: confluence:1335099393
source: confluence
type: page
space: TC
title: Terraform operating procedures
author: Jamie de Leest
date: '2026-08-28'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1335099393
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1335099393
---
# Terraform operating procedures

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1335099393  

## Content

Engineer-facing runbook for how changes to this repo get approved and deployed. For the pipeline's design and rationale, see [ci-cd-plan.md](file:///C:/Users/jamie/IdeaProjects/teqplay-terraform/docs/ci-cd-plan.md); this doc is the "what do I actually do" companion.

## 1. Approval authority

**Only the** `devops` **GitHub team may approve an apply.** This is enforced, not just a convention: the `dev` and `production` GitHub Environments both carry a `required_reviewers` protection rule whose sole reviewer is the `devops` team. No individual and no other team is a reviewer on either environment. Adding anyone else as a reviewer requires a deliberate, reviewed change to the environment settings — never do it as a one-off favor to unblock someone.

## 2. Standard change process (the default — use this unless you can't)

1. Open a PR. `terraform-pr.yml` runs a read-only plan per affected component and posts it as PR comments.
2. Get code review and merge to `master`.
3. `terraform-deploy.yml` triggers automatically: fresh plan for every affected `live/dev/*` component → **devops approval** on the `dev` environment → apply. Then, independently, the same for `live/prod/*` on the `production` environment.
4. A Slack notification and deployment manifest are posted automatically.

This is the only path that gets you PR review, a read-only plan for reviewers to check before merge, and a fresh plan re-validated at apply time. Use it for essentially everything, including most things that feel urgent — see §4 for why.

### Manually re-running the pipeline

`terraform-deploy.yml` also accepts `workflow_dispatch`, for retrying after a transient failure or re-running detection against current `HEAD`. This is still the *normal* pipeline — same fresh plan, same devops approval gate, no bypass of anything in §1. Prefer this over break-glass whenever the pipeline itself is functioning.

## 3. Manual (break-glass) deployment

Two break-glass paths exist for when the normal pipeline can't be used or isn't fast enough. Which one applies depends mostly on who's acting:

* **Devops**, with Terraform/Terragrunt set up locally, should prefer §3.1 (local `terragrunt apply`) — it stays inside Terraform and keeps state consistent, and should only reach for §3.2 when even that is too slow.
* **Techsupport** is not expected to have a local Terraform/Terragrunt setup, so §3.2 (direct AWS console change) is their normal break-glass path, provided the cleanup in §3.2's procedure — the mandatory reconciliation PR — actually happens.

Both skip the PR review, the automated plan comment, and the deployment manifest/Slack notification that the normal pipeline produces — so neither is a shortcut for convenience, only for genuine emergencies.

**Who:** the `devops` team, or `techsupport` when actively handling an incident. Break-glass authority doesn't extend beyond those two groups. Devops sign-off before acting is always preferred; techsupport may proceed without it only when no devops engineer is reachable in time (see each path's procedure below).

### 3.1 Local `terragrunt apply`

A local `terragrunt apply`, run directly against an AWS account with the named `dev`/`prod` profile, outside CI entirely.

**When:** the normal pipeline is unavailable or unusable for the situation — e.g. CI/the Actions runner is down, GitHub itself is degraded, or a production incident requires a change faster than a PR-driven flow can realistically move. It is not for skipping review because a PR takes too long, and not for changes with no time pressure.

**Procedure:**

1. **Get devops sign-off first, if any devops engineer is reachable** — even a quick Slack message. This is the preferred path, including when techsupport is the one applying. Only if no devops engineer can be reached may techsupport proceed without sign-off — don't let an unreachable devops engineer block an active incident, but treat this as the exception, not the default, and say explicitly in the Slack post (step 4) that no devops sign-off was obtained and why.
2. Run `terragrunt plan` for the specific component locally first, and actually read the output. Never apply blind.
3. Apply with the correct named profile (`AWS_PROFILE=dev` / `AWS_PROFILE=prod`) against the one component that needs it. Don't `run-all apply` broadly under break-glass.
4. Post to the `terraform-deployment` Slack channel by hand — component, what changed, why, who applied it, who signed off — since CI isn't doing this for you here.
5. **Mandatory retroactive PR.** Open a PR with the equivalent change to `master` as soon as practical (same day if at all possible), and get it reviewed and devops-approved even though the change is already live. This is what brings git back in sync with reality and gets a second set of eyes after the fact. Don't rely on the nightly `terraform-drift.yml` check to catch a skipped step here — it's a safety net, not the process.

### 3.2 Direct AWS console change

Changing the resource directly in the AWS console (or CLI), bypassing Terraform/Terragrunt entirely. This is the expected break-glass path for techsupport, who aren't expected to have Terraform/Terragrunt, on the condition that whoever makes the change cleans up after themselves per the procedure below. Devops should still prefer §3.1 when it's practical for them, since it keeps state consistent without a reconciliation step, but §3.2 is a legitimate choice for devops too when it's faster.

**Procedure:**

1. Same rule as §3.1 — get devops sign-off before making the change, even informally, if any devops engineer is reachable; if none are, techsupport may proceed without it, but must say so explicitly in the Slack post below. Post to the `terraform-deployment` Slack channel with what changed, why, who was involved, and whether devops signed off.
2. **Mandatory reconciliation.** As soon as practical afterward, the change must be added to this repo — either as new/edited Terraform config, or an `import` of the resource if it didn't previously exist here — and go through a PR reviewed and approved by devops, the same as §3.1's retroactive PR. Until that PR lands, the console change is drift: it will show up in `terraform-plan.yml`/PR plans as an unexpected diff and in the nightly `terraform-drift.yml` check, and whoever made the console change is responsible for closing that loop, not whoever happens to notice the drift later.

## 4. Urgent / support-driven changes

"Urgent" means an active production incident or a customer-impacting issue — not schedule pressure on an otherwise-routine change.

* **Default even when urgent: §2, expedited.** A plan + devops approval + apply is typically minutes once a PR is up — page or directly ping the devops rather than skipping the process. This preserves PR review and the automated plan check, which matter *more*, not less, when you're moving fast under pressure.
* **Only fall back to §3 (break-glass)** when §2 genuinely isn't usable for the incident — the pipeline itself is down, or the fix must land before a PR-driven flow can plausibly complete. Break-glass does not remove devops from the loop; it moves their review from before the change to immediately after it, and still requires the sign-off from §3 at the moment of applying.
* Within break-glass, devops should prefer §3.1 (local `terragrunt apply`) over §3.2 (direct AWS console change) when practical. Techsupport, who isn't expected to have Terraform/Terragrunt set up, would be the best path to use §3.2 . Either way, a console change must brought back into this repo and reviewed/approved by devops afterward per §3.2 — it is never a way to leave the change out of Terraform permanently.
* Devops always reviews the outcome after the fact, whichever path you take. Sign-off *before* acting is preferred but not always required: under §3, techsupport may act without devops sign-off if no devops engineer is reachable in time — but the retroactive PR/reconciliation review in §3.1/ §3.2 is never skippable. There is no path where a change lands in prod without devops reviewing it at some point.