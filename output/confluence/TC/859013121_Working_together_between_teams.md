---
id: confluence:859013121
source: confluence
type: page
space: TC
title: Working together between teams
author: Darius Wattimena
date: '2025-09-08'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/859013121
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/859013121
---
# Working together between teams

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/859013121  

## Content

# Ways of working

With the new team structure we decided on the following ways of working between the teams we have:

Here we decided that the Core Components team will be working mainly in an X-as-a-Service way. To make this more streamlined we have made some decisions and actions that are needed in both the platform team and the consumers that make use of the service.

# Decisions

## Agree on implementation plan between teams

Applicable for complex and large changes in a platform team or the consumers of said platform.

1. Define what the scope is of the feature.
2. Define what is scoped out.
3. Agreement on functional and non-functional requirements.
4. Agreement on working together form.

   1. x-as-a-service.
   2. collaboration, also agree when to part ways.
5. Document the plan.
6. Agree on plan routinely.

Boundaries of the platform remain strict, even when working in a collaboration way. This means that members of other teams do not make any changes in the platform. Next to this, the platform members do not make any changes in the consumer.

## Plan in synchronisation with consumers

When making changes make sure consumers are aware of the changes done to the platform. This means the following steps need to be taken care of:

1. Plan timely. Avoid planning too early as momentum and knowledge gets lost. Avoid planning too late as other teams are following their own plan.
2. Communicate changes towards consumers.

   1. What is the change?
   2. Why is it changed?
   3. What is affected?
   4. When will it be changed?
   5. Document changes and share with the consumers.
   6. Consumers should check how the changes affect them.

## Checklist for refinements

When doing refinements of cards having a checklist in place with questions to ask to ensure the right questions are asked.

1. Which endpoints are affected?
2. Who is consumer those endpoints?
3. How do we test our interface?

Next to this the consumers have additional questions they need to ask themself while doing a refinement:

1. Are we changing the endpoints we are consumer?
2. Are we changing the way we are consuming the endpoints?

With both those questions the platform should be informed on the intention of the change. With this it is expected from the teams to check how it will affects them.

## Safeguard changes

1. Embed changes in platform by logging them structurally in an understandable manner.
2. Safeguard changes by embedding them in tests.
3. QA member plays active role to collaborate with the team to work on test cases.
4. Test on platform’s interface with consumers. Test before you will deliver to your consumers.
5. Consumer should trust on testing, but products itself should be covered by automatic integration / regression testing

## Enrich knowledge level

To keep both the platform team and consumers on the right knowledge level the following steps should be taken:

1. Better understanding in platform team how all different components work . Having a clear understanding on the architecture but also the context.
2. Increase richness of API documentation.

## Better process control

Be proactive in escalating to avoid the “almost there“-problem. If this happens a sessions should be planned to discuss the following:

1. What are we trying to do?
2. What was the initial plan?
3. Are we still following this plan, yes/no, why?
4. What corrective actions do we take?
5. How do we focus and keep track of progress?

## Actions

To improve on this the following actions will be taken in the applicable teams:

1. Document the current Services delivered by improving the API Swagger.
2. Synchronise plans between teams on interface level.
3. Start by creating plan and agreeing on team-work form when having big/complex changes.
4. Implement refinement checklist.
5. Implement tests on interface.
6. Implement ‘We’re almost there’-Escape. Using stand-ups to identify.
7. When a new team member joins a team, inform them on the way how we collaborate with other teams.