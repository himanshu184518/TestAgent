// @ts-check
import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  testDir: './tests',

  fullyParallel: true,

  forbidOnly: !!process.env.CI,

  retries: process.env.CI ? 2 : 1,

  workers: process.env.CI ? 1 : undefined,

  reporter: [
    ['html', { open: 'always' }],
    ['list']
  ],

  use: {
    headless: false,

    // Capture screenshot for EVERY test
    screenshot: 'off',

    // Disable video completely
    video: 'off',

    // Disable traces completely
    trace: 'off',

    actionTimeout: 15000,

    navigationTimeout: 30000,

    viewport: {
      width: 1366,
      height: 768
    }
  },

  projects: [
    {
      name: 'chromium',
      use: {
        ...devices['Desktop Chrome']
      }
    }
  ]
});