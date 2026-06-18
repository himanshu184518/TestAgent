import { test as base, expect } from '@playwright/test';

export const test = base;

test.afterEach(async ({ page }, testInfo) => {

  try {

    const screenshot = await page.screenshot({
      fullPage: true
    });

    await testInfo.attach(
      'Final Screenshot',
      {
        body: screenshot,
        contentType: 'image/png'
      }
    );

  } catch (error) {

    console.log(
      'Unable to capture screenshot',
      error
    );
  }
});

export { expect };