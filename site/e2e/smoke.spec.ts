import { expect, test, type Page } from '@playwright/test'

const SHOTS = process.env.E2E_SHOTS ?? 'test-results/shots'

const consoleErrors: string[] = []
test.beforeEach(({ page }) => {
  page.on('console', (m) => {
    if (m.type() === 'error') consoleErrors.push(m.text())
  })
  page.on('pageerror', (e) => consoleErrors.push(`pageerror: ${e.message}`))
})

async function waitForPython(page: Page) {
  await expect(page.locator('.runner-pill')).toHaveText('Python ready', { timeout: 90_000 })
}

async function setEditor(page: Page, editor: ReturnType<Page['locator']>, code: string) {
  await editor.locator('.cm-content').click()
  await page.keyboard.press('ControlOrMeta+a')
  await page.keyboard.press('Delete')
  // insertText avoids CodeMirror auto-indent interfering with typed newlines
  await page.keyboard.insertText(code)
}

test('home loads, sidebar renders, Pyodide becomes ready', async ({ page }) => {
  await page.goto('')
  await expect(page.locator('.sidebar')).toContainText('Learn Python')
  await expect(page.locator('.sidebar')).toContainText('All problems')
  await expect(page.locator('.markdown h1')).toHaveText('Learn Python')
  await waitForPython(page)
  await page.screenshot({ path: `${SHOTS}/01-home.png`, fullPage: true })
})

test('play block runs and shows output', async ({ page }) => {
  await page.goto('learn-python/getting-started/values-and-print/')
  await waitForPython(page)
  const first = page.locator('.play').first()
  await first.getByRole('button', { name: 'Run' }).click()
  await expect(first.locator('.output')).toContainText('Welcome to the shop')
  await expect(first.locator('.output')).toContainText('42')

  // The "2 + 3" block prints nothing: must say so.
  const silent = page.locator('.play').nth(4)
  await silent.getByRole('button', { name: 'Run' }).click()
  await expect(silent.locator('.play-result')).toContainText('no output')

  // An error block: edit the first block to a NameError and run.
  await setEditor(page, first.locator('.editor'), 'print(nme)')
  await first.getByRole('button', { name: 'Run' }).click()
  await expect(first.locator('.error-summary')).toContainText('never defined')
  await page.screenshot({ path: `${SHOTS}/02-lesson-play.png`, fullPage: true })
})

test('exercise: starter fails, hints reveal, correct code passes and persists', async ({ page }) => {
  await page.goto('learn-python/getting-started/functions/')
  await waitForPython(page)
  const card = page.locator('.exercise', { hasText: 'Triple' })
  await card.getByRole('button', { name: 'Run tests' }).click()
  await expect(card.locator('.results-banner')).toContainText('0 of 4 checks passed')
  await expect(card.locator('.case.fail')).toHaveCount(4)

  await card.getByRole('button', { name: /Show hint 1/ }).click()
  await expect(card.locator('.hints ol li')).toHaveCount(1)
  // Opened hints can be hidden and shown again; the count used is kept.
  await card.getByRole('button', { name: 'Hide hints' }).click()
  await expect(card.locator('.hints ol li')).toHaveCount(0)
  await card.getByRole('button', { name: 'Show the hint you opened' }).click()
  await expect(card.locator('.hints ol li')).toHaveCount(1)

  await setEditor(page, card.locator('.editor'), 'def triple(x):\n    return x * 3\n')
  await card.getByRole('button', { name: 'Run tests' }).click()
  await expect(card.locator('.results-banner')).toContainText('All 4 checks passed')
  await expect(card.locator('.status-pill')).toHaveText('Solved with help')
  await page.screenshot({ path: `${SHOTS}/03-exercise-pass.png`, fullPage: true })

  // Progress survives a reload and shows in the sidebar.
  await page.reload()
  await expect(page.locator('.exercise', { hasText: 'Triple' }).locator('.status-pill')).toHaveText('Solved with help')
  await expect(page.locator('.sidebar .nav-row.current .page-status')).toHaveClass(/partial/)
})

test('exercise: missing definition and syntax error are explained', async ({ page }) => {
  await page.goto('problem/p-two-sum-dict/')
  await waitForPython(page)
  const card = page.locator('.exercise')
  await setEditor(page, card.locator('.editor'), 'def two_sun(nums, target):\n    return [0, 1]\n')
  await card.getByRole('button', { name: 'Run tests' }).click()
  await expect(card.locator('.results-banner')).toContainText('must define `two_sum`')

  await setEditor(page, card.locator('.editor'), 'def two_sum(nums, target)\n    return [0, 1]\n')
  await card.getByRole('button', { name: 'Run tests' }).click()
  await expect(card.locator('.error-summary')).toContainText('could not read your code')
  await page.screenshot({ path: `${SHOTS}/04-problem-errors.png`, fullPage: true })
})

test('exercise: infinite loop is stopped by the time budget', async ({ page }) => {
  test.setTimeout(180_000)
  await page.goto('problem/triple/')
  await waitForPython(page)
  const card = page.locator('.exercise')
  await setEditor(page, card.locator('.editor'), 'def triple(x):\n    while True:\n        pass\n')
  await card.getByRole('button', { name: 'Run tests' }).click()
  await expect(card.getByRole('button', { name: 'Stop' })).toBeVisible()
  await expect(card.locator('.results-banner')).toContainText('more than 10 seconds', { timeout: 30_000 })
  // Pyodide reloads after a kill; it must come back.
  await waitForPython(page)
})

test('script-style drill: output is captured and names are inspected', async ({ page }) => {
  await page.goto('problem/update-stock/')
  await waitForPython(page)
  const card = page.locator('.exercise')
  await card.getByRole('button', { name: 'Run tests' }).click()
  await expect(card.locator('.results-banner')).toContainText('0 of 2 checks passed')
  await setEditor(page, card.locator('.editor'), 'stock = 10\nstock -= 3\nprint(stock)\n')
  await card.getByRole('button', { name: 'Run tests' }).click()
  await expect(card.locator('.results-banner')).toContainText('All 2 checks passed')
  // The captured print must not leak into the output panel twice.
  await expect(card.locator('.results .output')).toHaveCount(0)
})

test('typing and running do not scroll the page to the top', async ({ page }) => {
  await page.goto('learn-python/getting-started/functions/')
  await waitForPython(page)
  const card = page.locator('.exercise', { hasText: 'Change due' })
  await card.scrollIntoViewIfNeeded()
  const before = await page.evaluate(() => window.scrollY)
  expect(before).toBeGreaterThan(300)

  await card.locator('.cm-content').click()
  await page.keyboard.type('# note')
  await page.waitForTimeout(600) // past the autosave debounce
  expect(await page.evaluate(() => window.scrollY)).toBeGreaterThan(300)

  await card.getByRole('button', { name: 'Run tests' }).click()
  await expect(card.locator('.results-banner')).toBeVisible()
  expect(await page.evaluate(() => window.scrollY)).toBeGreaterThan(300)
})

test('search finds a lesson by a method name and navigates on Enter', async ({ page }) => {
  await page.goto('')
  const box = page.getByRole('searchbox', { name: 'Search lessons and problems' })
  await box.fill('popleft')
  const first = page.locator('.search-hit').first()
  await expect(first).toContainText('Queues')
  await expect(first).toContainText('lesson')
  await box.press('Enter')
  await expect(page).toHaveURL(/stacks-queues-and-priority-queues\/queues\/$/)
  await expect(page.locator('.markdown h1')).toHaveText('Queues')
  await expect(box).toHaveValue('')

  // "/" focuses the box from the page, and nonsense gives a clear empty state.
  await page.keyboard.press('/')
  await expect(box).toBeFocused()
  await box.fill('zzqxv')
  await expect(page.locator('.search-empty')).toContainText('Nothing matches')
})

test('tutor prompt carries the code and failing checks but never the reference', async ({ page }) => {
  await page.goto('problem/p-two-sum-dict/')
  await waitForPython(page)
  const card = page.locator('.exercise')
  const text = () => card.locator('.tutor-text').inputValue()

  // Before any run: the "not run yet" opening.
  await card.getByRole('button', { name: 'What is this?' }).click()
  expect(await text()).toContain('has not run the checks yet')
  expect(await text()).toContain('strict but kind')

  // A wrong solution: results and the "why is it not working" opening appear.
  await setEditor(page, card.locator('.editor'), 'def two_sum(prices, target):\n    return (0, 1)\n')
  await card.getByRole('button', { name: 'Run tests' }).click()
  await expect(card.locator('.results-banner')).toContainText('checks passed')
  const t = await text()
  expect(t).toContain('return (0, 1)')
  expect(t).toContain('FAIL  no pair')
  expect(t).toContain('why they think their code is not working')
  expect(t).not.toContain('seen = {}')          // the reference solution
  expect(t).not.toContain('target - price in seen')
  expect(t).toContain('=== Hints the student has already seen ===\nnone')

  // Revealed hints are included.
  await card.getByRole('button', { name: /Show hint 1/ }).click()
  expect(await text()).toContain('1. seen = {} mapping price to index')
})

test('dark mode toggles the page and the editor, and persists', async ({ page }) => {
  await page.emulateMedia({ colorScheme: 'light' })
  await page.goto('learn-python/getting-started/values-and-print/')
  await page.waitForSelector('.cm-editor')
  const bg = () => page.evaluate(() => getComputedStyle(document.body).backgroundColor)
  const editorBg = () => page.evaluate(() => getComputedStyle(document.querySelector('.cm-editor')!).backgroundColor)
  const lightBg = await bg()
  const lightEditor = await editorBg()

  await page.getByRole('button', { name: 'Switch to dark mode' }).click()
  await expect(page.locator('html')).toHaveAttribute('data-theme', 'dark')
  expect(await bg()).not.toBe(lightBg)
  expect(await editorBg()).not.toBe(lightEditor)
  await page.screenshot({ path: `${SHOTS}/07-dark.png`, fullPage: false })

  await page.reload()
  await expect(page.locator('html')).toHaveAttribute('data-theme', 'dark')
  await page.getByRole('button', { name: 'Switch to light mode' }).click()
  await expect(page.locator('html')).toHaveAttribute('data-theme', 'light')
})

test('path routing: in-app links push real URLs and old hash links redirect', async ({ page, baseURL }) => {
  await page.goto('')
  // Clicking a sidebar link changes the address without a full reload.
  await page.evaluate(() => ((window as unknown as { __alive: boolean }).__alive = true))
  await page.locator('.sidebar a', { hasText: 'Learn Python' }).first().click()
  await expect(page).toHaveURL(`${baseURL}learn-python/`)
  await expect(page.locator('.markdown h1')).toHaveText('Learn Python')
  expect(await page.evaluate(() => (window as unknown as { __alive?: boolean }).__alive)).toBe(true)
  // Back button works.
  await page.goBack()
  await expect(page).toHaveURL(baseURL!)
  // A legacy hash URL lands on the path form.
  await page.goto('#/01-learn-python/01-getting-started/02-names')
  await expect(page).toHaveURL(`${baseURL}learn-python/getting-started/names/`)
  await expect(page.locator('.markdown h1')).toHaveText('Names')
  // A path that still carries the numeric ordering prefixes also lands on the clean form.
  await page.goto('01-learn-python/01-getting-started/02-names/')
  await expect(page).toHaveURL(`${baseURL}learn-python/getting-started/names/`)
})

test('problems list and settings render', async ({ page }) => {
  await page.goto('problems/')
  await expect(page.locator('.problems-table tbody tr')).toHaveCount(178)
  await page.goto('settings/')
  await expect(page.getByRole('button', { name: 'Export progress' })).toBeVisible()
  await page.screenshot({ path: `${SHOTS}/06-problems.png`, fullPage: true })
})

test.afterAll(() => {
  const real = consoleErrors.filter((e) => !/favicon/.test(e))
  if (real.length) console.log('CONSOLE ERRORS:\n' + real.join('\n'))
})
