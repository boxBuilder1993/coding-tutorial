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
  await page.goto('/#/')
  await expect(page.locator('.sidebar')).toContainText('Learn Python')
  await expect(page.locator('.sidebar')).toContainText('Algorithms')
  await expect(page.locator('.markdown h1')).toHaveText('Learn Python, then algorithms')
  await waitForPython(page)
  await page.screenshot({ path: `${SHOTS}/01-home.png`, fullPage: true })
})

test('play block runs and shows output', async ({ page }) => {
  await page.goto('/#/01-learn-python/01-values')
  await waitForPython(page)
  const first = page.locator('.play').first()
  await first.getByRole('button', { name: 'Run' }).click()
  await expect(first.locator('.output')).toContainText('Hello')
  await expect(first.locator('.output')).toContainText('42')

  // The "2 + 3" block prints nothing: must say so.
  const silent = page.locator('.play').nth(2)
  await silent.getByRole('button', { name: 'Run' }).click()
  await expect(silent.locator('.play-result')).toContainText('no output')

  // An error block: edit the first block to a NameError and run.
  await setEditor(page, first.locator('.editor'), 'print(nme)')
  await first.getByRole('button', { name: 'Run' }).click()
  await expect(first.locator('.error-summary')).toContainText('never defined')
  await page.screenshot({ path: `${SHOTS}/02-lesson-play.png`, fullPage: true })
})

test('exercise: starter fails, hints reveal, correct code passes and persists', async ({ page }) => {
  await page.goto('/#/01-learn-python/01-values')
  await waitForPython(page)
  const card = page.locator('.exercise', { hasText: 'Fahrenheit to Celsius' })
  await card.getByRole('button', { name: 'Run tests' }).click()
  await expect(card.locator('.results-banner')).toContainText('0 of 4 checks passed')
  await expect(card.locator('.case.fail')).toHaveCount(4)

  await card.getByRole('button', { name: /Show hint 1/ }).click()
  await expect(card.locator('.hints ol li')).toHaveCount(1)

  await setEditor(page, card.locator('.editor'), 'def to_celsius(f):\n    return (f - 32) * 5 / 9\n')
  await card.getByRole('button', { name: 'Run tests' }).click()
  await expect(card.locator('.results-banner')).toContainText('All 4 checks passed')
  await expect(card.locator('.status-pill')).toHaveText('Solved with help')
  await page.screenshot({ path: `${SHOTS}/03-exercise-pass.png`, fullPage: true })

  // Progress survives a reload and shows in the sidebar.
  await page.reload()
  await expect(page.locator('.exercise', { hasText: 'Fahrenheit to Celsius' }).locator('.status-pill')).toHaveText('Solved with help')
  await expect(page.locator('.sidebar .nav-row.current .page-status')).toHaveClass(/partial/)
})

test('exercise: missing definition and syntax error are explained', async ({ page }) => {
  await page.goto('/#/problem/two-sum')
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
  await page.goto('/#/problem/greet')
  await waitForPython(page)
  const card = page.locator('.exercise')
  await setEditor(page, card.locator('.editor'), 'def greet(name):\n    while True:\n        pass\n')
  await card.getByRole('button', { name: 'Run tests' }).click()
  await expect(card.getByRole('button', { name: 'Stop' })).toBeVisible()
  await expect(card.locator('.results-banner')).toContainText('more than 10 seconds', { timeout: 30_000 })
  // Pyodide reloads after a kill; it must come back.
  await waitForPython(page)
})

test('linked list helpers work in the browser', async ({ page }) => {
  await page.goto('/#/problem/reverse-linked-list')
  await waitForPython(page)
  const card = page.locator('.exercise')
  await setEditor(
    page,
    card.locator('.editor'),
    'def reverse_list(head):\n    prev = None\n    while head:\n        nxt = head.next\n        head.next = prev\n        prev, head = head, nxt\n    return prev\n',
  )
  await card.getByRole('button', { name: 'Run tests' }).click()
  await expect(card.locator('.results-banner')).toContainText('All 4 checks passed')
  await page.screenshot({ path: `${SHOTS}/05-problem-split.png`, fullPage: true })
})

test('problems list and settings render', async ({ page }) => {
  await page.goto('/#/problems')
  await expect(page.locator('.problems-table tbody tr')).toHaveCount(4)
  await page.goto('/#/settings')
  await expect(page.getByRole('button', { name: 'Export progress' })).toBeVisible()
  await page.screenshot({ path: `${SHOTS}/06-problems.png`, fullPage: true })
})

test.afterAll(() => {
  const real = consoleErrors.filter((e) => !/favicon/.test(e))
  if (real.length) console.log('CONSOLE ERRORS:\n' + real.join('\n'))
})
