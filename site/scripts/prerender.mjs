/**
 * Pre-render one index.html per page and problem into dist/, plus
 * sitemap.xml, robots.txt and 404.html.
 *
 * Runs after `vite build`. It takes dist/index.html as the template (so the
 * script and style tags match the built assets), and for each URL writes a
 * copy with the page's title, description, canonical and social tags in the
 * head and the page's content rendered to HTML inside #root. The app replaces
 * that content when it loads; search engines and link previews see it as is.
 *
 * Environment:
 *   SITE_URL   absolute origin + base of the deployed site, with trailing
 *              slash, e.g. https://example.github.io/coding-tutorial/
 *              Defaults to http://localhost:4173/ (vite preview) so local
 *              builds produce a usable sitemap.
 */
import { marked } from 'marked'
import { existsSync, mkdirSync, readFileSync, writeFileSync } from 'node:fs'
import { dirname, join } from 'node:path'
import { fileURLToPath } from 'node:url'

const here = dirname(fileURLToPath(import.meta.url))
const site = join(here, '..')
const dist = join(site, 'dist')
const content = join(site, 'public', 'content')

const siteUrl = (process.env.SITE_URL ?? 'http://localhost:4173/').replace(/\/?$/, '/')
const basePath = new URL(siteUrl).pathname // e.g. "/coding-tutorial/"

const template = readFileSync(join(dist, 'index.html'), 'utf8')
const tree = JSON.parse(readFileSync(join(content, 'tree.json'), 'utf8'))
const problems = JSON.parse(readFileSync(join(content, 'problems.json'), 'utf8'))

const SITE_TITLE = tree.title

function flatten(node, out = []) {
  out.push(node)
  node.children.forEach((c) => flatten(c, out))
  return out
}

function escapeHtml(s) {
  return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;')
}

/** First paragraph of markdown as plain text, trimmed to a description length. */
function describe(md) {
  const body = md.replace(/^#\s+[^\n]*\n+/, '')
  const para = body.split(/\n\s*\n/).find((p) => p.trim() && !p.trim().startsWith('```') && !p.trim().startsWith(':::') && !p.trim().startsWith('|') && !p.trim().startsWith('#'))
  const text = (para ?? '')
    .replace(/\[([^\]]+)\]\([^)]*\)/g, '$1')
    .replace(/[`*_]/g, '')
    .replace(/\s+/g, ' ')
    .trim()
  return text.length > 155 ? text.slice(0, 152).replace(/\s+\S*$/, '') + '…' : text
}

/** Rewrite relative markdown links (../02-names, 01-learn-python) to site paths. */
function rewriteLinks(md, pagePath) {
  return md.replace(/\]\(([^)\s]+)\)/g, (m, href) => {
    if (/^[a-z][a-z0-9+.-]*:/i.test(href) || href.startsWith('#') || href.startsWith('/')) {
      if (href.startsWith('problem:')) return `](${basePath}problem/${href.slice('problem:'.length)}/)`
      return m
    }
    const base = 'http://x/' + (pagePath ? pagePath + '/' : '')
    let path
    try {
      path = new URL(href, base).pathname
    } catch {
      return m
    }
    path = path.replace(/\/README\.md$/i, '').replace(/^\/+|\/+$/g, '')
    return `](${path ? basePath + path + '/' : basePath})`
  })
}

/** Markdown for a problem as it should appear when embedded in a page. */
function problemMarkdown(pr) {
  return `${pr.statement.replace(/^#\s+/, '### ')}\n\n\`\`\`python\n${pr.starter}\n\`\`\`\n`
}

function pageMarkdown(node) {
  const file = node.path ? join(content, 'site', node.path, 'README.md') : join(content, 'site', 'README.md')
  let md = readFileSync(file, 'utf8')
  md = md.replace(/^:::problem\s+([a-z0-9][a-z0-9-]*)\s*$/gm, (m, id) => (problems[id] ? problemMarkdown(problems[id]) : ''))
  // Drop fence info beyond the language so renderers do not choke on "python expect-error".
  md = md.replace(/^```python[^\n]*$/gm, '```python')
  return rewriteLinks(md, node.path)
}

function render(md) {
  return marked.parse(md, { gfm: true })
}

function html({ url, title, description, body, noindex = false }) {
  const fullTitle = title === SITE_TITLE ? SITE_TITLE : `${title} · ${SITE_TITLE}`
  const head = [
    `<title>${escapeHtml(fullTitle)}</title>`,
    `<meta name="description" content="${escapeHtml(description)}" />`,
    noindex ? `<meta name="robots" content="noindex" />` : `<link rel="canonical" href="${url}" />`,
    `<meta property="og:type" content="article" />`,
    `<meta property="og:site_name" content="${escapeHtml(SITE_TITLE)}" />`,
    `<meta property="og:title" content="${escapeHtml(fullTitle)}" />`,
    `<meta property="og:description" content="${escapeHtml(description)}" />`,
    `<meta property="og:url" content="${url}" />`,
    `<meta name="twitter:card" content="summary" />`,
  ].join('\n    ')
  return template
    .replace(/<title>[^<]*<\/title>/, head)
    .replace('<div id="root"></div>', `<div id="root"><main class="main"><article class="page"><div class="markdown">${body}</div></article></main></div>`)
}

function writePage(relPath, markup) {
  const dir = join(dist, relPath)
  mkdirSync(dir, { recursive: true })
  writeFileSync(join(dir, 'index.html'), markup)
}

const urls = []

// Site pages.
for (const node of flatten(tree)) {
  const md = pageMarkdown(node)
  const url = node.path ? `${siteUrl}${node.path}/` : siteUrl
  const markup = html({ url, title: node.title, description: describe(md), body: render(md) })
  if (node.path) writePage(node.path, markup)
  else writeFileSync(join(dist, 'index.html'), markup)
  urls.push(url)
}

// Problem pages.
for (const pr of Object.values(problems)) {
  const url = `${siteUrl}problem/${pr.id}/`
  const md = rewriteLinks(`# ${pr.title}\n\n${pr.statement.replace(/^#\s+[^\n]*\n+/, '')}\n\n\`\`\`python\n${pr.starter}\n\`\`\`\n`, '')
  writePage(`problem/${pr.id}`, html({ url, title: pr.title, description: describe(md), body: render(md) }))
  urls.push(url)
}

// Problems index and settings.
{
  const list = Object.values(problems)
    .sort((a, b) => a.title.localeCompare(b.title))
    .map((p) => `- [${p.title}](${basePath}problem/${p.id}/)`)
    .join('\n')
  const md = `# All problems\n\nEvery exercise on the site, in one list.\n\n${list}\n`
  const url = `${siteUrl}problems/`
  writePage('problems', html({ url, title: 'All problems', description: `Every exercise on ${SITE_TITLE}, in one list.`, body: render(md) }))
  urls.push(url)
  writePage('settings', html({ url: `${siteUrl}settings/`, title: 'Settings', description: 'Appearance and progress settings.', body: render('# Settings\n'), noindex: true }))
}

// 404: the app shell with no content, marked noindex.
writeFileSync(join(dist, '404.html'), html({ url: siteUrl, title: 'Page not found', description: 'That page does not exist.', body: render('# Page not found\n\n[Go to the start](' + basePath + ')\n'), noindex: true }))

// Sitemap and robots.
writeFileSync(
  join(dist, 'sitemap.xml'),
  `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${urls.map((u) => `  <url><loc>${u}</loc></url>`).join('\n')}\n</urlset>\n`,
)
writeFileSync(join(dist, 'robots.txt'), `User-agent: *\nAllow: /\nSitemap: ${siteUrl}sitemap.xml\n`)

if (!existsSync(join(dist, 'sitemap.xml'))) throw new Error('sitemap not written')
console.log(`prerendered ${urls.length} pages under ${siteUrl}`)
