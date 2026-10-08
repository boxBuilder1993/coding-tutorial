import { defineConfig } from '@playwright/test'

export default defineConfig({
  testDir: './e2e',
  timeout: 120_000,
  retries: 0,
  use: {
    baseURL: process.env.E2E_BASE_URL ?? 'http://localhost:5173/',
    viewport: { width: 1280, height: 900 },
    screenshot: 'only-on-failure',
  },
  reporter: [['list']],
})
