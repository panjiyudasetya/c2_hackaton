---
id: confluence:181403691
source: confluence
type: page
space: TC
title: TypeScript style guide
author: Damon Asberg
date: '2025-12-10'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/181403691
explicit_links:
- jira:UTF-8
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/181403691
---
# TypeScript style guide

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/181403691  

## Content

This guide is mostly based on the Google TypeScript code styling guide. <https://google.github.io/styleguide/tsguide.html>

These styling guidelines apply to all types of TypeScript files, whether that is `.ts`, `.tsx` or `.d.ts` (`.d.ts` file usage should be avoided)

### Semicolon usage

Even though this is a guideline, we do not use semicolons inside our TypeScript files to mark line endings.

This does not mean you cannot use them at all, there are some situations where it is approved to use them:

#### Single line type objects

To indicate multiple properties on a single line for a type definition, separation using a semicolon is allowed:

typescriptwide760type RandomObjectType = { type: 'SET\_ACTION'; userProfile: UserProfile | null }
export interface Settings {
defaultSetting?: number
overwrittenSubSettings?: { [key: string]: { port: SFPort; value: number } }
}
export function sortVisitsPerShip(
visits: IGenericVisitType[]
): { vesselId: string; visits: IGenericVisitType[] }[] {
...
}

#### Inside for loops

Preferably to iterate over containers like arrays, `forEach` or `map` is used. But for loops are technically allowed with semicolons inside of the for loop initialisation:

typescriptwide760for (let i = 0; i < someArr.length; i++) {
...
}

## Syntax

### Identifiers

Identifiers must only use ASCII letters, digits or underscores to allow compatibility with the compiler.

| **Style** | **Category** | **Example** |
| --- | --- | --- |
| `UpperCamelCase` | File names for React pages or components, React components, class names, interface / type / enum names | `MobileESofEstimateTimes.tsx`  `const DashboardPage = ...`  `interface SubscriptionMetadataResponse {` |
| `lowerCamelCase` | variables, parameters, function names, methods, properties | `getAllPossibleAccessors(...`  `entry.locationData.latitude` |
| `SCREAMING_SNAKE_CASE` | Global constant values (usually everything inside a `constants.ts` file) | `const BACKEND_URL = "https://...`  `const DATE_FORMAT_SHORT_DAY_FIRST = 'd MMM'` |

### Abbreviations

There are 2 methods which we use in projects. The preferred method is to abide to regular capitalisation even when there are abbreviations in the function name. Unless it is required by types outside of your control (e.g. pre-existing NodeJS types).

1. `formatIsoToInputDateFormat`, `getEtaFromTimestamps`, `loadXmlHttpRequest`

However, in some projects you might notice that abbreviations are capitalised for clarity:

* `formatISOToInputDateFormat`, `getETAFromTimestamps`, `loadXMLHTTPRequest`

### Type parameters

Type parameters in generic types like in `Array<T>`, should be treated with a single upper case letter or with `UpperCamelCase` just like any other type or interface is.

### Prefix/suffix

For non-class based code, identifiers should not use `_` as a prefix or a suffix. Meaning `_` should also not be used as an identifier by itself, to for example indicate something is unused.

Tip: If you only need some of the elements from an array (or TypeScript tuple), you can insert extra commas in a destructuring statement to ignore in-between elements:

typescriptwide760const [a, , b] = [1, 5, 10] // a <- 1, b <- 10

### Constants

Any variable using `CONSTANT_CASE` indicates that the variable is immutable and should not be changed. This does not mean that the variable is actually immutable (because JS…)

### Naming style

Names of types should not have information inside the name that is already included or implied with the type name.

Examples

* Do not use trailing or leading underscores for private properties or methods
* Do not use any prefix for optional parameters - like `opt_`

  + We can indicate these with `parameter?: string`
* Do not mark interfaces or types specifically. Give interfaces a name which expresses why it exists in the first place

  + `IMyObjectInterface`, `MyNewObjectType`
  + `class UserProfilePage`, `interface UserProfile`

### Descriptive names

* Names must be descriptive and clear to a new reader
* Prevent usage of abbreviations that are ambiguous or unfamiliar to readers outside the project
* Do not abbreviate by deleting letters within a word
* Prevent usage of single letter variable names as much as possible

  + With exceptions when the letter clearly implies the usage, such as using `x` or `y` when talking about a `x` or `y` position, or `i` in case of the index.

Examples

|  |  |
| --- | --- |
| `format(x: string[], y: string) {` | `formatCompaniesInSingleLine(companyNames: string[], companyType: CompanyType) {` |
| `interface SFESOFPOCDelayInfo {` | `interface SmartFleetEsofDelayInfoProofOfConcept {` |
| `agencies.map((x, i) => ...` | `agencies.map((agency, i) => ...` |

### File encoding

UTF-8

### No line continuations

Do not use *line continuations* (that is, ending a line inside a string literal with a backslash) in either ordinary or template string literals. Even though ES5 allows this, it can lead to tricky errors if any trailing whitespace comes after the slash, and is less obvious to readers.

Disallowed

typescriptwide760const LONG\_STRING = 'This is a very long string that far exceeds the 80 \
column limit. It unfortunately contains long stretches of spaces due \
to how the continued lines are indented.'

Allowed

typescriptwide760const LONG\_STRING = 'This is a very long string that far exceeds the 80 ' +
'column limit. It does not contain long stretches of spaces since ' +
'the concatenated strings are cleaner.'

### Comments & Documentation

There are 2 types of comments in TypeScript:

* // Inline code comments

  Use these comments for implementation comments, i.e. comments that only concern the implementation of the code itself.
* /\*\* JSDoc comments \*/

  Use these comments for documentation, i.e. comments a user of the code should read.

#### Omit comments that are redundant with TypeScript

For example, do not declare types in `@param` or `@return` blocks, do not write `@implements`, `@enum`, `@private`, `@override` etc. on code that uses the `implements`, `enum`, `private`, `override` etc. keywords.

#### Make comments that actually add information

Sometimes the name and type of the function or parameter is enough. Code will *usually* benefit from more documentation than just variable names.

* Avoid comments that restate the parameter name and type

  typescript/\*\* @param fooBarService The Bar service for the Foo application. \*/

## Language rules

### Visibility

Restricting visibility of properties, methods and entire types helps with keeping code decoupled.

* Limit symbol visibility as much as possible
* Consider converting private methods to non-exported functions within the same file but outside of any class, and moving private properties into a separate, non-exported class.
* TypeScript symbols are public by default. Never use the `public` modifier except when declaring non-readonly public parameter properties (in constructors).

  typescriptclass Foo {
  public bar = new Bar() // BAD: public modifier not needed
  constructor(public readonly baz: Baz) {} // BAD: readonly implies it's a property which defaults to public
  }class Foo {
  bar = new Bar() // GOOD: public modifier not needed
  constructor(public baz: Baz) {} // public modifier allowed
  }

### Constructors

Constructor calls *must* use parentheses, even when no arguments are passed:

typescriptwide760const x = new Footypescriptwide760const x = new Foo()

It is unnecessary to provide an empty constructor. In case a constructor with parameter properties, visibility modifiers or parameter decorators is provided it should not be omitted, even if the body of the constructor is empty.

typescriptwide760class UnnecessaryConstructor {
constructor() {}
}
class UnnecessaryConstructorOverride extends Base {
constructor(value: number) {
super(value)
}
}typescriptwide760class DefaultConstructor {
}
class ParameterProperties {
constructor(private myService) {}
}
class ParameterDecorators {
constructor(@SideEffectDecorator myService) {}
}
class NoInstantiation {
private constructor() {}
}

### Class members

#### No `#private` fields

Do not use private fields / private identifiers.

typescriptwide760class Clazz {
#ident = 1
}typescriptwide760class Clazz {
private ident = 1
}

#### Use `readonly`

Mark properties that are never reassigned outside of the constructor with the `readonly` modifier (these need not be deeply immutable).

#### Field initialisers

If a class member is not a parameter, initialise it where it's declared, which sometimes lets you drop the constructor entirely.

typescriptwide760class Foo {
private readonly userList: string[]
constructor() {
this.userList = []
}
}typescriptwide760class Foo {
private readonly userList: string[] = []
}

### Primitive types & wrapper classes

TypeScript code *must not* instantiate the wrapper classes for the primitive types `String`, `Boolean`, and `Number`. Wrapper classes have surprising behavior, such as `new Boolean(false)` evaluating to `true`.

typescriptwide760const s = new String('hello')
const b = new Boolean(false)
const n = new Number(5)typescriptwide760const s = 'hello'
const b = false
const n = 5

### Types

This also applies when using types:

typescriptwide760interface MyInterface {
property: String
anotherProperty: Number
}
type MyVeryCoolType = Numbertypescriptwide760interface MyInterface {
property: string
anotherProperty: number
}
type MyVeryCoolType = number

### Array constructor

TypeScript code *must not* use the `Array()` constructor, with or without `new`. It has confusing and contradictory usage:

typescriptwide760const a = new Array(2) // [undefined, undefined]
const b = new Array(2, 3) // [2, 3]

Instead, always use bracket notation to initialise arrays, or `from` to initialise an `Array` with a certain size:

typescriptwide760const a = [2]
const b = [2, 3]
// Equivalent to Array(2):
const c = []
c.length = 2
// [0, 0, 0, 0, 0]
Array.from<number>({length: 5}).fill(0)

### Type coercion

Do not use `String()` and `Boolean()` (note: no `new`!) functions, string template literals, or `!!` to coerce types. Even though TypeScript allows you to.

typescriptwide760const bool = Boolean(false)
const str = String(aNumber)
const bool2 = !!str
const str2 = `result: ${bool2}`

---

Code *must not* use unary plus (`+`) to coerce strings to numbers. Parsing numbers can fail, has surprising corner cases, and can be a code smell (parsing at the wrong layer). A unary plus is too easy to miss in code reviews given this.

It is also bad practice in general due to it not being an explicit type conversion like `parseInt` and being unclear due to the short description.

typescriptwide760const x = +y

---

Code also *must not* use `parseInt` or `parseFloat` to parse numbers, except for non-base-10 strings (see below). Both of those functions ignore trailing characters in the string, which can shadow error conditions (e.g. parsing `12 dwarves` as `12`).

typescriptwide760const n = parseInt(someString, 10) // Error prone,
const f = parseFloat(someString) // regardless of passing a radix.typescriptwide760const n = Number(someString)

---

#### Implicit coercion

Do not use explicit boolean coercions in conditional clauses that have implicit boolean coercion. Those are the conditions in an `if`, `for` and `while` statements.

typescriptwide760const foo: MyInterface|null = ...
if (!!foo) {...}
while (!!foo) {...}typescriptwide760const foo: MyInterface|null = ...
if (foo) {...}
while (foo) {...}typescriptwide760// Explicitly comparing > 0 is OK:
if (arr.length > 0) {...}
// so is relying on boolean coercion:
if (arr.length) {...}

### Variables

Always use `const` or `let` to declare variables. Use `const` by default, unless a variable needs to be reassigned. Never use `var`.

wide760const foo = otherValue // Use if "foo" never changes.
let bar = someValue // Use if "bar" is ever assigned into later on.

`const` and `let` are block scoped, like variables in most other languages. `var` in JavaScript is function scoped, which can cause difficult to understand bugs. Don't use it.

wide760var foo = someValue // Don't use - var scoping is complex and causes bugs.

Variables *must not* be used before their declaration.

### Exceptions

#### Instantiate Errors using new

Always use `new Error()` when instantiating exceptions, instead of just calling `Error()`. Both forms create a new `Error` instance, but using `new` is more consistent with how other objects are instantiated.

wide760throw new Error('Foo is not a valid bar.')wide760throw Error('Foo is not a valid bar.')

#### Only throw Errors

JavaScript (and thus TypeScript) allow throwing arbitrary values. However if the thrown value is not an `Error`, it does not get a stack trace filled in, making debugging hard.

wide760// bad: does not get a stack trace.
throw 'oh noes!'

Instead, only throw (subclasses of) `Error`:

wide760// Throw only Errors
throw new Error('oh noes!')
// ... or subtypes of Error.
class MyError extends Error {}
throw new MyError('my oh noes!')

#### Catching & rethrowing

When catching errors, code *should* assume that all thrown errors are instances of `Error`.

typescriptwide760try {
doSomething()
} catch (e: unknown) {
// All thrown errors must be Error subtypes. Do not handle
// other possible values unless you know they are thrown.
assert(e, isInstanceOf(Error))
displayError(e.message)
// or rethrow:
throw e
}

Exception handlers *must not* defensively handle non-`Error` types unless the called API is conclusively known to throw non-`Error`s in violation of the above rule. In that case, a comment should be included to specifically identify where the non-`Error`s originate.

wide760try {
badApiThrowingStrings()
} catch (e: unknown) {
// Note: bad API throws strings instead of errors.
if (typeof e === 'string') { ... }
}

Why?

Avoid [overly defensive programming](https://en.wikipedia.org/wiki/Defensive_programming#Offensive_programming). Repeating the same defenses against a problem that will not exist in most code leads to boiler-plate code that is not useful.

### Iterating objects

Iterating objects with `for (... in ...)` is error prone. It will include enumerable properties from the prototype chain.

Do not use unfiltered `for (... in ...)` statements:

typescriptwide760for (const x in someObj) {
// x could come from some parent prototype!
}

Either filter values explicitly with an `if` statement, or use `for (... of Object.keys(...))`.

typescriptwide760for (const x in someObj) {
if (!someObj.hasOwnProperty(x)) continue
// now x was definitely defined on someObj
}
for (const x of Object.keys(someObj)) { // note: for \_of\_!
// now x was definitely defined on someObj
}
for (const [key, value] of Object.entries(someObj)) { // note: for \_of\_!
// now key was definitely defined on someObj
}

### Iterating arrays

Do not use `for (... in ...)` to iterate over arrays. It will counterintuitively give the array's indices (as strings!), not values:

typescriptwide760for (const x in someArray) {
// x is the index!
}

Prefer `for (... of someArr)` to iterate over arrays. `Array.prototype.forEach` and vanilla `for` loops are also allowed:

typescriptwide760for (const x of someArr) {
// x is a value of someArr.
}
for (let i = 0; i < someArr.length; i++) {
// Explicitly count if the index is needed, otherwise use the for/of form.
const x = someArr[i]
// ...
}
for (const [i, x] of someArr.entries()) {
// Alternative version of the above.
}

### Using the spread operator

Using the spread operator `[...foo]; {...bar}` is a convenient shorthand for copying arrays and objects. When using the spread operator on objects, later values replace earlier values at the same key.

typescriptwide760const foo = {
num: 1,
}
const foo2 = {
...foo,
num: 5,
}
const foo3 = {
num: 5,
...foo,
}
foo2.num === 5
foo3.num === 1

When using the spread operator, the value being spread *must* match what is being created. That is, when creating an object, only objects may be used with the spread operator; when creating an array, only spread iterables. Primitives, including `null` and `undefined`, *must not* be spread.

typescriptwide760const foo = {num: 7}
const bar = {num: 5, ...(shouldUseFoo && foo)} // might be undefined
// Creates {0: 'a', 1: 'b', 2: 'c'} but has no length
const fooStrings = ['a', 'b', 'c']
const ids = {...fooStrings}typescriptwide760const foo = shouldUseFoo ? {num: 7} : {}
const bar = {num: 5, ...foo}
const fooStrings = ['a', 'b', 'c']
const ids = [...fooStrings, 'd', 'e']

### Control flow statements & blocks

Control flow statements must always use blocks for the containing code. With exceptions for one line returns.

typescriptwide760for (let i = 0; i < x; i++) {
doSomethingWith(i)
}
if (x) {
doSomethingWithALongMethodNameThatForcesANewLine(x)
}
if (user.drunk) return
if (user.drunk) {
return
}typescriptwide760if (x) x.doFoo()
if (x)
doSomethingWithALongMethodNameThatForcesANewLine(x)
for (let i = 0; i < x; i++) doSomethingWith(i)

#### Assignment in control statements

Prefer to avoid assignment of variables inside control statements. Assignment can be easily mistaken for equality checks inside control statements.

typescriptwide760if (x = someFunction()) {
// Assignment easily mistaken with equality check
// ...
}typescriptwide760x = someFunction()
if (x) {
// ...
}

n cases where assignment inside the control statement is preferred, enclose the assignment in additional parenthesis to indicate it is intentional.

typescriptwide760while ((x = someFunction())) {
// Double parenthesis shows assignment is intentional
// ...
}

### Switch statements

All `switch` statements *must* contain a `default` statement group, even if it contains no code.

wide760switch (x) {
case Y:
doSomethingElse()
break
default:
// nothing to do.
}

Non-empty statement groups (`case ...`) *must not* fall through (enforced by the compiler):

wide760switch (x) {
case X:
doSomething()
// fall through - not allowed!
case Y:
// ...
}

Empty statement groups are allowed to fall through:

wide760switch (x) {
case X:
case Y:
doSomething()
break
default: // nothing to do.
}

In cases where there is a lot of code inside a single switch statement group, it is preferably grouped using braces as such:

wide760switch (x) {
case X:
case Y: {
doSomething()
break
}
default: // nothing to do.
}

### Equality Checks

Always use triple equals (`===`) and not equals (`!==`). The double equality operators cause error prone type coercions that are hard to understand and slower to implement for JavaScript Virtual Machines. See also the [JavaScript equality table](https://dorey.github.io/JavaScript-Equality-Table/).

typescriptwide760if (foo == 'bar' || baz != bam) {
// Hard to understand behaviour due to type coercion.
}typescriptwide760if (foo === 'bar' || baz !== bam) {
// All good here.
}

**Exception**: Comparisons to the literal `null` value *may* use the `==` and `!=` operators to cover both `null` and `undefined` values.

typescriptwide760if (foo == null) {
// Will trigger when foo is null or undefined.
}

### Function expressions

#### Use arrow functions in expressions

Always use arrow functions instead of pre-ES6 function expressions defined with the `function` keyword.

typescriptwide760bar(() => { this.doSomething() })typescriptwide760bar(function () { ... })

#### Expression bodies vs block bodies

Use arrow functions with expressions or blocks as their body as appropriate.

typescriptwide760// Top level functions use function declarations.
function someFunction() {
// Block arrow function bodies, i.e. bodies with => { }, are fine:
const receipts = books.map((b: Book) => {
const receipt = payMoney(b.price)
recordTransaction(receipt)
return receipt
})
// Expression bodies are fine, too, if the return value is used:
const longThings = myValues.filter(v => v.length > 1000).map(v => String(v))
function payMoney(amount: number) {
// function declarations are fine, but don't access `this` in them.
}
// Nested arrow functions may be assigned to a const.
const computeTax = (amount: number) => amount \* 0.12
}

### @ts-ignore

Do not use `@ts-ignore` nor variants `@ts-expect-error` or `@ts-nocheck`. They superficially seem to be an easy way to fix a compiler error, but in practice, a specific compiler error is often caused by a larger problem that can be fixed more directly.

For example, if you are using `@ts-ignore` to suppress a type error, then it's hard to predict what types the surrounding code will end up seeing. For many type errors, the advice in [how to best use](https://google.github.io/styleguide/tsguide.html#any) `any` is useful.

### Type and Non-nullability Assertions

Type assertions (`x as SomeType`) and non-nullability assertions (`y!`) are unsafe. Both only silence the TypeScript compiler, but do not insert any runtime checks to match these assertions, so they can cause your program to crash at runtime.

Because of this, you *should not* use type and non-nullability assertions without an obvious or explicit reason for doing so.

Instead of the following:

typescriptwide760(x as Foo).foo()
y!.bar()

When you want to assert a type or non-nullability the best answer is to explicitly write a runtime check that performs that check.

typescriptwide760// assuming Foo is a class.
if (x instanceof Foo) {
x.foo()
}
if (y) {
y.bar()
}

Sometimes due to some local property of your code you can be sure that the assertion form is safe. In those situations, you *should* add clarification to explain why you are ok with the unsafe behavior:

wide760// x is a Foo, because ...
(x as Foo).foo()
// y cannot be null, because ...
y!.bar()

If the reasoning behind a type or non-nullability assertion is obvious, the comments *may* not be necessary. For example, generated proto code is always nullable, but perhaps it is well-known in the context of the code that certain fields are always provided by the backend. Use your judgement.

#### Type Assertions Syntax

Type assertions *must* use the `as` syntax (as opposed to the angle brackets syntax). This enforces parentheses around the assertion when accessing a member.

typescriptwide760const x = (<Foo>z).length
const y = <Foo>z.lengthtypescriptwide760// z must be Foo because ...
const x = (z as Foo).length

#### Type Assertions and Object Literals

Use type annotations (`: Foo`) instead of type assertions (`as Foo`) to specify the type of an object literal. This allows detecting refactoring bugs when the fields of an interface change over time.

typescriptwide760interface Foo {
bar: number
baz?: string // was "bam", but later renamed to "baz".
}
const foo = {
bar: 123,
bam: 'abc', // no error!
} as Foo
function func() {
return {
bar: 123,
bam: 'abc', // no error!
} as Foo
}typescriptwide760interface Foo {
bar: number
baz?: string
}
const foo: Foo = {
bar: 123,
bam: 'abc', // complains about "bam" not being defined on Foo.
}
function func(): Foo {
return {
bar: 123,
bam: 'abc', // complains about "bam" not being defined on Foo.
}
}

### Member property declarations

Interface and class declarations do not use a semicolon to separate individual member declarations. Instead, particular symbol has to be placed at the end of the declaration.

typescriptwide760interface Foo {
memberA: string;
memberB: number;
}typescriptwide760interface Foo {
memberA: string
memberB: number
}

With the sole exception being that in case type declaration fits into a single line, semicolons or comma’s must be used to separate individual member declarations. This is invalid for interfaces.

typescriptwide760const x = (propertyA: { firstProperty: string, secondProperty: number }): ReturnProperty => ...

#### Optimisation compatibility for property access

Code *should not* mix quoted property access with dotted property access unless it is unavoidable:

wide760// Bad: code must use either non-quoted or quoted access for any property
// consistently across the entire application:
console.log(x['someField'])
console.log(x.someField)

In unavoidable cases like having a generic lookup with keys, the quoted access is allowed.

wide760console.log(x["hello.world"])

### Debugger statements

Debugger statements *must not* be included in production code. This includes console statements, except `console.error()`.

typescriptwide760function debugMe() {
debugger
}
console.log("test")
console.trace()

## Source organisation

### Imports

TypeScript code *must* use paths to import other TypeScript code. Paths *may* be relative, i.e. starting with `.` or `..`, or rooted at the base directory, e.g. `root/path/to/file`.

Code *should* use relative imports (`./foo`) rather than absolute imports `path/to/foo` when referring to files within the same (logical) project as this allows to move the project around without introducing changes in these imports. There is a recommendation to configure the `src` folder as the default import inside `tsconfig.json`:

wide760"compilerOptions": {
...
"paths": {
"@/\*": ["./src/\*"]
},
}

Consider limiting the number of parent steps (`../../../`) as those can make module and path structures hard to understand - unless unavoidable.

wide760import {Symbol1} from 'path/from/root'
import {Symbol2} from '../parent/file'
import {Symbol3} from './sibling'

#### Extensions

File extensions of other TypeScript files should not be shown inside imports. Other types of files such as CSS, SCSS, SVG, PNG are allowed.

`import Component from '../../../component/Component'`

`import './Component.scss'`

`import Component from '../../../component/Component.tsx'`

#### Sorting/ordering

* Imports should be grouped together by type
* Imports should preferably be sorted alphabetically within each category and if there are multiple imports from a single file, within those as well

The order of import should be as follows:

1. Imports from libraries
2. Local component imports
3. Local function imports
4. Any other imports
5. CSS / SCSS files

This will result in something along the lines of:

typescriptwide760import { format } from 'date-fns'
import { groupBy } from 'lodash'
import React from 'react'
import { I18n } from 'react-redux-i18n'
import APIService from '../../api/APIService'
import DashboardPage from '../../pages/DashboardPage/DashboardPage'
import DateTimePicker from '../../components/DateTimePicker/DateTimePicker'
import { formatDataStructure } from '../../utils/general'
import { BACKEND\_URL } from '../../utils/constants'
import
import VeryCoolImage from '../../../images/VeryCoolImage.png'
import './Page.scss'
const Page = ({ }: IProps) => {
...

### Exports

Both named and default exports may be used throughout the project.

For React Components, we use a default export at the bottom of the page. This is in order to make sure one 1 item is exported from the file itself.

There are some bad practices which you should avoid.

Do not directly export anything directly from the top of a file

typescriptwide760export default () => {
return (
<div className="my-react-component">hello world</div>
)
}

Assign it to a variable first

typescriptwide760const ReactComponent = () => {
return (
<div className="my-react-component">hello world</div>
)
}
export default ReactComponent

Prevent putting any code underneath the export statement. Move it above the export statement.

typescriptwide760const ReactComponent = () => {
...
}
export default ReactComponent
const x = 10
function manipulateX() {
...
}

Prevent mixing default and named exports in a single file. Move any **generic** function that needs to be exported alongside a component to a utilities file. Regular functions which are only related to the component itself can be next to the exported function.

wide760const ReactComponent = () => {
...
}
export function manipulateDataEntries() {
...
}
export default ReactComponent

#### Renaming imports

Code *should* fix name collisions by using a module import or renaming the exports themselves. Code *may* rename imports (`import {SomeThing as SomeOtherThing}`) if needed.

Three examples where renaming can be helpful:

1. If it's necessary to avoid collisions with other imported symbols.
2. If the imported symbol name is generated.
3. If importing symbols whose names are unclear by themselves, renaming can improve code clarity.

#### Import & export type

Do not use `import type {...}` or `export type {...}`.

wide760import type {Foo}
export type {Bar}
export type {Bar} from './bar'

Instead, just use regular imports and exports:

wide760import {Foo} from './foo'
export {Bar} from './bar'

## Type System

### Type Inference

Code *may* rely on type inference as implemented by the TypeScript compiler for all type expressions (variables, fields, return types, etc).

typescriptwide760const x = 15 // Type inferredtypescriptwide760// Bad: 'Set' is trivially inferred from the initialization
const x: Set<string> = new Set()typescriptwide760const x = new Set<string>()

For more complex expressions, type annotations can help with readability of the program:

typescriptwide760// Hard to reason about the type of 'value' without an annotation.
const value = await rpc.getSomeValue().transform()

With additional type annotations, the readability has improved:

typescriptwide760// Can tell the type of 'value' at a glance.
const value: string[] = await rpc.getSomeValue().transform()

Whether an annotation is requiredimport is decided by the code reviewer.

### Return types

Whether to include return type annotations for functions and methods is up to the code author.

### null vs undefined

TypeScript supports `null` and `undefined` types. Nullable types can be constructed as a union type (`string|null`); similarly with `undefined`. There is no special syntax for unions of `null` and `undefined`.

TypeScript code can use either `undefined` or `null` to denote absence of a value, there is no general guidance to prefer one over the other. Many JavaScript APIs use `undefined` (e.g. `Map.get`), while many DOM and some APIs use `null`, so the appropriate absent value depends on the context.

#### Optionals vs `| undefined` type

In TypeScript there are 2 methods to indicate a parameter could be undefined **or** optional.

typescriptwide760interface FilterValues {
searchQuery: string
fromDate: string | undefined
toDate: string | undefined
}
// Valid values:
const x: FilterValues = { searchQuery: "hello world", fromDate: undefined, toDate: undefined }
const y: FilterValues = { searchQuery: "hello world", fromDate: "2023-05-10", toDate: undefined }
// Invalid:
const x: FilterValues = { searchQuery: "hello world", fromDate: undefined } // toDate has to be stated, even if its value would be undefined

This example states that all values, including `fromDate` and `toDate`, must always be provided for even if their provided value is `undefined`. This can for example be handy if you are adding new props to an existing component, and want to check if all implementations of the component use the new prop.

typescriptwide760interface FilterValues {
searchQuery: string
fromDate?: string
toDate?: string
}
// Valid values:
const a: FilterValues = { searchQuery: "hello world", fromDate: undefined, toDate: undefined }
const b: FilterValues = { searchQuery: "hello world", toDate: undefined }
const c: FilterValues = { searchQuery: "hello world" }
const d: FilterValues = { searchQuery: "hello world", fromDate: "2023-05-10", toDate: undefined }

This example states that only `searchQuery` needs to be provided, and the values of `fromDate` and `toDate` are optional values that could be omitted altogether from the object.

Both of these implementations can be correct, depending on the implementation.

### Structural Types vs Nominal Types

TypeScript's type system is structural, not nominal. That is, a value matches a type if it has at least all the properties the type requires and the properties' types match, recursively.

Use structural typing where appropriate in your code. Outside of test code, use interfaces to define structural types, not classes. In test code it can be useful to have mock implementations structurally match the code under test without introducing an extra interface.

When providing a structural-based implementation, explicitly include the type at the declaration of the symbol (this allows more precise type checking and error reporting).

typescriptwide760const foo: Foo = {
a: 123,
b: 'abc'
}typescriptwide760const badFoo = {
a: 123,
b: 'abc'
}

Why?

The badFoo object above relies on type inference. Additional fields could be added to badFoo and the type is inferred based on the object itself.

When passing a badFoo to a function that takes a Foo, the error will be at the function call site, rather than at the object declaration site. This is also useful when changing the surface of an interface across broad codebases.

typescriptwide760type Animal = {
sound: string
name: string
}
function makeSound(animal: Animal) {}
/\*\*
\* 'cat' has an inferred type of '{sound: string}'
\*/
const cat = {
sound: 'meow',
}
/\*\*
\* 'cat' does not meet the type contract required for the function, so the
\* TypeScript compiler errors here, which may be very far from where 'cat' is
\* defined.
\*/
makeSound(cat)
/\*\*
\* Horse has a structural type and the type error shows here rather than the
\* function call. 'horse' does not meet the type contract of 'Animal'.
\*/
const horse: Animal = {
sound: 'niegh',
}
const dog: Animal = {
sound: 'bark',
name: 'MrPickles',
}
makeSound(dog)
makeSound(horse)

### Interfaces vs Type Aliases

TypeScript supports [type aliases](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#type-aliases) for naming a type expression. This can be used to name primitives, unions, tuples, and any other types.

There is a strong preference for using `type` over `interface` for every declaration you use. See Why Use Type and not Interface in Typescript. Both `type` and `interface` are pretty much equal in usage.

### `Array<T>` or `T[]`

Both types have their purpose, for simple types the `T[]` notation should be used, and for anything which is more complex than that the `Array<T>` notation should be used. In doubt, make sure it is consistent with whatever is being done already in the project.

typescriptwide760const a: string[] = []
const b: Array<string | number> = []
const c: MyInterfaceType[] = []
const d: Array<GenericFunctionType<NewGenericType, GenericReturn>> = []typescriptwide760const a: Array<string> = []
const b: (string | number)[] = []
const c: Array<MyInterfaceType> = []
const d: (GenericFunctionType<NewGenericType, GenericReturn>)[] = []

### Indexable Types / index signatures (`{[key: string]: T}`)

Provide a meaningful label for the key, it is only used for documentation and unused otherwise

wide760const users: {[key: string]: number} = ...wide760const users: {[userName: string]: number} = ...
const dogs: Record<string, number> = ...

### `any` Type

TypeScript's `any` type is a super and subtype of all other types, and allows dereferencing all properties. As such, `any` is dangerous - it can mask severe programming errors, and its use undermines the value of having static types in the first place.

**Consider** ***not*** **to use** `any`. In circumstances where you want to use `any`, consider one of:

* Provide a more specific type
* Use `unknown`
* Suppress the lint warning and document why

#### Using `unknown` over `any`

The `any` type allows assignment into any other type and dereferencing any property off it. Often this behaviour is not necessary or desirable, and code just needs to express that a type is unknown. Use the built-in type `unknown` in that situation — it expresses the concept and is much safer as it does not allow dereferencing arbitrary properties.

typescriptwide760// Can assign any value (including null or undefined) into this but cannot
// use it without narrowing the type or casting.
const val: unknown = valuetypescriptwide760const danger: any = value /\* result of an arbitrary expression \*/
danger.whoops() // This access is completely unchecked!

To safely use `unknown` values, narrow the type using a type guard.

#### Suppressing `any` lint warnings

Sometimes using `any` is legitimate, for example in tests to construct a mock object. In such cases, add a comment that suppresses the lint warning, and document why it is legitimate.

typescriptwide760// This test only needs a partial implementation of BookService, and if
// we overlooked something the test will fail in an obvious way.
// This is an intentionally unsafe partial mock
// tslint:disable-next-line:no-any
const mockBookService = ({get() { return mockBook; }} as any) as BookService;
// Shopping cart is not used in this test
// tslint:disable-next-line:no-any
const component = new MyComponent(mockBookService, /\* unused ShoppingCart \*/ null as any);

### Wrapper types

There are a few types related to JavaScript primitives that *should not* ever be used:

* `String`, `Boolean`, and `Number` have slightly different meaning from the corresponding primitive types `string`, `boolean`, and `number`. Always use the lowercase version.
* `Object` has similarities to both `{}` and `object`, but is slightly looser. Use `{}` for a type that include everything except `null` and `undefined`, or lowercase `object` to further exclude the other primitive types (the three mentioned above, plus `symbol` and `bigint`).

Further, never invoke the wrapper types as constructors (with `new`).

## Consistency

For any style question that isn't settled definitively by this specification, do what the other code in the same file is already doing (be consistent). If that doesn't resolve the question, consider emulating the other files in the same directory or in the same project.

### Goals

1. **Code should avoid patterns that are known to cause problems, especially for users new to the language.**

   Examples:

   * The `any` type is easy to misuse (is that variable *really* both a number and callable as a function?), so we have recommendations for how to use it.
   * Periods within filenames make them ugly/confusing to import from JavaScript.
   * Static functions in classes optimise confusingly, while often file-level functions accomplish the same goal.
   * Users unaware of the `private` keyword will attempt to obfuscate their function names with underscores.
2. **Code across projects should be consistent across irrelevant variations.**

   When there are two options that are equivalent in a superficial way, we should consider choosing one just so we don't divergently evolve for no reason and avoid pointless debates in code reviews.

   We should usually match JavaScript style as well, because people often write both languages together.

   Examples:

   * The capitalisation style of names.
   * `x as T` syntax vs the equivalent `<T>x` syntax (disallowed).
   * `Array<[number, number]>` vs `[number, number][]`.
3. **Code should be maintainable in the long term.**

   Code usually lives longer than the original author works on it, it will most likely be handed over from you to the successor of your successors successor, so it needs to be maintainable.
4. **Code reviewers should be focused on improving the quality of the code, not enforcing arbitrary rules.**

   If it's possible to implement your rule as an automated check that is often a good sign. This also supports principle 3.

   If it really just doesn't matter that much -- if it's an obscure corner of the language or if it avoids a bug that is unlikely to occur -- it's probably worth leaving out.