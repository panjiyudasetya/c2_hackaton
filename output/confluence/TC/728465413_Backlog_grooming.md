---
id: confluence:728465413
source: confluence
type: page
space: TC
title: Backlog grooming
author: Joaquin Marquez Bugella
date: '2025-05-19'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/728465413
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/728465413
---
# Backlog grooming

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/728465413  

## Content

Work in progress

none

# Purpose of grooming

In words of probably some AI , the definition of grooming in the Agile methodologies verses like:

> ***A grooming session**, also known as **backlog grooming** or **backlog refinement**, is a regular meeting where a product team reviews and prioritizes items in the product backlog to prepare for upcoming sprints.*  
> *The goal is to ensure that the backlog is organized, up-to-date, and ready for effective sprint planning.*

So, in my own words, **grooming should be an agile artifact that adds value**, saves us time and makes our development and delivery process smooth.

So it’s important to prevent it from becoming tedious and time-eating, which is always a risk!

That’s why, this guideline is written, to *groom the grooming sessions* .

# Recommended process

Remember that this is only a guideline for a smooth and efficient grooming session (to avoid wasting time). Meaning that deviations from it are always welcome when needed (however deviations shouldn’t become a habit ).

## Frequency and length

The rule of thumb is **once per sprint**, for **1 hour + 15 minutes of preparation**.

## Tag set

For a fast and efficient grooming session, let’s use the following labels in the Jira cards.  
Keep in mind that Jira allows multiple labels in cards, so if they two labels are mutually *excluyent* (incompatible), this has to be handled manually.

| **Label** | **Purpose** |
| --- | --- |
| `JMB` | To use in combination with labels. The user initials, if you want to remember which cards you added which labels (i.e.`Grooming` `JMB`, or `ToRemove` `JMB`).  Multiple initials labels are possible, of course , meaning that all these people would like to contribute. |
| `Grooming` | This label indicates that this card requires to be evaluated (for first time or again) in the next grooming sessions. |
| `NeedsMoreInfo` | After evaluating the card, it indicates that we need additional information to properly set `ReadyForSprint`. |
| `NeedsFinalTest` | Not only for grooming specifically, but an adding it for its relevancy.  It can be seen as a more specific subclass of `NeedsMoreInfo` that stands for an action related to another label. I.e. in combination with `ToRemove`, would indicate that ***it needs a final test to be removed***. |
| `ReadyForSprint` | The card contains all information required to be included in a future sprint.  The card estimation should be set as story points.  Of course if the conditions and context change with time, this must be reconsidered at some point. |
| `ToRemove` | This label indicates that this card should be evaluated in the grooming session to be deleted. |
| **No tag** | No remark at all.  It could mean that it’s a new card or that the card is already in the current sprint. |

## Preparation

Before each session, each participant should have gone through the backlog (**time-boxed, please**) selecting the most relevant cards (in its opinion) to discuss in the session.

A set of cards, labeled with `Grooming` and the participant’s initials should be selected to discuss in the session.

## Session steps

### `Grooming` label evaluation

The Jira backlog should get filtered by the `Grooming` label. The process is as obvious as going through the filtered result and discuss them.

When possible, the `Grooming` label should be replaced by either of these:

* `ReadyForSprint`, if all relevant information is in the card, including the *DefinitionOfDone* and the estimated story points.
* `NeedsMoreInfo` , if not it’s not all relevant information is available.

  + In this case, a point should be added in the ***Actions*** meeting notes and in the card as a comment.
* `Grooming`, if there was no time to tackle it.

### Cleaning up

Cards that are labeled as `ToRemove` should be evaluated and eventually removed if everybody agrees.

## Outcome

In an ideal scenario, after the grooming, cards and their tasks should be more clear.

As many as possible cards previously labeled with `Grooming` should get it replaced by `ReadyForSprint`, `NeedsMoreInfo` or deleted – ideally, the first case .

### Actions

In every session (not only in grooming), a list of actions is in place.

In particular, the grooming actions shall contain all needed actions to resolve the cards labeled with `NeedsMoreInfo` (whenever it’s possible).

# Automation

Jira provides an automation mechanism to keep process details aligned.

When the process gets consolidated to a relevant degree, let’s set rules like:

* Forbid setting `ReadyForSprint` if Story Points aren’t set
* Remove `NeedsMoreInfo` when setting `ReadyForSprint`.