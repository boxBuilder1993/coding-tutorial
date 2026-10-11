/**
 * Content sweep: visits every page in the site tree and checks, in the real
 * browser, that
 *   - every runnable code block runs without an error, unless its fence is
 *     tagged `expect-error`, in which case it must error;
 *   - every exercise's reference solution passes its checks;
 *   - every internal link points at a page or problem that exists;
 *   - every problem in the library is embedded on some page;
 *   - the page produces no console errors.
 *
 * Problems are reported with expect.soft so one page's issues do not hide
 * another's. A markdown report is written to ../review/sweep.md.
 */
import { expect, test, type Locator, type Page } from '@playwright/test'
import { mkdirSync, writeFileSync } from 'node:fs'
import { dirname, resolve } from 'node:path'

interface TreeNode {
  path: string
  title: string
  problems: string[]
  children: TreeNode[]
}
interface Problem {
  id: string
  title: string
  reference: string
}

const REPORT = resolve(process.env.SWEEP_REPORT ?? '../review/sweep.md')

function flatten(node: TreeNode, out: TreeNode[] = []): TreeNode[] {
  out.push(node)
  node.children.forEach((c) => flatten(c, out))
  return out
}

function escapeRegExp(s: string): string {
  return s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')
}

async function setEditor(page: Page, editor: Locator, code: string) {
  await editor.locator('.cm-content').click()
  await page.keyboard.press('ControlOrMeta+a')
  await page.keyboard.press('Delete')
  await page.keyboard.insertText(code)
}

test('every page, block, reference and link', async ({ page, baseURL }) => {
  test.setTimeout(20 * 60 * 1000)
  const base = baseURL!.endsWith('/') ? baseURL! : baseURL + '/'

  const tree = (await (await page.request.get(base + 'content/tree.json')).json()) as TreeNode
  const problems = (await (await page.request.get(base + 'content/problems.json')).json()) as Record<string, Problem>
  const pages = flatten(tree)
  const pagePaths = new Set(pages.map((p) => p.path))

  const consoleErrors: string[] = []
  page.on('pageerror', (e) => consoleErrors.push(`pageerror: ${e.message}`))
  page.on('console', (m) => {
    if (m.type() === 'error') consoleErrors.push(m.text())
  })

  const report: string[] = []
  const embedded = new Set<string>()

  await page.goto(base)
  await expect(page.locator('.runner-pill')).toHaveText('Python ready', { timeout: 120_000 })

  for (const node of pages) {
    await test.step(node.path || 'home', async () => {
      const lines: string[] = [`## ${node.title}  (${node.path || 'home'})`]
      await page.goto(base + (node.path ? node.path + '/' : ''))
      await page.waitForSelector('.markdown')
      // Each goto is a full load; wait for the runner again before running blocks.
      await expect(page.locator('.runner-pill')).toHaveText('Python ready', { timeout: 120_000 })

      // Internal links must resolve.
      const basePath = new URL(base).pathname
      const hrefs = await page.locator('.markdown a').evaluateAll((as) => as.map((a) => a.getAttribute('href') ?? ''))
      for (const h of hrefs.filter((h) => h.startsWith(basePath) || h.startsWith('/'))) {
        const target = h.slice(h.startsWith(basePath) ? basePath.length : 1).replace(/\/+$/, '')
        const ok =
          target === '' ||
          pagePaths.has(target) ||
          (target.startsWith('problem/') && target.slice('problem/'.length) in problems) ||
          target === 'problems' ||
          target === 'settings'
        expect.soft(ok, `${node.path || 'home'}: broken link ${h}`).toBe(true)
        if (!ok) lines.push(`- BROKEN LINK: ${h}`)
      }

      // Every runnable block.
      const plays = page.locator('.play')
      const n = await plays.count()
      for (let i = 0; i < n; i++) {
        const block = plays.nth(i)
        const code = (await block.locator('.cm-content').innerText()).split('\n').slice(0, 2).join(' | ')
        const expectError = (await block.getAttribute('data-expect-error')) === 'true'
        await block.getByRole('button', { name: 'Run' }).click()
        await block.locator('.play-result').waitFor({ timeout: 20_000 })
        const errored = (await block.locator('.error-summary').count()) > 0
        const label = `${node.path || 'home'} block ${i + 1} (${code})`
        if (expectError) {
          expect.soft(errored, `${label}: marked expect-error but ran cleanly`).toBe(true)
          if (!errored) lines.push(`- EXPECTED AN ERROR in block ${i + 1} but it ran cleanly: ${code}`)
        } else {
          const summary = errored ? await block.locator('.error-summary').first().innerText() : ''
          expect.soft(errored, `${label}: unexpected error: ${summary}`).toBe(false)
          if (errored) lines.push(`- UNEXPECTED ERROR in block ${i + 1}: ${summary}\n  code: ${code}`)
        }
      }

      // Every exercise: the reference must pass.
      for (const pid of node.problems) {
        embedded.add(pid)
        const pr = problems[pid]
        const card = page.locator('.exercise', { has: page.locator('h3', { hasText: new RegExp('^' + escapeRegExp(pr.title) + '$') }) }).first()
        await setEditor(page, card.locator('.editor'), pr.reference + '\n')
        await card.getByRole('button', { name: 'Run tests' }).click()
        await card.locator('.results-banner').waitFor({ timeout: 30_000 })
        const banner = await card.locator('.results-banner').innerText()
        const passed = /^All \d+ checks passed/.test(banner)
        expect.soft(passed, `${pid}: reference solution fails in the browser: ${banner}`).toBe(true)
        if (!passed) lines.push(`- REFERENCE FAILS for ${pid}: ${banner}`)
      }

      report.push(lines.join('\n'))
      await page.evaluate(() => localStorage.clear())
    })
  }

  const unreferenced = Object.keys(problems).filter((id) => !embedded.has(id))
  expect.soft(unreferenced, 'problems not embedded on any page').toEqual([])
  const uniqueErrors = [...new Set(consoleErrors)]
  expect.soft(uniqueErrors, 'console errors').toEqual([])

  const header = [
    '# Content sweep',
    '',
    `Pages: ${pages.length}. Problems embedded: ${embedded.size} of ${Object.keys(problems).length}.`,
    unreferenced.length ? `Problems not embedded on any page: ${unreferenced.join(', ')}` : 'Every problem is embedded on a page.',
    uniqueErrors.length ? `Console errors:\n${uniqueErrors.map((e) => '- ' + e).join('\n')}` : 'No console errors.',
    'Pages with no findings below passed every check.',
    '',
  ]
  const findings = report.filter((r) => r.includes('\n- '))
  mkdirSync(dirname(REPORT), { recursive: true })
  writeFileSync(REPORT, header.join('\n') + '\n' + (findings.length ? findings.join('\n\n') + '\n' : 'No findings.\n'))
})
