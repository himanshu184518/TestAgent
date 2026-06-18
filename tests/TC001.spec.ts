// spec: plans/TC001-plan.md
// seed: seed.spec.ts

import { test, expect } from '@playwright/test';

const URL = process.env.ORANGEHRM_URL || 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login';

const SELECTORS = {
  username: 'input[name="username"]',
  password: 'input[name="password"]',
  loginButton: 'button[type="submit"]',
  dashboardHeader: 'h6'
};

test.describe('TC001 - Login Validation', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto(URL);
  });

  test('Login with valid credentials shows Dashboard', async ({ page }) => {
    // 1. Open OrangeHRM.
    // (navigation handled in beforeEach)

    // 2. Enter Admin.
    await page.fill(SELECTORS.username, 'Admin');

    // 3. Enter admin123.
    await page.fill(SELECTORS.password, 'admin123');

    // 4. Click Login
    await page.click(SELECTORS.loginButton);

    // Expected Result: Dashboard should appear
    await expect(
    page.getByRole(
        'heading',
        { name: 'Dashboard' }
    )
).toBeVisible();
  });
});
