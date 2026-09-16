---
id: confluence:815038520
source: confluence
type: page
space: TC
title: Vessel Complience - Code Practice
author: Fauzan Rifqy
date: '2025-07-31'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/815038520
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/815038520
---
# Vessel Complience - Code Practice

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/815038520  

## Content

## React Component Patterns

### 1. Function Components Over Class Components

✅ **DO**: Use function components exclusively

function Header(props: IProps) {
const [openMenu, setOpenMenu] = useState<boolean>(false)
// component logic
return <nav>...</nav>
}

❌ **DON'T**: Use class components

// Avoid class components
class Header extends React.Component { ... }

### 2. Props Interface Naming

✅ **DO**: Use `IProps` interface for component props

interface IProps {
userInfo?: CurrentUser
onLogout: (disableRedirect: boolean) => void
}
function Header(props: IProps) {
// component implementation
}

### 3. Component File Structure

✅ **DO**: Follow this file organization pattern:

src/components/ComponentName/
├── ComponentName.tsx
├── ComponentName.scss
└── index.ts (if needed)

## TypeScript Practices

### 1. Interface vs Type Usage

✅ **DO**: Use `interface` for object shapes and component props

export interface Clearance {
\_id: string
purpose: Purpose
status: Status
placeOfCall: string
// ... other properties
}
interface IProps {
userInfo?: CurrentUser
onLogout: (disableRedirect: boolean) => void
}

✅ **DO**: Use `type` for union types and aliases

type Status = 'ACCEPTED' | 'CONDITIONALLY\_ACCEPTED' | 'DENIED' | 'REQUESTED' | 'NOT\_REQUESTED' | 'WARNING'
type Environment = 'production' | 'staging' | 'development' | 'localhost'

### 2. Type Definitions Organization

✅ **DO**: Organize types in dedicated files under `src/@types/`

* `vc-backend.d.ts` - Backend API types
* `types.d.ts` - General application types
* `Enums.ts` - Enum definitions

### 3. Strict TypeScript Configuration

✅ **DO**: Use strict TypeScript settings

{
"compilerOptions": {
"strict": true,
"noFallthroughCasesInSwitch": true,
"forceConsistentCasingInFileNames": true
}
}

## State Management

### 1. React Hooks Pattern

✅ **DO**: Use React hooks for state management

function Header(props: IProps) {
const [openMenu, setOpenMenu] = useState<boolean>(false)
const navigate = useNavigate()
const { pathname } = useLocation()
// component logic
}

### 2. Custom Hooks

✅ **DO**: Create custom hooks for reusable logic

function useDimensions(ref: RefObject<HTMLElement>) {
const dimensions = useSyncExternalStore(subscribe, () =>
JSON.stringify({
width: ref.current?.offsetWidth ?? 0,
height: ref.current?.offsetHeight ?? 0,
})
)
return useMemo(() => JSON.parse(dimensions), [dimensions])
}

## Service Layer Patterns

### 1. Singleton Pattern for Services

✅ **DO**: Use singleton pattern for service classes

class AuthenticationService implements AuthenticationServiceLayer {
public static Instance(
initialUser: UserAuth,
backendUrl: string,
logoutUser: () => void
) {
return (
this.\_instance ||
(this.\_instance = new this(initialUser, backendUrl, logoutUser))
)
}
private static \_instance: AuthenticationService
private constructor(/\* params \*/) { /\* implementation \*/ }
}

## Import/Export Conventions

### 1. Import Organization

✅ **DO**: Organize imports in this order:

1. React and React-related imports
2. Third-party libraries
3. Internal types and interfaces
4. Internal components and services
5. Utilities and constants
6. Styles

import { useState } from 'react'
import { useLocation, useNavigate } from 'react-router-dom'
import { toast } from 'react-toastify'
import { CurrentUser } from '../../@types/vc-backend'
import { ENVIRONMENT } from '../../utils/constants'
import { isDeveloper, isSuperUser, roleTranslations } from '../../utils/roles'
import './Header.scss'

### 2. Default Exports

✅ **DO**: Use default exports for components

function Header(props: IProps) {
// component implementation
}
export default Header

## File Naming Conventions

### 1. Component Files

✅ **DO**: Use PascalCase for component files

* `Header.tsx`
* `LoadingSpinner.tsx`
* `DashboardTable.tsx`

### 2. Utility Files

✅ **DO**: Use camelCase for utility files

* `apiCalls.ts`
* `errorHandling.ts`
* `constants.ts`

### 3. Type Definition Files

✅ **DO**: Use kebab-case with `.d.ts` extension

* `vc-backend.d.ts`
* `types.d.ts`
* `react-table-config.d.ts`

## Styling Practices

### 1. SCSS Usage

✅ **DO**: Use SCSS for styling with component-specific files

src/components/Header/
├── Header.tsx
└── Header.scss

### 2. CSS Class Naming

✅ **DO**: Use kebab-case for CSS classes

.navbar {
.navbar-wrapper {
.user-info {
.navbar-menu {
// styles
}
}
}
}

## Error Handling

### 1. Error Boundaries

✅ **DO**: Use Error Boundaries for component error handling

<ErrorBoundary>
<DefaultRoutes
authenticationService={authenticationService}
userInfo={userInfo}
/>
</ErrorBoundary>

### 2. Service Layer Error Handling

✅ **DO**: Implement consistent error handling in services

// Custom error classes and handling in services
export class FetchError extends Error {
// error implementation
}

## Testing Practices

### 1. Testing Setup

✅ **DO**: Use Vitest with React Testing Library

* Configuration in `vitest.setup.ts`
* Test files co-located with components or in `__tests__` directories

## Code Quality Tools

### 1. Linting and Formatting

✅ **DO**: Use ESLint and Prettier with consistent configuration

{
"scripts": {
"lint": "eslint --ext .js,.jsx,.ts,.tsx src --color && pnpm run prettier-check",
"prettier-format-all": "prettier --write --config ./.prettierrc \"./src/\*\*/\*.ts\" \"./src/\*\*/\*.tsx\" \"./src/\*\*/\*.scss\""
}
}

### 2. Package Management

✅ **DO**: Use pnpm for package management

* Faster installation and better disk space usage
* Lock file: `pnpm-lock.yaml`

## Constants and Configuration

### 1. Environment Configuration

✅ **DO**: Centralize constants in utility files

export const BACKEND\_URL = process.env.REACT\_APP\_BACKEND\_URL
export const ENVIRONMENT = process.env.NODE\_ENV

### 2. Type-safe Environment Variables

✅ **DO**: Define environment types

type Environment = 'production' | 'staging' | 'development' | 'localhost'

## Performance Considerations

### 1. Modern React Patterns

✅ **DO**: Use modern React hooks like `useSyncExternalStore` for performance

const dimensions = useSyncExternalStore(subscribe, () =>
JSON.stringify({
width: ref.current?.offsetWidth ?? 0,
height: ref.current?.offsetHeight ?? 0,
})
)

### 2. Memoization

✅ **DO**: Use `useMemo` for expensive calculations

return useMemo(() => JSON.parse(dimensions), [dimensions])

---

## Summary

This codebase follows modern React and TypeScript best practices with:

* Function components with hooks
* Interface-first approach for object types
* Strict TypeScript configuration
* Consistent file organization and naming
* Singleton pattern for services
* SCSS for styling
* Comprehensive tooling for code quality