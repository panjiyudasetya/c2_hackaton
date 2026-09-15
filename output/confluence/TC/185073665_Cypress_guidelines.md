---
id: confluence:185073665
source: confluence
type: page
space: TC
title: Cypress guidelines
author: David Hansson
date: '2023-05-25'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/185073665
explicit_links: []
---
# Cypress guidelines

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/185073665  

## Content

## General

*Most information can be found here:* <https://docs.cypress.io/guides/references/best-practices>

Do use descriptive test names: Give your test cases meaningful and descriptive names that clearly explain what functionality or scenario they are testing. This makes it easier to understand the purpose of each test.

// Don't do this
it('should work', () => {
....
});
// Do this
it('should calculate the total price correctly when applying a discount', () => {
....
});

### Waiting for interactions

// Don't do this
cy.wait(3000);
// Do this
cy.get('.submit-button').should('be.visible');

Decreased test execution speed: Adding `cy.wait()` commands in your tests increases the overall execution time. If your test suite contains multiple unnecessary wait commands, it can significantly slow down the test execution.

### Make a solid submit or action (API)

// Don't only test UI interactions
cy.get('.submit-button').click();
cy.get('.notfication').should('be.visible');
// Do also test underlying functionality or API
cy.request('POST', '/api/login', { username, password }).then((response) => {
expect(response.status).to.equal(200);
cy.get('.notfication').should('be.visible');
});

In this case we also do test the backend, but also it will wait untill the request is done (unless timeout or 404)

### Make sure to delete the data when creating data

Remember, data cleanup should be an part of your test automation process to maintain a sustainable BE environment. Otherwise we will flood the BE with alot of test creating data, and not removing it. It’s also important that we don’t delete wrong stuff always take the ID

// Do this
it('should delete a post....', () => {
cy.visit('/posts');
// Find the post with the correct ID and delete it
cy.get(`[data-cy="post-delete-${postId}"]`).click();
// Add a listing for the API here and make sure it's 200
cy.wait('@deletePost').then(({ response }) => {
expect(response, 'status 200').to.have.property('statusCode', 200)
// Assert that the post is no longer displayed in the table
cy.get('[data-cy="post-table"]').should('not.contain', 'Test Post');
})
});
// Don't
it('should delete a post....', () => {
// delete the first child in the table without verifying if it is the correct post
cy.get('table tr:first-child [data-cy="post-delete"]').click();
// Don't assume the post is deleted without confirming its absence in the table
cy.get('[data-cy="post-table"]').should('not.contain', 'Test Post');
});

### Make solid name attributes and not generic ones

|  |  |  |
| --- | --- | --- |
| `cy.get('button').click()` | Never | Worst - too generic, no context. |
| `cy.get('.btn.btn-large').click()` | Never | Bad. Coupled to styling. Highly subject to change. |
| `cy.get('#main').click()` | Sparingly | Better. But still coupled to styling or JS event listeners. |
| `cy.get('[name="submission"]').click()` | Sparingly | Coupled to the `name` attribute which has HTML semantics. |
| `cy.contains('Submit').click()` | Depends | Much better. But still coupled to text content that may change. |
| `cy.get('[data-cy="submit"]').click()` | Always | Best. Isolated from all changes. |

### When creating an generic component that being used in multiple of times + same page

When you have a generic component, such as a `<select>` element, that is used in multiple instances on a page, adding the `data-cy` prop allows you to uniquely identify and target each instance during testing. In this way we will not accidently change the ID or name

<select data-cy={props.dataCy} …. />

# Portreporter - Cypress

### When running cypress for portreporter you need to:

1. Setup portreporter locally
2. npm install
3. Inside the **cypress.json** add the env

js"env":{
"username":"testautomationuser@teqplay.nl",
"password":// These credentials you will find in Lastpass
}

5. npm start
6. npm run cypress
7. You will find all test in cypress\integration folder

If you would like to run tests for multiple roles:

jsconst runAllTestsAsUserRole = (userRole?: string, portcall?: string) => {
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

jsnpm cypress run --spec "cypress\integration\config-screens\test.spec.ts"

⚠️ When using backend endpoints and adding things to backend. Remember to let the testautomationuser delete these items in the test.