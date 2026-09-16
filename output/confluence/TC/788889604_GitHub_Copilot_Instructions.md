---
id: confluence:788889604
source: confluence
type: page
space: TC
title: GitHub Copilot Instructions
author: Joost Dambrink
date: '2025-07-02'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/788889604
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/788889604
---
# GitHub Copilot Instructions

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/788889604  

## Content

## 📌 Using GitHub Copilot Instructions for Code Reviews

### What are Copilot Instructions?

GitHub Copilot instructions let you **customize how Copilot generates suggestions** by providing natural-language guidance about your coding standards and conventions. These instructions are especially valuable for **code reviews**, where they help Copilot propose improvements that align with your team’s expectations.

While the main goal of these instructions is to enhance the **quality, consistency, and speed of code reviews**, they also affect **code completions more broadly**, ensuring Copilot suggests code that matches your team’s practices even outside the review process.

When integrated into your review workflow, Copilot instructions can help you:

✅ Generate review comments and suggested changes that follow your standards  
✅ Automate repetitive or stylistic feedback  
✅ Maintain consistency in architecture, formatting, and naming conventions  
✅ Save time by streamlining the review process

---

### ✏️ Current Copilot Instructions for Code Reviews

Below are the current Copilot instructions configured specifically to improve **code reviews**:

# Copilot Code Review Guidelines
## Clarity and Maintainability
Ensure all functions clearly state their purpose with descriptive comments or docstrings. Comments must explain the reasoning behind complex logic instead of restating obvious details.
## Naming Conventions
Use descriptive, meaningful names for all variables, functions, and classes. Avoid single-letter names except for simple loop counters.
## Avoiding Deep Nesting
Avoid nesting loops and conditionals beyond three levels. Refactor deeply nested logic into separate, clearly named functions.
## Error Handling Best Practices
Handle potential errors explicitly. Provide clear and actionable error messages or exceptions instead of silent failures or generic responses.
## Performance Awareness
Avoid unnecessary object creation and redundant loops. Use efficient data structures (e.g., sets for membership checks) where appropriate to improve performance.
## Security Practices
Never commit sensitive information, such as API keys or credentials, directly in source code. Always reference environment variables or secure secrets management.
## Testing Coverage
Include tests for every new feature or significant change. Tests must cover both typical scenarios and edge cases.
## Consistent Logging
Use structured logging consistently throughout the project. Avoid excessive logging at INFO or DEBUG levels in production code.
## Modularity and Reusability
Ensure functions and modules have a single, clear responsibility. Break up functions that are excessively long (typically longer than one screen) into smaller, reusable components.
## API Coding Standards
### Empty Object Fields
Empty fields should not be returned through the endpoint. Always leave them undefined so they are not included in the response.
Avoid returning empty fields as: `null`, `0`, `""`, or `"-"`.
### Timestamps and ISODates
Choose either timestamps or ISOStrings for dates within a project, and use that consistently. Do not mix timestamps and ISOStrings unless both are returned at all times.
### Not Found Return Statement
For endpoints using search criteria:
- If searching for a list of items and nothing is found, return an empty array `[]`.
- If searching for a single item and nothing is found, return `404: Not Found`.

These instructions guide Copilot to propose changes during reviews that match our expectations, while also influencing completions when writing new code.

The instructions are added to the project under .github/copilot-instructions.md more info on how to create a file like this below.

---

### 📚 Helpful Documentation

To learn how to create and manage GitHub Copilot instructions for **code reviews and completions**, refer to these resources:

<https://docs.github.com/en/copilot/how-tos/agents/copilot-code-review/configuring-coding-guidelines>

<https://docs.github.com/en/copilot/how-tos/custom-instructions/adding-repository-custom-instructions-for-github-copilot>

---

### 📌 Current Scope

* **Repository:** These review-focused instructions are currently applied only to the `vesselvoyage` repository.

---