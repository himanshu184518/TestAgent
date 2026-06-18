# Additional Generation Rules

## Imports

Always generate:

```ts
import { test, expect } from '../base.fixture';
import { capture } from '../utils/screenshot';
```

Never generate:

```ts
import { test, expect } from '@playwright/test';
```

---

## Screenshot Capture

Capture screenshots automatically after:

* Initial page load
* Every major user action
* Final verification step

Example:

```ts
await page.goto(URL);

await capture(
  page,
  testInfo,
  'login_page'
);

await page.fill(
  SELECTORS.username,
  'Admin'
);

await capture(
  page,
  testInfo,
  'username_entered'
);

await page.fill(
  SELECTORS.password,
  'admin123'
);

await capture(
  page,
  testInfo,
  'password_entered'
);

await page.click(
  SELECTORS.loginButton
);

await capture(
  page,
  testInfo,
  'after_login'
);
```

---

## Test Signature

Always generate:

```ts
test(
  'Scenario Name',
  async ({ page }, testInfo) => {
```

Never generate:

```ts
test(
  'Scenario Name',
  async ({ page }) => {
```

---

## Locator Rules

Prefer:

```ts
page.getByRole()
page.getByLabel()
page.getByPlaceholder()
```

Avoid:

```ts
text=Dashboard
```

Use:

```ts
await expect(
  page.getByRole(
    'heading',
    { name: 'Dashboard' }
  )
).toBeVisible();
```

---

## Evidence Collection

Every generated test must collect evidence automatically.

Screenshots should be attached to the Playwright HTML report using:

```ts
await capture(
  page,
  testInfo,
  '<step_name>'
);
```

---

## Autonomous Testing Requirement

Generated tests must be self-documenting and self-diagnosable.

A failed execution should provide enough screenshots for a healing agent to understand:

* Current page state
* Last successful action
* Expected UI element
* Actual UI state

```
```
