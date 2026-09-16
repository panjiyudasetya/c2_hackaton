---
id: confluence:1075118081
source: confluence
type: page
space: TC
title: Augment AI ruleset for FE guidelines
author: David Hansson
date: '2026-01-13'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1075118081
explicit_links:
- jira:UTF-8
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1075118081
---
# Augment AI ruleset for FE guidelines

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1075118081  

## Content

This ruleset if following the other pages that we have for Typescript, SASS, React  
  
**How to add?**  
Go to Augment > Settings > Rules & Guidelines

wide760For styling (CSS/SCSS):
• Use kebab-case for all class names.
• Avoid camelCase unless embedding data in a class name.
• Class names must be descriptive (e.g., dashboard-container, approve-button).
• Prefer class selectors over tag selectors (avoid div, span, ul, etc.).
• Do not use ID selectors (#element) for styling.
• Add one empty line between CSS rulesets to improve readability.
• Use consistent color formats (rgb, rgba, hsl, hex).
• Use consistent unit types (px, rem, em).
• Keep SCSS nesting between 0–5 levels; never exceed 7.
• Refactor overly nested selectors into separate rules.
• Media queries should NOT be nested inside component selectors.
• Place media queries in page-level or layout-level style files.
• Use variables for frequently used values (colors, spacing, font sizes, etc.).
• Use shared project variables whenever available.
• Avoid using !important unless overriding styles from an external library.
• Avoid styled-components unless in legacy or experimental code.
• Avoid inline styles unless dynamic JS values are required.
• Keep selectors simple, clear, and readable.
• Avoid duplicate generic class names unless they are truly global.
• Maintain consistent formatting and structure across all CSS/SCSS.
For React components:
• Only include one React component per file, unless additional components are stateless helpers.
• Always use JSX syntax.
• Do not use React.createElement unless required by an external library.
• Prefer functional/stateless components; use class-based components only if absolutely necessary.
• Use .tsx for React components and .ts for utility files.
• Use PascalCase for filenames (e.g., ReservationCard.tsx).
• Use PascalCase for component names; camelCase for instances.
• The filename should match the component name.
• Avoid reusing DOM prop names for unrelated purposes.
• useState variables should have descriptive names; update functions should be set + variable name (e.g., [name, setName]).
• Follow consistent JSX alignment; closing brackets for multi-line tags should be on a new line; single-line tags can remain inline.
• Use double quotes for JSX attributes; single quotes for JS/TS code.
• Include a single space in self-closing tags.
• Use camelCase for prop names.
• Omit explicitly true values (e.g., <Foo hidden /> instead of <Foo hidden={true} />).
• Do not use array indexes as key props; prefer unique identifiers.
• Component props should be defined in an TProps type above the component.
• Prefer destructuring props in the function signature rather than using props.[name].
• Wrap multi-line JSX in parentheses.
• Self-close tags that have no children.
• Close multi-line JSX tags on a new line.
• Prefer ternary operators (? :) over && for conditional rendering when the left-hand value may be 0 or falsy.
• Avoid inline styling unless dynamic values or a library requires it.
• Use hooks (useState, useEffect) only when necessary.
• When updating state based on previous state, always use the functional form: setState(prev => prev + 1).
• Do not use reserved words (e.g., props, const) for variable or prop names.
TypeScript Guidelines
General File Guidelines
• Apply rules to all TypeScript files: .ts, .tsx, .d.ts (avoid .d.ts usage)
• Use UTF-8 encoding
• Avoid line continuations in string literals
Semicolons
• Do not use semicolons to terminate lines in TypeScript files
• Exceptions:
• Single-line type objects (e.g., type Obj = { a: string; b: number })
• For loops (for (let i = 0; i < arr.length; i++))
Identifiers & Naming
• Only use ASCII letters, digits, or underscores
• UpperCamelCase: File names, React components, classes, interfaces, enums
• lowerCamelCase: Variables, function names, methods, properties
• SCREAMING\_SNAKE\_CASE: Global constants
• Avoid abbreviations unless widely known
• No \_ prefix or suffix for non-class code
• Descriptive names; avoid single-letter variables except for indices (i, x, y)
Constants
• Use CONSTANT\_CASE for immutable values
• Values marked as constant should not be reassigned
Comments & Documentation
• // for implementation-specific inline comments
• /\*\* \*/ JSDoc for user-facing documentation
• Do not duplicate type information in comments
Variables
• Use const by default; let only if reassignment is needed
• Never use var
• Do not use variables before declaration
Control Flow & Assignments
• Always use blocks for control statements (if, for, while), except single-line returns
• Avoid assignments inside control statements unless wrapped in parentheses
• switch statements require a default case
• Non-empty cases must not fall through
Equality & Comparisons
• Always use === and !==
• Exception: == null to check for null or undefined
Functions
• Prefer arrow functions over function keyword
• Top-level functions may use function declarations
• Expression bodies vs block bodies depending on complexity
• Avoid @ts-ignore, @ts-nocheck, @ts-expect-error
TypeScript Type Rules
• Prefer interfaces over type aliases for objects
• Use T[] for simple arrays; Array<T> for complex generics
• Avoid wrapper types: String, Boolean, Number, Object; use lowercase primitives
• Do not instantiate primitive wrappers with new
• Avoid any; use unknown or a specific type; document exceptions
• Type assertions (x as Foo) and non-null assertions (y!) only if necessary; prefer runtime checks
• Interface/class members: no semicolons; single-line exceptions allowed
• Structural typing is preferred; explicitly annotate objects when needed
• Optional properties: param?: Type vs param: Type | undefined
Classes & Constructors
• Do not use #private fields; use private
• Use readonly for properties not reassigned
• Initialize fields inline when possible
• Constructor calls must always include parentheses (new Foo())
• Empty constructors unnecessary unless for parameter properties or decorators
Type Coercion
• Do not use String(), Boolean(), !! for coercion
• Do not use unary + or parseInt/parseFloat for number conversion; use Number()
• Avoid explicit boolean coercion in conditionals; rely on implicit conversion
Loops & Iteration
• Avoid for ... in for arrays; use for ... of or forEach
• Object iteration: use Object.keys or Object.entries with for ... of
Spread Operator
• Only spread objects into objects, arrays into arrays
• Later values overwrite earlier values at the same key
• Do not spread primitives, null, or undefined
Imports & Exports
• Use relative imports (./, ../) within the project
• Do not include .ts or .tsx extensions in imports
• Group imports: libraries → local components → local functions → others → CSS/SCSS
• Sort imports alphabetically within groups
• Default export React components at the bottom; assign to variable first
• Do not mix default and named exports in the same file
• Use renaming (import { X as Y }) only when necessary
• Do not use import type or export type; prefer regular imports/exports
Debugger Statements
• Do not include debugger, console.log(), or console.trace() in production code
• console.error() is allowed
Consistency & Maintainability
• Follow existing patterns in the file/project for unresolved style questions
• Prioritize readability, maintainability, and long-term code quality