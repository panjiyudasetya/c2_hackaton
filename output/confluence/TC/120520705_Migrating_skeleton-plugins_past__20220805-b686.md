---
id: confluence:120520705
source: confluence
type: page
space: TC
title: Migrating skeleton-plugins past `20220805-b686`
author: Former user (Deleted)
date: '2022-08-05'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/120520705
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/120520705
---
# Migrating skeleton-plugins past `20220805-b686`

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/120520705  

## Content

## Konfig deprecation (+ version.properties)

The usage of Konfig within skeleton-plugins has been removed in favor of `@ConfigurationProperties` that are provided by Spring.

This has the added benefit of being able to go in the `application.properties` and inspect the configuration object by ctrl+click-ing.

When upgrading to the newer skeleton-plugins versions you are required to do these migrations. For most applications this will be painless, as removing Konfig entirely and immediately isn’t required for an application itself. Described below are both short-term steps that are required to be done, and some longer-term steps to migrate your application fully away from Konfig.

## Steps to migrate short-term:

1. Upgrade your skeleton-plugins version to `20220805-b686` or higher
2. Remove the use of the skeleton-plugins gradle plugin

   1. remove `classpath "nl.teqplay.skeleton:nl.teqplay.skeleton.gradle.plugin:$skeleton_version"`
   2. remove `apply plugin: 'nl.teqplay.skeleton'`
3. Remove the `:common-kubernetes` skeleton-plugin from your dependencies
4. Search through your code to find usage of Konfig’s `PropertyGroup`, `stringType`, `booleanType`, etc or (y)our own `KonfigConfiguration` implementation.

   1. if you are not using Konfig, you can skip all next steps
   2. if you are using a different type of configuration management (which is not Konfig), please take a look at the longer-term migration plan for moving away from this custom config
   3. if you are using Konfig

      1. add the new `:konfig` skeleton-plugin to your dependencies
      2. if you use it, re-import `Auth0S2SClientPropertyGroup`
      3. if you use it, when using the `Auth0S2SClientWrapper` use the `.toProperties(config)` on the `Auth0S2SClientPropertyGroup` instance to get the properties to pass into the wrapper
      4. if you use it, re-import `KeyCloakS2SClientPropertyGroup`
      5. if you use it, rename `KeyCloakS2SClientWrapper` to `KeycloakS2SClientWrapper` and use `.toProperties(config)` on the `KeyCloakS2SClientPropertyGroup` instance to get the properties to pass into the wrapper
      6. in general, all names containing `KeyCloak` have been renamed to `Keycloak` for consistency
      7. change the import from `nl.teqplay.skeleton.common.kubernetes.KubernetesConfigMap` to `nl.teqplay.skeleton.konfig.kubernetes.KubernetesConfigMap`
      8. if you re-use logic from the skeleton and try to inject the Konfig configuration it will not work anymore, you need to use the required `xxProperties` object from `:common`, see the method itself for the required model (example: `config: KConfig => authCredentialsMongo: AuthCredentialsMongoProperties`)

Thusfar, these changes should mostly be painless. However, the `version.properties` file and the skeleton-plugins gradle task `generateVersionProperties` have been removed. The `version.properties` file will require docker images to always create a unique layer, purely because this file is there. Instead, the version of the application should/could be in the docker image tag.

Some applications have been identified that might have a certain degree of breaking changes (either due to the removal of Konfig or the `version.properties`. Even if an application is not listed, it may still be dependent or break. Please confirm your application works as intended before deploying.

* **BunkerPlanner**

  + set version in `build.gradle` (should be low impact since it first uses `.git` and the `version.properties` as fallback)
  + `application-intest.properties` is loaded in `KonfigConfiguration`, should instead activate the `"intest"` Spring profile when required
* **Ship Spare Logisitcs**

  + set version in `build.gradle` (version could stay unspecified otherwise, has a TODO about fixing the skeleton-plugins, was this already fixed?)
* **Portcall+**

  + `postPublish.py` is used to send a Slack notification which uses the version and commithash of the `version.properties`, instead use the `CIRCLE_SHA1` environment variable inside CircleCI and `version=$(./gradlew -q getVersion | tail -n 1)` to get the version

    - should be changed anyhow since the Slack webhook is currently committed in the repo (and we might want other applications to also post deploy notifications?)
* **TerminalPlanner**

  + sets `version.properties` itself in the `build.gradle`, could possibly just be removed

* **VesselMatcher**

  + `VersionResolver` will break, please determine the impact and how to migrate

## Steps to migrate longer-term:

Migrate all your Konfig/custom configuration to `@ConfigurationProperties`

How it will look:

**Konfig**

object auth\_credentials\_auth0\_s2s : PropertyGroup() {
val domain by stringType(warnOnEmpty = true)
val audience by stringType(warnOnEmpty = true)
}

**@ConfigurationProperties**

@ConstructorBinding
@ConfigurationProperties(prefix = "auth-credentials-auth0-s2s")
data class AuthCredentialsAuth0S2SProperties(
val domain: String? = null,
val audience: String = ""
)

1. Copy `auth_credentials_auth0_s2s` into the `@ConfigurationProperties(prefix = "...")` annotation

   1. make sure to replace the `_` to the `-` (if you don’t do this it will not be backwards-compatible and you’ll get a warning by IntelliJ as well)
2. Add the `@ConstructorBinding` annotation and make all variables a `val` instead of a `var`
3. Rename your object from `auth_credentials_auth0_s2s` to use camelCase + `Properties` = `AuthCredentialsAuth0S2SProperties`
4. Turn the `object` into a `data class` and remove the `: PropertyGroup()`
5. Remove the `by stringType(warnOnEmpty = true)` and replace it with `: String = ""` or `: String? = null` depending on your specific needs

   1. it’s perfectly fine to not default these, but be aware that you’ll get an error on startup if the value isn’t set (which is desirable behavior anyhow, but just to be aware of this)
   2. it’s not possible to preserve these warnings on empty values, if you’d like that you should implement this yourself (although it’s better practice to fail startup if certain values are required instead of swallowing the problem and printing a log statement)
   3. change all the custom `by ...` Konfig logic to reflect their Kotlin-type equivalents
6. By default, this configuration will not be picked up by Spring (you should also see a warning on the `@ConfigurationProperties` about this)

   1. You have two options, either use `@ConfigurationPropertiesScan` or `@EnableConfigurationProperties`
   2. skeleton-plugins uses `@EnableConfigurationProperties(YourPropertiesConfiguration::class)`, since they are only enabled if certain auto-configuration is ran
   3. However, since you are writing an application and not a re-usable plugin/lib it’s better to not enable configs one-by-one, but use `@ConfigurationPropertiesScan` instead

      1. Go to your application entrypoint (annotated with `@SpringBootApplication`) and add the `@ConfigurationPropertiesScan` annotation, as is suggested by the name all your configuration properties will be scanned automatically.

One more important note upon converting to `@ConfigurationProperties`, Spring can use relaxed binding for properties but only if you correctly name your variables!

Example: `client_id => clientId`

This will ensure that Spring’s relaxed binding can be applied, you can read more about it here:

<https://docs.spring.io/spring-boot/docs/current/reference/html/features.html#features.external-config.typesafe-configuration-properties.relaxed-binding>

**TLDR;** always use lower camel-casing, and no kebab/snake/other-casing in the configuration properties