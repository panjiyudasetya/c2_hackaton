---
id: confluence:1188036609
source: confluence
type: page
space: TC
title: SonarQube Possibilities
author: Joost Dambrink
date: '2026-04-16'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1188036609
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1188036609
---
# SonarQube Possibilities

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1188036609  

## Content

## SonarQube

**SonarQube is a static code analysis platform that continuously inspects code to identify bugs, security vulnerabilities, and code quality issues. It analyzes code across multiple languages, enforces coding standards, and provides actionable feedback to improve maintainability, reliability, and security.**

It integrates into development workflows (e.g. CI/CD pipelines) to automatically review code changes, track technical debt, and enforce quality gates before code is merged or deployed.

**Contents**

12falselistbracketstrue

## Pricing

### Pay per line of code analyzed

This is not based on how frequently your code is analyzed.

---

### Pricing tiers

* **100,000 total lines of code** — $32
* **300,000 total lines of code** — $190

---

### How lines of code (LOC) are counted

* Only lines from **private projects** count toward your limit
* If a project has multiple branches, only the **largest branch** is considered
* The number of analyses does **not** affect the LOC count

**Example**  
A project with 6,000 LOC analyzed 100 times in a month still counts as **6,000 LOC**, not 600,000.

**ais-engine** - 48k lines of code

**vesselvoyage** - 35k lines of code

**poma** - 14k lines of code

## Core Functionality

### Overview

SonarQube provides automated code analysis and delivers feedback to developers and teams about the quality of their code. Its primary role is to scan code, identify issues, and present the results in a structured and actionable way.

---

### 1. Code Analysis Results

SonarQube scans source code and produces a list of detected issues. These issues are clearly categorized and linked to specific locations in the codebase.

What the user gets:

* A detailed list of issues in the code
* Exact file and line references
* Descriptions explaining each issue
* Severity levels to prioritize fixes

---

### 2. Centralized Dashboard

SonarQube provides a web-based interface where all analysis results are displayed.

What the user gets:

* A project dashboard with current code quality status
* Historical data showing how code quality evolves over time
* Drill-down views from project level to individual lines of code

---

### 3. Pull Request Feedback

SonarQube integrates with version control platforms to analyze code changes before they are merged.

What the user gets:

* Comments directly on pull requests
* Identification of issues in newly added or modified code
* A clear pass/fail status for the proposed changes

---

### 4. Quality Gate Status

SonarQube evaluates whether code meets predefined quality standards.

What the user gets:

* A pass or fail result for each analysis
* Visibility into which conditions are not met
* Integration with pipelines to stop progression when standards are not satisfied

---

### 5. Issue Tracking and Management

SonarQube allows users to manage detected issues within the platform.

What the user gets:

* Ability to assign issues to team members
* Options to mark issues as resolved, false positive, or accepted
* Filtering and searching capabilities to manage large numbers of issues

---

### 6. Integration with Development Workflow

SonarQube integrates into development tools and processes.

What the user gets:

* Automatic analysis results as part of CI/CD pipelines
* Feedback within pull requests
* Optional real-time feedback in the IDE through connected tools

---

### 7. Historical Tracking

SonarQube stores results from previous analyses.

What the user gets:

* Visibility into trends over time
* Ability to compare current and past states of the codebase
* Insight into whether code quality is improving or degrading

---

### 8. Multi-Project Visibility

SonarQube can manage multiple projects within a single instance.

What the user gets:

* A centralized view across multiple repositories
* Consistent reporting structure across teams
* Aggregated insights (depending on edition)

## Measures used in Analysis by SonarQube

### Overview

When SonarQube analyzes code, it inspects source files, configurations, and (optionally) external reports to identify problems, risks, and structural issues. Its scanning capabilities cover correctness, security, maintainability, structure, and compliance.

---

### 1. Functional Correctness Issues (Bugs)

SonarQube scans for code that may behave incorrectly at runtime.

It looks for:

* Invalid logic and incorrect conditions
* Null reference risks
* Incorrect comparisons or assignments
* Infinite or unintended loops
* Resource leaks (e.g., unclosed files/streams)
* Misuse of APIs or language constructs
* Concurrency issues (race conditions, improper synchronization)
* Exception handling mistakes (swallowed exceptions, improper propagation)

---

### 2. Security Vulnerabilities

SonarQube scans for patterns that could be exploited.

It looks for:

* Injection vulnerabilities (SQL, command, LDAP, etc.)
* Cross-site scripting (XSS) patterns
* Unsafe deserialization
* Hardcoded credentials or secrets
* Weak cryptographic usage
* Insecure authentication or authorization patterns
* Exposure of sensitive data
* Insecure configuration usage
* Lack of input validation or sanitization

---

### 3. Security Hotspots (Review-Required Risks)

It identifies code that is not necessarily broken but requires manual review.

It looks for:

* Use of sensitive APIs
* Potentially dangerous operations
* Security-sensitive configurations
* Areas where intent must be validated by a developer

---

### 4. Maintainability Issues (Code Smells)

SonarQube scans for code that is difficult to maintain or evolve.

It looks for:

* Long or complex methods
* Large classes or files
* Poor or unclear naming
* Dead or unused code
* Redundant logic
* Overuse of comments instead of clear code
* Violations of clean code principles
* Poor separation of concerns

---

### 5. Code Complexity and Structure

It analyzes how complicated and structured the code is.

It looks for:

* Deep nesting of logic
* Complex branching structures
* Overly complicated expressions
* Unstructured or hard-to-follow logic flows
* Tight coupling between components
* Lack of modularity

---

### 6. Code Duplication

SonarQube scans for repeated code patterns.

It looks for:

* Copy-paste code blocks
* Structurally identical logic across files
* Repeated implementations of the same functionality

---

### 7. Coding Rule Violations

SonarQube checks code against predefined and custom rules.

It looks for:

* Violations of language best practices
* Style inconsistencies (where rules enforce them)
* Misuse of frameworks or libraries
* Deprecated or discouraged patterns
* Organization-specific rule violations

---

### 8. Test Coverage (Imported Data)

SonarQube incorporates test execution results.

It looks for:

* Which lines of code are executed by tests
* Which parts of the code are not tested
* Coverage gaps in new or modified code

Important:

* This is based on external reports, not computed by SonarQube itself

---

### 9. Code Size and Structure Indicators

It scans basic structural aspects of the codebase.

It looks for:

* Lines of code
* Number of files, classes, methods
* Distribution of code across modules

---

### 10. Documentation and Readability

SonarQube scans for clarity and documentation quality.

It looks for:

* Missing documentation in public APIs
* Inconsistent or unclear comments
* Code that is difficult to understand without explanation

---

### 11. Configuration and Project Setup Issues

SonarQube scans certain configuration aspects.

It looks for:

* Misconfigured project files
* Incorrect or inconsistent setup patterns
* Risky configuration usage

---

### 12. Dependency and Usage Patterns

Depending on language/plugins, it inspects how dependencies are used.

It looks for:

* Improper use of libraries
* Risky or outdated usage patterns
* Misuse of third-party APIs

---

### 13. New Code vs Existing Code

SonarQube differentiates between new and existing code.

It looks for:

* Issues introduced in new changes
* Whether new code meets defined standards
* Regressions in quality

---

### 14. Branch and Pull Request Changes

When integrated with version control, it scans code changes.

It looks for:

* Issues in modified lines only
* Impact of changes on overall code quality
* Violations introduced in pull requests

---

### 15. Language-Specific Issues

Each supported language has specialized rules.

It looks for:

* Language-specific anti-patterns
* Misuse of language features
* Framework-specific issues

---

### 16. Patterns Common in AI-Generated Code

SonarQube also scans for patterns often introduced by AI tools.

It looks for:

* Missing validation logic
* Overly generic implementations
* Insecure defaults
* Poor error handling

## TLDR; Use Cases for our workflow

SonarQube is integrated directly into our CI pipeline, where it runs automated **analysis** on every pull request and main branch update. Each analysis evaluates the code using a predefined set of rules defined in **Quality Profiles**, and produces metrics around **bugs**, **vulnerabilities**, and **code smells**, as well as broader indicators like **maintainability**, **reliability**, and **security ratings**.

**Quality Profiles** define what “good code” means for us. They are collections of rules per programming language that detect issues such as potential bugs, security risks, and poor coding practices. By configuring these profiles, we control which rules are enforced and how strict the analysis is, ensuring consistency across the team and codebase.

A central concept we rely on is the **Quality Gate**. This acts as an enforced checkpoint in CI: if the code does not meet the defined criteria (for example, introducing new issues or lowering coverage), the Quality Gate fails. In that case, the pull request should not be merged. This ensures that every change meets a minimum standard before entering the codebase.

We focus primarily on **New Code** rather than trying to immediately fix all legacy issues. SonarQube distinguishes between overall code and new code, allowing us to enforce strict standards only on recent changes. This helps us gradually improve the codebase without blocking development due to historical technical debt.

SonarQube also provides **Pull Request Analysis**, which gives developers direct feedback on their changes. Issues are surfaced early, often directly in the pull request, making it easier to fix problems before they are merged.