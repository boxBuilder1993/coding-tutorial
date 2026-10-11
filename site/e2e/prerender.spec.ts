/**
 * The built site must be readable without JavaScript: every page has its own
 * URL with a real HTML file, a title, a description, a canonical link, and
 * the page text in the body. The sitemap lists each URL exactly once, in
 * path form only. This project runs with JavaScript disabled against
 * `vite preview`, so `npm run build` must have run first.
 *
 * Pages are fetched from `baseURL` (the preview server). Canonical links and
 * the sitemap use the deployed address, `SITE_URL`, when the build was given
 * one; otherwise they equal the preview address.
 */
import { expect, test, type APIRequestContext } from '@playwright/test'

const siteUrl = (process.env.SITE_URL ?? '').replace(/\/?$/, '/')

function expectedSite(baseURL: string | undefined): string {
  return process.env.SITE_URL ? siteUrl : baseURL!
}

test('a lesson page is complete without JavaScript', async ({ page, baseURL }) => {
  const site = expectedSite(baseURL)
  const res = await page.goto('01-learn-python/01-getting-started/02-names/')
  expect(res?.status()).toBe(200)
  // The search-facing title and description come from the page's front block.
  await expect(page).toHaveTitle('Python variables: naming values and updating them · Learn Python')
  const description = await page.locator('meta[name="description"]').getAttribute('content')
  expect(description).toMatch(/^How to give a value a name in Python/)
  // The front block itself never reaches the page.
  await expect(page.locator('body')).not.toContainText('description:')
  // Structured data marks the page as a lesson of the course.
  const ld = JSON.parse((await page.locator('script[type="application/ld+json"]').textContent()) ?? '{}')
  expect(ld['@type']).toBe('LearningResource')
  expect(ld.learningResourceType).toBe('Lesson')
  expect(ld.isPartOf.name).toBe('Learn Python')
  const canonical = await page.locator('link[rel="canonical"]').getAttribute('href')
  expect(canonical).toBe(`${site}01-learn-python/01-getting-started/02-names/`)
  expect(canonical).not.toContain('#')
  // The text is in the HTML itself, not fetched by script.
  await expect(page.locator('h1')).toHaveText('Names')
  await expect(page.locator('body')).toContainText('Assigning again replaces the old value')
  // Embedded exercises appear as text too.
  await expect(page.locator('body')).toContainText('Update stock')
  // Relative links in the markdown became absolute site paths.
  const next = await page.locator('a', { hasText: 'How a program runs' }).first().getAttribute('href')
  expect(next).toBe(`${new URL(site).pathname}01-learn-python/01-getting-started/03-how-a-program-runs/`)
})

test('a problem page and the home page are complete without JavaScript', async ({ page, baseURL }) => {
  const site = expectedSite(baseURL)
  await page.goto('problem/p-binary-search/')
  await expect(page).toHaveTitle(/^Binary search \(Python exercise\) · /)
  await expect(page.locator('body')).toContainText('Keep two positions')
  await page.goto('')
  await expect(page).toHaveTitle('Learn Python')
  const og = await page.locator('meta[property="og:title"]').getAttribute('content')
  expect(og).toBe('Learn Python')
  expect(await page.locator('meta[name="description"]').getAttribute('content')).toMatch(/^Free Python course that runs in your browser/)
  expect(await page.locator('link[rel="canonical"]').getAttribute('href')).toBe(site)
  const ld = JSON.parse((await page.locator('script[type="application/ld+json"]').textContent()) ?? '{}')
  expect(ld['@type']).toBe('Course')
  expect(ld.isAccessibleForFree).toBe(true)
})

test('sitemap lists every page once, in path form, and robots points at it', async ({ request, baseURL }) => {
  const site = expectedSite(baseURL)
  const xml = await (await request.get('sitemap.xml')).text()
  expect(xml).not.toContain('#')
  const locs = [...xml.matchAll(/<loc>([^<]+)<\/loc>/g)].map((m) => m[1])
  expect(new Set(locs).size).toBe(locs.length)
  expect(locs).toContain(site)
  expect(locs).toContain(`${site}01-learn-python/05-practice/10-hard/`)
  expect(locs).toContain(`${site}problem/p-two-sum-dict/`)
  expect(locs).toContain(`${site}problems/`)
  expect(locs).not.toContain(`${site}settings/`)
  for (const loc of locs) expect(loc.startsWith(site)).toBe(true)

  const robots = await (await request.get('robots.txt')).text()
  expect(robots).toContain(`Sitemap: ${site}sitemap.xml`)

  // The settings page is served but asks not to be indexed.
  await expectNoindex(request, 'settings/')
})

async function expectNoindex(request: APIRequestContext, path: string) {
  const html = await (await request.get(path)).text()
  expect(html).toContain('<meta name="robots" content="noindex" />')
}
