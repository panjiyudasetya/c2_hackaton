---
id: confluence:651296770
source: confluence
type: page
space: TC
title: API Coding Standards
author: Richard van Klaveren
date: '2025-03-04'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/651296770
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/651296770
---
# API Coding Standards

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/651296770  

## Content

### **Empty Object Fields**

Empty fields should not be returned through the endpoint. These should always be undefined, and thus not returned.

So a empty field should not be returned as: `null` `0`, `""` or `"-"`

### **Timestamps and ISODates**

The choice between timestamps and ISOStrings is open for each project as long as either of the two is used within this project. Timestamps and ISOStrings should not be mixed together in the project unless both are returned at all times.

### **Not found return statement**

When an api endpoint with search criteria has not found any results the following should be returned:

1. In case of a LIST of items an empty array should be returned `[]`
2. In case of a single item being searched for the endpoint should return `404: Not Found`