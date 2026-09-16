---
id: confluence:181862476
source: confluence
type: page
space: TC
title: CSS / SASS code style guide
author: Damon Asberg
date: '2025-11-03'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/181862476
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/181862476
---
# CSS / SASS code style guide

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/181862476  

## Content

This code style guide is about the usage of CSS / SASS files inside our projects.

## Class and id casing

Try to use `kebab-case` for class names. This will ensure consistency throughout projects. `camelCase` is not allowed, unless you are including data in a class name.

## Allow breathing room between items

Ensure that within your CSS there is a “breathing room” / empty line between rulesets. This makes reading your ruleset less cramped.

Prettier should take care of your needs for this.

sasswide760.wrapper {
background: red;
.button {
color: white;
padding: 10px;
}
.container {
padding: 20px;
}
.header {
.header-inner {
margin-left: 10px;
margin-right: 8px;
}
.link {
margin-left: 10px;
font-size: 8px;
}
> div {
color: red;
}
}
}sasswide760.wrapper {
background: red;
.button {
color: white;
padding: 10px;
}
.container {
padding: 20px;
}
.header {
.header-inner {
margin-left: 10px;
margin-right: 8px;
}
.link {
margin-left: 10px;
font-size: 8px;
}
> div {
color: red;
}
}
}

## Be consistent in type usage

There is no strict rule on using either `rgb`, `rgba`, `hsl` or hexadecimal codes for colour coding - but make sure you are consistent throughout your project.

Same applies to `px`, `rm`, `em`, be consistent in its usage throughout your project.

## Top level className

Ensure the top level className in your CSS is the same name as the React component name for clarity.

typescriptwide760const ReactComponent = () => {
return (
<div className="my-cool-component">
...
</div>
)
}sasswide760.my-cool-component {
...
}typescriptwide760const ReactComponent = () => {
return (
<div className="react-component">
...
</div>
)
}sasswide760.react-component {
...
}

## Prevent excessive nesting

With SASS/SCSS you can nest multiple rulesets underneath each other, pretty much endlessly. This is a nice feature to simplify readability of the CSS rulesets. However, when excessive nesting is used it can actually cause the opposite to happen - become more unreadable then before.

Try to keep nesting levels between 0-5 levels of the start, with the occasional exception. In not a single place your CSS will need more than 7 levels of nesting, if it occurs you should consider refactoring your CSS.

sasswide760.container {
background: red;
.wrapper {
padding: 25px;
.header {
margin-bottom: 5px;
.title {
background: white;
padding: 15px 10px;
.buttons {
&.left {
margin-right: 10px;
}
button.button {
.subtitle {
font-size: 13px;
i {
margin-left: unset;
}
}
}
}
}
}
}
}wide760.container {
background: red;
.wrapper {
padding: 25px;
}
.header {
margin-bottom: 5px;
}
}
.title {
background: white;
padding: 15px 10px;
.buttons {
&.left {
margin-right: 10px;
}
.button .subtitle {
font-size: 13px;
i {
margin-left: unset;
}
}
}
}

The benefit of this is that inside any potential media query you might need to use later on, specifying your specific ruleset becomes easier.

sasswide760@media only screen and (max-width: 1615px) {
.container .wrapper .header .title .buttons button.button .subtitle i {
margin-left: 10px;
}
}sasswide760@media only screen and (max-width: 1615px) {
.title .buttons .button .subtitle i {
margin-left: 10px;
}
}

## Use descriptive class names

Keep usage of non-descriptive class names such as `div`, `wrapper`, `container`, `button` to a minimum, unless you are defining project-wide class names which will be used throughout the project. Having 10 different `container` class names for each page does not make sense.

Instead, try to add a page/component specific name to the class name. For example: `button-wrapper`, `dashboard-container`, `approve-button`.

## Prefer class name selection

Instead of using a tag name selector such as `div`, `ul`, `li`, `span`, it is preferred to target a specific class name. This prevents any unwanted usage over default behaviour of a tag name.

sasswide760ul {
color: #fff;
}sasswide760.class-name {
color: #fff;
}

It is also preferred to not assign any rules to identifiers. Rules that use identifiers are not reusable, as there can be only one of such on a page.

sasswide760#my-element {
color: #fff;
}sasswide760.my-element {
color: #fff;
}

## Keep media queries out of specific component rulesets

Media queries are usually meaningless if they are not paired with rulesets about a single page. A component might be used in multiple places, therefore its size, its context and surrounding elements can change.

It is preferred to put media queries inside rulesets that target a specific page in your application. This makes it easier to search for the media query that targets the component, and prevents any unwanted side-effects to occur.

`Component.scss`

sasswide760@media screen and (max-width: 1000px) {
.my-page {
.component {
width: 250px;
}
}
.my-other-page {
.component {
width: 350px;
}
}
}

`MyPage.scss`

sasswide760@media screen and (max-width: 1000px) {
.my-page {
.component {
width: 250px;
}
}
}

`MyOtherPage.scss`

sasswide760@media screen and (max-width: 1000px) {
.my-other-page {
.component {
width: 350px;
}
}
}

While possible to nest media queries inside regular CSS usage, it is not recommended. As screen size changes, in 99% of the cases there are multiple changes to be made. This would result in multiple of the same media queries to be inside multiple places in a single file, preventing ease of readability and adjustability.

sasswide760.component {
color: rgb(0,0,0);
background-color: rgba(244, 244, 200, 0.8);
padding-top: 25px;
margin-bottom: 5px;
font-size: 13px;
.sub-component {
.button {
.icon {
@media screen and (max-width: 1000px) {
font-size: 13px;
}
}
}
}
}sasswide760.component {
color: rgb(0,0,0);
background-color: rgba(244, 244, 200, 0.8);
padding-top: 25px;
margin-bottom: 5px;
font-size: 13px;
}
@media screen and (max-width: 1000px) {
.component .sub-component .button .icon {
font-size: 13px;
}
}

## Prefer to use variables

It is very much recommended to place frequently used parameters such as colours, padding/margin sizes, font styles, font sizes inside of a variables file for easy access. This also allows you to quickly change the look of your whole project by editing a couple variables. Nearly any variable can be placed in such a file, so please do!

Common styles should be used if they are available to you in the included style variables.

`Component.scss`

sasswide760.component {
color: rgb(0,0,0);
background-color: rgba(244, 244, 200, 0.8);
padding-top: 25px;
margin-bottom: 5px;
font-size: 13px;
}
.component-2 {
color: rgb(0,0,0);
padding: 5px;
font-size: 13px;
}

`Component.scss`

sasswide760.component {
color: $color-text;
background-color: $color-background;
padding-top: $spaces-large;
margin-bottom: $spaces-small;
font-size: $font-size-normal;
}
.component-2 {
color: $color-text;
padding: $spaces-small;
font-size: $font-size-normal;
}

`variables.scss`

sasswide760$color-text: rgb(0,0,0);
$color-background: rgba(244, 244, 200, 0.8);
$spaces-large: 25px;
$spaces-small: 5px;
$font-size-normal: 13px;

## Avoid !important

Unless you have no other option (i.e. another library controls the styling), you should avoid the usage of `!important` in any CSS file. It is a symptom of badly organised CSS.

## Styled components

We do not use any styled components, unless we have them because of “legacy” code or in an experimental codebase.

## Inline styling

Unless you have to control something using JS, you do not need to put your styling inside the JS file. Use CSS and SASS files for your styling at all times.