---
id: confluence:652738598
source: confluence
type: page
space: TC
title: Portreporter - Cypress
author: Richard van Klaveren
date: '2025-03-04'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652738598
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652738598
---
# Portreporter - Cypress

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652738598  

## Content

### When running cypress for portreporter you need to:

1. Setup portreporter locally
2. npm install
3. Inside the **cypress.json** add the env
4. "env":{
   "username":"testautomationuser@teqplay.nl",
   "password":// These credentials you will find in Lastpass
   }
5. npm start
6. npm run cypress
7. You will find all test in cypress\integration folder

If you would like to run tests for multiple roles:

const runAllTestsAsUserRole = (userRole?: string, portcall?: string) => {
beforeEach(() => {
cy.loginPortReporter(
userRole
? putRoleIntoUsername(Cypress.env('username'), `+${userRole}`)
: Cypress.env('username'),
Cypress.env('password')
)
})
it('Description of the test..', Test)
}
...
// Run the test for Terminal user
describe('[TERMINAL] Portcall page', () => runAllTestsAsUserRole('terminal'))

When doing complex and heavy testing sometimes the cypress UI/ Chrome can go out of memory, then it's better run it with:

npm cypress run --spec "cypress\integration\config-screens\test.spec.ts"

⚠️ When using backend endpoints and adding things to backend. Remember to let the testautomationuser delete these items in the test.