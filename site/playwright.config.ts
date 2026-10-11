import { defineConfig } from '@playwright/test'

const baseURL = process.env.E2E_BASE_URL ?? 'http://localhost:5173/'

export default defineConfig({
  testDir: './e2e',
  timeout: 120_000,
  retries: 0,
  use: {
    baseURL,
    viewport: { width: 1280, height: 900 },
    screenshot: 'only-on-failure',
  },
  reporter: [['list']],
  projects: [
    { name: 'smoke', testMatch: /smoke\.spec\.ts/ },
    { name: 'sweep', testMatch: /sweep\.spec\.ts/ },
  ],
  // Start the dev server unless E2E_BASE_URL points somewhere else (e.g. the live site).
  webServer: process.env.E2E_BASE_URL
    ? undefined
    : {
        command: 'npm run dev -- --port 5173 --strictPort',
        url: baseURL,
        reuseExistingServer: !process.env.CI,
        timeout: 60_000,
      },
})
