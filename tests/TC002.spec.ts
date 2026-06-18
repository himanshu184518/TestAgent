
import { test, expect } from '@playwright/test';

test('TC002', async ({ page }) => {

    await page.goto(
        'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
    );

    await expect(
        page.locator(
            'input[name="username"]'
        )
    ).toBeVisible();

});
