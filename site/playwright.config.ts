import { defineConfig } from '@playwright/test'

// The smoke and sweep projects run against the dev server (or E2E_BASE_URL,
// e.g. the live site). The prerender project checks the built output served
// by `vite preview`, with JavaScript disabled, so it needs `npm run build` first.
const devURL = process.env.E2E_BASE_URL ?? 'http://localhost:5173/'
const previewURL = process.env.E2E_BASE_URL ?? 'http://localhost:4173/'

export default defineConfig({
  testDir: './e2e',
  timeout: 120_000,
  retries: 0,
  use: {
    viewport: { width: 1280, height: 900 },
    screenshot: 'only-on-failure',
  },
  reporter: [['list']],
  projects: [
    { name: 'smoke', testMatch: /smoke\.spec\.ts/, use: { baseURL: devURL } },
    { name: 'sweep', testMatch: /sweep\.spec\.ts/, use: { baseURL: devURL } },
    { name: 'prerender', testMatch: /prerender\.spec\.ts/, use: { baseURL: previewURL, javaScriptEnabled: false } },
  ],
  webServer: process.env.E2E_BASE_URL
    ? undefined
    : [
        {
          command: 'npm run dev -- --port 5173 --strictPort',
          url: devURL,
          reuseExistingServer: !process.env.CI,
          timeout: 60_000,
        },
        {
          command: 'npx vite preview --port 4173 --strictPort',
          url: previewURL,
          reuseExistingServer: !process.env.CI,
          timeout: 60_000,
        },
      ],
})
