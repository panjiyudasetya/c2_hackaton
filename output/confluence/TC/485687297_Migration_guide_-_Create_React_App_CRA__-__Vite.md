---
id: confluence:485687297
source: confluence
type: page
space: TC
title: Migration guide - Create React App(CRA) -> Vite
author: Ojas Gulati (Unlicensed)
date: '2024-11-19'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/485687297
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/485687297
---
# Migration guide - Create React App(CRA) -> Vite

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/485687297  

## Content

This guide deals with migration of a frontend project bootstrapped with create react app(react-scripts) to Vite

# Benefits

* Build speed - Vite offers much higher build speeds as compared to CRA. Moreover the hot module reload speed is also much higher than CRA
* Flexible Configuration - The ease of use offered by CRA came at a cost: configurability. CRA with its webpack config hidden under the hood was a nightmare to configure of any change in configuration was required. Vite however keeps it simple and straightforward and is much easier to configure
* SSR: If a project required server side rendering then integrating it with Vite is much easier
* Framework agnostic: Vite can be used with any frontend framework as opposed to CRA which could be used only with React
* Maintenance: CRA is no longer being maintained with no updates coming from the Facebook team. This has led to it accumulating a lot of vulnerabilities.

# Steps

## 1. Uninstall react-scripts

First and foremost remove the react-scripts dependency. To do this you can either find an remove the dependency react-scrips from the dependency list or run the command  
`npm uninstall react-scripts`

## 2. Install Vite related dependencies

Run the following command to install Vite & other plugins

`npm install vite @vitejs/plugin-react-swc @vitest/coverage-v8 vite-plugin-checker --save-dev`

Note: Please follow last point in Extras if you install these as dev dependencies. Otherwise ESLint will complain about dependencies not being in the “Dependencies“ array in package.json

## 3. Move index.html file

CRA uses `public/index.html` as the default entry point, while Vite looks for index.html at the root level. To make the transition, move your index.html to the root directory and update the script tag for `index.ts` and other links accordingly

html<!-- index.html -->
<!doctype html>
<html lang="en">
<body>
<link rel="shortcut icon" href="/favicon.ico" />
<link rel="apple-touch-icon" sizes="57x57" href="/favicons/apple-icon-57x57.png" />
<link rel="apple-touch-icon" sizes="60x60" href="/favicons/apple-icon-60x60.png" />
<noscript>You need to enable JavaScript to run this app.</noscript>
<div id="root"></div>
---------------------
<script type="module" src="/src/index.tsx"></script>
</body>
</html>

Notice 2 kinds of changes here

* Remove `%PUBLIC_URL%` - Vite automatically resolves URLs inside `index.html`, so there's no need for `%PUBLIC_URL%` placeholders. You can do a search and replace inside your `index.html` file for this. Be sure to remove all occurrences.

BEFORE

`<link rel="shortcut icon" href="%PUBLIC_URL%/favicon.ico" />`

AFTER

`<link rel="shortcut icon" href="/favicon.ico" />`

## 4. Add vite.config.js

Add a file named vite.config.ts(which holds the vite config) at the root of the project with the following code

jsimport { defineConfig } from 'vitest/config'
import checker from 'vite-plugin-checker'
import react from '@vitejs/plugin-react-swc'
// https://vitejs.dev/config/
export default defineConfig({
base: '/',
plugins: [checker({ typescript: true }), react()],
server: {
port: 3000,
open: true
},
build: {
outDir: 'build'
},
})

## 5. Add vite.env.d.ts

Remove the `src/react-app-env.d.ts` file and create a `vite-env.d.ts` file instead inside the src folder with the following content:

/// <reference types="vite/client" />

## 6. Replace Environment variables

CRA uses certain env variables stored in the `.env` file in the format `REACT_APP_ENV_VAR_A`. But since we are going to vite such variable names have to be replaced with the format `VITE_ENV_VAR_A`. Additionally the usage of variables has to be replace from `process.env.REACT_APP_ENV_VAR_A` to `import.meta.env.VITE_ENV_VAR_A`

## 7. Enhancing TSConfig

The TS Config also needs to change to reflect the installation of vite

{
"compilerOptions": {
"target": "es5",
"lib": ["dom", "dom.iterable", "esnext"],
"allowJs": true,
"skipLibCheck": true,
"esModuleInterop": true,
"allowSyntheticDefaultImports": true,
"strict": true,
"forceConsistentCasingInFileNames": true,
"noFallthroughCasesInSwitch": true,
"module": "esnext",
"moduleResolution": "node",
"resolveJsonModule": true,
"isolatedModules": true,
"noEmit": true,
"jsx": "react-jsx",
"types": ["vite/client"] // NEW
},
"include": ["src", "vite.config.ts"] // NEW
}

## 8. Installing vitest (Follow this step if you have the testing setup)

If you are running unit tests in your project(which is recommended), you might want to replace Jest with Vitest which is the Vite’s replacement for CRA’s jest.

### a. Install dev dependencies

`npm i --save-dev jsdom vitest @vitest/coverage-v8`

Note: Please follow last point in *Extras* if you install these as dev dependencies

### b. Update the `package.json`

- Remove `jest` and `@types/jest` packages if present in your project

- If you have this snippet in your `package.json` ,

"eslintConfig": {
"extends": [
"react-app",
"react-app/jest"
]
},

then please remove `"react-app/jest"` from the object

### c. Update the `vite.config.ts` file

import { defineConfig } from 'vitest/config'
import checker from 'vite-plugin-checker'
import react from '@vitejs/plugin-react-swc'
// https://vitejs.dev/config/
export default defineConfig({
base: '/',
plugins: [checker({ typescript: true }), react()],
server: {
port: 3000,
open: true,
},
build: {
outDir: 'build',
},
test: {
globals: true,
environment: 'jsdom',
setupFiles: './src/vitest.setup.ts',
css: true,
reporters: ['verbose'],
coverage: {
reporter: ['text', 'json', 'html'],
include: ['src/\*\*/\*'],
exclude: [],
},
},
})

### d. Add `vite.setup.ts` file

Add a vite.setup.ts file under src folder with the following code

jsimport '@testing-library/jest-dom/vitest'
import { cleanup } from '@testing-library/react'
import { afterEach } from 'vitest'
afterEach(() => {
cleanup()
})

## 9. Update `package.json` with vite related scripts

Remove the react-scripts related scripts and add vite related scripts to your script object in the `package.json`

"scripts": {
"start": "vite",
"serve": "vite preview",
"build": "vite build",
// only add the following if you have installed Vitest
"test": "vitest",
"test:coverage": "vitest run --coverage --watch=false"
},

Extras

* You can also add the timezone to the test command just like react-scripts e.g. `"TZ=UTC vitest"`
* You might need to change the ways in which the unit tests are written and import bunch of stuff from vitest like `import { vi, test, expect } from 'vitest'`. More information can easily be found in the official vitest documentation
* It would be a good idea to add `src/vite-env.d.ts` to `.eslintignore` file and remove `src/react-app-env.d.ts` if present
* It would also be a good idea to add the following paths in `no-extraneous-dependencies`in the `eslintrc.json`file if the Vite related dependencies have been installed as dev-dependencies(which is recommended) instead of normal dependencies. Otherwise the eslint will complain on the imports in the Vite files.

"import/no-extraneous-dependencies": [
"error",
{
"devDependencies": [
"\*\*/\*.test.js",
"\*\*/\*.test.jsx",
"\*\*/\*.test.ts",
"\*\*/\*.test.tsx",
"src/tests/\*\*/\*",
"vite.config.ts",
"src/vitest.setup.ts"
]
}
],