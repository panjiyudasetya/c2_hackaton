---
id: confluence:651722761
source: confluence
type: page
space: TC
title: Java Coding Standards
author: Richard van Klaveren
date: '2025-03-04'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/651722761
explicit_links:
- jira:UTF-8
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/651722761
---
# Java Coding Standards

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/651722761  

## Content

## 1. Introduction

This document serves as the definition of Teqplay's coding standards for source code in the Java Programming Language. We will follow [Java's official Code Convention](http://www.oracle.com/technetwork/java/javase/documentation/codeconvtoc-136057.html). The following chapters are either an emphasis on the points outlined in the official Code Conventions, or are things not explicitly handled in them (like chapter 6, *Programming Practices*).

You can find the IDE Code Formatters reflecting these rules [here](https://bitbucket.org/teqplay/teqplay-wiki/src/master/ide-code-formatters/)

## 2. Source file basics

### 2.1. Space characters

The only space chars used are in source files are:

* `0x20` (space char)
* `\n` (line feed)
* `\r` (carriage return)

Source files will **never** contain tab characters!

### 2.2. Encoding

The file encoding will always be UTF-8.

## 3. Source file structure

### 3.1. Top level classes

There will be only one top-level class per source file.

// Foo.java
public class Foo {
}
// Wrong: if Bar is needed outside of Foo, it should be placed
// in its own source file, or if only used inside Foo,
// it should be put inside Foo.
class Bar {
}

## 4. Formatting

### 4.1. Braces

Braces are always used for `if`, `else`, `for`, `do` and `while` statements.

// Wrong:
if (expression)
System.out.println("true");
// Correct:
if (expression) {
System.out.println("true");
}

### 4.2. Indentation

Code will be indented by 4 spaces, and the continuation of a statement will be twice that amount (8).

public double divide(Double a, Double b) throws NullPointerException,
IllegalArgumentException, SomeOtherException {
// 8 spaces
// 4 spaces
return a / b;
}

### 4.3. Statements

There will be at most one statement per line, and each statement is followed by a line break.

// Wrong:
int a = 1; int b = 2;
int c = 3, d = 4;
// Correct:
int e = 5;
int f = 6;

### 4.4. Column length

There will not me more than 120 characters on a single line (indented spaced included!).

### 4.5. Grouping parenthesis

Grouping parenthesis are (highly!) preferred.

// Not preferred (at all):
if (a + b / c == d) {
// ...
}
// (Highly) preferred (although identical to the expression above):
if ((a + (b / c)) == d) {
// ...
}

### 4.6. Control flow statements

All control flow statements (`if`, `switch`, `do`...`while`, `while` and `for`) have braces on the line they start, and its parenthesis are surrounded with spaces:

// Wrong:
for(int i = 0; i < n; i++){
// ...
}
// Wrong:
for (int i=0;i<n;i++) {
// ...
}
// Wrong:
for (int i = 0; i < n; i++)
{
// ...
}
// Correct:
for (int i = 0; i < n; i++) {
// ...
}

Nesting ternary statements will not occur: a single `... ? ... : ...` is allowed.

// Wrong
var = (a > b) ? ((a > c) ? a : -1) : -1;
// Correct
if ((a > b) && (a > c)) {
var = a;
}
else {
var = -1;
}
// or also correct
var = ((a > b) && (a > c)) ? a : -1;

### 4.7. `switch` statement

All but the last statements inside a `switch` statements are terminated, or indicated by a comment to fall through:

switch (number) {
case 1:
foo();
break;
case 2:
return "we're done!"
case 3:
System.out.println("...");
// Falling through!
case 4:
bar();
break;
default:
handle(number);
}

### 4.8. Literals

Literal `long`s (or `Long`s) have a trailing capital `L`:

// Wrong:
long n = 10000000000l;
// Correct:
long p = 10000000000L;

### 4.9. Exceptions

The `try`, `catch` and `finally` keywords are always placed on a new line. And exceptions are **never** swallowed.

// Wrong:
try {
// ...
} catch(Exception e) {
} finally {
// ...
}
// Correct:
try {
// ...
}
catch(Exception e) {
// Preferably log it, but at the very least print its stack trace:
e.printStackTrace();
}
finally {
// ...
}

## 5. Naming

1. class/interface names always start with a capital letter and are camel-cased thereafter
2. instance variables always start with a lowercase letter and are camel-cased thereafter
3. all methods always start with a lowercase letter and are camel-cased thereafter
4. enum constants are entirely made of capitals and its words are separated by underscores
5. `static final` members are entirely made of capitals and its words are separated by underscores
6. `static` members always start with an underscore and lowercase letter and are camel-cased thereafter

// 1
public class Foo {
// 1
static enum Direction {
// 4
NORTH, EAST, SOUTH, WEST, UNKNOWN\_DIRECTION
}
// 5
public static final int A\_LONG\_CONSTANT\_NAME = 42;
// 6
private static int \_instanceCounter = 1;
// 2
private int ownCounter;
public Foo() {
this.ownCounter = \_instanceCounter++;
}
// 3
public int someMethodName() {
return -1;
}
}

## 6. Programming Practices

### 6.1. `@Override`

When overriding methods from a super class **always** use the `@Override` annotation.

### 6.2. Exceptions

Only throw an exception, when in unrecoverable state, catching when in a state to recover or stop and inform the user. Exception should never be part of a "normal" flow.

### 6.3. `equals(Object)` and `hashCode()`

When overriding one of `Object`'s `equals(Object)` or `hashCode()`, **always** override the other, and do so based on the other's use of attributes.

public class Point {
final int x;
final int y;
// ...
@Override
public boolean equals(Object o) {
if (o == null || super.getClass() != o.getClass()) {
return false;
}
Point that = (Point) o;
return (this.x == that.x) && (this.y == that.y);
}
@Override
public int hashCode() {
// Wrong:
// return this.x;
// Wrong:
// return this.x + this.y;
// Correct:
return (this.x \* 31) ^ (this.y \* 17);
}
}

## 7. Javadoc

All non-private, non-trivial methods should have JavaDocs and all parameters should be specified (not all need). Whenever a parameter, or return type is allowed to be be `null`, it should be stated in the JavaDocs. If the JavaDocs do not mention anything about a parameter or return type being `null`, it should be assumed that passing a `null` will result in an exception being thrown.

It is encouraged to use `@link`s where possible to make CTRL-clicking to relevant parts of code easy. But it is important to keep JavaDoc comments readable: do **not** litter it with countless (link) tags.

/\*\*
\* Some utilities no developer could do without!
\*/
final class Utils {
// No need to instantiate this class.
private Utils() {
}
/\*\*
\* Returns the integer value of `value`, or 0 when
\* `value` could not be parsed into a 32-bit integer.
\*
\* See: {@link Utils#tryParseInt(String, Integer)}
\*
\* @param value
\* the string to parse into an integer.
\*
\* @return the integer value of `value`, or 0 when
\* `value` could not be parsed into a 32-bit integer.
\*/
public static Integer tryParseInt(String value) {
return tryParseInt(value, 0);
}
/\*\*
\* Returns the integer value of `value`, or `returnValueOnFail` when
\* `value` could not be parsed into a 32-bit integer.
\*
\* See: {@link Utils#tryParseInt(String)}
\*
\* @param value
\* the string to parse into an integer.
\* @param returnValueOnFail
\* the value to return if `value` could not be parsed into
\* a 32-bit integer.
\*
\* @return the integer value of `value`, or `returnValueOnFail` when
\* `value` could not be parsed into a 32-bit integer.
\*
\* @throws NullPointerException when `value` could not be parsed into
\* a 32-bit integer, and `returnValueOnFail` is null.
\*/
public static Integer tryParseInt(String value, Integer returnValueOnFail)
throws NullPointerException {
try {
return Integer.valueOf(value);
}
catch (NumberFormatException e) {
if (returnValueOnFail == null) {
throw new NullPointerException("returnValueOnFail == null");
}
return returnValueOnFail;
}
}
}

## 8. Development Practices

### 8.1. SCM

Do not check-in/push too much in one go: a single commit should relate to a single enhancement/fix. Never commit code that does not compile. When committing unstable code, at the very least do so on a (temporary) branch, never on `master`.

When trying out something new, create a separate branch for it, but try to merge as soon as it is stable and either remove the branch, or let the branch die and switch back to `development`. We're working on a single product, which means a single (development) branch.

In order to incorporate hotfixes in production environments there is a seperate production master branch being maintained. All updates in the development branch will be moved into the master branch upon release. Hotfixes will be committed to both the master and the development branch.

Details on the branching method adopted can be found here: <http://nvie.com/posts/a-successful-git-branching-model/>

### 8.2. Unit Testing

All (small) non-private methods should be unit tested.

Each class `X` will have its own unit test class, `XTest` in the same package (under `src/test`). We will use JUnit 4.x and will follow [Roy Osherove's naming strategy](http://osherove.com/blog/2005/4/3/naming-standards-for-unit-tests.html):

[UnitOfWork\_StateUnderTest\_ExpectedBehavior]

An example:

public class Arithmetic {
public static double divide(Double a, Double b) {
return a / b;
}
}
public class ArithmeticTest {
@Test
public void divide\_NormalParams\_Success() {
assertThat(Arithmetic.divide(9.0, 3.0), is(3.0));
}
@Test(expected = NullPointerException.class)
public void divide\_NullParam\_ThrowsException() {
Arithmetic.divide(null, 3.0);
}
}