---
id: confluence:181370927
source: confluence
type: page
space: TC
title: React code style guide
author: Damon Asberg
date: '2025-11-03'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/181370927
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/181370927
---
# React code style guide

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/181370927  

## Content

This style guide was mostly based on Airbnb’s React/JSX style guide.

<https://airbnb.io/javascript/react/>

This guide is based on the standards that are currently in place in most of the projects used throughout Teqplay.

## Basic rules

* Only include **one** React component per file, unless they are stateless.
* Always use JSX syntax
* Do not use `React.createElement`, unless it is required by an external library.

## Class based or function based components

We prefer to use functional / stateless components as much as possible, only using class based components if we absolutely have to.

jsxwide760class Listing extends React.Component {
// ...
render() {
return <div>{this.state.hello}</div>
}
} jsxwide760const Listing = React.createClass({
// ...
render() {
return <div>{this.state.hello}</div>
}
})jsxwide760const Listing = () => {
const [hello, setHello] = useState<string>('hello')
return (
<div>{hello}</div>
)
)jsxwide760const Listing = ({ hello: string }) => (
<div>{hello}</div>
)

## Naming

#### Extensions

Use `.tsx` for React components. Use `.ts` if possible for utility files containing only functions.

#### Filename

Use PascalCase for filenames. For example: `ReservationCard.tsx`

#### Reference naming

Use PascalCase for React Components and camelCase for any instance of a React component.

jsxwide760import reservationCard from './ReservationCard'
const ReservationItem = <ReservationCard />jsxwide760import ReservationCard from './ReservationCard'
const reservationItem = <ReservationCard/>

#### Component naming

Use the filename as the component name. For example, `ReservationCard.tsx` should have a reference name of `ReservationCard`.

#### Props naming

Avoid using DOM component prop names for different purposes. This is to avoid misunderstanding the name of the prop vs what it actually does. `style` is used for inline styling, but if you create your own Component with a prop name `style` which does not adhere to the inline styling - it will cause confusion. Use another type of name for that.

jsxwide760<MyComponent style="fancy" />
<MyComponent className="fancy" />jsxwide760<MyComponent variant="fancy" />

#### useState naming

useState variables should have descriptive names, with the update function name being set + {variable name}

jsxwide760const [name, updateName] = useState("")jsxwide760const [name, setName] = useState("")

## Alignment

Follow the following alignment styles for JSX syntax.

eslint: `react/jsx-closing-bracket-location` `react/jsx-closing-tag-location`

jsxwide760<Foo superLongParam="bar"
anotherSuperLongParam="baz" />
// If it fits on one line, keep it on one line
<Foo
bar="bar"
/>jsxwide760<Foo
superLongParam="bar"
anotherSuperLongParam="baz"
/>
<Foo bar="bar" />
<Foo
superLongParam="bar"
anotherSuperLongParam="baz"
>
<Bar />
</Foo>

## Quote usage

Always use double quotes (`"`) for JSX attributes, but single quotes (`'`) for all other JS / TS.

eslint: `jsx-quotes`

jsxwide760<Foo bar='bar' />jsxwide760<Foo bar="bar" />

## Spacing

Always include a single space in your self-closing tag.

eslint: `no-multi-spaces`, `react/jsx-tag-spacing`

jsxwide760<Foo/>
<Foo />
<Foo
/>jsxwide760<Foo />

## Props

#### Casing

Always use camelCase for prop names

jsxwide760<Foo
UserName="hello"
phone\_number={0987654}
/>jsxwide760<Foo
userName="hello"
phoneNumber={0987654}
/>

#### Omit explicitly true values

jsxwide760<Foo
hidden={true}
/>jsxwide760<Foo
...
hidden
/>
<Foo hidden />

#### Avoid using an array index as `key` prop

<https://robinpokorny.medium.com/index-as-a-key-is-an-anti-pattern-e0349aece318>

jsxwide760{todos.map((todo, index) =>
<Todo
{...todo}
key={index}
/>
)}jsxwide760{todos.map(todo => (
<Todo
{...todo}
key={todo.id}
/>
))}

#### Component props interface

Props of a component should be inside of a `IProps` interface above the component.

jsxwide760const Component = (props: Proppies) => {
...
}
interface Proppies {
myProp: string
}jsxwide760interface IProps {
myProp: string
}
const Component = ({ myProp }: IProps) => {
...
}

#### Destructuring of props

Passing through props of a component can be done in multiple ways. There is a strong preference to deconstructing props instead of passing them all as `props` and calling them from `props.[propName]`.

An advantage for this is that some simple components could omit their `return` statement altogether. Another one is that `props.` can be removed throughout the code.

It is important to not mix the ways of passing props of a component, as this may cause confusion.

jsxwide760const Component = (props: IProps) => {
const { prop1, prop2 } = props
return (
<div>{prop1} and {prop2}</div>
)
}jsxwide760const Component = (props: IProps) => {
return (
<div>{props.prop1} and {props.prop2}</div>
)
}jsxwide760const Component = ({ prop1, prop2 }: IProps) => (
<div>{prop1} and {prop2}</div>
)

## Parentheses

Wrap JSX tags in parentheses when they span more than one line.

eslint: `react/jsx-wrap-multilines`

jsxwide760render() {
return <MyComponent variant="long body" foo="bar">
<MyChild />
</MyComponent>
}jsxwide760render() {
return (
<MyComponent variant="long body" foo="bar">
<MyChild />
</MyComponent>
)
}
// Good when single line
render() {
return <MyComponent>hello</MyComponent>
}

## Tags

#### Always self-close tags that have no children

eslint: `react/self-closing-comp`

jsxwide760<Foo variant="stuff"></Foo>jsxwide760<Foo variant="stuff" />

#### Multi-line closing

If your component has multi-line properties, close its tag on a new line.

eslint: `react/jsx-closing-bracket-location`

jsxwide760<Foo
bar="bar"
baz="baz" />jsxwide760<Foo
bar="bar"
baz="baz"
/>

## Conditional rendering

When using a shorthand for conditional rendering, prefer usage of a full ternary operator rather than using `&&`. Both options are permitted, but for safety you should opt for `? :`.

When a number is put on the left side of a && condition, and that number is 0 - it will be rendered as `0`. This should be avoided by making the left side of the && condition a boolean.

jsxwide760const authenticated = true
const newMessages = 0
return (
<div>
{authenticated && <p>You are logged in</p>}
{newMessages && <p>New messages: {newMessages}</p>}
</div>
)
// Will return:
<div>
<p>You are logged in</p>
0
</div>jsxwide760const authenticated = true
const newMessages = 0
return (
<div>
{authenticated && <p>You are logged in</p>}
{newMessages >= 0 && <p>New messages: {newMessages}</p>}
</div>
)
// Will return:
<div>
<p>You are logged in</p>
<p>New messages: 0</p>
</div>

## Inline styling

It is really not recommended to do. There are some cases you will need to do it:

* A library that is actively adjusting style properties (like `styled-components` or `react-spring`)
* Dynamic property values based upon JS calculations (e.g. adjusting color or height based on certain parameters)

  + When it is usable, please use class names to adjust the properties unless you can’t.

Any styling should be done using `className`’s and their specifications inside the CSS you provide. Unless you can’t.

## useEffect and hooks

Inside the flow of a React component, using hooks like useEffect make the component logic difficult to follow. If you do not have to use it, please do not use it. But if you have no other option, it is allowed.

typescriptwide760const component = () => {
[ keepState, setKeepState ] = useState(1)
useEffect(() => {
console.log("state changed")
}, [setKeepState])
return <button onClick={() => setKeepState(keepState + 1)}>Hello</button>
}typescriptwide760const component = () => {
[ keepState, setKeepState ] = useState(1)
function handleOnHelloClick(){
setKeepState(keepState + 1)
console.log("state changed")
}
return <button onClick={handleOnHelloClick}>Hello</button>
}

If you want to look at the previous state and edit the state based on that, make sure to do as follows as setting state is asynchronous:

wide760const component = () => {
useState [ keepState, setKeepState ] = useState(1)
function handleOnHelloClick(){
setKeepState(oldState => oldState + 1)
console.log("state changed")
}
return <button onClick={handleOnHelloClick}>Hello</button>
}

## Reserved words

Do not use any reserved words, such as `props`, `const` etc.