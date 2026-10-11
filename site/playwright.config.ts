import { defineConfig } from '@playwright/test'

// The smoke and sweep projects run against the dev server (or E2E_BASE_URL,
// e.g. the live site). The prerender project checks the built output served
// by `vite preview`, with JavaScript disabled, so it needs `npm run build` first.
// Both servers serve under VITE_BASE when it is set (as CI does).
const devURL = process.env.E2E_BASE_URL ?? `http://localhost:5173${process.env.VITE_BASE ?? '/'}`
// `vite preview` serves the build under its configured base (VITE_BASE).
const previewURL = process.env.E2E_BASE_URL ?? `http://localhost:4173${process.env.VITE_BASE ?? '/'}`

export default defineConfig({
  testDir: './e2e',
  timeout: 120_000,
  retries: 0,
  // The three projects are independent; run them side by side (the sweep is
  // one long test, so this roughly halves the wall-clock time).
  workers: 3,
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
        // Always start fresh: a leftover server from an earlier run may be
        // serving a different base path or stale content.
        {
          command: 'npm run dev -- --port 5173 --strictPort',
          url: devURL,
          reuseExistingServer: false,
          timeout: 60_000,
        },
        {
          command: 'npx vite preview --port 4173 --strictPort',
          url: previewURL,
          reuseExistingServer: false,
          timeout: 60_000,
        },
      ],
})
