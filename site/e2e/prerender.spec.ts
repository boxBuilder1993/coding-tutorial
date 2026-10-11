/**
 * The built site must be readable without JavaScript: every page has its own
 * URL with a real HTML file, a title, a description, a canonical link, and
 * the page text in the body. The sitemap lists each URL exactly once, in
 * path form only. This project runs with JavaScript disabled against
 * `vite preview`, so `npm run build` must have run first.
 */
import { expect, test } from '@playwright/test'

test('a lesson page is complete without JavaScript', async ({ page, baseURL }) => {
  const res = await page.goto('01-learn-python/01-getting-started/02-names/')
  expect(res?.status()).toBe(200)
  await expect(page).toHaveTitle(/^Names · /)
  const description = await page.locator('meta[name="description"]').getAttribute('content')
  expect(description).toMatch(/A name refers to a value/)
  const canonical = await page.locator('link[rel="canonical"]').getAttribute('href')
  expect(canonical).toBe(`${baseURL}01-learn-python/01-getting-started/02-names/`)
  expect(canonical).not.toContain('#')
  // The text is in the HTML itself, not fetched by script.
  await expect(page.locator('h1')).toHaveText('Names')
  await expect(page.locator('body')).toContainText('Assigning again replaces the old value')
  // Embedded exercises appear as text too.
  await expect(page.locator('body')).toContainText('Update stock')
  // Relative links in the markdown became absolute site paths.
  const next = await page.locator('a', { hasText: 'How a program runs' }).first().getAttribute('href')
  expect(next).toBe(`${new URL(baseURL!).pathname}01-learn-python/01-getting-started/03-how-a-program-runs/`)
})

test('a problem page and the home page are complete without JavaScript', async ({ page, baseURL }) => {
  await page.goto('problem/p-binary-search/')
  await expect(page).toHaveTitle(/^Binary search · /)
  await expect(page.locator('body')).toContainText('Keep two positions')
  await page.goto('')
  await expect(page).toHaveTitle('Learn Python')
  const og = await page.locator('meta[property="og:title"]').getAttribute('content')
  expect(og).toBe('Learn Python')
  expect(await page.locator('link[rel="canonical"]').getAttribute('href')).toBe(baseURL)
})

test('sitemap lists every page once, in path form, and robots points at it', async ({ request, baseURL }) => {
  const xml = await (await request.get('sitemap.xml')).text()
  expect(xml).not.toContain('#')
  const locs = [...xml.matchAll(/<loc>([^<]+)<\/loc>/g)].map((m) => m[1])
  expect(new Set(locs).size).toBe(locs.length)
  expect(locs).toContain(baseURL)
  expect(locs).toContain(`${baseURL}01-learn-python/05-practice/10-hard/`)
  expect(locs).toContain(`${baseURL}problem/p-two-sum-dict/`)
  expect(locs).toContain(`${baseURL}problems/`)
  expect(locs).not.toContain(`${baseURL}settings/`)
  for (const loc of locs) expect(loc.startsWith(baseURL!)).toBe(true)

  const robots = await (await request.get('robots.txt')).text()
  expect(robots).toContain(`Sitemap: ${baseURL}sitemap.xml`)

  // The settings page is served but asks not to be indexed.
  await page_noindex(request, `${baseURL}settings/`)
})

async function page_noindex(request: import('@playwright/test').APIRequestContext, url: string) {
  const html = await (await request.get(url)).text()
  expect(html).toContain('<meta name="robots" content="noindex" />')
}
