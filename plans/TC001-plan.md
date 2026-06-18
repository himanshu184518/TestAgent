# TC001 - Execution Plan

**Scope**
- **Goal**: Verify Login Validation for OrangeHRM: successful login displays the Dashboard.
- **In-scope**: UI-level login flow using web Playwright tests (page navigation, credential input, login action, dashboard visibility).
- **Out-of-scope**: API-level auth, multi-factor auth, user provisioning.

**Preconditions**
- **Application reachable**: OrangeHRM web app URL accessible from test environment.
- **Test account available**: Username `Admin` with password `admin123` exists and is not locked.
- **Clean state**: Browser context is fresh (no existing session/cookies).
- **Assumption**: Spec steps used exactly:
  1. Open OrangeHRM.
  2. Enter Admin.
  3. Enter admin123.
  4. Click Login

**Test Data**
- **Valid credentials**: Username: Admin, Password: admin123
- **Invalid credentials (variants)**:
  - Username: Admin, Password: wrongpass
  - Username: WrongUser, Password: admin123
  - Username: (empty), Password: admin123
  - Username: Admin, Password: (empty)
  - Injection payloads: `' OR '1'='1` (negative test)
- **Environment variables**:
  - ORANGEHRM_URL — test target base URL

**Test Steps mapped to Playwright actions**
- Steps below follow the spec exactly and map to Playwright actions and selectors. Replace selectors with the app's real selectors if different.

1. Navigate to the login page
   - Playwright action: `page.goto(process.env.ORANGEHRM_URL || 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')`
2. Enter username "Admin"
   - Playwright action: `page.fill('<username-selector>', 'Admin')`
3. Enter password "admin123"
   - Playwright action: `page.fill('<password-selector>', 'admin123')`
4. Click Login
   - Playwright action: `page.click('<login-button-selector>')`
5. Wait for Dashboard view
   - Playwright action: `await expect(page.locator('<dashboard-identifier-selector>')).toBeVisible()`

Suggested common selector candidates (verify in app):
- Username: `input[name="username"]`, `input#txtUsername`, `input[name="txtUsername"]`
- Password: `input[name="password"]`, `input#txtPassword`, `input[name="txtPassword"]`
- Login button: `button[type="submit"]`, `input#btnLogin`, `button:has-text("Login")`
- Dashboard identifier: `text=Dashboard`, `h1:has-text("Dashboard")`, `.oxd-topbar-header-title`

Example mapped step (concrete snippet):
```ts
await page.goto(URL);
await page.fill('input[name="username"]', 'Admin');
await page.fill('input[name="password"]', 'admin123');
await page.click('button[type="submit"]');
await expect(page.locator('text=Dashboard')).toBeVisible();
```

**Assertions / Expected Results**
- Primary assertion: Dashboard should appear (visible and interactable).
  - Example: `await expect(page.locator('text=Dashboard')).toBeVisible();`
- Secondary assertions (optional):
  - URL contains `/dashboard` or known dashboard path.
  - Topbar user menu visible: `await expect(page.locator('<user-menu-selector>')).toBeVisible();`
  - No login error message displayed.

**Setup and Teardown**
- Setup (before each test):
  - Launch browser context with fresh profile.
  - Set viewport and timeouts (e.g., `test.use({ viewport: { width: 1280, height: 800 } })`).
  - Set `ORANGEHRM_URL` env var or config.
- Teardown (after each test):
  - Clear cookies/localStorage or close context.
  - If test failed, capture screenshot and page HTML for debugging.

Example Playwright hooks:
```ts
import { test, expect } from '@playwright/test';
test.beforeEach(async ({ page }) => {
  await page.goto(process.env.ORANGEHRM_URL || 'https://<ORANGEHRM_HOST>');
});
test.afterEach(async ({ page }, testInfo) => {
  if (testInfo.status !== testInfo.expectedStatus) {
    await page.screenshot({ path: `screenshots/${testInfo.title}.png` });
  }
});
```

**Test Variants (positive / negative)**
- Positive:
  - Valid credentials (Admin / admin123) -> Dashboard appears
- Negative:
  - Wrong password -> Login error shown; Dashboard not visible
  - Wrong username -> Login error shown; Dashboard not visible
  - Empty username or password -> Field validation messages shown
  - SQL/injection-like input -> Validation or error handled gracefully
  - Excessively long username/password -> Proper validation or truncation
- Edge/Behavioral:
  - Leading/trailing spaces in username/password
  - Case sensitivity checks (e.g., `admin` vs `Admin`)
  - Multiple consecutive failed attempts -> account lock behavior (if applicable)

**Edge cases**
- Slow network/load: app delays rendering Dashboard — ensure use of robust waits (e.g., `locator.waitFor()`).
- Intermittent UI text change (localization): prefer stable selectors (ids/classes) over visible text when possible.
- Redirects or custom login flows (SSO) — test must detect and skip if SSO present.
- Session already active — ensure test always starts with a fresh context.

**Time estimates**
- Test implementation (single happy-path): 20–30 minutes
- Add negative variants and assertions: additional 30–45 minutes
- Full suite with robust selectors, hooks, and CI integration: 1.5–2 hours
- Flakiness debugging and stabilization: 30–60 minutes (if needed)

**Files to create (suggested)**
- tests/TC001.spec.ts — primary Playwright test file implementing the scenario (if updating an existing file, use that)
- tests/TC001.test-data.ts — test data constants (optional)
- tests/helpers/login.ts — helper to perform login actions (reuse across tests)
- test-results/screenshots/ — folder for failure screenshots
- .env.test or config/test.config.ts — ORANGEHRM_URL and credentials for test env

Note: `tests/TC001.spec.ts` already exists in workspace; verify and update it as needed.

**Dependencies**
- Playwright (installed in project): `@playwright/test`
- Node >= stable LTS
- Project Playwright config (`playwright.config.ts`) — ensure test match pattern includes `tests/*.spec.ts`
- Optional: dotenv for environment variables

Example package devDependencies snippet:
```json
"devDependencies": {
  "@playwright/test": "^1.x"
}
```

**Example Playwright test skeleton (TypeScript)**
```ts
import { test, expect } from '@playwright/test';

const URL = process.env.ORANGEHRM_URL || 'https://<ORANGEHRM_HOST>';

test.describe('TC001 - Login Validation', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto(URL);
  });

  test('Login with valid credentials shows Dashboard', async ({ page }) => {
    // Steps from spec exactly:
    // 1) Open OrangeHRM.
    // 2) Enter Admin.
    // 3) Enter admin123.
    // 4) Click Login
    await page.fill('input[name="username"]', 'Admin');
    await page.fill('input[name="password"]', 'admin123');
    await page.click('button[type="submit"]');
    await expect(page.locator('text=Dashboard')).toBeVisible();
  });
});
```

**Implementation checklist**
- - **Confirm URL**: Set ORANGEHRM_URL and test environment access.
- - **Select reliable selectors**: Inspect app, update username/password/login selectors.
- - **Create test file**: Add or update `tests/TC001.spec.ts`.
- - **Add helpers**: Extract login action to `tests/helpers/login.ts` if reused.
- - **Add hooks**: Implement `beforeEach`/`afterEach` for setup & teardown.
- - **Add negative variants**: Implement at least 3 negative tests (wrong password, empty fields, injection).
- - **Run locally**: Execute `npx playwright test tests/TC001.spec.ts`.
- - **Stabilize**: Add retries/timeouts if flaky; capture screenshots on failure.
- - **CI integration**: Ensure Playwright config used in CI pipelines.

**Playwright run commands**
```bash
# run single test file
npx playwright test tests/TC001.spec.ts

# run with trace and screenshot on failure
npx playwright test tests/TC001.spec.ts --trace on --retries 1
```

Use the spec steps verbatim in test documentation and step comments so the implementation maps clearly to the original requirement.
