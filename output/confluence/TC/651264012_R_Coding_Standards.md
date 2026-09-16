---
id: confluence:651264012
source: confluence
type: page
space: TC
title: R Coding Standards
author: Richard van Klaveren
date: '2025-03-04'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/651264012
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/651264012
---
# R Coding Standards

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/651264012  

## Content

## 1. R Style Guide

R code should be written in accordance to the [Google's R Style Guide](https://google.github.io/styleguide/Rguide.xml).

There is one exception to this style guide and a number of additions.

### 1.1 Function documentation

The only exception to this style guide is the way functions are documented!

* Documentation should be done using the Roxygen2 package (see section 2).

#' Add together two numbers
#'
#' @param x A number
#' @param y A number
#' @return The sum of \code{x} and \code{y}
#' @examples
#' add(1, 1)
#' add(10, 1)
add <- function(x, y) {
x + y
}

### 1.2 Loops

* Use `seq(along=x)` to protect against instances where x is empty
* Use `apply, lapply, etc` when possible

# Good
lapply(seq(along=x), function(i) {
doSomething(i)
})
# Acceptable
for (i in seq(along=x)) {
doSomething(i)
}
# Bad
for (i in 1:length(x)) {
doSomething(i)
}

### 1.3 Repeat

* Use repeat for better interpretability

# Good
repeat {
...
}
# Bad
while (TRUE) {
...
}

### 1.4 Pipes

If you use the `%>%` operator from the tidyverse, put each verb on its own line. This makes it simpler to rearrange them later, and makes it harder to overlook a step. It is ok to keep a one-step pipe in one line.

# Good
iris %>%
group\_by(Species) %>%
summarize\_all(mean) %>%
ungroup %>%
gather(measure, value, -Species) %>%
arrange(value)
iris %>% arrange(Petal.Width)
# Bad
iris %>% group\_by(Species) %>% summarize\_all(mean) %>%
ungroup %>% gather(measure, value, -Species) %>%
arrange(value)

## 2. Documentation

Documentation of R code should be written using the [roxygen2 package](https://github.com/klutometis/roxygen).

## 3. Package Development

Make R packages using [devtools](https://github.com/r-lib/devtools).

## 4. Unit Testing

Test functions using [testthat](https://github.com/r-lib/testthat). Track test coverage for your R package and view reports locally using [covr](https://github.com/r-lib/covr)

## 5. Static Code Analysis

Lintr can be used for [Static Code Analysis](https://github.com/jimhester/lintr). Note that not all rules from this coding standard is default in Lintr.